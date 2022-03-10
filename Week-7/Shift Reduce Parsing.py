non_terminals = []
production=[]
product1=[]
product2=[]
print("Enter the non terminals :")
non_terminals.append(input())
print("1st")
production.append(input())
print("2nd")
product1.append(input())
print("3rd")
product2.append(input())
lo =[]
lo.append(production)
lo.append(product1)
lo.append(product2)
lo
l= list(zip( lo[0],lo[1],lo[2]))
gram = dict(zip(non_terminals,l))


print(gram)
starting_terminal =non_terminals[0]
print("starting-terminal "+ str(starting_terminal))
print("input string")
inp=input()


stack = "$"
print(f'{"Stack": <15}'+"|"+f'{"Input Buffer": <15}'+"|"+f'Parsing Action')
print(f'{"-":-<50}')

while True:
	action = True
	i = 0
	while i<len(gram[starting_terminal]):
		if gram[starting_terminal][i] in stack:
			stack = stack.replace(gram[starting_terminal][i],starting_terminal)
			print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Reduce S->{gram[starting_terminal][i]}')
			i=-1
			action = False
		i+=1
	if len(inp)>1:
		stack+=inp[0]
		inp=inp[1:]
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Shift')
		action = False

	if inp == "$" and stack == ("$"+starting_terminal):
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Accepted')
		break

	if action:
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Rejected')
		break