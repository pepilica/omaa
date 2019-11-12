import math
import PIL
from PIL import ImageDraw, Image


class MyImageDraw(PIL.ImageDraw.ImageDraw):
    def regular_polygon(self, center_coords, sides, radius, rotation=0, fill=None, outline=None):
        self.ellipse([(center_coords[0] - radius, center_coords[0] - radius),
                     (center_coords[0] + radius, center_coords[1] + radius)], outline=outline)
        coords = [(center_coords[0] + radius * math.cos((2 * math.pi * i / sides
                                                              + rotation + (-3 * math.pi / 2))),
                   center_coords[1] + radius * math.sin(2 * math.pi * i / sides
                                                     + rotation + (-3 * math.pi / 2)))
                  for i in range(1, sides + 1)]
        self.polygon(coords, fill=fill, outline=outline)