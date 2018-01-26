from __future__ import absolute_import

from sentry.api.bases.project import ProjectEndpoint


class ProjectEnvironmentDetailsEndpoint(ProjectEndpoint):
    def get(self, request, project, environment):
        raise NotImplementedError

    def put(self, request, project, environment):
        raise NotImplementedError
