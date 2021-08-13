import cProfile
from min_heap import perform_test_min_heap, perform_test_std_collection


if __name__ == '__main__':
    print('-------MIN HEAP-------')
    cProfile.run('perform_test_min_heap(100000)')
    cProfile.run('perform_test_min_heap(1000000)')
    cProfile.run('perform_test_min_heap(10000000)')
    print('-------STD------------')
    cProfile.run('perform_test_std_collection(100000)')
    cProfile.run('perform_test_std_collection(1000000)')
    cProfile.run('perform_test_std_collection(10000000)')
