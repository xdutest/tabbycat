# Note: Needs to be in this directory for the proper asgi import
import logging
import sys

import asgi
import uvicorn


# Setup logging
root = logging.getLogger()
root.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)
root.info('TC_DEPLOY: Initialising uvicorn')

# Start Uvicorn
uvicorn.run(asgi.application, log_level="info", proxy_headers=True)
