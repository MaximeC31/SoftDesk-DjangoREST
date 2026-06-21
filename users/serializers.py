# PSEUDOCODE ONLY — no executable serializer code yet.
# Goal: validate user registration and profile operations.
# Registration input: username, password, age, can_be_contacted, can_data_be_shared.
# Reject registration when age is missing or lower than 15.
# Hash password through Django user creation utilities, never store raw password.
# Profile output should expose personal fields needed for RGPD access.
# Profile update should allow rectification of age and consent fields.
