/* Урок 4. Задание 1. Написать функцию, преобразующую число в объект. Передавая на вход число от 0 до 999,
надо получить на выходе объект, в котором в соответствующих свойствах описаны единицы,
десятки и сотни. Например, для числа 245 надо получить следующий объект: {‘единицы’: 5,
‘десятки’: 4, ‘сотни’: 2}. Если число превышает 999, необходимо выдать соответствующее
сообщение с помощью console.log и вернуть пустой объект.*/


let numberHave = {
    units: 0,
    tens: 0,
    hundreds: 0,

    getParts: function (x) {
        let numberNundreds = (x - x % 100) / 100;
        let y = x % 100;
        let numberTens = (y - y % 10) / 10;
        let numberUnits = y % 10;
        numberHave.units = numberUnits;
        numberHave.tens = numberTens;
        numberHave.hundreds = numberNundreds;
    }
}

let initGame = {
    startGame: function () {
        while (true) {
            number = parseInt(prompt('Введите число от 0 до 999. Если хотите выйти - введите "-1"'));

            if (number === -1) {
                alert('До свидания');
                break;
            }
            else if (0 > number || number > 999) {
                alert('Ошибка ввода.');
                continue;
            }
            else {
                numberHave.getParts(number);
                alert(`В введенном вами числе. ${numberHave.hundreds} сотен, ${numberHave.tens} десятков, ${numberHave.units} единиц`);
                if (!confirm('Хотители бы продолжить?')) {
                    alert('До свидания!');
                    break
                }
            }
        }
    }
}

initGame.startGame();



/*  Задание 2. Продолжить работу с интернет-магазином:
a. В прошлом домашнем задании вы реализовали корзину на базе массивов. Какими
объектами можно заменить их элементы?
b. Реализуйте такие объекты.
c. Перенести функционал подсчета корзины на объектно-ориентированную базу.
Задание 3. * Подумать над глобальными сущностями. К примеру, сущность «Продукт» в
интернет-магазине актуальна не только для корзины, но и для каталога. Стремиться нужно к
тому, чтобы объект «Продукт» имел единую структуру для различных модулей сайта, но в
разных местах давал возможность вызывать разные методы.*/


const basket = {
    getSumProduct: function (x) {
        countPrice = 0;
        for (const key in x) {
            countPrice += x[key];
        }
        return countPrice;
    }
}

class Product {
    constructor(name, color, price, weight, status = 'free') {
        this.name = name;
        this.color = color;
        this.price = price;
        this.weight = weight;
        this.status = status;
    }

    putToBasket(x) {
        //alert(`Товар ${this.name} добавлен в корзину`);
        this.status = 'inBasket';
        basket[this.name] = parseInt(this.price);


    }

    putToShowcase() {
        //alert(`Товар ${this.name} добавлен на витрину`);
        this.status = 'inShowcase';
    }

    addProduc() {
        alert('Заполните данные продукта');
        this.name = prompt('Введите наименование продукта'); //тут можно настроить корректность заполнения поля
        this.color = prompt('Введите цвет продукта'); //тут можно настроить корректность заполнения поля
        this.price = parseInt(prompt('Введите цену продукта в целых числах')); //тут можно настроить корректность заполнения поля
        this.weight = parseInt(prompt('Введите вес продукта в целых числах')); //тут можно настроить корректность заполнения поля
    }

}

let product_1 = new Product('Ручка', 'Черная', 100, 50);
let product_2 = new Product('Карандаш', 'Коричневый', 50, 30);
let product_3 = new Product('Стерка', 'Белая', 20, 10);

product_1.putToBasket(product_1);
product_2.putToBasket(product_2);
product_3.putToBasket(product_3);

//product_1.putToShowcase();


alert(basket.getSumProduct(basket));

