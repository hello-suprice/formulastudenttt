'''
NodeA Publisher
KTH Formula Student Driverless - Exercise 1

Syfte:
Publicerar ett heltal k med frekvensen 20 Hz på topic 'nader'.
k ökar med n = 4 för varje iteration.

Huvuddelar:
1. Initiering av publisher och timer (20 Hz)
2. Callback som inkrementerar och skickar k
3. Spin-loop och ren nedstängning
'''

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64


class NodeA(Node):

    def __init__(self):
        # Initiera noden med namnet 'nodeA'
        super().__init__('nodeA')

        # Skapa publisher: (Meddelandetyp, Topic-namn, Köstorlek)
        self.publisher_ = self.create_publisher(Int64, 'nader', 10)

        # Startvärde k och stegstorlek n = 4
        self.k = 0
        self.n = 4

        # 20 Hz innebär ett intervall på 1 / 20 = 0.05 s
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info('NodeA startad. Publicerar på topic: nader (20 Hz)')

    def timer_callback(self):
        '''Körs var 0.05:e sekund för att publicera och räkna upp k.'''
        msg = Int64()
        msg.data = self.k
        self.publisher_.publish(msg)

        self.get_logger().info(f'Publicerar k = {self.k}')

        # Inkrementera k med n inför nästa loop
        self.k += self.n


def main(args=None):
    rclpy.init(args=args)
    node = NodeA()

    try:
        # Håll noden vid liv och hantera callbacks
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # Stäng ner nod och frigör resurser
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
