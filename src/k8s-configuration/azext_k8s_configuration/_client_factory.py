# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands.client_factory import get_mgmt_service_client


def cf_k8s_configuration(cli_ctx, *_):
    from azext_k8s_configuration.vendored_sdks import SourceControlConfigurationClient
    return get_mgmt_service_client(cli_ctx, SourceControlConfigurationClient)


def cf_k8s_configuration_operation(cli_ctx, _):
    return cf_k8s_configuration(cli_ctx).source_control_configurations


def _resource_providers_client(cli_ctx):
    from azure.mgmt.resource import ResourceManagementClient
    return get_mgmt_service_client(cli_ctx, ResourceManagementClient).providers
