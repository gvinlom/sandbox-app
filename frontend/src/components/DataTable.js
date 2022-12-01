import * as React from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { Container } from '@mui/material';
import Button from '@mui/material/Button';
import axios from 'axios';

export default function DataTable(){
    const [sessions, setSessions] = React.useState([]);
    const [currentSession, setCurrentSession] = React.useState();

    function startNewSession(){
        // get start_time as current time
        var now = new Date()
        now.getTime()
        var data = {start_time: now.toISOString().replace('Z','')}
        // post a new session to api
        axios.post('/api/session', data).then(res=>{
            setCurrentSession(res.data.id);
            console.log('new id',res.data.id)
        })
    }

    function endSession(){
        var now = new Date()
        now.getTime()
        var data = {end_time: now.toISOString().replace('Z','')}
        axios.put(`/api/session/${currentSession}`, data=data).then(res=>{
            setCurrentSession(undefined);
        })
    }

    React.useEffect(()=>{
        axios.get('/api/session')
        .then((res)=>{
            console.log('my api',res.data);
            setSessions(res.data);
        })
        .catch(err=> console.log(err))
    },[currentSession]);
    
    const columns = [
      { field: 'id', headerName: 'ID', hide: true},
      { field: 'start_time', headerName: 'Start Time', width: 170 },
      { field: 'end_time', headerName: 'End Time', width:170},
      {
        field: 'hours',
        headerName: 'Duration',
        headerAlign: 'center',
        type: 'number',
        flex: 1
      },
    ];

    return (
    <Container style={{ display: 'flex', flexFlow:'column nowrap', height: '500px', width: '75%' }}>
        <h1>Sessions {process.env.NODE_ENV}</h1>
        <DataGrid
        rows={sessions}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        checkboxSelection
        />
        <Button sx={{mt:'10px'}} onClick={startNewSession} disabled={currentSession != undefined} className='Button' variant="contained">Start Session</Button>
        <Button sx={{mt:'10px'}} onClick={endSession} disabled={currentSession == undefined} className='Button' variant="contained">End Session</Button>
    </Container>
    );
};