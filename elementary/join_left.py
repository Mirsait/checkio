
def left_join(phrases):
    return ','.join(phrases).replace('right', 'left')


def test():
    left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
    left_join(("bright aright", "ok")) == "bleft aleft,ok"
    left_join(("brightness wright",)) == "bleftness wleft"
    left_join(("enough", "jokes")) == "enough,jokes"

if __name__ == '__main__':
    test()
