#https://github.com/spectralpython/spectral/blob/master/spectral/io/envi.py
import matplotlib.pyplot as plt
import numpy

#open_path = r'C:\SPECTRAL IMAGES\Specim V10\ColorChecker_8_binning\capture\Colorchecker.raw'

'''
spatial_pixels = 2144
sample_lines = 1357
spectral_bands = 135
open_path = r'C:\SPECTRAL IMAGES\Specim V10\ColorChecker_8_binning\capture\Colorchecker.raw'

# Specim V10 no binning
# Cannot read whole file due to its huge size. Need to skip n bytes fopen.seek(spatial_pixels*n*spectral_bands)
open_path = r'C:\SPECTRAL IMAGES\Specim V10\ColorChecker no binning\capture\halogen_emptyname_0008.raw'
spatial_pixels = 2144
sample_lines = 100 #1259
spectral_bands = 1080

# Specim V10 no binning
spatial_pixels = 1100
sample_lines = 500 #2252
spectral_bands = 567
open_path = r'C:\READ ENVI Matlab + Python\5_unwashed_washed_2019_09_02_17_06_03\data'

# Specim IQ
spatial_pixels = 512
sample_lines = 512
spectral_bands = 204
open_path = r'C:\SPECTRAL IMAGES\Specim IQ\moss\capture\2018-09-20_004.raw'

# N25 Infrared
spatial_pixels = 320
sample_lines = 449
spectral_bands = 256
open_path = r'C:\SPECTRAL IMAGES\Specim N25\Paintings Sarita\IR\capture\IR_best_orientation_inversed_0009.raw'

'''
# Specim IQ
spatial_pixels = 512
sample_lines = 512
spectral_bands = 204
open_path = r'F:\PHD\UEF Thesis\Dimitry\SPECTRAL IMAGES\Specim IQ\moss\capture\2018-09-20_004.raw'

#
fopen = open(open_path, "rb")

u = numpy.fromfile(fopen, dtype=numpy.uint16) #uint16 float32 #count=spatial_pixels*sample_lines*spectral_bands
print(u.shape)
print(spatial_pixels*sample_lines*spectral_bands)
u1 = numpy.reshape(u, (sample_lines, spectral_bands, spatial_pixels))
print(u1.shape)
plt.imshow(u1[150:350,160,150:350], cmap="gray")
plt.show()

# write to file
filename = r"C:\SPECTRAL IMAGES\Temp\Colorchecker_8bin_float32.raw"
fileobj = open(filename, mode='wb')
c = numpy.ndarray(shape=(spatial_pixels*sample_lines*spectral_bands,1), dtype=float)
c = u/255
c.tofile(fileobj)
fileobj.close()