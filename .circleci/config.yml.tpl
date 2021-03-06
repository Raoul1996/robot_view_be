image_config: &image_config	# 配置

  IMAGE_NAME: robot_view	# 镜像名
  DEV_SERVICE_NAME: robot_view_dev	# develop 分支对应的 service 名
  MASTER_SERVICE_NAME: robot_view_beta # master 分支对应的 service 名
  PROD_SERVICE_NAME: robot_view	# prod 分支对应的 service 名

version: 2
jobs:
  test:
    docker:
      # specify the version you desire here
      # use `-browsers` prefix for selenium tests, e.g. `3.6.1-browsers`
      - image: circleci/python:3.6.1
      # Specify service dependencies here if necessary
      # CircleCI maintains a library of pre-built images
      # documented at https://circleci.com/docs/2.0/circleci-images/

    working_directory: ~/repo

    steps:
      - checkout

      # Download and cache dependencies
      - restore_cache:
          keys:
          - v1-dependencies-{{ checksum "requirements.txt" }}
          # fallback to using the latest cache if no exact match is found
          - v1-dependencies-

      - run:
          name: install dependencies
          command: |
            python3 -m venv venv
            . venv/bin/activate
            pip install -r requirements.txt

      - save_cache:
          paths:
            - ./venv
          key: v1-dependencies-{{ checksum "requirements.txt" }}
      - run:
          name: make makemigrations
          command: |
            . venv/bin/activate
            python manage.py makemigrations snippets --settings=robot_view.test_settings
      - run:
          name: migrate
          command: |
            . venv/bin/activate
            python manage.py migrate --settings=robot_view.test_settings
      # run tests!
      # this example uses Django's built-in test-runner
      # other common Python testing frameworks include pytest and nose
      # https://pytest.org
      # https://nose.readthedocs.io
      - run:
          name: run tests
          command: |
            . venv/bin/activate
            python manage.py test --settings=robot_view.test_settings
      - store_test_results:
          path: test-reports
      - store_artifacts:
          path: test-reports
          destination: test-reports
#  build-example:
#    machine:
#      docker_layer_caching: true
#    environment:
#      <<: *image_config
#
#    steps:	# 登陆私有 dockerhub 并构建和上传镜像
#      - checkout
#      - run: docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD hkccr.ccs.tencentyun.com
#      - run: docker build -t hkccr.ccs.tencentyun.com/xxx/$IMAGE_NAME:$CIRCLE_BRANCH-${CIRCLE_SHA1:0:7} .
#      - run: docker push hkccr.ccs.tencentyun.com/xxx/$IMAGE_NAME:$CIRCLE_BRANCH-${CIRCLE_SHA1:0:7}
#      - store_artifacts:
#          path: Dockerfile
#  deploy-example:
#    machine: true
#    environment:
#      <<: *image_config
#    steps:
#      - add_ssh_keys:	# 需要在 CircleCI 里面进行 SSH 密钥配置，在此处指定 fingerprints
#          fingerprints:
#            - "09:2f:cb:df:27:bd:c6:5a:e4:f4:21:06:9a:d8:ed:g1"
#      - run:
#          name: Deploying
#          command: |	# 根据当前分支名更新相应的服务
#            if [ $CIRCLE_BRANCH == "master" ]; then
#              ssh root@11.11.11.11 docker service update $PROD_SERVICE_NAME --image hkccr.ccs.tencentyun.com/xxx/$IMAGE_NAME:$CIRCLE_BRANCH-${CIRCLE_SHA1:0:7}
#            else
#              ssh root@11.11.11.11 docker service update $DEV_SERVICE_NAME --image hkccr.ccs.tencentyun.com/xxx/$IMAGE_NAME:$CIRCLE_BRANCH-${CIRCLE_SHA1:0:7}
#            fi
workflows:
  version: 2
  test_build_deploy:
    jobs:
      - test
#      - build:
#          filters:
#            branches:
#              only:	# 只对 develop 和 master 分支进行 build
#                - master
#                - prod
#          requires:
#            - test	# 需要 test 通过才能执行
#      - deploy:
#          requires:
#            - build
