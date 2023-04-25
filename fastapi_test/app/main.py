# file: src/main.py
# =============================================

from app.app_setup.app_config import create_app, uvi_run
# =============================================

# Call the create_app as a global function
# to get the FastAPI app instance
app = create_app()
# =============================================

def main():
    # Run the FastAPI app using uvicorn
    uvi_run()

# If the script is being executed as the main program, call the main function
if __name__ == "__main__":
    main()
# =============================================
