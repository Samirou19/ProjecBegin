import PresenterDisplay as Present

launch = Present.FirstStep()
value = launch.retour()
print(value)
launch.SaveUser()
launch.SecondStep()
