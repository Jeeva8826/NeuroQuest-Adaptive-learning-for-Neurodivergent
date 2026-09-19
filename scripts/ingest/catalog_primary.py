"""
Authentic NCERT Academic Questions Catalog for Primary Standards (Classes 1 to 5)
Subjects: Mathematics, Science / Environmental Studies (EVS), English
Every entry is an authentic academic question testing the core concepts of the chapter.
"""

PRIMARY_QUESTIONS = {
    # =========================================================================
    # CLASS 1
    # =========================================================================
    (1, "Mathematics", 1): {
        "concept_name": "Inside-Outside & Spatial Orientation",
        "diff": 1,
        "objectives": ["Identify objects inside vs outside boundaries", "Understand spatial relationships"],
        "prereq": ["Recognizing common objects"],
        "std_exp": "Spatial terms like inside and outside describe position relative to an enclosed area or boundary.",
        "simp_exp": "When something is within a container or house, it is INSIDE! When it is outside the walls, it is OUTSIDE!",
        "analogies": {
            "space": "An astronaut floats inside the rocket capsule, while space probes fly outside in the galaxy!",
            "coding": "Variables declared inside curly braces { } stay inside, while global variables live outside!",
            "animals": "Baby chicks stay warm inside the coop, while the rooster crows outside in the farmyard."
        },
        "prompt": "The puppy is sleeping on its soft bed inside the dog house. Where is the puppy resting?",
        "options": ["Inside the dog house", "Outside in the garden", "On the roof of the shed", "Under the tree"],
        "answer": "Inside the dog house",
        "exp": "Because the puppy is surrounded by the walls of the dog house, its position is inside.",
        "hints": ["Look at where the puppy is sleeping.", "It is surrounded by the dog house walls.", "The opposite of outside is inside."],
        "scaffolds": ["Step 1: Locate the boundary of the dog house.", "Step 2: Check if the puppy is within the walls.", "Step 3: Choose 'Inside'."]
    },
    (1, "Mathematics", 2): {
        "concept_name": "Numbers from One to Nine",
        "diff": 1,
        "objectives": ["Count quantities up to 9", "Associate numeral symbols with counts"],
        "prereq": ["One-to-one correspondence"],
        "std_exp": "Counting objects in a collection assigns a unique counting number to each item.",
        "simp_exp": "Point your finger at each object one by one: 1, 2, 3, 4, 5, 6, 7, 8, 9!",
        "analogies": {
            "space": "Counting countdown seconds before rocket launch: 5, 4, 3, 2, 1, Liftoff!",
            "coding": "Like an index loop counter iterating from 1 to 9.",
            "animals": "Counting ducklings swimming in a row behind mother duck."
        },
        "prompt": "An astronaut spotted 4 blue planets and 3 green planets through the telescope. How many planets did the astronaut count in total?",
        "options": ["7 planets", "6 planets", "8 planets", "5 planets"],
        "answer": "7 planets",
        "exp": "Count 4 blue planets: 1, 2, 3, 4. Then count 3 more green planets: 5, 6, 7. In total there are 7 planets.",
        "hints": ["Start with the 4 blue planets.", "Count up 3 more: 5, 6, 7!", "4 + 3 = 7."],
        "scaffolds": ["Step 1: First group = 4.", "Step 2: Add second group = 3.", "Step 3: 4 + 3 = 7."]
    },
    (1, "Mathematics", 3): {
        "concept_name": "Addition (Sum up to 9)",
        "diff": 1,
        "objectives": ["Combine two groups of items", "Compute sums up to 9"],
        "prereq": ["Counting up to 9"],
        "std_exp": "Addition combines two or more numbers to determine the total sum.",
        "simp_exp": "Putting collections together to find how many there are in total!",
        "analogies": {
            "space": "Docking 3 cargo modules to 2 habitat modules gives 5 connected modules!",
            "coding": "Using the '+' operator to sum two integers.",
            "animals": "3 squirrels joined 2 squirrels under the oak tree: 3 + 2 = 5 squirrels!"
        },
        "prompt": "Riya has 5 red balloons. Her friend gives her 3 more yellow balloons. How many balloons does Riya have altogether?",
        "options": ["8 balloons", "7 balloons", "9 balloons", "6 balloons"],
        "answer": "8 balloons",
        "exp": "Combine 5 red balloons with 3 yellow balloons: 5 + 3 = 8 balloons.",
        "hints": ["Start with Riya's 5 balloons.", "Add the 3 new balloons: 6, 7, 8!", "5 + 3 = 8."],
        "scaffolds": ["Step 1: Start at 5.", "Step 2: Count forward 3 steps: 6, 7, 8.", "Step 3: Total is 8."]
    },
    (1, "Mathematics", 4): {
        "concept_name": "Subtraction (Take Away)",
        "diff": 1,
        "objectives": ["Remove objects from a group", "Find remaining difference"],
        "prereq": ["Counting up to 9", "Addition basics"],
        "std_exp": "Subtraction is taking away a quantity from a collection to find the remainder.",
        "simp_exp": "If you have 6 apples and eat 2, count how many delicious apples are left!",
        "analogies": {
            "space": "A spacecraft releases 2 booster rockets from its main body.",
            "coding": "Decrementing a counter variable or popping items from an array.",
            "animals": "6 birds were on a wire, 2 flew away to find seeds: 4 remain."
        },
        "prompt": "There are 7 ripe mangoes on a branch. A mischievous monkey plucks 2 mangoes. How many mangoes are left on the branch?",
        "options": ["5 mangoes", "4 mangoes", "6 mangoes", "3 mangoes"],
        "answer": "5 mangoes",
        "exp": "7 mangoes take away 2 mangoes: 7 - 2 = 5 mangoes remain on the branch.",
        "hints": ["Start with 7 mangoes.", "Take away 2: count back 6, 5.", "7 - 2 = 5."],
        "scaffolds": ["Step 1: Total mangoes = 7.", "Step 2: Subtract 2 mangoes.", "Step 3: Remaining = 5."]
    },
    (1, "Mathematics", 5): {
        "concept_name": "Numbers from Ten to Twenty",
        "diff": 1,
        "objectives": ["Understand bundles of ten", "Count from 10 to 20"],
        "prereq": ["Numbers 1 to 9"],
        "std_exp": "Numbers 10 to 20 are composed of one bundle of ten plus additional ones.",
        "simp_exp": "14 is one bundle of 10 sticks and 4 single sticks!",
        "analogies": {
            "space": "A rocket has 1 main engine bank of 10 thrusters plus 5 auxiliary thrusters = 15!",
            "coding": "Hexadecimal or decimal place value base representation.",
            "animals": "A pack of 10 wolves resting together plus 3 scout wolves nearby = 13 wolves."
        },
        "prompt": "A bundle contains 10 wooden sticks. Next to it are 4 loose sticks. What number do they represent together?",
        "options": ["14", "104", "12", "16"],
        "answer": "14",
        "exp": "1 bundle of ten (10) plus 4 loose ones (4) equals 14.",
        "hints": ["Start with the bundle of 10.", "Count forward 4 ones: 11, 12, 13, 14.", "10 + 4 = 14."],
        "scaffolds": ["Step 1: Tens = 1 (value 10).", "Step 2: Ones = 4.", "Step 3: 10 + 4 = 14."]
    },
    (1, "Mathematics", 6): {
        "concept_name": "Time & Daily Routine",
        "diff": 1,
        "objectives": ["Sequence daily activities", "Distinguish morning, afternoon, evening, and night"],
        "prereq": ["Daily routines awareness"],
        "std_exp": "Time progresses cyclically through morning, afternoon, evening, and night, organizing human routines.",
        "simp_exp": "We wake up and brush our teeth in the morning, eat lunch in the afternoon, and sleep at night!",
        "analogies": {
            "space": "The Earth rotates once every 24 hours, bringing sunrise and sunset to our homes.",
            "coding": "Scheduled cron tasks running in sequence: morning backup, evening sync.",
            "animals": "Roosters crow at sunrise; owls hunt during the quiet night."
        },
        "prompt": "Which activity do children typically do in the MORNING right after waking up?",
        "options": ["Brush their teeth and wash up", "Go to sleep for the night", "Eat dinner under stars", "Watch the sunset"],
        "answer": "Brush their teeth and wash up",
        "exp": "Brushing teeth and washing up is the standard healthy morning routine to start the day.",
        "hints": ["Think about what you do first when your alarm rings.", "It helps clean your mouth before breakfast.", "Morning routine starts with brushing teeth."],
        "scaffolds": ["Step 1: Identify the time of day: Morning.", "Step 2: Think about what happens after waking up.", "Step 3: Choose brushing teeth."]
    },
    (1, "Mathematics", 7): {
        "concept_name": "Measurement (Longer vs Shorter)",
        "diff": 1,
        "objectives": ["Compare lengths of objects directly", "Identify longer and shorter items"],
        "prereq": ["Visual comparison"],
        "std_exp": "Length is compared by aligning one endpoint and observing the extent of the other endpoint.",
        "simp_exp": "Line up two pencils at the bottom to see which one stretches higher!",
        "analogies": {
            "space": "Comparing the wingspan of a space shuttle to a satellite antenna.",
            "coding": "Comparing array.length or string length properties.",
            "animals": "A giraffe's neck is much longer than a rabbit's neck."
        },
        "prompt": "Rohan places a long wooden ruler (30 cm) and an eraser (4 cm) side by side. Which object is LONGER?",
        "options": ["The wooden ruler", "The eraser", "Both are equal length", "Cannot be determined"],
        "answer": "The wooden ruler",
        "exp": "The wooden ruler extends much further than the eraser, so the ruler is longer.",
        "hints": ["Imagine a 30 cm ruler and a small rubber eraser.", "Which one would stick out of your pocket?", "The ruler is longer."],
        "scaffolds": ["Step 1: Ruler length = 30 cm.", "Step 2: Eraser length = 4 cm.", "Step 3: 30 cm > 4 cm, so the ruler is longer."]
    },
    (1, "Mathematics", 8): {
        "concept_name": "Patterns & Shape Sequences",
        "diff": 1,
        "objectives": ["Identify repeating patterns", "Predict the next element in a sequence"],
        "prereq": ["Basic geometric shapes"],
        "std_exp": "A pattern is a regular, repeating arrangement of shapes, numbers, or symbols following a rule.",
        "simp_exp": "Circle, Square, Circle, Square... What comes next? Another Circle!",
        "analogies": {
            "space": "Binary signals sent from deep space: Dot, Dash, Dot, Dash, Dot!",
            "coding": "A repeating while loop executing on alternating states.",
            "animals": "The stripes of a zebra alternating black, white, black, white."
        },
        "prompt": "Look at the pattern: Circle, Triangle, Circle, Triangle, Circle, __. Which shape comes next?",
        "options": ["Triangle", "Square", "Circle", "Star"],
        "answer": "Triangle",
        "exp": "The pattern alternates between Circle and Triangle. After Circle comes Triangle.",
        "hints": ["Say the shapes out loud: Circle, Triangle, Circle, Triangle...", "What follows right after Circle in this rule?", "It is Triangle."],
        "scaffolds": ["Step 1: Identify the repeating unit: (Circle, Triangle).", "Step 2: The sequence just had a Circle.", "Step 3: The next shape is Triangle."]
    },

    # --- CLASS 1 SCIENCE (EVS) ---
    (1, "Science", 1): {
        "concept_name": "My Body & Senses",
        "diff": 1,
        "objectives": ["Identify 5 sensory organs", "Associate ears with hearing"],
        "prereq": ["Body parts recognition"],
        "std_exp": "Humans perceive the external world through five primary senses: sight, hearing, smell, taste, and touch.",
        "simp_exp": "Our ears catch sounds so we can hear songs, speech, and bird whistles!",
        "analogies": {
            "space": "Radio antennas on a spacecraft capture sound and telemetry waves.",
            "coding": "Audio input listener and microphone stream in an app.",
            "animals": "A deer twists its ears to detect predator rustling in the forest."
        },
        "prompt": "Which wonderful sensory organ allows you to listen to school bells ringing and your favorite music?",
        "options": ["Ears", "Eyes", "Nose", "Tongue"],
        "answer": "Ears",
        "exp": "Ears detect sound waves from the air, allowing us to hear speech, music, and warning bells.",
        "hints": ["You have two of them on the sides of your head.", "They catch vibrations of sound.", "Ears are for hearing."],
        "scaffolds": ["Step 1: Action = listening to sound.", "Step 2: Organ for hearing = Ears.", "Step 3: Select 'Ears'."]
    },
    (1, "Science", 2): {
        "concept_name": "Animals Around Us",
        "diff": 1,
        "objectives": ["Classify animals by habitat and traits", "Recognize domestic and farm animals"],
        "prereq": ["Common animals recognition"],
        "std_exp": "Domestic animals live close to human settlements and assist in transport, agriculture, and companionship.",
        "simp_exp": "Dogs guard homes, cats catch mice, and cows give fresh healthy milk!",
        "analogies": {
            "space": "Trained support robots on orbital stations assist astronauts with daily chores.",
            "coding": "Helper microservices that handle specific tasks like storage or logging.",
            "animals": "A mother cow grazing peacefully in a pasture providing nutritious milk."
        },
        "prompt": "Which gentle domestic animal provides us with fresh, calcium-rich milk every day?",
        "options": ["Cow", "Lion", "Eagle", "Crocodile"],
        "answer": "Cow",
        "exp": "Cows are gentle herbivorous domestic animals that provide nutritious milk for humans.",
        "hints": ["It says 'moo' and lives on a farm.", "It eats green grass and hay.", "The cow gives milk."],
        "scaffolds": ["Step 1: Characteristic = provides milk on farms.", "Step 2: Match with domestic herbivore: Cow.", "Step 3: Choose 'Cow'."]
    },
    (1, "Science", 3): {
        "concept_name": "Plants & Green Friends",
        "diff": 1,
        "objectives": ["Identify basic plant parts", "Recognize the role of roots in absorbing water"],
        "prereq": ["Observing trees and plants"],
        "std_exp": "Plant roots anchor the plant firmly into the soil and absorb water and dissolved minerals.",
        "simp_exp": "Roots act like underground drinking straws that suck up water from the soil for the green plant!",
        "analogies": {
            "space": "Underground recharge conduits supplying water to a greenhouse hydroponic bay on Mars.",
            "coding": "Database connection pools that draw raw records from underlying storage.",
            "animals": "An elephant using its trunk like a straw to drink fresh water."
        },
        "prompt": "Which part of a plant grows underground and drinks water from the soil to help the plant grow?",
        "options": ["Roots", "Flower", "Fruit", "Leaf"],
        "answer": "Roots",
        "exp": "Roots spread through the soil beneath the ground to absorb water and nutrients for the entire plant.",
        "hints": ["This plant part is hidden beneath the soil.", "It holds the plant firmly like an anchor.", "Roots absorb water."],
        "scaffolds": ["Step 1: Location = underground.", "Step 2: Function = absorbs water.", "Step 3: Plant part is Roots."]
    },
    (1, "Science", 4): {
        "concept_name": "Sun, Moon and Stars",
        "diff": 1,
        "objectives": ["Differentiate daytime sky from nighttime sky", "Identify the Sun as our source of light and warmth"],
        "prereq": ["Day and night awareness"],
        "std_exp": "The Sun is a glowing star at the center of our solar system that provides daylight and thermal energy to Earth.",
        "simp_exp": "The bright golden Sun shines during the day to give us light, warmth, and sunny skies!",
        "analogies": {
            "space": "The Sun is our solar system's central fusion reactor powering all planetary weather.",
            "coding": "The primary power supply powering the motherboard.",
            "animals": "Sunflowers turning their yellow heads to follow the Sun across the sky."
        },
        "prompt": "What bright celestial body shines in the daytime sky, giving our planet Earth bright light and warmth?",
        "options": ["The Sun", "The Moon", "Comets", "Distant Stars"],
        "answer": "The Sun",
        "exp": "The Sun illuminates our sky during daytime and radiates the heat that warms the Earth.",
        "hints": ["It rises in the East and sets in the West.", "It makes the daytime bright and warm.", "It is the Sun."],
        "scaffolds": ["Step 1: Time = daytime sky.", "Step 2: Provides = light and heat.", "Step 3: Choose 'The Sun'."]
    },

    # --- CLASS 1 ENGLISH ---
    (1, "English", 1): {
        "concept_name": "My Family and Me",
        "diff": 1,
        "objectives": ["Identify family relations", "Use polite conversational vocabulary"],
        "prereq": ["Spoken English vocabulary"],
        "std_exp": "Immediate family relationships include parents (father, mother), siblings (brother, sister), and grandparents.",
        "simp_exp": "Your father's father is your loving grandfather!",
        "analogies": {
            "space": "A constellation of stars bound together by gentle gravity.",
            "coding": "A class hierarchy with parent classes and inherited attributes.",
            "animals": "A lion pride where cubs play safely under the watch of their parents."
        },
        "prompt": "What do you call your father's father in your loving family?",
        "options": ["Grandfather", "Brother", "Uncle", "Nephew"],
        "answer": "Grandfather",
        "exp": "Your father's father (or mother's father) is known as your grandfather.",
        "hints": ["He is the parent of your parent.", "He is older and tells wonderful bedtime stories.", "He is your grandfather."],
        "scaffolds": ["Step 1: Relation = father's father.", "Step 2: English term = Grandfather.", "Step 3: Select 'Grandfather'."]
    },
    (1, "English", 2): {
        "concept_name": "Fun with Words & Rhymes",
        "diff": 1,
        "objectives": ["Identify rhyming phonemic endings", "Recognize CVC word patterns"],
        "prereq": ["Letter phonics sounds"],
        "std_exp": "Rhyming words share the same terminating vowel and consonant phonemes (e.g. -at in cat/bat/hat).",
        "simp_exp": "Words that end with the exact same twin sound rhyme, like CAT and HAT!",
        "analogies": {
            "space": "Modular space station couplers that have the exact same shape to connect.",
            "coding": "Strings that end with the identical suffix: string.endsWith('at').",
            "animals": "A playful cat wearing a funny pointed hat!"
        },
        "prompt": "Which word rhymes with the word 'CAT' because it ends with the exact same sound?",
        "options": ["HAT", "DOG", "SUN", "PEN"],
        "answer": "HAT",
        "exp": "CAT and HAT both end with the '-at' sound: c-at and h-at.",
        "hints": ["Say the words aloud: C-AT... H-...", "Which word ends with '-at'?", "HAT rhymes with CAT."],
        "scaffolds": ["Step 1: Ending sound of CAT = '-at'.", "Step 2: Test options: DOG (-og), SUN (-un), HAT (-at).", "Step 3: Choose 'HAT'."]
    },
    (1, "English", 3): {
        "concept_name": "Animals and Nature Tales",
        "diff": 1,
        "objectives": ["Identify character traits in stories", "Recognize Mittu the parrot's features"],
        "prereq": ["Listening comprehension"],
        "std_exp": "Mittu was a bright green parrot with a sharp red beak who loved flying in the blue sky and eating sweet yellow mangoes.",
        "simp_exp": "Mittu is a green parrot with a cute red beak who used a red balloon to outsmart a greedy crow!",
        "analogies": {
            "space": "A clever explorer using a reflective decoy balloon to safely pass an asteroid obstacle.",
            "coding": "Using a mock object to distract an error-handling interceptor.",
            "animals": "A clever parrot using sound mimicry to protect its favorite fruit tree."
        },
        "prompt": "In the delightful story 'Mittu and the Yellow Mango', what color was clever Mittu the parrot?",
        "options": ["Green with a red beak", "Purple with a yellow beak", "All black like a crow", "Blue with white spots"],
        "answer": "Green with a red beak",
        "exp": "Mittu was a green parrot who had a lovely red beak and loved eating mangoes.",
        "hints": ["Think about standard parrots in trees.", "Their feathers are green.", "Mittu was green with a red beak."],
        "scaffolds": ["Step 1: Character = Mittu the parrot.", "Step 2: Parrots have green feathers and red beaks.", "Step 3: Select 'Green with a red beak'."]
    },
    (1, "English", 4): {
        "concept_name": "Colors of the Rainbow",
        "diff": 1,
        "objectives": ["Name rainbow colors", "Use color descriptive adjectives"],
        "prereq": ["Color identification"],
        "std_exp": "White sunlight passing through rain droplets refracts into the visible rainbow spectrum: Violet, Indigo, Blue, Green, Yellow, Orange, and Red (VIBGYOR).",
        "simp_exp": "When sunlight shines through raindrops after rain, a beautiful rainbow of 7 colors arcs across the sky!",
        "analogies": {
            "space": "Spectroscopy breaking starlight into frequency bands to detect planetary atmospheres.",
            "coding": "CSS hex color gamut rendering RGB color spectra across digital displays.",
            "animals": "Peacock feathers shimmering with iridescent green, blue, and gold hues."
        },
        "prompt": "How many vibrant colors can you count in a glorious sky rainbow after a rain shower?",
        "options": ["7 colors", "3 colors", "12 colors", "5 colors"],
        "answer": "7 colors",
        "exp": "A natural rainbow has 7 colors: Violet, Indigo, Blue, Green, Yellow, Orange, and Red (VIBGYOR).",
        "hints": ["Remember the acronym V-I-B-G-Y-O-R.", "Count the letters: V, I, B, G, Y, O, R.", "There are 7 colors."],
        "scaffolds": ["Step 1: Recall rainbow acronym: VIBGYOR.", "Step 2: Count the colors: 1 to 7.", "Step 3: Total is 7 colors."]
    },

    # =========================================================================
    # CLASS 2
    # =========================================================================
    (2, "Mathematics", 1): {
        "concept_name": "What is Long, What is Round?",
        "diff": 2,
        "objectives": ["Distinguish rolling objects from sliding objects", "Identify spherical vs flat shapes"],
        "prereq": ["Basic 3D shapes recognition"],
        "std_exp": "Objects with curved spherical surfaces roll easily, whereas objects with flat planar faces slide along surfaces.",
        "simp_exp": "A round football ROLLS along the grass, while a flat wooden block SLIDES on the table!",
        "analogies": {
            "space": "Planets roll through gravitational curves, while solar panels slide open on flat rails.",
            "coding": "Ball physics colliders (sphere collider vs box collider in game engines).",
            "animals": "A round armadillo curls into a ball and rolls down a grassy slope."
        },
        "prompt": "Which of the following common objects will smoothly ROLL across the floor because it has a round, curved surface?",
        "options": ["A round tennis ball", "A flat matchbox", "A rectangular book", "A square wooden dice"],
        "answer": "A round tennis ball",
        "exp": "A tennis ball is spherical with a curved surface all around, which enables it to roll smoothly.",
        "hints": ["Think about what happens when you push each item on a ramp.", "Flat objects slide, curved round objects roll.", "A ball rolls."],
        "scaffolds": ["Step 1: Rolling requires curved surfaces.", "Step 2: Tennis ball is round sphere.", "Step 3: Select 'A round tennis ball'."]
    },
    (2, "Mathematics", 2): {
        "concept_name": "Counting in Groups",
        "diff": 2,
        "objectives": ["Count in pairs and bundles of 10", "Understand multiplication foundations"],
        "prereq": ["Counting up to 50"],
        "std_exp": "Grouping items into equal sets (like pairs of 2 or bundles of 10) allows efficient skip-counting.",
        "simp_exp": "If you have 4 pairs of socks, count by twos: 2, 4, 6, 8 socks in total!",
        "analogies": {
            "space": "Array thrusters firing in paired sets of 2 for balanced attitude control.",
            "coding": "Batch processing items in fixed chunks of 2 or 10.",
            "animals": "Birds flying in pairs across the sunset sky."
        },
        "prompt": "Karan arranged his shoes neatly in pairs. If there are 5 pairs of shoes on the rack, how many individual shoes are there?",
        "options": ["10 shoes", "7 shoes", "5 shoes", "12 shoes"],
        "answer": "10 shoes",
        "exp": "Each pair has 2 shoes. 5 pairs = 5 × 2 = 10 shoes (2, 4, 6, 8, 10).",
        "hints": ["Each pair means 2 shoes.", "Skip count by 2s five times: 2, 4, 6, 8, 10.", "5 × 2 = 10."],
        "scaffolds": ["Step 1: 1 pair = 2 shoes.", "Step 2: 5 pairs = 2 + 2 + 2 + 2 + 2.", "Step 3: 5 × 2 = 10 shoes."]
    },
    (2, "Mathematics", 3): {
        "concept_name": "How Much Can You Carry? (Weight)",
        "diff": 2,
        "objectives": ["Compare weights using a balance beam", "Distinguish heavier vs lighter"],
        "prereq": ["Basic measurement comparison"],
        "std_exp": "On a two-pan balance scale, the pan holding the heavier object tilts downwards due to gravitational pull.",
        "simp_exp": "The heavier side of a seesaw goes down, and the lighter side goes up in the air!",
        "analogies": {
            "space": "Mass calibration sensors balancing payload mass before space liftoff.",
            "coding": "Comparison operators: if (weightA > weightB) return heavier.",
            "animals": "A heavy elephant easily pushes down the seesaw against a light squirrel."
        },
        "prompt": "When comparing two objects on a two-pan balance scale, what happens to the pan holding the HEAVIER object?",
        "options": ["It goes down", "It goes up in the air", "It stays completely floating", "It disappears"],
        "answer": "It goes down",
        "exp": "Gravity pulls with greater force on greater mass, causing the heavier pan to tilt downwards.",
        "hints": ["Think about playing on a seesaw with a friend who is heavier than you.", "The heavier side pushes down.", "The heavier pan goes down."],
        "scaffolds": ["Step 1: Recall how balance scales work.", "Step 2: Greater weight pulls downward.", "Step 3: Pan goes down."]
    },
    (2, "Mathematics", 4): {
        "concept_name": "Counting in Tens & Tens and Ones",
        "diff": 2,
        "objectives": ["Identify 2-digit place values", "Expand numbers into Tens and Ones"],
        "prereq": ["Numbers up to 100"],
        "std_exp": "In the base-10 system, a 2-digit number $AB$ has place value $10 \times A + B$.",
        "simp_exp": "The number 46 has 4 tens (40) and 6 ones (6)!",
        "analogies": {
            "space": "4 rocket fuel booster tanks of 10 tons each plus 6 single fuel canisters.",
            "coding": "Integer division by 10 to extract quotient (tens) and modulus (% 10) for ones.",
            "animals": "4 nests with 10 eggs each, plus 6 eggs in a small nest = 46 eggs."
        },
        "prompt": "How is the number 46 broken down into Tens and Ones?",
        "options": ["4 Tens and 6 Ones", "6 Tens and 4 Ones", "40 Tens and 6 Ones", "46 Tens and 0 Ones"],
        "answer": "4 Tens and 6 Ones",
        "exp": "46 consists of 4 tens (40) and 6 ones (6): 40 + 6 = 46.",
        "hints": ["Look at the left digit (tens place): 4.", "Look at the right digit (ones place): 6.", "4 Tens and 6 Ones."],
        "scaffolds": ["Step 1: Tens place digit = 4 (value 40).", "Step 2: Ones place digit = 6 (value 6).", "Step 3: 4 Tens and 6 Ones."]
    },
    (2, "Mathematics", 5): {
        "concept_name": "Patterns in Nature and Numbers",
        "diff": 2,
        "objectives": ["Identify 2-digit number patterns", "Solve skip-counting sequences"],
        "prereq": ["Skip counting by 5s and 10s"],
        "std_exp": "An arithmetic pattern has a constant common difference between consecutive terms.",
        "simp_exp": "Look at the jumps: 10, 20, 30, 40... each step jumps forward by 10!",
        "analogies": {
            "space": "Periodic beacon pulses emitting every 10 milliseconds from an orbital satellite.",
            "coding": "A for-loop: for (let i = 10; i <= 50; i += 10).",
            "animals": "A frog hopping forward 10 lily pads with every giant leap."
        },
        "prompt": "Look at the jumping sequence: 10, 20, 30, 40, __. What number comes next?",
        "options": ["50", "45", "60", "41"],
        "answer": "50",
        "exp": "The numbers increase by 10 at each step. 40 + 10 = 50.",
        "hints": ["Notice the pattern: 10, 20, 30, 40...", "Each number adds 10.", "40 + 10 = 50."],
        "scaffolds": ["Step 1: Find step difference: 20 - 10 = 10.", "Step 2: Add 10 to 40.", "Step 3: 40 + 10 = 50."]
    },
    (2, "Mathematics", 6): {
        "concept_name": "Jugs and Mugs (Liquid Capacity)",
        "diff": 2,
        "objectives": ["Compare liquid capacities", "Estimate container volumes using non-standard units"],
        "prereq": ["Volume comparison"],
        "std_exp": "Capacity refers to the amount of liquid a container can hold, with larger vessels holding multiples of smaller cups.",
        "simp_exp": "A big water bucket holds much more water than a tiny tea cup!",
        "analogies": {
            "space": "Fuel tank capacity on a space transport module holding thousands of liters of propellants.",
            "coding": "Buffer capacity allocation: allocating a larger memory buffer for audio streams.",
            "animals": "A camel drinking gallons of water to fill its reservoir for long desert journeys."
        },
        "prompt": "Which container can hold the LARGEST volume of drinking water?",
        "options": ["A large water bucket", "A small tea cup", "A plastic spoon", "A medicine dropper"],
        "answer": "A large water bucket",
        "exp": "A bucket has a much larger physical capacity (several liters) compared to small cups or spoons.",
        "hints": ["Think about which container you use to take a bath or wash clothes.", "A cup holds only a little water, a bucket holds a lot.", "The bucket holds the largest volume."],
        "scaffolds": ["Step 1: Compare volumes of items.", "Step 2: Spoon < Cup < Bucket.", "Step 3: Bucket is largest."]
    },
    (2, "Mathematics", 7): {
        "concept_name": "Add Our Points & Give and Take",
        "diff": 2,
        "objectives": ["Perform 2-digit addition without carryover", "Solve simple addition word problems"],
        "prereq": ["Single-digit addition", "Place value tens and ones"],
        "std_exp": "Adding two 2-digit numbers involves summing the ones column and then summing the tens column.",
        "simp_exp": "Add the ones first: 3 + 4 = 7. Then add the tens: 2 + 1 = 3. Together: 37!",
        "analogies": {
            "space": "Combining battery charge from two solar panel arrays: 23 watts + 14 watts = 37 watts.",
            "coding": "Adding values of two numeric objects field by field.",
            "animals": "23 honeybees in one flower bed plus 14 honeybees in another: 37 bees collecting pollen."
        },
        "prompt": "Anusha scored 23 points in a ring toss game. In the second round, she scored 14 more points. What is her total score?",
        "options": ["37 points", "35 points", "27 points", "40 points"],
        "answer": "37 points",
        "exp": "Add ones: 3 + 4 = 7. Add tens: 2 + 1 = 3. Total score = 37 points.",
        "hints": ["Add ones: 3 + 4 = 7.", "Add tens: 20 + 10 = 30.", "30 + 7 = 37."],
        "scaffolds": ["Step 1: Tens: 20 + 10 = 30.", "Step 2: Ones: 3 + 4 = 7.", "Step 3: 30 + 7 = 37."]
    },

    # --- CLASS 2 SCIENCE (EVS) ---
    (2, "Science", 1): {
        "concept_name": "Our Food & Healthy Eating",
        "diff": 2,
        "objectives": ["Classify food by origin (plant vs animal)", "Recognize milk and eggs as animal products"],
        "prereq": ["Common foods recognition"],
        "std_exp": "Human food originates from two primary sources: plants (grains, fruits, vegetables) and animals (dairy, eggs, honey).",
        "simp_exp": "Apples and carrots come from plants, while eggs and milk come from animals!",
        "analogies": {
            "space": "Astronaut nutrition packets labeled as either synthetic hydroponic plant produce or biological protein rations.",
            "coding": "Data source routing: filterBySource('PLANT') vs filterBySource('ANIMAL').",
            "animals": "Honeybees collecting nectar to produce sweet honey."
        },
        "prompt": "Which of the following healthy foods is obtained directly from domestic farm ANIMALS?",
        "options": ["Fresh milk", "Wheat flour", "Ripe bananas", "Green spinach leaves"],
        "answer": "Fresh milk",
        "exp": "Milk is obtained from dairy animals such as cows, buffaloes, and goats. Wheat, bananas, and spinach come from plants.",
        "hints": ["Wheat, bananas, and spinach grow on plants in the soil.", "Cows and goats provide this white drink.", "Milk comes from animals."],
        "scaffolds": ["Step 1: Identify animal source.", "Step 2: Cows produce milk.", "Step 3: Select 'Fresh milk'."]
    },
    (2, "Science", 2): {
        "concept_name": "Water - Every Drop Counts",
        "diff": 2,
        "objectives": ["Identify primary freshwater source", "Recognize rain as the origin of rivers and lakes"],
        "prereq": ["Water uses in daily life"],
        "std_exp": "Rain is the primary natural source of freshwater on Earth, replenishing surface reservoirs and underground aquifers.",
        "simp_exp": "When clouds condense, rain falls from the sky to fill our lakes, rivers, ponds, and wells!",
        "analogies": {
            "space": "Atmospheric water recycling systems capturing evaporated moisture on the space station.",
            "coding": "The primary upstream data pipeline that populates all downstream read replicas.",
            "animals": "Frogs singing joyfully when monsoon rain fills the pond."
        },
        "prompt": "What is the primary natural source of fresh water on Earth that fills our rivers, lakes, and ponds?",
        "options": ["Rain", "Sea water", "Swimming pools", "Plastic bottles"],
        "answer": "Rain",
        "exp": "Rain is the primary natural source of freshwater that fills rivers, lakes, and recharges underground groundwater.",
        "hints": ["It falls from gray clouds in the monsoon sky.", "It is fresh, sweet water, unlike salty ocean water.", "Rain fills rivers and lakes."],
        "scaffolds": ["Step 1: Primary natural source = Rain.", "Step 2: Replenishes rivers and groundwater.", "Step 3: Choose 'Rain'."]
    },
    (2, "Science", 3): {
        "concept_name": "Shelters of Living Things",
        "diff": 2,
        "objectives": ["Match animals with their natural shelters", "Recognize bird nests"],
        "prereq": ["Animal recognition"],
        "std_exp": "Animals construct or inhabit specific shelters for protection against weather, predators, and to rear offspring.",
        "simp_exp": "Birds carefully weave twigs, grass, and feathers to build warm nests for their baby eggs!",
        "analogies": {
            "space": "Orbital habitat modules providing thermal shielding, radiation barriers, and life support for astronauts.",
            "coding": "Encapsulated secure sandbox containers isolating processes from external interference.",
            "animals": "A tailor bird sewing two large leaves together with plant fiber to create a cozy cradle."
        },
        "prompt": "Which cozy shelter does a mother bird carefully build with twigs, grass, and leaves to protect her fragile eggs?",
        "options": ["A nest", "A kennel", "A beehive", "A spider web"],
        "answer": "A nest",
        "exp": "Birds construct nests in tree branches or safe crevices to lay eggs and nurture their baby chicks.",
        "hints": ["It is built high up in tree branches using dry twigs.", "Baby birds hatch out of eggs inside it.", "Birds build nests."],
        "scaffolds": ["Step 1: Creature = bird.", "Step 2: Bird shelter = nest.", "Step 3: Select 'A nest'."]
    },
    (2, "Science", 4): {
        "concept_name": "Seasons and Weather",
        "diff": 2,
        "objectives": ["Connect clothing with weather seasons", "Understand thermal insulation of woolen clothes"],
        "prereq": ["Hot and cold sensations"],
        "std_exp": "Woolen clothing traps pockets of still air, which act as thermal insulators to retain body heat during cold winters.",
        "simp_exp": "In the cold winter season, we wear warm woolen sweaters, scarves, and mittens to keep our bodies cozy!",
        "analogies": {
            "space": "Multi-layer insulation (MLI) blankets wrapping satellites to protect instruments from freezing deep-space cold.",
            "coding": "Rate limiters and circuit breakers shielding core services during high traffic surges.",
            "animals": "Sheep growing thick fluffy wool coats that trap air and block freezing mountain winds."
        },
        "prompt": "During which chilly season do people wear warm woolen sweaters, woolen caps, and jackets?",
        "options": ["Winter", "Summer", "Monsoon", "Spring"],
        "answer": "Winter",
        "exp": "Winter is the cold season when temperatures drop, so people wear woolen garments to trap body heat.",
        "hints": ["Think about when it feels frosty and cold outside.", "You drink hot soup and wear sweaters.", "It is winter."],
        "scaffolds": ["Step 1: Woolen clothes provide warmth.", "Step 2: Needed when temperatures are cold.", "Step 3: Cold season = Winter."]
    },

    # --- CLASS 2 ENGLISH ---
    (2, "English", 1): {
        "concept_name": "First Day at School & Adventure",
        "diff": 2,
        "objectives": ["Recall story details from Haldi's Adventure", "Recognize character features"],
        "prereq": ["Story comprehension"],
        "std_exp": "In 'Haldi's Adventure', Haldi meets a polite talking giraffe named Smiley who wears spectacles and carries a book.",
        "simp_exp": "Haldi met Smiley the friendly giraffe on her way to school. Smiley wore big glasses and carried a book!",
        "analogies": {
            "space": "Meeting an unexpected friendly robot guide during a deep space expedition.",
            "coding": "A helpful terminal assistant providing friendly tips during a new project build.",
            "animals": "A tall, gentle giraffe bending its long neck to greet a child."
        },
        "prompt": "In the story 'Haldi's Adventure', what unusual accessory was Smiley the friendly giraffe wearing?",
        "options": ["Big glasses (spectacles)", "A gold watch on his tail", "A red party hat", "Blue swimming flippers"],
        "answer": "Big glasses (spectacles)",
        "exp": "Smiley the giraffe wore large glasses (spectacles) and held a book in his hand when Haldi met him.",
        "hints": ["He wore them over his eyes to read books.", "They helped him see clearly.", "He wore glasses (spectacles)."],
        "scaffolds": ["Step 1: Character = Smiley the giraffe.", "Step 2: Look at his face in the illustration.", "Step 3: He wore glasses (spectacles)."]
    },
    (2, "English", 2): {
        "concept_name": "I am Lucky! & Animal Smiles",
        "diff": 2,
        "objectives": ["Identify rhyming structure and gratitude themes", "Express appreciation for nature"],
        "prereq": ["Reading with expression"],
        "std_exp": "The poem 'I am Lucky' celebrates self-acceptance and gratitude for unique gifts, like a butterfly's wings or an elephant's trunk.",
        "simp_exp": "The poem says: If I were a butterfly, I would be thankful for my colorful wings!",
        "analogies": {
            "space": "Every satellite is thankful for its unique sensor payload designed for a specific planetary mission.",
            "coding": "Poly-morphic methods where each subclass has its own specialized function.",
            "animals": "A butterfly fluttering gracefully from flower to flower with bright painted wings."
        },
        "prompt": "In the joyful poem 'I am Lucky', what is the butterfly thankful for?",
        "options": ["For its colorful wings", "For its ability to swim fast", "For its sharp eagle claws", "For its heavy shell"],
        "answer": "For its colorful wings",
        "exp": "The poem begins: 'If I were a butterfly, I would be thankful for my wings.'",
        "hints": ["What helps a butterfly fly among flowers?", "Butterflies have beautiful painted wings.", "It is thankful for its wings."],
        "scaffolds": ["Step 1: Animal = Butterfly.", "Step 2: Key feature = Wings.", "Step 3: Thankful for its wings."]
    },
    (2, "English", 3): {
        "concept_name": "Elements of Nature - The Wind and the Sun",
        "diff": 2,
        "objectives": ["Identify narrative moral", "Understand gentle persuasion vs brute force"],
        "prereq": ["Story comprehension"],
        "std_exp": "In the fable 'The Wind and the Sun', gentle warmth succeeds in making a traveler take off his coat where fierce blowing fails.",
        "simp_exp": "Gentleness and warmth are stronger than cold fury and brute force!",
        "analogies": {
            "space": "Using gentle continuous ion propulsion to maneuver orbits rather than violent explosions.",
            "coding": "Graceful degradation and gentle error recovery over abrupt crash termination.",
            "animals": "A mother swan gently nudging her cygnets into water with soft soothing sounds."
        },
        "prompt": "In the classic fable 'The Wind and the Sun', how did the Sun successfully make the man take off his heavy coat?",
        "options": ["By shining warmly and brightly", "By blowing freezing gale winds", "By sending a thunder storm", "By asking a robber to take it"],
        "answer": "By shining warmly and brightly",
        "exp": "The Sun shone brighter and warmer, making the man feel hot so that he took off his coat gladly.",
        "hints": ["The Wind tried blowing hard, but the man held his coat tighter.", "Then the Sun began to shine warmly.", "The Sun shone brightly and warmly."],
        "scaffolds": ["Step 1: Wind's force failed.", "Step 2: Sun used warmth and brightness.", "Step 3: Man took off coat because of warmth."]
    },
    (2, "English", 4): {
        "concept_name": "Stories of Magic - The Magic Porridge Pot",
        "diff": 2,
        "objectives": ["Identify magic story triggers", "Recognize magic command phrases"],
        "prereq": ["Story sequencing"],
        "std_exp": "In 'The Magic Porridge Pot', the magic cooking phrase is 'Cook, pot, cook' and the stop command is 'Stop, pot, stop'.",
        "simp_exp": "To make the magic pot cook delicious porridge, Tara said: 'Cook, pot, cook!'",
        "analogies": {
            "space": "Executing automated robotic assembly sequence via voice activation keyword: START_SEQUENCE.",
            "coding": "Invoking a loop function: startGenerator() vs stopGenerator().",
            "animals": "An obedient dog performing tricks when hearing a specific clear vocal cue."
        },
        "prompt": "In the folktale 'The Magic Porridge Pot', what magic words did little Tara say to make the pot start cooking sweet porridge?",
        "options": ["Cook, pot, cook!", "Open sesame!", "Fly, pot, fly!", "Sleep, pot, sleep!"],
        "answer": "Cook, pot, cook!",
        "exp": "The kind old woman taught Tara to say 'Cook, pot, cook' to start cooking porridge.",
        "hints": ["It tells the pot what action to do: cook.", "It repeats the word cook.", "Tara said: 'Cook, pot, cook!'"],
        "scaffolds": ["Step 1: Action = cooking porridge.", "Step 2: Magic phrase = 'Cook, pot, cook!'.", "Step 3: Select 'Cook, pot, cook!'."]
    }
}
