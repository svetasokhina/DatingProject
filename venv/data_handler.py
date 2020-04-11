from flask import Flask, render_template, request, redirect, jsonify
import random
import json
import pandas as pd

# TODO: DELETE THIS DATA STRUCTURE -> save the data in external DB
columns = ['user_id', 'profile_1', 'profile_2', 'profile_3', 'profile_4', 'profile_5', 'profile_6',
           'profile_7', 'profile_8', 'profile_9', 'profile_10']
experiment_data = pd.DataFrame(columns=columns)

def create_new_row(user_id):
    new_row = {'user_id': user_id, 'profile_1': 0, 'profile_2': 0, 'profile_3': 0, 'profile_4': 0, 'profile_5': 0,
               'profile_6': 0, 'profile_7': 0, 'profile_8': 0, 'profile_9': 0, 'profile_10': 0}

    experiment_data = experiment_data.append(pd.DataFrame(new_row, columns=columns, igonre_index=True))

def test_print():
    print(experiment_data.head)