// Write a program that calculates the occupancy rate for a hostel. The program should start by asking the user how many floors the hostel has. A for loop should then iterates once for each floor. In each iteration, the loop should ask the user for number of rooms on the floor and how many of them are occupied. After all the iterations, the program should display how many rooms the hostel has, how many of them are occupied, how many are unoccupied, and the percentage of rooms that are occupied.

import java.util.*;
public class ssn {
    public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the number of floors in the hostel");
    int floors=sc.nextInt();
    int floor=1;
    int[][] rooms=new int[floors][3];
    for (int i = 0; i < rooms.length; i++) {
        for (int j = 0; j < rooms[0].length; j++) {
            if(j==0){
                rooms[i][j]=floor++;
            }
            else if(j==1){
                System.out.println("Enter the number of rooms on floor "+rooms[i][0]);
                rooms[i][j]=sc.nextInt();
            }
            else if(j==2){
                System.out.println("Enter the number of rooms occupied on floor "+rooms[i][0]);
                rooms[i][j]=sc.nextInt();
            }
            }
        }
    int totalRooms=0;
    int totalOccupied=0;
    int unoccupied=0;
    for(int i=0;i<floors;i++){
        totalRooms+=rooms[i][1];
        totalOccupied+=rooms[i][2];
        unoccupied+=rooms[i][1]-rooms[i][2];


    }
    System.out.println("Total rooms in the hostel: "+totalRooms);
    System.out.println("Total rooms occupied in the hostel: "+totalOccupied);
    System.out.println("Total rooms unoccupied in the hostel: "+unoccupied);
    System.out.println("Percentage of rooms occupied in the hostel: "+(totalOccupied*100)/totalRooms+"%");
    }
    
}


