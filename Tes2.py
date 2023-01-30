import femin

## Geometry
node = 10   # Max 40
obj_seg = 5

# Pellet Specification
inner_diameter_pellet = [0.0] * node # cm
outer_diameter_pellet = [0.820] * node # cm
p_pelet = [1.0]*node # cm
enrichment_pellet = [0.04] * node
density_pellet = [0.97] * node # Theorical Density Ratio
ax_pelet = [10.0]*node  # panjang pada tiap 10 segment
#weight_pellet = 550  # gram
femin.create_pellet(obj_seg, inner_diameter_pellet, outer_diameter_pellet, p_pelet, \
                    density_pellet, enrichment_pellet, ax_pelet)#, weight_pellet)


# Cladding Specification
id_clad = 0.83 # cm
od_clad = 0.97 # cm
mat_clad = 0  # 0 = RA Material, 1 = SR Material
femin.create_clad(mat_clad, id_clad, od_clad)


# Dish Specification
dish_dia = 0.6 # cm
dish_depth = 0.02 # cm
dish_botDia = 0.6 # cm
femin.create_dish(dish_dia, dish_depth, dish_botDia)


# Plenum Specification
up_plenum = 5 # cm^3
low_plenum = 5 # cm^3
femin.create_plenum(up_plenum, low_plenum)


# Gap Specification
gas_pressure = 1 # MPa
He_comp = 0.94     # %
Xe_comp = 0.01     # %
Kr_comp = 0.03     # %
N2_comp = 0.02     # %
femin.create_gap(gas_pressure, He_comp, N2_comp, Kr_comp, Xe_comp)


## History Data
# Relative Power Profile
ax1 = [.62, .865, 1, 1.149, 1.19, 1.163, 1.005, .931, .786, .541]           # 8
ax2 = [.656, .903, 1.098, 1.167, 1.201, 1.174, 1.073, .959, .817, .581]     # 8
femin.create_pf([ax1, ax2])


# Power History Data
time = []*16 # Hour
burnup = [    0,    10, 15000, 20000, 25000, 28000, 30000, 30500,\
          30501, 30510, 35000, 40000, 42000, 46000, 49000, 50000]       # MWd/tU

lin_heatrate = [.01, 114.5, 250, 270, 290, 270, 260, 100,\
                  1,   100, 200, 220, 210, 205, 190, 180]           #W/cm

cool_temp = [558.15]*16     # Kelvin
cool_pressure = [15.4]*16  # MPa
cool_velocity = [3.04]*16   # m/s
fast_nFlux = []*16   # n/cm^2 s
IT = []*16 # # 1 ON, 0 OFF
IP = [1, 0, 0, 0, 1, 1, 0, 1,\
      1, 0, 1, 0, 1, 0, 1, 1]          # 1 ON, 0 OFF
IS = []*16 # # 1 ON, 0 OFF

# Create history data
femin.create_time_hist(time)
femin.create_bu_hist([burnup[:8], burnup[8:16]])
femin.create_lhr_hist([lin_heatrate[:8], lin_heatrate[8:16]])
femin.create_nflux_hist(fast_nFlux)

femin.create_coolpress_hist([cool_pressure[:8], cool_pressure[8:16]])
femin.create_coolvelocity_hist([cool_velocity[:8], cool_velocity[8:16]])
femin.create_cooltemp_hist([cool_temp[:8], cool_temp[8:16]])

femin.create_iPrint_opt([IP[:8], IP[8:16]])
femin.create_iTime_opt(IT)
femin.create_iState_opt(IS)



# Save File
femin.save("data.h5")

# Load File
femin.load("data.h5")

# Preview and generate
femin.preview()
femin.generate("Masukan.txt")
femin.run_femaxi6("Masukan.txt", "Keluaran.txt")