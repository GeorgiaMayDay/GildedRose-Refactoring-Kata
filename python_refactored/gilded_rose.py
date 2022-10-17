# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from unicodedata import category

def increaseItem(item, increase_amount):
    if item.quality < 50:
        item.quality += increase_amount
    return item

def decreaseItem(item, decrease_amount):
    if item.quality > 0:
        item.quality -= decrease_amount
    return item

def decreaseQuality(quality, decrease_amount):
    if quality > 0:
        quality -= decrease_amount
    return quality

def increaseQuality(quality, increase_amount):
    if quality < 50:
        quality += increase_amount
    return quality

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            processor = ItemProcessor(item)
            
            updatedItem = processor.update_item()
            item.quality = updatedItem.quality
            item.sell_in = updatedItem.sell_in



class BaseItem(ABC):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def update_quality():
        pass


class Item(BaseItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Category(ABC):
    def __init__(self, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        pass
        
    def tick_days_down(self):
        self.sell_in -= 1

class Regular(Category):
    def __init__(self, sell_in, quality):
        super().__init__
        self.sell_in = sell_in
        self.quality = quality
    
    def tick_days_down(self):
        self.sell_in -= 1

    def update_quality(self):
        self.quality = decreaseQuality(self.quality, 1)
        Regular.tick_days_down(self)
        if self.sell_in < 0:
            self.quality = decreaseQuality(self.quality, 1)
        return self.sell_in, self.quality

class Conjured(Category):
    def __init__(self, sell_in, quality):
        super().__init__
        self.sell_in = sell_in
        self.quality = quality
    
    def tick_days_down(self):
        self.sell_in -= 1

    def update_quality(self):
        self.quality = decreaseQuality(self.quality, 2)
        Conjured.tick_days_down(self)
        if self.sell_in < 0:
            self.quality = decreaseQuality(self.quality, 2)
        return self.sell_in, self.quality

class Brie(Category):
    def __init__(self, sell_in, quality):
        super().__init__
        self.sell_in = sell_in
        self.quality = quality
    
    def tick_days_down(self):
        self.sell_in -= 1

    def update_quality(self):
        self.quality = increaseQuality(self.quality, 1)
        Brie.tick_days_down(self)
        if self.sell_in < 0:
            self.quality = increaseQuality(self.quality, 1)
        return self.sell_in, self.quality
        
class BackstagePass(Category):
    def __init__(self, sell_in, quality):
        super().__init__
        self.sell_in = sell_in
        self.quality = quality

    def tick_days_down(self):
        self.sell_in -= 1

    def update_quality(self):
        BackstagePass.tick_days_down(self)
        self.quality = increaseQuality(self.quality, 1)
        if self.sell_in < 11:
            self.quality = increaseQuality(self.quality, 1)
        if self.sell_in < 6:
            self.quality = increaseQuality(self.quality, 1)
        if self.sell_in < 0:
            self.quality = 0
        return self.sell_in, self.quality
        
        
class Legend(Category):
    def __init__(self, sell_in, quality):
        super().__init__
        self.sell_in = sell_in
        self.quality = quality

    def tick_days_down(self):
        self.sell_in -= 1

    def update_quality(self):
        return self.sell_in, self.quality

class ItemProcessor():
    def categorises_items(name, sell_in, quality):
        if(name == "Sulfuras, Hand of Ragnaros"):
           return Legend(sell_in, quality)
        if name == "Aged Brie":
            return Brie(sell_in, quality)
        if name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePass(sell_in, quality)
        if name == "Conjured Mana Cake":
            return Conjured(sell_in, quality)
        return Regular(sell_in, quality)
        

    def __init__(self, item):
        self.item = item
        self.category = ItemProcessor.categorises_items(item.name, item.sell_in, item.quality)

    def update_item(self):
        updated_sell_in, updated_quality = self.category.update_quality()
        return Item(self.item.name, updated_sell_in, updated_quality)




