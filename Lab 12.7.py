# Andrew Li
# 1824794

def fat_burning_heart_rate(age):
    rate = 0.7 * (220 - age)
    print("Fat burning hear rate for a {} year-old: {} bpm".format(age, rate))


def get_age():
    age_input = int(input("Enter age:"))
    return age_input


if __name__ == '__main__':
    age = get_age()
    if age < 18 or age > 75:
        raise ValueError("Invalid Age.\nCould not calculate heart rate info.")
    fat_burning_heart_rate(age)

