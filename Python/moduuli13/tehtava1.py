from flask import Flask, Response
import json


app = Flask(__name__)
@app.route('/alkuluku/<num1>')
def alkuluku(num1):

#alkuluku testaus kopioitu pienillä muokkauksilla aikaisemmista tehtävistä
    try:
        num1 = num1
        luku = int(num1)

        print(luku)

        on = True

        if luku < 2:
            on = False

        else:

            alkuluku = 1

            for x in range(2, luku):
                if luku % x == 0:
                    alkuluku = 0
                    break

        if alkuluku == 1:
            on = True

        else:
            on = False

        if on:
            return (f'Numero {num1} on alkuluku')
        if not on:
            return (f'Numero {num1} ei ole alkuluku')


    except ValueError:
        vastaus = {
        'status': 400,
        'text': 'could not float input'
        }

    json_answer = json.dumps(vastaus)
    return Response(response=json_answer, status='400', mimetype='application/json')


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
