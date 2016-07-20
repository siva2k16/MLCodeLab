import pickle as p
from sklearn.linear_model import Perceptron
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import hstack

# We have 60000 train tweets, 20000 dev and 20000 test
# Each of these files is a list of (tweet, sentiment pairs)
trainSetPath = "data/train.p"
devSetPath   = "data/dev.p"
testSetPath  = "data/test.p"

# For a given list tweet (in raw text), return a matrix of features 
#(one row representing each tweet).
# If we are getting features for the trainSet, have the dictVectorizer learn
# how to index additional features 
def getFeatures(tweets, countVec, dictVec, isTrainSet=False, verbose = False):
    bagOfWordsMatrix = #TODO Get back of words representation of tweets.

    if verbose:
        print "Shape of bag of word matrix", bagOfWordsMatrix.shape
        print

    # Build list of feature dictionaries
    additionalFeatures = #TODO build a list of feature dictionaries, to get the tweet length

    if isTrainSet:
        additionalFeatureMatrix = #TODO train dictVec on trainSet and get a feature matrix
    else:
        additionalFeatureMatrix = #TODO get a feature matrix from dictVec

    if verbose:
        print "Shape of additionalFeatureMatrix", additionalFeatureMatrix.shape
        print
        # Print feature names
        print "Names of additional features", dictVec.get_feature_names()        
        print

    # Horizontally stack matrices (column-wise) to build one large feature matrix
    X = #TODO Combine the two feature matricies

    if verbose:
        print "Shape of feature matrix", X.shape

        print "Example of tweet:", tweets[0]
        analyser = countVec.build_analyzer()        
        print "How this tweet was tokenized", analyser(tweets[0])
        print "Corresponding feature vector", X.toarray()[0]
    return X

# Return portion of Labels with postion of labels
def getLabelDist(Y):
    portionPos =  sum([int(y) for y in Y])*1./len(Y)
    return "Percent Labels Positive", str(portionPos)

if __name__ == "__main__":

    trainSet =  p.load(open(trainSetPath, 'rb'))

    perceptron = Perceptron(verbose=1, n_iter=15)

    #Extract tweets and labels into 2 lists
    trainTweets = [t[0] for t in trainSet]
    trainY = [t[1] for t in trainSet]

    print "Train label distribution", getLabelDist(trainY)

    # To reperent a tweet, we'll start with the following features
    # Bag of words for the 100 most common words (we'll use a CountVectorizer for this)
    # Length of the tweet in characters 

    countVec =  #TODO initiliaze the count vectorizer
    dictVec  =  #TODO initiliaze the dict vectorizer

    # Fit the CountVectorizer to the trainTweets
    # This method calculates the top words in the train set, and builds
    # The 100 word voculary the countVectorizer will use in the future    
    countVec.fit(trainTweets)

    print "Vocab of countVec"
    print #TODO print vocab of countVec


    # Implement getFeautres() to return a feature matrix for any
    # list of tweets.

    #Now get train features.
    trainX = getFeatures(trainTweets, countVec, dictVec, True, True)
    
    #Train the perceptron
    
    0 #TODO Train the perceptron

    #Get features and labels for development set.
    devSet =     #TODO open devSetPath and load it into devSet
    devTweets =  #TODO get the tweets from devSet

    devX =  #TODO Get features for those tweets
    devY =  #TODO Get the labels for the dev set

    print "Train label distribution", getLabelDist(devY)

    # This is how you predict labels for devSet
    predictedLabels = perceptron.predict(devX)

    #Print out accuracy for trainSet
    print "Train set accuracy:", #TODO get train set accuracy
    #Print out accuracy for devSet
    print "Dev set accuracy:", #TODO get dev set accuracy