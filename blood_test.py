# ==========================================
# CLINICAL HEMATOLOGY ANALYSIS ENGINE
# SYSTEM ENGINE DESIGNED BY A MOBILE INTERFACE
# ==========================================

# 1. ESTABLISH CLINICAL REFERENCE BOUNDARIES (STANDARD ADULT RANGES)
# These represent normal physiological baselines
NORMAL_RBC_MIN = 4.5  # Red Blood Cells (million/µL)
NORMAL_WBC_MAX = 11.0 # White Blood Cells (thousand/µL)
NORMAL_PLT_MIN = 150  # Platelets (thousand/µL)

# 2. PATIENT VARIABLE INGESTION (MOCK PATIENT DATA LAYER)
# Inputting parameters derived from a simulated blood panel draw
patient_rbc = 3.2   # Below baseline (Indicative of Anemia)
patient_wbc = 14.8  # Above baseline (Indicative of Leukocytosis/Infection)
patient_plt = 95    # Below baseline (Indicative of Thrombocytopenia)

print("--- EXECUTING CELLULAR METRIC EVALUATION ---")

# 3. CONDITIONAL EXECUTION MATRIX (THE ENGINE LOGIC)

# Red Blood Cell (RBC) Evaluation Loop
if patient_rbc < NORMAL_RBC_MIN:
    print("CRITICAL ALERT: RBC Count is Low.")
    print("Clinical Implication: Insufficient erythrocyte mass; screen for Anemia.")

# White Blood Cell (WBC) Evaluation Loop
if patient_wbc > NORMAL_WBC_MAX:
    print("CRITICAL ALERT: WBC Count is Elevated.")
    print("Clinical Implication: Acute immune response; screen for underlying infection or inflammation.")

# Platelet (PLT) Evaluation Loop
if patient_plt < NORMAL_PLT_MIN:
    print("CRITICAL ALERT: Platelet Count is Low.")
    print("Clinical Implication: Impaired coagulation cascade; high risk of hemorrhage/bleeding.")
