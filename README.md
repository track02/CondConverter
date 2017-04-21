# CondConverter
Simple command line tool for converting prefix-style conditionals (e.g. Scheme) to pseudocode

Copy a prefix conditional into the input.txt file and run the script, the result will be written to output.txt

Example:

`(AND A B (NOT C) (OR D (AND E F)))`

Is converted to:

`(A AND B AND (NOT C) AND (D OR (E AND F)))`


