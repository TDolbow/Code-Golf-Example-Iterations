
num_string = '123456789'
for i in range(0,18):
    if(i < 10):
        line = " " * (abs(9-i)) + num_string[:i % 10]
        line_part_2 = line[:len(line)-1]
        
        line_part_2 = line_part_2[::-1]

        line = line + line_part_2
    else:
        line = " " * (abs(9-i)) + num_string[:18 - i]
        line_part_2 = line[:len(line)-1]
        line_part_2 = line_part_2[::-1]
        line = line + line_part_2


    print(line)