from nautobot.core.apps import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuImportButton, NavMenuTab


menu_items = (
    NavMenuTab(
        name="Organization",
        weight=100,
        groups=(
            NavMenuGroup(
                name="Tags",
                weight=400,
                items=(
                    NavMenuItem(
                        link="extras:tag_list",
                        name="Tags",
                        weight=100,
                        permissions=[
                            "extras.view_tag",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:tag_add",
                                permissions=[
                                    "extras.add_tag",
                                ],
                            ),
                            NavMenuImportButton(
                                link="extras:tag_import",
                                permissions=[
                                    "extras.add_tag",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Statuses",
                weight=500,
                items=(
                    NavMenuItem(
                        link="extras:status_list",
                        name="Statuses",
                        weight=100,
                        permissions=[
                            "extras.view_status",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:status_add",
                                permissions=[
                                    "extras.add_status",
                                ],
                            ),
                            NavMenuImportButton(
                                link="extras:status_import",
                                permissions=[
                                    "extras.add_status",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
    NavMenuTab(
        name="Extensibility",
        weight=700,
        groups=(
            NavMenuGroup(
                name="Logging",
                weight=100,
                items=(
                    NavMenuItem(
                        link="extras:objectchange_list",
                        name="Change Log",
                        weight=100,
                        permissions=[
                            "extras.view_objectchange",
                        ],
                        buttons=(),
                    ),
                    NavMenuItem(
                        link="extras:jobresult_list",
                        name="Job Results",
                        weight=200,
                        permissions=[
                            "extras.view_jobresult",
                        ],
                        buttons=(),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Data Sources",
                weight=200,
                items=(
                    NavMenuItem(
                        link="extras:gitrepository_list",
                        name="Git Repositories",
                        weight=100,
                        permissions=[
                            "extras.view_gitrepository",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:gitrepository_add",
                                permissions=[
                                    "extras.add_gitrepository",
                                ],
                            ),
                            NavMenuImportButton(
                                link="extras:gitrepository_import",
                                permissions=[
                                    "extras.add_gitrepository",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Data Management",
                weight=300,
                items=(
                    NavMenuItem(
                        link="extras:graphqlquery_list",
                        name="GraphQL Queries",
                        weight=100,
                        permissions=[
                            "extras.view_graphqlquery",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:graphqlquery_add",
                                permissions=[
                                    "extras.add_graphqlquery",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:relationship_list",
                        name="Relationships",
                        weight=200,
                        permissions=[
                            "extras.view_relationship",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:relationship_add",
                                permissions=[
                                    "extras.add_relationship",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Automation",
                weight=400,
                items=(
                    NavMenuItem(
                        link="extras:configcontext_list",
                        name="Config Contexts",
                        weight=100,
                        permissions=[
                            "extras.view_configcontext",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:configcontext_add",
                                permissions=[
                                    "extras.add_configcontext",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:configcontextschema_list",
                        name="Config Context Schemas",
                        weight=100,
                        permissions=[
                            "extras.view_configcontextschema",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:configcontextschema_add",
                                permissions=[
                                    "extras.add_configcontextschema",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:exporttemplate_list",
                        name="Export Templates",
                        weight=200,
                        permissions=[
                            "extras.view_exporttemplate",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:exporttemplate_add",
                                permissions=[
                                    "extras.add_exporttemplate",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:job_list",
                        name="Jobs",
                        weight=300,
                        permissions=[
                            "extras.view_job",
                        ],
                        buttons=(),
                    ),
                    NavMenuItem(
                        link="extras:webhook_list",
                        name="Webhooks",
                        weight=400,
                        permissions=[
                            "extras.view_webhook",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:webhook_add",
                                permissions=[
                                    "extras.add_webhook",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Miscellaneous",
                weight=500,
                items=(
                    NavMenuItem(
                        link="extras:computedfield_list",
                        name="Computed Fields",
                        weight=100,
                        permissions=[
                            "extras.view_computedfield",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:computedfield_add",
                                permissions=[
                                    "extras.add_computedfield",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:customlink_list",
                        name="Custom Links",
                        weight=200,
                        permissions=[
                            "extras.view_customlink",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:customlink_add",
                                permissions=[
                                    "extras.add_customlink",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
