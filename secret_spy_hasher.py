# ==========================================
# HEALTH INSURANCE PORTABILITY AND ACCOUNTABILITY ACT (HIPAA)
# COMPLIANCE: DATA ANONYMIZATION ENGINE
# ==========================================

import hashlib

# 1. DATA INPUT LAYER (SENSITIVE PROTECTED HEALTH INFORMATION)
protected_patient_name = "Chidi Okafor"
clinical_diagnostic_payload = "Diagnosed: Severe Microcytic Anemia & Thrombocytopenia"

# 2. CRYPTOGRAPHIC TRANSFORM ENGINE
# We encode the string to bytes, then run it through the SHA-256 mathematical algorithm.
# .hexdigest() converts the binary hash into clean, readable text characters.
hashed_identity = hashlib.sha256(protected_patient_name.encode()).hexdigest()

# 3. COMPLIANT DATA OUTPUT
print("--- SECURE PROTOCOL INGESTION COMPLETE ---")
print("Cleartext Name Masked Successfully.")
print("Generated Unique Token:", hashed_identity)
print("\n[Database Entry Created Below]")
print("Token Ref: " + hashed_identity + " | Metric Payload: " + clinical_diagnostic_payload)
