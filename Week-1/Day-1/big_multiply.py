from big_sum import bigSum

# assumption num1 maybe greater in digits than num2 but num2 is not greater in digits than num1

def big_multiply(num1: str, num2: str):
    carry = 0
    val = ''
    addables = []

    # multiplication phase
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num1) - 1, -1, -1):
            num1_int = int(num1[i])
            num2_int = int(num2[j])

            curr_val = (num1_int * num2_int) + carry
            print(num1_int, num2_int, carry)

            if curr_val > 9 and i > 0:
                carry = curr_val // 10
                curr_val = curr_val % 10
            
            val = str(curr_val) + val

            if i == 0:
                carry = 0
                val = ''


        addables.append(val)

    print(addables)

    # # addition phase
    # for i in addables:



big_multiply('87', '92')