import { Button, Flex, FormControl, FormLabel, Input, Modal, ModalBody,
     ModalCloseButton, ModalContent, ModalFooter, ModalHeader, ModalOverlay, useColorModeValue, useDisclosure } from "@chakra-ui/react";
import { BiAddToQueue} from "react-icons/bi";

const CreateUserModal = () => {
    const {isOpen, onOpen, onClose} = useDisclosure()
    return <>
        <Button onClick={onOpen}>
            <BiAddToQueue size={20}/>
        </Button>

        <Modal
            isOpen={isOpen}
            onClose={onClose}
        >
            <ModalOverlay />
            <ModalContent  bg={useColorModeValue("pink.300", "pink.400")}>
                <ModalHeader> Adicionar usuário</ModalHeader>
                <ModalCloseButton/>

                <ModalBody pb={5}>
                    <Flex alignItems={"center"} gap={3}>
                        <FormControl>
                            <FormLabel>Nome</FormLabel>
                            <Input placeholder="Nome completo aqui "></Input>
                        </FormControl> 
                    </Flex>
                        <FormControl alignItems={"center"} gap={3}>
                            <FormLabel>Idade</FormLabel>
                            <Input placeholder="Idade aqui "></Input>
                        </FormControl>

                        <FormControl alignItems={"center"} gap={3}>
                            <FormLabel>Expressão</FormLabel>
                            <Input placeholder="Expressão aqui "></Input>
                        </FormControl>
                </ModalBody>

                <ModalFooter>
                    <Button colorScheme='pink' color={'blank'} mr={5}>
                        Adicionar
                    </Button>
                    <Button onClick={onClose}>Cancelar</Button>
                </ModalFooter>

            </ModalContent>

        </Modal>
    
    </>
    }

export default CreateUserModal;