import numpy as np
import sys
from time import time


sys_args = sys.argv[1:]

if not sys_args:
    # Verify if has any arguments
    print('Please insert one of these arguments:\n'
          '\t\033[1mshow, not_show\033[m')
    exit()
else:
    # Verify if the argument is correct
    if not sys_args[0] in ('show', 'not_show'):
        print('Wrong argument!')
        exit()


if __name__ == "__main__":
    ## Normal array ##
    timer = time()
    normal_array = [ i for i in range(0, 5_000_000) ] # Create the list

    ## Show list if its digited show in the final
    if sys_args[0] == 'show':
        print(normal_array)

    final_time = time() - timer
    print(f'Final time for normal array: {final_time:.2f}')

    ## Numpy array ##
    timer = time()
    numpy_array = np.array([ i for i in range(0, 5_000_000) ]) # Create the list

    ## Show list if its digited show in the final
    if sys_args[0] == 'show':
        print(numpy_array)

    final_time = time() - timer
    print(f'Final time for Numpy array: {final_time:.2f}')
