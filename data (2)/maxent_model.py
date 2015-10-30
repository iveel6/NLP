#input training file
#testing file
#run type 1 -  non-contextual model  (output_test1.tag)
#		  2 - context-sensitive model
#  		  3 - context-sensitive model with Viterbi

#command maxent_model.py data/train.tag data/test.tag 3 > output_test3.tag
import sys
train = sys.argv[1]
test = sys.argv[2]
output = sys.argv[3]
def model(train_file = train, test_file = test, outputNumber = sys.argv[3]):
	#print train_file, test_file, outputNumber
	f = open(train_file, 'r')
	identifier = f.readline()
	while identifier:
		tokens = f.readline()
		word_tags = tokens.split()
		print word_tags
		for word_tag in word_tags:
			wt = word_tag.split("_")
			w = wt[0]
			t = wt[1]
			print w, t
		identifier = f.readline()
 


if __name__ == "__main__":
	#model();
	model('./data/expTrain.tag')

