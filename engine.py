#import the libtcodpy with a slightly shorter name
import libtcodpy as libtcod
#import handle_keys function
from input_handlers import handle_keys

#the main method
def main():
    #2 variables for screen width and height
    screen_width = 80
    screen_height = 50
    
    #2 variables that allow for adjustment to the player's position and tracking
    player_x = int(screen_width/2)
    player_y = int(screen_height/2)

    #detail where the fole file is, and what type
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    #create the window and give it a height, width, title, and a variable for whether it goes full screen or not
    libtcod.console_init_root(screen_width, screen_height, 'Dare', False)
    #
    con = libtcod.console_new(screen_width, screen_height)
    #2 variables to hold our keyboard and mouse input
    key = libtcod.Key()
    mouse = libtcod.Mouse()
    #the game's loop, that never ends until the window closes
    while not libtcod.console_is_window_closed():
        #This function captures events(user input) and updates the appropriate variables
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        
        #give the color and location of the ascii symbol
        libtcod.console_set_default_foreground(con, libtcod.white)
        #which console where to put it x,y coords, which char to print, and what background it has 
        libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE)
        libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        libtcod.console_flush()
        
        libtcod.console_put_char(con, player_x, player_y, ' ', libtcod.BKGND_NONE)
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
            player_x += dx
            player_y += dy
        
        if exit:
            return True
        
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        if key.vk == libtcod.KEY_ESCAPE:
            return True

#only runs the script if its name is called otherwise it doesn't run
if __name__ == '__main__':
     main()