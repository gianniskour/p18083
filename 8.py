def latin(n):
    
    units = ["", "I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX"] #1 ~  9

    dozens = ["", "X", "XX", "XXX", "XL", "L","LX", "LXX", "LXXX", "XC"] #10 ~ 90

    hundreds = ["", "C", "CC", "CCC", "CD", "D","DC", "DCC", "DCCC", "CM"] #100 ~ 900

    thousands =  ["", "M", "MM", "MMM","IV̅","V̅","V̅M","V̅MM","V̅MMM","IX̅"] #1.000 ~ 9.000

                 
    tenthousands =  ["","X̅","X̅X̅","X̅X̅X̅","X̅L̅","L̅","L̅X̅","L̅X̅X̅","L̅X̅X̅X̅","X̅C̅"]  #10.000 ~ 90.000

    hundredthousands =  ["","C̅","C̅C̅","C̅C̅C̅","C̅D̅","D̅","D̅C̅","D̅C̅C̅","D̅C̅C̅C̅","̅CM̅̅"]   #100.000 ~ 900.000

    hundredthousands = hundredthousands[n // 100000]
    tenthousands = tenthousands[(n % 100000)// 10000]
    thousand = thousands[(n % 10000) // 1000]
    hundred = hundreds[(n % 1000) // 100]
    tens = dozens[(n % 100) // 10]
    ones = units[n % 10]
    
    ans = (hundredthousands+tenthousands + thousand + hundred +
		tens + ones)
    return ans
	 
latin(900000)
latin(10100)
a = input()
