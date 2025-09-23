import subprocess
import threading
import time
from dotenv import load_dotenv

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

load_dotenv()

def run_backend():
    try:
        logger.info("Starting Backend Server...")
        subprocess.run(["uvicorn", "app.backend.api:app", "--host", "127.0.0.1","--port", "9999"], check=True)

    except CustomException as e:
        logger.error(f"Problem with backend service")
        raise CustomException("Failed to start backend service", error_detail=e)
    

def run_frontend():
    try:
        logger.info("Starting Frontend Server...")
        subprocess.run(["streamlit", "run", "app/frontend/ui.py"], check=True)

    except CustomException as e:
        logger.error(f"Problem with frontend service")
        raise CustomException("Failed to start frontend service", error_detail=e)
    
if __name__ == "__main__":
    try:
        threading.Thread(target=run_backend).start()
        time.sleep(2)  # Wait for backend to start

        run_frontend()
    
    except Exception as e:
        logger.error(f"Error occurred while starting services: {e}")
        raise CustomException("Failed to start services", error_detail=e)