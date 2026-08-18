"""Column groupings for KDC.csv, used for chunked compression/splitting."""

column_groups = {
    "part1_":         ["kdc_index", "multiplicity",'M_s', 'R_s', 'c_1', 'c_2', 'R_p/R_s', 'R_pJ', 'R_pE','M_pE'],
    
    "part2_":     ["kdc_index", "multiplicity", 'rho_p', 'rho_s', 'M_p/M_s', 'M_pJ', 'sqrt(e)_cos(omega)', 'sqrt(e)_sin(omega)'],
    
    "part3_":        ["kdc_index", "multiplicity", 'i', 'Omega', 'e', 'omega', 'true_anomaly', 'eccentric_anomaly'],
    
    "part4_": ["kdc_index", "multiplicity",'mean_anomaly','mean_longitude', 'omega_rad', 'falsetrueanomaly', 'f'],
    
    "part5_":    ["kdc_index", "multiplicity", 'eccentric_anomaly_hamann', 'false_eccentric_anomaly', 'mean_anomaly_hamann', 'false_mean_anomaly', 
                          'mean_angular_motion', 'mean_anomaly_hamann_800'],
    
    "part6_":        ["kdc_index", "multiplicity", 'mean_anomaly_hamann_850', 'corrected_mean_anomaly_800', 'eccentric_anomaly_hamann_800', 
                          'eccentric_anomaly_hamann_850', 'true_anomaly_hamann_800', 'a_AU', 'a_R_s', 'peri_AU'],
    
    "part7_":        ["kdc_index", "multiplicity", 'peri_R_s', 'apo_AU', 'apo_R_s', 'd_AU', 'd_R_s', 'interior_mass_pJ'],
    
    "part8_":       ["kdc_index", "multiplicity", 'mu', 'q', 'Tp', 'x', 'y','z', 'vx', 'vy', 'vz'],
    
    "part9_":  ["kdc_index", "multiplicity", 'Period_days', 'T_0', 'b_trans', 'b_occ', 'p_trans'],
    
    "part10_":  ["kdc_index", "multiplicity", 'p_occ', 'T_total_hr', 'T_full_hr', 'K_RV','occurrence_rate_hsu', 'E_or_hsu', 'e_or_hsu', 
                          'hsu_flag', 'P/Pin', 'P/Pout', 'Tdur/Tdurin', 'Tdur/Tdurout'],
    
    "part11_":  ["kdc_index", "multiplicity", 'R/Rin', 'R/Rout', 'M/Min','M/Mout', 'rho/rhoin', 'rho/rhoout', 'i-iin', 'iout-i', 'xiin', 'xiout', 
                 'distin_hillrad', 'distout_hillrad', 'distin_hillrad_e', 'distout_hillrad_e', 'e/ein', 'eout/e', 'omega-omegain', 'omegaout-omega'],
    
    "part12_":   ["kdc_index", "multiplicity", 'dilute', 'chisq', 'Chain#', 'chisq_rank', 'step_number', 'phodymm_index', 'planet', 'is_hidden_planet', 
                  'is_monotransiting', 'KIC','KOI', 'Kepler', 'Period_days_rowe', 'e_Period_rowe', 'T0_rowe', 'e_T0_rowe', 'Rp/R*_rowe', 'E_Rp/R*_rowe', 
                  'e_Rp/R*_rowe', 'b_rowe', 'E_b_rowe','e_b_rowe', 'rho*M_rowe', 'E_rho*M_rowe', 'e_rho*M_rowe', 'u1_rowe', 'u2_rowe','TTVflag_rowe', 
                  'nTTobs_rowe', 'nTT_rowe', 'TDepth_rowe','e_TDepth_rowe', 'TDur_rowe', 'e_TDur_rowe', 'ATDur_rowe', 'e_ATDur_rowe','S/N_rowe', 'MES_rowe', 
                  'S/NImp_rowe', 'chi2W_rowe', 'chi2WO_rowe', 'a/R*_rowe', 'E_a/R*_rowe', 'e_a/R*_rowe','Inc_rowe', 'E_Inc_rowe', 'e_Inc_rowe', 'Rp_rowe', 
                  'E_Rp_rowe', 'e_Rp_rowe', 'S0_rowe', 'E_S0_rowe', 'e_S0_rowe', 'Kmag_rowe', 'rho*_rowe', 'E_rho*_rowe', 'e_rho*_rowe', 'Teff_rowe',
                  'e_Teff_rowe', 'R*_rowe', 'E_R*_rowe', 'e_R*_rowe','M*_rowe','true_anomaly_hamann_850', 'corrected_eccentric_anomaly_800', 
                  'corrected_true_anomaly_800','E_M*_rowe', 'e_M*_rowe', 'log(g)*_rowe', 'E_log(g)*_rowe', 'e_log(g)*_rowe', 'Z*_rowe', 'e_Z*_rowe', 
                  'Source_rowe', 'Status_rowe', 'BRp_rowe', 'E_BRp_rowe', 'e_BRp_rowe', 'BS0_rowe', 'E_BS0_rowe', 'e_BS0_rowe', 'Brho*_rowe', 'E_Brho*_rowe', 
                  'e_Brho*_rowe', 'BTeff_rowe', 'e_BTeff_rowe', 'BR*_rowe', 'E_BR*_rowe', 'e_BR*_rowe', 'BM*_rowe', 'E_BM*_rowe', 'e_BM*_rowe', 'Blog(g)*_rowe',
                  'E_Blog(g)*_rowe', 'e_Blog(g)*_rowe', 'BZ*_rowe','e_BZ*_rowe']
}