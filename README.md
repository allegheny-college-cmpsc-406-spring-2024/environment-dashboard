# Environment Dashboard Lab

**Completing all objectives in this assignment will earn you one point each for sensing, circuitry, data analysis and visualization, and inter-device communication**. This assignment covers all IoT [Course Learning Outcomes](https://github.com/allegheny-college-cmpsc-406-spring-2024/course-materials?tab=readme-ov-file#course-learning-outcomes).

As you work, be sure to copy, paste, and commit your Pico code regularly to `build/main.py` in this repo. The grader will check for at least three commits.

## Steps

### Step One: Use your Pico and a BME 280 to create a cloud dashboard measuring temperature, humidity, and barometric pressure

[Follow this tutorial](https://www.hivemq.com/blog/iot-reading-sensor-data-raspberry-pi-pico-w-micropython-mqtt-node-red/) to complete step one, but **before you begin take note of the caveats below**. This is NOT a very clear piece of documentation. Working with it is a good exercise in working with limited online resources.

### Caveats

- You will have already completed some of the necessary steps in the last Pico assignment.
- The MQTT library listed in the assignment is buggy. Instead, you'll use `micropython-mqtt`:
  - Save [this file](https://github.com/peterhinch/micropython-mqtt/blob/master/mqtt_as/mqtt_as.py) to the `lib` directory on your pico
  - Adapt your code using [this documentation](https://github.com/peterhinch/micropython-mqtt/blob/master/mqtt_as/README.md#8-hive-mq)
- We will be using Flask rather than NODE-RED to create our dashboards. When you get to this step, talk to professor. 

### Step Two: Add the onboard temp sensor to your dashboard

Reference the [Pico Sockets](https://github.com/allegheny-college-cmpsc-406-spring-2024/pico-sockets) assignment in reading from the onboard temperature sensor. Add this sensor to your IoT cloud dashboard on HiveMQ.

### Step Three: Add another sensor to the Pico and your dashboard.

Choose one more external sensor. Talk to your professor about available sensors — there are enough for everyone, but specific modules are first come, first served! If there is a sensor you really want you can ask about it before you start working.

Do independent research to figure out how to connect your sensor and add it to your IoT cloud dashboard.

### Step Four: Document your work

Make sure your code in `build/main.py` is up to date. Add images and writing as instructed to `docs/report.md`.
