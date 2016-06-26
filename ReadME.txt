KBE Tail Sizing Project

27/06/2016

By: Andrea Mancini - Jacopo Zamboni


This application gives the user a tool for rapid iterations of conventional designs with particular focus on the design and analysis of the tail.
The user interface is flexible and permits to import both .json and .xlsm files as inputs.
Moreover, all the inputs can be manipulated via Parapy's GUI.
The application gives the necessary warnings when an unfeasible design or geometry is created.
In particular, this application gives the user a tool for rapid design of three different kinds of tails: T tail, conventional and cruciform.

Application use:

1) Launch aircraft.py and wait for the GUI to appear.
2) Double click on any part to show the related geometry. The first time, a pop-up window will ask the user to open an input document.
   The user can choose between .json, .xlsm files or hit cancel. The application will automatically search for the required inputs in the given file.
   If the variable or its value are not found, the application will use a default value and warn the user via LOG.
3) The user is free to change the input values in order to produce a new design. In particular, the user can manipulate:
    3.1) Fuselage: basic dimensions. The application automatically calculates the tail divergence angle.
    3.2) Wing: taper ratio, t/c ratio, surface, airfoils and other parameters and parts of the wing can be chosen.
         It is possible to run xFoil analysis at the desired span location.
    3.3) Vertical and horizontal tail: the volume coefficients and tail type can be set in order to find a design that satisfies
          the constrains posed by the Htp wake and wing wake.
    3.4) Landing gear: landing gear height, wheel radius, lateral and longitudinal position can be set.
         The application analysis if the inputs satisfy constraints such as the tipback angle, lateral clearance angle and minimum lateral constraint.
    3.5) Engines: several parameters can be used to obtain a realistic geometry of an engine and its position on the wing or attached to the fuselage.
    3.6) Evaluations: this module automatically calculated the CG, aerodynamic center, the wing areas of interest (reference, wetted and exposed) and the main aerodynamic coefficients.
4) Once the user is satisfied with the result, the application can automatically generate an output file with all the inputs and the main attributes.
   The application can also generate a STEP file that can be easily imported in a CAD application.



