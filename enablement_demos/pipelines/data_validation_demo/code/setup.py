from setuptools import setup, find_packages
setup(
    name = 'data_validation_demo',
    version = '1.0',
    packages = find_packages(include = ('data_validation_demo*', )) + ['prophecy_config_instances.data_validation_demo'],
    package_dir = {'prophecy_config_instances.data_validation_demo' : 'configs/resources/data_validation_demo'},
    package_data = {'prophecy_config_instances.data_validation_demo' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.37'],
    entry_points = {
'console_scripts' : [
'main = data_validation_demo.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
