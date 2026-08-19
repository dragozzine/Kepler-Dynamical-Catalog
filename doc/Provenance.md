# Data Provenance of the Kepler Dynamical Catalog

This file indicates how each data column of the Kepler Dynamical Catalog was calculated. Here, each column is also given a source id number; see Sources.md to see which sources should be cited if you use a particular column.


## Overview

The Kepler Dynamical Catalog (KDC) contains the results of a homogeneous-as-possible model fit to the entire Kepler catalog. The model used to generate the KDC was PhoDyMM, a photodynamical solver that finds all of a system's transiting exoplanets' masses, in addition to their orbital parameters. In essence, PhoDyMM uses the transit timing variations (TTVs) of multi-planet systems to solve for their masses. Rather than include reductive summary statistics of the PhoDyMM model runs, the KDC includes the posteriors of these runs, downsampled to 1000 posterior draws. 

However, PhoDyMM cannot be run on every Kepler system. Several categories of systems do not allow for TTV modeling:

1. Single planet systems (where only 1 transiting planet was detected) may display TTVs, but these are not interpretable without further data.
2. Some multiplanet systems would not converge in the PhoDyMM simulations.

Both of these types of systems are still included in the KDC; however, their posterior draws are obtained not from PhoDyMM simulation, but simply from drawing from flat priors (in the case of masses), from lightcurve-inferrable information (the photoeccentric effect for eccentricity and argument of periastron) or from preexisting catalog information (assuming Gaussianity for period and radius). 

The result is that the KDC contains 1000 posterior draws representing the best-possible information obtainable from TTVs and lightcurve modeling for each Kepler planet. 

In addition, there are two classes of planets included in the KDC that are not canonical Kepler planets:

1. Many "single transit" events were observed by the Kepler mission. Without a second transit, the periods of these probable exoplanets remain poorly constrained, but their presence was included in PhoDyMM simulations and is thus included in the KDC.
2. In some multiplanet systems, the addition of an extra, non-transiting planet helps to explain the observed TTVs. PhoDyMM simulations included this "hidden" planets where appropriate.




## Notes

For a multiplanet system, each row corresponds with 1 posterior draw from a PhoDyMM photodynamical system solution.

For a single planet system, each row corresponds with 1 draw from assumed Gaussian distributions given in DR25.

Headers ending with \_rowe were taken from Table of Lissauer et al. 2024, a system-level look at Kepler DR25.

Headers ending with \_hsu were taken from Table  of Hsu et al. 2019, a planetary occurrence-rate study.

## Columns

*Format: description \[unit] (type)*

#### `kmdc\_index`

Unique row index in KMDC file \[\[KOI]\[chisqrank]] (int) 

For singles, we use the mass rank instead, because no PhoDyMM chisq value exists for these systems---as a TTV solver, PhoDyMM can only be intelligibly run on multiplanet systems. chisqrank is 0-padded to 4 digits. Hidden planets are given a KOI of 0 for the planet part of the KOI number.

#### `M\_s`

Stellar mass \[solar masses] (float32)

#### `R\_s`

Stellar radius \[solar radii] (float32)

#### `c\_1`

Limb darkening coefficient 1 \[unitless] (float32)

#### `c\_2`

Limb darkening coefficient 2 \[unitless] (float32)

#### `R\_p/R\_s`

Planet-to-star radius ratio \[unitless] (float32)

#### `R\_pJ`

Planet radius \[Jupiter radii] (float32)

#### `R\_pE`

Planet radius \[Earth radii] (float32)

#### `M\_pE`

Planet mass \[Earth masses] (float32)

#### `rho\_p`

Planet density \[g/cm³] (float32)

#### `rho\_s`

Stellar density \[g/cm³] (float32)

#### `M\_p/M\_s`

Planet-to-star mass ratio \[unitless] (float32)

#### `M\_pJ`

Planet mass \[Jupiter masses] (float32)

#### `sqrt(e)\_cos(omega)`

√eccentricity × cos(ω) \[unitless] (float32)

#### `sqrt(e)\_sin(omega)`

√eccentricity × sin(ω) \[unitless] (float32)

#### `i`

Inclination \[degrees] (float32)

#### `Omega`

Longitude of ascending node \[degrees] (float32)

#### `e`

Orbital eccentricity \[unitless] (float32)

#### `omega`

Argument of periastron \[degrees] (float32)

#### `true\_anomaly`

(incorrect) true anomaly at observation \[degrees] (float32)

#### `eccentric\_anomaly`

Eccentric anomaly; incorrect because based on true\_anomaly \[degrees] (float32)

#### `mean\_anomaly`

Mean anomaly; incorrect because based on true\_anomaly \[degrees] (float32)

#### `mean\_longitude`

Mean longitude \[degrees] (float32)

#### `omega\_rad`

Argument of periastron \[radians] (float32)

#### `falsetrueanomaly`

Duplicate of true\_anomaly, but in radians \[radians] (float32)

#### `f`

True anomaly, but including the 2nd-order corrective term \[radians] (float32)

#### `eccentric\_anomaly\_hamann`

Eccentric anomaly including 2nd-order corrective term \[radians] (float32)

#### `false\_eccentric\_anomaly`

Duplicate of eccentric\_anomaly, but in radians \[radians] (float32)

#### `mean\_anomaly\_hamann`

Mean anomaly including 2nd-order corrective term \[radians] (float32)

#### `false\_mean\_anomaly`

Duplicate of eccentric\_anomaly, but in radians \[radians] (float32)

#### `mean\_angular\_motion`

Mean angular motion of planet \[radian/day] (float32)

#### `mean\_anomaly\_hamann\_800`

Mean anomaly including 2nd-order corrective term at epoch=800 \[radians] (float32)

#### `mean\_anomaly\_hamann\_850`

Mean anomaly including 2nd-order corrective term at epoch=850 \[radians] (float32)

#### `corrected\_mean\_anomaly\_800`

Mean anomaly at epoch=800 \[radians] (float32)

#### `eccentric\_anomaly\_hamann\_800`

Eccentric anomaly including 2nd-order corrective term at epoch=800 \[radians] (float32)

#### `eccentric\_anomaly\_hamann\_850`

Eccentric anomaly including 2nd-order corrective term at epoch=850 \[radians] (float32)

#### `true\_anomaly\_hamann\_800`

True anomaly including 2nd-order corrective term at epoch=800 \[radians] (float32)

#### `true\_anomaly\_hamann\_850`

True anomaly including 2nd-order corrective term at epoch=850 \[radians] (float32)

#### `corrected\_eccentric\_anomaly\_800`

Eccentric anomaly at epoch=800 \[radians] (float32)

#### `corrected\_true\_anomaly\_800`

True anomaly at epoch=800 \[radians] (float32)

#### `a\_AU`

Semi-major axis \[AU] (float32)

#### `a\_R\_s`

Semi-major axis \[stellar radii] (float32)

#### `peri\_AU`

Periastron distance \[AU] (float32)

#### `peri\_R\_s`

Periastron distance \[stellar radii] (float32)

#### `apo\_AU`

Apoastron distance \[AU] (float32)

#### `apo\_R\_s`

Apoastron distance \[stellar radii] (float32)

#### `d\_AU`

Instantaneous star–planet distance \[AU] (float32)

#### `d\_R\_s`

Instantaneous star–planet distance \[stellar radii] (float32)

#### `interior\_mass\_pJ`

The mass of the planets interior to this one \[Jupiter masses] (float32)

#### `mu`

Gravitational parameter of the planet (includes all interior mass in the system) \[AU³/days²] (float32)

#### `q`

Periastron distance (duplicate of peri\_AU) \[AU] (float32)

#### `Tp`

Epoch...something (DR needs to confirm what this is) \[days] (float32)

#### `x`

x-position in Jacobean coordinates in PhoDyMM integration \[AU] (float32)

#### `y`

y-position in Jacobean coordinates in PhoDyMM integration \[AU] (float32)

#### `z`

z-position in Jacobean coordinates in PhoDyMM integration \[AU] (float32)

#### `vx`

x-velocity in Jacobean coordinates in PhoDyMM integration \[AU/day] (float32)

#### `vy`

y-velocity in Jacobean coordinates in PhoDyMM integration \[AU/day] (float32)

#### `vz`

z-velocity in Jacobean coordinates in PhoDyMM integration \[AU/day] (float32)

#### `Period\_days`

Orbital period \[days] (float64)

#### `T\_0`

Transit center time \[BJD] (float32)

#### `b\_trans`

Transit impact parameter \[unitless] (float32)

#### `b\_occ`

Occultation impact parameter \[unitless] (float32)

#### `p\_trans`

Transit probability \[unitless] (float32)

#### `p\_occ`

Occultation probability \[unitless] (float32)

#### `T\_total\_hr`

Total transit duration \[hours] (float32)

#### `T\_full\_hr`

Full (flat-bottom) transit duration \[hours] (float32)

#### `K\_RV`

RV semi-amplitude \[m/s] (float32)

#### `occurrence\_rate\_hsu`

Occurrence rate from Hsu et al. (2019) \[unitless] (float32)

#### `E\_or\_hsu`

Upper-bound on occurrence rate \[unitless] (float32)

#### `e\_or\_hsu`

Lower-bound on occurrence rate \[unitless] (float32)

#### `hsu\_flag`

1 = included in Hsu+2019; 0 = not included \[unitless] (bool)

#### `multiplicity`

Number of planets in system \[unitless] (int)

#### `P/Pin`

Period ratio with inner planet \[unitless] (float32)

#### `P/Pout`

Period ratio with outer planet \[unitless] (float32)

#### `Tdur/Tdurin`

Transit duration ratio with inner planet \[unitless]  (float32)

#### `Tdur/Tdurout`

Transit duration ratio with outer planet \[unitless] (float32)

#### `R/Rin`

Radius ratio with inner planet \[unitless] (float32)

#### `R/Rout`

Radius ratio with outer planet \[unitless] (float32)

#### `M/Min`

Mass ratio with inner planet \[unitless] (float32)

#### `M/Mout`

Mass ratio with outer planet \[unitless] (float32)

#### `rho/rhoin`

Density ratio with inner planet \[unitless] (float32)

#### `rho/rhoout`

Density ratio with outer planet \[unitless] (float32)

#### `i-iin`

Inclination difference with inner planet \[degrees] (float32)

#### `iout-i`

Inclination difference with outer planet \[degrees] (float32)

#### `xiin`

ξ stability metric with inner planet \[unitless] (float32)

#### `xiout`

ξ stability metric with outer planet \[unitless] (float32)

#### `distin\_hillrad`

Distance to inner planet \[Hill radii] (float32)

#### `distout\_hillrad`

Distance to outer planet \[Hill radii] (float32)

#### `distin\_hillrad\_e`

Same as above, eccentric orbit \[Hill radii] (float32)

#### `distout\_hillrad\_e`

Same as above, eccentric orbit \[Hill radii] (float32)

#### `e/ein`

Eccentricity ratio with inner planet \[unitless] (float32)

#### `eout/e`

Eccentricity ratio with outer planet \[unitless] (float32)

#### `omega-omegain`

ω difference with inner planet \[degrees] (float32)

#### `omegaout-omega`

ω difference with outer planet \[degrees] (float32)

#### `dilute`

Dilution factor in flux \[unitless] (float32)

#### `chisq`

Chi-squared value of model fit \[unitless] (float32)

#### `Chain#`

MCMC chain number \[unitless] (int)

#### `chisq\_rank`

Chi-squared rank within chain \[unitless] (int)

#### `step\_number`

MCMC step number \[unitless] (int)

#### `phodymm\_index`

Index that indicates the row of the PhoDyMM dqa file this draw was pulled from \[unitless] (int)

#### `planet`

PhoDyMM planet number; lower number indicates shorter period \[unitless] (float32)

#### `is\_hidden\_planet`

binary flag to indicate if this is a hidden planet added in PhoDyMM integrations \[unitless] (bool)

#### `is\_monotransiting`

binary flag to indicate if this is a planet with a single transit \[unitless] (bool)

#### `KIC`

Kepler Input Catalog ID \[unitless] (int)

#### `KOI`

Kepler Object of Interest number \[unitless] (float32)

#### `Kepler`

Kepler planet name \[unitless] (string)

#### `Period\_days\_rowe`

Orbital period from Rowe et al. (2024) \[days] (float64)

#### `e\_Period\_rowe`

Error in Period\_rowe \[days] (float64)

#### `T0\_rowe`

Transit epoch from Rowe \[BJD] (float32)

#### `e\_T0\_rowe`

Error in T0\_rowe \[BJD] (float32)

#### `Rp/R\*\_rowe`

Radius ratio from Rowe \[unitless] (float32)

#### `E\_Rp/R\*\_rowe`

Upper error in Rp/R\*\_rowe \[unitless] (float32)

#### `e\_Rp/R\*\_rowe`

Uncertainty in Rp/R\*\_rowe \[unitless] (float32)

#### `b\_rowe`

Impact parameter from Rowe \[unitless] (float32)

#### `E\_b\_rowe`

Upper error in b\_rowe \[unitless] (float32)

#### `e\_b\_rowe`

Uncertainty in b\_rowe \[unitless] (float32)

#### `rho\*M\_rowe`

Stellar density from transit fit \[g/cm³] (float32)

#### `E\_rho\*M\_rowe`

Upper error in rho\*M\_rowe \[unitless] (float32)

#### `e\_rho\*M\_rowe`

Uncertainty in rho\*M\_rowe \[unitless] (float32)

#### `u1\_rowe`

LD coefficient 1 from Rowe \[unitless] (float32)

#### `u2\_rowe`

LD coefficient 2 from Rowe \[unitless] (float32)

#### `TTVflag\_rowe`

binary TTV flag from Rowe \[unitless] (bool)

#### `nTTobs\_rowe`

Number of observed transit times \[unitless] (int)

#### `nTT\_rowe`

Total number of transits \[unitless] (int)

#### `TDepth\_rowe`

Transit depth \[ppm] (float32)

#### `e\_TDepth\_rowe`

Error in transit depth \[ppm] (float32)

#### `TDur\_rowe`

Transit duration \[hours] (float32)

#### `e\_TDur\_rowe`

Error in TDur\_rowe \[hours] (float32)

#### `ATDur\_rowe`

Adjusted transit duration \[hours] (float32)

#### `e\_ATDur\_rowe`

Error in ATDur\_rowe \[hours] (float32)

#### `S/N\_rowe`

Signal-to-noise ratio \[unitless] (float32)

#### `MES\_rowe`

Multiple event statistic \[unitless] (float32)

#### `S/NImp\_rowe`

Impact parameter S/N \[unitless] (float32)

#### `chi2W\_rowe`

χ² with weights \[unitless] (float32)

#### `chi2WO\_rowe`

χ² without weights \[hours]  (float32)

#### `a/R\*\_rowe`

Scaled semi-major axis \[unitless] (float32)

#### `E\_a/R\*\_rowe`

Upper error in a/R\*\_rowe \[unitless] (float32)

#### `e\_a/R\*\_rowe`

Uncertainty in a/R\*\_rowe \[unitless] (float32)

#### `Inc\_rowe`

Inclination from Rowe \[degrees] (float32)

#### `E\_Inc\_rowe`

Upper error in Inc\_rowe \[degrees] (float32)

#### `e\_Inc\_rowe`

Uncertainty in Inc\_rowe \[degrees] (float32)

#### `Rp\_rowe`

Planet radius \[Earth radii] (float32)

#### `E\_Rp\_rowe`

Upper error in Rp\_rowe \[Earth radii] (float32)

#### `e\_Rp\_rowe`

Uncertainty in Rp\_rowe \[Earth radii] (float32)

#### `S0\_rowe`

Insolation flux \[Earth units] (float32)

#### `E\_S0\_rowe`

Upper error in S0\_rowe \[Earth units] (float32)

#### `e\_S0\_rowe`

Uncertainty in S0\_rowe \[Earth units] (float32)

#### `Kmag\_rowe`

Target star Kepler passband magnitude \[mag] (float32)

#### `rho\*\_rowe`

Mean stellar density from parameter tables \[g/cm³] (float32)

#### `E\_rho\*\_rowe`

Upper error in rho\*\_rowe \[g/cm³] (float32)

#### `e\_rho\*\_rowe`

Uncertainty in rho\*\_rowe \[g/cm³] (float32)

#### `Teff\_rowe`

Effective temperature \[K] (float32)

#### `e\_Teff\_rowe`

Error in Teff\_rowe \[K] (float32)

#### `R\*\_rowe`

Stellar radius \[solar radii] (float32)

#### `E\_R\*\_rowe`

Upper error in R\*\_rowe \[solar radii] (float32)

#### `e\_R\*\_rowe`

Uncertainty in R\*\_rowe \[solar radii] (float32)

#### `M\*\_rowe`

Stellar mass \[solar masses] (float32)

#### `E\_M\*\_rowe`

Upper error in M\*\_rowe \[solar masses] (float32)

#### `e\_M\*\_rowe`

Uncertainty in M\*\_rowe \[solar masses] (float32)

#### `log(g)\*\_rowe`

Stellar surface gravity \[log10(cm/s²)] (float32)

#### `E\_log(g)\*\_rowe`

Upper error in log(g)\*\_rowe \[log10(cm/s²)] (float32)

#### `e\_log(g)\*\_rowe`

Uncertainty in log(g)\*\_rowe \[log10(cm/s²)] (float32)

#### `Z\*\_rowe`

Stellar etallicity \[Fe/H] (float32)

#### `e\_Z\*\_rowe`

Uncertainty in Z\*\_rowe \[Fe/H] (float32)

#### `Source\_rowe`

Source catalog or method \[unitless] (string)

#### `Status\_rowe`

Vetting status / disposition \[unitless] (string)

#### `BRp\_rowe`

Berger et al. 2020 radius \[Earth radii] (float32)

#### `E\_BRp\_rowe`

Upper error in BRp\_rowe \[Earth radii] (float32)

#### `e\_BRp\_rowe`

Uncertainty in BRp\_rowe \[Earth radii] (float32)

#### `BS0\_rowe`

Berger et al. 2020 insolation flux \[Earth units] (float32)

#### `E\_BS0\_rowe`

Upper error in BS0\_rowe \[Earth units] (float32)

#### `e\_BS0\_rowe`

Uncertainty in BS0\_rowe \[Earth units] (float32)

#### `Brho\*\_rowe`

Berger et al. 2020 stellar density \[g/cm³] (float32)

#### `E\_Brho\*\_rowe`

Upper error in Brho\*\_rowe \[g/cm³] (float32)

#### `e\_Brho\*\_rowe`

Uncertainty in Brho\*\_rowe \[g/cm³] (float32)

#### `BTeff\_rowe`

Berger et al. 2020 effective temperature \[K] (float32)

#### `e\_BTeff\_rowe`

Uncertainty in BTeff\_rowe \[K] (float32)

#### `BR\*\_rowe`

Berger et al. 2020 stellar radius \[solar radii] (float32)

#### `E\_BR\*\_rowe`

Upper error in BR\*\_rowe \[solar radii] (float32)

#### `e\_BR\*\_rowe`

Uncertainty in BR\*\_rowe \[solar radii] (float32)

#### `BM\*\_rowe`

Berger et al. 2020 stellar mass \[solar masses] (float32)

#### `E\_BM\*\_rowe`

Upper error in BM\*\_rowe \[solar masses] (float32)

#### `e\_BM\*\_rowe`

Uncertainty in BM\*\_rowe \[solar masses] (float32)

#### `Blog(g)\*\_rowe`

Berger et al. 2020 log(g) \[log10(cm/s²)] (float32)

#### `E\_Blog(g)\*\_rowe`

Upper error in Blog(g) \[log10(cm/s²)] (float32)

#### `e\_Blog(g)\*\_rowe`

Uncertainty in Blog(g) \[log10(cm/s²)] (float32)

#### `BZ\*\_rowe`

Berger et al. 2020 metallicity \[Fe/H] (float32)

#### `e\_BZ\*\_rowe`

Uncertainty in BZ\*\_rowe \[Fe/H] (float32)

