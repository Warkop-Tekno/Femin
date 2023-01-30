clad = {}

def create_clad(inner_dia, outer_dia, mat_clad):
    global clad
    clad['id'] = inner_dia
    clad['od'] = outer_dia
    clad['mat'] = mat_clad

def get_clad():
    return clad