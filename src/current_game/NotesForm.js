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

    return(
    
        <div className="container">
            <div className="row">
                <div>
                {
                    inputFields.map((data, index)=>{
                        return(
                            <div key={index}>
                                <div>
                                    <input type="text" onChange={(event)=>handleChange(index, event)} value={data} placeholder="Add a new note..." />
                                    {(inputFields.length!==1) ? <button onClick={removeInputFields}>x</button> : ''}
                                </div>
                            </div>
                            )
                        })
                }
     
                <div className="row">
                    <div>
                        <button className="" onClick={addInputField}>Add New</button>
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