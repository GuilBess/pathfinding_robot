def calibrate_rotate(self):
        TR = TRSensor()
        self.left()
        time.sleep(1)
        TR.calibrate()
        self.stop()

        print("Max : ", TR.calibratedMax)
        print("Min : ", TR.calibratedMin)

        time.sleep(2)
        self.right(15)

        sensor = TR.readCalibrated()
        print(sensor[2])
        while sensor[2] > 900:
            sensor = TR.readCalibrated()
        print("we are set")

        self.stop()
        
        time.sleep(2)

        t = time.time()
        #self.right()
        sensor = TR.readCalibrated()
        print(sensor[2])
        while sensor[2] < 100: # From bot wiki, black -> ~100-300, white -> ~800-900
            print(sensor[2])
            sensor = TR.readCalibrated()
        print("out of black")
        print(sensor[2])
        time.sleep(0.05)
        while sensor[2] > 900:
            sensor = TR.readCalibrated()
        print("back on black")
        t1 = time.time() - t
        #self.stop()
        time.sleep(2)
        
        #self.left(15)
        while sensor[2] > 900:
            sensor = TR.readCalibrated()
        #self.stop()
        time.sleep(2)

        t = time.time()
        #self.right()
        while sensor[2] < 100:
            sensor = TR.readCalibrated()
        print("out of black2")
        while sensor[2] > 900:
            sensor = TR.readCalibrated()
        print("back on black2")
        while sensor[2] < 100:
            sensor = TR.readCalibrated()
        print("out of black3")
        while sensor[2] > 900:
            sensor = TR.readCalibrated()
        print("back on black3")
        t2 = time.time() - t

        print(f"t1: {t1}, t2: {t2}")