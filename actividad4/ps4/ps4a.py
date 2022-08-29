 # Problem Set 4A
# Name: Rafael Santiago Suárez Gil
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    palabra_act=""
    regreso=[]
    if len(sequence)==1:#Caso base 1
        return[sequence]
    elif len(sequence)==2:#caso base 2
        regreso.extend([sequence])
        palabra_act=sequence[1]+sequence[0]
        if not palabra_act in regreso:
            regreso.extend([palabra_act])
        return regreso
    else:#caso recursivo
        resto=sequence[1:len(sequence)]
        for A in get_permutations(resto):
            maxim=len(A)+1
            for B in range(maxim):
                if B==0:
                    palabra_act=sequence[0]+A
                    if not palabra_act in regreso:
                        regreso.extend([palabra_act])
                elif B==maxim:
                    palabra_act=A+sequence[0]
                    if not palabra_act in regreso:
                        regreso.extend([palabra_act])
                else:
                    palabra_act=A[0:B]+sequence[0]+A[B:len(A)]
                    if not palabra_act in regreso:
                        regreso.extend([palabra_act])
        return regreso        
        
        
        
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)



