from pathlib import Path

########################### Change only these lines ###########################

# Put a Twitch Streamer name for a channel whose emotes you want to HDize here
t_streamer="backgroundguy02"

# https://dev.twitch.tv/docs/v5/#getting-a-client-id explains how to get this
api_client_id="ReplaceThisWithARealClientID"

# 1 is the highest quality, larger numbers are less precise with attempting to
# determine the dominant color of a quadrant.
color_pick_quality=1

# 4 will generate VERY HD imsges, 16 is Medium, 64, is VERY NOT HD kappa
# !!! Values other than the above will have weird results !!!
pixel_count=4

###############################################################################

################ These can be changed if you're feeling lucky #################

homedir_picpath="Pictures"

###############################################################################

working_directory=Path.home().joinpath(homedir_picpath).joinpath(f"HD_{t_streamer}")
