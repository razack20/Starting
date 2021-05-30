from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<title>Book store</title><body style=background-color:powderblue;><h1 style=text-align:center;>Online books store</h1><img src=https://th.bing.com/th/id/Red2631c08bf740fdd5412a1cad534e20?rik=JylEwfAjr3hGcg&riu=http%3a%2f%2fblog.bookswagon.com%2fwp-content%2fuploads%2f2018%2f08%2fengineering-books-online.jpg&ehk=eMsKnDbjS0PX4hqjKtE8v0E8KST%2bPIsSXuveTnr3BwQ%3d&risl=&pid=ImgRaw width=250 height=250>   <img src=https://inteng-storage.s3.amazonaws.com/img/iea/3gG998vaGV/sizes/mecathronics_resize_md.jpg width=250 height=250> <img src= https://image.isu.pub/150430134327-a6c75d39d738afb55d1daa1d1344fb28/jpg/page_1.jpg height=250 width=250>"
    
if __name__ == "__main__":
    app.run(port=8488)

 
