# friezepattern
Return a frieze pattern (finite or infinite) by specifiying the quiddity row, that is, the row right after the row of all 0s and all 1s.

### Depending on the given quiddity row, the frieze will be finite or infinite.
If a "frieze row" contains a zero, the computation stops there.
Otherwise, user specifies which row they would like to stop at.

### Examples
sage: matrix(frieze_mat((2,1,4,2,3),inputrow=15)).transpose() # From once-punctured pentagon trianguation

[ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]

[ 0  2  1  0  0  0  0  0  0  0  0  0  0  0  0  0]

[ 0  1  1  1  0  0  0  0  0  0  0  0  0  0  0  0]

[ 0  2  3  4  1  0  0  0  0  0  0  0  0  0  0  0]

[ 0  3  5  7  2  1  0  0  0  0  0  0  0  0  0  0]

[ 0  7 12 17  5  3  1  0  0  0  0  0  0  0  0  0]

[ 0 11 19 27  8  5  2  1  0  0  0  0  0  0  0  0]

[ 0  4  7 10  3  2  1  1  1  0  0  0  0  0  0  0]

[ 0  5  9 13  4  3  2  3  4  1  0  0  0  0  0  0]

[ 0  6 11 16  5  4  3  5  7  2  1  0  0  0  0  0]

[ 0 13 24 35 11  9  7 12 17  5  3  1  0  0  0  0]

[ 0 20 37 54 17 14 11 19 27  8  5  2  1  0  0  0]

[ 0  7 13 19  6  5  4  7 10  3  2  1  1  1  0  0]

[ 0  8 15 22  7  6  5  9 13  4  3  2  3  4  1  0]

[ 0  9 17 25  8  7  6 11 16  5  4  3  5  7  2  1]

sage: matrix(frieze_mat((2,1,3),inputrow=15)).transpose() # type A3

[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]


[0 2 1 0 0 0 0 0 0 0 0 0 0 0 0 0]

[0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0]

[0 1 2 3 1 0 0 0 0 0 0 0 0 0 0 0]

[0 1 3 5 2 1 0 0 0 0 0 0 0 0 0 0]

[0 0 1 2 1 1 1 0 0 0 0 0 0 0 0 0]

[0 0 0 1 1 2 3 1 0 0 0 0 0 0 0 0]

[0 0 0 0 1 3 5 2 1 0 0 0 0 0 0 0]

[0 0 0 0 0 1 2 1 1 1 0 0 0 0 0 0]

[0 0 0 0 0 0 1 1 2 3 1 0 0 0 0 0]

[0 0 0 0 0 0 0 1 3 5 2 1 0 0 0 0]

[0 0 0 0 0 0 0 0 1 2 1 1 1 0 0 0]

[0 0 0 0 0 0 0 0 0 1 1 2 3 1 0 0]

[0 0 0 0 0 0 0 0 0 0 1 3 5 2 1 0]

[0 0 0 0 0 0 0 0 0 0 0 1 2 1 1 1]

