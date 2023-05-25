from django.shortcuts import render, HttpResponse
from .models import Product, Comment

# Create your views here.
def index(req):
  if req.method == 'GET':
      products = Product.objects.all()[:3]

      comment = Comment.objects.filter(effect__gt = 3, delivery__gt = 3).first()
      if comment == None:
          comment = Comment.objects.first()

      return render(req, 'index.html', { 'products': products, 'comment': comment })

def buyDelivery(req):
   if req.method == 'GET':
        products = Product.objects.all()[:3]

        return render(req, 'buy_n_delivery_page.html', { 'products': products })
   
def surface(req):
    if req.method == 'GET':
        comments = Comment.objects.all()

        products = Product.objects.all()[:3]

        return render(req, 'surface_page.html', {'comments': comments, 'products': products})
    
def product(req, id):
    if req.method == 'GET':
        comment = Comment.objects.filter(effect__gt = 3, delivery__gt = 3).first()
        if comment == None:
            comment = Comment.objects.first()

        product = Product.objects.filter(id=id).first()
        product.price = int(product.price)

        products = Product.objects.all()

        index = None
        if (product.name == 'Касторовое масло'): index = 1
        elif (product.name == 'Белая глина'): index = 2
        elif (product.name == 'Псиллиум'): index = 3

        return render(req, f'product_page{index}.html', {'comment': comment, 'product': product, 'products': products})
    
def return_all_products(req):
    productCount = Product.objects.count()
    
    data = ''
    for i in range(1, productCount + 1):
        product = Product.objects.filter(Product.id == i).first()

        data += str(product.id) + '_' + str(product.title) + '_' + str(product.product_img_src) + '_' + str(product.bg_color)
        data += '&'
       
    data = data[0:len(data) - 1]

    return data

def add_comment(req):
    if req.method=="POST":
        req = req.POST['params'].split('&')
        req_data = {}

        for par in req:
            par_data = par.split('=')
            req_data[f'{par_data[0]}'] = par_data[1]

        product = Product.objects.filter(id=int(req_data['product'])).first()

        comment = Comment(
            title=req_data['text'][:10], 
            text=req_data['text'],
            email=req_data['email'],
            name=req_data['name'],
            effect=int(req_data['effect']),
            delivery=int(req_data['delivery']),
            product=product)

        comment.save()

        return HttpResponse(200)


# @app.route('/get-more-comments', methods=['POST'])
# def get_comments():
#     req = request.data.decode().split('&')

#     comments = db.session.query(Comment).filter(Comment.text.notin_(req)).limit(3).all()

#     res = ''
#     for comment in comments:
#         res += 'name=' + comment.name + '^' + 'text=' + comment.text + '^' + 'product_name=' + comment.product + '^' + 'effect=' + str(comment.effect) + '^' + 'delivery=' + str(comment.delivery)
#         res += '&'

#     res = res[0:len(res)-1]

#     if len(comments) == 0:
#         res = 'comments is`t already exist'


#     return res


# @app.route('/check-promocode', methods=['POST'])
# def check_promocode():
#     req = request.data.decode()
#     promocode = db.session.query(Promocode).filter(Promocode.code == req).first()
    
#     if promocode != None:
#         return str(promocode.discount)

#     else:
#         return 'not found'


# @app.route('/set-product-to-session', methods=['POST'])
# def return_product():
#     req = request.data.decode().split('&')
#     req_data = {}
#     for par in req:
#         par_data = par.split('=')
#         req_data[f'{par_data[0]}'] = par_data[1]

#     product_id = db.session.query(Product).filter(Product.title == req_data['title']).first().id

#     product_data = {
#         'product_id' : product_id,
#         'variable_id' : '',
#         'count' : req_data['count']
#     }

#     if 'capacity' in req_data:
#         variable_id = db.session.query(Variable).filter(Variable.product_id == product_id, Variable.title == req_data['capacity']).first().id

#     else:
#         variable_id = db.session.query(Variable).filter(Variable.product_id == product_id).first().id

#     product_data['variable_id'] = variable_id

#     set_product_to_session(product_data)


#     return 'ok'