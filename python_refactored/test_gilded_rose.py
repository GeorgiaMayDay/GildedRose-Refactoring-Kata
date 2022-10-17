# -*- coding: utf-8 -*-
import unittest

from gilded_rose import BackstagePass, Brie, Category, Conjured, Item, ItemProcessor, GildedRose, Legend, Regular


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_brie_quality(self):
        quality = 5
        items = [Item("Aged Brie", 4, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality+1, items[0].quality)
    
    def test_brie_sell_decrease(self):
        sell_in = 4
        items = [Item("Aged Brie", sell_in, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(sell_in-1, items[0].sell_in)

    def test_legendary_items_do_not_change(self):
        sell_in = 4
        quality = 80
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(sell_in, items[0].sell_in)
        self.assertEqual(quality, items[0].quality)
    
    def test_backstage_increase(self):
        sell_in = 12
        quality = 30
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality+1, items[0].quality)
    
    def test_backstage_increase_more_as_sell_in_date_gets_closer(self):
        sell_in = 9
        quality = 30
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality+2, items[0].quality)

        sell_in = 3
        quality = 30
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality+3, items[0].quality)
    
    def test_brie_after_sell_in_date(self):
        sell_in = 0
        quality = 30
        items = [Item("Aged Brie", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality+2, items[0].quality)

    def test_backstage_pass_after_sell_in_date(self):
        sell_in = -1
        quality = 30
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_does_not_go_above_50(self):
        sell_in = 12
        quality = 49
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality), Item("cheedle", sell_in, quality), Item("Aged Brie", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue(50 >= items[0].quality)

    def test_quality_does_not_go_below_0(self):
        sell_in = -2
        quality = 0
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality), Item("cheedle", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue(0 <= items[0].quality)
    
    def test_item_processor(self):
        sell_in = 10
        quality = 30
        item = Item("Cheedle", sell_in, quality)
        itemProcessor = ItemProcessor(item) 
        itemUpdated = itemProcessor.update_item()       
        
        self.assertEqual(itemUpdated.name, item.name)

    def test_item_processor_regular_update_quality_and_sell_in(self):
        sell_in = 10
        quality = 30
        item = Item("Cheedle", sell_in, quality)
        itemProcessor = ItemProcessor(item) 
        itemUpdated = itemProcessor.update_item()    
        print(itemUpdated.quality)  
        print(item.quality)    
        
        self.assertEqual(item.quality-1, itemUpdated.quality)
        self.assertEqual(sell_in-1, itemUpdated.sell_in)

    def test_category_regular_update_quality_and_sell_in(self):
        sell_in = 10
        quality = 30
        categoriser = Regular(sell_in, quality)
        updated_sell_in, updated_quality = categoriser.update_quality()  
        
        self.assertEqual(sell_in-1, updated_sell_in)
        self.assertEqual(quality-1, updated_quality)

    def test_item_processor_legendary_update_quality(self):
        sell_in = 10
        quality = 80
        item = Item("Sulfuras, Hand of Ragnaros", sell_in, quality)
        itemProcessor = ItemProcessor(item) 
        itemUpdated = itemProcessor.update_item()       
        
        self.assertEqual(item.quality, itemUpdated.quality)

    def test_category_regular_update_quality(self):
        sell_in = 10
        quality = 80
        categoriser = Legend(sell_in, quality)
        updated_sell_in, updated_quality = categoriser.update_quality()   

        self.assertEqual(sell_in, updated_sell_in)

    def test_item_processor_backstage_pass_update_quality(self):
        sell_in = 10
        quality = 30
        item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)
        itemProcessor = ItemProcessor(item) 
        itemUpdated = itemProcessor.update_item()       
        
        self.assertEqual(item.quality+2, itemUpdated.quality)

    def test_category_backstage_pass_update_quality(self):
        sell_in = 10
        quality = 30
        categoriser = BackstagePass(sell_in, quality)
        updated_sell_in, updated_quality = categoriser.update_quality() 

        self.assertEqual(sell_in-1, updated_sell_in)
        self.assertEqual(quality+2, updated_quality)
    
    def test_item_processor_brie_update_quality_and_sell_in(self):
        sell_in = 10
        quality = 30
        item = Item("Aged Brie", sell_in, quality)
        itemProcessor = ItemProcessor(item) 
        itemUpdated = itemProcessor.update_item()       
        
        self.assertEqual(item.quality+1, itemUpdated.quality)
        self.assertEqual(sell_in-1, itemUpdated.sell_in)

    def test_category_brie_update_quality_and_sell_in(self):
        sell_in = 10
        quality = 30
        categoriser = Brie(sell_in, quality)
        updated_sell_in, updated_quality = categoriser.update_quality()   
        
        self.assertEqual(sell_in-1, updated_sell_in)
        self.assertEqual(quality+1, updated_quality)

    def test_item_processor_conjured_update_quality_and_sell_in(self):
        sell_in = 10
        quality = 30
        item = Item("Conjured Mana Cake", sell_in, quality)
        itemProcessor = ItemProcessor(item) 
        itemUpdated = itemProcessor.update_item()       
        
        self.assertEqual(item.quality-2, itemUpdated.quality)
        self.assertEqual(sell_in-1, itemUpdated.sell_in)

    def test_category_conjured_update_quality_and_sell_in(self):
        sell_in = 10
        quality = 30
        categoriser = Conjured(sell_in, quality)
        updated_sell_in, updated_quality = categoriser.update_quality()   
        
        self.assertEqual(sell_in-1, updated_sell_in)
        self.assertEqual(quality-2, updated_quality)

        
if __name__ == '__main__':
    unittest.main()
