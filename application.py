from flask import Flask,request,render_template
from src.conversation.conversation_api import conversation_bp
from src.sentiment_analysis.sentiment_analysis_api import sentiment_bp
from src.suggestion_prediction.suggestion_api import suggestion_bp
from src.summary_generator.summary_generator_api import summary_bp



app = Flask(__name__)


# Register Blueprints
app.register_blueprint(conversation_bp, url_prefix='/api/conversation')
app.register_blueprint(sentiment_bp, url_prefix='/api/sentiment')
app.register_blueprint(suggestion_bp, url_prefix='/api/suggestion')
app.register_blueprint(summary_bp, url_prefix='/api/summary')

@app.route('/')
def index():
    return render_template('index.html')
 

if __name__ == '__main__':
    app.run(host="0.0.0.0")
