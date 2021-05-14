# **Not Maintained Anymore. Do checkout https://github.com/TheYoBots/Lishogi-Bot or https://github.com/The-bot-makers/Lishogi-Bot which maintained.**

# The Bot Playing Shogi

The code template to make a Lishogi Bot and deploy it to heroku server easily.

This is the code of [@TheB0t-PlAyInG-sH0gI](https://lishogi.org/@/TheB0t-PlAyInG-sH0gI) in [lishogi.org](https://lishogi.org)

Engine communication code taken from https://github.com/TheYoBots/Lishogi-Bot by [TheYoBots](https://github.com/TheYoBots)

### Shogi Engine

- Fairy Stockfish 11.2 POPCNT

### Heroku Buildpack

- heroku/python

### Heroku Stack

- heroku-20 (allowing a maximum hash size of 512 mb)

### How to Use

- Fork this repository.
- Edit only your token in the config.yml file over [here](https://github.com/abhijato/Thebotplayingshogi/blob/97202c46c5687afc76a87c4aa4176a4341f7447b/config.yml#L1).
- Create a new heroku app.
- Go to the 'Deploy' tab and click 'Connect to GitHub'.
- Click on 'search' and then select your fork of this repository.
- Then 'Enable Automatic Deploys' and then select the 'master' branch (which is already done by default) and Click 'Deploy'.
- Once it has been deployed, go to 'Resources' tab on heroku and enable 'worker' (bash startbot.sh) dynos. (do note that if you don't see any dynos in the 'Resources' tab, then you must refresh your heroku page.)
- You're now connected to lishogi and awaiting challenges! Your bot is up and ready!

