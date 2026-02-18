#/bin/bash

# Super simple bash script that takes the built binaries and symbolically links them to your .local/bin folder

PWD=$(pwd)
ln -s ${PWD}/lc3as ~/.local/bin/lc3as
ln -s ${PWD}/lc3convert ~/.local/bin/lc3convert
ln -s ${PWD}/lc3sim ~/.local/bin/lc3sim
ln -s ${PWD}/lc3sim-tk ~/.local/bin/lc3sim-tk
