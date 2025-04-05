from operator import itemgetter

import boto3
from botocore.exceptions import ClientError


def find_certificate_arn(domain_name):
    try:
        client = boto3.client('acm')

        response = client.list_certificates()

        certificate_summary_list = itemgetter('CertificateSummaryList')(response)
        for certificate in certificate_summary_list:
            domain_name_from_cert = itemgetter('DomainName')(certificate)
            if domain_name_from_cert == domain_name:
                return itemgetter('CertificateArn')(certificate)

        raise Exception("No matching certificate found")
    except ClientError as client_error:
        raise client_error
