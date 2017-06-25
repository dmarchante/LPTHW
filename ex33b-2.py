def looper(num_min, num_max, incrementor):
    numbers = []

    print "The numbers: "

    for num in range(num_min, num_max, incrementor):
        numbers.append(num)
        print num

looper(3, 30, 3)
