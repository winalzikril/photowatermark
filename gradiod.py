import gradio as gr
from PIL import Image, ImageDraw
import io

# Function to add a watermark image to another image at the top-left corner
def add_watermark(input_image, watermark_image, watermark_transparency=0.5):
    base_image = Image.open(io.BytesIO(input_image.read()))
    watermark = Image.open(io.BytesIO(watermark_image.read()))

    # Make sure both images have RGBA mode to support transparency
    if base_image.mode != "RGBA":
        base_image = base_image.convert("RGBA")
    if watermark.mode != "RGBA":
        watermark = watermark.convert("RGBA")

    # Calculate the position for the watermark in the top-left corner
    x = 0  # Adjust this value to control the horizontal position
    y = 0  # Adjust this value to control the vertical position

    # Resize the watermark to a smaller size (e.g., 100x100 pixels)
    watermark_width = 100
    watermark_height = 100
    watermark = watermark.resize((watermark_width, watermark_height), Image.ANTIALIAS)

    # Adjust the watermark transparency (alpha)
    alpha = int(255 * watermark_transparency)

    # Paste the watermark onto the base image with the specified alpha value
    watermark = watermark.convert("RGBA")
    watermark_with_transparency = Image.new("RGBA", watermark.size)
    for x_pixel in range(watermark.width):
        for y_pixel in range(watermark.height):
            r, g, b, a = watermark.getpixel((x_pixel, y_pixel))
            watermark_with_transparency.putpixel((x_pixel, y_pixel), (r, g, b, alpha))

    base_image.paste(watermark_with_transparency, (x, y), watermark_with_transparency)

    # Save the watermarked image
    output_image = io.BytesIO()
    base_image.save(output_image, "PNG")
    return output_image.getvalue()

iface = gr.Interface(
    fn=add_watermark,
    inputs=[
        gr.inputs.File(label="Input Image"),
        gr.inputs.File(label="Watermark Image"),
        gr.inputs.Slider(label="Watermark Transparency", default=0.5, minimum=0, maximum=1, step=0.01),
    ],
    outputs=gr.outputs.Image(label="Watermarked Image"),
    title="Image Watermarking",
    description="Add a watermark to your image.",
    live=True,
)

iface.launch()
