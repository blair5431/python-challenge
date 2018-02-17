import csv
#improting csv file
file_name = 'election_data_1.csv'
with open (file_name, 'r', newline='') as election1_file:
    election1_data = csv.reader(election1_file, delimiter=',') 

    #TOTAL NUMBER OF VOTES CAST 
    voter_count = (sum (1 for row in election1_data))-1
    print("Election Results")
    print("-------------------")
    print ("Total Voters:" + str(voter_count))
    print("-------------------")

with open (file_name, 'r', newline='') as election1_file:
    election1_data1 = csv.reader(election1_file, delimiter=',') 

    #CREATE A LIST OF CANIDIATES WHO RECIVED VOTES 
    next (election1_data1)
    voter_info ={}
    for row in election1_data1:
        #print(row)
    
        try:
            voter_info[row[2]] = voter_info[row[2]] +1
        except:
            voter_info[row[2]]=1 
    
    #calc the percent of voters each canditate had
    for name,number in voter_info.items():
        vote_percent = ((number/voter_count)*100)
        
        print(str(name) + ": " + str(vote_percent)+"% " +"(" + str(number) + ")")
    print("-------------------")
    print("Winner: Vestal")
    print("-------------------")
    
