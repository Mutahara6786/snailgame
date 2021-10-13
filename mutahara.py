import arcade
import random
import os

class Welcome(arcade.View):
    """Main welcome window
    """
    def __init__(self):
        super().__init__()
        self.grid = [[1,0,0,0,0,0,0,1,1,1],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [20,0,0,0,0,0,0,0,0,0],
                    [10,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [2,2,2,2,0,0,0,0,0,2]]
        arcade.set_background_color(arcade.color.MSU_GREEN)
    def on_draw(self):
        arcade.start_render()
        for x in range(0, 601, 60):
            arcade.draw_line(x, 0, x, 600, arcade.color.BLACK, 2)

        for y in range(0, 601, 60):
            arcade.draw_line(0, y, 600, y, arcade.color.BLACK, 2)

            #IMAGE IMPORT
        texture1 = arcade.load_texture("Download.jpg")
        texture2 = arcade.load_texture("Download1.jpg")
        texture3 = arcade.load_texture("Download2.png")
        texture4 = arcade.load_texture("Download3.png")
        scale = .23
        scale1 = .15

        for i in range(10):
            for j in range(10):
                if self.grid[j][i] == 1:
                    X,Y = self.front_end(i,j)
                    arcade.draw_scaled_texture_rectangle(X, Y, texture1, scale, 0)
                if self.grid[j][i] == 2:
                    X,Y = self.front_end(i,j)
                    arcade.draw_scaled_texture_rectangle(X, Y, texture2, scale, 0)

                if self.grid[j][i] == 10:
                    X,Y = self.front_end(i,j)
                    arcade.draw_scaled_texture_rectangle(X, Y, texture3, scale1, 0)
                if self.grid[j][i] == 20:
                    X,Y = self.front_end(i,j)
                    arcade.draw_scaled_texture_rectangle(X, Y, texture4, scale1, 0)



        arcade.draw_scaled_texture_rectangle(570, 575, texture2, scale, 0)

            #ADDING THE NAMES OF PLAYER IN THE INTERFACE
            #FOR PLAYER 1

        arcade.draw_text("Player1:",630,400, arcade.color.BLACK, 15)
        arcade.draw_rectangle_outline(680 ,350, 100, 40, arcade.color.BLACK)

            #ADDING THE NAMES OF PLAYER IN THE INTERFACE
            #FOR PLAYER 2

        arcade.draw_text("Player2:",630 ,290, arcade.color.BLACK, 15)
        arcade.draw_rectangle_outline(680 ,240, 100, 40, arcade.color.BLACK)
    def front_end(self, x,y):
        A,B= 30,30
        for i in range(30,((x*60)+31),60):
            for j in range(30,((y*60)+31),60):
                A=i
                B=j
        return A, B

if __name__ == "__main__":
    Window = arcade.open_window(750, 600, "Mutahara snail game")
    game = Welcome()
    Window.show_view(game)

    arcade.run()



