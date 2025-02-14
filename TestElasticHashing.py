import unittest
from ElasticHashing import ElasticHashTable

class TestElasticHashTable(unittest.TestCase):

    def setUp(self):
        self.n = 64
        self.delta = 0.1
        self.hash_table = ElasticHashTable(self.n, self.delta)
        self.keys = ["key1", "key2", "key3", "key4", "key5"]

    def test_insert(self):
        for key in self.keys:
            result = self.hash_table.insert(key)
            self.assertTrue(result, f"Insertion failed for key: {key}")

        # Attempt to insert a duplicate key
        result = self.hash_table.insert("key1")
        self.assertFalse(result, "Duplicate key insertion should fail")

    def test_search(self):
        for key in self.keys:
            self.hash_table.insert(key)

        for key in self.keys:
            index = self.hash_table.search(key)
            self.assertNotEqual(index, -1, f"Search failed for key: {key}")

        # Search for a key not in the table
        index = self.hash_table.search("key_not_in_table")
        self.assertEqual(index, -1, "Search should fail for a key not in the table")

    def test_table_representation(self):
        for key in self.keys:
            self.hash_table.insert(key)

        table_repr = repr(self.hash_table)
        self.assertIsInstance(table_repr, str, "Table representation should be a string")

if __name__ == '__main__':
    unittest.main()
