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
        self.colors = random.choice(COLORS)

    def on_update(self):
        self.centre_x += self.change_x
        self.centre_y += self.change_y
        if self.centre_x < self.longueur:
            self.change_x *= -1

        elif self.centre_x > SCREEN_WIDTH - self.longueur:
            self.change_x *= -1

        elif self.centre_y < self.largeur:
            self.change_y *= -1

        elif self.centre_y > SCREEN_HEIGHT - self.largeur:
            self.change_y *= -1

    def setup(self):
        pass

    def on_draw(self):
        arcade.draw_rectangle_filled(self.centre_x, self.centre_y, self.longueur, self.largeur, self.colors, self.tilt_angle)




class cercle:
    def __init__(self, x, y):
        self.rayon = 15
        self.change_x = 7
        self.change_y = 7
        self.centre_x = x
        self.centre_y = y
        self.colors = random.choice(COLORS)

    def on_update(self):
        self.centre_x += self.change_x
        self.centre_y += self.change_y
        if self.centre_x < self.rayon:
            self.change_x *= -1

        elif self.centre_x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1

        elif self.centre_y < self.rayon:
            self.change_y *= -1

        elif self.centre_y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1

    def setup(self):
        pass
    def on_draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.colors)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.list_rectangle = []
        self.list_cercle = []

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.list_cercle.append(cercle(x,y))
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.list_rectangle.append(rectangle(x, y))
    def setup(self):
        pass
    def on_update(self, delta_time: float):
        for cercle in self.list_cercle:
            cercle.on_update()

        for rectangle in self.list_rectangle:
            rectangle.on_update()

    def on_draw(self):
        arcade.start_render()
        for cercle in self.list_cercle:
            cercle.on_draw()

        for rectangle in self.list_rectangle:
            rectangle.on_draw()



def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
