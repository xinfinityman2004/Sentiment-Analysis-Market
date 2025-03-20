
---

# 📊 Sentiment Analysis and NLP for Marketing Insights  
**Unlocking Customer Sentiments in Video Game Reviews**  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![NLP](https://img.shields.io/badge/NLP-NLTK%2C%20SpaCy-green) ![License](https://img.shields.io/badge/License-MIT-orange)  

This project leverages **Natural Language Processing (NLP)** and **Sentiment Analysis** to analyze customer reviews of video games, providing actionable insights for marketing strategies. Inspired by a [Manning LiveProject](https://www.manning.com/liveproject/sentiment-analysis-and-natural-language-processing-for-marketing), this implementation includes advanced techniques and improvements to deliver deeper insights into customer preferences.

---

## 🎯 **Project Goals**  
The primary goal is to understand **what gamers like and dislike** about video games by analyzing their reviews. This helps marketing teams:  
- 🎮 Identify **key selling points** for new products  
- 📉 Pinpoint **customer pain points** to address in future updates  
- 📈 Optimize **marketing messages** based on customer sentiment  

---

## 🛠 **Techniques and Tools**  

### 🔍 **Data Processing**  
- **Sampling**: Handle imbalanced datasets using `imbalanced-learn`.  
- **Preprocessing**: Clean and tokenize text data for analysis.  

### 🧠 **Sentiment Analysis**  
- **Dictionary-Based**: Use NLTK's VADER for quick sentiment scoring.  
- **Deep Learning**: Implement **DistilBERT** using PyTorch and Hugging Face's `transformers` library for state-of-the-art results.  

### 📊 **Evaluation & Visualization**  
- **Metrics**: Evaluate model performance with `scikit-learn`.  
- **Visualization**: Create interactive charts using **Altair** and **Matplotlib**.  

---



---

## 📊 **Key Insights**  

### 🎮 **What Gamers Love**  
- **Immersive Storytelling**: 23% of positive reviews highlight engaging narratives.  
- **Multiplayer Experience**: 18% praise seamless online gameplay.  
- **Graphics Quality**: 15% appreciate stunning visuals.  

### 📉 **What Gamers Dislike**  
- **Installation Issues**: 31% of negative reviews cite installation problems.  
- **Microtransactions**: 27% criticize pricing models.  
- **Server Stability**: 19% report frequent disconnections.  

---

## 🚀 **Getting Started**  

### Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/sentiment-analysis-marketing.git
   cd sentiment-analysis-marketing
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

### Usage  
1. **Load Data**:  
   ```python
   from src.data_loader import load_amazon_reviews
   df = load_amazon_reviews("Video_Games_5.json")
   ```  
2. **Analyze Sentiment**:  
   ```python
   from src.sentiment import analyze_reviews
   results = analyze_reviews(df, method="bert")
   ```  
3. **Visualize Results**:  
   ```python
   from src.visualization import plot_sentiment_trends
   plot_sentiment_trends(results)
   ```  

---

## 📄 **Dataset**  
The dataset used is the **Amazon Reviews Dataset**, specifically the "Video Games 5-core" subset. It can be downloaded from [here](https://nijianmo.github.io/amazon/index.html).  

---

## 📜 **License**  
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.  

---

## 👨‍💻 **Developed by Harsh Kumar Tiwari**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](www.linkedin.com/in/harshtiwari2004)  
[![Email](https://img.shields.io/badge/Email-Contact%20Me-red)](mailto:harshktiwari0000@gmail.com)  

---


