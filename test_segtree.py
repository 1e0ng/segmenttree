# -*- coding: utf-8 -*-
import os, sys
TEST_DIR = os.path.dirname(os.path.realpath(__file__))
DALE_DIR = os.path.dirname(TEST_DIR)
sys.path.insert(0, DALE_DIR)


from unittest import main, TestCase

from segtree import SegmentTree

class TestSegmentTree(TestCase):
    def test_segtree(self):
        segtree = SegmentTree(1, 8)
        segtree.add(1, 3, 1)
        self.assertEqual(1, segtree.query(2, 5))

        segtree.add(3, 4, 1)
        self.assertEqual(2, segtree.query(2, 5))

        segtree.add(4, 5, 1)
        self.assertEqual(2, segtree.query(2, 5))

        segtree.add(3, 6, 1)
        self.assertEqual(3, segtree.query(2, 5))

        segtree.add(1, 7, 1)
        self.assertEqual(4, segtree.query(2, 5))

      
if __name__ == '__main__':
    main()
