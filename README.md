# READ ME
---

## How to run the program
1. Install Django
For Linux/Mac:
```bash
python -m pip install Django
```

For Windows:
```bash
py -m pip install Django
```
Ensure a virtual environment is ready and available on your PYTHONPATH environment variable

2. Run the command:
```bash
python3 manage.py runserver
```

## Project description

You Beauty is an appointment booking website for salons that allows users to browse salons and book with them based on availability.

## Proposed User stories

1. As a customer, I want to create an account by providing my details (username, email, password, first name, last name, phone number), so that I can make bookings with my desired salon.

2. As a customer, I want to log in using my username and password, so that I can access my account and use the services.

3. As a salon owner, I want to create an account by providing my details (username, email, password, first name, last name, and phone number), so that I can register and manage my salon on the website.

4. As a salon owner, I want to log in using my username and password, so that I can access my account and manage my salon’s information and services.

5. As a salon owner, I want to register my salon and the services it offers, so that customers can view and book appointments for my salon’s services.

6. As a customer, I want to book an appointment for a salon service, so that I can secure a time slot for the service I need.

7. As a customer, I want to reschedule my appointments, so that I have flexibility in adjusting my bookings if my plans change.

8. As a customer, I want to browse top salons and view happy hour deals on the homepage, so that I can quickly find the best salon services and discounts without needing to log in.

9. As a customer, I want to view a list of all top salons, so that I can easily find the most popular salons.

10. As a customer, I want to view a list of all salons offering happy hour deals, so that I can find the best discounts on services.

11. As a customer, I want to be able to select and view a salon, so that I can make an informed decision before booking services.

12. As a customer, I want to search for salons using specific keywords, location, or services offered, so that I can quickly find salons that meet my needs.

13. As a customer, I want to edit my profile information, so that I can keep my details up-to-date.

14. As a customer or salon owner, I want to return to the homepage by clicking on the YouBeauty logo, so that I can easily navigate back to the starting page relevant to my role.

15. As a user, I want to easily navigate through the website using a dropdown menu on every page, so that I can quickly access different pages.

16. As an authenticated customer, I should only have access to the customer side of the website, so that I don’t inadvertently access business-specific pages and functionalities.

17. As a salon, I want to be able to edit times and days of the week when I am available so that no bookings are made outside of salon business hours.

18. As a salon, I want to update my profile details, including address and contact number, so I can keep my information up-to-date.

19. As a salon, I want to be able to view my upcoming bookings, so I can schedule accordingly.

20. As a salon, I want to be able to cancel my upcoming bookings, in case of emergencies.

21. As a salon, I want to be able to opt for a “Happy Hour” discount to promote my business.

22. As a customer, I want to cancel my appointments, so that I have flexibility in adjusting my bookings if my plans change.

23. As a customer, I want to be able to view my booking history, so that I can see my upcoming, current, and past bookings together.

24. As a salon owner, I want to be able to view appointments on my appointment calendar so that I can manage and view the times of different appointments.

25. As a salon, I want to be able to reschedule my appointments in case of emergencies.

26. As a user, I want the website to work seamlessly across different screen sizes so that I can use it without compatibility issues.

27. As a customer or salon owner, I want to be able to access the FAQ page, so that I can get answers to my questions without having to contact someone.

28. As a customer or salon owner, I want to be able to access the About Us page, so that I can know more about the You Beauty website.

29. As a customer or salon owner, I want to be able to log out from my account, so that I can keep my account secure when it is not in use.

30. As a salon owner, I want to be able to view statistics of my appointments, so that I can track the performance of my business, analyze booking trends, and manage my resources efficiently.


## Initial plan

Initial plan:

1. Recurring meetings to be held: Out of tutorial (Tuesday 6-7pm), in tutorial (Friday 4-5pm), with tutor (Friday 5-6pm), and with clients (Friday 3-4pm)
2. Communication: mainly through Slack.
3. Documentation: Bitbucket (meeting minutes, code, README.md etc.) and Google Drive
4. To switch XP roles every 2 weeks (Weeks 2 & 3, 4 & 5, 6 & 7, 8 & 9, 10 & 11)


Rough plan for development:

- Wireframes to be made for front-end, to discuss with client.
- Database to be set up with "fake" data (AI-generated data as a placeholder for development).
- Implement login / sign up functionality for both users and salons.
- Search filter functionality done using database.
- Code front-end, ensuring the layout of the website optimises UX and the website has a good UI.
- Implement booking functionality (connect to database).
- Implement view booking history for users.
- Implement view booking calendar for salons.

Extra features to consider:

1. Using AI models to create style suggestions for users:
As a user, I want to get style suggestions so I can get recommendations when I want to try something new

2. FAQ page:
As a user/salon, I want a page that contains FAQ answered so I can quickly resolve small concerns without having to contact Admins

3. About-us page:
As a user/salon, I want to easily contact the Admins when I have an issue that cannot be resolved on my own

Extra user stories to consider:

19. As a salon, I want to be able to cancel appointments in case of emergencies where I can not provide my services
20. As a salon, I want to be able update booking appointments in case a customer reschedules
21. As a user, I want to be able to reschedule my appointments in case of emergencies
22. As a system administrator, I want to be able to manage salon registrations, including approval, suspension, and deletion of salon accounts, so that I can maintain the quality of service providers on the platform.
23. As a system administrator, I want the booking system to handle a high volume of concurrent users during peak hours without performance degradation, so that the platform will remain responsive and reliable.
24. As a website visitor, I want to be able to browse salons and services available from the homepage, so that I can research services from different salons.
25. As a user, I want the booking system to work seamlessly across different devices including laptop and mobile phones, so that I can book appointments without compatibility issues.

---
Other information...

.

.

.

.

.

# How to use Bitbucket
---
## Edit a file
You’ll start by editing this README file to learn how to edit a file in Bitbucket.

1. Click **Source** on the left side.
2. Click the README.md link from the list of files.
3. Click the **Edit** button.
4. Delete the following text: *Delete this line to make a change to the README from Bitbucket.*
5. After making your change, click **Commit** and then **Commit** again in the dialog. The commit page will open and you’ll see the change you just made.
6. Go back to the **Source** page.

## Create a file

Next, you’ll add a new file to this repository.

1. Click the **New file** button at the top of the **Source** page.
2. Give the file a filename of **contributors.txt**.
3. Enter your name in the empty file space.
4. Click **Commit** and then **Commit** again in the dialog.
5. Go back to the **Source** page.

Before you move on, go ahead and explore the repository. You've already seen the **Source** page, but check out the **Commits**, **Branches**, and **Settings** pages.

## Clone a repository

Use these steps to clone from SourceTree, our client for using the repository command-line free. Cloning allows you to work on your files locally. If you don't yet have SourceTree, [download and install first](https://www.sourcetreeapp.com/). If you prefer to clone from the command line, see [Clone a repository](https://confluence.atlassian.com/x/4whODQ).

1. You’ll see the clone button under the **Source** heading. Click that button.
2. Now click **Check out in SourceTree**. You may need to create a SourceTree account or log in.
3. When you see the **Clone New** dialog in SourceTree, update the destination path and name if you’d like to and then click **Clone**.
4. Open the directory you just created to see your repository’s files.

Now that you're more familiar with your Bitbucket repository, go ahead and add a new file locally. You can [push your change back to Bitbucket with SourceTree](https://confluence.atlassian.com/x/iqyBMg), or you can [add, commit,](https://confluence.atlassian.com/x/8QhODQ) and [push from the command line](https://confluence.atlassian.com/x/NQ0zDQ).