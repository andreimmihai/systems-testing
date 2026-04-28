import unittest

class TestTree(unittest.TestCase):
    def setUp(self):
        from tree import Tree
        self.tree = Tree()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)
    
    def test_find_exists(self):
        node = self.tree.find(3)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 3)

    def test_find_not_exists(self):
        node = self.tree.find(10)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
#comentariu exercitiul3
