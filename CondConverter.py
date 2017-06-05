output = ""
op_stack = []

# Three possible elements
# Start -> (Op
# Middle -> A
# End -> B)
# (Op A B)

# Whenever a start element is found, open a new bracket and push the operator to onto the stack (
# Special case for NOT) -> "("
# If a middle element is found add it along with the current operator on the stack -> "(" + "A OR"
# When an end element is found, count the number of closing brackets and pop this no. of operators from the stack
# If the end element is the final element in the list then just add it to the end "( A OR " + "B )"
# If the end element is not the final element in the list
# then add it along with the operator left on the stack "(A OR " + "B) AND "
# Open the input file and read in each line
with open("input.txt", mode="r") as fi:
    input = ("".join(fi.readlines())).replace("/", "").replace("\n", " ").split()


print("Beginning Conversion")

for item in input:

    # START
    if item.startswith("("):
        op_stack.append(item[1:])
        output = output + "("

        # If NOT, add this alongside bracket otherwise it will be skipped
        if item[1:] == "NOT":
            output = output + "{0} ".format(item[1:])

    # END
    if item.endswith(")"):

        for i in range(0, item.count(")")):
            op_stack.pop()
        if input.index(item) == (len(input) - 1):
            output = output + "{0}".format(item)
        else:
            output = output + "{0} {1} ".format(item, op_stack[-1:][0])

    # MIDDLE
    if (item.count("(") + item.count(")")) == 0:
        output = output + "{0} {1} ".format(item, op_stack[-1:][0])


with open("output.txt", mode="w") as fo:
    fo.writelines(output)

print("Finished Conversion")
