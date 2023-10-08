from PIL import Image, ImageDraw, ImageFont
import os

# Function to add a watermark to an image
def add_watermark(input_image_path, output_image_path, watermark_text):
    photo = Image.open(input_image_path)

    # Make sure the photo is in RGBA mode to support transparency
    if photo.mode != "RGBA":
        photo = photo.convert("RGBA")

    # Create a drawing context
    draw = ImageDraw.Draw(photo)

    try:
        font = ImageFont.truetype("arial.ttf", 200)
    except IOError:
        font = ImageFont.load_default()

    # Calculate text size
    textwidth, textheight = draw.textsize(watermark_text, font)

    # Calculate the x, y coordinates of the watermark text
    x = photo.width - textwidth - 10
    y = photo.height - textheight - 10

    # Draw the watermark text
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

    # Save the watermarked image
    photo.save(output_image_path, "PNG")

# Function to process a batch of photos
def add_watermark_to_batch(input_folder, output_folder, watermark_text):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    for file in files:
        if file.endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)
            add_watermark(input_path, output_path, watermark_text)

if __name__ == "__main__":
    input_folder = "input_photos"
    output_folder = "output_photos"
    watermark_text = "WINAL ZIKRIL"

    add_watermark_to_batch(input_folder, output_folder, watermark_text)
