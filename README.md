## what is this?
a tool to compare image similarities for 360 photos. built for vrb.


## algorithm
this utility implements the following equation, as developed by wang et al in 2013:

![ssim equation](http://file.scirp.org/Html/3-7800146/c060a765-b050-4f10-bc65-5e89c4ea228f.jpg =100x)

the resulting structural similarity index measure (ssim) score can vary between -1 and 1, where 1 indicates perfect similarity.

## references:
* Z. Wang, A. C. Bovik, H. R. Sheikh and E. P. Simoncelli. Image quality assessment: From error visibility to structural similarity. IEEE Transactions on Image Processing, 13(4):600--612, 2004.
* Z. Wang and A. C. Bovik. Mean squared error: Love it or leave it? - A new look at signal fidelity measures. IEEE Signal Processing Magazine, 26(1):98--117, 2009.