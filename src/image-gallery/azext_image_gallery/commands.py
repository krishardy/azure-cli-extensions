# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
from azure.cli.core.commands import CliCommandType
from ._client_factory import cf_community_gallery, cf_community_gallery_image, cf_community_gallery_image_version


def load_command_table(self, _):

    community_gallery_sdk = CliCommandType(
        operations_tmpl='azext_image_gallery.vendored_sdks.azure_mgmt_compute.operations._community_galleries_operations#CommunityGalleriesOperations.{}',
        client_factory=cf_community_gallery)

    community_gallery_image_sdk = CliCommandType(
        operations_tmpl='azext_image_gallery.vendored_sdks.azure_mgmt_compute.operations._community_gallery_images_operations#CommunityGalleryImagesOperations.{}',
        client_factory=cf_community_gallery_image)

    community_gallery_image_version_sdk = CliCommandType(
        operations_tmpl='azext_image_gallery.vendored_sdks.azure_mgmt_compute.operations._community_gallery_image_versions_operations#CommunityGalleryImageVersionsOperations.{}',
        client_factory=cf_community_gallery_image_version)

    with self.command_group('sig', community_gallery_sdk, client_factory=cf_community_gallery) as g:
        g.command('show-community', 'get', is_experimental=True)

    with self.command_group('sig image-definition', community_gallery_image_sdk,
                            client_factory=cf_community_gallery_image) as g:
        g.command('show-community', 'get', is_experimental=True)
        # g.command('list-community', 'list', is_experimental=True)

    with self.command_group('sig image-version', community_gallery_image_version_sdk,
                            client_factory=cf_community_gallery_image_version) as g:
        g.command('show-community', 'get', is_experimental=True)
        # g.command('list-community', 'list', is_experimental=True)
