def priority_setter(duration,dependancies):
    """
    Calculates the weighted priority for two equal-length list inputs, duration and 
    number_of_dependancies and returns a single list.
    """
    
    #Storage of the weighted priorities
    weighted_priority = []
    
    #Compute the weighted priority for every item in lists duration, dependancies
    for i in range(len(duration)):
        
        #Number of dependancies accounts for 75% of the value
        #The less dependencies, the higher the priority
        weighted_priority.append(round((duration[i]/max(duration))*25+(1 - (dependancies[i]/max(dependancies)))*75))
        
    return weighted_priority 
    
duration = [15,30,15,30,30,25,30,5,30,20,10,50,90,10,5,30,20,10,45,5,40,5,40,55,40,30,30,20,10,25,60,25]
dependancies = [0,1,2,1,0,0,0,0,1,0,0,1,2,0,1,2,3,1,0,1,1,1,1,0,1,2,3,0,1,1,1,1]

#print the list horizontally
print(priority_setter(duration,dependancies))

#tests
assert(priority_setter([1,2,3,4,5],[5,4,3,2,1]) == [5, 25, 45, 65, 85])
assert(priority_setter([1,1,1,1,1],[1,1,1,1,1]) == [25, 25, 25, 25, 25])
assert(priority_setter([4,0,7,5,9],[4,0,7,5,9]) == [53, 75, 36, 47, 25])
assert(priority_setter([1,2,3,4,5],[1,2,3,4,5]) == [65, 55, 45, 35, 25])
assert(priority_setter([5,4,3,2,1],[5,4,3,2,1]) == [25, 35, 45, 55, 65])