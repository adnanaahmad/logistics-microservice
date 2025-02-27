import React, { useState } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css'; // Import the styles for the calendar
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';

const ShippingCalendar = () => {
  const [date, setDate] = useState(new Date());
  const packages = [
    { id: '1', content: 'Package 1' },
    { id: '2', content: 'Package 2' },
  ];

  const onDragEnd = (result) => {
    // Handle drag and drop logic
    console.log(result);
  };

  return (
    <div>
      <Calendar onChange={setDate} value={date} />
      <DragDropContext onDragEnd={onDragEnd}>
        <Droppable droppableId="packages">
          {(provided) => (
            <div {...provided.droppableProps} ref={provided.innerRef}>
              <h2>Packages</h2>
              {packages.map((pkg, index) => (
                <Draggable key={pkg.id} draggableId={pkg.id} index={index}>
                  {(provided) => (
                    <div
                      ref={provided.innerRef}
                      {...provided.draggableProps}
                      {...provided.dragHandleProps}
                      style={{
                        padding: '8px',
                        margin: '4px',
                        backgroundColor: '#f0f0f0',
                        borderRadius: '4px',
                      }}
                    >
                      {pkg.content}
                    </div>
                  )}
                </Draggable>
              ))}
              {provided.placeholder}
            </div>
          )}
        </Droppable>
      </DragDropContext>
    </div>
  );
};

export default ShippingCalendar; 