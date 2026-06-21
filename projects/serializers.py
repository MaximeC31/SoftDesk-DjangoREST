# PSEUDOCODE ONLY — no executable serializer code yet.
# Goal: validate project and contributor payloads.
# Project creation input: title, description, type.
# Project author must always be the authenticated user, never client-provided.
# Contributor creation input: user identifier and project context.
# Reject duplicate contributor assignments.
# Reject contributor operations from users who are not authorized project authors if required by business rule.
