from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

restaurants = [
    {
        "id": 1,
        "name": "Arsalan",
        "emoji": "🍚",
        "cuisine": "Biryani • Mughlai",
        "rating": 4.5,
        "time": "30-40",
        "price": "₹400",
        "offer": "20% OFF",
        "score": 95,
        "moods": ["comfort", "happy"],
        "cats": ["biryani", "mughlai"]
    },
    {
        "id": 2,
        "name": "Peter Cat",
        "emoji": "🍗",
        "cuisine": "Continental • Mughlai",
        "rating": 4.6,
        "time": "30-40",
        "price": "₹800",
        "offer": "",
        "score": 92,
        "moods": ["romantic"],
        "cats": ["continental", "kebab"]
    },
    {
        "id": 3,
        "name": "Flurys",
        "emoji": "🍰",
        "cuisine": "Desserts • Bakery • Continental",
        "rating": 4.7,
        "time": "20-30",
        "price": "₹500",
        "offer": "",
        "score": 93,
        "moods": ["happy"],
        "cats": ["desserts", "bakery", "breakfast"]
    },
    {
        "id": 4,
        "name": "Kwality",
        "emoji": "🍨",
        "cuisine": "Ice Cream • Desserts",
        "rating": 4.4,
        "time": "15-25",
        "price": "₹300",
        "offer": "10% OFF",
        "score": 88,
        "moods": ["happy"],
        "cats": ["desserts", "ice cream"]
    },
    {
        "id": 5,
        "name": "Mocambo",
        "emoji": "🥩",
        "cuisine": "Continental • American",
        "rating": 4.5,
        "time": "35-45",
        "price": "₹900",
        "offer": "",
        "score": 91,
        "moods": ["romantic", "comfort"],
        "cats": ["continental", "steak"]
    },
    {
        "id": 6,
        "name": "Bar-B-Q",
        "emoji": "🔥",
        "cuisine": "Chinese • Mughlai",
        "rating": 4.3,
        "time": "30-40",
        "price": "₹600",
        "offer": "15% OFF",
        "score": 87,
        "moods": ["comfort"],
        "cats": ["chinese", "kebab"]
    },
    {
        "id": 7,
        "name": "Shiraz Golden Restaurant",
        "emoji": "🍛",
        "cuisine": "Biryani • Mughlai",
        "rating": 4.4,
        "time": "30-40",
        "price": "₹350",
        "offer": "20% OFF",
        "score": 89,
        "moods": ["comfort", "happy"],
        "cats": ["biryani", "mughlai"]
    },
    {
        "id": 8,
        "name": "Kewpie's Kitchen",
        "emoji": "🍲",
        "cuisine": "Bengali",
        "rating": 4.6,
        "time": "35-45",
        "price": "₹700",
        "offer": "",
        "score": 94,
        "moods": ["comfort", "romantic"],
        "cats": ["bengali"]
    },
    {
        "id": 9,
        "name": "Oh! Calcutta",
        "emoji": "🐟",
        "cuisine": "Bengali • Seafood",
        "rating": 4.5,
        "time": "40-50",
        "price": "₹1000",
        "offer": "",
        "score": 93,
        "moods": ["romantic"],
        "cats": ["bengali", "seafood"]
    },
    {
        "id": 10,
        "name": "6 Ballygunge Place",
        "emoji": "🍽️",
        "cuisine": "Bengali",
        "rating": 4.7,
        "time": "40-50",
        "price": "₹900",
        "offer": "",
        "score": 95,
        "moods": ["romantic", "comfort"],
        "cats": ["bengali"]
    },
    {
        "id": 11,
        "name": "Mainland China",
        "emoji": "🥢",
        "cuisine": "Chinese",
        "rating": 4.4,
        "time": "35-45",
        "price": "₹1000",
        "offer": "10% OFF",
        "score": 90,
        "moods": ["romantic"],
        "cats": ["chinese"]
    },
    {
        "id": 12,
        "name": "Aminia",
        "emoji": "🍚",
        "cuisine": "Biryani • Mughlai",
        "rating": 4.3,
        "time": "25-35",
        "price": "₹300",
        "offer": "15% OFF",
        "score": 86,
        "moods": ["comfort"],
        "cats": ["biryani", "mughlai"]
    },
    {
        "id": 13,
        "name": "The Oberoi Grand",
        "emoji": "👑",
        "cuisine": "Multi-Cuisine • Fine Dining",
        "rating": 4.8,
        "time": "45-60",
        "price": "₹2500",
        "offer": "",
        "score": 98,
        "moods": ["romantic"],
        "cats": ["fine dining", "continental", "bengali"]
    },
    {
        "id": 14,
        "name": "Barbeque Nation",
        "emoji": "🍖",
        "cuisine": "BBQ • Grill • Multi-Cuisine",
        "rating": 4.2,
        "time": "40-50",
        "price": "₹1200",
        "offer": "25% OFF",
        "score": 85,
        "moods": ["happy", "comfort"],
        "cats": ["bbq", "grill"]
    },
    {
        "id": 15,
        "name": "Zeeshan",
        "emoji": "🥘",
        "cuisine": "Biryani • Mughlai",
        "rating": 4.4,
        "time": "30-40",
        "price": "₹400",
        "offer": "20% OFF",
        "score": 88,
        "moods": ["comfort"],
        "cats": ["biryani", "mughlai"]
    },
    {
        "id": 16,
        "name": "Banana Leaf",
        "emoji": "🍌",
        "cuisine": "South Indian",
        "rating": 4.3,
        "time": "25-35",
        "price": "₹400",
        "offer": "10% OFF",
        "score": 86,
        "moods": ["comfort", "happy"],
        "cats": ["south indian"]
    },
    {
        "id": 17,
        "name": "Pice Hotel",
        "emoji": "🍛",
        "cuisine": "Bengali",
        "rating": 4.2,
        "time": "20-30",
        "price": "₹200",
        "offer": "",
        "score": 84,
        "moods": ["comfort"],
        "cats": ["bengali"]
    },
    {
        "id": 18,
        "name": "Oudh 1590",
        "emoji": "🏺",
        "cuisine": "Awadhi • Mughlai",
        "rating": 4.6,
        "time": "40-50",
        "price": "₹1200",
        "offer": "",
        "score": 94,
        "moods": ["romantic", "comfort"],
        "cats": ["mughlai", "awadhi"]
    },
    {
        "id": 19,
        "name": "Trincas",
        "emoji": "🎵",
        "cuisine": "Continental • Indian",
        "rating": 4.3,
        "time": "30-40",
        "price": "₹700",
        "offer": "",
        "score": 87,
        "moods": ["romantic"],
        "cats": ["continental"]
    },
    {
        "id": 20,
        "name": "Nizam's",
        "emoji": "🌯",
        "cuisine": "Kathi Roll • Mughlai",
        "rating": 4.5,
        "time": "15-25",
        "price": "₹200",
        "offer": "",
        "score": 92,
        "moods": ["comfort", "happy"],
        "cats": ["kathi roll", "street food"]
    },
    {
        "id": 21,
        "name": "Bohemian",
        "emoji": "🎨",
        "cuisine": "Bengali Fusion",
        "rating": 4.5,
        "time": "35-45",
        "price": "₹1000",
        "offer": "",
        "score": 92,
        "moods": ["romantic"],
        "cats": ["bengali", "fusion"]
    },
    {
        "id": 22,
        "name": "Haka",
        "emoji": "🍜",
        "cuisine": "Chinese",
        "rating": 4.4,
        "time": "30-40",
        "price": "₹800",
        "offer": "10% OFF",
        "score": 89,
        "moods": ["comfort"],
        "cats": ["chinese"]
    },
    {
        "id": 23,
        "name": "Momo I Am",
        "emoji": "🥟",
        "cuisine": "Momos • Tibetan",
        "rating": 4.3,
        "time": "20-30",
        "price": "₹300",
        "offer": "15% OFF",
        "score": 86,
        "moods": ["happy", "comfort"],
        "cats": ["momos", "tibetan"]
    },
    {
        "id": 24,
        "name": "Saptapadi",
        "emoji": "🍽️",
        "cuisine": "Bengali",
        "rating": 4.4,
        "time": "35-45",
        "price": "₹800",
        "offer": "",
        "score": 90,
        "moods": ["romantic", "comfort"],
        "cats": ["bengali"]
    },
    {
        "id": 25,
        "name": "Tung Fong",
        "emoji": "🥡",
        "cuisine": "Chinese",
        "rating": 4.2,
        "time": "25-35",
        "price": "₹500",
        "offer": "20% OFF",
        "score": 85,
        "moods": ["comfort"],
        "cats": ["chinese"]
    },
    {
        "id": 26,
        "name": "Smoke House Deli",
        "emoji": "🥗",
        "cuisine": "Continental • Cafe",
        "rating": 4.4,
        "time": "30-40",
        "price": "₹900",
        "offer": "",
        "score": 89,
        "moods": ["happy", "romantic"],
        "cats": ["continental", "cafe", "salad"]
    },
    {
        "id": 27,
        "name": "The Grid",
        "emoji": "🍔",
        "cuisine": "American • Burgers",
        "rating": 4.3,
        "time": "25-35",
        "price": "₹600",
        "offer": "10% OFF",
        "score": 87,
        "moods": ["happy"],
        "cats": ["burgers", "american"]
    },
    {
        "id": 28,
        "name": "Balwant Singh's Eating House",
        "emoji": "🍵",
        "cuisine": "Punjabi • North Indian",
        "rating": 4.5,
        "time": "20-30",
        "price": "₹250",
        "offer": "",
        "score": 91,
        "moods": ["comfort"],
        "cats": ["north indian", "punjabi"]
    },
    {
        "id": 29,
        "name": "Chung Wah",
        "emoji": "🍱",
        "cuisine": "Chinese",
        "rating": 4.3,
        "time": "30-40",
        "price": "₹600",
        "offer": "",
        "score": 86,
        "moods": ["comfort"],
        "cats": ["chinese"]
    },
    {
        "id": 30,
        "name": "Cafe Mezzuna",
        "emoji": "☕",
        "cuisine": "Italian • Continental • Cafe",
        "rating": 4.3,
        "time": "30-40",
        "price": "₹800",
        "offer": "15% OFF",
        "score": 87,
        "moods": ["romantic", "happy"],
        "cats": ["italian", "cafe", "pasta"]
    },
    {
        "id": 31,
        "name": "The Bhoj Company",
        "emoji": "🍛",
        "cuisine": "North Indian • Rajasthani",
        "rating": 4.4,
        "time": "30-40",
        "price": "₹600",
        "offer": "20% OFF",
        "score": 88,
        "moods": ["comfort", "happy"],
        "cats": ["north indian", "thali"]
    },
    {
        "id": 32,
        "name": "Tasca",
        "emoji": "🥩",
        "cuisine": "Continental • Steakhouse",
        "rating": 4.5,
        "time": "40-50",
        "price": "₹1500",
        "offer": "",
        "score": 91,
        "moods": ["romantic"],
        "cats": ["continental", "steak"]
    },
    {
        "id": 33,
        "name": "Mitra Cafe",
        "emoji": "🍳",
        "cuisine": "Breakfast • Continental",
        "rating": 4.4,
        "time": "20-30",
        "price": "₹300",
        "offer": "",
        "score": 89,
        "moods": ["happy", "comfort"],
        "cats": ["breakfast", "cafe"]
    },
    {
        "id": 34,
        "name": "Aaheli",
        "emoji": "🐠",
        "cuisine": "Bengali",
        "rating": 4.6,
        "time": "40-50",
        "price": "₹1100",
        "offer": "",
        "score": 94,
        "moods": ["romantic", "comfort"],
        "cats": ["bengali", "seafood"]
    },
    {
        "id": 35,
        "name": "Peerless Inn",
        "emoji": "🍽️",
        "cuisine": "Multi-Cuisine",
        "rating": 4.3,
        "time": "35-45",
        "price": "₹800",
        "offer": "10% OFF",
        "score": 86,
        "moods": ["romantic"],
        "cats": ["multi-cuisine"]
    },
    {
        "id": 36,
        "name": "Bhojo Hori Manna",
        "emoji": "🍲",
        "cuisine": "Bengali",
        "rating": 4.5,
        "time": "30-40",
        "price": "₹500",
        "offer": "",
        "score": 92,
        "moods": ["comfort", "happy"],
        "cats": ["bengali"]
    },
    {
        "id": 37,
        "name": "Marco Polo",
        "emoji": "🍕",
        "cuisine": "Italian • Pizza",
        "rating": 4.2,
        "time": "30-40",
        "price": "₹700",
        "offer": "15% OFF",
        "score": 85,
        "moods": ["happy"],
        "cats": ["italian", "pizza"]
    },
    {
        "id": 38,
        "name": "Olypub",
        "emoji": "🍺",
        "cuisine": "Continental • Pub Grub",
        "rating": 4.3,
        "time": "30-40",
        "price": "₹600",
        "offer": "",
        "score": 87,
        "moods": ["happy"],
        "cats": ["continental", "pub grub"]
    },
    {
        "id": 39,
        "name": "Spice Kraft",
        "emoji": "🌶️",
        "cuisine": "Indian Fusion",
        "rating": 4.4,
        "time": "35-45",
        "price": "₹900",
        "offer": "10% OFF",
        "score": 89,
        "moods": ["romantic", "happy"],
        "cats": ["fusion", "north indian"]
    },
    {
        "id": 40,
        "name": "Cafe Coffee Day Square",
        "emoji": "☕",
        "cuisine": "Cafe • Snacks",
        "rating": 4.0,
        "time": "15-25",
        "price": "₹300",
        "offer": "20% OFF",
        "score": 80,
        "moods": ["happy"],
        "cats": ["cafe", "snacks"]
    },
    {
        "id": 41,
        "name": "The Yellow Chilli",
        "emoji": "🌽",
        "cuisine": "North Indian",
        "rating": 4.2,
        "time": "30-40",
        "price": "₹700",
        "offer": "15% OFF",
        "score": 84,
        "moods": ["comfort"],
        "cats": ["north indian"]
    },
    {
        "id": 42,
        "name": "Zaffran",
        "emoji": "🏵️",
        "cuisine": "Mughlai • North Indian",
        "rating": 4.4,
        "time": "35-45",
        "price": "₹800",
        "offer": "",
        "score": 89,
        "moods": ["romantic", "comfort"],
        "cats": ["mughlai", "north indian"]
    },
    {
        "id": 43,
        "name": "Raj's Spanish Cafe",
        "emoji": "🥘",
        "cuisine": "Spanish • Continental",
        "rating": 4.3,
        "time": "30-40",
        "price": "₹700",
        "offer": "",
        "score": 86,
        "moods": ["romantic"],
        "cats": ["spanish", "continental"]
    },
    {
        "id": 44,
        "name": "Suruchi",
        "emoji": "🐟",
        "cuisine": "Bengali",
        "rating": 4.5,
        "time": "30-40",
        "price": "₹600",
        "offer": "",
        "score": 91,
        "moods": ["comfort"],
        "cats": ["bengali", "seafood"]
    },
    {
        "id": 45,
        "name": "Amber",
        "emoji": "🍗",
        "cuisine": "Mughlai • Continental",
        "rating": 4.4,
        "time": "35-45",
        "price": "₹700",
        "offer": "10% OFF",
        "score": 88,
        "moods": ["romantic", "comfort"],
        "cats": ["mughlai", "continental"]
    },
    {
        "id": 46,
        "name": "Rôtisserie by Saby",
        "emoji": "🥗",
        "cuisine": "French • Continental",
        "rating": 4.5,
        "time": "40-50",
        "price": "₹1400",
        "offer": "",
        "score": 92,
        "moods": ["romantic"],
        "cats": ["french", "continental"]
    },
    {
        "id": 47,
        "name": "Cafe Ozora",
        "emoji": "🌿",
        "cuisine": "Cafe • Continental",
        "rating": 4.3,
        "time": "25-35",
        "price": "₹500",
        "offer": "10% OFF",
        "score": 85,
        "moods": ["happy"],
        "cats": ["cafe", "continental"]
    },
    {
        "id": 48,
        "name": "Dumplings",
        "emoji": "🥟",
        "cuisine": "Chinese • Tibetan",
        "rating": 4.3,
        "time": "20-30",
        "price": "₹350",
        "offer": "20% OFF",
        "score": 86,
        "moods": ["happy", "comfort"],
        "cats": ["chinese", "momos"]
    },
    {
        "id": 49,
        "name": "Rajbhog",
        "emoji": "🍮",
        "cuisine": "Sweets • Snacks",
        "rating": 4.6,
        "time": "15-25",
        "price": "₹200",
        "offer": "",
        "score": 93,
        "moods": ["happy"],
        "cats": ["sweets", "snacks"]
    },
    {
        "id": 50,
        "name": "Sree Annapurna",
        "emoji": "🍱",
        "cuisine": "South Indian • North Indian",
        "rating": 4.3,
        "time": "25-35",
        "price": "₹350",
        "offer": "10% OFF",
        "score": 86,
        "moods": ["comfort"],
        "cats": ["south indian", "north indian", "thali"]
    },
]

foods = [
    # ── Arsalan (id 1) ──────────────────────────────────────────────────
    {"id": 101, "name": "Chicken Biryani", "emoji": "🍚", "restaurant": "Arsalan", "price": 299, "rating": 4.6, "desc": "Kolkata style biryani with potato.", "veg": False, "moods": ["comfort", "happy"], "cats": ["biryani"]},
    {"id": 102, "name": "Mutton Biryani", "emoji": "🍚", "restaurant": "Arsalan", "price": 349, "rating": 4.7, "desc": "Slow-cooked mutton biryani Kolkata style.", "veg": False, "moods": ["comfort"], "cats": ["biryani"]},
    {"id": 103, "name": "Chicken Rezala", "emoji": "🍗", "restaurant": "Arsalan", "price": 280, "rating": 4.5, "desc": "Tender chicken in white Mughlai gravy.", "veg": False, "moods": ["comfort"], "cats": ["mughlai"]},
    {"id": 104, "name": "Mutton Rezala", "emoji": "🍖", "restaurant": "Arsalan", "price": 330, "rating": 4.6, "desc": "Mutton cooked in yoghurt and spice gravy.", "veg": False, "moods": ["comfort", "romantic"], "cats": ["mughlai"]},
    {"id": 105, "name": "Chicken Chaap", "emoji": "🍗", "restaurant": "Arsalan", "price": 260, "rating": 4.5, "desc": "Rich Mughlai style chicken chaap.", "veg": False, "moods": ["comfort"], "cats": ["mughlai"]},
    {"id": 106, "name": "Seekh Kebab", "emoji": "🍢", "restaurant": "Arsalan", "price": 220, "rating": 4.4, "desc": "Minced mutton seekh grilled on skewers.", "veg": False, "moods": ["happy"], "cats": ["kebab"]},
    {"id": 107, "name": "Egg Biryani", "emoji": "🥚", "restaurant": "Arsalan", "price": 199, "rating": 4.3, "desc": "Light egg biryani Kolkata style.", "veg": False, "moods": ["comfort"], "cats": ["biryani"]},
    {"id": 108, "name": "Firni", "emoji": "🍮", "restaurant": "Arsalan", "price": 80, "rating": 4.5, "desc": "Chilled rice flour pudding with saffron.", "veg": True, "moods": ["happy"], "cats": ["desserts"]},

    # ── Peter Cat (id 2) ────────────────────────────────────────────────
    {"id": 201, "name": "Chelo Kebab", "emoji": "🍗", "restaurant": "Peter Cat", "price": 450, "rating": 4.7, "desc": "Legendary Kolkata kebab platter.", "veg": False, "moods": ["romantic"], "cats": ["kebab", "continental"]},
    {"id": 202, "name": "Chicken Stroganoff", "emoji": "🍛", "restaurant": "Peter Cat", "price": 420, "rating": 4.5, "desc": "Creamy classic Russian-style chicken.", "veg": False, "moods": ["romantic", "comfort"], "cats": ["continental"]},
    {"id": 203, "name": "Prawn Cocktail", "emoji": "🍤", "restaurant": "Peter Cat", "price": 350, "rating": 4.4, "desc": "Chilled prawns in tangy cocktail sauce.", "veg": False, "moods": ["romantic"], "cats": ["seafood", "continental"]},
    {"id": 204, "name": "Grilled Fish", "emoji": "🐟", "restaurant": "Peter Cat", "price": 480, "rating": 4.5, "desc": "Basa fillet grilled with herb butter.", "veg": False, "moods": ["romantic"], "cats": ["seafood"]},
    {"id": 205, "name": "Sizzling Brownie", "emoji": "🍫", "restaurant": "Peter Cat", "price": 180, "rating": 4.8, "desc": "Hot brownie on a sizzler plate with ice cream.", "veg": True, "moods": ["happy"], "cats": ["desserts"]},
    {"id": 206, "name": "Mutton Chops", "emoji": "🍖", "restaurant": "Peter Cat", "price": 500, "rating": 4.6, "desc": "Pan-fried mutton chops with gravy.", "veg": False, "moods": ["romantic"], "cats": ["continental"]},

    # ── Flurys (id 3) ───────────────────────────────────────────────────
    {"id": 301, "name": "Chocolate Pastry", "emoji": "🍰", "restaurant": "Flurys", "price": 180, "rating": 4.8, "desc": "Classic Park Street pastry.", "veg": True, "moods": ["happy"], "cats": ["desserts", "bakery"]},
    {"id": 302, "name": "English Breakfast", "emoji": "🍳", "restaurant": "Flurys", "price": 320, "rating": 4.7, "desc": "Full English with eggs, beans, and toast.", "veg": False, "moods": ["happy", "comfort"], "cats": ["breakfast"]},
    {"id": 303, "name": "Strawberry Tart", "emoji": "🍓", "restaurant": "Flurys", "price": 160, "rating": 4.6, "desc": "Fresh strawberries on crème pâtissière tart.", "veg": True, "moods": ["happy", "romantic"], "cats": ["desserts", "bakery"]},
    {"id": 304, "name": "Club Sandwich", "emoji": "🥪", "restaurant": "Flurys", "price": 280, "rating": 4.5, "desc": "Triple-decker toasted club sandwich.", "veg": False, "moods": ["happy"], "cats": ["snacks"]},
    {"id": 305, "name": "Darjeeling Tea", "emoji": "🍵", "restaurant": "Flurys", "price": 90, "rating": 4.8, "desc": "First flush Darjeeling served in a pot.", "veg": True, "moods": ["happy", "comfort"], "cats": ["beverages"]},
    {"id": 306, "name": "Éclair", "emoji": "🍫", "restaurant": "Flurys", "price": 120, "rating": 4.7, "desc": "Choux pastry filled with cream and glazed.", "veg": True, "moods": ["happy"], "cats": ["desserts", "bakery"]},
    {"id": 307, "name": "Chicken Patty", "emoji": "🥐", "restaurant": "Flurys", "price": 110, "rating": 4.5, "desc": "Flaky pastry with spiced chicken filling.", "veg": False, "moods": ["happy"], "cats": ["snacks", "bakery"]},

    # ── Kwality (id 4) ──────────────────────────────────────────────────
    {"id": 401, "name": "Royal Falooda", "emoji": "🍨", "restaurant": "Kwality", "price": 150, "rating": 4.5, "desc": "Rose syrup falooda with ice cream and basil seeds.", "veg": True, "moods": ["happy"], "cats": ["desserts", "ice cream"]},
    {"id": 402, "name": "Butterscotch Sundae", "emoji": "🍦", "restaurant": "Kwality", "price": 130, "rating": 4.4, "desc": "Butterscotch ice cream with praline crunch.", "veg": True, "moods": ["happy"], "cats": ["ice cream"]},
    {"id": 403, "name": "Mango Kulfi", "emoji": "🥭", "restaurant": "Kwality", "price": 110, "rating": 4.6, "desc": "Alphonso mango kulfi on a stick.", "veg": True, "moods": ["happy"], "cats": ["ice cream", "desserts"]},
    {"id": 404, "name": "Brownie with Ice Cream", "emoji": "🍫", "restaurant": "Kwality", "price": 160, "rating": 4.7, "desc": "Warm brownie with vanilla scoop.", "veg": True, "moods": ["happy", "comfort"], "cats": ["desserts"]},

    # ── Mocambo (id 5) ──────────────────────────────────────────────────
    {"id": 501, "name": "Prawn Thermidor", "emoji": "🦐", "restaurant": "Mocambo", "price": 650, "rating": 4.6, "desc": "Classic prawn thermidor in butter sauce.", "veg": False, "moods": ["romantic"], "cats": ["seafood", "continental"]},
    {"id": 502, "name": "Chicken a la Kiev", "emoji": "🍗", "restaurant": "Mocambo", "price": 480, "rating": 4.5, "desc": "Butter-stuffed chicken Kiev, deep fried.", "veg": False, "moods": ["romantic", "comfort"], "cats": ["continental"]},
    {"id": 503, "name": "Mushroom Soup", "emoji": "🍄", "restaurant": "Mocambo", "price": 180, "rating": 4.5, "desc": "Cream of mushroom soup with herb croutons.", "veg": True, "moods": ["comfort"], "cats": ["continental", "soup"]},
    {"id": 504, "name": "Beef Steak", "emoji": "🥩", "restaurant": "Mocambo", "price": 720, "rating": 4.7, "desc": "Tenderloin grilled to your liking.", "veg": False, "moods": ["romantic"], "cats": ["steak", "continental"]},
    {"id": 505, "name": "Devilled Crab", "emoji": "🦀", "restaurant": "Mocambo", "price": 580, "rating": 4.5, "desc": "Spiced crab in shell, baked.", "veg": False, "moods": ["romantic"], "cats": ["seafood"]},

    # ── Bar-B-Q (id 6) ──────────────────────────────────────────────────
    {"id": 601, "name": "BBQ Chicken", "emoji": "🔥", "restaurant": "Bar-B-Q", "price": 320, "rating": 4.4, "desc": "Smoky BBQ half chicken, char-grilled.", "veg": False, "moods": ["comfort", "happy"], "cats": ["bbq", "grill"]},
    {"id": 602, "name": "Dragon Chicken", "emoji": "🐉", "restaurant": "Bar-B-Q", "price": 280, "rating": 4.3, "desc": "Crispy fried chicken in chilli sauce.", "veg": False, "moods": ["happy"], "cats": ["chinese"]},
    {"id": 603, "name": "Chicken Fried Rice", "emoji": "🍳", "restaurant": "Bar-B-Q", "price": 200, "rating": 4.2, "desc": "Wok-tossed egg fried rice with chicken.", "veg": False, "moods": ["comfort"], "cats": ["chinese"]},
    {"id": 604, "name": "Tangra Prawn", "emoji": "🦐", "restaurant": "Bar-B-Q", "price": 380, "rating": 4.4, "desc": "Tangra-style chilli garlic prawn.", "veg": False, "moods": ["comfort", "happy"], "cats": ["chinese", "seafood"]},
    {"id": 605, "name": "Honey Chilli Potato", "emoji": "🍟", "restaurant": "Bar-B-Q", "price": 160, "rating": 4.3, "desc": "Crispy potato fingers in honey chilli.", "veg": True, "moods": ["happy"], "cats": ["chinese", "snacks"]},

    # ── Shiraz (id 7) ───────────────────────────────────────────────────
    {"id": 701, "name": "Mutton Biryani", "emoji": "🍚", "restaurant": "Shiraz Golden Restaurant", "price": 320, "rating": 4.5, "desc": "Awadhi-style mutton biryani with aloo.", "veg": False, "moods": ["comfort"], "cats": ["biryani"]},
    {"id": 702, "name": "Chicken Biryani", "emoji": "🍚", "restaurant": "Shiraz Golden Restaurant", "price": 270, "rating": 4.4, "desc": "Fragrant chicken biryani Kolkata-style.", "veg": False, "moods": ["comfort", "happy"], "cats": ["biryani"]},
    {"id": 703, "name": "Mutton Chaap", "emoji": "🍖", "restaurant": "Shiraz Golden Restaurant", "price": 290, "rating": 4.5, "desc": "Slow-cooked mutton chaap, melt-in-mouth.", "veg": False, "moods": ["comfort"], "cats": ["mughlai"]},
    {"id": 704, "name": "Chicken Korma", "emoji": "🍛", "restaurant": "Shiraz Golden Restaurant", "price": 250, "rating": 4.3, "desc": "Mild Mughlai chicken korma.", "veg": False, "moods": ["comfort"], "cats": ["mughlai"]},

    # ── Kewpie's Kitchen (id 8) ─────────────────────────────────────────
    {"id": 801, "name": "Shorshe Ilish", "emoji": "🐟", "restaurant": "Kewpie's Kitchen", "price": 520, "rating": 4.8, "desc": "Hilsa in mustard-poppy seed sauce.", "veg": False, "moods": ["comfort", "romantic"], "cats": ["bengali", "seafood"]},
    {"id": 802, "name": "Chingri Malaikari", "emoji": "🦐", "restaurant": "Kewpie's Kitchen", "price": 480, "rating": 4.7, "desc": "Tiger prawns in coconut milk curry.", "veg": False, "moods": ["romantic"], "cats": ["bengali", "seafood"]},
    {"id": 803, "name": "Aloo Posto", "emoji": "🥔", "restaurant": "Kewpie's Kitchen", "price": 150, "rating": 4.5, "desc": "Potatoes in Bengali poppy seed gravy.", "veg": True, "moods": ["comfort"], "cats": ["bengali"]},
    {"id": 804, "name": "Mishti Doi", "emoji": "🍮", "restaurant": "Kewpie's Kitchen", "price": 90, "rating": 4.7, "desc": "Sweet curd set in earthen pot.", "veg": True, "moods": ["happy"], "cats": ["desserts", "bengali"]},
    {"id": 805, "name": "Kosha Mangsho", "emoji": "🍖", "restaurant": "Kewpie's Kitchen", "price": 420, "rating": 4.8, "desc": "Bengali slow-cooked mutton dry curry.", "veg": False, "moods": ["comfort", "romantic"], "cats": ["bengali"]},

    # ── Oh! Calcutta (id 9) ─────────────────────────────────────────────
    {"id": 901, "name": "Bhetki Paturi", "emoji": "🐠", "restaurant": "Oh! Calcutta", "price": 450, "rating": 4.6, "desc": "Bhetki wrapped in banana leaf, steamed.", "veg": False, "moods": ["romantic"], "cats": ["bengali", "seafood"]},
    {"id": 902, "name": "Dab Chingri", "emoji": "🥥", "restaurant": "Oh! Calcutta", "price": 580, "rating": 4.7, "desc": "Prawns cooked inside tender coconut.", "veg": False, "moods": ["romantic"], "cats": ["bengali", "seafood"]},
    {"id": 903, "name": "Luchi-Alur Dom", "emoji": "🫓", "restaurant": "Oh! Calcutta", "price": 180, "rating": 4.5, "desc": "Bengali puri with spiced dum potato.", "veg": True, "moods": ["comfort", "happy"], "cats": ["bengali"]},
    {"id": 904, "name": "Roshogolla", "emoji": "⚪", "restaurant": "Oh! Calcutta", "price": 80, "rating": 4.8, "desc": "Soft spongy Bengali rasgulla in syrup.", "veg": True, "moods": ["happy"], "cats": ["desserts", "bengali"]},

    # ── 6 Ballygunge Place (id 10) ──────────────────────────────────────
    {"id": 1001, "name": "Mutton Kasha", "emoji": "🍖", "restaurant": "6 Ballygunge Place", "price": 460, "rating": 4.8, "desc": "Rich slow-cooked mutton Bengali style.", "veg": False, "moods": ["comfort", "romantic"], "cats": ["bengali"]},
    {"id": 1002, "name": "Chitol Maacher Muitha", "emoji": "🐟", "restaurant": "6 Ballygunge Place", "price": 390, "rating": 4.7, "desc": "Chitol fish dumplings in light gravy.", "veg": False, "moods": ["romantic"], "cats": ["bengali", "seafood"]},
    {"id": 1003, "name": "Begun Bhaja", "emoji": "🍆", "restaurant": "6 Ballygunge Place", "price": 100, "rating": 4.5, "desc": "Crispy pan-fried aubergine slices.", "veg": True, "moods": ["comfort"], "cats": ["bengali"]},
    {"id": 1004, "name": "Sandesh", "emoji": "🍬", "restaurant": "6 Ballygunge Place", "price": 70, "rating": 4.7, "desc": "Classic Bengali chhena sweet.", "veg": True, "moods": ["happy"], "cats": ["desserts", "bengali"]},
    {"id": 1005, "name": "Doi Maach", "emoji": "🐟", "restaurant": "6 Ballygunge Place", "price": 350, "rating": 4.6, "desc": "Fish in yoghurt-based Bengali sauce.", "veg": False, "moods": ["comfort"], "cats": ["bengali", "seafood"]},

    # ── Mainland China (id 11) ──────────────────────────────────────────
    {"id": 1101, "name": "Dim Sum Platter", "emoji": "🥟", "restaurant": "Mainland China", "price": 380, "rating": 4.5, "desc": "Assorted steamed dim sums.", "veg": False, "moods": ["romantic", "happy"], "cats": ["chinese"]},
    {"id": 1102, "name": "Peking Duck", "emoji": "🦆", "restaurant": "Mainland China", "price": 780, "rating": 4.6, "desc": "Sliced roast duck with pancakes and hoisin.", "veg": False, "moods": ["romantic"], "cats": ["chinese"]},
    {"id": 1103, "name": "Kung Pao Chicken", "emoji": "🌶️", "restaurant": "Mainland China", "price": 380, "rating": 4.4, "desc": "Spicy Sichuan chicken with peanuts.", "veg": False, "moods": ["happy", "comfort"], "cats": ["chinese"]},
    {"id": 1104, "name": "Hot & Sour Soup", "emoji": "🍜", "restaurant": "Mainland China", "price": 200, "rating": 4.4, "desc": "Classic tangy spicy soup.", "veg": False, "moods": ["comfort"], "cats": ["chinese", "soup"]},
    {"id": 1105, "name": "Lotus Stem Stir Fry", "emoji": "🌸", "restaurant": "Mainland China", "price": 290, "rating": 4.3, "desc": "Crispy lotus stem in chilli garlic.", "veg": True, "moods": ["happy"], "cats": ["chinese"]},

    # ── Aminia (id 12) ──────────────────────────────────────────────────
    {"id": 1201, "name": "Mutton Biryani", "emoji": "🍚", "restaurant": "Aminia", "price": 299, "rating": 4.4, "desc": "Aromatic Kolkata mutton biryani.", "veg": False, "moods": ["comfort"], "cats": ["biryani"]},
    {"id": 1202, "name": "Chicken Biryani", "emoji": "🍚", "restaurant": "Aminia", "price": 249, "rating": 4.3, "desc": "Everyday Kolkata chicken biryani.", "veg": False, "moods": ["comfort", "happy"], "cats": ["biryani"]},
    {"id": 1203, "name": "Rezala", "emoji": "🍛", "restaurant": "Aminia", "price": 260, "rating": 4.4, "desc": "White Mughlai gravy with mutton.", "veg": False, "moods": ["comfort"], "cats": ["mughlai"]},

    # ── The Oberoi Grand (id 13) ────────────────────────────────────────
    {"id": 1301, "name": "Bengali Thali", "emoji": "🍱", "restaurant": "The Oberoi Grand", "price": 1800, "rating": 4.9, "desc": "Grand multi-course Bengali meal.", "veg": False, "moods": ["romantic"], "cats": ["bengali", "fine dining"]},
    {"id": 1302, "name": "Lobster Thermidor", "emoji": "🦞", "restaurant": "The Oberoi Grand", "price": 2800, "rating": 4.8, "desc": "Butter-poached lobster in cream sauce.", "veg": False, "moods": ["romantic"], "cats": ["seafood", "continental", "fine dining"]},
    {"id": 1303, "name": "Chocolate Fondant", "emoji": "🍫", "restaurant": "The Oberoi Grand", "price": 650, "rating": 4.9, "desc": "Warm chocolate lava with gold leaf.", "veg": True, "moods": ["romantic", "happy"], "cats": ["desserts", "fine dining"]},

    # ── Barbeque Nation (id 14) ─────────────────────────────────────────
    {"id": 1401, "name": "Live Grill Starters", "emoji": "🍖", "restaurant": "Barbeque Nation", "price": 649, "rating": 4.3, "desc": "Unlimited table-grill starters — chicken, fish, paneer.", "veg": False, "moods": ["happy", "comfort"], "cats": ["bbq", "grill"]},
    {"id": 1402, "name": "Cajun Spice Chicken", "emoji": "🌶️", "restaurant": "Barbeque Nation", "price": 350, "rating": 4.2, "desc": "Chicken marinated in Cajun spices.", "veg": False, "moods": ["happy"], "cats": ["bbq"]},
    {"id": 1403, "name": "Banana Walnut Cake", "emoji": "🍰", "restaurant": "Barbeque Nation", "price": 180, "rating": 4.1, "desc": "Moist banana and walnut dessert cake.", "veg": True, "moods": ["happy"], "cats": ["desserts"]},

    # ── Zeeshan (id 15) ─────────────────────────────────────────────────
    {"id": 1501, "name": "Chicken Biryani", "emoji": "🍚", "restaurant": "Zeeshan", "price": 260, "rating": 4.4, "desc": "Fragrant Kolkata-style biryani.", "veg": False, "moods": ["comfort"], "cats": ["biryani"]},
    {"id": 1502, "name": "Mutton Biryani", "emoji": "🍚", "restaurant": "Zeeshan", "price": 310, "rating": 4.5, "desc": "Rich mutton biryani slow-dum cooked.", "veg": False, "moods": ["comfort"], "cats": ["biryani"]},
    {"id": 1503, "name": "Chicken Chaap", "emoji": "🍗", "restaurant": "Zeeshan", "price": 240, "rating": 4.4, "desc": "Mughlai chicken chaap with roomali roti.", "veg": False, "moods": ["comfort"], "cats": ["mughlai"]},

    # ── Banana Leaf (id 16) ─────────────────────────────────────────────
    {"id": 1601, "name": "Masala Dosa", "emoji": "🫓", "restaurant": "Banana Leaf", "price": 130, "rating": 4.4, "desc": "Crispy rice dosa with spiced potato.", "veg": True, "moods": ["comfort", "happy"], "cats": ["south indian"]},
    {"id": 1602, "name": "Idli Sambar", "emoji": "🍲", "restaurant": "Banana Leaf", "price": 100, "rating": 4.3, "desc": "Soft idlis with piping hot sambar.", "veg": True, "moods": ["comfort"], "cats": ["south indian"]},
    {"id": 1603, "name": "Uttapam", "emoji": "🥞", "restaurant": "Banana Leaf", "price": 120, "rating": 4.2, "desc": "Thick rice pancake with onion and tomato.", "veg": True, "moods": ["happy"], "cats": ["south indian"]},
    {"id": 1604, "name": "Chettinad Chicken Curry", "emoji": "🍛", "restaurant": "Banana Leaf", "price": 280, "rating": 4.4, "desc": "Fiery Chettinad spiced chicken curry.", "veg": False, "moods": ["comfort", "happy"], "cats": ["south indian"]},
    {"id": 1605, "name": "Filter Coffee", "emoji": "☕", "restaurant": "Banana Leaf", "price": 60, "rating": 4.6, "desc": "Traditional South Indian filter coffee.", "veg": True, "moods": ["happy"], "cats": ["beverages"]},

    # ── Pice Hotel (id 17) ──────────────────────────────────────────────
    {"id": 1701, "name": "Maacher Jhol", "emoji": "🐟", "restaurant": "Pice Hotel", "price": 120, "rating": 4.3, "desc": "Light Bengali fish curry with potatoes.", "veg": False, "moods": ["comfort"], "cats": ["bengali", "seafood"]},
    {"id": 1702, "name": "Dal Bhat", "emoji": "🍛", "restaurant": "Pice Hotel", "price": 80, "rating": 4.1, "desc": "Steamed rice with Bengali lentil dal.", "veg": True, "moods": ["comfort"], "cats": ["bengali"]},
    {"id": 1703, "name": "Muri Ghonto", "emoji": "🍚", "restaurant": "Pice Hotel", "price": 150, "rating": 4.2, "desc": "Fish head cooked with rice and spices.", "veg": False, "moods": ["comfort"], "cats": ["bengali"]},

    # ── Oudh 1590 (id 18) ───────────────────────────────────────────────
    {"id": 1801, "name": "Galawati Kebab", "emoji": "🥩", "restaurant": "Oudh 1590", "price": 420, "rating": 4.7, "desc": "Melt-in-mouth Lucknowi mutton kebab.", "veg": False, "moods": ["romantic", "comfort"], "cats": ["awadhi", "kebab"]},
    {"id": 1802, "name": "Dum Biryani Oudh", "emoji": "🍚", "restaurant": "Oudh 1590", "price": 480, "rating": 4.6, "desc": "Awadhi dum biryani sealed with dough.", "veg": False, "moods": ["romantic"], "cats": ["biryani", "awadhi"]},
    {"id": 1803, "name": "Nihari", "emoji": "🍖", "restaurant": "Oudh 1590", "price": 450, "rating": 4.7, "desc": "Slow-cooked overnight lamb shank stew.", "veg": False, "moods": ["romantic", "comfort"], "cats": ["mughlai", "awadhi"]},
    {"id": 1804, "name": "Shahi Tukda", "emoji": "🍮", "restaurant": "Oudh 1590", "price": 180, "rating": 4.6, "desc": "Fried bread soaked in rabdi and saffron.", "veg": True, "moods": ["happy", "romantic"], "cats": ["desserts"]},

    # ── Trincas (id 19) ─────────────────────────────────────────────────
    {"id": 1901, "name": "Chicken Roulade", "emoji": "🍗", "restaurant": "Trincas", "price": 420, "rating": 4.4, "desc": "Stuffed chicken roll in continental style.", "veg": False, "moods": ["romantic"], "cats": ["continental"]},
    {"id": 1902, "name": "Prawn Masala", "emoji": "🦐", "restaurant": "Trincas", "price": 460, "rating": 4.3, "desc": "Spiced prawn curry Indian style.", "veg": False, "moods": ["comfort"], "cats": ["seafood"]},
    {"id": 1903, "name": "Black Forest Cake", "emoji": "🎂", "restaurant": "Trincas", "price": 200, "rating": 4.5, "desc": "Classic Black Forest with cherries.", "veg": True, "moods": ["happy", "romantic"], "cats": ["desserts", "bakery"]},

    # ── Nizam's (id 20) ─────────────────────────────────────────────────
    {"id": 2001, "name": "Mutton Kathi Roll", "emoji": "🌯", "restaurant": "Nizam's", "price": 160, "rating": 4.6, "desc": "The original Kolkata mutton kathi roll.", "veg": False, "moods": ["comfort", "happy"], "cats": ["kathi roll", "street food"]},
    {"id": 2002, "name": "Chicken Kathi Roll", "emoji": "🌯", "restaurant": "Nizam's", "price": 120, "rating": 4.5, "desc": "Juicy chicken wrapped in paratha.", "veg": False, "moods": ["happy"], "cats": ["kathi roll", "street food"]},
    {"id": 2003, "name": "Egg Roll", "emoji": "🥚", "restaurant": "Nizam's", "price": 80, "rating": 4.4, "desc": "Classic Kolkata egg roll.", "veg": False, "moods": ["happy", "comfort"], "cats": ["kathi roll", "street food"]},
    {"id": 2004, "name": "Double Egg Mutton Roll", "emoji": "🌯", "restaurant": "Nizam's", "price": 200, "rating": 4.7, "desc": "Double egg + mutton in a paratha roll.", "veg": False, "moods": ["comfort", "happy"], "cats": ["kathi roll", "street food"]},

    # ── Bohemian (id 21) ────────────────────────────────────────────────
    {"id": 2101, "name": "Bhetki Saltimbocca", "emoji": "🐟", "restaurant": "Bohemian", "price": 580, "rating": 4.6, "desc": "Bengali bhetki with Italian influence.", "veg": False, "moods": ["romantic"], "cats": ["bengali", "fusion", "seafood"]},
    {"id": 2102, "name": "Gondhoraj Chicken", "emoji": "🍋", "restaurant": "Bohemian", "price": 480, "rating": 4.5, "desc": "Chicken with Bengali lime (gondhoraj).", "veg": False, "moods": ["romantic"], "cats": ["bengali", "fusion"]},
    {"id": 2103, "name": "Mishti Doi Panna Cotta", "emoji": "🍮", "restaurant": "Bohemian", "price": 220, "rating": 4.6, "desc": "Bengali sweet curd meets Italian dessert.", "veg": True, "moods": ["happy", "romantic"], "cats": ["desserts", "fusion"]},

    # ── Haka (id 22) ────────────────────────────────────────────────────
    {"id": 2201, "name": "Schezwan Fried Rice", "emoji": "🍳", "restaurant": "Haka", "price": 240, "rating": 4.4, "desc": "Spicy Schezwan wok-fried rice.", "veg": False, "moods": ["comfort", "happy"], "cats": ["chinese"]},
    {"id": 2202, "name": "Kolkata Chilli Chicken", "emoji": "🌶️", "restaurant": "Haka", "price": 280, "rating": 4.5, "desc": "Kolkata-style dry chilli chicken.", "veg": False, "moods": ["happy"], "cats": ["chinese"]},
    {"id": 2203, "name": "Wonton Soup", "emoji": "🥟", "restaurant": "Haka", "price": 180, "rating": 4.3, "desc": "Pork wonton in clear broth.", "veg": False, "moods": ["comfort"], "cats": ["chinese", "soup"]},
    {"id": 2204, "name": "Pork Ribs", "emoji": "🍖", "restaurant": "Haka", "price": 420, "rating": 4.5, "desc": "Braised pork ribs Cantonese style.", "veg": False, "moods": ["comfort", "romantic"], "cats": ["chinese"]},

    # ── Momo I Am (id 23) ───────────────────────────────────────────────
    {"id": 2301, "name": "Steamed Chicken Momo", "emoji": "🥟", "restaurant": "Momo I Am", "price": 120, "rating": 4.4, "desc": "Soft steamed chicken dumplings.", "veg": False, "moods": ["happy", "comfort"], "cats": ["momos", "tibetan"]},
    {"id": 2302, "name": "Fried Pork Momo", "emoji": "🥟", "restaurant": "Momo I Am", "price": 140, "rating": 4.5, "desc": "Crispy fried pork momos with dip.", "veg": False, "moods": ["happy"], "cats": ["momos", "tibetan"]},
    {"id": 2303, "name": "Veg Momo", "emoji": "🥦", "restaurant": "Momo I Am", "price": 100, "rating": 4.2, "desc": "Cabbage and paneer steamed dumplings.", "veg": True, "moods": ["happy"], "cats": ["momos", "tibetan"]},
    {"id": 2304, "name": "Thukpa", "emoji": "🍜", "restaurant": "Momo I Am", "price": 160, "rating": 4.3, "desc": "Tibetan noodle soup with chicken.", "veg": False, "moods": ["comfort"], "cats": ["tibetan", "soup"]},

    # ── Saptapadi (id 24) ───────────────────────────────────────────────
    {"id": 2401, "name": "Ilish Bhapa", "emoji": "🐟", "restaurant": "Saptapadi", "price": 540, "rating": 4.7, "desc": "Steamed hilsa in mustard, green chilli.", "veg": False, "moods": ["romantic", "comfort"], "cats": ["bengali", "seafood"]},
    {"id": 2402, "name": "Mutton Biryani Saptapadi", "emoji": "🍚", "restaurant": "Saptapadi", "price": 380, "rating": 4.5, "desc": "House-style Kolkata mutton biryani.", "veg": False, "moods": ["comfort"], "cats": ["biryani", "bengali"]},
    {"id": 2403, "name": "Chaler Payesh", "emoji": "🍮", "restaurant": "Saptapadi", "price": 100, "rating": 4.6, "desc": "Kheer / rice pudding Bengali style.", "veg": True, "moods": ["happy", "comfort"], "cats": ["desserts", "bengali"]},

    # ── Tung Fong (id 25) ───────────────────────────────────────────────
    {"id": 2501, "name": "Spring Rolls", "emoji": "🥢", "restaurant": "Tung Fong", "price": 160, "rating": 4.2, "desc": "Crispy vegetable spring rolls.", "veg": True, "moods": ["happy"], "cats": ["chinese", "snacks"]},
    {"id": 2502, "name": "Sweet & Sour Pork", "emoji": "🍖", "restaurant": "Tung Fong", "price": 320, "rating": 4.3, "desc": "Cantonese sweet and sour pork cubes.", "veg": False, "moods": ["comfort"], "cats": ["chinese"]},
    {"id": 2503, "name": "Hakka Noodles", "emoji": "🍜", "restaurant": "Tung Fong", "price": 180, "rating": 4.2, "desc": "Classic Hakka tossed noodles.", "veg": False, "moods": ["comfort", "happy"], "cats": ["chinese"]},

    # ── Smoke House Deli (id 26) ────────────────────────────────────────
    {"id": 2601, "name": "Smoked Salmon Salad", "emoji": "🥗", "restaurant": "Smoke House Deli", "price": 480, "rating": 4.5, "desc": "Norwegian smoked salmon with rocket.", "veg": False, "moods": ["happy", "romantic"], "cats": ["salad", "continental"]},
    {"id": 2602, "name": "Eggs Benedict", "emoji": "🍳", "restaurant": "Smoke House Deli", "price": 320, "rating": 4.5, "desc": "Poached eggs on English muffin, hollandaise.", "veg": False, "moods": ["happy"], "cats": ["breakfast", "continental"]},
    {"id": 2603, "name": "Truffle Fries", "emoji": "🍟", "restaurant": "Smoke House Deli", "price": 280, "rating": 4.6, "desc": "Shoestring fries tossed in truffle oil.", "veg": True, "moods": ["happy"], "cats": ["snacks", "continental"]},
    {"id": 2604, "name": "Cheesecake", "emoji": "🍰", "restaurant": "Smoke House Deli", "price": 260, "rating": 4.6, "desc": "Classic New York baked cheesecake.", "veg": True, "moods": ["happy", "romantic"], "cats": ["desserts"]},

    # ── The Grid (id 27) ────────────────────────────────────────────────
    {"id": 2701, "name": "Classic Smash Burger", "emoji": "🍔", "restaurant": "The Grid", "price": 320, "rating": 4.4, "desc": "Double smash patty with cheddar and pickles.", "veg": False, "moods": ["happy"], "cats": ["burgers", "american"]},
    {"id": 2702, "name": "Crispy Chicken Burger", "emoji": "🍔", "restaurant": "The Grid", "price": 280, "rating": 4.3, "desc": "Southern-fried chicken in brioche bun.", "veg": False, "moods": ["happy"], "cats": ["burgers"]},
    {"id": 2703, "name": "Loaded Nachos", "emoji": "🧀", "restaurant": "The Grid", "price": 240, "rating": 4.3, "desc": "Tortilla chips with salsa, guacamole, cheese.", "veg": True, "moods": ["happy"], "cats": ["american", "snacks"]},
    {"id": 2704, "name": "Milkshake", "emoji": "🥤", "restaurant": "The Grid", "price": 180, "rating": 4.4, "desc": "Thick shake — chocolate, vanilla, or strawberry.", "veg": True, "moods": ["happy"], "cats": ["beverages", "desserts"]},

    # ── Balwant Singh's Eating House (id 28) ────────────────────────────
    {"id": 2801, "name": "Paya Soup", "emoji": "🍲", "restaurant": "Balwant Singh's Eating House", "price": 150, "rating": 4.6, "desc": "Slow-cooked lamb trotter soup.", "veg": False, "moods": ["comfort"], "cats": ["north indian", "soup"]},
    {"id": 2802, "name": "Butter Chicken", "emoji": "🍗", "restaurant": "Balwant Singh's Eating House", "price": 220, "rating": 4.5, "desc": "Creamy tomato-based chicken curry.", "veg": False, "moods": ["comfort"], "cats": ["north indian", "punjabi"]},
    {"id": 2803, "name": "Tandoori Roti", "emoji": "🫓", "restaurant": "Balwant Singh's Eating House", "price": 30, "rating": 4.4, "desc": "Whole-wheat bread from clay oven.", "veg": True, "moods": ["comfort"], "cats": ["north indian"]},
    {"id": 2804, "name": "Lassi", "emoji": "🥛", "restaurant": "Balwant Singh's Eating House", "price": 70, "rating": 4.5, "desc": "Thick sweet yoghurt drink Punjabi style.", "veg": True, "moods": ["happy", "comfort"], "cats": ["beverages"]},

    # ── Chung Wah (id 29) ───────────────────────────────────────────────
    {"id": 2901, "name": "Chicken Manchurian", "emoji": "🍗", "restaurant": "Chung Wah", "price": 260, "rating": 4.3, "desc": "Desi Chinese chicken Manchurian gravy.", "veg": False, "moods": ["comfort", "happy"], "cats": ["chinese"]},
    {"id": 2902, "name": "Egg Fried Rice", "emoji": "🍳", "restaurant": "Chung Wah", "price": 160, "rating": 4.2, "desc": "Classic egg fried rice wok-style.", "veg": False, "moods": ["comfort"], "cats": ["chinese"]},
    {"id": 2903, "name": "Crispy Corn", "emoji": "🌽", "restaurant": "Chung Wah", "price": 180, "rating": 4.3, "desc": "Fried baby corn in sweet-spicy glaze.", "veg": True, "moods": ["happy"], "cats": ["chinese", "snacks"]},

    # ── Cafe Mezzuna (id 30) ────────────────────────────────────────────
    {"id": 3001, "name": "Penne Arrabbiata", "emoji": "🍝", "restaurant": "Cafe Mezzuna", "price": 320, "rating": 4.4, "desc": "Spicy tomato sauce with penne.", "veg": True, "moods": ["romantic", "happy"], "cats": ["italian", "pasta"]},
    {"id": 3002, "name": "Quattro Stagioni Pizza", "emoji": "🍕", "restaurant": "Cafe Mezzuna", "price": 420, "rating": 4.3, "desc": "Four seasons wood-fired pizza.", "veg": False, "moods": ["happy", "romantic"], "cats": ["italian", "pizza"]},
    {"id": 3003, "name": "Tiramisu", "emoji": "☕", "restaurant": "Cafe Mezzuna", "price": 280, "rating": 4.5, "desc": "Classic Italian coffee dessert.", "veg": True, "moods": ["romantic", "happy"], "cats": ["desserts", "italian"]},
    {"id": 3004, "name": "Cappuccino", "emoji": "☕", "restaurant": "Cafe Mezzuna", "price": 120, "rating": 4.4, "desc": "Italian-style frothy cappuccino.", "veg": True, "moods": ["happy"], "cats": ["beverages", "cafe"]},

    # ── The Bhoj Company (id 31) ────────────────────────────────────────
    {"id": 3101, "name": "Rajasthani Thali", "emoji": "🍱", "restaurant": "The Bhoj Company", "price": 450, "rating": 4.5, "desc": "Dal baati churma with lal maas and more.", "veg": False, "moods": ["comfort", "happy"], "cats": ["north indian", "thali"]},
    {"id": 3102, "name": "Dal Makhani", "emoji": "🍲", "restaurant": "The Bhoj Company", "price": 200, "rating": 4.4, "desc": "Creamy black lentil cooked overnight.", "veg": True, "moods": ["comfort"], "cats": ["north indian"]},
    {"id": 3103, "name": "Gulab Jamun", "emoji": "🍬", "restaurant": "The Bhoj Company", "price": 80, "rating": 4.5, "desc": "Soft milk solids dumplings in syrup.", "veg": True, "moods": ["happy"], "cats": ["desserts"]},

    # ── Tasca (id 32) ───────────────────────────────────────────────────
    {"id": 3201, "name": "Ribeye Steak", "emoji": "🥩", "restaurant": "Tasca", "price": 1200, "rating": 4.6, "desc": "200g USDA ribeye with chimichurri.", "veg": False, "moods": ["romantic"], "cats": ["steak", "continental"]},
    {"id": 3202, "name": "Grilled Octopus", "emoji": "🐙", "restaurant": "Tasca", "price": 780, "rating": 4.5, "desc": "Tender charred octopus with lemon oil.", "veg": False, "moods": ["romantic"], "cats": ["seafood", "continental"]},
    {"id": 3203, "name": "Crème Brûlée", "emoji": "🍮", "restaurant": "Tasca", "price": 350, "rating": 4.7, "desc": "Classic vanilla custard with caramel crust.", "veg": True, "moods": ["romantic", "happy"], "cats": ["desserts", "continental"]},

    # ── Mitra Cafe (id 33) ──────────────────────────────────────────────
    {"id": 3301, "name": "Mughlai Paratha", "emoji": "🥚", "restaurant": "Mitra Cafe", "price": 80, "rating": 4.5, "desc": "Egg and keema-stuffed flaky paratha.", "veg": False, "moods": ["comfort", "happy"], "cats": ["breakfast", "street food"]},
    {"id": 3302, "name": "French Toast", "emoji": "🍞", "restaurant": "Mitra Cafe", "price": 90, "rating": 4.4, "desc": "Eggy bread toast with jam and butter.", "veg": False, "moods": ["happy"], "cats": ["breakfast"]},
    {"id": 3303, "name": "Bread Omelette", "emoji": "🍳", "restaurant": "Mitra Cafe", "price": 70, "rating": 4.3, "desc": "Buttered bread with masala omelette.", "veg": False, "moods": ["comfort"], "cats": ["breakfast"]},

    # ── Aaheli (id 34) ──────────────────────────────────────────────────
    {"id": 3401, "name": "Chingri Bhapa", "emoji": "🦐", "restaurant": "Aaheli", "price": 520, "rating": 4.7, "desc": "Prawns steamed in mustard-coconut paste.", "veg": False, "moods": ["romantic", "comfort"], "cats": ["bengali", "seafood"]},
    {"id": 3402, "name": "Ilish Paturi", "emoji": "🐟", "restaurant": "Aaheli", "price": 560, "rating": 4.8, "desc": "Hilsa in banana leaf with mustard-mustard.", "veg": False, "moods": ["romantic"], "cats": ["bengali", "seafood"]},
    {"id": 3403, "name": "Nolen Gurer Mishti Doi", "emoji": "🍮", "restaurant": "Aaheli", "price": 120, "rating": 4.8, "desc": "Sweet curd with date palm jaggery.", "veg": True, "moods": ["happy", "romantic"], "cats": ["desserts", "bengali"]},

    # ── Peerless Inn (id 35) ────────────────────────────────────────────
    {"id": 3501, "name": "Bengali Fish Curry", "emoji": "🐟", "restaurant": "Peerless Inn", "price": 380, "rating": 4.3, "desc": "Classic rohu curry Bengali style.", "veg": False, "moods": ["comfort"], "cats": ["bengali", "seafood"]},
    {"id": 3502, "name": "Chicken Tikka", "emoji": "🍢", "restaurant": "Peerless Inn", "price": 320, "rating": 4.2, "desc": "Tandoor chicken tikka marinated overnight.", "veg": False, "moods": ["happy"], "cats": ["north indian"]},

    # ── Bhojohari Manna (id 36) ─────────────────────────────────────────
    {"id": 3601, "name": "Luchi Kosha Mangsho", "emoji": "🫓", "restaurant": "Bhojohari Manna", "price": 350, "rating": 4.6, "desc": "Kolkata luchi with slow-cooked mutton.", "veg": False, "moods": ["comfort", "happy"], "cats": ["bengali"]},
    {"id": 3602, "name": "Daab Chingri", "emoji": "🥥", "restaurant": "Bhojohari Manna", "price": 480, "rating": 4.5, "desc": "Prawns in tender coconut shell.", "veg": False, "moods": ["romantic"], "cats": ["bengali", "seafood"]},
    {"id": 3603, "name": "Kalojam", "emoji": "⚫", "restaurant": "Bhojohari Manna", "price": 70, "rating": 4.6, "desc": "Bengali dark fried milk sweet in syrup.", "veg": True, "moods": ["happy"], "cats": ["desserts", "bengali"]},

    # ── Marco Polo (id 37) ──────────────────────────────────────────────
    {"id": 3701, "name": "Margherita Pizza", "emoji": "🍕", "restaurant": "Marco Polo", "price": 320, "rating": 4.2, "desc": "Classic tomato, mozzarella, basil pizza.", "veg": True, "moods": ["happy"], "cats": ["italian", "pizza"]},
    {"id": 3702, "name": "Pepperoni Pizza", "emoji": "🍕", "restaurant": "Marco Polo", "price": 380, "rating": 4.3, "desc": "Loaded pepperoni on thin-crust base.", "veg": False, "moods": ["happy"], "cats": ["italian", "pizza"]},
    {"id": 3703, "name": "Pasta Carbonara", "emoji": "🍝", "restaurant": "Marco Polo", "price": 340, "rating": 4.2, "desc": "Creamy egg and pancetta pasta.", "veg": False, "moods": ["comfort", "romantic"], "cats": ["italian", "pasta"]},

    # ── Olypub (id 38) ──────────────────────────────────────────────────
    {"id": 3801, "name": "Fish & Chips", "emoji": "🐟", "restaurant": "Olypub", "price": 320, "rating": 4.3, "desc": "Beer-battered fish with chunky chips.", "veg": False, "moods": ["happy", "comfort"], "cats": ["continental", "pub grub"]},
    {"id": 3802, "name": "Chicken Wings", "emoji": "🍗", "restaurant": "Olypub", "price": 280, "rating": 4.2, "desc": "Spiced fried wings with blue cheese dip.", "veg": False, "moods": ["happy"], "cats": ["pub grub", "american"]},
    {"id": 3803, "name": "Kolkata Egg Devil", "emoji": "🥚", "restaurant": "Olypub", "price": 120, "rating": 4.4, "desc": "Devilled egg snack Kolkata style.", "veg": False, "moods": ["happy"], "cats": ["snacks", "pub grub"]},

    # ── Spice Kraft (id 39) ─────────────────────────────────────────────
    {"id": 3901, "name": "Lamb Rack", "emoji": "🍖", "restaurant": "Spice Kraft", "price": 880, "rating": 4.5, "desc": "French-cut lamb rack with Indian jus.", "veg": False, "moods": ["romantic"], "cats": ["fusion", "continental"]},
    {"id": 3902, "name": "Palak Paneer Ravioli", "emoji": "🍝", "restaurant": "Spice Kraft", "price": 420, "rating": 4.4, "desc": "Spinach-paneer filling in handmade pasta.", "veg": True, "moods": ["romantic"], "cats": ["fusion", "pasta"]},
    {"id": 3903, "name": "Mango Panna Cotta", "emoji": "🥭", "restaurant": "Spice Kraft", "price": 280, "rating": 4.5, "desc": "Alphonso mango set cream dessert.", "veg": True, "moods": ["happy", "romantic"], "cats": ["desserts", "fusion"]},

    # ── Cafe Coffee Day Square (id 40) ──────────────────────────────────
    {"id": 4001, "name": "Cafe Mocha", "emoji": "☕", "restaurant": "Cafe Coffee Day Square", "price": 180, "rating": 4.0, "desc": "Espresso with steamed milk and chocolate.", "veg": True, "moods": ["happy"], "cats": ["beverages", "cafe"]},
    {"id": 4002, "name": "Cold Coffee Frappe", "emoji": "🧋", "restaurant": "Cafe Coffee Day Square", "price": 160, "rating": 4.1, "desc": "Chilled blended coffee frappe.", "veg": True, "moods": ["happy"], "cats": ["beverages", "cafe"]},
    {"id": 4003, "name": "Veg Club Sandwich", "emoji": "🥪", "restaurant": "Cafe Coffee Day Square", "price": 180, "rating": 3.9, "desc": "Toasted sandwich with veggies and cheese.", "veg": True, "moods": ["happy"], "cats": ["snacks"]},

    # ── The Yellow Chilli (id 41) ────────────────────────────────────────
    {"id": 4101, "name": "Murgh Makhani", "emoji": "🍗", "restaurant": "The Yellow Chilli", "price": 320, "rating": 4.3, "desc": "Sanjeev Kapoor's signature butter chicken.", "veg": False, "moods": ["comfort"], "cats": ["north indian"]},
    {"id": 4102, "name": "Paneer Tikka Masala", "emoji": "🧀", "restaurant": "The Yellow Chilli", "price": 280, "rating": 4.2, "desc": "Cottage cheese cubes in tikka gravy.", "veg": True, "moods": ["comfort"], "cats": ["north indian"]},
    {"id": 4103, "name": "Garlic Naan", "emoji": "🫓", "restaurant": "The Yellow Chilli", "price": 60, "rating": 4.2, "desc": "Soft garlic-buttered naan from tandoor.", "veg": True, "moods": ["comfort"], "cats": ["north indian"]},

    # ── Zaffran (id 42) ─────────────────────────────────────────────────
    {"id": 4201, "name": "Seekh Kebab Platter", "emoji": "🍢", "restaurant": "Zaffran", "price": 380, "rating": 4.4, "desc": "Mixed kebab platter from the tandoor.", "veg": False, "moods": ["romantic", "happy"], "cats": ["mughlai", "kebab"]},
    {"id": 4202, "name": "Mutton Rogan Josh", "emoji": "🍖", "restaurant": "Zaffran", "price": 420, "rating": 4.4, "desc": "Kashmiri red mutton curry.", "veg": False, "moods": ["comfort", "romantic"], "cats": ["mughlai", "north indian"]},
    {"id": 4203, "name": "Phirni", "emoji": "🍮", "restaurant": "Zaffran", "price": 120, "rating": 4.4, "desc": "Ground rice pudding in clay saucer.", "veg": True, "moods": ["happy"], "cats": ["desserts"]},

    # ── Raj's Spanish Cafe (id 43) ───────────────────────────────────────
    {"id": 4301, "name": "Paella Valenciana", "emoji": "🥘", "restaurant": "Raj's Spanish Cafe", "price": 580, "rating": 4.4, "desc": "Saffron rice with chicken and seafood.", "veg": False, "moods": ["romantic"], "cats": ["spanish"]},
    {"id": 4302, "name": "Patatas Bravas", "emoji": "🥔", "restaurant": "Raj's Spanish Cafe", "price": 220, "rating": 4.3, "desc": "Fried potato cubes with spicy tomato sauce.", "veg": True, "moods": ["happy"], "cats": ["spanish", "snacks"]},
    {"id": 4303, "name": "Churros with Chocolate", "emoji": "🍩", "restaurant": "Raj's Spanish Cafe", "price": 240, "rating": 4.5, "desc": "Crispy churros with dark chocolate dip.", "veg": True, "moods": ["happy", "romantic"], "cats": ["desserts", "spanish"]},

    # ── Suruchi (id 44) ─────────────────────────────────────────────────
    {"id": 4401, "name": "Chital Macher Kalia", "emoji": "🐟", "restaurant": "Suruchi", "price": 420, "rating": 4.6, "desc": "Chitol fish in rich Bengali kalia curry.", "veg": False, "moods": ["comfort"], "cats": ["bengali", "seafood"]},
    {"id": 4402, "name": "Begun-er Torkari", "emoji": "🍆", "restaurant": "Suruchi", "price": 130, "rating": 4.4, "desc": "Bengali spiced eggplant sabji.", "veg": True, "moods": ["comfort"], "cats": ["bengali"]},
    {"id": 4403, "name": "Lobster Malaikari", "emoji": "🦞", "restaurant": "Suruchi", "price": 780, "rating": 4.7, "desc": "Lobster in coconut milk Bengali curry.", "veg": False, "moods": ["romantic"], "cats": ["bengali", "seafood"]},

    # ── Amber (id 45) ───────────────────────────────────────────────────
    {"id": 4501, "name": "Chicken Cafreal", "emoji": "🍗", "restaurant": "Amber", "price": 360, "rating": 4.4, "desc": "Goan-spiced green masala chicken.", "veg": False, "moods": ["comfort", "romantic"], "cats": ["continental", "mughlai"]},
    {"id": 4502, "name": "Mutton Biryani Amber", "emoji": "🍚", "restaurant": "Amber", "price": 380, "rating": 4.4, "desc": "House-style dum mutton biryani.", "veg": False, "moods": ["comfort"], "cats": ["biryani", "mughlai"]},
    {"id": 4503, "name": "Caramel Custard", "emoji": "🍮", "restaurant": "Amber", "price": 150, "rating": 4.5, "desc": "Baked vanilla custard with caramel top.", "veg": True, "moods": ["happy", "romantic"], "cats": ["desserts", "continental"]},

    # ── Rôtisserie by Saby (id 46) ───────────────────────────────────────
    {"id": 4601, "name": "Rotisserie Chicken", "emoji": "🍗", "restaurant": "Rôtisserie by Saby", "price": 680, "rating": 4.6, "desc": "French spit-roasted half chicken.", "veg": False, "moods": ["romantic", "comfort"], "cats": ["french", "continental"]},
    {"id": 4602, "name": "French Onion Soup", "emoji": "🧅", "restaurant": "Rôtisserie by Saby", "price": 280, "rating": 4.5, "desc": "Slow-caramelised onion soup with gruyère.", "veg": True, "moods": ["comfort", "romantic"], "cats": ["french", "soup"]},
    {"id": 4603, "name": "Tarte Tatin", "emoji": "🍎", "restaurant": "Rôtisserie by Saby", "price": 320, "rating": 4.6, "desc": "French upside-down caramelised apple tart.", "veg": True, "moods": ["romantic", "happy"], "cats": ["french", "desserts"]},

    # ── Cafe Ozora (id 47) ──────────────────────────────────────────────
    {"id": 4701, "name": "Avocado Toast", "emoji": "🥑", "restaurant": "Cafe Ozora", "price": 260, "rating": 4.3, "desc": "Sourdough with smashed avocado and chilli.", "veg": True, "moods": ["happy"], "cats": ["cafe", "breakfast"]},
    {"id": 4702, "name": "Granola Bowl", "emoji": "🥣", "restaurant": "Cafe Ozora", "price": 220, "rating": 4.2, "desc": "House granola with Greek yoghurt and berries.", "veg": True, "moods": ["happy"], "cats": ["cafe", "breakfast"]},
    {"id": 4703, "name": "Cold Brew Coffee", "emoji": "🧊", "restaurant": "Cafe Ozora", "price": 180, "rating": 4.4, "desc": "12-hour cold-steeped black coffee.", "veg": True, "moods": ["happy"], "cats": ["beverages", "cafe"]},

    # ── Dumplings (id 48) ───────────────────────────────────────────────
    {"id": 4801, "name": "Pork Gyoza", "emoji": "🥟", "restaurant": "Dumplings", "price": 180, "rating": 4.4, "desc": "Pan-fried Japanese-style pork dumplings.", "veg": False, "moods": ["happy", "comfort"], "cats": ["chinese", "momos"]},
    {"id": 4802, "name": "Xiao Long Bao", "emoji": "🥟", "restaurant": "Dumplings", "price": 220, "rating": 4.5, "desc": "Soup dumplings with pork filling.", "veg": False, "moods": ["happy"], "cats": ["chinese"]},
    {"id": 4803, "name": "Edamame", "emoji": "🫛", "restaurant": "Dumplings", "price": 120, "rating": 4.2, "desc": "Salted steamed edamame pods.", "veg": True, "moods": ["happy"], "cats": ["chinese", "snacks"]},

    # ── Rajbhog (id 49) ─────────────────────────────────────────────────
    {"id": 4901, "name": "Rasogolla", "emoji": "⚪", "restaurant": "Rajbhog", "price": 30, "rating": 4.7, "desc": "Soft spongy Bengali rasgulla.", "veg": True, "moods": ["happy"], "cats": ["sweets", "bengali"]},
    {"id": 4902, "name": "Rajbhog Sweet", "emoji": "🟡", "restaurant": "Rajbhog", "price": 50, "rating": 4.7, "desc": "Large saffron-stuffed rasgulla.", "veg": True, "moods": ["happy"], "cats": ["sweets", "bengali"]},
    {"id": 4903, "name": "Pantua", "emoji": "⚫", "restaurant": "Rajbhog", "price": 35, "rating": 4.6, "desc": "Bengali gulab jamun in light syrup.", "veg": True, "moods": ["happy"], "cats": ["sweets", "bengali"]},
    {"id": 4904, "name": "Mishti Doi Cup", "emoji": "🍮", "restaurant": "Rajbhog", "price": 40, "rating": 4.8, "desc": "Individual cup of sweet Bengali curd.", "veg": True, "moods": ["happy"], "cats": ["sweets", "bengali", "desserts"]},
    {"id": 4905, "name": "Kheer Kadam", "emoji": "🍡", "restaurant": "Rajbhog", "price": 45, "rating": 4.6, "desc": "Rasgulla coated in mawa sweet.", "veg": True, "moods": ["happy"], "cats": ["sweets", "bengali"]},

    # ── Sree Annapurna (id 50) ──────────────────────────────────────────
    {"id": 5001, "name": "Veg Thali", "emoji": "🍱", "restaurant": "Sree Annapurna", "price": 180, "rating": 4.3, "desc": "Full South Indian veg thali with rice.", "veg": True, "moods": ["comfort"], "cats": ["south indian", "thali"]},
    {"id": 5002, "name": "Pesarattu", "emoji": "🥞", "restaurant": "Sree Annapurna", "price": 110, "rating": 4.2, "desc": "Green moong dosa Andhra style.", "veg": True, "moods": ["comfort", "happy"], "cats": ["south indian"]},
    {"id": 5003, "name": "Sambar Rice", "emoji": "🍚", "restaurant": "Sree Annapurna", "price": 120, "rating": 4.3, "desc": "Rice mixed with lentil vegetable sambar.", "veg": True, "moods": ["comfort"], "cats": ["south indian"]},
    {"id": 5004, "name": "Pongal", "emoji": "🍲", "restaurant": "Sree Annapurna", "price": 100, "rating": 4.2, "desc": "Soft rice and lentil porridge with ghee.", "veg": True, "moods": ["comfort"], "cats": ["south indian", "breakfast"]},
    {"id": 5005, "name": "Payasam", "emoji": "🍮", "restaurant": "Sree Annapurna", "price": 90, "rating": 4.3, "desc": "South Indian vermicelli kheer dessert.", "veg": True, "moods": ["happy"], "cats": ["desserts", "south indian"]},
]



