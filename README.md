# friezepattern
Return a frieze pattern (finite or infinite) by specifiying the quiddity row , that is, the row right after the row of all 0s and all 1s, or a complete diagonal. Also gives options to customize the output. If the user inputs a quiddity row, he/she can specify which frieze row to print to, the width of the rows, and which quiddity row item should define the leftmost diagonal. If the user inputs a diagonal, he/she can specify the width of the rows. In this case, the program will print all the rows, at the desired width.

### Depending on the given quiddity row, the frieze will be finite or infinite.
Computation checks whether the quiddity row is likely to produce a finite frieze. However, this method is not perfect. For example, it will print a message if you input quiddity row [3,1] or [3,1,3,1] but not if you input a quiddity row [3,1,3,1,3,1]. This is because we can find a polygon triangulation of a hexagon such that the number of triangles at each vertex, ordered in a cyclic way, is 3,1,3,1,3,1, but we cannot do this for a quadrilateral, and we cannot even triangulate a bigon. 

If a "frieze row" contains a zero, the computation stops there.
Otherwise, user specifies which row they would like to stop at.

### Depending on the given diagonal, the frieze may contain (non-integer) rational numbers.
Computation checks whether this will be the case.
Note that the function assumes the user did not include the 1's from the border rows in the diagonal.

### How to use from terminal:
1. Open Sage in terminal.
2. Type: 
    `attach('path-to-folder/friezepattern/frieze.py')`
3. Alternatively, copy-all the frize.py file and paste into the terminal by typing 
   `%paste`

### How to use from notebook like Jupyter or sage math cloud (CoCalc):
    Copy-all the frize.py file and paste

### Examples for viewing the frieze pattern the usual way
    sage: print_frieze((1,2,4,1,2,2,3),inputrow=14)
      1   2   4   1   2   2   3   1   2   4   1   2   2
        1   7   3   1   3   5   2   1   7   3   1   3
          3   5   2   1   7   3   1   3   5   2   1
            2   3   1   2   4   1   2   2   3   1
              1   1   1   1   1   1   1   1   1
                0   0   0   0   0   0   0   0

    sage: print_frieze((3,1,3),inputrow=20)
      3   1   3   3   1   3   3   1   3   3   1   3   3   1   3   3   1   3   3
        2   2   8   2   2   8   2   2   8   2   2   8   2   2   8   2   2   8
          3   5   5   3   5   5   3   5   5   3   5   5   3   5   5   3   5
            7   3   7   7   3   7   7   3   7   7   3   7   7   3   7   7
              4   4  16   4   4  16   4   4  16   4   4  16   4   4  16
                5   9   9   5   9   9   5   9   9   5   9   9   5   9
                 11   5  11  11   5  11  11   5  11  11   5  11  11
                    6   6  24   6   6  24   6   6  24   6   6  24
                      7  13  13   7  13  13   7  13  13   7  13
                       15   7  15  15   7  15  15   7  15  15
                          8   8  32   8   8  32   8   8  32
                            9  17  17   9  17  17   9  17
                             19   9  19  19   9  19  19
                               10  10  40  10  10  40
                                 11  21  21  11  21
                                   23  11  23  23
                                     12  12  48
                                       13  25
                                         27

### Examples for viewing the frieze pattern as a matrix (where the main diagonal gives the quiddity row)
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

### References:
####2015:
1. http://arxiv.org/abs/1504.02695
2. http://arxiv.org/abs/1503.04352

####1970s:
http://www.link.cs.cmu.edu/15859-s11/notes/frieze-patterns-gazette.pdf
