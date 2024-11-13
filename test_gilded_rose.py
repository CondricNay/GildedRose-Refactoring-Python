# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_normal_item(self):
        items = [Item("Normal", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Normal", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_zero_quality_degrade_twice_as_fast(self):
        items = [Item("", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

    def test_negative_quality_degrade_twice_as_fast(self):
        items = [Item("", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

    def test_quality_never_negative(self):
        items = [Item("", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_increase_quality(self):
        items = [Item("Aged Brie", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_quality_normal_never_more_than_50(self):
        items = [Item("Normal", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(49, items[0].quality)

    def test_sulfuras_no_sell_in_and_quality_decrease(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(20, items[0].quality)

    def test_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 30, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(29, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_increase_quality_by_2_less_than_equal_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_increase_quality_by_3_less_than_equal_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(23, items[0].quality)

    def test_backstage_quality_is_0_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_update_many_normal_items(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="+10 Dexterity Vest", sell_in=10, quality=20),
            Item(name="+20 Aged Brie", sell_in=10, quality=20),
        ]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        for _ in range(len(items)):
            self.assertEqual(9, items[0].sell_in)
            self.assertEqual(19, items[0].quality)

    # def test_update_many_assorted_items(self):
    #     items = [
    #         Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
    #         Item(name="Aged Brie", sell_in=2, quality=0),
    #         Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
    #         Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
    #         Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
    #         Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
    #         Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
    #         Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
    #         Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    #     ]

    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()

    #     self.assertEqual(9, len(gilded_rose.items))



if __name__ == '__main__':
    unittest.main()
