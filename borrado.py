from src.cancion import Cancion
from src.interprete import Interprete
from src.album import Album, Medio
from src.declarative_base import Session, engine, Base

if __name__ == '__main__':
  session = Session()
  cancion2 = session.query(Cancion).get(2)
  session.delete(cancion2)
  session.commit()
  session.close()