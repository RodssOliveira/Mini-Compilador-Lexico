from flask import Flask, render_template, url_for, jsonify, request
import compilador

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    return render_template('compiler.html', titulo='Compilador')

@app.route('/api/process_code', methods=['POST'])
def compiler():
    code = request.form['code']
    resultado = compilador.compiler(code)
    app.logger.info(resultado)

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=False)