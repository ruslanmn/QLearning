import numpy as np

def action_to_field(action, w):
    y = action // w
    x = action % w
    return x, y


def field_to_action(x, y, w):
    return y * w + x


# return free fields by flatten index from [0, 1, 2, ..., w*h-1]
def get_available_acts(model):
    t = np.array([model.w, 1])
    a = np.argwhere(model.fields == 0)
    return a.dot(t)
