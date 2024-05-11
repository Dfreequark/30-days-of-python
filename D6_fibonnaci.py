def fibonnaci():
    while True:
        num_terms=input("Enter the length of the Fibonnaci Series :")
        if num_terms.isdigit():
            num_terms=int(num_terms)
            if num_terms<2:
                print("Length must be greater than equal to 2")
            else:
                break
        else:
            print("Enter the length in number.")
    number =[0,1]
    while len(number)< num_terms:
        first_no=number[-2]
        second_no= number[-1]
        result = first_no+second_no
        number.append(result)

    print("The Fibonnaci series upto ",num_terms," terms :\n", number)

fibonnaci()