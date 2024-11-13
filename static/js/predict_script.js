
    document.addEventListener('DOMContentLoaded', function() {
        const stateDropdown = new Choices('#State_Name', {
            searchEnabled: true,       // Enables search functionality
            itemSelectText: '',        // Removes "Press to select" text
            placeholderValue: 'Enter state name', // Adds placeholder text
        });
    });

    