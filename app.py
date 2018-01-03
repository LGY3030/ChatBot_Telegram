import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

import json
import os 

os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

with open('tunnels.json') as data_file:
    datajson = json.load(data_file)

for i in datajson['tunnels']:
    msg =i['public_url']+'/hook'

API_TOKEN = '454897554:AAEk7aa_dRdsUMTDWvhHZF0kAWpF1vPlM0I'
WEBHOOK_URL = msg

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'stateNCKUCSIEIntroduction',
        'stateHistory',
        'stateProfessor',
        'state1','state2',
        'state3','state4',
        'state5','state6',
        'state7','state8',
        'state9','state10',
        'state11','state12',
        'state13','state14',
        'state15','state16',
        'state17','state18',
        'state19','state20',
        'state21','state22',
        'state23','state24',
        'state25','state26',
        'state27','state28',
        'state29','state30',
        'state31','state32',
        'state33','state34',
        'state35','state36',
        'state37','state38',
        'state39','state40',
        'state41','state42',
        'statePsychologicalTest',
        'stateLove',
        'stateLoveA','stateLoveB',
        'stateLoveC','stateLoveD',
        'stateLoveE',
        'statePersonality',
        'statePersonalityA','statePersonalityB',
        'statePersonalityC','statePersonalityD',
        'stateWork',
        'stateWorkA','stateWorkB',
        'stateWorkC','stateWorkD',
        'stateChat',
        'stateChat1','stateChat2',
        'stateChat3','stateChat4',
        'stateJoke',
        'stateJokeNormal','stateJokeTurbo'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'stateNCKUCSIEIntroduction',
            'conditions': 'is_going_to_stateNCKUCSIEIntroduction'
        },
        {
            'trigger': 'advance',
            'source': 'stateNCKUCSIEIntroduction',
            'dest': 'stateHistory',
            'conditions': 'is_going_to_stateHistory'
        },
        {
            'trigger': 'advance',
            'source': 'stateNCKUCSIEIntroduction',
            'dest': 'stateProfessor',
            'conditions': 'is_going_to_stateProfessor'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state8',
            'conditions': 'is_going_to_state8'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state9',
            'conditions': 'is_going_to_state9'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state10',
            'conditions': 'is_going_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state11',
            'conditions': 'is_going_to_state11'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state12',
            'conditions': 'is_going_to_state12'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state13',
            'conditions': 'is_going_to_state13'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state14',
            'conditions': 'is_going_to_state14'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state15',
            'conditions': 'is_going_to_state15'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state16',
            'conditions': 'is_going_to_state16'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state17',
            'conditions': 'is_going_to_state17'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state18',
            'conditions': 'is_going_to_state18'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state19',
            'conditions': 'is_going_to_state19'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state20',
            'conditions': 'is_going_to_state20'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state21',
            'conditions': 'is_going_to_state21'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state22',
            'conditions': 'is_going_to_state22'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state23',
            'conditions': 'is_going_to_state23'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state24',
            'conditions': 'is_going_to_state24'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state25',
            'conditions': 'is_going_to_state25'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state26',
            'conditions': 'is_going_to_state26'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state27',
            'conditions': 'is_going_to_state27'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state28',
            'conditions': 'is_going_to_state28'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state29',
            'conditions': 'is_going_to_state29'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state30',
            'conditions': 'is_going_to_state30'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state31',
            'conditions': 'is_going_to_state31'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state32',
            'conditions': 'is_going_to_state32'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state33',
            'conditions': 'is_going_to_state33'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state34',
            'conditions': 'is_going_to_state34'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state35',
            'conditions': 'is_going_to_state35'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state36',
            'conditions': 'is_going_to_state36'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state37',
            'conditions': 'is_going_to_state37'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state38',
            'conditions': 'is_going_to_state38'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state39',
            'conditions': 'is_going_to_state39'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state40',
            'conditions': 'is_going_to_state40'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state41',
            'conditions': 'is_going_to_state41'
        },
        {
            'trigger': 'advance',
            'source': 'stateProfessor',
            'dest': 'state42',
            'conditions': 'is_going_to_state42'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'statePsychologicalTest',
            'conditions': 'is_going_to_statePsychologicalTest'
        },
        {
            'trigger': 'advance',
            'source': 'statePsychologicalTest',
            'dest': 'stateLove',
            'conditions': 'is_going_to_stateLove'
        },
        {
            'trigger': 'advance',
            'source': 'stateLove',
            'dest': 'stateLoveA',
            'conditions': 'is_going_to_stateLoveA'
        },
        {
            'trigger': 'advance',
            'source': 'stateLove',
            'dest': 'stateLoveB',
            'conditions': 'is_going_to_stateLoveB'
        },
        {
            'trigger': 'advance',
            'source': 'stateLove',
            'dest': 'stateLoveC',
            'conditions': 'is_going_to_stateLoveC'
        },
        {
            'trigger': 'advance',
            'source': 'stateLove',
            'dest': 'stateLoveD',
            'conditions': 'is_going_to_stateLoveD'
        },
        {
            'trigger': 'advance',
            'source': 'stateLove',
            'dest': 'stateLoveE',
            'conditions': 'is_going_to_stateLoveE'
        },
        {
            'trigger': 'advance',
            'source': 'statePsychologicalTest',
            'dest': 'statePersonality',
            'conditions': 'is_going_to_statePersonality'
        },
        {
            'trigger': 'advance',
            'source': 'statePersonality',
            'dest': 'statePersonalityA',
            'conditions': 'is_going_to_statePersonalityA'
        },
        {
            'trigger': 'advance',
            'source': 'statePersonality',
            'dest': 'statePersonalityB',
            'conditions': 'is_going_to_statePersonalityB'
        },
        {
            'trigger': 'advance',
            'source': 'statePersonality',
            'dest': 'statePersonalityC',
            'conditions': 'is_going_to_statePersonalityC'
        },
        {
            'trigger': 'advance',
            'source': 'statePersonality',
            'dest': 'statePersonalityD',
            'conditions': 'is_going_to_statePersonalityD'
        },
        {
            'trigger': 'advance',
            'source': 'statePsychologicalTest',
            'dest': 'stateWork',
            'conditions': 'is_going_to_stateWork'
        },
        {
            'trigger': 'advance',
            'source': 'stateWork',
            'dest': 'stateWorkA',
            'conditions': 'is_going_to_stateWorkA'
        },
        {
            'trigger': 'advance',
            'source': 'stateWork',
            'dest': 'stateWorkB',
            'conditions': 'is_going_to_stateWorkB'
        },
        {
            'trigger': 'advance',
            'source': 'stateWork',
            'dest': 'stateWorkC',
            'conditions': 'is_going_to_stateWorkC'
        },
        {
            'trigger': 'advance',
            'source': 'stateWork',
            'dest': 'stateWorkD',
            'conditions': 'is_going_to_stateWorkD'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'stateChat',
            'conditions': 'is_going_to_stateChat'
        },
        {
            'trigger': 'advance',
            'source': 'stateChat',
            'dest': 'stateChat1',
            'conditions': 'is_going_to_stateChat1'
        },
        {
            'trigger': 'advance',
            'source': 'stateChat1',
            'dest': 'stateChat2',
            'conditions': 'is_going_to_stateChat2'
        },
        {
            'trigger': 'advance',
            'source': 'stateChat2',
            'dest': 'stateChat3',
            'conditions': 'is_going_to_stateChat3'
        },
        {
            'trigger': 'advance',
            'source': 'stateChat2',
            'dest': 'stateChat4',
            'conditions': 'is_going_to_stateChat4'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'stateJoke',
            'conditions': 'is_going_to_stateJoke'
        },
        {
            'trigger': 'advance',
            'source': 'stateJoke',
            'dest': 'stateJokeNormal',
            'conditions': 'is_going_to_stateJokeNormal'
        },
        {
            'trigger': 'advance',
            'source': 'stateJoke',
            'dest': 'stateJokeTurbo',
            'conditions': 'is_going_to_stateJokeTurbo'
        },
        {
            'trigger': 'go_back',
            'source': [
                'stateHistory',
                'state1','state2',
                'state3','state4',
                'state5','state6',
                'state7','state8',
                'state9','state10',
                'state11','state12',
                'state13','state14',
                'state15','state16',
                'state17','state18',
                'state19','state20',
                'state21','state22',
                'state23','state24',
                'state25','state26',
                'state27','state28',
                'state29','state30',
                'state31','state32',
                'state33','state34',
                'state35','state36',
                'state37','state38',
                'state39','state40',
                'state41','state42',
                'stateLoveA','stateLoveB',
                'stateLoveC','stateLoveD',
                'stateLoveE',
                'statePersonalityA','statePersonalityB',
                'statePersonalityC','statePersonalityD',
                'stateWorkA','stateWorkB',
                'stateWorkC','stateWorkD',
                'stateChat3','stateChat4',
                'stateJokeNormal','stateJokeTurbo'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()

