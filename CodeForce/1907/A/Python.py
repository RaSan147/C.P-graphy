def main():
	c, r = list(input())
	
	C = list("abcdefgh")
	R = list("12345678")
	C.remove(c)
	R.remove(r)
	Cs = [f"{c}{y}" for y in R]
	Rs = [f"{x}{r}" for x in C]
	
	print(*(Cs + Rs), sep="\n")
	
for _ in range(int(input())):
	main()