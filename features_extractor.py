import javalang
import re


def ratio_calc(a, b):
    if not a and not b:
        return 0.5
    elif not a:
        return 0.0
    elif not b:
        return 1.0
    else:
        return len(a) / (len(a) + len(b))


def extract(file):
    # TODO: try catch for open
    # file = open(filename).read()
    lines = file.split('\n')
    tree = javalang.parse.parse(file)

    num_lines = len(lines)

    empty_lines = 0
    for line in lines:
        if not line.strip():
            empty_lines += 1

    avg_len_lines = len(file) / num_lines

    # TODO: # line comment
    # TODO: avg len line comment
    # TODO: # punctuation in line comment

    # TODO: # block comment
    # TODO: # javadoc comment

    variables = ([node.name for path, node
                  in tree.filter(javalang.tree.VariableDeclarator)])
    num_variables = len(variables)
    if num_variables:
        avg_len_variables = len(''.join(variables)) / num_variables
    else:
        avg_len_variables = 0

    num_if = len(list(tree.filter(javalang.tree.IfStatement)))

    num_for = len(list(tree.filter(javalang.tree.ForStatement)))

    num_do = len(list(tree.filter(javalang.tree.DoStatement)))

    num_while = len(list(tree.filter(javalang.tree.WhileStatement)))

    num_switch = len(list(tree.filter(javalang.tree.SwitchStatement)))

    num_cast = len(list(tree.filter(javalang.tree.Cast)))

    # TODO: cyclomatic complexity

    # "if(":"if ("
    cond_no_space = re.findall(r'(?:(?:if)|(?:for)|(?:while)|(?:do))\(', file)
    cond_space = re.findall(r'(?:(?:if)|(?:for)|(?:while)|(?:do)) \(', file)
    cond_space_ratio = ratio_calc(cond_no_space, cond_space)

    # "){ or ) {":")\n{"
    bracket_same_line = re.findall(r'\) *\t*\{', file)
    bracket_new_line = re.findall(r'\) *\t*\n *\t*\{', file)
    bracket_line_ratio = ratio_calc(bracket_same_line, bracket_new_line)

    # number of space excluding indentation
    num_space = 0
    for line in lines:
        num_space += line.strip().count(' ')

    return [
        num_lines,
        empty_lines,
        avg_len_lines,
        num_variables,
        avg_len_variables,
        num_if,
        num_for,
        num_do,
        num_while,
        num_switch,
        num_cast,
        cond_space_ratio,
        bracket_line_ratio,
        num_space
    ]


if __name__ == '__main__':
    print(extract('../files/set40/1rn18cs078racha1.java'))
