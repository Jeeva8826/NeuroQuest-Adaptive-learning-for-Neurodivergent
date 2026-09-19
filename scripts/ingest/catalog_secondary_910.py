"""
Authentic NCERT Academic Questions Catalog for Secondary School: Classes 9 and 10
Subjects: Mathematics, Science, English (35 chapters total)
"""

SECONDARY_910_QUESTIONS = {
    # =========================================================================
    # CLASS 9 (17 Chapters: 7 Math, 6 Science, 4 English)
    # =========================================================================
    # --- Mathematics (7 Chapters) ---
    (9, "Mathematics", 1): {
        "concept_name": "Number Systems (Rationalisation & Irrational Numbers)",
        "diff": 3,
        "objectives": ["Identify irrational numbers on the real number line", "Rationalise denominators containing square roots"],
        "prereq": ["Rational numbers and exponents"],
        "std_exp": "Real numbers comprise rational and irrational numbers. The decimal expansion of an irrational number is non-terminating and non-recurring (e.g., sqrt(2), pi). To rationalise 1 / (sqrt(a) + sqrt(b)), multiply by conjugate (sqrt(a) - sqrt(b)) / (sqrt(a) - sqrt(b)).",
        "simp_exp": "To remove the square root from the bottom of 1 / (sqrt(3) - sqrt(2)), multiply numerator and denominator by (sqrt(3) + sqrt(2)). The bottom becomes (3 - 2) = 1, leaving simply sqrt(3) + sqrt(2)!",
        "analogies": {
            "space": "Signal filtering: removing imaginary noise components from complex Fourier transform signals.",
            "coding": "Normalizing floating-point vectors to eliminate reciprocal radical division in graphics shaders.",
            "animals": "A nautilus shell spiral whose logarithmic growth curve embodies the golden ratio phi."
        },
        "prompt": "Rationalise the denominator of the radical expression: 1 / (sqrt(5) + sqrt(2))",
        "options": [
            "(sqrt(5) - sqrt(2)) / 3",
            "(sqrt(5) + sqrt(2)) / 3",
            "(sqrt(5) - sqrt(2)) / 7",
            "sqrt(5) - sqrt(2)"
        ],
        "answer": "(sqrt(5) - sqrt(2)) / 3",
        "exp": "Multiply numerator and denominator by the conjugate (sqrt(5) - sqrt(2)): (sqrt(5) - sqrt(2)) / ((sqrt(5))^2 - (sqrt(2))^2) = (sqrt(5) - sqrt(2)) / (5 - 2) = (sqrt(5) - sqrt(2)) / 3.",
        "hints": ["Multiply top and bottom by the conjugate: sqrt(5) - sqrt(2).", "In the denominator, apply (a+b)(a-b) = a^2 - b^2.", "5 - 2 = 3 in the denominator."],
        "scaffolds": ["Step 1: Conjugate of (sqrt(5) + sqrt(2)) is (sqrt(5) - sqrt(2)).", "Step 2: Denominator becomes (sqrt(5))^2 - (sqrt(2))^2 = 5 - 2 = 3.", "Step 3: Result is (sqrt(5) - sqrt(2)) / 3."]
    },
    (9, "Mathematics", 2): {
        "concept_name": "Polynomials (Remainder & Factor Theorem)",
        "diff": 3,
        "objectives": ["Apply the Remainder Theorem and Factor Theorem", "Factorise quadratic and cubic polynomials"],
        "prereq": ["Algebraic identities"],
        "std_exp": "By the Factor Theorem, (x - a) is a factor of polynomial p(x) if and only if p(a) = 0. The Remainder Theorem states that when p(x) is divided by (x - a), the remainder is p(a).",
        "simp_exp": "To check if (x - 2) is a factor of p(x) = x^2 - 5x + 6, substitute x = 2: p(2) = 2^2 - 5(2) + 6 = 4 - 10 + 6 = 0. Since the remainder is 0, (x - 2) is indeed a factor!",
        "analogies": {
            "space": "Orbital roots: determining the exact epoch point where satellite velocity vector delta reaches zero.",
            "coding": "Root-finding algorithms (Newton-Raphson) finding zero-crossings of cost functions.",
            "animals": "Locating the exact zero-gradient thermal contour where migrating birds find effortless lift."
        },
        "prompt": "Find the remainder when polynomial p(x) = 2x^3 - 3x^2 + 4x - 5 is divided by (x - 2).",
        "options": ["7", "9", "-1", "5"],
        "answer": "7",
        "exp": "By the Remainder Theorem, the remainder is p(2). Substitute x = 2: p(2) = 2(2^3) - 3(2^2) + 4(2) - 5 = 2(8) - 3(4) + 8 - 5 = 16 - 12 + 8 - 5 = 7.",
        "hints": ["Substitute x = 2 into the polynomial p(x).", "2*(8) - 3*(4) + 4*(2) - 5.", "16 - 12 + 8 - 5 = 7."],
        "scaffolds": ["Step 1: By Remainder Theorem, Remainder = p(2).", "Step 2: p(2) = 2(8) - 3(4) + 8 - 5 = 16 - 12 + 8 - 5.", "Step 3: 4 + 8 - 5 = 7."]
    },
    (9, "Mathematics", 3): {
        "concept_name": "Coordinate Geometry (Cartesian Plane & Quadrants)",
        "diff": 3,
        "objectives": ["Plot coordinates (x, y) on the 2D Cartesian plane", "Identify quadrant signs: Q1 (+,+), Q2 (-,+), Q3 (-,-), Q4 (+,-)"],
        "prereq": ["Number lines"],
        "std_exp": "The Cartesian plane consists of two perpendicular axes: horizontal x-axis (abscissa) and vertical y-axis (ordinate), intersecting at origin (0,0). The 4 quadrants have signed signatures: Q1 (+,+), Q2 (-,+), Q3 (-,-), Q4 (+,-).",
        "simp_exp": "Point (-3, 4) has negative x and positive y. Walk left 3 steps on x, then up 4 steps on y: you are in Quadrant II!",
        "analogies": {
            "space": "Celestial coordinate grid: Right Ascension and Declination fixing stellar positions.",
            "coding": "Screen coordinate rendering (x, y) in canvas/WebGL game viewports.",
            "animals": "A bat using sonar delay (x-distance) and frequency shift (y-height) to pinpoint a moth."
        },
        "prompt": "In which quadrant of the Cartesian coordinate plane does the point P(-4, 5) lie?",
        "options": ["Quadrant II", "Quadrant I", "Quadrant III", "Quadrant IV"],
        "answer": "Quadrant II",
        "exp": "For point P(-4, 5), the x-coordinate (abscissa) is negative (-4) and the y-coordinate (ordinate) is positive (+5). Points with signs (-, +) lie in Quadrant II.",
        "hints": ["Look at the signs of the coordinates: x is negative, y is positive.", "Q1 is (+,+), Q2 is (-,+), Q3 is (-,-), Q4 is (+,-).", "Therefore, (-4, 5) is in Quadrant II."],
        "scaffolds": ["Step 1: Identify sign of x: negative (-4).", "Step 2: Identify sign of y: positive (+5).", "Step 3: Quadrant with (-, +) is Quadrant II."]
    },
    (9, "Mathematics", 4): {
        "concept_name": "Linear Equations in Two Variables (Graphs & Solutions)",
        "diff": 3,
        "objectives": ["Represent linear relationships as ax + by + c = 0", "Find multiple coordinate solutions and graph the resulting straight line"],
        "prereq": ["Coordinate geometry"],
        "std_exp": "A linear equation in two variables ax + by + c = 0 has infinitely many solutions (x, y). Geometrically, every solution corresponds to a unique point on the straight line representing the equation.",
        "simp_exp": "For 2x + y = 7: If x = 0, y = 7. If x = 1, y = 5. If x = 2, y = 3. Connect these dots on graph paper, and they form a continuous straight line!",
        "analogies": {
            "space": "Constrained trajectory vector defining a spacecraft's planar transfer orbit.",
            "coding": "Linear regression boundary separating classification thresholds in binary classifiers.",
            "animals": "A boundary path patrol line walked by an alpha wolf marking its pack perimeter."
        },
        "prompt": "Which of the following ordered pairs (x, y) is a valid solution to the linear equation 3x + 2y = 18?",
        "options": ["(4, 3)", "(2, 5)", "(5, 2)", "(3, 4)"],
        "answer": "(4, 3)",
        "exp": "Substitute x = 4, y = 3 into LHS: 3(4) + 2(3) = 12 + 6 = 18. Since LHS = RHS, (4, 3) is a valid solution.",
        "hints": ["Test each option by substituting x and y into 3x + 2y.", "For (4,3): 3*4 + 2*3 = 12 + 6.", "12 + 6 = 18, matching the equation."],
        "scaffolds": ["Step 1: Test (4, 3): 3(4) + 2(3) = 12 + 6 = 18.", "Step 2: LHS = RHS = 18.", "Step 3: (4, 3) is a solution."]
    },
    (9, "Mathematics", 5): {
        "concept_name": "Lines, Angles & Triangle Congruence (SAS, ASA, SSS, RHS)",
        "diff": 3,
        "objectives": ["Apply triangle congruence criteria: SAS, ASA, SSS, and RHS", "Prove geometric properties of isosceles and equilateral triangles"],
        "prereq": ["Lines and angles"],
        "std_exp": "Two triangles are congruent if all corresponding sides and angles are equal. Criteria: SAS (Side-Angle-Side), ASA (Angle-Side-Angle), SSS (Side-Side-Side), RHS (Right angle-Hypotenuse-Side). AAA does NOT guarantee congruence.",
        "simp_exp": "If two right triangles have equal hypotenuses and one matching side, they are identical twins in size and shape by RHS congruence!",
        "analogies": {
            "space": "Modular docking collars requiring exact congruent geometric dimensions to seal an airlock.",
            "coding": "Deep structural equality assertion between two data objects verifying identical schema.",
            "animals": "Bilateral symmetry in bird wings ensuring equal lift forces during gliding."
        },
        "prompt": "Which of the following is NOT a valid mathematical criterion for establishing the CONGRUENCE of two triangles?",
        "options": ["AAA (Angle-Angle-Angle)", "SAS (Side-Angle-Side)", "RHS (Right angle-Hypotenuse-Side)", "SSS (Side-Side-Side)"],
        "answer": "AAA (Angle-Angle-Angle)",
        "exp": "AAA only guarantees similarity (same shape/proportions), not congruence (same size). A tiny equilateral triangle and a giant equilateral triangle have identical 60° angles but are not congruent.",
        "hints": ["Can two triangles have the same angles but completely different sizes?", "Think of scaling or zooming a photo.", "Equal angles without any side measurement is AAA (similarity, not congruence)."],
        "scaffolds": ["Step 1: Congruence requires triangles to have identical shape AND size.", "Step 2: AAA ensures identical angle shape, but size can vary arbitrarily.", "Step 3: Therefore, AAA is not a congruence criterion."]
    },
    (9, "Mathematics", 6): {
        "concept_name": "Surface Areas and Volumes (Cones, Spheres & Hemispheres)",
        "diff": 3,
        "objectives": ["Compute curved and total surface area of cones and spheres", "Compute volume of right circular cone: V = (1/3) * pi * r^2 * h"],
        "prereq": ["Cylinder surface area and volume"],
        "std_exp": "For a right circular cone with base radius r, height h, and slant height l = sqrt(r^2 + h^2): Curved surface area = pi * r * l; Volume = (1/3) * pi * r^2 * h. For a sphere: Volume = (4/3) * pi * r^3; Surface area = 4 * pi * r^2.",
        "simp_exp": "A cone holds exactly 1/3 the volume of a cylinder with the same base and height! If a cylinder holds 300 ml, a cone of the same size holds exactly 100 ml.",
        "analogies": {
            "space": "Aerodynamic nose cone fairing volume on satellite launch vehicles (e.g., Falcon 9 fairing).",
            "coding": "Bounding frustum volume calculations in 3D occlusion culling algorithms.",
            "animals": "An antlion larva digging a conical sand pit trap to capture falling prey."
        },
        "prompt": "A right circular cone has a base radius of 6 cm and a vertical height of 8 cm. What is its slant height (l)?",
        "options": ["10 cm", "14 cm", "12 cm", "7 cm"],
        "answer": "10 cm",
        "exp": "Slant height l = sqrt(r^2 + h^2) = sqrt(6^2 + 8^2) = sqrt(36 + 64) = sqrt(100) = 10 cm.",
        "hints": ["Slant height forms the hypotenuse of a right triangle with radius and height.", "l^2 = r^2 + h^2.", "6^2 + 8^2 = 36 + 64 = 100; sqrt(100) = 10 cm."],
        "scaffolds": ["Step 1: Formula for slant height: l = sqrt(r^2 + h^2).", "Step 2: l = sqrt(6^2 + 8^2) = sqrt(36 + 64) = sqrt(100).", "Step 3: l = 10 cm."]
    },
    (9, "Mathematics", 7): {
        "concept_name": "Statistics & Probability (Frequency Polygons & Empirical Probability)",
        "diff": 3,
        "objectives": ["Construct histograms and frequency polygons for continuous grouped data", "Calculate empirical probability: P(E) = Number of favorable trials / Total trials"],
        "prereq": ["Mean, median, and bar graphs"],
        "std_exp": "Empirical probability P(E) of an event is the ratio of the number of trials in which event E occurred to the total number of trials conducted: P(E) = m / n. 0 <= P(E) <= 1.",
        "simp_exp": "A coin is tossed 200 times. If heads turns up 105 times, the empirical probability of getting heads is 105 / 200 = 21 / 40 = 0.525!",
        "analogies": {
            "space": "Monte Carlo orbital debris collision risk probability simulations.",
            "coding": "A/B test click-through probability calculations in production web analytics.",
            "animals": "A predator calculating hunting strike success probability based on historical chase trials."
        },
        "prompt": "A coin is tossed 500 times with observed frequencies: Head: 240 times, Tail: 260 times. What is the empirical probability of getting a Head?",
        "options": ["0.48", "0.52", "0.24", "0.50"],
        "answer": "0.48",
        "exp": "Empirical probability P(Head) = Favorable trials / Total trials = 240 / 500 = 48 / 100 = 0.48.",
        "hints": ["Number of heads = 240, Total tosses = 500.", "Divide 240 by 500.", "240 / 500 = 0.48."],
        "scaffolds": ["Step 1: Formula: P(E) = n(E) / N.", "Step 2: P(Head) = 240 / 500.", "Step 3: 240 / 500 = 0.48."]
    },

    # --- Science (6 Chapters) ---
    (9, "Science", 1): {
        "concept_name": "Matter in Our Surroundings (States of Matter & Latent Heat)",
        "diff": 3,
        "objectives": ["Explain states of matter based on kinetic energy and intermolecular attraction", "Define latent heat of fusion and latent heat of vaporisation"],
        "prereq": ["Physical properties of materials"],
        "std_exp": "Matter exists in solid, liquid, and gas states governed by particle kinetic energy and intermolecular forces. During phase change, temperature remains constant as energy supplied is consumed as latent heat to overcome intermolecular bonds.",
        "simp_exp": "When boiling water at 100°C on a stove, the thermometer stays at exactly 100°C! The continuous heat added is absorbed as latent heat of vaporisation to convert liquid water into steam.",
        "analogies": {
            "space": "Cryogenic liquid hydrogen boil-off management inside Saturn V fuel tanks.",
            "coding": "Buffer allocation hysteresis: absorbing memory allocations without shifting system throughput state.",
            "animals": "Sweating or panting animals utilizing latent heat of evaporation to cool down."
        },
        "prompt": "Why does the temperature of water remain CONSTANT at 100°C while it is vigorously boiling into steam?",
        "options": [
            "Supplied heat energy is consumed as latent heat of vaporisation to overcome intermolecular forces of attraction between water molecules",
            "The thermometer loses sensitivity at 100°C",
            "Heat escapes into the surrounding air so fast that water stops absorbing energy",
            "Water molecules stop moving at 100°C"
        ],
        "answer": "Supplied heat energy is consumed as latent heat of vaporisation to overcome intermolecular forces of attraction between water molecules",
        "exp": "During boiling, heat energy supplied does not increase kinetic energy (temperature), but is absorbed as latent heat of vaporisation to break intermolecular bonds between liquid molecules.",
        "hints": ["Does the heat increase molecular speed or break molecular bonds?", "It is used to break bonds between liquid molecules.", "This hidden energy is called latent heat of vaporisation."],
        "scaffolds": ["Step 1: Boiling is a phase change from liquid to gas.", "Step 2: Temperature measures average kinetic energy.", "Step 3: Heat supplied breaks intermolecular bonds without raising temperature (latent heat)."]
    },
    (9, "Science", 2): {
        "concept_name": "Atoms and Molecules (Chemical Formulae & Law of Conservation of Mass)",
        "diff": 3,
        "objectives": ["Apply the Law of Conservation of Mass and Law of Constant Proportions", "Write chemical formulas of ionic compounds using valency (cross-over method)"],
        "prereq": ["Elements, compounds, and mixtures"],
        "std_exp": "Lavoisier's Law of Conservation of Mass states matter is neither created nor destroyed in a chemical reaction. Chemical formulas are derived by criss-crossing ionic valencies: Aluminium (Al^3+) and Sulphate (SO4^2-) yield Al2(SO4)3.",
        "simp_exp": "To write the formula for Aluminium Oxide: Al has charge +3, O has charge -2. Cross the numbers: Al gets 2 and O gets 3, giving Al2O3!",
        "analogies": {
            "space": "Stoichiometric propellant mass balancing: oxygen and hydrogen reacting to produce water mass without any lost atoms.",
            "coding": "Type-safe interface contracts: balancing method arguments and return types with zero dropped bytes.",
            "animals": "Biochemical mass balance inside cellular metabolic pathways."
        },
        "prompt": "Using the valencies of Aluminium (Al^3+) and Oxide (O^2-), what is the correct chemical formula for aluminium oxide?",
        "options": ["Al2O3", "Al3O2", "AlO", "AlO2"],
        "answer": "Al2O3",
        "exp": "By criss-crossing ionic valencies (Al has valency 3, O has valency 2), the subscript for Al becomes 2 and for O becomes 3, yielding Al2O3.",
        "hints": ["Criss-cross the charges of Al (3+) and O (2-).", "Al takes the 2, and O takes the 3.", "Formula is Al2O3."],
        "scaffolds": ["Step 1: Write symbols and valencies: Al (3), O (2).", "Step 2: Criss-cross valencies: Al_2 and O_3.", "Step 3: Chemical formula is Al2O3."]
    },
    (9, "Science", 3): {
        "concept_name": "The Fundamental Unit of Life (Cell Biology & Organelles)",
        "diff": 3,
        "objectives": ["Compare prokaryotic and eukaryotic cell anatomy", "Identify functions of nucleus, mitochondria (ATP), and plasma membrane osmosis"],
        "prereq": ["Living organisms and tissues"],
        "std_exp": "The cell is the structural and functional unit of life. Mitochondria synthesize ATP via cellular respiration and are termed the 'powerhouse of the cell'. The selectively permeable plasma membrane regulates osmosis and diffusion.",
        "simp_exp": "Mitochondria are the tiny batteries inside your cells: they burn food nutrients to produce ATP energy packs that your body uses to run, jump, and think!",
        "analogies": {
            "space": "Nuclear RTG power generators supplying continuous electrical wattage to deep space probes.",
            "coding": "Microservice container host providing CPU and memory execution cycles for application containers.",
            "animals": "Muscle cells of hummingbirds packed with dense mitochondria to sustain 80 wing-beats per second."
        },
        "prompt": "Which cellular organelle is known as the 'Powerhouse of the Cell' because it synthesizes cellular energy in the form of ATP molecules?",
        "options": ["Mitochondria", "Ribosome", "Golgi apparatus", "Lysosome"],
        "answer": "Mitochondria",
        "exp": "Mitochondria are sites of aerobic cellular respiration, synthesizing energy in the form of Adenosine Triphosphate (ATP), earning them the title 'Powerhouse of the Cell'.",
        "hints": ["Which organelle produces ATP energy?", "Ribosomes make proteins; lysosomes digest waste.", "Mitochondria generate cellular energy."],
        "scaffolds": ["Step 1: Identify ATP production site.", "Step 2: Cellular respiration occurs in mitochondria.", "Step 3: Mitochondria are called the powerhouse of the cell."]
    },
    (9, "Science", 4): {
        "concept_name": "Motion (Kinematics & Equations of Motion)",
        "diff": 3,
        "objectives": ["Differentiate distance vs displacement and speed vs velocity", "Apply equations of motion: v = u + at, s = ut + (1/2)at^2, v^2 = u^2 + 2as"],
        "prereq": ["Speed and time calculations"],
        "std_exp": "Displacement is the shortest straight-line vector from initial to final position. For uniformly accelerated motion: (1) v = u + at, (2) s = ut + 0.5*a*t^2, (3) v^2 = u^2 + 2as, where u is initial velocity, v is final velocity, a is acceleration, and t is time.",
        "simp_exp": "A car starts from rest (u = 0) and accelerates at 2 m/s^2 for 5 seconds. Its final speed is v = u + at = 0 + 2 * 5 = 10 m/s!",
        "analogies": {
            "space": "Orbital acceleration burn delta-v vector calculations for lunar injection trajectory.",
            "coding": "Kinematics Euler integration physics step: position += velocity * dt; velocity += accel * dt.",
            "animals": "A cheetah accelerating from 0 to 20 m/s in 3 seconds to catch an impala."
        },
        "prompt": "A train starts from rest (u = 0) and accelerates uniformly at 2 m/s^2 for 10 seconds. What distance does the train cover in this time?",
        "options": ["100 meters", "200 meters", "50 meters", "20 meters"],
        "answer": "100 meters",
        "exp": "Using second equation of motion: s = ut + (1/2)at^2. Since u = 0: s = 0 + (1/2) * 2 * (10^2) = 1 * 100 = 100 meters.",
        "hints": ["Use s = ut + (1/2)at^2.", "Initial velocity u = 0, so ut = 0.", "(1/2) * 2 * 100 = 100 meters."],
        "scaffolds": ["Step 1: Identify given: u = 0, a = 2 m/s^2, t = 10 s.", "Step 2: Substitute into s = ut + (1/2)at^2.", "Step 3: s = 0 + 0.5 * 2 * 100 = 100 m."]
    },
    (9, "Science", 5): {
        "concept_name": "Force and Laws of Motion (Newton's Laws & Momentum)",
        "diff": 3,
        "objectives": ["State Newton's 3 Laws of Motion", "Apply momentum p = mv and force formula F = m * a"],
        "prereq": ["Force and kinematics"],
        "std_exp": "Newton's First Law defines inertia. Second Law states rate of change of momentum is proportional to applied force: F = ma. Third Law states every action has an equal and opposite reaction (F_AB = -F_BA).",
        "simp_exp": "A cricket fielder pulls their hands backwards while catching a fast cricket ball to increase the time of catch, reducing force on their palms so it doesn't hurt!",
        "analogies": {
            "space": "Rocket propulsion: exhaust gas expelled downwards exerts an equal and opposite upward thrust force.",
            "coding": "Impulse response functions in physics engines computing rigid-body collision impulses.",
            "animals": "A frog jumping forward by pushing the ground backward with its powerful hind legs."
        },
        "prompt": "Why does a cricket fielder pull their hands backward while catching a fast-moving cricket ball?",
        "options": [
            "To increase the impact time, thereby reducing the rate of change of momentum and minimizing force on the hands",
            "To decrease the time taken to catch the ball so it stops instantly",
            "To increase the momentum of the ball before stopping it",
            "To allow air resistance to blow the ball away"
        ],
        "answer": "To increase the impact time, thereby reducing the rate of change of momentum and minimizing force on the hands",
        "exp": "By Newton's Second Law, Force = Delta p / Delta t. Pulling hands backward increases impact time (Delta t), which significantly reduces the force experienced by the fielder's hands, preventing injury.",
        "hints": ["Recall F = Delta p / Delta t.", "If time Delta t increases, what happens to Force F?", "Force decreases, preventing painful impact on hands."],
        "scaffolds": ["Step 1: Catching reduces ball momentum to zero.", "Step 2: Force = Rate of change of momentum (Delta p / Delta t).", "Step 3: Increasing time Delta t decreases force F on hands."]
    },
    (9, "Science", 6): {
        "concept_name": "Gravitation (Universal Law of Gravitation & Archimedes)",
        "diff": 3,
        "objectives": ["Apply Newton's Universal Law of Gravitation: F = G * (M * m) / r^2", "Explain Archimedes' principle and buoyant force in fluids"],
        "prereq": ["Force and acceleration"],
        "std_exp": "Every object attracts every other object with a gravitational force F = G * (m1 * m2) / d^2. Near Earth's surface, g = 9.8 m/s^2. Archimedes' principle states an object immersed in fluid experiences an upward buoyant force equal to the weight of fluid displaced.",
        "simp_exp": "A massive steel ship floats on water because its hollow hull displaces a massive volume of water whose weight is equal to the ship's entire weight! A tiny solid iron needle sinks because it displaces very little water.",
        "analogies": {
            "space": "Planetary orbit mechanics: gravitational attraction providing necessary centripetal force for Keplerian orbits.",
            "coding": "N-body gravitational simulations calculating mutual gravitational force tensors.",
            "animals": "Fish using swim bladders to adjust body density and buoyant force for effortless neutral buoyancy."
        },
        "prompt": "According to Archimedes' Principle, what is the magnitude of the upward buoyant force acting on an object submerged in water?",
        "options": [
            "Equal to the weight of the fluid displaced by the submerged object",
            "Equal to the total volume of water in the container",
            "Equal to the atmospheric pressure acting on the water surface",
            "Greater than the gravitational mass of Earth"
        ],
        "answer": "Equal to the weight of the fluid displaced by the submerged object",
        "exp": "Archimedes' principle states that when a body is immersed fully or partially in a fluid, it experiences an upward buoyant force equal to the weight of the fluid displaced by the body.",
        "hints": ["What does the displaced fluid weigh?", "The upward push matches that weight.", "Buoyant force = weight of displaced fluid."],
        "scaffolds": ["Step 1: Archimedes discovered flotation principles.", "Step 2: Submerging an object pushes water aside.", "Step 3: Upward buoyant force = weight of displaced water."]
    },

    # --- English (4 Chapters) ---
    (9, "English", 1): {
        "concept_name": "The Fun They Had by Isaac Asimov (Futuristic Education)",
        "diff": 3,
        "objectives": ["Analyze science fiction narrative speculating about automated education", "Contrast robotic mechanical teachers with human social classroom learning"],
        "prereq": ["Reading comprehension"],
        "std_exp": "Asimov's speculative sci-fi story set in 2157 depicts 11-year-old Margie who learns from an isolated mechanical tele-teacher at home. When she reads an old printed book about 20th-century schools where human teachers taught children together, she yearns for 'the fun they had'.",
        "simp_exp": "In 2157, Margie studied all alone with a television robot teacher. She wished she lived in the past when kids walked to school together, laughed in real classrooms, and had human teachers!",
        "analogies": {
            "space": "Long-duration solo deep space astronaut training via pre-recorded AI synthetic instructors.",
            "coding": "Fully automated personalized LMS bot vs collaborative peer programming study groups.",
            "animals": "A lone pup raised by an automated feeder vs playing in a social wolf pack."
        },
        "prompt": "In Isaac Asimov's story 'The Fun They Had', why did Margie hate her mechanical teacher?",
        "options": [
            "It gave her continuous geography tests that were too difficult, requiring monotonous solitary screen learning",
            "It kept breaking down and emitting electrical sparks",
            "It forced her to do physical exercises outside in the cold",
            "It refused to answer any of Margie's questions"
        ],
        "answer": "It gave her continuous geography tests that were too difficult, requiring monotonous solitary screen learning",
        "exp": "The mechanical teacher was programmed at an advanced speed, giving Margie test after test in geography which she struggled with, turning learning into a lonely, joyless chore.",
        "hints": ["What subject was giving Margie trouble?", "The mechanical teacher's geography sector was geared too high.", "It gave repeated frustrating tests on screen."],
        "scaffolds": ["Step 1: Margie despised her mechanical teacher.", "Step 2: The geography sector was geared too fast for an 11-year-old.", "Step 3: She received test after test alone without human peer connection."]
    },
    (9, "English", 2): {
        "concept_name": "The Sound of Music: Evelyn Glennie (Overcoming Sensory Challenges)",
        "diff": 3,
        "objectives": ["Analyze biographical account of profound deafness and neurodiversity", "Examine somatic sensory perception of music through bodily vibration"],
        "prereq": ["Biographical reading"],
        "std_exp": "Profoundly deaf Scottish percussionist Dame Evelyn Glennie learned to perceive musical acoustic frequencies not through ears, but somatically through bone conduction and bodily vibration (higher pitches through waist up, lower pitches waist down).",
        "simp_exp": "Evelyn became deaf as a young girl, but she took off her shoes to feel the low rumble and high tingle of drums through her bare feet and skin, becoming a world-famous percussionist!",
        "analogies": {
            "space": "Seismometers on Mars detecting deep planetary seismic rumblings without atmospheric audio waves.",
            "coding": "Haptic feedback sensors translating audio telemetry into tactile vibrational waveforms.",
            "animals": "Snakes sensing ground vibrations through jawbones in the absence of external ears."
        },
        "prompt": "How does deaf virtuoso percussionist Evelyn Glennie perceive musical pitch and rhythm without using auditory ear hearing?",
        "options": [
            "She senses acoustic vibrations somatically through different parts of her body and bare feet",
            "She reads the lip movements of orchestra conductors",
            "She wears high-power electronic hearing aids at every concert",
            "She memorizes sheet music numbers without sensing vibrations"
        ],
        "answer": "She senses acoustic vibrations somatically through different parts of her body and bare feet",
        "exp": "Glennie famously removes her shoes on wooden concert stages to feel vibrations pass up through her bare feet, sensing higher notes above her waist and lower notes below her waist.",
        "hints": ["How did percussionist Ron Forbes teach her to listen?", "He told her not to listen through ears, but sense it another way.", "She feels vibrations through her body and feet."],
        "scaffolds": ["Step 1: Evelyn lost her hearing by age 12.", "Step 2: Master percussionist Forbes tuned two drums to different notes.", "Step 3: She learned to feel sound vibrations somatically through her body."]
    },
    (9, "English", 3): {
        "concept_name": "A Truly Beautiful Mind: Albert Einstein (Neurodivergence & Pacifism)",
        "diff": 3,
        "objectives": ["Examine biographical details of Albert Einstein's neurodivergent childhood traits", "Trace his humanitarian pacifism and opposition to nuclear warfare"],
        "prereq": ["Historical biographies"],
        "std_exp": "The chapter charts Einstein's trajectory: late speech development (neurodivergent childhood), visual spatial thinking, rejection of rote authoritarian schooling in Munich, revolutionary 1905 Annus Mirabilis physics papers, and outspoken global pacifism.",
        "simp_exp": "As a boy, Einstein didn't speak until age three and hated rote memorization in school. Yet his unique visual imagination led him to discover the Theory of Relativity and advocate for world peace!",
        "analogies": {
            "space": "General Relativity predicting gravitational lens curvature of starlight around massive stellar bodies.",
            "coding": "Out-of-the-box non-linear algorithmic thinking solving problems that traditional iterative code fails on.",
            "animals": "An owl seeing invisible infrared thermal patterns that daylight hunters miss entirely."
        },
        "prompt": "Why did Albert Einstein clash with teachers and leave his high school in Munich, Germany at age 15?",
        "options": [
            "He felt suffocated by strict rote discipline and authoritarian regimentation that stifled independent curiosity",
            "He repeatedly failed all mathematics and physics examinations",
            "He was expelled for refusing to participate in school sports",
            "His family wanted him to become a military officer immediately"
        ],
        "answer": "He felt suffocated by strict rote discipline and authoritarian regimentation that stifled independent curiosity",
        "exp": "Einstein despised the rigid, mindless military regimentation of German schools where rote memorization was prized over questioning and free inquiry, leading him to leave Munich.",
        "hints": ["Did Einstein like rote memorization?", "He hated strict authoritarian rules that blocked free thought.", "He felt suffocated by school regimentation."],
        "scaffolds": ["Step 1: Einstein valued questioning and conceptual visualization.", "Step 2: Munich gymnasium emphasized rigid military discipline.", "Step 3: He felt stifled and left to study in Switzerland."]
    },
    (9, "English", 4): {
        "concept_name": "My Childhood by A.P.J. Abdul Kalam (Secular Harmony & Humility)",
        "diff": 3,
        "objectives": ["Analyze Kalam's autobiographical reflection from Wings of Fire", "Appreciate communal harmony, paternal values, and resilience"],
        "prereq": ["Reading comprehension"],
        "std_exp": "In this chapter from 'Wings of Fire', Dr. A.P.J. Abdul Kalam reflects on his upbringing in the pilgrimage town of Rameswaram, depicting deep communal harmony between Hindu and Muslim families, his father Jainulabdeen's spiritual wisdom, and overcoming religious bigotry in school.",
        "simp_exp": "Growing up in Rameswaram, Abdul Kalam and his close Brahmin friends Ramanadha, Aravindan, and Sivaprakasan studied together without any religious divide, supported by wise elders who nurtured brotherhood.",
        "analogies": {
            "space": "India's space programme (ISRO) uniting scientists of diverse backgrounds to launch SLV-3 rockets.",
            "coding": "Open-source collaboration uniting global contributors across diverse platforms into unified software.",
            "animals": "Mixed-species bird feeding flocks cooperating harmoniously to find food in forest canopies."
        },
        "prompt": "In 'My Childhood', how did head priest Lakshmana Sastry handle the new school teacher who forced Kalam to move away from his Brahmin friend Ramanadha?",
        "options": [
            "He sternly told the teacher not to poison innocent children's minds with social inequality and demanded an immediate apology",
            "He transferred his son Ramanadha to another private school",
            "He complained to the British colonial commissioner in Madras",
            "He advised Abdul Kalam to sit quietly at the back of the classroom"
        ],
        "answer": "He sternly told the teacher not to poison innocent children's minds with social inequality and demanded an immediate apology",
        "exp": "Lakshmana Sastry summoned the new teacher and made it clear that religious communal prejudice would not be tolerated in their community, reforming the young teacher.",
        "hints": ["Did the head priest support or condemn religious segregation?", "He strongly condemned prejudice.", "He ordered the teacher to apologize or quit the school."],
        "scaffolds": ["Step 1: The new teacher separated Kalam and Ramanadha based on religion.", "Step 2: Lakshmana Sastry summoned the teacher.", "Step 3: He commanded the teacher never to spread communal intolerance among children."]
    },

    # =========================================================================
    # CLASS 10 (18 Chapters: 8 Math, 6 Science, 4 English)
    # =========================================================================
    # --- Mathematics (8 Chapters) ---
    (10, "Mathematics", 1): {
        "concept_name": "Real Numbers (Fundamental Theorem of Arithmetic & HCF/LCM)",
        "diff": 4,
        "objectives": ["Apply the Fundamental Theorem of Arithmetic for unique prime factorisation", "Prove irrationality of sqrt(2) and sqrt(3) using contradiction"],
        "prereq": ["Prime numbers and divisibility"],
        "std_exp": "The Fundamental Theorem of Arithmetic states every composite number can be uniquely expressed as a product of primes, apart from the order of factors. For any two positive integers a and b: HCF(a, b) * LCM(a, b) = a * b.",
        "simp_exp": "If two numbers have HCF = 6 and LCM = 36, their product is 6 * 36 = 216! If one number is 12, the other must be 216 / 12 = 18.",
        "analogies": {
            "space": "Decomposing complex orbital ephemeris frequencies into prime harmonic sinusoids.",
            "coding": "Cryptographic RSA encryption factoring massive semiprime integers into two unique prime keys.",
            "animals": "Deoxyribonucleic acid (DNA) base pairs uniquely encoding complex organic genomes."
        },
        "prompt": "If HCF(306, 657) = 9, what is the LCM(306, 657)?",
        "options": ["22,338", "21,114", "24,552", "18,920"],
        "answer": "22,338",
        "exp": "Using formula HCF * LCM = Product of numbers: 9 * LCM = 306 * 657 => LCM = (306 * 657) / 9 = 34 * 657 = 22,338.",
        "hints": ["Use: HCF * LCM = a * b.", "LCM = (306 * 657) / 9.", "306 / 9 = 34; 34 * 657 = 22,338."],
        "scaffolds": ["Step 1: Formula: LCM(a, b) = (a * b) / HCF(a, b).", "Step 2: LCM = (306 * 657) / 9.", "Step 3: 34 * 657 = 22,338."]
    },
    (10, "Mathematics", 2): {
        "concept_name": "Polynomials & Quadratic Equations (Discriminant & Roots)",
        "diff": 4,
        "objectives": ["Relate zeroes and coefficients: alpha + beta = -b/a, alpha * beta = c/a", "Determine root nature using discriminant D = b^2 - 4ac"],
        "prereq": ["Factorisation of quadratics"],
        "std_exp": "For quadratic equation ax^2 + bx + c = 0, roots are x = (-b +- sqrt(D)) / (2a) where D = b^2 - 4ac. If D > 0: two distinct real roots; if D = 0: two equal real roots; if D < 0: no real roots.",
        "simp_exp": "Look at x^2 - 6x + 9 = 0: D = (-6)^2 - 4(1)(9) = 36 - 36 = 0. Because D is 0, the equation has two identical real roots: x = 3!",
        "analogies": {
            "space": "Parabolic escape velocity threshold: D > 0 hyperbolic escape, D = 0 parabolic trajectory, D < 0 closed elliptic orbit.",
            "coding": "Evaluating discriminant thresholds in 3D ray-sphere intersection testing for raytracers.",
            "animals": "A leaping dolphin's ballistic parabolic trajectory arc across water."
        },
        "prompt": "What is the nature of the roots of the quadratic equation 2x^2 - 4x + 3 = 0?",
        "options": [
            "No real roots (discriminant D < 0)",
            "Two distinct real roots (discriminant D > 0)",
            "Two equal real roots (discriminant D = 0)",
            "Infinitely many real roots"
        ],
        "answer": "No real roots (discriminant D < 0)",
        "exp": "Discriminant D = b^2 - 4ac = (-4)^2 - 4(2)(3) = 16 - 24 = -8. Since D < 0, the equation possesses no real roots.",
        "hints": ["Calculate D = b^2 - 4ac.", "a = 2, b = -4, c = 3.", "D = 16 - 24 = -8. Since -8 < 0, there are no real roots."],
        "scaffolds": ["Step 1: Identify a = 2, b = -4, c = 3.", "Step 2: D = (-4)^2 - 4(2)(3) = 16 - 24 = -8.", "Step 3: D < 0 implies no real roots."]
    },
    (10, "Mathematics", 3): {
        "concept_name": "Pair of Linear Equations in Two Variables (Consistency & Methods)",
        "diff": 4,
        "objectives": ["Identify consistency conditions: intersecting (unique), parallel (no solution), coincident (infinitely many)", "Solve simultaneous linear systems using elimination and substitution"],
        "prereq": ["Linear equations in two variables"],
        "std_exp": "For a1*x + b1*y + c1 = 0 and a2*x + b2*y + c2 = 0: (1) If a1/a2 != b1/b2: unique solution (intersecting lines); (2) If a1/a2 = b1/b2 != c1/c2: no solution (parallel lines); (3) If a1/a2 = b1/b2 = c1/c2: infinitely many solutions (coincident lines).",
        "simp_exp": "If two railway tracks are parallel, they never cross! Parallel lines have matching slopes (a1/a2 = b1/b2) but different intercepts, meaning they have ZERO solutions.",
        "analogies": {
            "space": "Orbital plane intersection line nodes where two spacecraft orbits can execute rendezvous maneuvers.",
            "coding": "Matrix rank evaluation solving systems of linear equations Ax = b.",
            "animals": "Two parallel hunting trails walked by rival predator packs that never intersect."
        },
        "prompt": "Under what condition does a pair of linear equations a1*x + b1*y + c1 = 0 and a2*x + b2*y + c2 = 0 represent PARALLEL lines with NO solution?",
        "options": [
            "a1/a2 = b1/b2 != c1/c2",
            "a1/a2 != b1/b2",
            "a1/a2 = b1/b2 = c1/c2",
            "a1*a2 + b1*b2 = 0"
        ],
        "answer": "a1/a2 = b1/b2 != c1/c2",
        "exp": "When ratio of x-coefficients equals ratio of y-coefficients but differs from ratio of constant terms (a1/a2 = b1/b2 != c1/c2), the lines are parallel and possess no common solution point.",
        "hints": ["Parallel lines have equal slopes but different intercepts.", "Equal slopes means a1/a2 = b1/b2.", "Different intercepts means != c1/c2."],
        "scaffolds": ["Step 1: Intersecting (unique) = a1/a2 != b1/b2.", "Step 2: Coincident (infinite) = a1/a2 = b1/b2 = c1/c2.", "Step 3: Parallel (no solution) = a1/a2 = b1/b2 != c1/c2."]
    },
    (10, "Mathematics", 4): {
        "concept_name": "Arithmetic Progressions (AP nth Term & Sum Formulae)",
        "diff": 4,
        "objectives": ["Compute nth term: a_n = a + (n - 1)d", "Compute sum of first n terms: S_n = (n/2) * [2a + (n - 1)d]"],
        "prereq": ["Sequences and series basics"],
        "std_exp": "An AP has constant common difference d = a_(k+1) - a_k. The nth term is given by a_n = a + (n - 1)d. The sum of n terms is S_n = (n/2) * (a + l) = (n/2) * [2a + (n - 1)d].",
        "simp_exp": "In the sequence 2, 7, 12, 17... the first term a = 2 and common jump d = 5. To find the 10th term: a_10 = 2 + (10 - 1) * 5 = 2 + 45 = 47!",
        "analogies": {
            "space": "Multi-stage solid rocket booster burns delivering uniform incremental delta-v velocity stages.",
            "coding": "Array striding in memory with fixed byte offset: address = base_address + index * stride.",
            "animals": "Rings on a growing tortoise carapace expanding by equal radial increments each year."
        },
        "prompt": "Find the 12th term of the Arithmetic Progression (AP): 3, 8, 13, 18, ...",
        "options": ["58", "63", "53", "68"],
        "answer": "58",
        "exp": "Here first term a = 3, common difference d = 8 - 3 = 5. Using a_n = a + (n - 1)d: a_12 = 3 + (12 - 1)*5 = 3 + 11*5 = 3 + 55 = 58.",
        "hints": ["First term a = 3, common difference d = 5.", "Formula: a_n = a + (n - 1)d.", "a_12 = 3 + 11*5 = 3 + 55 = 58."],
        "scaffolds": ["Step 1: a = 3, d = 5, n = 12.", "Step 2: a_12 = 3 + (12 - 1) * 5.", "Step 3: 3 + 55 = 58."]
    },
    (10, "Mathematics", 5): {
        "concept_name": "Triangles & Coordinate Geometry (Thales Theorem & Distance)",
        "diff": 4,
        "objectives": ["Apply Basic Proportionality Theorem (Thales' Theorem)", "Calculate distance between two points: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)"],
        "prereq": ["Triangle congruence and Cartesian coordinates"],
        "std_exp": "Thales' Theorem states if a line is drawn parallel to one side of a triangle intersecting the other two sides, it divides those sides in the same ratio: AD/DB = AE/EC. Distance between points is d = sqrt((x2 - x1)^2 + (y2 - y1)^2).",
        "simp_exp": "To find distance between (1, 2) and (4, 6): change in x is (4 - 1) = 3; change in y is (6 - 2) = 4. Distance = sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5 units!",
        "analogies": {
            "space": "Laser rangefinder ranging distance between an orbital docking pod and ISS docking ring.",
            "coding": "Spatial indexing distance queries in geospatial databases (PostGIS / KD-Tree).",
            "animals": "Geese maintaining fixed proportional spacing in a V-flight formation."
        },
        "prompt": "Find the distance between the two coordinate points A(2, 3) and B(6, 6) in the Cartesian plane.",
        "options": ["5 units", "7 units", "25 units", "sqrt(7) units"],
        "answer": "5 units",
        "exp": "Distance d = sqrt((x2 - x1)^2 + (y2 - y1)^2) = sqrt((6 - 2)^2 + (6 - 3)^2) = sqrt(4^2 + 3^2) = sqrt(16 + 9) = sqrt(25) = 5 units.",
        "hints": ["Use the distance formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2).", "(6 - 2) = 4 and (6 - 3) = 3.", "sqrt(16 + 9) = sqrt(25) = 5."],
        "scaffolds": ["Step 1: dx = 6 - 2 = 4; dy = 6 - 3 = 3.", "Step 2: d^2 = 4^2 + 3^2 = 16 + 9 = 25.", "Step 3: d = sqrt(25) = 5 units."]
    },
    (10, "Mathematics", 6): {
        "concept_name": "Introduction to Trigonometry (Ratios & Standard Identities)",
        "diff": 4,
        "objectives": ["Define trigonometric ratios: sin, cos, tan, cosec, sec, cot", "Apply standard trigonometric identity: sin^2(theta) + cos^2(theta) = 1"],
        "prereq": ["Right-angled triangles and Pythagoras theorem"],
        "std_exp": "For angle theta in a right triangle: sin(theta) = Opposite/Hypotenuse, cos(theta) = Adjacent/Hypotenuse, tan(theta) = sin/cos = Opposite/Adjacent. Fundamental identity: sin^2(theta) + cos^2(theta) = 1, 1 + tan^2(theta) = sec^2(theta).",
        "simp_exp": "For 30 degrees: sin(30°) = 1/2 and cos(30°) = sqrt(3)/2. Notice: (1/2)^2 + (sqrt(3)/2)^2 = 1/4 + 3/4 = 4/4 = 1! The identity always equals 1!",
        "analogies": {
            "space": "Attitude quaternion calculations resolving spacecraft roll, pitch, and yaw angles.",
            "coding": "Computing unit vector direction components using Math.cos() and Math.sin() in 3D physics engines.",
            "animals": "An archer fish calculating the refraction water angle to shoot a water droplet at an insect."
        },
        "prompt": "If sin(theta) = 3/5 for an acute angle theta, what is the value of cos(theta)?",
        "options": ["4/5", "3/4", "5/4", "1/5"],
        "answer": "4/5",
        "exp": "Using identity sin^2(theta) + cos^2(theta) = 1: cos(theta) = sqrt(1 - sin^2(theta)) = sqrt(1 - (3/5)^2) = sqrt(1 - 9/25) = sqrt(16/25) = 4/5.",
        "hints": ["Use the Pythagorean trigonometric identity: cos^2(theta) = 1 - sin^2(theta).", "1 - (3/5)^2 = 1 - 9/25 = 16/25.", "sqrt(16/25) = 4/5."],
        "scaffolds": ["Step 1: Formula: cos(theta) = sqrt(1 - sin^2(theta)).", "Step 2: 1 - (9/25) = 16/25.", "Step 3: sqrt(16/25) = 4/5."]
    },
    (10, "Mathematics", 7): {
        "concept_name": "Applications of Trigonometry (Heights and Distances)",
        "diff": 4,
        "objectives": ["Distinguish angle of elevation from angle of depression", "Calculate heights of towers and widths of rivers using tan(theta)"],
        "prereq": ["Trigonometric ratios (tan 30°, tan 45°, tan 60°)"],
        "std_exp": "The angle of elevation is formed by the line of sight with the horizontal when looking up. To find height h of a tower at distance d: tan(theta) = h / d => h = d * tan(theta). tan(45°) = 1, tan(30°) = 1/sqrt(3), tan(60°) = sqrt(3).",
        "simp_exp": "Stand 30 meters away from a tower. If the angle looking up at the top is 45°, because tan(45°) = 1, the tower height is exactly equal to your distance: 30 meters!",
        "analogies": {
            "space": "Triangulating lunar mountain peak altitudes from shadow cast angles measured by lunar orbiters.",
            "coding": "Camera field-of-view perspective projection mapping in 3D rendering engines.",
            "animals": "A falcon perching on a crag gauging dive height from the ground sighting angle."
        },
        "prompt": "A person stands 30 meters away from the base of a vertical mobile tower. If the angle of elevation of the top of the tower is 45°, what is the height of the tower?",
        "options": ["30 meters", "15 meters", "30*sqrt(3) meters", "60 meters"],
        "answer": "30 meters",
        "exp": "In right triangle: tan(45°) = Height / Distance => 1 = Height / 30 => Height = 30 meters.",
        "hints": ["tan(theta) = Opposite / Adjacent = Height / 30.", "What is the value of tan(45°)? It is 1.", "Height = 30 * 1 = 30 meters."],
        "scaffolds": ["Step 1: Set up trigonometric ratio: tan(45°) = h / 30.", "Step 2: Recall tan(45°) = 1.", "Step 3: h = 30 * 1 = 30 meters."]
    },
    (10, "Mathematics", 8): {
        "concept_name": "Statistics and Probability (Grouped Mean & Classical Probability)",
        "diff": 4,
        "objectives": ["Compute mean of grouped continuous frequency distribution using direct method", "Apply classical probability: P(E) = n(E) / n(S)"],
        "prereq": ["Grouped frequency tables"],
        "std_exp": "Direct method for grouped mean: Mean x_bar = Sum(fi * xi) / Sum(fi), where xi is class mark (Upper limit + Lower limit)/2. In a fair deck of 52 cards, P(Ace) = 4 / 52 = 1 / 13.",
        "simp_exp": "From a well-shuffled standard pack of 52 playing cards, there are 4 Aces. The probability of drawing an Ace is 4 / 52, which simplifies to 1 / 13!",
        "analogies": {
            "space": "Statistical reliability analysis of redundant flight thrusters during re-entry windows.",
            "coding": "Probability density function sampling in randomized Monte Carlo algorithms.",
            "animals": "Probabilistic foraging success model for migratory sea birds targeting fish schools."
        },
        "prompt": "One card is drawn at random from a well-shuffled standard deck of 52 playing cards. What is the probability of drawing a Queen?",
        "options": ["1/13", "1/52", "1/4", "4/13"],
        "answer": "1/13",
        "exp": "There are 4 Queens in a standard deck of 52 cards. Probability P(Queen) = Favorable outcomes / Total outcomes = 4 / 52 = 1 / 13.",
        "hints": ["How many Queens are in a standard 52-card deck?", "There are 4 Queens.", "Divide 4 by 52 to get 1/13."],
        "scaffolds": ["Step 1: Number of favorable outcomes n(E) = 4 Queens.", "Step 2: Total sample space n(S) = 52 cards.", "Step 3: P(E) = 4 / 52 = 1 / 13."]
    },

    # --- Science (6 Chapters) ---
    (10, "Science", 1): {
        "concept_name": "Chemical Reactions and Equations (Types of Reactions & Balancing)",
        "diff": 4,
        "objectives": ["Balance chemical equations following conservation of mass", "Differentiate reaction types: combination, decomposition, displacement, and redox"],
        "prereq": ["Chemical symbols and valency"],
        "std_exp": "A balanced chemical equation has equal atoms of each element on both sides. In redox reactions, oxidation involves gain of oxygen or loss of electrons, while reduction involves loss of oxygen or gain of electrons: CuO + H2 -> Cu + H2O.",
        "simp_exp": "When you put an iron nail into blue copper sulphate solution, iron kicks copper out because iron is more reactive: Fe + CuSO4 -> FeSO4 + Cu! The solution turns pale green and reddish copper coats the nail.",
        "analogies": {
            "space": "Hypergolic rocket engines where dinitrogen tetroxide and hydrazine react spontaneously upon contact.",
            "coding": "Atomic database transaction: state transformation must preserve total ledger balance without phantom loss.",
            "animals": "Cellular respiration enzymatic cascade oxidizing glucose to fuel metabolic life."
        },
        "prompt": "In the chemical reaction: CuO + H2 -> Cu + H2O, which substance is being REDUCED?",
        "options": [
            "Copper(II) oxide (CuO)",
            "Hydrogen gas (H2)",
            "Water (H2O)",
            "Pure copper (Cu)"
        ],
        "answer": "Copper(II) oxide (CuO)",
        "exp": "Reduction is the loss of oxygen. Copper(II) oxide (CuO) loses oxygen to become copper (Cu), meaning CuO is reduced. Hydrogen gains oxygen and is oxidized.",
        "hints": ["Reduction means loss of oxygen.", "Which reactant loses its oxygen atom during the reaction?", "CuO loses oxygen to form Cu, so CuO is reduced."],
        "scaffolds": ["Step 1: Identify reactants: CuO and H2.", "Step 2: CuO loses oxygen to become Cu.", "Step 3: Loss of oxygen is reduction; therefore, CuO is reduced."]
    },
    (10, "Science", 2): {
        "concept_name": "Acids, Bases and Salts (pH Scale & Common Salts)",
        "diff": 4,
        "objectives": ["Explain the pH scale (0 to 14) and universal indicator colors", "Identify chemical formulas and uses of baking soda, washing soda, and Plaster of Paris"],
        "prereq": ["Acids and bases"],
        "std_exp": "pH measures hydrogen ion concentration: pH = -log[H+]. pH < 7 is acidic, pH = 7 is neutral (pure water), pH > 7 is basic. Baking soda is Sodium hydrogen carbonate (NaHCO3), which releases CO2 on heating to make cakes soft and spongy.",
        "simp_exp": "Pure water has pH 7. Stomach acid has pH ~1.5 (very acidic!). Baking soda is NaHCO3: when heated, it produces carbon dioxide bubbles that puff up fluffy cakes!",
        "analogies": {
            "space": "Closed-loop hydroponic water pH sensors maintaining optimal root nutrient assimilation at pH 6.0.",
            "coding": "Normalizing continuous feature values onto a standard 0.0 to 14.0 scaling range.",
            "animals": "Human blood maintaining tightly buffered pH between 7.35 and 7.45 using bicarbonate buffer."
        },
        "prompt": "What is the chemical formula and name of the salt commonly used as Baking Soda to make cakes soft and fluffy?",
        "options": [
            "NaHCO3 (Sodium hydrogen carbonate)",
            "Na2CO3 . 10H2O (Sodium carbonate decahydrate)",
            "CaOCl2 (Bleaching powder)",
            "CaSO4 . (1/2)H2O (Plaster of Paris)"
        ],
        "answer": "NaHCO3 (Sodium hydrogen carbonate)",
        "exp": "Baking soda is Sodium hydrogen carbonate (NaHCO3). On heating during baking, it decomposes to release carbon dioxide gas, which causes cake batter to rise.",
        "hints": ["It contains sodium, hydrogen, carbon, and oxygen.", "Its chemical name is Sodium hydrogen carbonate.", "The formula is NaHCO3."],
        "scaffolds": ["Step 1: Baking soda release CO2 when heated.", "Step 2: Chemical name = Sodium hydrogen carbonate (bicarbonate).", "Step 3: Formula = NaHCO3."]
    },
    (10, "Science", 3): {
        "concept_name": "Life Processes (Biochemistry, Double Circulation & Nephrons)",
        "diff": 4,
        "objectives": ["Explain human double circulation: pulmonary and systemic circuits", "Describe the filtration mechanism of the functional kidney unit (nephron)"],
        "prereq": ["Human digestive and respiratory systems"],
        "std_exp": "In human double circulation, blood passes through the four-chambered heart twice per cycle (pulmonary circuit through lungs for oxygenation; systemic circuit through body). Nephrons filter metabolic urea in Bowman's capsule and reabsorb glucose, amino acids, and water.",
        "simp_exp": "Your heart has 4 rooms (two atria on top, two ventricles below) to ensure oxygen-rich blood never mixes with carbon dioxide blood, providing maximum energy for your active body!",
        "analogies": {
            "space": "Dual-loop regenerative thermal radiator pumps on the ISS circulating cooled and warmed ammonia.",
            "coding": "Two-phase commit transaction protocol ensuring decoupled read and write replication streams.",
            "animals": "Four-chambered hearts in birds and mammals maintaining high endothermic metabolic rates."
        },
        "prompt": "Why does the human heart have four distinct chambers separating oxygen-rich blood from deoxygenated blood?",
        "options": [
            "To prevent mixing of oxygenated and deoxygenated blood, ensuring highly efficient oxygen delivery to sustain warm-blooded metabolism",
            "To allow air to circulate directly into the brain",
            "To store extra blood when the body is asleep",
            "To decrease blood pressure so veins do not burst"
        ],
        "answer": "To prevent mixing of oxygenated and deoxygenated blood, ensuring highly efficient oxygen delivery to sustain warm-blooded metabolism",
        "exp": "Complete separation of the right side (deoxygenated) and left side (oxygenated) of the heart prevents mixing, ensuring a high supply of oxygen to maintain constant warm body temperature.",
        "hints": ["Are humans warm-blooded or cold-blooded?", "Warm-blooded mammals require huge amounts of oxygen.", "Separating blood chambers provides maximum oxygen efficiency."],
        "scaffolds": ["Step 1: Right chambers handle deoxygenated blood; left chambers handle oxygenated blood.", "Step 2: Separation prevents oxygen dilution.", "Step 3: This supports high metabolic energy requirements in warm-blooded humans."]
    },
    (10, "Science", 4): {
        "concept_name": "Control and Coordination (Neurobiology, Reflex Arc & Endocrine)",
        "diff": 4,
        "objectives": ["Trace electrical impulse transmission across a neuron and synapse", "Explain the involuntary reflex arc and endocrine hormonal regulation (insulin, thyroxine)"],
        "prereq": ["Nervous system basics"],
        "std_exp": "A reflex arc mediates involuntary automatic response to dangerous stimuli: Receptor -> Sensory neuron -> Spinal cord (interneuron) -> Motor neuron -> Effector muscle. At synapses, electrical impulses trigger neurotransmitter chemical diffusion.",
        "simp_exp": "When you accidentally touch a boiling pan, your hand jerks away instantly before your brain even feels the pain! The spinal cord handles this emergency reflex arc instantly.",
        "analogies": {
            "space": "Emergency automatic flight abort systems executing within milliseconds before ground control can react.",
            "coding": "Hardware interrupt requests (IRQ) bypassing CPU operating system scheduling to service critical faults immediately.",
            "animals": "A gazelle instantly reflex-springing sideways upon hearing the dry snap of a predator's paw."
        },
        "prompt": "What is the correct pathway followed by a nerve impulse in a spinal REFLEX ARC when touching a hot object?",
        "options": [
            "Receptor -> Sensory neuron -> Spinal cord -> Motor neuron -> Effector muscle",
            "Effector muscle -> Motor neuron -> Brain -> Sensory neuron -> Receptor",
            "Receptor -> Brain -> Spinal cord -> Sensory neuron -> Muscle",
            "Sensory neuron -> Receptor -> Motor neuron -> Spinal cord"
        ],
        "answer": "Receptor -> Sensory neuron -> Spinal cord -> Motor neuron -> Effector muscle",
        "exp": "The reflex arc starts at heat receptors in skin, travels via sensory neurons to the spinal cord, and immediately directs motor neurons to trigger effector muscle contraction without waiting for conscious brain processing.",
        "hints": ["Start at the skin receptor.", "Impulses travel in: sensory -> spinal cord -> motor.", "Ends at the effector muscle."],
        "scaffolds": ["Step 1: Stimulus detected by Receptor.", "Step 2: Sensory neuron carries signal to Spinal cord.", "Step 3: Motor neuron triggers Effector muscle contraction."]
    },
    (10, "Science", 5): {
        "concept_name": "Electricity & Magnetic Effects (Ohm's Law & Motor Principle)",
        "diff": 4,
        "objectives": ["Apply Ohm's Law: V = I * R and compute equivalent resistances in series and parallel", "State Fleming's Left-Hand Rule and the working principle of electric motors"],
        "prereq": ["Electric circuits and magnets"],
        "std_exp": "Ohm's Law states potential difference is directly proportional to current: V = IR. In series, R_eq = R1 + R2; in parallel, 1/R_eq = 1/R1 + 1/R2. Fleming's Left-Hand Rule dictates the Lorentz force direction on a current-carrying conductor in a magnetic field.",
        "simp_exp": "If two 6-ohm resistors are connected in parallel, the electricity has two paths to flow: 1/R = 1/6 + 1/6 = 2/6 = 1/3, so equivalent resistance is cut down to only 3 ohms!",
        "analogies": {
            "space": "Hall effect plasma thrusters using crossed electric and magnetic fields to accelerate xenon ions.",
            "coding": "Load balancer routing traffic through parallel worker instances to halve network latency resistance.",
            "animals": "Mormyrid electric fish detecting subtle conductivity changes in murky riverbeds."
        },
        "prompt": "Two resistors of resistances 6 ohms and 12 ohms are connected in PARALLEL across a 12V battery. What is the equivalent resistance of the circuit?",
        "options": ["4 ohms", "18 ohms", "8 ohms", "2 ohms"],
        "answer": "4 ohms",
        "exp": "For parallel resistors: 1 / R_eq = 1/6 + 1/12 = 2/12 + 1/12 = 3/12 = 1/4. Therefore, R_eq = 4 ohms.",
        "hints": ["Use parallel resistance formula: 1/R = 1/R1 + 1/R2.", "1/6 + 1/12 = 2/12 + 1/12 = 3/12.", "Flip 3/12 to get R = 12/3 = 4 ohms."],
        "scaffolds": ["Step 1: Formula: 1/R = 1/6 + 1/12.", "Step 2: Common denominator 12: 1/R = (2 + 1) / 12 = 3/12 = 1/4.", "Step 3: R = 4 ohms."]
    },
    (10, "Science", 6): {
        "concept_name": "Light: Reflection and Refraction (Optics & Lens Formula)",
        "diff": 4,
        "objectives": ["Apply Snell's Law of Refraction: n = sin(i) / sin(r)", "Apply Lens Formula: 1/f = 1/v - 1/u and calculate power of a lens P = 1/f (in dioptres)"],
        "prereq": ["Light rays and reflections"],
        "std_exp": "Snell's Law states n1 * sin(i) = n2 * sin(r). For spherical lenses, the lens formula is 1/f = 1/v - 1/u (with Cartesian sign convention). Power P of a lens is P = 1 / f(in meters), measured in Dioptres (D). Convex lens has positive power; concave lens has negative power.",
        "simp_exp": "A convex reading glass lens has a focal length of +0.5 meters. Its optical power is P = 1 / 0.5 = +2.0 Dioptres (D)!",
        "analogies": {
            "space": "Hubble and James Webb Space Telescope primary optical mirrors focusing distant deep space starlight.",
            "coding": "Ray tracing refraction algorithms calculating Snell angle bends across glass and water shaders.",
            "animals": "Chameleon eyes with independently moving convex lenses zooming in on tiny insects."
        },
        "prompt": "A convex lens has a focal length of +50 cm (+0.5 meters). What is the optical power of this lens in Dioptres?",
        "options": ["+2.0 Dioptres", "+0.5 Dioptres", "-2.0 Dioptres", "+5.0 Dioptres"],
        "answer": "+2.0 Dioptres",
        "exp": "Power P = 1 / f (in meters). Since f = +50 cm = +0.5 m, P = 1 / 0.5 = +2.0 Dioptres (D). Convex lenses have positive power.",
        "hints": ["Convert focal length to meters first: 50 cm = 0.5 m.", "Formula: Power P = 1 / f(in meters).", "P = 1 / 0.5 = +2.0 D."],
        "scaffolds": ["Step 1: Convert f to meters: f = 50 cm = 0.5 m.", "Step 2: Formula P = 1 / f.", "Step 3: P = 1 / 0.5 = +2.0 Dioptres."]
    },

    # --- English (4 Chapters) ---
    (10, "English", 1): {
        "concept_name": "A Letter to God by G.L. Fuentes (Faith, Irony & Human Nature)",
        "diff": 4,
        "objectives": ["Analyze dramatic situational irony in literature", "Evaluate faith versus cynicism in human relationships"],
        "prereq": ["Reading comprehension"],
        "std_exp": "Gregorio Lopez Fuentes' classic story portrays Lencho, a poor Mexican farmer whose corn harvest is destroyed by hailstorms. Lencho writes a letter to God requesting 100 pesos. The kind postmaster collects 70 pesos from postal workers to sustain Lencho's faith. In a poignant irony, Lencho accuses the post office staff of stealing the missing 30 pesos ('bunch of crooks').",
        "simp_exp": "Lencho had supreme faith in God. When the kind postal workers raised 70 pesos to help him, Lencho didn't suspect God at all—he thought the post office clerks stole the other 30 pesos!",
        "analogies": {
            "space": "A space rover attributing a fortuitous software patch to cosmic luck while ignoring the engineering mission control team.",
            "coding": "A client blaming the cloud server host for missing cache records after engineers worked overtime to restore 70% of lost data.",
            "animals": "A rescued dog barking aggressively at the vet who is dressing its wounds."
        },
        "prompt": "What profound situational irony concludes the story 'A Letter to God'?",
        "options": [
            "Lencho suspects the compassionate postal workers who generously contributed money of being 'a bunch of crooks' who stole from him",
            "The postmaster refuses to read Lencho's letter and burns it",
            "A second hailstorm arrives and destroys the post office building",
            "Lencho discovers gold buried under his destroyed corn field"
        ],
        "answer": "Lencho suspects the compassionate postal workers who generously contributed money of being 'a bunch of crooks' who stole from him",
        "exp": "The poignant situational irony is that the very post office employees who sacrificed their own salaries out of pure charity to preserve Lencho's faith are branded by him as dishonest thieves.",
        "hints": ["What did Lencho call the post office workers in his second letter?", "He called them a 'bunch of crooks'.", "They were the ones who actually gave him their own money."],
        "scaffolds": ["Step 1: Postmaster collected 70 pesos out of kindness.", "Step 2: Lencho received 70 pesos instead of 100.", "Step 3: Irony: Lencho blamed the charitable helpers for stealing the missing 30 pesos."]
    },
    (10, "English", 2): {
        "concept_name": "Nelson Mandela: Long Walk to Freedom (Courage & Emancipation)",
        "diff": 4,
        "objectives": ["Analyze political memoir and rhetorical eloquence", "Define courage as the triumph over fear, and evaluate the twin obligations of man"],
        "prereq": ["Historical reading"],
        "std_exp": "Mandela's autobiography marks the 1994 inauguration of South Africa's first democratic non-racial government. Mandela reflects: 'Courage was not the absence of fear, but the triumph over it', and asserts that both the oppressed and the oppressor are robbed of their humanity by prejudice.",
        "simp_exp": "Nelson Mandela spent 27 years in prison fighting apartheid. He taught the world that being brave does not mean you never feel fear: bravery means facing and conquering your fear!",
        "analogies": {
            "space": "Apollo astronauts igniting lunar escape thrusters despite immense life-or-death fear.",
            "coding": "Refactoring monolithic legacy infrastructure under extreme downtime risk with decisive courage.",
            "animals": "A lioness defending her cubs against a pack of hyenas despite severe wounds."
        },
        "prompt": "According to Nelson Mandela in 'Long Walk to Freedom', how is TRUE COURAGE defined?",
        "options": [
            "Courage is not the absence of fear, but the triumph over fear",
            "Courage is the complete lack of physical or emotional fear",
            "Courage is winning military battles without negotiating peace",
            "Courage is ignoring the needs of others to protect oneself"
        ],
        "answer": "Courage is not the absence of fear, but the triumph over fear",
        "exp": "Mandela observed: 'I learned that courage was not the absence of fear, but the triumph over it. The brave man is not he who does not feel afraid, but he who conquers that fear.'",
        "hints": ["Does a brave person feel fear?", "Yes, but they conquer it.", "Courage is the triumph over fear."],
        "scaffolds": ["Step 1: Mandela watched comrades risk lives for an ideal.", "Step 2: He noted fear is a natural human emotion.", "Step 3: True courage is conquering and triumphing over fear."]
    },
    (10, "English", 3): {
        "concept_name": "From the Diary of Anne Frank (Holocaust Testimony & Adolescence)",
        "diff": 4,
        "objectives": ["Analyze historical primary source diary literature", "Examine psychological resilience and adolescent introspection during war"],
        "prereq": ["World War II history basics"],
        "std_exp": "13-year-old Jewish girl Anne Frank hid in a secret annex in Amsterdam for two years during Nazi occupation. Her diary, affectionately named 'Kitty', captures the profound philosophical insight that 'paper has more patience than people', blending normal adolescent humor with harrowing historical resilience.",
        "simp_exp": "Anne was in hiding from the Nazis, yet she poured her deepest thoughts into her diary named 'Kitty', showing that writing down your feelings gives you strength in the hardest times!",
        "analogies": {
            "space": "Black box flight recorders preserving telemetry and voice communications during perilous flight re-entries.",
            "coding": "Immutable append-only audit logs recording mission state changes during crisis deployments.",
            "animals": "A badger surviving in deep concealed underground burrows through hostile winter storms."
        },
        "prompt": "What famous observation did Anne Frank record in her diary regarding why she preferred writing to confiding in acquaintances?",
        "options": [
            "'Paper has more patience than people'",
            "'Silence is the ultimate weapon of war'",
            "'Books are more dangerous than guns'",
            "'Words fade away while deeds remain'"
        ],
        "answer": "'Paper has more patience than people'",
        "exp": "Anne wrote 'Paper has more patience than people' because a diary listens quietly without judgment, boredom, or betrayal, allowing her to express her authentic thoughts freely.",
        "hints": ["Think about paper versus human listeners.", "Paper never gets tired of listening to your thoughts.", "She wrote: 'Paper has more patience than people'."],
        "scaffolds": ["Step 1: Anne had loving parents and friends, but lacked a true confidante.", "Step 2: She reflected on her desire to confide completely.", "Step 3: She concluded: 'Paper has more patience than people'."]
    },
    (10, "English", 4): {
        "concept_name": "Glimpses of India & The Trees (Cultural Heritage & Liberation)",
        "diff": 4,
        "objectives": ["Examine regional Indian cultural heritage (Goan pader, Coorg coffee, Assam tea)", "Analyze poetic symbolism in Adrienne Rich's 'The Trees'"],
        "prereq": ["Poetry analysis and cultural geography"],
        "std_exp": "The prose trilogy explores India's rich cultural mosaic: Goan Portuguese bakers ('pader'), warrior heritage and coffee estates of Coorg, and legendary origins of Assam tea. Adrienne Rich's feminist poem 'The Trees' symbolizes trees breaking free from decorative interior captivity back to their natural forest.",
        "simp_exp": "The story takes us to Goa with traditional village bread bakers, Coorg with fragrant coffee hills, and Assam where lush green tea gardens stretch across misty rivers!",
        "analogies": {
            "space": "Exploration rovers surveying diverse planetary geology across volcanic plains, frozen craters, and canyons.",
            "coding": "Modular micro-frontends each reflecting distinct localized cultural UI/UX paradigms.",
            "animals": "Spotted deer, king cobras, and hornbills thriving in the lush rainforests of Coorg."
        },
        "prompt": "In 'Glimpses of India', what traditional title is given to the beloved village bread baker in Goa?",
        "options": ["Pader", "Kabai", "Boliya", "Chaiwala"],
        "answer": "Pader",
        "exp": "The traditional Goan bread baker, whose jingling bamboo staff announced fresh morning loaves, is affectionately known as the 'Pader' in Goa.",
        "hints": ["It is a Portuguese-influenced Goan word for baker.", "Begins with the letter 'P'.", "The traditional baker is called a Pader."],
        "scaffolds": ["Step 1: Recall the traditional bakery heritage in Goa.", "Step 2: Elders fondly reminisce about the bread makers.", "Step 3: The bakers are known as 'Pader'."]
    }
}
