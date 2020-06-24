from flask import Blueprint, request
import uuid

from googletrans import Translator

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
