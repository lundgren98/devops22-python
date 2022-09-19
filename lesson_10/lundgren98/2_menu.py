from menu import Menu
from rectangle import Rectangles

def main():
    rects = Rectangles()
    main_menu = Menu([
            ('Create a rectangle',rects.append),
            ('Print a rectangle', rects.show),
            ('Delete a rectangle', rects.delete)])
    main_menu.run()

if __name__ == '__main__':
    main()
