import { Container, Stack, useColorModeValue } from '@chakra-ui/react';
import Navbar from "./components/Navbar"
import UserGrid from './components/UserGrid';
import { useState } from 'react';

export const BASE_URL = "http://127.0.0.1:5000/api"

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

