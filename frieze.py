

def frieze_mat(quiddity_row=(2,1,4,2,3),inputcol=1,inputrow=8):
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
    # Fill in the 1s at position (2,1), (3,2), (4,3), until (inputrow,inputrow-1)
    # i.e. we fill in the "frieze row"=0
    for col in range(2,inputrow+1):
        if m.has_key((col,col-1)):
            raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col,col-1)))
        m[(col,col-1)]=1
        #print m[(col,col-1)]
    # Fill in the values at position (1,1), (2,2), (3,3), until (inputrow,inputrow)
    # i.e. we fill in the quiddity row (repeated), the "frieze row" after the row of 1s.
    #print '\n'
    for col in range(1,inputrow):
        if m.has_key((col,col)):
            raise ValueError('There is a bug. This key {} should not have been assigned.'.format((col,col)))
        m[(col,col)]=quiddity_row[(col % n)-1] # Python index starts at 0, hence minus 1
        #print m[(col,col)]
    # Fill in the rest of the "frieze rows" below the quiddity row
    #print '\n'
    for friezerow in range(1, inputrow-inputcol):
        for col in range(inputcol,inputrow-friezerow):
            i,j=col,col+friezerow
            if m.has_key((i,j)):
                raise ValueError('There is a bug. This key {} should not exist'.format((i,j)))
            if m[(i+1,j-1)]<1:
                break
            m[(i,j)] = (m[(i,j-1)]*m[(i+1,j)]-1)/m[(i+1,j-1)]
            #print m[(i,j)]
        if m[(inputcol,inputcol+friezerow)]<1:
            break
        #print '\n'
    return m

print matrix(frieze_mat()).transpose()

# sage: matrix(frieze_mat((2,1,3),inputrow=15)).transpose() # type A3