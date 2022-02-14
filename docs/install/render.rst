.. _install-render:

====================
Installing on Render
====================

Render is a web hosting platform, similar to Heroku. Support for deploying Tabbycat to Render is currently **very experimental**. Please note:

- Render provides a similar '1 click' method as to Heroku; e.g. it should be approachable to people without experience in deploying web applications
- Although Tabbycat is setup to run within the free-tier of Render, you may need to add a credit card to your account in order to deploy Tabbycat
- Tabbycat's performance on Render is not optimised. Don't use render if you are going to have lots of people accessing your tab site
- Render's free-tier database will **stop working and delete all your data after 90 days**. If you want to keep your tab data around for the long term, you must backup your data and host it elsewhere after the tournament ends
- Some Tabbycat functionality **will not work** (yet). As of the 14th of Feb, this includes:
  - Automatic allocation of adjudicators and venues
  - All email-related functionality
  - Possibly some other stuff we haven't noticed yet

To deploy to Render, you should click the below button...

.. image:: https://render.com/images/deploy-to-render-button.svg
  :target: https://render.com/deploy?repo=https://github.com/TabbycatDebate/tabbycat/tree/feature/render

...and on the following page, give your "Service Group" a name. Anything will do.

Then, leave "Branch" as it is. Enter your email and Time Zone in the fields. Time zones are formatted as per Heroku — pick the "TZ database name" `pick from this list <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List>`_, e.g. *Europe/Copenhagen*.

Then, click "Apply" at the bottom of the page. The button will disappear. Give it  a few minutes then go to your *Dashboard*. It should take up to 30 minutes for all items have a *STATUS* of "Deploy succeeded" or "Available". You may need to refresh the page to see these updated. When everything is successful/available, click through to the "Web Service" item on your Render Dashboard to see the URL of your site. Open it to complete the normal Tabbycat admin account setup.

Note that this URL cannot be changed unless you `add a custom domain using a URL you already own <https://render.com/docs/custom-domains>`_.
