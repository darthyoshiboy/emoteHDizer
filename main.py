import image_slicer, requests, os, config
from pathlib import Path
from colorthief import ColorThief
from PIL import Image, ImageDraw

url = f"https://api.twitch.tv/api/channels/{config.t_streamer}/product?client_id={config.api_client_id}"

streamer_product = requests.get(url)
sjp = streamer_product.json()
cwd = config.working_directory
cwtd = config.working_directory.joinpath("working")
if not os.path.exists(cwd):
    os.mkdir(cwd)
if not os.path.exists(cwtd):
    os.mkdir(cwtd)
print(f"HDizing emotes for: {config.t_streamer}")

for image in sjp['emoticons']:
    img_url = f"https://static-cdn.jtvnw.net/emoticons/v1/{image['id']}/3.0"
    c_emote_filename = f"{image['regex']}.png"
    c_emote_wpath = Path.joinpath(cwtd).joinpath(c_emote_filename)
    print(f"Downloading: {image['regex']}:{img_url} Image saved to: {c_emote_wpath}")
    c_emote = requests.get(img_url)
    open(c_emote_wpath, 'wb').write(c_emote.content)
    e_tiles = image_slicer.slice(c_emote_wpath, config.pixel_count)
    for tile in e_tiles:
        pixel = ColorThief(tile.filename)
        try:
            fill_color = pixel.get_color(quality=config.color_pick_quality)
        except:
            fill_color = (255,255,255)
        tile_temp = cwd.joinpath(tile.filename)
        tile_image = Image.open(tile.filename)
        pil_image = Image.new("RGB", (tile_image.size[0],tile_image.size[1]), color=fill_color)
        tile.image = pil_image
    hd_image = image_slicer.join(e_tiles)
    for size in (28,56,112):
        save_image = hd_image.resize((size,size))
        c_emote_fpath = Path.joinpath(cwd).joinpath(f"{image['regex']}_hd_{size}.png")
        print(f"Saved 'HD' emote to {c_emote_fpath}")
        save_image.save(c_emote_fpath, "PNG")
