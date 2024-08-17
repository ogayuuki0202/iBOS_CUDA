import vtk
import vtk.util.numpy_support as numpy_support

def numpyToVTK(data, output_file):
    data_type = vtk.VTK_FLOAT
    shape = data.shape

    flat_data_array = data.flatten()
    vtk_data = numpy_support.numpy_to_vtk(num_array=flat_data_array, deep=True, array_type=data_type)

    img = vtk.vtkImageData()
    img.GetPointData().SetScalars(vtk_data)
    img.SetDimensions(shape[0], shape[1], shape[2])

    # Save the VTK file
    writer = vtk.vtkXMLImageDataWriter()
    writer.SetFileName(output_file)
    writer.SetInputData(img)
    writer.Write()

if __name__ == "__main__":
    output_file = 'output_volume.vti'  # Use '.vti' extension for XML-based VTK files
    numpyToVTK(DATA, output_file)