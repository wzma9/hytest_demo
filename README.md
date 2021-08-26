# hytest自动测试框架功能展示
       1.用例存放在cases中
       2. __st__.py中suite_setup,suite_teardown用来进行整个用例目录级的初始化、清除操作
       3.用例文件中suite_setup,suite_teardown用来进行当前用例文件的初始化、清除操作
       4.单个测试用例（class）中用 setup,teardown用来进行单个用例的初始化、清除操作
## force_tags 列表用来存放用例标签，可根据标签选择用例执行
       1 放在__st__文件中，整个目录下用例都获得相同标签
       2 放在 单个用例文件中，当前整个文件中用例都获得相同标签
       3 单个用例（class）用 tags 来添加标签
         执行方法，hytest --tag tag_name
                  hytest --nottag tag_name （非）
                  hytest --tag "'tag_name1' and 'tag_name2'" （与）
                  hytest --tag tag_name1 tag_name2   (或）
 ## name 用例名称
      根据名称选择用例执行
          hytest --test name
 ## INFO('') 将INFO中内容打印在自动生成的报告中
 ## STEP(1,'desc') 步骤说明，会打印在报告中
 ## CHECK_POINT('desc', bool) 断言
