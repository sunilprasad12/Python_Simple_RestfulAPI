from unittest import TestCase

from models.item import ItemModel

class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 19.99)

        self.assertEqual(item.name, 'test', 'thkdlfsjlksjlkjlwkdflksajlksadflklkaslkfdljk')
        self.assertEqual(item.name, 19.99, 'fdsjlkdajlkjlkjlkadjslkdjlskdfajlksadjflksdaflk')

    def test_item_json(self):
        item = ItemModel('test', 19.99)
        expected = {
            'name': 'test',
            'price': 19.99
        }

        self.assertEqual(item.json(), expected, "the json export of the item is incorrect. Receiveed {}, expected{}".format(item.json(),
                                                                                                                          expected ))
