#Input Code
#Number of rows - n
n= int (input("# of rows: "))
#Input restrictions
if n<1:
    print ("Input out of range! Enter a number greater than or equal to 1")
    n= int (input("Enter the number of rows: "))

#Number of Columns - m
m= int (input("# of columns: "))
#Input restrictions
if m>20:
    print ("Input out of range! Enter a number found to be less than or equal to 20")
    m= int (input("Enter the number of columns: "))

rows=1
y_list= []
while rows != n+1:
    newy_list = []
    height= (input("Enter height of the building (<50) moving horizontally downward: ")).split()

    for x in height:
        newy_list.append(int(x))
    y_list.append(newy_list)
    rows+=1

    print (y_list)

end=0

#Cavity logic
arr=[]
newarr=[]
cavities=False
while cavities== False:
    for q in range (1,(n-1)):
        for r in range (1,(m-1)):
            if (y_list[q][r])<(y_list[q][r-1]) and (y_list[q][r])<(y_list[q][r+1]) and (y_list[q][r])<(y_list[q+1][r]) and (y_list[q][r])< (y_list[q-1][r]):
                count_add=min(y_list[q][r-1],y_list[q][r+1],y_list[q+1][r],y_list[q-1][r])-y_list[q][r]
                arr.append(count_add)
                y_list[q][r]=min(y_list[q][r-1],y_list[q][r+1],y_list[q+1][r],y_list[q-1][r])
            else:
                print ("None")
    cavities=True


print (y_list)
print ("Analysing")

#Check for spill overs
spillover_cavities= False
arr2=[]
while spillover_cavities== False:
    for q in range (1,(n-1)):
        for r in range (1,(m-1)):
            temp_list= []
            temp_list.append (y_list[q][r-1])
            temp_list.append (y_list[q][r+1])
            temp_list.append (y_list[q-1][r])
            temp_list.append (y_list[q+1][r])
            if y_list[q][r]== y_list[q][r-1] and y_list[q][r]== y_list[q][r+1] and y_list[q][r]== y_list[q+1][r] and y_list[q][r]== y_list[q-1][r]:
                print ("Processing")
                
            elif y_list[q][r] == y_list[q][r-1] and r-1!=0 :
                temp_list.pop(0)
                r=r-1
                #print (y_list[q][r]) 
                temp_list.append (y_list[q][r-1])
                temp_list.append (y_list[q-1][r])
                temp_list.append (y_list[q+1][r])
                print (temp_list)
                if y_list[q][r]> min(temp_list):
                    print("found to be less than")
                
                elif y_list[q][r]== min(temp_list)and ((q+2 >= 0 or q-2 <=n )and (r+2<=m or r-2>=0))  :
                    print ("found to be equal")
                    count_add1=(min(temp_list)+1)- y_list[q][r]
                    print (count_add1)
                    arr.append(count_add1)
                    y_list[q][r]=min(temp_list)+1
                


                    
                else:
                    count_add1=min(temp_list)- y_list[q][r]
                    print (count_add1)
                    arr.append(count_add1)
                    y_list[q][r]=min(temp_list)+1
        
            elif y_list[q][r] == y_list[q][r+1] and r+1!=m:
                temp_list.pop(1)
                r+=1
                temp_list.append (y_list[q][r+1])
                temp_list.append (y_list[q-1][r])
                temp_list.append (y_list[q+1][r])
                print (temp_list)
                if y_list[q][r]> min(temp_list):
                    print("found to be less than")
                elif y_list[q][r]== min(temp_list)and ((q+2 >= 0 or q-2 <=n )and (r+2<=m or r-2>=0))  :
                    print ("equal works")
                    count_add1=(min(temp_list)+1)- y_list[q][r]
                    print (count_add1)
                    arr.append(count_add1)
                    y_list[q][r]=min(temp_list)+1


                else:
                    count_add2=min(temp_list)- y_list[q][r]
                    arr.append(count_add2)
                    y_list[q][r]=min(temp_list)
            
            elif y_list[q][r] == y_list[q+1][r] and  q+1!=0:
                temp_list.pop(3)
                q+=1
                temp_list.append (y_list[q][r-1])
                temp_list.append (y_list[q][r+1])
                temp_list.append (y_list[q+1][r])
                print (temp_list)
                if y_list[q][r]> min(temp_list):
                    print("found to be less than")
                elif y_list[q][r]== min(temp_list)and ((q+2 >= 0 or q-2 <=n )and (r+2<=m or r-2>=0))  :
                    print ("equal works")
                    count_add1=(min(temp_list)+1)- y_list[q][r]
                    print (count_add1)
                    arr.append(count_add1)
                    y_list[q][r]=min(temp_list)+1


                else:
                    count_add3=min(temp_list)- y_list[q][r]
                    arr.append(count_add3)
                    y_list[q][r]=min(temp_list)
            
            elif y_list[q][r] == y_list[q-1][r] and q-1!=n:
                temp_list.pop(2)
                q-=1
                temp_list.append (y_list[q][r-1])
                temp_list.append (y_list[q][r+1])
                temp_list.append (y_list[q-1][r])
                print (temp_list)
                if y_list[q][r]> min(temp_list):
                    print("found to be less than")
                elif y_list[q][r]== min(temp_list)and ((q+2 >= 0 or q-2 <=n )and (r+2<=m or r-2>=0))  :
                    print ("found to be equal")
                    count_add1=(min(temp_list)+1)- y_list[q][r]
                    print (count_add1)
                    arr.append(count_add1)
                    y_list[q][r]=min(temp_list)+1
                else:
                    count_add4=min(temp_list)- y_list[q][r]
                    arr.append(count_add4)
                    y_list[q][r]=min(temp_list)
                    
            else:
                print ("Done...")
    end+=1
    if end== 20:
        spillover_cavities= True
    else:
        spillover_cavities= False

#This checks for final cavities
print ("Success")

cavities=False
while cavities== False:
    for q in range (1,(n-1)):
        for r in range (1,(m-1)):
            if (y_list[q][r])<(y_list[q][r-1]) and (y_list[q][r])<(y_list[q][r+1]) and (y_list[q][r])<(y_list[q+1][r]) and (y_list[q][r])< (y_list[q-1][r]):
                count_add=min(y_list[q][r-1],y_list[q][r+1],y_list[q+1][r],y_list[q-1][r])-y_list[q][r]
                arr.append(count_add)
                y_list[q][r]=min(y_list[q][r-1],y_list[q][r+1],y_list[q+1][r],y_list[q-1][r])
    print (y_list)
    cavities=True

final_sum= sum(arr)
print ("The volume of water is:",final_sum, "units")
print (y_list)
    

       
                    
