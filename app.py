import json
import random
import string
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
from sqlalchemy import func

# import db_handler

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    debug = True
    engine = app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataBase.db'
else:
    debug = False
    engine = app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgres://gyvmazmozgmftg:b2fea44de215c35346dab1dccb5e01970d5011dc63c4b767c2123e701c36c491@ec2-34-197-212-240.compute-1.amazonaws.com:5432/dbuu6dgo6kqf69'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# ---------  database Tables -------------------------------------
class UsersTable(db.Model):
    __tablename__ = 'UsersTable'
    user_id = db.Column("user_id", db.Integer, primary_key=True, autoincrement=True)
    chosen_gender = db.Column('chosen_gender', db.Integer)
    device = db.Column("device", db.Unicode)
    text = db.Column("text", db.Integer)
    user_EG_num = db.Column('user_EG_num', db.Integer)
    trans_code = db.Column('trans_code', db.Unicode)
    profile1 = db.Column("profile1", db.Unicode)
    profile2 = db.Column("profile2", db.Unicode)
    profile3 = db.Column("profile3", db.Unicode)
    profile4 = db.Column("profile4", db.Unicode)
    profile5 = db.Column("profile5", db.Unicode)
    profile6 = db.Column("profile6", db.Unicode)
    profile7 = db.Column("profile7", db.Unicode)
    profile8 = db.Column("profile8", db.Unicode)
    profile9 = db.Column("profile9", db.Unicode)
    profile10 = db.Column("profile10", db.Unicode)
    profile11 = db.Column("profile11", db.Unicode)
    profile12 = db.Column("profile12", db.Unicode)

    q1 = db.Column("q1", db.Unicode)
    q2 = db.Column("q2", db.Unicode)
    q3 = db.Column("q3", db.Unicode)
    q4 = db.Column("q4", db.Unicode)
    q5 = db.Column("q5", db.Unicode)
    q6 = db.Column("q6", db.Unicode)
    q7 = db.Column("q7", db.Unicode)
    q8 = db.Column("q8", db.Unicode)
    q9 = db.Column("q9", db.Unicode)
    q10 = db.Column("q10", db.Unicode)
    q11 = db.Column("q11", db.Unicode)
    q12 = db.Column("q12", db.Unicode)

    s1 = db.Column("s1", db.Unicode)
    s2 = db.Column("s2", db.Unicode)
    s3 = db.Column("s3", db.Unicode)
    s4 = db.Column("s4", db.Unicode)
    s5 = db.Column("s5", db.Unicode)
    s6 = db.Column("s6", db.Unicode)
    s7 = db.Column("s7", db.Unicode)
    s8 = db.Column("s8", db.Unicode)

    final_code = db.Column("final_code", db.Unicode)
    done = db.Column('done', db.Integer)

    def __init__(self):
        self.device = None
        self.text = None
        self.chosen_gender = None
        self.user_EG_num = None
        self.trans_code = None
        self.profile1 = None
        self.profile2 = None
        self.profile3 = None
        self.profile4 = None
        self.profile5 = None
        self.profile6 = None
        self.profile7 = None
        self.profile8 = None
        self.profile9 = None
        self.profile10 = None
        self.profile11 = None
        self.profile12 = None

        self.q1 = None
        self.q2 = None
        self.q3 = None
        self.q4 = None
        self.q5 = None
        self.q6 = None
        self.q7 = None
        self.q8 = None
        self.q9 = None
        self.q10 = None
        self.q11 = None
        self.q12 = None

        self.s1 = None
        self.s2 = None
        self.s3 = None
        self.s4 = None
        self.s5 = None
        self.s6 = None
        self.s7 = None
        self.s8 = None

        self.final_code = None
        self.done = 0

    def __init__(self, device, text, user_EG_num):
        self.device = device
        self.text = text
        self.user_EG_num = user_EG_num

        self.trans_code = None
        self.profile1 = None
        self.profile2 = None
        self.profile3 = None
        self.profile4 = None
        self.profile5 = None
        self.profile6 = None
        self.profile7 = None
        self.profile8 = None
        self.profile9 = None
        self.profile10 = None
        self.profile11 = None
        self.profile12 = None

        self.q1 = None
        self.q2 = None
        self.q3 = None
        self.q4 = None
        self.q5 = None
        self.q6 = None
        self.q7 = None
        self.q8 = None
        self.q9 = None
        self.q10 = None
        self.q11 = None
        self.q12 = None

        self.s1 = None
        self.s2 = None
        self.s3 = None
        self.s4 = None
        self.s5 = None
        self.s6 = None
        self.s7 = None
        self.s8 = None

        self.final_code = None
        self.done = 0


db.create_all()
print('tables were created')


# ---------  database functions -------------------------------------
def db_create_user_init_params(device, text, user_EG_num):
    submit = UsersTable(device, text, user_EG_num)
    db.session.add(submit)
    db.session.commit()
    print('new row was added with id:', submit.user_id)
    return submit.user_id


def db_start_experiment(user_id, user_gender_choice):
    # TODO: choose which EG
    # app.db.session.update(Tables.UsersTable).where(Tables.UsersTable.user_id == user_id). \
    #     values(chosen_gender=user_gender_choice)

    db.session.query(UsersTable).filter(UsersTable.user_id == int(user_id)).update(
        {UsersTable.chosen_gender: user_gender_choice})
    db.session.commit()

    print('user {}: gender choice is: {} '.format(user_id, user_gender_choice))


def db_insert_profile_score(user_id, profile_idx, profile_id, score, response_time):
    cell_data = {
        'profile_id:': profile_id,
        'score': score,
        'response_time': response_time
    }

    column_name = int(profile_idx)

    jsoned = json.dumps(cell_data)
    sql_command = "UPDATE UsersTable SET profile{}==:s2 WHERE user_id==:s3;".format(column_name)
    db.session.execute(sql_command, {'s2': jsoned, 's3': user_id})
    db.session.commit()


def db_insert_questions_answers(data):
    user_id = data['user_id']
    user_row = UsersTable.query.filter_by(user_id=user_id).first()
    user_row.q1 = data['q1']
    user_row.q2 = data['q2']
    user_row.q3 = data['q3']
    user_row.q4 = data['q4']
    user_row.q5 = data['q5']
    user_row.q6 = data['q6']
    user_row.q7 = data['q7']
    user_row.q8 = data['q8']
    user_row.q9 = data['q9']
    user_row.q10 = data['q10']
    user_row.q11 = data['q11']
    user_row.q12 = data['q12']
    user_row.s1 = data['s1']
    user_row.s2 = data['s2']
    user_row.s3 = data['s3']
    user_row.s4 = data['s4']
    user_row.s5 = data['s5']
    user_row.s6 = data['s6']
    user_row.s7 = data['s7']
    user_row.s8 = data['s8']
    user_row.done = 1

    db.session.commit()

    print('Questions for user: ', user_id, ' were insert to the DB')


def db_get_count_EG():
    answer = db.session.query(
        UsersTable.user_EG_num,
        func.count()).filter(UsersTable.done == 1).group_by(UsersTable.user_EG_num).all()

    EG_status = {}
    for pair in answer:
        EG_status[pair[0]] = pair[1]

    return EG_status


def db_get_device(user_id):
    result = db.session.query(UsersTable.device).filter_by(user_id=user_id).first()
    if result is None:
        print('ID {} doesnt exist'.format(user_id))
        return ''
    else:
        desired_device = ''
        for res in result:
            desired_device = res
        return desired_device


def db_insert_trans_code(user_id, trans_code):
    # res = app.db.session.query(Tables.UsersTable.trans_code).filter_by(user_id=user_id).first()
    # if res is None:
    answer = db.session.query(UsersTable).filter(UsersTable.user_id == int(user_id)).update(
        {UsersTable.trans_code: trans_code})
    db.session.commit()


def db_insert_final_code(user_id, final_code):
    db.session.query(UsersTable).filter(UsersTable.user_id == int(user_id)).update(
        {UsersTable.final_code: final_code})
    db.session.commit()


def db_get_trans_code(user_id, trans_code):
    result = db.session.query(UsersTable.trans_code).filter_by(user_id=user_id).first()

    if result is None:
        print('ID {} doesnt exist'.format(user_id))
        return 'False'
    else:
        temp = ''
        for res in result:
            temp = res

        if temp == trans_code:
            print('trans Code {} exists'.format(trans_code))
            return 'True'
        else:
            print('trans Code {} doesnt exist'.format(trans_code))
            return 'False'


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


# ---------  app routes -------------------------------------
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
    EG_status = db_get_count_EG()

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
    user_id = db_create_user_init_params(random_device, text, chosen_EG)
    if validity == 'False':
        trans_code = uniqueString(str(user_id))
    else:
        trans_code = '0'

    db_insert_trans_code(user_id, trans_code)

    print('user_device: {} - chosen_device: {} --> validity: {}'.format(data['user_device'], random_device, validity))
    return jsonify(valid=validity, user_id=user_id, device=data['user_device'], trans_code=trans_code)


@app.route("/check_if_valid_after", methods=['GET', 'POST'])
def check_if_valid_after():
    data = request.get_json()
    trans_code = data['user_code']
    user_id = trans_code[6:]
    desired_device = db_get_device(user_id)

    if desired_device:
        trans_code_match = db_get_trans_code(user_id, trans_code)
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

        db_start_experiment(user_id, user_choice)

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
    db_insert_profile_score(int(user_id), profile_idx, profile_id, score, response_time)
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
    db_insert_questions_answers(data)
    return jsonify(data=data['user_id'])


@app.route("/end_of_experiment", methods=['GET', 'POST'])
def end_of_experiment():
    params = request.args.get('param')
    json_params = json.loads(params)
    user_id = json_params['data']
    final_code = uniqueString(str(user_id))
    db_insert_final_code(user_id, final_code)
    return render_template('ending_page.html', myData=final_code)


@app.route('/open_enter_code')
def open_enter_code():
    return render_template('enter_code.html')


@app.route('/close_experiment')
def close_experiment():
    return render_template('close_page.html')


if __name__ == '__main__':
    app.run(debug=debug)
