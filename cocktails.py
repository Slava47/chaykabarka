"""
Данные о коктейлях бара Ли Бо.
"""

COLD_COCKTAILS = [
    {
        "name": "Банановое молоко",
        "description": "Сладкий, легкий, фруктовый, тягучий, мягкий.",
        "ingredients": "Молочный улун, османтус, банан",
        "price": 230,
        "image": "bananovoe_moloko",
        "tags": {"taste": "sweet", "tea": "more", "strength": "soft"},
    },
    {
        "name": "Лиловая гуанинь",
        "description": "Освежающий, с кислинкой, цветочный, легкий.",
        "ingredients": "Те Гуанинь, лаванда, мята, лайм, лимон",
        "price": 260,
        "image": "lilovaya_guanin",
        "tags": {"taste": "sour_sweet", "tea": "more", "strength": "soft"},
    },
    {
        "name": "Старый князь",
        "description": "Крепкий, забористый, классический, цитрусовый, яркий.",
        "ingredients": "Шу-пуэр, апельсин, орхидея",
        "price": 340,
        "image": "stariy_knyaz",
        "tags": {"taste": "sour_sweet", "tea": "more", "strength": "strong"},
    },
    {
        "name": "Нефритовая река",
        "description": "Десертный, тягучий, цитрусовый, дождливый.",
        "ingredients": "Зеленый чай, апельсин, лимон, мелисса",
        "price": 430,
        "image": "nefritovaya_reka",
        "tags": {"taste": "sweet", "tea": "more", "strength": "soft"},
    },
    {
        "name": "Золотая обезьяна",
        "description": "Сладковато-пряный, десертный, терпкий и фруктовый.",
        "ingredients": "Красный чай, корица, груша, матэ",
        "price": 340,
        "image": "zolotaya_obezyana",
        "tags": {"taste": "sweet", "tea": "more", "strength": "soft"},
    },
    {
        "name": "Тайваньские пираты",
        "description": "Насыщенный, необычный, ягодный, тягучий, крепкий, темный.",
        "ingredients": "Лиу Пао, малина, лимон",
        "price": 470,
        "image": "tayvanskie_piraty",
        "tags": {"taste": "sour_sweet", "tea": "more", "strength": "strong"},
    },
    {
        "name": "Аметистовое вино",
        "description": "Космический, свежий, тайский, пикантный, с нежной кислинкой.",
        "ingredients": "Клитория, лимон, мята",
        "price": 320,
        "image": "ametistovoe_vino",
        "tags": {"taste": "sour", "tea": "less", "strength": "soft"},
    },
    {
        "name": "Сестрицы мэй",
        "description": "Ягодный, яркий, взрывной, с кислинкой, цветочно-садовый.",
        "ingredients": "Те Гуанинь, роза, мята, базилик",
        "price": 360,
        "image": "sestricy_mey",
        "tags": {"taste": "sour_sweet", "tea": "more", "strength": "soft"},
    },
    {
        "name": "Южный феникс",
        "description": "Насыщенный, фруктовый, необычный, бодрящий, ореховый.",
        "ingredients": "Дан Цхун, банан, апельсин",
        "price": 500,
        "image": "yuzhniy_feniks",
        "tags": {"taste": "sweet", "tea": "more", "strength": "strong"},
    },
    {
        "name": "Цветы и птицы Сюй Вэя",
        "description": "Освежающий, цветочный, с тонкой сладкой ноткой.",
        "ingredients": "Те Гуанинь, мята, сакура",
        "price": 320,
        "image": "cvety_i_pticy",
        "tags": {"taste": "sweet", "tea": "more", "strength": "soft"},
    },
    {
        "name": "Гроздья ягод бытия",
        "description": "Ягодный, текстурный, светлый, с легчайшей терпчинкой.",
        "ingredients": "Зеленый чай, клубника, базилик",
        "price": 430,
        "image": "grozdya_yagod",
        "tags": {"taste": "sour_sweet", "tea": "more", "strength": "soft"},
    },
]

HOT_COCKTAILS = [
    {
        "name": "Без тревог",
        "description": "Чистый, сладостный, фруктовый, успокаивающий.",
        "ingredients": "Габа-улун, брусника, мед",
        "price": 350,
        "image": "bez_trevog",
        "tags": {"taste": "sweet", "tea": "more", "strength": "soft"},
    },
    {
        "name": "Сычуаньские перцы",
        "description": "Острый, сытный, коньячный.",
        "ingredients": "Шу-пуэр, кокосовый экстракт, смесь перцев",
        "price": 310,
        "image": "sychuanskie_percy",
        "tags": {"taste": "sour", "tea": "more", "strength": "strong"},
    },
    {
        "name": "Красная обезьяна",
        "description": "Восточный, десертный, сладкий, глубокий.",
        "ingredients": "Красный чай, матэ, пряности, облепиха",
        "price": 320,
        "image": "krasnaya_obezyana",
        "tags": {"taste": "sweet", "tea": "more", "strength": "soft"},
    },
    {
        "name": "Чутка киселе",
        "description": "Сладкий, фруктовый, согревающий, новогодний.",
        "ingredients": "Красный чай, грейпфрут",
        "price": 320,
        "image": "chutka_kisele",
        "tags": {"taste": "sweet", "tea": "less", "strength": "soft"},
    },
    {
        "name": "Горячая свинюшка",
        "description": "Копченый, десертный, неожиданный.",
        "ingredients": "Хей Чха, смесь перцев, кленовый сироп",
        "price": 490,
        "image": "goryachaya_svinyushka",
        "tags": {"taste": "sweet", "tea": "more", "strength": "strong"},
    },
    {
        "name": "Правила Чэн Ай Сао",
        "description": "Плотный, тактильный, темный, фруктовый, пиратский.",
        "ingredients": "Лиу Пао, малина, лимон",
        "price": 470,
        "image": "pravila_chen_ay_sao",
        "tags": {"taste": "sour_sweet", "tea": "more", "strength": "strong"},
    },
    {
        "name": "Лунный апельсин",
        "description": "Дымный, терпкий, пряный, цитрусовый.",
        "ingredients": "Шэн-пуэр, апельсин, корица",
        "price": 380,
        "image": "lunniy_apelsin",
        "tags": {"taste": "sour", "tea": "more", "strength": "strong"},
    },
    {
        "name": "Еще киселе",
        "description": "Яркий, кисло-сладкий, на вкус как лето.",
        "ingredients": "Те Гуаньинь, грейпфрут, апельсин",
        "price": 390,
        "image": "eshe_kisele",
        "tags": {"taste": "sour_sweet", "tea": "more", "strength": "soft"},
    },
    {
        "name": "Осенняя дымка",
        "description": "Насыщенный, фруктовый, необычный, бодрящий, ореховый.",
        "ingredients": "Као-улун, тыква, пряник, молоко",
        "price": 420,
        "image": "osennyaya_dymka",
        "tags": {"taste": "sweet", "tea": "less", "strength": "soft"},
    },
    {
        "name": "Полночь в саду",
        "description": "Тягучий, плотный, молочный, сладкий, уютный.",
        "ingredients": "Шу-пуэр, шоколад, банан, молоко",
        "price": 320,
        "image": "polnoch_v_sadu",
        "tags": {"taste": "sweet", "tea": "less", "strength": "soft"},
    },
    {
        "name": "Чукинский экспресс",
        "description": "Сладкий, фруктовый, согревающий, новогодний.",
        "ingredients": "Шу-пуэр, молоко, кленовый сироп, апельсин, имбирь",
        "price": 430,
        "image": "chukinskiy_ekspress",
        "tags": {"taste": "sweet", "tea": "more", "strength": "soft"},
    },
]

ALCOHOLIC_COCKTAILS = [
    {
        "name": "Биси",
        "description": "Алкогольный коктейль на основе чая.",
        "ingredients": "Те гуаньинь, роза, мята, базилик, можжевельник",
        "price": 550,
        "image": "bisi",
        "tags": {"taste": "sour_sweet", "tea": "more", "strength": "strong"},
    },
    {
        "name": "Яцзы",
        "description": "Алкогольный коктейль на основе чая.",
        "ingredients": "Лиу пао, лимон, малина, тростник",
        "price": 550,
        "image": "yaczi",
        "tags": {"taste": "sour_sweet", "tea": "more", "strength": "strong"},
    },
    {
        "name": "Чивэнь",
        "description": "Алкогольный коктейль на основе чая.",
        "ingredients": "Клитория, лимон, мята, вино",
        "price": 550,
        "image": "chiven",
        "tags": {"taste": "sour", "tea": "less", "strength": "soft"},
    },
    {
        "name": "Цуню",
        "description": "Алкогольный коктейль на основе чая.",
        "ingredients": "Дан цхун, вишня, роза, можжевельник",
        "price": 550,
        "image": "cunyu",
        "tags": {"taste": "sweet", "tea": "more", "strength": "strong"},
    },
    {
        "name": "Чаофэн",
        "description": "Алкогольный коктейль на основе чая.",
        "ingredients": "Зеленый чай, яблоко, лимон, блю курасао, можжевельник",
        "price": 550,
        "image": "chaofeng",
        "tags": {"taste": "sour_sweet", "tea": "less", "strength": "strong"},
    },
    {
        "name": "Цзяоту",
        "description": "Алкогольный коктейль на основе чая.",
        "ingredients": "Красный чай, вишня",
        "price": 550,
        "image": "czyaotu",
        "tags": {"taste": "sweet", "tea": "more", "strength": "soft"},
    },
    {
        "name": "Пулао",
        "description": "Алкогольный коктейль на основе чая.",
        "ingredients": "Да Хун Пао, лимон, малина, можжевельник",
        "price": 550,
        "image": "pulao",
        "tags": {"taste": "sour_sweet", "tea": "more", "strength": "strong"},
    },
    {
        "name": "Биань",
        "description": "Алкогольный коктейль на основе чая.",
        "ingredients": "Дан цхун, апельсин, имбирь, лимон, можжевельник",
        "price": 550,
        "image": "bian",
        "tags": {"taste": "sour", "tea": "more", "strength": "strong"},
    },
    {
        "name": "Суаньни",
        "description": "Алкогольный коктейль на основе чая.",
        "ingredients": "Да хун пао, шоколадное печенье, сгущенное молоко, тростник",
        "price": 550,
        "image": "suanni",
        "tags": {"taste": "sweet", "tea": "less", "strength": "soft"},
    },
]


def get_all_cocktails():
    """Возвращает все коктейли."""
    return COLD_COCKTAILS + HOT_COCKTAILS + ALCOHOLIC_COCKTAILS


def get_category_name(category: str) -> str:
    names = {
        "cold": "Холодные безалкогольные",
        "hot": "Горячие безалкогольные",
        "alcoholic": "Алкогольные",
    }
    return names.get(category, category)


def get_cocktails_by_category(category: str) -> list:
    mapping = {
        "cold": COLD_COCKTAILS,
        "hot": HOT_COCKTAILS,
        "alcoholic": ALCOHOLIC_COCKTAILS,
    }
    return mapping.get(category, [])


def match_cocktails(answers: dict) -> list:
    """
    Подбирает коктейли на основе ответов пользователя.
    Возвращает топ-3 наиболее подходящих.
    """
    is_alcoholic = answers.get("alcoholic") == "yes"
    temperature = answers.get("temperature")  # cold / hot / any
    taste = answers.get("taste")  # sweet / sour_sweet / sour
    tea = answers.get("tea_strength")  # more / less
    strength = answers.get("strength")  # strong / soft

    if is_alcoholic:
        pool = list(ALCOHOLIC_COCKTAILS)
    else:
        if temperature == "cold":
            pool = list(COLD_COCKTAILS)
        elif temperature == "hot":
            pool = list(HOT_COCKTAILS)
        else:
            pool = list(COLD_COCKTAILS) + list(HOT_COCKTAILS)

    scored = []
    for c in pool:
        score = 0
        tags = c.get("tags", {})
        if taste and tags.get("taste") == taste:
            score += 2
        if tea and tags.get("tea") == tea:
            score += 1
        if strength and tags.get("strength") == strength:
            score += 1
        scored.append((score, c))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [item[1] for item in scored[:3]]
