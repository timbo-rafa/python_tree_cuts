from tree_cuts import solution
from itertools import repeat

class Unit_Test:
    _multiprocess_can_split_ = True

    def test_zero_trees(self):
        T = []

        ans = solution(T)
        assert ans == 0

    def test_one_tree(self):
        T = [999]

        ans = solution(T)
        assert ans == 0

    def test_two_ascending_trees(self):
        T = [1, 3]

        ans = solution(T)
        assert ans == 0

    def test_two_descending_trees(self):
        T = [4, 2]

        ans = solution(T)
        assert ans == 0

    def test_two_equal_trees(self):
        T = [5, 5]

        ans = solution(T)
        assert ans == 1

    def test_three_ascending_trees(self):
        T = [22, 45, 66]

        ans = solution(T)
        assert ans == 1

    def test_three_descending_trees(self):
        T = [444, 222, 5]

        ans = solution(T)
        assert ans == 1

    def test_three_equal_trees(self):
        T = [11, 11, 11]

        ans = solution(T)
        assert ans == 1
    
    def test_ten_equal_trees(self):
        T = list(repeat(8, 10))

        ans = solution(T)
        assert ans == 5

    def test_eleven_equal_trees(self):
        T = list(repeat(8, 11))

        ans = solution(T)
        assert ans == 5

    def test_even_valleys_even_length(self):
        T = [1, 500, 2, 501, 3, 502, 4, 503]

        ans = solution(T)
        assert ans == 0
    
    def test_even_valleys_odd_length(self):
        T = [1, 500, 2, 501, 3, 502, 4, 503, 5]

        ans = solution(T)
        assert ans == 0

    def test_odd_valleys_even_length(self):
        T = [100, 9, 101, 8, 102, 7, 103, 6]

        ans = solution(T)
        assert ans == 0

    def test_odd_valleys_odd_length(self):
        T = [100, 9, 101, 8, 102, 7, 103, 6, 104]

        ans = solution(T)
        assert ans == 0