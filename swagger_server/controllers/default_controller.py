# import connexion
# import six
#
# from swagger_server.models.student import Student  # noqa: E501
# from swagger_server import util
# from swagger_server.service.student_service import *
#
# def add_student(body=None):  # noqa: E501
#     """Add a new student
#
#     Adds an item to the system # noqa: E501
#
#     :param body: Student item to add
#     :type body: dict | bytes
#
#     :rtype: str
#     """
#     if connexion.request.is_json:
#         body = Student.from_dict(connexion.request.get_json())  # noqa: E501
#         return add(body)
#     return 'do some magic!'
#
#
# def delete_student(student_id):  # noqa: E501
#     """gets student
#
#     delete a single student  # noqa: E501
#
#     :param student_id: the uid
#     :type student_id:
#
#     :rtype: object
#     """
#     # return 'do some magic!'
#     return delete(student_id)
#
# def get_student_by_id(student_id):  # noqa: E501
#     """gets student
#
#     Returns a single student # noqa: E501
#
#     :param student_id: the uid
#     :type student_id:
#
#     :rtype: Student
#     """
#     # return 'do some magic!'
#     return get_by_id(student_id)

import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util
from swagger_server.service.student_service import *

def add_student(body=None):  # noqa: E501
    """Add a new student

    Adds an item to the system # noqa: E501

    :param body: Student item to add
    :type body: dict | bytes

    :rtype: str
    """
    if not connexion.request.is_json:
        return "Invalid request format. Expected JSON.", 400

    body = Student.from_dict(connexion.request.get_json())  # Convert request JSON to Student object
    result = add(body)  # Call add() function in student_service.py

    if isinstance(result, tuple):  # Check if it's returning ("already exists", 409)
        return result

    return {"student_id": result}, 201  # Return MongoDB ObjectId inside a JSON response


def delete_student(student_id):  # noqa: E501
    """Delete a student

    Deletes a single student  # noqa: E501

    :param student_id: The UID of the student
    :type student_id: str

    :rtype: object
    """
    result = delete(student_id)

    if result == "not found":
        return "Student not found", 404

    return {"deleted_student_id": student_id}, 200


def get_student_by_id(student_id):  # noqa: E501
    """Get a student by ID

    Returns a single student # noqa: E501

    :param student_id: The UID of the student
    :type student_id: str

    :rtype: Student
    """
    student = get_by_id(student_id)

    if isinstance(student, tuple):  # If it's returning ("not found", 404)
        return student

    return student, 200  # Return student data with status 200
