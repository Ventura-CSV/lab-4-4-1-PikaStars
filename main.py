def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    #Input Validation
    number = int(input('Enter your input:'))

    while (number < 0 or number > 100):
        number = int(input("The input should be between 0 and 100"))
    
    print(number)

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
