from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.utils import Utils
import time, asyncio


class Controller():
    @classmethod
    async def start_controller(self, video_data):
        # log controller start
        Utils.draw_log(status=True,
                       datetime=Utils.get_current_datetime(),
                       message='Initializing controllers')

        # Driver options
        options = Options()
        options.add_argument('--log-level=3')
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')
        PROXY = "http://api.scraperapi.com?api_key=26ba274254599620ff7aa0f676f09bd1&render=true&url="
        options.add_argument(
            '--proxy-server=%s' %
            PROXY
        )
        options.add_argument('--headless')
        options.add_argument('--mute-audio')

        driver = webdriver.Chrome(chrome_options=options,
                                  executable_path=r'./driver/chromedriver')

        # video data
        video_url = video_data['url']
        views = video_data['views']

        # watching loop
        for view in range(0, views):
            # load video url in chrome driver
            driver.get(video_url)

            # Play video
            driver.execute_script(
                "return document.getElementById('movie_player')").click()

            # variable for check if video is playing
            video_is_playing = True

            ads = driver.execute_script(
                "return document.getElementsByClassName('ytp-ad-skip-button-text')[0]"
            )
            if ads is not None:
               # print(ads)
                time.sleep(6)
                ads.click()
                ads = "Skip Ads"

            # minimize window
            driver.minimize_window()

            # log watching current video
            Utils.draw_log(
                status=True,
                datetime=Utils.get_current_datetime(),
                message='Watch video: {}, Views: {}/{} ads: {}'.format(
                    video_url, view + 1, views, ads))

            while video_is_playing:
                # get video status, 1 = running, 2 = stopped
                player_status = driver.execute_script(
                    "return document.getElementById('movie_player').getPlayerState()"
                )

                # get current url from driver
                current_url = driver.current_url

                # check current url for prevent an bug when driver jump in another video in some playlist (force correctly url)
                if current_url != video_url.replace(
                        '?autoplay=1', ''):  # fix removing autoplay from url
                    driver.get(video_url)
                    Utils.draw_log(
                        status=False,
                        datetime=Utils.get_current_datetime(),
                        message=
                        'Changing to correctly url, from: {}, to: {} ads: {}'.
                        format(current_url, video_url, ads))

                # check video is running
                if player_status == 1:
                    await asyncio.sleep(1)
                # video is stopped
                elif player_status == 0:
                    video_is_playing = False
                    break

        # close current driver
        driver.close()
