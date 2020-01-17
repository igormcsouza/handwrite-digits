#!/bin/bash
docker run --rm -it \
-v `pwd`/scripts:/workdir/ \
-v `pwd`/data:/data \
-v `pwd`/weights:/weights \
igormcsouza/ml:handwrite-digits