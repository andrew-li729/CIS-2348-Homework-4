# Andrew Li
# 1824794

def fat_burning_heart_rate(age):
    rate = 0.7 * (220 - age)
    return rate


def get_age():
    age_input = int(input())
    if age_input < 18 or age_input > 75:
        raise ValueError("Invalid Age.")
    return age_input


if __name__ == '__main__':
    try:
        age = get_age()
        rate = fat_burning_heart_rate(age)
        print("Fat burning heart rate for a {} year-old: {} bpm".format(age, rate))
    except ValueError as exception:
        print(exception)
        print("Could not calculate heart rate info.")


