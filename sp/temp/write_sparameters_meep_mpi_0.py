import pathlib
import pickle
from gdsfactory.simulation.gmeep import write_sparameters_meep

from gdsfactory.read import import_gds
from gdsfactory.technology import LayerStack

if __name__ == '__main__':
	with open("/home/runner/work/gdsfactory/gdsfactory/data/sp/temp/write_sparameters_meep_mpi_0.pkl", 'rb') as inp:
		parameters_dict = pickle.load(inp)

	component = import_gds('/home/runner/work/gdsfactory/gdsfactory/data/sp/temp/write_sparameters_meep_mpi_0.gds', read_metadata=True)
	filepath_json = pathlib.Path('/home/runner/work/gdsfactory/gdsfactory/data/sp/temp/write_sparameters_meep_mpi_0.json')
	layer_stack = LayerStack.parse_raw(filepath_json.read_text())
	write_sparameters_meep(component=component, overwrite=False, layer_stack=layer_stack, filepath='/home/runner/work/gdsfactory/gdsfactory/data/sp/coupler_ring_13b72964d08829db2d2f8f786ccc8416.npz',		ymargin = parameters_dict["ymargin"],
		ymargin_bot = parameters_dict["ymargin_bot"],
		xmargin = parameters_dict["xmargin"],
	)