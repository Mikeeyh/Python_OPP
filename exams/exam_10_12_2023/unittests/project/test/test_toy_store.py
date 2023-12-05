from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.toy = ToyStore()
        self.toy_shelf ={
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

    def test_correct_init(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy.toy_shelf)

    def test_add_toy_shelf_not_existing_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("Z", "toyiiz")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_already_exists_name_matches_raises_exception(self):
        self.toy.add_toy("A", "toyiiz")
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("A", "toyiiz")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_already_exists_name_miss_matches_raises_exception(self):
        self.toy.add_toy("A", "toyiiz")
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("A", "koyiiz")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_with_success(self):
        self.toy_store = ToyStore()
        result = self.toy_store.add_toy("A", "ToyTestName")

        self.assertEqual(result, "Toy:ToyTestName placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": "ToyTestName",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_remove_toy_method_shelf_is_already_taken(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("K", "ToyTestName")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_method_toy_on_that_shelf_does_not_exist(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "ToyTestName")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

        self.toy_store.add_toy("A", "ToyTestNameOne")
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "ToyTestNameTwo")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_method_successfully_removed_toy_from_shelf(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy("A", "ToyTestName")
        result = self.toy_store.remove_toy("A", "ToyTestName")

        self.assertEqual(result, "Remove toy:ToyTestName successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })


if __name__ == '__main__':
    main()

