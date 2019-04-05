# Python Facial Recognition

A repo of practice with Python's Facial Recognition library. Some of this is done with terminal commands in a virtual environment.

### Usage

- Make sure that you have the most up to date version of Python and the package manager pip installed.
- Make sure that you have `$ pipenv` installed by using `$ pip install pipenv` from the terminal.
- Use command `$ pipenv shell` to start virtual environment.
- Once working in the virtual environment, run command `$ pipenv install face_recognition` (If there is an error during installation, run `$ pip install cmake`, and then run command `$ pip --no-cache-dir install face_recognition`).
- Happy coding!~

### How it Works
Using the command line, we compare the unknown images in our unknown folder against the folder of known images to see if they are similar in structure using the command `$ face_recognition ./img/known ./img/unknown`, and displays what person that image matches, or if it is an `unknown_person`.

![Unknown Persons](./img\screenshots\detection.png)

![Detected Persons](./img\screenshots\unknown.png)

We can even see how it performs against lookalikes, and see the distance between how similar one face in a picture is to another by adding the flag `--show-distance true` to our command.