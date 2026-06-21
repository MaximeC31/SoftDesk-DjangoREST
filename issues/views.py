# PSEUDOCODE ONLY — no executable view code yet.
# Goal: expose project-scoped issue endpoints.
# List issues only for projects where the authenticated user is a contributor.
# Retrieve issue only when the authenticated user contributes to the linked project.
# Create issue only when the authenticated user contributes to the linked project.
# Update or delete issue only when the authenticated user is the issue author.
# Use select_related for project, author, and assignee to reduce query count.
