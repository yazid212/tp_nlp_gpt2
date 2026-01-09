"""
Assistant Pédagogique avec GPT-2 - VERSION FINALE
TP NLP - Complétion du projet selon le PDF fourni
"""

# ============================
# IMPORTS
# ============================
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import re

# ============================
# QUESTION 2 : CHARGEMENT DU MODÈLE
# ============================
print("Chargement du modèle GPT-2...")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# CORRECTION COMPLÈTE : Configurer le tokenizer
tokenizer.pad_token = tokenizer.eos_token

print("✅ Modèle GPT-2 chargé !\n")

# ============================
# QUESTION 1 : PRÉTRAITEMENT DU TEXTE
# ============================
def preprocess_text(texte):
    """
    Prétraitement simple du texte pédagogique
    Réduit le bruit et homogénéise l'entrée
    """
    # 1. Supprimer les caractères spéciaux non désirés
    texte = re.sub(r'[^\w\s.,!?:;\-éèêëàâäôöûüçÉÈÊËÀÂÄÔÖÛÜÇ]', '', texte)

    # 2. Normaliser les espaces
    texte = re.sub(r'\s+', ' ', texte)
    texte = texte.strip()

    # 3. Remplacer les sauts de ligne multiples
    texte = texte.replace('\n', ' ').replace('\r', ' ')

    return texte

# ============================
# QUESTION 3 : REFORMULATION DE TEXTE
# ============================
def reformuler_texte(texte, max_length=100):
    """
    Reformule un texte pédagogique de manière simple
    UTILISE UN PROMPT EN ANGLAIS POUR DE MEILLEURS RÉSULTATS
    """
    # PROMPT EN ANGLAIS + demande de réponse en français
    prompt = "Explain the following concept in simple French: " + texte

    # Encodage avec attention_mask
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = torch.ones_like(inputs)

    # Génération du texte avec TOUS les paramètres nécessaires
    outputs = model.generate(
        inputs,
        attention_mask=attention_mask,  # CORRECTION IMPORTANTE
        max_length=max_length,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,  # Ajouté pour de meilleurs résultats
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
        repetition_penalty=1.1  # Évite la répétition
    )

    # Décodage
    resultat = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Retirer le prompt du résultat
    if prompt in resultat:
        resultat = resultat.replace(prompt, "").strip()

    return resultat

# ============================
# QUESTION 4 : EFFET DU PROMPT
# ============================
def tester_prompts_differents(texte, max_length=120):
    """
    Teste deux prompts différents sur le même texte
    TOUS LES PROMPTS SONT EN ANGLAIS
    """
    # Prompt 1 : Simple
    prompt_simple = "Explain in simple French: " + texte

    # Prompt 2 : Avec exemple
    prompt_exemple = "Explain in French and give a concrete example: " + texte

    resultats = {}

    prompts = {
        "Reformulation simple": prompt_simple,
        "Reformulation avec exemple": prompt_exemple
    }

    for nom, prompt in prompts.items():
        inputs = tokenizer.encode(prompt, return_tensors="pt")
        attention_mask = torch.ones_like(inputs)

        outputs = model.generate(
            inputs,
            attention_mask=attention_mask,  # CORRECTION
            max_length=max_length,
            do_sample=True,
            top_k=50,
            top_p=0.9,
            temperature=0.8,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id
        )

        texte_genere = tokenizer.decode(outputs[0], skip_special_tokens=True)
        if prompt in texte_genere:
            texte_genere = texte_genere.replace(prompt, "").strip()
        resultats[nom] = texte_genere

    return resultats

# ============================
# QUESTION 4 bis : GÉNÉRATION DE QCM
# ============================
def generer_qcm(texte, max_length=200):
    """
    Génère un mini QCM à partir d'un texte pédagogique
    PROMPT EN ANGLAIS
    """
    # Prompt orienté QCM - en anglais
    prompt = (
        "Based on this text, create a short quiz in French with 2 questions "
        "and 3 answer choices per question. Include the correct answer.\n\n"
        "Text: " + texte + "\n\n"
        "Quiz:"
    )

    # Encodage
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = torch.ones_like(inputs)

    # Génération
    outputs = model.generate(
        inputs,
        attention_mask=attention_mask,  # CORRECTION
        max_length=max_length,
        do_sample=True,
        top_k=40,
        top_p=0.85,
        temperature=0.9,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

    # Décodage
    qcm = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Nettoyage
    if prompt in qcm:
        qcm = qcm.replace(prompt, "").strip()

    return qcm

# ============================
# FONCTION PRINCIPALE - DÉMONSTRATION
# ============================
def main():
    print("=" * 60)
    print("ASSISTANT PÉDAGOGIQUE GPT-2 - TP NLP")
    print("=" * 60)

    # Texte pédagogique d'exemple
    texte_exemple = """
    La photosynthèse est un processus utilisé par les plantes pour convertir 
    l'énergie lumineuse en énergie chimique. Elle se déroule dans les chloroplastes 
    et nécessite du dioxyde de carbone, de l'eau et de la lumière.
    """

    print("\n📝 TEXTE ORIGINAL :")
    print(texte_exemple)

    # 1. Prétraitement
    texte_propre = preprocess_text(texte_exemple)
    print("\n✅ TEXTE APRÈS PRÉTRAITEMENT :")
    print(texte_propre)

    # 2. Reformulation (Question 3)
    print("\n" + "=" * 60)
    print("QUESTION 3 : REFORMULATION DE TEXTE")
    print("=" * 60)

    texte_reformule = reformuler_texte(texte_propre, max_length=120)
    print("📝 Résultat de la reformulation :")
    print(texte_reformule)

    # 3. Effet des prompts (Question 4)
    print("\n" + "=" * 60)
    print("QUESTION 4 : EFFET DU PROMPT")
    print("=" * 60)

    resultats_prompts = tester_prompts_differents(texte_propre)

    for nom, resultat in resultats_prompts.items():
        print(f"\n🔹 {nom} :")
        print(resultat)

    # 4. Génération de QCM (Question 4 bis)
    print("\n" + "=" * 60)
    print("QUESTION 4 bis : GÉNÉRATION DE QCM")
    print("=" * 60)

    qcm_genere = generer_qcm(texte_propre, max_length=250)
    print("📝 QCM généré :")
    print(qcm_genere)

    # 5. Analyse critique (Question 5)
    print("\n" + "=" * 60)
    print("QUESTION 5 : ANALYSE CRITIQUE")
    print("=" * 60)
    print("""
    LIMITES DE GPT-2 DANS UN CONTEXTE ÉDUCATIF :

    1. LANGUE : Principalement entraîné sur l'anglais, français limité
    2. PRÉCISION : Risque d'inexactitudes factuelles
    3. CONTEXTE : Ne comprend pas le niveau de l'apprenant
    4. COHÉRENCE : Peut générer des contradictions
    5. VÉRIFICATION : Pas de validation automatique
    6. BIAIS : Reproduction des biais du dataset
    7. QCM : Options parfois peu pertinentes
    """)

    print("\n" + "=" * 60)
    print("✅ PROJET TERMINÉ AVEC SUCCÈS !")
    print("=" * 60)

# ============================
# EXÉCUTION
# ============================
if __name__ == "__main__":
    main()