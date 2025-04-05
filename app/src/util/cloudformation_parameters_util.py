def create_parameters(service_name, dns_prefix, cost_center, task_arn, certificate_arn):
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
        },
        {
            'ParameterKey': 'TaskArn',
            'ParameterValue': task_arn,
        },
        {
            'ParameterKey': 'CertificateArn',
            'ParameterValue': certificate_arn,
        }
    ]
