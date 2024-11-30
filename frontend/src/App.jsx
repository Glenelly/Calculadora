import { Container, Stack, useColorModeValue } from '@chakra-ui/react';
import Navbar from "./components/Navbar"
import UserGrid from './components/UserGrid';
import { useState } from 'react';

export const BASE_URL = "postgresql://neondb_owner:mK5ErcHOtuv2@ep-dark-king-a54fcoql.us-east-2.aws.neon.tech/neondb?sslmode=require"

function App() {
  const [users, setUsers] = useState([])
  return (
    <Stack minH={"100vh"}  bg={useColorModeValue("pink.200", "pink.400")}>
      <Navbar setUsers={setUsers}/>

      <Container maxW={"1200px"} my={4}>

        <UserGrid users={users} setUsers={setUsers}/>
      </Container>
    </Stack>
  );
}

export default App;

