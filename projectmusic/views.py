import json
from flask import request, Response
from projectmusic import app,db
from projectmusic.utils import ModelFactory
from projectmusic.utils import UpdateFactory

@app.route('/<audioFIleType>',methods=['GET'])
@app.route('/<audioFIleType>/<audioFileID>',methods=['GET'])
def get_music(audioFIleType,audioFileID = None):
    if not audioFileID:
        res = ''
        model = ModelFactory().get_model(audioFIleType)
        instances = model.query.all()
        for instance in instances:
            res += instance.get_data() + '\n'
        return Response(status=200)
    else:
        model = ModelFactory().get_model(audioFIleType)
        instance = model.query.get(audioFileID)
        return Response(status=200)

@app.route('/',methods=['POST'])
def post_music():
    if request.data:
        data = json.loads(request.data)
        audioFIleType = data['audioFIleType']
        data = data['audioFileMetaData']
        # place = data['place']
        model = ModelFactory().get_model(audioFIleType,**data)
        db.session.add(model)
        db.session.commit()
        return Response(status=200)
    else:
        return Response(status=400)

@app.route('/<audioFIleType>/<audioFileID>',methods=['PUT'])
def put_music(audioFIleType,audioFileID):
    data = json.loads(request.data)
    print(data)
    model = ModelFactory().get_model(audioFIleType)
    update = UpdateFactory().get_object(audioFIleType)
    instance = model.query.get(audioFileID)
    if instance:
        update.update(instance,data)
        db.session.commit()
        return Response(status=200)
    return Response(status=400)

@app.route('/<audioFIleType>/<audioFileID>',methods=['DELETE'])
def delete_music(audioFIleType,audioFileID):
    try:
        model = ModelFactory().get_model(audioFIleType)
        model.query.filter_by(id = audioFileID).delete()
        db.session.commit()
        return Response(status=200)
    except:
        return Response(status=400)