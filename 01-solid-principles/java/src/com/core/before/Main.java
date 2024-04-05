package com.core.before;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Vehicle> vehicles = new ArrayList<>();
        vehicles.add(new Car());
        vehicles.add(new MotorCycle());
        vehicles.add(new BikeCycle());

        for (Vehicle vehicle : vehicles) {
            System.out.println("Number of wheels: " + vehicle.getNumOfWheel());
            System.out.println("Has engine: " + vehicle.hasEngine().toString());
            System.out.println();
        }
    }
}

// // Before
// abstract class Vehicle {
// public abstract int getNumOfWheel();

// public abstract boolean hasEngine();
// }

// class Car extends Vehicle {
// public int getNumOfWheel() {
// return 4;
// }

// public boolean hasEngine() {
// return true;
// }
// }

// class Motorbike extends Vehicle {
// public int getNumOfWheel() {
// return 2;
// }

// public boolean hasEngine() {
// return true;
// }
// }

// class Bike extends Vehicle {
// public int getNumOfWheel() {
// return 2;
// }

// public boolean hasEngine() {
// throw new InternalError("Bike does not have an engine");
// }

// }
