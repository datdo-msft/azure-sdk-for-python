# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AddressValue
    from ._models_py3 import AnalyzeDocumentRequest
    from ._models_py3 import AnalyzeResult
    from ._models_py3 import AnalyzeResultOperation
    from ._models_py3 import AuthorizeCopyRequest
    from ._models_py3 import AzureBlobContentSource
    from ._models_py3 import BoundingRegion
    from ._models_py3 import BuildDocumentModelRequest
    from ._models_py3 import ComponentModelInfo
    from ._models_py3 import ComposeDocumentModelRequest
    from ._models_py3 import CopyAuthorization
    from ._models_py3 import CurrencyValue
    from ._models_py3 import CustomDocumentModelsInfo
    from ._models_py3 import DocTypeInfo
    from ._models_py3 import Document
    from ._models_py3 import DocumentCaption
    from ._models_py3 import DocumentField
    from ._models_py3 import DocumentFieldSchema
    from ._models_py3 import DocumentFootnote
    from ._models_py3 import DocumentImage
    from ._models_py3 import DocumentKeyValueElement
    from ._models_py3 import DocumentKeyValuePair
    from ._models_py3 import DocumentLanguage
    from ._models_py3 import DocumentLine
    from ._models_py3 import DocumentPage
    from ._models_py3 import DocumentParagraph
    from ._models_py3 import DocumentSelectionMark
    from ._models_py3 import DocumentSpan
    from ._models_py3 import DocumentStyle
    from ._models_py3 import DocumentTable
    from ._models_py3 import DocumentTableCell
    from ._models_py3 import DocumentWord
    from ._models_py3 import Error
    from ._models_py3 import ErrorResponse
    from ._models_py3 import GetInfoResponse
    from ._models_py3 import GetModelsResponse
    from ._models_py3 import GetOperationResponse
    from ._models_py3 import GetOperationsResponse
    from ._models_py3 import InnerError
    from ._models_py3 import ModelInfo
    from ._models_py3 import ModelSummary
    from ._models_py3 import OperationInfo
except (SyntaxError, ImportError):
    from ._models import AddressValue  # type: ignore
    from ._models import AnalyzeDocumentRequest  # type: ignore
    from ._models import AnalyzeResult  # type: ignore
    from ._models import AnalyzeResultOperation  # type: ignore
    from ._models import AuthorizeCopyRequest  # type: ignore
    from ._models import AzureBlobContentSource  # type: ignore
    from ._models import BoundingRegion  # type: ignore
    from ._models import BuildDocumentModelRequest  # type: ignore
    from ._models import ComponentModelInfo  # type: ignore
    from ._models import ComposeDocumentModelRequest  # type: ignore
    from ._models import CopyAuthorization  # type: ignore
    from ._models import CurrencyValue  # type: ignore
    from ._models import CustomDocumentModelsInfo  # type: ignore
    from ._models import DocTypeInfo  # type: ignore
    from ._models import Document  # type: ignore
    from ._models import DocumentCaption  # type: ignore
    from ._models import DocumentField  # type: ignore
    from ._models import DocumentFieldSchema  # type: ignore
    from ._models import DocumentFootnote  # type: ignore
    from ._models import DocumentImage  # type: ignore
    from ._models import DocumentKeyValueElement  # type: ignore
    from ._models import DocumentKeyValuePair  # type: ignore
    from ._models import DocumentLanguage  # type: ignore
    from ._models import DocumentLine  # type: ignore
    from ._models import DocumentPage  # type: ignore
    from ._models import DocumentParagraph  # type: ignore
    from ._models import DocumentSelectionMark  # type: ignore
    from ._models import DocumentSpan  # type: ignore
    from ._models import DocumentStyle  # type: ignore
    from ._models import DocumentTable  # type: ignore
    from ._models import DocumentTableCell  # type: ignore
    from ._models import DocumentWord  # type: ignore
    from ._models import Error  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import GetInfoResponse  # type: ignore
    from ._models import GetModelsResponse  # type: ignore
    from ._models import GetOperationResponse  # type: ignore
    from ._models import GetOperationsResponse  # type: ignore
    from ._models import InnerError  # type: ignore
    from ._models import ModelInfo  # type: ignore
    from ._models import ModelSummary  # type: ignore
    from ._models import OperationInfo  # type: ignore

from ._form_recognizer_client_enums import (
    AnalyzeResultOperationStatus,
    ApiVersion,
    ContentType,
    DocumentBuildMode,
    DocumentFieldType,
    DocumentPageKind,
    DocumentSignatureType,
    DocumentTableCellKind,
    LengthUnit,
    OperationKind,
    OperationStatus,
    ParagraphRole,
    SelectionMarkState,
    StringIndexType,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AddressValue',
    'AnalyzeDocumentRequest',
    'AnalyzeResult',
    'AnalyzeResultOperation',
    'AuthorizeCopyRequest',
    'AzureBlobContentSource',
    'BoundingRegion',
    'BuildDocumentModelRequest',
    'ComponentModelInfo',
    'ComposeDocumentModelRequest',
    'CopyAuthorization',
    'CurrencyValue',
    'CustomDocumentModelsInfo',
    'DocTypeInfo',
    'Document',
    'DocumentCaption',
    'DocumentField',
    'DocumentFieldSchema',
    'DocumentFootnote',
    'DocumentImage',
    'DocumentKeyValueElement',
    'DocumentKeyValuePair',
    'DocumentLanguage',
    'DocumentLine',
    'DocumentPage',
    'DocumentParagraph',
    'DocumentSelectionMark',
    'DocumentSpan',
    'DocumentStyle',
    'DocumentTable',
    'DocumentTableCell',
    'DocumentWord',
    'Error',
    'ErrorResponse',
    'GetInfoResponse',
    'GetModelsResponse',
    'GetOperationResponse',
    'GetOperationsResponse',
    'InnerError',
    'ModelInfo',
    'ModelSummary',
    'OperationInfo',
    'AnalyzeResultOperationStatus',
    'ApiVersion',
    'ContentType',
    'DocumentBuildMode',
    'DocumentFieldType',
    'DocumentPageKind',
    'DocumentSignatureType',
    'DocumentTableCellKind',
    'LengthUnit',
    'OperationKind',
    'OperationStatus',
    'ParagraphRole',
    'SelectionMarkState',
    'StringIndexType',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()