def calc_z_position(distance) -> int:
    if distance > 100:
        return 130
    if distance < 30:
        return 0

    d = int((distance - 30) / 70 * 130)

    return d

def calc_y_position(y: int) -> int:
    if y > 450:
        return 0
    if y < 20:
        return 100

    d = int((1 - ((y - 20) / 450)) * 100)

    return d

def calc_x_position(x: int) -> int:
    if x > 550:
        return 45
    if x < 20:
        return 0

    d = int(((x - 20) / 550) * 45)

    return d