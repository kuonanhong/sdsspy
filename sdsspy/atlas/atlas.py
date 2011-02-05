import numpy
import _py_atlas

SOFT_BIAS=1000
def read(filename, id, trim=True):
    imdict = _py_atlas.py_read_atlas(filename, id)

    if trim:
        for band in xrange(5):
            im = imdict['images'][band]

            # there is no way that I know of to get the exact region.
            #
            # This is not exact, since even noisy spots could end up zero, but
            # at least we know we would be in the noise anyway

            w1,w2 = numpy.where(im != SOFT_BIAS)
            if w1.size > 0:
                minrow = w1.min()
                maxrow = w1.max()
                mincol = w2.min()
                maxcol = w2.max()

                if ((minrow > 0) 
                        or (maxrow < (im.shape[0]-1))
                        or (mincol > 0)
                        or (maxcol < (im.shape[1]-1))):
                    im = im[minrow:maxrow+1, mincol:maxcol+1]
                    imdict['images'][band] = im


    return imdict
