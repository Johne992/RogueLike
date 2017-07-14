#import the libtcodpy with a slightly shorter name
import libtcodpy as libtcod
#import handle_keys function
from input_handlers import handle_keys
from entity import Entity
from render_functions import clear_all, render_all
from map_objects.game_map import GameMap
#the main method
def main():
    #2 variables for screen width and height
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground':libtcod.Color(50, 50, 150)
    }
    
    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow)
    entities = [npc, player]

    #detail where the fole file is, and what type
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    #create the window and give it a height, width, title, and a variable for whether it goes full screen or not
    libtcod.console_init_root(screen_width, screen_height, 'Dare', False)
    
    con = libtcod.console_new(screen_width, screen_height)
    
    game_map = GameMap(map_width, map_height)
    
    #2 variables to hold our keyboard and mouse input
    key = libtcod.Key()
    mouse = libtcod.Mouse()
    #the game's loop, that never ends until the window closes
    while not libtcod.console_is_window_closed():
        #This function captures events(user input) and updates the appropriate variables
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        
        render_all(con, entities, game_map, screen_width, screen_height, colors)
        libtcod.console_flush()
        
        clear_all(con, entities)
        #assign the handle_keys function to the name action
        action = handle_keys(key)
        #all of these check the returned dictionary for a particular key and assign the value to the
        #variable of choice
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')
        #make logical decisions depending on which key is returned
        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y +dy):
                player.move(dx, dy)
        
        if exit:
            return True
        
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        if key.vk == libtcod.KEY_ESCAPE:
            return True

#only runs the script if its name is called otherwise it doesn't run
if __name__ == '__main__':
     main()