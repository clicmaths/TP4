import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.csscolor.BEIGE, arcade.csscolor.RED, arcade.csscolor.TAN, arcade.csscolor.BLUE, arcade.csscolor.CORAL, arcade.csscolor.DARK_OLIVE_GREEN, arcade.csscolor.GOLD, arcade.csscolor.GREEN]

class rectangle:
    def __init__(self, x, y):
        self.longueur = 21
        self.largeur = 10
        self.change_x = 7
        self.change_y = 7
        self.centre_x = x
        self.centre_y = y
        self.tilt_angle = 90
        self.colors = COLORS


class cercle:
    def __init__(self, x, y):
        self.rayon = 15
        self.change_x = 7
        self.change_y = 7
        self.centre_x = x
        self.centre_y = y
        self.colors = COLORS

        def on_update(self):
            if self.centre_x < self.rayon:
                self.change_x *= -1

            if self.centre_x > SCREEN_WIDTH - self.rayon:
                pass
            if self.centre_y < self.rayon:
                pass
            if self.centre_y > SCREEN_HEIGHT - self.rayon:
                self.change_y *= -1

        def setup(self):
            pass
        def on_draw(self):
            pass


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        pass

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

        pass


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
