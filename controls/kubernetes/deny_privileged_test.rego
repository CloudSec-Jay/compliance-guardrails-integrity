package kubernetes.admission

import rego.v1

test_denies_privileged_container if {
  violations := deny with input as pod_review("app", true, false)
  count(violations) == 1
}

test_denies_privileged_init_container if {
  violations := deny with input as pod_review("app", false, true)
  count(violations) == 1
}

test_allows_unprivileged_pod if {
  violations := deny with input as pod_review("app", false, false)
  count(violations) == 0
}

pod_review(name, container_privileged, init_privileged) := {
  "request": {
    "kind": {"kind": "Pod"},
    "object": {
      "metadata": {"name": name},
      "spec": {
        "containers": [{
          "name": "app",
          "securityContext": {"privileged": container_privileged}
        }],
        "initContainers": [{
          "name": "setup",
          "securityContext": {"privileged": init_privileged}
        }]
      }
    }
  }
}

