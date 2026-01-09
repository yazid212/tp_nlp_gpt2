"""
test_simple.py - Fichier de test pour l'assistant pédagogique
"""

# ============================
# IMPORTS
# ============================
from assistant_pedagogique import preprocess_text, reformuler_texte

# ============================
# TESTS
# ============================
print("🧪 TESTS SIMPLES - ASSISTANT PÉDAGOGIQUE")
print("=" * 50)

# Test 1 : Prétraitement
print("\n1. TEST DE PRÉTRAITEMENT :")
texte_test_1 = "La photosynthèse est importante pour les plantes!!!   Avec  plusieurs   espaces."
print(f"   Original : '{texte_test_1}'")
print(f"   Nettoyé  : '{preprocess_text(texte_test_1)}'")

# Test 2 : Reformulation courte
print("\n2. TEST DE REFORMULATION (court) :")
texte_test_2 = "La photosynthèse est importante."
print(f"   Original   : {texte_test_2}")
resultat = reformuler_texte(texte_test_2, max_length=60)
print(f"   Reformulé : {resultat}")

# Test 3 : Reformulation plus longue
print("\n3. TEST DE REFORMULATION (long) :")
texte_test_3 = """
Les plantes utilisent la photosynthèse pour transformer la lumière du soleil 
en énergie chimique grâce à la chlorophylle dans leurs feuilles.
"""
print(f"   Original : {texte_test_3.strip()}")
resultat_long = reformuler_texte(texte_test_3, max_length=100)
print(f"   Reformulé : {resultat_long}")

# Test 4 : Test avec différents textes
print("\n4. TESTS AVEC DIFFÉRENTS CONCEPTS :")
concepts = [
    "L'eau bout à 100 degrés Celsius.",
    "La gravité est une force d'attraction entre les masses.",
    "Les mitochondries produisent l'énergie dans les cellules."
]

for i, concept in enumerate(concepts, 1):
    print(f"\n   Concept {i}: {concept}")
    print(f"   Prétraité : {preprocess_text(concept)}")
    print(f"   Reformulé : {reformuler_texte(concept, max_length=70)}")

# Test 5 : Vérification des longueurs
print("\n5. TEST DES LONGUEURS :")
print("   Max 40 caractères :", reformuler_texte("La Terre est ronde.", max_length=40)[:50])
print("   Max 80 caractères :", reformuler_texte("La Terre est ronde.", max_length=80)[:50])
print("   Max 120 caractères:", reformuler_texte("La Terre est ronde.", max_length=120)[:50])

print("\n" + "=" * 50)
print("✅ TOUS LES TESTS SONT TERMINÉS !")
print("=" * 50)