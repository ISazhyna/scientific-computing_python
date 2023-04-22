def arithmetic_arranger(problems, default=False):
    #TODO: more than 5 problems
    if len(problems)>5:
        return("Error: Too many problems.")
    else:
        mult_div=["*", "/"]

        #empty rows
        str_a = ""
        str_b = "\n"
        str_delimeter = "\n"
        str_result = "\n"

        # Split problems into their components
        for each in problems:
            a, operator, b = each.split(' ')
            #TODO: only addition and subtraction
            if operator in mult_div:
                return("Error: Operator must be '+' or '-'.")
            else:
                if a.isdigit() and b.isdigit():
                    if len(a) <= 4 and len(b) <= 4:
                        if default == True:
                            result = int(a) + int(operator + b)
                        else:
                            result = ""
                        # Calc how many digits is one problem, add 2 places for an operator and a whitespace
                        max_len = max(len(a), len(b)) + 2
                        str_a = str_a + '{:>{max_len}}'.format(a, max_len=max_len) + " " * 4
                        str_b = str_b + operator + " " + '{:>{max_len}}'.format(b, max_len=max_len - 2) + " " * 4
                        str_delimeter = str_delimeter + "-" * max_len + " " * 4
                        str_result = str_result + '{:>{max_len}}'.format(result, max_len=max_len) + " " * 4
                    else:
                        #TODO: no more than 4 digits
                        return ("Error: Numbers cannot be more than four digits.")
                else:
                    #TODO: only digits
                    return("Error: Numbers must only contain digits.")
    arranged_problems=str_a.rstrip()+str_b.rstrip()+str_delimeter.rstrip()+str_result.rstrip()
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))

