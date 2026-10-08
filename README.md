This is the upgraded version (V2.0) of my Smart Rover project. In the first version, the rover had limited vision (4 steps ahead) which causes the clone to be half blind . And clones were not sharing information with each other . 
But in this version (V2.0) clones share information with each other and this reduces the RAM usage . Because they dont visit the same place . Every clone visits different coordinates . 
Instead of calculating the route once and blindly following it, the rover recalculates the shortest path at every single step. It clears its memory, looks around from its new position, and plans again. This makes the system "future-proof" against dynamic obstacles.
I fixed a "teleportation" bug where the rover was moving to the target instantly in a for loop. Now it takes only the first step of the calculated route (selected_route[0]), making it a real-time simulation.
To test the limits of my algorithm , I asked AI to produce me a Map Generator . So the Map Generator inside this code was made by AI . 

Like the first version, I used no extra libraries. The entire logic is built from scratch using basic Python tools, lists, and dictionaries.

Rover: 🤖
Visited (Rover's path): 👣
Target: 🎯
Obstacles: ⬛
Empty Space: ⬜
