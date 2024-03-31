import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "in ha mood"

class MyGame(arcade.Window):
  def __init__(self):
    super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)
    self.wall_list = None
    self.player_list = None
    
  def setup(self):
    """Set up the game here. Call this function to restart the game."""
    self.player_list = arcade.SpriteList()
    self.wall_list = arcade.SpriteList(use_spatial_hash=True)
    #creates the first player
    self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
    self.player_sprite.center_x = 64
    self.player_sprite.center_y = 128
    self.player_list.append(self.player_sprite)
    # Create the ground
    for x in range(0, 1250, 64):
      street = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
      street.center_x = x
      street.center_y = 32
      self.wall_list.append(street)
      
      coordinate_list = [[512, 96], [256, 96], [768, 96]]

      for coordinate in coordinate_list:
          # Add a crate on the ground
          wall = arcade.Sprite(
              ":resources:images/tiles/boxCrate_double.png", TILE_SCALING
          )
          wall.position = coordinate
          self.wall_list.append(wall)

    
    pass

  def on_draw(self):
    self.clear()
    
def main():
  window = MyGame()
  window.setup()
  arcade.run()


if __name__ == "__main__":
  main()

self.player_list = arcade.SpriteList()
self.wall_list = arcade.SpriteList(use_spatial_hash=True)

'''
nice_spice = Rectangle(50,50)
nice_spice.fill("#FF9F00")
nice_spice.set_position(0,0)
add(nive_spice)
"""