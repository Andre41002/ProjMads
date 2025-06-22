from setuptools import setup, find_packages

setup(
    requires=["setuptools","wheel"],
    build_backend = "setuptools.build_meta",
    name='gestao-alunos',
    version='0.1.1',
    packages=find_packages(),
    install_requires=['tabulate'],
    author='Grupo 2 MADS 2ano',
    author_email='a041011@example.com',
    description='Sistema de gestão de alunos, docentes, turmas e disciplinas.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/a041002/gestao-alunos',    
    python_requires='>=3.6',
    

)
