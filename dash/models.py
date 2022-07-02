from djongo import models

# Create your models here.



class personal(models.Model):

	GENDER=[
		('Male','Male'),
		('Female','Female'),
	]
	Name=models.CharField(max_length=100)
	Designation=models.CharField(max_length=100)
	Emp_ID=models.IntegerField()
	School=models.CharField(max_length=100)
	DOJ=models.DateField()
	DOB=models.DateField()
	Gender=models.CharField(max_length=10,choices=GENDER)
	ORCID_ID=models.IntegerField()
	Researchgate=models.CharField(max_length=100)
	linkedin=models.CharField(max_length=100)
	Google_scholar_name=models.CharField(max_length=100)
	Personal_page=models.CharField(max_length=100)

	def __str__(self):
		return self.Name

class authorinfo(models.Model):
	TYPE=[
		('NationaL','NationaL'),
		('International','International'),
		('Internal','Internal'),

	]
	Author_name=models.CharField(max_length=100)
	Designation=models.CharField(max_length=20)
	Collaboration=models.CharField(max_length=20,choices=TYPE)

	class Meta:
		abstract=True


class conference(models.Model):
	POSITION=[
		(1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5),
		(6,6),
	]

	TY=[
		('NationaL','NationaL'),
		('International','International'),
		
	]

	jy=[
		('Yes','Yes'),
		('No','No'),
	]

	TP=[
		('Open Access','Open Access'),
		('Subscription','Subscription'),
	]


	
	Artical_title=models.CharField(max_length=100)
	no_of_authors=models.IntegerField()
	Author_info=models.EmbeddedField(
				model_container=authorinfo, null=True
		)
	Author_pos=models.IntegerField(choices=POSITION)
	Conference_name=models.CharField(max_length=100)
	Conference_startdate=models.DateField()
	Conference_enddate=models.DateField()
	Place_of_conference=models.CharField(max_length=100)
	Type=models.CharField(max_length=20,choices=TY)
	Indexed_Scopus=models.CharField(max_length=4,choices=jy)
	DOI=models.CharField(max_length=30,null=True)
	Type_of_publication=models.CharField(max_length=100, choices=TP)
	Emp_ID=models.ForeignKey(personal,null=True,on_delete=models.SET_NULL)
	Funder_name=models.CharField('Enter Funder name if type is "Open" ',max_length=100,blank=True)
	Amount_of_Publication=models.IntegerField('Enter Amount of Publication if type is "Open" ',blank=True, null=True)
	Support=models.CharField('Whether Support received from Vellore Institute of Technology?',max_length=4,choices=jy,null=True)

	def __str__(self):
		return self.Artical_title

	@property
	def daysbetween(self):
		sdays=self.Conference_startdate.date()
		edays=self.Conference_enddate.date() - sdays
		return edays 

class journal(models.Model):
	INDEX=[
		('SCI','SCI'),
		('SCIE','SCIE'),
		('SCOPUS','SCOPUS'),
	]

	POSITION=[
		(1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5),
		(6,6),
	]
	jy=[
		('Yes','Yes'),
		('No','No'),
	]

	TP=[
		('Open Access','Open Access'),
		('Subscription','Subscription'),
	]

	Artical_title=models.CharField(max_length=100)
	no_of_authors=models.IntegerField()
	Author_info=models.EmbeddedField(
				model_container=authorinfo, null=True
		)
	Author_pos=models.IntegerField(choices=POSITION)
	Journal_name=models.CharField(max_length=100)
	Indexing=models.CharField(max_length=20,choices=INDEX)
	Impact_factor=models.FloatField('optional',null=True)
	year=models.IntegerField()
	Vol_no=models.IntegerField('optional',null=True)
	Issue_no=models.IntegerField('optional',null=True)
	DOI=models.CharField('optional', max_length=30,null=True)
	Emp_ID=models.ForeignKey(personal,null=True,on_delete=models.SET_NULL)
	Type_of_publication=models.CharField(max_length=100, choices=TP)
	Funder_name=models.CharField('Enter Funder name if type is "Open" ',max_length=100,blank=True)
	Amount_of_Publication=models.IntegerField('Enter Amount of Publication if type is "Open" ',blank=True, null=True)
	Support=models.CharField('Whether Support received from Vellore Institute of Technology?',max_length=4,choices=jy,null=True)

	def __str__(self):
		return self.Artical_title


class book_chapters(models.Model):
	INDEX=[
		('SCI','SCI'),
		('SCIE','SCIE'),
		('SCOPUS','SCOPUS'),
	]

	POSITION=[
		(1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5),
		(6,6),
	]
	jy=[
		('Yes','Yes'),
		('No','No'),
	]

	TP=[
		('Open Access','Open Access'),
		('Subscription','Subscription'),
	]

	TY=[
		('NationaL','NationaL'),
		('International','International'),
		
	]

	Chapter_title=models.CharField(max_length=100)
	no_of_authors=models.IntegerField()
	Author_info=models.EmbeddedField(
				model_container=authorinfo, null=True
		)
	Author_pos=models.IntegerField(choices=POSITION)
	Indexing=models.CharField(max_length=20,choices=INDEX)
	ISSN_ISBN_number=models.IntegerField()
	year=models.IntegerField()
	book_title=models.CharField(max_length=100)
	publisher_name=models.CharField(max_length=30)
	TYpe_of_publisher=models.CharField(max_length=30,choices=TY)
	Vol_no=models.IntegerField('optional',null=True)
	Issue_no=models.IntegerField('optional',null=True)
	DOI=models.CharField('optional', max_length=30,null=True)
	Emp_ID=models.ForeignKey(personal,null=True,on_delete=models.SET_NULL)
	Type_of_publication=models.CharField(max_length=100, choices=TP)
	Funder_name=models.CharField('Enter Funder name if type is "Open" ',max_length=100,blank=True)
	Amount_of_Publication=models.IntegerField('Enter Amount of Publication if type is "Open" ',blank=True, null=True)
	Support=models.CharField('Whether Support received from Vellore Institute of Technology?',max_length=4,choices=jy,null=True)

	def __str__(self):
		return self.Chapter_title


class book_editor(models.Model):

	POSITION=[
		(1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5),
		(6,6),
	]

	jy=[
		('Yes','Yes'),
		('No','No'),
	]

	TP=[
		('Open Access','Open Access'),
		('Subscription','Subscription'),
	]

	TY=[
		('NationaL','NationaL'),
		('International','International'),
		
	]

	INDEX=[
		('SCI','SCI'),
		('SCIE','SCIE'),
		('SCOPUS','SCOPUS'),
	]


	book_title=models.CharField(max_length=50)
	no_of_authors=models.IntegerField()
	Author_info=models.EmbeddedField(
				model_container=authorinfo, null=True
		)
	Author_pos=models.IntegerField(choices=POSITION)
	Indexing=models.CharField(max_length=20,choices=INDEX)
	ISSN_ISBN_number=models.IntegerField()
	year=models.IntegerField()
	book_title=models.CharField(max_length=100)
	publisher_name=models.CharField(max_length=30)
	TYpe_of_publisher=models.CharField(max_length=30,choices=TY)
	Vol_no=models.IntegerField('optional',null=True)
	Issue_no=models.IntegerField('optional',null=True)
	DOI=models.CharField('optional', max_length=30,null=True)
	Emp_ID=models.ForeignKey(personal,null=True,on_delete=models.SET_NULL)
	Type_of_publication=models.CharField(max_length=100, choices=TP)
	Funder_name=models.CharField('Enter if type is "Open" ',max_length=100,blank=True)
	Amount_of_Publication=models.IntegerField('Enter if type is "Open" ',blank=True, null=True)
	Support=models.CharField('Whether Support received from Vellore Institute of Technology?',max_length=4,choices=jy,null=True)

	def __str__(self):
		return self.book_title


class consultancy_project(models.Model):

	jy=[
		('Yes','Yes'),
		('No','No'),
	]

	TYPE=[
		('Product development','Product development'),
		('Research Collaboration','Research Collaboration'),
	]


	Emp_ID=models.ForeignKey(personal,null=True,on_delete=models.SET_NULL)
	type_of_consultancy=models.CharField(max_length=50,choices=TYPE)
	company_name=models.CharField(max_length=50)
	Funding=models.CharField(max_length=5,null=True,choices=jy,blank=True)
	Amount=models.IntegerField('if funding recieved Enter Amount:',blank=True,null=True)
	invoice_number=models.IntegerField('if funding recieved Enter invoice',blank=True,null=True)
	Consultancy_startdate=models.DateField()
	Consultancy_enddate=models.DateField()

	def __str__(self):
		return self.company_name

	@property
	def days(self):
		cdays=self.Consultancy_startdate.date()
		ddays=self.Consultancy_enddate.date() - cdays
		return ddays

class patent(models.Model):

	TY=[
		('NationaL','NationaL'),
		('International','International'),
		
	]
	POSITION=[
		(1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5),
		(6,6),
	]


	Emp_ID=models.ForeignKey(personal,null=True,on_delete=models.SET_NULL)
	patent_title=models.CharField(max_length=40)
	Type_of_patent=models.CharField(max_length=20,choices=TY)
	no_of_authors_in_patent=models.IntegerField()
	Author_pos=models.IntegerField(choices=POSITION)

	def __str__(self):
		return self.patent_title













