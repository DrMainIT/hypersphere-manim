from manim import *

class ColorfulSphere(ThreeDScene):
    def construct(self):
        # Set the camera orientation to display the top of the sphere
        # Number of circles that will compose the sphere
        num_circles = 20
        
        # Generate a list of colors for the circles
        colors = color_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE], num_circles)
        vertical_offset = 0.1
        initial_circles = VGroup()
        # Create circles at different angles, with varying radii and colors
        for i in range(num_circles):
            # Latitude angle (from -PI/2 to PI/2)
            theta = PI * (i / num_circles - 0.5)
            # Radius of the circle decreases as we move up or down the sphere
            radius = np.cos(theta)
            # Create the circle with varying radius and color
            circle = Circle(radius=radius, color=colors[i], stroke_width=3)
            circle.shift(UP * vertical_offset * i)
            # Add the circle to the scene
            initial_circles.add(circle)
        self.add(initial_circles)
        self.wait(5)
        
        target_circles = VGroup()
        #create a circle near the sphere to show the sphere is 3D
        for i in range(num_circles):
            # Latitude angle (from -PI/2 to 0)
            theta = PI * (i / num_circles - 0.5)
            # Radius of the circle decreases as we move up or down the sphere
            radius = np.cos(theta)
            # Create the circle with varying radius and color
            circle = Circle(radius=radius, color=colors[i], stroke_width=3)
            # Add the circle to the scene
            target_circles.add(circle)

        self.play(Transform(initial_circles, target_circles), run_time=3)
        # Animate the scene (optional)
        self.wait(2)


class GrowingAndShrinkingSpheres(ThreeDScene):
    def construct(self):
        #set the camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        # Create a list to hold all spheres
        spheres = VGroup()

        # Create 10 spheres with increasing radii over time
        num_spheres = 3
        initial_radius = 0.3
        

        # Calculate the radius for each sphere
        radius = initial_radius
        # Create a sphere with a specific radius
        sphere = Sphere(radius=radius, color=BLUE, stroke_width=1)
        spheres.add(sphere)
        
        # Add all the spheres to the scene
        self.add(spheres)

        # Animate the spheres growing and shrinking
        self.play(spheres.animate.scale(5), run_time=3)  # Make the spheres grow
        self.play(spheres.animate.scale(0.3), run_time=3)  # Then shrink them back

        self.wait(2)

