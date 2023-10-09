from transformers import BertTokenizer, BertModel
import numpy as np

# Cargar el modelo y el tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Ejemplo de documentos
documents = ["Este es el primer documento.", "Aquí hay un segundo documento.", "Y este es el tercer documento."]

# Tokenizar y obtener embeddings para los documentos
document_embeddings = []
for doc in documents:
    tokens = tokenizer(doc, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**tokens)
        embeddings = outputs.last_hidden_state.mean(dim=1).numpy()  # Promedio de embeddings de tokens
    document_embeddings.append(embeddings)

# Ahora tienes representaciones vectoriales de los documentos
for i, embedding in enumerate(document_embeddings):
    print(f"Embedding del documento {i + 1}:\n{embedding}\n")

