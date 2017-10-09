import six
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
            if six.PY2:
                with open(header.globalname, 'r') as filehandler:
                    headers["SLOC"] += sum(1 for line in filehandler)
            else:
                with open(header.globalname, 'r', errors='ignore') as filehandler:
                    headers["SLOC"] += sum(1 for line in filehandler)
    print('Headers: ' + str(headers['files']) + ' (' + str(headers['SLOC']) + ' SLOC)')
    enumerations = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, EnumerationProxy) and not node.access in ['protected', 'private']:
            enumerations['source'] += 1
            enumerations['wrapped'] +=int(node.boost_python_export and (not isinstance(node.boost_python_export, bool) or not isinstance(node.parent.boost_python_export, bool)))
    if enumerations['source'] > 0:
        print('Enumerations: ' + str(enumerations['source']) + ' (' + enumerations['wrapped']) + ' wrapped)')
    variables = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, VariableProxy) and not node.access in ['protected', 'private']:
            variables['source'] += 1
            variables['wrapped'] += int(node.boost_python_export and (not isinstance(node.boost_python_export, bool) or not isinstance(node.parent.boost_python_export, bool)))
    if variables['source'] > 0:
        print('Variables: ' + str(variables['source']) + ' (' + str(variables['wrapped']) + ' wrapped)')
    functions = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, FunctionProxy) and not node.access in ['protected', 'private']:
            functions['source'] += 1
            functions['wrapped'] += int(node.boost_python_export and (not isinstance(node.boost_python_export, bool) or not isinstance(node.parent.boost_python_export, bool)))
    if functions['source'] > 0:
        print('Functions: ' + str(functions['source']) + ' (' + str(functions['wrapped']) + ' wrapped)')
    classes = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, ClassProxy) and not node.access in ['protected', 'private']:
            classes['source'] += 1
            classes['wrapped'] += int(node.boost_python_export and not isinstance(node.boost_python_export, bool))
    if classes['source'] > 0:
        print('Classes: ' + str(classes['source']) + ' (' + str(classes['wrapped']) + ' wrapped)')
    specializations = dict(source = 0, wrapped = 0)
    for node in asg.nodes():
        if isinstance(node, ClassTemplateSpecializationProxy) and not node.access in ['protected', 'private']:
            specializations['source'] += 1
            specializations['wrapped'] += int(node.boost_python_export and not isinstance(node.boost_python_export, bool))
    if specializations['source'] > 0:
        print('Specializations: ' + str(specializations['source']) + ' (' + str(round(specializations['wrapped'] / float(specializations['source']) * 100, 2)) + '%)')
