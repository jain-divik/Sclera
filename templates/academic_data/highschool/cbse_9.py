# CBSE Grade 9 Academic Data
# Mathematics, Chemistry, Physics, Biology, and other subjects

CBSE_9_DATA = {
    'Mathematics': {
        'chapters': {
            'Orienting Yourself – The Use of Coordinates': {
                'topics': [
                    {
    'name': 'The Historical Journey of Coordinates',
    'overview': (
        'A coordinate system uses numbers to locate points on a grid. '
        'Its roots stretch from the Indus Valley’s grid‑planned cities (2600 BCE), '
        'through Baudhāyana, Āryabhata, Brahmagupta, and Arab mathematicians, '
        'to Descartes’ formal Cartesian plane (1637 CE). '
        'This topic explores that journey, highlighting why each contribution matters.'
    ),
    'explanations': [
        # 1. What is a coordinate system?
        'A coordinate system is a framework that uses numbers to identify the exact position of a point on a plane.',
        'The two most common reference lines are a horizontal X‑axis and a vertical Y‑axis.',
        'The point where they meet is called the origin, labelled (0, 0).',
        'Using this system, any location can be described by a unique ordered pair (x, y).',
        'This combination of algebra and geometry is called coordinate geometry.',

        # 2. Indus Valley Civilisation (Sindhu‑Sarasvati)
        'Around 2600 BCE, the Sindhu‑Sarasvati Civilisation built cities like Mohenjo‑daro and Harappa with a precise grid of streets.',
        'Main streets ran exactly North–South and East–West at regular intervals of about 10 metres.',
        'This created a natural coordinate system: one could locate a shop by counting blocks from the city centre.',
        'Thus, the concept of using two perpendicular directions to pinpoint a location existed over 4,500 years ago.',

        # 3. Baudhāyana (c. 800 BCE)
        'Baudhāyana wrote the Baudhāyana Śulbasūtra, a text on geometry.',
        'He used East–West and North–South reference lines for constructing altars and geometric figures.',
        'He stated the theorem: the diagonal of a rectangle produces an area equal to the sum of the areas produced by its sides.',
        'This is today called the Baudhāyana–Pythagoras Theorem, and it is the foundation of the distance formula.',
        'Thus, coordinate geometry’s core tool (distance between two points) originated with Baudhāyana.',

        # 4. Ujjayinī – India’s prime meridian
        'Ancient Indian astronomers defined Ujjayinī (modern Ujjain) as the central longitude reference.',
        'By the 4th century BCE, the Siddhāntas described it as the zero‑longitude line for astronomical calculations.',
        'The Greek astronomer Ptolemy (c. 150 BCE) catalogued thousands of places by latitude and longitude, including “Ozine” (Ujjayinī).',
        'This shows that the idea of a fixed reference line (meridian) was well established in India long before Greenwich.',

        # 5. Āryabhata (c. 499 CE)
        'Āryabhata revolutionised astronomy by replacing the Greek system of chords with sines (jyā).',
        'Working with sines made it much simpler to calculate coordinates of stars, planets, and cities.',
        'He mapped the entire sky using Celestial Coordinates, measuring positions from the ecliptic (the Sun’s apparent path).',
        'His sine table and methods later spread to the Arab world and Europe, becoming the basis for modern trigonometry.',

        # 6. Brahmagupta (c. 628 CE)
        'Brahmagupta’s text Brāhmasphuṭasiddhānta defined zero as a number and gave rules for arithmetic with zero.',
        'He also treated negative numbers as legitimate entities, explaining how to add, subtract, multiply, and divide them.',
        'Without zero, we could not define the origin (0, 0). Without negative numbers, we could not have axes extending in opposite directions.',
        'His work directly enabled the four‑quadrant Cartesian plane that you will use throughout this chapter.',
        'His book was translated into Arabic (as Sindhind), and the Ujjayinī meridian became known as “Arin” on Arab maps.',

        # 7. Al‑Birūnī (c. 1000 CE) and Omar Khayyām (c. 1100 CE)
        'Al‑Birūnī travelled to India, studied Indian Siddhāntas, and used Indian trigonometry to compute coordinates of cities across Asia.',
        'He perfected the astrolabe, a handheld instrument that allowed sailors to find their latitude and longitude by observing stars.',
        'Omar Khayyām, a Persian mathematician and poet, was the first to solve algebraic equations using geometry.',
        'He interpreted equations as curves on a plane, effectively treating them as coordinate‑based graphs – a major step towards analytic geometry.',

        # 8. René Descartes (1637 CE)
        'Descartes, building on Fermat’s work, formalised the Cartesian coordinate system.',
        'He showed that every point in a plane can be described by an ordered pair (x, y), representing distances from two perpendicular axes.',
        'Geometric shapes like lines and circles could now be described by algebraic equations, uniting geometry and algebra.',
        'This “Cartesian” plane is the same system you will use throughout this and future chapters.',

        # 9. Why this history is important (exam connection)
        'Understanding the historical development helps you remember the key concepts: the axes, origin, ordered pairs, and the distance formula.',
        'Questions often ask: “Which Indian mathematician’s work made the four‑quadrant plane possible?” – Answer: Brahmagupta.',
        'Or: “State the theorem used to find the distance between two points.” – Answer: Baudhāyana‑Pythagoras Theorem.',

        # End‑of‑topic exam‑oriented Q&A
        'Q1: What is a coordinate system, and why is it important? A: A coordinate system uses numbers (x, y) to describe exact locations on a plane. It connects algebra and geometry, enabling precise measurement and description of shapes.',
        'Q2: Name the civilisation that first used grid‑based town planning. A: The Sindhu‑Sarasvati (Indus Valley) Civilisation, around 2600 BCE.',
        'Q3: Who formalised zero and negative numbers, and why was this essential for coordinate geometry? A: Brahmagupta (c. 628 CE). Zero became the origin (0, 0), and negatives allowed axes to extend left and down, creating all four quadrants.',
        'Q4: What theorem forms the basis of the distance formula? A: The Baudhāyana–Pythagoras Theorem – the square of the hypotenuse equals the sum of squares of the other two sides.',
        'Q5: How did Āryabhata improve coordinate calculations? A: He replaced chords with sines (jyā), making it easier to calculate coordinates of celestial and terrestrial objects.',
        'Q6: What role did Ujjayinī play in the history of coordinates? A: It served as India’s prime meridian, the reference line from which longitudes were measured, as early as the 4th century BCE.',
    ],
    'key_points': [
        'Coordinate system: a grid using an X‑axis and a Y‑axis to locate points with ordered pairs (x, y).',
        'Indus Valley (2600 BCE): grid‑planned streets (N‑S and E‑W) — earliest known practical coordinate system.',
        'Baudhāyana (800 BCE): used reference lines; gave the Baudhāyana–Pythagoras Theorem → foundation of the distance formula.',
        'Ujjayinī (4th century BCE): India’s prime meridian; used by Ptolemy as “Ozine”.',
        'Āryabhata (499 CE): replaced chords with sines; created Celestial Coordinates.',
        'Brahmagupta (628 CE): formalised zero and negative numbers → made the four‑quadrant plane possible.',
        'Al‑Birūnī (1000 CE): computed city coordinates with Indian methods; improved the astrolabe.',
        'Omar Khayyām (1100 CE): solved algebraic equations by treating them as curves on a coordinate plane.',
        'Descartes (1637): invented the Cartesian plane — any point defined by (x, y); united algebra and geometry.',
        'Exam priority: Brahmagupta → zero/negatives; Baudhāyana → distance formula; Descartes → Cartesian plane.',
    ],
    'images': [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Cartesian-coordinate-system.svg',
            'caption': 'The Cartesian coordinate plane: two perpendicular axes intersecting at the origin (0, 0), dividing the plane into four quadrants.'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/3/31/Civilt%C3%A0ValleIndoMappa.png',
            'caption': 'Map of the Indus Valley Civilization showing Mohenjo‑daro and other major sites with grid‑planned cities.'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/7/7d/Mahakal_Temple_Ujjain.JPG',
            'caption': 'Mahakaleshwar Temple in Ujjain (ancient Ujjayinī) — India\'s historic prime meridian mentioned in ancient Siddhāntas.'
        },
    ],
    'resources': {
        'videos': [
            'https://www.youtube.com/watch?v=LgtyMZsLV7E',
            'https://www.youtube.com/watch?v=bgfS3A_u27c',
            'https://www.youtube.com/watch?v=Ut2jlLOGKkg',
            'https://youtu.be/DTwzCoiiRAs?si=hkOFAMPog9nhvw-h',
        ],
        'pdfs': [
            'https://ncert.nic.in/textbook.php?iemh1=1-8',
            'https://ncert.nic.in/textbook/pdf/iemh1-1.pdf',
        ],
        'practice': [
            'Think and Reflect (Textbook p. 3): Why can’t the position of windows be marked on a floor map (Fig. 1.1)?',
            'Research: Find out about the grid‑based town planning of Dholavira. Compare it with Mohenjo‑daro.',
            'Discuss: How did Brahmagupta’s work on zero and negative numbers make the four‑quadrant plane possible?',
            'Exam‑style question: Name the ancient Indian city that served as the prime meridian.',
            'Exam‑style question: Which theorem is used to find the distance between two points in a plane?',
        ],
    },
},
                {
    'name': 'The 2‑D Cartesian Coordinate System',
    'overview': (
        'This system uses two perpendicular number lines (axes) meeting at the origin (0, 0) '
        'to divide the plane into four quadrants. Every point is represented by an ordered pair '
        '(x, y), where x is the distance from the Y‑axis and y is the distance from the X‑axis. '
        'It is the foundation for all work in coordinate geometry.'
    ),
    'explanations': [
        # --- 1. The two axes ---
        'The Cartesian plane consists of a horizontal number line called the X‑axis and a vertical number line called the Y‑axis.',
        'These axes are perpendicular to each other. They intersect at a point called the origin, labelled O (0, 0).',
        'Both axes extend infinitely in both positive and negative directions, just like ordinary number lines.',

        # --- 2. The origin ---
        'The origin is the reference point from which all distances are measured.',
        'Its coordinates are (0, 0): the x‑coordinate is 0 (no horizontal distance) and the y‑coordinate is 0 (no vertical distance).',
        'It is the common starting point for locating any other point on the plane.',

        # --- 3. Positive and negative directions ---
        'On the X‑axis, values to the right of the origin are positive; to the left are negative.',
        'On the Y‑axis, values above the origin are positive; below are negative.',
        'This convention is universal and is used consistently throughout all coordinate geometry problems.',

        # --- 4. The four quadrants ---
        'The axes divide the plane into four regions called quadrants, numbered I, II, III, IV in a counter‑clockwise manner.',
        'Quadrant I: both x and y are positive (+, +).',
        'Quadrant II: x is negative, y is positive (−, +).',
        'Quadrant III: both x and y are negative (−, −).',
        'Quadrant IV: x is positive, y is negative (+, −).',
        'These sign conventions are crucial because they instantly tell you which quadrant a point lies in without plotting.',

        # --- 5. Locating a point ---
        'A point is represented by an ordered pair (x, y), where x is the abscissa (first coordinate) and y is the ordinate (second coordinate).',
        'To locate the point (a, b), start at the origin. Move |a| units horizontally: right if a > 0, left if a < 0.',
        'Then move |b| units vertically: up if b > 0, down if b < 0. Mark the spot. That is the point P(a, b).',
        'The order matters: (3, 4) and (4, 3) are different points unless 3 = 4.',

        # --- 6. Points on the axes ---
        'Any point lying on the X‑axis has its y‑coordinate equal to 0. It can be written as (a, 0).',
        'Any point lying on the Y‑axis has its x‑coordinate equal to 0. It can be written as (0, b).',
        'The origin itself lies on both axes, hence (0, 0).',
        'This property is often used to quickly test if a point belongs to an axis.',

        # --- 7. The special case of coordinates being equal ---
        'If x = y, the points lie on a line that passes through the origin at 45° to both axes (the line y = x).',
        'Such points have coordinates like (1, 1), (−2, −2), (0, 0). They are symmetric with respect to the axes. This is an important observation used in many geometry problems.',

        # --- 8. Real‑world connection (Reiaan and Shalini) ---
        'In the textbook, Reiaan and Shalini’s room‑planning problem illustrates the need for two coordinates.',
        'A single number (like distance along a wall) could not locate a window’s position; a second number (distance from the adjacent wall) was needed.',
        'This is exactly why a coordinate system needs two axes: to describe a point’s position in a plane unambiguously.',

        # --- 9. Connection to the distance formula (preview) ---
        'Once a point is plotted, its distance from another point can be found using the Baudhāyana‑Pythagoras theorem (the distance formula).',
        'Though this is covered in a later section, knowing that (x, y) values feed directly into the formula shows why correct plotting is vital.',

        # --- Exam‑oriented Q&A ---
        'Q1: What is the Cartesian plane? A: A plane with two perpendicular number lines (axes) intersecting at the origin (0, 0). Any point is represented by an ordered pair (x, y).',
        'Q2: Name the four quadrants and the sign of coordinates in each. A: Quadrant I (+, +), II (−, +), III (−, −), IV (+, −).',
        'Q3: Where does the point (0, −5) lie? A: On the Y‑axis, 5 units below the origin (negative y‑axis).',
        'Q4: The point (−3, 4) lies in which quadrant? A: Quadrant II (x negative, y positive).',
        'Q5: What are the coordinates of the origin? A: (0, 0).',
        'Q6: How do you plot the point (2, −3)? A: Start at O. Move 2 units right, then 3 units down. Mark the point.',
        'Q7: Why is the order of coordinates important? A: Because (x, y) and (y, x) represent different points unless x = y. For example, (2, 3) and (3, 2) are distinct points.',
        'Q8: If a point has y‑coordinate 0, where does it lie? A: On the X‑axis.',
    ],
    'key_points': [
        'Cartesian plane: formed by two perpendicular number lines (X‑axis and Y‑axis) intersecting at the origin.',
        'Origin: (0, 0) — the reference point for all measurements.',
        'X‑axis: horizontal; positive to the right, negative to the left.',
        'Y‑axis: vertical; positive upwards, negative downwards.',
        'Quadrants: I (+, +), II (−, +), III (−, −), IV (+, −).',
        'Ordered pair (x, y): x is the abscissa (horizontal distance), y is the ordinate (vertical distance).',
        'Plotting: move right/left by x, then up/down by y.',
        'Points on X‑axis: y = 0 (form (a, 0)). Points on Y‑axis: x = 0 (form (0, b)).',
        'The coordinate system gives every point a unique address, enabling geometric figures to be described algebraically.',
    ],
    'images': [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/4/44/Cartesian_coordinate_system_%28comma%29.svg',
            'caption': 'Cartesian coordinate system with grid lines and sample points plotted in different quadrants, showing how coordinates are written as ordered pairs (x, y).'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/2/2e/Cartesian-coordinate-system-with-circle.svg',
            'caption': 'Cartesian plane with a circle centered at the origin, demonstrating how the distance formula relates to the Pythagorean theorem for finding distances between points.'
        },
    ],
    'resources': {
        'videos': [
            'https://www.youtube.com/watch?v=wr_GXSIGYZQ',
            'https://www.youtube.com/watch?v=3MIZUl6bWxY'
        ],
        'pdfs': [
            'https://ncert.nic.in/textbook.php?iemh1=1-8',
            'https://ncert.nic.in/textbook/pdf/iemh1-1.pdf',
        ],
        'practice': [
            'Textbook Exercise 1.1: Plot the points (2, 3), (−1, 5), (−4, −2), (3, −4) and identify the quadrant for each.',
            'Think and Reflect: Why is the origin called (0, 0)?',
            'Try by yourself: If you are at (−5, 0) and move 3 units right and 2 units up, what are your new coordinates?',
            'Exam‑style: In which quadrant does the point (−2, 7) lie? (Answer: II)',
            'Exam‑style: A point lies on the X‑axis. Its x‑coordinate is −3. Write its coordinates. (Answer: (−3, 0))',
        ],
    },
},
{
    'name': 'Coordinates of Points on the Axes',
    'overview': (
        'Points that lie directly on the X‑axis or Y‑axis have a special property: '
        'one of their coordinates is always zero. A point on the X‑axis has the form '
        '(x, 0), and a point on the Y‑axis has the form (0, y). The origin (0, 0) is '
        'the unique point that lies on both axes simultaneously. This topic explains '
        'how to identify, write, and plot such points, and why this property is crucial '
        'for coordinate geometry.'
    ),
    'explanations': [
        # 1. Recap: the axes and the origin
        'The Cartesian plane is formed by two perpendicular number lines: the horizontal X‑axis and the vertical Y‑axis.',
        'These axes intersect at a single point called the origin, labelled O, with coordinates (0, 0).',
        'The origin is the reference point from which all distances and positions are measured.',
        'Both axes extend infinitely in positive and negative directions, just like ordinary number lines.',

        # 2. Points on the X‑axis
        'Any point that lies exactly on the X‑axis has its y‑coordinate equal to 0.',
        'This is because the point has no vertical displacement — it is neither above nor below the axis.',
        'The general form of a point on the X‑axis is (a, 0), where a is the distance from the Y‑axis.',
        'If a > 0, the point lies to the right of the origin on the positive X‑axis.',
        'If a < 0, the point lies to the left of the origin on the negative X‑axis.',
        'If a = 0, the point is the origin itself: (0, 0).',
        'Examples: (3, 0) lies 3 units to the right of the origin. (−5, 0) lies 5 units to the left. (0, 0) is the origin.',

        # 3. Points on the Y‑axis
        'Any point that lies exactly on the Y‑axis has its x‑coordinate equal to 0.',
        'This is because the point has no horizontal displacement — it is neither to the right nor to the left of the axis.',
        'The general form of a point on the Y‑axis is (0, b), where b is the distance from the X‑axis.',
        'If b > 0, the point lies above the origin on the positive Y‑axis.',
        'If b < 0, the point lies below the origin on the negative Y‑axis.',
        'If b = 0, the point is again the origin: (0, 0).',
        'Examples: (0, 4) lies 4 units above the origin. (0, −2) lies 2 units below. (0, 0) is the origin.',

        # 4. The origin — a point on both axes
        'The origin (0, 0) is the only point that satisfies both conditions: it lies on the X‑axis (because y = 0) and on the Y‑axis (because x = 0).',
        'When asked "Which point lies on both axes?", the answer is always the origin.',

        # 5. How to determine if a point lies on an axis
        'Step 1: Look at the ordered pair (x, y).',
        'Step 2: If y = 0, the point is on the X‑axis (or is the origin if x is also 0).',
        'Step 3: If x = 0, the point is on the Y‑axis (or is the origin if y is also 0).',
        'Step 4: If both x and y are non‑zero, the point lies in one of the four quadrants — not on any axis.',

        # 6. Visualising points on axes
        'On graph paper, points on the X‑axis appear exactly on the horizontal line.',
        'Points on the Y‑axis appear exactly on the vertical line.',
        'Plotting these points is simpler because you only need to move in one direction: either horizontally for (a, 0) or vertically for (0, b).',

        # 7. Connection to the textbook story (Reiaan and Shalini)
        'In the textbook, Reiaan’s room (Fig. 1.3) has points marked on the axes.',
        'For example, the door point D₁ = (8, 0) lies on the X‑axis, meaning it is on the floor line with no height.',
        'The corner O = (0, 0) is the origin where the two walls meet.',
        'This shows how points on axes are used to describe real‑world positions along walls, floors, or reference lines.',

        # 8. Common mistakes to avoid
        'Mistake 1: Writing (0, x) instead of (x, 0) for a point on the X‑axis. Remember: X‑axis → y = 0, so it is (x, 0).',
        'Mistake 2: Writing (y, 0) instead of (0, y) for a point on the Y‑axis. Remember: Y‑axis → x = 0, so it is (0, y).',
        'Mistake 3: Thinking that (0, 0) lies only on one axis. It lies on both.',
        'Mistake 4: Confusing "point on X‑axis" with "point in Quadrant I". A point like (3, 0) is on the axis, not in any quadrant.',
        'Mistake 5: Forgetting the sign. Negative coordinates are valid: (−4, 0) and (0, −3) are both legitimate points on axes.',

        # 9. Why this topic matters (exam connection)
        'Questions on points on axes appear frequently in CBSE exams, often as 1‑mark or 2‑mark questions.',
        'Typical exam question: "Write the coordinates of a point on the X‑axis that is 5 units away from the origin."',
        'Answer: (5, 0) or (−5, 0). Both are correct unless the direction is specified.',
        'Knowing the form of points on axes also helps in plotting graphs, solving geometry problems, and understanding symmetry.',

        # Exam‑oriented Q&A
        'Q1: What is the general form of a point on the X‑axis? A: (x, 0), where x is the distance from the Y‑axis.',
        'Q2: What is the general form of a point on the Y‑axis? A: (0, y), where y is the distance from the X‑axis.',
        'Q3: What are the coordinates of the origin? A: (0, 0). It is the only point that lies on both axes.',
        'Q4: The point (0, −7) lies on which axis? A: On the Y‑axis, 7 units below the origin (negative Y‑axis).',
        'Q5: The point (11, 0) lies on which axis? A: On the X‑axis, 11 units to the right of the origin.',
        'Q6: How do you determine if a point (a, b) lies on an axis? A: Check if a = 0 (Y‑axis) or b = 0 (X‑axis). If both are 0, it is the origin.',
        'Q7: A point lies on the X‑axis at a distance of 6 units from the origin. Write its possible coordinates. A: (6, 0) or (−6, 0).',
        'Q8: A point lies on the Y‑axis at a distance of 3 units from the origin. Write its possible coordinates. A: (0, 3) or (0, −3).',
        'Q9: Which of these points lie on the axes: (4, 0), (0, −2), (3, 3), (−1, 0), (0, 0)? A: (4, 0) on X‑axis; (0, −2) on Y‑axis; (−1, 0) on X‑axis; (0, 0) on both. (3, 3) is not on any axis; it is in Quadrant I.',
        'Q10: Why is the origin special? A: It is the reference point (0, 0) where both axes meet. All coordinates are measured from it.',
    ],
    'key_points': [
        'Points on the X‑axis have the form (x, 0): the y‑coordinate is always zero.',
        'Points on the Y‑axis have the form (0, y): the x‑coordinate is always zero.',
        'The origin (0, 0) lies on both axes — it is the only point with this property.',
        'To test if a point lies on an axis: check if either coordinate is zero.',
        'X‑axis points have no vertical displacement; Y‑axis points have no horizontal displacement.',
        'Points on positive X‑axis: x > 0, y = 0. Points on negative X‑axis: x < 0, y = 0.',
        'Points on positive Y‑axis: x = 0, y > 0. Points on negative Y‑axis: x = 0, y < 0.',
        'Points on axes are NOT in any of the four quadrants — they lie on the boundary lines.',
        'Plotting axis points: move only horizontally for (x, 0) or only vertically for (0, y).',
        'Exam priority: form of points on axes, identifying axis from given coordinates, and writing coordinates for a given distance on an axis.',
    ],
    'images': [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Cartesian-coordinate-system.svg',
            'caption': 'The Cartesian coordinate plane showing the X‑axis (horizontal), Y‑axis (vertical), origin (0, 0) at the centre, and sample points on both axes.'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/2D_Cartesian_Coordinates.svg/1024px-2D_Cartesian_Coordinates.svg.png',
            'caption': 'Points marked on the X‑axis (y = 0) and Y‑axis (x = 0), illustrating the special forms (x, 0) and (0, y).'
        },
    ],
    'resources': {
        'videos': [
            'https://www.youtube.com/watch?v=LgtyMZsLV7E', ### TO CHANGE
            'https://www.youtube.com/watch?v=bgfS3A_u27c', ### TO CHANGE
            'https://www.youtube.com/watch?v=kKnfiJjX2qM', ### TO CHANGE
        ],
        'pdfs': [
            'https://ncert.nic.in/textbook.php?iemh1=1-8',
            'https://ncert.nic.in/textbook/pdf/iemh1-1.pdf',
        ],
        'practice': [
            'Textbook Exercise 1.1 (p. 5): Refer to Fig. 1.3. Identify which points lie on the X‑axis and which lie on the Y‑axis. Write their coordinates.',
            'Think and Reflect: Can a point lie on both axes? If yes, which point?',
            'Plot on graph paper: (6, 0), (−3, 0), (0, 5), (0, −4), (0, 0). Label each point and state which axis it belongs to.',
            'Exam‑style: A point lies on the X‑axis at a distance of 9 units from the origin. Write its coordinates.',
            'Exam‑style: Name the axis on which the point (0, −11) lies.',
            'Challenge: A point is 4 units away from the X‑axis and lies on the Y‑axis. Find its possible coordinates.',
        ],
    },
},
{
    'name': 'Distance Between Two Points in the 2‑D Plane',
    'overview': (
        'The distance between any two points in the Cartesian plane is found using the '
        'Baudhāyana–Pythagoras theorem. If the coordinates of the points are (x₁, y₁) '
        'and (x₂, y₂), the distance d is √[(x₂ − x₁)² + (y₂ − y₁)²]. '
        'This formula works for all points, whether they lie in the same quadrant, '
        'different quadrants, or even on the axes.'
    ),
    'explanations': [
        # 1. The need for the distance formula
        'When two points are plotted on the Cartesian plane, the straight line joining them is the hypotenuse of a right‑angled triangle.',
        'The legs of this triangle are the horizontal and vertical differences between the points.',
        'The horizontal leg is the difference of x‑coordinates: |x₂ − x₁|.',
        'The vertical leg is the difference of y‑coordinates: |y₂ − y₁|.',
        'These two legs form the perpendicular sides of a right triangle, with the distance between the points as the hypotenuse.',

        # 2. Baudhāyana–Pythagoras theorem connection
        'Baudhāyana (c. 800 BCE) gave the earliest known statement of the theorem: the square of the hypotenuse equals the sum of the squares of the other two sides.',
        'Applying this theorem to the right triangle formed by the differences gives: d² = (x₂ − x₁)² + (y₂ − y₁)².',
        'Taking the square root yields the distance formula: d = √[(x₂ − x₁)² + (y₂ − y₁)²].',
        'This formula is thus a direct application of the Baudhāyana–Pythagoras theorem in a coordinate setting.',

        # 3. How to use the formula — step by step
        'Step 1: Identify the coordinates of the two points. Label them (x₁, y₁) and (x₂, y₂). The labelling order does not matter.',
        'Step 2: Find the difference of the x‑coordinates: x₂ − x₁.',
        'Step 3: Find the difference of the y‑coordinates: y₂ − y₁.',
        'Step 4: Square both differences.',
        'Step 5: Add the squared values.',
        'Step 6: Take the square root of the sum. That is the distance.',

        # 4. Special case: horizontal distance
        'If the two points have the same y‑coordinate (y₁ = y₂), the line is horizontal.',
        'The formula simplifies to d = √[(x₂ − x₁)² + 0] = |x₂ − x₁|, which is the absolute difference of the x‑coordinates.',
        'This is the length of the horizontal leg, confirming that the general formula works for simple cases.',

        # 5. Special case: vertical distance
        'If the two points have the same x‑coordinate (x₁ = x₂), the line is vertical.',
        'Then d = √[0 + (y₂ − y₁)²] = |y₂ − y₁|, the absolute difference of the y‑coordinates.',
        'Again, the general formula reduces to a one‑dimensional length.',

        # 6. Distance from the origin
        'To find the distance of a point (x, y) from the origin (0, 0), substitute (0, 0) as the first point.',
        'd = √[(x − 0)² + (y − 0)²] = √(x² + y²).',
        'This is a frequently used special case.',

        # 7. Properties and important observations
        'Distance is always non‑negative. The square root ensures d ≥ 0.',
        'Distance is symmetric: the distance from A to B is equal to the distance from B to A.',
        'The formula uses squares, so the order of subtraction (x₁ − x₂ vs x₂ − x₁) does not matter because squaring removes the sign.',
        'The distance between two coincident points (same coordinates) is 0.',

        # 8. Common errors to avoid
        'Mistake 1: Forgetting to square the differences before adding.',
        'Mistake 2: Adding the differences before squaring (x₂−x₁ + y₂−y₁)² — this is wrong.',
        'Mistake 3: Taking the square root of each term separately (√(a²) + √(b²)) instead of √(a²+b²).',
        'Mistake 4: Mixing up the coordinates; (x₁,y₂) and (x₂,y₁) are wrong substitutions.',
        'Mistake 5: Using the formula when one of the points is unknown — always ensure coordinates are correctly identified first.',

        # 9. Worked example (from NCERT style)
        'Example: Find the distance between A(3, 4) and B(7, 1).',
        'Solution: x₁=3, y₁=4; x₂=7, y₂=1.',
        'x₂−x₁ = 7−3 = 4; (4)² = 16.',
        'y₂−y₁ = 1−4 = −3; (−3)² = 9.',
        'Sum = 16+9 = 25.',
        'Distance = √25 = 5 units.',

        # 10. Exam‑oriented Q&A
        'Q1: State the distance formula. A: The distance between (x₁,y₁) and (x₂,y₂) is √[(x₂−x₁)² + (y₂−y₁)²].',
        'Q2: Which theorem is used to derive the distance formula? A: The Baudhāyana–Pythagoras theorem.',
        'Q3: Find the distance between the points (0, 0) and (−3, 4). A: √[(−3−0)² + (4−0)²] = √(9+16) = √25 = 5 units.',
        'Q4: The distance between (a, 0) and (0, 0) is 5. Find the possible values of a. A: √(a²) = 5 → |a| = 5 → a = ±5.',
        'Q5: If two points have the same x‑coordinate, what is the distance formula simplified to? A: |y₂−y₁|.',
        'Q6: Is the distance between (2, 3) and (2, 3) zero? A: Yes, because both points coincide.',
        'Q7: Find the distance between the points (1, 2) and (4, 6). A: √[(4−1)²+(6−2)²] = √(9+16) = √25 = 5.',
        'Q8: What is the distance of point (−6, 8) from the origin? A: √(36+64) = √100 = 10.',
        'Q9: If the distance between (2, y) and (5, 3) is √13, find y. A: (5−2)² + (3−y)² = 13 → 9 + (3−y)² = 13 → (3−y)² = 4 → 3−y = ±2 → y = 1 or 5.',
        'Q10: Can the distance between two distinct points be negative? A: No, distance is always non‑negative.',
    ],
    'key_points': [
        'Distance formula: d = √[(x₂ − x₁)² + (y₂ − y₁)²].',
        'Derived from the Baudhāyana–Pythagoras theorem using the horizontal and vertical differences as legs of a right triangle.',
        'The formula works for any two points in the plane, irrespective of quadrant or axis.',
        'If y₁ = y₂, the line is horizontal and d = |x₂ − x₁|.',
        'If x₁ = x₂, the line is vertical and d = |y₂ − y₁|.',
        'Distance from origin to (x, y): d = √(x² + y²).',
        'Distance is always non‑negative; symmetric; zero only for coincident points.',
        'Order of subtraction does not matter because of squaring.',
        'Common exam use: finding lengths of sides of triangles, verifying collinearity, and checking if given coordinates form a specific geometric shape.',
    ],
    'images': [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/5/5e/Triangle.Centroid.svg',
            'caption': 'Triangle with centroid marked: shows how coordinate geometry is used to find geometric centers like centroids using coordinate averages.'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/8/8e/Ellipse_in_coordinate_system_with_semi-axes_labelled.svg',
            'caption': 'Ellipse in coordinate system: demonstrates how conic sections are represented using coordinate equations with center and axes.'
        },
    ],
    'resources': {
        'videos': [
            'https://www.youtube.com/watch?v=nyZuiteUsPM',
            'https://www.youtube.com/watch?v=0IOEPcAHpm4',
            'https://www.youtube.com/watch?v=HhEQy3WDR1E',
        ],
        'pdfs': [
            'https://ncert.nic.in/textbook.php?iemh1=1-8',
            'https://ncert.nic.in/textbook/pdf/iemh1-1.pdf',
        ],
        'practice': [
            'Textbook Exercise (Section 1.4, p. 7–8): Find the distances between given pairs of points.',
            'Think and Reflect: Why is the distance formula symmetric?',
            'Practice: Plot A(2,3) and B(5,7) on graph paper and verify the distance using the formula.',
            'Exam‑style: Show that the points (1,2), (3,6), and (6,3) form a right triangle using the distance formula.',
            'Exam‑style: Find the value(s) of k if the distance between (2,k) and (−3,1) is √41.',
        ],
    },
},
## Topic 1.5 – Midpoint of a Line Segment
{
    'name': 'Midpoint of a Line Segment',
    'overview': (
        'The midpoint of a line segment is the point that divides it into two equal parts. '
        'If the endpoints are A(x₁, y₁) and B(x₂, y₂), the coordinates of the midpoint M are '
        '((x₁ + x₂)/2, (y₁ + y₂)/2). This formula averages the x‑coordinates and the y‑coordinates '
        'separately, giving the exact centre of the segment.'
    ),
    'explanations': [
        # 1. What is a midpoint?
        'A midpoint is the point that lies exactly halfway along a line segment.',
        'It divides the segment into two equal lengths. If M is the midpoint of AB, then AM = MB.',
        'The midpoint lies on the line segment itself, directly between the endpoints.',

        # 2. How to find the midpoint — step by step
        'Step 1: Write down the coordinates of the two endpoints. Label them (x₁, y₁) and (x₂, y₂).',
        'Step 2: Add the x‑coordinates: x₁ + x₂.',
        'Step 3: Divide the sum by 2. This gives the x‑coordinate of the midpoint.',
        'Step 4: Add the y‑coordinates: y₁ + y₂.',
        'Step 5: Divide the sum by 2. This gives the y‑coordinate of the midpoint.',
        'Step 6: Write the midpoint as an ordered pair: M = ((x₁ + x₂)/2, (y₁ + y₂)/2).',

        # 3. Why this formula works
        'The x‑coordinate of the midpoint is simply the average (mean) of the x‑coordinates of the endpoints.',
        'Similarly, the y‑coordinate is the average of the y‑coordinates.',
        'This makes sense because the midpoint lies exactly at the centre of both the horizontal and vertical projections.',
        'If you move half the horizontal difference and half the vertical difference from one endpoint, you reach the midpoint.',
        'Indeed: starting from A(x₁,y₁), moving (x₂−x₁)/2 horizontally and (y₂−y₁)/2 vertically lands at M.',

        # 4. Special cases
        'If the segment is horizontal (y₁ = y₂), the midpoint still has y = y₁ = y₂, and x = (x₁+x₂)/2.',
        'If the segment is vertical (x₁ = x₂), the midpoint has x = x₁ = x₂, and y = (y₁+y₂)/2.',
        'The midpoint of a segment from (a, b) to (−a, b) is (0, b) because the x‑coordinates cancel.',

        # 5. Midpoint and symmetry
        'The midpoint is the centre of symmetry for the line segment. Both endpoints are equidistant from it.',
        'If M is the midpoint of AB, then reflecting A across M gives B, and vice versa.',
        'This property is used in many geometry problems, including finding the fourth vertex of a parallelogram.',

        # 6. Application: finding an endpoint when the midpoint is known
        'If one endpoint A(x₁,y₁) and the midpoint M(mx, my) are known, the other endpoint B can be found.',
        'Since mx = (x₁ + x₂)/2, solving gives x₂ = 2mx − x₁.',
        'Similarly, y₂ = 2my − y₁.',
        'This is a common exam question type.',

        # 7. Common mistakes
        'Mistake 1: Adding x₁ and y₁, then dividing by 2 — you must add corresponding coordinates of the two points.',
        'Mistake 2: Subtracting instead of adding: (x₂−x₁)/2 gives the half‑distance, not the midpoint coordinate.',
        'Mistake 3: Writing the midpoint as ( (x₁+y₁)/2 , (x₂+y₂)/2 ) — this mixes x and y incorrectly.',
        'Mistake 4: Forgetting to divide by 2.',

        # 8. Worked example (NCERT style)
        'Example: Find the midpoint of the segment joining A(2, 3) and B(8, 7).',
        'Solution: x₁=2, y₁=3; x₂=8, y₂=7.',
        'x‑coordinate of midpoint = (2+8)/2 = 10/2 = 5.',
        'y‑coordinate of midpoint = (3+7)/2 = 10/2 = 5.',
        'Midpoint M = (5, 5).',

        # 9. Exam‑oriented Q&A
        'Q1: Write the midpoint formula. A: ((x₁+x₂)/2, (y₁+y₂)/2).',
        'Q2: Find the midpoint of the segment joining (4, −2) and (−6, 8). A: ((4−6)/2, (−2+8)/2) = (−1, 3).',
        'Q3: If (3, 4) is the midpoint of AB and A is (1, 2), find B. A: B = (2·3−1, 2·4−2) = (5, 6).',
        'Q4: The midpoint of a segment is (0, 0) and one endpoint is (a, b). What is the other endpoint? A: (−a, −b).',
        'Q5: Show that the midpoint of a segment joining (x₁,y₁) and (x₂,y₂) is also the midpoint of the segment joining (x₂,y₂) and (x₁,y₁). A: The formula is symmetric.',
        'Q6: Is the midpoint always inside the segment? A: Yes, by definition it lies on the segment exactly halfway between the endpoints.',
        'Q7: Find the midpoint of a segment joining (0, 0) and (0, 0). A: (0, 0).',
        'Q8: The midpoint of a segment on the X‑axis joining (a,0) and (b,0) is? A: ((a+b)/2, 0).',
    ],
    'key_points': [
        'Midpoint M of A(x₁,y₁) and B(x₂,y₂): M = ((x₁+x₂)/2, (y₁+y₂)/2).',
        'The midpoint formula simply averages the x‑coordinates and the y‑coordinates separately.',
        'The midpoint divides the segment into two equal parts: AM = MB.',
        'If the midpoint and one endpoint are known, the other endpoint is obtained by doubling the midpoint coordinates and subtracting the known coordinates.',
        'For horizontal segments (y₁=y₂), midpoint y‑coordinate remains unchanged.',
        'For vertical segments (x₁=x₂), midpoint x‑coordinate remains unchanged.',
        'The midpoint is the centre of symmetry of the segment.',
        'Common uses: finding centres of line segments, verifying bisectors, constructing parallelograms, and solving coordinate geometry puzzles.',
    ],
    'images': [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Midpoint.svg/1024px-Midpoint.svg.png',
            'caption': 'The midpoint M of a line segment AB: it divides the segment into two equal lengths. The coordinates are the averages of the endpoints\' coordinates.'
        },
    ],
    'resources': {
        'videos': [
            'https://www.youtube.com/watch?v=Ez_-RwV9yVo',
            'https://www.youtube.com/watch?v=2mY5j1gJqCY',
            'https://www.youtube.com/watch?v=8llIhR4FO4A',
        ],
        'pdfs': [
            'https://ncert.nic.in/textbook.php?iemh1=1-8',
            'https://ncert.nic.in/textbook/pdf/iemh1-1.pdf',
        ],
        'practice': [
            'Textbook Exercise (Section 1.5, p. 9–10): Find the midpoints of given segments.',
            'Think and Reflect: How is the midpoint formula related to the concept of average?',
            'Practice: Plot A(−2,3) and B(4,−1). Find the midpoint, plot it on the same graph, and verify distances.',
            'Exam‑style: If M(2,−3) is the midpoint of AB and A(5,1), find B.',
            'Exam‑style: The three vertices of a parallelogram are (1,2), (4,5), and (7,2). Find the fourth vertex using the midpoint property of diagonals.',
        ],
    },
}
                ]
            },
            'Introduction to Linear Polynomials': {
                'topics': [
    {
        'name': 'Algebraic Expressions — Terms, Variables, Coefficients, Constants',
        'overview': (
            'An algebraic expression is a combination of numbers, variables (letters that represent quantities), '
            'and operations (addition, subtraction, multiplication, division). '
            'This topic teaches how to identify terms, coefficients, and constants, '
            'how to simplify by combining like terms, and how to distinguish a polynomial from other expressions.'
        ),
        'explanations': [
            # 1. What is an algebraic expression?
            'An algebraic expression is made up of numbers, variables, and arithmetic operations (+, −, ×, ÷).',
            'It does not contain an equality sign (=). An equation has an equality sign; an expression does not.',
            'Example: 3x + 5, 7y − 2, and 4a² + 2a − 1 are algebraic expressions.',
            'An expression can have one or more terms.',
            'Based on number of terms: monomial (1 term), binomial (2 terms), trinomial (3 terms), polynomial (many terms).',

            # 2. Terms of an expression
            'A term is a part of an expression separated by a “+” or “−” sign.',
            'In 4x + 7y − 3, the terms are 4x, 7y, and −3.',
            'Terms have a sign attached to them. The expression 5x − 2 has terms 5x and −2.',
            'When listing terms, always include the sign before the term.',
            'A term without a variable is a constant term.',

            # 3. Variable, coefficient, constant
            'Variable: a symbol (usually a letter) whose value can vary; e.g., in 3x + 5, x is the variable.',
            'Coefficient: the numerical factor of a term containing a variable; in 3x, the coefficient of x is 3.',
            'Constant: a term with a fixed numerical value and no variable; in 3x + 5, 5 is the constant.',
            'If a term is just x, the coefficient is 1. If it is −y, the coefficient is −1.',
            'Numerical coefficient: the number part. Literal coefficient: the variable part (including exponents).',
            'In 4xy, the numerical coefficient is 4, and the literal coefficient is xy.',

            # 4. Like and unlike terms
            'Like terms have the same variable(s) with the same exponent(s). Example: 5x and −3x are like terms.',
            'Unlike terms have different variables or exponents. Example: 4x and 4y are unlike terms.',
            'Only like terms can be combined (added or subtracted).',
            'Combining like terms: add/subtract the coefficients, keep the variable part unchanged.',
            'Example: 7a + 3b − 2a + b = (7a−2a) + (3b+b) = 5a + 4b.',
            '3xy² and −5xy² are like terms; 3x²y and 3xy² are unlike terms.',

            # 5. What is a polynomial?
            'A polynomial is an algebraic expression where the variables have only whole‑number exponents (0, 1, 2, 3, …).',
            'The exponents cannot be negative, fractional, or under a root.',
            'Thus, 2x + 3 is a polynomial, but 1/x (which is x⁻¹) and √x (which is x^(1/2)) are NOT polynomials.',
            'All polynomials are algebraic expressions, but not all algebraic expressions are polynomials.',
            'Zero polynomial: The constant 0 is a polynomial with undefined degree.',
            'Constant polynomial: e.g., 5, −3 are polynomials of degree 0.',

            # 6. Degree of a term and of an expression
            'The degree of a term is the sum of the exponents of its variables. For the term 3x², the degree is 2.',
            'For a term like 4x²y³, degree = 2+3 = 5.',
            'The degree of a polynomial is the highest degree among its terms.',
            'Example: 4x³ + 2x − 7 has degree 3.',
            'A constant term (like 5) has degree 0.',
            'Arrange polynomials in descending order of degree for standard form.',

            # 7. Evaluating an expression
            'To evaluate an expression, replace the variable with a given number and compute the result.',
            'Example: Find the value of 2x + 3 when x = 4. 2·4 + 3 = 8 + 3 = 11.',
            'Use parentheses when substituting negative values: 2(−3) + 1 = −6 + 1 = −5.',
            'Evaluation is like using a formula — it gives a numerical output for each input.',

            # 8. Common mistakes
            'Mistake 1: Thinking every algebraic expression is a polynomial — remember exponent rules.',
            'Mistake 2: Combining unlike terms (e.g., 3x + 2y cannot be simplified further).',
            'Mistake 3: Ignoring the sign of a term when simplifying.',
            'Mistake 4: Forgetting that a variable on its own has coefficient 1.',
            'Mistake 5: Saying x/2 is not a polynomial — it is (1/2)x, which is fine because exponent of x is 1.',
            'Mistake 6: Confusing term with factor: in 2(x+3), (x+3) is not a term; the expression is not in simplest polynomial form.',

            # 9. Exam‑oriented Q&A
            'Q1: Define algebraic expression. A: A combination of numbers, variables, and operations (+, −, ×, ÷) without an equality sign.',
            'Q2: Identify the terms in 5x − 2y + 7. A: 5x, −2y, 7.',
            'Q3: Write the coefficient of y in −9y. A: −9.',
            'Q4: Is 1/(x+2) a polynomial? A: No, because the variable appears in the denominator, making the exponent −1 (not a whole number).',
            'Q5: What is the degree of the polynomial 6x⁴ − 2x² + 3? A: 4.',
            'Q6: Simplify: 3a + 5b − 2a + b. A: (3a−2a) + (5b+b) = a + 6b.',
            'Q7: Evaluate 4x − 7 for x = 3. A: 4·3 − 7 = 12 − 7 = 5.',
            'Q8: Classify as monomial, binomial, trinomial: 2x, x+y, a²+2ab+b². A: monomial, binomial, trinomial.',
        ],
        'key_points': [
            'Algebraic expression: numbers, variables, operations — no equality sign.',
            'Terms are separated by + or −; each term has a sign.',
            'Coefficient: numerical part of a term with a variable; constant: term with only a number.',
            'Like terms have identical variable parts; they can be combined.',
            'Polynomial: variables have only whole‑number exponents, no division by variable.',
            'Degree of a polynomial = highest sum of exponents of variables in any term.',
            'Evaluation: substitute the variable with a number and calculate.',
            'Monomial (1 term), binomial (2 terms), trinomial (3 terms).',
            'Zero polynomial has no defined degree, constant non-zero polynomial has degree 0.',
            'A variable without a visible coefficient has coefficient 1; e.g., x means 1x.',
        ],
        'images': [
            {
                'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Algebraic_expression.svg/1024px-Algebraic_expression.svg.png',
                'caption': 'An algebraic expression consists of terms, coefficients, variables, and constants. This diagram illustrates the parts of 3x³ + 2x² + x + 5.'
            },
        ],
        'resources': {
            'videos': [
                'https://www.youtube.com/watch?v=9BQJ1jGNGhM',   # Khan Academy: terms, factors, coefficients
                'https://www.youtube.com/watch?v=U7GtA1UQnYQ',   # Magnet Brains: Algebraic Expressions Class 9
            ],
            'pdfs': [
                'https://ncert.nic.in/textbook.php?iemh1=2-12',
                'https://ncert.nic.in/textbook/pdf/iemh1-2.pdf',
            ],
            'practice': [
                'Textbook Exercise 2.1 (p. 19): Identify polynomials, find coefficients, evaluate expressions.',
                'Think and Reflect: Is 0 a polynomial? (Hint: Yes, it is a constant polynomial.)',
                'Simplify: 7x − 4y + 2x + 9y − 3.',
                'Write an algebraic expression for: “5 more than twice a number n”.',
                'Exam‑style: Which of these are polynomials? (a) 3x² + 4 (b) 1/x (c) √x (d) x³ − 2x + 1.',
                'Find the degree of the polynomial 3x²y + 4xy − 5.',
                'Evaluate 2a² − 3a + 1 for a = −2.',
            ],
        },
    },
    {
        'name': 'Linear Polynomials — Definition, Degree, General Form',
        'overview': (
            'A linear polynomial is a polynomial of degree 1. It has the general form '
            'p(x) = ax + b (a ≠ 0), where a and b are constants. '
            'This topic covers the definition, evaluation, zero of a linear polynomial, '
            'and how it represents a straight‑line relationship.'
        ),
        'explanations': [
            # 1. Definition of a linear polynomial
            'A polynomial whose highest power of the variable is 1 is called a linear polynomial.',
            'It is also called a first‑degree polynomial.',
            'The name “linear” comes from the fact that its graph is a straight line.',
            'Examples: 2x + 3, −4y + 1, 5z − 7, p(x) = 0.5x + 2.',
            'Non-examples: x² + 3 (degree 2), 1/x (not a polynomial), 5 (constant).',

            # 2. General form
            'The general form is p(x) = ax + b, where a and b are constants, and a ≠ 0.',
            'If a = 0, the expression reduces to just b (a constant polynomial), which is not linear.',
            'a and b can be any real numbers (integers, fractions, decimals).',
            'The variable can be any letter; the important thing is the exponent is 1.',
            'If b = 0, the linear polynomial becomes p(x) = ax, which passes through the origin.',

            # 3. Degree of a linear polynomial
            'The degree is simply 1, because the highest exponent of the variable is 1.',
            'Example: In 5x − 3, the term 5x has degree 1 and the constant −3 has degree 0; overall degree = 1.',
            'Degree 1 implies exactly one variable raised to power 1.',

            # 4. Evaluating a linear polynomial
            'Replace the variable with a given number and compute the value.',
            'Example: For p(x) = 2x + 3, p(4) = 2·4 + 3 = 11.',
            'Use brackets for negative values: p(−1) = 2(−1) + 3 = 1.',
            'Evaluation helps in plotting points to draw the straight‑line graph.',

            # 5. Zero of a linear polynomial
            'The zero (or root) of a linear polynomial is the value of the variable that makes the polynomial equal to zero.',
            'Set ax + b = 0 → x = −b/a.',
            'Every linear polynomial has exactly one zero (since a ≠ 0).',
            'Example: Zero of 3x − 6 is 3x − 6 = 0 → x = 2.',
            'Graphically, the zero is the x‑coordinate where the line crosses the X‑axis (x‑intercept).',
            'To verify, substitute the zero back: p(2) = 3(2)−6 = 0.',

            # 6. Linear polynomial as a function
            'A linear polynomial behaves like a function: each input x gives exactly one output p(x).',
            'We can write it as y = ax + b, which is the equation of a straight line.',
            'This connection between algebra and geometry is a big idea in coordinate geometry.',

            # 7. Common mistakes
            'Mistake 1: Forgetting that a must not be zero. If a = 0, it is a constant polynomial, not linear.',
            'Mistake 2: Confusing “linear polynomial” with “linear equation”. A polynomial is an expression; an equation has an “=” sign.',
            'Mistake 3: Thinking the coefficient of x must be 1 — no, it can be any non‑zero number.',
            'Mistake 4: Incorrectly stating the zero; always solve ax + b = 0 carefully.',
            'Mistake 5: Saying p(x) = 2x + 3x² is linear — it is quadratic because of x² term.',
            'Mistake 6: Writing zero as b/a instead of −b/a.',

            # 8. Exam‑oriented Q&A
            'Q1: Define a linear polynomial. A: A polynomial of degree 1, written in the form ax + b where a ≠ 0.',
            'Q2: Give two examples of linear polynomials. A: 4x − 7 and −2y + 9.',
            'Q3: Write the general form and state the condition. A: p(x) = ax + b, a ≠ 0.',
            'Q4: Find the degree of 7x − 4. A: 1.',
            'Q5: Evaluate p(x) = 5x + 2 for x = −1. A: 5(−1) + 2 = −3.',
            'Q6: Find the zero of the linear polynomial 2x + 8. A: 2x + 8 = 0 → x = −4.',
            'Q7: Is 0·x + 3 a linear polynomial? A: No, because the coefficient of x is 0; it is a constant polynomial.',
            'Q8: If the zero of a linear polynomial p(x) = ax + 3 is 1, find a. A: a·1 + 3 = 0 → a = −3.',
            'Q9: Write a linear polynomial whose zero is −5. A: p(x) = x + 5 (since x+5=0 → x=−5); or any multiple like 2x+10.',
            'Q10: Is 2 a linear polynomial? Justify. A: No, it is a constant polynomial; degree 0, not 1.',
        ],
        'key_points': [
            'Linear polynomial: degree = 1; general form: p(x) = ax + b, a ≠ 0.',
            'Evaluation: substitute the given value of x and simplify.',
            'Zero of linear polynomial: solve ax + b = 0 → x = −b/a.',
            'The graph of y = ax + b is a straight line (introduced but explored fully in next topic).',
            'Constant polynomial (degree 0) is NOT linear.',
            'Linear polynomials are the simplest type of non‑constant polynomial.',
            'Every non-zero linear polynomial has exactly one zero.',
            'Coefficient a can be any non-zero real number (integer, fraction, decimal).',
            'A linear polynomial with b=0 passes through the origin (0,0).',
            'Zeros are also called roots or solutions of ax+b=0.',
        ],
        'images': [
            {
                'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Linear_function_graph.svg/1024px-Linear_function_graph.svg.png',
                'caption': 'Graph of a linear polynomial y = ax + b is always a straight line. Here a is the slope and b is the y‑intercept.'
            },
        ],
        'resources': {
            'videos': [
                'https://www.youtube.com/watch?v=1SlKX3JbO30',   # Magnet Brains: Linear Polynomials Class 9
                'https://www.youtube.com/watch?v=Hd_8bjPP2dM',   # LearnoHub: Linear Polynomials
            ],
            'pdfs': [
                'https://ncert.nic.in/textbook.php?iemh1=2-12',
                'https://ncert.nic.in/textbook/pdf/iemh1-2.pdf',
            ],
            'practice': [
                'Textbook Exercise 2.2 (p. 22): Identify linear polynomials, evaluate, find zeros.',
                'Think and Reflect: Can a linear polynomial have more than one zero? (No, only one.)',
                'Write five linear polynomials of your own and find their zeros.',
                'If p(x) = 7x − 14, find p(3) and the zero of p(x).',
                'Exam‑style: Is 3/x + 5 a linear polynomial? Justify.',
                'Find a if the zero of p(x) = ax − 8 is 4.',
                'Write the linear polynomial whose zero is 2/3 and coefficient of x is 3.',
            ],
        },
    },
    {
        'name': 'Slope and y‑intercept of the Straight Line y = ax + b',
        'overview': (
            'When a linear polynomial p(x) = ax + b is plotted, it gives a straight line. '
            'The coefficient a is called the slope (steepness), and the constant b is the y‑intercept '
            '(the point where the line crosses the Y‑axis). '
            'This topic explains how to interpret and graph using slope and intercept.'
        ),
        'explanations': [
            # 1. From linear polynomial to straight line
            'If we write y = p(x) = ax + b, we get the equation of a straight line.',
            'Every point (x, y) on this line satisfies the equation.',
            'The graph of y = ax + b is a straight line extending infinitely in both directions.',
            'The line is completely determined by its slope and y-intercept.',

            # 2. The meaning of “slope” (a)
            'Slope measures the steepness of the line. It tells how much y changes when x increases by 1.',
            'Slope = (change in y) / (change in x) = a.',
            'If a > 0, the line goes upward from left to right (positive slope — as x increases, y increases).',
            'If a < 0, the line goes downward from left to right (negative slope — as x increases, y decreases).',
            'If a = 0, the line is horizontal (y = b), and is no longer a linear polynomial but a constant function.',
            'The larger the absolute value of a, the steeper the line.',
            'Slope can be expressed as a fraction (rise/run).',

            # 3. The meaning of “y‑intercept” (b)
            'The y‑intercept is the y‑coordinate of the point where the line meets the Y‑axis.',
            'At that point, x = 0, so y = a·0 + b = b. Thus the point is (0, b).',
            'It tells you “where the line starts” on the Y‑axis.',
            'If b = 0, the line passes through the origin (0,0).',

            # 4. Finding x‑intercept
            'The x‑intercept is the point where the line crosses the X‑axis (y = 0).',
            'Set y = 0 and solve: 0 = ax + b → x = −b/a. Point is (−b/a, 0).',
            'For the line y = 2x + 4, x‑intercept: 0 = 2x + 4 → x = −2; point (−2,0).',

            # 5. Graphing using slope and intercept
            'Step 1: Plot the y‑intercept (0, b) on the graph.',
            'Step 2: From that point, use the slope to find another point. Move 1 unit to the right (increase x by 1), then move a units up (if a positive) or down (if a negative). Mark that second point.',
            'Step 3: Draw a straight line through the two points and extend it.',
            'Example: y = 2x + 1. y‑intercept (0,1); slope = 2. From (0,1), go right 1, up 2 → (1,3). Plot (0,1) and (1,3), draw line.',
            'If slope is a fraction p/q, move right q units, up/down p units.',

            # 6. Slope between two points
            'If two points (x1,y1) and (x2,y2) lie on the line, slope a = (y2 − y1) / (x2 − x1).',
            'This formula is used to find slope from a graph or data table.',
            'Example: (1,2) and (3,8) → a = (8−2)/(3−1) = 6/2 = 3.',

            # 7. Effect of changing a and b
            'Changing a changes the steepness and possibly the direction (positive/negative).',
            'Changing b shifts the line up or down without changing its slope.',
            'Lines with same a but different b are parallel.',
            'Lines with same b but different a all pass through (0,b).',
            'Perpendicular lines have slopes that multiply to −1 (e.g., 2 and −1/2) — beyond class 9 but good to know.',

            # 8. Real‑life meaning of slope and intercept
            'Slope represents a constant rate: speed (km per hour), cost per unit (₹ per kg), etc.',
            'y‑intercept represents an initial value: starting fee, fixed charge, starting distance, etc.',
            'Example: A taxi charges ₹20 as base fare and ₹15 per km. The fare y for x km is y = 15x + 20. Slope = 15 (rate per km), y‑intercept = 20 (initial fare).',

            # 9. Common mistakes
            'Mistake 1: Confusing slope with y‑intercept — remember “a” is slope (multiplier of x), “b” is the constant.',
            'Mistake 2: Plotting slope backwards: if slope = −3, moving right 1 means moving down 3, not up.',
            'Mistake 3: Forgetting that slope is “rise over run”, so a fraction like 1/2 means 1 up for 2 right.',
            'Mistake 4: Saying a horizontal line has no slope — it has slope 0.',
            'Mistake 5: Writing the y‑intercept as just b instead of the point (0,b).',
            'Mistake 6: Forgetting to solve ax+b=0 correctly for x‑intercept; sign error.',

            # 10. Exam‑oriented Q&A
            'Q1: What does the coefficient a represent in y = ax + b? A: The slope (steepness) of the line.',
            'Q2: What is the y‑intercept of the line y = −3x + 7? A: 7 (the point (0,7)).',
            'Q3: How do you graph y = −x + 4? A: Plot (0,4); slope −1 means right 1, down 1 to (1,3); draw line.',
            'Q4: Is the line y = 2x + 5 steeper than y = x + 5? A: Yes, because slope 2 > slope 1; it rises faster.',
            'Q5: Identify the slope and y‑intercept of the line y = 0.5x − 3. A: Slope = 0.5, y‑intercept = −3.',
            'Q6: Write the equation of a line with y‑intercept 4 and slope −2. A: y = −2x + 4.',
            'Q7: What does it mean if two lines have the same slope? A: They are parallel.',
            'Q8: Find the x‑intercept of y = 4x − 8. A: Set y=0 → 4x−8=0 → x=2. Point (2,0).',
            'Q9: A line passes through (0,5) and has slope −3. Write its equation. A: y = −3x + 5.',
        ],
        'key_points': [
            'y = ax + b is a straight line; a = slope, b = y‑intercept.',
            'Slope a: rate of change of y per unit increase in x.',
            'a > 0 → line rises; a < 0 → line falls; a = 0 → horizontal.',
            'y‑intercept b: the point (0, b) where the line crosses the Y‑axis.',
            'x‑intercept: set y=0 → x = −b/a; point (−b/a, 0).',
            'Graphing: start at (0,b), use slope a to find second point, draw line.',
            'Same a → parallel lines; same b → lines intersect Y‑axis at the same point.',
            'Real life: slope = rate (cost per unit, speed); intercept = initial value.',
            'Slope from two points: a = (y2−y1)/(x2−x1).',
            'For fractional slope p/q, move right q, up/down p.',
        ],
        'images': [
            {
                'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Slope_of_a_line.svg/1024px-Slope_of_a_line.svg.png',
                'caption': 'A line with positive slope. The slope is the rise over run: a = Δy / Δx. The line crosses the Y‑axis at the y‑intercept b.'
            },
        ],
        'resources': {
            'videos': [
                'https://www.youtube.com/watch?v=2j3La4G8b5Q',   # Khan Academy: Graph from slope-intercept equation
                'https://www.youtube.com/watch?v=OBxwlJAjjCU',   # LearnoHub: Slope and intercept
            ],
            'pdfs': [
                'https://ncert.nic.in/textbook.php?iemh1=2-12',
                'https://ncert.nic.in/textbook/pdf/iemh1-2.pdf',
            ],
            'practice': [
                'Textbook Exercise 2.3 (p. 25): Graph given lines, identify slope and intercept from equations.',
                'Think and Reflect: If a line passes through the origin, what is its y‑intercept? (0)',
                'Draw the lines y = 3x, y = 3x + 2, y = 3x − 2 on the same graph. What do you notice?',
                'Find the slope and y‑intercept of 2y = 4x + 6 (first write in y = ax + b form).',
                'Exam‑style: A line has equation y = −5x + 3. Does the line pass through the origin? Explain.',
                'Find the equation of the line with slope 4 passing through (0, −2).',
                'What is the x‑intercept of y = −2x + 10?',
            ],
        },
    },
    {
        'name': 'Linear Relationships in Real‑life Contexts',
        'overview': (
            'Many everyday situations can be modelled using linear polynomials. '
            'If a quantity changes at a constant rate, its relationship with another quantity is linear. '
            'This topic teaches how to identify such relationships, form the linear rule y = ax + b, '
            'and distinguish linear from non‑linear patterns.'
        ),
        'explanations': [
            # 1. What is a linear relationship?
            'A relationship between two quantities is linear if the rate of change of one with respect to the other is constant.',
            'In a table of values, equal changes in x produce equal changes in y.',
            'The graph of a linear relationship is a straight line.',
            'Mathematically, it can be modelled by y = ax + b.',

            # 2. Identifying linear relationships from a table
            'Step: Check that for each unit increase in x, the change in y is the same.',
            'Example: x: 0,1,2,3; y: 5,8,11,14 → differences: 3,3,3 → linear.',
            'If differences are not constant, the relationship is non‑linear.',
            'The constant difference is the slope a.',

            # 3. Forming a linear rule from a real situation
            'Step 1: Identify the two variables involved. Choose which one is independent (x) and which is dependent (y).',
            'Step 2: Find the constant rate of change — this is the slope a. Look for “per”, “each”, “every”.',
            'Step 3: Identify the initial value (value of y when x = 0) — this is the y‑intercept b.',
            'Step 4: Write the rule as y = ax + b.',
            'Step 5: Use the rule to predict other values.',
            'Independent variable is the cause/input (e.g., time, number of items). Dependent is the effect/output (e.g., cost, distance).',

            # 4. Example 1: Cost of apples
            'Apples cost ₹80 per kg. The total cost y for x kg is y = 80x.',
            'Here a = 80 (rate per kg), b = 0 (no fixed charge).',
            'The relationship is linear. If you buy 3 kg, cost = 80·3 = ₹240.',
            'Table: (0,0), (1,80), (2,160)... shows constant difference 80.',

            # 5. Example 2: Temperature conversion
            'Fahrenheit (F) and Celsius (C) relate by F = (9/5)C + 32.',
            'a = 9/5 (slope), b = 32 (y‑intercept).',
            'This is a linear relationship. The rate of change is constant: each 1°C rise increases F by 1.8°F.',
            'At C=0, F=32.',

            # 6. Example 3: Taxi fare (fixed + per km)
            'A taxi charges ₹20 as a fixed start fee and ₹15 per km travelled. Fare y for distance x km: y = 15x + 20.',
            'a = 15 (per km), b = 20 (initial fare).',
            'For 5 km, fare = 15·5 + 20 = 75 + 20 = ₹95.',
            'Graph starts at (0,20) and rises with slope 15.',

            # 7. Example 4: Water tank leaking (linear decay)
            'A water tank contains 100 L of water and leaks 5 L per hour. After x hours, water left y = 100 − 5x.',
            'a = −5 (negative slope, because quantity decreases), b = 100 (initial amount).',
            'After 3 hours, water left = 100 − 5·3 = 85 L.',
            'This models depletion at a constant rate.',

            # 8. More real‑life examples
            'Simple interest: I = (P×r/100)×t. For fixed P and r, I is linear in time t, with a = P×r/100, b = 0.',
            'Distance by car at constant speed v: d = vt. a = v, b = 0.',
            'Mobile phone bill: fixed monthly ₹100 plus ₹1.5 per minute: y = 1.5x + 100.',
            'Linear growth: plant height H = initial height + growth rate × weeks. e.g., H = 5 + 2w.',
            'Currency conversion: amount in new currency = exchange rate × amount in old currency. Linear with b=0.',
            'Cost of call: connection fee + rate per minute.',
            'Not all relationships are linear: area of square A = s² (quadratic), population growth often exponential.',

            # 9. How to tell if a relationship is linear
            'Check the differences in y for equal intervals of x. If they are equal, it is linear.',
            'Example: x: 1,2,3,4; y: 5,8,11,14 → differences: 3,3,3 → linear.',
            'If the differences are not constant, the relationship is non‑linear.',
            'Graphically, a non‑linear relationship will curve (not a straight line).',
            'Equation method: if equation can be written as y = ax + b (no powers other than 1), it’s linear.',

            # 10. Common mistakes
            'Mistake 1: Assuming every relationship is linear — always test with differences or check if rate is constant.',
            'Mistake 2: Mixing up which variable is dependent (y) and independent (x).',
            'Mistake 3: Not including a fixed starting value (b = 0 correctly when none exists).',
            'Mistake 4: Using negative slope incorrectly; for decrease, a must be negative.',
            'Mistake 5: Writing the rule as x = ay + b when the dependent variable should be isolated as y = ax + b.',
            'Mistake 6: Forgetting units when interpreting slope (e.g., ₹ per km, km per hour).',

            # 11. Exam‑oriented Q&A
            'Q1: A plumber charges ₹300 for a visit and ₹200 per hour of work. Write the total charge y for x hours. A: y = 200x + 300.',
            'Q2: How do you check if a table of values represents a linear relationship? A: Verify that equal differences in x correspond to equal differences in y.',
            'Q3: Is the relationship y = 3x² + 2 linear? A: No, because of the x² term; the graph is a parabola.',
            'Q4: A car is moving at a constant speed. Is the distance‑time relation linear? A: Yes, distance = speed × time, slope = speed (constant).',
            'Q5: For y = 50 − 10x, interpret the slope and intercept. A: Slope −10 means the quantity decreases by 10 per unit; intercept 50 is the initial value.',
            'Q6: Write an equation for: “The total cost of n pencils is ₹5 per pencil plus a ₹10 package charge”. A: y = 5n + 10.',
            'Q7: A tank has 200 L of water. Water is pumped out at 25 L per minute. Write equation for volume V after t minutes. A: V = 200 − 25t.',
            'Q8: What is the independent variable in “cooking time for a turkey: time = 20 minutes per pound plus 15 minutes”? A: weight in pounds; dependent: total time.',
        ],
        'key_points': [
            'Linear relationship: constant rate of change (equal y‑differences for equal x‑steps).',
            'Forming a linear rule: identify independent (x) and dependent (y), find rate (slope a) and starting value (y‑intercept b).',
            'Equation: y = ax + b.',
            'Positive a → growth; negative a → decay/decrement.',
            'Real‑life examples: cost per item, fixed + variable charges, temperature conversion, distance‑time (constant speed), simple interest, leak rates.',
            'Test for linearity: check constant differences or straight‑line graph.',
            'Non‑linear examples: area of square (A = s²), distance fallen under gravity (quadratic).',
            'Slope a is the “per unit” rate; y‑intercept b is the “initial fixed amount”.',
            'When b=0, the relationship is a direct proportion (y ∝ x).',
            'Always define what x and y represent when writing the equation.',
        ],
        'images': [
            {
                'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Taxifare_example_linear_function.svg/1024px-Taxifare_example_linear_function.svg.png',
                'caption': 'A real-life linear model: taxi fare = initial fare + (rate per km) × distance. Graph is a straight line.'
            },
        ],
        'resources': {
            'videos': [
                'https://www.youtube.com/watch?v=VbT8y4hx1os',   # Applications of linear equations in real life
                'https://www.youtube.com/watch?v=4v2c_OvKHfQ',   # Writing linear equations from word problems
            ],
            'pdfs': [
                'https://ncert.nic.in/textbook.php?iemh1=2-12',
                'https://ncert.nic.in/textbook/pdf/iemh1-2.pdf',
            ],
            'practice': [
                'Textbook Exercise 2.4 (p. 30): Form linear equations for given situations, solve problems.',
                'Think and Reflect: Is “y = 2ˣ” (exponential) linear? Check differences.',
                'Your electricity bill has a fixed meter charge of ₹50 and ₹6 per unit of consumption. Write the total bill for u units.',
                'A plant is 10 cm tall and grows 2 cm per week. Write its height after w weeks.',
                'Exam‑style: A mobile plan costs ₹100 per month plus ₹1.5 per minute of talk time. If your bill is ₹250, how many minutes did you talk?',
                'A car rental charges ₹500 plus ₹12 per km driven. Write equation for cost C for k km. Find cost for 150 km.',
                'Identify which of these tables represent linear relationships. For those that do, write the equation.',
            ],
        },
    },
    {
    'name': 'Visualising Linear Relationships — Tables, Plots, and the Straight Line',
    'overview': (
        'Any linear relationship of the form y = ax + b can be visualised by making a table of values, '
        'plotting the corresponding points on the Cartesian plane, and joining them. '
        'The result is always a straight line that extends infinitely in both directions. '
        'This topic teaches how to graph a linear equation, read values from the graph, and '
        'understand why the line represents every possible (x, y) pair that satisfies the equation.'
    ),
    'explanations': [
        # 1. From algebra to picture
        'The equation y = ax + b has infinitely many solutions: for every x, there is a corresponding y.',
        'Each solution (x, y) can be plotted as a point on the Cartesian plane.',
        'When enough points are plotted, they line up perfectly — the visual proof that the relationship is “linear”.',

        # 2. Making a table of values
        'Choose a few convenient x‑values (usually integers like −2, −1, 0, 1, 2).',
        'For each x, compute y = ax + b.',
        'Record the pairs (x, y) in a table.',
        'Example: For y = 2x − 1, when x = 0, y = −1; x = 1 → y = 1; x = 2 → y = 3.',
        'The table gives you ordered pairs ready to plot.',

        # 3. Plotting the points
        'Locate each point on the graph paper or Cartesian plane using its (x, y) coordinates.',
        'Start with the y‑intercept point (0, b) — this is always one of the points.',
        'Plot all the other points from the table.',
        'Use a ruler to check if they lie in a straight line.',

        # 4. Drawing the line
        'Join the plotted points with a straight line.',
        'Extend the line beyond the first and last points, putting arrows on both ends.',
        'The arrowheads indicate that the line continues forever, representing all real‑number solutions.',
        'The entire line is the graph of the equation y = ax + b.',

        # 5. Reading the graph
        'From the graph, you can find y for any given x (follow a vertical line from x up to the graph, then across to the y‑axis).',
        'You can also find x for a given y (go horizontal to the graph, then down to the x‑axis).',
        'This is called “reading the graph” and is very useful when you don’t want to solve algebraically.',

        # 6. Slope as steepness visually
        'Lines with larger |a| are steeper.',
        'Lines with the same slope are parallel — they never meet.',
        'A horizontal line (a = 0) has no steepness.',
        'A vertical line is not of the form y = ax + b; its equation is x = constant, and it is not a function.',

        # 7. Special features of a linear graph
        'The point where the line meets the X‑axis is the x‑intercept (found by setting y = 0 → x = −b/a).',
        'The point where the line meets the Y‑axis is the y‑intercept (0, b).',
        'These two intercepts are often the easiest points to plot when drawing the graph.',
        'If both intercepts are plotted, you can draw the line with just those two points.',

        # 8. Checking if a point lies on the line
        'A point (x₁, y₁) lies on the line if its coordinates satisfy the equation: y₁ = a·x₁ + b.',
        'This is a simple substitution check.',
        'If the equation is true, the point is on the line; if false, it is not.',

        # 9. Common mistakes
        'Mistake 1: Plotting (x, y) in the wrong order — remember, the first number is always x (horizontal), second is y (vertical).',
        'Mistake 2: Not extending the line beyond the plotted points; the line is infinite.',
        'Mistake 3: Drawing a wavy or kinked line instead of a straight one — always use a ruler.',
        'Mistake 4: Joining only the dots without checking if they are collinear; if one point is off, re‑check the calculation.',

        # 10. Exam‑oriented Q&A
        'Q1: How do you graph y = −x + 3? A: Make a table (e.g., x=0→y=3, x=1→y=2, x=3→y=0). Plot (0,3), (1,2), (3,0) and draw a straight line through them.',
        'Q2: Why is the graph a straight line? A: Because the relationship is linear: constant rate of change (slope) between x and y.',
        'Q3: How can you find the y‑intercept from the graph? A: It is the point where the line crosses the Y‑axis; its coordinates are (0, b).',
        'Q4: How do you check if (2, 5) lies on y = 3x − 1? A: Substitute: 5 = 3·2 − 1? 5 = 5, yes, so it lies on the line.',
        'Q5: What does a line with negative slope look like? A: It slants downward from left to right.',
        'Q6: Can you draw the graph using only the intercepts? A: Yes, plot (0,b) and (−b/a, 0), then draw the line.',
        'Q7: If a line passes through (0,0) and (2,6), what is its equation? A: Slope = 6/2 = 3; y‑intercept = 0 → y = 3x.',
    ],
    'key_points': [
        'Table of values: choose x‑values, compute corresponding y = ax + b.',
        'Plot the (x, y) pairs; they will align in a straight line.',
        'Draw the line through the points and extend it with arrows on both ends.',
        'The entire line represents all solutions of y = ax + b.',
        'Read the graph: go from x up to the line, then across to y‑axis, or reverse for x.',
        'Steeper lines have larger |a| (absolute slope); same a → parallel lines.',
        'Intercepts: y‑intercept (0,b); x‑intercept (−b/a, 0).',
        'A point is on the line if its coordinates satisfy the equation.',
        'Always use a ruler to draw the line straight.',
    ],
    'images': [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Graph_of_linear_function.png/1024px-Graph_of_linear_function.png',
            'caption': 'Graph of a linear function y = 2x + 1 showing a straight line. Points from a table of values lie exactly on the line.'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Linear_Function_Graph.svg/1024px-Linear_Function_Graph.svg.png',
            'caption': 'Multiple linear graphs with different slopes and intercepts. All are straight lines.'
        },
    ],
    'resources': {
        'videos': [
            'https://www.youtube.com/watch?v=2j3La4G8b5Q',   # Khan Academy: Graphing from slope-intercept equation
            'https://www.youtube.com/watch?v=OBxwlJAjjCU',   # LearnoHub: Graphing Linear Equations
        ],
        'pdfs': [
            'https://ncert.nic.in/textbook.php?iemh1=2-12',
            'https://ncert.nic.in/textbook/pdf/iemh1-2.pdf',
        ],
        'practice': [
            'Textbook Exercise 2.3 (p. 25): Draw graphs of y = 2x + 1, y = −x + 4, etc.',
            'Think and Reflect: If a line passes through (−1,−3) and (1, 3), what is its slope? Y‑intercept?',
            'Draw the line for y = 3x − 2. From the graph, find y when x = 2.5 and x when y = 1.',
            'Are the points (3,7), (0,1), and (−1,−1) collinear? Verify using both algebra and graph.',
            'Exam‑style: A line has y‑intercept 3 and passes through (2,7). Plot the line and find its equation.',
        ],
    },
},
{
    'name': 'Modelling Linear Growth and Linear Decay',
    'overview': (
        'When a quantity increases or decreases by a fixed amount each time period, '
        'its change is linear and can be expressed as y = ax + b. '
        'If a > 0, it models linear growth; if a < 0, linear decay. '
        'This topic teaches how to identify such patterns, write the linear model, graph it, '
        'and use it to make predictions.'
    ),
    'explanations': [
        # 1. What is a linear model?
        'A linear model uses a linear polynomial to describe how one quantity depends on another.',
        'The general form is y = ax + b, where x is the independent variable (time, number of items, etc.) and y is the dependent quantity.',
        'The model works when the quantity changes by a constant amount for each unit increase in x.',

        # 2. Linear growth (a > 0)
        'If the coefficient a is positive, the quantity y increases by a fixed amount each time x increases by 1.',
        'The graph is a straight line rising from left to right.',
        'Examples: savings with a fixed monthly deposit, plant height with constant weekly growth, cost proportional to number of items.',

        # 3. Example of linear growth
        'A person saves ₹200 every week. Starting with ₹500 already saved. After t weeks, total savings S = 200t + 500.',
        'Here a = 200 (rate of saving per week), b = 500 (initial amount).',
        'After 4 weeks: S = 200·4 + 500 = 800 + 500 = ₹1300.',
        'The graph is a line with y‑intercept 500 and slope 200.',

        # 4. Linear decay (a < 0)
        'If the coefficient a is negative, the quantity y decreases by a fixed amount each time x increases by 1.',
        'The graph is a straight line falling from left to right.',
        'Examples: water leaking from a tank at a constant rate, simple depreciation, temperature drop at a constant rate.',

        # 5. Example of linear decay
        'A water tank holds 100 litres and leaks 5 litres per hour. After t hours, water left W = 100 − 5t.',
        'Here a = −5 (rate of leakage), b = 100 (initial quantity).',
        'After 3 hours: W = 100 − 5·3 = 85 litres.',
        'Notice that a is negative, so the line slopes downward.',

        # 6. Interpreting the slope and intercept
        'In growth: a > 0 is the constant increase per unit of x. b is the starting value (when x = 0).',
        'In decay: a < 0 is the constant decrease per unit of x. b is the initial maximum value.',
        'The slope’s absolute value tells the rate of change; the sign tells the direction.',
        'The y‑intercept (b) is the value before any change occurs (x = 0).',

        # 7. Making predictions using the model
        'Once the linear equation is set up, you can substitute any x to find y (future or past values, within the valid range).',
        'You can also solve for x when y is given to find when a certain value will be reached.',
        'Example: When will the tank be empty? Set W = 0 → 0 = 100 − 5t → t = 20 hours.',

        # 8. Distinguishing linear from non‑linear growth/decay
        'Linear: constant difference in y for equal differences in x.',
        'Exponential or quadratic: differences are not constant; growth/decay speeds up.',
        'Example: Compound interest is not linear (interest earned grows each period).',
        'Simple interest is linear (same interest each period).',

        # 9. Common mistakes
        'Mistake 1: Confusing growth and decay — always check the sign of a.',
        'Mistake 2: Forgetting to include the starting value b. If initial amount is not zero, b must appear.',
        'Mistake 3: Using the model beyond reasonable limits (e.g., negative time, or negative water).',
        'Mistake 4: Thinking negative slope means decay in all contexts — negative slope can also just mean a decreasing variable, not necessarily decay over time.',

        # 10. Exam‑oriented Q&A
        'Q1: A plant is 8 cm tall and grows 3 cm per week. Write the equation for height h after w weeks. A: h = 3w + 8.',
        'Q2: A mobile phone loses ₹200 in value every month. If it costs ₹10,000 now, find its value after m months. A: V = 10000 − 200m.',
        'Q3: How can you tell from its equation whether a relationship models growth or decay? A: If the coefficient of x is positive, it is growth; if negative, it is decay.',
        'Q4: What does the y‑intercept represent in a growth/decay model? A: The initial value (when x = 0).',
        'Q5: A candle is 30 cm long and burns 2 cm per hour. How long until it burns completely? A: 30 − 2t = 0 → t = 15 hours.',
        'Q6: Is the interest earned from simple interest linear? A: Yes, because the amount increases by the same constant each year (interest = P·R·T/100).',
        'Q7: A taxi charges ₹25 fixed plus ₹12 per km. Write the fare equation. Is it growth or just a linear relationship? A: y = 12x + 25; it is a linear increase (growth) in fare with distance.',
    ],
    'key_points': [
        'Linear growth: quantity increases by a constant amount per unit → y = ax + b with a > 0.',
        'Linear decay: quantity decreases by a constant amount per unit → y = ax + b with a < 0.',
        'a is the constant rate of change (per unit of x); b is the initial value (when x = 0).',
        'Graph of growth: line sloping upward; graph of decay: line sloping downward.',
        'Use the model to predict: substitute x to find y; set y and solve for x.',
        'Check for linearity: equal changes in x → equal changes in y (constant differences).',
        'Real‑world applications: budgeting, science experiments, population studies (under constant rate assumptions).',
    ],
    'images': [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Linear_Growth_and_Decay.svg/1024px-Linear_Growth_and_Decay.svg.png',
            'caption': 'Comparison of linear growth (positive slope) and linear decay (negative slope). Both are straight lines, showing constant rates of change.'
        },
    ],
    'resources': {
        'videos': [
            'https://www.youtube.com/watch?v=4v2c_OvKHfQ',   # Linear growth and decay word problems
            'https://www.youtube.com/watch?v=IMZbKnN6Q4M',   # Applications of linear equations
        ],
        'pdfs': [
            'https://ncert.nic.in/textbook.php?iemh1=2-12',
            'https://ncert.nic.in/textbook/pdf/iemh1-2.pdf',
        ],
        'practice': [
            'Textbook Exercise 2.4 (p. 30): Solve real‑life problems on growth and decay.',
            'Think and Reflect: If a pool is filled at 10 litres per minute and initially contains 200 litres, write the volume equation. Is this growth or just accumulation?',
            'A car’s value depreciates linearly: it was ₹5,00,000 new and ₹4,50,000 after one year. Write its value V after y years (assuming linear depreciation).',
            'A candle burns at 0.5 cm per minute. If it is 20 cm long, find how long it takes to burn down to 5 cm.',
            'Exam‑style: A company’s profit was ₹2 lakh in 2020 and has increased by ₹10,000 every year since. Write the profit (P) as a function of years (t) after 2020. Predict the profit in 2025.',
        ],
    },
}
                ]
            },
            'The World of Numbers': {
                'topics': [
{
    'name': 'The Dawn of Mathematics — Counting, Natural Numbers, and Early Systems',
    'overview': (
        'Mathematics began as a human need to count possessions, animals, and days. '
        'Early humans used one‑to‑one correspondence (pebbles ↔ cattle) to keep track. '
        'This led to the concept of Natural Numbers (1, 2, 3, …). '
        'Ancient artifacts like the Lebombo bone and Ishango bone show tally marks '
        'dating back tens of thousands of years. '
        'In India, the Harappan civilisation used standardised weights, the Vedas named '
        'large powers of 10 up to 10¹², and Buddhist texts described numbers up to 10⁵³. '
        'Understanding natural numbers also involves recognising their algebraic properties, '
        'such as closure under addition but not under subtraction.'
    ),
    'explanations': [
        # 1. The need to count
        'Counting arose from practical needs: tracking how many animals were in a herd, how many pots were stored, or how many days had passed.',
        'The simplest method was **one‑to‑one correspondence** — matching each object to be counted with a physical token (pebble, notch on a stick, knot on a rope).',
        'This matching idea is the root of the concept of number: a pebble “stands for” one animal, and a collection of pebbles represents the set of animals.',

        # 2. Natural numbers
        'The numbers we use for counting — 1, 2, 3, 4, … — are called **Natural Numbers**.',
        'The set of natural numbers is denoted by ℕ = {1, 2, 3, 4, …}.',
        'Natural numbers are the simplest, most fundamental numbers. They answer “how many?” for positive whole‑number quantities.',

        # 3. The Lebombo bone (∼35 000 years old)
        'The Lebombo bone was discovered in the Lebombo Mountains of South Africa.',
        'It is a baboon fibula with 29 distinct notches carved into it.',
        'It is believed to be a tally stick — perhaps used to count the days of a lunar month — and is the oldest known mathematical artifact.',

        # 4. The Ishango bone (∼20 000 BCE)
        'The Ishango bone was found in the Nile Valley (present‑day Democratic Republic of Congo).',
        'It has three columns of asymmetric notches. One column shows the numbers 11, 13, 17, and 19 — all prime numbers!',
        'Another column seems to follow a pattern of doubling (3 and 6, 4 and 8, 5 and 10).',
        'This suggests that early humans were already experimenting with patterns and possibly prime numbers long before formal mathematics.',

        # 5. Harappan civilisation and standardised trade
        'The Indus Valley (Harappan) civilisation used standardised weights made of chert, following a binary‑decimal system: 1, 2, 4, 8, 16, 32, 64, then 160, 320, 640, etc.',
        'This uniformity allowed accurate trade in cotton, pottery, and precious stones (lapis lazuli) across huge distances — from Lothal to Mesopotamia.',
        'Seals and impressions from Harappa and Mohenjo‑daro indicate that a well‑developed accounting system existed.',

        # 6. Vedic large numbers (powers of 10)
        'The Vedas, particularly the Yajurveda, list names for powers of 10 up to 10¹² (*Parārdha*).',
        'For example, *śatam* (100), *sahasra* (1000), *ayuta* (10 000), *niyuta* (100 000), *prayuta* (1 000 000), *arbuda* (10 000 000), *nyarbuda* (100 000 000), etc., culminating in *parārdha* (10¹²).',
        'This shows that the concept of very large numbers existed in India over 3 000 years ago, and these names formed the basis of the decimal place‑value system.',
        'The Buddhist text *Lalitavistara* goes even further — Buddha names powers of 10 up to *tallakṣhaṇa* (10⁵³).',

        # 7. Base‑12 counting (finger‑joint counting)
        'In many ancient cultures, counting was also done in base 12 using the joints of the fingers: on one hand, use your thumb to count the three joints on each of the four fingers → 12 joints.',
        'This is why we still have 12 hours on a clock face, 12 inches in a foot, and dozens as a unit of sale.',
        'The practice is illustrated in the textbook to show that the base‑10 system was not the only early way of counting.',

        # 8. Algebraic properties of natural numbers: closure
        'A set is **closed** under an operation if performing that operation on any two members of the set always produces a member of the same set.',
        'Natural numbers are closed under addition: the sum of any two natural numbers is a natural number.',
        'Natural numbers are closed under multiplication: the product of any two natural numbers is a natural number.',
        'But natural numbers are **not** closed under subtraction: 4 − 5 is not a natural number (it is negative).',
        'This failure of closure eventually leads to the need for integers (which include negatives).',

        # 9. The leap from counting to arithmetic
        'Once numbers were abstracted from tokens, humans began to perform operations on them: adding, subtracting (within limits), multiplying, and eventually dividing.',
        'This transformed counting into the earliest forms of arithmetic — the foundation of all mathematics.',
    ],
    'key_points': [
        'Counting began with one‑to‑one correspondence (matching objects to tokens).',
        'Natural numbers ℕ = {1, 2, 3, …} are the counting numbers.',
        'Lebombo bone (∼35 000 years ago) — earliest known tally stick.',
        'Ishango bone (∼20 000 BCE) — notches showing possible prime numbers.',
        'Harappan civilisation used standardised weights (binary‑decimal system) for trade.',
        'Vedic literature named powers of 10 up to 10¹² (Parārdha); Buddhist texts up to 10⁵³.',
        'Base‑12 finger‑joint counting was also common.',
        'ℕ is closed under addition and multiplication, but not under subtraction.',
        'The failure of closure under subtraction leads to the extension to integers.',
    ],
    'images': [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Lebombo_bone.jpg/800px-Lebombo_bone.jpg',
            'caption': 'The Lebombo bone — baboon fibula with 29 notches, one of the oldest known mathematical artefacts (∼35 000 years old).'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Ishango_bone.jpg/800px-Ishango_bone.jpg',
            'caption': 'The Ishango bone (∼20 000 BCE) — notches arranged in columns that suggest early knowledge of prime numbers and doubling.'
        },
    ],
    'resources': {
        'videos': [
            'https://www.youtube.com/watch?v=0mIDFgXqH08',   # History of Numbers
            'https://www.youtube.com/watch?v=3gXmnTdMrv4',   # Natural Numbers and Whole Numbers
        ],
        'pdfs': [
            'https://ncert.nic.in/textbook.php?iemh1=3-19',
            'https://ncert.nic.in/textbook/pdf/iemh1-3.pdf',
        ],
        'practice': [
            'Think and Reflect: Why is one‑to‑one correspondence considered the earliest form of counting?',
            'List the first ten natural numbers. Are they closed under multiplication? Give an example.',
            'Research: Find out the Vedic name for 1,000,000,000 (10⁹). (Hint: it is also a large unit used in modern Indian numbering.)',
            'Exam‑style: Is the division of two natural numbers always a natural number? Explain with an example.',
        ],
    },
},
{
    'name': 'The Revolution of Śhūnya — The Invention of Zero',
    'overview': (
        'Zero is not just a symbol; it is one of the most profound ideas in mathematics. '
        'The concept of Śhūnya (void) began as a philosophical notion in India and later '
        'evolved into a tangible number — a symbol representing “nothing” that could be '
        'used in calculations. The Bakhśhālī manuscript shows the first known written zero, '
        'and Brahmagupta (628 CE) was the first to treat zero as a full number with rules '
        'for arithmetic. This revolution enabled the place‑value system and all of modern algebra.'
    ),
    'explanations': [
        # 1. The philosophical origin: Śhūnyatā
        'In Indian philosophy, *Śhūnya* means “void”, “emptiness”, or “nothingness”.',
        'The concept appears in early Upaniṣhads and Buddhist texts, describing the nature of reality.',
        'It was this deep philosophical background that allowed Indian mathematicians to imagine “nothing” as an entity that could be manipulated mathematically.',

        # 2. Zero as a placeholder: the Bakhśhālī manuscript
        'The Bakhśhālī manuscript (dated between 224 CE and 383 CE, discovered near Peshawar) is the oldest known Indian text containing a written zero symbol.',
        'In it, zero appears as a dot (·) used as a placeholder in the decimal place‑value system.',
        'For example, writing 305 meant 3 hundreds, 0 tens, and 5 ones — the dot held the tens place so the digits would not shift.',
        'This placeholder function of zero distinguished the number 1 from 10, 100, etc., and was essential for the base‑10 system to work properly.',

        # 3. The transition from placeholder to number
        'The key leap was to treat zero not just as an empty space or placeholder, but as a number in its own right — a number you could add, subtract, multiply, and even divide by (with care).',
        'This leap was made explicitly by Brahmagupta in the 7th century CE.',
        'Before Brahmagupta, no known mathematical text had given clear arithmetic rules for zero.',

        # 4. Brahmagupta’s rules for zero (from *Brāhmasphuṭasiddhānta*, 628 CE)
        'Brahmagupta stated: “The sum of zero and a positive number is the positive number; the sum of zero and a negative number is the negative number; the sum of zero and zero is zero.”',
        'He also gave: “A positive number subtracted from zero becomes negative; a negative number subtracted from zero becomes positive.”',
        'And crucially: “Zero multiplied by any number is zero.”',
        'Brahmagupta even attempted to define division by zero, though his rule led to further sophistication by later mathematicians.',
        'These rules were the first systematic treatment of zero as an algebraic entity.',

        # 5. The symbol for zero
        'The symbol for zero evolved from a dot (bindu) to a small circle (śūnya‑bindu) and, over time, became the 0 we use today.',
        'The circular shape likely originated in India and spread to the Arab world and then to Europe.',
        'The Arabic word “ṣifr” (meaning empty) gave rise to both “zero” and the word “cipher”.',

        # 6. Why this is so important
        'Without zero as a number, we could not have a place‑value system that uses only ten digits (0‑9).',
        'Without zero, we could not represent numbers like 2005 (two thousand and five) compactly — we would need separate symbols for each order of magnitude.',
        'Zero also plays a crucial role in algebra, calculus, and computer science — it is the identity element for addition (a + 0 = a) and the annihilator in multiplication (a × 0 = 0).',

        # 7. Exam‑oriented Q&A
        'Q1: What is the Bakhśhālī manuscript, and why is it significant? A: It is the oldest Indian manuscript with a written zero symbol (a dot), showing the use of zero as a placeholder in the decimal system.',
        'Q2: Who first formalised arithmetic rules for zero? A: Brahmagupta, in his text *Brāhmasphuṭasiddhānta* (628 CE).',
        'Q3: What are Brahmagupta’s rules for adding and multiplying with zero? A: Adding zero leaves the number unchanged; subtracting zero leaves the number unchanged; multiplying any number by zero gives zero.',
        'Q4: Why is zero considered a “revolution” in mathematics? A: Because it transformed a mere placeholder into a full number with arithmetic properties, enabling the modern place‑value system and algebra.',
        'Q5: How did the symbol for zero originate? A: It started as a dot (bindu), then a small circle, and evolved into the modern 0.',
    ],
    'key_points': [
        'Śhūnya = void, emptiness. Indian philosophy provided the conceptual basis for zero.',
        'The oldest recorded zero symbol is a dot in the Bakhśhālī manuscript (3rd–4th century CE).',
        'Zero as a placeholder distinguishes numbers like 1, 10, 100 in a place‑value system.',
        'Brahmagupta (628 CE) was the first to treat zero as a number with arithmetic rules (addition, subtraction, multiplication).',
        'Zero + a number = that number. Zero × any number = 0.',
        'The circular symbol 0 evolved from the Indian śūnya‑bindu.',
        'Zero is the additive identity: a + 0 = a.',
    ],
    'images': [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Bakhshali_manuscript.jpg/800px-Bakhshali_manuscript.jpg',
            'caption': 'A fragment of the Bakhśhālī manuscript showing a dot representing zero (placeholder). This is the oldest known written zero.'
        },
    ],
    'resources': {
        'videos': [
            'https://www.youtube.com/watch?v=pV_gXbW4LJU',   # History of Zero
            'https://www.youtube.com/watch?v=Sm2kELHkHJg',   # Brahmagupta and Zero
        ],
        'pdfs': [
            'https://ncert.nic.in/textbook.php?iemh1=3-19',
            'https://ncert.nic.in/textbook/pdf/iemh1-3.pdf',
        ],
        'practice': [
            'Think and Reflect: Why couldn’t the Romans or Greeks write the number 2005 easily? (Hint: they lacked a zero.)',
            'Explain in your own words the difference between “zero as a placeholder” and “zero as a number”.',
            'Apply Brahmagupta’s rules: compute 0 + (−7), 0 × 23, and (−5) − 0.',
            'Exam‑style: Name the mathematician who first gave rules for arithmetic with zero. Which book did he write?',
        ],
    },
},
{
    'name': 'Integers — Positive, Negative, and the Full Number Line',
    'overview': (
        'The natural numbers are not enough to describe all real‑life situations — '
        'we need negative numbers for debts, temperatures below zero, and floors below ground level. '
        'Integers extend the natural numbers by including their opposites (negatives) and zero. '
        'Brahmagupta classified integers as *Dhana* (fortunes/positives) and *Riṇa* (debts/negatives) '
        'and laid down the rules for arithmetic with them. The integer set ℤ = {…, −3, −2, −1, 0, 1, 2, 3, …} '
        'is closed under addition, subtraction, and multiplication, making it a powerful tool for calculations.'
    ),
    'explanations': [
        # 1. The need for negative numbers
        'Natural numbers (1, 2, 3, …) are fine for counting objects, but when we talk about loss, debt, or temperature below zero, we need numbers that can go below zero.',
        'For example, if the temperature is 2°C one day and drops 5°C the next, we cannot express that with natural numbers alone.',
        'Similarly, if a trader owes ₹100 more than the cash he has, his net worth is negative.',

        # 2. Brahmagupta’s classification: Dhana and Riṇa
        'Brahmagupta (628 CE) used the Sanskrit terms *Dhana* (wealth, fortune) for positive numbers and *Riṇa* (debt, liability) for negative numbers.',
        'He gave clear rules for combining them, which correspond to our modern addition and subtraction of signed numbers:',
        '   (i) A *Dhana* plus a *Dhana* is *Dhana* (positive + positive = positive)',
        '   (ii) A *Riṇa* plus a *Riṇa* is *Riṇa* (negative + negative = negative)',
        '   (iii) The sum of a *Dhana* and a *Riṇa* is their difference, with the sign of the larger magnitude.',

        # 3. Constructing the integers
        'The set of Integers is denoted by ℤ (from the German *Zahlen*, meaning numbers).',
        'ℤ = {…, −4, −3, −2, −1, 0, 1, 2, 3, 4, …}.',
        'It includes all natural numbers (positive integers), their negatives, and zero.',
        'We can think of integers as extending the number line to the left of zero by mirroring the natural numbers in the negative direction.',

        # 4. Representation on the number line
        'Draw a horizontal line. Mark a point as 0. Choose a unit distance.',
        'Mark 1, 2, 3, … to the right; mark −1, −2, −3, … to the left.',
        'Every integer has a unique position on this line.',
        'The number line helps visualise addition (moving right/left) and subtraction (moving in the opposite direction).',

        # 5. Brahmagupta’s rules for multiplication of signed numbers
        'Brahmagupta also gave rules for multiplying integers:',
        '   (i) *Dhana* × *Dhana* = *Dhana* (positive × positive = positive)',
        '   (ii) *Riṇa* × *Dhana* = *Riṇa* (negative × positive = negative)',
        '   (iii) *Riṇa* × *Riṇa* = *Dhana* (negative × negative = positive)',
        'These rules are exactly the sign rules we use today: minus × minus = plus.',
        'This was a remarkable insight, as it is not obvious why the product of two debts should be a fortune.',

        # 6. The special role of zero in integers
        'Zero is an integer and acts as the neutral element for addition: a + 0 = a, for any integer a.',
        'Zero is also the “origin” of the number line, separating positive from negative numbers.',
        'When we add an integer and its opposite, we get zero: 5 + (−5) = 0. These are called additive inverses.',

        # 7. Closure properties of integers
        'Integers are closed under addition: sum of any two integers is an integer.',
        'Integers are closed under subtraction: difference of any two integers is an integer. (This is an improvement over ℕ.)',
        'Integers are closed under multiplication: product of any two integers is an integer.',
        'Integers are **not** closed under division: 5 ÷ 2 = 2.5, which is not an integer.',
        'This failure of closure under division leads to the need for rational numbers.',

        # 8. Real‑world applications
        'Temperature: 3°C above zero is +3°C; 3°C below zero is −3°C.',
        'Altitude: Above sea level is positive; below sea level is negative.',
        'Bank balance: Deposits are positive; withdrawals/overdrafts are negative.',
        'Profit and loss: Profit → positive; loss → negative.',

        # 9. Subtracting a negative: a tricky concept explained
        'Why is 5 − (−3) = 5 + 3 = 8?',
        'Think of debts: subtracting a debt means reducing the amount you owe, which makes you richer.',
        'On the number line: subtracting −3 means “move 3 units to the right”, which is the same as adding +3.',
        'Thus, subtracting a negative integer is equivalent to adding the corresponding positive integer.',

        # 10. Exam‑oriented Q&A
        'Q1: What is an integer? A: An integer is a whole number that can be positive, negative, or zero. The set is ℤ = {…, −3, −2, −1, 0, 1, 2, 3, …}.',
        'Q2: What are Dhana and Riṇa according to Brahmagupta? A: Dhana (positive numbers) represent assets/wealth; Riṇa (negative numbers) represent debts.',
        'Q3: State the sign rule for multiplying two negative integers. A: The product of two negative integers is a positive integer. (Riṇa × Riṇa = Dhana)',
        'Q4: Is the set of integers closed under subtraction? Give an example. A: Yes. Example: 4 − 7 = −3, which is an integer.',
        'Q5: Why do we need integers if we have natural numbers? A: Natural numbers cannot express quantities less than zero (debts, temperatures below zero, losses). Integers provide that ability.',
        'Q6: Represent −5 and 3 on a number line. Which is larger? A: 3 is larger because it lies to the right of −5.',
        'Q7: Compute: (−8) + 5, (−3) − (−2), (−4) × (−6). A: −3, −1, +24.',
        'Q8: Is division of integers always an integer? Give a counterexample. A: No. Example: 5 ÷ 2 = 2.5 (not an integer).',
    ],
    'key_points': [
        'Integers ℤ = {…, −3, −2, −1, 0, 1, 2, 3, …} extend ℕ with negatives and zero.',
        'Brahmagupta (628 CE) classified them as Dhana (positive) and Riṇa (negative) and gave arithmetic rules.',
        'Addition and subtraction on the number line: right is positive, left is negative.',
        'Sign rules for multiplication: positive × positive = positive; negative × negative = positive; positive × negative = negative.',
        'Subtracting a negative is the same as adding the positive: a − (−b) = a + b.',
        'Integers are closed under addition, subtraction, multiplication; NOT under division.',
        'Zero is the additive identity: a + 0 = a. Every integer has an additive inverse (opposite).',
    ],
    'images': [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Number-line.svg/1024px-Number-line.svg.png',
            'caption': 'The number line showing integers — positive numbers to the right of 0, negatives to the left.'
        },
    ],
    'resources': {
        'videos': [
            'https://www.youtube.com/watch?v=0T2xXx_iA2g',   # Integers Class 9
            'https://www.youtube.com/watch?v=AFmH8DdSm14',   # Brahmagupta's rules for integers
        ],
        'pdfs': [
            'https://ncert.nic.in/textbook.php?iemh1=3-19',
            'https://ncert.nic.in/textbook/pdf/iemh1-3.pdf',
        ],
        'practice': [
            'Textbook Exercises 3.1, 3.2: Addition and subtraction of integers, number line representation.',
            'Think and Reflect: Why is the product of two negatives positive? Can you give a real‑life analogy?',
            'Simplify: (a) (−15) + 9, (b) 23 − (−8), (c) (−7) × (−4) × (−1).',
            'Exam‑style: A submarine is at −200 m (below sea level). It rises 75 m. What is its new depth?',
        ],
    },
},
{
    'name': 'Rational Numbers — Fractions, Number Line, and Density',
    'overview': (
        'Rational numbers arise from the need to divide a whole into parts. '
        'A rational number is any number that can be written in the form p/q, '
        'where p and q are integers and q ≠ 0. '
        'Rational numbers can be represented on the number line, and between any two '
        'rational numbers, infinitely many other rational numbers exist — this is called '
        'the density property. Methods to find numbers between two rationals include '
        'the average (mean) method, the common denominator method, and the decimal boundary method.'
    ),
    'explanations': [
        # 1. Defining rational numbers
        'A rational number is any number that can be expressed as a fraction p/q, where p and q are integers and q ≠ 0.',
        'The set of rational numbers is denoted by ℚ (from “quotient”).',
        'Examples: 3/4, −5/2, 0 (since 0 = 0/1), 7 (since 7 = 7/1).',

        # 2. Equivalent rational numbers
        'A rational number can be written in infinitely many equivalent forms: 1/2 = 2/4 = 3/6 = 50/100 = …',
        'These are equivalent because they are obtained by multiplying (or dividing) the numerator and denominator by the same non‑zero integer.',
        'The simplest form of a rational number is when the numerator and denominator have no common factor other than 1 (i.e., they are coprime).',
        'For example, 4/6 simplifies to 2/3 by dividing both by 2.',

        # 3. Representing rational numbers on the number line
        'A rational number p/q lies on the number line between integers; its position is obtained by dividing the interval between consecutive integers into q equal parts.',
        'For positive rationals: mark the integer part, then add the fractional part by subdividing.',
        'For negative rationals: mark symmetrically to the left of zero.',
        'Example: To plot 3/4, divide the segment from 0 to 1 into 4 equal parts, then mark the 3rd part.',
        'Example: To plot −5/2 = −2.5, go to −2, then halfway between −2 and −3.',

        # 4. The density property
        'The rational numbers are **dense**: between any two distinct rational numbers, there is always another rational number.',
        'This is different from “infinite” — it means you can never find two rationals that are “next to” each other; there is always one in between.',
        'Proof idea: If a and b are rational with a < b, then their average (a+b)/2 is also rational and lies strictly between them.',
        'Applying this repeatedly gives infinitely many rationals between any two.',

        # 5. Method 1: Average (mean) method
        'To find a rational number between a and b, compute (a + b)/2.',
        'Example: Between 1/3 and 1/2, compute (1/3 + 1/2)/2 = (5/6)/2 = 5/12. So 5/12 lies between them.',
        'You can repeat: find between 1/3 and 5/12, etc., generating infinitely many.',

        # 6. Method 2: Common denominator method
        'Convert a and b to fractions with the same denominator (LCM).',
        'If the numerators are not consecutive integers, you can pick any integer between them and put it over the common denominator to get a new rational.',
        'If the numerators are consecutive (like 2/6 and 3/6), multiply the fractions by a large numerator/denominator (e.g., 10) to create more space: 20/60 and 30/60, then pick 21/60, 22/60, etc.',

        # 7. Method 3: Decimal expansion boundary method
        'Write a and b as decimals to several places. Since they are rational, their decimal expansions are either terminating or eventually repeating.',
        'Insert a number that has a decimal expansion lying strictly between the two decimal boundaries.',
        'Example: Between 3.1415 and 3.1416, you can insert 3.14155, 3.141551, etc.',
        'Any terminating decimal is a rational number (e.g., 3.14155 = 314155/100000).',

        # 8. Rational numbers and measurement
        'Rational numbers are sufficient for all finite‑precision measurements: length, weight, time, etc.',
        'Any exact value of a metric measurement can be expressed as a rational number because the instruments have finite precision.',
        'But as we will see, some geometric lengths (like the diagonal of a unit square) cannot be expressed as a rational number.',

        # 9. Common mistakes
        'Mistake 1: Thinking a rational number must be a “proper fraction” — whole numbers like 4 are also rational (4/1).',
        'Mistake 2: Forgetting that denominator cannot be zero.',
        'Mistake 3: Assuming that fractions with larger denominators are always smaller in value — always compare by cross‑multiplication or decimal conversion.',
        'Mistake 4: Thinking that between two rationals there is only one rational — the density property guarantees infinitely many.',

        # 10. Exam‑oriented Q&A
        'Q1: Define a rational number. A: A number of the form p/q, where p, q are integers and q ≠ 0.',
        'Q2: Is 0 a rational number? A: Yes, 0 = 0/1.',
        'Q3: Find five rational numbers between 1 and 2. A: Many possible answers; 3/2, 5/3, 7/4, 9/5, 11/6, etc.',
        'Q4: Show that between 1/3 and 1/4 there are infinitely many rational numbers. A: Their average is 7/24; then find between 1/4 and 7/24, etc. — the process never ends.',
        'Q5: Represent −7/5 on the number line. A: −7/5 = −1.4, so it lies between −2 and −1, 4/10 of the way from −1 to −2.',
        'Q6: Convert 3.75 into p/q form. A: 375/100 = 15/4.',
        'Q7: Is the set of rational numbers closed under division? A: Not completely — division by zero is undefined. But for all non‑zero divisors, the quotient is rational.',
    ],
    'key_points': [
        'Rational numbers ℚ: p/q, p, q ∈ ℤ, q ≠ 0.',
        'Equivalent rationals obtained by multiplying/dividing numerator and denominator by the same integer.',
        'Simplest form: numerator and denominator are coprime (HCF = 1).',
        'Number line representation: subdivide intervals into equal parts.',
        'Density property: between any two rationals, there exists another rational (infinitely many).',
        'Methods to find in‑between rationals: mean method, common denominator method, decimal boundary method.',
        'Rationals include all integers and terminating/repeating decimals.',
    ],
    'images': [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Fractions_on_number_line.svg/1024px-Fractions_on_number_line.svg.png',
            'caption': 'Fractions (rational numbers) placed on the number line. The interval between integers is divided into equal parts according to the denominator.'
        },
    ],
    'resources': {
        'videos': [
            'https://www.youtube.com/watch?v=7cYMYL1u1U4',   # Rational Numbers Class 9
            'https://www.youtube.com/watch?v=BLu4N-MSCIA',   # Density of rationals
        ],
        'pdfs': [
            'https://ncert.nic.in/textbook.php?iemh1=3-19',
            'https://ncert.nic.in/textbook/pdf/iemh1-3.pdf',
        ],
        'practice': [
            'Textbook Exercises 3.3, 3.4: Plotting rationals, finding numbers between given rationals.',
            'Think and Reflect: Are rational numbers “continuous” or do they have gaps? (They have gaps, filled by irrationals.)',
            'Find 3 rational numbers between 2/5 and 3/5. Explain which method you used.',
            'Exam‑style: Write five rational numbers between −2/3 and 1/2. Which is the smallest?',
        ],
    },
},
{
    'name': 'Irrational Numbers — Proof, Construction, and the Story of π',
    'overview': (
        'Not all numbers can be expressed as a fraction of two integers. '
        'Numbers like √2, √3, and π are **irrational** — their decimal expansions go on forever without repeating. '
        'This topic provides the rigorous proof of irrationality of √2 (by contradiction), '
        'shows how to construct irrational lengths on the number line using the Baudhāyana–Pythagoras theorem, '
        'and explores the fascinating history of π and Madhava’s infinite series.'
    ),
    'explanations': [
        # 1. The discovery of incommensurable lengths
        'The ancient Greeks discovered that the diagonal of a square with side 1 could not be expressed as a ratio of whole numbers.',
        'If side = 1, by the Baudhāyana–Pythagoras theorem, diagonal = √(1² + 1²) = √2.',
        'They could not find two integers p and q such that √2 = p/q.',
        'This led to the shocking realisation that there are numbers that are not rational — they called them “incommensurable” (without common measure).',

        # 2. Definition of irrational numbers
        'A number is irrational if it cannot be written in the form p/q, where p, q are integers and q ≠ 0.',
        'Equivalently, an irrational number has a non‑terminating, non‑repeating decimal expansion.',
        'Examples: √2 ≈ 1.41421356…, √3 ≈ 1.7320508…, π ≈ 3.14159265…',

        # 3. Proof that √2 is irrational (by contradiction)
        'Step 1: Assume the opposite — that √2 is rational. Then √2 = p/q, where p, q are integers, q ≠ 0, and the fraction is in its simplest form (p and q have no common factor other than 1).',
        'Step 2: Square both sides: 2 = p² / q²  →  p² = 2q².',
        'Step 3: This means p² is even (since it equals 2 × an integer). Therefore, p must be even (because the square of an odd number is odd).',
        'Step 4: Write p = 2k, where k is an integer. Substitute: (2k)² = 2q² → 4k² = 2q² → q² = 2k².',
        'Step 5: Now q² is also even, so q must be even.',
        'Step 6: Both p and q are even, so they have a common factor 2. This contradicts our assumption that p/q is in simplest form.',
        'Step 7: The contradiction shows that our original assumption (that √2 is rational) must be false. Therefore, √2 is irrational.',
        'This proof is universally used and shows the power of logical reasoning.',

        # 4. Generalising the proof
        'The same proof structure can be used to prove that √3, √5, √6, √7, etc., are irrational, as long as the number is not a perfect square.',
        'For example, to prove √3 is irrational, assume √3 = p/q (simplest form) → 3q² = p². Then p is divisible by 3 (if p² is divisible by 3, p is divisible by 3). Substituting shows q is also divisible by 3, contradiction.',
        'This technique reinforces the method of proof by contradiction.',

        # 5. Geometric construction of irrational lengths (the square‑root spiral)
        'Irrational lengths can be constructed geometrically using the Baudhāyana–Pythagoras theorem.',
        'Start with an isosceles right triangle with legs of length 1. Its hypotenuse is √2.',
        'Now construct a right triangle with one leg = √2 and the other leg = 1. The new hypotenuse = √( (√2)² + 1² ) = √3.',
        'Continuing: add a perpendicular of length 1 each time, obtaining successive hypotenuses √4 (=2), √5, √6, … — this spiral is called the square‑root spiral (or Theodorus spiral).',
        'This shows that irrational numbers correspond to actual geometric lengths, even though they are not rational.',

        # 6. The story of π (pi)
        'π is defined as the ratio of a circle’s circumference to its diameter.',
        'Measurements give approximate rational values like 22/7 or 3.14, but these are only approximations.',
        'π is an irrational number: its decimal expansion never terminates and never repeats (it is also transcendental, a stronger property).',
        'Indian mathematician Madhava of Sangamagrama (c. 14th century) discovered an infinite series that gives π to any desired accuracy: π/4 = 1 − 1/3 + 1/5 − 1/7 + 1/9 − … (the Leibniz‑Madhava series).',
        'This series shows that π can be expressed as the sum of infinitely many rational numbers, even though π itself is irrational.',

        # 7. Distinguishing rational from irrational
        'If a decimal terminates (e.g., 0.25) or repeats cyclically (e.g., 0.333…), the number is rational.',
        'If a decimal goes on forever without any repeating pattern, it is irrational.',
        'However, proving irrationality requires a logical argument, not just looking at a few decimal places.',

        # 8. Common mistakes
        'Mistake 1: Assuming √4 is irrational. No, √4 = 2, which is rational. Irrationality only applies when the number is not a perfect square.',
        'Mistake 2: Using 22/7 as exact value of π — it is only an approximation.',
        'Mistake 3: In the proof of irrationality, forgetting to mention that p/q is in simplest form (co‑prime). This step is crucial for the contradiction.',
        'Mistake 4: Thinking that all non‑terminating decimals are irrational — repeating non‑terminating decimals are rational.',

        # 9. Exam‑oriented Q&A
        'Q1: Define irrational numbers. A: Numbers that cannot be expressed as p/q (p, q integers, q ≠ 0). Their decimal expansion is non‑terminating and non‑repeating.',
        'Q2: Prove that √2 is irrational. A: (Give the full contradiction proof as above.)',
        'Q3: Is √(25) irrational? A: No, √25 = 5, which is rational.',
        'Q4: How do you construct √5 on the number line? A: Use the square‑root spiral: after obtaining √4 (which is 2), draw a perpendicular of 1 unit at the point representing √4. The new hypotenuse will be √5. Transfer this length to the number line using a compass.',
        'Q5: Is π rational? A: No, π is irrational. Its decimal expansion is infinite and non‑repeating.',
        'Q6: Who discovered the infinite series for π in India? A: Madhava of Sangamagrama (14th century).',
        'Q7: Give an example of an irrational number between 1 and 2. A: √2 ≈ 1.414, or √3 ≈ 1.732.',
    ],
    'key_points': [
        'Irrational numbers cannot be written as p/q; decimal expansions are non‑terminating and non‑repeating.',
        'Proof that √2 is irrational uses contradiction: assume √2 = p/q (simplest form), then p and q both even → contradiction.',
        'Same method proves √3, √5, etc., irrational (if not perfect squares).',
        'Irrational lengths can be constructed geometrically using the Baudhāyana–Pythagoras theorem (square‑root spiral).',
        'π is irrational; Madhava’s infinite series: π/4 = 1 − 1/3 + 1/5 − 1/7 + …',
        'Repeating non‑terminating decimals are rational; non‑repeating ones are irrational.',
        'Irrational numbers fill the “gaps” between rationals on the number line.',
    ],
    'images': [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Square_root_spiral.svg/1024px-Square_root_spiral.svg.png',
            'caption': 'The square‑root spiral (Theodorus spiral) — each successive right triangle with a unit leg produces hypotenuses of lengths √2, √3, √4, √5, …'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Pi-unrolled-720.gif/800px-Pi-unrolled-720.gif',
            'caption': 'Pi (π) is the constant ratio of a circle\'s circumference to its diameter — an irrational number that cannot be expressed exactly as a fraction.'
        },
    ],
    'resources': {
        'videos': [
            'https://www.youtube.com/watch?v=2vNWbY8DCNE',   # Proof that √2 is irrational
            'https://www.youtube.com/watch?v=FEnUojjLnbQ',   # Square root spiral construction
            'https://www.youtube.com/watch?v=1-JxESMftII',   # History of π and Madhava series
        ],
        'pdfs': [
            'https://ncert.nic.in/textbook.php?iemh1=3-19',
            'https://ncert.nic.in/textbook/pdf/iemh1-3.pdf',
        ],
        'practice': [
            'Textbook Exercises 3.5: Prove irrationality of √3, √5; construct square‑root spiral.',
            'Think and Reflect: Can an irrational number be negative? Give an example. (Yes, e.g., −√2.)',
            'Prove that √7 is irrational using the method of contradiction.',
            'Exam‑style: Show that (3 + √5) is irrational. (Hint: assume it is rational and derive a contradiction.)',
        ],
    },
},
{
    'name': 'Real Numbers — Decimal Expansions and the Real Number Line',
    'overview': (
        'Rational and irrational numbers together form the set of **Real Numbers** (ℝ). '
        'Every real number has a decimal expansion: for rational numbers, it either terminates '
        'or eventually repeats in a cycle; for irrationals, it never repeats. '
        'This topic explores the classification of decimal expansions, algebraic conversion '
        'of repeating decimals to p/q form, the intriguing cyclic behaviour of fractions '
        'like 1/7, and the complete real number line where every point corresponds to a real number.'
    ),
    'explanations': [
        # 1. The set of real numbers
        'Real numbers include all rational numbers (ℚ) and all irrational numbers.',
        'The symbol is ℝ. Often visualised as the entire number line, with no gaps.',
        'Every point on the number line corresponds to a unique real number, and every real number has a unique point.',
        'This is called the **completeness** of the real line — it is a continuous, unbroken line.',

        # 2. Decimal expansion of rational numbers
        'When we convert a rational number p/q into decimal by long division, two things can happen:',
        '   (a) The division terminates (remainder becomes 0). Example: 1/8 = 0.125.',
        '   (b) The division never terminates, but the digits repeat in a cycle. Example: 1/3 = 0.333… (repeating block “3”).',
        'If the denominator (in simplest form) has only prime factors 2 and/or 5, the decimal expansion terminates.',
        'If the denominator has any prime factor other than 2 or 5, the decimal expansion is non‑terminating repeating.',
        'Thus, rational numbers correspond exactly to terminating or non‑terminating repeating decimals.',

        # 3. Converting a terminating decimal to fraction
        'A terminating decimal like 0.375 is simply 375/1000, which simplifies to 3/8.',
        'General rule: write the decimal as a fraction with denominator a power of 10, then simplify.',

        # 4. Converting a pure repeating decimal to fraction
        'Example 1: 0.\overline{6} = 0.666…',
        'Let x = 0.666…',
        'Multiply by 10: 10x = 6.666…',
        'Subtract: 10x − x = 6.666… − 0.666… → 9x = 6 → x = 6/9 = 2/3.',
        'This method uses algebra to eliminate the repeating block.',
        'General rule for a repeating block of length n: multiply by 10ⁿ, then subtract the original equation.',

        # 5. Converting a mixed repeating decimal
        'Example: 0.4\overline{7} = 0.4777… (only the 7 repeats).',
        'Let x = 0.4777…',
        'Multiply by 10: 10x = 4.777…',
        'Multiply by 100: 100x = 47.777…',
        'Subtract the first from the second: 100x − 10x = 47.777… − 4.777… → 90x = 43 → x = 43/90.',
        'The trick is to align the repeating parts before subtracting.',

        # 6. The fascinating cycle of 1/7
        '1/7 = 0.\overline{142857} — a block of 6 digits repeats forever.',
        'Multiples of 1/7 give cyclic permutations of the same block:',
        '   2/7 = 0.\overline{285714}',
        '   3/7 = 0.\overline{428571}',
        '   4/7 = 0.\overline{571428}',
        '   5/7 = 0.\overline{714285}',
        '   6/7 = 0.\overline{857142}',
        'This cyclic nature occurs because 7 is a prime and 10 is a primitive root modulo 7.',
        'This property makes 1/7 a favourite in number theory and can be used to predict digits without long division.',
        'A similar cyclic property is seen with 1/13 (a 6‑digit repeating cycle, but not a pure cyclic permutation for all multiples).',

        # 7. Decimal expansion of irrational numbers
        'Irrational numbers have decimal expansions that never terminate and never repeat.',
        'For example, √2 = 1.414213562373095048801688724209… — no repeating pattern emerges.',
        'π = 3.141592653589793238462643383279… — also non‑repeating.',
        'Because of this, we cannot write irrationals as a fraction of two integers; they are infinite and non‑periodic.',

        # 8. Properties of real numbers
        'Real numbers obey the familiar arithmetic laws:',
        '   Closure: Sum or product of two reals is a real.',
        '   Commutative: a + b = b + a, ab = ba.',
        '   Associative: (a + b) + c = a + (b + c), (ab)c = a(bc).',
        '   Distributive: a(b + c) = ab + ac.',
        'These properties make the real numbers a **field**.',

        # 9. The real number line
        'The real number line is a continuous line where every point corresponds to a unique real number.',
        'Rational numbers are scattered densely, but there are still “holes” — those holes are filled by irrational numbers.',
        'Together, the rationals and irrationals make the line complete.',
        'When we draw the number line, we are implicitly assuming the existence of both rational and irrational numbers.',

        # 10. Common mistakes
        'Mistake 1: Thinking that all non‑terminating decimals are irrational — repeating ones are rational.',
        'Mistake 2: Confusing “terminating” with “finite” — the decimal representation of a rational may be infinite but still periodic.',
        'Mistake 3: Forgetting to simplify the fraction obtained from converting decimals to p/q form.',
        'Mistake 4: Misapplying the cyclic pattern of 1/7 — it works only for 7, not all primes.',

        # 11. Exam‑oriented Q&A
        'Q1: What is a real number? A: Any number that is either rational or irrational. The set ℝ includes all numbers on the number line.',
        'Q2: How can you tell if a decimal expansion is rational? A: If it terminates or repeats (eventually).',
        'Q3: Convert 0.\overline{12} to p/q form. A: x = 0.1212…, 100x = 12.1212… → 99x = 12 → x = 12/99 = 4/33.',
        'Q4: Without dividing, predict the decimal expansion of 3/7 using the cyclic property. A: 3/7 = 0.\overline{428571}.',
        'Q5: Is 0.101001000100001… rational? A: No, because the pattern does not repeat; it is an irrational number.',
        'Q6: State the closure property of real numbers for addition. A: The sum of any two real numbers is a real number.',
        'Q7: Why is √2 a real number? A: Because it corresponds to a specific point on the number line (the diagonal of a unit square).',
    ],
    'key_points': [
        'Real numbers ℝ = ℚ ∪ {irrationals}. Every point on the number line is a real number.',
        'Rational decimal expansions are terminating or non‑terminating repeating.',
        'Irrational decimal expansions are non‑terminating and non‑repeating.',
        'Converting repeating decimals to fractions: use algebraic elimination of the repeating block.',
        'Cyclic fractions like 1/7 = 0.\overline{142857} — multiples of 1/7 are cyclic permutations.',
        'Real numbers obey closure, commutativity, associativity, and distributivity.',
        'The number line is complete and continuous because of the real numbers.',
    ],
    'images': [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Real_number_line.svg/1024px-Real_number_line.svg.png',
            'caption': 'The real number line — every point is a real number. Rationals are dense, and irrationals fill the gaps to make it continuous.'
        },
    ],
    'resources': {
        'videos': [
            'https://www.youtube.com/watch?v=lBhsF-XlLZI',   # Converting repeating decimals to fractions
            'https://www.youtube.com/watch?v=Wz5MvWbCbhg',   # Cyclic fractions 1/7 magic
        ],
        'pdfs': [
            'https://ncert.nic.in/textbook.php?iemh1=3-19',
            'https://ncert.nic.in/textbook/pdf/iemh1-3.pdf',
        ],
        'practice': [
            'Textbook Exercises 3.6: Convert recurring decimals to fractions, explore cyclic patterns of 1/13.',
            'Think and Reflect: Why is the decimal expansion of 1/7 cyclic, but 1/8 is terminating?',
            'Convert 0.2\overline{35} to p/q form.',
            'Write the decimal expansion of 5/7 using the cyclic property of 1/7.',
            'Exam‑style: Prove that 0.1010010001… (with increasing number of zeros) is irrational.',
        ],
    },
}
                ]
            },
            'Co-Ordinate Geometry': {
                'topics': [
                    {
                        'name': 'Polynomials',
                        'overview': 'Understanding polynomials, degrees, and basic operations',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    },
                    {
                        'name': 'Linear Equations in Two Variables',
                        'overview': 'Solving linear equations with two variables',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Euclidean Geometry': {
                'topics': [
                    {
                        'name': 'Polynomials',
                        'overview': 'Understanding polynomials, degrees, and basic operations',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    },
                    {
                        'name': 'Linear Equations in Two Variables',
                        'overview': 'Solving linear equations with two variables',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Lines and Angles': {
                'topics': [
                    {
                        'name': 'Polynomials',
                        'overview': 'Understanding polynomials, degrees, and basic operations',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    },
                    {
                        'name': 'Linear Equations in Two Variables',
                        'overview': 'Solving linear equations with two variables',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Triangles': {
                'topics': [
                    {
                        'name': 'Polynomials',
                        'overview': 'Understanding polynomials, degrees, and basic operations',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    },
                    {
                        'name': 'Linear Equations in Two Variables',
                        'overview': 'Solving linear equations with two variables',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Quadrilaterals': {
                'topics': [
                    {
                        'name': 'Polynomials',
                        'overview': 'Understanding polynomials, degrees, and basic operations',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    },
                    {
                        'name': 'Linear Equations in Two Variables',
                        'overview': 'Solving linear equations with two variables',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Circles': {
                'topics': [
                    {
                        'name': 'Polynomials',
                        'overview': 'Understanding polynomials, degrees, and basic operations',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    },
                    {
                        'name': 'Linear Equations in Two Variables',
                        'overview': 'Solving linear equations with two variables',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Heron"s Formula': {
                'topics': [
                    {
                        'name': 'Polynomials',
                        'overview': 'Understanding polynomials, degrees, and basic operations',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    },
                    {
                        'name': 'Linear Equations in Two Variables',
                        'overview': 'Solving linear equations with two variables',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Surface Area and Volume': {
                'topics': [
                    {
                        'name': 'Polynomials',
                        'overview': 'Understanding polynomials, degrees, and basic operations',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    },
                    {
                        'name': 'Linear Equations in Two Variables',
                        'overview': 'Solving linear equations with two variables',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Statistics': {
                'topics': [
                    {
                        'name': 'Polynomials',
                        'overview': 'Understanding polynomials, degrees, and basic operations',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    },
                    {
                        'name': 'Linear Equations in Two Variables',
                        'overview': 'Solving linear equations with two variables',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            }
        }
    },
    'Chemistry': {
        'chapters': {
            'Matter in Our Surroundings': {
                'topics': [
                    {
                        'name': 'States of Matter',
                        'overview': 'Solid, liquid, and gas - understanding properties',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    },
                    {
                        'name': 'Change of State',
                        'overview': 'Temperature and pressure effects on matter',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Is Matter Around Us Pure?': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Atoms and Molecules': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Structure of the Atom': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
        }
    },
    'Physics': {
        'chapters': {
            'Motion': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Force and Laws of Motion': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Gravitation': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Work and Energy': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Sound': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
        }
    },
    'Biology': {
        'chapters': {
            'Fundamental Unit of Life': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Tissues': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Improvement in Food Resoures': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            }
        }
    },
    'History': {
        'chapters': {
            'The French Revolution': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Socialism in Europe and the Russian Revolution': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Nazism and the Rise of Hitler': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Pastoralists in the Modern World - Only Periodic Assessment': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            }
        }
    },
    'Geography': {
        'chapters': {
            'India - Size and Location': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Physical Features of India': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Drainage': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Climate': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Population': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            }
        }
    },
    'Political Science': {
        'chapters': {
            'What is Democracy? Why Democracy?': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Constitutional Design': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Electoral Politics': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            },
            'Working of Institution': {
                'topics': [
                    {
                        'name': 'Distance and Displacement',
                        'overview': 'Understanding scalar and vector quantities',
                        'resources': {
                            'videos': [],
                            'pdfs': [],
                            'practice': []
                        }
                    }
                ]
            }
        }
    }
}
