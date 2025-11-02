n = int(input())
s = input().strip()

if n % 11 != 0:
    print(0)
else:
    segments = n // 11
    for i in range(segments):
        start_index = i * 11
        if s[start_index] != '7' or s[start_index + 1] != '9':
            print(0)
            break
    else:
        print(1)
