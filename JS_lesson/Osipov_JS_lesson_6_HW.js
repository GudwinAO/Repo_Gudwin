/* Урок 6.
Задание  1. Продолжаем реализовывать модуль корзины:
a. Добавлять в объект корзины выбранные товары по клику на кнопке «Купить» без
перезагрузки страницы;
b. Привязать к событию покупки товара пересчет корзины и обновление ее внешнего
вида.
*/

const localPlace = document.getElementById('basket');
const localPlaceProduct = document.getElementById('products');

class Product {
    constructor(id, name, color, price, weight, status = 'free') {
        this.id = id;
        this.name = name;
        this.color = color;
        this.price = price;
        this.weight = weight;
        this.status = status;
    }

}

const basket = {
    items: [],

    addToBasket: function (product, y) {
        this.items.push({ ...product, count: y });
    },


    getSumProduct: function () {
        countPrice = 0;
        this.items.forEach(item => countPrice += item.price * item.count);
        return countPrice;
    },

    getCountProduct: function () {
        countProduct = 0;
        this.items.forEach(item => countProduct += item.count);
        return countProduct;
    },

    referenceBasket: function () {
        if (totalCount === 0) {
            localPlace.innerHTML = 'Корзина пуста';
        }
        else {
            localPlace.innerHTML = `Стоимость добавленных вами ${totalCount} товаров составляет ${totalPrice}`
        }
    }
};

const totalPrice = basket.getSumProduct();
const totalCount = basket.getCountProduct();

const showcase = {

    settings: {
        modalImageCloseSrc: 'img/add'
    },

    items: [],

    addToShowcase: function (product) {
        this.items.push({ ...product, count: 1 });
    },

    referenceShowcase: function (x) {
        for (i = 0; i <= x.lenght; i++) {
            localPlaceProduct.innerHTML = ('beforeend',
                `<div id="${this.items.id}" class="prod_item">
                    <div class="item">
                        <div class="name"><h4>${this.items.name}</h4>${this.items.color}
                            <div class="price">Цена:
                                    <span>${this.items.price}</span> руб.
                            </div>
                        </div>
                    </div>
                    <div class="sale">
                        <div data-id="${this.items.id}" class="button">В корзину</div>
                    </div>
                </div>`);

        }

        basket.referenceBasket();
    },
}


localPlaceProduct.addEventListener('click', function (e) {
    if (e.target.className === 'button') {
        const id = Number(e.target.getAttribute('data-id'));
        const choice = showcase.items[id];
        basket.addToBasket(choice);
        basket.referenceBasket();
        ;
    }
});

let product_1 = new Product(123, 'Ручка', 'Черная', 100, 50);
let product_2 = new Product(456, 'Карандаш', 'Коричневый', 50, 30);
let product_3 = new Product(556, 'Стерка', 'Белая', 20, 10);

showcase.addToShowcase(product_1);
showcase.addToShowcase(product_2);
showcase.addToShowcase(product_3);


showcase.referenceShowcase(showcase);
console.log(showcase.items)

