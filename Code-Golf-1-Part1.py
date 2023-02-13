#836 Characters (We can do better)

num_string = '123456789' #Define number string

for i in range(0,18):
    
    #Case 1: First half of the pyramid
    if(i < 10):

        #Add spaces and correct numbers
        line = " " * (abs(9-i)) + num_string[:i % 10]
        
        #Reverse the second part of the line
        line_part_2 = line[:len(line)-1]
        line_part_2 = line_part_2[::-1]

        #Append line part 2 to line
        line = line + line_part_2
    
    #Case 2: Second half of the pyramid
    else:
        #Add spaces and correct numbers (In the reverse order of case 1)
        line = " " * (abs(9-i)) + num_string[:18 - i]
        
        #Reverse the second part of the line
        line_part_2 = line[:len(line)-1]
        line_part_2 = line_part_2[::-1]
       
        #Append line part 2 to line
        line = line + line_part_2


    #print out the line
    print(line)