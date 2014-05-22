Asset generator
===============

Very rough proof-of-concept for generating a lot of fake asset files for performance testing an application.

Relies on a *nix system with `dd` and `file`.

The idea is that multiple files of a given file type and of random size (within a range) are generated from a small source file that is just big enough for the *nix `file` command to recognise, based on the byte signature (and thus is likely to also be recognised by file type detection in an application).

The small source files are generated from known file types using `typegen.py <path_to_file>`. This is a one-off process for a given file type. Output is a file called `types/type.<ext>` where `<ext>` matches the input file's extension and, by default, is 10 bytes in size. Typically, 10 bytes is enough that `file` will still recognise the output file as the same type as the input file. If it isn't enough then a second, integer argument can be given to make it bigger. E.g.:

```
[assetgen] ./typegen.py /tmp/foo.psd
Input type:
        /tmp/foo.psd: Adobe Photoshop Image, 3508 x 2480, RGBA, 4x 8-bit channels
Output type:
        types/type.psd: Adobe Photoshop Image
```

A sample set of source files have been generated for doc, gif, jpg, pdf and png.

The `assets.txt` is where you can declare what set of assets you want to generate. The format is an asset file type per line with four parameters:

```
file_type_extension min_file_size_in_bytes max_file_size_in_bytes number_of_asset_files
```

E.g.

```
gif 512 1024 10
psd 2048 2048 5
```

When `assetgen.py` is run this file will be read and the corresponding asset files will be generated as `assets/asset<N>.<ext>` where `<N>` is an incremental number for an asset file type `<ext>`.

The above example would produce 10 gif files between 0.5K and 1K in size named asset[1-10].gif, and 5 psd files of 2K in size named asset[1-5].psd.
