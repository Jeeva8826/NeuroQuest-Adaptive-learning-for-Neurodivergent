"""
Authentic NCERT Academic Questions Catalog for Middle School: Classes 6, 7, and 8
Subjects: Mathematics, Science, English (55 chapters total)
"""

SECONDARY_678_QUESTIONS = {
    # =========================================================================
    # CLASS 6 (19 Chapters: 8 Math, 7 Science, 4 English)
    # =========================================================================
    # --- Mathematics (8 Chapters) ---
    (6, "Mathematics", 1): {
        "concept_name": "Knowing Our Numbers (Place Value & Rounding)",
        "diff": 2,
        "objectives": ["Understand Indian and International place value notation", "Round numbers to nearest hundred and thousand"],
        "prereq": ["4-digit numbers and basic place value"],
        "std_exp": "The Indian place value system groups digits as ones, tens, hundreds, thousands, ten thousands, lakhs, and crores. In rounding to the nearest hundred, if the tens digit is 5 or greater, round up.",
        "simp_exp": "To round 4,762 to the nearest hundred, look at the tens digit (6). Since 6 >= 5, 762 rounds up to 800, giving 4,800!",
        "analogies": {
            "space": "Telemetry distances rounded to nearest thousand kilometers for orbital flight safety corridors.",
            "coding": "Using Math.round() or formatting floating point integers to significant digits.",
            "animals": "Counting a migratory flock of flamingos in rounded clusters of hundreds."
        },
        "prompt": "According to the Indian place value system, how is the number 7,54,320 written in words, and what is its value when rounded to the nearest thousand?",
        "options": [
            "Seven lakh fifty-four thousand three hundred twenty; rounded to nearest thousand is 7,54,000",
            "Seven million fifty-four thousand; rounded to nearest thousand is 7,55,000",
            "Seventy-five thousand four hundred thirty-two; rounded is 75,000",
            "Seven lakh five thousand four hundred twenty; rounded is 7,00,000"
        ],
        "answer": "Seven lakh fifty-four thousand three hundred twenty; rounded to nearest thousand is 7,54,000",
        "exp": "7,54,320 is 'Seven lakh fifty-four thousand three hundred twenty'. The hundreds digit is 3 (< 5), so rounding to the nearest thousand gives 7,54,000.",
        "hints": ["Check the periods: lakhs, thousands, hundreds.", "To round to nearest thousand, check the hundreds digit (3).", "Since 3 is less than 5, keep the thousands digit as 4."],
        "scaffolds": ["Step 1: Read periods: 7 (lakhs), 54 (thousands), 320 (ones).", "Step 2: Check hundreds digit: 3 < 5.", "Step 3: 7,54,320 rounds down to 7,54,000."]
    },
    (6, "Mathematics", 2): {
        "concept_name": "Whole Numbers (Properties & Number Line)",
        "diff": 2,
        "objectives": ["Identify predecessor and successor", "Apply closure and commutative properties of whole numbers"],
        "prereq": ["Natural numbers and place values"],
        "std_exp": "Whole numbers include all natural numbers along with 0 (W = {0, 1, 2, ...}). Addition and multiplication are commutative: a + b = b + a and a * b = b * a.",
        "simp_exp": "The successor of a number is +1, and the predecessor is -1. 0 has no predecessor in whole numbers! Also, 14 + 27 gives the exact same result as 27 + 14.",
        "analogies": {
            "space": "Countdown clock: T-minus 1 is predecessor, T-plus 1 is successor, and T-0 is whole number origin.",
            "coding": "Zero-indexed arrays where indices are whole numbers [0, 1, 2, ...].",
            "animals": "A mother duck leading a line of ducklings where duckling 0 is right behind mother."
        },
        "prompt": "Which of the following statements about whole numbers is TRUE?",
        "options": [
            "Every whole number has a successor, but 0 does not have a predecessor in whole numbers",
            "Division by zero yields a whole number equal to zero",
            "Subtraction of any two whole numbers always gives a whole number",
            "The natural number 1 has no predecessor in natural numbers or whole numbers"
        ],
        "answer": "Every whole number has a successor, but 0 does not have a predecessor in whole numbers",
        "exp": "Whole numbers start at 0 (0, 1, 2, ...). 0 has no predecessor in the set of whole numbers, but every whole number n has successor n+1. Division by 0 is undefined.",
        "hints": ["What comes before zero in whole numbers?", "Are negative numbers included in whole numbers?", "Whole numbers start at 0, so 0 has no predecessor in whole numbers."],
        "scaffolds": ["Step 1: Recall definition of W = {0, 1, 2, 3...}.", "Step 2: Predecessor means n - 1.", "Step 3: 0 - 1 = -1, which is not a whole number."]
    },
    (6, "Mathematics", 3): {
        "concept_name": "Playing with Numbers (HCF, LCM & Divisibility)",
        "diff": 2,
        "objectives": ["Find HCF and LCM of given numbers", "Apply divisibility rules for 3, 6, and 9"],
        "prereq": ["Multiplication tables and factors"],
        "std_exp": "The Highest Common Factor (HCF) is the greatest factor common to given numbers. The Lowest Common Multiple (LCM) is the smallest positive multiple common to all.",
        "simp_exp": "For 12 and 18: Factors of 12 are 1, 2, 3, 4, 6, 12. Factors of 18 are 1, 2, 3, 6, 9, 18. The greatest shared factor is 6 (HCF). Smallest common multiple is 36 (LCM)!",
        "analogies": {
            "space": "Two orbital satellites align at the same point every LCM of their orbital periods.",
            "coding": "Clock sync intervals in distributed computing using lowest common multiples.",
            "animals": "Two cicada broods emerging every 3 and 4 years will synchronize emergence every LCM(3,4) = 12 years."
        },
        "prompt": "Two neon signs blink at intervals of 12 seconds and 18 seconds respectively. If they blink together at 8:00 PM, after how many seconds will they next blink together simultaneously?",
        "options": ["36 seconds", "24 seconds", "48 seconds", "72 seconds"],
        "answer": "36 seconds",
        "exp": "The simultaneous blink time is the LCM of 12 and 18. Multiples of 12: 12, 24, 36, 48... Multiples of 18: 18, 36, 54... The lowest common multiple is 36.",
        "hints": ["We need the smallest common multiple of 12 and 18.", "List the multiples of 18: 18, 36, 54...", "Is 36 divisible by 12? Yes: 12 * 3 = 36."],
        "scaffolds": ["Step 1: Identify that simultaneous occurrence requires LCM.", "Step 2: Prime factors: 12 = 2^2 * 3, 18 = 2 * 3^2.", "Step 3: LCM = 2^2 * 3^2 = 4 * 9 = 36 seconds."]
    },
    (6, "Mathematics", 4): {
        "concept_name": "Basic Geometrical Ideas (Points, Lines & Polygons)",
        "diff": 2,
        "objectives": ["Distinguish between ray, line, and line segment", "Identify vertices, sides, and diagonals of polygons"],
        "prereq": ["Basic 2D shapes"],
        "std_exp": "A line segment has two fixed endpoints and a definite length. A ray extends infinitely in one direction with one endpoint. A line extends infinitely in both directions.",
        "simp_exp": "A line segment is like a ruler with two ends [A------B]. A sunbeam is a ray starting at the sun and shooting into space. A highway that never ends in both directions is a line!",
        "analogies": {
            "space": "A laser beam fired from a satellite into deep space is a geometric ray.",
            "coding": "Raycasting algorithm in 3D game engines shooting visual rays from the camera.",
            "animals": "A spider's dragline anchored at point A and point B forms a line segment."
        },
        "prompt": "Which of the following geometric figures has exactly ONE endpoint and extends infinitely in the other direction?",
        "options": ["Ray", "Line segment", "Straight line", "Diagonal"],
        "answer": "Ray",
        "exp": "A ray has one starting endpoint (origin) and extends endlessly in one direction (e.g., ray AB starts at A and goes through B endlessly).",
        "hints": ["Think about a sunbeam or flashlight beam.", "It starts at the bulb and goes outward forever.", "This figure is called a ray."],
        "scaffolds": ["Step 1: Line segment has 2 endpoints.", "Step 2: Line has 0 endpoints (infinite in both directions).", "Step 3: Ray has exactly 1 endpoint."]
    },
    (6, "Mathematics", 5): {
        "concept_name": "Integers (Number Line & Signed Arithmetic)",
        "diff": 2,
        "objectives": ["Plot negative and positive integers on a number line", "Solve additions and subtractions with directed numbers"],
        "prereq": ["Whole numbers"],
        "std_exp": "Integers include positive numbers, negative numbers, and zero (Z = {..., -3, -2, -1, 0, 1, 2, 3, ...}). Subtracting a negative number is equivalent to adding its opposite: a - (-b) = a + b.",
        "simp_exp": "Think of temperature: If it is -5°C and the temperature drops by 3°C, it becomes -8°C. If it warms up by 10°C from -5°C, -5 + 10 = +5°C!",
        "analogies": {
            "space": "Altitude: 100 meters above sea level is +100, 50 meters below sea level in an ocean trench is -50.",
            "coding": "Signed integer data types (int8, int32) storing positive and negative magnitudes with two's complement.",
            "animals": "A penguin diving 15 meters below sea level (-15m) and leaping 2 meters above sea level (+2m)."
        },
        "prompt": "In Leh Ladakh, the temperature on Monday night was -4°C. On Tuesday, the temperature dropped by another 6°C. What was the temperature on Tuesday?",
        "options": ["-10°C", "-2°C", "2°C", "10°C"],
        "answer": "-10°C",
        "exp": "Starting at -4°C, dropping by 6°C means moving 6 units to the left on the number line: -4 - 6 = -(4 + 6) = -10°C.",
        "hints": ["A drop in temperature means subtraction.", "Start at -4 on the number line and move left by 6.", "-4 - 6 = -10."],
        "scaffolds": ["Step 1: Initial temperature = -4°C.", "Step 2: Temperature drop = - 6°C.", "Step 3: -4 - 6 = -10°C."]
    },
    (6, "Mathematics", 6): {
        "concept_name": "Fractions and Decimals (Equivalent Fractions)",
        "diff": 2,
        "objectives": ["Identify proper, improper, and mixed fractions", "Compute equivalent fractions and convert to decimals"],
        "prereq": ["Fraction basics"],
        "std_exp": "A proper fraction has numerator < denominator. An improper fraction has numerator >= denominator. To convert 3/4 to a decimal, divide 3 by 4 = 0.75.",
        "simp_exp": "If you eat 3 out of 4 pizza slices, you ate 3/4. Multiply top and bottom by 25: (3 * 25) / (4 * 25) = 75/100 = 0.75!",
        "analogies": {
            "space": "Fuel tank showing 3/4 capacity indicator in mission control telemetry.",
            "coding": "Converting fixed-point fractions into floating-point numbers in computer memory.",
            "animals": "A hummingbird spending 3/4 of its waking day foraging nectar."
        },
        "prompt": "A carpenter cuts 3/5 of a wooden plank. Which of the following is equivalent to 3/5 in decimal notation?",
        "options": ["0.6", "0.35", "0.53", "0.15"],
        "answer": "0.6",
        "exp": "3/5 can be converted to decimal by multiplying numerator and denominator by 2: (3 * 2) / (5 * 2) = 6/10 = 0.6.",
        "hints": ["Convert the denominator 5 to 10.", "Multiply both top and bottom by 2.", "3 * 2 = 6, and 6/10 = 0.6."],
        "scaffolds": ["Step 1: Fraction is 3/5.", "Step 2: Equivalent fraction with base 10 = (3 * 2)/(5 * 2) = 6/10.", "Step 3: 6/10 = 0.6."]
    },
    (6, "Mathematics", 7): {
        "concept_name": "Introduction to Algebra (Variables & Expressions)",
        "diff": 2,
        "objectives": ["Understand the concept of variable as an unknown quantity", "Form linear algebraic expressions from word statements"],
        "prereq": ["Arithmetic operations"],
        "std_exp": "A variable represents an unknown quantity denoted by letters like x, y, n. An expression combines variables, constants, and operators without an equals sign.",
        "simp_exp": "If making one matchstick square takes 4 matchsticks, making 'n' squares takes 4 * n matchsticks. Here 'n' is the variable!",
        "analogies": {
            "space": "Payload weight variable 'w' calculated against rocket thrust capacity.",
            "coding": "Declaring a variable: let totalSticks = 4 * n;",
            "animals": "Number of legs in a flock of sheep: 4 * s where s is the number of sheep."
        },
        "prompt": "Raju makes triangular shapes using matchsticks. Each triangle requires 3 matchsticks. If 'n' represents the number of triangles made, which expression gives the total number of matchsticks required?",
        "options": ["3n", "3 + n", "n / 3", "n - 3"],
        "answer": "3n",
        "exp": "Each triangle requires 3 matchsticks. For 'n' triangles, the total number of matchsticks is 3 multiplied by n, written as 3n.",
        "hints": ["For 1 triangle: 3 * 1 = 3.", "For 2 triangles: 3 * 2 = 6.", "For n triangles: 3 * n = 3n."],
        "scaffolds": ["Step 1: Matchsticks per triangle = 3.", "Step 2: For n triangles, multiply 3 by n.", "Step 3: Expression is 3n."]
    },
    (6, "Mathematics", 8): {
        "concept_name": "Ratio and Proportion (Unitary Method)",
        "diff": 2,
        "objectives": ["Express comparisons as ratios in simplest form", "Solve real-world problems using the Unitary method"],
        "prereq": ["Division and multiplication"],
        "std_exp": "A ratio compares two quantities of the same kind by division (a : b = a/b). In the unitary method, first determine the value of a single unit, then multiply to find the desired value.",
        "simp_exp": "A recipe uses 2 cups of sugar for every 3 cups of flour. If you use 9 cups of flour, notice 9 is 3 times 3. So you need 2 * 3 = 6 cups of sugar!",
        "analogies": {
            "space": "Fuel to oxidizer ratio in rocket combustion chambers: 1 part fuel to 3 parts oxidizer.",
            "coding": "Aspect ratio calculation for responsive video viewports (16:9 widescreen).",
            "animals": "Worker bees to queen bee ratio in an active healthy honeybee hive."
        },
        "prompt": "A recipe calls for 2 cups of sugar for every 3 cups of flour. If a baker uses 9 cups of flour, how many cups of sugar are needed to maintain the exact same ratio?",
        "options": ["6 cups", "4 cups", "5 cups", "8 cups"],
        "answer": "6 cups",
        "exp": "The ratio of sugar to flour is 2 : 3. To find sugar for 9 cups of flour: (2 / 3) * 9 = 2 * 3 = 6 cups.",
        "hints": ["Write the ratio as 2 / 3 = x / 9.", "Flour increased from 3 to 9 (multiplied by 3).", "Multiply sugar by 3: 2 * 3 = 6 cups."],
        "scaffolds": ["Step 1: Ratio is 2 cups sugar : 3 cups flour.", "Step 2: Flour used is 9 cups = 3 * 3.", "Step 3: Sugar needed = 2 * 3 = 6 cups."]
    },

    # --- Science (7 Chapters) ---
    (6, "Science", 1): {
        "concept_name": "Components of Food & Nutrition",
        "diff": 2,
        "objectives": ["Identify major nutrients: carbohydrates, proteins, fats, vitamins, and minerals", "Recognize deficiency diseases like scurvy, rickets, and beriberi"],
        "prereq": ["Food sources"],
        "std_exp": "Food contains essential nutrients. Carbohydrates and fats supply energy; proteins support body growth and tissue repair; vitamins and minerals protect against diseases. Deficiency of Vitamin C causes scurvy.",
        "simp_exp": "Pulses, eggs, and milk contain proteins for muscle building. Oranges and lemons give Vitamin C to keep gums healthy. Without Vitamin C, gums bleed (scurvy).",
        "analogies": {
            "space": "Astronaut space rations packed with precise macronutrient ratios to maintain bone density.",
            "coding": "Dependencies in a software package: if a core library is missing, system runtime errors occur.",
            "animals": "Bears eating salmon rich in proteins and fats before hibernation."
        },
        "prompt": "A child has bleeding gums and wounds that take an unusually long time to heal. Which nutrient deficiency is the child most likely suffering from?",
        "options": ["Vitamin C deficiency (Scurvy)", "Iron deficiency (Anaemia)", "Vitamin A deficiency (Night blindness)", "Vitamin D deficiency (Rickets)"],
        "answer": "Vitamin C deficiency (Scurvy)",
        "exp": "Bleeding gums and delayed wound healing are classic symptoms of scurvy, caused by a lack of Vitamin C found in citrus fruits like lemons and amla.",
        "hints": ["Think about citrus fruits like oranges, lemons, and amla.", "Which vitamin keeps gums and skin healthy?", "Deficiency of Vitamin C causes scurvy."],
        "scaffolds": ["Step 1: Identify symptoms: bleeding gums, slow wound healing.", "Step 2: Match symptoms to deficiency disease: Scurvy.", "Step 3: Scurvy is caused by Vitamin C deficiency."]
    },
    (6, "Science", 2): {
        "concept_name": "Sorting Materials into Groups (Properties of Materials)",
        "diff": 2,
        "objectives": ["Classify materials by transparency: opaque, transparent, and translucent", "Differentiate materials based on hardness, solubility, and density in water"],
        "prereq": ["Common materials around us"],
        "std_exp": "Materials are grouped by physical properties. Transparent materials allow light to pass through completely (clear glass); translucent materials allow partial light transmission (butter paper); opaque materials block light entirely (wood, metal).",
        "simp_exp": "You can see clearly through a clean window (transparent). You can see a blurry shadow through frosted shower glass (translucent). You cannot see anything through a wooden door (opaque).",
        "analogies": {
            "space": "Spaceship visor: outer gold reflective visor is translucent/reflective; cabin glass is transparent.",
            "coding": "CSS opacity property: 1.0 is opaque, 0.5 is translucent, 0.0 is transparent.",
            "animals": "A chameleon looking through clear water vs murky translucent swamp water."
        },
        "prompt": "An oily patch on a sheet of notebook paper allows you to see the light of an electric bulb dimly and blurred. The oily paper is classified as:",
        "options": ["Translucent", "Transparent", "Opaque", "Luminous"],
        "answer": "Translucent",
        "exp": "Materials through which objects can be seen, but not clearly, are called translucent. An oily patch makes paper translucent.",
        "hints": ["Can you see clearly through it? No, only dimly.", "Is it completely blocked? No.", "A material that lets partial light through is called translucent."],
        "scaffolds": ["Step 1: Assess light transmission: partial/blurred.", "Step 2: Recall definitions: Transparent = clear, Opaque = no light, Translucent = partial light.", "Step 3: The correct term is Translucent."]
    },
    (6, "Science", 3): {
        "concept_name": "Separation of Substances (Methods of Separation)",
        "diff": 2,
        "objectives": ["Identify separation methods: handpicking, threshing, winnowing, sieving, filtration", "Explain sedimentation, decantation, and evaporation"],
        "prereq": ["Mixtures and solutions"],
        "std_exp": "Separation exploits differences in physical properties like particle size, weight, and solubility. Winnowing separates heavier grain seeds from lighter husk using wind blowing.",
        "simp_exp": "When farmers drop wheat from a height in a breeze, the wind blows the light husk far away while heavy grain falls straight down: this is WINNOWING!",
        "analogies": {
            "space": "Centrifugal separation of fuel contaminants inside spacecraft booster pumps.",
            "coding": "Array filter functions separating elements based on boolean condition predicates.",
            "animals": "Flamingos using specialized beak combs to sieve tiny shrimp from muddy lagoon water."
        },
        "prompt": "A farmer drops a mixture of harvested wheat grains and dry husk from a height in the direction of blowing wind. The lighter husk blows away while grains fall straight down. What is this process called?",
        "options": ["Winnowing", "Threshing", "Sieving", "Sedimentation"],
        "answer": "Winnowing",
        "exp": "Winnowing is the method used to separate heavier and lighter components of a mixture by wind or by blowing air, commonly used by farmers to separate husk from grains.",
        "hints": ["Wind is used to blow away the lighter component.", "Threshing beats the stalks; winnowing uses wind.", "The process is winnowing."],
        "scaffolds": ["Step 1: Identify components: heavy grains + light husk.", "Step 2: Mechanism: wind separates by weight.", "Step 3: This process is called Winnowing."]
    },
    (6, "Science", 4): {
        "concept_name": "Getting to Know Plants (Structure & Leaf Venation)",
        "diff": 2,
        "objectives": ["Differentiate herbs, shrubs, and trees", "Identify reticulate and parallel venation and relate to root types"],
        "prereq": ["Parts of a plant"],
        "std_exp": "Plants with reticulate venation (net-like veins) typically have taproots (e.g., mustard, rose). Plants with parallel venation (parallel vein lines) have fibrous roots (e.g., wheat, grass).",
        "simp_exp": "Look at grass: its leaf veins run side by side in parallel lines, and its roots are a bunch of thin fibrous hair! Peepal leaf has net-like veins and a thick taproot.",
        "analogies": {
            "space": "Solar panel wiring: grid array (reticulate) vs parallel strip busbars (parallel).",
            "coding": "Tree data structures: binary tree root branching vs flat array list parallel nodes.",
            "animals": "Blood vessels branching like reticulate veins through human lungs."
        },
        "prompt": "A student observes that grass leaves have veins running parallel to one another. What type of root system will this grass plant have?",
        "options": ["Fibrous root system", "Taproot system with lateral roots", "Aerial prop root system", "Tuberous root system"],
        "answer": "Fibrous root system",
        "exp": "Leaves with parallel venation are consistently paired with fibrous root systems, whereas leaves with reticulate venation are associated with taproots.",
        "hints": ["Grass has parallel venation.", "Does grass have one thick carrot-like taproot or a bundle of thin roots?", "Parallel venation pairs with fibrous roots."],
        "scaffolds": ["Step 1: Identify venation type: parallel.", "Step 2: Recall rule: Parallel venation = Fibrous roots; Reticulate venation = Taproot.", "Step 3: Therefore, grass has fibrous roots."]
    },
    (6, "Science", 5): {
        "concept_name": "Body Movements & Skeletal System (Joints)",
        "diff": 2,
        "objectives": ["Identify types of movable joints: ball and socket, hinge, and pivotal joints", "Explain the role of muscles, cartilage, and tendons in locomotion"],
        "prereq": ["Human body parts"],
        "std_exp": "Ball and socket joints (shoulder, hip) permit 360-degree multi-directional rotational movement. Hinge joints (elbow, knee) allow back-and-forth movement in a single plane like a door hinge.",
        "simp_exp": "Your shoulder can swing your arm all the way around in circles (ball and socket). Your elbow can only bend open and shut like a door (hinge joint)!",
        "analogies": {
            "space": "Robotic arm joints: spherical gimbal socket at shoulder vs single-axis hinge at elbow.",
            "coding": "Physics engine joint constraints: 3-DOF spherical ball joint vs 1-DOF revolute hinge.",
            "animals": "A cheetah's flexible scapula and ball-and-socket hips allowing explosive rotational strides."
        },
        "prompt": "Which joint in the human skeleton allows maximum movement in all directions (full rotational swinging)?",
        "options": ["Ball and socket joint (shoulder and hip)", "Hinge joint (elbow and knee)", "Pivotal joint (neck)", "Fixed joint (cranium)"],
        "answer": "Ball and socket joint (shoulder and hip)",
        "exp": "The ball-and-socket joint, where the rounded head of one bone fits into the cavity of another, permits rotational movement in all directions.",
        "hints": ["Can your elbow rotate in a full circle? No.", "Can your shoulder swing an arm around in circles? Yes.", "The joint is the ball and socket joint."],
        "scaffolds": ["Step 1: Hinge joint = 1 direction (back and forth).", "Step 2: Fixed joint = no movement.", "Step 3: Ball and socket joint = movement in all directions."]
    },
    (6, "Science", 6): {
        "concept_name": "Electricity and Circuits (Conductors & Insulators)",
        "diff": 2,
        "objectives": ["Understand closed and open electric circuits", "Classify materials as electrical conductors or insulators"],
        "prereq": ["Basic safety with electricity"],
        "std_exp": "Electric current flows only through a closed continuous circuit from the positive terminal to the negative terminal of a cell. Conductors allow electric current to pass; insulators block current.",
        "simp_exp": "Metals like copper and iron let electricity pass (conductors). Plastic, rubber, and wood stop electricity (insulators). Electricians wear rubber gloves so they don't get shocked!",
        "analogies": {
            "space": "Gold wiring harnesses in space probes conducting power from solar arrays without corrosion.",
            "coding": "Circuit breaker design patterns in backend APIs routing or terminating flow.",
            "animals": "Electric eels generating 600V electric discharge through specialized electrocyte cells."
        },
        "prompt": "An electrician wears thick rubber gloves while repairing a live electric switchboard. Why are rubber gloves used?",
        "options": [
            "Rubber is a poor conductor of electricity (insulator) and prevents electric shocks",
            "Rubber attracts electric current away from the switchboard",
            "Rubber acts as a strong conductor, helping the circuit complete quickly",
            "Rubber generates electrical power to test the switchboard"
        ],
        "answer": "Rubber is a poor conductor of electricity (insulator) and prevents electric shocks",
        "exp": "Rubber is an electrical insulator. It does not allow electric current to pass through it, thereby protecting the electrician from dangerous electric shocks.",
        "hints": ["Does electricity flow through rubber?", "Rubber does not conduct electricity.", "It acts as an insulator to prevent electric shocks."],
        "scaffolds": ["Step 1: Identify material: rubber.", "Step 2: Electrical property of rubber: insulator (does not allow current to pass).", "Step 3: Purpose: protects human body from electric shock."]
    },
    (6, "Science", 7): {
        "concept_name": "Fun with Magnets (Magnetic Poles & Properties)",
        "diff": 2,
        "objectives": ["Identify North and South magnetic poles", "State the laws of magnetic attraction and repulsion"],
        "prereq": ["Shapes of magnets"],
        "std_exp": "Every magnet has two poles: North (N) and South (S). Like poles repel each other (N-N or S-S), while unlike poles attract each other (N-S). A freely suspended magnet always aligns along the North-South direction.",
        "simp_exp": "Bring two North poles together, and they push each other away! Bring a North pole near a South pole, and they snap together. Opposites attract, likes repel!",
        "analogies": {
            "space": "Earth's geomagnetic shield deflecting charged solar wind particles at the magnetosphere.",
            "coding": "Bipolar data polarity filtering in magnetic storage media (hard drives).",
            "animals": "Migratory sea turtles navigating across oceans using Earth's magnetic field lines."
        },
        "prompt": "When the North pole of a bar magnet is brought close to the North pole of another freely suspended bar magnet, what happens?",
        "options": [
            "The two magnets repel (push away from each other)",
            "The two magnets attract (pull together strongly)",
            "Both magnets lose their magnetism immediately",
            "They rotate until their North poles stick together permanently"
        ],
        "answer": "The two magnets repel (push away from each other)",
        "exp": "The fundamental law of magnetism states that like poles repel each other and unlike poles attract. Thus, North pole repels North pole.",
        "hints": ["Are the two poles the same (like) or opposite (unlike)?", "They are both North poles (like poles).", "Like poles repel each other."],
        "scaffolds": ["Step 1: Identify poles being brought together: North and North.", "Step 2: Rule of magnetism: Like poles repel; unlike poles attract.", "Step 3: Outcome: They repel each other."]
    },

    # --- English (4 Chapters) ---
    (6, "English", 1): {
        "concept_name": "Who Did Patrick's Homework? (Self-Reliance)",
        "diff": 2,
        "objectives": ["Understand character motivation and narrative irony", "Identify the theme of hard work and self-reliance"],
        "prereq": ["Basic reading comprehension"],
        "std_exp": "In the story, Patrick dislikes doing homework until he discovers a tiny elf who agrees to do it. However, because the elf knows nothing of human studies, Patrick must guide, read, calculate, and write everything himself, unknowingly transforming into a dedicated scholar.",
        "simp_exp": "Patrick thought the elf was doing his homework, but the elf asked so many questions that Patrick had to look up every word and solve every math sum himself!",
        "analogies": {
            "space": "An automated autopilot computer that forces the pilot to calculate every orbital parameter manually.",
            "coding": "Rubber duck debugging: explaining a bug to a toy duck forces the programmer to solve the problem themselves.",
            "animals": "A baby bird learning to flap its wings while trying to catch a moving twig."
        },
        "prompt": "Who actually completed Patrick's homework throughout the story?",
        "options": [
            "Patrick himself, because the elf required Patrick's constant research and guidance for every question",
            "The magical elf completely independently using wizardry",
            "Patrick's parents secretly during the night",
            "Patrick's school teacher who gave him automatic answers"
        ],
        "answer": "Patrick himself, because the elf required Patrick's constant research and guidance for every question",
        "exp": "The delightful twist of the story is that the elf was merely a catalyst. Patrick read the books, looked up dictionary meanings, and solved the sums himself, earning straight A's.",
        "hints": ["Did the elf know multiplication tables or history?", "Who looked up words in the dictionary?", "Patrick did all the actual work."],
        "scaffolds": ["Step 1: The elf pleaded ignorance about human subjects.", "Step 2: Patrick stayed up late reading and solving every problem for the elf.", "Step 3: Conclusion: Patrick did his own homework."]
    },
    (6, "English", 2): {
        "concept_name": "How the Dog Found Himself a Master! (Domestication & Loyalty)",
        "diff": 2,
        "objectives": ["Identify the chronological sequence of animal masters", "Understand why the dog chose man as the ultimate master"],
        "prereq": ["Story comprehension"],
        "std_exp": "The folk narrative explains animal domestication. The dog seeks the strongest creature on Earth as his master: first serving the Wolf, then the Bear, then the Lion, and finally Man, whom all wild beasts fear.",
        "simp_exp": "The dog wanted the strongest master. The wolf feared the bear, the bear feared the lion, and the lion feared humans! So the dog chose man.",
        "analogies": {
            "space": "Selecting the most powerful propulsion rocket engine for deep space voyages.",
            "coding": "Hierarchy of permission inheritance: root/admin superuser has ultimate control over all child nodes.",
            "animals": "Symbiotic pack alliance between early canines and human hunter-gatherers."
        },
        "prompt": "In the story 'How the Dog Found Himself a Master!', whom did the dog finally choose to serve faithfully forever?",
        "options": ["Man", "The Lion", "The Bear", "The Wolf"],
        "answer": "Man",
        "exp": "When the dog saw that even the mighty Lion feared human scent and avoided man, the dog realized Man was the strongest being on Earth and chose to be his faithful companion.",
        "hints": ["Who did the mighty Lion fear in the forest?", "The Lion smelled human beings approaching.", "The dog chose Man."],
        "scaffolds": ["Step 1: Dog served Wolf -> Bear -> Lion.", "Step 2: Lion feared Man.", "Step 3: Dog chose Man as the ultimate master."]
    },
    (6, "English", 3): {
        "concept_name": "Kalpana Chawla - An Indian-American Woman in Space",
        "diff": 2,
        "objectives": ["Extract factual biographical details from informational text", "Identify themes of perseverance and aerospace ambition"],
        "prereq": ["Biographical reading"],
        "std_exp": "Kalpana Chawla was born in Karnal, Haryana, graduated from Punjab Engineering College, and earned a PhD in aerospace engineering in the USA, becoming the first woman of Indian origin to fly in space aboard Space Shuttle Columbia.",
        "simp_exp": "Born in Karnal, Kalpana loved airplanes as a little girl. She studied hard, became an astronaut at NASA, and inspired millions by flying to space aboard the Space Shuttle Columbia!",
        "analogies": {
            "space": "Orbital space missions requiring thousands of hours of scientific flight simulation.",
            "coding": "Breaking glass ceilings by writing pioneering open-source foundational algorithms.",
            "animals": "A falcon soaring high above mountain ranges through unyielding determination."
        },
        "prompt": "In which city in Haryana, India was astronaut Kalpana Chawla born?",
        "options": ["Karnal", "Ambala", "Chandigarh", "Panipat"],
        "answer": "Karnal",
        "exp": "Kalpana Chawla was born in Karnal, Haryana. She later graduated in aeronautical engineering from Punjab Engineering College, Chandigarh.",
        "hints": ["It is a historic city in Haryana.", "Her hometown begins with the letter 'K'.", "The city is Karnal."],
        "scaffolds": ["Step 1: Recall Kalpana Chawla's birthplace mentioned in NCERT text.", "Step 2: She was born in Karnal, Haryana.", "Step 3: Karnal is the correct answer."]
    },
    (6, "English", 4): {
        "concept_name": "A Different Kind of School (Inclusion & Empathy)",
        "diff": 2,
        "objectives": ["Understand Miss Beam's experiential education method", "Appreciate empathy toward neurodivergent individuals and people with disabilities"],
        "prereq": ["Character analysis"],
        "std_exp": "Miss Beam's school implemented dedicated awareness days: Blind Day, Lame Day, Deaf Day, and Maimed Day. Students experienced temporary sensory and physical limitations to foster deep, genuine empathy and compassion.",
        "simp_exp": "At Miss Beam's school, every child spent one day blindfolded with a helper to lead them. This taught them how challenging it is to be blind and how to be kind helpers!",
        "analogies": {
            "space": "Astronaut neutral buoyancy training simulators experiencing microgravity limitations underwater.",
            "coding": "Accessibility testing using screen readers (ARIA standards) to experience web software as visually impaired users do.",
            "animals": "An elephant herd slowing its march pace to accommodate an injured calf."
        },
        "prompt": "What was the core educational purpose of the 'Blind Day' and 'Lame Day' at Miss Beam's school?",
        "options": [
            "To teach children thoughtfulness, kindness, and deep empathy for people with disabilities through firsthand experience",
            "To test physical strength and endurance for competitive sports",
            "To punish students who failed academic exams",
            "To train children to become medical doctors"
        ],
        "answer": "To teach children thoughtfulness, kindness, and deep empathy for people with disabilities through firsthand experience",
        "exp": "Miss Beam explained that the real aim of her school was not just scholastic knowledge, but teaching thoughtfulness, appreciation, and authentic empathy by having children experience limitations firsthand.",
        "hints": ["Was it for grades or for human kindness?", "Miss Beam wanted children to understand what it feels like to face challenges.", "It taught empathy and compassion."],
        "scaffolds": ["Step 1: Identify the special practice at Miss Beam's school.", "Step 2: Students took turns having bandages on eyes or tying an arm.", "Step 3: Purpose: to build deep empathy for individuals with disabilities."]
    },

    # =========================================================================
    # CLASS 7 (19 Chapters: 8 Math, 7 Science, 4 English)
    # =========================================================================
    # --- Mathematics (8 Chapters) ---
    (7, "Mathematics", 1): {
        "concept_name": "Integers (Multiplication & Division Rules)",
        "diff": 3,
        "objectives": ["Apply sign rules for integer multiplication and division", "Solve multi-step expressions following order of operations"],
        "prereq": ["Integer addition and subtraction"],
        "std_exp": "The product of two negative integers is positive: (-a) * (-b) = a * b. The product of a positive and a negative integer is negative: a * (-b) = -(a * b).",
        "simp_exp": "Negative times negative equals positive: (-4) * (-5) = +20. Positive times negative equals negative: 6 * (-3) = -18.",
        "analogies": {
            "space": "Inverting camera polarity twice returns the image to its standard upright orientation.",
            "coding": "Boolean NOT operator: !(!true) evaluates to true.",
            "animals": "Reversing an animal's retreat direction twice returns it to an forward charge."
        },
        "prompt": "Evaluate the mathematical expression: (-12) * (-5) + (-30) / 6",
        "options": ["55", "65", "-55", "-65"],
        "answer": "55",
        "exp": "First, (-12) * (-5) = +60. Next, (-30) / 6 = -5. Then, 60 + (-5) = 60 - 5 = 55.",
        "hints": ["Multiply first: what is (-12) * (-5)? It is +60.", "Divide next: what is (-30) / 6? It is -5.", "Now combine: 60 + (-5) = 55."],
        "scaffolds": ["Step 1: (-12) * (-5) = +60 (neg * neg = pos).", "Step 2: (-30) / 6 = -5 (neg / pos = neg).", "Step 3: 60 + (-5) = 55."]
    },
    (7, "Mathematics", 2): {
        "concept_name": "Fractions and Decimals (Multiplication & Division)",
        "diff": 3,
        "objectives": ["Multiply fractions by reciprocal for division", "Multiply decimals and place the decimal point correctly"],
        "prereq": ["Equivalent fractions and decimal place values"],
        "std_exp": "To divide by a fraction, multiply by its reciprocal: (a/b) / (c/d) = (a/b) * (d/c). In decimal multiplication, count total decimal places across factors.",
        "simp_exp": "To divide 3/4 by 1/2, flip 1/2 into 2/1 and multiply: (3/4) * (2/1) = 6/4 = 3/2 = 1.5!",
        "analogies": {
            "space": "Thrust scaling ratios calculated by fractional reciprocal multipliers in orbital maneuvers.",
            "coding": "Fixed-point floating point scaling using reciprocal integer shifts.",
            "animals": "Dividing a food stash among honeybee larvae combs."
        },
        "prompt": "A rope of length 7/2 meters is cut into smaller pieces of length 1/4 meter each. How many pieces of rope are obtained?",
        "options": ["14 pieces", "12 pieces", "16 pieces", "7 pieces"],
        "answer": "14 pieces",
        "exp": "Divide total length by piece length: (7/2) / (1/4) = (7/2) * (4/1) = 28 / 2 = 14 pieces.",
        "hints": ["To divide by a fraction, multiply by its reciprocal.", "The reciprocal of 1/4 is 4/1.", "(7/2) * 4 = 28 / 2 = 14."],
        "scaffolds": ["Step 1: Formula = Total length / Piece length.", "Step 2: (7/2) / (1/4) = (7/2) * 4.", "Step 3: 28 / 2 = 14."]
    },
    (7, "Mathematics", 3): {
        "concept_name": "Data Handling (Mean, Median & Mode)",
        "diff": 3,
        "objectives": ["Calculate arithmetic mean, median, and mode of datasets", "Interpret bar graphs and double bar graphs"],
        "prereq": ["Basic arithmetic operations"],
        "std_exp": "Mean = Sum of observations / Total number of observations. Median is the middle value when data is arranged in ascending order. Mode is the most frequently occurring value.",
        "simp_exp": "For numbers [2, 3, 5, 5, 10]: Mean is (2+3+5+5+10)/5 = 5. Median is middle number 5. Mode is 5 because it appears twice!",
        "analogies": {
            "space": "Calculating average telemetry sensor readings from Mars Rover environmental sensors.",
            "coding": "Writing aggregate functions AVG(), MEDIAN(), and MODE() in SQL / pandas.",
            "animals": "Finding the average daily distance traveled by a wolf pack across a season."
        },
        "prompt": "Find the median of the following test scores: 12, 18, 11, 25, 19, 14, 15.",
        "options": ["15", "16", "18", "14"],
        "answer": "15",
        "exp": "First arrange data in ascending order: 11, 12, 14, 15, 18, 19, 25. With n = 7 (odd), the median is the 4th value: 15.",
        "hints": ["Always sort the numbers in ascending order first.", "Sorted list: 11, 12, 14, 15, 18, 19, 25.", "Which number sits exactly in the center? It is 15."],
        "scaffolds": ["Step 1: Sort scores: 11, 12, 14, 15, 18, 19, 25.", "Step 2: Total scores n = 7.", "Step 3: Middle position = (7+1)/2 = 4th item = 15."]
    },
    (7, "Mathematics", 4): {
        "concept_name": "Simple Equations (Linear Equations in One Variable)",
        "diff": 3,
        "objectives": ["Formulate linear equations from verbal descriptions", "Solve equations using the transposition method"],
        "prereq": ["Algebraic expressions"],
        "std_exp": "In a linear equation ax + b = c, transposition moves a term across the equals sign by changing its sign: ax = c - b, then x = (c - b) / a.",
        "simp_exp": "If 3x + 7 = 22, subtract 7 from both sides: 3x = 15. Then divide by 3: x = 5!",
        "analogies": {
            "space": "Balancing satellite fuel mass equation to achieve designated escape velocity delta-v.",
            "coding": "Solving for unknown loop iterations given a total frame execution budget.",
            "animals": "Equilibrium balance between predator calorie intake and hunting energy expenditure."
        },
        "prompt": "Solve for x in the equation: 4x - 7 = 25",
        "options": ["8", "7", "6", "9"],
        "answer": "8",
        "exp": "Transpose -7 to RHS: 4x = 25 + 7 = 32. Divide both sides by 4: x = 32 / 4 = 8.",
        "hints": ["Move -7 to the right side by adding 7.", "4x = 25 + 7 = 32.", "Divide 32 by 4: x = 8."],
        "scaffolds": ["Step 1: 4x - 7 = 25.", "Step 2: 4x = 25 + 7 = 32.", "Step 3: x = 32 / 4 = 8."]
    },
    (7, "Mathematics", 5): {
        "concept_name": "Lines and Angles (Transversals & Angle Properties)",
        "diff": 3,
        "objectives": ["Identify complementary (sum 90°) and supplementary (sum 180°) angles", "Apply alternate interior and corresponding angle theorems"],
        "prereq": ["Basic geometry and angles"],
        "std_exp": "When a transversal intersects two parallel lines, alternate interior angles are equal, corresponding angles are equal, and interior angles on the same side of the transversal sum to 180°.",
        "simp_exp": "Complementary angles add to 90°. Supplementary angles add to 180°. When a line cuts through railway tracks, the zig-zag alternate angles inside are equal!",
        "analogies": {
            "space": "Star navigation angles measured by optical sextants relative to orbital plane transversals.",
            "coding": "Ray-plane angle of reflection calculations in physics game shaders.",
            "animals": "Bees measuring flight angles relative to the sun's azimuth."
        },
        "prompt": "Two angles are supplementary. If one angle measures 65°, what is the measure of the other angle?",
        "options": ["115°", "25°", "125°", "35°"],
        "answer": "115°",
        "exp": "Supplementary angles have a sum of 180°. Therefore, the second angle is 180° - 65° = 115°.",
        "hints": ["Supplementary angles add up to 180°.", "Subtract 65° from 180°.", "180 - 65 = 115°."],
        "scaffolds": ["Step 1: Recall supplementary angle definition: a + b = 180°.", "Step 2: Substitute: 65° + b = 180°.", "Step 3: b = 180° - 65° = 115°."]
    },
    (7, "Mathematics", 6): {
        "concept_name": "The Triangle and its Properties (Pythagoras & Angle Sum)",
        "diff": 3,
        "objectives": ["Apply angle sum property of a triangle (sum = 180°)", "Apply Pythagoras theorem: a^2 + b^2 = c^2 in right triangles"],
        "prereq": ["Triangles and basic angles"],
        "std_exp": "The three interior angles of any planar triangle sum to 180°. In a right-angled triangle, the square of the hypotenuse equals the sum of the squares of the other two sides: c^2 = a^2 + b^2.",
        "simp_exp": "In a right triangle with legs 3 cm and 4 cm: 3^2 + 4^2 = 9 + 16 = 25. Square root of 25 is 5 cm (hypotenuse)!",
        "analogies": {
            "space": "Triangulating distance to Mars using three deep space tracking telemetry dishes.",
            "coding": "Euclidean distance formula: sqrt(dx^2 + dy^2) for collision detection in 2D games.",
            "animals": "A hawk swooping along the hypotenuse vector to reach prey with shortest flight time."
        },
        "prompt": "A right-angled triangle has legs of lengths 6 cm and 8 cm. What is the length of its hypotenuse?",
        "options": ["10 cm", "14 cm", "12 cm", "9 cm"],
        "answer": "10 cm",
        "exp": "By Pythagoras theorem: Hypotenuse^2 = 6^2 + 8^2 = 36 + 64 = 100. Hypotenuse = sqrt(100) = 10 cm.",
        "hints": ["Use Pythagoras theorem: c^2 = a^2 + b^2.", "6^2 = 36 and 8^2 = 64.", "36 + 64 = 100, and sqrt(100) = 10."],
        "scaffolds": ["Step 1: Formula: c^2 = a^2 + b^2.", "Step 2: c^2 = 6^2 + 8^2 = 36 + 64 = 100.", "Step 3: c = sqrt(100) = 10 cm."]
    },
    (7, "Mathematics", 7): {
        "concept_name": "Comparing Quantities (Percentages, Profit/Loss & Simple Interest)",
        "diff": 3,
        "objectives": ["Convert fractions and ratios to percentages", "Calculate Simple Interest using formula I = (P * R * T) / 100"],
        "prereq": ["Ratio and proportion"],
        "std_exp": "Simple Interest is calculated as SI = (P * R * T) / 100, where P is principal, R is annual rate of interest, and T is time in years. Profit % = (Profit / Cost Price) * 100.",
        "simp_exp": "If you deposit Rs 1,000 at 10% per year for 2 years, interest is (1000 * 10 * 2) / 100 = Rs 200. Total money you get back is Rs 1,200!",
        "analogies": {
            "space": "Power degradation percentage per year of solar panels on the International Space Station.",
            "coding": "Calculating financial interest and discount rates in fintech transaction engines.",
            "animals": "Percentage of body weight a squirrel must store in acorns before winter."
        },
        "prompt": "A sum of Rs 5,000 is borrowed at an annual simple interest rate of 6% for 3 years. What is the total simple interest accrued?",
        "options": ["Rs 900", "Rs 600", "Rs 1,500", "Rs 300"],
        "answer": "Rs 900",
        "exp": "SI = (P * R * T) / 100 = (5000 * 6 * 3) / 100 = 50 * 18 = Rs 900.",
        "hints": ["Use formula: SI = (P * R * T) / 100.", "P = 5000, R = 6, T = 3.", "(5000 * 18) / 100 = 50 * 18 = 900."],
        "scaffolds": ["Step 1: Identify P = 5000, R = 6, T = 3.", "Step 2: SI = (5000 * 6 * 3) / 100.", "Step 3: SI = 50 * 18 = Rs 900."]
    },
    (7, "Mathematics", 8): {
        "concept_name": "Perimeter and Area (Triangles, Parallelograms & Circles)",
        "diff": 3,
        "objectives": ["Compute area of triangles (1/2 * b * h) and parallelograms (b * h)", "Compute circumference (2*pi*r) and area (pi*r^2) of circles"],
        "prereq": ["Area of rectangles and squares"],
        "std_exp": "Area of a parallelogram = base * height. Area of a triangle = (1/2) * base * height. For a circle of radius r, circumference C = 2 * pi * r and area A = pi * r^2 (using pi = 22/7).",
        "simp_exp": "For a circular garden with radius 7 meters: Circumference is 2 * (22/7) * 7 = 44 meters. Area is (22/7) * 7 * 7 = 154 square meters!",
        "analogies": {
            "space": "Calculating orbital sweep area and heat shield circular surface cross-section.",
            "coding": "Bounding box vs circular collision geometry calculations in 2D physics libraries.",
            "animals": "A circular corral fenced to enclose maximum grazing area."
        },
        "prompt": "A circular flowerbed has a radius of 7 meters. Using pi = 22/7, what is the circumference (boundary perimeter) of the flowerbed?",
        "options": ["44 meters", "154 meters", "22 meters", "88 meters"],
        "answer": "44 meters",
        "exp": "Circumference C = 2 * pi * r = 2 * (22/7) * 7 = 2 * 22 = 44 meters.",
        "hints": ["Circumference formula is 2 * pi * r.", "Cancel the 7 in the denominator with radius 7.", "2 * 22 = 44 meters."],
        "scaffolds": ["Step 1: Formula = 2 * pi * r.", "Step 2: C = 2 * (22/7) * 7.", "Step 3: C = 2 * 22 = 44 m."]
    },

    # --- Science (7 Chapters) ---
    (7, "Science", 1): {
        "concept_name": "Nutrition in Plants (Photosynthesis & Heterotrophs)",
        "diff": 3,
        "objectives": ["Formulate the chemical requirements of photosynthesis", "Explain symbiotic relationships, saprotrophs, and insectivorous plants"],
        "prereq": ["Plant structure"],
        "std_exp": "Green plants produce glucose via photosynthesis: 6CO2 + 6H2O in the presence of sunlight and chlorophyll yields C6H12O6 + 6O2. Insectivorous plants (Pitcher plant) trap insects for nitrogen in nutrient-poor soils.",
        "simp_exp": "Plants take carbon dioxide through stomata, water through roots, and use chlorophyll to catch sunlight to bake food (sugar) and release oxygen for us to breathe!",
        "analogies": {
            "space": "Algae bioreactors in space stations recycling CO2 exhaled by astronauts into fresh oxygen.",
            "coding": "Factory pipeline: raw inputs (CO2 + H2O) -> compiler/engine (chlorophyll + light) -> artifact (glucose + O2).",
            "animals": "Leafcutter ants farming fungal gardens inside underground colonies."
        },
        "prompt": "Why does a pitcher plant trap and digest insects even though it has green leaves and performs photosynthesis?",
        "options": [
            "To obtain essential nitrogen compounds lacking in the soil where it grows",
            "Because it cannot perform photosynthesis or make its own food",
            "To absorb water that it cannot get through its roots",
            "To protect neighboring plants from insect infestations"
        ],
        "answer": "To obtain essential nitrogen compounds lacking in the soil where it grows",
        "exp": "Pitcher plants grow in nitrogen-deficient soil. While they are green and perform photosynthesis to produce carbohydrates, they digest insects to obtain required nitrogen compounds.",
        "hints": ["Does the pitcher plant have chlorophyll? Yes, it is green.", "What essential nutrient is missing in boggy soil?", "It digests insects to get nitrogen."],
        "scaffolds": ["Step 1: Note that pitcher plants have chlorophyll and make sugar.", "Step 2: They grow in marshy bogs lacking nitrogen.", "Step 3: Insect digestion supplies nitrogen compounds."]
    },
    (7, "Science", 2): {
        "concept_name": "Nutrition in Animals (Digestive System & Ruminants)",
        "diff": 3,
        "objectives": ["Trace food through the human digestive tract (mouth to large intestine)", "Explain rumination and cellulose digestion in herbivores"],
        "prereq": ["Food nutrients"],
        "std_exp": "Human digestion begins in the mouth (salivary amylase digests starch), continues in the stomach (HCl and pepsin digest proteins), and completes in the small intestine where villi absorb nutrients. Ruminants ferment cellulose in the rumen.",
        "simp_exp": "Cows swallow grass quickly into the rumen, then bring it back into their mouth to chew slowly later: this is called chewing the cud!",
        "analogies": {
            "space": "Closed-loop life support wastewater purification filtering through sequential membranes.",
            "coding": "Multi-stage data ETL pipeline: ingest -> parse -> validate -> extract -> load to store.",
            "animals": "Ruminants housing symbiotic cellulose-degrading microbes in four-chambered stomachs."
        },
        "prompt": "Which organ in the human digestive system is primarily responsible for the absorption of digested nutrients into the bloodstream via villi?",
        "options": ["Small intestine", "Stomach", "Large intestine", "Esophagus"],
        "answer": "Small intestine",
        "exp": "The inner wall of the small intestine has millions of microscopic finger-like projections called villi, which provide enormous surface area for absorbing digested nutrients into the bloodstream.",
        "hints": ["Villi are finger-like projections.", "Where does the final absorption of food occur?", "It takes place in the small intestine."],
        "scaffolds": ["Step 1: Stomach begins protein digestion.", "Step 2: Large intestine absorbs water.", "Step 3: Small intestine absorbs digested food nutrients through villi."]
    },
    (7, "Science", 3): {
        "concept_name": "Heat & Temperature (Conduction, Convection & Radiation)",
        "diff": 3,
        "objectives": ["Differentiate conduction, convection, and radiation", "Explain sea breeze and land breeze mechanisms"],
        "prereq": ["Temperature measurement"],
        "std_exp": "Conduction transfers heat through direct solid contact without bulk particle motion. Convection transfers heat in fluids (liquids/gases) via circulating currents. Radiation transfers heat through electromagnetic waves without any material medium.",
        "simp_exp": "A metal spoon gets hot in soup by conduction. Boiling water circulates heat by convection. Heat from the Sun warms your face across the vacuum of space by radiation!",
        "analogies": {
            "space": "Radiative heat shields on the James Webb Space Telescope blocking solar infrared radiation in deep vacuum.",
            "coding": "Message passing: shared memory (conduction) vs packet broadcast (radiation) vs stream buffering (convection).",
            "animals": "Desert lizards basking on warm rocks to gain heat through direct thermal conduction."
        },
        "prompt": "How does heat energy travel from the Sun across empty space to reach Earth?",
        "options": ["Radiation", "Conduction", "Convection", "Advection"],
        "answer": "Radiation",
        "exp": "Since outer space between the Sun and Earth is a vacuum devoid of any material medium, heat can only travel through electromagnetic waves by radiation.",
        "hints": ["Is there air in deep space to carry heat by convection?", "Can heat touch Earth by conduction without touching material?", "Heat through empty vacuum travels by radiation."],
        "scaffolds": ["Step 1: Conduction and convection require matter (solid, liquid, gas).", "Step 2: Space between Sun and Earth is a vacuum.", "Step 3: Only radiation transfers heat through a vacuum."]
    },
    (7, "Science", 4): {
        "concept_name": "Acids, Bases and Salts (Indicators & Neutralisation)",
        "diff": 3,
        "objectives": ["Identify natural indicators: litmus, turmeric, and China rose", "Explain neutralisation reaction: Acid + Base -> Salt + Water"],
        "prereq": ["Properties of materials"],
        "std_exp": "Acids turn blue litmus red and taste sour. Bases turn red litmus blue and feel soapy. When an acid reacts with a base, they neutralise each other forming salt and water: HCl + NaOH -> NaCl + H2O.",
        "simp_exp": "If an ant stings you, it injects formic acid. Rubbing moist baking soda (a mild base) neutralises the acid and stops the burning pain!",
        "analogies": {
            "space": "Lithium hydroxide canisters neutralizing toxic CO2 and acid gases inside spacesuit rebreathers.",
            "coding": "Error handling middleware neutralizing unhandled exceptions to return standard status 200/500.",
            "animals": "Bees injecting acidic venom vs wasps injecting alkaline venom."
        },
        "prompt": "When a drop of lemon juice (acid) is placed on moist turmeric paper, what color change is observed?",
        "options": [
            "It remains yellow (no color change)",
            "It turns deep red immediately",
            "It turns dark blue",
            "It turns completely colorless"
        ],
        "answer": "It remains yellow (no color change)",
        "exp": "Turmeric is a natural indicator that turns reddish-brown in basic solutions (like soap or lime water), but remains yellow in acidic and neutral solutions.",
        "hints": ["Turmeric turns reddish-brown with soap (base).", "Lemon juice is an acid.", "Turmeric remains yellow in acid."],
        "scaffolds": ["Step 1: Turmeric turns reddish-brown only with bases.", "Step 2: Lemon juice contains citric acid (acidic).", "Step 3: Therefore, turmeric remains yellow."]
    },
    (7, "Science", 5): {
        "concept_name": "Physical and Chemical Changes (Rusting & Crystallisation)",
        "diff": 3,
        "objectives": ["Distinguish reversible physical changes from irreversible chemical changes", "Identify rust formation: Iron + Oxygen + Water -> Iron Oxide"],
        "prereq": ["States of matter"],
        "std_exp": "In a physical change, substance identity and chemical formula remain unchanged (e.g., melting ice, dissolving sugar). In a chemical change, new chemical substances with different properties are formed (e.g., rusting of iron, burning wood).",
        "simp_exp": "Melting an ice cube is a physical change: you can freeze it back into ice! Rusting of an iron nail is a chemical change: a new reddish-brown substance (iron oxide) is made that cannot be undone.",
        "analogies": {
            "space": "Rocket propellant combustion is an irreversible chemical change releasing enormous exhaust kinetic energy.",
            "coding": "Pure functional transformation vs mutating database state with irreversible writes.",
            "animals": "Digesting food inside an animal's gut is a complex chemical change."
        },
        "prompt": "Which of the following processes represents a CHEMICAL change?",
        "options": [
            "Rusting of an iron gate exposed to moist air",
            "Melting of wax on a warm plate",
            "Dissolving common salt in a glass of water",
            "Boiling water to produce steam"
        ],
        "answer": "Rusting of an iron gate exposed to moist air",
        "exp": "Rusting is a chemical change because iron reacts with atmospheric oxygen and water vapor to form a chemically new substance, hydrated iron(III) oxide (rust).",
        "hints": ["Can the change be reversed easily?", "In which process is a completely new chemical substance formed?", "Rust is a new compound (iron oxide)."],
        "scaffolds": ["Step 1: Melting and boiling are physical phase changes.", "Step 2: Dissolving salt is reversible by evaporation.", "Step 3: Rusting creates a new chemical compound (rust), making it a chemical change."]
    },
    (7, "Science", 6): {
        "concept_name": "Respiration in Organisms (Aerobic vs Anaerobic)",
        "diff": 3,
        "objectives": ["Formulate cellular respiration: Glucose + Oxygen -> CO2 + H2O + Energy (ATP)", "Contrast aerobic respiration with anaerobic lactic acid buildup in muscles"],
        "prereq": ["Components of food"],
        "std_exp": "Cellular respiration breaks down glucose to release energy. In the presence of oxygen (aerobic), glucose yields CO2, H2O, and 36-38 ATP. During heavy sprinting, lack of oxygen causes anaerobic breakdown into lactic acid, producing muscle cramps.",
        "simp_exp": "When you run a fast race and pant for breath, your muscles run short of oxygen and produce lactic acid, which causes sudden muscle cramps!",
        "analogies": {
            "space": "Fuel cells combining hydrogen and oxygen to generate electrical energy and potable water.",
            "coding": "Normal high-throughput async processing vs degraded synchronous fallback when worker threads starve.",
            "animals": "Whales storing surplus myoglobin oxygen in deep muscle tissues for extended 90-minute dives."
        },
        "prompt": "During an intense 100-meter sprint, an athlete experiences severe cramps in their leg muscles. What substance accumulation causes these cramps?",
        "options": ["Lactic acid", "Carbonic acid", "Acetic acid", "Hydrochloric acid"],
        "answer": "Lactic acid",
        "exp": "During strenuous exercise, muscle cells respire anaerobically due to temporary oxygen scarcity, partially breaking down glucose into lactic acid, which accumulates and causes muscle cramps.",
        "hints": ["Muscle cramps occur when oxygen supply is insufficient.", "Glucose breaks down anaerobically in human muscles.", "The accumulated compound is lactic acid."],
        "scaffolds": ["Step 1: Strenuous exercise leads to oxygen deficit in muscles.", "Step 2: Anaerobic respiration occurs in muscle cells.", "Step 3: Glucose -> Lactic acid + energy; lactic acid accumulation causes cramps."]
    },
    (7, "Science", 7): {
        "concept_name": "Electric Current and its Effects (Electromagnets & Heating)",
        "diff": 3,
        "objectives": ["Explain the heating effect of electric current and electric fuses", "Describe the magnetic effect of current and construction of electromagnets"],
        "prereq": ["Basic electric circuits"],
        "std_exp": "Current flowing through a high-resistance conductor generates heat (Joule heating: H = I^2*R*t), utilised in heaters and safety fuses. An insulated wire wrapped around an iron nail acts as an electromagnet when current flows.",
        "simp_exp": "Wrap insulated copper wire around an iron nail and connect it to a battery: the nail turns into a magnet that picks up iron paperclips! When you disconnect the switch, the magnetism vanishes.",
        "analogies": {
            "space": "Magnetorquers in satellites using electromagnets against Earth's magnetic field for attitude control.",
            "coding": "Thermal throttling in computer CPUs when high current draws generate excessive junction heat.",
            "animals": "Electric organs in torpedo rays discharging stored electromagnetic energy."
        },
        "prompt": "An electric safety fuse wire melts and breaks the circuit whenever excessive current flows. What property makes fuse wire suitable for this safety function?",
        "options": [
            "It has a low melting point so it melts rapidly under excess heat",
            "It has infinite electrical resistance so current never flows",
            "It is an insulator that repels electric current",
            "It has an extremely high melting point that withstands lightning"
        ],
        "answer": "It has a low melting point so it melts rapidly under excess heat",
        "exp": "A fuse wire is made of an alloy with a low melting point. When excessive current produces heating, the wire melts quickly, safely breaking the circuit to prevent electrical fires.",
        "hints": ["A fuse is designed to break when current is dangerously high.", "Should it melt easily or never melt?", "It must have a low melting point to melt safely."],
        "scaffolds": ["Step 1: Excess current causes Joule heating (H = I^2 R t).", "Step 2: If current is dangerously high, fuse wire must melt to interrupt circuit.", "Step 3: Therefore, it must be made of a material with a low melting point."]
    },

    # --- English (4 Chapters) ---
    (7, "English", 1): {
        "concept_name": "Three Questions by Leo Tolstoy (Wisdom & Mindfulness)",
        "diff": 3,
        "objectives": ["Analyze philosophical allegories in literature", "Identify the three essential truths: right time, right person, right deed"],
        "prereq": ["Reading comprehension"],
        "std_exp": "Tolstoy's philosophical parable demonstrates that the most important time is NOW (the present), the most important person is the one you are with at that moment, and the most important pursuit is doing good for that person.",
        "simp_exp": "The king wanted to know the best time to act. The wise hermit showed him: the only important time is the PRESENT moment, because that is the only time we have the power to act!",
        "analogies": {
            "space": "Real-time command execution during atmospheric entry where only current telemetry matters.",
            "coding": "Event-driven reactive streams processing the current event payload in the event loop.",
            "animals": "A predator focusing 100% sensory attention on the present stalk moment."
        },
        "prompt": "According to the wise hermit in Leo Tolstoy's parable 'Three Questions', what is the ONLY most important time?",
        "options": ["The present moment ('Now')", "The planned future", "The past remembered", "The early morning hours"],
        "answer": "The present moment ('Now')",
        "exp": "The hermit taught the king that the most important time is 'Now', because the present is the only time over which we possess any real power to act.",
        "hints": ["Can you act in the past? No.", "Can you act in the future before it arrives? No.", "The only time you can act is NOW."],
        "scaffolds": ["Step 1: Hermit answered the king's three questions.", "Step 2: Past is gone; future is uncertain.", "Step 3: The only time that matters is 'Now' (the present)."]
    },
    (7, "English", 2): {
        "concept_name": "A Gift of Chappals (Empathy & Compassion)",
        "diff": 3,
        "objectives": ["Understand narrative point of view and social empathy", "Examine child morality versus adult societal conventions"],
        "prereq": ["Story comprehension"],
        "std_exp": "Set in Chennai, the story portrays young children (Mridu, Ravi, Meena) who notice a poor beggar walking with blistered, bleeding feet on scorching hot tar roads and spontaneously give him a pair of old chappals belonging to the music master.",
        "simp_exp": "Seeing blisters on the poor beggar's bare feet in the summer heat, the kind children give him the music teacher's slippers so his feet will stop burning.",
        "analogies": {
            "space": "Sharing limited astronaut emergency oxygen canisters with an impaired crew member.",
            "coding": "Graceful degradation policy allocating emergency resource buffers to critical starving tasks.",
            "animals": "A dolphin pod carrying an exhausted member to the surface for breathing air."
        },
        "prompt": "Why did Ravi and the children decide to give away the music master's chappals to the beggar?",
        "options": [
            "The beggar was barefoot and had painful peeling blisters on his feet from the scorching road",
            "The music master had asked them to throw his old slippers away",
            "The beggar offered money in exchange for comfortable footwear",
            "They wanted to play a mischievous prank on the music teacher"
        ],
        "answer": "The beggar was barefoot and had painful peeling blisters on his feet from the scorching road",
        "exp": "The children demonstrated pure empathy when they saw the beggar's bare feet covered with painful blisters caused by walking on the boiling sun-heated asphalt road.",
        "hints": ["What did the children notice on the beggar's feet?", "His feet had blisters from the hot road.", "They gave slippers out of genuine compassion."],
        "scaffolds": ["Step 1: Identify the beggar's distress: walking barefoot on boiling asphalt.", "Step 2: His soles were peeling with heat blisters.", "Step 3: Compassion prompted the children to give him chappals."]
    },
    (7, "English", 3): {
        "concept_name": "Gopal and the Hilsa Fish (Wits & Strategy)",
        "diff": 3,
        "objectives": ["Identify satire and clever psychological distraction in storytelling", "Analyze comedic narrative structure in comic format"],
        "prereq": ["Reading comic strip stories"],
        "std_exp": "To win the king's challenge that no one can prevent people from talking about Hilsa fish for five minutes, Gopal shaves half his face, smears ash on himself, and wears rags. Everyone gossips exclusively about Gopal's comical appearance, completely ignoring the giant fish he carries!",
        "simp_exp": "Gopal disguised himself so ridiculously with half a beard and messy ash that everyone stared at his crazy face and totally forgot to ask about the Hilsa fish!",
        "analogies": {
            "space": "Using radar decoys to redirect sensor telemetry attention away from the primary spacecraft.",
            "coding": "Honeypot security architecture diverting adversarial traffic away from production databases.",
            "animals": "A killdeer bird faking a broken wing to distract predators away from its ground nest."
        },
        "prompt": "How did Gopal successfully enter the royal court without anyone mentioning or discussing the giant Hilsa fish he bought?",
        "options": [
            "He dressed in torn rags with half a shaven face and ash, making people talk only about his eccentric appearance",
            "He concealed the fish inside a large sealed wooden treasure trunk",
            "He bribed the palace guards with silver coins to stay silent",
            "He walked into the palace in the middle of the dark night while everyone was asleep"
        ],
        "answer": "He dressed in torn rags with half a shaven face and ash, making people talk only about his eccentric appearance",
        "exp": "Gopal created such an overpowering visual spectacle by half-shaving his face and smearing ash that townspeople and courtiers talked only about his madness, winning the king's challenge.",
        "hints": ["What did Gopal look like when he walked through town?", "Half his beard was shaved and he had ash on his face.", "People were too shocked by his appearance to notice the fish."],
        "scaffolds": ["Step 1: The challenge was to bring a Hilsa fish without anyone asking about it.", "Step 2: Gopal created an even bigger distraction with his absurd attire.", "Step 3: No one mentioned the fish because they were fascinated by his appearance."]
    },
    (7, "English", 4): {
        "concept_name": "The Invention of Vita-Wonk by Roald Dahl (Fantasy)",
        "diff": 3,
        "objectives": ["Identify imaginative hyperbole and whimsical descriptive language", "Analyze characterization in Roald Dahl's fantasy literature"],
        "prereq": ["Literary fantasy comprehension"],
        "std_exp": "In this whimsical excerpt from 'Charlie and the Great Glass Elevator', Mr. Willy Wonka seeks ingredients from the oldest living organisms on Earth (bristlecone pine trees, ancient tortoises, 207-year-old rats) to invent Vita-Wonk, a magical tonic that makes people grow older.",
        "simp_exp": "Mr. Wonka needed to make people older, so he collected bits from the oldest living things on Earth—like sap from a 4,000-year-old Bristlecone pine tree!",
        "analogies": {
            "space": "Collecting 4.5-billion-year-old primordial asteroid dust samples from OSIRIS-REx to uncover cosmic origins.",
            "coding": "Compiling historical telemetry logs spanning decades of database operation to train time-series models.",
            "animals": "Analyzing growth rings of Greenland sharks that survive for over 400 years."
        },
        "prompt": "According to Mr. Willy Wonka in Roald Dahl's story, which of the following is the oldest living organism on Earth from which he collected sap?",
        "options": ["The Bristlecone pine tree", "The giant Douglas fir tree", "The California redwood tree", "The weeping willow tree"],
        "answer": "The Bristlecone pine tree",
        "exp": "Mr. Wonka specifically highlights the Bristlecone pine tree growing on the slopes of Wheeler Peak in Nevada, which lives for more than 4,000 years, as the oldest living tree.",
        "hints": ["Look for the tree named by Willy Wonka that lives over 4,000 years.", "Its name starts with 'Bristle...'", "It is the Bristlecone pine."],
        "scaffolds": ["Step 1: Willy Wonka looked for the oldest living thing.", "Step 2: He discovered that Bristlecone pines live for thousands of years.", "Step 3: He gathered sap from the Bristlecone pine."]
    },

    # =========================================================================
    # CLASS 8 (17 Chapters: 7 Math, 6 Science, 4 English)
    # =========================================================================
    # --- Mathematics (7 Chapters) ---
    (8, "Mathematics", 1): {
        "concept_name": "Rational Numbers (Properties & Number Line)",
        "diff": 3,
        "objectives": ["Identify closure, commutative, and associative properties of rational numbers", "Find rational numbers between any two given rational numbers"],
        "prereq": ["Fractions and integers"],
        "std_exp": "A rational number is any number expressible in the form p/q, where p and q are integers and q != 0. Rational numbers are closed, commutative, and associative under addition and multiplication, but NOT under division (due to division by zero).",
        "simp_exp": "Between any two rational numbers, like 1/3 and 1/2, there are infinitely many rational numbers! For example, 1/3 = 4/12 and 1/2 = 6/12, so 5/12 lies right between them.",
        "analogies": {
            "space": "Fine-tuning satellite radio carrier frequencies between 2.4 GHz and 2.5 GHz across infinitely subdivisible bands.",
            "coding": "Arbitrary precision arithmetic libraries (BigDecimal) representing rational fractions without floating point rounding error.",
            "animals": "Subdividing flight migration coordinates into micro-fractional latitude waypoints."
        },
        "prompt": "Which of the following operations is NOT closed for the entire set of rational numbers?",
        "options": ["Division", "Addition", "Multiplication", "Subtraction"],
        "answer": "Division",
        "exp": "The set of rational numbers is not closed under division because dividing any rational number by zero is undefined (e.g., 5/0 is not a rational number).",
        "hints": ["Can you divide any number by zero?", "Division by zero is undefined.", "Therefore, rational numbers are not closed under division."],
        "scaffolds": ["Step 1: Closure means applying an operation to any two members always produces a member of the set.", "Step 2: Consider rational number a and rational number 0.", "Step 3: a / 0 is undefined, violating closure."]
    },
    (8, "Mathematics", 2): {
        "concept_name": "Linear Equations in One Variable (Variables on Both Sides)",
        "diff": 3,
        "objectives": ["Solve linear equations with variable terms on both sides", "Formulate and solve real-world word problems"],
        "prereq": ["Simple equations"],
        "std_exp": "To solve equations like ax + b = cx + d, collect variable terms on one side by transposition: (a - c)x = d - b, then isolate x = (d - b) / (a - c).",
        "simp_exp": "If 5x - 3 = 2x + 12, bring 2x to the left: 5x - 2x = 3x. Move -3 to the right: 12 + 3 = 15. So 3x = 15, which means x = 5!",
        "analogies": {
            "space": "Balancing gravitational pull of Earth and Moon at the Lagrange L1 equilibrium point.",
            "coding": "Binary search equilibrium where low and high pointers converge on identical partition boundary.",
            "animals": "Two bird flocks exchanging members until both flocks reach identical carrying capacity."
        },
        "prompt": "Solve the linear equation for x: 5x - 7 = 2x + 8",
        "options": ["5", "3", "-5", "1"],
        "answer": "5",
        "exp": "Transpose 2x to LHS and -7 to RHS: 5x - 2x = 8 + 7 => 3x = 15 => x = 15 / 3 = 5.",
        "hints": ["Move 2x to the left: 5x - 2x = 3x.", "Move -7 to the right: 8 + 7 = 15.", "Divide 15 by 3 to get x."],
        "scaffolds": ["Step 1: 5x - 7 = 2x + 8.", "Step 2: 5x - 2x = 8 + 7.", "Step 3: 3x = 15 => x = 5."]
    },
    (8, "Mathematics", 3): {
        "concept_name": "Understanding Quadrilaterals (Properties & Angle Sum)",
        "diff": 3,
        "objectives": ["Apply angle sum property of quadrilaterals (sum = 360°)", "Classify parallelograms, rhombuses, rectangles, and squares by diagonal properties"],
        "prereq": ["Triangles and polygons"],
        "std_exp": "The sum of interior angles of a quadrilateral is (n - 2) * 180° = 360°. In a parallelogram, opposite angles are equal and adjacent angles are supplementary (sum 180°). In a rhombus, diagonals bisect each other at right angles (90°).",
        "simp_exp": "Opposite angles in a parallelogram are twins: if one angle is 70°, the opposite angle is also 70°, and the neighboring angle is 180° - 70° = 110°!",
        "analogies": {
            "space": "Deployable rectangular solar panels folding along diagonal hinge lines.",
            "coding": "Mesh polygon vertex transformations in 3D graphics engines.",
            "animals": "A honeycomb diamond facet maintaining quadrilateral equilibrium under mechanical stress."
        },
        "prompt": "In a parallelogram ABCD, angle A measures 75°. What is the measure of adjacent angle B?",
        "options": ["105°", "75°", "115°", "85°"],
        "answer": "105°",
        "exp": "In any parallelogram, adjacent angles are consecutive interior angles between parallel lines and are therefore supplementary: Angle B = 180° - 75° = 105°.",
        "hints": ["Adjacent angles in a parallelogram add up to 180°.", "Subtract 75° from 180°.", "180 - 75 = 105°."],
        "scaffolds": ["Step 1: Adjacent angles of a parallelogram are supplementary.", "Step 2: Angle A + Angle B = 180°.", "Step 3: Angle B = 180° - 75° = 105°."]
    },
    (8, "Mathematics", 4): {
        "concept_name": "Squares and Square Roots (Pythagorean Triplets & Long Division)",
        "diff": 3,
        "objectives": ["Identify perfect squares and Pythagorean triplets (2m, m^2 - 1, m^2 + 1)", "Find square roots using prime factorisation and the long division method"],
        "prereq": ["Exponents and multiplication"],
        "std_exp": "A square number n^2 is formed by multiplying an integer by itself. For any natural number m > 1, (2m, m^2 - 1, m^2 + 1) forms a Pythagorean triplet. Square root of 1024 = 32.",
        "simp_exp": "To check if 6, 8, 10 is a Pythagorean triplet: 6^2 + 8^2 = 36 + 64 = 100, which equals 10^2! It works perfectly.",
        "analogies": {
            "space": "Pixel dimensions of square CCD sensors on Hubble Space Telescope (e.g., 1024 x 1024 pixels).",
            "coding": "Square matrix indexing (N x N arrays) in machine learning weight tensors.",
            "animals": "Square territorial grazing grid monitored by a pack of territorial lions."
        },
        "prompt": "What is the square root of the number 1,225?",
        "options": ["35", "25", "45", "37"],
        "answer": "35",
        "exp": "Prime factorisation of 1225: 5 * 5 * 7 * 7 = (5 * 7)^2 = 35^2. Therefore, sqrt(1225) = 35.",
        "hints": ["The number ends in 25, so its square root must end in 5.", "Test 35: 35 * 35 = 1225.", "The square root is 35."],
        "scaffolds": ["Step 1: 1225 = 5 * 245 = 5 * 5 * 49 = 5^2 * 7^2.", "Step 2: sqrt(1225) = sqrt(5^2 * 7^2) = 5 * 7.", "Step 3: 5 * 7 = 35."]
    },
    (8, "Mathematics", 5): {
        "concept_name": "Cubes and Cube Roots (Prime Factorisation Method)",
        "diff": 3,
        "objectives": ["Compute cubes of numbers (n^3)", "Extract cube roots using prime factorisation grouping into triplets"],
        "prereq": ["Squares and prime factorisation"],
        "std_exp": "The cube of a number n is n^3 = n * n * n. To find the cube root of a number by prime factorisation, resolve the number into prime factors and group identical factors into triplets of three.",
        "simp_exp": "To find the cube root of 216: 216 = (2 * 2 * 2) * (3 * 3 * 3). Take one from each triplet: 2 * 3 = 6! So cube root of 216 is 6.",
        "analogies": {
            "space": "Volumetric fuel capacity in cubic meters for deep-space cryogenic booster stages.",
            "coding": "3D voxel grid rendering in modern Minecraft-style voxel graphics engines.",
            "animals": "A cubic burrow chamber excavated by prairie dogs to store winter seeds."
        },
        "prompt": "Find the cube root of the integer 3,375 using prime factorisation.",
        "options": ["15", "25", "13", "17"],
        "answer": "15",
        "exp": "Prime factorisation of 3375 = 3 * 3 * 3 * 5 * 5 * 5 = (3^3) * (5^3). Taking one factor from each triplet gives 3 * 5 = 15.",
        "hints": ["Group factors into triplets of three identical numbers.", "3375 = (3 * 3 * 3) * (5 * 5 * 5).", "Multiply 3 by 5 to get 15."],
        "scaffolds": ["Step 1: 3375 / 3 = 1125 / 3 = 375 / 3 = 125.", "Step 2: 125 = 5 * 5 * 5. Factors: (3 * 3 * 3) and (5 * 5 * 5).", "Step 3: Cube root = 3 * 5 = 15."]
    },
    (8, "Mathematics", 6): {
        "concept_name": "Algebraic Expressions and Identities (Standard Identities)",
        "diff": 3,
        "objectives": ["Apply standard identity: (a + b)^2 = a^2 + 2ab + b^2", "Apply difference of squares: (a + b)(a - b) = a^2 - b^2"],
        "prereq": ["Algebraic multiplication"],
        "std_exp": "Standard algebraic identities hold true for all values of variables: (1) (a + b)^2 = a^2 + 2ab + b^2; (2) (a - b)^2 = a^2 - 2ab + b^2; (3) (a + b)(a - b) = a^2 - b^2.",
        "simp_exp": "To multiply 103 * 97 easily, use (100 + 3)(100 - 3) = 100^2 - 3^2 = 10,000 - 9 = 9,991! No long multiplication needed!",
        "analogies": {
            "space": "Trajectory curvature expansion series in orbital orbital perturbation calculations.",
            "coding": "Optimizing compiler transforms replacing multiplication loops with pre-evaluated algebraic identities.",
            "animals": "Geometric area subdivision of foraging territory shared between two animal groups."
        },
        "prompt": "Expand the algebraic expression (2x + 3y)^2 using the standard algebraic identity.",
        "options": ["4x^2 + 12xy + 9y^2", "4x^2 + 6xy + 9y^2", "4x^2 + 9y^2", "2x^2 + 6xy + 3y^2"],
        "answer": "4x^2 + 12xy + 9y^2",
        "exp": "Using identity (a + b)^2 = a^2 + 2ab + b^2 where a = 2x and b = 3y: (2x)^2 + 2(2x)(3y) + (3y)^2 = 4x^2 + 12xy + 9y^2.",
        "hints": ["Recall (a + b)^2 = a^2 + 2ab + b^2.", "Here a = 2x and b = 3y.", "Middle term is 2 * (2x) * (3y) = 12xy."],
        "scaffolds": ["Step 1: Square of first term: (2x)^2 = 4x^2.", "Step 2: Twice product of terms: 2 * (2x) * (3y) = 12xy.", "Step 3: Square of second term: (3y)^2 = 9y^2. Total: 4x^2 + 12xy + 9y^2."]
    },
    (8, "Mathematics", 7): {
        "concept_name": "Mensuration (Surface Area & Volume of Solids)",
        "diff": 3,
        "objectives": ["Compute total and lateral surface area of cuboids and cylinders", "Compute volume of right circular cylinder (V = pi * r^2 * h)"],
        "prereq": ["Perimeter and area"],
        "std_exp": "For a right circular cylinder of radius r and height h: Curved surface area = 2 * pi * r * h; Total surface area = 2 * pi * r * (r + h); Volume = pi * r^2 * h.",
        "simp_exp": "A cylindrical water tank with radius 7 m and height 10 m has volume = (22/7) * 7 * 7 * 10 = 1,540 cubic meters!",
        "analogies": {
            "space": "Fuel tank volume calculations for cylindrical rocket propellant tanks.",
            "coding": "Voxel bounding volume hierarchy (BVH) algorithms in game collision detection.",
            "animals": "A circular underground burrow volume calculated to ensure adequate air ventilation."
        },
        "prompt": "A solid right circular cylinder has a base radius of 7 cm and a height of 10 cm. Using pi = 22/7, what is its volume?",
        "options": ["1,540 cm^3", "440 cm^3", "770 cm^3", "2,200 cm^3"],
        "answer": "1,540 cm^3",
        "exp": "Volume = pi * r^2 * h = (22/7) * 7 * 7 * 10 = 22 * 7 * 10 = 154 * 10 = 1,540 cm^3.",
        "hints": ["Volume of a cylinder is pi * r^2 * h.", "Substitute r = 7 and h = 10.", "(22/7) * 49 * 10 = 22 * 7 * 10 = 1540."],
        "scaffolds": ["Step 1: Formula = pi * r^2 * h.", "Step 2: Substitute: (22/7) * 7 * 7 * 10.", "Step 3: 22 * 7 * 10 = 1,540 cm^3."]
    },

    # --- Science (6 Chapters) ---
    (8, "Science", 1): {
        "concept_name": "Crop Production and Management (Agricultural Practices)",
        "diff": 3,
        "objectives": ["Differentiate Kharif (monsoon) and Rabi (winter) crop cycles", "Compare modern irrigation techniques: drip irrigation and sprinkler systems"],
        "prereq": ["Plant growth and agriculture"],
        "std_exp": "Kharif crops (paddy, maize, soybean, cotton) are sown during the monsoon season (June-September). Rabi crops (wheat, gram, mustard, pea) are sown during winter (October-March). Drip irrigation delivers water drop by drop directly to root zones, maximizing water conservation.",
        "simp_exp": "Paddy needs tons of water, so it is grown in the rainy monsoon (Kharif). Wheat is grown in the cold winter season (Rabi). Drip irrigation saves water in dry regions by watering roots directly!",
        "analogies": {
            "space": "Automated aeroponic and hydroponic plant growth chambers aboard the International Space Station.",
            "coding": "Scheduled cron job pipelines executing seasonal batch workflows at designated calendar epochs.",
            "animals": "Leafcutter ants systematically cultivating fungal crop gardens using mulch leaves."
        },
        "prompt": "Which of the following agricultural crops is classified as a RABI (winter) crop in India?",
        "options": ["Wheat", "Paddy (Rice)", "Maize", "Cotton"],
        "answer": "Wheat",
        "exp": "Wheat, gram, peas, and mustard are classic Rabi crops sown in winter (October to March) and harvested in spring, whereas paddy, maize, and cotton are Kharif monsoon crops.",
        "hints": ["Rabi crops are grown in winter.", "Does paddy grow in winter or heavy monsoon rain?", "Wheat is grown during the cool winter season."],
        "scaffolds": ["Step 1: Recall Kharif = Monsoon (Paddy, Maize, Cotton).", "Step 2: Recall Rabi = Winter (Wheat, Gram, Mustard).", "Step 3: Therefore, Wheat is the Rabi crop."]
    },
    (8, "Science", 2): {
        "concept_name": "Microorganisms: Friend and Foe (Antibiotics & Nitrogen Cycle)",
        "diff": 3,
        "objectives": ["Identify four major microbe groups: bacteria, fungi, protozoa, and algae", "Explain the role of Rhizobium in biological nitrogen fixation"],
        "prereq": ["Cell basics and living organisms"],
        "std_exp": "Rhizobium bacteria live symbiotically in the root nodules of leguminous plants (beans, peas), fixing atmospheric nitrogen gas (N2) into plant-absorbable soil nitrates. Alexander Fleming discovered penicillin from Penicillium mold.",
        "simp_exp": "Plants cannot breathe in nitrogen from the air. Helpful Rhizobium bacteria in bean roots grab nitrogen from the air and turn it into natural soil fertilizer!",
        "analogies": {
            "space": "Bacterial bioreactors converting astronaut organic waste into fertilizer for hydroponic crops.",
            "coding": "Background daemon services silently translating raw network packets into structured database tables.",
            "animals": "Gut microbiome bacteria in termites digesting tough wood cellulose into simple sugars."
        },
        "prompt": "Which bacterium lives in the root nodules of leguminous plants and fixes atmospheric nitrogen to enrich soil fertility?",
        "options": ["Rhizobium", "Lactobacillus", "Vibrio cholerae", "Escherichia coli"],
        "answer": "Rhizobium",
        "exp": "Rhizobium lives symbiotically in the root nodules of leguminous crops (pulses, beans, peas), converting atmospheric nitrogen gas into water-soluble nitrates that plants use for protein synthesis.",
        "hints": ["Think about leguminous plants like beans, peas, and pulses.", "Lactobacillus makes curd; which one fixes nitrogen in roots?", "The bacterium is Rhizobium."],
        "scaffolds": ["Step 1: Identify symbiotic nitrogen-fixing organism.", "Step 2: Lactobacillus turns milk into curd.", "Step 3: Rhizobium inhabits legume roots to fix nitrogen."]
    },
    (8, "Science", 3): {
        "concept_name": "Combustion and Flame (Zones of Flame & Extinguishers)",
        "diff": 3,
        "objectives": ["Identify the three conditions for combustion: fuel, oxygen, and ignition temperature", "Describe the three zones of a candle flame (outer blue, middle yellow, inner dark)"],
        "prereq": ["Heat and temperature"],
        "std_exp": "Combustion requires fuel, oxygen, and heat reaching ignition temperature. The outermost non-luminous zone of a candle flame undergoes complete combustion, has the highest temperature, and glows faint blue. Goldsmiths use this outer zone to melt gold.",
        "simp_exp": "The outside tip of a candle flame is the hottest part because it gets plenty of fresh oxygen. Goldsmiths blow through a brass blowpipe into this hot outer zone to melt metals!",
        "analogies": {
            "space": "Rocket engine combustion chambers mixing liquid hydrogen and liquid oxygen at stoichiometric ignition ratios.",
            "coding": "Resource exhaustion threshold limits triggering circuit breakers before service crashes.",
            "animals": "Bombardier beetles combining hydroquinones and hydrogen peroxide to shoot a boiling chemical spray."
        },
        "prompt": "Which zone of a candle flame is the HOTTEST, where complete combustion of fuel occurs?",
        "options": [
            "Outermost non-luminous blue zone",
            "Middle luminous yellow zone",
            "Innermost dark zone surrounding the wick",
            "The molten wax pool at the bottom"
        ],
        "answer": "Outermost non-luminous blue zone",
        "exp": "The outermost zone of a flame receives abundant oxygen, allowing complete combustion. It is the hottest part of the flame and glows blue.",
        "hints": ["Which part gets the most oxygen from the surrounding air?", "The very outside of the flame.", "The outermost blue zone is the hottest."],
        "scaffolds": ["Step 1: Innermost zone = unburnt wax vapor (least hot).", "Step 2: Middle zone = partial combustion (moderately hot).", "Step 3: Outermost zone = complete combustion with abundant air (hottest)."]
    },
    (8, "Science", 4): {
        "concept_name": "Force and Pressure (Atmospheric Pressure & Formula P = F/A)",
        "diff": 3,
        "objectives": ["Apply the pressure formula: Pressure = Force / Area", "Explain atmospheric pressure and contact vs non-contact forces"],
        "prereq": ["Push and pull forces"],
        "std_exp": "Pressure is defined as the force acting perpendicularly per unit surface area: P = F / A. Smaller contact area results in dramatically higher pressure for the same applied force. Atmospheric pressure is exerted by the column of air above Earth.",
        "simp_exp": "A sharp knife cuts apples easily because its edge is razor thin (tiny area = huge pressure!). A dull knife has a thicker edge (larger area = low pressure) and cannot cut.",
        "analogies": {
            "space": "Spacewalk pressure suits pressurized to maintain 1 atmosphere around the astronaut in deep space vacuum.",
            "coding": "Rate limiting: distributing high incoming traffic requests over large server pool area to reduce server load pressure.",
            "animals": "Camels having broad wide footpads that reduce ground pressure so they do not sink into soft desert sand."
        },
        "prompt": "Why do heavy school bags and luggage backpacks have broad, wide shoulder straps instead of thin strings?",
        "options": [
            "A wider strap increases the surface area, thereby reducing the pressure exerted on the shoulders",
            "A wider strap increases the force pulling down on the shoulders",
            "A wider strap generates frictional heat to keep the student warm",
            "A wider strap eliminates the gravitational weight of the bag completely"
        ],
        "answer": "A wider strap increases the surface area, thereby reducing the pressure exerted on the shoulders",
        "exp": "Since Pressure = Force / Area, increasing the surface area over which the bag's weight acts significantly reduces the pressure exerted on the shoulders, making it comfortable to carry.",
        "hints": ["Formula: Pressure = Force / Area.", "When Area increases in the denominator, what happens to Pressure?", "Pressure decreases, making it less painful to carry."],
        "scaffolds": ["Step 1: Formula is P = F / A.", "Step 2: Wide straps increase contact area (A).", "Step 3: Larger A means smaller Pressure (P) on shoulders."]
    },
    (8, "Science", 5): {
        "concept_name": "Friction (Static, Sliding, Rolling & Lubrication)",
        "diff": 3,
        "objectives": ["Compare friction types: Static > Sliding > Rolling", "Explain methods of increasing and reducing friction (ball bearings, lubricants)"],
        "prereq": ["Force basics"],
        "std_exp": "Friction opposes relative motion between contacting surfaces due to interlocking microscopic irregularities. Friction hierarchy: Static friction > Sliding friction > Rolling friction. Ball bearings convert sliding friction into much smaller rolling friction.",
        "simp_exp": "Rolling a heavy suitcase on wheels is much easier than dragging it flat across the floor because rolling friction is tiny compared to sliding friction!",
        "analogies": {
            "space": "Reaction wheel ball bearings in space telescopes operating in vacuum with dry lubricants.",
            "coding": "Reducing computational friction by caching database lookups in fast memory buffers.",
            "animals": "Snails secreting slimy mucus beneath their muscular foot to reduce ground friction."
        },
        "prompt": "Arrange the three types of friction in order of DECREASING magnitude (from strongest to weakest):",
        "options": [
            "Static friction > Sliding friction > Rolling friction",
            "Rolling friction > Sliding friction > Static friction",
            "Sliding friction > Static friction > Rolling friction",
            "Rolling friction > Static friction > Sliding friction"
        ],
        "answer": "Static friction > Sliding friction > Rolling friction",
        "exp": "Static friction is the greatest because surface interlocking is deepest at rest. Once motion begins, sliding friction is lower. Rolling friction involves minimal contact deformation, making it the smallest.",
        "hints": ["Is it hardest to start moving an object, keep it sliding, or roll it on wheels?", "Starting from rest takes maximum effort (static).", "Wheels take the least effort (rolling)."],
        "scaffolds": ["Step 1: Overcoming static rest requires maximum force (Static is highest).", "Step 2: Sliding encounters moving irregularities (Sliding is intermediate).", "Step 3: Rolling minimizes contact friction (Rolling is lowest)."]
    },
    (8, "Science", 6): {
        "concept_name": "Sound and Acoustics (Vibration, Amplitude & Frequency)",
        "diff": 3,
        "objectives": ["Explain that sound is produced by vibrating bodies through a medium", "Relate frequency (Hz) to pitch, and amplitude to loudness"],
        "prereq": ["Hearing and ears"],
        "std_exp": "Sound propagates as longitudinal mechanical waves requiring a material medium (cannot travel in vacuum). Pitch depends on frequency (measured in Hertz, Hz). Loudness depends on wave amplitude (measured in decibels, dB). Human audible range is 20 Hz to 20,000 Hz.",
        "simp_exp": "High frequency means high pitch, like a shrill bird whistle! Large amplitude means loud volume, like the thunderous roar of a lion. Sound cannot travel through the empty vacuum of space!",
        "analogies": {
            "space": "In space, no one can hear explosions because there is no air medium to propagate sound waves.",
            "coding": "Audio waveform digital sampling: sample rate (frequency) and peak bit depth (amplitude).",
            "animals": "Bats using ultrasonic echolocation above 40,000 Hz to navigate and hunt moths in total darkness."
        },
        "prompt": "Which wave characteristic of a sound determines its PITCH (shrillness or gravitas)?",
        "options": ["Frequency of vibration", "Amplitude of vibration", "Speed of propagation", "Loudness in decibels"],
        "answer": "Frequency of vibration",
        "exp": "The frequency of vibration (number of oscillations per second, in Hertz) determines the pitch or shrillness of a sound. Higher frequency corresponds to higher pitch.",
        "hints": ["Amplitude determines loudness.", "What determines pitch or shrillness?", "The number of vibrations per second is frequency."],
        "scaffolds": ["Step 1: Loudness is governed by Amplitude.", "Step 2: Shrillness/pitch is governed by Frequency.", "Step 3: Therefore, Frequency determines pitch."]
    },

    # --- English (4 Chapters) ---
    (8, "English", 1): {
        "concept_name": "The Best Christmas Present in the World by Michael Morpurgo",
        "diff": 3,
        "objectives": ["Analyze historical fiction and the 1914 WWI Christmas Truce", "Evaluate themes of universal humanity, peace, and tragic longing"],
        "prereq": ["Reading comprehension"],
        "std_exp": "Set against the historical 1914 World War I Western Front Christmas Truce, British soldier Jim Macpherson's letter recounts German and British soldiers stepping into No Man's Land to share schnapps, sausages, and football instead of gunfire.",
        "simp_exp": "On Christmas Day during World War I, enemy soldiers stopped shooting, came out of their trenches, wished each other Merry Christmas, and played football together in the snow!",
        "analogies": {
            "space": "The Apollo-Soyuz handshake in 1975 where rival American astronauts and Soviet cosmonauts docked in space in friendship.",
            "coding": "Cross-platform interoperability protocol uniting two previously incompatible software ecosystems.",
            "animals": "Two rival wolf packs calling a temporary truce at a shared frozen watering hole."
        },
        "prompt": "What extraordinary event occurred on Christmas Day in 1914 between British and German soldiers in No Man's Land?",
        "options": [
            "A spontaneous temporary truce where soldiers celebrated Christmas, shared food, and played football together",
            "A surprise massive military offensive launched in deep snow",
            "The signing of the final peace treaty ending World War I permanently",
            "An air raid conducted by newly invented combat airplanes"
        ],
        "answer": "A spontaneous temporary truce where soldiers celebrated Christmas, shared food, and played football together",
        "exp": "The 1914 Christmas Truce saw opposing British and German soldiers emerge from trenches into No Man's Land without weapons to celebrate Christmas, share food, and play football.",
        "hints": ["It took place on Christmas Day.", "Did they fight or celebrate together?", "They celebrated a spontaneous peaceful Christmas truce."],
        "scaffolds": ["Step 1: The letter describes Christmas 1914.", "Step 2: German soldier Fritz and British soldier Tommy greeted each other.", "Step 3: They shared food and played a football match in peace."]
    },
    (8, "English", 2): {
        "concept_name": "The Tsunami & Disaster Resilience (2004 Indian Ocean)",
        "diff": 3,
        "objectives": ["Extract disaster response lessons from factual historical eyewitness accounts", "Examine animal sensory prescience before natural disasters"],
        "prereq": ["Informational reading"],
        "std_exp": "The chapter details the devastating December 26, 2004 Indian Ocean tsunami, highlighting 10-year-old British schoolgirl Tilly Smith who recognized retreating frothy ocean water from her geography lesson and evacuated Phuket beach, saving dozens of lives.",
        "simp_exp": "10-year-old Tilly remembered her school geography teacher showing video of a tsunami: when the sea sucked back leaving bubbling foam, she warned everyone to run up the hill immediately!",
        "analogies": {
            "space": "Early warning telemetry detection of solar coronal mass ejections allowing satellites to enter safe mode.",
            "coding": "Canary monitoring alarms detecting abnormal latency spikes before a catastrophic production outage.",
            "animals": "Elephants and coastal birds sensing infrasonic earthquake vibrations and fleeing to high hills."
        },
        "prompt": "How was 10-year-old schoolgirl Tilly Smith able to save dozens of tourists on a beach in Phuket, Thailand during the 2004 tsunami?",
        "options": [
            "She recognized the warning signs (sea swelling and retreating with frothy bubbles) from a geography lesson taught by her teacher",
            "She received a sudden emergency text notification on her mobile phone",
            "She followed the high-tech sirens activated by the local coastal patrol",
            "She read an emergency notice printed in the morning hotel newspaper"
        ],
        "answer": "She recognized the warning signs (sea swelling and retreating with frothy bubbles) from a geography lesson taught by her teacher",
        "exp": "Tilly Smith recognized the rapid sea recession and bubbling froth from a video shown by her geography teacher in England two weeks earlier, enabling her to sound the alarm.",
        "hints": ["Think about what she learned in school two weeks before.", "Her geography teacher showed a video of a tsunami.", "She recognized the bubbling, retreating ocean water."],
        "scaffolds": ["Step 1: Tilly was on holiday in Thailand.", "Step 2: She noticed the sea frothing and pulling back rapidly.", "Step 3: Remembering her geography lesson, she screamed that a tsunami was coming."]
    },
    (8, "English", 3): {
        "concept_name": "Glimpses of the Past (1757 - 1857 Indian Freedom Struggle)",
        "diff": 3,
        "objectives": ["Analyze graphic pictorial history of colonial India", "Trace causes of the 1857 First War of Independence"],
        "prereq": ["History of India basics"],
        "std_exp": "Presented in comic-strip format, the chapter outlines British East India Company expansion through superior weaponry and internal ruler division, leading to oppressive land taxes, loss of cottage industries, grease-cartridge controversy, and the 1857 rebellion.",
        "simp_exp": "The East India Company took over India by using divide-and-rule politics, heavy taxes on poor farmers, and ruining traditional weavers until brave freedom fighters rose in 1857!",
        "analogies": {
            "space": "A foreign space probe systematically overriding regional orbital communications relay stations.",
            "coding": "Monopolistic software lock-in slowly replacing native open-source protocols with proprietary licensing.",
            "animals": "An invasive predator species taking over a local ecosystem by dividing and displacing native species."
        },
        "prompt": "In the graphic history 'Glimpses of the Past', which Indian soldier fired the first shot of open mutiny at Barrackpore against British grease-cartridges in 1857?",
        "options": ["Mangal Pandey", "Tatya Tope", "Kunwar Singh", "Nana Sahib"],
        "answer": "Mangal Pandey",
        "exp": "Sepoy Mangal Pandey of the 34th Bengal Native Infantry at Barrackpore led the open uprising against the grease-cartridges, sparking the 1857 rebellion.",
        "hints": ["He was a young sepoy at Barrackpore.", "His heroic action ignited the 1857 rebellion.", "His name is Mangal Pandey."],
        "scaffolds": ["Step 1: Identify the mutiny spark: greased rifle cartridges.", "Step 2: Young sepoy at Barrackpore attacked his British officers.", "Step 3: The sepoy was Mangal Pandey."]
    },
    (8, "English", 4): {
        "concept_name": "A Visit to Cambridge (Stephen Hawking & Disability Pride)",
        "diff": 3,
        "objectives": ["Analyze autobiographical interview with Stephen Hawking", "Appreciate disability resilience, neurodivergence, and intellect beyond physical limitations"],
        "prereq": ["Reading informational interviews"],
        "std_exp": "Firdaus Kanga, an Indian journalist with osteogenesis imperfecta (brittle bone disease), travels to Cambridge to interview world-renowned astrophysicist Stephen Hawking, who lived with ALS and communicated via a computerized speech synthesizer.",
        "simp_exp": "Two brilliant disabled thinkers met at Cambridge. Stephen Hawking showed the world that a paralyzed body cannot stop a mind from exploring the deepest black holes in the universe!",
        "analogies": {
            "space": "A space telescope with stationary solar anchors using radio synthesis to probe black hole horizons.",
            "coding": "Text-to-speech assistive synthesis converting minimal keystroke inputs into expressive natural voice audio.",
            "animals": "An injured eagle perched on a mountain peak observing planetary weather patterns."
        },
        "prompt": "In 'A Visit to Cambridge', what powerful life advice did astrophysicist Stephen Hawking give to disabled people?",
        "options": [
            "Disabled people should concentrate on what they are good at and not waste energy on artificial things",
            "They should continuously train for the Olympic games regardless of interest",
            "They should avoid academic studies and focus only on relaxing music",
            "They should travel abroad to live in foreign universities permanently"
        ],
        "answer": "Disabled people should concentrate on what they are good at and not waste energy on artificial things",
        "exp": "Hawking advised disabled people to concentrate on things they are exceptionally good at and avoid forcing themselves into artificial competitions that waste their vital energy.",
        "hints": ["What did Hawking say about disabled people trying to do things they aren't suited for?", "Focus on your natural strengths and intellect.", "Concentrate on what you are genuinely good at."],
        "scaffolds": ["Step 1: Firdaus Kanga asked Hawking for advice for disabled people.", "Step 2: Hawking remarked that disabled Olympics were often artificial.", "Step 3: He advised: 'They should concentrate on what they are good at'."]
    }
}
