### ========== 0xT-BOT ========== ###

> A simple Python Youtube Wachtime for [YTbebot](https://github.com/leandrovieiraa/ytubebot)

# YT-Viewer - Youtube Bot
 [![PayPal](https://user-images.githubusercontent.com/6497827/53698092-42032280-3dfe-11e9-8054-1597c62d344e.png)](https://paypal.me/0xT001)
 
Simple bot that was development in python 3.7, that automatically watch youtube videos. It can be used to give more views in your channel helping in the spread and increase followers/subscribers because your videos begin to gain new positions in research mechanics.

## Concept proof

### Overview
The search time was seven days, but the script was run in only two days (48h).
![Overview](https://image.prntscr.com/image/oDbzCOL7Q2mQY_uq6ebmZw.png)

### Reach
![Reach](https://image.prntscr.com/image/AMrVxRlrRvq93grZDPcRnw.png)

## Description
- The script reads the "./config/playlist.json" file, multiplies the instance for each video by the configured value, and starts the chromedriver. - The mechanic has a system that identifies that the video is running, at the end it will be loaded again generating a view.

```json
[
     {
          "url": "https://www.youtube.com/...",
          "views": 50
     },
     {
          "url": "https://www.youtube.com/...",
          "views": 50
     }
]
```

- If the video modifies the URL for some reason the script identifies and corrects this problem.

- The script uses "selenium" to watch the videos, passing some settings that improve performance and do not interrupt the use of the computer.

- The script was developed using "asyncio" so you need python 3.7, so we can perform asynchronous functions.

- Inside script file "./app.py", you will configure how many async instances to launch, ie: instances = 1

- The instance multiplies the drivers to watch the videos, ie, will instantiate for each video the configured value.

## Running script

```python
pip install -r requirements.txt
python app.py
```

## Observations
- The script can be improved and modified, so feel free to use it any way you like.

- I will not be responsible for any problems related to youtube, because it is a project focused only for studies, keep this in mind.

- The script did not generate revenue in two days because the channel tested does not exceed 300 subscribers, it might help on this issue on channels with more than 1k of subscribers (maybe?).

- I hope it helps someone, and can help in studies aimed at webcrawler + selenium.

- Put "?autoplay=1" in end of video link and use absolute link, final link will be like: https://www.youtube.com/watch?v=xxxxxxxxxxx?autoplay=1

• **Ubuntu server - Install chromedriver**

>```sudo apt-get install chromium-chromedriver```

• **Patch**

>```/usr/lib/chromium-browser/chromedriver```


## Donation
[![Support via PayPal](https://camo.githubusercontent.com/19fc947af2adcacd24b6cdbd4a33c10d7cbaeb6c/68747470733a2f2f63646e2e7261776769742e636f6d2f74776f6c66736f6e2f70617970616c2d6769746875622d627574746f6e2f312e302e302f646973742f627574746f6e2e737667)](https://paypal.me/0xT001)

### =========== Finish =========== ###


