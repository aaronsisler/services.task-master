from botocore.exceptions import ClientError

from app.src.blueprint.create_receipt_response import CreateReceiptResponse
from app.src.blueprint.create_stack_request import CreateStackRequest
from app.src.blueprint.delete_receipt_response import DeleteReceiptResponse
from app.src.util import cloudformation_stack_util, cloudformation_template_util, cloudformation_parameters_util, \
    ecs_task_util, certificate_util


def create_stack(create_stack_request: CreateStackRequest):
    stack_name = create_stack_request.service_name + "-stack"
    does_stack_exist = cloudformation_stack_util.check_for_stack_existence(stack_name)

    if does_stack_exist:
        return CreateReceiptResponse(stack_name=stack_name, does_stack_exist=True)

    try:
        stack_template_content = cloudformation_template_util.get_ecs_template_content()

        ecs_task_name = create_stack_request.service_name + "-task"
        ecs_latest_task_arn = ecs_task_util.find_latest_task_arn(ecs_task_name)

        certificate_arn = certificate_util.find_certificate_arn(create_stack_request.domain_name)

        if create_stack_request.service_short_name is None:
            parameters = cloudformation_parameters_util.create_parameters(
                create_stack_request.service_name,
                create_stack_request.service_name,
                create_stack_request.dns_prefix,
                create_stack_request.cost_center_tag,
                create_stack_request.domain_name,
                ecs_latest_task_arn,
                certificate_arn
            )
        else:
            parameters = cloudformation_parameters_util.create_parameters(
                create_stack_request.service_name,
                create_stack_request.service_short_name,
                create_stack_request.dns_prefix,
                create_stack_request.cost_center_tag,
                create_stack_request.domain_name,
                ecs_latest_task_arn,
                certificate_arn
            )

        stack_id = cloudformation_stack_util.create_stack(stack_name,
                                                          stack_template_content,
                                                          parameters
                                                          )

        return CreateReceiptResponse(stack_name=stack_name, stack_id=stack_id)

    except ClientError as client_error:
        return CreateReceiptResponse(stack_name=stack_name, error_message=client_error)


def delete_stack(stack_name):
    does_stack_exist = cloudformation_stack_util.check_for_stack_existence(stack_name)

    if not does_stack_exist:
        return DeleteReceiptResponse(stack_name=stack_name,
                                     does_stack_exist=does_stack_exist)
    try:
        cloudformation_stack_util.delete_stack(stack_name)

        return DeleteReceiptResponse(stack_name=stack_name,
                                     was_delete_triggered=True)

    except ClientError as client_error:
        return DeleteReceiptResponse(stack_name=stack_name,
                                     error_message=client_error)
