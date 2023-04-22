def arithmetic_arranger(problems, default=False):
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
            if operator in mult_div:
                return("Error: Operator must be '+' or '-'.")
            else:
                if a.isdigit() and b.isdigit():
                    pass
                else:
                    return("Error: Numbers must only contain digits.")
    arranged_problems=str_a.rstrip()+str_b.rstrip()+str_delimeter.rstrip()+str_result.rstrip()
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))

