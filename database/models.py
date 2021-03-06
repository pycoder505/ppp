import sys
from django.db import models
from django.utils.text import slugify
reload(sys)
sys.setdefaultencoding('utf-8')


QLEVEL = (
    ('L1', 'LEVEL1'),
    ('L2', 'LEVEL2'),
    ('L3', 'LEVEL3'),
)


def url(self, filename):
    print self.question
    return "%s/%s" % (self.question, filename)


class Year(models.Model):
    date = models.DateField(unique=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return str(self.date)


class Company(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    about = models.CharField(max_length=10000, null=True)
    history = models.CharField(max_length=10000, null=True)
    why_join = models.CharField(max_length=10000, null=True)

    def __str__(self):
        return self.name

    def year_papers(self):
        years = Year.objects.all()
        paper_years = []
        for year in years:
            if Question.objects.filter(company__id=self.id, date=year):
                paper_years.append(year)
        return paper_years


class Topic(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class SubTopic(models.Model):
    topic = models.ForeignKey(Topic, related_name='subtopics')
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    reading = models.TextField(null=True)
    # meta_title = models.CharField(max_length=100, blank=True)
    # meta_description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Question(models.Model):
    data = models.CharField(max_length=10000, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to=url, blank=True, null=True)
    company = models.ManyToManyField(Company, blank=True, related_name="questions")
    sub_topic = models.ForeignKey(SubTopic, related_name='questions')
    level = models.CharField(choices=QLEVEL, max_length=10, default="L1")
    reference = models.ForeignKey(
        'self', null=True, blank=True, related_name='linked_questions')
    date = models.ManyToManyField(Year, blank=True)

    def __str__(self):
        from lxml import html
        doc = html.fromstring(self.data)
        # .decode('iso-8859-1').encode('utf8'))
        question_text = str(doc.text_content())
        return str(self.sub_topic.topic) + ":" + question_text[:100]

    def save(self, *args, **kwargs):
        if self.id:
            self.slug = slugify(str(self.id) + "/" + str(self).replace(":", "-", 1).replace("\n", " ").replace(" ", "-"))

        super(Question, self).save(*args, **kwargs)


class Choice(models.Model):
    description = models.CharField(max_length=10000)
    question = models.ForeignKey(Question, related_name='choices')
    image = models.ImageField(upload_to=url, blank=True, null=True)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.question)


class Answer(models.Model):
    explination = models.CharField(max_length=10000)
    image = models.ImageField(upload_to=url, blank=True, null=True)
    question = models.OneToOneField(Question, related_name='answers')

    def __str__(self):
        return str(self.question)
