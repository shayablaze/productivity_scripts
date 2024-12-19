def replace_secrets_with_stars(byte_list, secrets):
    """
    Replaces occurrences of secret strings in a list of bytes with '****'.

    Args:
        byte_list (list of bytes): The list of bytes to process.
        secrets (list of str): The list of secrets to replace.

    Returns:
        list of bytes: A new list of bytes with the secrets replaced by '****'.
    """
    # Convert secrets to bytes
    secrets_bytes = [secret.encode('utf-8') for secret in secrets]

    # Process each byte entry
    result = []
    for byte_entry in byte_list:
        for secret_bytes in secrets_bytes:
            byte_entry = byte_entry.replace(secret_bytes, b'jethrotull')
        result.append(byte_entry)

    return result

# Example usage:
byte_data = [b'{"id": 14524348, "isNewTest": true, "name": "gondalak", "userId": 1862206, "creatorClientId": "gui", "overrideExecutions": [{"concurrency": 20, "executor": "", "holdFor": "19m", "locations": {"us-east4-a": 20}, "locationsPercents": {"us-east4-a": 100}, "rampUp": "1m", "steps": 0}], "executions": [{"concurrency": 20, "usersNotConfigured": false, "holdFor": "19m", "durationIsNotConfigured": false, "iterationAndDurationDisabled": false, "rampUp": "1m", "steps": 0, "locations": {"us-east4-a": 20}, "locationsPercents": {"us-east4-a": 100}, "scenario": "default-scenario-14524348"}], "hasThreadGroupsToOverride": false, "hasNonRegularThreadGroup": false, "hasMultipleThreadGroups": false, "shouldSendReportEmail": true, "dependencies": {}, "shouldRemoveJmeter": true, "created": 1733763063, "updated": 1733763067, "projectId": 1679992, "lastUpdatedById": 1862206, "configuration": {"type": "taurus", "dedicatedIpsEnabled": false, "canControlRampup": false, "targetThreads": 500, "executionType": "taurusCloud", "enableLoadConfiguration": true, "threads": 500, "testMode": "", "extraSlots": 0, "plugins": {"jmeter": {"version": "stable", "consoleArgs": "", "enginesArgs": "", "versionInfo": [{"key": "stable", "text": "Stable", "number": "5.5", "enabled": true}, {"key": "latest", "text": "Latest", "number": "5.6.3", "enabled": true}, {"key": "auto", "text": "Auto Detect", "number": "", "enabled": false}]}, "thresholds": {"thresholds": [], "fromTaurus": false}}}, "subscribers": [1862206], "revisionTimestamp": 1733763084386}']
print(byte_data)
secrets = ["gondalak"]
updated_data = replace_secrets_with_stars(byte_data, secrets)
print(updated_data)