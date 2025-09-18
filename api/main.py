from fastapi import FastAPI
from dotenv import load_dotenv
from routers.journal_router import router as journal_router
import logging

load_dotenv()

# TODO: Setup basic console logging
# Hint: Use logging.basicConfig() with level=logging.INFO
# Steps:
# 1. Configure logging with basicConfig()
# 2. Set level to logging.INFO
logging.basicConfig(level=logging.INFO) # sets level for root logger (default is WARNING & higher), if set to DEBUG it will show DEBUG and INFO logs form entry_service.py in the console 

# 3. Add console handler
app_logger = logging.getLogger("main")
app_logger.setLevel(level=logging.DEBUG) # This overrides the root logger's level for app_logger

app_console_handler = logging.StreamHandler()
app_console_handler.setLevel(logging.INFO) # It receives DEBUG and higher order logs from app_logger but filters Only INFO logs
app_console_handler.setFormatter(logging.Formatter('%(asctime)s || %(name)s || %(levelname)s || %(message)s'))
app_logger.addHandler(app_console_handler)
app_logger.propagate = False

# 4. Test by adding a log message when the app starts
app_logger.info("Journal App is setting up..")
app = FastAPI(title="Journal API", description="A simple journal API for tracking daily work, struggles, and intentions")
app_logger.debug("FastAPI App initiated.. Fetching all endpoints")
app.include_router(journal_router)
app_logger.info("Journal App is up and running")
app_logger.warning("Resets each time file is saved")