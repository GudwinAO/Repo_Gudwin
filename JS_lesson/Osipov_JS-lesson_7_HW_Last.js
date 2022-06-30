/* Урок 7.
1. Реализовать страницу корзины:
a. Добавить возможность не только смотреть состав корзины, но и редактировать его,
обновляя общую стоимость или выводя сообщение «Корзина пуста».
2. На странице корзины:
a. Сделать отдельные блоки «Состав корзины», «Адрес доставки», «Комментарий»;
b. Сделать эти поля сворачиваемыми;
c. Заполнять поля по очереди, то есть давать посмотреть состав корзины, внизу которого
есть кнопка «Далее». Если нажать ее, сворачивается «Состав корзины» и открывается
«Адрес доставки» и так далее.
3. * Убрать границы поля: пересекая их, змейка должна появляться с противоположной стороны.
4. * Для задачи со звездочкой из шестого урока реализовать функционал переключения между
картинками по стрелкам на клавиатуре.
*/

// Блок первичных настроек. Надо перевести в объект settings

const localPlace = document.getElementById('basket');
const localNext = document.getElementById('next')
const localPlaceProduct = document.getElementById('products');
const localDelivery = document.getElementById('delivery');
const localComments = document.getElementById('comments');


const localButtonNext = document.getElementsByClassName('button_next');
const BasketItems = document.getElementsByClassName("prod_item");


// Блок продуктов

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

let product_1 = new Product(123, 'Ручка', 'Черная', 100, 50);
let product_2 = new Product(456, 'Карандаш', 'Коричневый', 50, 30);
let product_3 = new Product(556, 'Стерка', 'Белая', 20, 10);
let product_4 = new Product(589, 'Кисть', 'Серая', 200, 50);
let product_5 = new Product(656, 'Тетрадь', 'Зеленая', 75, 40);

// Блок корзины

const basket = {
    items: [],

    totalPrice: 0,
    totalCount: 0,

    addToBasket: function (product, y) {
        this.items.push({ ...product, count: y });
        this.totalPrice = basket.getSumProduct();
        this.totalCount = basket.getCountProduct();

    },

    getSumProduct: function () {
        let countPrice = 0;
        this.items.forEach(item => countPrice += item.price * item.count);
        return countPrice;
    },

    getCountProduct: function () {
        let countProduct = 0;
        this.items.forEach(item => countProduct += item.count);
        return countProduct;
    },

    deleteFromBasket(id) {
        const indexItem = this.items.findIndex((item) => {
            return item.id === id;
        });
        this.items.splice(indexItem, 1);
        basket.referenceBasket(basket.items);
    },

    referenceBasket: function (x) {

        if (this.totalCount === 0) {
            localPlace.innerHTML = '<br> <h2>Корзина пуста</h2>';
            localDelivery.innerHTML = '';
            localComments.innerHTML = '';
        }
        else {
            this.totalCount = basket.getCountProduct();
            this.totalPrice = basket.getSumProduct();
            localPlace.innerHTML = `<br> <h3>Стоимость добавленных вами ${this.totalCount}
            товаров составляет ${this.totalPrice} рублей</h3> <br> <h4>Состав корзины:</h4> `

            for (let i = 0; i < x.length; i++) {
                const div = document.createElement('div');
                div.innerHTML =
                    `<div id="${x[i].id}" class="prod_item">
                        <div class="item_basket">
                            <div class="name"><h4>${x[i].name}</h4>${x[i].color}
                                <div class="price">Цена:
                                    <span>${x[i].price}</span> руб.
                                    <div class = "count_basket"> Количество ${x[i].count} </div>
                                </div>
                            </div>
                        </div>

                        <div><button data-id="${x[i].id}" class="button_basket_delete">Удалить</button> </div>
                        <br>
                        <div><button data-id="${i}" class="button_basket_add">Увеличить число товара</button></div>
                        <br>
                        <div><button data-id="${i}" class="button_basket_minus">Уменьшить число товара</button></div>
                        <br>
                    </div>`;

                localPlace.appendChild(div);
            }

            basket.referenseDeliveryAdress();
            basket.referenceComments();
            basket.referenseButtonNext();
        }

    },

    referenseDeliveryAdress: function () {

        localDelivery.innerHTML =
            `<div class="adress">
                <br>
                <h4 id = "delivery"> Ваш адрес доставки </h4>
                <div id = "hidden_adress">
                    <div>Город</div>
                    <input type="text" size="40">
                    <div>Улица</div>
                    <input type="text" size="40">
                    <div>Дом</div>
                    <input type="text" size="40">
                    <div>Квартира</div>
                    <input type="text" size="40">
                    <p><input type="submit" value="Отправить">
                    <input type="reset" value="Очистить"></p>
                </div>
            </div>`;

    },


    referenceComments: function () {

        localComments.innerHTML =
            `<div  class="comments">
                <div class="comment_clock">
                    <h4 id = "comment_hidden">Поле комментария</h4>
                    <div id = "hidden_comment">
                        <form name="test" method="post" action="input1.php">
                        <p><b>Ваше имя:</b><br>
                        <input type="text" size="40">
                        </p>

                        <p>Комментарий<Br>
                        <textarea name="comment" cols="40" rows="3"></textarea></p>
                        <p><input type="submit" value="Отправить">
                        <input type="reset" value="Очистить"></p>
                        </form>
                    </div>
                </div>
            </div>`;
    },


    referenseButtonNext: function () {

        if (basket.items.length == 0) {
            localNext.innerHTML = "";
        } else {
            //const div = document.createElement('div');
            localNext.innerHTML =
                `<br>
            <div><button class="button_next">Далее</button></div>
            `;
        }
    },

}

// Блок витрины

const showcase = {

    settings: {
        modalImageCloseSrc: 'img/add'
    },

    items: [],

    addToShowcase: function (product) {
        this.items.push({ ...product, count: 1 });
    },


    referenceShowcase: function (x) {
        for (let i = 0; i < x.length; i++) {
            const div = document.createElement('div');
            div.innerHTML =
                `<div id="${x[i].id}" class="prod_item">
                    <div class="item">
                        <div class="name"><h4>${x[i].name}</h4>${x[i].color}
                            <div class="price">Цена:
                                    <span>${x[i].price}</span> руб.
                            </div>
                        </div>
                    </div>
                    <div class="sale">
                        <button data-id="${x[i].id}" class="button">В корзину</button>
                    </div>
                </div>`;
            localPlaceProduct.appendChild(div);
        }
        basket.referenceBasket();
    },
}

// Блок событий

// Добавление в корзину с витрины

localPlaceProduct.addEventListener('click', function (e) {
    if (e.target.className === 'button') {
        const id = e.target.dataset.id;
        const choice = showcase.items.findIndex(item => {
            return item.id === +id;
        })
        const choice_basket = basket.items.findIndex(item => {
            return item.id === +id;
        });
        if (choice_basket !== -1) {
            basket.items[choice_basket].count += 1;
            console.log(basket.items);
            basket.referenceBasket(basket.items);
        }
        else {
            basket.addToBasket(showcase.items[choice], 1);
            basket.referenceBasket(basket.items);
        }
    }
});

// Удаление из корзины

localPlace.addEventListener('click', function (f) {
    if (f.target.className === 'button_basket_delete') {
        const id = Number(f.target.dataset.id);
        basket.deleteFromBasket(id);
        basket.referenceBasket(basket.items);
    }
});

// Увеличение объема продукта в корзине

localPlace.addEventListener('click', function (y) {
    if (y.target.className === 'button_basket_add') {
        const id = Number(y.target.dataset.id);
        basket.items[id].count += 1;
        basket.referenceBasket(basket.items);
    }
});

//Уменьшение объема продукта в корзине

localPlace.addEventListener('click', function (z) {
    if (z.target.className === 'button_basket_minus') {
        const id = Number(z.target.dataset.id);
        if (basket.items[id].count < 1) {
            basket.deleteFromBasket(id);
            basket.referenceBasket(basket.items);
        }
        else {
            basket.items[id].count--;
            basket.referenceBasket(basket.items);
        }
    }
});

// Клик по кнопке "далее"

let i = 0;
localNext.addEventListener('click', function (y) {

    if (y.target.className === 'button_next' && i == 0) {
        localDelivery.classList.remove('hidden');
        localPlace.classList.add('hidden');
        basket.referenceBasket(basket.items);
        i++;
    } else if (y.target.className === 'button_next' && i == 1) {
        localDelivery.classList.add('hidden');
        localComments.classList.remove('hidden');
        basket.referenceBasket(basket.items);
        i++;
    } else if (y.target.className === 'button_next' && i == 2) {
        localDelivery.classList.add('hidden');
        localPlace.classList.remove('hidden');
        localComments.classList.add('hidden');
        basket.referenceBasket(basket.items);
        i -= 2;
    }
});



// Блок вызовов

showcase.addToShowcase(product_1);
showcase.addToShowcase(product_2);
showcase.addToShowcase(product_3);
showcase.addToShowcase(product_4);
showcase.addToShowcase(product_5);

showcase.referenceShowcase(showcase.items);



