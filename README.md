<h1 align="center">E-COMMERCE</h1>

<p align="center">
  RESTful API for an e-commerce system
</p>

<p align="center">
  <a href="#architecture">ARCHITECTURE</a> &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#project">PROJECT</a> &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#technologies">TECHNOLOGIES</a> &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#run">RUN</a> &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#license">LICENSE</a>
</p>

<p align="center">
  <img alt="license" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</p>

## 🏗️ <a id="architecture"></a> ARCHITECTURE

```mermaid
graph TB
    Client[Client/HTTP Requests]

    subgraph API["Flask Application"]
        CORS[CORS Middleware]
        LoginManager[Flask-Login / LoginManager]
        Routes[Routes<br/>login, logout, products, cart]
        Models[Models<br/>User, Product, CartItem]
    end

    subgraph Auth["Authentication"]
        LoginRoute[POST /login]
        LogoutRoute[POST /logout]
    end

    subgraph Products["Products API"]
        AddProduct[POST /api/products/add]
        DeleteProduct[DELETE /api/products/delete/:id]
        GetProduct[GET /api/products/:id]
        UpdateProduct[PUT /api/products/update/:id]
        ListProducts[GET /api/products]
    end

    subgraph Cart["Cart API"]
        AddCart[POST /api/cart/add/:id]
        RemoveCart[DELETE /api/cart/remove/:id]
        ViewCart[GET /api/cart]
        Checkout[POST /api/cart/checkout]
    end

    subgraph Database["Database"]
        DB[(SQLite / e-commerce.db)]
    end

    Client --> CORS
    CORS --> LoginManager
    LoginManager --> Routes
    Routes --> Auth
    Routes --> Products
    Routes --> Cart
    Auth --> Models
    Products --> Models
    Cart --> Models
    Models --> DB

    style API fill:#2B2D42,color:#fff
    style Auth fill:#EF233C,color:#fff
    style Products fill:#2196F3,color:#fff
    style Cart fill:#FF9800,color:#fff
    style Database fill:#003B57,color:#fff
```

## 💻 <a id="project"></a> PROJECT

"E-COMMERCE" is a RESTful API for managing products, shopping cart, and user authentication in an e-commerce platform.

## 🌐 <a id="technologies"></a> TECHNOLOGIES

This project was developed using the following technologies:

- Flask
- Python
- SQLite
- Git and Github

## ⚙️ <a id="run"></a> RUN

To install the required dependencies, run the following command:

```sh
pip3 install -r requirements.txt
```

## ⚖️ <a id="license"></a> LICENSE

This project is licensed under the MIT License.

---

Made with ♥ by Miguel
