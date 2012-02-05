#!/usr/bin/python3
'''
Created on 2012-02-04

@author: kevin
'''
def main():   
    print("Enter your alphabet. Type ! when done")
    alphabet = []
    char = input("{}: ".format(len(alphabet)))
    while(char != '!'):
        alphabet.append(char)
        char = input("{}: ".format(len(alphabet)))
    
    print("Enter your states. Type ! when done")
    states = []
    state = input("{}: ".format(len(states)))
    while(state != '!'):
        states.append(state)
        state = input("{}: ".format(len(states)))
        
    print("Enter the starting state")
    start_state = input()
    states.index(start_state)
    
    print("Enter your finish states")
    finish_states = []
    fstate = input("{}: ".format(len(finish_states)))
    while(fstate != '!'):
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
    
    print(len(alphabet))
    for a in alphabet: print(a)
    
    print(len(states))
    for s in states: print(s)
    
    print(start_state)
    
    print(len(finish_states))
    for f in finish_states: print(f)
    
    print(len(transitions))
    for t in transitions:
        print("{} {} {}".format(t[0],t[1],t[2]))

if __name__ == "__main__": main()