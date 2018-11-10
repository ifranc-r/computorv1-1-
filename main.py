import sys

def is_num(num):
    try:
        float(num)
    except ValueError:
    	return False
    return True

def is_space(str):
	try:
		if str == " ":
			return True
	except ValueError:
		return False
	return False

def is_operation(char):
	operation = ['/', '*', '-', '+']
	if len(char) is 1:

		try:
			if char in operation:
				return True
		except ValueError:
			return False
	return False

def is_equal(str):
	try:
		if str is "=":
			return True
	except ValueError:
		return False
	return False

def is_point(str):
	if char is 1:
		try:
			if char is ".":
				return True
		except ValueError:
			return False
	return False

def is_x_coordinate(str):
	try:
		coord, power = str.split('^')
		if coord is 'X' and is_num(power)is True:
			return True
		else:
			return False
	except ValueError:
		return False
	return False

def check_formula(formule):
	for str in formule:

		if is_num(str) or \
				is_operation(str) or\
				is_x_coordinate(str):
			# print str, "--> ",is_num(str), is_operation(str), is_x_coordinate(str)
			pass
		else:
			return False
	return True


def is_equation(str):

	if str.count('=') is 1:
		equation, result =  str.split('=')
		if len(result.split()) > 0 and \
				len(equation.split()) > 0:
			if check_formula(equation.split()) and check_formula(result.split()):
				equation = paratheses(take_minos(equation.split()))
				result = paratheses(take_minos(result.split()))
				return equation, result
		return False
	else:
		return False

def take_minos(equation):
	operation_index = []
	tmp = equation[:]
	for x in range(len(equation)):
		if equation[x] is "-":
			operation_index.append(x)
			tmp[x + 1] = str(float(equation[x + 1]) * -1)
		if equation[x] is "+":
			operation_index.append(x)

	for i in operation_index:
		tmp.pop(i - (len(equation) - len(tmp)))
	return tmp

def paratheses(equation):
	operation_index = []
	tmp = []
	for x in range(len(equation)):
		if 'X' in equation[x] and x > 1:
			tmp.append({"power" : int(equation[x][2]),\
						"operation" : equation[x - 1],\
						"num": float(equation[x - 2])})
	return tmp

def solve_part1(equation, result):
	solve_equation = []
	for index_r in range(len(result)):
		for index_e in range(len(equation)):
			if (result[index_r]["power"] is \
				equation[index_e]["power"]):
				solve_equation.append({
						"power" : equation[index_e]["power"],\
						"operation" : equation[index_e]["operation"],\
						"num": equation[index_e]["num"] - result[index_r]["num"]
						})
			else:
				solve_equation.append(equation[index_e])
	return solve_equation
					

def print_equation(equation):
	string_equ = ""
	minus = ""
	for obj in equation:
		minus_int = 1
		if obj["num"] < 0:
			minus = " - "
			minus_int = -1
		tmp = minus \
				+ str(obj["num"] * minus_int) \
				+ " " \
				+ obj["operation"] \
				+ " " \
				+ "X^"\
				+ str(obj["power"])
		minus = " + "
		string_equ = string_equ + tmp
	print string_equ + " = 0"

if __name__ == '__main__':
	if len(sys.argv) > 1:
		equation, result = is_equation(sys.argv[1])
		print_equation(solve_part1(equation, result))



















