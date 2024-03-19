import flask
from flask import jsonify
from . import db_session
from .Jobs import Jobs


blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')
jobs_fields = ('id', 'job', 'work_size', 'collaborators',
               'start_date', 'end_date', 'is_finished', 'team_leader')


@blueprint.route('/api/jobs/<int:job_id>')
def get_job(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify({'job': jobs.to_dict(only=jobs_fields)})


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {'jobs': [item.to_dict(only=jobs_fields) for item in jobs]})
