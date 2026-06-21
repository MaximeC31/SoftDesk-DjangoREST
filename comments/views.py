# PSEUDOCODE ONLY — no executable view code yet.
# Goal: expose issue-scoped comment endpoints.
# List comments only when the authenticated user contributes to the linked project.
# Retrieve comment only when the authenticated user contributes to the linked project.
# Create comment only when the authenticated user contributes to the linked project.
# Update or delete comment only when the authenticated user is the comment author.
# Use select_related for issue, project, and author to reduce query count.
