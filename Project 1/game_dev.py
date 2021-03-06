#===< Quizes >===#

def quiz_1():
    """
    Ця функція виводить питання вікторини для першої глави й 
    запитує гравця правильну відповідь після чого виводить, чи 
    правильно гравець відповів на питання
    
    >>> (1) Хто є автором картини "Народження Венери"?
                1 - Сандро Ботічеллі
	            2 - Леонардо да Вінчі
	            3 - Пікассо
        
        >>> 1
        Правильно
    
    Залежно від відповіді гравця функція повертає значення
    змінної game_state, що в подальшому оброблятиметься
    функцією first_act
    """
    counter = 0
    mistake_rate = 3 
    quiz = ['(1) Хто є автором картини "Народження Венери"?\n' #забрати правильні відповіді
                '\t1! - Сандро Ботічеллі\n'
	            '\t2 - Леонардо да Вінчі\n'
	            '\t3 - Пікассо\n', 
            '(2) Однією з відомих картин Рафаеля Санті є:\n'
                '\t1! - Сікстинська Мадонна\n'
	            '\t2 - Весна\n'
	            '\t3 - Мона Ліза\n', 
            '(3) На картині "Афінська школа" Рафаеля Санті було зображено:\n'
                '\t1 - Платона і Геродота\n'
	            '\t2 - Геродота і Перікла\n'
	            '\t3! - Аристотеля і Платона\n', 
            '(4) Автор картини "Мона Ліза" також був автором картини:\n'
                '\t1 - Весна\n'
	            '\t2! - Таємна вечеря\n'
	            '\t3 - Створення Адама\n', 
            '(5) Хто зображений в центрі картини "Страшний суд" Мікеланджело Буанарроті:\n'
                '\t1 - Феміда\n'
	            '\t2 - Марія Магдалина\n'
	            '\t3! - Ісус Христос\n', 
            '(6) Хто був автором картини "Успіння Богородиці":\n'
                '\t1 - Мікеланджело\n'
	            '\t2 - Леонардо да Вінчі\n'
	            '\t3! - Тиціан\n', 
            '(7) Яка альтернативна назва "Мони Лізи":\n'
            	"\t1 - Ізабелла д'Есте\n"
	            '\t2! - Джоконда\n'
	            '\t3 - Ліза Герардіні\n', 
            '(8) Який з цих винаходів не належить Леонардо да Вінчі?\n'
            	'\t1 - Танк\n'
	            '\t2! - Дельтаплан\n'
	            '\t3 - Кулемет\n', 
            '(9) Розпис Сікстинської капели здійснив:\n'
                '\t1! - Мікеланджело\n'
	            '\t2 - Тиціан\n'
	            '\t3 - Сандро Ботічеллі\n', 
            '(10) Хто на картині "Сікстинська мадонна" має 6 пальців?\n'
                '\t1 - Богородиця\n'
	            '\t2 - Ангел внизу картини\n'
	            '\t3! - Папа Сікст ІІ\n']
    
    answers = ["1", "1", "3", "2", "3", "3", "2", "2", "1", "3"]
    
    for i in range(len(quiz)):
        if mistake_rate == 0:
            print("Саймон загинув від руки вершника Кетерфільда")
            game_state = 0
            return game_state
        elif counter == 10:
            game_state = 1
            return game_state
        print(quiz[i])
        user_answer = input(">>> ")
        if user_answer == answers[i]:
            print("Правильно\n")
        else:
            print("Неправильно\n")
            mistake_rate -= 1
        counter += 1

def bonus_quiz():
    """
    Ця функція виводить бонусні питання вікторини для другої глави й 
    запитує гравця правильну відповідь після чого виводить, чи 
    правильно гравець відповів на питання
    
    >>> (1) Коли відбувся перший хрестовий похід?
                1 - 1090-1095 рр.
	            2 - 1096 - 1099 рр.
	            3 - 1100 - 1105 рр.
        
        >>> 1
        Неправильно
    
    Функція повертає значення game_state, який ніде не обробляється
    """
    counter = 0
    quiz = ['(1) Коли відбувся перший хрестовий похід?\n'
                '\t1 - 1090-1095 рр.\n'
	            '\t2! - 1096 - 1099 рр.\n'
	            '\t3 - 1100 - 1105 рр.\n', 
            '(2) Учасником третього хрестового походу не був:\n'
                '\t1 - Річард І Левине Серце\n'
	            '\t2 - Фрідріх І Барбаросса\n'
	            '\t3! - Раймунд де Пуатьє\n', 
            '(3) Орден лицарів-госпітальєрів був заснований:\n'
                '\t1 - 1096 р.\n'
	            '\t2! - 1099 р.\n'
	            '\t3 - 1100 р.\n', 
            '(4) Орден лицарів-тамплієрів був заснований:\n'
                '\t1!- 1096 р.\n'
	            '\t2 - 1099 р.я\n'
	            '\t3 - 1100 р.\n', 
            '(5) Тевтонський орден рицарів був заснований:\n'
                '\t1! - 1190 р.\n'
	            '\t2 - 1205 р.\n'
	            '\t3 - 1184 р.\n'] 
    
    answers = ["2", "3", "2", "1", "1"]
    
    for i in range(len(quiz)):
        counter += 1
        print(quiz[i])
        user_answer = input(">>> ")
        if user_answer == answers[i]:
            print("Правильно\n")
        else:
            print("Неправильно\n")
        if counter == 5:
            game_state = 1
            return game_state

def quiz_2():
    """
    Ця функція виводить питання вікторини для другої глави й 
    запитує гравця правильну відповідь після чого виводить, чи 
    правильно гравець відповів на питання
    
    >>> (1) Яка з перелічених споруд побудована у романському стилі:
                1 - Нотр Дам де Парі
	            2 - Церква Санто Домінго
	            3 - Вестмінстерське аббатство
        
        >>> 1
        Неправильно
    
    Залежно від відповіді гравця функція повертає значення
    змінної game_state, що в подальшому оброблятиметься
    функцією second_act
    """
    counter = 0
    mistake_rate = 3
    quiz = ['(1) Яка з перелічених споруд побудована у романському стилі:\n' #забрати правильні відповіді
                '\t1 - Нотр Дам де Парі\n'
	            '\t2! - Церква Санто Домінго\n'
	            '\t3 - Вестмінстерське аббатство\n', 
            '(2) Якої статуї нема у Соборі Святого Петра?\n'
                '\t1! - Святої Олени\n'
	            "\t2 - П'єтта\n"
	            '\t3 - Святого Патриція\n', 
            '(3) Де розташований Собор Святого Стефана?\n'
                '\t1 - Париж\n'
	            '\t2! - Відень\n'
	            '\t3 - Реймс\n', 
            '(4) Де розташований Собор Святої Родини?\n'
                '\t1 - Париж\n'
	            '\t2 - Київ\n'
	            '\t3! - Барселона\n', 
            '(5) Де розташований Собор Санта-Марія-дель-Фьоре?\n'
                '\t1 - Іспанія\n'
	            '\t2! - Італія\n'
	            '\t3 - Франція\n', 
            '(6) Архітектором якого собору був Мікеланджело?\n'
                '\t1! - Собор Святого Петра\n'
	            '\t2 - Собор Паризької Богоматері\n'
	            '\t3 - Собор Василія Великого\n', 
            '(7) Яка з перелічених споруд не належить до стилю ренесансу?\n'
            	"\t1 - Вежа Корнякта\n"
	            '\t2! - Версальський палац\n'
	            '\t3 - Палац дель Те\n', 
            '(8) До якого стилю належить Йоркський собор?\n'
            	'\t1! - Готичний\n'
	            '\t2 - Ренесанс\n'
	            '\t3 - Романський\n', 
            '(9) Позначте правильне твердження про скульптуру "Мойсей" Мікеланджело Буанаротті:\n'
                '\t1! - Мойсей має ріжки\n'
	            '\t2 - Мойсей зображений стоячи\n'
	            '\t3 - Крижалі, які тримає Мойсей є зламаними\n', 
            "(10) Який підпис має римська П'єтта Мікеланджело?\n"
                '\t1 - Aut cum scuto, aut in scuto\n'
	            '\t2 - Sator arepo tenet opera rotas\n'
	            '\t3! - Michael Angelus Buonarrotus Florent. faciebat\n']
    
    answers = ["2", "1", "2", "3", "2", "1", "2", "1", "1", "3"]
    
    for i in range(len(quiz)):
        if mistake_rate == 0:
            print("Саймону розкололи череп сокирою")
            game_state = 0
            return game_state
        elif counter == 10:
            game_state = 1
            return game_state
        print(quiz[i])
        user_answer = input(">>> ")
        if user_answer == answers[i]:
            print("Правильно\n")
        else:
            print("Неправильно\n")
            mistake_rate -= 1
        counter += 1

def quiz_3():
    """
    Ця функція виводить питання вікторини для третьої глави й 
    запитує гравця правильну відповідь після чого виводить, чи 
    правильно гравець відповів на питання
    
    >>> (1) Коли відбулася битва під Таутоном?
                1 - 1461 р.
	            2 - 1465 р.
	            3 - 1478 р.
        
        >>> 1
        Правильно
    
    Залежно від відповіді гравця функція повертає значення
    змінної game_state, що в подальшому оброблятиметься
    функцією third_act
    """
    counter = 0
    mistake_rate = 3
    quiz = ['(1) Коли відбулася битва під Таутоном\n' #забрати правильні відповіді
                '\t1! - 1461 р.\n'
	            '\t2 - 1465 р.\n'
	            '\t3 - 1478 р.\n', 
            '(2) Столітня війна відбувалася у 1337-1453 рр. між:\n'
                '\t1! - Англією і Францією\n'
	            '\t2 - Польщею і Угорщиною\n'
	            '\t3 - Іспанією і Португалією\n', 
            '(3) Облога Орлеана тривала протягом:\n'
                '\t1 - 1427-1428 рр.\n'
	            '\t2! - 1428-1429 рр.\n'
	            '\t3 - 1429-1430 рр.\n', 
            '(4) Грюнвальдська битва відбулася в:\n'
                '\t1 - 1420 р.\n'
	            '\t2 - 1415 р.\n'
	            '\t3! - 1410 р.\n', 
            '(5) Хто програв у Грюнвальдській битві?\n'
                '\t1 - Руське королівство\n'
	            '\t2 - Польща\n'
	            '\t3! - Тевтонський орден\n', 
            '(6) Який півострів був звільнений у результаті реконкісти?\n'
                '\t1 - Кримський\n'
	            '\t2! - Піренейський\n'
	            '\t3 - Балканський\n', 
            '(7) Хто був командувачем битви на Синіх Водах зі сторони ВКЛ:\n'
            	"\t1 - Ягайло Ольгердович\n"
	            '\t2! - Ольгерд Гедимінович\n'
	            '\t3 - Свидригайло Ольгердович\n', 
            '(8) Скільки запорожців загинуло в битві під Хотином?\n'
            	'\t1! - 6500\n'
	            '\t2 - 5500\n'
	            '\t3 - 7000\n', 
            '(9) Хто був на чолі запорозького війська під час Хотинської битви?\n'
                '\t1 - Богдан Хмельницький\n'
	            '\t2 - Пилип Орлик\n'
	            '\t3! - Петро Сагайдачний\n', 
            '(10) Який воєвода захищав Київ під час навали монголів?\n'
                '\t1! - Дмитро\n'
	            '\t2 - Василь\n'
	            '\t3 - Кирило\n']
    
    answers = ["1", "1", "2", "3", "3", "2", "2", "1", "3", "1"]
    
    for i in range(len(quiz)):
        if mistake_rate == 0:
            print("Саймону потрапила стріла в око")
            game_state = 0
            return game_state
        elif counter == 10:
            game_state = 1
            return game_state
        print(quiz[i])
        user_answer = input(">>> ")
        if user_answer == answers[i]:
            print("Правильно\n")
        else:
            print("Неправильно\n")
            mistake_rate -= 1
        counter += 1

#===< Game Acts >===#

def introduction():
    """
    Дана функція вітається з гравцем, запитує його ім'я й
    коротко описує середовище гри
    """
    player_name = input("Вітаю гравець! Як мені Вас називати?\n>>> ")
    print(f"\nЧудово, {player_name}, запрошуєм у Дрейквіль - маленьке селище ХХIV ст.\n"
           "Ви гратимете за 8-річного селянського хлопчину Саймона,\n"
           "життя якого одного дня кардинально перевернулося")

def first_act():
    """
    Дана функція виводить першу главу історії про головного героя
    і в процесі оповіді викликає функцію quiz_1.
    Залежно від значення функції quiz_1 гра або продовжується
    або гравцеві пропонується перепройти рівень

    >>> "Глава 1: Непросте життя"
        ...
        Бажаєте перепройти?
        >>> Ні
        Дякую за гру! Сподіваюсь ви гарно провели час :)
    """
    input(">>> ")
    print("Глава 1: Непросте життя\n")
    print("Ішов третій рік війни між Греббергом і Кетерфільдом.\n" 
          "Дух болю, голоду, смерті й втрати витали над обома країнами,\n" 
          "армії грабували та зрівнювали все із землею, де проходили.\n"
          "Та наша історія починається в Дрейквілі - маленькому містечку на маленькій річечці Квельт,\n" 
          "яка розділяла країну Греббергу на полігон для війни й плодючі поля.")
    input(">>> ")
    print("Одного ранку Саймон прокинувся й вийшов на ганок свого \n"
          "будиночку трохи раніше, ніж містечко зазвичай оживало.\n"
          "Свіже вранішнє повітря наповнило легені нашого малого героя,\n"
          "а ритм його серця попадав у тихе хлюпотіння річки.\n"
          "Щоправда хлопця дещо турбувало й він довго не міг зрозуміти, що саме.\n"
          "Раптом до нього прийшло усвідомлення:\n"
          "надворі було могильно тихо. Неначе природа затаїлась і чекала чогось. \n"
          "Чого? Він це зрозумів доволі швидко.\n"
          "Піднявши голову догори, хлопець побачив те, що нагадувало \n"
          "оповідки батьків про зірки, які падають.\n"
          "Та це були не зірки. Підпалені стріли посипались зверху,\n"
          "як вогняний град. Село спалхнуло, як сірник.\n"
          "Люди вибігли на вулиці й почалася метушня. Здалеку почувся стук копит.\n"
          "Було зрозуміло одне: потрібно рятуватись.")
    input(">>> ")
    game_state = quiz_1()
    if game_state == 0:
        adventure = input("\nБажаєте переграти?\n>>> ")
        if adventure == "Так":
            first_act()
        else:
            print("Дякую за гру! Сподіваюсь ви гарно провели час :)")
            exit()
    else:
        print("Того дня вулиці Дрейквілю потопали у крові. \n"
              "Вершники Катерфільда не залишили нічого, що нагадувало б\n"
              "про безтурботне минуле містечка. Спалені хижі, розбиті прилавки,\n"
              "пограбовані храми - нічого не врятувалося\n" 
              "від їхнього іго... окрім одного хлопця в одній бочці,\n"
              " що закотилася під прилавок місцевого ринку.")
        input(">>> ")
        print("Саймона в бочці знайшов командир загону, який прибув на місце побоїща,\n"
              "побачивши дим, що звивався та губився в небі.\n"
              "Очевидо було, що Саймон залишився сиротою. Командирові стало шкода хлопця,\n"
              "тому він вирішив усиновити його й виховати на свій лад.\n")

def second_act():
    """
    Дана функція виводить другу главу історії про головного героя
    і в процесі оповіді викликає функції bonus_quiz та quiz_2.
    Незалежно від значення функції bonus_quiz гра продовжується, а
    значення функції quiz_2 вирішує чи гра продовжується чи гравцеві
    пропонується перепройти рівень

    >>> Глава 2: Нове життя
        ...
        Бажаєте перепройти?
        >>> Так
        Глава 2: Нове життя
    """
    input(">>> ")
    print("Глава 2: Нове життя\n")
    print("Спершу Саймону не надто подобалась його нове життя,\n"
          "втім, згодом він звик. Виснажуючі тренування й\n" 
          "біль у м'язах йшли йому на користь. Окрім того\n"
          "лицарське ремесло чимось вабило його,\n" 
          "а оповіді батька-командира про бойойві подвиги\n"
          "горіли вогником у його ще дитячих очах.")
    input(">>> ")
    print("Окрім того, Саймон доволі сумував за своїм містечком і,\n"
          " звичайно, за батьками, з якими він провів більшість\n"
          "свого життя. Тому глибоко в душі він хотів помсти\n"
          "і це мотивувало його ще більше.")
    input(">>> ")
    bonus_quiz()
    print("Минали роки... Саймон тренувався й змужнів.\n"
          "Всі любили Саймона, адже він був доброзичливим, справедливим,\n" 
          "поміркованим і, водночас, до неможливості винахідливим чортякою. \n"
          "Саймон цінував це й обожнював усіх своїх\n" 
          "побратимів, а також дуже любив свого батька.")
    input(">>> ")
    print("Новини з фронту були не зовсім втішні. Країни не могли переважити\n"
          "одна одну й фронт залишався непорушним.Одного дня командир вирішив, \n" 
          "що Саймон був готовий відправитися в патруль разом із загоном.\n"
          "Патруль мав проїхати через ліс і віддати про це рапорт.")
    input(">>> ")
    print("...Патрулювання проходило гладко, за оцінкою командира патруль\n"
          "перебував десь на половині шляху. Та Саймона дещо непокоїло.\n" 
          "Він не міг зрозуміти що саме, але думка, що щось не так все ніяк\n"
          "не покидала його голову. І тут він зрозумів: було могильно тихо.\n" 
          "Враз стріла вилетіла з-за дерева й звалила з коня вершника.\n"
          "Це була засідка, тож довелося відбиватися")
    input(">>> ")
    
    game_state = quiz_2()
    if game_state == 0:
        adventure = input("\nБажаєте переграти?\n>>> ")
        if adventure == "Так":
            second_act()
        else:
            print("Дякую за гру! Сподіваюсь ви гарно провели час :)")
            exit()
    else:
        print("Бій був безжальним і кривавим. Саймону вдалося прорватися до\n"
              "командира загону ворожих солдат і вбити його ударом меча в серце.\n"
              "Після перемоги над супостатами з грудей Саймона вирвався тріумфальний\n"
              "клич. Та, коли він обернувся, тріумф перетворився у відчай,\n" 
              "а відчай у лють. Під деревом, смертельно поранений, лежав його\n"
              "названий батько. Звичайно, наш герой канонічно підбіг до останнього\n"
              "й намагався запобігти неминучій смерті або хоча б максимально відтягнути\n"
              "її. Та це було неможливо. Останніми словами мудрого командира до молодого\n"
              "юнака були слова про шлях воїна. Воїни ніколи не вмирають у ліжку...")

def third_act():
    """
    Дана функція виводить другу главу історії про головного героя
    і в процесі оповіді викликає функцію quiz_3.
    Залежно від значення функції quiz_3 гра або продовжується
    або гравцеві пропонується перепройти рівень

    >>> Глава 3. Кінець?
        ...
        Бажаєте перепройти?
        >>> Так
        Глава 3. Кінець?
    """
    input(">>> ")
    input("Глава 3. Кінець?\n")
    print("Від того дня нашим героєм рухала тільки жага помсти. Битва за битвою,\n"
          "кампанія за кампанією, й скоро по усьому Греббергу ходили легенди про\n" 
          "лицаря Саймона Жорстокого, який не шкодував жодного ворога, який траплявся\n"
          "йому на шляху. Чин за чином, і невдовзі Саймон мав вести армію в останню\n" 
          "битву, де вирішувалася доля двох країн. Дві основні сили збралися того дня\n"
          "у вузькому переході на північному природньому кордоні в горах Хайграундс.\n"
          "У битві мали брати участь двоє королів, отже знищення армії прирівнювалося\n"
          "до капітуляції однієї із сторін.")
    input(">>> ")
    print("Саймон почув звуки бойового рогу. Він згадав усе: від знищення його містечка\n"
          "і смерті названого батька до тих жорстокостей на полі бою, до яких вдавалися\n"
          "воїни Кетерфільда. Ним рухала безмежна злість, однак все ж розум його лишався\n"
          "холодним. Він повів у бій своїх воїнів і розпочалася одна з наймасштабніших\n"
          "битв у історії двох країн")
    input(">>> ")
    game_state = quiz_3()
    if game_state == 0:
        adventure = input("\nБажаєте переграти?\n>>> ")
        if adventure == "Так":
            third_act()
        else:
            print("Дякую за гру! Сподіваюсь ви гарно провели час :)")
            exit()
    else:
        print("Саймон був у самому вогні поєдинку. У пилу бою він встиг побачити короля ворожого\n"
              "війська й розрубавши навпіл чергового воїна, направився у сторону першого.\n"
              "Поєдинок був запеклим, однак у результаті Саймон кинув на поле бою голову\n" 
              "короля Кетерфільда. Воїни, побачивши це, опустили свою зброю і кинулися втікати.\n"
              "Після бою Саймона визнали героєм Греббергу.")
        input(">>> ")
        print("На бенкеті Саймон не сидів з усіма. Він багато розмірковував про те, що йому \n"
              "довелося пережити і що ще пережити доведеться. Так він дивився у нічне небо і,\n"
              "здавалося, що воно посміхається йому.\n")

#===< Complete Game >===#

def main():
    """
    У даній функції викликаються усі попередні функції,
    таким чином формуючи повноцінну гру.
    У кінці гри гравцеві пропонується перепройти її.
    Якщо відповідь ствердна, функція викликає сама себе,
    починаючи гру заново

    >>> ...
        Дякую за гру! Бажаєте зіграти ще раз?
        >>> Так
        ...
    """
    introduction()
    first_act()
    second_act()
    third_act()
    adventure = input("Дякую за гру! Бажаєте зіграти ще раз?\n>>> ")
    if adventure == "Так":
        main()
    else:
        print("Сподіваюсь ви гарно провели час :)\n"
              "До зустрічі!")

#===< Play the Game >===#

main()
