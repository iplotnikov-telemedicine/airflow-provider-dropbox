# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

import warnings
from typing import Any
import dropbox
from airflow.hooks.base import BaseHook


class DropboxBaseHook(BaseHook):
    """
    A base hook for Dropbox related tasks.

    :param dropbox_conn_id: The connection ID to use when fetching connection info.
    """

    conn_name_attr = "dropbox_conn_id"
    default_conn_name = "dropbox_default"
    conn_type = "dropbox"
    hook_name = "Dropbox"

    @staticmethod
    def get_connection_form_widgets() -> dict[str, Any]:
        """Returns connection widgets to add to connection form."""
        from flask_appbuilder.fieldwidgets import BS3PasswordFieldWidget, BS3TextFieldWidget
        from flask_babel import lazy_gettext
        from wtforms import PasswordField, StringField

        return {
            "service_account_json": PasswordField(
                lazy_gettext("Service account auth JSON"),
                widget=BS3PasswordFieldWidget(),
                description="Service account auth JSON. Looks like "
                '{"id", "...", "service_account_id": "...", "private_key": "..."}. '
                "Will be used instead of OAuth token and SA JSON file path field if specified.",
            ),
            "service_account_json_path": StringField(
                lazy_gettext("Service account auth JSON file path"),
                widget=BS3TextFieldWidget(),
                description="Service account auth JSON file path. File content looks like "
                '{"id", "...", "service_account_id": "...", "private_key": "..."}. '
                "Will be used instead of OAuth token if specified.",
            ),
            "oauth": PasswordField(
                lazy_gettext("OAuth Token"),
                widget=BS3PasswordFieldWidget(),
                description="User account OAuth token. "
                "Either this or service account JSON must be specified.",
            ),
            "folder_id": StringField(
                lazy_gettext("Default folder ID"),
                widget=BS3TextFieldWidget(),
                description="Optional. This folder will be used "
                "to create all new clusters and nodes by default",
            ),
            "public_ssh_key": StringField(
                lazy_gettext("Public SSH key"),
                widget=BS3TextFieldWidget(),
                description="Optional. This key will be placed to all created Compute nodes"
                "to let you have a root shell there",
            ),
            "endpoint": StringField(
                lazy_gettext("API endpoint"),
                widget=BS3TextFieldWidget(),
                description="Optional. Specify an API endpoint. Leave blank to use default.",
            ),
        }

    @classmethod
    def provider_user_agent(cls) -> str | None:
        """Construct User-Agent from Airflow core & provider package versions."""
        import airflow
        from airflow.providers_manager import ProvidersManager

        try:
            manager = ProvidersManager()
            provider_name = manager.hooks[cls.conn_type].package_name  # type: ignore[union-attr]
            provider = manager.providers[provider_name]
            return f"apache-airflow/{airflow.__version__} {provider_name}/{provider.version}"
        except KeyError:
            warnings.warn(f"Hook '{cls.hook_name}' info is not initialized in airflow.ProviderManager")
            return None
        

    @staticmethod
    def get_ui_field_behaviour() -> dict:
        """Returns custom field behaviour"""
        import json

        return {
            "hidden_fields": ['port'],
            "relabeling": {},
            "placeholders": {
                'extra': json.dumps(
                    {
                        "example_parameter": "parameter",
                    },
                    indent=1,
                ),
                'host': 'example hostname',
                'schema': 'example schema',
                'login': 'example username',
                'password': 'example password',
                'extra__example__account': 'example account name',
                'extra__example__secret_key': 'example secret key',
            },
        }
