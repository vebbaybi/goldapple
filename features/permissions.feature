Feature: Capability-specific permission
  Scenario: Workspace read does not imply execution
    Given a user grants read access to one canonical workspace root
    When an adapter requests command execution or an outside path
    Then the request is denied
    And the denial is recorded without sensitive content

  Scenario: Revocation stops new work
    Given an investigation is using workspace permission
    When the user revokes that permission
    Then no new evidence capture begins
    And cancellable in-flight capture is cancelled
