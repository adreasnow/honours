## General Info

This is a repo containibng the final iPython notebooks used to generate most of the data for my honours thesis. The only things that have been excluded are my PyMOL work, as those .pse files with isosurfaces and MEPs are many gigabytes of binary data, not suitable for a github repo.

To use the notebooks form this repo, you'll need:
* matplotlib
* numpy
* colorsys
* scipy
* plotly
* ipywidgets
* pandas
* csv

*Yes, I know it's a mess of packages, but these notebooks have been slowly evolving over the year and and aren't indicative of how cleanly I actually work.*

To run the OEEF notebooks, you will need to have the included data folder in the same directory.

The pymol-scripts folder only has a couple of scripts that I've used to generate the .pse files, from the .csv files and .xyz geoms:
* pymolEfield.py - a function to generate the spheres representation of the OEEF scans
* A PyMOL plugin I wrote as a wrapper to the above function (see below)

## PyMOL Plugin and Psi4 Script
the `pymolEfield.py` script has also had a gui developed for it, after a fun night hacking together some code while getting coffee with friends, and is available in the `pymol-scripts/examples` folder.

![plugin_pic.png](plugin_pic.png)

This produces figures that look like this (without the black axes. They were added separately):

| ![catscan](pymol-scripts/examples/catscan.png) | ![rsscan](pymol-scripts/examples/rssepscan.png) |
| :------: | :------: |

The format of the CSV file is as follows:
* First row for headings (gets ignored)
* Columns with the following data
    * X, Y and Z components of <a href="https://www.codecogs.com/eqnedit.php?latex=\vec&space;F" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\vec&space;F" title="\vec F" /></a>
        * <a href="https://www.codecogs.com/eqnedit.php?latex=F_X" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_X" title="F_X" /></a>
        * <a href="https://www.codecogs.com/eqnedit.php?latex=F_X" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_Y" title="F_Y" /></a>
        * <a href="https://www.codecogs.com/eqnedit.php?latex=F_X" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_Z" title="F_Z" /></a>

    * <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta\Delta&space;E\:(KJ\cdot&space;mol^{-1})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta\Delta&space;E\:(KJ\cdot&space;mol^{-1})" title="\Delta\Delta E\:(KJ\cdot mol^{-1})" /></a> (perturbation energy as <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta&space;E_{\text{perturbed}}-\Delta&space;E_{\text{unperturbed}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta&space;E_{\text{perturbed}}-\Delta&space;E_{\text{unperturbed}}" title="\Delta E_{\text{perturbed}}-\Delta E_{\text{unperturbed}}" /></a>)
    * X, Y and Z components of <a href="https://www.codecogs.com/eqnedit.php?latex=\vec&space;\mu" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\vec&space;\mu" title="\vec \mu" /></a>
        * <a href="https://www.codecogs.com/eqnedit.php?latex=\mu_X" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mu_X" title="\mu_X" /></a>
        * <a href="https://www.codecogs.com/eqnedit.php?latex=\mu_Y" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mu_Y" title="\mu_Y" /></a>
        * <a href="https://www.codecogs.com/eqnedit.php?latex=\mu_Z" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mu_Z" title="\mu_Z" /></a>

* The first row should be the properties of the unperturbed molecule, with all perturbations following

e.g.:

|    x     |    y     |    z     |  e_kjmol   | dipole(x)  | dipole(y)  | dipole(z)  |
| :------: | :------: | :------: | :--------: | :--------: | :--------: | :--------: |
| 0.00e+00 | 0.00e+00 | 0.00e+00 |     0      | 2.84909414 | -4.989243  | 1.57583802 |
| 1.94e-03 | 0.00e00 | 0.00e+00 | 3.54743169 | 0.67670253 | -4.5698034 | 1.77719687 |
| 1.78e-03 | 7.91e-04 | 0.00e+00 | -0.574705  | 1.01374995 | -5.158874  | 1.74510839 |

<a href="https://www.codecogs.com/eqnedit.php?latex=\vec&space;F" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\vec&space;F" title="\vec F" /></a> needs to be in atomic units following physics notation (pointing from positive to negative) and <a href="https://www.codecogs.com/eqnedit.php?latex=\vec&space;\mu" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\vec&space;\mu" title="\vec \mu" /></a> needs to be in Debye, following standard chemistry notation (also pointing from positive to negative). The electric field vector will be flipped to be displayed in gaussian notation.



An example Psi4 script to perturb a molecule based on a list of electric field vectors and generate a compliant .csv file has been provided in the `pymol-scripts/examples` folder, along with some example .csv files.

For each perturbation, the the Psi4 script also generates .cube files for the electron density (alpha, beta, spin and total), as well as an ESP .cube, and spits out the perturbed geometry and unperturbed geometry (this one was an accident...) as .xyz 

