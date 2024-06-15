import numpy as np
import sys
from time import time

sys_args = sys.argv

if __name__ == "__main__":
    ## Normal array ##
    timer = time()
    normal_array = [ i for i in range(0, 5_000_000) ] # Create the list

    ## Show list if its digited show in the final
    if sys_args[-1] == 'show':
        print(normal_array)

    final_time = time() - timer
    print(f'Final time for normal array: {final_time:.2f}')

    ## Numpy array ##
    timer = time()
    numpy_array = np.array([ i for i in range(0, 5_000_000) ]) # Create the list

    ## Show list if its digited show in the final
    if sys_args[-1] == 'show':
        print(numpy_array)

    final_time = time() - timer
    print(f'Final time for Numpy array: {final_time:.2f}')
