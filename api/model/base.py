import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
MODEL_PATH =BASE_DIR +"/"+ "model.joblib"
LOCATION_ENCODER_PATH  = BASE_DIR +"/"+ "location_encoder.joblib"