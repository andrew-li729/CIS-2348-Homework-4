# Andrew Li
# 1824794

def fat_burning_heart_rate(age):
    rate = 0.7 * (220 - age)
    # print("Fat burning hear rate for a {} year-old: {} bpm".format(age, rate))
    return rate


def get_age():
    age_input = int(input())
    if age_input < 18 or age_input > 75:
        raise ValueError("Invalid Age.")
    return age_input


if __name__ == '__main__':
    age = get_age()

    fat_burning_heart_rate(age)

