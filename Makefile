app:
	cd neural-net && streamlit run streamlit_app.py

build-linux:
	cd webscraping && GOOS=linux go build -o binaries main.go