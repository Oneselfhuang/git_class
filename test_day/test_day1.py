


def test_solution(nums_a: list, nums_b: list)-> list:
    for i in nums_b:
        while i in nums_a:
            nums_a.remove(i)
            print(nums_a)
    return nums_a



assert test_solution([1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3]) == [2, 2, 4]
assert test_solution([8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2 , 3], [2, 4, 3]) == [8, 7, 6, 5, 1]
assert test_solution([1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8], [1, 3, 4, 2]) == [5, 6 ,7 ,8]