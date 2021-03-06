import pandas as pd

OPTIONS = { 'LOVE' : [
    "married",
    "wed",
    "husband",
    "marry",
    "couple",
    "marriage",
    "adore",
    "affection",
    "bigamist",
    "wife",
    "newlywed",
    "affair",
    "honeymoon",
    "morganatic",
    "estranged",
    "bigamy",
    "gay",
    "loving",
    "embrace",
    "paramour",
    "cohabit",
    "marital",
    "polygamy",
    "sex",
    "seduce",
    "fiancee",
    "conjoin",
    "relationship",
    "connubial",
    "dowry"
  ],

  'POLITICS' : [
    "technocracy",
    "statecraft",
    "electorate",
    "diplomacy",
    "diplomatic",
    "election",
    "jingo",
    "ballot",
    "vote",
    "suppression",
    "aristocracy",
    "president",
    "candidate",
    "ruling",
    "plebiscite",
    "embassy",
    "constituency",
    "referendum",
    "government",
    "regime",
    "society",
    "elector",
    "voting",
    "sovereignty",
    "consul",
    "democratize",
    "foreign",
    "worldwide",
    "hustings",
    "political"
  ],

  'FOOD' : [
    "edible",
    "sandwich",
    "delicious",
    "meal",
    "palatable",
    "cooked",
    "recipe",
    "comestible",
    "intake",
    "diet",
    "bread",
    "eatable",
    "nutrition",
    "dessert",
    "calorie",
    "cheese",
    "sweet",
    "victual",
    "eat",
    "dinner",
    "appetizing",
    "vegetarian",
    "luscious",
    "savory",
    "dietary",
    "victuals",
    "wholesome",
    "healthy",
    "flavor",
    "commissariat"
  ],

  'SCHOOl': [
    "graduated",
    "valedictorian",
    "attendance",
    "classroom",
    "graduation",
    "tutor",
    "educational",
    "convent",
    "teach",
    "class",
    "classmate",
    "teacher",
    "schoolmaster",
    "undergraduate",
    "dormitory",
    "college",
    "university",
    "informative",
    "teaching",
    "pupil",
    "headmaster",
    "student",
    "polytechnic",
    "homeroom",
    "academy",
    "pedagogy",
    "campus",
    "trainee",
    "pedagogics",
    "academic"
  ],

  'FINANCES' : [
    "subsidize",
    "treasury",
    "fund",
    "funding",
    "loan",
    "amortize",
    "investment",
    "mortgage",
    "accounting",
    "endue",
    "refinance",
    "debt",
    "ministry",
    "account",
    "bank",
    "enthrone",
    "economy",
    "repayment",
    "installment",
    "cash",
    "financial",
    "moratorium",
    "owing",
    "owe",
    "debenture",
    "lender",
    "borrow",
    "financing",
    "money",
    "expenditure"
  ],

  'EXERCISE' : [
    "calisthenics",
    "gymnastics",
    "stroller",
    "jogging",
    "jog",
    "running",
    "walker",
    "fitness",
    "bicycle",
    "usage",
    "canter",
    "marathon",
    "utilization",
    "jogger",
    "sport",
    "emotionally",
    "jumping",
    "cycling",
    "walk",
    "healthy",
    "amble",
    "exercising",
    "lope",
    "run",
    "sportive",
    "wholesomeness",
    "walking",
    "movement",
    "ride",
    "health"
  ],

}

DATA = pd.read_csv('/Users/olivialam/Desktop/SaltySocials/venv/src/saltysocials/twitter_data.csv', index_col=0)