
//Урок 2. JS. Домашняя работа

//Практикум - игра в число.

let number;
let attempts;

function resetGame() {
    attempts = 0;
    number = Math.floor(Math.random() * 100);
}

function tryGuessNumber() {
    const userAnswer = parseInt(prompt('Введите число от 0 до 100, для выхода введите -1'));

    if (userAnswer === -1) {
        alert('До свидания');
        return;
    }

    if (Number.isNaN(userAnswer) || userAnswer < 0 || userAnswer >= 100) {
        alert('Необходимо число от 0 до 100');
        tryGuessNumber();
        return;
    }

    attempts++;

    if (userAnswer > number) {
        alert('Попробуйте число меньше');
    } else if (userAnswer < number) {
        alert('Попробуйте число больше');
    } else {
        alert(`Поздравляю! Вы выиграли с ${attempts} попытки`);

        if (!confirm('Хотите сыграть еще раз?')) {
            alert('До свидания');
            return;
        }
        resetGame();
    }

    tryGuessNumber();
}

resetGame();
tryGuessNumber();

//Задание 1

var a = 1, b = 1, c, d;
c = ++a; alert(c); // 2 Операция инкремента - первично значение увеличивается,
// после присваивается. Алерт выводит уже увеличенное значение.
d = b++; alert(d); // 1 Операция инкремента - первично значение присваивается, после увеличивается на 1
// алерт выводит присвоенное значение
c = (2 + ++a); alert(c); // 5 2 складывается с увеличенным на 1 значением а(2+1), инкремент стоит до переменной
d = (2 + b++); alert(d); // 4 2 складывается с присвоенным значением b (2), инкремент стоит после переменной и
//увеличивает ее на 1 после арифметической операции
alert(a); // 3 Переменная а = 3 (к первичной а применен дважды инкремент)
alert(b); // 3 Переменная b = 3 (к первичной а применен дважды инкремент)


//Задание 2
var a = 2;
var x = 1 + (a *= 2);
//х будет равен 5. Первично выполняются операторы за скобками-умножение на 2, после - сложение +1

// Задание 3. Объявить две целочисленные переменные — a и b и задать им произвольные начальные
//значения. Затем написать скрипт, который работает по следующему принципу:
//- если a и b положительные, вывести их разность;
//- если а и b отрицательные, вывести их произведение;
//- если а и b разных знаков, вывести их сумму;
// Ноль можно считать положительным числом.

function numbersMath() {
    let a = 50 - Math.floor(Math.random() * 100);
    let b = 50 - Math.floor(Math.random() * (100));
    alert(`Первое случайное число  ${a}`);
    alert(`Второе случайное число ${b}`);

    if (a >= 0 && b >= 0) {
        return (`Разность чисел ${a - b}`);
    }

    else if (a < 0 && b < 0) {
        return (`Произведение чисел ${a * b}`);
    }

    else {
        return (`Сумма чисел ${a + b}`);
    }
}

alert(numbersMath());

//Задание 4.
//Присвоить переменной а значение в промежутке [0..15]. С помощью оператора switch
//организовать вывод чисел от a до 15.

function numbersView() {
    let a = Math.floor(Math.random() * 15);
    console.log(`Случайное число от 0 до 15: ${a}`);
    return a;
}

function numberPrint(number) {
    switch (number) {
        case 15:
            return console.log(number);

        default:
            return console.log(number), numberPrint(number + 1);
    }
}

numberPrint(numbersView())



//Задание 5.
/* Реализовать четыре основные арифметические операции в виде функций с двумя
параметрами. Обязательно использовать оператор return.*/
//Задание 6.
/* Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation),
где arg1, arg2 — значения аргументов, operation — строка с названием операции. В
зависимости от переданного значения выполнить одну из арифметических операций
(использовать функции из пункта 5) и вернуть полученное значение (применить switch).*/

function addNumbers(a, b) {
    return a + b;
}

function minusNumbers(a, b) {
    return a - b;
}

function divNumbers(a, b) {
    return a / b;
}

function multiplyNumbers(a, b) {
    return (a * b);
}

function numbersMath(arg1, arg2, operation) {
    switch (operation) {
        case '+':
            return addNumbers(arg1, arg2);
        case '-':
            return minusNumbers(arg1, arg2);
        case '/':
            if (arg2 != 0) {
                return divNumbers(arg1, arg2);
            }
            else {
                return 'Ошибка. Деление на ноль';
            }
        case '*':
            return multiplyNumbers(arg1, arg2);
        default:
            return 'Ошибка оператора функции';
    }
}

console.log(numbersMath(1, 2, '+'));
console.log(numbersMath(1, 2, '-'));
console.log(numbersMath(1, 2, '/'));
console.log(numbersMath(1, 2, '*'));
console.log(numbersMath(1, 2, 'e'));
console.log(numbersMath(1, 0, '/'));


//Задание 7.
// 7. * Сравнить null и 0. Объяснить результат.

console.log(0 == null);// false
console.log(0 === null);// false
console.log(0 > null);// false
console.log(0 < null);// false
console.log(null > 0); // false
console.log(null <= 0); // false
console.log(null >= 0); // true
console.log(typeof (0)); //number
console.log(typeof (null)); //object

//сей парадокс хорошо объянен на Хабре. Пруф: https://habr.com/ru/company/ruvds/blog/337732/
//краткий вывод: Если null < 0 принимает значение false, то null >= 0 принимает значение true

//Задание 8.
/* *С помощью рекурсии организовать функцию возведения числа в степень. Формат: function
power(val, pow), где val — заданное число, pow –— степень.*/

function power(val, pow) {
    if (pow == 0) {
        return 1;
    }
    else if (pow < 0) {
        return 1 / (val * power(val, (Math.abs(pow) - 1)));
    }
    else if (pow == 1) {
        return val;
    }
    else if (pow == -1) {
        return 1 / val;
    }
    else {
        return val * power(val, pow - 1);
    }
}

console.log(power(2, 3));
console.log(power(2, 0));
console.log(power(2, -3));
console.log(power(3, -1));
console.log(power(3, 3));
console.log(power(10, 10));
