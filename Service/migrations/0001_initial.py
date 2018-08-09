# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='接口名称', max_length=32)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='接口描述')),
                ('doc', models.CharField(verbose_name='接口文档路径', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='CMDBUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('username', models.CharField(verbose_name='用户账号', max_length=32)),
                ('password', models.CharField(verbose_name='用户密码', max_length=32)),
                ('nickname', models.CharField(verbose_name='用户姓名', max_length=32)),
                ('phone', models.CharField(verbose_name='用户手机号', max_length=11)),
                ('email', models.EmailField(verbose_name='用户邮箱', max_length=254)),
                ('photo', models.ImageField(verbose_name='用户头像', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('processor', models.CharField(blank=True, max_length=32, null=True)),
                ('vendor_id', models.CharField(blank=True, max_length=32, null=True)),
                ('cpu_family', models.CharField(blank=True, max_length=32, null=True)),
                ('model', models.CharField(blank=True, max_length=32, null=True)),
                ('model_name', models.CharField(blank=True, max_length=32, null=True)),
                ('stepping', models.CharField(blank=True, max_length=32, null=True)),
                ('microcode', models.CharField(blank=True, max_length=32, null=True)),
                ('cpu_MHz', models.CharField(blank=True, max_length=32, null=True)),
                ('cache_size', models.CharField(blank=True, max_length=32, null=True)),
                ('physical_id', models.CharField(blank=True, max_length=32, null=True)),
                ('siblings', models.CharField(blank=True, max_length=32, null=True)),
                ('core_id', models.CharField(blank=True, max_length=32, null=True)),
                ('cpu_cores', models.CharField(blank=True, max_length=32, null=True)),
                ('apicid', models.CharField(blank=True, max_length=32, null=True)),
                ('initial_apicid', models.CharField(blank=True, max_length=32, null=True)),
                ('fpu', models.CharField(blank=True, max_length=32, null=True)),
                ('fpu_exception', models.CharField(blank=True, max_length=32, null=True)),
                ('cpuid_level', models.CharField(blank=True, max_length=32, null=True)),
                ('wp', models.CharField(blank=True, max_length=32, null=True)),
                ('flags', models.TextField(blank=True, max_length=32, null=True)),
                ('bogomips', models.CharField(blank=True, max_length=32, null=True)),
                ('clflush_size', models.CharField(blank=True, max_length=32, null=True)),
                ('cache_alignment', models.CharField(blank=True, max_length=32, null=True)),
                ('address_sizes', models.CharField(blank=True, max_length=32, null=True)),
                ('power_management', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('MemTota', models.CharField(blank=True, max_length=32, null=True)),
                ('MemFree', models.CharField(blank=True, max_length=32, null=True)),
                ('MemAvailable', models.CharField(blank=True, max_length=32, null=True)),
                ('Buffers', models.CharField(blank=True, max_length=32, null=True)),
                ('Cached', models.CharField(blank=True, max_length=32, null=True)),
                ('SwapCached', models.CharField(blank=True, max_length=32, null=True)),
                ('Active', models.CharField(blank=True, max_length=32, null=True)),
                ('Inactive', models.CharField(blank=True, max_length=32, null=True)),
                ('Active_anon', models.CharField(blank=True, max_length=32, null=True)),
                ('Inactive_anon', models.CharField(blank=True, max_length=32, null=True)),
                ('Active_file', models.CharField(blank=True, max_length=32, null=True)),
                ('Inactive_file', models.CharField(blank=True, max_length=32, null=True)),
                ('Unevictable', models.CharField(blank=True, max_length=32, null=True)),
                ('Mlocked', models.CharField(blank=True, max_length=32, null=True)),
                ('SwapTotal', models.CharField(blank=True, max_length=32, null=True)),
                ('SwapFree', models.CharField(blank=True, max_length=32, null=True)),
                ('Dirty', models.CharField(blank=True, max_length=32, null=True)),
                ('Writeback', models.CharField(blank=True, max_length=32, null=True)),
                ('AnonPages', models.CharField(blank=True, max_length=32, null=True)),
                ('Mapped', models.CharField(blank=True, max_length=32, null=True)),
                ('Shmem', models.CharField(blank=True, max_length=32, null=True)),
                ('Slab', models.CharField(blank=True, max_length=32, null=True)),
                ('SReclaimable', models.CharField(blank=True, max_length=32, null=True)),
                ('SUnreclaim', models.CharField(blank=True, max_length=32, null=True)),
                ('KernelStack', models.CharField(blank=True, max_length=32, null=True)),
                ('PageTables', models.CharField(blank=True, max_length=32, null=True)),
                ('NFS_Unstable', models.CharField(blank=True, max_length=32, null=True)),
                ('Bounce', models.CharField(blank=True, max_length=32, null=True)),
                ('WritebackTmp', models.CharField(blank=True, max_length=32, null=True)),
                ('CommitLimit', models.CharField(blank=True, max_length=32, null=True)),
                ('Committed_AS', models.CharField(blank=True, max_length=32, null=True)),
                ('VmallocTotal', models.CharField(blank=True, max_length=32, null=True)),
                ('VmallocUsed', models.CharField(blank=True, max_length=32, null=True)),
                ('VmallocChunk', models.CharField(blank=True, max_length=32, null=True)),
                ('HardwareCorrupted', models.CharField(blank=True, max_length=32, null=True)),
                ('AnonHugePages', models.CharField(blank=True, max_length=32, null=True)),
                ('HugePages_Total', models.CharField(blank=True, max_length=32, null=True)),
                ('HugePages_Free', models.CharField(blank=True, max_length=32, null=True)),
                ('HugePages_Rsvd', models.CharField(blank=True, max_length=32, null=True)),
                ('HugePages_Surp', models.CharField(blank=True, max_length=32, null=True)),
                ('Hugepagesize', models.CharField(blank=True, max_length=32, null=True)),
                ('DirectMap4k', models.CharField(blank=True, max_length=32, null=True)),
                ('DirectMap2M', models.CharField(blank=True, max_length=32, null=True)),
                ('DirectMap1G', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('ip', models.CharField(verbose_name='服务器ip', max_length=32)),
                ('mac', models.CharField(verbose_name='服务器物理地址', max_length=32)),
                ('cpu', models.CharField(verbose_name='服务器CPU', max_length=32)),
                ('memory', models.CharField(verbose_name='服务器内存', max_length=32)),
                ('disk', models.CharField(verbose_name='服务器磁盘', max_length=32)),
                ('isalive', models.CharField(verbose_name='服务器状态', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Cpu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('service_id', models.IntegerField()),
                ('cpu_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service_Memory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('service_id', models.IntegerField()),
                ('memory_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='cmdbuser',
            name='service',
            field=models.ManyToManyField(to='Service.Service'),
        ),
    ]
