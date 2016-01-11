# -*- coding: utf-8 -*-
from unittest import main, TestCase

from segmenttree import SegmentTree

class TestSegmentTree(TestCase):
    def test_segtree(self):
        segtree = SegmentTree(1, 8)
        segtree.add(1, 3, 1)
        self.assertEqual(1, segtree.query_max(2, 5))
        self.assertEqual(2, segtree.query_len(2, 5))
        self.assertEqual(2, segtree.query_sum(2, 5))

        segtree.add(3, 4, 1)
        self.assertEqual(2, segtree.query_max(2, 5))
        self.assertEqual(3, segtree.query_len(2, 5))
        self.assertEqual(4, segtree.query_sum(2, 5))

        segtree.add(4, 5, 1)
        self.assertEqual(2, segtree.query_max(2, 5))
        self.assertEqual(4, segtree.query_len(2, 5))
        self.assertEqual(6, segtree.query_sum(2, 5))

        segtree.add(3, 6, 2)
        self.assertEqual(4, segtree.query_max(2, 5))
        self.assertEqual(4, segtree.query_len(2, 5))
        self.assertEqual(12, segtree.query_sum(2, 5))

        segtree.add(1, 7)
        self.assertEqual(5, segtree.query_max(2, 5))
        self.assertEqual(4, segtree.query_len(2, 5))
        self.assertEqual(16, segtree.query_sum(2, 5))

    def test_demo(self):
        segtree = SegmentTree(1, 8)
        segtree.add(1, 3, 1)
        segtree.add(3, 4, 1)
        segtree.add(4, 5, 1)
        segtree.add(3, 6, 2)
        segtree.add(1, 71)
        self.assertEqual(5, segtree.query_max(2, 5))
        self.assertEqual(4, segtree.query_len(2, 5))
        self.assertEqual(16, segtree.query_sum(2, 5))


    def test_empty(self):
        segtree = SegmentTree(0, 8)
        segtree.add(1, 1, 1)
        segtree.add(8, 8, 1)
        self.assertEqual(1, segtree.query_max(0, 8))
        self.assertEqual(2, segtree.query_len(0, 8))
        self.assertEqual(2, segtree.query_sum(0, 8))

if __name__ == '__main__':
    main()
