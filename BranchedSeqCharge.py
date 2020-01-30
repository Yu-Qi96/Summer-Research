'''
Computation of Sequence Charge Decoration
Author: Yu Qi
'''

def BranchedSeqCharge(b1, b2, tail, branchpoint):
    # `
    #  ` <-- branch1  |    b1 and b2 are branch sequences without the "tail"
    #   `        V
    #    ` （NC)_ _ _ _  <--- TAIL (starts after "NC")    NC(from formula) is branchpoint
    #    ,
    #   ,
    #  ,         ^
    # ,   <-- branch2 \    tail begins at the 5th char (index 4) in this example

    total1 = 0
    total2 = 0
    total3 = 0

    pCharged = ["K", "H", "R"]
    nCharged = ["D", "E"]

    #Section 1
    #summation from m=2 (second letter of b1 sequence) to N1
        #summation from n=1 (first letter of b1) to m-1 (second to last letter of b1 sequence)

    #First we must add the first and second branches together, with NC in between:
    tempstring = b1 + branchpoint

    for x in range(0,len(b2)):
        tempstring += b2[len(b2) - x - 1]

    for m in range (1, len(tempstring)):  #m is index number of the string - in formula it starts at 2 instead of 1
        if(tempstring[m] in pCharged):   #assign Q values based on amino
            q1 = 1
        elif(tempstring[m] in nCharged):
            q1 = -1
        else:
            q1 = 0
        for n in range (0, m): #n can be up to m-1, which is essentially c (b/c m = c + 1), but still is the index number of the string
            if(tempstring[n] in pCharged):
                q2 = 1
            elif(tempstring[n] in nCharged):
                q2 = -1
            else:
                q2 = 0
            total1 += q1 * q2 * ((m-n)**0.5)
    print("Total1: " + str(total1) + "\n")

    #Section 2
    #to be determined based on sequence indexes, math part is complete.


    for m in range(0, len(tail)):
        if(tail[m] in pCharged):
            q1 = 1
        elif(tail[m] in nCharged):
            q1 = -1
        else:
            q1 = 0
        mIndex = len(b1) + m + 2
        for n in range(0, len(b1)): #if using for index, these are not proper index values
            if(b1[m] in pCharged):
                q2 = 1
            elif(b1[m] in nCharged):
                q2 = -1
            else:
                q2 = 0
            nIndex = n + 1
            nC = len(b1) + 1
            total2 += (q1*q2*((nC - nIndex)**2))/((mIndex-(nIndex))**(3/2))
    print("Total2: " + str(total2) + "\n")


    #Section 3
    #to be determined based on sequence indexes, math part is complete.

    #concatenate and reverse b2 with branching point
    # for instance "ABC"(b2) + "D" (branching point) becomes "DCBA"

    tempb2 = b2 + branchpoint
    tempb2reverse = ""

    for x in range(0,len(tempb2)):
        tempb2reverse += b2[len(b2) - x - 1]

    for m in range(0, len(tempb2reverse)): #if using for index, these are not proper index values
        if(tempb2reverse[m] in pCharged):
            q1 = 1
        elif(tempb2reverse[m] in nCharged):
            q1 = -1
        else:
            q1 = 0
        mIndex = len(b1) + 1 + m
        for n in range(0, len(tail)):
            if(tail[n] in pCharged):
                q2 = 1
            elif(tail[n] in nCharged):
                q2 = -1
            else:
                q2 = 0
            nIndex = len(b1) + n + 2
            nC = len(b1) + 1
            total3 += (q1*q2*((mIndex-nC)**2))/((mIndex+nIndex-(2*(nC)))**(3/2))
    print("Total3: " + str(total3) + "\n")

    return total1 + total2 + total3


