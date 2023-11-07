from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from servicio import MovieService

app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"
service = MovieService()

@app.get("/", tags=["Home"])
def message():
    return HTMLResponse(content="<h1>¡Hola Mundo!</h1>", status_code=200)

@app.get('/movies', tags=["Movies"])
def get_movies():
    return service.get_movies()

@app.get('/movies/{id}', tags=["Movies"])
def get_movie(id: int):
    movie = service.get_movie_by_id(id)
    if movie is not None:
        return movie
    return {'Error': 'No se encontró la película'}

@app.post('/movies/', tags=["Movies"])
def get_movies_by_category(category: str, year: int):
    return service.get_movies_by_category(category)

@app.post('/movies/', tags=["Movies"])
def create_movie(id: int= Body(...), title: str= Body(...), overview: str= Body(...), 
                 year: str= Body(...), rating: float= Body(...), category: str= Body(...)):
    service.add_movie(id, title, overview, year, rating, category)
    return service.get_movies()