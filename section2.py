def get_pixel_color(c):
    r = (c & 0x00FF0000) >> 16
    g = (c & 0x0000FF00) >> 16
    b = (c & 0x000000FF) >> 16
    return r, g, b
