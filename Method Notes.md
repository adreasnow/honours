

## MD

## Cyclisation of aminchalcone

* \cite{Du} showed $\ce{[HBIm][CF3SO3]}$ to be the best for amine addition to chalcone, however this was in an aqueous environment. This used the IL as a Brönsted acid

* \cite{Zheng2013} showed that piperidine as a Lewis base with $\ce{KOH}$ was exceptionally efficient at converting the aminochalcone to the cyclised product (>99\% yield r.t.)

* I'm guessing that this was adding in to the ketone, withdrawing electron density from the $\alpha,\beta$ double bond, making it more electrophilic, then the $\ce{KOH}$ came through and mopped up the mopped up the proton form the resulting $\ce{RNH3+}$

* \cite{Bunce2011} synthesised the product and made the flavone using just conc. $\ce{HCl}$

* Would be activation by protonating the carbonyl, or the $\alpha$ site. according to the paper, these are both valid pathway

## MD in general \cite{Cramer2004}

* Even at 0K, a molecule will sample a range of structures due to ZPVE

* The ensemble are whatever variables are being held constant (NVP/NPT)

* Phase space is the n-dimensional space that encompasses all degrees of freedom and all momenta of particles within a system. Particles are described as having 6 coordinates in phase space $X(q,p)=(x,y,z,p_x,p_y,p_z)$.

* Given that phase space encompasses the position and momenta of every particle in the system, it is possible to determine how the particles will move relative to their current phase space coordinates.

* MD utilises this to simulate the behaviour of the system over time.

* structure-property relationship of chemistry

* sampling a system over time to obtain representative data

* utilising many possible states of the system and their relative energies to determine the expectation values of the properties of the system

### MD of ILs



### Polarisability

### Drude

* "charge on a spring" model. Adds additional charged particles (oscillators) to the centre of each atom, that are attached by a spring, mimicking the behaviour of physical dipoles and distorting the electron density.

* The dipole is between the atom centre which has the partial charge of the atom ($-q_D$) as determined by partitioning and the Drude particle, which is free floating on a spring and has charge $+q_D$

* $q_D$ is calculated using the atomic polarisability ($\alpha$) and the harmonic oscillator constant as such:

$$
\begin{align}
\alpha=\frac{q_D^2}{k_D}\label{eqn:drude}
\end{align}
$$

* force constants for the Drude oscillator are fixed for all atom types at $500-1000\:Kcal\cdot mol^{-1}$

#### Charge Scaling/$k_{ij}$

* when using force fields that utilise partial charges for LJ interactions, since the partial charges will include effects for dispersion, which are now being explicitly modelled using the Drude oscillator, it's necessary to remove a certain amount of charge from the charge of the atom. This is the $k_{ij}$ parameter and is calculated using SAPT to obtain the ratio of 

\ce{LigParGen -> pdb + prm ->[psfgen] fftk ->[optimise params] fftk ->[manually update] il .ff}\\
\ce{LigParGen -> .itp + .lmp ->[convertLigParGen.py] il .ff}

### 

## QM
### QM in general

### Introduce Dethods (MP2/DFT)

### Introduce Dasis Dets

### Dispersion Dorrections


### Extrapolation to CBS
Where $X$ and $Y$ are the "cardinal" numbers of the basis used to extrapolate with (e.g. $X=3$ for aug-cc-pVTZ, $Y=4$ for aug-cc-pVQZ) \cite{Halkier1998}

* only works for correlation consistent basis sets, due to systematic improvements as $\zeta$ is increased
$3\to4\zeta$.

* the cardinal numbers $Y$ and $X$ should be one apart.
	* if these numbers are too low, then they don't contain enough information about the asymptotic convergence of the correlation energy to be particularly useful, hence introducing a large amount of error.

* \ref{eqn:mp2cbs} is an extrapolation of $3\to4\zeta$, to identify the CBS energy, where \ref{eqn:ccsdtcbs} is a CCSD(T) correction to the MP2/CBS energy

$$
\begin{align}
E(MP2/CBS)&=\frac{X^3E_X^{MP2}-Y^3E_Y^{MP2}}{X^3-Y^3}\label{eqn:mp2cbs}\\
E(CCSD(T)/CBS)&=E(MP2/CBS) + \big[E(CCSD(T)/DZ) - E(MP2/DZ)\big]\label{eqn:ccsdtcbs}
\end{align}
$$

* Seems to have errors of $\sim13\:KJ\cdot mol^{-1}$ for internal energy at $3\to4\zeta$, and I'm not sure about the CCSD(T) corrections. I'm not sure how the internal energy error translates to intermolecular energy errors.


### QM ILs
* Dispersion is important and can account for between 8 and 15\% of the interaction energy (-28 to $-59\:KJ\cdot mol^{-1}$)\cite{Izgorodina2014,Bernard2010}
	* in terms of dispersion effects; Imidazolium > pyrrolidinium > chloride/bromide

* This increases as you add more ion pairs, with four ion pairs increasing the dispersion interactions to 11-28% ($-68$ to $-81\:KJ\cdot mol^{-1}$)\cite{Izgorodina2014}

* M062X\cite{Zhao2008} and SRS-MP2\cite{Tan2017} highly recommended \cite{Izgorodina2017,Tan2017} 

* Many body effects

	* FMO allows for the ions to be calculated independently and for interaction energies to be iteratively accounted for. FMO2 allows for 2-body interactions, FMO3 allows for 3-body interactions.\cite{Fedorov2017}
	
	* FMO3-MP2 for interaction energies of accuracy \SI{0.2}{\kjmol}; \SI{<2}{\kjmol} for FMO2-MP2\cite{Izgorodina2012}

$$
\begin{align}
E_{FMO1}&=\sum_I^NE_I\label{eqn:fmo1}\\
E_{FMO2}&=E_{FMO1}+\sum_{I>J}^N(E_{IJ}-E_I-E_J)\label{eqn:fmo2}\\
E_{FMO3}&=E_{FMO2}+\sum_{I>J>K}^N
\begin{bmatrix}
(E_{IJK}-E_I-E_J-E_K)-(E_{IJ}-E_I-E_J)\\
-(E_{JK}-E_J-E_K)-(E_{IK}-E_K-E_I)
\end{bmatrix}\label{eqn:fmo3}
\end{align}
$$

* allows for molecular fragments to be added to scale linearly, rather than 
