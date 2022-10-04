#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    temp = dir(hidden_4)
    for temp in temp:
        if temp[:2] != "__":
            print(temp)
