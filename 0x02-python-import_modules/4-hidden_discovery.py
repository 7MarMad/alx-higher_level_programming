#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    res_dir = dir(hidden_4)
    i = 0
    for j in res_dir:
        if j[0:2] != "__":
            break
        i = i + 1
    for p in range(i, len(res_dir)):
        print(res_dir[p])
