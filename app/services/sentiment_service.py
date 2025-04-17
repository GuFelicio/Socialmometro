from transformers import XLMRobertaTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

model_name = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

labels = ['negativo', 'neutro', 'positivo']

def analisar_sentimento(texto: str) -> dict:
    try:
        # Tokeniza e prepara input
        inputs = tokenizer(texto, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
            scores = F.softmax(outputs.logits, dim=1)[0]

        sentimento_index = torch.argmax(scores).item()
        sentimento_label = labels[sentimento_index]

        # NOVO: pega score da classe positiva (índice 2)
        score_positivo = scores[2].item()
        porcentagem = int(score_positivo * 100)
        estrelas = round(porcentagem / 20)

        return {
            "sentimento": sentimento_label,
            "porcentagem": porcentagem,
            "estrelas": estrelas
        }

    except Exception:
        return {
            "sentimento": "neutro",
            "porcentagem": 50,
            "estrelas": 3
        }