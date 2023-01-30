import webview
import h5py
import subprocess
from . import geo
from . import hist_data
from . import gen


def save(name):
	global pellet, clad, dish, chamfer, plenum, gap
	global pwr_hist, ax_seg_pf

	h5 = h5py.File(name, 'w')

	# Geometry Group
	geo_grp = h5.create_group("geo")
	for key in geo.pellet.keys():
		if key == "obj_seg":
			geo_grp.create_dataset("pellet_" + key, data=geo.pellet[key], dtype='i')
		else:
			geo_grp.create_dataset("pellet_" + key, data=geo.pellet[key], dtype='d')

	for key in geo.clad.keys():
		if key == "mat":
			geo_grp.create_dataset("clad_" + key, data=geo.clad[key], dtype='i')
		else:
			geo_grp.create_dataset("clad_" + key, data=geo.clad[key], dtype='d')

	for key in geo.dish.keys():
		geo_grp.create_dataset("dish_" + key, data=geo.dish[key], dtype='d')

	for key in geo.plenum.keys():
		geo_grp.create_dataset("plenum_" + key, data=geo.plenum[key], dtype='d')

	for key in geo.gap.keys():
		geo_grp.create_dataset("gap_" + key, data=geo.gap[key], dtype='d')

	# History Data Group
	hist_grp = h5.create_group("hist_data")
	for key in hist_data.pwr_hist.keys():
		if (key[:6] == "iTime") or (key[:6] == "iPrint") or (key[:6] == "iState"):
			hist_grp.create_dataset(key, data=hist_data.pwr_hist[key], dtype='i')
		else:
			hist_grp.create_dataset(key, data=hist_data.pwr_hist[key], dtype='d')

	for key in hist_data.ax_seg_pf.keys():
		hist_grp.create_dataset(key, data=hist_data.ax_seg_pf[key], dtype='d')

	h5.close()


def preview():
	gen.gen_for_preview()
	#print(__name__)
	if __name__ == 'femin.save':
		# Create a standard webview window
		window = webview.create_window('Simple browser', 'femin/view/index.html', easy_drag=False, text_select=True, resizable=False, min_size=(1200, 600))
		webview.start()


def generate(file_name):
	gen.gen_for_femaxi(file_name)


def run_femaxi6():
	batch_file = "FEM6.exe"
	print("Simulating..........")
	subprocess.run([batch_file])
	print("Finish")