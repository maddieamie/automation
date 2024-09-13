# import pytest
# import os
# import shutil
# import lab.scripts.automate as automate
#
#
# def test_make_folder():
#     """Test folder creation."""
#     folder_name = "blah"
#     automate.make_folder(folder_name)
#     assert os.path.exists(f"../assets/user-docs/{folder_name}")
#
#
# def test_del_folder():
#     """Test folder deletion."""
#     folder_name = "blah"
#     automate.del_folder(folder_name)
#     assert not os.path.exists(f"../assets/user-docs/{folder_name}")
#
#
# def test_create_user():
#     """Test user creation."""
#     user_name = "Tucker"
#     automate.create_user(user_name)
#     assert os.path.exists(f"../assets/user-docs/{user_name}")
#
#
# def test_del_user():
#     """Test user deletion."""
#     user_name = "test_user"
#     automate.del_user(user_name)
#     assert not os.path.exists(f"../assets/user-docs/{user_name}")
#
#
# def test_sort_things():
#     """Test sorting files into logs and mail."""
#     folder_name = "user1"
#     automate.sort_things(folder_name)
#     assert os.path.exists(f"{folder_name}/logs")
#     assert os.path.exists(f"{folder_name}/mail")
#
#
# def test_count_things():
#     """Test counting specific file types in a folder."""
#     folder_name = "user2"
#     automate.count_things(folder_name, '.log.txt')
#
#
# def test_parse_log():
#     """Test parsing log files and extracting errors/warnings."""
#     automate.parse_log('lab/assets/user-docs/test_user/log3.log.txt')
#     assert os.path.exists('extra_logs/errors.log.txt')
#     assert os.path.exists('extra_logs/warnings.log.txt')
#
