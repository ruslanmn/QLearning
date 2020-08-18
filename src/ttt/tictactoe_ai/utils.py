def action_to_field(action, w):
    y = action / w
    x = action % w
    return x, y

def field_to_action(x, y, w):
    return y * w + x
