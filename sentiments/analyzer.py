import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        
        
        word = []
        self.positives =[]
        self.negatives = []
    
        with open("positive-words.txt", "r") as pos_words:
            
            for line in pos_words:
        
                if (not line.startswith(";")  and not line.startswith(" ")):
                    
                    
                    self.positives.extend(line.split())
               
        with open("negative-words.txt", "r") as neg_words:
            for line in neg_words:
      
                if (not line.startswith(";")  and not line.startswith(" ")):
                    
                    self.negatives.extend(line.split())
         
         
       

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        
        score =0
        
        for token in tokens:
           
           
           if token.lower() in self.positives:
               score += 1
               
           elif token.lower() in self.negatives:
               score -= 1
               
        return score
