from flask import Flask, render_template, request, send_file, redirect
from scrapper import search_books
from file import save_to_csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    page = int(request.args.get('page', 1))

    books = search_books(keyword, page)
    
    return render_template('search.html', 
                           keyword=keyword, 
                           books=books, 
                           page=page) 

@app.route("/file")
def file():
    keyword = request.args.get("keyword")
    if not keyword: return redirect("/")
    
    all_books = []
    for i in range(1, 11): 
        books = search_books(keyword, i)
        if not books: break 
        all_books.extend(books)
    
    save_to_csv(all_books)
    return send_file("./downloads.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)