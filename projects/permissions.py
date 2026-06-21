# PSEUDOCODE ONLY — no executable permission code yet.
# Goal: centralize project-level object authorization.
# Allow read access only when the authenticated user is a project contributor.
# Allow update and delete only when the authenticated user is the project author.
# Reject unauthenticated users everywhere except registration and JWT obtain endpoints.
# Reuse contributor checks for issues and comments to avoid duplicated permission logic.
