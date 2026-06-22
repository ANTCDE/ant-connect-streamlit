# AUTO-GENERATED from ant-connect-ts types — do not edit manually.
# Regenerate: cd packages/ant-connect-ts && pnpm run generate:python-types

from __future__ import annotations

from enum import Enum, StrEnum
from typing import Any, Dict, Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, RootModel


class Model(RootModel[Any | None]):
    root: Any | None = None


class Source(StrEnum):
    resource = 'resource'
    local = 'local'
    timeseries = 'timeseries'


class Meta(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Meta1(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Meta2(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Meta3(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Type(BaseModel):
    key: str | None = None


class Meta4(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Meta5(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Permissions(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    configure: bool | None = None
    create: bool | None = None
    delete: bool | None = None
    read: bool | None = None
    update: bool | None = None


class Meta6(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class AssignableUser(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    email: str | None = None
    first_name: str | None = None
    id: str | None = None
    last_name: str | None = None


class Status(StrEnum):
    invited = 'invited'
    active = 'active'
    inactive = 'inactive'


class AssignedTo(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    email: str | None = None
    firstname: str | None = None
    id: str | None = None
    lastname: str | None = None
    mfa_required: bool | None = None
    name: str | None = None
    profile_picture: str | None = None
    status: Status | None = None


class TemplateSource(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    id: str | None = None
    title: str | None = None


class Meta7(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Meta8(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Change(StrEnum):
    created = 'created'
    updated = 'updated'
    deleted = 'deleted'
    trashed = 'trashed'
    restored = 'restored'


class ColumnType1(StrEnum):
    text = 'text'
    text_field = 'text-field'
    number = 'number'
    integer = 'integer'
    float = 'float'
    boolean = 'boolean'
    document = 'document'
    date = 'date'
    dropdown = 'dropdown'
    uuid = 'uuid'
    email = 'email'
    link = 'link'
    sbscode = 'sbscode'
    table = 'table'


class ColumnType(RootModel[str | ColumnType1 | None]):
    root: str | ColumnType1 | None = None


class Sbs(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    code: str | None = None


class DmsFilePermissions(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    dms_configure: bool | None = Field(None, alias='dms.configure')
    dms_delete: bool | None = Field(None, alias='dms.delete')
    dms_read: bool | None = Field(None, alias='dms.read')
    dms_upload: bool | None = Field(None, alias='dms.upload')


class File(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    extension: str | None = None
    file: str | None = None
    id: str | None = None
    mimetype: str | None = None
    name: str | None = None
    size: float | None = None


class FileResponse(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    extension: str | None = Field(
        None, description="File extension without leading dot (e.g. 'json', 'pdf')"
    )
    file: str | None = Field(None, description='Base64-encoded file content')
    id: str | None = None
    mimetype: str | None = None
    name: str | None = Field(None, description='File name including extension')
    project: str | None = None
    size: float | None = Field(None, description='File size in bytes')


class ImportProgressStatus(StrEnum):
    started = 'started'
    progress = 'progress'
    completed = 'completed'
    failed = 'failed'


class JobProgressStatus(StrEnum):
    started = 'started'
    progress = 'progress'
    completed = 'completed'
    failed = 'failed'
    canceled = 'canceled'


class Label(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    children: list[Label] | None = None
    color: str | None = None
    depth: float | None = None
    description: str | None = None
    icon: str | None = None
    id: str | None = None
    license_id: str | None = None
    name: str | None = None
    parent_id: str | None = None
    project_id: str | None = None


class LabelOperator(StrEnum):
    and_ = 'and'
    or_ = 'or'


class LabelTargetType(StrEnum):
    projects = 'projects'
    tasks = 'tasks'
    sbs = 'sbs'
    apps = 'apps'
    tables = 'tables'
    triggers = 'triggers'
    licenses = 'licenses'
    records = 'records'
    dms_files = 'dms_files'


class LicensePermissionMap(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    apps_configure: bool | None = Field(None, alias='apps.configure')
    projects_create: bool | None = Field(None, alias='projects.create')
    projects_delete: bool | None = Field(None, alias='projects.delete')
    projects_update: bool | None = Field(None, alias='projects.update')
    rbac_configure: bool | None = Field(None, alias='rbac.configure')
    tables_configure: bool | None = Field(None, alias='tables.configure')
    triggers_configure: bool | None = Field(None, alias='triggers.configure')
    triggers_read: bool | None = Field(None, alias='triggers.read')
    users_configure: bool | None = Field(None, alias='users.configure')


LicensePermissionMap.__annotations__['__pydantic_extra__'] = Dict[str, bool]
LicensePermissionMap.model_rebuild(force=True)


class LimitResourceType(StrEnum):
    records = 'records'
    total_records = 'total_records'
    tables = 'tables'
    projects = 'projects'
    users = 'users'
    rbac_roles = 'rbac_roles'
    dms_storage_mb = 'dms_storage_mb'
    sbs_records = 'sbs_records'
    triggers = 'triggers'


class LimitScope(StrEnum):
    table = 'table'
    project = 'project'
    license = 'license'


class LockUserInfo(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    id: str | None = None
    name: str | None = None
    profile_picture: str | None = None


class App(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    favorite: float | None = None
    id: str | None = None
    title: str | None = None


class NavigateToApp(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    app: App | None = None


class Type1(StrEnum):
    success = 'success'
    error = 'error'
    warning = 'warning'
    info = 'info'


class Notification(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    message: str | None = None
    type: Type1 | None = None


class ProjectPermissionMap(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    apps_configure: bool | None = Field(None, alias='apps.configure')
    rbac_configure: bool | None = Field(None, alias='rbac.configure')
    sbs_configure: bool | None = Field(None, alias='sbs.configure')
    tables_configure: bool | None = Field(None, alias='tables.configure')
    tasks_configure: bool | None = Field(None, alias='tasks.configure')
    tasks_read: bool | None = Field(None, alias='tasks.read')
    triggers_configure: bool | None = Field(None, alias='triggers.configure')
    triggers_read: bool | None = Field(None, alias='triggers.read')
    users_configure: bool | None = Field(None, alias='users.configure')
    users_read: bool | None = Field(None, alias='users.read')


ProjectPermissionMap.__annotations__['__pydantic_extra__'] = Dict[str, bool]
ProjectPermissionMap.model_rebuild(force=True)


class PropagationRunStatus(StrEnum):
    pending = 'pending'
    running = 'running'
    completed = 'completed'
    failed = 'failed'


class RecordDocument(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    document_id: str | None = Field(None, alias='documentId')
    name: str | None = None
    record_id: str | None = Field(None, alias='recordId')
    table_id: str | None = Field(None, alias='tableId')


class ReferenceTargetType(StrEnum):
    table = 'table'
    user = 'user'
    task = 'task'
    project = 'project'


class RelatedEntity(StrEnum):
    project = 'project'
    task = 'task'
    user = 'user'
    table = 'table'
    table_record = 'table_record'


class Pivot(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    created_at: str | None = None
    created_by: str | None = None
    label_os_id: str | None = None
    resource_id: str | None = None
    resource_type: str | None = None
    updated_at: str | None = None


class ResourceLabel(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    color: str | None = None
    icon: str | None = None
    id: str | None = None
    name: str | None = None
    pivot: Pivot | None = None


class ResourceLimitInfo(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    limit: float | None = Field(None, description='Maximum allowed (null = unlimited)')
    remaining: float | None = Field(
        None, description='Remaining capacity (null = unlimited)'
    )
    usage: float | None = Field(
        None, description='Current usage (count or MB depending on resource type)'
    )


class RouteSignal(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    path: str | None = None
    query: dict[str, str | list[str | None] | None] | None = None


class SbsRecord(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    children: list[SbsRecord] | None = None
    children_count: float | None = None
    code: str | None = None
    has_children: bool | float | None = Field(None, alias='hasChildren')
    id: str | None = None
    is_open: bool | None = Field(None, alias='isOpen')
    label: str | None = None
    level: float | None = None
    loading: bool | None = None
    parent: str | None = None
    parent_id: str | None = None


class CloseFilePreview(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    file_token: str | None = Field(None, alias='fileToken')


class CloseFlow(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    task_id: str | None = Field(None, alias='taskId')


class Hotkeys(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    ctrl: Literal[True] = True
    shift: Literal[True] = True


class Immersive(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    mode: bool | Literal['toggle'] | None = None


class Method(StrEnum):
    push = 'push'
    replace = 'replace'


class To(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    favorite: float | None = None


class Navigate(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    method: Method | None = None
    to: (
        Literal['OS.dash']
        | Literal['OS.login']
        | Literal['OS.profile']
        | str
        | To
        | NavigateToApp
        | None
    ) = Field(
        None,
        description='If it is one of the literals, it will try to navigate to that screen DEPRECATED If it is a string; it will assume a like-search for apps, so it will try to navigate to the first app it can find DEPRECATED Otherwise it will try to navigate to a favorite. Otherwise, it will look for an app with a specific ID, an app with a title (like & case-insensitive search), or a favorite index',
    )


class Notepad(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: bool | Literal['toggle'] | None = None


class Notifications(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: bool | Literal['toggle'] | None = None


class ScopeEnum(StrEnum):
    project = 'project'
    license = 'license'


class Type2(StrEnum):
    user = 'user'
    license = 'license'
    project = 'project'
    task = 'task'
    sbs = 'sbs'
    table = 'table'
    column = 'column'
    dms_file = 'dmsFile'
    project_task = 'projectTask'


class Observe(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    actions: list[Change] | None = None
    id: str | None = None
    random: str | None = None
    scope: list[ScopeEnum] | None = None
    type: str | Type2 | None = None


class OpenFilePreview(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    content_url: str | None = Field(
        None,
        alias='contentUrl',
        description='Pre-resolved content URL (blob or data URL). Skips DMS download when provided.',
    )
    created_at: str | None = Field(
        None, alias='createdAt', description='ISO date string — file creation date'
    )
    file_extension: str | None = Field(
        None,
        alias='fileExtension',
        description='File extension without dot (for details sidebar icon)',
    )
    file_name: str | None = Field(
        None, alias='fileName', description='Display name for the window title'
    )
    file_size: float | None = Field(
        None, alias='fileSize', description='File size in bytes (for details sidebar)'
    )
    file_token: str | None = Field(
        None,
        alias='fileToken',
        description='DMS file token to preview (used to resolve download URL)',
    )
    license_id: str | None = Field(
        None,
        alias='licenseId',
        description='License scope for download URL resolution (used when projectId is absent)',
    )
    owner_avatar: str | None = Field(
        None, alias='ownerAvatar', description='Owner avatar URL'
    )
    owner_name: str | None = Field(
        None, alias='ownerName', description='Owner display name'
    )
    project_id: str | None = Field(
        None, alias='projectId', description='Project scope for download URL resolution'
    )
    updated_at: str | None = Field(
        None, alias='updatedAt', description='ISO date string — last modified date'
    )


class OpenFlow(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    readonly: bool | None = Field(
        None, description='Open in read-only mode (locks all editing)'
    )
    task_id: str | None = Field(
        None, alias='taskId', description='The root task ID to open in the flow editor'
    )
    title: str | None = Field(
        None, description='Optional window title (falls back to task title)'
    )


class App1(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    id: str | None = None
    title: str | None = None


class Layout(StrEnum):
    h = 'h'
    v = 'v'


class Pane(Enum):
    number_0 = 0
    number_1 = 1


class OpenSplit(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    app: App1 | None = Field(
        None,
        description='App to open in the split pane — resolve by id or title (case-insensitive)',
    )
    layout: Layout | None = Field(
        None, description="Split direction: 'v' = side-by-side (default), 'h' = stacked"
    )
    pane: Pane | None = Field(
        None, description='Which pane: 0 = left/top, 1 = right/bottom. Defaults to 1.'
    )


class Select(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    project: str | None = None
    sbs: str | None = None
    task: str | None = None


class SubscribeChannel(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    channel: str | None = Field(
        None, description='The Echo channel name (e.g., "App.Table.{id}.Limits")'
    )
    events: list[str] | None = Field(
        None, description='Event names to listen for on this channel'
    )


class Scope(StrEnum):
    project = 'project'
    license = 'license'


class Topic(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    field_loop_break_id: str | None = Field(None, alias='_loopBreakId')
    data: Any | None = None
    name: str | None = None
    scope: Scope | None = None


class Unobserve(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    random: str | None = None


class UnsubscribeChannel(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    channel: str | None = Field(
        None, description='The Echo channel name to unsubscribe from'
    )


class TableLimits(RootModel[dict[str, ResourceLimitInfo]]):
    root: dict[str, ResourceLimitInfo]


class TableLockInfo(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    locked_at: str | None = None
    locked_by: LockUserInfo | None = None


class AssignedTo1(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    email: str | None = None
    firstname: str | None = None
    id: str | None = None
    lastname: str | None = None
    mfa_required: bool | None = None
    name: str | None = None
    profile_picture: str | None = None
    status: Status | None = None


class TaskApp(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    color: str | None = None
    icon: str | None = None
    id: str | None = None
    state: dict[str, str] | None = None
    title: str | None = None


class TaskLike(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    id: str | None = None


class TaskPriority(StrEnum):
    low = 'low'
    normal = 'normal'
    high = 'high'
    urgent = 'urgent'


class Params(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    mime_like: str | None = None
    min: float | None = None
    name_regex: str | None = None


class TaskRule(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: str | None = None
    id: str | None = None
    params: Params | None = None
    resource: Any = None
    resource_id: str | None = None
    resource_key: str | None = None
    resource_type: str | None = None


class TaskStatus(StrEnum):
    open = 'open'
    closed = 'closed'
    canceled = 'canceled'
    processing = 'processing'
    executed = 'executed'
    failed = 'failed'
    inactive = 'inactive'
    skipped = 'skipped'


class Event(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    code: str | None = None
    description: str | None = None
    id: str | None = None
    name: str | None = None


class TriggerBase(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    close_task_after_execution: bool | None = None
    event: Event | None = None
    id: str | None = None
    is_active: bool | None = None
    name: str | None = None


class UserShort(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    email: str | None = None
    firstname: str | None = None
    id: str | None = None
    lastname: str | None = None
    mfa_required: bool | None = None
    name: str | None = None
    profile_picture: str | None = None
    status: Status | None = None


class Meta9(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Data10(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    created_at: str | None = None
    display_name: str | None = None
    extension: str | None = None
    id: str | None = None
    is_folder: bool | None = None
    is_system: bool | None = None
    labels: list[Label] | None = None
    license_id: str | None = None
    name: str | None = None
    owner: UserShort | None = None
    owner_id: str | None = None
    parent_id: str | None = None
    path: str | None = None
    permissions: DmsFilePermissions | None = None
    project_id: str | None = None
    size: float | None = None
    token: str | None = None
    updated_at: str | None = None
    visibility: str | None = None


class Meta10(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Cause3CDmsFile3E(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data10 | None = None
    id: str | None = None
    meta: Meta10 | None = None


class Meta11(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Type3(BaseModel):
    key: str | None = None


class Meta12(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Data13(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    children: list[SbsRecord] | None = None
    children_count: float | None = None
    code: str | None = None
    has_children: bool | float | None = Field(None, alias='hasChildren')
    id: str | None = None
    is_open: bool | None = Field(None, alias='isOpen')
    label: str | None = None
    level: float | None = None
    loading: bool | None = None
    parent: str | None = None
    parent_id: str | None = None


class Meta13(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Cause3CSbsRecord3E(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data13 | None = None
    id: str | None = None
    meta: Meta13 | None = None


class Data14(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    history_enabled: bool | None = None
    id: str | None = None
    is_locked: bool | None = None
    labels: list[ResourceLabel] | None = None
    limits: TableLimits | None = Field(
        None,
        description='Resource limits for this table based on license type. Empty object for unlimited (enterprise) licenses.',
    )
    lock: TableLockInfo | None = None
    name: str | None = None
    permissions: Permissions | None = None
    project: str | None = None


class Meta14(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Cause3CTable3E(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data14 | None = None
    id: str | None = None
    meta: Meta14 | None = None


class AssignedTo2(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    email: str | None = None
    firstname: str | None = None
    id: str | None = None
    lastname: str | None = None
    mfa_required: bool | None = None
    name: str | None = None
    profile_picture: str | None = None
    status: Status | None = None


class Meta15(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Meta16(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    source: Source | None = None


class Cause(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: dict[str, Any] | None = Field(None, max_length=0)
    id: str | None = None
    meta: Meta | None = None


class Data1(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    created_at: str | None = None
    display_name: str | None = None
    extension: str | None = None
    id: str | None = None
    is_folder: bool | None = None
    is_system: bool | None = None
    labels: list[Label] | None = None
    license_id: str | None = None
    name: str | None = None
    owner: UserShort | None = None
    owner_id: str | None = None
    parent_id: str | None = None
    path: str | None = None
    permissions: DmsFilePermissions | None = None
    project_id: str | None = None
    size: float | None = None
    token: str | None = None
    updated_at: str | None = None
    visibility: str | None = None


class CauseDmsFile(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data1 | None = None
    id: str | None = None
    meta: Meta2 | None = None


class Data4(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    children: list[SbsRecord] | None = None
    children_count: float | None = None
    code: str | None = None
    has_children: bool | float | None = Field(None, alias='hasChildren')
    id: str | None = None
    is_open: bool | None = Field(None, alias='isOpen')
    label: str | None = None
    level: float | None = None
    loading: bool | None = None
    parent: str | None = None
    parent_id: str | None = None


class CauseSbsRecord(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data4 | None = None
    id: str | None = None
    meta: Meta5 | None = None


class Data5(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    history_enabled: bool | None = None
    id: str | None = None
    is_locked: bool | None = None
    labels: list[ResourceLabel] | None = None
    limits: TableLimits | None = Field(
        None,
        description='Resource limits for this table based on license type. Empty object for unlimited (enterprise) licenses.',
    )
    lock: TableLockInfo | None = None
    name: str | None = None
    permissions: Permissions | None = None
    project: str | None = None


class CauseTable(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data5 | None = None
    id: str | None = None
    meta: Meta6 | None = None


class ColumnReference(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    display_column_id: str | None = Field(
        None,
        description='UUID of the display column in the target table (table references only)',
    )
    display_field: str | None = Field(
        None,
        description="Field name to show for system entity references (e.g. 'name', 'email')",
    )
    id: str | None = None
    is_object_reference: bool | None = Field(
        None,
        description="True when target_type = 'table' and target_column_id is null (object reference)",
    )
    is_system_entity: bool | None = Field(
        None, description='True when target_type is user/task/project'
    )
    target_column_id: str | None = Field(
        None,
        description='UUID of the indexed column to match against (null = match on record id)',
    )
    target_table_id: str | None = Field(
        None,
        description="UUID of the target dynamic table (only set when target_type = 'table')",
    )
    target_type: ReferenceTargetType | None = None


class ColumnRelation(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    column_id: str | None = None
    created_at: str | None = None
    display_label: str | None = None
    id: str | None = None
    related_entity: RelatedEntity | None = None
    related_table_id: str | None = None
    updated_at: str | None = None


class DmsFile(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    created_at: str | None = None
    display_name: str | None = None
    extension: str | None = None
    id: str | None = None
    is_folder: bool | None = None
    is_system: bool | None = None
    labels: list[Label] | None = None
    license_id: str | None = None
    name: str | None = None
    owner: UserShort | None = None
    owner_id: str | None = None
    parent_id: str | None = None
    path: str | None = None
    permissions: DmsFilePermissions | None = None
    project_id: str | None = None
    size: float | None = None
    token: str | None = None
    updated_at: str | None = None
    visibility: str | None = None


class Data8(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    created_at: str | None = None
    display_name: str | None = None
    extension: str | None = None
    id: str | None = None
    is_folder: bool | None = None
    is_system: bool | None = None
    labels: list[Label] | None = None
    license_id: str | None = None
    name: str | None = None
    owner: UserShort | None = None
    owner_id: str | None = None
    parent_id: str | None = None
    path: str | None = None
    permissions: DmsFilePermissions | None = None
    project_id: str | None = None
    size: float | None = None
    token: str | None = None
    updated_at: str | None = None
    visibility: str | None = None


class DmsFileBatchChange(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: str | None = None
    data: Data8 | None = None
    id: str | None = None


class DmsFileBatchSignal(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    actor_id: str | None = None
    changes: list[DmsFileBatchChange] | None = None
    type: Literal['dmsFileBatch'] = 'dmsFileBatch'


class DmsGallery(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    files: list[DmsFile] | None = None
    index: float | None = None
    license_id: str | None = Field(None, alias='licenseId')
    project_id: str | None = Field(None, alias='projectId')


class ImportProgressEvent(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    error: str | None = None
    import_id: str | None = None
    message: str | None = None
    processed: float | None = None
    status: ImportProgressStatus | None = None
    table_id: str | None = None
    total: float | None = None


class JobProgressEvent(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    error: str | None = Field(
        None, description="Error message (when status is 'failed')"
    )
    job_id: str | None = Field(
        None, description='Unique identifier for this job instance'
    )
    job_type: str | None = Field(
        None,
        description="Type of job: 'import', 'generation', 'export', 'validation', etc.",
    )
    message: str | None = Field(None, description='Optional status message')
    phase: str | None = Field(
        None,
        description="Optional phase within the job (e.g., 'modules', 'elements', 'objects')",
    )
    processed: float | None = Field(
        None, description='Number of items processed so far'
    )
    resource_id: str | None = Field(
        None, description='ID of the resource (table_id, project_id, etc.)'
    )
    resource_type: str | None = Field(
        None,
        description="Type of resource being processed: 'records', 'modules', 'elements', etc.",
    )
    source: str | None = Field(
        None,
        description="App/feature name for notification context (e.g., 'Manual Import', 'Tables')",
    )
    status: JobProgressStatus | None = Field(None, description='Current job status')
    summary: dict[str, Any] | None = Field(
        None, description='Summary data (typically on completion)'
    )
    total: float | None = Field(None, description='Total number of items to process')


class LabelFilterState(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    include_children: bool | None = Field(None, alias='includeChildren')
    labels: list[str] | None = None
    operator: LabelOperator | None = None
    resources: list[LabelTargetType] | None = None


class LicenseLimits(RootModel[dict[str, ResourceLimitInfo]]):
    root: dict[str, ResourceLimitInfo]


class LimitChangeEvent(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    limits: ResourceLimitInfo | None = Field(None, description='Updated limit values')
    resource_id: str | None = Field(
        None,
        description='ID of the resource whose limit changed (table_id, project_id, license_id)',
    )
    resource_type: LimitResourceType | None = Field(
        None, description='Type of resource limit that changed'
    )
    scope: LimitScope | None = Field(
        None, description='Level at which this limit applies'
    )
    scope_id: str | None = Field(
        None,
        description='ID of the scope container (table_id, project_id, or license_id)',
    )


class ProjectLimits(RootModel[dict[str, ResourceLimitInfo]]):
    root: dict[str, ResourceLimitInfo]


class PropagationRun(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    created_at: str | None = None
    error: str | None = None
    finished_at: str | None = None
    id: str | None = None
    project_id: str | None = None
    started_at: str | None = None
    status: PropagationRunStatus | None = None
    template_id: str | None = None
    updated_at: str | None = None


class Table(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    history_enabled: bool | None = None
    id: str | None = None
    is_locked: bool | None = None
    labels: list[ResourceLabel] | None = None
    limits: TableLimits | None = Field(
        None,
        description='Resource limits for this table based on license type. Empty object for unlimited (enterprise) licenses.',
    )
    lock: TableLockInfo | None = None
    name: str | None = None
    permissions: Permissions | None = None
    project: str | None = None


class TaskAppendix(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    created_at: AwareDatetime | str | None = None
    deleted_at: AwareDatetime | str | None = None
    dms_file: DmsFile | None = None
    dms_file_link_id: str | None = None
    dms_readable: bool | None = Field(
        None,
        description='Whether the current user has DMS read permission (only set for DMS-backed files)',
    )
    extension: str | None = None
    id: str | None = None
    mimetype: str | None = None
    name: str | None = None
    size: float | None = None
    task: str | None = None


class Overlay(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: (
        bool | list[TaskAppendix] | TaskLike | DmsGallery | RecordDocument | None
    ) = None


class AuthLicense(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    company: str | None = None
    id: str | None = None
    is_admin: bool | None = None
    labels: list[ResourceLabel] | None = None
    limits: LicenseLimits | None = Field(
        None,
        description='Resource limits for this license based on its type. Empty object for unlimited (enterprise) licenses.',
    )
    mfa_required: bool | None = None
    name: str | None = None
    node_api_url: str | None = None
    node_base_url: str | None = None
    theme: str | None = None
    type: str | None = None
    url: str | None = None
    user_is_admin: bool | None = None
    user_permissions: LicensePermissionMap | None = None
    user_roles: list[Role] | None = None


class Data(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    column_reference: ColumnReference | None = None
    column_relation: ColumnRelation | None = None
    default_value: str | bool | None = None
    field_name: str | None = None
    has_relation: bool | None = None
    hint: str | None = None
    id: str | None = None
    is_indexed: bool | None = None
    is_unique: bool | None = None
    name: str | None = None
    options_value: list[str] | None = None
    order: float | None = None
    relation: TableRelation | None = None
    required: bool | None = None
    table: str | None = None
    type: ColumnType | None = None


class CauseColumn(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data | None = None
    id: str | None = None
    meta: Meta1 | None = None


class Data2(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    company: str | None = None
    id: str | None = None
    is_admin: bool | None = None
    labels: list[ResourceLabel] | None = None
    limits: LicenseLimits | None = Field(
        None,
        description='Resource limits for this license based on its type. Empty object for unlimited (enterprise) licenses.',
    )
    mfa_required: bool | None = None
    name: str | None = None
    node_api_url: str | None = None
    node_base_url: str | None = None
    theme: str | None = None
    type: str | None = None
    url: str | None = None
    user_is_admin: bool | None = None
    user_permissions: LicensePermissionMap | None = None
    user_roles: list[Role] | None = None


class CauseLicense(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data2 | None = None
    id: str | None = None
    meta: Meta3 | None = None


class Data3(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    created_at: str | None = None
    description: str | None = None
    field_values: dict[str, Any] | None = Field(
        None, description='Custom field values for this project, keyed by field key.'
    )
    id: str | None = None
    image: str | None = None
    image_src: str | FileResponse | None = Field(None, alias='imageSrc')
    is_archive: bool | None = None
    is_favorite: bool | None = None
    is_master: float | None = None
    labels: list[ResourceLabel] | None = None
    license: str | None = None
    limits: ProjectLimits | None = Field(
        None,
        description='Resource limits for this project based on license type. Empty object for unlimited (enterprise) licenses.',
    )
    name: str | None = None
    number: str | None = None
    propagation_runs: list[PropagationRun] | None = Field(
        None,
        description='Propagation runs for this project. Only present when with_propagation_runs=1 was passed.',
    )
    sbs_records: list[SbsRecord] | None = None
    slug: str | None = None
    tasks: list[Task] | None = None
    type: Type | None = Field(
        None,
        description='Combined type object returned by fetchProject: key + inlined field values.',
    )
    type_key: str | None = Field(
        None, description='The key of the project type assigned to this project.'
    )
    user_is_admin: bool | None = None
    user_permissions: ProjectPermissionMap | None = None
    user_roles: list[Role] | None = None


class CauseProject(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data3 | None = None
    id: str | None = None
    meta: Meta4 | None = None


class Data6(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    app: TaskApp | None = None
    appendixes: list[TaskAppendix] | None = None
    assignable_users: list[AssignableUser] | None = None
    assigned_to: AssignedTo | str | None = None
    attachments: list[TaskAppendix] | None = None
    attachments_count: float | None = None
    checks_count: float | None = None
    children: list[Task] | None = None
    children_count: float | None = None
    created_at: str | None = None
    created_by: UserShort | str | None = None
    description: str | None = None
    due: str | AwareDatetime | None = None
    duration_active_days: list[float] | None = None
    duration_days: float | None = None
    has_children: bool | None = Field(None, alias='hasChildren')
    id: str | None = None
    is_locked: bool | None = None
    is_private: bool | None = None
    is_task: bool | None = None
    is_template: bool | None = Field(
        None,
        description="New-system templates flag. Optional because legacy payloads don't set it. Added as part of the task templates MVP — see TASK_TEMPLATES_PLAN.md.",
    )
    labels: list[ResourceLabel] | None = None
    license: str | None = None
    location: str | None = None
    locked_by: str | None = None
    numbeed_start: str | None = None
    number: float | None = None
    parent: str | None = None
    parent_task: dict[str, Any] | None = None
    parents: dict[str, Any] | str | None = None
    planned_end: str | AwareDatetime | None = None
    planned_start: str | AwareDatetime | None = None
    plannr: float | None = None
    position_x: float | None = None
    position_y: float | None = None
    priority: TaskPriority | None = None
    progress: float | None = None
    project: str | None = None
    relations: list[Any] | None = None
    rules: list[TaskRule] | None = None
    sbs_record: SbsRecord | None = None
    sbscode: str | None = None
    script: str | None = None
    status: TaskStatus | None = None
    task_project: ProjectShort | None = None
    task_type: Any | None = None
    template_source: TemplateSource | None = Field(
        None,
        description="Eager-loaded source-template summary, when the backend includes it. Null when the task wasn't applied from a template.",
    )
    template_source_id: str | None = Field(
        None,
        description='Informational link back to the template a task was applied from. Only set on the new root when a template is applied into a project or license scope. No FK constraint and no versioning — just a one-way pointer for the "active templates" view.',
    )
    template_version_id: str | None = Field(
        None,
        description='Pointer to the specific template version a task was applied from. Used by the flow editor to detect when a newer version of the source template is available.',
    )
    title: str | None = None
    trigger: TriggerBase | None = None
    trigger_id: str | None = None
    type: Any | None = None


class CauseTask(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data6 | None = None
    id: str | None = None
    meta: Meta7 | None = None


class Data7(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    company_name: str | None = None
    email: str | None = None
    firstname: str | None = None
    id: str | None = None
    is_admin: bool | None = None
    language: str | None = None
    lastname: str | None = None
    licenses: list[AuthLicense] | None = None
    mfa_verified: float | bool | None = None
    name: str | None = None
    photo: File | str | None = None
    profile_picture: str | None = None
    two_factor_enabled: float | bool | None = None


class CauseUser(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data7 | None = None
    id: str | None = None
    meta: Meta8 | None = None


class ChangeSignal(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    column: Cause3CColumn3E | None = None
    dms_file: Cause3CDmsFile3E | None = Field(None, alias='dmsFile')
    license: Cause3CLicense3E | None = None
    project: Cause3CProject3E | None = None
    project_task: Cause3CTask3E | None = Field(None, alias='projectTask')
    sbs: Cause3CSbsRecord3E | None = None
    table: Cause3CTable3E | None = None
    task: Cause3CTask3E | None = None
    user: Cause3CUser3E | None = None


class Column(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    column_reference: ColumnReference | None = None
    column_relation: ColumnRelation | None = None
    default_value: str | bool | None = None
    field_name: str | None = None
    has_relation: bool | None = None
    hint: str | None = None
    id: str | None = None
    is_indexed: bool | None = None
    is_unique: bool | None = None
    name: str | None = None
    options_value: list[str] | None = None
    order: float | None = None
    relation: TableRelation | None = None
    required: bool | None = None
    table: str | None = None
    type: ColumnType | None = None


class Context(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    dark_mode: bool | None = Field(None, alias='darkMode')
    initial_route_query: dict[str, str] | None = Field(
        None,
        alias='initialRouteQuery',
        description='Initial URL query parameters at the time the app loaded — used for deep-link restoration.',
    )
    license: License | None = None
    notepad_task: Task | None = Field(None, alias='notepadTask')
    project: ProjectShort | None = None
    sbs: Sbs | None = None
    selected_labels: LabelFilterState | None = Field(None, alias='selectedLabels')
    selected_task: Task | None = Field(None, alias='selectedTask')
    task: Task | None = None
    tour_mode: bool | None = Field(
        None,
        alias='tourMode',
        description='True while the OS exploration tour is active. Apps use this to show TourZone overlays.',
    )
    user: User | None = None


class License(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    company: str | None = None
    id: str | None = None
    is_admin: bool | None = None
    labels: list[ResourceLabel] | None = None
    limits: LicenseLimits | None = Field(
        None,
        description='Resource limits for this license based on its type. Empty object for unlimited (enterprise) licenses.',
    )
    mfa_required: bool | None = None
    name: str | None = None
    node_api_url: str | None = None
    node_base_url: str | None = None
    theme: str | None = None
    type: str | None = None
    url: str | None = None
    user_is_admin: bool | None = None
    user_permissions: LicensePermissionMap | None = None
    user_roles: list[Role] | None = None


class Permission(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    created_at: str | None = None
    description: str | None = None
    id: str | None = None
    is_direct_permission: bool | None = None
    name: str | None = None
    resource_id: str | None = None
    resource_type: str | None = None
    roles: list[Role] | None = None
    updated_at: str | None = None


class ProjectShort(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    description: str | None = None
    id: str | None = None
    image: str | None = None
    image_src: str | FileResponse | None = Field(None, alias='imageSrc')
    labels: list[ResourceLabel] | None = None
    limits: ProjectLimits | None = Field(
        None,
        description='Resource limits for this project based on license type. Empty object for unlimited (enterprise) licenses.',
    )
    name: str | None = None
    number: str | None = None
    slug: str | None = None
    user_is_admin: bool | None = None
    user_permissions: ProjectPermissionMap | None = None
    user_roles: list[Role] | None = None


class Role(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    created_at: str | None = None
    description: str | None = None
    id: str | None = None
    is_admin: bool | None = None
    license_id: str | None = None
    name: str | None = None
    permissions: list[Permission] | None = None
    resource_id: str | None = None
    resource_type: str | None = None
    updated_at: str | None = None
    users: list[User] | None = None


class Signal(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    close_file_preview: CloseFilePreview | None = Field(
        None,
        alias='closeFilePreview',
        description='Request ant-os to close a file preview window.',
    )
    close_flow: CloseFlow | None = Field(
        None, alias='closeFlow', description='Request ant-os to close a flow window.'
    )
    column: Cause3CColumn3E | None = None
    dms_file: Cause3CDmsFile3E | None = Field(None, alias='dmsFile')
    dms_file_batch: DmsFileBatchSignal | None = Field(None, alias='dmsFileBatch')
    hotkeys: Hotkeys | None = None
    immersive: Immersive | None = None
    import_progress: ImportProgressEvent | None = Field(
        None,
        alias='importProgress',
        description='Import progress events relayed from WebSocket Sent by ant-os when async import progress is received',
    )
    job_progress: JobProgressEvent | None = Field(
        None,
        alias='jobProgress',
        description='Generic job progress events relayed from WebSocket Sent by ant-os when async job progress is received (generation, export, validation, etc.)',
    )
    license: Cause3CLicense3E | None = None
    limit_change: LimitChangeEvent | None = Field(
        None,
        alias='limitChange',
        description='Resource limit change events relayed from WebSocket Sent by ant-os when resource limits change (record created/deleted, project created, etc.)',
    )
    navigate: Navigate | None = None
    notepad: Notepad | None = None
    notifications: Notifications | None = None
    observe: Observe | None = None
    open_file_preview: OpenFilePreview | None = Field(
        None,
        alias='openFilePreview',
        description='Request ant-os to open a DMS file preview in a floating window. Supports images and PDFs — unsupported types trigger a download instead.',
    )
    open_flow: OpenFlow | None = Field(
        None,
        alias='openFlow',
        description="Request ant-os to open a flow/workflow in a floating window. Can be sent from any app via signals to show a task's flow editor.",
    )
    open_split: OpenSplit | None = Field(
        None,
        alias='openSplit',
        description='Request ant-os to open an app in split-screen mode alongside the current app. The current app stays in pane 0; the requested app opens in pane 1 by default.',
    )
    overlay: Overlay | None = None
    ping: Literal[True] = True
    pong: Literal[True] = True
    project: Cause3CProject3E | None = None
    project_task: Cause3CTask3E | None = Field(None, alias='projectTask')
    resource: dict[str, Cause] | None = Field(
        None,
        description="Arbitrary entity change signals for app-defined resource types. Observed via `signal.with('homeowner', id, actions, scope)`. Echo-backed through a generic `App.Project.{id}.Resources` channel.",
    )
    route: RouteSignal | None = None
    sbs: Cause3CSbsRecord3E | None = None
    select: Select | None = None
    subscribe_channel: SubscribeChannel | None = Field(
        None,
        alias='subscribeChannel',
        description='Request ant-os to subscribe to an Echo channel on behalf of the app. Events received on the channel will be relayed back via signals.',
    )
    table: Cause3CTable3E | None = None
    task: Cause3CTask3E | None = None
    topic: Topic | None = Field(
        None,
        description='Generic topic pub/sub via Echo whisper (client events). Sends a message to all other subscribers on the same topic — sender excluded. Topic name must match [a-zA-Z0-9_-] (no dots).',
    )
    unobserve: Unobserve | None = None
    unsubscribe_channel: UnsubscribeChannel | None = Field(
        None,
        alias='unsubscribeChannel',
        description='Request ant-os to unsubscribe from an Echo channel.',
    )
    user: Cause3CUser3E | None = None


class TableRelation(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    column: Column | None = None
    id: str | None = None
    project: str | None = None
    related_column: Column | None = None
    related_project: str | None = None
    related_table: Table | None = None
    table: str | None = None


class Task(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    app: TaskApp | None = None
    appendixes: list[TaskAppendix] | None = None
    assignable_users: list[AssignableUser] | None = None
    assigned_to: AssignedTo1 | str | None = None
    attachments: list[TaskAppendix] | None = None
    attachments_count: float | None = None
    checks_count: float | None = None
    children: list[Task] | None = None
    children_count: float | None = None
    created_at: str | None = None
    created_by: UserShort | str | None = None
    description: str | None = None
    due: str | AwareDatetime | None = None
    duration_active_days: list[float] | None = None
    duration_days: float | None = None
    has_children: bool | None = Field(None, alias='hasChildren')
    id: str | None = None
    is_locked: bool | None = None
    is_private: bool | None = None
    is_task: bool | None = None
    is_template: bool | None = Field(
        None,
        description="New-system templates flag. Optional because legacy payloads don't set it. Added as part of the task templates MVP — see TASK_TEMPLATES_PLAN.md.",
    )
    labels: list[ResourceLabel] | None = None
    license: str | None = None
    location: str | None = None
    locked_by: str | None = None
    numbeed_start: str | None = None
    number: float | None = None
    parent: str | None = None
    parent_task: dict[str, Any] | None = None
    parents: dict[str, Any] | str | None = None
    planned_end: str | AwareDatetime | None = None
    planned_start: str | AwareDatetime | None = None
    plannr: float | None = None
    position_x: float | None = None
    position_y: float | None = None
    priority: TaskPriority | None = None
    progress: float | None = None
    project: str | None = None
    relations: list[Any] | None = None
    rules: list[TaskRule] | None = None
    sbs_record: SbsRecord | None = None
    sbscode: str | None = None
    script: str | None = None
    status: TaskStatus | None = None
    task_project: ProjectShort | None = None
    task_type: Any | None = None
    template_source: TemplateSource | None = Field(
        None,
        description="Eager-loaded source-template summary, when the backend includes it. Null when the task wasn't applied from a template.",
    )
    template_source_id: str | None = Field(
        None,
        description='Informational link back to the template a task was applied from. Only set on the new root when a template is applied into a project or license scope. No FK constraint and no versioning — just a one-way pointer for the "active templates" view.',
    )
    template_version_id: str | None = Field(
        None,
        description='Pointer to the specific template version a task was applied from. Used by the flow editor to detect when a newer version of the source template is available.',
    )
    title: str | None = None
    trigger: TriggerBase | None = None
    trigger_id: str | None = None
    type: Any | None = None


class User(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    company_name: str | None = None
    email: str | None = None
    firstname: str | None = None
    id: str | None = None
    is_admin: bool | None = None
    language: str | None = None
    lastname: str | None = None
    licenses: list[AuthLicense] | None = None
    mfa_verified: float | bool | None = None
    name: str | None = None
    photo: File | str | None = None
    profile_picture: str | None = None
    two_factor_enabled: float | bool | None = None


class Data9(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    column_reference: ColumnReference | None = None
    column_relation: ColumnRelation | None = None
    default_value: str | bool | None = None
    field_name: str | None = None
    has_relation: bool | None = None
    hint: str | None = None
    id: str | None = None
    is_indexed: bool | None = None
    is_unique: bool | None = None
    name: str | None = None
    options_value: list[str] | None = None
    order: float | None = None
    relation: TableRelation | None = None
    required: bool | None = None
    table: str | None = None
    type: ColumnType | None = None


class Cause3CColumn3E(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data9 | None = None
    id: str | None = None
    meta: Meta9 | None = None


class Data11(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    company: str | None = None
    id: str | None = None
    is_admin: bool | None = None
    labels: list[ResourceLabel] | None = None
    limits: LicenseLimits | None = Field(
        None,
        description='Resource limits for this license based on its type. Empty object for unlimited (enterprise) licenses.',
    )
    mfa_required: bool | None = None
    name: str | None = None
    node_api_url: str | None = None
    node_base_url: str | None = None
    theme: str | None = None
    type: str | None = None
    url: str | None = None
    user_is_admin: bool | None = None
    user_permissions: LicensePermissionMap | None = None
    user_roles: list[Role] | None = None


class Cause3CLicense3E(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data11 | None = None
    id: str | None = None
    meta: Meta11 | None = None


class Data12(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    created_at: str | None = None
    description: str | None = None
    field_values: dict[str, Any] | None = Field(
        None, description='Custom field values for this project, keyed by field key.'
    )
    id: str | None = None
    image: str | None = None
    image_src: str | FileResponse | None = Field(None, alias='imageSrc')
    is_archive: bool | None = None
    is_favorite: bool | None = None
    is_master: float | None = None
    labels: list[ResourceLabel] | None = None
    license: str | None = None
    limits: ProjectLimits | None = Field(
        None,
        description='Resource limits for this project based on license type. Empty object for unlimited (enterprise) licenses.',
    )
    name: str | None = None
    number: str | None = None
    propagation_runs: list[PropagationRun] | None = Field(
        None,
        description='Propagation runs for this project. Only present when with_propagation_runs=1 was passed.',
    )
    sbs_records: list[SbsRecord] | None = None
    slug: str | None = None
    tasks: list[Task] | None = None
    type: Type3 | None = Field(
        None,
        description='Combined type object returned by fetchProject: key + inlined field values.',
    )
    type_key: str | None = Field(
        None, description='The key of the project type assigned to this project.'
    )
    user_is_admin: bool | None = None
    user_permissions: ProjectPermissionMap | None = None
    user_roles: list[Role] | None = None


class Cause3CProject3E(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data12 | None = None
    id: str | None = None
    meta: Meta12 | None = None


class Data15(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    app: TaskApp | None = None
    appendixes: list[TaskAppendix] | None = None
    assignable_users: list[AssignableUser] | None = None
    assigned_to: AssignedTo2 | str | None = None
    attachments: list[TaskAppendix] | None = None
    attachments_count: float | None = None
    checks_count: float | None = None
    children: list[Task] | None = None
    children_count: float | None = None
    created_at: str | None = None
    created_by: UserShort | str | None = None
    description: str | None = None
    due: str | AwareDatetime | None = None
    duration_active_days: list[float] | None = None
    duration_days: float | None = None
    has_children: bool | None = Field(None, alias='hasChildren')
    id: str | None = None
    is_locked: bool | None = None
    is_private: bool | None = None
    is_task: bool | None = None
    is_template: bool | None = Field(
        None,
        description="New-system templates flag. Optional because legacy payloads don't set it. Added as part of the task templates MVP — see TASK_TEMPLATES_PLAN.md.",
    )
    labels: list[ResourceLabel] | None = None
    license: str | None = None
    location: str | None = None
    locked_by: str | None = None
    numbeed_start: str | None = None
    number: float | None = None
    parent: str | None = None
    parent_task: dict[str, Any] | None = None
    parents: dict[str, Any] | str | None = None
    planned_end: str | AwareDatetime | None = None
    planned_start: str | AwareDatetime | None = None
    plannr: float | None = None
    position_x: float | None = None
    position_y: float | None = None
    priority: TaskPriority | None = None
    progress: float | None = None
    project: str | None = None
    relations: list[Any] | None = None
    rules: list[TaskRule] | None = None
    sbs_record: SbsRecord | None = None
    sbscode: str | None = None
    script: str | None = None
    status: TaskStatus | None = None
    task_project: ProjectShort | None = None
    task_type: Any | None = None
    template_source: TemplateSource | None = Field(
        None,
        description="Eager-loaded source-template summary, when the backend includes it. Null when the task wasn't applied from a template.",
    )
    template_source_id: str | None = Field(
        None,
        description='Informational link back to the template a task was applied from. Only set on the new root when a template is applied into a project or license scope. No FK constraint and no versioning — just a one-way pointer for the "active templates" view.',
    )
    template_version_id: str | None = Field(
        None,
        description='Pointer to the specific template version a task was applied from. Used by the flow editor to detect when a newer version of the source template is available.',
    )
    title: str | None = None
    trigger: TriggerBase | None = None
    trigger_id: str | None = None
    type: Any | None = None


class Cause3CTask3E(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data15 | None = None
    id: str | None = None
    meta: Meta15 | None = None


class Data16(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    company_name: str | None = None
    email: str | None = None
    firstname: str | None = None
    id: str | None = None
    is_admin: bool | None = None
    language: str | None = None
    lastname: str | None = None
    licenses: list[AuthLicense] | None = None
    mfa_verified: float | bool | None = None
    name: str | None = None
    photo: File | str | None = None
    profile_picture: str | None = None
    two_factor_enabled: float | bool | None = None


class Cause3CUser3E(BaseModel):
    model_config = ConfigDict(
        extra='ignore', populate_by_name=True,
    )
    action: Change | None = None
    data: Data16 | None = None
    id: str | None = None
    meta: Meta16 | None = None


Label.model_rebuild()
SbsRecord.model_rebuild()
AuthLicense.model_rebuild()
Data.model_rebuild()
Data2.model_rebuild()
Data3.model_rebuild()
Data6.model_rebuild()
ChangeSignal.model_rebuild()
Column.model_rebuild()
Context.model_rebuild()
License.model_rebuild()
Permission.model_rebuild()
ProjectShort.model_rebuild()
Role.model_rebuild()
Signal.model_rebuild()
