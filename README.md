# KTHFS Driverless - Exercises

Detta repository innehåller lösningar för Exercise 1 och Exercise 2 för KTH Formula Student Driverless.

---

## Exercise 1: ROS 2 Network

Två ROS 2 noder i Python (`rclpy`):
* `package1` (`nodeA`): Publicerar heltalet k med en frekvens på 20 Hz på topic `nader`. Talet ökar med n = 4 per iteration.
* `package2` (`nodeB`): Prenumererar på topic `nader`, skalar värdet med q = 0.15 och publicerar resultatet som `Float64` på `/kthfs/result`.

### Köra från noll med Docker (Windows / Mac / Linux)

Om man inte har Ubuntu eller ROS 2 installerat lokalt körs noderna smidigast via Docker Desktop.

#### 1. Förberedelser
1. Ladda ner och starta [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Klona eller ladda ner detta repository till din dator.

#### 2. Starta ROS 2 Jazzy Containern
Öppna PowerShell eller en terminal på din dator och kör:

` docker run -it --name ros_jazzy osrf/ros:jazzy-desktop /bin/bash `

3. 
Öppna ett nytt terminalfönster och kör:
` docker exec ros_jazzy mkdir -p /root/kthfs_ws/src `

# Kopiera in paketen från lokala mapp till containerns src
` docker cp ./exercise1/package1 ros_jazzy:/root/kthfs_ws/src/ `

` docker cp ./exercise1/package2 ros_jazzy:/root/kthfs_ws/src/ `

4.
container-terminalen (där prompten visar root@...), kör följande:

` cd /root/kthfs_ws `

` source /opt/ros/jazzy/setup.bash `

` colcon build --symlink-install `

` source install/setup.bash `

5. Kör noderna i tre terminaler
Öppna 4 separata terminaler på din dator och anslut till containern:

Terminal 1 (Kör NodeA):


` docker exec -it ros_jazzy /bin/bash `

` source /opt/ros/jazzy/setup.bash `

` source ~/kthfs_ws/install/setup.bash `

` ros2 run package1 nodeA `

Terminal 2 (Kör NodeB):


` docker exec -it ros_jazzy /bin/bash `

` source /opt/ros/jazzy/setup.bash `

` source ~/kthfs_ws/install/setup.bash `

` ros2 run package2 nodeB `


Terminal 3 (Verifiera data & 20 Hz):

` docker exec -it ros_jazzy /bin/bash `

` source /opt/ros/jazzy/setup.bash `

` source ~/kthfs_ws/install/setup.bash `

` ros2 topic hz /nader ` 

` ros2 topic echo /kthfs/result `

Terminal 3.1 (Verifiera data & 20 Hz):
` docker exec -it ros_jazzy /bin/bash `

` source /opt/ros/jazzy/setup.bash `

` source ~/kthfs_ws/install/setup.bash ` 

` ros2 topic echo /kthfs/result `


------------------------------------------------------------------

## Exercise 2: Data Visualisation

# Installera bibliotek
pip install numpy matplotlib

# Kör skriptet
python ex2.py
