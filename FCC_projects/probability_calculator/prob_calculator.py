import copy
import random
# Consider using the modules imported above.


class Hat:

    # This method creates an empty list and then adds all the keys in the dictionary the number of times their value.
    def __init__(self, **kwargs):
        self.contents = []
        if kwargs:
            for key, value in kwargs.items():
                self.contents.extend([key] * value)

    # this method takes a number and chooses a random item from the contents list and adds that item to a new list and then removes it from the contents list
    def draw(self, amount):
        draws = []
        for i in range(amount):
            if self.contents:
                item = random.choice(self.contents)
                draws.append(item)
                self.contents.remove(item)
            else:
                return draws

        return draws

# this function takes 4 arguments and returns a probability
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    # a count variable that keeps track of the draws
    ball_draw_count = 0

    # this creates a list of the expected balls' keys
    colors = list(expected_balls.keys())

    # loop through the range, using the number of experiments as an arg
    for i in range(num_experiments):

        # using the Hat object initialization method
        if hat.contents:

            # create a copy of the hat instance
            hat_copy = copy.deepcopy(hat)

            # using the draw method, to select a random number of balls
            draw_ = hat_copy.draw(num_balls_drawn)

            # loop through the colors to count the number of balls drawn
            actual_balls_drawn = [draw_.count(color) for color in colors]

            # a list of the values of the expected balls dictionary
            draws_list = list(expected_balls.values())

            # checks if balls drawn is more than or equal to the values of the expected balls dictionary and increments the ball draw counts
            if (actual_balls_drawn >= draws_list):
                ball_draw_count += 1

    # this returns the probability
    return ball_draw_count / num_experiments