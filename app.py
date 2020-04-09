# flask api
from flask import Flask, request

# services
from services.game import BlackjackGame

app = Flask(__name__)

blackJack = BlackjackGame()

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/init_game')
def init_game():
    return blackJack.init_game()


@app.route('/gameplay/step', methods=['GET', 'POST'])
def play_hand():
    if request.method == 'POST':
        data = request.get_json()
        return blackJack.step(data['action'])
    elif request.method == 'GET':
        return blackJack.get_state(blackJack.get_player_id())


if __name__ == '__main__':
    app.run()
