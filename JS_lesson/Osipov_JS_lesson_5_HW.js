/* Урок 5.Практикум*/


const settings = {
    rowsCount: 10,
    colsCount: 10,
    startPositionX: 4,
    startPositionY: 6,
    startDirection: 'right',
    stepInSecond: 5,
    playerPositionColor: '#cb2222',
    emptyPositionColor: '#cccccc',
};

const player = {
    x: null,
    y: null,
    direction: null,

    init(startPosX, startPosY, startDirection) {
        this.x = startPosX;
        this.y = startPosY;
        this.direction = startDirection;
    },

    makeStep() {
        const nextPosition = this.getNextPosition();

        this.x = nextPosition.x;
        this.y = nextPosition.y;
    },

    getNextPosition() {
        const position = {
            x: this.x,
            y: this.y,
        }

        switch (this.direction) {
            case 'up':
                position.y--;
                break;
            case 'down':
                position.y++;
                break;
            case 'left':
                position.x--;
                break;
            case 'right':
                position.x++;
                break;
        }

        return position;
    },

    setDirection(direction) {
        this.direction = direction;
    },
};

const game = {
    settings: settings,
    player: player,
    containerElement: null,
    tdElements: [],

    init() {
        this.player.init(
            this.settings.startPositionX,
            this.settings.startPositionY,
            this.settings.startDirection,
        );
        this.containerElement = document.getElementById('game');
        this.renderPlayerField();
        this.renderPlayer();
        this.initEventHandler();
    },

    runGame() {
        this.init();

        setInterval(() => {
            if (this.canPlayerMakeStep()) {
                this.player.makeStep();
                this.renderPlayer();
            }
        }, 1000 / this.settings.stepInSecond);
    },

    renderPlayerField() {
        this.containerElement.innerHTML = '';

        for (let row = 0; row < this.settings.rowsCount; row++) {
            const trElem = document.createElement('tr');
            this.containerElement.append(trElem);

            for (let col = 0; col < this.settings.colsCount; col++) {
                const tdElem = document.createElement('td');
                this.tdElements.push(tdElem);
                trElem.append(tdElem);
            }
        }
    },

    initEventHandler() {
        document.addEventListener('keydown', (event) => {
            this.keyDownHandler(event);
        });
    },

    keyDownHandler(event) {
        switch (event.code) {
            case 'KeyW':
                this.player.setDirection('up');
                break;
            case 'KeyS':
                this.player.setDirection('down');
                break;
            case 'KeyA':
                this.player.setDirection('left');
                break;
            case 'KeyD':
                this.player.setDirection('right');
                break;
        }
    },

    renderPlayer() {
        this.tdElements.forEach((td) => {
            td.style.backgroundColor = this.settings.emptyPositionColor;
        });

        const playerPosition = document
            .querySelector(`tr:nth-child(${this.player.y + 1})`)
            .querySelector(`td:nth-child(${this.player.x + 1})`);

        playerPosition.style.backgroundColor = this.settings.playerPositionColor;
    },

    canPlayerMakeStep() {
        const nextPosition = this.player.getNextPosition();

        return nextPosition.x >= 0
            && nextPosition.y >= 0
            && nextPosition.x < this.settings.colsCount
            && nextPosition.y < this.settings.rowsCount;
    },
};

window.addEventListener('load', () => {
    game.runGame();
});





/*Задание 1. Создать функцию, генерирующую шахматную доску. Можно использовать любые html-теги.
Доска должна быть верно разлинована на черные и белые ячейки. Строки должны
нумероваться числами от 1 до 8, столбцы — латинскими буквами A, B, C, D, E, F, G, H.*/


const table = document.createElement('table');
const array = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ''];
const number = ['', '1', '2', '3', '4', '5', '6', '7', '8', ''];
const reverseNumber = number.reverse();

function renderchessDesk() {
    for (let i = 0; i < 10; ++i) {
        let tr = document.createElement('tr');
        table.append(tr);
        for (let j = 0; j < 10; ++j) {
            let td = document.createElement('td');
            tr.append(td);
            td.innerHTML = (i + 1) + j;

            if (td.innerHTML % 2 == 0) {
                td.style.backgroundColor = "#000000";//Закрашивание темных ячеек
            }

            if (i == 9 && 0 <= j <= 9) { // Последняя буквенная строка координат
                td.innerHTML = array[j];
            } else if (i == 0 && 0 <= j <= 9) { // Первая буквенная строка координат
                td.innerHTML = array[j];
            } else if (i <= 8 && j == 0) {//Левый цифровой столбец
                td.innerHTML = reverseNumber[i];
            } else if (i <= 8 && j == 9) {//Правый цифровой столбец
                td.innerHTML = reverseNumber[i];
            } else {
                td.innerHTML = '';
            }
        }
    }
    document.querySelector('div').append(table);
}

renderchessDesk();


/*Задание 2. Сделать генерацию корзины динамической: верстка корзины не должна находиться в
HTML-структуре. Там должен быть только div, в который будет вставляться корзина,
сгенерированная на базе JS:
a. Пустая корзина должна выводить строку «Корзина пуста»;
b. Наполненная должна выводить «В корзине: n товаров на сумму m рублей».*/

const basket = []
const localPlace = document.getElementById('basket');

function finalCost(basket) {
    return basket.reduce(function (acc, basket) {
        return acc + (basket.price * basket.count)
    }, 0)
};

function finalCount(basket) {
    return basket.reduce(function (acc, basket) {
        return acc + basket.count
    }, 0)
};

function referenceBasket() {
    if (finalCount(basket) === 0) {
        localPlace.innerHTML = 'Корзина пуста';
    }
    else {
        localPlace.innerHTML = `Стоимость добавленных вами ${finalCount(basket)} товаров составляет ${finalCost(basket)}`
    }
}


class Product {
    constructor(id, name, color, price, weight, status = 'free') {
        this.id = id;
        this.name = name;
        this.color = color;
        this.price = price;
        this.weight = weight;
        this.status = status;
    }

    putToBasket() {
        //const countProduct = parseInt(prompt(`Введите количество товара ${ this.name } `));
        const countProduct = 10;
        const idProductBasket = basket.length + 1;
        const productBasket = {
            id: idProductBasket,
            name: this.name,
            color: this.color,
            price: this.price,
            weight: this.weight,
            status: this.status,
            count: countProduct
        }
        //alert(`Товар ${ this.name } добавлен в корзину`);
        this.status = 'inBasket';
        basket.push(productBasket);
    }
}

let product_1 = new Product(123, 'Ручка', 'Черная', 100, 50);
let product_2 = new Product(456, 'Карандаш', 'Коричневый', 50, 30);
let product_3 = new Product(556, 'Стерка', 'Белая', 20, 10);


product_1.putToBasket();
product_2.putToBasket();
product_3.putToBasket();

referenceBasket();

