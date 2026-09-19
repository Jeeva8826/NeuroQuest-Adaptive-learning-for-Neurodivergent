"""
Authentic NCERT Academic Questions Catalog for Classes 3, 4, and 5
Subjects: Mathematics, Science / Environmental Studies (EVS), English
"""

PRIMARY_345_QUESTIONS = {
    # =========================================================================
    # CLASS 3
    # =========================================================================
    (3, "Mathematics", 1): {
        "concept_name": "Where to Look From (Perspective & Symmetry)",
        "diff": 2,
        "objectives": ["Identify top, side, and front views of 3D objects", "Recognize lines of reflective symmetry"],
        "prereq": ["Visual perception of shapes"],
        "std_exp": "An object presents distinct 2D projections depending on the viewing angle (top view, front view, side view).",
        "simp_exp": "When looking at a car from high above on a rooftop, you see the flat roof and windshield: that is the TOP VIEW!",
        "analogies": {
            "space": "Satellite orbital reconnaissance taking top-down overhead satellite imagery of landforms.",
            "coding": "Isometric 2D game camera vs top-down orthographic camera rendering mode.",
            "animals": "An eagle soaring in clouds looking straight down at the ground."
        },
        "prompt": "When standing on the 4th floor balcony looking down at a parked car on the street, which view of the car do you observe?",
        "options": ["Top view", "Side view showing doors", "Front view showing headlights", "Underbody view"],
        "answer": "Top view",
        "exp": "Looking down from above an object provides its top (aerial) view, showing the roof, hood, and trunk.",
        "hints": ["You are high above looking straight down.", "You see the roof of the car.", "This is called the top view."],
        "scaffolds": ["Step 1: Observer position = above the car.", "Step 2: Viewing angle = looking straight down.", "Step 3: This is the Top view."]
    },
    (3, "Mathematics", 2): {
        "concept_name": "Fun with Numbers (3-Digit Numbers & Century)",
        "diff": 2,
        "objectives": ["Understand 3-digit place values", "Recognize a century equals 100"],
        "prereq": ["Numbers up to 100"],
        "std_exp": "In cricket and mathematics, a 'century' equals exactly 100 runs or units.",
        "simp_exp": "In cricket, when a batsman scores a century, they scored exactly 100 runs!",
        "analogies": {
            "space": "A spacecraft reaching 100 kilometers altitude crosses the Kármán line into space.",
            "coding": "A 100% progress bar loading completion milestone.",
            "animals": "A giant Galapagos tortoise living for an entire century (100 years)."
        },
        "prompt": "In cricket, a batsman scores a glorious 'Century'. Exactly how many runs did the batsman score?",
        "options": ["100 runs", "50 runs", "200 runs", "10 runs"],
        "answer": "100 runs",
        "exp": "A century in sport and numerical measurement represents exactly 100 units or runs.",
        "hints": ["Think about the word 'cent' in century.", "A half-century is 50, so a full century is...", "A century equals 100 runs."],
        "scaffolds": ["Step 1: Recall definition of century.", "Step 2: 1 century = 100.", "Step 3: Answer is 100 runs."]
    },
    (3, "Mathematics", 3): {
        "concept_name": "Give and Take (Addition with Carryover)",
        "diff": 2,
        "objectives": ["Add 3-digit numbers with regrouping", "Solve word problems with carryover"],
        "prereq": ["2-digit addition with carryover"],
        "std_exp": "When summing digits in a column yields 10 or greater, the tens value is regrouped into the next higher place column.",
        "simp_exp": "Add ones: 6 + 5 = 11 (write 1, carry 1). Add tens: 3 + 4 + 1 = 8. Add hundreds: 1 + 2 = 3. Total is 381!",
        "analogies": {
            "space": "When fuel canisters overflow 10 units, 1 unit transfers automatically into the main tank.",
            "coding": "Bitwise addition carry-out propagation in full adders.",
            "animals": "When a small bird's nest has 10 twigs, it weaves them into one sturdy bundle."
        },
        "prompt": "A school library has 136 Hindi storybooks and 245 English storybooks. How many storybooks are in the library in total?",
        "options": ["381 storybooks", "371 storybooks", "391 storybooks", "400 storybooks"],
        "answer": "381 storybooks",
        "exp": "Add ones: 6 + 5 = 11 (1 ones, carry 1 ten). Add tens: 3 + 4 + 1 = 8 tens. Add hundreds: 1 + 2 = 3 hundreds. Total = 381.",
        "hints": ["Add ones: 6 + 5 = 11.", "Add tens: 30 + 40 + 10 = 80.", "Add hundreds: 100 + 200 = 300. Total is 381."],
        "scaffolds": ["Step 1: 6 + 5 = 11 (carry 1).", "Step 2: 1 + 3 + 4 = 8.", "Step 3: 1 + 2 = 3 -> 381."]
    },
    (3, "Mathematics", 4): {
        "concept_name": "Long and Short (Metric Measurement)",
        "diff": 2,
        "objectives": ["Convert metres to centimetres", "Understand standard metric scale: 1 m = 100 cm"],
        "prereq": ["Using a ruler in cm"],
        "std_exp": "In the standard international metric system, 1 metre equals 100 centimetres ($1\\text{ m} = 100\\text{ cm}$).",
        "simp_exp": "One whole metre stick has 100 small centimetres marked along its length!",
        "analogies": {
            "space": "Calibrating distance sensors: 1 meter equals 100 centimeters for robotic rover arms.",
            "coding": "Unit conversion functions: function toCm(meters) { return meters * 100; }.",
            "animals": "A baby kangaroo hops 1 metre (100 cm) forward in a single leap."
        },
        "prompt": "How many centimetres (cm) are there in exactly 1 full metre (m)?",
        "options": ["100 cm", "10 cm", "1000 cm", "50 cm"],
        "answer": "100 cm",
        "exp": "The metric standard definition establishes that 1 metre is composed of 100 centimetres.",
        "hints": ["The prefix 'centi' means one-hundredth.", "There are 100 cents in a dollar and 100 cm in a metre.", "1 m = 100 cm."],
        "scaffolds": ["Step 1: Metric unit rule: 1 m = 100 cm.", "Step 2: Select '100 cm'."]
    },
    (3, "Mathematics", 5): {
        "concept_name": "Shapes and Designs (Edges & Vertices)",
        "diff": 2,
        "objectives": ["Identify edges and vertices of polygons", "Count corners of rectangles"],
        "prereq": ["2D shapes"],
        "std_exp": "A rectangle is a quadrilateral possessing 4 straight edges and 4 right-angled vertices (corners).",
        "simp_exp": "A postcard or mobile phone has 4 straight edges and 4 pointed corners (vertices)!",
        "analogies": {
            "space": "A rectangular solar panel wing mounted by its 4 structural corner pivot brackets.",
            "coding": "A 2D bounding box defined by 4 corner vertices: (x1,y1) to (x2,y2).",
            "animals": "A rectangular beehive frame held at 4 corners by beekeepers."
        },
        "prompt": "How many straight edges and pointed corners (vertices) does a standard rectangular notebook cover have?",
        "options": ["4 edges and 4 corners", "3 edges and 3 corners", "5 edges and 5 corners", "6 edges and 8 corners"],
        "answer": "4 edges and 4 corners",
        "exp": "A rectangle is a 4-sided polygon with 4 straight sides (edges) and 4 vertices (corners).",
        "hints": ["Look at your book cover or sheet of paper.", "Count top, bottom, left, and right sides: that's 4 sides.", "Count corners: 4."],
        "scaffolds": ["Step 1: Shape = rectangle.", "Step 2: Count edges = 4.", "Step 3: Count vertices = 4."]
    },
    (3, "Mathematics", 6): {
        "concept_name": "Time Goes On (Clocks & Hours)",
        "diff": 2,
        "objectives": ["Read analogue clock faces", "Recognize full hour positions"],
        "prereq": ["Numbers 1 to 12"],
        "std_exp": "When the long minute hand points directly at 12, the short hour hand indicates the exact full hour (o'clock).",
        "simp_exp": "When the long hand points straight up at 12 and the short hand points to 4, it is 4 o'clock!",
        "analogies": {
            "space": "Rotational alignment of docking ports matching 12 o'clock and 4 o'clock clocking positions.",
            "coding": "Parsing Date.getHours() when minutes equal 0.",
            "animals": "Birds returning to nests promptly at 6 o'clock when the sun begins to set."
        },
        "prompt": "On an analogue wall clock, the short hour hand points directly at 4, and the long minute hand points at 12. What time is it?",
        "options": ["4 o'clock (4:00)", "12 o'clock (12:00)", "4:30", "12:04"],
        "answer": "4 o'clock (4:00)",
        "exp": "When the minute hand points to 12, it is the top of the hour. Since the hour hand points to 4, the time is 4:00.",
        "hints": ["Look at the short hand: it tells the hour (4).", "The long hand on 12 means zero minutes past.", "It is 4 o'clock."],
        "scaffolds": ["Step 1: Short hand = 4 (Hour).", "Step 2: Long hand = 12 (00 minutes).", "Step 3: Time is 4:00."]
    },
    (3, "Mathematics", 7): {
        "concept_name": "How Many Times? (Multiplication)",
        "diff": 2,
        "objectives": ["Understand multiplication as repeated addition", "Compute products using times tables"],
        "prereq": ["Skip counting", "Addition"],
        "std_exp": "Multiplication represents repeated addition of identical groups ($a \\times b = b + b + \\dots + b$).",
        "simp_exp": "4 groups of 5 is the same as: 5 + 5 + 5 + 5 = 20!",
        "analogies": {
            "space": "4 rocket engines consuming 5 liters of fuel per second = 20 liters per second.",
            "coding": "Array.fill(5).reduce((a, b) => a + b) = 4 * 5 = 20.",
            "animals": "4 nests with 5 blue robin eggs in each nest: 4 × 5 = 20 eggs."
        },
        "prompt": "A gardener planted 4 neat rows of sunflower plants. Each row has 5 sunflowers. How many sunflowers are planted in total?",
        "options": ["20 sunflowers", "16 sunflowers", "25 sunflowers", "9 sunflowers"],
        "answer": "20 sunflowers",
        "exp": "4 rows of 5 flowers: 4 × 5 = 5 + 5 + 5 + 5 = 20 sunflowers.",
        "hints": ["Add 5 four times: 5, 10, 15, 20.", "4 times 5 equals 20.", "4 × 5 = 20."],
        "scaffolds": ["Step 1: Number of rows = 4.", "Step 2: Flowers per row = 5.", "Step 3: 4 × 5 = 20 sunflowers."]
    },
    (3, "Mathematics", 8): {
        "concept_name": "Can We Share? (Division & Equal Sharing)",
        "diff": 2,
        "objectives": ["Divide a total quantity into equal groups", "Calculate division quotients"],
        "prereq": ["Multiplication facts"],
        "std_exp": "Division distributes a total collection into equal subsets ($15 \\div 3 = 5$).",
        "simp_exp": "Sharing 15 sweet lollipops equally among 3 best friends gives 5 lollipops to each friend!",
        "analogies": {
            "space": "Dividing 15 power cells equally among 3 exploration rovers gives 5 cells per rover.",
            "coding": "Load balancing: distributing 15 incoming requests evenly across 3 worker pods.",
            "animals": "A mother bear dividing 15 caught fish equally between her 3 cubs: 5 fish each."
        },
        "prompt": "Grandmother has 15 delicious lollipops to distribute EQUALLY among her 3 grandchildren. How many lollipops does each grandchild receive?",
        "options": ["5 lollipops", "3 lollipops", "4 lollipops", "6 lollipops"],
        "answer": "5 lollipops",
        "exp": "Divide 15 equally by 3: 15 ÷ 3 = 5 lollipops for each grandchild.",
        "hints": ["Think: 3 times what number equals 15?", "3 × 5 = 15.", "Each gets 5 lollipops."],
        "scaffolds": ["Step 1: Total lollipops = 15.", "Step 2: Number of children = 3.", "Step 3: 15 ÷ 3 = 5."]
    },

    # --- CLASS 3 SCIENCE (EVS) ---
    (3, "Science", 1): {
        "concept_name": "The Plant Fairy & Photosynthesis Basics",
        "diff": 2,
        "objectives": ["Identify green pigment in plant leaves", "Understand chlorophyll role"],
        "prereq": ["Plant observation"],
        "std_exp": "Green plant leaves contain chlorophyll, a specialized pigment that absorbs sunlight to synthesize food via photosynthesis.",
        "simp_exp": "Leaves are green because they contain chlorophyll, which acts like tiny solar panels making food from sunshine!",
        "analogies": {
            "space": "Green-tinted photovoltaic solar arrays absorbing sunlight to generate power for the space station.",
            "coding": "An energy transformer service converting raw incoming solar telemetry into stored application data.",
            "animals": "Reptiles basking in morning sunshine to absorb heat into their green scales."
        },
        "prompt": "What special green substance inside plant leaves traps sunlight so the plant can prepare its own food?",
        "options": ["Chlorophyll", "Mud", "Honey", "Wax"],
        "answer": "Chlorophyll",
        "exp": "Chlorophyll is the green pigment in leaves that absorbs solar energy to synthesize food during photosynthesis.",
        "hints": ["It gives leaves their bright green color.", "It starts with the letter 'C'.", "It is called chlorophyll."],
        "scaffolds": ["Step 1: Green pigment in leaves.", "Step 2: Traps sunlight for food.", "Step 3: Answer is Chlorophyll."]
    },
    (3, "Science", 2): {
        "concept_name": "Water O' Water! (States of Water)",
        "diff": 2,
        "objectives": ["Identify three states of water", "Recognize ice as solid water"],
        "prereq": ["States of matter observation"],
        "std_exp": "Water exists in three interchangeable states: solid (ice), liquid (water), and gas (water vapor/steam).",
        "simp_exp": "When liquid water gets freezing cold below 0 degrees Celsius, it freezes into hard, solid ICE!",
        "analogies": {
            "space": "Water ice craters at the lunar south pole preserved in perpetual freezing shadow.",
            "coding": "An immutable state variable frozen to prevent mutations.",
            "animals": "Polar bears walking across thick floating sea ice in the Arctic."
        },
        "prompt": "When liquid water is placed in a deep freezer and becomes freezing cold, which solid form does it turn into?",
        "options": ["Ice", "Steam", "Smoke", "Lava"],
        "answer": "Ice",
        "exp": "Liquid water freezes at 0°C to form ice, which is the solid state of water.",
        "hints": ["Think about ice cubes in a cold summer drink.", "Ice is cold and hard.", "Water freezes into ice."],
        "scaffolds": ["Step 1: Liquid water cools below freezing.", "Step 2: State changes from liquid to solid.", "Step 3: Solid water = Ice."]
    },
    (3, "Science", 3): {
        "concept_name": "Our Friends - Animals (Feeding Habits)",
        "diff": 2,
        "objectives": ["Classify animals by diet", "Define herbivores"],
        "prereq": ["Animal diets"],
        "std_exp": "Herbivores are primary consumers whose digestive physiology is adapted to eating only vegetation, grass, and plants.",
        "simp_exp": "Animals that eat ONLY plants, green leaves, and grass—like cows, deer, and rabbits—are called HERBIVORES!",
        "analogies": {
            "space": "Bio-regenerative life support systems that process only organic vegetable biomass.",
            "coding": "A strictly typed interface that accepts only PlantBasedInput models.",
            "animals": "A peaceful deer grazing on tender green grass in a sunlit meadow."
        },
        "prompt": "What scientific term describes animals like cows, horses, and deer that eat ONLY grass, leaves, and plants?",
        "options": ["Herbivores", "Carnivores", "Omnivores", "Parasites"],
        "answer": "Herbivores",
        "exp": "Herbivores are animals that feed exclusively on plants and plant products.",
        "hints": ["'Herb' means plant.", "Herbivores eat herbs, grass, and leaves.", "Cows and deer are herbivores."],
        "scaffolds": ["Step 1: Diet = plants and grass only.", "Step 2: Prefix 'Herb-' = plant.", "Step 3: Term is Herbivores."]
    },
    (3, "Science", 4): {
        "concept_name": "From Here to There (Transport Systems)",
        "diff": 2,
        "objectives": ["Identify transport infrastructure", "Recognize trains require railway tracks"],
        "prereq": ["Vehicles recognition"],
        "std_exp": "Railways are specialized transport systems utilizing steel locomotive wheels traveling on parallel steel tracks.",
        "simp_exp": "Trains cannot drive on ordinary dirt roads; they need strong steel railway tracks to carry hundreds of passengers!",
        "analogies": {
            "space": "Magnetic rail accelerators launching supply payloads along dedicated orbital guide tracks.",
            "coding": "Dedicated message queues where packets must follow predefined network routes.",
            "animals": "Ants strictly following an organized pheromone trail across a forest branch."
        },
        "prompt": "Which specialized pathway does a heavy passenger train need to travel safely across long distances?",
        "options": ["Steel railway tracks", "Open ocean water", "Muddy footpaths", "Air runways"],
        "answer": "Steel railway tracks",
        "exp": "Trains run on designated iron/steel railway tracks that support their heavy weight and guide their wheels.",
        "hints": ["Look at a train station.", "Trains have grooved metal wheels that fit into steel tracks.", "They run on railway tracks."],
        "scaffolds": ["Step 1: Vehicle = Train.", "Step 2: Required surface = Railway tracks.", "Step 3: Select 'Steel railway tracks'."]
    },

    # --- CLASS 3 ENGLISH ---
    (3, "English", 1): {
        "concept_name": "Nature Wonders - Good Morning Poem",
        "diff": 2,
        "objectives": ["Identify poetic themes", "Recognize morning greetings in poetry"],
        "prereq": ["Poetry reading"],
        "std_exp": "In the poem 'Good Morning', the child enthusiastically greets the sky, sun, winds, birds, trees, and creeping grass.",
        "simp_exp": "The child in 'Good Morning' says hello to the morning sky, the glowing sun, the singing birds, and green trees!",
        "analogies": {
            "space": "A space habitat waking up as the orbital station moves out of Earth's shadow into the golden dawn.",
            "coding": "System boot initialization pinging and greeting all connected peripheral sensors.",
            "animals": "Birds bursting into joyful morning chorus as the first light touches the treetops."
        },
        "prompt": "In the uplifting poem 'Good Morning', who does the happy child joyfully greet as the new day begins?",
        "options": ["The sky, sun, birds, and trees", "Only a dark stormy cloud", "A sleeping cat under the bed", "No one at all"],
        "answer": "The sky, sun, birds, and trees",
        "exp": "The child greets: 'Good morning, sky! Good morning, sun! Good morning, little winds that run! Good morning, birds!'",
        "hints": ["The child greets all the bright morning nature elements.", "Sky, sun, birds, and green trees.", "The child greets the sky, sun, birds, and trees."],
        "scaffolds": ["Step 1: Poem = 'Good Morning'.", "Step 2: Review first stanza lines.", "Step 3: Greets sky, sun, birds, and trees."]
    },
    (3, "English", 2): {
        "concept_name": "Empathy and Animal Tales - Nina and the Baby Sparrows",
        "diff": 2,
        "objectives": ["Identify character motivations", "Demonstrate empathy for animals"],
        "prereq": ["Story comprehension"],
        "std_exp": "Nina refused to buy new wedding clothes because locking her room would starve the baby sparrows nesting on her bookshelf.",
        "simp_exp": "Nina was deeply compassionate; she was worried that locking the house would stop the mother sparrow from feeding her babies!",
        "analogies": {
            "space": "An astronaut delaying departure to verify an automated biological habitat incubator has uninterrupted nutrient delivery.",
            "coding": "Ensuring an active background task completes its pipeline before shutting down the server container.",
            "animals": "A mother bird tirelessly flying back and forth with seeds to feed her hungry chirping chicks."
        },
        "prompt": "In the story 'Nina and the Baby Sparrows', why was gentle Nina crying and unwilling to attend the family wedding in Delhi?",
        "options": [
            "She worried the baby sparrows in her room would starve if the house was locked",
            "She lost her favorite red dancing shoes",
            "She was afraid of traveling on the train",
            "She did not want to meet her cousins"
        ],
        "answer": "She worried the baby sparrows in her room would starve if the house was locked",
        "exp": "Nina was worried that locking the room would prevent the mother and father sparrows from feeding their tiny babies.",
        "hints": ["Think about the baby birds in the nest on her bookshelf.", "She cared about the sparrows' safety.", "She was worried the baby sparrows would starve."],
        "scaffolds": ["Step 1: Conflict = family wedding in Delhi.", "Step 2: Nina's worry = sparrows in her bedroom.", "Step 3: Choose sparrow safety."]
    },
    (3, "English", 3): {
        "concept_name": "Curiosity and Exploration - The Enormous Turnip",
        "diff": 2,
        "objectives": ["Identify literary moral: power of teamwork", "Sequence collaborative story events"],
        "prereq": ["Story sequencing"],
        "std_exp": "In 'The Enormous Turnip', individual efforts failed, but cooperative teamwork of the man, woman, boy, and girl succeeded.",
        "simp_exp": "When everyone pulled together—the old man, old woman, boy, and girl—the giant turnip finally popped up!",
        "analogies": {
            "space": "Multiple booster thrusters firing simultaneously to achieve escape velocity.",
            "coding": "Distributed computing: combining worker threads to complete a massive parallel processing job.",
            "animals": "Army ants linking their bodies together to pull a large leaf across a stream."
        },
        "prompt": "What important moral lesson does the story 'The Enormous Turnip' teach young readers?",
        "options": ["Teamwork and helping each other makes difficult tasks possible", "It is better to work all alone in secret", "Never plant vegetables in gardens", "Only strong giants can accomplish goals"],
        "answer": "Teamwork and helping each other makes difficult tasks possible",
        "exp": "The giant turnip could not be pulled by one person, but when all worked together in unity, they succeeded.",
        "hints": ["Think about how they pulled: the man, woman, boy, and girl all pulled together.", "United we stand!", "Teamwork makes difficult tasks possible."],
        "scaffolds": ["Step 1: Individual pulling failed.", "Step 2: Group cooperation succeeded.", "Step 3: Moral = Teamwork."]
    },
    (3, "English", 4): {
        "concept_name": "Communication and Letters - Postal Mail",
        "diff": 2,
        "objectives": ["Identify postal address components", "Understand PIN code function"],
        "prereq": ["Everyday communication"],
        "std_exp": "A Postal Index Number (PIN code) is a 6-digit numerical code used by postal services to accurately route mail to delivery post offices.",
        "simp_exp": "The 6-digit PIN code written on an envelope helps the post office deliver your letter straight to the right neighborhood!",
        "analogies": {
            "space": "Orbital coordinates directing deep-space laser communications directly to a ground relay station.",
            "coding": "An IP address and port number routing packets through network switches to the exact server.",
            "animals": "Homing pigeons using magnetic coordinates to return directly to their home roost."
        },
        "prompt": "When writing a letter to your friend, what important 6-digit numerical code on the envelope helps the postman find the exact delivery zone?",
        "options": ["PIN Code (Postal Index Number)", "Phone passcode", "School roll number", "Shoe size number"],
        "answer": "PIN Code (Postal Index Number)",
        "exp": "The PIN code (Postal Index Number) has 6 digits that identify the specific state, district, and delivery post office.",
        "hints": ["It has 6 digits like 110001 or 560001.", "It stands for Postal Index Number.", "It is the PIN Code."],
        "scaffolds": ["Step 1: Purpose = route postal mail.", "Step 2: 6-digit code = PIN Code.", "Step 3: Select 'PIN Code'."]
    },

    # =========================================================================
    # CLASS 4
    # =========================================================================
    (4, "Mathematics", 1): {
        "concept_name": "Building with Bricks (3D Shapes)",
        "diff": 3,
        "objectives": ["Identify faces of a 3D cuboid", "Count rectangular faces on a standard brick"],
        "prereq": ["3D shapes basics"],
        "std_exp": "A brick is geometrically a cuboid possessing 6 rectangular planar faces, 12 edges, and 8 vertices.",
        "simp_exp": "A brick has top, bottom, front, back, left, and right: that makes 6 flat rectangular faces!",
        "analogies": {
            "space": "Modular satellite chassis constructed as sturdy 6-sided cuboids for electronics bays.",
            "coding": "A 3D cube mesh with 6 distinct texture UV-mapped quad faces.",
            "animals": "A wombat producing cube-shaped droppings that do not roll away."
        },
        "prompt": "How many flat rectangular faces does a standard construction brick (a 3D cuboid) have in total?",
        "options": ["6 faces", "4 faces", "8 faces", "12 faces"],
        "answer": "6 faces",
        "exp": "A cuboid brick has 6 faces: top, bottom, front, back, left side, and right side.",
        "hints": ["Count: top and bottom (2), front and back (2), two sides (2).", "2 + 2 + 2 = 6.", "A brick has 6 faces."],
        "scaffolds": ["Step 1: Shape = cuboid.", "Step 2: Faces = top/bottom + 4 vertical sides.", "Step 3: 2 + 4 = 6 faces."]
    },
    (4, "Mathematics", 2): {
        "concept_name": "Long and Short (Distance Conversion)",
        "diff": 3,
        "objectives": ["Convert kilometres to metres", "Understand 1 km = 1000 m"],
        "prereq": ["Metric units cm and m"],
        "std_exp": "1 kilometre equals 1,000 metres ($1\\text{ km} = 1000\\text{ m}$). Therefore, $3\\text{ km} = 3 \\times 1000 = 3000\\text{ m}$.",
        "simp_exp": "Every single kilometre has 1000 metres! So 3 kilometres is 3000 metres!",
        "analogies": {
            "space": "Orbital altitude: a satellite orbiting 300 km above Earth is 300,000 meters above sea level.",
            "coding": "Memory allocation: 1 Kilobyte is roughly 1000 bytes (or 1024).",
            "animals": "A marathon-running ostrich covering 3 km (3000 meters) across savannah grasslands."
        },
        "prompt": "If an athlete completes a 3-kilometre cross-country race, how many metres (m) did they run in total?",
        "options": ["3000 metres", "300 metres", "30 metres", "30,000 metres"],
        "answer": "3000 metres",
        "exp": "1 kilometre = 1000 metres. Therefore, 3 km = 3 × 1000 = 3000 metres.",
        "hints": ["Remember: 1 km = 1000 m.", "Multiply 3 by 1000.", "3 × 1000 = 3000 m."],
        "scaffolds": ["Step 1: 1 km = 1000 m.", "Step 2: 3 km = 3 × 1000 m.", "Step 3: Distance = 3000 m."]
    },
    (4, "Mathematics", 3): {
        "concept_name": "A Trip to Bhopal (Multi-Operation Math)",
        "diff": 3,
        "objectives": ["Calculate total cost from unit rates", "Solve practical multiplication problems"],
        "prereq": ["Multiplication by tens"],
        "std_exp": "Total expenditure is calculated by multiplying unit price by the number of tickets ($\\text{Total} = \\text{Rate} \\times \\text{Quantity}$).",
        "simp_exp": "4 tickets at 50 rupees each: 4 × 50 = 200 rupees!",
        "analogies": {
            "space": "Calculating total delta-V propellant cost: 4 maneuvering burns requiring 50 kg of fuel each = 200 kg.",
            "coding": "Cost calculation: totalCost = ticketCount * unitPrice.",
            "animals": "4 horses each needing 50 kg of fresh oats for a long cross-country ride = 200 kg."
        },
        "prompt": "A family buys 4 bus tickets to visit the Bhopal boat club. If each bus ticket costs ₹50, what is the total cost of all 4 tickets?",
        "options": ["₹200", "₹150", "₹250", "₹100"],
        "answer": "₹200",
        "exp": "Total cost = 4 tickets × ₹50 per ticket = ₹200.",
        "hints": ["Multiply 4 by 50.", "4 × 5 = 20, so 4 × 50 = 200.", "Total cost is ₹200."],
        "scaffolds": ["Step 1: Quantity = 4 tickets.", "Step 2: Rate = ₹50.", "Step 3: 4 × ₹50 = ₹200."]
    },
    (4, "Mathematics", 4): {
        "concept_name": "Tick-Tick-Tick (24-Hour Railway Time)",
        "diff": 3,
        "objectives": ["Convert 24-hour time to 12-hour PM time", "Read railway schedules"],
        "prereq": ["12-hour clock reading"],
        "std_exp": "To convert 24-hour times past 12:00 to 12-hour PM format, subtract 12 from the hours ($17:30 - 12:00 = 5:30\\text{ PM}$).",
        "simp_exp": "On a railway clock showing 17:30, subtract 12: 17 - 12 = 5, so it is 5:30 in the evening (PM)!",
        "analogies": {
            "space": "Mission Control using UTC 24-hour Zulu time (17:30Z) for universal telemetry timestamping.",
            "coding": "Formatting timestamps: moment(time).format('h:mm A').",
            "animals": "Bats emerging from caves at 19:00 hours (7:00 PM) as dusk falls."
        },
        "prompt": "A railway departure display shows the train departure time as 17:30. What is this time on a standard 12-hour PM clock?",
        "options": ["5:30 PM", "7:30 PM", "3:30 PM", "5:30 AM"],
        "answer": "5:30 PM",
        "exp": "17:30 is in the afternoon/evening. Subtract 12: 17 - 12 = 5, so 17:30 = 5:30 PM.",
        "hints": ["For times greater than 12, subtract 12 from the hour.", "17 - 12 = 5.", "17:30 is 5:30 PM."],
        "scaffolds": ["Step 1: Hour is 17 (> 12, so it's PM).", "Step 2: 17 - 12 = 5.", "Step 3: Time = 5:30 PM."]
    },
    (4, "Mathematics", 5): {
        "concept_name": "The Junk Seller (Profit & Commerce)",
        "diff": 3,
        "objectives": ["Compute commercial profit", "Apply formula: Profit = Selling Price - Cost Price"],
        "prereq": ["Subtraction of 2-digit numbers"],
        "std_exp": "Profit occurs when selling price ($SP$) exceeds cost price ($CP$), calculated as $\\text{Profit} = SP - CP$.",
        "simp_exp": "Bought for 10 rupees and sold for 14 rupees: 14 - 10 = 4 rupees profit!",
        "analogies": {
            "space": "Energy storage profit: solar panels gathering 14 kilowatt-hours while systems consume 10, leaving 4 net surplus.",
            "coding": "Calculating net delta: netGain = revenue - cost.",
            "animals": "A squirrel storing 14 nuts and eating 10, saving a net profit of 4 nuts for winter."
        },
        "prompt": "Kiran buys old newspapers for ₹10 per kg and sells them to a recycling depot for ₹14 per kg. How much profit does she earn per kg?",
        "options": ["₹4 per kg", "₹24 per kg", "₹14 per kg", "₹5 per kg"],
        "answer": "₹4 per kg",
        "exp": "Profit = Selling Price - Cost Price = ₹14 - ₹10 = ₹4 per kg.",
        "hints": ["Selling price is ₹14, Cost price is ₹10.", "Profit = 14 - 10.", "Profit is ₹4 per kg."],
        "scaffolds": ["Step 1: Selling Price = ₹14.", "Step 2: Cost Price = ₹10.", "Step 3: Profit = ₹14 - ₹10 = ₹4."]
    },
    (4, "Mathematics", 6): {
        "concept_name": "Halves and Quarters (Fraction Representation)",
        "diff": 3,
        "objectives": ["Identify fractions of a geometric whole", "Recognize equivalent fractions 2/4 = 1/2"],
        "prereq": ["Dividing shapes into equal parts"],
        "std_exp": "When a region is partitioned into 4 equal congruent quarters, shading 2 of them represents $\\frac{2}{4}$, which simplifies to $\\frac{1}{2}$.",
        "simp_exp": "If a round pizza is cut into 4 equal slices and you eat 2 slices, you have eaten half (1/2) of the pizza!",
        "analogies": {
            "space": "Two out of 4 orbital thruster banks active represents 50% (1/2) propulsion thrust.",
            "coding": "Evaluating ratio 2/4 reducing to float 0.5.",
            "animals": "A bird eating 2 berries out of a cluster of 4 equal berries: half the cluster is eaten."
        },
        "prompt": "A round chapati is cut into 4 equal quarters. If you eat 2 of the quarters, what fraction of the chapati have you eaten?",
        "options": ["1/2 (Half)", "1/4 (One quarter)", "3/4 (Three quarters)", "1/3 (One third)"],
        "answer": "1/2 (Half)",
        "exp": "2 parts out of 4 equal parts is 2/4. Dividing numerator and denominator by 2 gives 1/2 (one half).",
        "hints": ["2 out of 4 equal parts.", "2 is exactly half of 4.", "2/4 = 1/2."],
        "scaffolds": ["Step 1: Fraction = 2/4.", "Step 2: Simplify by dividing by 2: (2÷2)/(4÷2) = 1/2.", "Step 3: Fraction is 1/2."]
    },
    (4, "Mathematics", 7): {
        "concept_name": "Tables and Shares (Division with Equal Sets)",
        "diff": 3,
        "objectives": ["Solve word problems involving division", "Calculate items per set"],
        "prereq": ["Multiplication tables up to 10"],
        "std_exp": "Equally dividing a dividend by a divisor determines the quotient: $28 \\div 4 = 7$.",
        "simp_exp": "Distributing 28 glass marbles equally into 4 bags puts exactly 7 marbles in each bag!",
        "analogies": {
            "space": "Dividing 28 science samples equally into 4 return cargo pods gives 7 samples per pod.",
            "coding": "Array partitioning: splitting 28 elements into 4 balanced chunks of 7.",
            "animals": "A flock of 28 birds landing equally across 4 tree branches: 7 birds per branch."
        },
        "prompt": "A teacher distributes 28 colorful craft papers equally among 4 student groups. How many craft papers does each group receive?",
        "options": ["7 craft papers", "6 craft papers", "8 craft papers", "9 craft papers"],
        "answer": "7 craft papers",
        "exp": "Divide total craft papers by groups: 28 ÷ 4 = 7 papers per group.",
        "hints": ["Think: 4 times what number equals 28?", "4 × 7 = 28.", "Each group gets 7 craft papers."],
        "scaffolds": ["Step 1: Total = 28.", "Step 2: Groups = 4.", "Step 3: 28 ÷ 4 = 7."]
    },
    (4, "Mathematics", 8): {
        "concept_name": "Fields and Fences (Perimeter of a Rectangle)",
        "diff": 3,
        "objectives": ["Calculate perimeter of a rectangle", "Apply formula: Perimeter = 2 * (Length + Width)"],
        "prereq": ["Addition of 2-digit numbers"],
        "std_exp": "The perimeter of a rectangle is the total distance around its boundary: $P = 2 \\times (L + W)$. For $L = 8\\text{ m}, W = 5\\text{ m}$, $P = 2 \\times (8 + 5) = 26\\text{ m}$.",
        "simp_exp": "To build a fence around a garden 8 metres long and 5 metres wide, add all sides: 8 + 5 + 8 + 5 = 26 metres!",
        "analogies": {
            "space": "Perimeter boundary of an exploration rover solar charging zone measuring 8m by 5m.",
            "coding": "Bounding rect perimeter: 2 * (width + height).",
            "animals": "A guard dog walking the outer boundary fence of an 8m by 5m pasture."
        },
        "prompt": "A rectangular vegetable patch is 8 metres long and 5 metres wide. What length of wire fence is needed to enclose the entire boundary?",
        "options": ["26 metres", "40 metres", "13 metres", "24 metres"],
        "answer": "26 metres",
        "exp": "Perimeter = 2 × (Length + Width) = 2 × (8 + 5) = 2 × 13 = 26 metres.",
        "hints": ["Add all 4 sides: 8 + 5 + 8 + 5.", "8 + 5 = 13, and 13 × 2 = 26.", "The perimeter is 26 metres."],
        "scaffolds": ["Step 1: Length = 8 m, Width = 5 m.", "Step 2: Sum of two sides = 8 + 5 = 13 m.", "Step 3: Perimeter = 13 × 2 = 26 m."]
    },

    # --- CLASS 4 SCIENCE (EVS) ---
    (4, "Science", 1): {
        "concept_name": "Going to School & Geography (Bridges)",
        "diff": 3,
        "objectives": ["Identify regional adaptations in India", "Understand why Assam uses bamboo bridges"],
        "prereq": ["Indian geography awareness"],
        "std_exp": "In Assam, heavy monsoon rains frequently flood roads, necessitating elevated bridges built from locally abundant bamboo and rope.",
        "simp_exp": "Because Assam receives very heavy rain and flooding, children cross elevated bamboo bridges to reach school safely!",
        "analogies": {
            "space": "Lightweight carbon-fiber truss bridges deployed across craters on planetary bases.",
            "coding": "Adapter design pattern bridging disparate system protocols across network gaps.",
            "animals": "Monkeys holding hands to form living bridges across rainforest canopy gaps."
        },
        "prompt": "In which northeastern state of India do children walk across elevated bamboo and rope bridges to reach school because of heavy monsoon rain?",
        "options": ["Assam", "Rajasthan", "Gujarat", "Punjab"],
        "answer": "Assam",
        "exp": "Assam receives intense monsoon rainfall that floods rivers, so communities build raised bamboo bridges for safe crossing.",
        "hints": ["It is famous for tea gardens and the Brahmaputra river.", "It is in Northeast India.", "The state is Assam."],
        "scaffolds": ["Step 1: Clue = heavy rainfall and bamboo bridges.", "Step 2: Match state = Assam.", "Step 3: Select 'Assam'."]
    },
    (4, "Science", 2): {
        "concept_name": "Anita and the Honeybees (Bee Colony Castes)",
        "diff": 3,
        "objectives": ["Identify honeybee caste roles", "Recognize the Queen bee's reproductive function"],
        "prereq": ["Insects observation"],
        "std_exp": "A honeybee colony has a strict division of labor: one fertile Queen bee lays thousands of eggs, worker bees collect nectar, and drones mate.",
        "simp_exp": "In a busy beehive, the Queen bee is the most important mother bee who lays all the eggs for the colony!",
        "analogies": {
            "space": "A mothership primary module carrying all embryo growth incubators for deep colony missions.",
            "coding": "A master database node responsible for all write transactions and record creation.",
            "animals": "An ant queen living deep in the underground chamber laying eggs for the anthill."
        },
        "prompt": "In a honeybee colony, which single specialized female bee is responsible for laying all the eggs to grow the colony?",
        "options": ["The Queen bee", "The Worker bee", "The Drone bee", "The Soldier bee"],
        "answer": "The Queen bee",
        "exp": "The Queen bee is the sole fertile female in the hive whose primary biological responsibility is laying eggs.",
        "hints": ["She is the largest bee in the hive.", "She lays up to 2,000 eggs a day.", "She is the Queen bee."],
        "scaffolds": ["Step 1: Role = laying eggs in colony.", "Step 2: Female caste = Queen bee.", "Step 3: Choose 'The Queen bee'."]
    },
    (4, "Science", 3): {
        "concept_name": "A River's Tale (Water Pollution)",
        "diff": 3,
        "objectives": ["Identify sources of river contamination", "Understand industrial runoff impact"],
        "prereq": ["Freshwater ecology"],
        "std_exp": "Rivers originate pure and clear in mountain glaciers, but accumulate chemical waste, sewage, and debris as they pass through cities.",
        "simp_exp": "River water gets polluted and brown when dirty sewage and toxic chemical waste from city factories are dumped into it!",
        "analogies": {
            "space": "Contamination in an astronaut closed-loop water recycler when filtration scrubbers fail.",
            "coding": "Data stream pollution when corrupted packets bypass upstream validation filters.",
            "animals": "Freshwater fish migrating away from contaminated river water to survive."
        },
        "prompt": "As a clear mountain river flows past large cities and industrial zones, what primarily causes its water to turn dirty and unsafe for drinking?",
        "options": [
            "Dumping of factory chemical waste and untreated city sewage",
            "Fish swimming in the water",
            "Sunlight shining on the water",
            "Clean mountain snow melting into it"
        ],
        "answer": "Dumping of factory chemical waste and untreated city sewage",
        "exp": "Industrial effluents, chemical dumping, and domestic sewage pollute river ecosystems, threatening aquatic life and making water toxic.",
        "hints": ["Fish and sunlight are natural.", "Pollution comes from human factories and cities dumping waste.", "Factory waste and sewage."],
        "scaffolds": ["Step 1: Identify pollutant source = human factories and cities.", "Step 2: Mechanism = dumping untreated waste.", "Step 3: Choose factory waste and sewage."]
    },
    (4, "Science", 4): {
        "concept_name": "From Seed to Sprout (Seed Germination)",
        "diff": 3,
        "objectives": ["Identify conditions required for seed germination", "Recognize need for moisture, air, and warmth"],
        "prereq": ["Plants growth basics"],
        "std_exp": "Seed germination requires moisture (water) to soften the seed coat, oxygen (air) for cellular respiration, and optimal warmth.",
        "simp_exp": "To sprout into a healthy green seedling, a dry seed needs water, fresh air, and gentle warmth!",
        "analogies": {
            "space": "Automated Martian greenhouse chambers regulating hydration, oxygen, and temperature to sprout wheat seeds.",
            "coding": "Container initialization checks: verifying dependencies (DB, Redis, Network) before starting server.",
            "animals": "Bird eggs requiring warmth from the mother's body and airflow through the porous shell to hatch."
        },
        "prompt": "Which combination of essential environmental conditions does a dormant bean seed need to successfully sprout (germinate)?",
        "options": ["Water, Air, and Warmth", "Complete darkness and freezing ice", "Only dry chemical fertilizer", "No water and zero air"],
        "answer": "Water, Air, and Warmth",
        "exp": "Seeds need water to activate metabolic enzymes, air (oxygen) for respiration, and suitable warmth to grow into seedlings.",
        "hints": ["Without water a seed stays dry and dormant.", "It also needs air to breathe and warmth.", "Water, Air, and Warmth."],
        "scaffolds": ["Step 1: Seeds require hydration = Water.", "Step 2: Seeds require respiration = Air.", "Step 3: Seeds require temperature = Warmth."]
    },

    # --- CLASS 4 ENGLISH ---
    (4, "English", 1): {
        "concept_name": "Wake Up! & Neha's Alarm Clock",
        "diff": 3,
        "objectives": ["Understand the internal biological clock", "Identify circadian rhythm in literature"],
        "prereq": ["Reading comprehension"],
        "std_exp": "In 'Neha's Alarm Clock', Neha realizes that even when her clock, birds, and mother don't wake her, her internal body clock wakes her up at 6:00.",
        "simp_exp": "Inside each of us is an internal body clock that reminds us when to wake up, when to eat lunch, and when to sleep!",
        "analogies": {
            "space": "The spacecraft master quartz clock synchronizing telemetry cycles irrespective of external day or night.",
            "coding": "A background setInterval timer triggering scheduled cron updates.",
            "animals": "Roosters crowing reliably at 5:00 AM using their internal circadian rhythm."
        },
        "prompt": "In the charming story 'Neha's Alarm Clock', what mysterious internal clock wakes up Neha at 6:00 AM even when her alarm clock is turned off?",
        "options": ["Her own internal body clock", "A loud railway horn outside", "Her dog barking at a cat", "A talking computer"],
        "answer": "Her own internal body clock",
        "exp": "Mother explains to Neha that every human has an internal body clock that prompts them when to eat, sleep, and wake up.",
        "hints": ["It is inside her own body.", "It tells us when we are hungry or sleepy.", "It is her internal body clock."],
        "scaffolds": ["Step 1: All external alarms failed.", "Step 2: Mother explains human biology.", "Step 3: Neha's internal body clock."]
    },
    (4, "English", 2): {
        "concept_name": "Alice in Wonderland & Curiosity",
        "diff": 3,
        "objectives": ["Recall story details from Lewis Carroll's classic", "Recognize the White Rabbit's unusual traits"],
        "prereq": ["Classic story comprehension"],
        "std_exp": "Alice was captivated when she saw a White Rabbit take a pocket watch out of its waistcoat pocket and hurry down a large rabbit hole.",
        "simp_exp": "Alice chased a curious White Rabbit with pink eyes who wore a waistcoat and checked a golden pocket watch!",
        "analogies": {
            "space": "Following an unexpected orbital telemetry beacon that leads an astronaut into an uncharted wormhole.",
            "coding": "Tracing an intriguing stack trace log that leads deep into legacy codebase architecture.",
            "animals": "A wild rabbit darting swiftly through meadow burrows."
        },
        "prompt": "In 'Alice in Wonderland', what extraordinary item did the White Rabbit pull out of his waistcoat pocket that astonished Alice?",
        "options": ["A pocket watch", "A gold coin", "A magic wand", "A compass"],
        "answer": "A pocket watch",
        "exp": "Alice was amazed because rabbits do not wear waistcoats or carry pocket watches to check the time.",
        "hints": ["It tells the time.", "The rabbit looked at it and cried 'Oh dear, I shall be late!'", "It was a pocket watch."],
        "scaffolds": ["Step 1: Character = White Rabbit.", "Step 2: Action = checking if he was late.", "Step 3: Object = Pocket watch."]
    },
    (4, "English", 3): {
        "concept_name": "Courage and Inclusion - Helen Keller",
        "diff": 3,
        "objectives": ["Understand sensory inclusion", "Recall Helen Keller's breakthrough with Miss Sullivan"],
        "prereq": ["Biographical reading"],
        "std_exp": "Helen Keller, who lost both sight and hearing as an infant, understood language when Miss Sullivan spelled 'W-A-T-E-R' while pumping cool water over her hand.",
        "simp_exp": "Helen's world opened up when cool water flowed over one hand while her teacher spelled W-A-T-E-R on her palm!",
        "analogies": {
            "space": "Establishing a tactile telemetry interface when both visual screens and radio audio fail.",
            "coding": "Mapping raw sensor touch input into symbolic ASCII character encoding.",
            "animals": "Dolphins using tactile flipper contact to communicate affection and navigation intent."
        },
        "prompt": "What life-changing word did dedicated teacher Anne Sullivan spell onto Helen Keller's palm while cool water pumped over her hand?",
        "options": ["W-A-T-E-R", "M-O-T-H-E-R", "S-C-H-O-O-L", "L-I-G-H-T"],
        "answer": "W-A-T-E-R",
        "exp": "The connection between the physical sensation of cool liquid and the tactile letters W-A-T-E-R unlocked language for Helen.",
        "hints": ["It was cool liquid running from a water pump.", "It spelled the name of what she drank.", "The word was W-A-T-E-R."],
        "scaffolds": ["Step 1: Context = pump water over hand.", "Step 2: Spelled letters = W-A-T-E-R.", "Step 3: Word is WATER."]
    },
    (4, "English", 4): {
        "concept_name": "The Giving Tree & Environmental Values",
        "diff": 3,
        "objectives": ["Identify literary themes of selflessness", "Recognize reciprocity in nature"],
        "prereq": ["Reading with reflection"],
        "std_exp": "In Shel Silverstein's 'The Giving Tree', the tree exemplifies unconditional love by giving its apples, branches, and trunk to make the boy happy.",
        "simp_exp": "The loving tree gave its sweet apples for food, its branches to build a home, and its trunk to build a boat!",
        "analogies": {
            "space": "A planetary habitat module that selflessly exhausts all stored solar energy to sustain life for colonists.",
            "coding": "A shared core open-source library that powers thousands of downstream applications without demanding payment.",
            "animals": "A pelican mother feeding her hungry chicks with everything she gathers from the sea."
        },
        "prompt": "In the moving story 'The Giving Tree', what was the tree's emotional state whenever it gave its gifts to the boy?",
        "options": ["The tree was truly happy", "The tree was angry and bitter", "The tree was scared and wept", "The tree wanted revenge"],
        "answer": "The tree was truly happy",
        "exp": "Throughout the story, despite giving away everything it possessed, 'and the tree was happy' because of its selfless love.",
        "hints": ["The tree loved the boy unconditionally.", "Giving made the tree feel joyful.", "The tree was truly happy."],
        "scaffolds": ["Step 1: Theme = unconditional love and giving.", "Step 2: Key recurring refrain in the book.", "Step 3: 'The tree was happy'."]
    },

    # =========================================================================
    # CLASS 5
    # =========================================================================
    (5, "Mathematics", 1): {
        "concept_name": "The Fish Tale (Speed, Distance, Time & Large Numbers)",
        "diff": 3,
        "objectives": ["Apply speed formula: Distance = Speed * Time", "Understand large number denominations"],
        "prereq": ["Multiplication of 2-digit numbers"],
        "std_exp": "Distance equals speed multiplied by time ($D = v \\times t$). A motorboat traveling at $20\\text{ km/h}$ covers $20 \\times 3 = 60\\text{ km}$ in 3 hours.",
        "simp_exp": "If a boat travels 20 kilometres in 1 hour, in 3 hours it travels 20 + 20 + 20 = 60 kilometres!",
        "analogies": {
            "space": "A space probe traveling at 20 km per second covers 60 km in 3 seconds.",
            "coding": "Physics engine translation: position.x += speed * deltaTime.",
            "animals": "A fast marlin fish cruising at 20 km/h covering 60 km across the ocean reef."
        },
        "prompt": "A fisherman's motorboat travels across the sea at a steady speed of 20 kilometres per hour. How far will the boat travel in 3 hours?",
        "options": ["60 kilometres", "40 kilometres", "50 kilometres", "80 kilometres"],
        "answer": "60 kilometres",
        "exp": "Distance = Speed × Time = 20 km/h × 3 hours = 60 kilometres.",
        "hints": ["Distance = Speed × Time.", "Multiply 20 by 3.", "20 × 3 = 60 km."],
        "scaffolds": ["Step 1: Speed = 20 km/h.", "Step 2: Time = 3 hours.", "Step 3: Distance = 20 × 3 = 60 km."]
    },
    (5, "Mathematics", 2): {
        "concept_name": "Shapes and Angles (Types of Angles)",
        "diff": 3,
        "objectives": ["Classify angles by degrees", "Recognize a right angle equals 90 degrees"],
        "prereq": ["Using clock hands as angle rays"],
        "std_exp": "An angle measuring exactly $90^\\circ$ is a right angle; an angle $< 90^\\circ$ is acute, and $> 90^\\circ$ is obtuse.",
        "simp_exp": "The square corner of a book or door makes a perfect 90-degree RIGHT ANGLE like the letter 'L'!",
        "analogies": {
            "space": "Perpendicular orientation of attitude control thrusters firing at 90 degrees to spacecraft velocity.",
            "coding": "Perpendicular raycasting vectors with dot product equal to 0.",
            "animals": "A praying mantis holding its front raptorial arms at a sharp 90-degree right angle."
        },
        "prompt": "What is the exact name of an angle that forms a perfect 'L' square corner and measures exactly 90 degrees?",
        "options": ["Right angle", "Acute angle", "Obtuse angle", "Reflex angle"],
        "answer": "Right angle",
        "exp": "An angle of exactly 90 degrees is defined as a Right Angle.",
        "hints": ["It looks like the letter L.", "The corner of a square is 90°.", "It is called a right angle."],
        "scaffolds": ["Step 1: Angle measure = 90°.", "Step 2: Geometry classification = Right angle.", "Step 3: Choose 'Right angle'."]
    },
    (5, "Mathematics", 3): {
        "concept_name": "How Many Squares? (Area of a Rectangle)",
        "diff": 3,
        "objectives": ["Calculate area using grid units", "Apply formula: Area = Length * Width"],
        "prereq": ["Multiplication facts"],
        "std_exp": "The area of a rectangle is the product of its length and width: $\\text{Area} = L \\times W = 6\\text{ cm} \\times 4\\text{ cm} = 24\\text{ sq cm}$.",
        "simp_exp": "A rectangle 6 cm long and 4 cm wide contains 6 rows of 4 square centimetres = 24 square cm in total!",
        "analogies": {
            "space": "Surface area of solar cell array panels: 6 meters by 4 meters yields 24 square meters of solar collection area.",
            "coding": "2D texture buffer pixel resolution: width * height = total pixels.",
            "animals": "A honeycomb section containing 6 rows of 4 hexagonal storage chambers = 24 chambers."
        },
        "prompt": "A rectangular bookmark is 6 cm long and 4 cm wide. How many square centimetres (sq cm) of paper are there on its surface area?",
        "options": ["24 sq cm", "20 sq cm", "10 sq cm", "28 sq cm"],
        "answer": "24 sq cm",
        "exp": "Area of rectangle = Length × Width = 6 cm × 4 cm = 24 sq cm.",
        "hints": ["Area = Length × Width.", "Multiply 6 by 4.", "6 × 4 = 24 sq cm."],
        "scaffolds": ["Step 1: Length = 6 cm, Width = 4 cm.", "Step 2: Area formula = L × W.", "Step 3: 6 × 4 = 24 sq cm."]
    },
    (5, "Mathematics", 4): {
        "concept_name": "Parts and Wholes (Fraction Addition)",
        "diff": 3,
        "objectives": ["Add fractions with like denominators", "Simplify fractions"],
        "prereq": ["Fractions representation"],
        "std_exp": "To add fractions with identical denominators, add the numerators while retaining the common denominator: $\\frac{1}{4} + \\frac{2}{4} = \\frac{3}{4}$.",
        "simp_exp": "One quarter plus two quarters equals three quarters (3/4)!",
        "analogies": {
            "space": "Fuel tank capacity: 1/4 tank remaining + 2/4 tank refilled = 3/4 full.",
            "coding": "Fraction addition class: add(new Fraction(1,4), new Fraction(2,4)) = 3/4.",
            "animals": "A turtle swimming 1/4 across the pond, resting, then swimming 2/4 more: 3/4 total distance covered."
        },
        "prompt": "Reena ate 1/4 of a chocolate bar in the morning and 2/4 of the same bar in the afternoon. What total fraction did she eat?",
        "options": ["3/4", "3/8", "1/2", "2/4"],
        "answer": "3/4",
        "exp": "When denominators are the same, add numerators: 1/4 + 2/4 = (1 + 2)/4 = 3/4.",
        "hints": ["Denominators are both 4.", "Add the top numbers: 1 + 2 = 3.", "The total is 3/4."],
        "scaffolds": ["Step 1: Common denominator = 4.", "Step 2: Numerators sum = 1 + 2 = 3.", "Step 3: Fraction = 3/4."]
    },
    (5, "Mathematics", 5): {
        "concept_name": "Be My Multiple, I'll be Your Factor (LCM)",
        "diff": 3,
        "objectives": ["Find least common multiples (LCM)", "Identify common multiples of two integers"],
        "prereq": ["Times tables for 4 and 6"],
        "std_exp": "The Least Common Multiple (LCM) of 4 and 6 is the smallest non-zero positive integer divisible by both: $\\text{LCM}(4, 6) = 12$.",
        "simp_exp": "Multiples of 4: 4, 8, 12, 16... Multiples of 6: 6, 12, 18... The very first number they both share is 12!",
        "analogies": {
            "space": "Orbital synchronization: two satellites orbiting every 4 hours and 6 hours align together every 12 hours.",
            "coding": "Finding periodic sync cycle between two polling timers: lcm(4, 6) = 12.",
            "animals": "Two cicadas singing on 4-day and 6-day cycles singing in chorus on the 12th day."
        },
        "prompt": "What is the SMALLEST positive common multiple (LCM) shared by both the numbers 4 and 6?",
        "options": ["12", "24", "10", "18"],
        "answer": "12",
        "exp": "Multiples of 4: 4, 8, 12, 16... Multiples of 6: 6, 12, 18... The least common multiple is 12.",
        "hints": ["List multiples of 4: 4, 8, 12, 16.", "List multiples of 6: 6, 12, 18.", "The smallest shared number is 12."],
        "scaffolds": ["Step 1: Multiples of 4 = 4, 8, 12, 16, 20.", "Step 2: Multiples of 6 = 6, 12, 18, 24.", "Step 3: Smallest common number = 12."]
    },
    (5, "Mathematics", 6): {
        "concept_name": "Tenths and Hundredths (Decimal Currency)",
        "diff": 3,
        "objectives": ["Convert paise into decimal Rupees", "Understand hundredths place value: 1 Rupee = 100 paise"],
        "prereq": ["Fractions to decimals"],
        "std_exp": "Since $1\\text{ Rupee} = 100\\text{ paise}$, $75\\text{ paise} = \\frac{75}{100}\\text{ Rupees} = ₹0.75$.",
        "simp_exp": "75 paise is 75 hundredths of a rupee, written as ₹0.75!",
        "analogies": {
            "space": "Telemetry battery level: 75 out of 100 millivolts expressed as 0.75 volts.",
            "coding": "Floating point formatting: (75 / 100).toFixed(2) = '0.75'.",
            "animals": "A chameleon that has shed 75 out of 100 scales: 0.75 of the molt complete."
        },
        "prompt": "If a postage stamp costs 75 paise, how is this amount correctly written in Indian Rupees using a decimal point?",
        "options": ["₹0.75", "₹7.50", "₹75.00", "₹0.075"],
        "answer": "₹0.75",
        "exp": "1 Rupee = 100 paise. Therefore, 75 paise = 75/100 = ₹0.75.",
        "hints": ["100 paise = ₹1.00.", "75 paise is less than 1 Rupee.", "It is written as ₹0.75."],
        "scaffolds": ["Step 1: Conversion rate: 100 paise = ₹1.", "Step 2: 75 ÷ 100 = 0.75.", "Step 3: ₹0.75."]
    },
    (5, "Mathematics", 7): {
        "concept_name": "Area and its Boundary (Square Area & Perimeter)",
        "diff": 3,
        "objectives": ["Compute perimeter and area of a square", "Distinguish boundary length from surface area"],
        "prereq": ["Multiplication"],
        "std_exp": "For a square of side $s = 5\\text{ cm}$: Perimeter $= 4 \\times s = 20\\text{ cm}$; Area $= s^2 = 25\\text{ sq cm}$.",
        "simp_exp": "Boundary fence is 5 + 5 + 5 + 5 = 20 cm. Inside floor area is 5 × 5 = 25 square cm!",
        "analogies": {
            "space": "A square solar panel of 5m side has a 20m structural perimeter and generates power across 25 sq m.",
            "coding": "Square viewport: perimeter = 4 * side, area = side * side.",
            "animals": "A mother bird guarding a square territory of 5m side: perimeter is 20m, hunting area is 25 sq m."
        },
        "prompt": "A square tile has side length of 5 cm. What are its PERIMETER (boundary) and its AREA (surface)?",
        "options": [
            "Perimeter = 20 cm, Area = 25 sq cm",
            "Perimeter = 25 cm, Area = 20 sq cm",
            "Perimeter = 10 cm, Area = 15 sq cm",
            "Perimeter = 20 cm, Area = 20 sq cm"
        ],
        "answer": "Perimeter = 20 cm, Area = 25 sq cm",
        "exp": "Perimeter = 4 × side = 4 × 5 = 20 cm. Area = side × side = 5 × 5 = 25 sq cm.",
        "hints": ["Perimeter = 4 × side = 4 × 5 = 20 cm.", "Area = side × side = 5 × 5 = 25 sq cm.", "Perimeter is 20 cm, Area is 25 sq cm."],
        "scaffolds": ["Step 1: Side = 5 cm.", "Step 2: Perimeter = 4 × 5 = 20 cm.", "Step 3: Area = 5 × 5 = 25 sq cm."]
    },

    # --- CLASS 5 SCIENCE (EVS) ---
    (5, "Science", 1): {
        "concept_name": "Super Senses (Animal Sensory Biology)",
        "diff": 3,
        "objectives": ["Understand animal communication", "Identify ant chemical pheromone trails"],
        "prereq": ["Animal behavior observation"],
        "std_exp": "Ants navigate and communicate food locations by depositing chemical scent markers called pheromones on the ground.",
        "simp_exp": "As ants march forward, they leave a trail of smell (pheromones) on the ground so other ants can follow behind in a neat line!",
        "analogies": {
            "space": "Breadcrumb radio transponders deployed along an asteroid surface to guide extraction rovers.",
            "coding": "Distributed tracing headers passed across microservices to trace the request execution path.",
            "animals": "Wolf packs howling across mountain valleys to communicate hunting boundaries."
        },
        "prompt": "When marching in an organized straight line toward sugar, what do worker ants leave on the ground for other ants to follow?",
        "options": ["A trail of chemical smell (pheromones)", "Tiny footprints carved in stone", "Flashing colorful light signals", "A trail of salt crystals"],
        "answer": "A trail of chemical smell (pheromones)",
        "exp": "Ants secrete chemical scent markers (pheromones) that other colony members detect with their antennae to follow the trail.",
        "hints": ["They use their sense of smell.", "The lead ant leaves a scented chemical trail.", "They leave a trail of smell (pheromones)."],
        "scaffolds": ["Step 1: Behavior = ants walking in line.", "Step 2: Communication medium = chemical scent.", "Step 3: Answer is pheromone smell trail."]
    },
    (5, "Science", 2): {
        "concept_name": "From Tasting to Digesting (Human Digestion)",
        "diff": 3,
        "objectives": ["Identify initial stage of human digestion", "Recognize saliva's role in breaking down starch"],
        "prereq": ["Body organs"],
        "std_exp": "Digestion initiates in the oral cavity where salivary amylase enzymatically breaks down complex carbohydrates (starches) into simpler sugars.",
        "simp_exp": "Digestion begins right in your mouth when teeth chew and watery saliva starts breaking down food into sweet sugars!",
        "analogies": {
            "space": "Initial shredding and chemical pre-treatment of solid waste before secondary bioreactor processing.",
            "coding": "Request middleware sanitizing and parsing incoming JSON payloads before controller handling.",
            "animals": "A cow chewing its cud repeatedly to allow salivary enzymes to begin breaking down cellulose."
        },
        "prompt": "Where in the human body does the very FIRST step of digestion begin as food is chewed and mixed with saliva?",
        "options": ["In the mouth", "In the stomach", "In the small intestine", "In the lungs"],
        "answer": "In the mouth",
        "exp": "Digestion begins in the mouth where teeth mechanically break down food and saliva enzymatically starts digesting starches.",
        "hints": ["Think about where food enters your body first.", "Your teeth chew it and saliva mixes with it.", "Digestion starts in the mouth."],
        "scaffolds": ["Step 1: First point of digestive tract = Mouth.", "Step 2: Mechanical chewing + salivary amylase.", "Step 3: Select 'In the mouth'."]
    },
    (5, "Science", 3): {
        "concept_name": "Experiments with Water (Density & Buoyancy)",
        "diff": 3,
        "objectives": ["Understand density and buoyancy", "Recognize why salt water increases buoyant force"],
        "prereq": ["Floating and sinking"],
        "std_exp": "Dissolving salt in water increases liquid density and buoyant upthrust force, allowing dense objects (like eggs or swimmers) to float.",
        "simp_exp": "In the Dead Sea, water has so much dissolved salt that it is super dense, allowing people and eggs to float effortlessly on the surface!",
        "analogies": {
            "space": "Dense planetary atmospheres providing greater aerodynamic lift to atmospheric entry gliders.",
            "coding": "High-density hash tables providing immediate O(1) lookup efficiency.",
            "animals": "Water striders distributing their weight across water surface tension to glide."
        },
        "prompt": "A fresh egg sinks to the bottom in plain tap water. What happens when you dissolve plenty of table salt into the water?",
        "options": ["The egg floats to the top", "The egg explodes instantly", "The egg turns into ice", "The egg dissolves completely"],
        "answer": "The egg floats to the top",
        "exp": "Dissolving salt increases water density. When the salty water becomes denser than the egg, the buoyant force pushes the egg up to float.",
        "hints": ["Salt makes water heavier and denser.", "Dense liquid pushes objects upward.", "The egg floats to the top."],
        "scaffolds": ["Step 1: Plain water: Egg density > Water density (sinks).", "Step 2: Add salt: Salty water density > Egg density.", "Step 3: The egg floats."]
    },
    (5, "Science", 4): {
        "concept_name": "Sunita in Space (Gravitation & Microgravity)",
        "diff": 3,
        "objectives": ["Understand microgravity in orbital flight", "Explain why astronauts float"],
        "prereq": ["Earth's gravity"],
        "std_exp": "Astronauts aboard the orbiting ISS experience microgravity (apparent weightlessness) because the station is in continuous free-fall around Earth.",
        "simp_exp": "Inside the orbiting space station, there is zero effective weight, so astronaut Sunita Williams and her water droplets floated in mid-air!",
        "analogies": {
            "space": "The ISS orbiting at 28,000 km/h in perpetual free-fall around Earth's curvature.",
            "coding": "Setting rigidBody.useGravity = false in a 3D physics simulation engine.",
            "animals": "A scuba diver achieving neutral buoyancy hovering motionless mid-depth in coral seas."
        },
        "prompt": "When astronaut Sunita Williams lived aboard the International Space Station, why did her hair stand up and her food float in mid-air?",
        "options": [
            "Because of microgravity (apparent weightlessness in orbit)",
            "Because giant fans blew air upwards constantly",
            "Because space capsules have magnetic floors",
            "Because there was no air inside the cabin"
        ],
        "answer": "Because of microgravity (apparent weightlessness in orbit)",
        "exp": "In orbit, the spacecraft and astronauts are in continuous free fall, creating apparent weightlessness (microgravity) where objects float.",
        "hints": ["There is normal breathable air inside the station.", "Objects float because gravity isn't pulling them onto a floor.", "It is due to microgravity."],
        "scaffolds": ["Step 1: Phenomenon = floating in space station.", "Step 2: Cause = orbital free fall (microgravity).", "Step 3: Choose microgravity."]
    },

    # --- CLASS 5 ENGLISH ---
    (5, "English", 1): {
        "concept_name": "Wonderful Waste! (Culinary Upcycling)",
        "diff": 3,
        "objectives": ["Recall story details of Avial origin", "Value creative reuse and sustainability"],
        "prereq": ["Story comprehension"],
        "std_exp": "In the traditional folklore of Travancore (Kerala), the Maharaja ordered his cook not to waste vegetable scraps, leading to the creation of the famous dish 'Avial'.",
        "simp_exp": "The clever cook boiled washed vegetable scraps with coconut, green chilies, and curry leaves to invent the delicious Kerala dish 'Avial'!",
        "analogies": {
            "space": "Recycling booster stage structural alloys into orbital habitat expansion frames.",
            "coding": "Refactoring deprecated legacy code modules into reusable utility libraries.",
            "animals": "Hermit crabs adopting discarded snail shells as protective mobile homes."
        },
        "prompt": "In the delightful Kerala folktale 'Wonderful Waste!', which famous traditional feast dish was invented by creatively cooking leftover vegetable scraps?",
        "options": ["Avial", "Biryani", "Sambar", "Dosa"],
        "answer": "Avial",
        "exp": "Avial is the traditional Kerala mixed-vegetable dish created when the cook seasoned vegetable peelings and scraps with coconut and curd.",
        "hints": ["It is a famous traditional Kerala dish.", "It begins with the letter 'A'.", "The dish is Avial."],
        "scaffolds": ["Step 1: Setting = Palace of Travancore, Kerala.", "Step 2: Cook used vegetable scraps.", "Step 3: Dish created was Avial."]
    },
    (5, "English", 2): {
        "concept_name": "Teamwork & Flying Together",
        "diff": 3,
        "objectives": ["Identify the wisdom of elder advice", "Understand collective action"],
        "prereq": ["Fable comprehension"],
        "std_exp": "In 'Flying Together', an old wise bird advised the flock of wild geese to destroy a tiny creeper before it grew thick enough for a hunter to climb.",
        "simp_exp": "The wise old bird warned the geese: 'Destroy the young creeper while it is small, or a hunter will climb up our tree!'",
        "analogies": {
            "space": "Patching a tiny orbital seal micro-leak immediately before it compromises pressure across the station.",
            "coding": "Fixing a small memory leak in code before it accumulates and crashes production servers.",
            "animals": "An experienced elephant matriarch leading the herd away from drought valleys."
        },
        "prompt": "In the fable 'Flying Together', why did the wise old goose urge the flock to destroy the tender young creeper at the foot of the tree?",
        "options": [
            "Lest it grow thick and allow a hunter to climb up and catch them",
            "Because it had bad-tasting leaves",
            "Because it blocked sunlight from the river",
            "Because the birds wanted to eat it"
        ],
        "answer": "Lest it grow thick and allow a hunter to climb up and catch them",
        "exp": "The wise bird foresaw that when the creeper grew into a strong rope, a hunter could easily climb up the tall tree and trap the flock.",
        "hints": ["A thick creeper acts like a ladder.", "A hunter could use it to climb.", "It could help a hunter catch them."],
        "scaffolds": ["Step 1: Warning = destroy creeper.", "Step 2: Consequence of waiting = creeper becomes ladder.", "Step 3: Hunter could climb up."]
    },
    (5, "English", 3): {
        "concept_name": "Robinson Crusoe & Logical Deduction",
        "diff": 3,
        "objectives": ["Analyze literary suspense and deduction", "Examine Robinson Crusoe's discovery"],
        "prereq": ["Reading with inference"],
        "std_exp": "Living alone on an isolated island, Robinson Crusoe was filled with terror when he discovered the distinct print of a human foot on the sand.",
        "simp_exp": "Robinson Crusoe had lived alone for years until he was shocked to find the print of a man's naked foot on the beach sand!",
        "analogies": {
            "space": "An astronaut discovering an unexpected alien boot print in the untouched red dust of Mars.",
            "coding": "Discovering an unrecorded SSH session log timestamped at midnight in a restricted secure bastion host.",
            "animals": "A solitary leopard freezing when smelling fresh scent marks of a rival in its hunting territory."
        },
        "prompt": "In the gripping adventure story, what startling discovery on the sandy beach filled solitary Robinson Crusoe with astonishment and fear?",
        "options": [
            "The print of a man's naked foot in the sand",
            "A chest filled with golden pirate coins",
            "A broken ship anchor buried in mud",
            "A giant sea turtle laying eggs"
        ],
        "answer": "The print of a man's naked foot in the sand",
        "exp": "Crusoe saw the distinct print of a human foot—toes, heel, and every part of a foot—proving another human was on the island.",
        "hints": ["He thought he was completely alone on the island.", "He saw an imprint in the sand made by a foot.", "The print of a man's foot."],
        "scaffolds": ["Step 1: Setting = lonely deserted island.", "Step 2: Startling discovery = footprint in sand.", "Step 3: Print of a human foot."]
    },
    (5, "English", 4): {
        "concept_name": "Gulliver's Travels & Relative Scale",
        "diff": 3,
        "objectives": ["Understand relative scale and perspective", "Recognize literary parody in Brobdingnag"],
        "prereq": ["Classic story comprehension"],
        "std_exp": "In Jonathan Swift's satire, Gulliver travels to Brobdingnag, a country inhabited by giants sixty feet tall where Gulliver appears tiny as an insect.",
        "simp_exp": "In the giant land of Brobdingnag, the farmers were as tall as church steeples (60 feet tall) and Gulliver was as tiny as a doll!",
        "analogies": {
            "space": "A tiny exploratory space probe docking beside a massive gargantuan orbital megastructure.",
            "coding": "Comparing microservice payload size (1 kilobyte) to big data data warehouse clusters (petabytes).",
            "animals": "A tiny beetle walking cautiously between the giant paws of an African bull elephant."
        },
        "prompt": "In Jonathan Swift's classic adventure 'Gulliver's Travels', what was extraordinary about the people in the land of Brobdingnag?",
        "options": [
            "They were enormous giants sixty feet tall",
            "They were tiny people only six inches tall",
            "They could fly using feathered wings",
            "They lived completely underwater"
        ],
        "answer": "They were enormous giants sixty feet tall",
        "exp": "In Brobdingnag, everything was gigantic; the farmers were sixty feet tall, making Gulliver look like a miniature creature.",
        "hints": ["In Lilliput people were tiny, but in Brobdingnag they were...", "They were huge giants.", "They were enormous giants sixty feet tall."],
        "scaffolds": ["Step 1: Land = Brobdingnag.", "Step 2: Lilliput = tiny; Brobdingnag = giants.", "Step 3: Giants sixty feet tall."]
    }
}
