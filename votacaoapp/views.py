from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy

from . import models, forms

# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Comments(CreateView):
	model = models.Comments
	success_url = reverse_lazy('list')
	template_name = 'comments.html'
	form_class = forms.CommentsForm
	def get(self, request, pk):
		global pkid
		pkid = pk
		return super(Comments, self).get(request, pk)
	def form_valid(self, form):
		print(pkid)
		obj = form.save(commit=False)
		obj.leiId = pkid
		obj.save()
		return super(Comments, self).form_valid(form)

class CommentsView(ListView):
	model = models.Comments
	template_name = 'commentslist.html'
	def get(self, request, pk):
		global pkid2
		pkid2 = pk
		return super(CommentsView, self).get(request, pk)
	def get_queryset(self):
		if(len(models.Comments.objects.filter(leiId=pkid2)) >= 1):
			return models.Comments.objects.filter(leiId=pkid2)
		else:
			return HttpResponseRedirect('/list/')

class Popup(generic.ListView):
    model = models.Votacao
    template_name = 'popup.html'

class CreateVoting(CreateView):

    model = models.Votacao
    template_name = 'create-voting.html'
    success_url = reverse_lazy('home')
    fields = ['name', 'description']

class VotingList(generic.ListView):
    model = models.Votacao
    template_name = 'list-voting.html'


    def get_queryset(self):
    	#print(self.request.user.pk)
    	now = datetime.now()
    	for x in models.Votacao.objects.all():
    		votoSim = x.votoSim
    		votoNao = x.votoNao
    		total = votoSim + votoNao
    		if(now.hour >= x.final_time.hour and now.minute >= x.final_time.minute):
	    		x.active = False
	    		x.save()
    		if(votoSim > (50 / 100.0 * total) and x.active == False):
    			x.resultado = True
    			x.save()
    	return models.Votacao.objects.all()

class VotingTrue(DetailView):
    def get(self, request, pk):
    	#print(self.request.user.pk)
    	print(len(models.Votadas.objects.all()))
    	if(len(models.Votadas.objects.all())):
    		for x in models.Votadas.objects.all():
    			if(x.userId == int(self.request.user.pk) and x.leiId == int(pk)):
	    			return HttpResponseRedirect('/popup')
	    		else:
	    			obj =  models.Votacao.objects.get(id=pk)
	    			obj.votoSim = obj.votoSim + 1
	    			obj.userVot = self.request.user.pk
	    			obj.save()
	    			aux = models.Votadas.objects.create(
			    			userId=self.request.user.pk,
			    			leiId=pk,
			  				)
	    			aux.save()
	    			print(pk)

    	
    	else:
    		obj =  models.Votacao.objects.get(id=pk)
    		obj.votoSim = obj.votoSim + 1
    		obj.userVot = self.request.user.pk
    		obj.save()
    		aux = models.Votadas.objects.create(
			    			userId=self.request.user.pk,
			    			leiId=pk,
			  				)
    		aux.save()
    		print(pk)
    	return HttpResponseRedirect('/list/')

class VotingFalse(DetailView):
	def get(self, request, pk):
		if(len(models.Votadas.objects.all())):
			for x in models.Votadas.objects.all():
				if(x.userId == int(self.request.user.pk) and x.leiId == int(pk)):
					return HttpResponseRedirect('/popup')
				else:
					obj =  models.Votacao.objects.get(id=pk)
					obj.votoNao = obj.votoNao + 1
					obj.userVot = self.request.user.pk
					obj.save()
					aux = models.Votadas.objects.create(
			    			userId=self.request.user.pk,
			    			leiId=pk,
			  				)
					aux.save()
					print(pk)
		else:
			obj =  models.Votacao.objects.get(id=pk)
			obj.votoNao = obj.votoNao + 1
			obj.userVot = self.request.user.pk
			obj.save()
			aux = models.Votadas.objects.create(
			    			userId=self.request.user.pk,
			    			leiId=pk,
			  				)
			aux.save()
			print(pk)
		return HttpResponseRedirect('/list/')


    

