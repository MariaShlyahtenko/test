import sys

def circular(n, m):
    result = []
    index = 0 
    while True:
        result.append(index + 1)  
        index = (index + m - 1) % n  

        if index == 0:
            break

    return ''.join(map(str, result))

if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    print(circular(n, m))
