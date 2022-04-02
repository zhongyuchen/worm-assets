# worm-assets
3D models of C. elegans for MuJoCo

## Installation
* install the project in editable mode from local project path
    ```
    pip install -e .
    ```
* change local packages to be built in-place without first copying to a temporary directory
    ```
    pip install -e . --use-feature=in-tree-build
    ```

## Sphere
* built using Blender 3.0.1
* based on an UV sphere: Segments=100, Rings=50, Rotation Y=90, Scale X=0.1, Y=0.1, Z=1.25
* model length = 2.5, the largest radius = 0.1 -> length:radius = 25:1
* segmented into 25 segments with equal length of 0.1: cuts at x = 1.25 - i * 0.1, 1 <= i <= 24
* each segment is a cylinder shaped mesh without top and bottom faces, so top and bottom faces are filled with F.
* The faces pointing in the opposite direction of x-axis in Sphere.004 and Sphere.005 segments were filled with F, 
but the exported meshes don't include that faces, so they are filled with Alt+F instead.
* the object of each segment is exported in *.stl format, and with 'selection only' option turned on

### Reference
https://doi.org/10.3389/fncom.2012.00010
* The model approximates the tapered shape of the worm as a prolate ellipse.
* C.elegans length = 1mm, the largest radius = 0.04mm -> length:radius = 25:1

## Virtual Worm
* rotated so that the dorsal/ventral plane is parallel to x/y plane

### Reference
* The 3D model of C. elegans is based on the blender model from [the VirtualWorm project](http://caltech.wormbase.org/virtualworm/)
