# Andrew Li
# 1824794

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
    except ValueError:  # if converting part[1] to int gives an error, do this
        age = 0         # sets age to zero if second part of input is not an integer
        print('{} {}'.format(name, age))

    # Get next line
    parts = input().split()
    name = parts[0]
