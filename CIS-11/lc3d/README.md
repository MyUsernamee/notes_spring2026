# LC3D

The most basic linker ever. (Basically preprocessor)

Just take a lc3 source file, and expands out "C like" include statements, i.e.

```c
#include "something.asm"
```

Then passes them to the LC3 assembler, for now.

I might make this a more full blown assembler down the line, but for now, this is all it does.
