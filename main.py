# Check: https://en.wikipedia.org/wiki/Elementary_cellular_automaton

def D2b(n):
    """
    Convert a decimal number to binary and add enough leading zeros 
    to make its length 8, thus representing each of the possible 
    outputs for each cell of an elementary cellular automaton.
    
    Keyword arguments:
    n -- Integer between 0 and 255
    
    Returns:
    rule -- List of 8 binary integers
    """
    rule = bin(n).replace("0b", "")
    
    while len(rule)<8:
        rule = str(0) + rule
    
    if len(rule)>8: raise Exception("Sorry, there is no rule "+str(n))
    
    rule = [int(c) for c in rule]
    return(rule)


def new_cell(terna, rule):
    """ 
    Calculates the output of a given cell in the next iteration 
    based on the state of that cell and its neighbors in the current 
    iteration according to the active rule. 
    
    Keyword arguments:
    terna -- List of three binary integers
    rule -- List of 8 binary integers
    
    Returns:
    rule[i] -- Binary integer
    """
    if terna == [1,1,1]: return(rule[0])
    elif terna == [1,1,0]: return(rule[1]) 
    elif terna == [1,0,1]: return(rule[2])       
    elif terna == [1,0,0]: return(rule[3])  
    elif terna == [0,1,1]: return(rule[4]) 
    elif terna == [0,1,0]: return(rule[5])   
    elif terna == [0,0,1]: return(rule[6]) 
    elif terna == [0,0,0]: return(rule[7])
    

def new_state(current_state, m):
    """
    Receives the status of the current iteration and calculates the 
    next iteration according to the rule represented by "m".

    
    Keyword arguments:
    current_state -- List of n binary integers
    m -- Interger between 0 and 255
    
    Returns:
    next_state -- List of n binary integers
    """
    
    rule = D2b(m)
    next_state = [0]
    current_state.append(current_state[0])
    for j in range(1, len(current_state)-1):
        
        c = current_state[j]
        i = current_state[j-1]
        d = current_state[j+1]
        
        terna = [i,c,d]
        result = new_cell(terna, rule)
        next_state.append(result)
        
    return(next_state)

def draw(state):
    """
    Print the state to the console.
    """
    cadena = ""
    for cell in state:
        if cell==0:
            cadena += "■"
        elif cell==1:
            cadena += "□"
    
    print(cadena)


# We now run the simulation:
    
from time import sleep  
import random

n = 32  # Number of cells
k = 100 # Number of iterations
current_state = [random.choice([0, 1]) for x in range(n)] # Random choice of initial conditions


    
for i in range(k):
    current_state = new_state(current_state, 110)
    draw(current_state)
    sleep(0.05)