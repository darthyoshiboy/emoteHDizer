# emoteHDizer
This is a Python 3.7+ script to make make HD versions of a Twitch Streamer's emotes

main.py
================================================================================
This is the script that you run to generate your "HD" emote set. It depends on values in the config.py being set properly to run. It uses the following libs:

- **Image Slicer**: https://pypi.org/project/image_slicer/
- **Requests**: https://pypi.org/project/requests/
- **Pillow**: https://pypi.org/project/Pillow/
- **Color Thief**: https://pypi.org/project/colorthief/
- **Pathlib**: Included in Python 3.4+ (I'm thinking this code will not work below 3.7, but if you want to try you're going to need pathlib. The _config.py_ file also uses this, so it really has to be there.)


config.py
================================================================================
This is the file that sets things up for success. You need to specify the following values for main.py to get things done:

- **t_streamer** - This is a Twitch streamer username, it's set to Backgroundguy02 by default because he's awesome and you should follow him. The streamer specified has to have emotes. The script won't work if the streamer doesn't have emotes. The script doesn't check for emotes and it will just implode if they're not there.
- **api_client_id** - This is a Twitch API Client ID. It's filled with garbage text by default. https://dev.twitch.tv/docs/v5/#getting-a-client-id explains how to get a client ID. https://dev.twitch.tv/console/apps/create is where the work is actually done. Create an application (Set the "OAuth Redirect URL" to http://localhost) and get the Client ID for that application to insert as the value here.
- **color_pick_quality** - This is set to 1 by default. Lower values tend to be more accurate, but higher values might generate "HD" emotes that are more pleasing to the eye?
- **pixel_count** - This is set to 4 by default for the most HD HD images that can be generated. This needs to be 4, 16, or 64. It will accept any numerical value and the results of it attempting to round things out to the correct values can be interesting, but will not be perfect like the prescribed values.

The following can be changed if you'd like, but probably shouldn't unless you know what you're doing.

- **homedir_picpath** - This is set to "Pictures" by default and that's going to be perfect for most OSes that put a user's images in $HOME/Pictures. Each streamer you run the script on will create a new directory under that directory with the "HD" Emote set inside once the script has run and a working directory that shows the originals with the working pieces once things are all done.
