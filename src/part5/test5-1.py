

if __name__ == "__main__":
    # N = 3
    # sample = ["10 40 70", "20 50 80", "30 60 90"]
    # data = [[int(j) for j in sample[i].split()] for i in range(N)]
    data = [[int(j) for j in input().split()] for i in range(int(input()))]
    last_idx = -1
    sum_data = 0
    for i in range(len(data)):
        max_data = data[i][0]
        for j in range(1,3):
            if data[i][j] > max_data and j != last_idx:
                max_data = data[i][j]
                max_idx = j
        last_idx = max_idx
        sum_data += max_data
    print(sum_data)
        
        

        
        



