## Text Mining
### Natural Language Toolkit
- A basic library for text mining on Python
- Text mining involves looking at pieces of text and trying to make sense out of them.

##### Word cloud
- Look at the words in the text
- Count their frequency
- Throw them out intot the cloud, where each word is sized based relative to its frequency in the text.
- We can very quickly see what the text is saying


##### Text analysis-Complexity analysis
- Look at how complex a particular document is.
  - In general, if you have a technical document, it might have longer words.
  - The average sentence length for people expressing more complex ideas,
  - then they will probably use longer sentences rather than shorter ones.
  - the vocabulary of the sentence / see the ratio of unique words. It's a little bit iffy.
  - Keeping that in mind, so when you do the vocabulary proportion, you probably want to be also comparing documents that are similar in size.
- Complexity is the average word length of a document.
  - average word length: longer words adds to complexity
  - average sentence length: longer sentences are more complex (unless the text is rambling!)
  - vocabulary: the ratio of unique words used to the total number of words (more variety, more complexity)

- So in general, when you're dealing with text mining,
  - you start with the idea of a token.
  - A token is a sequence or a group of characters of interest.
    - Generally: A token is the base unit of analysis
  - So, the first step is to convert text into tokens and nltk text object
    - NLTK provides two functions that are useful for that.
    - There's sentence tokenize and word tokenize.
    - And each of them are there to create words and sentences.
    - Get rid of stuff that is not something that's a word or a sentence.

##### Look at US Presidentinaugural speeches
- Often, a comparitive analysis helps us understand text better


- Dispersion plots are really useful,
  - show us given certain woods,
  - show how the relative frequency of those words change over time.


##### Named entity analysis
- Let's say you're looking at analyst reports,
- and you have a set of 1,000 reports--you want to take a few hundred of them and run through those,
- pull out all the named entities from there, and then eyeball them and see, do they make sense?
- And then remove things that are not named entities.

- The whole goal
  - is that once you have the named entities,
  - you can use these named entities to compute sentiments on them.
  - So let's say we want to-- we know that Service is the name entity, and we want to
  - find out whether the restaurant is positive in service or negative in service.

##### Text summarization
- Generate a short summary of a large piece of text automatically.
- These summaries can serve as an input into a topic analyzer to
- figure out what the main topic of the text is.

- Extraction based summarization
  - Most of text summarization works on something called extraction based summarization.
  - Take the text, and look for what sentences you consider important,
  - and then report those sentences in your summary.
  - Sort of way
    - Identify the most frequent words in a piece of text,
    - and use those occurrences of those words in a sentence to
    - decide whether that is important or not.
  - How
    - Import the stuff
    - import word tokenize, sentense tokenize
      - lowercase the words and sentenses
      - Tokenize the strip text, get a bunch of candidate sentences.
    - import stop words, which is words that are unimportant,
      - like or, and, the, and all that stuff.
      - Getting rid of unimportant ones, numbers and end of line chars.
    - import the frequents FREQ distribution,
      - which determines the frequency distribution of words.
      - construct the word frequencies and
      - choose the most common n of those words.

    - import order dictionary, which is a special kind of dictionary.
      - Remember dictionaries in Python are not ordered.
    - Setting candidate sentence to an empty set, summary sentences to an empty list.
    - Candidate sentences dictionary
      - when we compute our summary, we want to be using only lower case letters.
      - When we report our summary, we want to report it with the original cases.
      - Get the total count of the frequency score, each candidate senence count
      - Sort it by the count, order the dict

- Advanced techniques called abstraction based,
  - which try to abstract knowledge from the document itself,
  - but those are more complicated.

- A naive form of summarization is to
  - identify the most frequent words in a piece of text and
  - use the occurrence of these words in sentences to
  - rate the importance of a sentence.

- If the documents are focused, you're going to get a good summary.


##### Gensim summarizer
- is a little bit better summarizer
- It uses nodes and lexical similarity as weights on the OCs.

##### Topic modeling
- What Python can do is
  - it can give you a sense for what the main topics of a document are.
  - But you have to make sense of those topics.
  - It'll give you a bunch of words and say
  - these are the words that are likely to be going together as a topic.

- We need to import
  - JSON includes the LDA model.
  - for JSON, we need to Import capora.
  - a LDA model.
  -  input stop words.
  -  input PPrint, for pretty printing stuff.

- Take out the stop words, we get a sentence here.
  - A list of sentence words. A list of lists, and each sublist is the words in a sentence.
- Create a dictionary and a corpus.
  - The dictionary is every word in the text is given a number (word,frequency) pairs.
  - The goal here roughly is to construct sentences that are
    - replacing the word by number,
    - keep track of what the linkage between the word and the number is.
    - all LDA is doing is it's creating a network of these sentences.
- See how closely related they are.
  - Then it knows that there's a linkage of three of the words are connected in those two sentences.
  - So rather than looking at words, it looks at numbers.
  - It's much faster. So text is much harder to handle.

- Goal
  - replace our sentences by--the words in our sentences by numbers,
  - and then create a corpus that has two pos where
    - you have the number of the word in a sentence
    - and the frequency of its occurrence in that sentence.
  - So rechargeable occurs twice in this,
  - so that's an important word in that sentence.
  - That's the vaguely rough idea.


#### LDA
- Parameters:
  - Number of topics: The number of topics you want generated.
  - The larger the document, the more the desirable topics
  - Passes: The LDA model makes through the document. More passes, slower analysis

- How do we match tipics to documents?

- You have a bunch of documents
- Figure all these topics are
- Give names to these tipics

##### The similarity of documents.

