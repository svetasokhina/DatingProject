import json
import random
import string

import pandas as pd
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
from sqlalchemy import func
import db_handler

app = Flask(__name__)

engine = app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataBase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# print('tables were created')


profiles_man = [120, 130, 140, 110, 160, 182, 171, 150, 1112, 1121, 1101, 192]
profiles_woman = [210, 220, 230, 240, 250, 260, 271, 282, 292, 2101, 2111, 2122]
user_choice = 1

profiles_man_no_text = [110, 120, 130, 140, 150, 160, 170, 180, 190, 1100, 1110, 1120]
profiles_woman_no_text = [210, 220, 230, 240, 250, 260, 270, 280, 290, 2100, 2110, 2120]


# creating man vector of profiles with text
def profiles_man_text():
    profiles_man_proper = [111, 121, 131, 141, 151, 161, 171, 181, 191, 1101, 1111, 1121]
    profiles_man_corrupt = [112, 122, 132, 142, 152, 162, 172, 182, 192, 1102, 1112, 1122]
    profiles_man_text = []
    for num in range(12):
        prob = random.uniform(0, 1)
        if prob > 0.5:
            profiles_man_text.insert(num, profiles_man_proper[num])
        else:
            profiles_man_text.insert(num, profiles_man_corrupt[num])

    return profiles_man_text


# print(profiles_man_text())
profiles_woman_proper = [211, 221, 231, 241, 251, 261, 271, 281, 291, 2101, 2111, 2121]
profiles_woman_corrupt = [212, 222, 232, 242, 252, 262, 272, 282, 292, 2102, 2112, 2122]


# creating woman vector of profiles with text
def profiles_woman_text():
    profiles_woman_text = []
    for num in range(12):
        prob = random.uniform(0, 1)
        if prob > 0.5:
            profiles_woman_text.insert(num, profiles_woman_proper[num])
        else:
            profiles_woman_text.insert(num, profiles_woman_corrupt[num])

    return profiles_woman_text


# print(profiles_woman_text())


@app.route('/')
def index():
    # db_handler.add_row_to_balancingTable()

    return render_template('welcome.html')


def randomString(stringLength=6):
    """Generate a random string of fixed length """
    letters = string.ascii_letters

    return ''.join(random.choice(letters) for i in range(stringLength))


def uniqueString(id):
    id = "" + id
    rand_string = randomString(6)
    res = rand_string + id
    return res


@app.route("/check_if_valid", methods=['GET', 'POST'])
def check_if_valid():
    data = request.get_json()
    EGroups = [1, 2, 3, 4]
    EG_status = db_handler.get_count_EG()

    for EG in EG_status.keys():
        if EG_status[EG] >= 30:
            EGroups.remove(EG)

    chosen_EG = random.choice(EGroups)
    if chosen_EG == 1 or chosen_EG == 3:
        text = 1
    else:
        text = 0
    print('the chosen EG is:', chosen_EG)
    print('if text:', text)

    if chosen_EG == 3 or chosen_EG == 4:
        random_device = 'Mobile'
    else:
        random_device = 'PC'

    validity = 'False'
    if data['user_device'] == random_device:
        validity = 'True'

    # creating the table with user_id
    user_id = db_handler.create_user_init_params(random_device, text, chosen_EG)
    if validity == 'False':
        trans_code = uniqueString(str(user_id))
    else:
        trans_code = '0'

    db_handler.insert_trans_code(user_id, trans_code)

    print('user_device: {} - chosen_device: {} --> validity: {}'.format(data['user_device'], random_device, validity))
    return jsonify(valid=validity, user_id=user_id, device=data['user_device'], trans_code=trans_code)


@app.route("/check_if_valid_after", methods=['GET', 'POST'])
def check_if_valid_after():
    data = request.get_json()
    trans_code = data['user_code']
    user_id = trans_code[6:]
    desired_device = db_handler.get_device(user_id)

    if desired_device:
        trans_code_match = db_handler.get_trans_code(user_id, trans_code)
        print('the desired device is:', desired_device)
        print('data user_device is:', data['user_device'])
        validity = 'False'
        if data['user_device'] == desired_device:
            validity = 'True'
            print('validity:', validity)
    else:
        validity = 'False'
    return jsonify(valid=validity, user_id=user_id, device=desired_device, trans_code=trans_code_match)


@app.route('/open_instructions')
def open_instructions():
    param = request.args.get('param')  # extract the parameters transfered via the url
    data = json.loads(param)
    print(data)
    return render_template('instructions.html', data=data)


@app.route('/random_Mob')
def open_random_Mob():
    param = request.args.get('param')  # extract the parameters transfered via the url
    data = json.loads(param)
    return render_template('random_Mob.html', data=data)


@app.route('/random_PC')
def open_random_PC():
    param = request.args.get('param')  # extract the parameters transfered via the url
    data = json.loads(param)
    return render_template('random_PC.html', data=data)


@app.route('/open_agreement')
def open_agreement():
    param = request.args.get('param')  # extract the parameters transfered via the url
    data = json.loads(param)
    return render_template('agreement.html', data=data)


@app.route('/open_intro')
def open_intro():
    param = request.args.get('param')  # extract the parameters transfered via the url
    data = json.loads(param)
    return render_template('introduction.html', data=data)


# here we just creating the profile list for the user
@app.route("/profiles", methods=['GET', 'POST'])
def start_experiment():
    data = request.get_json()
    print('user_choice: {} \tuser_device: {}'.format(data['user_choice'], data['user_device']))
    user_id = data['user_id']
    if data:
        user_choice = data['user_choice']
        selected_profiles = []
        if user_choice == '1':  # men
            selected_profiles = profiles_man
        if user_choice == '2':  # women
            selected_profiles = profiles_woman
        if user_choice == '3':  # both
            combined_list = profiles_man + profiles_woman
            selected_profiles = random.sample(combined_list, 12)

        random.shuffle(selected_profiles)
        print('the selected profiles is: {}'.format(selected_profiles))

        db_handler.start_experiment(user_id, user_choice)

    return jsonify(mylist=selected_profiles, pointer=0, id=user_id)


# every profile page -> submit button will send a post request to this route
@app.route("/save_data", methods=['GET', 'POST'])
def save_data():
    data = request.get_json()
    user_id = data['user_id']
    profile_idx = data['profile_idx']
    profile_id = data['profile']
    score = data['score']
    response_time = data['response_time']
    db_handler.insert_profile_score(int(user_id), profile_idx, profile_id, score, response_time)
    return jsonify(data=data)


@app.route("/profiles/<profile_id>", methods=['GET', 'POST'])
def profile(profile_id):
    params = request.args.get('param')  # extract the parameters trasfered via the url
    json_params = json.loads(params)
    # increase the pointer for the next page
    json_params['pointer'] = json_params['pointer'] + 1
    if json_params['pointer'] == 13:
        return render_template('questions.html', myData=json_params)
    return render_template('profile_{}.html'.format(profile_id), myData=json_params)


@app.route("/save_questions", methods=['GET', 'POST'])
def save_questions():
    data = request.get_json()
    db_handler.insert_questions_answers(data)
    return jsonify(data=data['user_id'])


@app.route("/end_of_experiment", methods=['GET', 'POST'])
def end_of_experiment():
    params = request.args.get('param')
    json_params = json.loads(params)
    user_id = json_params['data']
    final_code = uniqueString(str(user_id))
    db_handler.insert_final_code(user_id, final_code)
    return render_template('ending_page.html', myData=final_code)


@app.route('/open_enter_code')
def open_enter_code():
    # param = request.args.get('param')  # extract the parameters transfered via the url
    # data = json.loads(param)
    return render_template('enter_code.html')


if __name__ == '__main__':
    app.run(debug=True)
