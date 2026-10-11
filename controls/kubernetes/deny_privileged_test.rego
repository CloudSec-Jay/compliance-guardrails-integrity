package kubernetes.admission

import rego.v1

test_denies_privileged_container if {
  count(deny with input as pod_review("app", true, false)) == 1
}

test_denies_privileged_init_container if {
  count(deny with input as pod_review("app", false, true)) == 1
}

test_allows_unprivileged_pod if {
  count(deny with input as pod_review("app", false, false)) == 0
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

