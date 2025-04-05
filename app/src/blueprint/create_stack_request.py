class CreateStackRequest:
    def __init__(self, service_name, dns_prefix, cost_center_tag, domain_name="otterandcow.com"):
        self.service_name = service_name
        self.dns_prefix = dns_prefix
        self.cost_center_tag = cost_center_tag
        self.domain_name = domain_name
