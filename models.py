# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActionShape(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.ForeignKey('Actions', models.DO_NOTHING)
    shape = models.ForeignKey('Shapes', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'action_shape'


class Actions(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    content = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type_action = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions'


class Attachments(models.Model):
    id = models.BigAutoField(primary_key=True)
    format = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    model_type = models.IntegerField(blank=True, null=True)
    attachmentable_type = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    attachmentable_id = models.BigIntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachments'


class Backups(models.Model):
    id = models.BigAutoField(primary_key=True)
    route = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.BooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'backups'


class Capsules(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    url_image = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    link = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'capsules'


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    code = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class DetailsProgress(models.Model):
    id = models.BigAutoField(primary_key=True)
    progress = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    last_progress = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    error_points = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    game_time = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    completado = models.BooleanField(blank=True, null=True)
    progress_0 = models.ForeignKey('Progress', models.DO_NOTHING, db_column='progress_id')  # Field renamed because of name conflict.
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details_progress'


class EquipmentFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipment = models.ForeignKey('Equipments', models.DO_NOTHING)
    file = models.ForeignKey('Files', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment_file'


class EquipmentVirtualPlant(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipment = models.ForeignKey('Equipments', models.DO_NOTHING)
    virtual_plant = models.ForeignKey('VirtualPlants', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment_virtual_plant'


class Equipments(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name_english = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    main = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cover = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    gift = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description_1 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description_2 = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    url_iteractivo = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    video = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    video_imagen = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    file = models.ForeignKey('Files', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipments'


class ExamQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    exam = models.ForeignKey('Exams', models.DO_NOTHING)
    question = models.ForeignKey('Questions', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_question'


class ExamQuestionParents(models.Model):
    id = models.BigAutoField(primary_key=True)
    number_questions = models.IntegerField()
    type = models.IntegerField()
    exam = models.ForeignKey('Exams', models.DO_NOTHING)
    level = models.ForeignKey('Levels', models.DO_NOTHING, blank=True, null=True)
    file = models.ForeignKey('Files', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_question_parents'


class ExamResults(models.Model):
    id = models.BigAutoField(primary_key=True)
    correct = models.IntegerField(blank=True, null=True)
    incorrect = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    state = models.IntegerField()
    exam = models.ForeignKey('Exams', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_results'


class ExamTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_types'


class Exams(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    begind_date = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    end_date = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    state = models.IntegerField()
    exam_type = models.ForeignKey(ExamTypes, models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exams'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    connection = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    queue = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    payload = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    exception = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Files(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    description = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tag = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    code_primary = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    code_secondary = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    icon_url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cover_url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    documenttype = models.IntegerField(db_column='documentType', blank=True, null=True)  # Field name made lowercase.
    file_url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    slug = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    level = models.ForeignKey('Levels', models.DO_NOTHING, blank=True, null=True)
    is_pdf = models.BooleanField(blank=True, null=True)
    is_video = models.BooleanField(blank=True, null=True)
    have_questions = models.BooleanField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'


class Historicals(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    tag = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cover_url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    file_url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    revision = models.IntegerField()
    principal = models.BooleanField(blank=True, null=True)
    file = models.ForeignKey(Files, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historicals'


class Icons(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    tag = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icons'


class Images(models.Model):
    id = models.BigAutoField(primary_key=True)
    format = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    url = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    level = models.ForeignKey('Levels', models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'


class Interlug(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_shape_from = models.ForeignKey('Shapes', models.DO_NOTHING, db_column='id_shape_from')
    id_shape_to = models.ForeignKey('Shapes', models.DO_NOTHING, db_column='id_shape_to')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interlug'


class Levels(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    imgurl = models.TextField(db_column='imgUrl', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'levels'


class MapShape(models.Model):
    id = models.BigAutoField(primary_key=True)
    shape = models.ForeignKey('Shapes', models.DO_NOTHING)
    map = models.ForeignKey('Maps', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_shape'


class MapTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_types'


class Maps(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tag = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    imagesvg_url = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type_data = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    location = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    coordinates = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    color = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    procedure = models.ForeignKey('Procedures', models.DO_NOTHING)
    type = models.ForeignKey(MapTypes, models.DO_NOTHING)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maps'


class Migrations(models.Model):
    migration = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Options(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    answer = models.IntegerField(blank=True, null=True)
    question = models.ForeignKey('Questions', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'options'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    token = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PermissionRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    permission = models.ForeignKey('Permissions', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permission_role'


class Permissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    slug = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class Procedures(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    code = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    file = models.ForeignKey(Files, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedures'


class Progress(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    capsule = models.ForeignKey(Capsules, models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'progress'


class QuestionLevels(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_levels'


class QuestionResults(models.Model):
    id = models.BigAutoField(primary_key=True)
    answer = models.IntegerField()
    question = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    option = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    exam_result = models.ForeignKey(ExamResults, models.DO_NOTHING)
    question_0 = models.ForeignKey('Questions', models.DO_NOTHING, db_column='question_id')  # Field renamed because of name conflict.
    option_0 = models.ForeignKey(Options, models.DO_NOTHING, db_column='option_id', blank=True, null=True)  # Field renamed because of name conflict.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_results'


class Questions(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    file = models.ForeignKey(Files, models.DO_NOTHING)
    question_level = models.ForeignKey(QuestionLevels, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class RoleUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_user'


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    slug = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    full_access = models.BooleanField(db_column='full-access', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    system_type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class ScoreDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    level = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    score = models.IntegerField()
    score_0 = models.ForeignKey('Scores', models.DO_NOTHING, db_column='score_id')  # Field renamed because of name conflict.
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'score_details'


class Scores(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.IntegerField()
    last_score = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    capsule = models.ForeignKey(Capsules, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scores'


class Sessions(models.Model):
    id = models.CharField(primary_key=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    user_id = models.BigIntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    user_agent = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    payload = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Shapes(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_shape = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    instrument_shape = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tag = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cause_shape = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    solution_shape = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    types_shape = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    information_shape = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    coordinates_shape = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type_shape = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    color_shape = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    state_shape = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shapes'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Troubleshooting(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    attributed_cause = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    superintendent = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    supervisor = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    operators = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    downtime = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    details = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    take_actions = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    results = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    equipment = models.ForeignKey(Equipments, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'troubleshooting'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    surname = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    phone = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    system_type = models.IntegerField()
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    remember_token = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sso = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Versions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_table = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    action = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    original_url = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'versions'


class VirtualPlants(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    image = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    location = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    coordinates_plant = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    file = models.ForeignKey(Files, models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'virtual_plants'


class WebsocketsStatisticsEntries(models.Model):
    app_id = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    peak_connection_count = models.IntegerField()
    websocket_message_count = models.IntegerField()
    api_message_count = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'websockets_statistics_entries'
