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
            diff = int(budget_list[date+1][1])
            total_diff = total_diff + diff
            avg_diff = round(total_diff/month_count,2)
            max_rev = max(rev)
            min_rev = min(rev)
        
        if rev == max_rev:
            print(rev)
            
        if rev == min_rev:
            print(rev[0])
            
        
    print("Average Revenue Change: " + "$" + str(avg_diff))
    print("Greatest Increase in Revenue: " + str(max_rev))
    print("Greatest Decrease in Revenue: " + "$" + str(min_rev))
    
    