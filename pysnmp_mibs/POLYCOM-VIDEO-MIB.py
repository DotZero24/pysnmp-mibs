_a='polycomVSLatency'
_Z='polycomVSJitter'
_Y='polycomVSPercentPacketLoss'
_X='polycomVSUPnPStatus'
_W='polycomVSCurrentNicLineCount'
_V='polycomVSPreviousNicLineCount'
_U='polycomVSV35PortsEnabled'
_T='polycomVSCurrentNicType'
_S='polycomVSPreviousNicType'
_R='polycomVSCurrentIPAddress'
_Q='polycomVSPreviousIPAddress'
_P='polycomVSTimeServerSetting'
_O='polycomVSAutoAnswerSetting'
_N='polycomVSMicData'
_M='polycomVSPlead'
_L='polycomVSReason'
_K='NotificationType'
_J='polycomVSGatekeeperAddress'
_I='polycomVSTimeServerAddress'
_H='polycomVSAuthClientAddress'
_G='polycomVSAuthLocation'
_F='polycomVSGDSAddress'
_E='polycomVSPhoneNumber'
_D='polycomVSNicLineNumber'
_C='mandatory'
_B='read-only'
_A='POLYCOM-VIDEO-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_K,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_K,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Polycom_ObjectIdentity=ObjectIdentity
polycom=_Polycom_ObjectIdentity((1,3,6,1,4,1,2684))
_PolycomVideo_ObjectIdentity=ObjectIdentity
polycomVideo=_PolycomVideo_ObjectIdentity((1,3,6,1,4,1,2684,1))
_PolycomViewStation_ObjectIdentity=ObjectIdentity
polycomViewStation=_PolycomViewStation_ObjectIdentity((1,3,6,1,4,1,2684,1,1))
_PolycomVSAuthLocation_Type=Integer32
_PolycomVSAuthLocation_Object=MibScalar
polycomVSAuthLocation=_PolycomVSAuthLocation_Object((1,3,6,1,4,1,2684,1,1,1),_PolycomVSAuthLocation_Type())
polycomVSAuthLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSAuthLocation.setStatus(_C)
_PolycomVSPhoneNumber_Type=DisplayString
_PolycomVSPhoneNumber_Object=MibScalar
polycomVSPhoneNumber=_PolycomVSPhoneNumber_Object((1,3,6,1,4,1,2684,1,1,2),_PolycomVSPhoneNumber_Type())
polycomVSPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSPhoneNumber.setStatus(_C)
_PolycomVSReason_Type=DisplayString
_PolycomVSReason_Object=MibScalar
polycomVSReason=_PolycomVSReason_Object((1,3,6,1,4,1,2684,1,1,3),_PolycomVSReason_Type())
polycomVSReason.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSReason.setStatus(_C)
_PolycomVSPlead_Type=DisplayString
_PolycomVSPlead_Object=MibScalar
polycomVSPlead=_PolycomVSPlead_Object((1,3,6,1,4,1,2684,1,1,4),_PolycomVSPlead_Type())
polycomVSPlead.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSPlead.setStatus(_C)
_PolycomVSMicData_Type=DisplayString
_PolycomVSMicData_Object=MibScalar
polycomVSMicData=_PolycomVSMicData_Object((1,3,6,1,4,1,2684,1,1,5),_PolycomVSMicData_Type())
polycomVSMicData.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSMicData.setStatus(_C)
_PolycomVSAutoAnswerSetting_Type=DisplayString
_PolycomVSAutoAnswerSetting_Object=MibScalar
polycomVSAutoAnswerSetting=_PolycomVSAutoAnswerSetting_Object((1,3,6,1,4,1,2684,1,1,6),_PolycomVSAutoAnswerSetting_Type())
polycomVSAutoAnswerSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSAutoAnswerSetting.setStatus(_C)
_PolycomVSTimeServerAddress_Type=DisplayString
_PolycomVSTimeServerAddress_Object=MibScalar
polycomVSTimeServerAddress=_PolycomVSTimeServerAddress_Object((1,3,6,1,4,1,2684,1,1,7),_PolycomVSTimeServerAddress_Type())
polycomVSTimeServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSTimeServerAddress.setStatus(_C)
_PolycomVSTimeServerSetting_Type=DisplayString
_PolycomVSTimeServerSetting_Object=MibScalar
polycomVSTimeServerSetting=_PolycomVSTimeServerSetting_Object((1,3,6,1,4,1,2684,1,1,8),_PolycomVSTimeServerSetting_Type())
polycomVSTimeServerSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSTimeServerSetting.setStatus(_C)
_PolycomVSGDSAddress_Type=DisplayString
_PolycomVSGDSAddress_Object=MibScalar
polycomVSGDSAddress=_PolycomVSGDSAddress_Object((1,3,6,1,4,1,2684,1,1,9),_PolycomVSGDSAddress_Type())
polycomVSGDSAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSGDSAddress.setStatus(_C)
_PolycomVSGatekeeperAddress_Type=DisplayString
_PolycomVSGatekeeperAddress_Object=MibScalar
polycomVSGatekeeperAddress=_PolycomVSGatekeeperAddress_Object((1,3,6,1,4,1,2684,1,1,10),_PolycomVSGatekeeperAddress_Type())
polycomVSGatekeeperAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSGatekeeperAddress.setStatus(_C)
_PolycomVSPreviousIPAddress_Type=DisplayString
_PolycomVSPreviousIPAddress_Object=MibScalar
polycomVSPreviousIPAddress=_PolycomVSPreviousIPAddress_Object((1,3,6,1,4,1,2684,1,1,11),_PolycomVSPreviousIPAddress_Type())
polycomVSPreviousIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSPreviousIPAddress.setStatus(_C)
_PolycomVSCurrentIPAddress_Type=DisplayString
_PolycomVSCurrentIPAddress_Object=MibScalar
polycomVSCurrentIPAddress=_PolycomVSCurrentIPAddress_Object((1,3,6,1,4,1,2684,1,1,12),_PolycomVSCurrentIPAddress_Type())
polycomVSCurrentIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSCurrentIPAddress.setStatus(_C)
_PolycomVSPreviousNicType_Type=DisplayString
_PolycomVSPreviousNicType_Object=MibScalar
polycomVSPreviousNicType=_PolycomVSPreviousNicType_Object((1,3,6,1,4,1,2684,1,1,13),_PolycomVSPreviousNicType_Type())
polycomVSPreviousNicType.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSPreviousNicType.setStatus(_C)
_PolycomVSCurrentNicType_Type=DisplayString
_PolycomVSCurrentNicType_Object=MibScalar
polycomVSCurrentNicType=_PolycomVSCurrentNicType_Object((1,3,6,1,4,1,2684,1,1,14),_PolycomVSCurrentNicType_Type())
polycomVSCurrentNicType.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSCurrentNicType.setStatus(_C)
_PolycomVSNicLineNumber_Type=DisplayString
_PolycomVSNicLineNumber_Object=MibScalar
polycomVSNicLineNumber=_PolycomVSNicLineNumber_Object((1,3,6,1,4,1,2684,1,1,15),_PolycomVSNicLineNumber_Type())
polycomVSNicLineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSNicLineNumber.setStatus(_C)
_PolycomVSPreviousNicLineCount_Type=DisplayString
_PolycomVSPreviousNicLineCount_Object=MibScalar
polycomVSPreviousNicLineCount=_PolycomVSPreviousNicLineCount_Object((1,3,6,1,4,1,2684,1,1,16),_PolycomVSPreviousNicLineCount_Type())
polycomVSPreviousNicLineCount.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSPreviousNicLineCount.setStatus(_C)
_PolycomVSCurrentNicLineCount_Type=DisplayString
_PolycomVSCurrentNicLineCount_Object=MibScalar
polycomVSCurrentNicLineCount=_PolycomVSCurrentNicLineCount_Object((1,3,6,1,4,1,2684,1,1,17),_PolycomVSCurrentNicLineCount_Type())
polycomVSCurrentNicLineCount.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSCurrentNicLineCount.setStatus(_C)
_PolycomVSV35PortsEnabled_Type=DisplayString
_PolycomVSV35PortsEnabled_Object=MibScalar
polycomVSV35PortsEnabled=_PolycomVSV35PortsEnabled_Object((1,3,6,1,4,1,2684,1,1,18),_PolycomVSV35PortsEnabled_Type())
polycomVSV35PortsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSV35PortsEnabled.setStatus(_C)
_PolycomVSAuthClientAddress_Type=DisplayString
_PolycomVSAuthClientAddress_Object=MibScalar
polycomVSAuthClientAddress=_PolycomVSAuthClientAddress_Object((1,3,6,1,4,1,2684,1,1,19),_PolycomVSAuthClientAddress_Type())
polycomVSAuthClientAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSAuthClientAddress.setStatus(_C)
_PolycomVSUPnPStatus_Type=DisplayString
_PolycomVSUPnPStatus_Object=MibScalar
polycomVSUPnPStatus=_PolycomVSUPnPStatus_Object((1,3,6,1,4,1,2684,1,1,20),_PolycomVSUPnPStatus_Type())
polycomVSUPnPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSUPnPStatus.setStatus(_C)
_PolycomVSPercentPacketLoss_Type=DisplayString
_PolycomVSPercentPacketLoss_Object=MibScalar
polycomVSPercentPacketLoss=_PolycomVSPercentPacketLoss_Object((1,3,6,1,4,1,2684,1,1,21),_PolycomVSPercentPacketLoss_Type())
polycomVSPercentPacketLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSPercentPacketLoss.setStatus(_C)
_PolycomVSJitter_Type=DisplayString
_PolycomVSJitter_Object=MibScalar
polycomVSJitter=_PolycomVSJitter_Object((1,3,6,1,4,1,2684,1,1,22),_PolycomVSJitter_Type())
polycomVSJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSJitter.setStatus(_C)
_PolycomVSLatency_Type=DisplayString
_PolycomVSLatency_Object=MibScalar
polycomVSLatency=_PolycomVSLatency_Object((1,3,6,1,4,1,2684,1,1,23),_PolycomVSLatency_Type())
polycomVSLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:polycomVSLatency.setStatus(_C)
_PolycomAudio_ObjectIdentity=ObjectIdentity
polycomAudio=_PolycomAudio_ObjectIdentity((1,3,6,1,4,1,2684,2))
_PolycomData_ObjectIdentity=ObjectIdentity
polycomData=_PolycomData_ObjectIdentity((1,3,6,1,4,1,2684,3))
loginOK=NotificationType((1,3,6,1,4,1,2684,1,1,0,1))
loginOK.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:loginOK.setStatus('')
loginFail=NotificationType((1,3,6,1,4,1,2684,1,1,0,2))
loginFail.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:loginFail.setStatus('')
lowBattery=NotificationType((1,3,6,1,4,1,2684,1,1,0,3))
if mibBuilder.loadTexts:lowBattery.setStatus('')
callUp=NotificationType((1,3,6,1,4,1,2684,1,1,0,4))
callUp.setObjects((_A,_E))
if mibBuilder.loadTexts:callUp.setStatus('')
callDown=NotificationType((1,3,6,1,4,1,2684,1,1,0,5))
callDown.setObjects((_A,_E))
if mibBuilder.loadTexts:callDown.setStatus('')
callFail=NotificationType((1,3,6,1,4,1,2684,1,1,0,6))
callFail.setObjects(*((_A,_L),(_A,_E)))
if mibBuilder.loadTexts:callFail.setStatus('')
userAssist=NotificationType((1,3,6,1,4,1,2684,1,1,0,7))
userAssist.setObjects((_A,_M))
if mibBuilder.loadTexts:userAssist.setStatus('')
visualConcertUp=NotificationType((1,3,6,1,4,1,2684,1,1,0,8))
if mibBuilder.loadTexts:visualConcertUp.setStatus('')
visualConcertOff=NotificationType((1,3,6,1,4,1,2684,1,1,0,9))
if mibBuilder.loadTexts:visualConcertOff.setStatus('')
micChange=NotificationType((1,3,6,1,4,1,2684,1,1,0,10))
micChange.setObjects((_A,_N))
if mibBuilder.loadTexts:micChange.setStatus('')
autoAnswerChange=NotificationType((1,3,6,1,4,1,2684,1,1,0,11))
autoAnswerChange.setObjects((_A,_O))
if mibBuilder.loadTexts:autoAnswerChange.setStatus('')
timeServerUp=NotificationType((1,3,6,1,4,1,2684,1,1,0,12))
timeServerUp.setObjects((_A,_I))
if mibBuilder.loadTexts:timeServerUp.setStatus('')
timeServerDown=NotificationType((1,3,6,1,4,1,2684,1,1,0,13))
timeServerDown.setObjects((_A,_I))
if mibBuilder.loadTexts:timeServerDown.setStatus('')
timeServerOn=NotificationType((1,3,6,1,4,1,2684,1,1,0,14))
timeServerOn.setObjects((_A,_P))
if mibBuilder.loadTexts:timeServerOn.setStatus('')
timeServerOff=NotificationType((1,3,6,1,4,1,2684,1,1,0,15))
if mibBuilder.loadTexts:timeServerOff.setStatus('')
gdsUp=NotificationType((1,3,6,1,4,1,2684,1,1,0,16))
gdsUp.setObjects((_A,_F))
if mibBuilder.loadTexts:gdsUp.setStatus('')
gdsDown=NotificationType((1,3,6,1,4,1,2684,1,1,0,17))
gdsDown.setObjects((_A,_F))
if mibBuilder.loadTexts:gdsDown.setStatus('')
gdsOff=NotificationType((1,3,6,1,4,1,2684,1,1,0,18))
gdsOff.setObjects((_A,_F))
if mibBuilder.loadTexts:gdsOff.setStatus('')
gatekeeperReg=NotificationType((1,3,6,1,4,1,2684,1,1,0,19))
gatekeeperReg.setObjects((_A,_J))
if mibBuilder.loadTexts:gatekeeperReg.setStatus('')
gatekeeperDown=NotificationType((1,3,6,1,4,1,2684,1,1,0,20))
gatekeeperDown.setObjects((_A,_J))
if mibBuilder.loadTexts:gatekeeperDown.setStatus('')
gatekeeperOff=NotificationType((1,3,6,1,4,1,2684,1,1,0,21))
if mibBuilder.loadTexts:gatekeeperOff.setStatus('')
ipAddressChange=NotificationType((1,3,6,1,4,1,2684,1,1,0,22))
ipAddressChange.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ipAddressChange.setStatus('')
interfaceTypeChange=NotificationType((1,3,6,1,4,1,2684,1,1,0,23))
interfaceTypeChange.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:interfaceTypeChange.setStatus('')
lineEnabled=NotificationType((1,3,6,1,4,1,2684,1,1,0,24))
lineEnabled.setObjects((_A,_D))
if mibBuilder.loadTexts:lineEnabled.setStatus('')
lineDisabled=NotificationType((1,3,6,1,4,1,2684,1,1,0,25))
lineDisabled.setObjects((_A,_D))
if mibBuilder.loadTexts:lineDisabled.setStatus('')
lineUp=NotificationType((1,3,6,1,4,1,2684,1,1,0,26))
lineUp.setObjects((_A,_D))
if mibBuilder.loadTexts:lineUp.setStatus('')
lineDown=NotificationType((1,3,6,1,4,1,2684,1,1,0,27))
lineDown.setObjects((_A,_D))
if mibBuilder.loadTexts:lineDown.setStatus('')
v35PortsEnabled=NotificationType((1,3,6,1,4,1,2684,1,1,0,28))
v35PortsEnabled.setObjects((_A,_U))
if mibBuilder.loadTexts:v35PortsEnabled.setStatus('')
lineCountChange=NotificationType((1,3,6,1,4,1,2684,1,1,0,29))
lineCountChange.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:lineCountChange.setStatus('')
mainCameraUp=NotificationType((1,3,6,1,4,1,2684,1,1,0,30))
if mibBuilder.loadTexts:mainCameraUp.setStatus('')
mainCameraDown=NotificationType((1,3,6,1,4,1,2684,1,1,0,31))
if mibBuilder.loadTexts:mainCameraDown.setStatus('')
upnpChange=NotificationType((1,3,6,1,4,1,2684,1,1,0,32))
upnpChange.setObjects((_A,_X))
if mibBuilder.loadTexts:upnpChange.setStatus('')
percentPacketLossExcessive=NotificationType((1,3,6,1,4,1,2684,1,1,0,33))
percentPacketLossExcessive.setObjects((_A,_Y))
if mibBuilder.loadTexts:percentPacketLossExcessive.setStatus('')
jitterExcessive=NotificationType((1,3,6,1,4,1,2684,1,1,0,34))
jitterExcessive.setObjects((_A,_Z))
if mibBuilder.loadTexts:jitterExcessive.setStatus('')
latencyExcessive=NotificationType((1,3,6,1,4,1,2684,1,1,0,35))
latencyExcessive.setObjects((_A,_a))
if mibBuilder.loadTexts:latencyExcessive.setStatus('')
mibBuilder.exportSymbols(_A,**{'polycom':polycom,'polycomVideo':polycomVideo,'polycomViewStation':polycomViewStation,'loginOK':loginOK,'loginFail':loginFail,'lowBattery':lowBattery,'callUp':callUp,'callDown':callDown,'callFail':callFail,'userAssist':userAssist,'visualConcertUp':visualConcertUp,'visualConcertOff':visualConcertOff,'micChange':micChange,'autoAnswerChange':autoAnswerChange,'timeServerUp':timeServerUp,'timeServerDown':timeServerDown,'timeServerOn':timeServerOn,'timeServerOff':timeServerOff,'gdsUp':gdsUp,'gdsDown':gdsDown,'gdsOff':gdsOff,'gatekeeperReg':gatekeeperReg,'gatekeeperDown':gatekeeperDown,'gatekeeperOff':gatekeeperOff,'ipAddressChange':ipAddressChange,'interfaceTypeChange':interfaceTypeChange,'lineEnabled':lineEnabled,'lineDisabled':lineDisabled,'lineUp':lineUp,'lineDown':lineDown,'v35PortsEnabled':v35PortsEnabled,'lineCountChange':lineCountChange,'mainCameraUp':mainCameraUp,'mainCameraDown':mainCameraDown,'upnpChange':upnpChange,'percentPacketLossExcessive':percentPacketLossExcessive,'jitterExcessive':jitterExcessive,'latencyExcessive':latencyExcessive,_G:polycomVSAuthLocation,_E:polycomVSPhoneNumber,_L:polycomVSReason,_M:polycomVSPlead,_N:polycomVSMicData,_O:polycomVSAutoAnswerSetting,_I:polycomVSTimeServerAddress,_P:polycomVSTimeServerSetting,_F:polycomVSGDSAddress,_J:polycomVSGatekeeperAddress,_Q:polycomVSPreviousIPAddress,_R:polycomVSCurrentIPAddress,_S:polycomVSPreviousNicType,_T:polycomVSCurrentNicType,_D:polycomVSNicLineNumber,_V:polycomVSPreviousNicLineCount,_W:polycomVSCurrentNicLineCount,_U:polycomVSV35PortsEnabled,_H:polycomVSAuthClientAddress,_X:polycomVSUPnPStatus,_Y:polycomVSPercentPacketLoss,_Z:polycomVSJitter,_a:polycomVSLatency,'polycomAudio':polycomAudio,'polycomData':polycomData})