package kubernetes.admission

import rego.v1

deny contains message if {
  input.request.kind.kind == "Pod"
  some container in input.request.object.spec.containers
  object.get(object.get(container, "securityContext", {}), "privileged", false)
  message := sprintf("Pod %q is rejected: container %q requests privileged access.", [input.request.object.metadata.name, container.name])
}

deny contains message if {
  input.request.kind.kind == "Pod"
  some container in object.get(input.request.object.spec, "initContainers", [])
  object.get(object.get(container, "securityContext", {}), "privileged", false)
  message := sprintf("Pod %q is rejected: init container %q requests privileged access.", [input.request.object.metadata.name, container.name])
}

