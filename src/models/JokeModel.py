from .entities.Joke import Joke, JokeSchema, db
import uuid

joke_schema =  JokeSchema()
jokes_schema =  JokeSchema(many=True)

class JokeModel():

    @classmethod
    def get_jokes(self):
        try:
            all_jokes = Joke.query.all()
            result = jokes_schema.dump(all_jokes)
            return result
        except Exception as e:
            raise Exception('jokes not founds')


    @classmethod
    def get_joke(self, id):
        try:
            joke = Joke.query.get(id)
            result = Joke.to_JSON(joke)
            return result
        except Exception as e:
            raise Exception('joke with id'+id+' not found')


    @classmethod
    def add_joke(self, joke):
        try:
            id = str(uuid.uuid4())
            joke = Joke(id, joke)
            db.session.add(joke)
            db.session.commit()
            result = Joke.to_JSON(joke)
            return result
        except Exception as e:
            raise Exception(e)

    @classmethod
    def update_joke(self, id, joke_value):
        try:
            joke = Joke.query.get(id)
            joke.joke = joke_value
            db.session.commit()
            result = Joke.to_JSON(joke)
            return result
        except Exception as e:
            raise Exception('joke with id'+id+' not found')


    @classmethod
    def delete_joke(self, id):
        try:
            joke = Joke.query.get(id)
            db.session.delete(joke)
            db.session.commit()
            result = Joke.to_JSON(joke)
            print(result)
            return result
        except Exception as e:
            raise Exception('joke with id'+id+' not found')
