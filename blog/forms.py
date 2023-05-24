from django import forms
from tinymce.widgets import AdminTinyMCE, TinyMCE

from blog.models import Post


class AdminBlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'content': AdminTinyMCE(
                attrs={'rows': 30},
                mce_attrs={
                    "plugins": (
                        "paste autolink autosave image link media codesample table charmap hr anchor advlist lists "
                        "wordcount imagetools help quickbars emoticons",
                    ),
                    "toolbar": (
                        "undo redo | "
                        "bold italic underline strikethrough | "
                        "fontselect fontsizeselect formatselect | "
                        "alignleft aligncenter alignright alignjustify | "
                        "outdent indent table numlist bullist hr | "
                        "forecolor backcolor removeformat | "
                        "charmap emoticons | "
                        "insertfile image media link anchor codesample",
                    ),
                }
            )
        }
