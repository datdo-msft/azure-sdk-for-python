# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from . import models
from ._configuration import AzureMachineLearningWorkspacesConfiguration
from .operations import AsyncOperationsOperations, RegistryManagementNonWorkspaceOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.rest import HttpRequest, HttpResponse

class AzureMachineLearningWorkspaces(object):
    """AzureMachineLearningWorkspaces.

    :ivar async_operations: AsyncOperationsOperations operations
    :vartype async_operations:
     azure.mgmt.machinelearningservices.operations.AsyncOperationsOperations
    :ivar registry_management_non_workspace: RegistryManagementNonWorkspaceOperations operations
    :vartype registry_management_non_workspace:
     azure.mgmt.machinelearningservices.operations.RegistryManagementNonWorkspaceOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param base_url: Service URL. Default value is ''.
    :type base_url: str
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        base_url="",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        self._config = AzureMachineLearningWorkspacesConfiguration(credential=credential, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.async_operations = AsyncOperationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registry_management_non_workspace = RegistryManagementNonWorkspaceOperations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request,  # type: HttpRequest
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpResponse
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AzureMachineLearningWorkspaces
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)