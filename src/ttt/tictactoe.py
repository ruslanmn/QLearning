import arcade
from ttt.tictactoe_model import TicTacToeModel


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.model = TicTacToeModel(3, 3, 3)
        self.field_size_x = width // self.model.w
        self.field_size_y = height // self.model.h


    def draw_background(self):
        for i in range(1, self.model.w):
            x = i * self.field_size_x
            arcade.draw_line(x, 0, x, self.height, arcade.color.BLUE)
        for i in range(1, self.model.h):
            y = i * self.field_size_y
            arcade.draw_line(0, y, self.width, y, arcade.color.BLUE)

    def draw_fields(self):
        for x in range(self.model.w):
            for y in range(self.model.h):
                val = self.model.fields[y, x]
                if val == 1:
                    self.draw_cross(x, y)
                elif val == 2:
                    self.draw_nought(x, y)

    def get_field_coords(self, x, y):
        x = x // self.field_size_x
        y = (self.height - y) // self.field_size_y
        return (x, y)

    def get_left_up_corner(self, x, y):
        x = x * self.field_size_x
        y = (self.model.h - y) * self.field_size_y
        return (x, y)

    def draw_cross(self, x, y):
        (x, y) = self.get_left_up_corner(x, y)
        arcade.draw_line(x, y, x + self.field_size_x, y - self.field_size_y, arcade.color.BLUE)
        arcade.draw_line(x, y - self.field_size_y, x + self.field_size_x, y, arcade.color.BLUE)

    def draw_nought(self, x, y):
        (x, y) = self.get_left_up_corner(x, y)
        arcade.draw_ellipse_outline(x + self.field_size_x / 2, y - self.field_size_y / 2,
                                    self.field_size_x, self.field_size_y,
                                    arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()
        self.draw_background()
        self.draw_fields()

    def on_mouse_release(self, x, y, button, modifiers):
        (x, y) = self.get_field_coords(x, y)
        if self.model.act(x, y):
            self.model.reset()


def main():
    game = MyGame(800, 800, 'Anime Tictactoe')
    arcade.run()

if __name__ == "__main__":
    main()
