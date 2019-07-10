# news-category
simple category classifier using flask


How to run:
1. run all cell in text_classifier.ipynb
2. execute command ```python app.py``` as application server
3. execute this command in new command prompt for predict category of the text
```
curl -X POST -d "{\"text\": \"this is a news news news\"}" http://localhost:5000/predict -H "Content-Type:application/json
```
