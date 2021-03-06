# Methods of Dispersion -> Finding Mean, Median, Mode of Grouped Data

# from Measures_of_Dispersion import input_values 
# # import above ^ is commented out because ot the section of code below also being commented out

def main():
    set_labels = []
    frequency_count = []
    counter = 0
    status = True

    interval = int(input('Enter interval for set: '))
    lower_limit = int(input('Enter a lower limit: '))
    upper_limit = int(input('Enter a higher limit: '))

    lower_limit_clone = lower_limit

    # Assigning labels for set intervals
    for i in range(lower_limit, upper_limit, interval):
        set_labels.append(str(lower_limit_clone) + ' -> ' + str(lower_limit_clone + (interval-1)))
        frequency_count.append(0)
        lower_limit_clone += interval
        counter += 1

    # If data is present in the given
    print()

    for i in range(0, len(frequency_count)):
        frequency_count[i] = int(input(f'Enter frequency for {set_labels[i]}: '))

    # # For raw data input
    # data_set = []

    # input_values(data_set)
    # lower_limit_clone = lower_limit                   # -> DO NOT DELETE THIS SECTION <- #

    # for i in range(0, counter):

    #     for j in range(0, len(data_set)):

    #         if data_set[j] < (lower_limit_clone + interval) and data_set[j] >= lower_limit_clone:
    #             frequency_count[i] += 1

    #     lower_limit_clone += interval

    while (True):
        method_of_dispersion = input('\nPress [1] for Mean\nPress [2] for Median\nPress [3] for Mode\nEnter choice: ')

        if method_of_dispersion == '1':
            mean_operation = input('\nPress [1] for Long Method\nPress [2] for Coded Deviation\nEnter choice: ')

            if mean_operation == '1':
                long_method(set_labels, frequency_count, lower_limit, upper_limit, interval)
            elif mean_operation == '2':
                coded_deviation(set_labels, frequency_count, lower_limit, upper_limit, interval)

        elif method_of_dispersion == '2':
            median(set_labels, frequency_count, lower_limit, interval)

        elif method_of_dispersion == '3':
            mode(set_labels, frequency_count, lower_limit, interval)

        print('\nPress [1] to select another mode\nPress [2] to reset data input\nPress [3] to exit program')
        user_repeat = input('\nEnter choice: ')

        if user_repeat == '1':
            pass
        elif user_repeat == '2':
            print(f'\n[INFO] Resetting data values...\n')
            break
        else:
            print('\nThank you for using the program!')
            status = False
            break
    
    return status

def median(set_labels: list, frequency_count:list, lower_limit: int, interval: int):
    lb_mc = 0
    sum_of_f = 0
    f_mc = 0
    modal_class = 0
    less_cf_perm = 0
    less_cf_temp = 0
    lower_limit_clone = lower_limit
    highest_freq = frequency_count[0]

    lb_list = []
    less_cf_list = []

    for i in range(0, len(frequency_count)):
        lb = lower_limit_clone - 0.5
        sum_of_f += frequency_count[i]
        lower_limit_clone += interval
        lb_list.append(lb)

        less_cf_temp += frequency_count[i]
        less_cf_list.append(less_cf_temp)

        if frequency_count[i] > highest_freq:
            modal_class = i
            highest_freq = frequency_count[i]

    f_mc = frequency_count[modal_class]
    lb_mc = lb_list[modal_class]

    if modal_class <= 0:
        less_cf_perm = 0
    else:
        less_cf_perm = less_cf_list[modal_class - 1]

    set_median = lb_mc + ((((sum_of_f /2 ) - less_cf_perm) / f_mc) * interval)

     # Printing the final table
    print(f'\nData\t\tFrequency\tlb\t<cf')

    for i in range(len(set_labels)):
        print(f'{set_labels[len(set_labels)-(i+1)]}\t{frequency_count[len(set_labels)-(i+1)]}', end='')
        print(f'\t\t{lb_list[len(set_labels)-(i+1)]}\t{less_cf_list[len(set_labels)-(i+1)]}')

    print(f'\nSum of f = {sum_of_f}')
    print(f'Median = ' + '{:.2f}'.format(round(set_median, 2)))
    print(f'lb_mc = ' + '{:.2f}'.format(round(lb_mc, 2)))
    print(f'<cf = {less_cf_perm}')
    print(f'f_mc = {f_mc}')


def mode(set_labels: list, frequency_count:list, lower_limit: int, interval: int):
    lb_mo = 0
    d1 = 0
    d2 = 0
    sum_of_f = 0
    modal_class = 0
    lower_limit_clone = lower_limit
    highest_freq = frequency_count[0]

    lb_list = []

    for i in range(0, len(frequency_count)):
        lb = lower_limit_clone - 0.5
        sum_of_f += frequency_count[i]
        lower_limit_clone += interval
        lb_list.append(lb)

        if frequency_count[i] > highest_freq:
            modal_class = i
            highest_freq = frequency_count[i]
        
    lb_mo = lb_list[modal_class]

    if modal_class >= (len(frequency_count) -1):
        d1 = frequency_count[modal_class] - 0
    else:
        d1 = (frequency_count[modal_class]) - (frequency_count[modal_class + 1])

    if modal_class <= 0:
        d2 = frequency_count[modal_class] - 0
    else:
        d2 = (frequency_count[modal_class]) - (frequency_count[modal_class - 1])

    set_mode = lb_mo + (d1 / ((d1 + d2)) * interval)

    # Printing the final table
    print(f'\nData\t\tFrequency\tlb')

    for i in range(len(set_labels)):
        print(f'{set_labels[len(set_labels)-(i+1)]}\t{frequency_count[len(set_labels)-(i+1)]}', end='')
        print(f'\t\t{lb_list[len(set_labels)-(i+1)]}')

    print(f'\nSum of f = {sum_of_f}')
    print(f'Mode = ' + '{:.2f}'.format(round(set_mode, 2)))


def long_method(set_labels: list, frequency_count:list, lower_limit: int, upper_limit, interval: int):
    x = []
    fx = []
    sum_of_f = 0
    sum_of_fx = 0
    lower_limit_clone = lower_limit

    # Printing the first table
    print(f'\nData\t\tFrequency')

    for i in range(len(set_labels)):
        print(f'{set_labels[len(set_labels)-(i+1)]}\t{frequency_count[len(set_labels)-(i+1)]}')

    # Assigning values per column
    for i in range(lower_limit, upper_limit, interval):
        row_mean = ((lower_limit_clone + (lower_limit_clone + (interval-1))) / 2)
        x.append(row_mean)
        lower_limit_clone += interval

    for i in range(0, len(x)):
        product = frequency_count[i] * x[i]
        fx.append(product)
        
        sum_of_f += frequency_count[i]
        sum_of_fx += product

    data_mean = sum_of_fx / sum_of_f

    # Printing the final table
    print(f'\nData\t\tFrequency\tX\t\tFX')

    for i in range(len(set_labels)):
        print(f'{set_labels[len(set_labels)-(i+1)]}\t{frequency_count[len(set_labels)-(i+1)]}', end='')
        print(f'\t\t{x[len(set_labels)-(i+1)]}\t\t{fx[len(set_labels)-(i+1)]}')

    print(f'\nSum of f = {sum_of_f}')
    print(f'Sum of fx = {sum_of_fx}')
    print(f'Mean = {data_mean}')


def coded_deviation(set_labels: list, frequency_count:list, lower_limit: int, upper_limit, interval: int):
    x = []
    d = []
    fd = []
    sum_of_f = 0
    sum_of_fd = 0
    lower_limit_clone = lower_limit
    highest_freq_value = frequency_count[0]
    AM_placeholder = 0

    # Printing the first table
    print(f'\nData\t\tFrequency')

    for i in range(len(set_labels)):
        print(f'{set_labels[len(set_labels)-(i+1)]}\t{frequency_count[len(set_labels)-(i+1)]}')

    for i in range(lower_limit, upper_limit, interval):
        row_mean = ((lower_limit_clone + (lower_limit_clone + (interval-1))) / 2)
        x.append(row_mean)
        lower_limit_clone += interval

    # Checking the highest frequency value
    for i in range (0, len(frequency_count)):
        d.append(0)

        if frequency_count[i] > highest_freq_value:
            highest_freq_value = frequency_count[i]
            AM_placeholder = i

    # Assigning the 'd' values
    counter = 0    

    for i in range(AM_placeholder, len(frequency_count)):
        d[i] = counter
        counter += 1

    counter = 0
    index = AM_placeholder

    while (index >= 0):
        d[index] = counter
        index -= 1
        counter -= 1

    # Getting the 'fd'
    for i in range(0, len(d)):
        product = frequency_count[i] * d[i]
        fd.append(product)

        sum_of_f += frequency_count[i]
        sum_of_fd += product

    data_mean = x[AM_placeholder] + ((sum_of_fd * interval) / sum_of_f)

    # Printing the final table
    print(f'\nData\t\tFrequency\tX\t\td\tfd')

    for i in range(len(set_labels)):
        print(f'{set_labels[len(set_labels)-(i+1)]}\t{frequency_count[len(set_labels)-(i+1)]}', end='')
        print(f'\t\t{x[len(set_labels)-(i+1)]}\t\t{d[len(set_labels)-(i+1)]}\t{fd[len(set_labels)-(i+1)]}')

    print(f'\nSum of f = {sum_of_f}')
    print(f'Sum of fd = {sum_of_fd}')
    print(f'Mean = {data_mean}')

 
if __name__ == '__main__':
    while (True):
        reset = main()

        if reset == False:
            break
