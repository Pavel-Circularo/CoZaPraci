from re import S
from django_unicorn.components import UnicornView
from jobs_app.models import Job


class JoblistView(UnicornView):
    job = ""
    all_jobs = Job.objects.exclude(is_approved=0)

    def clear_jobs(self):
        self.job = ""

    def jobs(self):
        if not self.job:
            return []

        res = []
        for s in self.all_jobs:
            jn = s.job_name
            if jn.lower().startswith(self.job.lower()):
                res.append(s)

        return res
    class Meta:
        exclude = ("all_jobs",)
