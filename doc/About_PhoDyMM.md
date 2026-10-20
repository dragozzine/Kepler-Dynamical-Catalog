# PhoDyMM

The primary software used to process our data is the PhotoDynamical Multi-Planet Model, otherwise known as PhoDyMM. For a detailed description of the model's inner workings, readers are directed to Ragozzine et al. in prep., Jones et al. in preparation or the model repository [https://github.com/dragozzine/PhoDyMM]. This document gives a short summary of the model's capabilities and shortcomings:

PhoDyMM is a Bayesian inference tool that jointly models both the Kepler lightcurves and the dynamical interactions between planetary bodies.

For a Kepler system, PhoDyMM fits each orbiting planet's period (*P*), time of conjunction (*T₀*), eccentricity (*e*), argument of periastron (*ω*), inclination (*i*), radius (*R_p*), and mass (*M_p*). PhoDyMM also fits for the stellar properties of the system, namely the star's mass (*M\**), radius (*R\**), limb darkening coefficients (*c₁* and *c₂*) and background contamination (*dilute*). A summary of each fitted parameter, as well as its units, is given in the table below. This is done through the implementation of a Differential Evolution Markov Chain Monte Carlo fitting algorithm ([Ter Braak 2006](https://ui.adsabs.harvard.edu/abs/2006S%26C....16..239T)) coupled to an n-body integrator.


| Parameter | Symbol | Units |
|---|---|---|
| Period | *P* | days |
| Epoch of conjunction | *T₀* | days |
| Eccentricity | *e* | – |
| Argument of Periastron | *ω* | degrees |
| Inclination | *i* | degrees |
| Planetary Radius | *R_p* | *R*⊕ |
| Planetary Mass | *M_p* | *M*⊕ |
| Stellar Mass | *M\** | *M*☉ |
| Stellar Radius | *R\** | *R*☉ |
| Limb Darkening 1 | *c₁* | – |
| Limb Darkening 2 | *c₂* | – |
| Background contamination | *dilute* | – |

PhoDyMM's approach contains several distinct advantages over traditional TTV modeling:

1. PhoDyMM fits to the entire lightcurve instead of transit time metadata, the current TTV modeling standard. This makes the analysis more self-consistent, pulling data straight from Kepler with no intermediate processes and no reduction of data into a single time of center transit. The inclusion of the full data allows for atypical lightcurves to be modeled, e.g., high-eccentricity, non-standard shapes.
2. Because it utilizes Bayesian methods, PhoDyMM is able to return a full posterior for each free parameter, rather than a single best-likelihood value.
3. PhoDyMM's joint modeling of all relevant quantities allows analyses inclusive of all potential factors.
4. Unlike previous systematic TTV modelers, PhoDyMM incorporates both the long- and short-cadence Kepler data to increase TTV precision (by up to 200% for the smallest planets).
5. PhoDyMM imposes no minimum S/N requirement on its transits, allowing fainter signals to be modeled.
6. Per likelihood evaluation, PhoDyMM is not much slower than conventional lightcurve modeling. (However, the number of calculations needed to build a full posterior mean that Jones et al.'s runs were extremely computationally intensive).
7. Even in systems without tightly-constrained planetary masses, PhoDyMM can return a mass upper limit.
8. PhoDyMM has been "battle-tested," producing useful scientific results and characterizing the complex gravitational interplay between planets in a variety of studies; it has already been used for individual systems, as in [Mills et al. 2016](https://ui.adsabs.harvard.edu/abs/2016Natur.533..509M), [2017](https://ui.adsabs.harvard.edu/abs/2017ApJ...838L..11M), [2021](https://ui.adsabs.harvard.edu/abs/2021AJ....162..114M); it was also recently used for a catalog-wide analysis, Jones et al. in prep., from which we build our catalog.

---
