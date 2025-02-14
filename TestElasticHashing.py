import unittest
from ElasticHashing import ElasticHashTable
import string
import random

class TestElasticHashTable(unittest.TestCase):

    def setUp(self):
        self.n = 64
        self.delta = 0.1
        self.hash_table = ElasticHashTable(self.n, self.delta)

    def test_insert_until_full(self):
        steps_per_insertion = []
        for _ in range(self.n):
            key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            steps = self.insert_with_steps(key)
            if steps is not None:
                steps_per_insertion.append(steps)
            else:
                break

        # Print statistics
        for i, steps in enumerate(steps_per_insertion):
            print(f"Insertion {i + 1}: {steps} steps")

        # Ensure table is full
        self.assertEqual(len(self.hash_table.inserted_keys), self.n, "Table should be full")

    def insert_with_steps(self, key):
        """
        Inserts a key into the hash table and returns the number of steps taken.
        Returns None if the table is full.
        """
        if key in self.hash_table.inserted_keys:
            return 0
        
        steps = 0
        for i, array_size in enumerate(self.hash_table.arrays):
            probe_sequence = self.hash_table._probe_sequence(key, i)
            for probe in probe_sequence:
                steps += 1
                if self.hash_table.table[probe] is None:
                    self.hash_table.table[probe] = key
                    self.hash_table.inserted_keys.add(key)
                    return steps
        return None

if __name__ == '__main__':
    unittest.main()
