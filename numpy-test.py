try:
    import numpy as np
except:
    print('Numpy isn\'t installed...')
    exit()

if __name__ == "__main__":
    print(f'The Numpy version is: {np.__version__}.')
