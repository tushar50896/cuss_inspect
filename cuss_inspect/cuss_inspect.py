import pickle
import pkg_resources
#load vectorizer to make  tfidfvectors of the review
vectorizer = pickle.load(open(pkg_resources.resource_filename('cuss_inspect', 'data/vectorizer_v4.lgst'),'rb'))

#load our pretrained ML model
model = pickle.load(open(pkg_resources.resource_filename('cuss_inspect', 'data/logitclf_v4.lgst'),'rb'))

def process(user_input):
	input_type = type(user_input)
	if input_type ==str:
		return  [user_input]
	else:
		return  user_input

def predict(texts):
    return model.predict(vectorizer.transform(process(texts)))

def predict_prob(texts):
    return model.predict_proba(vectorizer.transform(process(texts)))[:,1].round(decimals=2)
