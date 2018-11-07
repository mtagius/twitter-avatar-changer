
start chrome
sleeep1

set list=^
 "https://github.com/mtagius/twitter-avatar-changer"^
 "https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_image.html"^
 "https://twitter.com/eigenbom"^
 "https://twitter.com/mtagius_"
for %%a in (%list%) do ( 
   start chrome %%a 
)

::localhost 80