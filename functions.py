import numpy as np
import numpy.linalg as la

def save_tex(var,name):
    """
    Save var as LaTeX variable by printing it out (will be saved into a file by
    shell).

    Parameters
    ----------
    var : *
        The varaible (must be printable) to save.
    name : str
        What name to give the variable in LaTeX.
    """
    print('\\gdef\%s'%(name),'{',var,'}',sep='')

def matrix_multiply(A,B,out="C"):
    """
    Matrix multiplication A*B=C.

    Parameters
    ----------
    A : 2D list
        Left matrix.
    B : 2D list
        Right matrix.
    out (optional) : str
        The name to give the result in LaTeX.
    """
    A = np.array(A)
    B = np.array(B)
    C = (A.dot(B)).tolist()
    save_tex(C,out)

def matrix_inverse(A,out="Ainv"):
    """
    Matrix inverse of A^-1=Ainv.

    Parameters
    ----------
    A : 2D list
        Matrix to invert.
    out (optional) : str
        The name to give the result in LaTeX.
    """
    A = np.array(A)
    Ainv = (la.inv(A)).tolist()
    save_tex(Ainv,out)

def matrix_add(A,B,out="C"):
    """
    Add matrices A+B=C.

    Parameters
    ----------
    A : 2D list
        Left matrix.
    B : 2D list
        Right matrix.
    out (optional) : str
        The name to give the result in LaTeX.
    """
    A = np.array(A)
    B = np.array(B)
    C = (A+B).tolist()
    save_tex(C,out)
