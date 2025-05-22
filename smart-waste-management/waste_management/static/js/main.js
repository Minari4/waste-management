// Main JavaScript for interactive elements
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Add hover effect to table rows
    document.querySelectorAll('table.table-hover tbody tr').forEach(row => {
        row.addEventListener('mouseenter', () => row.classList.add('table-active'));
        row.addEventListener('mouseleave', () => row.classList.remove('table-active'));
    });

    // Status indicators
    document.querySelectorAll('.bin-status-indicator').forEach(indicator => {
        const status = indicator.getAttribute('data-status');
        indicator.classList.add(`status-${status}`);
    });

    // Report List Filtering, Searching, Sorting
    const filterStatus = document.getElementById('filterStatus');
    const searchReports = document.getElementById('searchReports');
    const sortReports = document.getElementById('sortReports');
    const reportList = document.getElementById('reportList');

    if (filterStatus && searchReports && sortReports && reportList) {
        const reportItems = Array.from(reportList.getElementsByClassName('report-item'));

        function filterAndSortReports() {
            const statusFilter = filterStatus.value;
            const searchTerm = searchReports.value.trim().toLowerCase();
            const sortOption = sortReports.value;

            let filteredReports = reportItems.filter(item => {
                const status = item.getAttribute('data-status');
                const location = item.getAttribute('data-location');
                const description = item.getAttribute('data-description');

                const matchesStatus = (statusFilter === 'all') || (status === statusFilter);
                const matchesSearch = location.includes(searchTerm) || description.includes(searchTerm);

                return matchesStatus && matchesSearch;
            });

            // Sorting
            filteredReports.sort((a, b) => {
                if (sortOption === 'reported_at_desc') {
                    return parseInt(b.getAttribute('data-reported-at')) - parseInt(a.getAttribute('data-reported-at'));
                } else if (sortOption === 'reported_at_asc') {
                    return parseInt(a.getAttribute('data-reported-at')) - parseInt(b.getAttribute('data-reported-at'));
                } else if (sortOption === 'location_asc') {
                    return a.getAttribute('data-location').localeCompare(b.getAttribute('data-location'));
                } else if (sortOption === 'location_desc') {
                    return b.getAttribute('data-location').localeCompare(a.getAttribute('data-location'));
                }
                return 0;
            });

            // Clear current list
            reportList.innerHTML = '';

            if (filteredReports.length === 0) {
                const noResultsDiv = document.createElement('div');
                noResultsDiv.className = 'alert alert-info mt-3';
                noResultsDiv.textContent = 'No illegal dumping reports found.';
                reportList.appendChild(noResultsDiv);
            } else {
                filteredReports.forEach(item => {
                    reportList.appendChild(item);
                });
            }
        }

        filterStatus.addEventListener('change', filterAndSortReports);
        searchReports.addEventListener('input', filterAndSortReports);
        sortReports.addEventListener('change', filterAndSortReports);

        // Initial call to display sorted and filtered reports
        filterAndSortReports();
    }

    console.log('Interactive elements initialized.');
});
