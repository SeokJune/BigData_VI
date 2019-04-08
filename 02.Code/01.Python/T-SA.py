'''
T-SA.py
      Title: T-SA의 기능 실행
     Author: Lee SeokJune
  Create on: 2019.04.08
'''
while True:
    '''
      기능 선택 입력 받
      1. KeyWord Search
      2. User Search
      3. Visualization
      4. Exit
    '''
    print('1. Keyword Search')
    print('2. User Search')
    print('3. Visualization')
    print('4. Exit')
    print('Choice Number: ')
    cNum = input()
    
    # 입력 오류 체크
    if cNum not in ['1', '2', '3', '4']:
        print('Re-enter')
        continue

    # 종료 실행(4)
    if cNum == '4':
        print('Exit!!')
        break

    '''
      기능 실행(1, 2, 3)
    '''
    # Keyword Search 실행(1)
    if cNum == '1':
        print('Keyword Search 시작')
        # TwitterAPI.py 작업

        # dbModule.py 작업
        
        print('Keyword Search 완료')
    # User Search 실행(2)
    elif cNum == '2':
        print('User Search 시작')
        # TwitterAPI.py 작업

        # dbModule.py 작업
        
        print('User Search 완료')
    # Visualization 실행(3)
    elif cNum == '3':
        print('Visualization 시작')
        # Visualization.py 작업
        
        print('Visualization 완료')