=# SOFT3888_F16_04 meeting minutes

## Information:
- Subject: Out of tutorial meeting 3 September (Week 6)
- Project name: P24 You Beauty
- Facilitator: Henry Lo
- Prepared by: Mohitha Mohan
- Mode: Online google meet
- Date: 17/09/2024
- Time: 6:00pm-7:00pm
- Attendees: Katholiki Kritharides, Selina Thai, Mohitha Mohan, Henry Lo, Oydan Khan
- Absent: Niranjana Saxena, Claudia Choi

## Agenda items

<table>

<tr>
    <th> Agenda Item </th>
    <th> Description </th>
    <th> Actions needed</th>
    <th> Who </th>>
    <th> Notes/Decisions </th>
</tr>

<tr>
    <th> 1st demo presentation</th>
    <td> Presentation due Friday tutorial time 
    </td>
    <td><ol>
        <li>Write script for responsible parts of oresentation</li>
        <li>Presentation rehersal on Thursday evening (6pm subject to everyone's availability)
        </li>
    </ol>
    </td>
    <td><ol>
        <li>Everyone</li>
    </ol>
    </td>
    <td><ul>
        <li>Mohitha to talk about overview and stakeholder (1m)</li>
        <li>Henry to talk about requirements (1m)</li>
        <li>Kathy to talk about testing plan (1m)</li>
        <li>Oydan to talk about implemented user stories (3m)</li>
        <li>Kathy to talk about plan for other stories (30s)        </li>
        <li>Oydan to talk about system architecture (1m)        </li>
        <li>Niranjana to talk about potential risks (30s)        </li>
        <li>Salina to talk about group process (1m)        </li>
        <li>Claudia to talk about Discipline (30s)        </li>
    </ul></td>
</tr>

<tr>
    <th> Meeting participation table </th>
    <td> Update meeting participation table</td>
    <td> Update meeting participation table and upload on bitbucket</td>
    <td> Mohitha
    </td>
    <td>Finish by next week</td>
</tr>

<tr>
    <th> Client demo </th>
    <td> Discuss what needs to be prepared for week 7 client demo
        <ul>
        <li>Require slides and user stories</li>
        <li>Duration: 40-60 minutes with prepared agenda and timeline</li>
        <li>Ask in week 6 tutorial for clarification on Q&A section</li>
        <li>Decide demo agenda on thursday</li>
        </ul>
    </td>
    <td>TBD on Thursday meeting</td>
    <td>Everyone   </td>
    <td>
    </td>
</tr>

<tr>
    <th> Website progress and task assignment </th>
    <td> Update of current development progress
        <ul>
        <li>User login is functional but not yet for business side</li>
        <li>Assigned functionality tasks to be done this week (w6)</li>
        <li>Consider splitting customer and business side teams on implementing functionalities to catch up timeline</li>
        </ul>
    </td>
    <td>Programming tasks to be done by this week. More functionality of the website should come in play in the next few.</td>
    <td>Everyone</td>
    <td>
        <ul>
        <li>Claudia to do figma pages/wireframe</li>
        <li>Henry to do business sign up, email notification for foget password</li>
        <li>Salina to do sitemap - standardized page name</li>
        <li>Narangina to finish business pre-login page</li>
        <li>Kathy to do profile page (flex display)</li>
        <li>Mohitha to do FAQ</li>
        <li>Oydan to add instructions to use webapp and complete manage booking page</li>
        </ul>
    </td>
</tr>



</table>

## Additional Meeting Notes
- Database restructuring 
    - Lucid chart done Mohitha
    - Decided to split into salon and customer did research on this
    - Henry has completed the code
    - Mohitha will check again as well.
- Jira adding tasks Oydan said she’ll do it? But no we can do it ourselves (individual!!)
- Figma wireframes - Mohitha will do it by thursday/friday. About claudia not sure.
- Database populating???
    - How are you populating it? Writing a script for it.
    - Anything else that needs to be populated, put that down as a task. 
- Kathy - working on profile edit function, created form for it and making sure it works as intended. 
- Mohitha will work on FAQ as well.
- JIRA issues of redundant tasks
    - Is there a way for Jira to show who’s been working on it?? Probably not.
    - Does it matter? 
    - Epics? Segregation of epics and how to. (Front-end, back-end, testing, report-writing, documentation) - MOHITHA WILL ADD THIS.
- Testing for Kathy
    - What to test for, any code completed???
    - Kathy will look into it she wants to code.
    - Kathy needs to build on Niranjana’s tests (static pages loading).
- Selina’s work
    - She’ll stick with front end for the salon page
- Henry mentioned issue with login: 
    - PROBLEM: Business person can access customer, customer can access business page.
    - Solution: use authentication authorization thing on Django. 
    - May need to use decorators 
    - Created a new branch on thingy.
- Mohitha to update meeting minutes 
- Kathy concluding: Do stuff we’ve decided on first, and then work on everything else.
