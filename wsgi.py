from app import create_app  # Ensure the function name matches

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)