class GeneralPrinciplesOfFoundationalSciencePrompt:
    CELL_STRUCTURE_AND_FUNCTION = (
        "You are an expert in foundational medical sciences. Generate a USMLE Step 2 CK-style question about cell structure and function. Return ONLY a valid JSON object as described in the schema."
    )
    BIOCHEMISTRY = (
        "You are an expert in foundational medical sciences. Generate a USMLE Step 2 CK-style question about biochemistry. Return ONLY a valid JSON object as described in the schema."
    )
    GENETICS = (
        "You are an expert in foundational medical sciences. Generate a USMLE Step 2 CK-style question about genetics. Return ONLY a valid JSON object as described in the schema."
    )
    MOLECULAR_BIOLOGY = (
        "You are an expert in foundational medical sciences. Generate a USMLE Step 2 CK-style question about molecular biology. Return ONLY a valid JSON object as described in the schema."
    )


class ImmuneSystemPrompt:
    INNATE_IMMUNITY = (
        "You are an immunology expert. Generate a USMLE Step 2 CK-style question about innate immunity. Return ONLY a valid JSON object as described in the schema."
    )
    ADAPTIVE_IMMUNITY = (
        "You are an immunology expert. Generate a USMLE Step 2 CK-style question about adaptive immunity. Return ONLY a valid JSON object as described in the schema."
    )
    IMMUNODEFICIENCIES = (
        "You are an immunology expert. Generate a USMLE Step 2 CK-style question about immunodeficiencies. Return ONLY a valid JSON object as described in the schema."
    )
    AUTOIMMUNE_DISORDERS = (
        "You are an immunology expert. Generate a USMLE Step 2 CK-style question about autoimmune disorders. Return ONLY a valid JSON object as described in the schema."
    )


class BloodAndLymphoreticularSystemPrompt:
    ANEMIAS = (
        "You are a hematology expert. Generate a USMLE Step 2 CK-style question about anemias. Return ONLY a valid JSON object as described in the schema."
    )
    LEUKEMIAS_AND_LYMPHOMAS = (
        "You are a hematology expert. Generate a USMLE Step 2 CK-style question about leukemias and lymphomas. Return ONLY a valid JSON object as described in the schema."
    )
    HEMOSTASIS_AND_COAGULATION_DISORDERS = (
        "You are a hematology expert. Generate a USMLE Step 2 CK-style question about hemostasis and coagulation disorders. Return ONLY a valid JSON object as described in the schema."
    )


class BehavioralHealthPrompt:
    PSYCHIATRIC_DISORDERS = (
        "You are a behavioral health expert. Generate a USMLE Step 2 CK-style question about psychiatric disorders. Return ONLY a valid JSON object as described in the schema."
    )
    SUBSTANCE_USE_DISORDERS = (
        "You are a behavioral health expert. Generate a USMLE Step 2 CK-style question about substance use disorders. Return ONLY a valid JSON object as described in the schema."
    )
    THERAPEUTIC_INTERVENTIONS = (
        "You are a behavioral health expert. Generate a USMLE Step 2 CK-style question about therapeutic interventions. Return ONLY a valid JSON object as described in the schema."
    )


class NervousSystemAndSpecialSensesPrompt:
    CENTRAL_NERVOUS_SYSTEM = (
        "You are a neurology expert. Generate a USMLE Step 2 CK-style question about the central nervous system. Return ONLY a valid JSON object as described in the schema."
    )
    PERIPHERAL_NERVOUS_SYSTEM = (
        "You are a neurology expert. Generate a USMLE Step 2 CK-style question about the peripheral nervous system. Return ONLY a valid JSON object as described in the schema."
    )
    SPECIAL_SENSES = (
        "You are a neurology expert. Generate a USMLE Step 2 CK-style question about special senses. Return ONLY a valid JSON object as described in the schema."
    )


class MusculoskeletalSystemSkinAndSubcutaneousTissuePrompt:
    BONES_AND_JOINTS = (
        "You are an expert in musculoskeletal and skin systems. Generate a USMLE Step 2 CK-style question about bones and joints. Return ONLY a valid JSON object as described in the schema."
    )
    MUSCLE_DISORDERS = (
        "You are an expert in musculoskeletal and skin systems. Generate a USMLE Step 2 CK-style question about muscle disorders. Return ONLY a valid JSON object as described in the schema."
    )
    SKIN_DISORDERS = (
        "You are an expert in musculoskeletal and skin systems. Generate a USMLE Step 2 CK-style question about skin disorders. Return ONLY a valid JSON object as described in the schema."
    )


class CardiovascularSystemPrompt:
    ARRHYTHMIAS = (
        "You are a cardiology expert. Generate a USMLE Step 2 CK-style question about arrhythmias. Return ONLY a valid JSON object as described in the schema."
    )
    HEART_FAILURE = (
        "You are a cardiology expert. Generate a USMLE Step 2 CK-style question about heart failure. Return ONLY a valid JSON object as described in the schema."
    )
    VASCULAR_DISEASES = (
        "You are a cardiology expert. Generate a USMLE Step 2 CK-style question about vascular diseases. Return ONLY a valid JSON object as described in the schema."
    )


class RespiratorySystemPrompt:
    OBSTRUCTIVE_LUNG_DISEASES = (
        "You are a pulmonology expert. Generate a USMLE Step 2 CK-style question about obstructive lung diseases. Return ONLY a valid JSON object as described in the schema."
    )
    RESTRICTIVE_LUNG_DISEASES = (
        "You are a pulmonology expert. Generate a USMLE Step 2 CK-style question about restrictive lung diseases. Return ONLY a valid JSON object as described in the schema."
    )
    PULMONARY_INFECTIONS = (
        "You are a pulmonology expert. Generate a USMLE Step 2 CK-style question about pulmonary infections. Return ONLY a valid JSON object as described in the schema."
    )


class GastrointestinalSystemPrompt:
    UPPER_GI_DISORDERS = (
        "You are a gastroenterology expert. Generate a USMLE Step 2 CK-style question about upper GI disorders. Return ONLY a valid JSON object as described in the schema."
    )
    LOWER_GI_DISORDERS = (
        "You are a gastroenterology expert. Generate a USMLE Step 2 CK-style question about lower GI disorders. Return ONLY a valid JSON object as described in the schema."
    )
    LIVER_AND_PANCREAS = (
        "You are a gastroenterology expert. Generate a USMLE Step 2 CK-style question about the liver and pancreas. Return ONLY a valid JSON object as described in the schema."
    )


class RenalUrinarySystemAndMaleReproductivePrompt:
    GLOMERULAR_DISEASES = (
        "You are a nephrology and urology expert. Generate a USMLE Step 2 CK-style question about glomerular diseases. Return ONLY a valid JSON object as described in the schema."
    )
    TUBULAR_DISORDERS = (
        "You are a nephrology and urology expert. Generate a USMLE Step 2 CK-style question about tubular disorders. Return ONLY a valid JSON object as described in the schema."
    )
    MALE_REPRODUCTIVE_DISORDERS = (
        "You are a nephrology and urology expert. Generate a USMLE Step 2 CK-style question about male reproductive disorders. Return ONLY a valid JSON object as described in the schema."
    )


class PregnancyChildbirthAndPuerperiumPrompt:
    NORMAL_PREGNANCY = (
        "You are an obstetrics expert. Generate a USMLE Step 2 CK-style question about normal pregnancy. Return ONLY a valid JSON object as described in the schema."
    )
    PREGNANCY_COMPLICATIONS = (
        "You are an obstetrics expert. Generate a USMLE Step 2 CK-style question about pregnancy complications. Return ONLY a valid JSON object as described in the schema."
    )
    POSTPARTUM_CARE = (
        "You are an obstetrics expert. Generate a USMLE Step 2 CK-style question about postpartum care. Return ONLY a valid JSON object as described in the schema."
    )


class FemaleReproductiveSystemAndBreastPrompt:
    MENSTRUAL_DISORDERS = (
        "You are a gynecology and breast health expert. Generate a USMLE Step 2 CK-style question about menstrual disorders. Return ONLY a valid JSON object as described in the schema."
    )
    GYNECOLOGIC_ONCOLOGY = (
        "You are a gynecology and breast health expert. Generate a USMLE Step 2 CK-style question about gynecologic oncology. Return ONLY a valid JSON object as described in the schema."
    )
    BREAST_DISORDERS = (
        "You are a gynecology and breast health expert. Generate a USMLE Step 2 CK-style question about breast disorders. Return ONLY a valid JSON object as described in the schema."
    )


class EndocrineSystemPrompt:
    DIABETES_MELLITUS = (
        "You are an endocrinology expert. Generate a USMLE Step 2 CK-style question about diabetes mellitus. Return ONLY a valid JSON object as described in the schema."
    )
    THYROID_DISORDERS = (
        "You are an endocrinology expert. Generate a USMLE Step 2 CK-style question about thyroid disorders. Return ONLY a valid JSON object as described in the schema."
    )
    ADRENAL_DISORDERS = (
        "You are an endocrinology expert. Generate a USMLE Step 2 CK-style question about adrenal disorders. Return ONLY a valid JSON object as described in the schema."
    )


class MultisystemProcessesAndDisordersPrompt:
    SEPSIS = (
        "You are an expert in multisystem disorders. Generate a USMLE Step 2 CK-style question about sepsis. Return ONLY a valid JSON object as described in the schema."
    )
    SHOCK = (
        "You are an expert in multisystem disorders. Generate a USMLE Step 2 CK-style question about shock. Return ONLY a valid JSON object as described in the schema."
    )
    SYSTEMIC_INFLAMMATORY_RESPONSE_SYNDROME = (
        "You are an expert in multisystem disorders. Generate a USMLE Step 2 CK-style question about systemic inflammatory response syndrome. Return ONLY a valid JSON object as described in the schema."
    )


class BiostatisticsEpidemiologyPopulationHealthInterpretationOfMedicalLiteraturePrompt:
    STUDY_DESIGN = (
        "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK-style question about study design. Return ONLY a valid JSON object as described in the schema."
    )
    STATISTICAL_ANALYSIS = (
        "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK-style question about statistical analysis. Return ONLY a valid JSON object as described in the schema."
    )
    POPULATION_HEALTH = (
        "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK-style question about population health. Return ONLY a valid JSON object as described in the schema."
    )


class SocialSciencesLegalEthicalIssuesProfessionalismSystemsBasedPracticePatientSafetyPrompt:
    MEDICAL_ETHICS = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about medical ethics. Return ONLY a valid JSON object as described in the schema."
    )
    PATIENT_SAFETY = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about patient safety. Return ONLY a valid JSON object as described in the schema."
    )
    PROFESSIONALISM = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about professionalism. Return ONLY a valid JSON object as described in the schema."
    )


class BiochemistryPrompt:
    AMINO_ACIDS_PROTEINS_AND_ENZYMES = (
        "You are a biochemistry expert. Generate a USMLE Step 1 question about amino acid metabolism or enzyme defects (e.g., PKU, homocystinuria, urea cycle defects). "
        "Include a clinical vignette, relevant labs, 4–5 answer options, correct answer, and short explanation. "
        "Return ONLY a valid JSON object as described in the schema."
    )

    BIOENERGETICS_AND_CARBOHYDRATE_METABOLISM = (
        "You are a biochemistry expert. Create a USMLE Step 1 vignette-style question testing glycolysis, gluconeogenesis, or a glycogen storage disease. "
        "Include age, symptoms (e.g., fasting hypoglycemia, hepatomegaly), and relevant metabolic labs. "
        "Provide 5 choices, correct answer, and brief explanation. Return ONLY a valid JSON object as described in the schema."
    )

    LIPID_METABOLISM = (
        "You are a biochemistry expert. Write a Step 1-style question on fatty acid oxidation, ketone production, or lipoprotein disorders (e.g., MCAD, abetalipoproteinemia, familial hypercholesterolemia). "
        "Include a clinical vignette and 4–5 plausible answer choices with explanation. Return ONLY a valid JSON object as described in the schema."
    )

    CELL_AND_MOLECULAR_BIOLOGY = (
        "You are a cell and molecular biology expert. Generate a USMLE Step 1 question focused on DNA replication, transcription, RNA processing, or cell organelles. "
        "Use a genetic disorder or cell biology concept (e.g., xeroderma pigmentosum, I-cell disease). Include correct answer and short explanation. "
        "Return ONLY a valid JSON object as described in the schema."
    )

    MISCELLANEOUS = (
        "You are a biochemistry expert. Create a Step 1 MCQ that tests understanding of vitamin/cofactor deficiencies (e.g., B1, B12, biotin) or integrated metabolism (e.g., alcohol metabolism, starvation, fasting). "
        "Include a short clinical vignette, answer choices, correct answer, and explanation. Return ONLY a valid JSON object as described in the schema."
    )
