from flask import Flask
from conversation.conversation_api import conversation_bp
from sentiment_analysis.sentiment_analysis_api import sentiment_bp
from suggestion_prediction.suggestion_api import suggestion_bp
from summary_generator.summary_generator_api import summary_bp



app = Flask(__name__)


# Register Blueprints
app.register_blueprint(conversation_bp, url_prefix='/api/conversation')
app.register_blueprint(sentiment_bp, url_prefix='/api/sentiment')
app.register_blueprint(suggestion_bp, url_prefix='/api/suggestion')
app.register_blueprint(summary_bp, url_prefix='/api/summary')

if __name__ == '__main__':
    app.run(debug=True)
