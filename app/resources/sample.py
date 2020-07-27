from datetime import timedelta

from flask_restx import Namespace, Resource, fields

from models.sample_model import Sample, SampleSchema

api = Namespace('sample', description='Manage Sample')

sample_schema = SampleSchema()
samples_schema = SampleSchema(many=True)

@api.route('')
class SampleList(Resource):
    @api.doc('list_Samples')
    def get(self):
        '''List all samples'''
        return {'message': 'Welcome to Flask-restx boilerplate.'}

    @api.doc('Post_Samples')
    def post(self):
        pass

@api.route('/<int:id>')
@api.param('id', 'The Sample identifier')
class SuspendSample(Resource):
    @api.doc('Get_Single_Sample')
    def get(self, id):
        '''Get Sample'''
        pass

    @api.doc('Update_Sample')
    def put(self, id):
        '''Update Sample'''
        pass

    @api.doc('delete_Sample')
    def delete(self, id):
        '''Delete Sample'''
        pass
