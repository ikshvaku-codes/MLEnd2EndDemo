from ccDefault.pipeline.pipeline import Pipeline
from ccDefault.logger import logging
def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        
        
if __name__ == '__main__':
    main()