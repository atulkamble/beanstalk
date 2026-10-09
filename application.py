
from flask import Flask, jsonify

application = Flask(__name__)

@application.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AWS Elastic Beanstalk | Flask Demo</title>

    <style>
        * { box-sizing: border-box; }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            line-height: 1.6;
        }

        header {
            background: #111827;
            border-bottom: 1px solid #334155;
            padding: 18px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }

        .brand {
            font-size: 21px;
            font-weight: bold;
            color: #ff9900;
        }

        nav a {
            color: #cbd5e1;
            text-decoration: none;
            margin-left: 20px;
        }

        nav a:hover { color: #ff9900; }

        .hero {
            text-align: center;
            padding: 75px 20px;
            background: linear-gradient(135deg, #172554, #0f172a);
        }

        .badge {
            display: inline-block;
            background: #14532d;
            color: #86efac;
            padding: 7px 16px;
            border-radius: 30px;
            font-size: 13px;
        }

        h1 {
            font-size: clamp(32px, 5vw, 52px);
            margin: 22px 0 12px;
            line-height: 1.2;
        }

        .hero p {
            color: #94a3b8;
            max-width: 620px;
            margin: 0 auto 26px;
        }

        .button {
            display: inline-block;
            background: #ff9900;
            color: #111827;
            padding: 12px 24px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
        }

        .button:hover { background: #ffb84d; }

        .container {
            max-width: 1100px;
            margin: auto;
            padding: 55px 20px;
        }

        h2 { margin-bottom: 10px; }

        .subtitle {
            color: #94a3b8;
            margin-bottom: 25px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }

        .card {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 25px;
        }

        .card h3 { color: #ff9900; }

        .card p { color: #cbd5e1; }

        .step {
            border-left: 3px solid #ff9900;
            padding: 12px 20px;
            margin-bottom: 15px;
            background: #1e293b;
            border-radius: 0 8px 8px 0;
        }

        .step strong { color: #ff9900; }

        .architecture {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 25px;
            text-align: center;
        }

        .architecture img {
            max-width: 100%;
            max-height: 450px;
            height: auto;
            background: white;
            border-radius: 8px;
        }

        code {
            color: #86efac;
            overflow-wrap: anywhere;
        }

        footer {
            background: #111827;
            padding: 25px;
            text-align: center;
            color: #94a3b8;
            border-top: 1px solid #334155;
        }

        @media (max-width: 600px) {
            header { justify-content: center; }
            nav a { margin: 0 8px; }
            .hero { padding: 55px 20px; }
        }
    </style>
</head>

<body>

<header>
    <div class="brand">☁ AWS Elastic Beanstalk</div>
    <nav>
        <a href="#features">Features</a>
        <a href="#architecture">Architecture</a>
        <a href="#deployment">Deployment</a>
        <a href="/health">Health API</a>
    </nav>
</header>

<section class="hero">
    <span class="badge">● Flask Application Running</span>
    <h1>Deploy Applications<br>Without Managing Servers</h1>
    <p>
        A simple Flask web application demonstrating
        AWS Elastic Beanstalk, application deployment,
        scaling, monitoring and environment management.
    </p>
    <a class="button" href="#features">Explore Features →</a>
</section>

<section class="container" id="features">
    <h2>Elastic Beanstalk Features</h2>
    <p class="subtitle">Understand the main capabilities.</p>

    <div class="grid">
        <div class="card">
            <h3>🚀 Easy Deployment</h3>
            <p>Deploy Python applications without manually configuring servers.</p>
        </div>

        <div class="card">
            <h3>⚖ Auto Scaling</h3>
            <p>Automatically adjust EC2 capacity based on application demand.</p>
        </div>

        <div class="card">
            <h3>🔀 Load Balancing</h3>
            <p>Distribute incoming traffic across multiple EC2 instances.</p>
        </div>

        <div class="card">
            <h3>📊 Monitoring</h3>
            <p>Monitor environment health and metrics with AWS services.</p>
        </div>

        <div class="card">
            <h3>🔄 Blue-Green Deployment</h3>
            <p>Switch between environments to reduce deployment downtime.</p>
        </div>

        <div class="card">
            <h3>🐍 Python Flask</h3>
            <p>Run a Python web application using the Flask framework.</p>
        </div>
    </div>
</section>

<section class="container" id="architecture">
    <h2>Application Architecture</h2>
    <p class="subtitle">Typical load-balanced environment architecture.</p>

    <div class="architecture">
        <img src="/beanstalk.svg" alt="Elastic Beanstalk Architecture">
    </div>
</section>

<section class="container" id="deployment">
    <h2>Deployment Workflow</h2>
    <p class="subtitle">Basic deployment process using the EB CLI.</p>

    <div class="step">
        <strong>Step 1 — Create Flask Application</strong>
        <p>Write the application code in <code>app.py</code>.</p>
    </div>

    <div class="step">
        <strong>Step 2 — Install Dependencies</strong>
        <p><code>pip install -r requirements.txt</code></p>
    </div>

    <div class="step">
        <strong>Step 3 — Initialize Elastic Beanstalk</strong>
        <p><code>eb init</code></p>
    </div>

    <div class="step">
        <strong>Step 4 — Create Environment</strong>
        <p><code>eb create flask-demo-env</code></p>
    </div>

    <div class="step">
        <strong>Step 5 — Deploy Updates</strong>
        <p><code>eb deploy</code></p>
    </div>

    <div class="step">
        <strong>Step 6 — Open Website</strong>
        <p><code>eb open</code></p>
    </div>
</section>

<section class="container">
    <h2>Blue-Green Deployment</h2>
    <p class="subtitle">Use separate environments for application releases.</p>

    <div class="architecture">
        <img src="/blue-green.svg" alt="Blue Green Deployment">
    </div>
</section>

<footer>
    AWS Elastic Beanstalk | Flask Demo Application
    <p>Cloud & DevOps Training Project</p>
</footer>

</body>
</html>
"""


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
