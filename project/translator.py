import os
from google.cloud import language_v1
from google.cloud import translate_v2 as translate
from google.api_core.exceptions import InvalidArgument

PROJECT_ID = 'cnguyen4-cpsc324-final-project'

def detect_language(text):
    """Detects the language of the text."""
    translate_client = translate.Client()
    result = translate_client.detect_language(text)
    return result['language']

def translate_text(text, target_language="en"):
    """Translates text into the target language if necessary."""
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

def analyze_entities(text):
    """Analyzes entities in the text if the language is supported."""
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    try:
        response = client.analyze_entities(document=document)
        entities = [{'name': entity.name, 'type': entity.type_, 'salience': entity.salience} for entity in response.entities]
        return entities
    except InvalidArgument as e:
        print(f"Unsupported language for entity analysis: {e}")
        return None

def process_text(text):
    """Processes the text to detect language, translate if necessary, and analyze entities."""
    detected_language = detect_language(text)
    print(f"Detected language: {detected_language}")

    if detected_language != "en":
        print("Translating text to English for analysis...")
    
    # print("Analyzing entities...")
    # entities = analyze_entities(text)
    # if entities:
    #     print("Detected entities:", entities)

