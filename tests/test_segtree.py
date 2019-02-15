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
        segtree.add(1, 1)
        segtree.add(8, 8)
        self.assertEqual(1, segtree.query_max(0, 8))
        self.assertEqual(2, segtree.query_len(0, 8))
        self.assertEqual(2, segtree.query_sum(0, 8))

    def test_full_out_of_bound(self):
        segtree = SegmentTree(0, 8)
        segtree.add(0, 8)

        # Test full out of bound adding element fails
        self.assertEqual(False, segtree.add(10, 16))
        self.assertEqual(False, segtree.add(-16, -10))

        # Test full out of bound len query returns 0
        self.assertEqual(0, segtree.query_len(10, 16))
        self.assertEqual(0, segtree.query_len(-16, -10))

        # Test full out of bounds len query returns 0
        self.assertEqual(0, segtree.query_sum(10, 16))
        self.assertEqual(0, segtree.query_sum(-16, -10))

        # Test full out of bounds max query returns None
        self.assertEqual(None, segtree.query_max(10, 16))
        self.assertEqual(None, segtree.query_max(-16, -10))

    def test_partial_out_of_bound(self):
        segtree = SegmentTree(0, 8)
        segtree.add(0, 8)

        # Test partial out of bound adding element
        self.assertEqual(True, segtree.add(8, 16))
        self.assertEqual(True, segtree.add(-16, 0))

        # Test partial out of bound len query
        self.assertEqual(2, segtree.query_len(7, 16))
        self.assertEqual(2, segtree.query_len(-16, 1))

        # Test partial out of bounds len query
        self.assertEqual(3, segtree.query_sum(7, 16))
        self.assertEqual(3, segtree.query_sum(-16, 1))

        # Test full out of bounds max query
        self.assertEqual(2, segtree.query_max(7, 16))
        self.assertEqual(2, segtree.query_max(-16, 1))

if __name__ == '__main__':
    main()
