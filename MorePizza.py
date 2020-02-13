"""
Input Format:
    first line:
        an integer M, 1<=M<=10^9-----the maximum no. of pizza slices to order
        an integer N, 1<=N<=10^5-----the no. of different pizza types
    second line:
        N integers----the no. of slices in each type of pizza in non-decreasing (ascending) order

Output format:
    first line:
        an integer K, 0<=K<=N------the no. of differnet pizza types to order
    second line:
        K integers----the types of pizzas to order

The total no. of slices in the ordered pizzas must be less than or equal to M.
"""

def OrderPizza(Target, Slice):
    Sum = 0
    current_Sum = 0
    Pizza = []
    current_Pizzas = []
    l = len(Slice)
    i = 0
    for i in range (l-1, -1, -1):
        j = i
        current_Sum = 0
        current_Pizzas = []
        while j >= 0 and current_Sum <= Target:
            current_Sum += Slice[j]
            if current_Sum > Target:
                current_Sum -= Slice[j]
            else:
                current_Pizzas.append(str(j))
            j -= 1
        if abs(Sum-Target) > abs(current_Sum-Target):
            Sum = current_Sum
            Pizza = current_Pizzas
    Pizza.sort()
    return Pizza


Target = 0
Slice = []

with open("c_medium.in") as File:
    Given_input = File.read()
    #print (type(Given_input))
    Input = Given_input.split()
    #print (Input)
    for i in range (2, 2+int(Input[1])):
        Slice.append(int(Input[i]))
    Target = int(Input[0])

#print (Target)
#print (Slice)

result = OrderPizza(Target, Slice)
modified_results = ' '.join(result)

print (len(result))
print (modified_results)