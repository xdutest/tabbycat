.. _install-render:

====================
Installing on Render
====================

Render is a web hosting platform, similar to Heroku. Support for deploying Tabbycat to Render is currently **very experimental**. Please note:

- Render provides a similar '1 click' method as to Heroku; e.g. it should be approachable to people without experience in deploying web applications
- Although Tabbycat is setup to run within the free-tier of Render, you may need to add a credit card to your account in order to deploy Tabbycat
- Tabbycat's performance on Render is not optimised. Don't use Render if you are going to have lots of people accessing your tab site
- Render's free-tier database will **stop working and delete all your data after 90 days**. If you want to keep your tab data around for the long term, you must backup your data and host it elsewhere after the tournament ends
- Some Tabbycat functionality will not work (yet). As of the 14th of Feb, this includes:
   - Automatic allocation of adjudicators and venues
   - All email-related functionality
   - Possibly some other stuff we haven't noticed yet

To deploy to Render, follow the instructions below.

1. Signup
=========

`Follow this link <https://dashboard.render.com/register?next=/>`_ and sign-up for the Render service.

Login when finished, and navigate to your *Dashboard*.

2. Create 'Redis'
=================

For now, there is one part of Tabbycat that can't be setup automatically: the 'Redis' caching system. On the *Dashboard* screen of Render, click the **New** dropdown in the top-right and select "Redis".

  .. image:: images/render-dropdown.png
      :alt: The dropdown menu to make a Redis

Give your 'New Redis Instance' a Name. Ensure you change the plan to *Ephemeral* unless you are OK being charged.

.. admonition:: Warning
  :class: warning

  We would strongly advise running against all but the smallest tournaments on this *Ephemeral* plan. Higher-capacity versions of Redis are crucial to managing many simultaneous visitors to a Tabbycat site.

Then, click the blue **Create** button at the bottom of the page.

On the next page, take a precise note of the **Hostname** and **Port** text. You will need to copy/paste these in a second.

  .. image:: images/render-settings.png
      :alt: The values to note down

3. Setup the Other Stuff
========================

.. image:: https://render.com/images/deploy-to-render-button.svg
  :target: https://render.com/deploy?repo=https://github.com/TabbycatDebate/tabbycat/tree/feature/render

Click the button above. Enter whatever you want as the **Service Group Name** and leave "Branch" as it is.

In the text-field to the right of ``REDIS_HOSTNAME`` enter the **Hostname** text from the Redis page. In the text-field to the right of ``REDIS_PORT`` enter the **Port** text from the Redis page.

Then, enter your email and Time Zone in the fields. Time zones are formatted as per Heroku — copy of a "TZ database name" `from this list <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List>`_, e.g. *Europe/Copenhagen*.

Then, click "Apply" at the bottom of the page. The button will disappear.

Wait it  a few minutes then go to your *Dashboard*. It may take up to 30 minutes for all items have a *STATUS* of "Deploy succeeded" or "Available" and you may need to refresh the page to see these updated status.

4. Login to Tabbycat
====================

When everything is successful/available, click through to the "Web Service" item on your Render Dashboard to see the URL of your site below the title. Open the URL to complete the normal Tabbycat admin account setup.

Note that this URL cannot be changed unless you `add a custom domain using a URL you already own <https://render.com/docs/custom-domains>`_.
