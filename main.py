from PIL import Image, ImageDraw, ImageFont
import os

name_list = ["Rajdeep Bisai", "Swarnendu Bhandari", "Mayukh Mandal"]

# Path to your certificate template and font file
certificate_template_path = "cert.png"
font_path = "fonts\BRUSHSCI.TTF"

# Output directory for saving certificates
output_directory = "certificates"
# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

for name in name_list:
    try:
        # Open the certificate template
        im = Image.open(certificate_template_path).convert("RGB")
        d = ImageDraw.Draw(im)

        # Set location, text color, and font size
        location = (620 + 25*(19 - len(name)), 590)
        text_color = (0, 0, 0)
        font_size = 100

        # Load font
        font = ImageFont.truetype(font_path, font_size)

        # Write name on the certificate
        d.text(location, name, fill=text_color, font=font)

        # Save the certificate as PDF
        certificate_filename = f"certificate_{name}.pdf"
        certificate_filepath = os.path.join(
            output_directory, certificate_filename)
        im.save(certificate_filepath)
        print(f"Certificate saved for {name}")
    except Exception as e:
        print(f"Error occurred for {name}: {e}")
