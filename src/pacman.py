import arcade
import numpy as np
from map_init import tiles
from os.path import isfile


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.tiles = np.array(tiles)
        self.tiles = np.flip(self.tiles, axis=1)
        (self.w, self.h) = np.shape(self.tiles)
        self.tile_size = width // self.w

        #self.pressed = False

    def to_field(self, v):
        return v // self.tile_size

    def rect_center(self, v):
        return self.tile_size * v  + self.tile_size / 2

    def draw_obstacle(self, x, y):
        y = self.rect_center(y)
        x = self.rect_center(x)
        arcade.draw_rectangle_filled(x, y, self.tile_size, self.tile_size, arcade.color.BLUE)

    def draw_tiles(self):
        for y in range(self.h):
            for x in range(self.w):
                if self.tiles[x, y]:
                    self.draw_obstacle(x, y)

    def on_draw(self):
        arcade.start_render()
        self.draw_tiles()

    def set_tile(self, x, y, val):
        if (0 <= x) and (x < self.w) and (0 <= y) and (y < self.h):
            self.tiles[x, y] = val

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int):
        y = self.to_field(y)
        x = self.to_field(x)
        self.set_tile(x, y, buttons == 1)

    def on_mouse_press(self, x, y, button, modifiers):
        y = self.to_field(y)
        x = self.to_field(x)
        self.set_tile(x, y, button == 1)

    def on_mouse_release(self, x, y, button, modifiers):
        pass


def main():
    global tiles

    file = 'tiles.npy'
    if (isfile(file)):
        tiles = np.load(file)
    game = MyGame(800, 800, 'Anime Pacman')
    arcade.run()
    np.save(file, game.tiles)


if __name__ == "__main__":
    main()