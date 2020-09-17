# Adobe Variable Font Prototype

Variable font in OpenType-CFF2 and TrueType formats, made from [UFO] sources derived from
[Source Serif Pro], designed by [Frank Grießhammer].

The font files are intended to serve as test cases for environments and workflows that aim
to support [OpenType variable fonts].

The fonts are functional but have some limitations — see [Current limitations].
We plan to update them as the tools improve.

[UFO]: http://unifiedfontobject.org/
[Source Serif Pro]: https://github.com/adobe-fonts/source-serif-pro
[Frank Grießhammer]: https://github.com/frankrolf
[OpenType variable fonts]: https://medium.com/@tiro/introducing-opentype-variable-fonts-12ba6cd2369
[Current limitations]: #current-limitations


## Font characteristics

**Adobe Variable Font Prototype** contains two axes — weight and contrast — five design
masters, and eight named instances — Extra Light, Light, Regular, Semibold, Bold, Black,
Black Medium Contrast, and Black High Contrast.

The weight axis has an intermediate master (**master_1**), and the design space can be
thought of as having the shape of a square triangle. This is achieved by using **master_0**
twice, and by having **master_4** along the *diagonal* defined by **master_0** and
**master_3**. This arrangement effectively collapses half of the original rectangular-shaped
design space, concealing interpolation imperfections that would be visible otherwise.
See [design space notes](DesignSpaceNotes) for more details.

The font also contains transitional designs for the glyphs $ (dollar) and ¢ (cent), in
which the inner-counter part of the stroke is removed, when the weight axis reaches Bold
or heavier.

The font supports the [Adobe Latin 2] character set, GPOS kerning, and the GSUB features
listed below.

    pnum (proportional figures)
    tnum (tabular figures [default])
    onum (old-style a.k.a. text figures)
    lnum (lining figures [default])
    zero (slashed zero)
    case (case-sensitive forms such as parentheses, hyphen)
    liga (ligatures fi fl ft)

[Adobe Latin 2]: https://github.com/adobe-type-tools/adobe-latin-charsets#adobe-latin-2-adobe-western-2


## Downloading the font files

* [Latest release](../../releases/latest)
* [All releases](../../releases)


## Building the fonts from source

### Requirements

- Python 3.6 or later. We recommend _not_ using your system-installed Python if
   you are using macOS or a Linux system with Python 3 pre-installed. Instead,
   use either an installer from [Python.org](http://python.org) **or** use
   [Homebrew](https://brew.sh/) (macOS only).

- We also recommend the use of a [Python virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).
  
- Install the requirements with `pip`:

   ```pip3 install -r requirements-dev.txt```


### Build command
With the requirements installed, you can build with the supplied build script:

#### macOS and Linux:

```sh
sh buildFont.sh
```

#### Windows:

```sh
cmd buildFont.sh
```

### Build process

The **buildFont.sh** script first builds the OpenType-CFF2 font with the FDK tools
`buildMasterOTFs` and `buildCFF2VF`.
The first tool generates OpenType-CFF fonts from each of the UFO masters. And the
second takes the set of OTFs built in the previous step, and combines them to produce
the CFF2 variable font.

The CFF2 table is then subroutinized with FDK's `tx` tool, and the modified table
is replaced in place using FDK's `sfntedit` tool.

Next, `fontmake` is used for building the variable TrueType font.

Finally, `sfntedit` is used for copying/replacing several tables between the
OTF and TTF fonts.


### Testing

A test suite is available to check the built fonts to ensure they were built with
expected values. You can initiate the tests with:

```pytest tests```

The tests are designed to catch unexpected regressions that might be caused by
changes in tools or other environment differences.


## Current limitations

* Support for the variable OTF-CFF2 flavor is not as broad as for the variable TTF flavor.
* Neither of the fonts is hinted.
