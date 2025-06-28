Biochemistry = {
    "AMINO_ACIDS_PROTEINS_AND_ENZYMES": {
        "prompt": (
            "You are a biochemistry expert. Generate a USMLE Step 1 question about amino acid metabolism or enzyme defects (e.g., PKU, homocystinuria, urea cycle defects). "
            "Include a clinical vignette, relevant labs, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A 5-month-old infant is brought to the emergency department due to poor feeding, vomiting, and lethargy. 
            On physical examination, the child is hypotonic and exhibits a mousy body odor. 
            Blood analysis reveals elevated phenylalanine and low tyrosine levels. Genetic analysis confirms a mutation in the PAH gene.
             Despite adequate dietary phenylalanine restriction, the patient continues to have neurological deficits.
            Further analysis reveals a deficiency in an enzyme responsible for the regeneration of tetrahydrobiopterin (BH₄) from dihydrobiopterin (BH₂). 
            Which of the following enzymes is most likely deficient in this patient?""",
            "choices": ["A) Dihydropteridine reductase", "B) Phenylalanine hydroxylase", "C) Tyrosine hydroxylase", "D) Homogentisate oxidase", "E) Tryptophan hydroxylase"],
            "answer": "A) Dihydropteridine reductase", 
            "explanation": """This infant presents with phenylketonuria (PKU) symptoms but does not improve with dietary phenylalanine restriction alone, suggesting atypical or malignant PKU.
            In classic PKU, the enzyme phenylalanine hydroxylase (PAH) is deficient. However, PAH also requires tetrahydrobiopterin (BH₄) as a cofactor to function properly.
            A defect in the enzyme dihydropteridine reductase (DHPR) impairs the regeneration of BH₄ from its oxidized form, dihydrobiopterin (BH₂). 
            Without sufficient BH₄, several important hydroxylase reactions fail. These include the conversion of phenylalanine to tyrosine by PAH, the conversion of tyrosine to DOPA by tyrosine hydroxylase, and the conversion of tryptophan to 5-hydroxytryptophan (5-HTP) by tryptophan hydroxylase.
            The failure of these reactions leads to sa broader neurotransmitter deficiency, which explains the continued neurological deterioration despite adequate dietary management. 
            Therefore, a deficiency in DHPR is the underlying cause of malignant PKU in this case.""",
        }
    },

    "BIOENERGETICS_AND_CARBOHYDRATE_METABOLISM": {
        "prompt": (
            "You are a biochemistry expert. Create a USMLE Step 1 vignette-style question testing glycolysis, gluconeogenesis, or a glycogen storage disease. "
            "Include age, symptoms (e.g., fasting hypoglycemia, hepatomegaly), and relevant metabolic labs. "
            "Provide 5 choices, correct answer, and brief explanation. Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A 3-month-old infant is brought to the clinic due to recurrent episodes of irritability and drowsiness, especially after missed feedings. Physical examination reveals hepatomegaly. Laboratory studies show hypoglycemia, elevated lactate, elevated triglycerides, and elevated uric acid. A liver biopsy reveals excessive glycogen accumulation with a normal structure. Genetic testing identifies a deficiency in glucose-6-phosphatase.
            Which of the following is the most likely diagnosis?""",
            "choices": ["A) Pompe disease", "B) McArdle disease", "C) Cori disease", "D) Von Gierke disease", "E) Her's disease"],
            "answer": "D) Von Gierke disease",
            "explanation": """This infant shows signs of impaired fasting tolerance, evidenced by hypoglycemia and lethargy during periods without food. The metabolic findings — hypoglycemia, lactic acidosis, hyperlipidemia, and hyperuricemia — are classic for a defect in glucose release during fasting. The key clue is the liver biopsy showing an excess of structurally normal glycogen, which indicates that glycogen is being synthesized correctly but cannot be broken down efficiently to maintain blood glucose.
            The enzyme glucose-6-phosphatase catalyzes the final step in both glycogenolysis and gluconeogenesis: converting glucose-6-phosphate into free glucose that can enter the bloodstream. A deficiency in this enzyme results in the accumulation of glucose-6-phosphate within hepatocytes. This leads to diversion into glycolysis (producing excess lactate), lipogenesis (causing hypertriglyceridemia), and the pentose phosphate pathway (producing purine degradation and hyperuricemia). Because glucose cannot be mobilized from the liver, the patient develops severe fasting hypoglycemia.
            This presentation is diagnostic of Von Gierke disease, also known as Glycogen Storage Disease Type I.""",
        }
    },
    

    "LIPID_METABOLISM": {
        "prompt": (
            "You are a biochemistry expert. Write a Step 1-style question on fatty acid oxidation, ketone production, or lipoprotein disorders (e.g., MCAD, abetalipoproteinemia, familial hypercholesterolemia). "
            "Include a clinical vignette and 5 plausible answer choices with explanation. Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A 4-month-old male is brought to the pediatrician due to failure to thrive and hepatomegaly. His parents report that he has had several episodes of vomiting and lethargy, especially after feeding. Laboratory studies reveal hypoglycemia, elevated liver transaminases, hyperammonemia, and elevated dicarboxylic acids in the urine. Further testing shows low levels of free carnitine in plasma.
            Which of the following is the most likely underlying cause of this patient's condition?""",
            "choices": ["A) Medium-chain acyl-CoA dehydrogenase deficiency", "B) Primary carnitine deficiency", "C) Carnitine palmitoyltransferase II deficiency", "D) Systemic carnitine transporter overexpression", "E) Acetyl-CoA carboxylase deficiency"],
            "answer": "B) Primary carnitine deficiency",
            "explanation": """This infant presents with signs of impaired fatty acid oxidation, such as fasting hypoglycemia without ketone production (hypoketotic hypoglycemia), hepatomegaly, and lethargy. The presence of elevated dicarboxylic acids in the urine indicates that omega-oxidation is being used as a backup pathway due to defective beta-oxidation.
            The key lab finding here is low plasma free carnitine, which suggests a defect in carnitine transport into cells. Carnitine is essential for the transport of long-chain fatty acids into the mitochondria for beta-oxidation. Without carnitine, fatty acids cannot be used as an energy source during fasting or metabolic stress, resulting in energy deficiency and toxic accumulation of fatty acid intermediates.
            Primary carnitine deficiency is caused by a defect in the OCTN2 carnitine transporter. This leads to low intracellular and plasma carnitine levels and manifests as hypoketotic hypoglycemia, hepatomegaly, muscle weakness, and cardiomyopathy, typically in infancy or early childhood.
            Medium-chain acyl-CoA dehydrogenase (MCAD) deficiency can present similarly but would have normal or elevated carnitine levels and typically does not show elevated dicarboxylic acids to the same extent as a transport defect. CPT-II deficiency more commonly presents in muscle tissue with exercise-induced pain in older children or adults.""",
        }
    },
     "CELL_AND_MOLECULAR_BIOLOGY": {
        "prompt": (
            "You are a cell and molecular biology expert. Generate a USMLE Step 1 question focused on DNA replication, transcription, RNA processing, or cell organelles. "
            "Use a genetic disorder or cell biology concept (e.g., xeroderma pigmentosum, I-cell disease). Include correct answer and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A researcher is studying the effects of proteasome inhibition on cell cycle progression. She treats cultured human fibroblasts with a small molecule that selectively inhibits the 26S proteasome. After treatment, the cells are found to accumulate in the G1 phase and fail to progress into S phase. Which of the following molecules is most likely responsible for this arrest?""",
            "choices": ["A) Cyclin D", "B) p53", "C) Retinoblastoma protein (Rb)", "D) CDK4", "E) E2F"],
            "answer": "C) Retinoblastoma protein (Rb)",
            "explanation": """The 26S proteasome is responsible for degrading ubiquitinated proteins, a key mechanism for controlling levels of regulatory molecules in the cell cycle. In this scenario, inhibition of the proteasome prevents degradation of certain proteins, leading to accumulation or persistent activity.
            Progression from the G1 phase into the S phase of the cell cycle is tightly regulated by the interaction between the retinoblastoma protein (Rb) and the E2F family of transcription factors. In its unphosphorylated (active) state, Rb binds to E2F, preventing transcription of genes required for S phase entry. As the cell progresses through G1, cyclin D–CDK4/6 complexes phosphorylate Rb, inactivating it and releasing E2F to initiate S phase gene transcription.
            If the proteasome is inhibited, proteins like the active, hypophosphorylated form of Rb may accumulate because they are not being properly degraded or regulated. As a result, Rb continues to bind and inhibit E2F, blocking the G1-to-S transition and causing G1 arrest.
            While cyclin D, CDK4, and E2F are important regulators, the key inhibitory checkpoint being affected here is the persistent activity of Rb, making it the correct answer."""
        }
    },

    # "MISCELLANEOUS": {
    #     "prompt": (
    #         "You are a biochemistry expert. Create a Step 1 MCQ that tests understanding of vitamin/cofactor deficiencies (e.g., B1, B12, biotin) or integrated metabolism (e.g., alcohol metabolism, starvation, fasting). "
    #         "Include a short clinical vignette, answer choices, correct answer, and explanation. Return ONLY a valid JSON object as described in the schema."
    #     ),
    #     "sample_question": {
    #         "question": "What is the correct answer?",
    #         "answer": "A",
    #         "explanation": "This is the explanation for the answer."
    #     }
    # }
}


class Genetics:
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


class AllergiesAndImmunology:
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


class Cardiovascular:
    ANEMIAS = (
        "You are a hematology expert. Generate a USMLE Step 2 CK-style question about anemias. Return ONLY a valid JSON object as described in the schema."
    )
    LEUKEMIAS_AND_LYMPHOMAS = (
        "You are a hematology expert. Generate a USMLE Step 2 CK-style question about leukemias and lymphomas. Return ONLY a valid JSON object as described in the schema."
    )
    HEMOSTASIS_AND_COAGULATION_DISORDERS = (
        "You are a hematology expert. Generate a USMLE Step 2 CK-style question about hemostasis and coagulation disorders. Return ONLY a valid JSON object as described in the schema."
    )


class Microbiology:
    PSYCHIATRIC_DISORDERS = (
        "You are a behavioral health expert. Generate a USMLE Step 2 CK-style question about psychiatric disorders. Return ONLY a valid JSON object as described in the schema."
    )
    SUBSTANCE_USE_DISORDERS = (
        "You are a behavioral health expert. Generate a USMLE Step 2 CK-style question about substance use disorders. Return ONLY a valid JSON object as described in the schema."
    )
    THERAPEUTIC_INTERVENTIONS = (
        "You are a behavioral health expert. Generate a USMLE Step 2 CK-style question about therapeutic interventions. Return ONLY a valid JSON object as described in the schema."
    )


class Dermatology:
    CENTRAL_NERVOUS_SYSTEM = (
        "You are a neurology expert. Generate a USMLE Step 2 CK-style question about the central nervous system. Return ONLY a valid JSON object as described in the schema."
    )
    PERIPHERAL_NERVOUS_SYSTEM = (
        "You are a neurology expert. Generate a USMLE Step 2 CK-style question about the peripheral nervous system. Return ONLY a valid JSON object as described in the schema."
    )
    SPECIAL_SENSES = (
        "You are a neurology expert. Generate a USMLE Step 2 CK-style question about special senses. Return ONLY a valid JSON object as described in the schema."
    )


class Pathology:
    BONES_AND_JOINTS = (
        "You are an expert in musculoskeletal and skin systems. Generate a USMLE Step 2 CK-style question about bones and joints. Return ONLY a valid JSON object as described in the schema."
    )
    MUSCLE_DISORDERS = (
        "You are an expert in musculoskeletal and skin systems. Generate a USMLE Step 2 CK-style question about muscle disorders. Return ONLY a valid JSON object as described in the schema."
    )
    SKIN_DISORDERS = (
        "You are an expert in musculoskeletal and skin systems. Generate a USMLE Step 2 CK-style question about skin disorders. Return ONLY a valid JSON object as described in the schema."
    )


class Pharmacology:
    ARRHYTHMIAS = (
        "You are a cardiology expert. Generate a USMLE Step 2 CK-style question about arrhythmias. Return ONLY a valid JSON object as described in the schema."
    )
    HEART_FAILURE = (
        "You are a cardiology expert. Generate a USMLE Step 2 CK-style question about heart failure. Return ONLY a valid JSON object as described in the schema."
    )
    VASCULAR_DISEASES = (
        "You are a cardiology expert. Generate a USMLE Step 2 CK-style question about vascular diseases. Return ONLY a valid JSON object as described in the schema."
    )


class EarNoseAndThroat:
    OBSTRUCTIVE_LUNG_DISEASES = (
        "You are a pulmonology expert. Generate a USMLE Step 2 CK-style question about obstructive lung diseases. Return ONLY a valid JSON object as described in the schema."
    )
    RESTRICTIVE_LUNG_DISEASES = (
        "You are a pulmonology expert. Generate a USMLE Step 2 CK-style question about restrictive lung diseases. Return ONLY a valid JSON object as described in the schema."
    )
    PULMONARY_INFECTIONS = (
        "You are a pulmonology expert. Generate a USMLE Step 2 CK-style question about pulmonary infections. Return ONLY a valid JSON object as described in the schema."
    )


class BiostatsAndEpidemiology:
    UPPER_GI_DISORDERS = (
        "You are a gastroenterology expert. Generate a USMLE Step 2 CK-style question about upper GI disorders. Return ONLY a valid JSON object as described in the schema."
    )
    LOWER_GI_DISORDERS = (
        "You are a gastroenterology expert. Generate a USMLE Step 2 CK-style question about lower GI disorders. Return ONLY a valid JSON object as described in the schema."
    )
    LIVER_AND_PANCREAS = (
        "You are a gastroenterology expert. Generate a USMLE Step 2 CK-style question about the liver and pancreas. Return ONLY a valid JSON object as described in the schema."
    )


class EndocrineAndDiabetesAndMetabolism:
    GLOMERULAR_DISEASES = (
        "You are a nephrology and urology expert. Generate a USMLE Step 2 CK-style question about glomerular diseases. Return ONLY a valid JSON object as described in the schema."
    )
    TUBULAR_DISORDERS = (
        "You are a nephrology and urology expert. Generate a USMLE Step 2 CK-style question about tubular disorders. Return ONLY a valid JSON object as described in the schema."
    )
    MALE_REPRODUCTIVE_DISORDERS = (
        "You are a nephrology and urology expert. Generate a USMLE Step 2 CK-style question about male reproductive disorders. Return ONLY a valid JSON object as described in the schema."
    )


class PosioningAndEnviromentalExposure:
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


class PsychiatricAndSubstanceUseDisorders:
    DIABETES_MELLITUS = (
        "You are an endocrinology expert. Generate a USMLE Step 2 CK-style question about diabetes mellitus. Return ONLY a valid JSON object as described in the schema."
    )
    THYROID_DISORDERS = (
        "You are an endocrinology expert. Generate a USMLE Step 2 CK-style question about thyroid disorders. Return ONLY a valid JSON object as described in the schema."
    )
    ADRENAL_DISORDERS = (
        "You are an endocrinology expert. Generate a USMLE Step 2 CK-style question about adrenal disorders. Return ONLY a valid JSON object as described in the schema."
    )


class SocialSciences:
    SEPSIS = (
        "You are an expert in multisystem disorders. Generate a USMLE Step 2 CK-style question about sepsis. Return ONLY a valid JSON object as described in the schema."
    )
    SHOCK = (
        "You are an expert in multisystem disorders. Generate a USMLE Step 2 CK-style question about shock. Return ONLY a valid JSON object as described in the schema."
    )
    SYSTEMIC_INFLAMMATORY_RESPONSE_SYNDROME = (
        "You are an expert in multisystem disorders. Generate a USMLE Step 2 CK-style question about systemic inflammatory response syndrome. Return ONLY a valid JSON object as described in the schema."
    )


class HematologyAndOncology:
    STUDY_DESIGN = (
        "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK-style question about study design. Return ONLY a valid JSON object as described in the schema."
    )
    STATISTICAL_ANALYSIS = (
        "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK-style question about statistical analysis. Return ONLY a valid JSON object as described in the schema."
    )
    POPULATION_HEALTH = (
        "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK-style question about population health. Return ONLY a valid JSON object as described in the schema."
    )


class InfectiousDiseases:
    MEDICAL_ETHICS = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about medical ethics. Return ONLY a valid JSON object as described in the schema."
    )
    PATIENT_SAFETY = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about patient safety. Return ONLY a valid JSON object as described in the schema."
    )
    PROFESSIONALISM = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about professionalism. Return ONLY a valid JSON object as described in the schema."
    )

class MaleReproductiveSystem:
    MEDICAL_ETHICS = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about medical ethics. Return ONLY a valid JSON object as described in the schema."
    )
    PATIENT_SAFETY = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about patient safety. Return ONLY a valid JSON object as described in the schema."
    )
    PROFESSIONALISM = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about professionalism. Return ONLY a valid JSON object as described in the schema."
    )

class NervousSystem:
    MEDICAL_ETHICS = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about medical ethics. Return ONLY a valid JSON object as described in the schema."
    )
    PATIENT_SAFETY = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about patient safety. Return ONLY a valid JSON object as described in the schema."
    )
    PROFESSIONALISM = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about professionalism. Return ONLY a valid JSON object as described in the schema."
    )

class Ophthalmology:
    MEDICAL_ETHICS = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about medical ethics. Return ONLY a valid JSON object as described in the schema."
    )
    PATIENT_SAFETY = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about patient safety. Return ONLY a valid JSON object as described in the schema."
    )
    PROFESSIONALISM = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about professionalism. Return ONLY a valid JSON object as described in the schema."
    )


class PregnancyChildbirthAndPuerperium:
    MEDICAL_ETHICS = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about medical ethics. Return ONLY a valid JSON object as described in the schema."
    )
    PATIENT_SAFETY = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about patient safety. Return ONLY a valid JSON object as described in the schema."
    )
    PROFESSIONALISM = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about professionalism. Return ONLY a valid JSON object as described in the schema."
    )

class CriticalCare:
    MEDICAL_ETHICS = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about medical ethics. Return ONLY a valid JSON object as described in the schema."
    )
    PATIENT_SAFETY = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about patient safety. Return ONLY a valid JSON object as described in the schema."
    )
    PROFESSIONALISM = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about professionalism. Return ONLY a valid JSON object as described in the schema."
    )

class RenalAndUrinary:
    MEDICAL_ETHICS = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about medical ethics. Return ONLY a valid JSON object as described in the schema."
    )
    PATIENT_SAFETY = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about patient safety. Return ONLY a valid JSON object as described in the schema."
    )
    PROFESSIONALISM = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about professionalism. Return ONLY a valid JSON object as described in the schema."
    )


class RheumatologyAndOrthopedics:
    MEDICAL_ETHICS = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about medical ethics. Return ONLY a valid JSON object as described in the schema."
    )
    PATIENT_SAFETY = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about patient safety. Return ONLY a valid JSON object as described in the schema."
    )
    PROFESSIONALISM = (
        "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK-style question about professionalism. Return ONLY a valid JSON object as described in the schema."
    )
