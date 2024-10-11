document.addEventListener("DOMContentLoaded", function () {
    // generic events
    const events = [
        { date: '2024-10-10', title: 'facial', start_time: '10:00', end_time: '13:00', color: 'blue' },
        { date: '2024-10-11', title: 'haircut', start_time: '15:00', end_time: '17:00', color: 'red' },
        { date: '2024-10-12', title: 'nails', start_time: '14:00', end_time: '16:00', color: 'green' },
        { date: '2024-10-13', title: 'whatever', start_time: '18:00', end_time: '21:00', color: 'yellow' },
    ];

    const calendarGrid = document.getElementById('calendarGrid');
    const currentMonthElement = document.getElementById('currentMonth');
    const weekViewBtn = document.getElementById('weekViewBtn');
    const monthViewBtn = document.getElementById('monthViewBtn');
    let currentDate = new Date();

    weekViewBtn.addEventListener('click', function () {
        switchView('week');
    });

    monthViewBtn.addEventListener('click', function () {
        switchView('month');
    });

    function createMonthGrid() {
        const year = currentDate.getFullYear();
        const month = currentDate.getMonth();
        const firstDay = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();
        const emptyCells = (firstDay === 0 ? 6 : firstDay - 1);

        for (let i = 0; i < emptyCells; i++) {
            const emptyCell = document.createElement('div');
            emptyCell.className = 'calendar-day';
            calendarGrid.appendChild(emptyCell);
        }

        for (let i = 1; i <= daysInMonth; i++) {
            const dayElement = document.createElement('div');
            dayElement.className = 'calendar-day';
            dayElement.innerHTML = `<div class="day-label">${i}</div>`;
            calendarGrid.appendChild(dayElement);
        }

        const totalCells = emptyCells + daysInMonth;
        const remainingCells = totalCells % 7 === 0 ? 0 : 7 - (totalCells % 7);

        for (let i = 0; i < remainingCells; i++) {
            const emptyCell = document.createElement('div');
            emptyCell.className = 'calendar-day';
            calendarGrid.appendChild(emptyCell);
        }

        populateEvents('month');
    }

    function switchView(view) {
        clearCalendarGrid();

        if (view === 'week') {
            const startOfWeek = new Date(currentDate);
            startOfWeek.setDate(currentDate.getDate() - currentDate.getDay() + 1); // Set to Monday

            calendarGrid.style.gridTemplateColumns = 'repeat(7, 1fr)';
            calendarGrid.style.gridAutoRows = 'auto';

            for (let i = 0; i < 7; i++) {
                const dayElement = document.createElement('div');
                dayElement.className = 'calendar-day';
                const date = new Date(startOfWeek);
                date.setDate(startOfWeek.getDate() + i);
                dayElement.innerHTML = `<div class="day-label">${date.getDate()}</div>`;
                calendarGrid.appendChild(dayElement);
            }

            populateEvents('week');
        } else if (view === 'month') {
            calendarGrid.style.gridTemplateColumns = 'repeat(7, 1fr)';
            calendarGrid.style.gridAutoRows = '100px';
            createMonthGrid();
        }
    }

    function populateEvents(view) {
        events.forEach(event => {
            const eventDate = new Date(event.date);
            const eventDay = eventDate.getDate();
            const eventMonth = eventDate.getMonth();
            let dayIndex;
    
            if (view === 'week') {
                const startOfWeek = new Date(currentDate);
                startOfWeek.setDate(currentDate.getDate() - currentDate.getDay() + 1); // Set to Monday
    
                const endOfWeek = new Date(startOfWeek);
                endOfWeek.setDate(startOfWeek.getDate() + 6); // Set to Sunday
    
                if (eventDate >= startOfWeek && eventDate <= endOfWeek) {
                    dayIndex = (eventDate.getDay() === 0 ? 6 : eventDate.getDay() - 1);
                }
            } else if (view === 'month' && eventMonth === currentDate.getMonth()) {
                const firstDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1).getDay();
                const emptyCells = firstDay === 0 ? 6 : firstDay - 1;
                dayIndex = eventDay - 1 + emptyCells + 7; // Adjust for the days of the week header and empty cells
            }
    
            if (typeof dayIndex !== 'undefined') {
                const dayElement = calendarGrid.children[dayIndex];
                if (dayElement) {
                    const eventElement = document.createElement('div');
                    eventElement.className = 'event event-item';
                    eventElement.setAttribute('data-color', event.color);
                    eventElement.textContent = `${event.start_time}-${event.end_time} ${event.title}`;
                    dayElement.appendChild(eventElement);
                }
            }
        });
    }
    

    function clearCalendarGrid() {
        while (calendarGrid.children.length > 7) {
            calendarGrid.removeChild(calendarGrid.lastChild);
        }

        const eventElements = document.querySelectorAll('.event-item');
        eventElements.forEach(eventElement => eventElement.remove());
    }

    function changeMonth(offset) {
        currentDate.setMonth(currentDate.getMonth() + offset);
        updateCalendar();
    }

    function updateCalendar() {
        const options = { month: 'long', year: 'numeric' };
        currentMonthElement.textContent = currentDate.toLocaleDateString(undefined, options);
        switchView('month');
    }

    updateCalendar();
});
