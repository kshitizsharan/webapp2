import os
import openai
import re

key1= 'sk-rSTVWFtPfxKuFs7IXeRtT3'
key2='BlbkFJ50KJZ0UA8So2Z1k2iVS7'
openai.api_key = f"{key1}{key2}"





def generateBlogTopicsPipe(prompt1):
    article=[]
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Generate blog topics on: {}. \n \n 1.  ".format(prompt1),
      temperature=0.7,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    temp=response['choices'][0]['text'].split('?')
    length=len(temp)
    #for i in range(0,length):
    temp1=generateBlogTopics(temp[0])
    temp1=temp1.replace('\n','').replace('.','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
    temp1=temp1.split('?')


    temp2=generateBlogSections(temp1[0])
    #article.append(temp2)
    temp2=temp2.replace('-','')
    temp2=temp2.split(':')

    length=len(temp2)
    for i in range(0,length):
      temp3=blogSectionExpander(temp2[i])
      article.append(temp3)
      finalarticle=' '.join(article)


    #print(temp)
    #return response['choices'][0]['text']
    return finalarticle





def generateBlogTopics(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Generate blog topics on: {}. \n \n 1.  ".format(prompt1),
      temperature=0.7,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']

def generateBlogSections(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the blog title in to high level blog sections: {} \n\n- Introduction: ".format(prompt1),
      temperature=0.6,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']


def blogSectionExpander(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the blog section in to a detailed professional , witty and clever explanation.\n\n {}".format(prompt1),
      temperature=0.7,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']

#print(generateBlogTopicsPipe('Machine Learning')) 
