import React from 'react';

function NotesForm({setNotes}){
    
    const [inputFields, setInputFields] = React.useState([]);
    
    const addInputField = ()=>{
        setInputFields([...inputFields, ''])  
    }

    const removeInputFields = (index)=>{
        const rows = [...inputFields];
        rows.splice(index, 1);
        setInputFields(rows);
    }
    
    const handleChange = (index, event)=>{
        const value = event.target.value;
        const list = [...inputFields]; 
        list[index] = value;
        setInputFields(list);
        setNotes(list);
    }

    const handleKeyDown = (event) => {
        if(event.key === 'Enter'){
            addInputField();
        }
    }

    return(
    
        <div className="container">
            <div className="row">
                <div>
                {
                    inputFields.map((data, index)=>{
                        return(
                            <div key={index}>
                                <div>
                                    <input type="text"
                                        value={data} 
                                        onChange={(event)=>handleChange(index, event)} 
                                        onKeyDown={(event) => handleKeyDown(event) } 
                                        placeholder="Add a new note..." 
                                        autoFocus
                                    />
                                    {(inputFields.length!==1) ? <button onClick={removeInputFields}>x</button> : ''}
                                </div>
                            </div>
                            )
                        })
                }
     
                <div className="row">
                    <div>
                        <button onClick={addInputField}>Add New</button>
                    </div>
                </div>
                </div>
            </div>
            
            <div className="">
            </div>
        </div>
        
    )
}
export default NotesForm