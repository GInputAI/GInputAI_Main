import math

def math_grad(x = 0, y = 0, side_fov_y = 90):
    side_fov_x = math.degrees(math.atan(math.tan(math.radians(side_fov_y/2)) * 1920/1080))
    side_fov_y = side_fov_y / 2
    tg_x = math.tan(math.radians(side_fov_x))
    tg_y = math.tan(math.radians(side_fov_y))
    x, y = x - 960, y - 540
    px, py = 1, 1
    if x < 0:
        x = -x
        px = -1
    if y < 0:
        y = -y
        py = -1
    #gx
    tg_x = x / (960 / tg_x)
    #gy
    tg_y = y / (540 / tg_y)


    return px * math.degrees(math.atan(tg_x)), py * math.degrees(math.atan(tg_y))

print(math_grad(0,0))