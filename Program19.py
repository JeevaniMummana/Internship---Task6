if __name__ == '__main__':
    s = input()

    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    for ch, freq in result[:3]:
        print(ch, freq)