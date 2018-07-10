def frieze_mat3(quiddity_row=(2,1,4,2,3),leftstart = 0,width = 5,friezerow = 4, flag_rectangle=True):
    """
    def frieze_mat3(quiddity_row=(2,1,4,2,3),leftstart = 0,width = 5,friezerow = 4,   flag_rectangle=True)
    quiddity_row - give at least one complete period of the quiddity row of your frieze. The program assumes this periodicity. Give this as a list or a tuple.
    leftstart - Assuming the first entry of the inputted quiddity row exists at index (0,2), give i such that the leftmost quiddity row entry is (i,i+2).
    width - desired width of each row of the frieze when passing to the print feature
    friezerow - The index of the last row we want in the frieze.

    We begin indexing the rows of our frieze pattern at the row of all 0’s, so
    the row of 0s is at “frieze row” = 0,
    the row of 1s is at "frieze row" = 1
    and the quiddity row is at "frieze row"=2
    
    Return a dictionary of frieze patterns indexed by (i,j)
    following the convention of Gunawan-Musiker-Volgel: Cluster Algebraic Interpretations of Inifinite Friezes
    To view the frieze patterns as a matrix, do:
    matrix(frieze_ma3t())


    """
    n=len(quiddity_row)
    if leftstart < 0:
    	leftstart = Integer(mod(leftstart,n))    
    m=dict()
 #   inputcol = Integer(mod((leftstart + 1),n))
  #  print inputcol


    if flag_rectangle: # not working yet (I want to have a rectangle shape and not triangle)
       matrixwidth  = friezerow + width
   
 # Fill in 0s at position (1,1), (2,2), (3,3), until (inputrow,inputrow)
    # i.e. we fill in the quiddity row (repeated), the "frieze row" after the row of 1s.
    #print '\n'

    for col in range(matrixwidth-1):
        if m.has_key((col,col)):
            raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col,col)))
        m[(col,col)]=0
        #print m[(col,col)]
	#print (col, col)

    # Fill in the 1s at position (i,j) where |i - j| = 1 until (inputrow,inputrow +/- 1)
    # i.e. we fill in the "frieze row" =2
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
    #    print m[(col-1,col)]
	#print (col-1, col)
   
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

    # Fill in the rest of the "frieze rows" below the quiddity row
    #print '\n'
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

def print_frieze(quiddity_row=(2,1,4,2,3),leftstart = 0,width = 5,friezerow = 4,flag_rectangle=True):
  """
  def print_frieze(quiddity_row=(2,1,4,2,3),leftstart = 0,width = 5,friezerow = 4,flag_rectangle=True)
  quiddity_row - give at least one complete period of the quiddity row of your frieze. The program assumes this periodicity. Give this as a list or a tuple.
    leftstart - Assuming the first entry of the inputted quiddity row exists at index (0,2), give i such that the leftmost quiddity row entry is (i,i+2).
    width - desired width of each row of the frieze 
    friezerow - The index of the last row we want in the frieze.
	Note - if frieze row is greater than the total number of rows of the frieze pattern, the program will simply print the entire frieze pattern and nothing additional. 

    We begin indexing the rows of our frieze pattern at the row of all 0’s, so
    the row of 0s is at “frieze row” = 0,
    the row of 1s is at "frieze row" = 1
    and the quiddity row is at "frieze row"=2

    The purpose of this function is to output code that will display the frieze pattern. Use view(print_frieze()) to see the frieze. It should also work on Latex??
  """
    m = frieze_mat3(quiddity_row,leftstart,width,friezerow,flag_rectangle)
 #   Create a list with all the entries we will put into the frieze pattern.
    L = []
 #   ones = []
 #   for k in range(0,width): # fill in 1s
 #       ones.append(1)
  #  L.append(ones)
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
    print L

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