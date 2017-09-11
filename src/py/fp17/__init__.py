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
        if header.on_disk:
            headers["files"] += 1
            with open(header.globalname, 'r') as filehandler:
                headers["SLOC"] += sum(1 for line in filehandler)
    print('Headers:', headers['files'], '(' + str(headers['SLOC']) + '%)')
    enumerations = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, EnumerationProxy):
            enumerations['source'] += 1
            enumerations['wrapped'] += isinstance(node.boost_python_export, str)
    if enumerations['source'] > 0:
        print('Enumerations:', enumerations['source'], '(' + str(round(enumerations['wrapped'] / float(enumerations['source']) * 100, 2)) + '%)')
    variables = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, VariableProxy) and not isinstance(node, FieldProxy):
            variables['source'] += 1
            variables['wrapped'] += isinstance(node.boost_python_export, str)
    if variables['source'] > 0:
        print('Variables:', variables['source'], '(' + str(round(variables['wrapped'] / float(variables['source']) * 100, 2)) + '%)')
    fields = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, FieldProxy):
            fields['source'] += 1
            fields['wrapped'] += isinstance(node.boost_python_export, str)
    if fields['source'] > 0:
        print('Fields:', fields['source'], '(' + str(round(fields['wrapped'] / float(fields['source']) * 100, 2)) + '%)')
    functions = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, FunctionProxy) and not isinstance(node, MethodProxy):
            functions['source'] += 1
            functions['wrapped'] += isinstance(node.boost_python_export, str)
    if functions['source'] > 0:
        print('Functions:', functions['source'], '(' + str(round(functions['wrapped'] / float(functions['source']) * 100, 2)) + '%)')
    methods = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, MethodProxy):
            methods['source'] += 1
            methods['wrapped'] += isinstance(node.boost_python_export, str)
    if enumerations['source'] > 0:
        print('Methods:', methods['source'], '(' + str(round(methods['wrapped'] / float(methods['source']) * 100, 2)) + '%)')
    classes = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, ClassProxy):
            classes['source'] += 1
            classes['wrapped'] += isinstance(node.boost_python_export, str)
    if classes['source'] > 0:
        print('Classes:', classes['source'], '(' + str(round(classes['wrapped'] / float(classes['source']) * 100, 2)) + '%)')
    specializations = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, EnumerationProxy):
            specializations['source'] += 1
            specializations['wrapped'] += isinstance(node.boost_python_export, str)
    if specializations['source'] > 0:
        print('Specializations:', specializations['source'], '(' + str(round(specializations['wrapped'] / float(specializations['source']) * 100, 2)) + '%)')