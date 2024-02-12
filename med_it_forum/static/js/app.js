document.addEventListener('DOMContentLoaded', () => { // DOM готов к взаимодейтсвию

    const onScrollHeader = (elementClass) => { // объявляем основную функцию onScrollHeader
        
        const header = document.querySelector(elementClass) // находим header и записываем в константу

            let prevScroll = window.pageYOffset // узнаем на сколько была прокручена страница ранее
            let currentScroll // на сколько прокручена страница сейчас (пока нет значения)

            window.addEventListener('scroll', () => { // при прокрутке страницы

            currentScroll = window.pageYOffset // узнаем на сколько прокрутили страницу

            // const headerHidden = () => header.classList.contains('header_hidden') // узнаем скрыт header или нет

            // if (currentScroll > prevScroll) { // если прокручиваем страницу вниз и header не скрыт
            //     header.classList.add('header_hidden') // то скрываем header
            // }
            // if (currentScroll < prevScroll) { // если прокручиваем страницу вверх и header скрыт
            //     header.classList.remove('header_hidden') // то отображаем header
            // }

            prevScroll = currentScroll // записываем на сколько прокручена страница на данный момент

        })
        
    }
    const elementAr = ['.header', '.side-nav']
    for (const element of elementAr) {
        onScrollHeader(element) // вызываем основную функцию onScrollHeader
        }
    });