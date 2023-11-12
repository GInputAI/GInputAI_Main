import math

#Geometry
def math_grad(x = 0, y = 0, wigth = 1920, height = 1080, side_fov_y = 90):
    side_fov_x = math.degrees(math.atan(math.tan(math.radians(side_fov_y/2)) * 1920/1080))
    side_fov_y = side_fov_y / 2
    tg_x = math.tan(math.radians(side_fov_x))
    tg_y = math.tan(math.radians(side_fov_y))
    x, y = x - (wigth/2), y - (height/2)
    px, py = 1, 1
    if x < 0:
        x = -x
        px = -1
    if y < 0:
        y = -y
        py = -1

    tg_x = x / (960 / tg_x)
    tg_y = y / (540 / tg_y)


    return px * math.degrees(math.atan(tg_x)), py * math.degrees(math.atan(tg_y))

def grad_calc(xg, yg, width = 1920, hight = 1080, pxtograd = 0.15):
    return (width/2) + (xg / pxtograd) // 1, (hight/2) + (yg / pxtograd) // 1
#pxtograd - сколько градусов в движении на один пиксель (на каждую сенсу, чувствительность и игру своё значение)
#Для майнкрафта допустим с сенсой 800dpi (вроде) и 100% чувств. движение на пиксель = 0.15 град.