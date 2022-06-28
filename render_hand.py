import sys, random, math, pygame
from pygame.locals import *
import argparse

card_dict={
  '2': '2',        
  '3': '3',        
  '4': '4',        
  '5': '5',        
  '6': '6',        
  '7': '7',        
  '8': '8',        
  '9': '9',        
  'T': '10',        
  'J': 'J',        
  'Q': 'Q',        
  'K': 'K',        
  'A': 'A',        
  'B': 'Joker_B',
  'R': 'Joker_R'
}

type_dict={
    0: 'C',
    1: 'H',
    2: 'S',
    3: 'D',
}

card_size = (190.0, 275.0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--card", help="card sequence", type=str)
    parser.add_argument("-s", "--space", help="inner space of rendered cards", type=float, default=2.7)
    args = parser.parse_args()

    inner_space = args.space
    pygame.init()
    # space = pygame.image.load("./imgs/Poker_C10.png").convert_alpha()
    # card_size = space.get_rect().size
    screen = pygame.display.set_mode((card_size[0]*15, card_size[1]+10))
    mid_size = card_size[1]

    total_width = 0
    total_height = card_size[1]

    for card in args.card:
        if card not in card_dict.keys():
            continue
        card_name = card_dict[card]
        card_color = type_dict[random.randint(0, 3)]
        if 'Joker' in card_name:
            card_color = ''
        print('./imgs/Poker_{}{}.png'.format(card_color, card_name))
        card_file_name = './imgs/Poker_{}{}.png'.format(card_color, card_name)
        space = pygame.image.load(card_file_name).convert_alpha()

        screen.blit(space, (total_width, 0))
        pygame.draw.line(screen, (0,0,0), (total_width, 0), (total_width, total_height), 2)
        total_width += card_size[0]/inner_space

    total_width = total_width-card_size[0]/inner_space + card_size[0]
    rect = pygame.Rect(0, 0, total_width, total_height)
    print(total_width, total_height)
    sub = screen.subsurface(rect)

    pygame.image.save(sub, "{}.png".format(args.card.strip()))
    # pygame.image.save(screen, "screenshot.jpg")
    exit(0)
