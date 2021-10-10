
import arcade




arcade.open_window(750, 600, "Mutahara's snail game inferfae")
arcade.set_background_color(arcade.color.MSU_GREEN)
arcade.start_render()
for x in range(0, 640, 60):
    arcade.draw_line(x, 0, x, 600, arcade.color.BLACK, 2)

for y in range(0, 650, 50):
    arcade.draw_line(0, y, 600, y, arcade.color.BLACK, 2)

    #IMAGE IMPORT
texture1 = arcade.load_texture("Download.jpg")
texture2 = arcade.load_texture("Download1.jpg")
scale = .23
arcade.draw_scaled_texture_rectangle(31, 25, texture1, scale, 0)
arcade.draw_scaled_texture_rectangle(570, 575, texture2, scale, 0)

    #ADDING THE NAMES OF PLAYER IN THE INTERFACE
    #FOR PLAYER 1

arcade.draw_text("Player1:",630,400, arcade.color.BLACK, 15)
arcade.draw_rectangle_outline(680 ,350, 100, 40, arcade.color.BLACK)

    #ADDING THE NAMES OF PLAYER IN THE INTERFACE
    #FOR PLAYER 2

arcade.draw_text("Player2:",630 ,290, arcade.color.BLACK, 15)
arcade.draw_rectangle_outline(680 ,240, 100, 40, arcade.color.BLACK)
   


























arcade.finish_render()
arcade.run()