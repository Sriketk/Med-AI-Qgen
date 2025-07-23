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
            "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK-style clinical question focused on population health, public health interventions, social determinants of health, or global burden of disease. "
            "Include a realistic clinical vignette with demographic context, relevant statistics or public health data, 5 answer choices, a correct answer, and a concise explanation that includes core epidemiologic reasoning. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A 62-year-old man with type 2 diabetes and hypertension presents for a routine follow-up. His primary care physician practices in a county with high rates of cardiovascular disease-related mortality. The physician wants to prioritize interventions that offer the greatest impact on population health in this region. Which of the following public health strategies would be expected to have the greatest effect on reducing cardiovascular mortality at the population level?""",
            "choices": [
                "Implementing a community exercise program for adults over age 60",
                "Launching a national awareness campaign about dietary sodium",
                "Subsidizing medications for secondary prevention of coronary artery disease",
                "Regulating tobacco product advertising and sales",
                "Expanding access to cardiac catheterization laboratories",
            ],
            "answer": "Regulating tobacco product advertising and sales",
            "explanation": "Tobacco control policies (e.g., advertising bans, taxation, sales restrictions) are among the most effective and scalable public health interventions for reducing cardiovascular mortality. While clinical programs are helpful, regulatory strategies targeting risk factors at the population level have the broadest and most cost-effective impact.",
        },
    },
    "MEASURES_AND_DISTRIBUTION_OF_DATA": {
        "prompt": (
            "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK-style question focused on interpretation of central tendency, variability, skewness, or distribution of data in a clinical or research context. "
            "Include a clinical vignette, relevant numerical data, 5 answer options, a correct answer, and a short explanation with interpretation of statistical measures. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A researcher collects systolic blood pressure measurements from 1,000 patients in a cardiology clinic. The data are right-skewed due to a subset of patients with poorly controlled hypertension. The mean is 148 mmHg, median is 135 mmHg, and mode is 130 mmHg. Which of the following statements best describes this data set?""",
            "choices": [
                "The data are normally distributed",
                "The median is greater than the mean",
                "The mean is the best measure of central tendency",
                "The distribution is left-skewed",
                "The median is less affected by outliers than the mean",
            ],
            "answer": "The median is less affected by outliers than the mean",
            "explanation": "In a right-skewed distribution, the mean is pulled in the direction of the tail by extreme values (outliers). The median is more resistant to outliers and better represents the central location of skewed data.",
        },
    },
    "PROBABILITY_AND_PRINCIPLES_OF_TESTING": {
        "prompt": (
            "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK-style question involving test characteristics (sensitivity, specificity, PPV, NPV, likelihood ratios, Bayes' theorem), clinical decision thresholds, or diagnostic reasoning. "
            "Embed these concepts within a realistic clinical vignette and return 5 answer options, a correct answer, and a concise explanation that teaches core probability principles. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A 45-year-old woman presents with fatigue, weight gain, and cold intolerance. Her physician suspects hypothyroidism and orders a TSH test, which returns slightly elevated. The physician considers ordering confirmatory free T4 levels. The TSH test has a sensitivity of 95% and specificity of 85% for hypothyroidism. The prevalence of hypothyroidism in the population is 2%. Which of the following best explains the likelihood that this patient actually has hypothyroidism based on the TSH result?""",
            "choices": [
                "High due to the test’s high sensitivity",
                "Low due to the test’s low specificity",
                "Low due to the low prevalence of hypothyroidism",
                "High because the TSH test is a gold standard",
                "Uncertain without the free T4 level",
            ],
            "answer": "Low due to the low prevalence of hypothyroidism",
            "explanation": "Despite high sensitivity and specificity, the positive predictive value of a test depends heavily on disease prevalence. In low-prevalence settings, even good tests have a higher rate of false positives, reducing the likelihood that a positive result reflects true disease (Bayes' theorem).",
        },
    },
    "STUDY_DESIGN_AND_INTERPRETATION": {
        "prompt": (
            "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK-style question about study design or result interpretation. Focus on randomized controlled trials, cohort studies, case-control studies, biases, confounders, or validity measures. "
            "Provide a clinical vignette with study parameters and 5 answer choices. Include the correct answer and a concise explanation that reinforces key epidemiologic reasoning. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A study evaluates the effect of a new diabetes drug on the incidence of stroke. Researchers assign patients with poor glycemic control to the treatment group and those with well-controlled diabetes to the placebo group. Over 5 years, the treatment group has a lower incidence of stroke. Which of the following best explains the primary limitation of this study design?""",
            "choices": [
                "Recall bias",
                "Loss to follow-up",
                "Survivorship bias",
                "Confounding by indication",
                "Selection bias due to randomization",
            ],
            "answer": "Confounding by indication",
            "explanation": "Patients with worse disease severity were preferentially assigned to treatment, introducing confounding by indication — a type of selection bias where disease severity influences treatment choice and outcome. This weakens causal inference unless controlled via randomization or statistical adjustment.",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are a biostatistics and epidemiology expert. Generate a USMLE Step 2 CK-style question about an advanced or mixed-concept topic that does not fit neatly into core categories. "
            "This may include ROC curves, number needed to treat, attributable risk, interaction effects, meta-analysis, or ethics in statistical reporting. Include a vignette, 5 answer choices, correct answer, and a concise teaching explanation. "
            "Return ONLY a valid JSON object as described in the schema."
        ),
        "sample_question": {
            "question": """A clinical trial compares two cholesterol-lowering drugs. The number needed to treat (NNT) with Drug A is 50 to prevent one myocardial infarction, while the NNT for Drug B is 100. Which of the following conclusions is most appropriate?""",
            "choices": [
                "Drug B is more effective at reducing MI risk",
                "Drug A has twice the efficacy of Drug B",
                "Drug A has a greater absolute risk reduction than Drug B",
                "The relative risk reduction of Drug B is greater",
                "Both drugs are equally effective since both reduce risk",
            ],
            "answer": "Drug A has a greater absolute risk reduction than Drug B",
            "explanation": "NNT is the inverse of absolute risk reduction (ARR). A lower NNT means a higher ARR, implying Drug A prevents more events per treated patient. It does not necessarily reflect relative risk or overall efficacy without context.",
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
            "You are a dermatology expert. Generate a high-yield USMLE Step 2 CK question on normal structure and function of the skin. "
            "Include a clinical vignette, patient presentation, histological correlation, 5 answer options, correct answer, and a brief but clear explanation. "
            "Return ONLY a valid JSON object according to the schema."
        ),
        "sample_question": {
            "question": "A 22-year-old swimmer presents with persistent skin dryness and cracking, especially after training sessions. Examination reveals xerotic patches and mild erythema on the dorsal hands and feet. A skin biopsy reveals decreased ceramide content and disruption of the stratum corneum lipid layer. Which of the following skin functions is most directly impaired?",
            "choices": [
                "Barrier to water loss",
                "Melanin production",
                "Sebum secretion",
                "Tactile sensation",
                "Thermoregulation via eccrine glands",
            ],
            "answer": "Barrier to water loss",
            "explanation": "The stratum corneum is the outermost layer of the epidermis, rich in lipids (including ceramides), which form the water barrier. Dysfunction here impairs water retention and causes xerosis.",
        },
    },
    "DISORDERS_OF_EPDERMAL_APPENDAGES": {
        "prompt": (
            "You are a dermatology expert. Write a clinically detailed USMLE Step 2 CK question on disorders of epidermal appendages. "
            "Include a full vignette with symptoms, possible risk factors, histology if relevant, 5 answer options, correct answer, and a short explanation."
        ),
        "sample_question": {
            "question": "A 34-year-old woman presents with painful nodules and draining sinus tracts in the groin and underarms. She notes scarring from prior lesions. She has a BMI of 32 and reports smoking 1 pack per day. Biopsy shows follicular occlusion and perifollicular lymphocytic infiltration. What is the most likely diagnosis?",
            "choices": [
                "Hidradenitis suppurativa",
                "Acne conglobata",
                "Folliculitis decalvans",
                "Pilonidal cyst",
                "Dissecting cellulitis",
            ],
            "answer": "Hidradenitis suppurativa",
            "explanation": "Hidradenitis suppurativa is a chronic inflammatory condition affecting apocrine gland–bearing areas, often triggered by follicular occlusion. It presents with nodules, sinus tracts, and scarring.",
        },
    },
    "INFLAMMATORY_DERMATOSES_AND_BULLOUS_DISEASES": {
        "prompt": (
            "You are a dermatology expert. Generate a challenging USMLE Step 2 CK vignette about inflammatory dermatoses and bullous diseases. "
            "Include symptoms, progression, biopsy findings, and plausible distractors. Provide 5 answer choices, correct answer, and a concise explanation."
        ),
        "sample_question": {
            "question": "A 72-year-old man presents with itchy, tense blisters on his lower abdomen and thighs. Nikolsky sign is negative. Skin biopsy reveals a subepidermal split with linear IgG and C3 deposition along the basement membrane on direct immunofluorescence. What is the most likely diagnosis?",
            "choices": [
                "Bullous pemphigoid",
                "Pemphigus vulgaris",
                "Dermatitis herpetiformis",
                "Linear IgA bullous dermatosis",
                "Toxic epidermal necrolysis",
            ],
            "answer": "Bullous pemphigoid",
            "explanation": "Bullous pemphigoid presents with tense, non-fragile blisters in older adults. It shows subepidermal separation and linear IgG/C3 deposition along the basement membrane zone.",
        },
    },
    "SKIN_AND_SOFT_TISSUE_INFECTIONS": {
        "prompt": (
            "You are a dermatology expert. Create a USMLE Step 2 CK question on skin and soft tissue infections. Include microbiology, risk factors, clinical presentation, and decision-making. "
            "Provide 5 answer options, the correct one, and a brief explanation."
        ),
        "sample_question": {
            "question": "A 64-year-old man with diabetes presents with an erythematous, warm, and tender plaque on his lower leg. He has a low-grade fever. The borders are raised and sharply demarcated. Blood cultures are pending. What is the most likely causative organism?",
            "choices": [
                "Streptococcus pyogenes",
                "Staphylococcus aureus",
                "Pseudomonas aeruginosa",
                "Clostridium perfringens",
                "Mycobacterium marinum",
            ],
            "answer": "Streptococcus pyogenes",
            "explanation": "Erysipelas, a superficial skin infection with sharply demarcated borders, is classically caused by Streptococcus pyogenes. Risk factors include diabetes and skin barrier disruption.",
        },
    },
    "SKIN_TUMORS_AND_TUMOR_LIKE_LESIONS": {
        "prompt": (
            "You are a dermatology expert. Write a USMLE Step 2 CK–level question about skin tumors. Include histopathological clues and clinical differentiation. "
            "Return a JSON with a question stem, 5 choices, the correct answer, and a short explanation."
        ),
        "sample_question": {
            "question": "A 59-year-old woman presents with a slowly enlarging pearly papule on her upper cheek. It bleeds occasionally when rubbed. Dermoscopy reveals arborizing telangiectasias. A punch biopsy shows basaloid cell nests with peripheral palisading. What is the most likely diagnosis?",
            "choices": [
                "Basal cell carcinoma",
                "Squamous cell carcinoma",
                "Amelanotic melanoma",
                "Actinic keratosis",
                "Seborrheic keratosis",
            ],
            "answer": "Basal cell carcinoma",
            "explanation": "Basal cell carcinoma commonly presents as a pearly nodule with telangiectasias. Histology shows basaloid cells with peripheral palisading and clefting from surrounding stroma.",
        },
    },
    "MISCELLANEOUS": {
        "prompt": (
            "You are a dermatology expert. Create a high-yield USMLE Step 2 CK vignette from a miscellaneous dermatology topic (e.g., systemic disease manifestations, drug eruptions, photodermatoses). "
            "Include a clinical stem, 5 answer choices, the correct answer, and a brief rationale."
        ),
        "sample_question": {
            "question": "A 28-year-old woman presents with facial rash that worsens after sun exposure. Examination reveals a malar rash sparing the nasolabial folds. She also reports arthralgias and fatigue. ANA is positive with anti-dsDNA antibodies. What is the most likely diagnosis?",
            "choices": [
                "Systemic lupus erythematosus",
                "Polymorphous light eruption",
                "Rosacea",
                "Seborrheic dermatitis",
                "Dermatomyositis",
            ],
            "answer": "Systemic lupus erythematosus",
            "explanation": "The malar rash in SLE typically spares the nasolabial folds. Other systemic features (arthralgia, fatigue) and positive anti-dsDNA support the diagnosis.",
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
