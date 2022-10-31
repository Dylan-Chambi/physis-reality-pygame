import pygame
from game.items.Item import Item
# from utils.utils import calculate_center, collition_query

from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FPS


class Scene:
    def __init__(self, background_img: pygame.Surface = None, bg_color: tuple = (39, 185, 245, 0.8)):
        self.item_list: list = []
        self.bg_color: tuple = bg_color
        self.static_items = pygame.sprite.Group()
        self.dynamic_items = pygame.sprite.Group()
        if background_img is None:
            self.background_img = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.background_img.fill(self.bg_color)
        else:
            self.background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))


    def add_static_item(self, item: Item) -> None:
        self.item_list.insert(0, item)
        self.static_items.add(item)

    def add_dynamic_item(self, item: Item) -> None:
        self.item_list.append(item)
        self.dynamic_items.add(item)
    
    def pre_loads(self) -> None:
        pass

    def update(self, pressed_keys: list) -> None:
        screen = pygame.display.get_surface()
        screen.blit(self.background_img, (0, 0))
        for item in self.item_list:
            item.draw_in_screen()
            item.update(pressed_keys, self)



    def on_event(self, event: pygame.event) -> None:
        pass
        # for player in self.players:
        #     player.on_event(event)