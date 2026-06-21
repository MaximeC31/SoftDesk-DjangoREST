# PSEUDOCODE ONLY — no executable serializer code yet.
# Goal: validate issue creation and updates.
# Issue creation input: title, description, optional assignee, priority, tag, optional status.
# Project should come from the route context, not arbitrary client input.
# Author should be the authenticated user, never client-provided.
# Reject assignee when the selected user is not a project contributor.
# Keep status default as To Do when omitted.
