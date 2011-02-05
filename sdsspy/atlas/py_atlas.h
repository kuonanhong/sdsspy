#include "dervish.h"
#include "phFits.h"
#include "phConsts.h"

PyObject* py_read_atlas(const char* filename, int id);

ATLAS_IMAGE* py_load_atlas_images(const char* filename, int id);
PyObject* py_store_atlas_data(ATLAS_IMAGE* ai);
void py_copy_images(ATLAS_IMAGE* ai, PyObject* dict);
PyObject* py_copy_image(ATLAS_IMAGE* ai, int band);

PyObject* py_create_uint16_image(int nrow, int ncol);

void py_copy_stats(ATLAS_IMAGE* ai, PyObject* dict);
