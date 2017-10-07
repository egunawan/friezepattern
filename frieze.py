

def frieze_mat(quiddity_row=(2,1,4,2,3),inputcol=1,inputrow=8,flag_rectangle=True):
    """
    Return a dictionary of frieze patterns indexed by (i,j)
    following the convention of Baur-Parsons-Tschabold: Inifinite Friezes
    To view the frieze patterns as a matrix, do:
    matrix(frieze_mat()).transpose()

    Note that "Frieze row"="row" - "col"
    so that the quiddity row is at "frieze row"=0
    and the row of 1s is at "frieze row" = -1
    """
    n=len(quiddity_row)
    m=dict()

    if flag_rectangle: # not working yet (I want to have a rectangle shape and not triangle)
        inputrowplusextra = inputrow * 2
    # Fill in the 1s at position (2,1), (3,2), (4,3), until (inputrow,inputrow-1)
    # i.e. we fill in the "frieze row"=0
    for col in range(2,inputrowplusextra+1):
        if m.has_key((col,col-1)):
            raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col,col-1)))
        m[(col,col-1)]=1
        #print m[(col,col-1)]
    # Fill in the values at position (1,1), (2,2), (3,3), until (inputrow,inputrow)
    # i.e. we fill in the quiddity row (repeated), the "frieze row" after the row of 1s.
    #print '\n'

    for col in range(1,inputrowplusextra):
        if m.has_key((col,col)):
            raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col,col)))
        m[(col,col)]=quiddity_row[(col % n)-1] # Python index starts at 0, hence minus 1
        #print m[(col,col)]
    # Fill in the rest of the "frieze rows" below the quiddity row
    #print '\n'
    for friezerow in range(1, inputrowplusextra-inputcol):
        for col in range(inputcol,inputrowplusextra-friezerow):
            i,j=col,col+friezerow
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
        if m[(inputcol,inputcol+friezerow)]<1:
            break
        #print '\n'
    return m

def print_frieze(quiddity_row=(2,1,4,2,3),inputcol=1,inputrow=8,flag_rectangle=True):
    m = frieze_mat(quiddity_row,inputcol,inputrow,flag_rectangle)
    L = []
    ones = []
    for k in range(0,inputrow-inputcol+1): # fill in 1s
        ones.append(1)
    L.append(ones)
    for friezerow in range(0,inputrow-inputcol):
        li = []
        for col in range(inputcol, inputrow-friezerow):
            i,j = col, col+friezerow
            if m.has_key((i,j)):
                li.append(m[(i,j)])
                #print m[(i,j)]
            else:
                break
        L.append(li)

    ret = ""
    for i,row in enumerate(L):
        #ret += ' '*i*2 + ' '.join('%3s'%x for x in row)
        ret += ' '*i*2 + ' '.join("{:>3}".format(x) for x in row)
        ret += '\n'
        if (i+1)%len(quiddity_row)==0:
            ret += ' '*i*2 + '  '
            ret += '--'*inputrow + '\n'
        #ret +='\n'

    return ret[:-1]


#print matrix(frieze_mat()).transpose()

# sage: matrix(frieze_mat((2,1,3),inputrow=15)).transpose() # type A3
