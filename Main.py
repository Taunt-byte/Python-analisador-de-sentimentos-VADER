import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Baixar os recursos do VADER (se necessário)
nltk.download('vader_lexicon')

# Instanciar o SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Função para realizar a análise de sentimento
def analyze_sentiment():
    text = text_entry.get("1.0", "end-1c")  # Obter o texto da caixa de texto
    
    if text.strip() == "":
        messagebox.showwarning("Aviso", "Digite um texto para análise de sentimento.")
        return
    
    # Realizar a análise de sentimento
    sentiment_scores = sia.polarity_scores(text)
    compound_score = sentiment_scores['compound']

    # Classificar o sentimento com base no valor da polaridade
    if compound_score >= 0.05:
        sentiment = 'Positivo'
    elif compound_score <= -0.05:
        sentiment = 'Negativo'
    else:
        sentiment = 'Neutro'

    # Exibir o resultado em uma caixa de diálogo
    messagebox.showinfo("Resultado", f"Sentimento: {sentiment}\nPontuação composta: {compound_score}")

# Criar a janela principal
window = tk.Tk()
window.title("Analisador de Sentimentos")
window.geometry("400x300")

# Rótulo
label = tk.Label(window, text="Insira o texto para análise de sentimento:")
label.pack(pady=10)

# Caixa de texto
text_entry = tk.Text(window, height=5)
text_entry.pack()

# Botão de análise
analyze_button = tk.Button(window, text="Analisar Sentimento", command=analyze_sentiment)
analyze_button.pack(pady=10)

# Executar a interface gráfica
window.mainloop()
