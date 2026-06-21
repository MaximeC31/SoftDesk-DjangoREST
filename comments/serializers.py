# PSEUDOCODE ONLY — no executable serializer code yet.
# Goal: validate comment creation and updates.
# Comment creation input: description.
# Issue should come from the route context, not arbitrary client input.
# Author should be the authenticated user, never client-provided.
# Reject creation when the user is not a contributor of the issue project.
# Expose UUID, description, author, issue, and created_time in responses.
