from django.http import Http404

from inplace.boundaries.views import BoundaryDetailView

from .models import NeighborhoodGroup


class NeighborhoodGroupDetailView(BoundaryDetailView):
    model = NeighborhoodGroup

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        try:
            return queryset.get(label=self.kwargs.get('label', None))
        except NeighborhoodGroup.DoesNotExist:
            raise Http404
