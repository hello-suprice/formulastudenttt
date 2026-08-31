'''
NodeB Processing Node
KTH Formula Student Driverless - Exercise 1

Syfte:
Lyssnar på heltal k från topic 'nader', beräknar resultatet k / q
där q = 0.15, och publicerar float-värdet på topic '/kthfs/result'.

Huvuddelar:
1. Initiering av subscription ('nader') och publisher ('/kthfs/result')
2. Callback för skalning (k / 0.15) och vidarebefordran
3. Spin-loop och säker avstängning
'''

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64, Float64


class NodeB(Node):

    def __init__(self):
        # Initiera noden med namnet 'nodeB'
        super().__init__('nodeB')

        # Skapa subscriber för att lyssna på topic 'nader'
        self.subscription = self.create_subscription(
            Int64,
            'nader',
            self.listener_callback,
            10
        )

        # Skapa publisher för att skicka vidare beräknat resultat
        self.publisher_ = self.create_publisher(Float64, '/kthfs/result', 10)

        # Divisor q = 0.15
        self.q = 0.15

        self.get_logger().info('NodeB startad. Lyssnar på "nader" och publicerar på "/kthfs/result"')

    def listener_callback(self, msg):
        """Tar emot heltal från NodeA, delar med q och publicerar som float."""
        k_val = msg.data
        result_val = float(k_val) / self.q

        # Skapa och skicka Float64-meddelande
        out_msg = Float64()
        out_msg.data = result_val
        self.publisher_.publish(out_msg)

        self.get_logger().info(f'Mottaget: {k_val} | Beräknat: {result_val:.2f}')


def main(args=None):
    rclpy.init(args=args)
    node = NodeB()

    try:
        # Håll noden aktiv och lyssnande
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # Stäng ner nod och frigör resurser
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
