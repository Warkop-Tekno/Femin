pellet = {}
clad = {}
dish = {}
chamfer = {}
plenum = {}
gap = {}


def create_pellet(inner_dia, outer_dia, length, den, enrch, l_node, weight = 0):
	pellet['id'] = inner_dia	 # cm
	pellet['od'] = outer_dia	 # cm
	pellet['l_pellet'] = length		 # cm
	pellet['den'] = den			 # Pellet theoretical density ratio
	pellet['enrch'] = enrch
	pellet['l_node'] = l_node			 # Axial segment length of pellet stack (cm)
	if (weight>0):
		pellet['weight'] = weight

def create_clad(mat_clad, inner_dia, outer_dia):
	clad['id'] = inner_dia		# cm
	clad['od'] = outer_dia		# cm
	clad['mat'] = mat_clad		# Cladding material, 0 = RA mat, 1 = SR mat


def create_dish(dia, depth, bot_dia):
	dish['dia'] = dia 		# cm
	dish['dep'] = depth 	# cm
	dish['bot'] = bot_dia 	# cm


def create_chamfer(width, depth):
	chamfer['wid'] = width	 # cm
	chamfer['dep'] = depth	 # cm


def create_plenum(up_vol, low_vol):
	plenum['up vol'] = up_vol	 # cm^3
	plenum['low vol'] = low_vol			 # cm^3


def create_gap(init_gas_pressure, comp_He, comp_N2, comp_Kr, comp_Xe):
	gap['init gas pressure'] = init_gas_pressure	 # MPa
	gap['init He comp'] = comp_He
	gap['init N2 comp'] = comp_N2
	gap['init Kr comp'] = comp_Kr
	gap['init Xe comp'] = comp_Xe

