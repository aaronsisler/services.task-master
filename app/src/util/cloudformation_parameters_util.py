def create_parameters(service_name, service_short_name, dns_prefix, cost_center, domain_name, task_arn,
                      certificate_arn):
    return [
        {
            'ParameterKey': 'CertificateArn',
            'ParameterValue': certificate_arn,
        },
        {
            'ParameterKey': 'CostCenterTag',
            'ParameterValue': cost_center,
        },
        {
            'ParameterKey': 'DnsPrefix',
            'ParameterValue': dns_prefix,
        },
        {
            'ParameterKey': 'DomainName',
            'ParameterValue': domain_name,
        },
        {
            'ParameterKey': 'PrefixedServiceName',
            'ParameterValue': service_name,
        },
        {
            'ParameterKey': 'PrefixedServiceShortName',
            'ParameterValue': service_short_name,
        },
        {
            'ParameterKey': 'TaskArn',
            'ParameterValue': task_arn,
        }
    ]
