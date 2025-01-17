from console_ui.entity.ConsoleUiRoutingState import ConsoleUiRoutingState
from console_ui.entity.ConsoleUiState import ConsoleUiState
from console_ui.entity.Session import Session
from console_ui.repository.ConsoleUiRepository import ConsoleUiRepository
from custom_protocol.entity.CustomProtocol import CustomProtocol


class ConsoleUiRepositoryImpl(ConsoleUiRepository):
    __instance = None
    __menuTable = {}
    __convertCommandTable = {}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__menuTable[
                ConsoleUiRoutingState.INITIALIZED.value] = cls.__instance.__initialMenu
            cls.__instance.__menuTable[
                ConsoleUiRoutingState.PRODUCT_LIST.value] = cls.__instance.__productListMenu
            cls.__instance.__menuTable[
                ConsoleUiRoutingState.PRODUCT_DETAILS.value] = cls.__instance.__productReadMenu
            cls.__instance.__menuTable[
                ConsoleUiRoutingState.ORDER_LIST.value] = cls.__instance.__myOrderListMenu
            cls.__instance.__menuTable[
                ConsoleUiRoutingState.ORDER_DETAILS.value] = cls.__instance.__myOrderReadMenu

            cls.__instance.__convertCommandTable[
                ConsoleUiRoutingState.INITIALIZED.value] = cls.__instance.__initialStateCommandConverter
            cls.__instance.__convertCommandTable[
                ConsoleUiRoutingState.PRODUCT_LIST.value] = cls.__instance.__productListCommandConverter
            cls.__instance.__convertCommandTable[
                ConsoleUiRoutingState.PRODUCT_DETAILS.value] = cls.__instance.__productReadCommandConverter
            cls.__instance.__convertCommandTable[
                ConsoleUiRoutingState.ORDER_LIST.value] = cls.__instance.__myOrderListCommandConverter
            cls.__instance.__convertCommandTable[
                ConsoleUiRoutingState.ORDER_DETAILS.value] = cls.__instance.__myOrderReadCommandConverter

        return cls.__instance

    def __init__(self):
        print("ConsoleUiRepositoryImpl 생성자 호출")
        self.__consoleUiState = ConsoleUiState()
        self.__session = Session()

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __initialMenu(self):

        if self.getSessionId() is None:
            print('\033[92m1. 회원가입\033[0m')
            print('\033[94m2. 로그인\033[0m')
            print('\033[92m3. 상품 리스트 조회\033[94m')
            print('\033[94m4. 종료\033[0m')
            return

        print('\033[92m1. 로그아웃\033[0m')
        print('\033[94m2. 상품 리스트 조회\033[0m')
        print('\033[92m3. 내 주문 내역 확인\033[0m')
        print('\033[94m4. 회원탈퇴\033[0m')
        print('\033[92m5. 종료\033[0m')

    def __productListMenu(self):

        if self.getSessionId() is None:
            print('\033[92m1. 상품 조회\033[0m')
            print('\033[94m2. 뒤로 가기\033[0m')
            return

        print('\033[92m1. 상품 조회\033[0m')
        print('\033[94m2. 상품 등록\033[0m')
        print('\033[92m3. 뒤로 가기\033[0m')

    def __productReadMenu(self):

        if self.getSessionId() is None:
            print('\033[94m1. 뒤로 가기\033[0m')
            return

        print('\033[92m1. 상품 수정\033[0m')
        print('\033[94m2. 상품 삭제\033[0m')
        print('\033[92m3. 상품 주문\033[0m')
        print('\033[94m4. 뒤로 가기\033[0m')

    def __myOrderListMenu(self):
        print('\033[92m1. 주문 상세 보기\033[0m')
        print('\033[94m2. 뒤로 가기\033[0m')

    def __myOrderReadMenu(self):
        print('\033[94m1. 내 주문 삭제\033[0m')
        print('\033[92m2. 뒤로 가기\033[0m')

    def __initialStateCommandConverter(self, userCommand):

        if self.getSessionId() is None:
            if userCommand == 1:
                return CustomProtocol.ACCOUNT_REGISTER.value
            if userCommand == 2:
                return CustomProtocol.ACCOUNT_LOGIN.value
            if userCommand == 3:
                return CustomProtocol.PRODUCT_LIST.value
            if userCommand == 4:
                return CustomProtocol.EXIT.value

        if userCommand == 1:
            return CustomProtocol.ACCOUNT_LOGOUT.value
        if userCommand == 2:
            return CustomProtocol.PRODUCT_LIST.value
        if userCommand == 3:
            return CustomProtocol.ORDER_LIST.value
        if userCommand == 4:
            return CustomProtocol.ACCOUNT_REMOVE.value
        if userCommand == 5:
            return CustomProtocol.EXIT.value

        else:
            print("\033[91m잘못된 입력입니다! 다시 입력해주세요.\033[0m")

    def __productListCommandConverter(self, userCommand):

        if self.getSessionId() is None:
            if userCommand == 1:
                return CustomProtocol.PRODUCT_READ.value
            if userCommand == 2:
                return CustomProtocol.NOTHING.value

        if userCommand == 1:
            return CustomProtocol.PRODUCT_READ.value
        if userCommand == 2:
            return CustomProtocol.PRODUCT_REGISTER.value
        if userCommand == 3:
            return CustomProtocol.NOTHING.value

        else:
            print("\033[91m잘못된 입력입니다! 다시 입력해주세요.\033[0m")

    def __productReadCommandConverter(self, userCommand):

        if self.getSessionId() is None:
            if userCommand == 1:
                return CustomProtocol.PRODUCT_LIST.value

        if userCommand == 1:
            return CustomProtocol.PRODUCT_MODIFY.value
        if userCommand == 2:
            return CustomProtocol.PRODUCT_REMOVE.value
        if userCommand == 3:
            return CustomProtocol.PRODUCT_PURCHASE.value
        if userCommand == 4:
            return CustomProtocol.PRODUCT_LIST.value

        else:
            print("\033[91m잘못된 입력입니다! 다시 입력해주세요.\033[0m")

    def __myOrderListCommandConverter(self, userCommand):
        if userCommand == 1:
            return CustomProtocol.ORDER_READ.value
        if userCommand == 2:
            return CustomProtocol.NOTHING.value
        else:
            print("\033[91m잘못된 입력입니다! 다시 입력해주세요.\033[0m")

    def __myOrderReadCommandConverter(self, userCommand):
        if userCommand == 1:
            return CustomProtocol.ORDER_REMOVE.value
        if userCommand == 2:
            return CustomProtocol.ORDER_LIST.value
        else:
            print("\033[91m잘못된 입력입니다! 다시 입력해주세요.\033[0m")

    def menuPrinter(self):
        currentRoutingState = self.__consoleUiState.getCurrentRoutingState()
        menu = self.__menuTable[currentRoutingState]
        menu()

    def commandConverter(self, userCommand):
        currentRoutingState = self.__consoleUiState.getCurrentRoutingState()
        converter = self.__convertCommandTable[currentRoutingState]
        return converter(userCommand)

    def routingStateConverter(self, convertedUserChoice):
        if convertedUserChoice == CustomProtocol.NOTHING.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.INITIALIZED.value)

        elif convertedUserChoice == CustomProtocol.ACCOUNT_REGISTER.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.INITIALIZED.value)

        elif convertedUserChoice == CustomProtocol.ACCOUNT_LOGIN.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.INITIALIZED.value)

        elif convertedUserChoice == CustomProtocol.ACCOUNT_LOGOUT.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.INITIALIZED.value)

        elif convertedUserChoice == CustomProtocol.ACCOUNT_REMOVE.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.INITIALIZED.value)

        elif convertedUserChoice == CustomProtocol.PRODUCT_LIST.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.PRODUCT_LIST.value)

        elif convertedUserChoice == CustomProtocol.PRODUCT_REGISTER.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.PRODUCT_LIST.value)

        elif convertedUserChoice == CustomProtocol.PRODUCT_READ.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.PRODUCT_DETAILS.value)

        elif convertedUserChoice == CustomProtocol.PRODUCT_MODIFY.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.PRODUCT_DETAILS.value)

        elif convertedUserChoice == CustomProtocol.PRODUCT_PURCHASE.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.PRODUCT_DETAILS.value)

        elif convertedUserChoice == CustomProtocol.PRODUCT_REMOVE.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.PRODUCT_DETAILS.value)

        elif convertedUserChoice == CustomProtocol.ORDER_LIST.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.ORDER_LIST.value)

        elif convertedUserChoice == CustomProtocol.ORDER_READ.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.ORDER_DETAILS.value)

        elif convertedUserChoice == CustomProtocol.ORDER_REMOVE.value:
            self.saveCurrentRoutingState(ConsoleUiRoutingState.ORDER_DETAILS.value)

        elif convertedUserChoice == CustomProtocol.EXIT.value:
            pass

    def saveCurrentRoutingState(self, currentState):
        self.__consoleUiState.setCurrentRoutingState(currentState)

    def acquireCurrentRoutingState(self):
        return self.__consoleUiState.getCurrentRoutingState()

    def setSessionIdByUserId(self, userId):
        self.__session.setSessionId(userId)

    def getSessionId(self):
        return self.__session.getSessionId()

    def resetSessionId(self):
        self.__session.setSessionId(None)

    def setProductNumber(self, productNumber):
        self.__consoleUiState.setCurrentReadNumber(productNumber)

    def getProductNumber(self):
        return self.__consoleUiState.getCurrentReadNumber()

    def resetProductNumber(self):
        self.__consoleUiState.setCurrentReadNumber(None)
