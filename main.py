import numpy as np
from wand.color import Color
from wand.drawing import Drawing
from wand.display import display
from wand.image import Image

length = 300
point1 = (0, 0)
point2 = (length, 0)
point3 = (length / 2, length * 3 ** 0.5 / 2)

colors = {
    Color('RED'): point1,
    Color('GREEN1'): point2,
    Color('BLUE'): point3
}

black = np.zeros([500, 500, 3], dtype=np.uint8)

with Image.from_array(black) as image:
    with image.clone() as mask:
        with Drawing() as draw:
            points = [point1, point2, point3]
            draw.fill_color = Color('white')
            draw.polygon(points)
            draw.draw(mask)
            image.sparse_color('barycentric', colors)
            image.composite_channel('all_channels', mask, 'multiply', 0, 0)
            image.format = 'png'
            image.save(filename='result.png')
            display(image)
