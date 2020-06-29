from flask import Blueprint, request
import uuid

from googletrans import Translator

from api.yolo import predict_image

api = Blueprint("utils", __name__)

translator = Translator()


@api.route('convert/<src>/<dest>', methods=['POST'])
def convert(src, dest):
    data = request.data
    data = data.decode().splitlines()
    name = data[0::2]
    content = data[1::2]
    list = []
    l = len(name)
    for i in range(l):
        id = uuid.uuid1()
        n = name[i]
        c = content[i]
        item = {"id": id, "name": n, "content": c, "lang": src}
        list.append(item)
        id = uuid.uuid1()
        c = translator.translate(content[i], src=src, dest=dest).text
        item = {"id": id, "name": n, "content": c, "lang": dest}
        list.append(item)
    return {"message": list}


"""
    username_pass_incorrect
    Username or password incorrect!
    user_deactivated
    Your account is deactivated, please contact with admin to activate your account!
    user_blocked
    Your account has been blocked, please contact with admin to unlock your account
    login_success
    Logged in successfully!
    logout_success
    Logout successfully!
    username_existed
    The user name has existed!
    not_found_group
    Not found the user group
    create_user_success
    Create user successfully!
    not_found_user
    Not found user!
    update_user_success
    Update user successfully!
    current_pass_incorrect
    Current password incorrect!
    change_pass_success
    Change password successfully!
    new_pass_invalid
    Your password is too weak, Please choose another password.
    reset_pass_success
    Reset password successfully!
    delete_user_success
    Delete user successfully!
    deactivate_user_success
    Deactivate user successfully!
    activate_user_success
    Activate user successfully!
    group_name_existed
    The group name has existed!
    create_group_success
    Create the group successfully!
    update_group_success
    Update group successfully!
    duplicate_group_success
    Duplicate group successfully!
    delete_group_success
    Delete group successfully!
    update_policy_success
    Update security policy successfully!
    can_not_deactivate_user
    Cannot deactivate this user!
    can_not_delete_user
    Cannot delete this user!
    can_not_deactivate_per
    Cannot deactivate this permission!
    change_status_per_success
    Status change successful!
    cannot_delete_group
    Cannot delete this group!
"""

SECRET_KEY = 'ABDCA23114'
dict = {i: chr(i + 48) for i in range(10)}
dict2 = {i + 10: chr(i + 65) for i in range(26)}
mapping_number = {**dict, **dict2}
mapping_size = 36
output_size = 16


def adjust(value):
    if value < 0:
        n = -(value + 1) // mapping_size + 1
        value += n * mapping_size
    else:
        value %= mapping_size
    return value


def encode(str):
    l = len(str)
    a = [l, 0, 0, 0, 0]
    k = 1
    i = 0
    for ch in str:
        ch = ord(ch)
        a[1] += ch
        a[2] += ch * k
        a[3] += ch * (i + 1)
        a[4] += ch * k * (i + 2)
        k = -k
        i += 1

    c = [0] * output_size
    d = ((a[0] + 16) * (a[1] + 8) * (a[2] + 4) * (a[3] + 2) * (a[4] + 1)) + a[4] + 1
    c[0] = adjust(d)
    n = 0
    k = 11
    for i in range(1, output_size):
        d = c[i - 1] * (a[n] + k) + k * i + 1
        c[i] = adjust(d)
        n += 1
        if n == 5:
            n = 0
        k += 1

    str = ''
    for i in range(output_size):
        if i % 4 == 0 and i != 0:
            str += '-'
        str += mapping_number[c[i]]
    return str


@api.route('make_key/<src>', methods=['POST'])
def make_key(src):
    src += SECRET_KEY
    return {"encode": encode(src)}


# import base64
# from PIL import Image
# import io
#
# import numpy as np
# from keras.models import load_model
#
# model = load_model('api/model.h5')
#
#
# @api.route('predict_number', methods=['POST'])
# def predict_number():
#     # data = request.get_json()
#     # data = data.get("content", None)
#     # image_base64 = base64.decodebytes(data.encode())
#     image = Image.open(io.BytesIO(request.data)).convert('L').resize((28, 28))
#     # image.show()
#     image = np.array(image) / 255
#     my_predict = np.array([image])
#     classes = model.predict_classes(my_predict)
#     return {"predict": int(classes[0])}

# @api.route('yolo', methods=['POST'])
# def predict():
#     data = request.get_json()
#     data = data.get("image", None)
#     data = predict_image(data)
#     return {"predict": data.decode()}
