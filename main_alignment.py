import global_space_efficient
import global_base
import fitting_space_efficient
import fitting_base
import local_space_efficient
import local_base

keys = ['A', 'C', 'T', 'G', '-']
delta = {}
for i in range(len(keys)):
    delta[keys[i]] = {k : v for (k,v) in zip(keys, [1 if keys[i] == keys[j]  else -1 for j in range(len(keys))])}
    
# Call global alignment function 
def global_alignment(v, w):
    (va, wa) = global_space_efficient.get_alignment(v, w, global_space_efficient.hirschberg(v, w, delta))
    print(va, wa)

# Call fitting alignment function 
def fitting_alignment(v, w):
    (va, wa) = fitting_space_efficient.fitting(v, w, delta)
    print(va, wa)

# Call local alignment function 
def local_alignment(v, w):
    (va, wa) = local_space_efficient.local(v, w, delta)
    print(va, wa)