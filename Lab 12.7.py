# Andrew Li
# 1824794

def fat_burning_heart_rate(age):
    rate = 0.7 * (220 - age)
    return rate


def get_age():
    pass


if __name__ == '__main__':
    test = fat_burning_heart_rate(int(input()))
    print(test)