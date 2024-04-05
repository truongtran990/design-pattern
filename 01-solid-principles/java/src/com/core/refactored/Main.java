package com.core.refactored;

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

            // we have the compiler error here because the hasEngine() 
            // method is not defined in the Vehicle class => so we can not perform this operation
            // System.out.println("Has engine: " + vehicle.hasEngine().toString());
            System.out.println();
        }
    }
}
