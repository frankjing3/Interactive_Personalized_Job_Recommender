import * as React from 'react';
import JobRecommendations from './JobRecommendations';
import MarketAnalysis from './MarketAnalysis';
import { alpha } from '@mui/material';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Container from '@mui/material/Container';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import JobSearchService from '../../../services/jobSearchService';
import Divider from '@mui/material/Divider';


export default function JobSearchWithMap() {
  const { data, error, fetchData } = JobSearchService();
  const states = ['All States', 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
            'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
            'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
            'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
            'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

  const positions = ['Senior Software Enginner', "Software Engineer", "Data Engineer"]
  const jobMap = require('../../../../src/Assets/job-map.png')

  const [state, setState] = React.useState(states[0]);
  const [skills, setSkills] = React.useState('');
  const [position, setPosition] = React.useState(positions[0]);
  const [jobs, SetJobs] = React.useState([]);

  const jobMapStyle = {
    width: '100%',
    height: '100%',
    cursor: 'pointer',
  };

  const handleSearch = () => {
    const requestBody = {
      "state": state,
      "position": position,
      "skills": skills
    };
    fetchData(requestBody).then(response => SetJobs(response));
  }

  const handleChangeState = (e) => {
    setState(e.target.value)
  }

  const handleChangeSkills = (e) => {
    setSkills(e.target.value)
  }

  const handleChangePosition = (e) => {
    setPosition(e.target.value)
  }

  const stateMenuItems = states.map(s => <MenuItem value={s}>{s}</MenuItem>)
  const positionMenuItems = positions.map(p => <MenuItem value={p}>{p}</MenuItem>)

  return (
    <Box
      id="hero"
      sx={(theme) => ({
        width: '100%',
        backgroundImage:
          theme.palette.mode === 'light'
            ? 'linear-gradient(180deg, #CEE5FD, #FFF)'
            : `linear-gradient(#02294F, ${alpha('#090E10', 0.0)})`,
        backgroundSize: '100% 20%',
        backgroundRepeat: 'no-repeat',
      })}
    >
      <Container
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          pt: { xs: 14, sm: 20 },
          pb: { xs: 8, sm: 12 },
        }}
      >
        <Stack spacing={2} useFlexGap sx={{ width: { xs: '100%', sm: '70%' } }}>
          <Typography
            component="h1"
            variant="h1"
            sx={{
              display: 'flex',
              flexDirection: { xs: 'column', md: 'row' },
              alignSelf: 'center',
              textAlign: 'center',
            }}
          >
            Make&nbsp;
            <Typography
              component="span"
              variant="h1"
              sx={{
                color: (theme) =>
                  theme.palette.mode === 'light' ? 'primary.main' : 'primary.light',
              }}
            >
              Job Search
            </Typography>
            &nbsp;Easier
          </Typography>
          <Typography variant="body1" textAlign="center" color="text.secondary">
            Explore our cutting-edge dashboard, delivering high-quality matches
            to your skills, location, and position type. <br />
            Elevate your job seeker experience with AI based intelligent pool.
          </Typography>
          <Stack
            direction={{ xs: 'column', sm: 'row' }}
            alignSelf="center"
            spacing={3}
            useFlexGap
            sx={{ pt: 2, width: { xs: '100%', sm: 'auto' } }}
          >
            <FormControl sx={{minWidth: 120, width: 160}}>
              <InputLabel id="state-select-label">State</InputLabel>
              <Select
                labelId="state-select"
                id="state-select"
                value={state}
                label="State"
                onChange={handleChangeState}
              >
                {
                  stateMenuItems
                }
              </Select>
            </FormControl>
            <FormControl sx={{minWidth: 120, width: 240}}>
              <InputLabel id="position-select-label">Position</InputLabel>
              <Select
                labelId="position-select"
                id="position-select"
                value={position}
                label="Position"
                onChange={handleChangePosition}
              >
                {
                  positionMenuItems
                }
              </Select>
            </FormControl>
            <TextField 
              id="skills-search" 
              label="Skills" type="search"              
              value={skills}
              onChange={handleChangeSkills}
              inputProps={{
                autocomplete: 'off',
                ariaLabel: 'Enter your skills',
              }}
            />
            <Button variant="contained" color="primary" sx={{alignSelf: "center"}} onClick={handleSearch}>
              Search
            </Button>
          </Stack>
          <Typography variant="caption" textAlign="center" sx={{ opacity: 0.8 }}>
            By clicking &quot;Search&quot; you will see related recommendations.&nbsp;
          </Typography>
        </Stack>
        {/* <iframe src="https://public.tableau.com/app/profile/bohan.ye/viz/JobRecommenderVisualizationTemplate/Dashboard?publish=yes&embed=true" width={1000} height={500} ></iframe> */}
        {jobs.length > 0 && <Box
          id="image"
          sx={(theme) => ({
            mt: { xs: 8, sm: 10 },
            alignSelf: 'center',
            height: { xs: 200, sm: 700 },
            width: '100%',
            backgroundImage:
              theme.palette.mode === 'light'
                ? 'url("/static/images/templates/templates-images/hero-light.png")'
                : 'url("/static/images/templates/templates-images/hero-dark.png")',
            backgroundSize: 'cover',
            borderRadius: '10px',
            outline: '1px solid',
            outlineColor:
              theme.palette.mode === 'light'
                ? alpha('#BFCCD9', 0.5)
                : alpha('#9CCCFC', 0.1),
            boxShadow:
              theme.palette.mode === 'light'
                ? `0 0 12px 8px ${alpha('#9CCCFC', 0.2)}`
                : `0 0 24px 12px ${alpha('#033363', 0.2)}`,
          })}
        >
          <img src={jobMap} style={jobMapStyle}></img>
        </Box>}
      </Container>
      {jobs.length > 0 && <JobRecommendations recommendedJobs={jobs.filter(job => states.includes(job.state.trim().toUpperCase()))} />}
      {jobs.length > 0 && 
        <>
          <Divider />
          <MarketAnalysis />
          <Divider />
        </>
      }
    </Box>
  );
}
