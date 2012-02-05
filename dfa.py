#!/usr/bin/python3
'''
Created on 2012-02-04

@author: kevin
'''
def main():   
    print("Enter your alphabet.")
    alphabet = []
    char = input("{}: ".format(len(alphabet)))
    while(char != ''):
        alphabet.append(char)
        char = input("{}: ".format(len(alphabet)))
    
    print("Enter your states.")
    states = []
    state = input("{}: ".format(len(states)))
    while(state != ''):
        states.append(state)
        state = input("{}: ".format(len(states)))
        
    print("Enter the starting state")
    start_state = input()
    states.index(start_state)
    
    print("Enter your finish states")
    finish_states = []
    fstate = input("{}: ".format(len(finish_states)))
    while(fstate != ''):
        try:
            states.index(fstate)
            finish_states.append(fstate)
        except:
            print("The state you entered does not exist")
        finally:
            fstate = input("{}: ".format(len(finish_states)))
    
    transitions = []
    print("Enter transitions.")
    for s in states:
        for a in alphabet:
            transition = input("{} {} ".format(s,a))
            if transition != '':
                transitions.append((s,a,transition))
    
    outfile = input("Enter the output file name: ")
    f = open(outfile,"w")

    print(len(alphabet), end="\n", file=f)
    for a in alphabet: print(a, end="\n", file=f)
    
    print(len(states), sep='', file=f)
    for s in states: print(s, end="\n", file=f)
    
    print(start_state, end="\n", file=f)
    
    print(len(finish_states), end="\n", file=f)
    for fs in finish_states: print(fs, end="\n", file=f)
    
    print(len(transitions), end="\n", file=f)
    for t in transitions:
        print("{} {} {}".format(t[0],t[1],t[2]), end="\n", file=f)
    
    f.close()
if __name__ == "__main__": main()
