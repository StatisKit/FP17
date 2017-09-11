from autowig.asg import (EnumerationProxy,
                         VariableProxy,
                         FieldProxy,
                         FunctionProxy,
                         MethodProxy,
                         ClassProxy,
                         ClassTemplateSpecializationProxy,
                         ClassTemplateProxy)

def report(asg):
    headers = dict(files = 0, SLOC = 0)
    for header in asg.files(header = True):
        headers["files"] += 1
        with open(header.globalname, 'r') as filehandler:
            headers["SLOC"] += sum(1 for line in filehandler)
    print('Headers:', headers['files'], '(' + headers['SLOC'] + ')')
    enumerations = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, EnumerationProxy):
            enumerations['source'] += 1
            enumerations['wrapped'] += isinstance(node.boost_python_export, str)
    print('Enumerations:', enumerations['source'], '(' + round(enumerations['wrapped'] / float(enumerations['source']) * 100, 2) + ')')
    variables = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, VariableProxy) and not isinstance(node, FieldProxy):
            variables['source'] += 1
            variables['wrapped'] += isinstance(node.boost_python_export, str)
    print('Variables:', variables['source'], '(' + round(variables['wrapped'] / float(variables['source']) * 100, 2) + ')')
    fields = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, FieldProxy):
            fields['source'] += 1
            fields['wrapped'] += isinstance(node.boost_python_export, str)
    print('Fields:', fields['source'], '(' + round(fields['wrapped'] / float(fields['source']) * 100, 2) + ')')
    functions = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, FunctionProxy) and not isinstance(node, MethodProxy):
            functions['source'] += 1
            functions['wrapped'] += isinstance(node.boost_python_export, str)
    print('Functions:', functions['source'], '(' + round(functions['wrapped'] / float(functions['source']) * 100, 2) + ')')
    methods = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, MethodProxy):
            methods['source'] += 1
            methods['wrapped'] += isinstance(node.boost_python_export, str)
    print('Methods:', methods['source'], '(' + round(methods['wrapped'] / float(methods['source']) * 100, 2) + ')')
    classes = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, ClassProxy):
            classes['source'] += 1
            classes['wrapped'] += isinstance(node.boost_python_export, str)
    print('Classes:', classes['source'], '(' + round(classes['wrapped'] / float(classes['source']) * 100, 2) + ')')
    specializations = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, EnumerationProxy):
            specializations['source'] += 1
            specializations['wrapped'] += isinstance(node.boost_python_export, str)
    print('Specializations:', specializations['source'], '(' + round(specializations['wrapped'] / float(specializations['source']) * 100, 2) + ')')