# HW 22 Tasks for figuring out O[N] solutions

## Function isSumTwo

- Takes two parameters: list of integer numbers (numbers) and one integer number (sum)<br>
- Returns True (T should be capital) if the given list (numbers) contains two items, sum of which equals the given number (sum), otherwise returns False

### Examples

- isSumTwo([1, 2, 3, 4], 4) -> True <br>
- isSumTwo([1, 2, 3, 4], 2) -> False

### Unit tests

Unit tests in a separate file (module)

## Function maxNegativeRepr

- Takes one parameter: list of integer numbers (numbers)<br>
- Returns either maximal positive number from the given list having its negative representation or -1 if no any <br>

### Examples

- maxNegativeRepr(100, 4, 1, -1, -4, -100) -> 100 <br>
- maxNegativeRepr(100, 4, 1, 1, 4, 100, -1) -> 1 <br>
- maxNegativeRepr(100, 4, 1, 1, 4, 100, 1, -2) -> -1

### Unit tests

Unit tests in a separate file (module)
