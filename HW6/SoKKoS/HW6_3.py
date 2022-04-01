input_txt = input("Enter string - ")
output_list = list(input_txt)
output_dict = {}

for i in output_list:
    output_dict[i] = input_txt.count(i)


print(f'Output {output_dict}')





