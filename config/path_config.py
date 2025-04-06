import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print(PROJECT_ROOT)

CONFIG_PATH = os.path.join(PROJECT_ROOT, "config", "config.yaml")

RAW_DIR = os.path.join(PROJECT_ROOT, "artifacts", "raw")
RAW_FILE_PATH = os.path.join(RAW_DIR, "raw.csv")
TRAIN_FILE_PATH = os.path.join(RAW_DIR, "train.csv")
TEST_FILE_PATH = os.path.join(RAW_DIR, "test.csv")
print(PROJECT_ROOT)


################## DATA PROCESSING ##########################
PROCESSED_DIR=PROJECT_ROOT+"/artifacts/processed"
print(PROCESSED_DIR)
PROCESSED_TRAIN_DATA_PATH=os.path.join(PROCESSED_DIR,"processed_train.csv")
PROCESSED_TEST_DATA_PATH=os.path.join(PROCESSED_DIR,"processed_test.csv")


###################### MODEL TRAINING ###########################
MODEL_OUTPUT_PATH=PROJECT_ROOT+'/artifacts/model/lgbm_model.pkl'
