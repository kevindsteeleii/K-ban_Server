from flask import Flask, Blueprint, request
from models import CheckList, checklist_schema, checklists_schema

checklists_blueprint = Blueprint(
    'checklists',
    __name__
)

# @checklists_blueprint.route('', methods=['POST'])
# def add_checklist_item():
    