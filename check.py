def winner(arr,y_axis,x_axis):


    # functions
    def dig_lst(lst,lst_2,lst_3):
        num = 0
        for i in range(len(lst) - 3):
            for i in range(4):
                lst_2.append(lst[num])
                num += 1
            lst_3.append(lst_2)
            lst_2 = []
            num -= 3


    def dig(lst,k,l,m,n):
        c,d = k,l
        for i in range(3):
            c += m
            d += n
            if 5 >= c >= 0 and 6 >= d >= 0:
                lst.append([c, d])


    def check(y,x):


        # variables
        arr_x = [[[y, 0], [y, 1], [y, 2], [y, 3]], [[y, 1], [y, 2], [y, 3], [y, 4]], [[y, 2], [y, 3], [y, 4], [y, 5]], [[y, 3], [y, 4], [y, 5], [y, 6]]]
        arr_dig = []
        array = []
        arr = []


        # y axis
        if y >= 3:
            arr.append([[y, x], [y - 1, x], [y - 2, x], [y - 3, x]])


        # x axis
        if x < 4:
            for i in range(x + 1):
                arr.append(arr_x[i])
        else:
            for i in range(x - 3, 4):
                arr.append(arr_x[i])


        # diagonal
        dig(array,y,x,-1,-1)
        array = array[::-1]
        array.append([y, x])
        dig(array,y,x,1,1)
        dig_lst(array,arr_dig,arr)
        array = []
        arr_dig = []
        dig(array,y,x,-1,1)
        array = array[::-1]
        array.append([y, x])
        dig(array,y,x,1,-1)
        dig_lst(array,arr_dig,arr)


        # return
        return arr




    # the code
    num = 0
    array = check(y_axis,x_axis)
    for axis in array:
        for single in axis:
            play = arr[single[0]][single[1]]
            if play == 'x':
                num += 2
            elif play == 'o':
                num += 7
        if num == 8:
            return 'Yellow'
        elif num == 28:
            return 'Red'
        else:
            num = 0