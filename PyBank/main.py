import csv 


#CREATING NESSARRY VARIABLES
file_name = 'budget_data_1.csv'
month_count = 0
total_rev = 0
total_diff = 0
diff_new = []

#IMPORTING CSV FILE 
with open (file_name, 'r', newline='') as budget1_file:
    budget1_data = csv.reader(budget1_file, delimiter=',') 
    
    #passing headers
    next (budget1_data)
    
    budget_list = list(budget1_data)
    
    #calcuating total months and total reveune 
    for data,rev in enumerate(budget_list):
        month_count = month_count + 1
        total_rev = total_rev +int(rev[1])
    print("Total Months: " + str(month_count))
    print("Total Revenue: " + "$" + str(total_rev)) 
    
    #cacluating average difference 
    for date, rev in enumerate(budget_list):
        if date + 1 < month_count:
            diff = int(budget_list[date+1][1]) - int(budget_list[date][1])
            total_diff = total_diff + diff
            avg_diff = round(total_diff/month_count,2)
            diff_new.append(diff)
        
    #print(diff_new)
    
    #creating list of absolue values of revenue differences
    diff_absolute =[]
    for row in diff_new:
        diff_absolute.append(abs(row))
        
    #print(diff_absolute)
    
    #calculating the max and min revenue difference
    max_rev = max(diff_absolute)
    min_rev = min(diff_absolute)
    #print(max_rev)
    #print(min_rev)
    min_index=(diff_absolute.index(min_rev))
    max_index=(diff_absolute.index(max_rev))
    #print(min_index)
    #print(max_index)
    #print(diff_absolute)
    #print(max_rev)
    #print(min_rev)
            
        
    print("Average Revenue Change: " + "$" + str(avg_diff))
    print("Greatest Increase in Revenue: " + str(budget_list[max_index+1][0])+ " $" +str(diff_new[max_index]))
    print("Greatest Decrease in Revenue: " + str(budget_list[min_index+1][0])+ " $" +str(diff_new[min_index]))
    
    with open('output.txt', 'w') as out_file:
        out_file.write(("Total Months: " + str(month_count))+ "\n")
        out_file.write("Total Revenue: " + "$" + str(total_rev)+ "\n")
        out_file.write("Average Revenue Change: " + "$" + str(avg_diff) +"\n")
        out_file.write("Greatest Increase in Revenue: " + str(budget_list[max_index+1][0])+ " $" +str(diff_new[max_index])+ "\n")
        out_file.write("Greatest Decrease in Revenue: " + str(budget_list[min_index+1][0])+ " $" +str(diff_new[min_index])+ "\n")
    
        
    