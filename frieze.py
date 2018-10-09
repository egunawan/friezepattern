from math import sqrt
from sage.matrix.all import matrix
from sage.misc.functional import det

def frieze_dict_diag(diag = [1,1,1],width = 6):
    """
    def frieze_dict_diag(diag = [1,1,1],width = 6)
    diag - give one diagonal of the nontrivial part of a frieze pattern. This will be the leftmost diagonal of the output.
    WARNING - we assume you did not include the border rows of 0's and 1's in this diagonal.
    WARNING - we assume this is the diagonal of a valid frieze pattern. We test to verify that this diagonal should generate a positive integer frieze. 
    WARNING - inputting 0's or a mix of positive and negative integers may result in a computation that involves dividing by 0.
    width - desired width of each row of the frieze when passing to the print feature. Each row will have equal width. This could also be viewed as the number of diagonals produced
    In order to achieve this width, the dictionary will include extra entries, creating partial diagonals past the width quantity of full diagonals. 
    
    Return a dictionary of frieze patterns indexed by (i,j)
    following the convention of Gunawan-Musiker-Volgel: Cluster Algebraic Interpretations of Inifinite Friezes
    
    We assume the diagonal goes from the North-West to the South-East. 
    
    To view as matrix, as in Bessenrodt-Holm-Jorgensen, use matrix(frieze_dict_diag())

    """
  
    n=len(diag) 
    m=dict()
    friezerow = n + 3
    matrixwidth  = friezerow + width - 1
    leftstart = 0
    
    if (diag[1] + 1)% diag[0] != 0:
    	print(' This is not the diagonal of a positive integer frieze pattern. Recheck position 0')
    for i in range(n-2):
        if (diag[i+2] + diag[i]) % diag[i+1] != 0:
            print(' This is not the diagonal of a positive integer frieze pattern. Recheck position {}'.format(i))
    if (1+diag[n-2])% diag[n-1] != 0:
    	print(' This is not the diagonal of a positive integer frieze pattern. Recheck position {}'.format(n))

   
    # Fill in 0s at position (1,1), (2,2), (3,3), until (inputrow,inputrow)
    # i.e. we fill in the quiddity row (repeated), the "frieze row" after the row of 1s.
    #print '\n'

    for col in range(matrixwidth+1):
        if m.has_key((col,col)):
            raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col,col)))
        m[(col,col)]=0
    m[(0,n+3)] = 0
    m[(n+3,0)] = 0

    # Fill in the 1s at position (i,j) where |i - j| = 1 until (inputrow,inputrow +/- 1)
    for col in range(1,matrixwidth+1):
        if m.has_key((col,col-1)):
            raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col,col-1)))
        m[(col,col-1)]=1
        #print m[(col,col-1)]
        #print (col,col-1)
    for col in range(1,matrixwidth+1):
        if m.has_key((col-1,col)):
            raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col-1,col)))
        m[(col-1,col)]=1
        #print m[(col-1,col)]
	 #print (col-1, col)
   
    #Fill in diagonal of frieze in first row and column of matrix
    for col in range(0,n):
        if m.has_key((col+2,0)):
	    raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col+2,0)))
        m[(col+2,0)]=diag[col]
        #print m[(col+2,col)]
        if m.has_key((0,col+2)):
	    raise ValueError('There is a bug. This key {} should not have been assigned.'.format((0,col+2)))
        m[(0,col+2)]=diag[col]
        #print m[(col+2,col)]
    m[(n+2,0)] = 1
    m[(0,n+2)] = 1


    # Fill in the rest of the "frieze rows" using the diamond relation
    
    for row in range(1,matrixwidth-friezerow+1):
        m[(friezerow+row, row)] = 0
        m[(row, friezerow+row)] = 0
    for row in range(1, matrixwidth+1):
    	for col in range(2,min(friezerow, matrixwidth-row+1)):
            i,j=row,col+row
            if m.has_key((i,j)):
                raise ValueError('There is a bug. This key {} should not exist'.format((i,j)))
            m[(i,j)] = (m[(i,(j-1))]*m[(i-1,j)]+1)/m[(i-1,(j-1))]
            if type(m[(i,j)]) == type(sqrt(2)):
                m[(i,j)] = m[(i,j)].full_simplify()
	for col in range(2,min(friezerow, matrixwidth - row + 1)):
            i,j=col+row,row
            if m.has_key((i,j)):
                raise ValueError('There is a bug. This key {} should not exist'.format((i,j)))
            m[(i,j)] = (m[((i-1),j)]*m[(i,(j-1))]+1)/m[((i-1),(j-1))]
            if type(m[(i,j)]) == type(sqrt(2)):
                m[(i,j)] = m[(i,j)].full_simplify()
    return m


def frieze_dict_quid(quiddity_row=(2,1,4,2,3),leftstart = 0,width = 5,friezerow = 4, flag_rectangle=True):
    """
    def frieze_dict_quid(quiddity_row=(2,1,4,2,3),leftstart = 0,width = 5,friezerow = 4,   flag_rectangle=True)
    quiddity_row - give at least one complete period of the quiddity row of your frieze. The program assumes this periodicity. Give this as a list or a tuple.
    leftstart - Assuming the first entry of the inputted quiddity row exists at index (0,2), give i such that the leftmost quiddity row entry is (i,i+2).
    width - desired width of each row of the frieze when passing to the print feature
    friezerow - The index of the last row we want in the frieze.

    We begin indexing the rows of our frieze pattern at the row of all 0's, so
    the row of 0s is at "frieze row" = 0,
    the row of 1s is at "frieze row" = 1
    and the quiddity row is at "frieze row"=2
    
    WARNING - inputting 0's or a mix of positive and negative integers may result in a computation that involves dividing by 0.
    
    Return a dictionary of frieze patterns indexed by (i,j)
    following the convention of Gunawan-Musiker-Volgel: Cluster Algebraic Interpretations of Infinite Friezes
    
    To view as matrix, as in Bessenrodt-Holm-Jorgensen, use matrix(frieze_dict_quid())

    """
    n=len(quiddity_row)
    if leftstart < 0:
    	leftstart = Integer(mod(leftstart,n))    
    m=dict()
    matrixwidth = friezerow + width+1
  
   #Check whether quiddity row could produce finite frieze pattern, using check as in Morier-Genoud's paper https://arxiv.org/abs/1503.05049 although originally in Coxeter's original frieze pattern paper.
   #We make continuants in terms of quiddity row entries. Given a quiddity sequence of length n, These will check whether rows n-1 and n are boundary rows. 
   #Of course, as in the case of 3,1,3,1,3,1, one could just input quiddity_row = (3,1), which will give the right frieze pattern but will fail this test. 
    checkdict1 = dict()
    checkdict2 = dict()
    checkdict3 = dict()
    for i in range(n-1):
        checkdict1[(i,i)] = quiddity_row[i]
        checkdict2[(i,i)] = quiddity_row[i+1]
    for i in range(n-2):
        checkdict1[(i,i+1)] = 1
        checkdict1[(i+1,i)] = 1
        checkdict2[(i,i+1)] = 1
        checkdict2[(i+1,i)] = 1
        checkdict3[(i,i)] = quiddity_row[i+1]
    for i in range(n-3):
        checkdict3[(i,i+1)] = 1
        checkdict3[(i+1,i)] = 1   
    check1 = matrix(checkdict1)
    check2 = matrix(checkdict2)
    check3 = matrix(checkdict3)
    if det(check1) != 0 or det(check2)!= 0 or det(check3)!= 1:
            print('This is not the quiddity row of a finite frieze pattern, although it could be subsequence of a periodic quiddity row which does produce a finite frieze pattern')

   

    # Fill in 0s at position (1,1), (2,2), (3,3), until (inputrow,inputrow)
    #i.e. we fill in the "frieze row" = 0
    for col in range(matrixwidth-1):
        if m.has_key((col,col)):
            raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col,col)))
        m[(col,col)]=0
        #print m[(col,col)]
	#print (col, col)

    # Fill in the 1s at position (i,j) where |i - j| = 1 until (inputrow,inputrow +/- 1)
    # i.e. we fill in the "frieze row" =1
    for col in range(1,matrixwidth):
        if m.has_key((col,col-1)):
            raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col,col-1)))
        m[(col,col-1)]=1
      #  print m[(col,col-1)]
        #print (col,col-1)
    for col in range(1,matrixwidth):
        if m.has_key((col-1,col)):
            raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col-1,col)))
        m[(col-1,col)]=1

   
    #Fill in quiddity row for (i,j) where |i - j| = 2
    for col in range(0,matrixwidth-2):
        if m.has_key((col+2,col)):
	    raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col+2,col)))
        m[(col+2,col)]=quiddity_row[((col+leftstart) % n)]
        #print m[(col+2,col)]
    for col in range(0,matrixwidth-2):
        if m.has_key((col,col+2)):
            raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col,col+2)))
        m[(col,col+2)]=quiddity_row[(col+leftstart)%n]

    # Fill in the rest of the "frieze rows" below the quiddity row using the quiddity row
    for row in range(3, matrixwidth-(leftstart+1)):
        for col in range(0,matrixwidth-row):
            i,j=col,col+row
            if m.has_key((i,j)):
                raise ValueError('There is a bug. This key {} should not exist'.format((i,j)))
            if m[(i+1,j-1)]<1:
                break
            #print (i,(j-1)%n+1)
            #print (i+1,j%n+1)
            #print m.keys()
            m[(i,j)] = (m[(i,(j-1))]*m[(i+1,j)]-1)/m[(i+1,(j-1))]
            if type(m[(i,j)]) == type(sqrt(2)):
                m[(i,j)] = m[(i,j)].full_simplify()
            #print m[(i,j)]
	for col in range(0,matrixwidth-row):
            i,j=col+row,col
            if m.has_key((i,j)):
                raise ValueError('There is a bug. This key {} should not exist'.format((i,j)))
            if m[(i-1,j+1)]<1:
                break
            #print (i,(j-1)%n+1)
            #print (i+1,j%n+1)
            #print m.keys()
            m[(i,j)] = (m[((i-1),j)]*m[(i,(j+1))]-1)/m[((i-1),(j+1))]
            if type(m[(i,j)]) == type(sqrt(2)):
                m[(i,j)] = m[(i,j)].full_simplify()
            #print m[(i,j)]
        if m[(leftstart+row,leftstart)]<1:
            break
        #print '\n'
    return m

def print_frieze(inputtype = 'quid', input_row=(2,1,4,2,3),leftstart = 0,width = 5, friezerow = 4,flag_rectangle=True):
    """
    def print_frieze(inputtype = 'quid', input_row=(2,1,4,2,3),leftstart = 0,width = 5,friezerow = 4,flag_rectangle=True)
    inputtype - for now write 'quid' or 'quiddity' if the input is a quiddity row, and 'diag' or 'diagonal' is the input is a diagonal. Must input as a string.
    input_row - give at least one complete period of the quiddity row of your frieze or give one diagonal of your frieze. Give this as a list or a tuple.
    leftstart - Only applicable if inputtype = 'quid'. Assuming the first entry of the inputted quiddity row exists at index (0,2), give i such that the leftmost quiddity row entry is (i,i+2).
    width - desired width of each row of the frieze 
    friezerow - Only applicable if inputtype = 'quid'. The index of the last row we want in the frieze. Note we consider the quiddity row to be friezerow = 2.
    Note - if frieze row is greater than the total number of rows of the frieze pattern, the program will simply print the entire frieze pattern and nothing additional. 

    We begin indexing the rows of our frieze pattern at the row of all 0's, so
    the row of 0s is at "frieze row" = 0,
    the row of 1s is at "frieze row" = 1
    and the quiddity row is at "frieze row"=2

    The purpose of this function is to output code that will display the frieze pattern. Use view(print_frieze()) to see the frieze. The output should be ready to be put into a latex document.
    """
    if inputtype == 'quid' or inputtype == 'quiddity':
        m = frieze_dict_quid(input_row,leftstart,width,friezerow,flag_rectangle)
    elif inputtype == 'diag' or inputtype == 'diagonal':
        m = frieze_dict_diag(input_row, width)
        friezerow = len(input_row) + 4
    else:
        m = dict()
        width = 0
        friezerow = 0
        print 'Invalid input type. If your input is the quiddity row, use inputtype = quid or quiddity (with quotes) If your input is a diagonal, use inputtype = diag or diagonal (with quotes). Other input types are not currently accepted.'
        

    #   Create a list with all the entries we will put into the frieze pattern.
    L = []
    for row in range(0,friezerow):
        li = []
        for col in range(0, width):
            i,j = col, col+row
            if m.has_key((i,j)):
                li.append(m[(i,j)])
                #print m[(i,j)]
            else:
                break
        L.append(li)
    #for i in range(len(L)):
    #    print('  '*i, L[i])

    ret = ""
    for i,row in enumerate(L):
       # ret += ' '*i*2 + ' '.join('%3s'%x for x in row)
        ret += ' '*i*2 + ' '.join("{:>3}".format(x) for x in row)
        ret += '\n'
	#The following may be useful for infinite friezes arising from punctured polygons. This inserts a dashed line after every n = len(quiddity row), so that all entries in the same compartment, defined by these dashed lines, corresponds to an arc in the punctured polygon with the same number of self-crossings. The uppermost compartment corresponds to arcs with no self-crossings.
       # if (i+1)%len(quiddity_row)==0:
       #     ret += ' '*i*2 + '  '
       #     ret += '--'*friezerow + '\n'
        #ret +='\n'

    return ret[:-1]


#print matrix(frieze_mat()).transpose()

# sage: matrix(frieze_mat((2,1,3),inputrow=15)).transpose() # type A3