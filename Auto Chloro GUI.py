# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:49:27 2021

@authors: Md. Farhadul Islam & Sarah Zabeen
"""


from easygui import *
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import sys

detection=load_model('auto_chloro_model.h5')

# message to be displayed  
text = 'স্বাগতম, প্রিয় ব্যবহারকারী\
\nআপনার ফসলের (পাতা জাতীয়) রোগ এবং রোগের প্রতিকার জানার জন্য, পাতার একটি ছবি তুলে\
\n*ছবি সিলেক্ট করুন* বাটনে ক্লিক করে সেই ছবি আপলোড করুন।'

# show logo
img="auto-chloro.PNG"

# window title 
title = "File Open-Path"
  
# button list 
button_list = [] 
  
# button 1 
button1 = "ছবি সিলেক্ট করুন"
button2 = "বন্ধ করুন"

# appending button to the button list 
button_list.append(button1) 
button_list.append(button2)


  
# creating a button box 
output = buttonbox(msg=text, title=title,image=img, choices=button_list) 
if output=='ছবি সিলেক্ট করুন':
    txt=''
    path=fileopenbox()
    pred = buttonbox(msg="রোগটি নির্ধারণ করতে ছবিতে ক্লিক করুন", title='Detection',image=path,choices=('Cancel',)) 
    if pred!=path:
        sys.exit()
        
    test_img=image.load_img(path,target_size=(48,48))
    test_img=image.img_to_array(test_img)
    test_img=np.expand_dims(test_img,axis=0) 
    result=detection.predict(test_img)
    a=result.argmax()
    classes=['Pepper__bell___Bacterial_spot images',
             'Pepper__bell___healthy images',
             'Potato___Early_blight images',
             'Potato___healthy images',
             'Potato___Late_blight images',
             'Tomato_Bacterial_spot images',
             'Tomato_Early_blight images',
             'Tomato_healthy images',
             'Tomato_Late_blight images',
             'Tomato_Leaf_Mold images',
             'Tomato_Septoria_leaf_spot images',
             'Tomato_Spider_mites_Two_spotted_spider_mite images',
             'Tomato__Target_Spot images',
             'Tomato__Tomato_mosaic_virus images',
             'Tomato__Tomato_YellowLeaf__Curl_Virus images']
    category=[]
    for i in classes:
          category.append(i)
    for i in range(len(classes)):
           if(i==a):
                output=category[i]
    if output=='Pepper__bell___Bacterial_spot images':
        output='ঘণ্টামরিচ/ক্যাপ্সিকামের ব্যাকটেরিয়াজনিত দাগ রোগ'
        txt='জৈবিক নিয়ন্ত্রণ: \n\nব্যাকটেরিয়াজনিত দাগের দমন ব্যবস্থা খুব জটিল এবং ব্যয়বহুল। \
যদি মরশুমের শুরুতে এ রোগ দেখা দেয়, তবে সমগ্র ফসল নষ্ট করে দেওয়া ভাল। \
কপার সমৃদ্ধ ব্যাকটেরিয়ানাশক, ফল ও পত্রপল্লবের উপর একটি  রক্ষণাত্মক আবরণ তৈরি করে। \
ব্যাকটেরিয়াল ভাইরাস (  ব্যাকটেরিওফাজ) প্রতিষেধক বাজারে পাওয়া যায় যা নির্দিষ্ট ব্যাকটেরিয়াকে মেরে ফেলে। \
১.৩ % সোডিয়াম হাইপোক্লোরাইট (sodium hypochlorite) দ্রবনে ১ মিনিট বা গরম জলে (৫০ ডিগ্রি সেলসিয়াস) বীজ ২৫ মিনিট ডুবিয়ে রাখুন। \
\n\nরাসায়নিক নিয়ন্ত্রণ: \
\n\nসম্ভবমতো সমন্বিত বালাই ব্যবস্থাপনার আওতায় জৈবিক নিয়ন্ত্রণের মাধ্যমে সর্বদা প্রতিরোধের ব্যবস্থা নিন। \
শুধুমাত্র কপার সংগঠিত ব্যাকটেরিয়ানাশকের  ব্যবহার করে রোগ প্রতিরোধ করা সম্ভব এবং আংশিক ভাবে রোগ দমন হয়। \
রোগ দেখা দেওয়ার সাথে সাথে স্প্রে করতে হবে, এবং ১০-১৪ দিন  পর পর উষ্ণ ও আর্দ্র পরিবেশে প্রয়োগ করতে হবে। \
ম্যানকোজেব ও কপার সমৃদ্ধ মিশ্র  বালাইনাশক কিছুটা  ভালো সুরক্ষা দিতে পারে। '
        
    elif output=='Potato___Early_blight images':
        output='আলুর আগাম ধ্বসা রোগ'
        txt='জৈবিক নিয়ন্ত্রণ: \n\nব্যাসিলাস সাবটিলিস সমন্বিত পদার্থ অথবা তাম্র-উপাদান ভিত্তিক \
জৈব ছত্রাকনাশক হিসেবে স্বীকৃত যা এই রোগের বিরুদ্ধে প্রয়োগ করা যায়। \
\n\nরাসায়নিক নিয়ন্ত্রণ: \
\n\nসম্ভবমত সমম্বিত বালাই ব্যবস্থাপনার আওতায় জৈবিক নিয়ন্ত্রণের মাধ্যমে প্রতিরোধের ব্যবস্থা নিন। \
বাজারে বিভিন্ন প্রকারের ছত্রাকনাশক পাওয়া যায় যা আলুর আশুধ্বসা রোগ নিয়ন্ত্রণ করতে পারে। \
অ্যাজোক্সিট্রবিন, পাইরাক্লোস্ট্রোবিন, ডাইফেনকোনাজল, বস্কালিড, ক্লোরোথ্যালোনিল,  ফেনামিডোন, ম্যানেব, ম্যানকোজেব, ট্রাইফ্লক্সিস্ট্রবিন, \
ও জিরান ইত্যাদি ছত্রাকনাশক আলুর আশুধ্বসা রোগ নিয়ন্ত্রণে ব্যবহার করা হয়। \
পর্যায়ক্রমে বিভিন্ন ধরণের রাসায়নিক মিশ্রণ ব্যবহারের সুপারিশ রয়েছে।  উপযুক্ত আবহাওয়ায় সময়মতো সকল পরিচর্যা শেষ করুন। \
এ উপাদানগুলো প্রয়োগ করার পর, ফসল সংগ্রহের পূর্বে একটি বিরতি দিন যাতে স্বাস্থ্যের জন্য নিরাপদ থাকে। '
        
    elif output=='Potato___Late_blight images':
        output='আলুর নাবী ধ্বসা রোগ'
        txt='জৈবিক নিয়ন্ত্রণ: \n\nশুষ্ক আবহাওয়া শুরু হওয়ার আগেই কপার নির্ভর ছত্রাকনাশক প্রয়োগ করুন। \
পাতায় জৈব আচ্ছাদনকারী পদার্থ স্প্রে করেও সংক্রমণের হাত থেকে রক্ষা পাওয়া যেতে পারে। \
\n\nরাসায়নিক নিয়ন্ত্রণ: \
\n\n সমন্বিত বালাই ব্যবস্থাপনার আওতায় জৈবিক নিয়ন্ত্রনের মাধ্যমে সর্বদা প্রতিরোধের ব্যবস্থা নিন। \
মাঠের সর্বত্র বিশেষ করে আর্দ্র অংশগুলোতে নাবীধ্বসা রোগ নিয়ন্ত্রণ করতে ছত্রাকনাশক ব্যবহার করা জরুরী। \
সংশ্লিষ্ট ছত্রাকনাশক যেটা পাতাকে ঢেকে রাখে সেটা সংক্রমণের পূর্বে অনেক কার্যকরী এবং ছত্রাককে ছত্রাকনাশকের বিরুদ্ধে প্রতিরোধ গড়ে তুলতে দেয় না। \
প্রতিরোধমূলক ব্যবস্থার জন্য ম্যান্ডিপ্রোপামিড (mandipropamid), ক্লোরোথালোনিল (chlorothalonil), ফ্লুয়াজিনাম (fluazinam), \
ট্রাইফিনাইলটিন (triphenyltin), অথবা ম্যানকোজেব (mancozeb) সংঘটিত ছত্রাকনাশক ব্যবহার করা যেতে পারে। \
বীজ বপনের পূর্বেই ছত্রাকনাশক যেমন ম্যানকোজেব দ্বারা বীজ শোধন করে নিলেও কাজ হয়। '
        
    elif output=='Tomato_Bacterial_spot images':
        output='টমেটোর ব্যাকটেরিয়াজনিত দাগ রোগ'
        txt='জৈবিক নিয়ন্ত্রণ: \n\nব্যাকটেরিয়ার দাগ রোগ দমন খুবই কঠিন এবং ব্যয়বহুল। \
রোগ যদি মরশুমের শুরুতে আক্রমণ করে তাহলে পুরো জমি নষ্ট করে ফেলে। কপার সংঘটিত উপাদানের ব্যাকটেরিয়ানাশক \
পাতা এবং ফলে প্রতিষেধক হিসাবে ব্যবহার করা হয়। ব্যাকটেরিয়াভোজী ভাইরাস (ব্যাকটেরিওফাজেস) যা ব্যাকটেরিয়া মেরে ফেলে \
তা সব সময় পাওয়া যায়। এক মিনিটের জন্য ১.৩% সোডিয়াম হাইপোক্লোরাইট বা গরম জলে (৫০ ডিগ্রী সেন্টিগ্রেড) ২৫  মিনিটের জন্য  \
বীজ ডুবিয়ে রাখলে রোগের সংক্রমণ কমাতে পারে। \
\n\nরাসায়নিক নিয়ন্ত্রণ: \
\n\nসম্ভবমতো সমন্বিত বালাই ব্যবস্থাপনার আওতায় জৈবিক নিয়ন্ত্রণের মাধ্যমে রোগ প্রতিরোধের ব্যবস্থা নিন। \
কপার সংঘটিত উপাদানের ব্যাকটেরিয়ানাশক প্রতিষেধক হিসাবে ব্যবহার করা হয় এবং আংশিক রোগ \
নিয়ন্ত্রণ প্রদান করতে পারে। প্রথম  লক্ষণ দেখার সাথে সাথে ব্যাকটেরিয়ানাশক প্রয়োগ করুন এবং \
তারপর উষ্ণ [ক্ষুদ্র দাগ/ঠাণ্ডা (দাগ)], আর্দ্র আবহাওয়া থাকলে ১০ থেকে ১৪ দিন পর পর প্রয়োগ করতে হবে। \
যেহেতু কপারের ধারাবাহিক ব্যবহারের কারণে ব্যাকটেরিয়া প্রতিরোধী ব্যবস্থা গড়ে তোলে তাই কপার সংঘটিত উপাদানের \
ব্যাকটেরিয়ানাশকের সাথে ম্যানকোজেব ব্যবহারের সুপারিশ করা হয়। '
        
    elif output=='Tomato_Early_blight images':
        output='টমেটোর আগাম ধ্বসা রোগ'
        txt='জৈবিক নিয়ন্ত্রণ: \n\nব্যাসিলাস সাবটিলিস সমন্বিত পদার্থ অথবা তাম্র-উপাদান ভিত্তিক \
জৈব ছত্রাকনাশক হিসেবে স্বীকৃত যা এই রোগের বিরুদ্ধে প্রয়োগ করা যায়। \
\n\nরাসায়নিক নিয়ন্ত্রণ: \
\n\nসম্ভবমত সমম্বিত বালাই ব্যবস্থাপনার আওতায় জৈবিক নিয়ন্ত্রণের মাধ্যমে প্রতিরোধের ব্যবস্থা নিন। \
বাজারে বিভিন্ন প্রকারের ছত্রাকনাশক পাওয়া যায় যা আলুর আশুধ্বসা রোগ নিয়ন্ত্রণ করতে পারে। \
অ্যাজোক্সিট্রবিন, পাইরাক্লোস্ট্রোবিন, ডাইফেনকোনাজল, বস্কালিড, ক্লোরোথ্যালোনিল,  ফেনামিডোন, ম্যানেব, ম্যানকোজেব, ট্রাইফ্লক্সিস্ট্রবিন, \
ও জিরান ইত্যাদি ছত্রাকনাশক আলুর আশুধ্বসা রোগ নিয়ন্ত্রণে ব্যবহার করা হয়। \
পর্যায়ক্রমে বিভিন্ন ধরণের রাসায়নিক মিশ্রণ ব্যবহারের সুপারিশ রয়েছে।  উপযুক্ত আবহাওয়ায় সময়মতো সকল পরিচর্যা শেষ করুন। \
এ উপাদানগুলো প্রয়োগ করার পর, ফসল সংগ্রহের পূর্বে একটি বিরতি দিন যাতে স্বাস্থ্যের জন্য নিরাপদ থাকে। '
        
    elif output=='Tomato_Late_blight images':
        output='টমেটোর নাবী ধ্বসা রোগ'
        txt='জৈবিক নিয়ন্ত্রণ: \n\nঅদ্যাবধি  নাবীধ্বসা রোগের বিরুদ্ধে কোন জৈবিক প্রতিরোধ ব্যবস্থা কার্যকরী হয়েছে বলে জানা যায়নি। \
রোগের বিস্তার এড়াতে, সংক্রামিত স্থানের ফসল অবিলম্বে অপসারণ করুন বা ধ্বংস করুন এবং সংক্রামিত ফসল \
থেকে জৈবসার তৈরীতে বিরত থাকুন। \
\n\nরাসায়নিক নিয়ন্ত্রণ: \
\n\nসমন্বিত বালাই ব্যবস্থাপনার আওতায় জৈবিক নিয়ন্ত্রণের মাধ্যমে রোগ প্রতিরোধের ব্যবস্থা নিন। \
নাবীধ্বসা রোগ প্রতিরোধে ম্যান্ডিপ্রোপামিড,  ক্লোরোথ্যালোনিল, ফ্লুয়াজিনাম, এবং  ম্যানকোজেব  সংগঠিত উপাদানের ছত্রাকনাশক স্প্রে করুন। \
গাছের উপর থেকে জলসেচ দিলে বা বছরের যে সময়ে অতি বৃষ্টিপাত হয়, সে সময় ছত্রাকনাশক প্রয়োগ করতে হয়। '
        
    elif output=='Tomato_Leaf_Mold images':
        output='টমেটো পাতার ছত্রাক রোগ\n'
        txt='জৈবিক নিয়ন্ত্রণ: \n\nজীবাণুমুক্ত করার জন্য গরম জল (১২২ ডিগ্রি ফারেনহাইট বা ৫০ ডিগ্রি সেলসিয়াস তাপমাত্রায় ২৫ মিনিট)\
দিয়ে বীজ শোধন করার পরামর্শ রয়েছে। এক্রেমোনিয়াম স্ট্রিকটাম, ডাইসিমা পালভিন্যাটা, ট্রাইকোডার্মা হারজিনাম\
বা ট্রাইকোডার্মা ভিরিডি এবং ট্রাইকোথেসিয়াম রোসিয়াম ছত্রাক মাইকোভেলোসিলা ফালভার শত্রু এবং এর দমনে সেগুলো ব্যবহার করা যায়।\
গ্রীণহাউজে এক্রেমোনিয়াম স্ট্রিকটাম, ট্রাইকোডার্মা ভিরিডির স্ট্রেইন ৩ এবং ট্রাইকোথেসিয়াম রোসিয়াম যথাক্রমে ৫৩, ৬৬ এবং ৮৪ শতাংশ\
হারে প্রয়োগে টমেটোর মাইকোভেলোসিলা ফালভা দমন হয়। ছোট পরিসরে, আপেল সিডার, রসুন বা দুধ এবং ভিনিগার মিশ্রণ\
এ ছত্রাক দমনে ব্যবহার করা যেতে পারে। \
\n\nরাসায়নিক নিয়ন্ত্রণ: \
\n\nসম্ভমবমতো সমন্বিত বালাই ব্যবস্থাপনার আওতায় জৈবিক নিয়ন্ত্রণের মাধ্যমে সর্বদা প্রতিরোধের ব্যবস্থা নিন। রোগ বৃদ্ধির জন্য অনুকুল আবহাওয়া বিরাজ করলে\
সংক্রমণের পূর্বেই ছত্রাকনাশক ছিটাতে হবে। ক্লোরথ্যালোনিল (chlorothalonil), ম্যানেব (maneb), ম্যানকোজেব (mancozeb) এবং \
কপার ঘটিত ছত্রাক নাশক মাঠে ব্যবহার করার জন্য পরামর্শ দেওয়া হয়ে থাকে। গ্রীণহাউজের জন্য ডাইফেনোকোনাজল (difenoconazole),\
ম্যাণ্ডিপ্রোপামিড (mandipropamid), সাইমোক্স্যানিল (cymoxanil), ফ্যামোক্স্যাডন (famoxadone) এবং সাইপ্রোডাইনিল (cyprodinil)\
ব্যবহারের পরামর্শ দেওয়া হয়। '
    
    elif output=='Tomato_Septoria_leaf_spot images':
        output='জৈবিক নিয়ন্ত্রণ: \n\nটমেটোর সেপটোরিয়া দাগ রোগ\n'
        txt='কপার সংঘঠিত ছত্রাকনাশক, যেমন – বোর্দো মিশ্রণ, কপার হাইড্রক্সাইড , কপার সালফেট ,\
অথবা কপার অক্সিক্লোরাইড সালফেট  এ রোগের জীবাণু নিয়ন্ত্রণে সাহায্য করতে পারে।\
৭ থেকে ১০ দিন অন্তর অন্তর সারা মৌসুম জুড়ে বিশেষ করে ফুল ও ফল ধরার সময় স্প্রে করতে হবে।\
ফসল তোলার আগে কি নিয়মে ব্যবহার করতে হবে তা কীটনাশকের মোড়কে লেখা নিয়ম দেখে অনুসরণ করুন। \
\n\nরাসায়নিক নিয়ন্ত্রণ: \
\n\nসম্ভবমত সমন্বিত বালাই ব্যবস্থাপনার আওতায় জৈবিক নিয়ন্ত্রণের মাধ্যমে প্রতিরোধের ব্যবস্থা নিন। মানেব, \
ম্যানকোজেব এবং  ক্লোরোথালোনিল  সংঘটিত ছত্রাকনাশক টমেটোর সেপটোরিয়া রোগ নিয়ন্ত্রণে কার্যকরী। \
৭ থেকে ১০ দিন অন্তর অন্তর সারা মৌসুম জুড়ে বিশেষ করে ফুল ও ফল ধরার সময় স্প্রে করতে হবে। \
ফসল তোলার আগে কি নিয়মে ব্যবহার করতে হবে তা কীটনাশকের মোড়কে লেখা নিয়ম দেখে অনুসরণ করুন। '
        
    elif output=='Tomato_Spider_mites_Two_spotted_spider_mite images':
        output='সাধারন লাল মাকড়'
        txt='জৈবিক নিয়ন্ত্রণ: \n\nসামান্য আক্রমণে মাকড়কে শুধু জল দিয়ে ধুয়ে অপসারণ করুন এবং আক্রান্ত পাতা তুলে ফেলে দিন। \
রেড়ি, তুলসী, সয়াবীন ও নিম তেলের মিশ্রন প্রস্তুত করে টি. আর্টিসি-র বংশবৃদ্ধি কমাতে পাতায় স্প্রে করুন। \
এছাড়াও রসুন চা, বিছুটি পাতার কাঁই বা কীটনাশক সাবানের দ্রবণ ব্যবহার করে এ মাকড়ের বংশবৃদ্ধি কমানো যায়। \
মাঠে মাকড়ের প্রজাতি অনুসারে জৈব নিয়ন্ত্রক সহ শিকারী মাকড়সাকে কাজে লাগান (উদাহরণ হিসাবে ফাইটোসেইউলাস পারসিমিলিস) \
বা জৈব কীটনাশক ব্যাসিলাস থিউরিনজিয়েনসিস ব্যবহার করুন। প্রাথমিক স্প্রে করার ২-৩ দিন পরে দ্বিতীয় স্প্রে প্রয়োগ করাটা জরুরী। \
\n\nরাসায়নিক নিয়ন্ত্রণ: \
\n\nসম্ভবমতো সমন্বিত বালাই ব্যবস্থাপনার আওতায় জৈবিক নিয়ন্ত্রণের মাধ্যমে সর্বদা প্রতিরোধের ব্যবস্থা নিন। \
এ মাকড়কে বিষাক্ত দ্রব্য দিয়ে নিয়ন্ত্রণ করা খুবই কষ্টকর কারণ অধিকাংশ প্রজন্মের মধ্যে বেশ কয়েক বছর ধরে ব্যবহার করা \
বিভিন্ন রাসায়নিকের বিরুদ্ধে প্রতিরোধ ক্ষমতা গড়ে ওঠে। খুব সাবধানে রাসায়নিক নিয়ন্ত্রক নির্বাচন করুন যাতে এ মাকড়ের শিকারী পতঙ্গকে \
তা নির্বিচারে ধ্বংস না করে। উদাহরণ হিসাবে জলে সিক্ত করা যায় এমন সালফার (৩ গ্রাম/লিটার), স্পাইরোমেসিফেন (১ মিলি./লিটার), \
ডিকোফল (৫ মিলি/লিটার) বা অ্যাবামেকটিন সমৃদ্ধ ছত্রাকনাশক ব্যবহার করা যায়। প্রাথমিক স্প্রে ব্যবহার করার ২ থেকে ৩ দিন পরে দ্বিতীয়বার \
স্প্রে প্রয়োগ করা জরুরী। '
        
    elif output=='Tomato__Target_Spot images':
        output='টমেটোর টার্গেট দাগ  রোগ'
        txt='সকালে জল দিতে হবে যেন  টমেটো উদ্ভিদের  পাতা শুকানোর সময় থাকে । গাছের গোড়ায় জল বা পাতা শুকানোর \
জন্য একটি  মোজাবিশেষ বা ড্রিপ সিস্টেম ব্যবহার করুন। ফলটি মাটির সাথে সরাসরি যোগাযোগ থেকে নিরীক্ষণ করতে একটি তিল প্রয়োগ করুন। '
        
    elif output=='Tomato__Tomato_mosaic_virus images':
        output='টমেটোর মোজাইক ভাইরাস রোগ'
        txt='জৈবিক নিয়ন্ত্রণ: \n\n৭০° সেলসিয়াস তাপমাত্রায় ৪ দিন অথবা ৮২-৮৫° সেলসিয়াস তাপমাত্রায় ২৪ ঘন্টা  শুষ্কভাবে \
উত্তপ্ত করে বীজশোধন করলে বীজ ভাইরাস মুক্ত রাখতে সহায়তা করে। বিকল্পভাবে,  ১০০গ্রাম/লিটার \
ট্রাইসোডিয়াম ফসফেটের (trisodium phosphate)  দ্রবণে ১৫ মিনিট বীজ  ভিজিয়ে রেখে জল দিয়ে ভালোভাবে ধুয়ে \
পরে শুকিয়ে নিলেও কাজ হয়। \
\n\nরাসায়নিক নিয়ন্ত্রণ: \
\n\nসম্ভবমতো সমন্বিত বালাই ব্যবস্থাপনার আওতায় জৈবিক নিয়ন্ত্রনের মাধ্যমে প্রতিরোধের ব্যবস্থা নিন। \
টমেটো মোজাইক ভাইরাসের জন্য কোন কার্যকর রাসায়নিক বালাই ব্যবস্থাপনা নেই। '
        
    elif output=='Tomato__Tomato_YellowLeaf__Curl_Virus images':
        output='টমেটোর হলুদ পাতা কোঁকড়ানো ভাইরাস রোগ'
        txt='জৈবিক নিয়ন্ত্রণ: \n\nটমেটোর হলুদ পাতা কোঁকড়ানো ভাইরাস (TYLCV) রোগের বিরুদ্ধে \
কোন দমন ব্যবস্থার কথা জানা নেই। ভাইরাসের আক্রমণ এড়িয়ে যেতে হলে সাদা মাছির বংশবৃদ্ধি নিয়ন্ত্রণ করুন। \
\n\nরাসায়নিক নিয়ন্ত্রণ: \
\n\nভাইরাস দ্বারা একবার আক্রান্ত হলে এর বিরুদ্ধে আর কোন দমন ব্যবস্থা কাজ করে না। \
ভাইরাসের আক্রমণ এড়িয়ে যেতে হলে সাদা মাছির বংশবৃদ্ধি নিয়ন্ত্রণ করতে হবে। \
পাইরেথ্রয়েডস্ (pyrethroids) বর্গের কীটনাশক চারাগাছে বা মাটি নিষিক্ত করার জন্য ব্যবহার করে সাদামাছির \
বংশবৃদ্ধি কমানো যায়। কিন্তু এগুলোর মাত্রাতিরিক্ত ব্যবহার সাদামাছির  প্রতিরোধক্ষমতা বৃদ্ধি করতে পারে। '
        
    elif output=='Pepper__bell___healthy images' or output=='Potato___healthy images' or output=='Tomato_healthy images' :
        output='সুস্থ'
        
    if output!='সুস্থ':
        new=textbox(output,'Detection',txt)
    else:
        new=msgbox(output,'Detection','End')
    
elif output==img:
    new=msgbox("অটো ক্লোরো একটি চিত্র থেকে উদ্ভিদ রোগ সনাক্ত করার জন্য একটি মেশিন লার্নিং সফ্টওয়্যার। \
এই সফ্টওয়্যার রোগের প্রতিকারও দিয়ে থাকে।\
\n\nDeveloped by Farhad and Sarah.\
\nTeam Hydro AI - 2021",
               "About Us", "End")
    
