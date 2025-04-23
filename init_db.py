# init_db.py
from database import Base, engine
import models  # make sure models are imported so Base knows about them

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
