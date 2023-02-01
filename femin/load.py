import h5py
import numpy as np
from . import geo
from . import hist_data


def load(name):
    data = h5py.File(name, 'r')

    geo_grp = data.get("geo")
    for key in list(geo_grp):
        if key[0:6] == 'pellet':
            geo.pellet[key[7:]] = np.array(geo_grp.get(key)).tolist()
        elif key[0:4] == 'clad':
            geo.clad[key[5:]] = np.array(geo_grp.get(key)).tolist()
        elif key[0:4] == 'dish':
            geo.dish[key[5:]] = np.array(geo_grp.get(key)).tolist()
        elif key[0:6] == 'plenum':
            geo.plenum[key[7:]] = np.array(geo_grp.get(key)).tolist()
        elif key[0:7] == 'chamfer':
            geo.chamfer[key[8:]] = np.array(geo_grp.get(key)).tolist()
        elif key[0:3] == 'gap':
            geo.gap[key[4:]] = np.array(geo_grp.get(key)).tolist()

    hist_grp = data.get("hist_data")
    for key in list(hist_grp):
        if key[0:6] == 'ax_seg':
            hist_data.ax_seg_pf[key] = np.array(hist_grp.get(key)).tolist()
        else:
            hist_data.pwr_hist[key] = np.array(hist_grp.get(key)).tolist()
