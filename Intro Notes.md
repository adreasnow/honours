

## Structure

## Computational Chemistry


## Grand Perspective

### Electronic Environment

Mostly from \citeauthor{Xu2020}:
External electronic field (EEF) catalysis has been shown to work, previously through pH dependent functionality creating localised electronic fields being used as STM tips, that catalyse bond breaking and forming reactions, as well as functionalised surfaces/catalysts.

Issues include that the solvent itself can interfere with the the EEF particularly in polar solvents, though the solubility of polar solvents (which are ore susceptible to the influence of an EEF) are less soluble in apolar solvents.

STM reactions are good, but very small in scale and so moving to electrodes with a solvent dielectric turns an EEF catalysed reaction into an electrochemical one. The potential in these circumstances is negligible beyond the EDL

Experimentally, overcoming this falloff requires the use of bipolar cells or potentially the use of microfluidics, so being able to study it experimentally is a massive boon.

To be able to use an EEF then, there needs to be some way to facilitate a relatively homogeneous charge through the bulk. Enter the ordered solvent.

### Evidence for ordered solvents from EEF

Computational study showing that the solvation shell can be broken by an electronic field - used implicit and cluster continuum solvation \cite{Warshel2006}

As determined by MD The dielectric constant of polar organic solvents decreases with increasing electric field up to $0.4\:V\cdot\AA$ \cite{Daniels2017}

\citeauthor{Daniels2017} also showed that as the EEF is increased, many solvents tend to increase in viscosity and crystallise ("electrofreezing"), however ILs tend to become decrease in density/viscosity, making them more suitable

### reordered Solvents

To try and minimise the likelihood of electrochemical reactions happening, the EEF can be pulsed, in order to facilitate pre-ordering of the solvent without allowing for migration to the electrodes that would allow for redox processes to occur, though this requires a solvent species that will be able to maintain the ordered structure between pulses to make use of this.

### Marcus Theory

Separates out the reaction energy of electron-transfer reactions into internal and external reorganisation energy. Typically shows a larger solvent reorganisation energy than internal reorganisation energy, showing that it is the driving force for the reaction
\cite{MarcusTheory,Xu2020}

Explains the impressive catalytic ability of enzymes, as they can stabilise the highly polar transition state, and minimise the reorganisation energy required to get to the transition state, by \it{pre}-organising the reaction site, to provide a "preorganised polar environment". \cite{Warshel2006}


## ILs

* Can be thought of through the context of two ideas:
  * The substance is a liquid ($t_m$ and/or $t_g < 100^\circ C$ )
  * Contains ions and exhibits ionic conductivity

### imidazolium ILs

* In \ce{C2mim}, hydrogen bonding preferentially occurs with the \ce{C2} hydrogen, and above/below the imidazolium ring, over the \ce{C4} and \ce{C5} hydrogens \cite{Thar2009}


## Protic Ionic Liquids

## H-Bonding

> "It is to be stressed that the anisotropy of the hydrogen bonding interaction should be strong enough to ‘hold’ the ‘hydrogen bond’ at least at the zero point level, otherwise it is better to think of it as non-existent. At a given temperature, the thermal energy along a coordinate that can break the hydrogen bond should be below the barrier along that coordinate."

> "A hydrogen bond is said to exist when: (1) there is evidence of a bond and (2) there is evidence that this bond specifically involves a hydrogen atom already bonded to another atom"
>
> \citea{Goswami2009}



### How Ionic is the IL

* ILs can have lots of reacting species and can form lots of weird byproducts, so a "pure" IL is typically considered to be one which has $<1\%$ neutral species. Higher than this can be considered mixtures of IL and neutral species. \cite{Kar2019} This also extends to the degree of proton transfer in the IL, The species must be $> 99\%$ to the right of The eqn below

$$
\ce{HA + B <=> [BH]+ + B-}\label{eqn:dissociation}
$$

* aqueous $pK_A$ differences ($pK_A(base)-pK_a(acid)$) can be suggestive of how complete the proton transfer is in a PIL

* *PILs with a $\Delta pK_a>8$ have nearly ideal Walden behaviour. \cite{Yoshizawa2003}?

* Walden plot of ionicity? one metric of how ionic a salt is - $\log(\text{molar conductivity})$vs $\log(\frac{1}{\eta})$
	* $\frac{1}{\eta}=\text{fluidity}$
	* empirical means of qualitatively describing the likely degree of proton-transfer
* The strength of the PIL acid has more of an impact on the ionicity than the size, with low $pK_A$ values leading to higher ionicity - a measure of how ionic a salt is.
* Liquid state has high viscosity, then as the temperature decreases you hit the melting point ($T_m$) where the liquid turns into a "plastic crystal" which is an amorphous non-crystalline solid. we keep decreasing the temperature, we hit the glass transition temperature ($T_g$) , corresponding to a maximum heat capacity, where the plastic crystal can fully crystallise.
  * In ILs, as the temperature decreases, the viscosity will gradually decrease, but won't have a definite melting point, it will just become more and more viscous.

* The glass transition temperature ($T_g$) is a "qualitative signature" of the ion mobility in the IL (10.1002/chem.200400817)
* Unsurprisingly, more hydrogen bonding means higher viscosity, as does more vdW interactions
* Ion size doesn't affect imidazolium ILs that much (10.1021/ic951325x)

### Acidity

* $pK_As$ are based on proton lability in aqueous environments and aren't representative of the proton dynamics in bulk IL solution. using aqueous $pK_A$s results in proton dissociations that are "orders of magnitude lower than one would predict"\cite{Kar2019}
* Hammett method for determining $pK_A$

$$
\begin{gather}
H_0=pK(I)_{aq}+\log\Bigg(\frac{[I^-]_s}{[IH]_s}\Bigg)\label{eqn:hammetacidity}
\end{gather}
$$

* $pK_A$ can also be determined by titration
* The acidity seems to be of the IL pair and not of the acidic component alone \cite{Greaves2008a}
* When using the same cation, the basicity of the anion (based on the $pK_A$) dictated the relative acidity, and thus the catalytic ability of the ion pair (tested with [bbim] and [Hbim] and \cite{Palimkar2003}

### Catalytically

* The ability for PILs to catalyse a reaction through a Br{\o}nsted acid activated pathways was strongly correlated to the acid strength of the IL pair \cite{Greaves2008a}
  * Furthers that the $\Delta pK_a$ can be used as a relative indicator of the catalytic potential of a PIL \cite{Palimkar2003}
* \il{HBIm}{BF4} has also been used to catalyse condensation reactions with 85-94\% yield at $100^\circ C$ (10.1021/j100227a003)



