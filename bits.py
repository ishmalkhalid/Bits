class BitList:
    # Part 1 goes here!

    # constructor
    def __init__(self, num):
        self.bin_num = None
        #ensuring object starts with 0b
        if num[:2] != '0b':
            raise ValueError("Format is invalid; does not start with 0b")
        #ensuring object contains only 0 and 1
        for n in num[2:]:
            if n != '0' and n != '1':
                raise ValueError("Format is invalid; does not consist of only 0 and 1.")

        self.bits = num[2:]

    @staticmethod
    def from_ints(*bnums):
        #ensuring object contains only 0 and 1
        for i in range(len(bnums)):
            if bnums[i] != 0 and bnums[i] != 1:
                raise ValueError("Format is invalid; does not consist of only 0 and 1.")

        num = '0b' + ''.join([str(n) for n in bnums])
        return BitList(num)

    #to print out the value of a bitlist instance
    def __str__(self):
        return str(''.join(self.bits))

    #shift the bits in the series to the left
    def arithmetic_shift_left(self):
        binlist = list(self.bits)
        binlist.pop(0)
        binlist.append(binlist[0])
        self.bits = '0b' + ''.join(binlist)

    #shift the bits in the series to the right
    def arithmetic_shift_right(self):
        binlist = list(self.bits)
        binlist.pop(-1)
        binlist.insert(1, binlist[0])
        self.bits = ''.join(binlist)

    #to allow comparison between two series of bits
    def __eq__(self, other):
        return self.bin_num == other.bin_num

    #comparing bitlists to find the truth value
    def bitwise_and(self, otherBitList):
        if len(self.bits) == len(otherBitList.bits):
            newbit = []
            for i in range(2, len(self.bits)):
                result = int(self.bits[i]) * int(otherBitList.bits[i])
                newbit.append(str(result))
            return BitList('0b' + ''.join(newbit))
        else:
            print("The lengths of the bits are not the same.")

    #decoding a bitlist
    def decode(self, encoding):
        if encoding != "us-ascii" and encoding != "utf-8":
            print("Error! The encoding can only be us-ascii or utf-8.")
        count = 0
        code_point = ''
        decimal = []
        for i in range(len(self.bits)):
            count += 1
            if count < 8:
                code_point += self.bits[i]
            elif count == 8:
                code_point += ' '
                code_point += self.bits[i]
                count = 1

        # display the code points in decimal
        decimallist = code_point.split(" ")
        decodelist = []
        for i in range(len(decimallist)):
            decimal = int(int(decimallist[i], 2))
            decodelist.append(chr(decimal))
        return ''.join(decodelist)

# ---------------------------------------
#PART 2 STARTS HERE
if __name__ == '__main__':
    print('Part 2 goes here!')
    final_list = []
    while True:
        cont = True
        each_loop_list = []
        # ask the user for series of 0s and 1s
        corr_form = False
        while corr_form == False:

            old_bits = input("Give me some bits!\n")

            # remove spaces from the input
            bits = old_bits
            for b in old_bits:
                if b == ' ':
                    bits = old_bits.replace(' ', '')

            # make sure only 1s and 0s are entered
            for b in bits:
                if b != '0' and b != '1':
                    print("Error! Incorrect format. Please re-enter value.")
                    corr_form = False
                    break
                else:
                    corr_form = True

        # ensure bits are divisible by 7
        if len(bits) % 7 != 0:
            num_of_zeroes = 7 - (len(bits) % 7)
            bits = num_of_zeroes * '0' + bits

        # ----------------------------------------
        # ask for an encoding
        while True:
            encoding = input("Give me an encoding!\n")
            each_loop_list.append(encoding)

            if encoding == "us-ascii":
                break

            else:
                print("Please enter us-ascii.")

        # -----------------------------------------
        # display original input without spaces
        print("Input: ", bits)

        # display code points in binary
        count = 0
        code_point = ''
        decimal = []
        for i in range(len(bits)):
            count += 1
            if count < 8:
                code_point += bits[i]
            elif count == 8:
                code_point += ' '
                code_point += bits[i]
                count = 1

        print("Code Points Binary: ", code_point)
        each_loop_list.append(code_point)

        #checking if the encoding and the input has not been entered before
        for alist in final_list:
            if alist[0] == each_loop_list[0] and alist[1] == each_loop_list[1]:
                print("You already entered those bits and encoding: ", alist[2])
                cont = False
                break

        if cont == True:
            # display the code points in decimal
            print("Code Points Decimal: ", end="")
            decimallist = code_point.split(" ")
            decodelist = []
            for i in range(len(decimallist)):
                decimal = int(int(decimallist[i], 2))
                decodelist.append(chr(decimal))
                print(decimal, end=" ")
            print("")

            print("Decoded String: ", end="")
            for decoder in decodelist:
                print(decoder, end=" ")
            print("")
            each_loop_list.append(''.join(decodelist))
            final_list.append(each_loop_list)
        # ask the user if they would like to continue
        answer = input("Type Y to enter more bits?\n")
        print("==========================\n\n")

        # end system if no continuation
        if answer != 'Y':
            print("Thanks, these were all the bits you entered!")
            for i in final_list:
                 print(i[0] + "-" + i[1], " >>> ", i[2])
            break

#-----------------------------------------------
#END OF PROGRAM