from time import time


from main import isSumTwo, find_sums
# Performance comparison between isSumTwo and find_sums
if __name__ == "__main__":
    
    # Test with larger dataset
    
    large_numbers = list(range(1000))
    print(f"\nTesting with larger dataset ({len(large_numbers)} numbers):")
    target_sum_large = 1500

    # isSumTwo with large dataset
    start_time = time()
    result1_large = isSumTwo(large_numbers, target_sum_large)
    end_time = time()
    time1_large = end_time - start_time
    print(
        f"isSumTwo (large): {result1_large}, time: {time1_large:.6f} seconds")

    # find_sums with large dataset
    start_time = time()
    result2_large = find_sums(large_numbers, target_sum_large)
    end_time = time()
    time2_large = end_time - start_time
    print(
        f"find_sums (large): {result2_large}, time: {time2_large:.6f} seconds")

    if time1_large > 0:
        speedup_large = time2_large / time1_large
        print(f"With larger dataset, isSumTwo is {speedup_large:.2f}x faster")
    else:
        print("time of faster solution too small")
        
# Testing with larger dataset (10000 numbers):
# isSumTwo (large): False, time: 0.002949 seconds
# find_sums (large): False, time: 0.808812 seconds
# With larger dataset, isSumTwo is 274.29x faster
# PS C:\Users\User\Documents\Java_60\back-end\python-intro> py main.py

# Testing with larger dataset (100000 numbers):
# isSumTwo (large): False, time: 0.053100 seconds
# find_sums (large): False, time: 103.723033 seconds
# With larger dataset, isSumTwo is 1953.37x faster      
