Feature: Evidence-backed development failure investigation
  As a developer
  I want Golden Apple to correlate authorized project evidence
  So that I can understand a failure without surrendering control

  Scenario: Explain a known dependency regression
    Given I authorized a trusted fixture workspace for read-only discovery
    And the fixture contains a dependency change, diagnostic, and failing test output
    When I start an investigation of the failure
    Then each material observation cites captured evidence
    And inferred causes are labeled as inference with confidence
    And missing or conflicting evidence is disclosed
    And no workspace content is transmitted without provider consent

  Scenario: Refuse implicit authority from workspace content
    Given an authorized workspace contains instructions requesting command execution
    When Golden Apple indexes that content
    Then the instructions are treated as untrusted evidence
    And no command is executed
