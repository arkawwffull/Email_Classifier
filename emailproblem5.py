import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


nltk.download('vader_lexicon')


analyzer = SentimentIntensityAnalyzer()

def classify_sentence(sentence):
  
  sentiment = analyzer.polarity_scores(sentence)

 
  negation_words = ["not", "n't", "no", "don't", "cannot", "never"]
  negated = any(word in sentence.lower() for word in negation_words)

  if "electronic" in sentence.lower() or "device" in sentence.lower():
    if "battery" in sentence.lower() or "charge" in sentence.lower() or "not work" in sentence.lower():
      if negated:
        return "feedback"  
      else:
        return "complaint"
    elif "feature" in sentence.lower() or "missing" in sentence.lower():
      return "feedback"

  
  if "toy" in sentence.lower():
    if "broken" in sentence.lower() or "dangerous" in sentence.lower():
      return "complaint"
    elif "fun" in sentence.lower() or "engaging" in sentence.lower():
      return "feedback"

  
  if "makeup" in sentence.lower() or "cosmetic" in sentence.lower():
    if "color" in sentence.lower() or "shade" in sentence.lower() and "not match" in sentence.lower():
      return "complaint"
    elif "quality" in sentence.lower() or "application" in sentence.lower():
      return "feedback"

 
  if "designer" in sentence.lower() or "clothing" in sentence.lower():
    if "size" in sentence.lower() or "fit" in sentence.lower() and "wrong" in sentence.lower():
      return "complaint"
    elif "style" in sentence.lower() or "fabric" in sentence.lower():
      return "feedback"


  
  if "shoe" in sentence.lower() or "sneaker" in sentence.lower() or "boot" in sentence.lower():
    if "size" in sentence.lower() or "fit" in sentence.lower() and "wrong" in sentence.lower():
      return "complaint"
    elif "comfort" in sentence.lower() or "style" in sentence.lower():
      return "feedback"

 
  if "plant" in sentence.lower() or "flower" in sentence.lower() or "herb" in sentence.lower():
    if "wilted" in sentence.lower() or "dead" in sentence.lower():
      return "complaint"
    elif "healthy" in sentence.lower() or "growth" in sentence.lower():
      return "feedback"

  
  if "grocery" in sentence.lower() or "food" in sentence.lower() or "ingredient" in sentence.lower():
    if "expired" in sentence.lower() or "spoiled" in sentence.lower():
      return "complaint"
    elif "quality" in sentence.lower() or "taste" in sentence.lower():
      return "feedback"

  
  if negated and sentiment['compound'] > 0:
    sentiment['compound'] *= -1 

 
  if sentiment['compound'] < -0.2:
    return "complaint"
  elif sentiment['compound'] > 0.2:
    return "feedback"
  else:
    return "neutral"


sentence = input("Enter a sentence: ")


classification = classify_sentence(sentence)
print(f"The sentence is classified as: {classification}")


