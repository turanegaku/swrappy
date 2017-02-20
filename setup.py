from setuptools import setup

if __name__ == '__main__':
    setup(name='swrappy',
            version='0.0.1',
            description='Slack API Wrapper by Python',
            url='http://github.com/turanegaku/swrappy',
            author='turanegaku',
            author_email='turanegaku@gmail.com',
            license='MIT',
            packages=['swrappy'],
            install_requires=[
                'ws4py',
                'requests'],
            zip_safe=False)
