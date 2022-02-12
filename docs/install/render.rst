.. _install-render:

====================
Installing on Render
====================

Render is a web hosting platform, similar to Heroku. Support for deploying Tabbycat to Render is currently **very experimental**. Please note:

- Render provides a similar '1 click' method as to Heroku; e.g. it should be approachable to people without experience in deploying web applications
- Although Tabbycat is setup on the free-tiers of Render, you may need to add a credit card to your account in order to deploy Tabbycat
- Tabbycat's performance on Render is not optimised. Don't use render if you are going to have lots of people accessing your tab site
- Render's free-tier database will **stop working and delete all your data** after 90 days. If you want to keep your tab data around for the long term, you must backup your data and host it elsewhere after the tournament ends
- Some Tabbycat functionality may not work
- Email-related functionality will definitely not work
- These instructions are provisional drafts

To deploy to Render, you should click the below button...

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/TabbycatDebate/tabbycat/tree/feature/render)

...and on the following page, give your "Service Group" a name. Anything will do. Leave "Branch" as it is and then click "Apply" at the bottom of the page.
