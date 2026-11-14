from flask import Flask, jsonify, render_template

application = Flask(__name__)

@application.route("/")
def home():
    return render_template("index.html")


@application.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Flask Elastic Beanstalk Demo",
        "version": "1.0"
    })


@application.route("/beanstalk.svg")
def architecture():
    return application.send_static_file("beanstalk.svg")


@application.route("/blue-green.svg")
def blue_green():
    return application.send_static_file("blue-green.svg")


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
