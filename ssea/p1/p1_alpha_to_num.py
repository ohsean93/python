# incording : utf-8
# p1_alpha_to_num.py

str_origin = list(input().upper())

num_str = [(ord(x)-64) for x in str_origin]

print(num_str)

