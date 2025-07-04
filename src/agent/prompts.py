template_step1 = """
            You are a professional medical board exam question writer.

            You are tasked with generating high-quality USMLE **Step 1**–style **multiple-choice clinical vignette questions**. The questions must be conceptually accurate, test clinical understanding, and reflect realistic scenarios relevant to medical students preparing for Step 1. **Step 1 focuses primarily on DIAGNOSIS** - understanding pathophysiology, mechanisms, and identifying conditions.

            ### Context:
            - Topic: {topic}
            - Subtopic: {subtopic}
            - Prompt guidance: {subtopic_prompt}

            ### Instructions:
            - Generate 10 unique questions, each based on a different clinical vignette.
            - Each vignette should reflect authentic Step 1 scenarios and test understanding of the concept.
            - **Focus on DIAGNOSIS**: Questions should primarily test the ability to identify conditions, understand pathophysiology, and recognize disease mechanisms.
            - Vary the patient presentation (e.g., age, gender, symptoms).
            - Emphasize clinical reasoning over fact recall.
            - Questions must include vitals, labs, or relevant physical findings where appropriate.
            - Ensure the questions are at an appropriate Step 1 difficulty level (not Step 2 CK).
            - Do NOT reuse phrasing or explanations from the sample.
            - Do NOT include letters or numbers (e.g., A, B, C or 1, 2, 3) in the answer choices or the answer.
            - Provide a clear, concise explanation for the correct answer in no more than 5 sentences, focusing on the key clinical reasoning points.
            - Do NOT repeat or reuse any sample content in your generation.

            ### Reference Sample:
            Sample Question: {sample_question}  
            Sample Choices: {sample_choices}  
            Sample Answer: {sample_answer}  
            Sample Explanation: {sample_explanation}

            
            """

template_step2_ck = """
            You are a professional medical board exam question writer.

            You are tasked with generating high-quality USMLE **Step 2 Clinical Knowledge (CK)**–style **multiple-choice clinical vignette questions**. The questions must reflect the unique characteristics of Step 2 CK, focusing on clinical reasoning, diagnosis, management, and patient care scenarios encountered during clinical rotations. **Step 2 CK focuses on DIAGNOSIS + TREATMENT** - not just identifying conditions, but determining the best management, treatment plans, and next steps in patient care.

            ### Context:
            - Topic: {topic}
            - Subtopic: {subtopic}
            - Prompt guidance: {subtopic_prompt}

            ### Instructions:
            - Generate 10 unique questions, each based on a different clinical vignette.
            - Present detailed clinical vignettes, including relevant patient demographics, history, physical exam findings, and laboratory or imaging results.
            - Each patient should vary in age, gender, and symptoms.
            - **Focus on DIAGNOSIS + TREATMENT**: Questions should test not only the ability to diagnose conditions but also to determine appropriate management, treatment plans, and next steps in patient care.
            - Focus on clinical reasoning, diagnosis, management, or the next best step in patient care—especially treatment decisions, considering comorbidities, contraindications, or complications.
            - Reflect real-world scenarios encountered during or after clinical rotations, not preclinical or basic science content.
            - Incorporate content areas unique or emphasized in Step 2 CK, such as ethics, patient safety, hospital systems, quality improvement, and interpretation of clinical research abstracts or pharmaceutical advertisements.
            - Use the "one-best-answer" format:  five plausible answer choices, with only one correct answer.
            - Ensure distractors are realistic and based on common clinical errors or misconceptions.
            - Make the question stem long and information-rich, while keeping answer choices concise.
            - Avoid negative phrasing (e.g., "Which of the following is NOT…").
            - For sequential-item or abstract-based formats, clearly indicate and provide the relevant information.
            - Do NOT include letters or numbers (e.g., A, B, C or 1, 2, 3) in the answer choices or the answer.
            - Provide a clear, concise explanation for the correct answer and why the other options are incorrect, in no more than 5 sentences.
            - Do NOT repeat or reuse any sample content in your generation.
            - Make sure all of the questions are worded differently. Dont format all of the questions the same.
            - ONLY Include Patient Details that are relevant to the question. 
            - Do not include extra patient information that is not relevant to the question or might be misleading.

            ### Reference Sample:
            Sample Question: {sample_question}  
            Sample Choices: {sample_choices}  
            Sample Answer: {sample_answer}  
            Sample Explanation: {sample_explanation}

            
            """
