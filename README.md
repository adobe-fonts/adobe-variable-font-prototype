# Adobe Variable Font Prototype

OpenType-CFF2 variable font made from [UFO] sources derived from [Source Serif Pro],
designed by [Frank Grießhammer].

This font is intended to serve as a test and demonstration for environments and workflows
that support the Compact Font Format flavor of the [OpenType variable fonts].

The font is functional but it's not considered *shippable* — see [Current limitations].
We plan to update it as the tools improve.

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


## Downloading the font

* [Latest release](../../releases/latest)
* [All releases](../../releases)


## Building the font from source

### Requirements

To build **AdobeVFPrototype.otf** from source, you need to have installed a custom build
(2.5.65463 or later) of the [Adobe Font Development Kit for OpenType] which can be
downloaded from <http://www.adobe.com/devnet/opentype/afdko/AFDKO-Variable-Font-Support.html>

[Adobe Font Development Kit for OpenType]: http://www.adobe.com/devnet/opentype/afdko.html


### Build command

macOS and Linux:

```sh
$ sh buildFont.sh
```

Windows:

```sh
> cmd buildFont.sh
```

### Build process

The **buildFont.sh** file calls two scripts, `buildMasterOTFs` and `buildCFF2VF`.
The first script generates OpenType-CFF fonts from each of the UFO masters. And the
second takes the set of OTF fonts built in the previous step, and combines them to produce
an OpenType-CFF2 variable font. More details about the process are provided at
<http://www.adobe.com/devnet/opentype/afdko/AFDKO-Variable-Font-Support.html>

The build script finally runs TTX to make some changes to the `name` and `GSUB` tables.
In the `name` table, the placeholder word *Custom* is changed to *Contrast*.
And in the `GSUB` table, a *[feature variations table]* is added.

[feature variations table]: https://www.microsoft.com/typography/otspec/chapter2.htm#featvartable


## Current limitations

* Adobe Variable Font Prototype cannot be displayed by macOS or Windows because their font
rasterizers do not yet support the newer `CFF2` table. (As of this moment, the only tool
that can render OT-CFF2 fonts is [FontView]).
* The font's glyphs will not be hinted because the AFDKO's `autohint` tool cannot yet
produce hinting data that is compatible across a set of master fonts.
* The font does not contain the required `MVAR` and `STAT` tables.
* The font's `CFF2` table lacks subroutinization.

[FontView]: https://github.com/googlei18n/fontview
