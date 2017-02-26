# InfoMP API

## Made at HackIllinois 2017 by Devarsh (@devarsh1997) and Keshav (@KeshavH)

## InfoMP Rest API
  * Simple Easy-to-use API to find out an Indian district's MP (Member of Parliament) information.
  * MP's information includes contact details, party affiliation and countries he/she has visited.
  * Made to build useful Apps/APIs on it. For instance, we wanted to create a Chat Bot that sends us details of the MP
    based on constituency. No other API/website allows to do this right now in an easy, simple way.
  * Objective: To enable non-profit/for-profit software/App developers to advance GovTech infrastructure in India, and rais political awareness.
 
## Build Instructions

   * The API is deployed on Heroku.
   * Use Python guides on Heroku/Cloud Service provider to launch your private instance of the API.
   * Dependencies have been listed on file called 'requirements.txt'
   * This version was built and locally tested on MacOS Sierra and Windows 10. Any OS that works with deployment platform would suffice.
   
## Usage Instructions
   * The current version has been deployed here: https://safe-earth-99322.herokuapp.com/   
   * If you are a web user, just go to the website and follow the instructions after the next line.
   * If you are a developer,  you can just curl or do a GET request. To learn more about API structure/usage go to next line.     
   * On either the above deployment, or your own private deployment, usage is as follows
   * Going to the main url returns you to the start of the API execution.
   * Adding "/infomp" to the end of the url displays the entirety of the data on one page
   * Adding "/ConstituencyName" on top of that will pull just the constituency's data.
   * Constituency name is case sensitive, and can vary in terms of spacing style (" " vs "-")
* First letters must be capitalized
   * Once at the single constituency stage you cannot return to the original full list directly
   *Simply removing the constituency url addition will not suffice.
* You must return to the original base site to restart your instance
* Simply changing the constituency at URL end will still function
*Example consituency level url: https://safe-earth-99322.herokuapp.com/infomp/Bangaon

## Contributor Guide
   * This API is open sourced because Indian GovTech infrastructure needs a lot of work.
   * Websites/APIs made available by Government are inefficient/incosistent for non-profits.
   * If you have any features in mind that relates to the mission of improving and advancing Indian GovTech,  begin contributing!
   * Particular goals for contributors:
       * Improve and regularly update the data using POST method (under development).
       * Improve variety of accepted variations of a single constituency.
    * Remove case sensitivity, implement dashes, spaces, or underscores all working.
* Implement ways to filter the data to allow for easier data science analytics.
* Branch out into similar efforts for other nations with a need for better structured government data.
* Implement Indian MLA (Member of Legislative Assembly) politicians as well.
