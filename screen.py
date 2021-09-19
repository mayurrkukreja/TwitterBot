from PIL import Image, ImageFont, ImageDraw
import textwrap
def get_image(quote):

    image = Image.new('RGB', (800, 500), color=(0,0,0))
    font = ImageFont.truetype("Arial.ttf", 40)
    text_color = (200, 200, 200)
    text_start_height = 100
    write_text_on_image(image, quote, font, text_color, text_start_height)
    image.save('created_image.png')


def write_text_on_image(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=50)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text),line, font=font, fill=text_color)
        y_text += line_height
