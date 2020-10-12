# cuss_inspect

## How It Works

`cuss_inspect` is a logistic regression based model trained on 180K+ reviews and tested on 24K+ reviews.

### Performance


|  | 1 Prediction (ms) | 10 Predictions (ms) | 100 Predictions (ms) | 1000 Predictions (ms) | 10000 Predictions (ms) 
| --------|-------------------|---------------------|-----------------------| -----------------------|----------------------- 
| cuss_inspect | 0.2 | 0.3 | 0.8 | 4.3 | 24.7




### Accuracy

This table speaks for itself:

| | Precision | Recall | F1 Score
| --- | ------- | ------------- | ---------------------- 
0 | 0.84 | 0.94 | 0.89
1 | 0.99 | 0.96 | 0.98
Accuracy | | | 0.96
macro avg | 0.91 | 0.95 | 0.93
weighted avg | 0.96 | 0.96 | 0.96


### Receiver Operating Characteristics 
![ROC Curve](https://github.com/LMSharma/cuss_inspect/blob/main/ROC_Curve.jpeg) 

## Installation

```
$ pip install cuss_inspect
```

## Usage

```python
from cuss_inspect import predict, predict_prob

# for simple string
text_0 = "this is simple review. you have done a good job"
print(predict(text_0))
# [0]
print(predict_prob(text_0)
# [0.05]

text_1 = "son of a bitch"
print(predict(text_1))
# [1]
print(predict_prob(text_1)
# [1.]

# for list of inputs
test = ['who are you?' , 'what do you want?' , 'son of a dog' , 'how the hell can you say that' , 'fuck it']
print(predict(test))
# [0 0 1 1 1]
print(predict_prob(test))
# [0.12 0.22 0.55 0.96 1.]

```

*`predict()` and `predict_prob` return [`numpy`](https://pypi.org/project/numpy/) arrays.
