import matplotlib.mlab as ml
import numpy as np
def get_sightings(filename,ani):
    
    tab=ml.csv2rec(filename)
    ani=ani.capitalize()
    print tab ['animal']
    isfocus=(tab[ 'Animal' ] == ani)
    total_rec=np.sum(isfocus)

   if total_rec == 0:
        meancount=0

   else:
        meancount=np.mean(tab[ 'count' ][isfocus])

