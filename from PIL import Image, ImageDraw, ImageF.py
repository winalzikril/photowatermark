from PIL import Image, ImageDraw
import os

# Function to add a watermark image to another image at the top-left corner
def add_watermark(input_image_path, output_image_path, watermark_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)

    # Make sure both images have RGBA mode to support transparency
    if base_image.mode != "RGBA":
        base_image = base_image.convert("RGBA")
    if watermark.mode != "RGBA":
        watermark = watermark.convert("RGBA")

    # Calculate the position for the watermark in the top-left corner
    x = 0  # Adjust this value to control the horizontal position
    y = 0  # Adjust this value to control the vertical position

    # Resize the watermark to a smaller size (e.g., 100x100 pixels)
    watermark_width = 300
    watermark_height = 300
    watermark = watermark.resize((watermark_width, watermark_height), Image.ANTIALIAS)

    # Adjust the watermark transparency (alpha)
    alpha = 128  # Adjust the alpha value (0-255) to control transparency

    # Paste the watermark onto the base image
    base_image.paste(watermark, (x, y), watermark)

    # Save the watermarked image
    base_image.save(output_image_path, "PNG")

# Function to process a batch of photos
def add_watermark_to_batch(input_folder, output_folder, watermark_image_path):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    for file in files:
        if file.endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)
            add_watermark(input_path, output_path, watermark_image_path)

if __name__ == "__main__":
    input_folder = "input_photos"
    output_folder = "output_photos"
    watermark_image_path = "watermark.png"  # Replace with the path to your watermark image

    add_watermark_to_batch(input_folder, output_folder, watermark_image_path)
