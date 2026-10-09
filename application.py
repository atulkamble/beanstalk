
from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return """
    <h1>AWS Elastic Beanstalk</h1>
    <p>Website deployed successfully!</p>
    """

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
