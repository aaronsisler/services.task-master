def create_parameters(service_name, dns_prefix, cost_center):
    return [
        {
            'ParameterKey': 'PrefixedServiceName',
            'ParameterValue': service_name,
        },
        {
            'ParameterKey': 'DnsPrefix',
            'ParameterValue': dns_prefix,
        },
        {
            'ParameterKey': 'CostCenterTag',
            'ParameterValue': cost_center,
        }
    ]
