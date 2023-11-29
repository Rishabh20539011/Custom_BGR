# #!/bin/bash

# if [ "$1" = "frontend" ]; then
#   # Start the PM2 process for frontend with error handling and automatic restart
#   cd /path/to/frontend
#   pm2 start npm --name "frontend" -- start --watch --ignore-watch="node_modules"
# elif [ "$1" = "backend" ]; then
#   # Start the PM2 process for backend with error handling and automatic restart
#   cd /path/to/backend
#   pm2 start uvicorn --name "backend" --main "main:app" --host "0.0.0.0" --port 8000 --watch
# else
#   echo "Invalid argument. Use 'frontend' or 'backend'."
#   exit 1
# fi

# # Keep the script running to prevent the container from exiting
# tail -f /dev/null



# #!/bin/bash

# while true; do
#   if [ "$1" = "frontend" ]; then
#     # Start the frontend directly
#     cd /path/to/frontend
#     npm start
#   elif [ "$1" = "backend" ]; then
#     # Start the backend directly
#     cd /path/to/backend
#     uvicorn main:app --host 0.0.0.0 --port 8000
#   else
#     echo "Invalid argument. Use 'frontend' or 'backend'."
#     exit 1
#   fi

#   # Sleep for a short duration before attempting a restart
#   echo "Restarting process in 5 seconds..."
#   sleep 5
# done


