from flask import Flask, render_template, request, jsonify, send_file
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/A1G')
def a1g_page():
    return render_template('pages/A/A1G.html')


@app.route('/A1F')
def a1f_page():
    return render_template('pages/A/A1F.html')


@app.route('/A1E')
def a1e_page():
    return render_template('pages/A/A1E.html')


@app.route('/B1G')
def b1g_page():
    return render_template('pages/B/B1G.html')


@app.route('/B1F')
def b1f_page():
    return render_template('pages/B/B1F.html')


@app.route('/B1E')
def b1e_page():
    return render_template('pages/B/B1E.html')


@app.route('/B2G')
def b2g_page():
    return render_template('pages/B/B2G.html')


@app.route('/B2F')
def b2f_page():
    return render_template('pages/B/B2F.html')


@app.route('/B2E')
def b2e_page():
    return render_template('pages/B/B2E.html')


@app.route('/B3G')
def b3g_page():
    return render_template('pages/B/B3G.html')


@app.route('/B3F')
def b3f_page():
    return render_template('pages/B/B3F.html')


@app.route('/B3E')
def b3e_page():
    return render_template('pages/B/B3E.html')


@app.route('/B4G')
def b4g_page():
    return render_template('pages/B/B4G.html')


@app.route('/B4F')
def b4f_page():
    return render_template('pages/B/B4F.html')


@app.route('/B4E')
def b4e_page():
    return render_template('pages/B/B4E.html')


@app.route('/C1G')
def c1g_page():
    return render_template('pages/C/C1G.html')


@app.route('/C1F')
def c1f_page():
    return render_template('pages/C/C1F.html')


@app.route('/C1E')
def c1e_page():
    return render_template('pages/C/C1E.html')


@app.route('/runcode', methods=['POST'])
def run_code():
    try:
        code = request.json['code']
        result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, text=True)
        return jsonify({'output': result})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/download_pdf/<filename>')
def download_pdf(filename):
    # Specify the path to the PDF files directory
    pdfs_directory = 'static/doc_files/'

    # Use Flask's send_file function to send the requested file for download
    return send_file(pdfs_directory + filename, as_attachment=True)


if __name__ == '__main__':
    app.run()
