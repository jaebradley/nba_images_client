import tempfile
import uuid

from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg
from willow.image import Image

from nba_images_client.models import FileType, ImageDimensions


def convert_from_svg_to_png(data):
    # apparently, you need to name these files for the conversion to work
    with tempfile.NamedTemporaryFile(prefix=uuid.uuid4().hex, suffix='.svg') as svg_file:
        # write data to temporary svg file
        svg_file.write(data)
        svg_file.seek(0)
        with tempfile.NamedTemporaryFile(prefix=uuid.uuid4().hex, suffix='.png') as png_file:
            # draw png from svg file
            renderPM.drawToFile(svg2rlg(svg_file.name), png_file.name, fmt='PNG')
            png_file.seek(0)
            return png_file.read()


def resize_image(png_data, file_type=FileType.PNG, image_dimensions=ImageDimensions(100, 100)):
    with tempfile.NamedTemporaryFile(prefix=uuid.uuid4().hex, suffix='.png') as png_file:
        png_file.write(png_data)
        png_file.seek(0)
        image = Image.open(png_file)
        image = image.resize((image_dimensions.length, image_dimensions.height))
        with tempfile.NamedTemporaryFile(prefix=uuid.uuid4().hex, suffix=FileType.get_extension(file_type)) as resized_file:
            if file_type == FileType.PNG:
                image.save_as_png(resized_file)
            elif file_type == FileType.JPG:
                image.save_as_jpeg(f=resized_file, quality=100)
            else:
                raise RuntimeError('Unknown file type: {file_type}'.format(file_type=file_type))

            resized_file.seek(0)
            return resized_file.read()

