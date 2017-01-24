nalu_build_dir=${HOME}/nalu/
trilinos_install_dir=$nalu_build_dir/install/trilinos
yaml_install_dir=$nalu_build_dir/install

EXTRA_ARGS=$@

# Cleanup old cache before we configure
# Note:  This does not remove files produced by make.  Use "make clean" for this.
find . -name "CMakeFiles" -exec rm -rf {} \;
rm -f CMakeCache.txt

cmake \
  -DTrilinos_DIR:PATH=$trilinos_install_dir \
  -DYAML_DIR:PATH=$yaml_install_dir \
  -DENABLE_INSTALL:BOOL=OFF \
  -DCMAKE_BUILD_TYPE=RELEASE \
$EXTRA_ARGS \
../
