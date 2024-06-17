def inject_generic_repr(cls):
    """ Injects a generic repr function """
    def generic_repr(that):
        class_items = [f'{k}={v}' for k, v in that.__dict__.items()]
        return f'<{that.__class__.__name__} ' + ', '.join(class_items) + '>'

    cls.__repr__ = generic_repr
    return cls
