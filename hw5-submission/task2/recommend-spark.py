from pyspark.mllib.recommendation import ALS
from pyspark import SparkContext

# load training and test data into (user, product, rating) tuples

def parseRating(line):
  fields = line.split()
  if len(fields) > 2:
      return (int(fields[0]), int(fields[1]), float(fields[2]))   
  else:
      return (int(fields[0]), int(fields[1]), 0.0)

sc = SparkContext()
training = sc.textFile("spark-input-rating.txt").map(parseRating).cache()
test = sc.textFile("spark-input-pair.txt").map(parseRating)
 
# train a recommendation model
model = ALS.train(training, rank = 10, iterations = 5)
 
# make predictions on (user, product) pairs from the test data
predictions = model.predictAll(test.map(lambda x: (x[0], x[1])))
