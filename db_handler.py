import app
import Tables
import json


def create_user_init_params(device, text, user_EG_num):
    submit = Tables.UsersTable(device, text, user_EG_num)
    app.db.session.add(submit)
    app.db.session.commit()
    print('new row was added with id:', submit.user_id)
    return submit.user_id


def start_experiment(user_id, user_gender_choice):
    # TODO: choose which EG
    # app.db.session.update(Tables.UsersTable).where(Tables.UsersTable.user_id == user_id). \
    #     values(chosen_gender=user_gender_choice)

    app.db.session.query(Tables.UsersTable).filter(Tables.UsersTable.user_id == int(user_id)).update(
        {Tables.UsersTable.chosen_gender: user_gender_choice})
    app.db.session.commit()

    print('user {}: gender choice is: {} '.format(user_id, user_gender_choice))


def check_counter():
    group1_counter = Tables.BalancingTable.query.filter(row_id=1).group1
    group2_counter = Tables.BalancingTable.query.filter(row_id=1).group2
    group3_counter = Tables.BalancingTable.query.filter(row_id=1).group3
    group4_counter = Tables.BalancingTable.query.filter(row_id=1).group4

    return group1_counter, group2_counter, group3_counter, group4_counter


# def start_experiment(gender_choice, device):
#     submit = Tables.UsersTable(gender_choice, device)
#     app.db.session.add(submit)
#     app.db.session.commit()
#     print('new row was added with id:', submit.user_id)
#     return submit.user_id


def insert_profile_score(user_id, profile_idx, profile_id, score, response_time):
    cell_data = {
        'profile_id:': profile_id,
        'score': score,
        'response_time': response_time
    }

    column_name = int(profile_idx)

    jsoned = json.dumps(cell_data)
    sql_command = "UPDATE UsersTable SET profile{}==:s2 WHERE user_id==:s3;".format(column_name)
    app.db.session.execute(sql_command, {'s2': jsoned, 's3': user_id})
    app.db.session.commit()


def insert_questions_answers(data):
    user_id = data['user_id']
    user_row = Tables.UsersTable.query.filter_by(user_id=user_id).first()
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

    app.db.session.commit()

    print('Questions for user: ', user_id, ' were insert to the DB')


def get_count_EG():
    answer = app.db.session.query(
        Tables.UsersTable.user_EG_num,
        app.func.count()).filter(Tables.UsersTable.done == 1).group_by(Tables.UsersTable.user_EG_num).all()

    EG_status = {}
    for pair in answer:
        EG_status[pair[0]] = pair[1]

    return EG_status


def get_device(user_id):
    result = app.db.session.query(Tables.UsersTable.device).filter_by(user_id=user_id).first()
    if result is None:
        print('ID {} doesnt exist'.format(user_id))
        return ''
    else:
        desired_device = ''
        for res in result:
            desired_device = res
        return desired_device


def insert_trans_code(user_id, trans_code):
    # res = app.db.session.query(Tables.UsersTable.trans_code).filter_by(user_id=user_id).first()
    # if res is None:
    answer = app.db.session.query(Tables.UsersTable).filter(Tables.UsersTable.user_id == int(user_id)).update(
        {Tables.UsersTable.trans_code: trans_code})
    app.db.session.commit()

def insert_final_code (user_id, final_code):
    app.db.session.query(Tables.UsersTable).filter(Tables.UsersTable.user_id == int(user_id)).update(
        {Tables.UsersTable.final_code: final_code})
    app.db.session.commit()


def get_trans_code(user_id, trans_code):
    result = app.db.session.query(Tables.UsersTable.trans_code).filter_by(user_id=user_id).first()

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