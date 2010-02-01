# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = request.profile)
        if form.is_valid():
            new_profile = form.save()
            request.user.message_set.create(message=u"你的资料已经成功修改。")
            return HttpResponseRedirect(reverse('paila_profile_edit', ))
    else:
        form =ProfileForm(instance = request.profile)
    return render_to_response('profile_edit.html',locals(), context_instance = RequestContext(request))
