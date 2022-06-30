// Урок 3. Домашнее задание.
//Задание 1. С помощью цикла while вывести все простые числа в промежутке от 0 до 100.

let n = 0;
let y = 100;
let arrNumbers = [];


function getSimpleNumbers(n, y) {
    while (n <= y) {
        if (n == 3 || n == 5 || n == 7) {
            arrNumbers.push(n);
            n++;
            continue;
        }
        else if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0 || n == 1) {
            n++;
            continue;
        }
        else {
            arrNumbers.push(n);
            n++;
            continue;
        }
    }
    return arrNumbers
}

console.log(getSimpleNumbers(n, y));


//Задание 2. С этого урока начинаем работать с функционалом интернет-магазина. Предположим, есть
//сущность корзины. Нужно реализовать функционал подсчета стоимости корзины в
//зависимости от находящихся в ней товаров.
//Задание 3. Товары в корзине хранятся в массиве. Задачи:
//a. Организовать такой массив для хранения товаров в корзине;
//b. Организовать функцию countBasketPrice, которая будет считать стоимость корзины.


const basket = new Object();

basket['pen'] = 100;
basket['pencil'] = 200;
basket['steak'] = 300;
basket['paper'] = 500;
basket['lamp'] = 600;

console.log(basket);

function countBasketPrice(x) {
    let sumPrice = 0;
    for (const key in x) {
        sumPrice += x[key];
    }
    return sumPrice;
}

console.log(countBasketPrice(basket));

//Задание 4. Вывести с помощью цикла for числа от 0 до 9, не используя тело цикла. Выглядеть это
//должно так: for(...){здесь пусто}

for (let i = 0; i <= 9; console.log(i), i++);

// Задание 5. * Нарисовать пирамиду с 20 рядами с помощью console.log, как показано на рисунке:

let x = 20;

function drawPhyramid(x) {
    let strDraw = ''
    for (let i = 1; i <= x; console.log(strDraw += 'x'), i++);
}

drawPhyramid(x)

