from .combined_component import CombinedComponent
from fasthtml.common import Button, Form, Div

# Assign an explicit alias fallback to match the rest of the file's internal calls
def Group(*args, **kwargs):
    kwargs['cls'] = f"group {kwargs.get('cls', '')}".strip()
    return Div(*args, **kwargs)


class FormGroup(CombinedComponent):

    id = ""
    action = ""
    method = ""
    children = []
    button_label = "Submit"

    def call_children(self, userid, model):
        children = super().call_children(userid, model)
        children.append(Button(self.button_label))

        return children

    def outer_div(self, children, div_args):

        return Form(Group(*children), **div_args)
    
    def div_args(self, userid, model):

        return {
            'id': self.id,
            'action': self.action,
            'method': self.method,
            }