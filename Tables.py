from app import db


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
