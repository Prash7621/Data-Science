# This operator are used to compare the binary numbers :
# types :
 # 1.AND (&) operator
 # 2.OR (|) operator
 # 3.XOR (^) operator
 # 4.>>zero fill left shift
 # 5.<<zero fill right shift

print(bin(10))
print(bin(15))

# 1.AND (&) operator 
# (0 , 0 = 0)
# (1 , 0 = 0)
# (0 , 1 = 0)
# (1 , 1 = 1) 
print(10 & 8)

# 2.OR (|) operator
#(0 | 0 = 0)
#(1 | 0 = 1)
#(0 | 1 = 1)
#(1 | 1 = 1)
print(10 | 8)

# 3. XOR (^) operator
#(0 ^ 0 = 0)
#(1 ^ 0 = 1)
#(0 ^ 1 = 1)
#(1 ^ 1 = 1)
print(10 ^ 8)

# 4.>>zero fill left shift
print(10>>1)
# 5.<<zero fill right shift
print(10<<1)
