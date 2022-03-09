---
title: TENSCALC
section: 1
header: User Manual
footer: tenscalc 0.1.0
date: March 9, 2022
---

# NAME
tenscalc - tension estimator for stringed instruments

# SYNOPSIS
tenscalc string [--si] gauge material pitch length

tenscalc set [-h] [--file FILE] [--title TITLE]

tenscalc set [-h] [--length LENGTH] [--gauges [G ...]]
                    [--materials [M ...]] [--pitches [P ...]]
                    [--double] [--si] [--title TITLE]
tenscalc help

# SUBCOMMANDS
## tenscalc string
Estimate tension for a single string.

    REQUIRED ARGUMENTS
        gauge       String gauge in inches, 1/1000in, or mm with the
                    --si flag. Inch gauges may optionally be in thousandths
                    of an inch: "11" or ".011" are both valid and produce
                    the same output.

        material    Short code for string construction material.
                    Options:
                        code  material
                        ----  --------
                          ps  plain steel
                         nps  nickel plated steel wound
                          pb  phosphor bronze wound
                        8020  80/20 bronze wound
                        8515  85/15 bronze wound
                          ss  stainless steel roundwound
                          fw  stainless steel flatwound
                          pn  pure nickel wound

        pitch       Tuned pitch of string in scientific pitch notation,
                    from A0-E5. Middle C is C4, and A440 is A4. 
                    Examples of open-string pitches in standard tunings:
                        Guitar: E2, A2, D3, G3, B3, E4
                        Bass: (B0), E1, A1, D2, G2
                        Mandolin/violin: G3, D4, A4, E5
                        Banjo: G4, D3, G3, B3, D4

        length      Scale length of the instrument in inches, 1/1000in,
                    or mm with the --si flag.

    OPTIONAL ARGUMENTS
        --si        Supply <gauge> and <length> arguments in millimenters.
                    Tension is returned in kilograms (converted from
                    pounds; used in place of Newtons.)

    EXAMPLES
        tenscalc string .011 ps E4 25.5
        tenscalc string --si 1.37 pb E2 632.5

## tenscalc set
Estimate individual and total tensions for a string set. String sets may
    either be entered on the command line or read from a "set file".

    Set files use the following format:
        ---- begin set file ---
        [set]
        length = LENGTH
        gauges = G [G ...]
        materials = M [M ...]
        pitches = P [str ...]
        double = true OR false (optional)
        si = true OR false (optional)
        ---- end set file ----

    The [set] section header and all keys are required. Any other sections or
        keys are ignored. Lists for gauges, materials, and pitches keys must be
        of equal length. List items are space-separated. An example set file 
        for a set of medium-gauge electric guitar strings on a Fender-scale
        instrument, with nickel plated steel wound strings, might look like:
        ---- begin set file ----
        [set]
        length = 25.5
        gauges = 11 15 18 26 36 50
        materials = ps ps ps nps nps nps
        pitches = e4 b3 d3 g3 a2 e2
        ---- end set file ----

    When entering sets on the command line, --gauges, --materials, and
        --pitches must have the same number of arguments.

    ARGUMENTS
        --file FILE         A path to a valid set file. Any arguments other
                            than --title are ignored if --file is present.
        
        --length LENGTH     Scale length of instrument in inches, 1/1000in,
                            or mm with the --si flag.

        --gauges [G ...]    List of string gauges in inches, 1/1000in, or
                            mm with the --si flag.
        
        --materials [M ...] List of valid string material codes.
                            Options: ps, nps, pb, 8020, 8515, ss, fw, pn

        --pitches [P ...]   List of pitches in scientific pitch notation,
                            from A0-E5. Middle C is C4, and A440 is A4.

        --double            When preset, double each argument to --gauges,
                            --materials, and --pitches. For double-coursed
                            instruments like mandolin.

        --si                Supply --length and --gauges arguments in
                            millimeters. String and set total tensions are
                            returned in kilograms.

        --title TITLE       Optional title for output chart.

    EXAMPLES
        tenscalc set ~/path/to/set.txt

        tenscalc set --length 25.5 --gauges 11 15 18 26 36 50
            --materials ps ps ps nps nps nps --pitches e4 b3 g3 d3 a2 e2

        tenscalc set --double --length 16.75 --gauges 11 15 26 40
            --materials ps ps 8020 8020 --pitches e5 a4 d4 g3
            --title "80/20 Bronze Mandolin Set"

## tenscalc help
Print this manual.

# AUTHOR
    Written by David Lambert.

# REPORTING BUGS
    tenscalc on GitHub: <https://github.com/davidelambert/tenscalc/issues>

# COPYRIGHT
    Copyright (C)  2022  David Lambert.
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3
    or any later version published by the Free Software Foundation;
    with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
    A copy of the license is included in the section entitled "GNU
    Free Documentation License".
