import moment from "moment";
import { useCallback, useState } from "react";
import withDragAndDrop from "react-big-calendar/lib/addons/dragAndDrop";
import 'react-big-calendar/lib/css/react-big-calendar.css';
import { Calendar as BigCalendar, momentLocalizer, Views } from "react-big-calendar";
import "./ShippingCalendar.css";

const DnDCalendar = withDragAndDrop(BigCalendar);
const localizer = momentLocalizer(moment);

function ShippingCalendar() {
  const [events, setEvents] = useState([]);
  const [draggedEvent, setDraggedEvent] = useState();
  const [isDragging, setIsDragging] = useState(false);
  const [packages, setPackages] = useState([
    { id: 1, name: "Package 1" },
    { id: 2, name: "Package 2" },
    { id: 3, name: "Package 3" },
    { id: 4, name: "Package 4" },
  ]);

  const onChangeDeliveryTime = useCallback(
    ({
      event,
      start,
      end,
    }) => {
      setEvents((prevEvents) =>
        prevEvents.map((prevEvent) =>
          prevEvent.id === event.id
            ? { ...event, start, end }
            : prevEvent
        )
      );
    },
    []
  );  

  const onDroppedFromOutside = useCallback(
    ({
      start,
      end,
    }) => {
      if (!draggedEvent) return;
      
      // Add the event to calendar
      setEvents((prevEvents) => [
        ...prevEvents,
        {
          id: new Date().getTime(),
          start,
          end,
          data: { package: draggedEvent },
          isDraggable: true,
          isResizable: true,
          title: draggedEvent.name,
        },
      ]);

      // Remove the package from the packages list
      setPackages((prevPackages) => 
        prevPackages.filter((pkg) => pkg.id !== draggedEvent.id)
      );
      
      setIsDragging(false);
    },
    [draggedEvent]
  );

  const handleDragStart = (pkg) => {
    setDraggedEvent(pkg);
    setIsDragging(true);
  };

  const handleDragEnd = () => {
    setIsDragging(false);
  };

  return (
    <div className="shipping-calendar-container-parent">
      <h2>Shipping Calendar</h2>
      <div className="shipping-calendar-container">
        <div className="calendar-section calendar-wrapper">
          <DnDCalendar
            localizer={localizer}
            events={events}
            startAccessor="start"
            endAccessor="end"
            defaultView={Views.WEEK}
            draggableAccessor={(event) => !!event.isDraggable}
            onEventDrop={onChangeDeliveryTime}
            onDropFromOutside={onDroppedFromOutside}
            selectable
            resizable
          />
        </div>

        <div className="packages-section">
          <h3 className="packages-title">Available Packages</h3>
          <div className="packages-list">
            {packages.map((pkg) => (
              <div
                key={pkg.id}
                className={`package-item ${isDragging && draggedEvent?.id === pkg.id ? 'dragging' : ''}`}
                onDragStart={() => handleDragStart(pkg)}
                onDragEnd={handleDragEnd}
                draggable
              >
                {pkg.name}
              </div>
            ))}
            {packages.length === 0 && (
              <div className="package-item" style={{ opacity: 0.6, cursor: 'default' }}>
                No packages available
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default ShippingCalendar;