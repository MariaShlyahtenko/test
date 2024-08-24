import sys

def calculate_min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

def read_nums(file_path):
    with open(file_path, 'r') as f:
        return [int(line.strip()) for line in f]

if __name__ == "__main__":
    file_path = sys.argv[1]
    nums = read_nums(file_path)

    min_moves = calculate_min_moves(nums)
    print(min_moves)
