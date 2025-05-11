import unittest
from src.homework.i_dictionaries_and_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory = {}
      
        add_inventory(inventory, "Widget1", 10)
        self.assertEqual(inventory["Widget1"], 10)

        # Update existing widget
        add_inventory(inventory, "Widget1", 25)
        self.assertEqual(inventory["Widget1"], 35)

        # Subtract from existing widget
        add_inventory(inventory, "Widget1", -10)
        self.assertEqual(inventory["Widget1"], 25)

    def test_remove_inventory_widget(self):
        inventory = {
            "Widget1": 10,
            "Widget2": 20
        }
        result = remove_inventory_widget(inventory, "Widget1")
        self.assertEqual(result, "Record deleted")
        self.assertEqual(len(inventory), 1)
        self.assertIn("Widget2", inventory)
