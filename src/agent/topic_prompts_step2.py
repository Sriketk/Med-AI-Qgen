AllergyAndImmunology = {
    "ANAPHYLAXIS_AND_ALLERGIC_REACTIONS": {
        "prompt": (
            "You are an allergy and immunology expert. Generate a USMLE Step 2 CK question about anaphylaxis and allergic reactions. "
            "Include a clinical vignette, relevant symptoms, labs, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A 28-year-old woman with no significant past medical history is brought to the emergency department by her coworkers after she suddenly developed difficulty breathing, swelling of her lips and tongue, and widespread hives during lunch at a restaurant. She had just started eating shrimp when her symptoms began. On arrival, she is anxious and has audible stridor. Her blood pressure is 85/50 mm Hg, pulse is 120/min, and respirations are 28/min. Physical examination reveals periorbital and oropharyngeal swelling, urticaria on her trunk and arms, and use of accessory muscles for breathing. Which of the following is the most appropriate next step in management?""",
            "choices": [
                "Administer intramuscular epinephrine",
                "Administer intravenous diphenhydramine",
                "Administer intravenous methylprednisolone",
                "Provide supplemental oxygen and observe",
                "Intubate and admit to intensive care unit",
            ],
            "answer": "Administer intramuscular epinephrine",
            "explanation": """This patient is experiencing anaphylaxis, characterized by acute onset of hypotension, airway compromise (stridor, swelling), and cutaneous findings (urticaria, angioedema) after exposure to a known allergen (shrimp). The immediate and most important step in management is administration of intramuscular epinephrine, which rapidly reverses airway obstruction and hypotension. Antihistamines (B) and corticosteroids (C) are adjunctive therapies but do not act quickly enough for life-threatening symptoms. Supplemental oxygen (D) may help but is not definitive. Intubation (E) may be necessary if airway compromise worsens, but epinephrine is the first-line intervention in acute anaphylaxis""",
        },
    },
    "AUTOIMMUNE_DISEASES": {
        "prompt": (
            "You are an allergy and immunology expert. Generate a USMLE Step 2 CK question about autoimmune diseases. "
            "Include a clinical vignette, relevant symptoms, labs, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A 32-year-old woman comes to the clinic because of a 3-month history of joint pain, fatigue, and a facial rash. She reports morning stiffness in her hands and wrists lasting over an hour and swelling in multiple finger joints. She also notes increased sensitivity to sunlight and intermittent low-grade fevers. On examination, she has tenderness and swelling of the metacarpophalangeal and proximal interphalangeal joints bilaterally, as well as a well-demarcated, erythematous rash over her cheeks and nasal bridge that spares the nasolabial folds. Laboratory studies show hemoglobin 10.2 g/dL, leukocytes 3,200/μL, and platelets 120,000/μL. Urinalysis reveals proteinuria and red blood cell casts. ANA and anti-dsDNA antibodies are positive.Which of the following is the most appropriate initial treatment for this patient’s current condition?""",
            "choices": [
                "Hydroxychloroquine",
                "Methotrexate",
                "Prednisone",
                "Mycophenolate mofetil",
                "Infliximab",
            ],
            "answer": "Prednisone",
            "explanation": """This patient meets criteria for systemic lupus erythematosus (SLE), presenting with arthritis, malar rash, hematologic abnormalities, and renal involvement (proteinuria and RBC casts). The presence of nephritis and cytopenias indicates a moderate to severe flare. Systemic corticosteroids (prednisone) are the most appropriate initial treatment to quickly control active inflammation and prevent organ damage. Hydroxychloroquine (A) is used for mild disease and as maintenance therapy. Methotrexate (B) is more appropriate for isolated joint involvement. Mycophenolate mofetil (D) is used for maintenance or steroid-sparing in lupus nephritis but not as initial therapy. Infliximab (E) is not used for SLE.""",
        },
    },
    "IMMUNE_DEFICIENCIES": {
        "prompt": (
            "You are an allergy and immunology expert. Generate a USMLE Step 2 CK question about immune deficiencies. "
            "Include a clinical vignette, relevant symptoms, labs, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A 6-month-old boy is brought to the pediatrician by his parents due to recurrent infections. He has had four episodes of otitis media, two episodes of pneumonia, and a hospitalization for bacterial meningitis since birth. He was born at term with no complications. Family history reveals that a maternal uncle died in infancy from a severe infection. On examination, the child appears well-nourished but has absent tonsillar tissue and no palpable lymph nodes. Laboratory studies show:

    Hemoglobin: 12.0 g/dL

    White blood cell count: 7,800/μL

    Platelets: 250,000/μL

    Immunoglobulin G: < 100 mg/dL (normal: 200–800 mg/dL)

    Immunoglobulin M: undetectable

    Immunoglobulin A: undetectable
    Which of the following is the most likely diagnosis?
""",
            "choices": [
                "Severe combined immunodeficiency",
                "X-linked agammaglobulinemia",
                "Common variable immunodeficiency",
                "DiGeorge syndrome",
                "Chronic granulomatous disease",
            ],
            "answer": "X-linked agammaglobulinemia",
            "explanation": """This infant has a history of recurrent bacterial infections, absent tonsils and lymph nodes, and markedly decreased immunoglobulin levels, which are classic findings of X-linked agammaglobulinemia (Bruton’s disease). This disorder is caused by a defect in B-cell maturation, leading to very low or absent B cells and immunoglobulins. The X-linked inheritance pattern is supported by the family history of an affected maternal uncle. Severe combined immunodeficiency (A) would present with both T and B cell defects and more severe, opportunistic infections. Common variable immunodeficiency (C) typically presents later in childhood or adulthood. DiGeorge syndrome (D) is associated with cardiac defects, hypocalcemia, and facial anomalies. Chronic granulomatous disease (E) presents with recurrent catalase-positive bacterial and fungal infections, but immunoglobulin levels are normal.""",
        },
    },
    "TRANSPLANT_MEDICINE": {
        "prompt": (
            "You are an allergy and immunology expert. Generate a USMLE Step 2 CK question about transplant medicine. "
            "Include a clinical vignette, relevant symptoms, labs, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A 45-year-old woman with end-stage renal disease due to hypertension underwent a living-donor kidney transplant three weeks ago. She is maintained on tacrolimus, mycophenolate mofetil, and prednisone. She now presents with a 2-day history of fever, malaise, and decreased urine output. Her temperature is 38.4°C (101.1°F), blood pressure is 135/80 mm Hg, and pulse is 92/min. Physical examination reveals mild tenderness over the transplanted kidney. Laboratory studies show:

    Serum creatinine: 2.5 mg/dL (baseline: 1.1 mg/dL)

    Blood urea nitrogen: 34 mg/dL

    Urinalysis: 2+ protein, 10–15 WBCs/hpf, no bacteria

    BK virus PCR: negative

A renal biopsy is performed.

Which of the following is the most likely finding on histological examination?

""",
            "choices": [
                "Neutrophilic infiltration with fibrinoid necrosis of small arteries",
                "Dense mononuclear infiltration of the interstitium and arterial wall necrosis",
                "Interstitial fibrosis with tubular atrophy",
                "Interstitial inflammation with basophilic intranuclear inclusions",
                "Widespread thrombosis of graft vessels",
            ],
            "answer": "Dense mononuclear infiltration of the interstitium and arterial wall necrosis",
            "explanation": """This patient is presenting with acute renal transplant rejection, which typically occurs within weeks to months after transplantation. The clinical features include fever, graft tenderness, and rising creatinine. The most characteristic histological finding is dense mononuclear (lymphocytic) infiltration of the interstitium and necrosis of the arterial wall (vasculitis).

    (A) Neutrophilic infiltration with fibrinoid necrosis is seen in hyperacute rejection.

    (C) Interstitial fibrosis with tubular atrophy is seen in chronic rejection.

    (D) Basophilic intranuclear inclusions are seen in BK virus nephropathy (ruled out by negative PCR).

    (E) Widespread thrombosis of graft vessels is also seen in hyperacute rejection

.""",
        },
    },
    "PRINCIPLES_OF_IMMUNOLOGY": {
        "prompt": (
            "You are an allergy and immunology expert. Generate a USMLE Step 2 CK question about principles of immunology. "
            "Include a clinical vignette, relevant symptoms, labs, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A 24-year-old man comes to the clinic because of a 2-month history of recurrent sinus infections and persistent eczema. He also reports frequent respiratory tract infections since childhood. Physical examination reveals dry, scaly patches on the flexural surfaces of his arms and mild swelling of the nasal mucosa. Laboratory studies show:

    Absolute neutrophil count: 4,500/μL (normal)

    Serum IgE: 2,500 IU/mL (normal < 100 IU/mL)

    Serum IgA: 120 mg/dL (normal)

    Serum IgG: 1,200 mg/dL (normal)

    Serum IgM: 90 mg/dL (normal)

    Eosinophil count: 800/μL (elevated)

Which of the following best explains the pathophysiology underlying this patient’s condition?""",
            "choices": [
                "Defective phagocyte oxidative burst",
                "Impaired B cell maturation",
                "Defective T cell-mediated cytokine signaling",
                "Absence of thymic tissue",
                "Complement C1 esterase inhibitor deficiency",
            ],
            "answer": "Defective T cell-mediated cytokine signaling",
            "explanation": """This patient’s history of recurrent infections, severe eczema, and markedly elevated IgE is characteristic of Hyper-IgE syndrome (Job syndrome). The underlying pathophysiology is a defect in T cell-mediated cytokine signaling, specifically mutations affecting STAT3, which impairs Th17 cell differentiation. This leads to defective recruitment of neutrophils to sites of infection, resulting in recurrent bacterial infections and eczematous dermatitis.

    (A) Defective phagocyte oxidative burst is seen in chronic granulomatous disease.

    (B) Impaired B cell maturation is seen in X-linked agammaglobulinemia.

    (D) Absence of thymic tissue is seen in DiGeorge syndrome.

    (E) C1 esterase inhibitor deficiency causes hereditary angioedema, not eczema or recurrent infections.

This question assesses understanding of immunological principles, including the role of cytokines and T cell subsets in immune system function
.""",
        },
    },
}

BiostatsAndEpidemiology = {
    "EPIDEMIOLOGY_AND_POPULATION_HEALTH": {
        "prompt": (
            "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK question about epidemiology and population health. "
            "Include a clinical vignette, relevant data, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A study is conducted to assess the prevalence of hypertension in a population. The sample includes 1000 individuals, and 150 are found to have hypertension. What is the prevalence of hypertension in this population?",
            "choices": ["10%", "15%", "20%", "25%", "30%"],
            "answer": "15%",
            "explanation": "Prevalence is calculated as the number of cases divided by the total population. Here, 150 out of 1000 individuals have hypertension, resulting in a prevalence of 15%.",
        },
    },
    "MEASURES_AND_DISTRIBUTION_OF_DATA": {
        "prompt": (
            "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK question about measures and distribution of data. "
            "Include a clinical vignette, relevant data, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A researcher is analyzing the distribution of cholesterol levels in a sample of 200 adults. The mean cholesterol level is 200 mg/dL with a standard deviation of 20 mg/dL. Assuming a normal distribution, what percentage of individuals have cholesterol levels between 180 mg/dL and 220 mg/dL?",
            "choices": ["68%", "75%", "80%", "85%", "90%"],
            "answer": "68%",
            "explanation": "In a normal distribution, approximately 68% of the data falls within one standard deviation of the mean. Here, 180 mg/dL to 220 mg/dL represents one standard deviation from the mean of 200 mg/dL.",
        },
    },
    "PROBABILITY_AND_PRINCIPLES_OF_TESTING": {
        "prompt": (
            "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK question about probability and principles of testing. "
            "Include a clinical vignette, relevant data, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A new diagnostic test for diabetes has a sensitivity of 90% and a specificity of 95%. In a population where the prevalence of diabetes is 10%, what is the positive predictive value of the test?",
            "choices": ["50%", "60%", "70%", "80%", "90%"],
            "answer": "70%",
            "explanation": "Positive predictive value (PPV) is the probability that subjects with a positive screening test truly have the disease. It is influenced by the prevalence of the disease in the population. Here, the PPV is calculated using the sensitivity, specificity, and prevalence.",
        },
    },
    "STUDY_DESIGN_AND_INTERPRETATION": {
        "prompt": (
            "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK question about study design and interpretation. "
            "Include a clinical vignette, relevant data, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A randomized controlled trial is conducted to evaluate the efficacy of a new antihypertensive drug. The trial includes 500 participants, with 250 receiving the drug and 250 receiving a placebo. After 6 months, the mean reduction in blood pressure is 10 mmHg in the drug group and 5 mmHg in the placebo group. What is the absolute risk reduction?",
            "choices": ["1%", "2%", "3%", "4%", "5%"],
            "answer": "5%",
            "explanation": "Absolute risk reduction (ARR) is the difference in event rates between two groups. Here, the ARR is the difference in mean blood pressure reduction between the drug and placebo groups, which is 5 mmHg.",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK question about miscellaneous topics in biostatistics and epidemiology. "
            "Include a clinical vignette, relevant data, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A cohort study is conducted to investigate the association between smoking and lung cancer. The study follows 1000 smokers and 1000 non-smokers for 10 years. At the end of the study, 100 smokers and 10 non-smokers develop lung cancer. What is the relative risk of lung cancer in smokers compared to non-smokers?",
            "choices": ["5", "10", "15", "20", "25"],
            "answer": "10",
            "explanation": "Relative risk (RR) is the ratio of the probability of an event occurring in the exposed group versus a non-exposed group. Here, the RR is calculated as (100/1000) / (10/1000) = 10, indicating smokers are 10 times more likely to develop lung cancer compared to non-smokers.",
        },
    },
}

Cardiovascular = {
    "AORTIC_AND_PERIPHERAL_ARTERY_DISEASES": {
        "prompt": (
            "You are a cardiology expert. Generate a USMLE Step 2 CK question about aortic and peripheral artery diseases. "
            "Include a clinical vignette, relevant symptoms, labs, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 65-year-old man presents with leg pain while walking that resolves with rest. Physical examination reveals diminished pulses in the lower extremities. Ankle-brachial index is 0.6. What is the most likely diagnosis?",
            "choices": [
                "Deep vein thrombosis",
                "Peripheral artery disease",
                "Chronic venous insufficiency",
                "Acute arterial occlusion",
                "Varicose veins",
            ],
            "answer": "Peripheral artery disease",
            "explanation": "The patient's symptoms and ankle-brachial index suggest peripheral artery disease, characterized by intermittent claudication and reduced blood flow to the extremities.",
        },
    },
    "CARDIAC_ARRHYTHMIAS_AND_SYNCOPE": {
        "prompt": (
            "You are a cardiology expert. Generate a USMLE Step 2 CK question about cardiac arrhythmias and syncope. "
            "Include a clinical vignette, relevant symptoms, ECG findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 70-year-old woman presents with palpitations and dizziness. ECG shows an irregularly irregular rhythm with no discernible P waves. What is the most likely diagnosis?",
            "choices": [
                "Atrial fibrillation",
                "Atrial flutter",
                "Ventricular tachycardia",
                "Sinus bradycardia",
                "First-degree AV block",
            ],
            "answer": "Atrial fibrillation",
            "explanation": "Atrial fibrillation is characterized by an irregularly irregular rhythm and absence of P waves on ECG.",
        },
    },
    "CONGENITAL_HEART_DISEASE": {
        "prompt": (
            "You are a cardiology expert. Generate a USMLE Step 2 CK question about congenital heart disease. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 2-month-old infant presents with cyanosis and difficulty feeding. Echocardiogram reveals a right-to-left shunt. What is the most likely diagnosis?",
            "choices": [
                "Tetralogy of Fallot",
                "Ventricular septal defect",
                "Atrial septal defect",
                "Patent ductus arteriosus",
                "Coarctation of the aorta",
            ],
            "answer": "Tetralogy of Fallot",
            "explanation": "Tetralogy of Fallot is a congenital heart defect that causes cyanosis due to a right-to-left shunt.",
        },
    },
    "CORONARY_HEART_DISEASE": {
        "prompt": (
            "You are a cardiology expert. Generate a USMLE Step 2 CK question about coronary heart disease. "
            "Include a clinical vignette, relevant symptoms, labs, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 55-year-old man presents with chest pain on exertion that is relieved by rest. What is the most likely diagnosis?",
            "choices": [
                "Stable angina",
                "Unstable angina",
                "Myocardial infarction",
                "Pericarditis",
                "Aortic dissection",
            ],
            "answer": "Stable angina",
            "explanation": "Stable angina is characterized by chest pain on exertion that is relieved by rest, indicating a fixed coronary artery stenosis.",
        },
    },
    "HEART_FAILURE_AND_SHOCK": {
        "prompt": (
            "You are a cardiology expert. Generate a USMLE Step 2 CK question about heart failure and shock. "
            "Include a clinical vignette, relevant symptoms, labs, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 60-year-old woman presents with shortness of breath, orthopnea, and leg swelling. Echocardiogram shows reduced ejection fraction. What is the most likely diagnosis?",
            "choices": [
                "Heart failure with reduced ejection fraction",
                "Heart failure with preserved ejection fraction",
                "Acute coronary syndrome",
                "Pulmonary embolism",
                "Chronic obstructive pulmonary disease",
            ],
            "answer": "Heart failure with reduced ejection fraction",
            "explanation": "The patient's symptoms and echocardiogram findings are consistent with heart failure with reduced ejection fraction, also known as systolic heart failure.",
        },
    },
    "HYPERTENSION": {
        "prompt": (
            "You are a cardiology expert. Generate a USMLE Step 2 CK question about hypertension. "
            "Include a clinical vignette, relevant symptoms, labs, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 45-year-old man is diagnosed with hypertension. His blood pressure is 150/95 mmHg. What is the first-line treatment?",
            "choices": [
                "Lifestyle modification",
                "ACE inhibitors",
                "Beta-blockers",
                "Calcium channel blockers",
                "Diuretics",
            ],
            "answer": "Lifestyle modification",
            "explanation": "Lifestyle modification is the first-line treatment for hypertension, including dietary changes, exercise, and weight loss.",
        },
    },
    "MYOPERICARDIAL_DISEASES": {
        "prompt": (
            "You are a cardiology expert. Generate a USMLE Step 2 CK question about myopericardial diseases. "
            "Include a clinical vignette, relevant symptoms, ECG findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old man presents with chest pain that worsens with inspiration and is relieved by sitting forward. ECG shows diffuse ST elevation. What is the most likely diagnosis?",
            "choices": [
                "Pericarditis",
                "Myocarditis",
                "Acute coronary syndrome",
                "Pulmonary embolism",
                "Aortic dissection",
            ],
            "answer": "Pericarditis",
            "explanation": "Pericarditis is characterized by chest pain that worsens with inspiration and is relieved by sitting forward, along with diffuse ST elevation on ECG.",
        },
    },
    "VALVULAR_HEART_DISEASES": {
        "prompt": (
            "You are a cardiology expert. Generate a USMLE Step 2 CK question about valvular heart diseases. "
            "Include a clinical vignette, relevant symptoms, auscultation findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 70-year-old woman presents with exertional dyspnea and a systolic ejection murmur heard best at the right second intercostal space. What is the most likely diagnosis?",
            "choices": [
                "Aortic stenosis",
                "Mitral regurgitation",
                "Aortic regurgitation",
                "Mitral stenosis",
                "Tricuspid regurgitation",
            ],
            "answer": "Aortic stenosis",
            "explanation": "Aortic stenosis is characterized by a systolic ejection murmur heard best at the right second intercostal space, often associated with exertional dyspnea.",
        },
    },
    "CARDIOVASCULAR_DRUGS": {
        "prompt": (
            "You are a cardiology expert. Generate a USMLE Step 2 CK question about cardiovascular drugs. "
            "Include a clinical vignette, relevant symptoms, drug interactions, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 50-year-old man with a history of atrial fibrillation is started on warfarin. What is the most important dietary advice to give this patient?",
            "choices": [
                "Avoid grapefruit",
                "Limit vitamin K intake",
                "Increase calcium intake",
                "Avoid dairy products",
                "Increase fiber intake",
            ],
            "answer": "Limit vitamin K intake",
            "explanation": "Patients on warfarin should limit vitamin K intake as it can affect the drug's anticoagulant effect.",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are a cardiology expert. Generate a USMLE Step 2 CK question about miscellaneous cardiovascular topics. "
            "Include a clinical vignette, relevant symptoms, labs, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old woman presents with palpitations and anxiety. Her thyroid function tests reveal hyperthyroidism. What is the most likely cardiovascular manifestation of her condition?",
            "choices": [
                "Atrial fibrillation",
                "Bradycardia",
                "Heart block",
                "Ventricular tachycardia",
                "Sinus arrhythmia",
            ],
            "answer": "Atrial fibrillation",
            "explanation": "Hyperthyroidism can lead to atrial fibrillation due to increased sympathetic activity and metabolic rate.",
        },
    },
}

Dermatology = {
    "NORMAL_STRUCTURE_AND_FUNCTION_OF_SKIN": {
        "prompt": (
            "You are a dermatology expert. Generate a USMLE Step 2 CK question about the normal structure and function of skin. "
            "Include a clinical vignette, relevant symptoms, histological findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 25-year-old woman presents with dry, itchy skin. Examination reveals fine scaling and lichenification. What is the most likely underlying cause of her symptoms?",
            "choices": [
                "Epidermal barrier dysfunction",
                "Autoimmune reaction",
                "Bacterial infection",
                "Fungal infection",
                "Viral infection",
            ],
            "answer": "Epidermal barrier dysfunction",
            "explanation": "The patient's symptoms are consistent with atopic dermatitis, which is often due to epidermal barrier dysfunction leading to dry, itchy skin.",
        },
    },
    "DISORDERS_OF_EPDERMAL_APPENDAGES": {
        "prompt": (
            "You are a dermatology expert. Generate a USMLE Step 2 CK question about disorders of epidermal appendages. "
            "Include a clinical vignette, relevant symptoms, histological findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old man presents with multiple painful nodules on his axillae. Examination reveals inflamed nodules and sinus tracts. What is the most likely diagnosis?",
            "choices": [
                "Hidradenitis suppurativa",
                "Acne vulgaris",
                "Folliculitis",
                "Psoriasis",
                "Eczema",
            ],
            "answer": "Hidradenitis suppurativa",
            "explanation": "Hidradenitis suppurativa is characterized by painful nodules and sinus tracts in areas with apocrine glands, such as the axillae.",
        },
    },
    "INFLAMMATORY_DERMATOSES_AND_BULLOUS_DISEASES": {
        "prompt": (
            "You are a dermatology expert. Generate a USMLE Step 2 CK question about inflammatory dermatoses and bullous diseases. "
            "Include a clinical vignette, relevant symptoms, histological findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old woman presents with tense blisters on her abdomen and thighs. Biopsy shows subepidermal blisters with eosinophils. What is the most likely diagnosis?",
            "choices": [
                "Bullous pemphigoid",
                "Pemphigus vulgaris",
                "Dermatitis herpetiformis",
                "Erythema multiforme",
                "Stevens-Johnson syndrome",
            ],
            "answer": "Bullous pemphigoid",
            "explanation": "Bullous pemphigoid is characterized by tense blisters and subepidermal blisters with eosinophils on biopsy.",
        },
    },
    "SKIN_AND_SOFT_TISSUE_INFECTIONS": {
        "prompt": (
            "You are a dermatology expert. Generate a USMLE Step 2 CK question about skin and soft tissue infections. "
            "Include a clinical vignette, relevant symptoms, microbiological findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 50-year-old man presents with a painful, swollen leg. Examination reveals erythema, warmth, and tenderness. What is the most likely causative organism?",
            "choices": [
                "Staphylococcus aureus",
                "Streptococcus pyogenes",
                "Pseudomonas aeruginosa",
                "Escherichia coli",
                "Candida albicans",
            ],
            "answer": "Streptococcus pyogenes",
            "explanation": "Cellulitis is commonly caused by Streptococcus pyogenes, presenting with erythema, warmth, and tenderness.",
        },
    },
    "SKIN_TUMORS_AND_TUMOR_LIKE_LESIONS": {
        "prompt": (
            "You are a dermatology expert. Generate a USMLE Step 2 CK question about skin tumors and tumor-like lesions. "
            "Include a clinical vignette, relevant symptoms, histological findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 60-year-old woman presents with a pearly papule on her nose. Biopsy shows nests of basaloid cells. What is the most likely diagnosis?",
            "choices": [
                "Basal cell carcinoma",
                "Squamous cell carcinoma",
                "Melanoma",
                "Actinic keratosis",
                "Seborrheic keratosis",
            ],
            "answer": "Basal cell carcinoma",
            "explanation": "Basal cell carcinoma is characterized by a pearly papule and nests of basaloid cells on biopsy.",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are a dermatology expert. Generate a USMLE Step 2 CK question about miscellaneous dermatology topics. "
            "Include a clinical vignette, relevant symptoms, labs, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 35-year-old woman presents with a butterfly-shaped rash on her face. What is the most likely associated condition?",
            "choices": [
                "Systemic lupus erythematosus",
                "Rosacea",
                "Psoriasis",
                "Seborrheic dermatitis",
                "Contact dermatitis",
            ],
            "answer": "Systemic lupus erythematosus",
            "explanation": "A butterfly-shaped rash on the face is characteristic of systemic lupus erythematosus.",
        },
    },
}

MaleReproductiveSystem = {
    "DISORDERS_OF_THE_MALE_REPRODUCTIVE_SYSTEM": {
        "prompt": (
            "You are a urology expert. Generate a USMLE Step 2 CK question about disorders of the male reproductive system. "
            "Include a clinical vignette, relevant symptoms, labs, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 50-year-old man presents with difficulty urinating and a weak stream. Digital rectal examination reveals an enlarged, non-tender prostate. What is the most likely diagnosis?",
            "choices": [
                "Benign prostatic hyperplasia",
                "Prostate cancer",
                "Prostatitis",
                "Urethral stricture",
                "Bladder cancer",
            ],
            "answer": "Benign prostatic hyperplasia",
            "explanation": "The patient's symptoms and examination findings are consistent with benign prostatic hyperplasia, a common condition in older men.",
        },
    }
}

NervousSystem = {
    "NORMAL_STRUCTURE_AND_FUNCTION_OF_THE_NERVOUS_SYSTEM": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about the normal structure and function of the nervous system. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old woman presents with muscle weakness and fatigue. Neurological examination reveals decreased deep tendon reflexes. MRI of the brain is normal. What is the most likely diagnosis?",
            "choices": [
                "Multiple sclerosis",
                "Myasthenia gravis",
                "Guillain-Barré syndrome",
                "Amyotrophic lateral sclerosis",
                "Muscular dystrophy",
            ],
            "answer": "Myasthenia gravis",
        },
    },
    "CONGENITAL_AND_DEVELOPMENTAL_ANOMALIES": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about congenital and developmental anomalies of the nervous system. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A newborn is noted to have a sac-like protrusion in the lumbar region. MRI reveals a defect in the vertebral arches. What is the most likely diagnosis?",
            "choices": [
                "Spina bifida",
                "Anencephaly",
                "Hydrocephalus",
                "Cerebral palsy",
                "Microcephaly",
            ],
            "answer": "Spina bifida",
        },
    },
    "CEREBROVASCULAR_DISEASE": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about cerebrovascular disease. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 70-year-old man presents with sudden onset of right-sided weakness and slurred speech. CT scan of the head shows an ischemic stroke in the left middle cerebral artery territory. What is the most appropriate initial treatment?",
            "choices": [
                "Aspirin",
                "Thrombolysis",
                "Heparin",
                "Warfarin",
                "Clopidogrel",
            ],
            "answer": "Thrombolysis",
        },
    },
    "CNS_INFECTIONS": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about CNS infections. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 25-year-old man presents with fever, headache, and neck stiffness. Lumbar puncture reveals elevated white blood cell count with lymphocytic predominance. What is the most likely diagnosis?",
            "choices": [
                "Bacterial meningitis",
                "Viral meningitis",
                "Tuberculous meningitis",
                "Fungal meningitis",
                "Encephalitis",
            ],
            "answer": "Viral meningitis",
        },
    },
    "DEMYELINATING_DISEASES": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about demyelinating diseases. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 28-year-old woman presents with blurred vision and weakness in her right leg. MRI of the brain shows multiple white matter lesions. What is the most likely diagnosis?",
            "choices": [
                "Multiple sclerosis",
                "Guillain-Barré syndrome",
                "Neuromyelitis optica",
                "Chronic inflammatory demyelinating polyneuropathy",
                "Acute disseminated encephalomyelitis",
            ],
            "answer": "Multiple sclerosis",
        },
    },
    "DISORDERS_OF_PERIPHERAL_NERVES_AND_MUSCLES": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about disorders of peripheral nerves and muscles. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 45-year-old man presents with progressive weakness and muscle atrophy. Electromyography shows evidence of denervation. What is the most likely diagnosis?",
            "choices": [
                "Amyotrophic lateral sclerosis",
                "Myasthenia gravis",
                "Guillain-Barré syndrome",
                "Muscular dystrophy",
                "Peripheral neuropathy",
            ],
            "answer": "Amyotrophic lateral sclerosis",
        },
    },
    "HEADACHE": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about headaches. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old woman presents with recurrent, throbbing headaches associated with nausea and photophobia. What is the most likely diagnosis?",
            "choices": [
                "Migraine",
                "Tension headache",
                "Cluster headache",
                "Sinus headache",
                "Trigeminal neuralgia",
            ],
            "answer": "Migraine",
        },
    },
    "NEURODEGENERATIVE_DISORDERS_AND_DEMENTIAS": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about neurodegenerative disorders and dementias. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 70-year-old man presents with memory loss and difficulty performing daily activities. MRI of the brain shows cortical atrophy. What is the most likely diagnosis?",
            "choices": [
                "Alzheimer's disease",
                "Parkinson's disease",
                "Lewy body dementia",
                "Frontotemporal dementia",
                "Vascular dementia",
            ],
            "answer": "Alzheimer's disease",
        },
    },
    "SEIZURES_AND_EPILEPSY": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about seizures and epilepsy. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 20-year-old man presents with episodes of loss of consciousness and convulsions. EEG shows generalized spike-and-wave discharges. What is the most likely diagnosis?",
            "choices": [
                "Generalized tonic-clonic seizure",
                "Absence seizure",
                "Focal seizure",
                "Myoclonic seizure",
                "Atonic seizure",
            ],
            "answer": "Generalized tonic-clonic seizure",
        },
    },
    "SPINAL_CORD_DISORDERS": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about spinal cord disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old woman presents with sudden onset of back pain and weakness in her legs. MRI of the spine shows a herniated disc compressing the spinal cord. What is the most likely diagnosis?",
            "choices": [
                "Herniated disc",
                "Spinal stenosis",
                "Transverse myelitis",
                "Spinal cord tumor",
                "Cauda equina syndrome",
            ],
            "answer": "Herniated disc",
        },
    },
    "TRAUMATIC_BRAIN_INJURIES": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about traumatic brain injuries. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 25-year-old man presents with confusion and headache after a motor vehicle accident. CT scan of the head shows a subdural hematoma. What is the most likely diagnosis?",
            "choices": [
                "Subdural hematoma",
                "Epidural hematoma",
                "Concussion",
                "Contusion",
                "Diffuse axonal injury",
            ],
            "answer": "Subdural hematoma",
        },
    },
    "TUMORS_OF_THE_NERVOUS_SYSTEM": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about tumors of the nervous system. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 50-year-old woman presents with headaches and seizures. MRI of the brain shows a mass in the frontal lobe. What is the most likely diagnosis?",
            "choices": [
                "Glioblastoma",
                "Meningioma",
                "Astrocytoma",
                "Oligodendroglioma",
                "Metastatic tumor",
            ],
            "answer": "Glioblastoma",
        },
    },
    "HYDROCEPHALUS": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about hydrocephalus. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 60-year-old man presents with gait instability and urinary incontinence. MRI of the brain shows enlarged ventricles. What is the most likely diagnosis?",
            "choices": [
                "Normal pressure hydrocephalus",
                "Obstructive hydrocephalus",
                "Communicating hydrocephalus",
                "Congenital hydrocephalus",
                "Idiopathic intracranial hypertension",
            ],
            "answer": "Normal pressure hydrocephalus",
        },
    },
    "ANESTHESIA_PHARMACOTHERAPY": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about anesthesia and pharmacotherapy. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 45-year-old woman undergoing surgery develops malignant hyperthermia. What is the most appropriate treatment?",
            "choices": ["Dantrolene", "Lidocaine", "Propofol", "Midazolam", "Fentanyl"],
            "answer": "Dantrolene",
        },
    },
    "SLEEP_DISORDERS": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about sleep disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 35-year-old man presents with excessive daytime sleepiness and cataplexy. What is the most likely diagnosis?",
            "choices": [
                "Narcolepsy",
                "Obstructive sleep apnea",
                "Insomnia",
                "Restless legs syndrome",
                "Circadian rhythm disorder",
            ],
            "answer": "Narcolepsy",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are a neurology expert. Generate a USMLE Step 2 CK question about miscellaneous neurological conditions. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old woman presents with sudden onset of facial droop on the right side. What is the most likely diagnosis?",
            "choices": [
                "Bell's palsy",
                "Stroke",
                "Trigeminal neuralgia",
                "Multiple sclerosis",
                "Myasthenia gravis",
            ],
            "answer": "Bell's palsy",
        },
    },
}

Ophthalmology = {
    "DISORDERS_OF_THE_EYE_AND_ASSOCIATED_STRUCTURES": {
        "prompt": (
            "You are an ophthalmology expert. Generate a USMLE Step 2 CK question about disorders of the eye and associated structures. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 60-year-old woman presents with gradual loss of vision in her right eye. Fundoscopic examination reveals drusen deposits in the macula. What is the most likely diagnosis?",
            "choices": [
                "Age-related macular degeneration",
                "Diabetic retinopathy",
                "Retinal detachment",
                "Glaucoma",
                "Cataract",
            ],
            "answer": "Age-related macular degeneration",
        },
    },
}

PoisoningAndEnvironmentalExposure = {
    "ENVIRONMENTAL_EXPOSURE": {
        "prompt": (
            "You are an environmental medicine expert. Generate a USMLE Step 2 CK question about environmental exposure. "
            "Include a clinical vignette, relevant symptoms, exposure history, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 45-year-old man presents with cough and shortness of breath after working in a factory with asbestos exposure. Chest X-ray shows pleural plaques. What is the most likely diagnosis?",
            "choices": [
                "Asbestosis",
                "Silicosis",
                "Coal worker's pneumoconiosis",
                "Chronic bronchitis",
                "Lung cancer",
            ],
            "answer": "Asbestosis",
        },
    },
    "TOXICOLOGY": {
        "prompt": (
            "You are a toxicology expert. Generate a USMLE Step 2 CK question about toxicology. "
            "Include a clinical vignette, relevant symptoms, substance exposure, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old woman presents with confusion and metabolic acidosis after ingesting antifreeze. What is the most appropriate antidote?",
            "choices": [
                "Fomepizole",
                "N-acetylcysteine",
                "Activated charcoal",
                "Sodium bicarbonate",
                "Atropine",
            ],
            "answer": "Fomepizole",
        },
    },
}

PsychiatricBehavioralAndSubstanceUseDisorder = {
    "NORMAL_BEHAVIOR_AND_DEVELOPMENT": {
        "prompt": (
            "You are a psychiatry expert. Generate a USMLE Step 2 CK question about normal behavior and development. "
            "Include a clinical vignette, relevant symptoms, developmental milestones, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 2-year-old child is brought in for a routine check-up. The child can walk up stairs with assistance and uses two-word phrases. What developmental milestone is expected next?",
            "choices": [
                "Riding a tricycle",
                "Using three-word sentences",
                "Drawing a circle",
                "Skipping",
                "Tying shoelaces",
            ],
            "answer": "Using three-word sentences",
        },
    },
    "ANXIETY_AND_TRAUMA_RELATED_DISORDERS": {
        "prompt": (
            "You are a psychiatry expert. Generate a USMLE Step 2 CK question about anxiety and trauma-related disorders. "
            "Include a clinical vignette, relevant symptoms, history, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old woman presents with excessive worry about various aspects of her life for the past 6 months. She also reports muscle tension and difficulty sleeping. What is the most likely diagnosis?",
            "choices": [
                "Generalized anxiety disorder",
                "Panic disorder",
                "Post-traumatic stress disorder",
                "Obsessive-compulsive disorder",
                "Social anxiety disorder",
            ],
            "answer": "Generalized anxiety disorder",
        },
    },
    "MOOD_DISORDERS": {
        "prompt": (
            "You are a psychiatry expert. Generate a USMLE Step 2 CK question about mood disorders. "
            "Include a clinical vignette, relevant symptoms, history, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 25-year-old man presents with a 2-week history of depressed mood, loss of interest in activities, and fatigue. He denies any history of manic episodes. What is the most likely diagnosis?",
            "choices": [
                "Major depressive disorder",
                "Bipolar disorder",
                "Dysthymia",
                "Cyclothymia",
                "Adjustment disorder",
            ],
            "answer": "Major depressive disorder",
        },
    },
    "NEURODEVELOPMENTAL_AND_NEUROCOGNITIVE_DISORDERS": {
        "prompt": (
            "You are a psychiatry expert. Generate a USMLE Step 2 CK question about neurodevelopmental and neurocognitive disorders. "
            "Include a clinical vignette, relevant symptoms, history, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 5-year-old boy is brought in for evaluation due to difficulty in social interactions and repetitive behaviors. He has limited eye contact and prefers solitary play. What is the most likely diagnosis?",
            "choices": [
                "Autism spectrum disorder",
                "Attention-deficit/hyperactivity disorder",
                "Intellectual disability",
                "Specific learning disorder",
                "Social communication disorder",
            ],
            "answer": "Autism spectrum disorder",
        },
    },
    "PERSONALITY_IMPULSE_CONTROL_AND_SEXUAL_DISORDERS": {
        "prompt": (
            "You are a psychiatry expert. Generate a USMLE Step 2 CK question about personality, impulse control, and sexual disorders. "
            "Include a clinical vignette, relevant symptoms, history, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 35-year-old man presents with a long-standing pattern of unstable relationships, impulsivity, and intense emotions. He has a history of self-harm. What is the most likely diagnosis?",
            "choices": [
                "Borderline personality disorder",
                "Antisocial personality disorder",
                "Histrionic personality disorder",
                "Narcissistic personality disorder",
                "Obsessive-compulsive personality disorder",
            ],
            "answer": "Borderline personality disorder",
        },
    },
    "PSYCHOTIC_DISORDERS": {
        "prompt": (
            "You are a psychiatry expert. Generate a USMLE Step 2 CK question about psychotic disorders. "
            "Include a clinical vignette, relevant symptoms, history, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 22-year-old man presents with auditory hallucinations and delusions of persecution for the past 6 months. He has no history of mood symptoms. What is the most likely diagnosis?",
            "choices": [
                "Schizophrenia",
                "Schizoaffective disorder",
                "Bipolar disorder with psychotic features",
                "Major depressive disorder with psychotic features",
                "Brief psychotic disorder",
            ],
            "answer": "Schizophrenia",
        },
    },
    "SUBSTANCE_USE_DISORDERS": {
        "prompt": (
            "You are a psychiatry expert. Generate a USMLE Step 2 CK question about substance use disorders. "
            "Include a clinical vignette, relevant symptoms, history, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old man presents with tremors, sweating, and agitation 12 hours after his last drink. He has a history of alcohol dependence. What is the most appropriate treatment?",
            "choices": [
                "Benzodiazepines",
                "Antipsychotics",
                "Antidepressants",
                "Beta-blockers",
                "Anticonvulsants",
            ],
            "answer": "Benzodiazepines",
        },
    },
    "EATING_DISORDERS": {
        "prompt": (
            "You are a psychiatry expert. Generate a USMLE Step 2 CK question about eating disorders. "
            "Include a clinical vignette, relevant symptoms, history, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 19-year-old woman presents with a 6-month history of binge eating followed by self-induced vomiting. She is concerned about her weight and body shape. What is the most likely diagnosis?",
            "choices": [
                "Bulimia nervosa",
                "Anorexia nervosa",
                "Binge eating disorder",
                "Body dysmorphic disorder",
                "Avoidant/restrictive food intake disorder",
            ],
            "answer": "Bulimia nervosa",
        },
    },
    "SOMATOFORM_DISORDERS_AND_SLEEP_DISORDERS": {
        "prompt": (
            "You are a psychiatry expert. Generate a USMLE Step 2 CK question about somatoform disorders and sleep disorders. "
            "Include a clinical vignette, relevant symptoms, history, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 28-year-old woman presents with excessive daytime sleepiness and cataplexy. She has a history of vivid hallucinations upon falling asleep. What is the most likely diagnosis?",
            "choices": [
                "Narcolepsy",
                "Insomnia",
                "Sleep apnea",
                "Restless legs syndrome",
                "Circadian rhythm sleep disorder",
            ],
            "answer": "Narcolepsy",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are a psychiatry expert. Generate a USMLE Step 2 CK question about miscellaneous psychiatric conditions. "
            "Include a clinical vignette, relevant symptoms, history, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old woman presents with sudden onset of facial droop on the right side. What is the most likely diagnosis?",
            "choices": [
                "Bell's palsy",
                "Stroke",
                "Trigeminal neuralgia",
                "Multiple sclerosis",
                "Myasthenia gravis",
            ],
            "answer": "Bell's palsy",
        },
    },
}

FemaleReproductiveSystemAndBreast = {
    "NORMAL_STRUCTURE_AND_FUNCTION_OF_THE_FEMALE_REPRODUCTIVE_SYSTEM_AND_BREAST": {
        "prompt": (
            "You are a gynecology expert. Generate a USMLE Step 2 CK question about the normal structure and function of the female reproductive system and breast. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 25-year-old woman presents for a routine check-up. She has regular menstrual cycles and no complaints. What is the most likely phase of her menstrual cycle if her endometrial lining is thick and glandular?",
            "choices": [
                "Proliferative phase",
                "Secretory phase",
                "Menstrual phase",
                "Follicular phase",
                "Luteal phase",
            ],
            "answer": "Secretory phase",
        },
    },
    "CONGENITAL_AND_DEVELOPMENTAL_ANOMALIES": {
        "prompt": (
            "You are a gynecology expert. Generate a USMLE Step 2 CK question about congenital and developmental anomalies of the female reproductive system. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 16-year-old girl presents with primary amenorrhea and cyclic abdominal pain. Physical examination reveals a bulging hymen. What is the most likely diagnosis?",
            "choices": [
                "Imperforate hymen",
                "Müllerian agenesis",
                "Androgen insensitivity syndrome",
                "Turner syndrome",
                "Polycystic ovary syndrome",
            ],
            "answer": "Imperforate hymen",
        },
    },
    "BREAST_DISORDERS": {
        "prompt": (
            "You are a gynecology expert. Generate a USMLE Step 2 CK question about breast disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 45-year-old woman presents with a painless lump in her breast. Mammography shows a spiculated mass. What is the most likely diagnosis?",
            "choices": [
                "Breast cancer",
                "Fibroadenoma",
                "Breast cyst",
                "Mastitis",
                "Fat necrosis",
            ],
            "answer": "Breast cancer",
        },
    },
    "GENITAL_TRACT_TUMORS_AND_TUMOR_LIKE_LESIONS": {
        "prompt": (
            "You are a gynecology expert. Generate a USMLE Step 2 CK question about genital tract tumors and tumor-like lesions. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 60-year-old woman presents with postmenopausal bleeding. Ultrasound reveals a thickened endometrial lining. What is the most likely diagnosis?",
            "choices": [
                "Endometrial cancer",
                "Cervical cancer",
                "Ovarian cyst",
                "Uterine fibroid",
                "Endometrial hyperplasia",
            ],
            "answer": "Endometrial cancer",
        },
    },
    "GENITOURINARY_TRACT_INFECTIONS": {
        "prompt": (
            "You are a gynecology expert. Generate a USMLE Step 2 CK question about genitourinary tract infections. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old woman presents with dysuria and increased urinary frequency. Urinalysis shows pyuria and bacteriuria. What is the most likely diagnosis?",
            "choices": [
                "Urinary tract infection",
                "Pyelonephritis",
                "Interstitial cystitis",
                "Vaginitis",
                "Urethritis",
            ],
            "answer": "Urinary tract infection",
        },
    },
    "MENSTRUAL_DISORDERS_AND_CONTRACEPTION": {
        "prompt": (
            "You are a gynecology expert. Generate a USMLE Step 2 CK question about menstrual disorders and contraception. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 22-year-old woman presents with irregular menstrual cycles and hirsutism. Ultrasound shows polycystic ovaries. What is the most likely diagnosis?",
            "choices": [
                "Polycystic ovary syndrome",
                "Hypothyroidism",
                "Hyperprolactinemia",
                "Premature ovarian failure",
                "Cushing's syndrome",
            ],
            "answer": "Polycystic ovary syndrome",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are a gynecology expert. Generate a USMLE Step 2 CK question about miscellaneous conditions of the female reproductive system and breast. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old woman presents with sudden onset of facial droop on the right side. What is the most likely diagnosis?",
            "choices": [
                "Bell's palsy",
                "Stroke",
                "Trigeminal neuralgia",
                "Multiple sclerosis",
                "Myasthenia gravis",
            ],
            "answer": "Bell's palsy",
        },
    },
}

PulmonaryAndCriticalCare = {
    "NORMAL_PULMONARY_STRUCTURE_AND_FUNCTION": {
        "prompt": (
            "You are a pulmonology expert. Generate a USMLE Step 2 CK question about normal pulmonary structure and function. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old man presents for a routine check-up. Pulmonary function tests show normal lung volumes and diffusion capacity. What is the most likely interpretation?",
            "choices": [
                "Normal lung function",
                "Obstructive lung disease",
                "Restrictive lung disease",
                "Pulmonary hypertension",
                "Interstitial lung disease",
            ],
            "answer": "Normal lung function",
        },
    },
    "CONGENITAL_AND_DEVELOPMENTAL_ANOMALIES": {
        "prompt": (
            "You are a pulmonology expert. Generate a USMLE Step 2 CK question about congenital and developmental anomalies of the pulmonary system. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A newborn is noted to have respiratory distress shortly after birth. Chest X-ray shows a diaphragmatic hernia. What is the most likely diagnosis?",
            "choices": [
                "Congenital diaphragmatic hernia",
                "Tracheoesophageal fistula",
                "Pulmonary hypoplasia",
                "Bronchopulmonary dysplasia",
                "Cystic fibrosis",
            ],
            "answer": "Congenital diaphragmatic hernia",
        },
    },
    "CRITICAL_CARE_AND_TRAUMA_MEDICINE": {
        "prompt": (
            "You are a critical care expert. Generate a USMLE Step 2 CK question about critical care and trauma medicine. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old man is admitted to the ICU after a motor vehicle accident. He is intubated and on mechanical ventilation. What is the most appropriate initial ventilator setting?",
            "choices": [
                "Volume control ventilation",
                "Pressure control ventilation",
                "High-frequency oscillatory ventilation",
                "Non-invasive ventilation",
                "Spontaneous breathing trial",
            ],
            "answer": "Volume control ventilation",
        },
    },
    "INTERSTITIAL_PULMONARY_AND_OTHER_SYSTEMIC_DISORDERS": {
        "prompt": (
            "You are a pulmonology expert. Generate a USMLE Step 2 CK question about interstitial pulmonary and other systemic disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 55-year-old woman presents with progressive dyspnea and dry cough. High-resolution CT scan shows reticular opacities and honeycombing. What is the most likely diagnosis?",
            "choices": [
                "Idiopathic pulmonary fibrosis",
                "Sarcoidosis",
                "Hypersensitivity pneumonitis",
                "Pulmonary edema",
                "Bronchiectasis",
            ],
            "answer": "Idiopathic pulmonary fibrosis",
        },
    },
    "CANCER_AND_PULMONARY_MEDIASTINAL_MASSES": {
        "prompt": (
            "You are a pulmonology expert. Generate a USMLE Step 2 CK question about cancer and pulmonary/mediastinal masses. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 60-year-old man presents with cough and weight loss. Chest X-ray shows a mass in the right upper lobe. What is the most likely diagnosis?",
            "choices": [
                "Lung cancer",
                "Tuberculosis",
                "Lung abscess",
                "Pulmonary embolism",
                "Pneumonia",
            ],
            "answer": "Lung cancer",
        },
    },
    "OBSTRUCTIVE_AND_RESTRICTIVE_LUNG_DISEASE": {
        "prompt": (
            "You are a pulmonology expert. Generate a USMLE Step 2 CK question about obstructive and restrictive lung disease. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 50-year-old woman presents with shortness of breath and wheezing. Pulmonary function tests show decreased FEV1/FVC ratio. What is the most likely diagnosis?",
            "choices": [
                "Chronic obstructive pulmonary disease",
                "Asthma",
                "Pulmonary fibrosis",
                "Sarcoidosis",
                "Pleural effusion",
            ],
            "answer": "Chronic obstructive pulmonary disease",
        },
    },
    "PULMONARY_INFECTIONS": {
        "prompt": (
            "You are a pulmonology expert. Generate a USMLE Step 2 CK question about pulmonary infections. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 35-year-old man presents with fever, cough, and pleuritic chest pain. Chest X-ray shows a lobar consolidation. What is the most likely diagnosis?",
            "choices": [
                "Pneumonia",
                "Tuberculosis",
                "Lung abscess",
                "Pulmonary embolism",
                "Bronchitis",
            ],
            "answer": "Pneumonia",
        },
    },
    "PULMONARY_VASCULAR_AND_CARDIOPULMONARY_DISEASE": {
        "prompt": (
            "You are a pulmonology expert. Generate a USMLE Step 2 CK question about pulmonary vascular and cardiopulmonary disease. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 45-year-old woman presents with shortness of breath and chest pain. CT angiography shows a filling defect in the pulmonary artery. What is the most likely diagnosis?",
            "choices": [
                "Pulmonary embolism",
                "Pulmonary hypertension",
                "Aortic dissection",
                "Myocardial infarction",
                "Pneumothorax",
            ],
            "answer": "Pulmonary embolism",
        },
    },
    "SLEEP_DISORDERS": {
        "prompt": (
            "You are a pulmonology expert. Generate a USMLE Step 2 CK question about sleep disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 50-year-old man presents with excessive daytime sleepiness and loud snoring. Polysomnography shows apneic episodes. What is the most likely diagnosis?",
            "choices": [
                "Obstructive sleep apnea",
                "Insomnia",
                "Narcolepsy",
                "Restless legs syndrome",
                "Circadian rhythm sleep disorder",
            ],
            "answer": "Obstructive sleep apnea",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are a pulmonology expert. Generate a USMLE Step 2 CK question about miscellaneous pulmonary conditions. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old woman presents with sudden onset of facial droop on the right side. What is the most likely diagnosis?",
            "choices": [
                "Bell's palsy",
                "Stroke",
                "Trigeminal neuralgia",
                "Multiple sclerosis",
                "Myasthenia gravis",
            ],
            "answer": "Bell's palsy",
        },
    },
}

GastrointestinalAndNutrition = {
    "NORMAL_STRUCTURE_AND_FUNCTION_OF_THE_GI_TRACT": {
        "prompt": (
            "You are a gastroenterology expert. Generate a USMLE Step 2 CK question about the normal structure and function of the GI tract. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 28-year-old man presents for a routine check-up. Endoscopy shows normal mucosa throughout the GI tract. What is the most likely interpretation?",
            "choices": [
                "Normal GI function",
                "Gastritis",
                "Peptic ulcer disease",
                "Celiac disease",
                "Crohn's disease",
            ],
            "answer": "Normal GI function",
        },
    },
    "CONGENITAL_AND_DEVELOPMENTAL_ANOMALIES": {
        "prompt": (
            "You are a gastroenterology expert. Generate a USMLE Step 2 CK question about congenital and developmental anomalies of the GI tract. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A newborn is noted to have bilious vomiting and abdominal distension. An upper GI series shows a 'double bubble' sign. What is the most likely diagnosis?",
            "choices": [
                "Duodenal atresia",
                "Pyloric stenosis",
                "Hirschsprung's disease",
                "Malrotation",
                "Intussusception",
            ],
            "answer": "Duodenal atresia",
        },
    },
    "BILIARY_TRACT_DISORDERS": {
        "prompt": (
            "You are a gastroenterology expert. Generate a USMLE Step 2 CK question about biliary tract disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 45-year-old woman presents with right upper quadrant pain and jaundice. Ultrasound shows gallstones and a dilated common bile duct. What is the most likely diagnosis?",
            "choices": [
                "Choledocholithiasis",
                "Cholecystitis",
                "Cholangitis",
                "Gallbladder cancer",
                "Pancreatitis",
            ],
            "answer": "Choledocholithiasis",
        },
    },
    "DISORDERS_OF_NUTRITION": {
        "prompt": (
            "You are a gastroenterology expert. Generate a USMLE Step 2 CK question about disorders of nutrition. "
            "Include a clinical vignette, relevant symptoms, dietary history, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old man presents with fatigue and pallor. Blood tests reveal microcytic anemia. What is the most likely nutritional deficiency?",
            "choices": [
                "Iron deficiency",
                "Vitamin B12 deficiency",
                "Folate deficiency",
                "Vitamin D deficiency",
                "Calcium deficiency",
            ],
            "answer": "Iron deficiency",
        },
    },
    "GASTROESOPHAGEAL_DISORDERS": {
        "prompt": (
            "You are a gastroenterology expert. Generate a USMLE Step 2 CK question about gastroesophageal disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 50-year-old man presents with heartburn and regurgitation. Endoscopy shows erosive esophagitis. What is the most likely diagnosis?",
            "choices": [
                "Gastroesophageal reflux disease",
                "Peptic ulcer disease",
                "Barrett's esophagus",
                "Achalasia",
                "Esophageal cancer",
            ],
            "answer": "Gastroesophageal reflux disease",
        },
    },
    "HEPATIC_DISORDERS": {
        "prompt": (
            "You are a gastroenterology expert. Generate a USMLE Step 2 CK question about hepatic disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 60-year-old man presents with jaundice and ascites. Liver biopsy shows cirrhosis. What is the most likely underlying cause?",
            "choices": [
                "Alcoholic liver disease",
                "Hepatitis B",
                "Hepatitis C",
                "Non-alcoholic fatty liver disease",
                "Hemochromatosis",
            ],
            "answer": "Alcoholic liver disease",
        },
    },
    "INTESTINAL_AND_COLORECTAL_DISORDERS": {
        "prompt": (
            "You are a gastroenterology expert. Generate a USMLE Step 2 CK question about intestinal and colorectal disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old woman presents with abdominal pain and bloody diarrhea. Colonoscopy shows continuous colonic inflammation. What is the most likely diagnosis?",
            "choices": [
                "Ulcerative colitis",
                "Crohn's disease",
                "Diverticulitis",
                "Irritable bowel syndrome",
                "Colorectal cancer",
            ],
            "answer": "Ulcerative colitis",
        },
    },
    "PANCREATIC_DISORDERS": {
        "prompt": (
            "You are a gastroenterology expert. Generate a USMLE Step 2 CK question about pancreatic disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 55-year-old man presents with epigastric pain radiating to the back. Serum lipase is elevated. What is the most likely diagnosis?",
            "choices": [
                "Acute pancreatitis",
                "Chronic pancreatitis",
                "Pancreatic cancer",
                "Peptic ulcer disease",
                "Gallstones",
            ],
            "answer": "Acute pancreatitis",
        },
    },
    "TUMORS_OF_THE_GI_TRACT": {
        "prompt": (
            "You are a gastroenterology expert. Generate a USMLE Step 2 CK question about tumors of the GI tract. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 70-year-old woman presents with weight loss and anemia. Endoscopy reveals a mass in the stomach. What is the most likely diagnosis?",
            "choices": [
                "Gastric cancer",
                "Colorectal cancer",
                "Esophageal cancer",
                "Pancreatic cancer",
                "Liver cancer",
            ],
            "answer": "Gastric cancer",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are a gastroenterology expert. Generate a USMLE Step 2 CK question about miscellaneous gastrointestinal conditions. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old woman presents with sudden onset of facial droop on the right side. What is the most likely diagnosis?",
            "choices": [
                "Bell's palsy",
                "Stroke",
                "Trigeminal neuralgia",
                "Multiple sclerosis",
                "Myasthenia gravis",
            ],
            "answer": "Bell's palsy",
        },
    },
}

RheumatologyOrthopedicsSports = {
    "CONGENITAL_AND_DEVELOPMENTAL_ANOMALIES": {
        "prompt": (
            "You are an expert in rheumatology and orthopedics. Generate a USMLE Step 2 CK question about congenital and developmental anomalies. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 5-year-old boy presents with bowing of the legs and a waddling gait. X-ray shows widening of the growth plates. What is the most likely diagnosis?",
            "choices": [
                "Rickets",
                "Blount's disease",
                "Achondroplasia",
                "Osteogenesis imperfecta",
                "Developmental dysplasia of the hip",
            ],
            "answer": "Rickets",
        },
    },
    "ARTHRITIS_AND_SPONDYLOARTHROPATHIES": {
        "prompt": (
            "You are an expert in rheumatology and orthopedics. Generate a USMLE Step 2 CK question about arthritis and spondyloarthropathies. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old woman presents with joint pain and morning stiffness lasting more than an hour. X-ray shows joint space narrowing and erosions. What is the most likely diagnosis?",
            "choices": [
                "Rheumatoid arthritis",
                "Osteoarthritis",
                "Ankylosing spondylitis",
                "Psoriatic arthritis",
                "Reactive arthritis",
            ],
            "answer": "Rheumatoid arthritis",
        },
    },
    "AUTOIMMUNE_DISORDERS_AND_VASCULITIDES": {
        "prompt": (
            "You are an expert in rheumatology and orthopedics. Generate a USMLE Step 2 CK question about autoimmune disorders and vasculitides. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 45-year-old man presents with fatigue, weight loss, and a new rash on his legs. Laboratory tests show elevated ESR and positive ANCA. What is the most likely diagnosis?",
            "choices": [
                "Granulomatosis with polyangiitis",
                "Systemic lupus erythematosus",
                "Rheumatoid arthritis",
                "Polyarteritis nodosa",
                "Giant cell arteritis",
            ],
            "answer": "Granulomatosis with polyangiitis",
        },
    },
    "BONE_JOINT_AND_SOFT_TISSUE_INJURIES_AND_INFECTIONS": {
        "prompt": (
            "You are an expert in rheumatology and orthopedics. Generate a USMLE Step 2 CK question about bone, joint, and soft tissue injuries and infections. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 60-year-old man presents with fever and severe pain in his right knee. Synovial fluid analysis shows high white blood cell count with neutrophil predominance. What is the most likely diagnosis?",
            "choices": [
                "Septic arthritis",
                "Gout",
                "Pseudogout",
                "Rheumatoid arthritis",
                "Osteoarthritis",
            ],
            "answer": "Septic arthritis",
        },
    },
    "BONE_TUMORS_AND_TUMOR_LIKE_LESIONS": {
        "prompt": (
            "You are an expert in rheumatology and orthopedics. Generate a USMLE Step 2 CK question about bone tumors and tumor-like lesions. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 20-year-old man presents with pain and swelling in his left femur. X-ray shows a sunburst pattern and Codman's triangle. What is the most likely diagnosis?",
            "choices": [
                "Osteosarcoma",
                "Ewing's sarcoma",
                "Chondrosarcoma",
                "Osteoid osteoma",
                "Giant cell tumor",
            ],
            "answer": "Osteosarcoma",
        },
    },
    "SPINAL_PERIPHERAL_NERVE_DISORDERS_AND_BACK_PAIN": {
        "prompt": (
            "You are an expert in rheumatology and orthopedics. Generate a USMLE Step 2 CK question about spinal/peripheral nerve disorders and back pain. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 50-year-old woman presents with lower back pain radiating to her left leg. MRI shows a herniated disc at L5-S1. What is the most likely diagnosis?",
            "choices": [
                "Herniated disc",
                "Spinal stenosis",
                "Sciatica",
                "Spondylolisthesis",
                "Ankylosing spondylitis",
            ],
            "answer": "Herniated disc",
        },
    },
    "METABOLIC_BONE_DISORDERS": {
        "prompt": (
            "You are an expert in rheumatology and orthopedics. Generate a USMLE Step 2 CK question about metabolic bone disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 70-year-old woman presents with a hip fracture after a minor fall. DEXA scan shows decreased bone density. What is the most likely diagnosis?",
            "choices": [
                "Osteoporosis",
                "Osteomalacia",
                "Paget's disease",
                "Hyperparathyroidism",
                "Osteogenesis imperfecta",
            ],
            "answer": "Osteoporosis",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are an expert in rheumatology and orthopedics. Generate a USMLE Step 2 CK question about miscellaneous rheumatology/orthopedics conditions. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old man presents with heel pain and morning stiffness. X-ray shows calcaneal spur. What is the most likely diagnosis?",
            "choices": [
                "Plantar fasciitis",
                "Achilles tendinitis",
                "Ankylosing spondylitis",
                "Gout",
                "Rheumatoid arthritis",
            ],
            "answer": "Plantar fasciitis",
        },
    },
}

SocialSciencesEthicsLegalProfessional = {
    "COMMUNICATION_AND_INTERPERSONAL_SKILLS": {
        "prompt": (
            "You are an expert in medical ethics and communication. Generate a USMLE Step 2 CK question about communication and interpersonal skills. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 45-year-old man is upset about his recent diagnosis and is not willing to listen to the treatment options. What is the most appropriate initial step in communication?",
            "choices": [
                "Acknowledge his feelings",
                "Provide detailed treatment options",
                "Refer to a specialist",
                "Schedule a follow-up",
                "Discuss prognosis",
            ],
            "answer": "Acknowledge his feelings",
        },
    },
    "HEALTHCARE_POLICY_AND_ECONOMICS": {
        "prompt": (
            "You are an expert in healthcare policy. Generate a USMLE Step 2 CK question about healthcare policy and economics. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A hospital is implementing a new policy to reduce readmission rates. What is the most effective strategy to achieve this goal?",
            "choices": [
                "Enhanced discharge planning",
                "Increased staffing",
                "New electronic health records",
                "Patient satisfaction surveys",
                "Extended visiting hours",
            ],
            "answer": "Enhanced discharge planning",
        },
    },
    "MEDICAL_ETHICS_AND_JURISPRUDENCE": {
        "prompt": (
            "You are an expert in medical ethics. Generate a USMLE Step 2 CK question about medical ethics and jurisprudence. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A patient refuses a life-saving blood transfusion due to religious beliefs. What is the most appropriate action?",
            "choices": [
                "Respect the patient's wishes",
                "Seek a court order",
                "Administer the transfusion",
                "Consult the ethics committee",
                "Discuss with family",
            ],
            "answer": "Respect the patient's wishes",
        },
    },
    "PATIENT_SAFETY": {
        "prompt": (
            "You are an expert in patient safety. Generate a USMLE Step 2 CK question about patient safety. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A nurse notices a medication error before administration. What is the most appropriate next step?",
            "choices": [
                "Report the error immediately",
                "Administer the correct dose",
                "Document the error",
                "Inform the patient",
                "Consult with a pharmacist",
            ],
            "answer": "Report the error immediately",
        },
    },
    "SYSTEM_BASED_PRACTICE_AND_QUALITY_IMPROVEMENT": {
        "prompt": (
            "You are an expert in quality improvement. Generate a USMLE Step 2 CK question about system-based practice and quality improvement. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A clinic is looking to improve patient wait times. What is the most effective initial step?",
            "choices": [
                "Analyze current workflow",
                "Hire more staff",
                "Extend clinic hours",
                "Upgrade technology",
                "Increase appointment slots",
            ],
            "answer": "Analyze current workflow",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are an expert in medical ethics and professionalism. Generate a USMLE Step 2 CK question about miscellaneous social sciences topics. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A medical student witnesses unprofessional behavior by a colleague. What is the most appropriate action?",
            "choices": [
                "Report to a supervisor",
                "Confront the colleague",
                "Ignore the behavior",
                "Discuss with peers",
                "Seek advice from a mentor",
            ],
            "answer": "Report to a supervisor",
        },
    },
}

InfectiousDiseases = {
    "ANTIMICROBIAL_DRUGS": {
        "prompt": (
            "You are an expert in infectious diseases. Generate a USMLE Step 2 CK question about antimicrobial drugs. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 60-year-old man with a history of chronic kidney disease is prescribed an antibiotic for a urinary tract infection. Which antibiotic requires dose adjustment in renal impairment?",
            "choices": [
                "Ciprofloxacin",
                "Azithromycin",
                "Doxycycline",
                "Clindamycin",
                "Metronidazole",
            ],
            "answer": "Ciprofloxacin",
        },
    },
    "BACTERIAL_INFECTIONS": {
        "prompt": (
            "You are an expert in infectious diseases. Generate a USMLE Step 2 CK question about bacterial infections. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 25-year-old woman presents with fever, chills, and a productive cough. Chest X-ray shows lobar consolidation. What is the most likely causative organism?",
            "choices": [
                "Streptococcus pneumoniae",
                "Mycoplasma pneumoniae",
                "Legionella pneumophila",
                "Chlamydia pneumoniae",
                "Klebsiella pneumoniae",
            ],
            "answer": "Streptococcus pneumoniae",
        },
    },
    "FUNGAL_INFECTIONS": {
        "prompt": (
            "You are an expert in infectious diseases. Generate a USMLE Step 2 CK question about fungal infections. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old man with HIV presents with fever and cough. Sputum culture grows yeast with a thick capsule. What is the most likely diagnosis?",
            "choices": [
                "Cryptococcosis",
                "Histoplasmosis",
                "Candidiasis",
                "Aspergillosis",
                "Blastomycosis",
            ],
            "answer": "Cryptococcosis",
        },
    },
    "HIV_AND_SEXUALLY_TRANSMITTED_INFECTIONS": {
        "prompt": (
            "You are an expert in infectious diseases. Generate a USMLE Step 2 CK question about HIV and sexually transmitted infections. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old man presents with a painless ulcer on his genitalia. Serology tests are positive for Treponema pallidum. What is the most likely diagnosis?",
            "choices": [
                "Primary syphilis",
                "Secondary syphilis",
                "Tertiary syphilis",
                "Chancroid",
                "Genital herpes",
            ],
            "answer": "Primary syphilis",
        },
    },
    "INFECTION_CONTROL": {
        "prompt": (
            "You are an expert in infectious diseases. Generate a USMLE Step 2 CK question about infection control. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A hospital is experiencing an outbreak of Clostridium difficile infection. What is the most effective method to prevent the spread?",
            "choices": [
                "Hand hygiene with soap and water",
                "Use of alcohol-based hand sanitizers",
                "Isolation of affected patients",
                "Routine use of antibiotics",
                "Increased cleaning of common areas",
            ],
            "answer": "Hand hygiene with soap and water",
        },
    },
    "PARASITIC_AND_HELMINTHIC_INFECTIONS": {
        "prompt": (
            "You are an expert in infectious diseases. Generate a USMLE Step 2 CK question about parasitic and helminthic infections. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 10-year-old boy presents with abdominal pain and diarrhea. Stool examination reveals eggs with a rough surface. What is the most likely diagnosis?",
            "choices": [
                "Ascariasis",
                "Trichuriasis",
                "Hookworm infection",
                "Strongyloidiasis",
                "Enterobiasis",
            ],
            "answer": "Ascariasis",
        },
    },
    "VIRAL_INFECTIONS": {
        "prompt": (
            "You are an expert in infectious diseases. Generate a USMLE Step 2 CK question about viral infections. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 5-year-old girl presents with fever, cough, and a maculopapular rash. Koplik spots are noted on examination. What is the most likely diagnosis?",
            "choices": ["Measles", "Rubella", "Varicella", "Roseola", "Fifth disease"],
            "answer": "Measles",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are an expert in infectious diseases. Generate a USMLE Step 2 CK question about miscellaneous infectious diseases topics. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 35-year-old woman presents with fever and a new heart murmur. Blood cultures grow Staphylococcus aureus. What is the most likely diagnosis?",
            "choices": [
                "Infective endocarditis",
                "Rheumatic fever",
                "Pericarditis",
                "Myocarditis",
                "Aortic stenosis",
            ],
            "answer": "Infective endocarditis",
        },
    },
}

RenalUrinarySystemsElectrolytes = {
    "NORMAL_STRUCTURE_AND_FUNCTION_OF_THE_KIDNEYS_AND_URINARY_SYSTEM": {
        "prompt": (
            "You are an expert in nephrology. Generate a USMLE Step 2 CK question about the normal structure and function of the kidneys and urinary system. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 25-year-old man presents with flank pain and hematuria. Imaging shows normal kidney structure. What is the most likely diagnosis?",
            "choices": [
                "Renal colic",
                "Pyelonephritis",
                "Glomerulonephritis",
                "Polycystic kidney disease",
                "Renal artery stenosis",
            ],
            "answer": "Renal colic",
        },
    },
    "CONGENITAL_AND_DEVELOPMENTAL_ANOMALIES": {
        "prompt": (
            "You are an expert in nephrology. Generate a USMLE Step 2 CK question about congenital and developmental anomalies of the kidneys and urinary system. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A newborn is found to have a palpable abdominal mass. Ultrasound reveals a multicystic dysplastic kidney. What is the most likely diagnosis?",
            "choices": [
                "Multicystic dysplastic kidney",
                "Polycystic kidney disease",
                "Wilms tumor",
                "Hydronephrosis",
                "Neuroblastoma",
            ],
            "answer": "Multicystic dysplastic kidney",
        },
    },
    "ACUTE_KIDNEY_INJURY": {
        "prompt": (
            "You are an expert in nephrology. Generate a USMLE Step 2 CK question about acute kidney injury. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 70-year-old woman presents with oliguria and elevated creatinine after starting an ACE inhibitor. What is the most likely cause of her acute kidney injury?",
            "choices": [
                "Prerenal azotemia",
                "Acute tubular necrosis",
                "Acute interstitial nephritis",
                "Postrenal obstruction",
                "Glomerulonephritis",
            ],
            "answer": "Prerenal azotemia",
        },
    },
    "CHRONIC_KIDNEY_DISEASE": {
        "prompt": (
            "You are an expert in nephrology. Generate a USMLE Step 2 CK question about chronic kidney disease. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 60-year-old man with diabetes presents with fatigue and anemia. Laboratory tests show decreased GFR. What is the most likely diagnosis?",
            "choices": [
                "Chronic kidney disease",
                "Acute kidney injury",
                "Diabetic nephropathy",
                "Hypertensive nephrosclerosis",
                "Polycystic kidney disease",
            ],
            "answer": "Chronic kidney disease",
        },
    },
    "CYSTIC_KIDNEY_DISEASES": {
        "prompt": (
            "You are an expert in nephrology. Generate a USMLE Step 2 CK question about cystic kidney diseases. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 45-year-old woman presents with hypertension and hematuria. Ultrasound shows multiple cysts in both kidneys. What is the most likely diagnosis?",
            "choices": [
                "Polycystic kidney disease",
                "Multicystic dysplastic kidney",
                "Simple renal cyst",
                "Medullary sponge kidney",
                "Nephronophthisis",
            ],
            "answer": "Polycystic kidney disease",
        },
    },
    "FLUID_ELECTROLYTES_AND_ACID_BASE": {
        "prompt": (
            "You are an expert in nephrology. Generate a USMLE Step 2 CK question about fluid, electrolytes, and acid-base disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old man presents with muscle cramps and weakness. Laboratory tests show hypokalemia and metabolic alkalosis. What is the most likely cause?",
            "choices": [
                "Diuretic use",
                "Renal tubular acidosis",
                "Hyperaldosteronism",
                "Bartter syndrome",
                "Gitelman syndrome",
            ],
            "answer": "Diuretic use",
        },
    },
    "GLOMERULAR_DISEASES_NEPHOTIC_NEPHRITIC_SYNDROME": {
        "prompt": (
            "You are an expert in nephrology. Generate a USMLE Step 2 CK question about glomerular diseases, nephrotic/nephritic syndrome. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 10-year-old boy presents with edema and proteinuria. Laboratory tests show hypoalbuminemia and hyperlipidemia. What is the most likely diagnosis?",
            "choices": [
                "Minimal change disease",
                "Focal segmental glomerulosclerosis",
                "Membranous nephropathy",
                "IgA nephropathy",
                "Post-streptococcal glomerulonephritis",
            ],
            "answer": "Minimal change disease",
        },
    },
    "NEOPLASMS_AND_TRAUMA_OF_THE_KIDNEYS_AND_URINARY_TRACT": {
        "prompt": (
            "You are an expert in nephrology. Generate a USMLE Step 2 CK question about neoplasms and trauma of the kidneys and urinary tract. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 50-year-old man presents with hematuria and flank pain. CT scan shows a mass in the left kidney. What is the most likely diagnosis?",
            "choices": [
                "Renal cell carcinoma",
                "Transitional cell carcinoma",
                "Wilms tumor",
                "Angiomyolipoma",
                "Oncocytoma",
            ],
            "answer": "Renal cell carcinoma",
        },
    },
    "NEPHROLITHIASIS_HEMATURIA_AND_URINARY_TRACT_OBSTRUCTION": {
        "prompt": (
            "You are an expert in nephrology. Generate a USMLE Step 2 CK question about nephrolithiasis, hematuria, and urinary tract obstruction. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 35-year-old woman presents with severe flank pain and hematuria. CT scan shows a 5mm stone in the ureter. What is the most likely diagnosis?",
            "choices": [
                "Nephrolithiasis",
                "Pyelonephritis",
                "Renal cell carcinoma",
                "Bladder cancer",
                "Ureteral stricture",
            ],
            "answer": "Nephrolithiasis",
        },
    },
    "DIABETES_INSIPIDUS": {
        "prompt": (
            "You are an expert in nephrology. Generate a USMLE Step 2 CK question about diabetes insipidus. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old man presents with polyuria and polydipsia. Laboratory tests show low urine osmolality and high serum osmolality. What is the most likely diagnosis?",
            "choices": [
                "Diabetes insipidus",
                "Diabetes mellitus",
                "Primary polydipsia",
                "SIADH",
                "Hypercalcemia",
            ],
            "answer": "Diabetes insipidus",
        },
    },
    "URINARY_INCONTINENCE_RETENTION_GU_INFECTION": {
        "prompt": (
            "You are an expert in nephrology. Generate a USMLE Step 2 CK question about urinary incontinence, retention, and GU infection. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 65-year-old woman presents with urinary urgency and frequency. Urinalysis shows pyuria and bacteriuria. What is the most likely diagnosis?",
            "choices": [
                "Urinary tract infection",
                "Interstitial cystitis",
                "Overactive bladder",
                "Bladder cancer",
                "Vaginitis",
            ],
            "answer": "Urinary tract infection",
        },
    },
}

PregnancyChildbirthPuerperium = {
    "NORMAL_PREGNANCY_CHILDBIRTH_AND_PUERPERIUM": {
        "prompt": (
            "You are an expert in obstetrics. Generate a USMLE Step 2 CK question about normal pregnancy, childbirth, and puerperium. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 28-year-old woman at 39 weeks of gestation presents with regular uterine contractions. Cervical examination shows 5 cm dilation. What is the most appropriate next step in management?",
            "choices": [
                "Admit to labor and delivery",
                "Perform a cesarean section",
                "Administer oxytocin",
                "Discharge home",
                "Perform an amniotomy",
            ],
            "answer": "Admit to labor and delivery",
        },
    },
    "DISORDERS_OF_PREGNANCY_CHILDBIRTH_AND_PUERPERIUM": {
        "prompt": (
            "You are an expert in obstetrics. Generate a USMLE Step 2 CK question about disorders of pregnancy, childbirth, and puerperium. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 32-year-old woman at 28 weeks of gestation presents with severe headache and visual disturbances. Blood pressure is 160/110 mmHg. What is the most likely diagnosis?",
            "choices": [
                "Preeclampsia",
                "Gestational hypertension",
                "Eclampsia",
                "Chronic hypertension",
                "HELLP syndrome",
            ],
            "answer": "Preeclampsia",
        },
    },
}

EarNoseThroatENT = {
    "DISORDERS_OF_THE_EAR_NOSE_AND_THROAT": {
        "prompt": (
            "You are an expert in otolaryngology. Generate a USMLE Step 2 CK question about disorders of the ear, nose, and throat. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old man presents with hearing loss and a sensation of fullness in his right ear. Otoscopic examination reveals a retracted tympanic membrane. What is the most likely diagnosis?",
            "choices": [
                "Eustachian tube dysfunction",
                "Otitis media",
                "Cholesteatoma",
                "Otosclerosis",
                "Acoustic neuroma",
            ],
            "answer": "Eustachian tube dysfunction",
        },
    },
}

EndocrineDiabetesMetabolism = {
    "NORMAL_STRUCTURE_AND_FUNCTION_OF_ENDOCRINE_GLANDS": {
        "prompt": (
            "You are an expert in endocrinology. Generate a USMLE Step 2 CK question about the normal structure and function of endocrine glands. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old woman presents with fatigue and weight gain. Laboratory tests show low T3 and T4 levels with elevated TSH. What is the most likely diagnosis?",
            "choices": [
                "Primary hypothyroidism",
                "Secondary hypothyroidism",
                "Hyperthyroidism",
                "Subclinical hypothyroidism",
                "Euthyroid sick syndrome",
            ],
            "answer": "Primary hypothyroidism",
        },
    },
    "CONGENITAL_AND_DEVELOPMENTAL_ANOMALIES": {
        "prompt": (
            "You are an expert in endocrinology. Generate a USMLE Step 2 CK question about congenital and developmental anomalies of the endocrine system. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A newborn is noted to have ambiguous genitalia and hyponatremia. Laboratory tests show elevated 17-hydroxyprogesterone. What is the most likely diagnosis?",
            "choices": [
                "Congenital adrenal hyperplasia",
                "Androgen insensitivity syndrome",
                "Turner syndrome",
                "Klinefelter syndrome",
                "Hypopituitarism",
            ],
            "answer": "Congenital adrenal hyperplasia",
        },
    },
    "ADRENAL_DISORDERS": {
        "prompt": (
            "You are an expert in endocrinology. Generate a USMLE Step 2 CK question about adrenal disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 50-year-old man presents with hypertension and hypokalemia. Laboratory tests show elevated aldosterone and low renin levels. What is the most likely diagnosis?",
            "choices": [
                "Primary hyperaldosteronism",
                "Secondary hyperaldosteronism",
                "Cushing's syndrome",
                "Addison's disease",
                "Pheochromocytoma",
            ],
            "answer": "Primary hyperaldosteronism",
        },
    },
    "DIABETES_MELLITUS": {
        "prompt": (
            "You are an expert in endocrinology. Generate a USMLE Step 2 CK question about diabetes mellitus. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 45-year-old woman presents with polyuria and polydipsia. Laboratory tests show fasting glucose of 180 mg/dL. What is the most likely diagnosis?",
            "choices": [
                "Type 2 diabetes mellitus",
                "Type 1 diabetes mellitus",
                "Gestational diabetes",
                "Diabetes insipidus",
                "Maturity-onset diabetes of the young",
            ],
            "answer": "Type 2 diabetes mellitus",
        },
    },
    "ENDOCRINE_TUMORS": {
        "prompt": (
            "You are an expert in endocrinology. Generate a USMLE Step 2 CK question about endocrine tumors. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 60-year-old man presents with headaches and sweating. Laboratory tests show elevated catecholamines. Imaging reveals an adrenal mass. What is the most likely diagnosis?",
            "choices": [
                "Pheochromocytoma",
                "Adrenal adenoma",
                "Adrenal carcinoma",
                "Cushing's syndrome",
                "Neuroblastoma",
            ],
            "answer": "Pheochromocytoma",
        },
    },
    "HYPOTHALAMUS_AND_PITUITARY_DISORDERS": {
        "prompt": (
            "You are an expert in endocrinology. Generate a USMLE Step 2 CK question about hypothalamus and pituitary disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 35-year-old woman presents with amenorrhea and galactorrhea. Laboratory tests show elevated prolactin levels. What is the most likely diagnosis?",
            "choices": [
                "Prolactinoma",
                "Hypothyroidism",
                "Cushing's disease",
                "Acromegaly",
                "Sheehan's syndrome",
            ],
            "answer": "Prolactinoma",
        },
    },
    "OBESITY_AND_DYSLIPIDEMIA": {
        "prompt": (
            "You are an expert in endocrinology. Generate a USMLE Step 2 CK question about obesity and dyslipidemia. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 50-year-old man presents with obesity and elevated cholesterol levels. What is the most appropriate initial lifestyle modification?",
            "choices": [
                "Dietary changes",
                "Exercise",
                "Medication",
                "Surgery",
                "Behavioral therapy",
            ],
            "answer": "Dietary changes",
        },
    },
    "REPRODUCTIVE_ENDOCRINOLOGY": {
        "prompt": (
            "You are an expert in endocrinology. Generate a USMLE Step 2 CK question about reproductive endocrinology. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 25-year-old woman presents with irregular menstrual cycles and hirsutism. Laboratory tests show elevated testosterone levels. What is the most likely diagnosis?",
            "choices": [
                "Polycystic ovary syndrome",
                "Hypothyroidism",
                "Hyperprolactinemia",
                "Cushing's syndrome",
                "Androgen insensitivity syndrome",
            ],
            "answer": "Polycystic ovary syndrome",
        },
    },
    "THYROID_DISORDERS": {
        "prompt": (
            "You are an expert in endocrinology. Generate a USMLE Step 2 CK question about thyroid disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old woman presents with weight loss and palpitations. Laboratory tests show low TSH and elevated T3 and T4 levels. What is the most likely diagnosis?",
            "choices": [
                "Graves' disease",
                "Hashimoto's thyroiditis",
                "Subacute thyroiditis",
                "Toxic adenoma",
                "Thyroid storm",
            ],
            "answer": "Graves' disease",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are an expert in endocrinology. Generate a USMLE Step 2 CK question about miscellaneous endocrine topics. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 55-year-old woman presents with fatigue and hyperpigmentation. Laboratory tests show hyponatremia and hyperkalemia. What is the most likely diagnosis?",
            "choices": [
                "Addison's disease",
                "Cushing's syndrome",
                "Hypothyroidism",
                "Hyperparathyroidism",
                "Pheochromocytoma",
            ],
            "answer": "Addison's disease",
        },
    },
}

HematologyOncology = {
    "HEMOSTASIS_AND_THROMBOSIS": {
        "prompt": (
            "You are an expert in hematology. Generate a USMLE Step 2 CK question about hemostasis and thrombosis. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 60-year-old man presents with leg swelling and pain. Doppler ultrasound shows a deep vein thrombosis. What is the most appropriate initial treatment?",
            "choices": ["Heparin", "Warfarin", "Aspirin", "Clopidogrel", "Rivaroxaban"],
            "answer": "Heparin",
        },
    },
    "PLASMA_CELL_DISORDERS": {
        "prompt": (
            "You are an expert in hematology. Generate a USMLE Step 2 CK question about plasma cell disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 70-year-old woman presents with bone pain and fatigue. Laboratory tests show hypercalcemia and elevated serum protein. What is the most likely diagnosis?",
            "choices": [
                "Multiple myeloma",
                "Waldenström's macroglobulinemia",
                "MGUS",
                "Amyloidosis",
                "Chronic lymphocytic leukemia",
            ],
            "answer": "Multiple myeloma",
        },
    },
    "PLATELET_DISORDERS": {
        "prompt": (
            "You are an expert in hematology. Generate a USMLE Step 2 CK question about platelet disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 25-year-old woman presents with petechiae and mucosal bleeding. Laboratory tests show thrombocytopenia. What is the most likely diagnosis?",
            "choices": [
                "Immune thrombocytopenic purpura",
                "Thrombotic thrombocytopenic purpura",
                "Hemolytic uremic syndrome",
                "Disseminated intravascular coagulation",
                "Aplastic anemia",
            ],
            "answer": "Immune thrombocytopenic purpura",
        },
    },
    "RED_BLOOD_CELL_DISORDERS": {
        "prompt": (
            "You are an expert in hematology. Generate a USMLE Step 2 CK question about red blood cell disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 30-year-old man presents with fatigue and pallor. Laboratory tests show microcytic anemia. What is the most likely cause?",
            "choices": [
                "Iron deficiency anemia",
                "Thalassemia",
                "Sideroblastic anemia",
                "Anemia of chronic disease",
                "Lead poisoning",
            ],
            "answer": "Iron deficiency anemia",
        },
    },
    "TRANSFUSION_MEDICINE": {
        "prompt": (
            "You are an expert in hematology. Generate a USMLE Step 2 CK question about transfusion medicine. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 40-year-old woman requires a blood transfusion. She has a history of multiple transfusions. What is the most likely complication?",
            "choices": [
                "Alloimmunization",
                "Transfusion-related acute lung injury",
                "Febrile non-hemolytic transfusion reaction",
                "Acute hemolytic transfusion reaction",
                "Iron overload",
            ],
            "answer": "Alloimmunization",
        },
    },
    "WHITE_BLOOD_CELL_DISORDERS": {
        "prompt": (
            "You are an expert in hematology. Generate a USMLE Step 2 CK question about white blood cell disorders. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 50-year-old man presents with fatigue and night sweats. Laboratory tests show leukocytosis with a left shift. What is the most likely diagnosis?",
            "choices": [
                "Chronic myeloid leukemia",
                "Acute myeloid leukemia",
                "Chronic lymphocytic leukemia",
                "Acute lymphoblastic leukemia",
                "Infectious mononucleosis",
            ],
            "answer": "Chronic myeloid leukemia",
        },
    },
    "PRINCIPLES_OF_ONCOLOGY": {
        "prompt": (
            "You are an expert in oncology. Generate a USMLE Step 2 CK question about the principles of oncology. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 65-year-old woman presents with a breast lump. Biopsy shows invasive ductal carcinoma. What is the most appropriate next step in management?",
            "choices": [
                "Surgical resection",
                "Chemotherapy",
                "Radiation therapy",
                "Hormonal therapy",
                "Observation",
            ],
            "answer": "Surgical resection",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are an expert in hematology and oncology. Generate a USMLE Step 2 CK question about miscellaneous topics in hematology and oncology. "
            "Include a clinical vignette, relevant symptoms, imaging findings, 5 answer options, correct answer, and short explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": "A 45-year-old man presents with fatigue and splenomegaly. Laboratory tests show pancytopenia. What is the most likely diagnosis?",
            "choices": [
                "Myelodysplastic syndrome",
                "Aplastic anemia",
                "Chronic myeloid leukemia",
                "Hairy cell leukemia",
                "Lymphoma",
            ],
            "answer": "Myelodysplastic syndrome",
        },
    },
}
