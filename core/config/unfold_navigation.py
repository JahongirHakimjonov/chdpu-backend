from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def user_has_group_or_permission(user, permission):
    if user.is_superuser:
        return True

    group_names = user.groups.values_list("name", flat=True)
    if not group_names:
        return True

    return user.groups.filter(permissions__codename=permission).exists()


PAGES = [
    {
        "seperator": True,
        "items": [
            {
                "title": _("Bosh sahifa"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Foydalanuvchilar"),
        "items": [
            {
                "title": _("Guruhlar"),
                "icon": "person_add",
                "link": reverse_lazy("admin:auth_group_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_group"
                ),
            },
            {
                "title": _("Foydalanuvchilar"),
                "icon": "person_add",
                "link": reverse_lazy("admin:auth_user_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_user"
                ),
            },
            {
                "title": _("Site sozlamalari"),
                "icon": "person_add",
                "link": reverse_lazy("admin:sites_site_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_site"
                ),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Ma'lumotlar"),
        "items": [
            {
                "title": _("Fakultet haqida umumiy ma’lumot"),
                "icon": "info",
                "link": reverse_lazy("admin:backend_info_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_info"
                ),
            },
            {
                "title": _("Fakultet rahbariyati"),
                "icon": "school",
                "link": reverse_lazy("admin:backend_leadership_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_leadership"
                ),
            },
            {
                "title": _("Fakultet kafedralari va ularning faoliyati"),
                "icon": "fact_check",
                "link": reverse_lazy("admin:backend_chair_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_chair"
                ),
            },
            {
                "title": _("Fakultetning ilmiy-tadqiqot va innovatsion loyihalari"),
                "icon": "rebase_edit",
                "link": reverse_lazy("admin:backend_laboratory_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_laboratory"
                ),
            },
            {
                "title": _("Talabalar hayoti va tashkilotlari"),
                "icon": "settings_accessibility",
                "link": reverse_lazy("admin:backend_student_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_student"
                ),
            },
            {
                "title": _("Xalqaro hamkorlik va akademik almashinuv dasturlari"),
                "icon": "handshake",
                "link": reverse_lazy("admin:backend_cooperation_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_cooperation"
                ),
            },
            {
                "title": _("Multimedia va ijtimoiy tarmoqlar"),
                "icon": "add_a_photo",
                "link": reverse_lazy("admin:backend_interview_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_interview"
                ),
            },
            {
                "title": _("Fakultet yangiliklari va e’lonlar"),
                "icon": "campaign",
                "link": reverse_lazy("admin:backend_news_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_news"
                ),
            },
            {
                "title": _("Talabalarimizdan fikrlar"),
                "icon": "chat_bubble",
                "link": reverse_lazy("admin:backend_testimonial_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_testimonial"
                ),
            },
            {
                "title": _("Me'yoriy hujjatlar"),
                "icon": "description",
                "link": reverse_lazy("admin:backend_document_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_document"
                ),
            },
            {
                "title": _("O'quv binolari"),
                "icon": "apartment",
                "link": reverse_lazy("admin:backend_building_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_building"
                ),
            },
            {
                "title": _("Fakultetning ta’lim sifati va baholash tizimi"),
                "icon": "hotel_class",
                "link": reverse_lazy("admin:backend_rating_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_rating"
                ),
            },
            {
                "title": _("Qabul"),
                "icon": "calendar_month",
                "link": reverse_lazy("admin:backend_admission_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_admission"
                ),
            },
        ],
    },
]

TABS = [
    {
        "models": [
            "backend.news",
            "backend.newscategory",
        ],
        "items": [
            {
                "title": _("Fakultet yangiliklari va e’lonlar"),
                "link": reverse_lazy("admin:backend_news_changelist"),
            },
            {
                "title": _("Kategoriyalar"),
                "link": reverse_lazy("admin:backend_newscategory_changelist"),
            },
        ],
    },
    {
        "models": [
            "backend.chair",
            "backend.chairmember",
            "backend.chaircontact",
        ],
        "items": [
            {
                "title": _("Fakultet kafedralari va ularning faoliyati"),
                "link": reverse_lazy("admin:backend_chair_changelist"),
            },
            {
                "title": _("Hodimlar"),
                "link": reverse_lazy("admin:backend_chairmember_changelist"),
            },
            {
                "title": _("Kontaktlar"),
                "link": reverse_lazy("admin:backend_chaircontact_changelist"),
            },
        ],
    },
    {
        "models": [
            "backend.laboratory",
            "backend.laboratorygallery",
        ],
        "items": [
            {
                "title": _("Fakultetning ilmiy-tadqiqot va innovatsion loyihalari"),
                "link": reverse_lazy("admin:backend_laboratory_changelist"),
            },
            {
                "title": _("Galareya"),
                "link": reverse_lazy("admin:backend_laboratorygallery_changelist"),
            },
        ],
    },
    {
        "models": [
            "backend.leadership",
            "backend.worktimeline",
        ],
        "items": [
            {
                "title": _("Fakultet rahbariyati"),
                "link": reverse_lazy("admin:backend_leadership_changelist"),
            },
            {
                "title": _("Qabul kunlari"),
                "link": reverse_lazy("admin:backend_worktimeline_changelist"),
            },
        ],
    },
    {
        "models": [
            "backend.building",
            "backend.buildinggallery",
        ],
        "items": [
            {
                "title": _("O'quv binolari"),
                "link": reverse_lazy("admin:backend_building_changelist"),
            },
            {
                "title": _("Galareya"),
                "link": reverse_lazy("admin:backend_buildinggallery_changelist"),
            },
        ],
    },
]
