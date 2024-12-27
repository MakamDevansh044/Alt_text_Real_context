from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

    #meta-llama/Llama-3.2-11B-Vision-Instruct
#https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct