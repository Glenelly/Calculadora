import { Card, CardHeader, Flex, Heading, Box, Text, IconButton , useColorModeValue, CardBody, Button} from "@chakra-ui/react"
import { BiTrash } from "react-icons/bi";
import EditModal from "./EditModal";

const UserCard = ({user}) => {
  return <Card>
    <CardHeader bg={useColorModeValue("pink.300", "pink.500")}>
        <Flex gap={4}>
            <Flex flex={"1"} gap={4} alignItems={"center"}>
                <Box>
                    <Heading size='sm'>{user.nome}</Heading>
                    <Text>Idade: {user.idade}</Text>
                    <Text>Expressão: {user.expressao}</Text>
                </Box>
            </Flex>

            <Flex>
                <EditModal/>
                <IconButton
                    variant='ghost'
                    colorScheme='red'
                    size={"sm"}
                    aria-label="Ver menu"
                    icon={<BiTrash size={20} />}
                />
            </Flex>
        </Flex>
    </CardHeader>

    <CardBody bg={useColorModeValue("pink.300", "pink.500")}>
        <Button>Calcular Expressão</Button>
    </CardBody>
  </Card>
}

export default UserCard;