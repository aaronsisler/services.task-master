from app.src.util import ecs_service_util
from app.src.util import load_balancer_listener_util
from app.src.util import load_balancer_target_group_util
from app.src.util import load_balancer_util
from app.src.util import route_53_util


def orchestrate():
    # LoadBalancer
    load_balancer_util.create()

    # Route53Record Depends on: LoadBalancer
    route_53_util.create()

    # LoadBalancerTargetGroup
    load_balancer_target_group_util.create()

    # LoadBalancerListener Depends on: LoadBalancer, LoadBalancerTargetGroup
    load_balancer_listener_util.create()

    # EcsService Depends on: LoadBalancer, LoadBalancerTargetGroup, LoadBalancerListener
    ecs_service_util.create()

    return True
