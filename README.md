Il a pour but de vérifier la force du mot de passe saisi par l'utilisateur. 
La force du mot de passe est déterminée en fonction de plusieurs critères. 
Lorsqu'un mot de passe fort est saisi, l'utilisateur est informé que l'opération a réussi. S'il est faible, 
un nouveau mot de passe sera demandé à nouveau jusqu'à ce que les conditions soient remplies.

---------------------------

Critères utilisés pour déterminer la force du mot de passe :
Longueur du mot de passe : Le mot de passe doit comporter au moins 8 caractères.
Majuscule : Le mot de passe doit contenir au moins une lettre majuscule.
Chiffre : Le mot de passe doit contenir au moins un chiffre.

---------------------------

1. Messages explicatifs :
print("Pour que votre mot de passe soit fort, vous devez")
print("- Contenir au moins 8 caractères")
print("- Contient au moins une lettre majuscule")
print("- Contenir au moins un chiffre")
# تقوم هذه الرسائل بإبلاغ المستخدم بالشروط الواجب توفرها في كلمة المرور.
# Ces messages informent l'utilisateur des conditions qui doivent être remplies dans le mot de passe.

2. Fonction de vérification de la force du mot de passe : 
def is_strong_password(p):
    length = (len(p) >= 8)  # التحقق من طول الكلمة
    majuscule = any(i.isupper() for i in p)  # التحقق من وجود حرف كبير
    chiffre = any(i.isdigit() for i in p)  # التحقق من وجود رقم
    return length and majuscule and chiffre
# المدخلات: كلمة المرور p (String).
# المخرجات: قيمة منطقية (Boolean) تعبر عن قوة كلمة المرور:
# True إذا كانت الكلمة قوية
# False إذا لم تستوفِ الشروط

3. Boucle itérative : 
while True :
    password = input("Entrez un mot de passe ici : ")

    if is_strong_password(password) :
        print("Bravo, vous avez écrit un mot de passe fort")
        break
    else:
        print("Malheureusement, mon mot de passe est faible. Veuillez le retaper")
# يقوم الكود بطلب كلمة مرور من المستخدم باستخدام input.
# يتم إرسال كلمة المرور إلى الدالة is_strong_password للتحقق من قوتها.
# إذا كانت كلمة المرور قوية:
# تظهر رسالة تهنئة، ويتم إنهاء البرنامج باستخدام break.
# إذا كانت كلمة المرور ضعيفة:
# يتم عرض رسالة توضح أن الكلمة ضعيفة، ويطلب من المستخدم إعادة المحاولة.

كيفية تشغيل الكود:
انسخ الكود إلى ملف Python (مثلاً: password_checker.py).
افتح سطر الأوامر أو بيئة Python IDE.
قم بتشغيل الكود.
أدخل كلمة مرور حسب الشروط المحددة، وسيقوم البرنامج بتوجيهك عند الحاجة.

Ce code se concentre sur la simplicité et la facilité de compréhension.

Version 1.00
Berrada Mehdi