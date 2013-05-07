#encoding:utf-8
#Created by Liang Sun on May, 6, 2013
class SegmentTree(object):
    def _init(self, start, end):
        self.data[(start, end)] = 0
        if start < end:
            mid = start + (end - start) / 2
            self._init(start, mid)
            self._init(mid+1, end)

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.data = {}
        self._init(start, end)

    def add(self, start, end, weight=1):
        if start < self.start or end > self.end:
            return False
        self._add(start, end, weight, self.start, self.end)
        return True

    def _add(self, start, end, weight, in_start, in_end):
        if in_start == in_end:
            self.data[(in_start, in_end)] += weight
            return

        mid = in_start + (in_end - in_start) / 2
        if mid >= end:
            self._add(start, end, weight, in_start, mid)
        elif mid+1 <= start:
            self._add(start, end, weight, mid+1, in_end)
        else:
            self._add(start, mid, weight, in_start, mid)
            self._add(mid+1, end, weight, mid+1, in_end)
        self.data[(in_start, in_end)] = max(self.data[(in_start, mid)], self.data[(mid+1, in_end)])

    def query(self, start, end):
        return self._query(start, end, self.start, self.end)

    def _query(self, start, end, in_start, in_end):
        if start == in_start and end == in_end:
            ans = self.data[(start, end)]
        else:
            mid = in_start + (in_end - in_start) / 2
            if mid >= end:
                ans = self._query(start, end, in_start, mid)
            elif mid+1 <= start:
                ans = self._query(start, end, mid+1, in_end)
            else:
                ans = max(self._query(start, mid, in_start, mid),
                        self._query(mid+1, end, mid+1, in_end))
        #print start, end, in_start, in_end, ans
        return ans
