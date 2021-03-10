from django.contrib import admin
from .models import User
from django_object_actions import DjangoObjectActions
from django_object_actions.utils import ChangeActionView
from django.conf.urls import url


@admin.register(User)
class UserAdmin(DjangoObjectActions, admin.ModelAdmin):
    change_form_template = 'admin/otp_change_form.html'
    change_actions = ("hello",)

    # def _get_action_urls(self):
    #     model_name = self.model._meta.model_name
    #     base_url_name = "%s_%s" % (self.model._meta.app_label, model_name)
    #     return super(UserAdmin, self)._get_action_urls() + [
    #          url(
    #             r"^(?P<pk>.+)/actions/(?P<tool>\w+)/$",
    #             self.admin_site.admin_view(
    #                 ChangeActionView.as_view(
    #                     model=self.model,
    #                     actions=self.actions,
    #                     back="admin:%s_change" % base_url_name,
    #                     current_app=self.admin_site.name,
    #                 )
    #             )
    #         )
    #     ]

    def hello(self, request, user):
        print(self, request, user, request.GET.get('otp_code'))
        self.message_user(request=request, message="hello!")
