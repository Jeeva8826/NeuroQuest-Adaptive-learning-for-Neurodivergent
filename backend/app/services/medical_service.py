from typing import List
from app.models.medical import MedicalQuestion

def generate_adhd_questions() -> List[MedicalQuestion]:
    return [
        MedicalQuestion(id=f"adhd_{i}", text=text, options=["Never", "Rarely", "Sometimes", "Often", "Very Often"])
        for i, text in enumerate([
            "Fails to give close attention to details or makes careless mistakes in schoolwork?",
            "Has difficulty sustaining attention in tasks or play activities?",
            "Does not seem to listen when spoken to directly?",
            "Does not follow through on instructions and fails to finish schoolwork or chores?",
            "Has difficulty organizing tasks and activities?",
            "Avoids, dislikes, or is reluctant to engage in tasks that require sustained mental effort?",
            "Loses things necessary for tasks or activities (e.g., school materials, pencils, books)?",
            "Is easily distracted by extraneous stimuli?",
            "Is forgetful in daily activities?",
            "Fidgets with or taps hands or feet or squirms in seat?",
            "Leaves seat in situations when remaining seated is expected?",
            "Runs about or climbs in situations where it is inappropriate?",
            "Unable to play or engage in leisure activities quietly?",
            "Is 'on the go,' acting as if 'driven by a motor'?",
            "Talks excessively?",
            "Blurts out an answer before a question has been completed?",
            "Has difficulty waiting their turn?",
            "Interrupts or intrudes on others (e.g., butts into conversations, games, or activities)?",
            "At what age were these symptoms first consistently observed?",
            "Is there a family history of ADHD or related executive functioning disorders?",
            "Are symptoms present in two or more settings (e.g., home and school)?",
            "Do the symptoms significantly interfere with academic or social functioning?",
            "Has the child previously been prescribed stimulant medication?",
            "Has the child previously been prescribed non-stimulant medication?",
            "Are there observed co-occurring tics or Tourette's syndrome symptoms?",
            "Does the child experience significant sleep onset insomnia?",
            "Are there documented instances of hyperfocus on specific interests?",
            "Has an EEG been performed to rule out absence seizures?",
            "Is there a history of occupational therapy for fine motor skills?",
            "Does the child experience frequent emotional dysregulation or 'meltdowns'?"
        ])
    ]

def generate_autism_questions() -> List[MedicalQuestion]:
    return [
        MedicalQuestion(id=f"asd_{i}", text=text, options=["Never", "Rarely", "Sometimes", "Often", "Very Often"])
        for i, text in enumerate([
            "Exhibits deficits in social-emotional reciprocity?",
            "Fails to initiate or respond to social interactions?",
            "Demonstrates reduced sharing of interests, emotions, or affect?",
            "Exhibits deficits in nonverbal communicative behaviors used for social interaction?",
            "Displays abnormalities in eye contact and body language?",
            "Shows deficits in understanding and use of gestures?",
            "Has a total lack of facial expressions and nonverbal communication?",
            "Exhibits deficits in developing, maintaining, and understanding relationships?",
            "Has difficulty adjusting behavior to suit various social contexts?",
            "Shares imaginative play or makes friends easily?",
            "Shows an absence of interest in peers?",
            "Exhibits stereotyped or repetitive motor movements, use of objects, or speech?",
            "Lines up toys or flips objects repetitively?",
            "Uses echolalia or idiosyncratic phrases?",
            "Insists on sameness, inflexible adherence to routines, or ritualized patterns?",
            "Experiences extreme distress at small changes?",
            "Has difficulties with transitions or rigid thinking patterns?",
            "Demonstrates highly restricted, fixated interests that are abnormal in intensity?",
            "Displays strong attachment to or preoccupation with unusual objects?",
            "Exhibits hyper- or hyporeactivity to sensory input?",
            "Shows apparent indifference to pain or temperature?",
            "Has an adverse response to specific sounds or textures?",
            "Engages in excessive smelling or touching of objects?",
            "Displays visual fascination with lights or movement?",
            "Were symptoms present in the early developmental period?",
            "Do symptoms cause clinically significant impairment in current functioning?",
            "Are these disturbances better explained by intellectual disability or global developmental delay?",
            "Has the child undergone formal ADOS-2 or ADI-R testing?",
            "Is there a history of speech delay or regression of language skills?",
            "Are there gastrointestinal comorbidities (e.g., chronic constipation/diarrhea)?"
        ])
    ]

def generate_dyslexia_questions() -> List[MedicalQuestion]:
    return [
        MedicalQuestion(id=f"dys_{i}", text=text, options=["Never", "Rarely", "Sometimes", "Often", "Very Often"])
        for i, text in enumerate([
            "Difficulty reading words accurately and fluently?",
            "Struggles with spelling?",
            "Difficulty with reading comprehension?",
            "Avoids reading aloud?",
            "Reads slowly and with great effort?",
            "Confuses visually similar letters (e.g., b/d, p/q)?",
            "Confuses words that sound alike?",
            "Difficulty sounding out unfamiliar words?",
            "Has a history of language delay?",
            "Difficulty remembering sequences (e.g., days of the week, months)?",
            "Struggles with rote memorization?",
            "Has difficulty expressing thoughts in writing?",
            "Exhibits poor handwriting or fine motor difficulties?",
            "Has trouble copying from the board?",
            "Requires extra time to complete written assignments?",
            "Has a family history of reading difficulties?",
            "Did the child struggle with learning nursery rhymes?",
            "Has difficulty recognizing rhyming words?",
            "Struggles to break words into syllables?",
            "Difficulty identifying the first sound in a word?",
            "Has trouble learning the names and sounds of letters?",
            "Guesses at words based on context or the first letter?",
            "Skips or replaces small words (e.g., a, the, of) when reading?",
            "Complains that words move or blur on the page?",
            "Experiences headaches or eye strain when reading?",
            "Has an aversion to school or reading-related activities?",
            "Has difficulty following multi-step written instructions?",
            "Struggles with math word problems despite good calculation skills?",
            "Has received previous phonics-based interventions?",
            "Shows a significant discrepancy between verbal ability and reading performance?"
        ])
    ]

def get_medical_questions(condition: str) -> List[MedicalQuestion]:
    cond = condition.lower()
    if "autism" in cond or "asd" in cond:
        return generate_autism_questions()
    elif "dyslexia" in cond:
        return generate_dyslexia_questions()
    else:
        # Default to ADHD or generic
        return generate_adhd_questions()
