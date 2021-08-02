const puppeteer = require('puppeteer');

async function testTaxiResult() {

    console.log('Запуск браузера');
    const browser = await puppeteer.launch({
        headless: false,
        slowMo: 100,
    });

    console.log('+ Новая вкладка');
    const page = await browser.newPage();

    console.log('Переход по ссылке');
    await page.goto("http://qa-routes.praktikum-services.ru/");

    console.log('Шаг1: Ввод времени: 08:00');
    const houreInput = await page.$('#form-input-hour');
    await houreInput.type('08');

    const minuteInput = await page.$('#form-input-minute');
    await minuteInput.type('00');

    console.log('Шаг2: Откуда: Усачева, 3');
    const fromInput = await page.$('#form-input-from');
    await fromInput.type('Усачева, 3');

    console.log('Шаг3: Куда: Комсомольский проспект, 18');
    const toInput = await page.$('#form-input-to');
    await toInput.type('Комсомольский проспект, 18');

    console.log('Шаг4: Выбираем режим: Свой');
    const modeCustom = await page.$('#form-mode-custom');
    await modeCustom.click();

    console.log('Шаг5: Выбираем вид транспорта: Такси');
    const typeOfTransport = await page.$('#from-type-taxi');
    await typeOfTransport.click();

    console.log('Шаг6: Ожидание элемента с результатом');
    await page.waitForSelector('#result-time-price');

    console.log('Шаг7: Получаем сторики с результатом');
    const text = await page.$eval('#result-time-price', element => element.textContent);

    console.log('Шаг8: Проверка ОР с ФР');
        if (text.startsWith('Такси ~ 13 руб.')) {
            console.log('Успех');
        }
        else {
            console.log('Ошибка')
        }

    console.log('Закрытие браузера');
    await browser.close();
}

testTaxiResult();