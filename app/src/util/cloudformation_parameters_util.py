def create_parameters(service_name, dns_prefix, cost_center):
    return [
        {
            'ParameterKey': 'string',
            'ParameterValue': service_name,
        },
        {
            'ParameterKey': 'string',
            'ParameterValue': dns_prefix,
        },
        {
            'ParameterKey': 'string',
            'ParameterValue': cost_center,
        }
    ],
