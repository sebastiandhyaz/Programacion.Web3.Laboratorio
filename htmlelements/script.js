const SVG_ICON = `
  <svg class="event-svg" width="28" height="28" viewBox="0 0 24 24" fill="#d8e5ee" xmlns="http://www.w3.org/2000/svg">
    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z"/>
  </svg>
`;

function addEvent(type, text, username) {
    totalEvents += 1;
    let element;
    if (textOrder === "actionFirst") {
        element = `
    <div class="event-container" id="event-${totalEvents}">
        ${SVG_ICON}
        <span class="username-container">${text}</span>
        <span class="details-container">${username}</span>
    </div>`;
    } else {
        element = `
    <div class="event-container" id="event-${totalEvents}">
        ${SVG_ICON}
        <span class="username-container">${username}</span>
        <span class="details-container">${text}</span>
    </div>`;
    }
    if (direction === "bottom") {
        $('.main-container').removeClass("fadeOutClass").show().append(element);
    } else {
        $('.main-container').removeClass("fadeOutClass").show().prepend(element);
    }
    if (fadeoutTime !== 999) {
        $('.main-container').addClass("fadeOutClass");
    }
    if (totalEvents > eventsLimit) {
        removeEvent(totalEvents - eventsLimit);
    }
}