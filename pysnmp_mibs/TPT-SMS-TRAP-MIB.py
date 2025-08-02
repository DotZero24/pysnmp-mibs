_S='tptSmsUnQuarantineRequest'
_R='tptSmsQuarantineCommand'
_Q='tptSmsQuarantineReleaseAck'
_P='tptSmsQuarantineAck'
_O='tptSmsQuarantinePolicyNotification'
_N='tptSmsQuarantineReleaseRequest'
_M='tptSmsQuarantineRequest'
_L='tptSmsQuarantinePolicyName'
_K='tptSmsQuarantineDeviceMAC'
_J='Integer32'
_I='tptSmsRepDvVersion'
_H='tptSmsQuarantineDeviceIP'
_G='tptSmsQuarantinePolicyMatchData'
_F='tptSmsQuarantineNotifyData'
_E='tptSmsMessage'
_D='tptSmsQuarantineNotifyId'
_C='accessible-for-notify'
_B='TPT-SMS-TRAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_reg,=mibBuilder.importSymbols('TIPPINGPOINT-REG-MIB','tpt-reg')
tpt_sms_eventsV2,tpt_sms_groups,tpt_sms_notifypayload,tpt_smsMIBs=mibBuilder.importSymbols('TPT-SMSMIBS','tpt-sms-eventsV2','tpt-sms-groups','tpt-sms-notifypayload','tpt-smsMIBs')
tptSmsTrapsModule=ModuleIdentity((1,3,6,1,4,1,10734,3,4,4))
class _TptSmsQuarantineNotifyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_TptSmsQuarantineNotifyId_Type.__name__=_J
_TptSmsQuarantineNotifyId_Object=MibScalar
tptSmsQuarantineNotifyId=_TptSmsQuarantineNotifyId_Object((1,3,6,1,4,1,10734,3,4,3,1,1),_TptSmsQuarantineNotifyId_Type())
tptSmsQuarantineNotifyId.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsQuarantineNotifyId.setStatus(_A)
_TptSmsQuarantineNotifyData_Type=OctetString
_TptSmsQuarantineNotifyData_Object=MibScalar
tptSmsQuarantineNotifyData=_TptSmsQuarantineNotifyData_Object((1,3,6,1,4,1,10734,3,4,3,1,2),_TptSmsQuarantineNotifyData_Type())
tptSmsQuarantineNotifyData.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsQuarantineNotifyData.setStatus(_A)
_TptSmsQuarantinePolicyMatchData_Type=OctetString
_TptSmsQuarantinePolicyMatchData_Object=MibScalar
tptSmsQuarantinePolicyMatchData=_TptSmsQuarantinePolicyMatchData_Object((1,3,6,1,4,1,10734,3,4,3,1,3),_TptSmsQuarantinePolicyMatchData_Type())
tptSmsQuarantinePolicyMatchData.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsQuarantinePolicyMatchData.setStatus(_A)
_TptSmsQuarantineNotifyType_Type=OctetString
_TptSmsQuarantineNotifyType_Object=MibScalar
tptSmsQuarantineNotifyType=_TptSmsQuarantineNotifyType_Object((1,3,6,1,4,1,10734,3,4,3,1,4),_TptSmsQuarantineNotifyType_Type())
tptSmsQuarantineNotifyType.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsQuarantineNotifyType.setStatus(_A)
_TptSmsQuarantineDeviceIP_Type=IpAddress
_TptSmsQuarantineDeviceIP_Object=MibScalar
tptSmsQuarantineDeviceIP=_TptSmsQuarantineDeviceIP_Object((1,3,6,1,4,1,10734,3,4,3,1,5),_TptSmsQuarantineDeviceIP_Type())
tptSmsQuarantineDeviceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsQuarantineDeviceIP.setStatus(_A)
_TptSmsQuarantineDeviceMAC_Type=OctetString
_TptSmsQuarantineDeviceMAC_Object=MibScalar
tptSmsQuarantineDeviceMAC=_TptSmsQuarantineDeviceMAC_Object((1,3,6,1,4,1,10734,3,4,3,1,6),_TptSmsQuarantineDeviceMAC_Type())
tptSmsQuarantineDeviceMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsQuarantineDeviceMAC.setStatus(_A)
_TptSmsQuarantineSwitchPort_Type=OctetString
_TptSmsQuarantineSwitchPort_Object=MibScalar
tptSmsQuarantineSwitchPort=_TptSmsQuarantineSwitchPort_Object((1,3,6,1,4,1,10734,3,4,3,1,7),_TptSmsQuarantineSwitchPort_Type())
tptSmsQuarantineSwitchPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsQuarantineSwitchPort.setStatus(_A)
_TptSmsQuarantineEndpointUser_Type=OctetString
_TptSmsQuarantineEndpointUser_Object=MibScalar
tptSmsQuarantineEndpointUser=_TptSmsQuarantineEndpointUser_Object((1,3,6,1,4,1,10734,3,4,3,1,8),_TptSmsQuarantineEndpointUser_Type())
tptSmsQuarantineEndpointUser.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsQuarantineEndpointUser.setStatus(_A)
_TptSmsQuarantineNotifyActionList_Type=OctetString
_TptSmsQuarantineNotifyActionList_Object=MibScalar
tptSmsQuarantineNotifyActionList=_TptSmsQuarantineNotifyActionList_Object((1,3,6,1,4,1,10734,3,4,3,1,9),_TptSmsQuarantineNotifyActionList_Type())
tptSmsQuarantineNotifyActionList.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsQuarantineNotifyActionList.setStatus(_A)
_TptSmsQuarantineNotifyParamList_Type=OctetString
_TptSmsQuarantineNotifyParamList_Object=MibScalar
tptSmsQuarantineNotifyParamList=_TptSmsQuarantineNotifyParamList_Object((1,3,6,1,4,1,10734,3,4,3,1,10),_TptSmsQuarantineNotifyParamList_Type())
tptSmsQuarantineNotifyParamList.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsQuarantineNotifyParamList.setStatus(_A)
_TptSmsQuarantineNotifyOptionList_Type=OctetString
_TptSmsQuarantineNotifyOptionList_Object=MibScalar
tptSmsQuarantineNotifyOptionList=_TptSmsQuarantineNotifyOptionList_Object((1,3,6,1,4,1,10734,3,4,3,1,11),_TptSmsQuarantineNotifyOptionList_Type())
tptSmsQuarantineNotifyOptionList.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsQuarantineNotifyOptionList.setStatus(_A)
_TptSmsQuarantinePolicyName_Type=OctetString
_TptSmsQuarantinePolicyName_Object=MibScalar
tptSmsQuarantinePolicyName=_TptSmsQuarantinePolicyName_Object((1,3,6,1,4,1,10734,3,4,3,1,12),_TptSmsQuarantinePolicyName_Type())
tptSmsQuarantinePolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsQuarantinePolicyName.setStatus(_A)
_TptSmsRepDvVersion_Type=OctetString
_TptSmsRepDvVersion_Object=MibScalar
tptSmsRepDvVersion=_TptSmsRepDvVersion_Object((1,3,6,1,4,1,10734,3,4,3,1,13),_TptSmsRepDvVersion_Type())
tptSmsRepDvVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsRepDvVersion.setStatus(_A)
_TptSmsMessage_Type=OctetString
_TptSmsMessage_Object=MibScalar
tptSmsMessage=_TptSmsMessage_Object((1,3,6,1,4,1,10734,3,4,3,1,14),_TptSmsMessage_Type())
tptSmsMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:tptSmsMessage.setStatus(_A)
tptSmsQuarantineDataGroup=ObjectGroup((1,3,6,1,4,1,10734,3,4,1,1,1))
tptSmsQuarantineDataGroup.setObjects(*((_B,_D),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:tptSmsQuarantineDataGroup.setStatus(_A)
tptSmsQuarantineRequest=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,1))
tptSmsQuarantineRequest.setObjects(*((_B,_D),(_B,_F)))
if mibBuilder.loadTexts:tptSmsQuarantineRequest.setStatus(_A)
tptSmsQuarantineAck=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,2))
tptSmsQuarantineAck.setObjects(*((_B,_D),(_B,_F)))
if mibBuilder.loadTexts:tptSmsQuarantineAck.setStatus(_A)
tptSmsQuarantineReleaseRequest=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,3))
tptSmsQuarantineReleaseRequest.setObjects(*((_B,_D),(_B,_F)))
if mibBuilder.loadTexts:tptSmsQuarantineReleaseRequest.setStatus(_A)
tptSmsQuarantineReleaseAck=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,4))
tptSmsQuarantineReleaseAck.setObjects(*((_B,_D),(_B,_F)))
if mibBuilder.loadTexts:tptSmsQuarantineReleaseAck.setStatus(_A)
tptSmsQuarantinePolicyNotification=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,5))
tptSmsQuarantinePolicyNotification.setObjects((_B,_G))
if mibBuilder.loadTexts:tptSmsQuarantinePolicyNotification.setStatus(_A)
tptSmsUnQuarantineRequest=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,6))
tptSmsUnQuarantineRequest.setObjects(*((_B,_D),(_B,_H),(_B,_K)))
if mibBuilder.loadTexts:tptSmsUnQuarantineRequest.setStatus(_A)
tptSmsBoot=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,7))
if mibBuilder.loadTexts:tptSmsBoot.setStatus(_A)
tptSmsReboot=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,8))
if mibBuilder.loadTexts:tptSmsReboot.setStatus(_A)
tptSmsShuttingDown=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,9))
if mibBuilder.loadTexts:tptSmsShuttingDown.setStatus(_A)
tptSmsReady=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,10))
if mibBuilder.loadTexts:tptSmsReady.setStatus(_A)
tptSmsAuthenticationError=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,11))
if mibBuilder.loadTexts:tptSmsAuthenticationError.setStatus(_A)
tptSmsEgpNeighborDownstate=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,12))
if mibBuilder.loadTexts:tptSmsEgpNeighborDownstate.setStatus(_A)
tptSmsSystemRestart=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,13))
if mibBuilder.loadTexts:tptSmsSystemRestart.setStatus(_A)
tptSmsQuarantineCommand=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,14))
tptSmsQuarantineCommand.setObjects(*((_B,_H),(_B,_L)))
if mibBuilder.loadTexts:tptSmsQuarantineCommand.setStatus(_A)
tptSmsRepDvVerifySuccess=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,15))
tptSmsRepDvVerifySuccess.setObjects(*((_B,_I),(_B,_E)))
if mibBuilder.loadTexts:tptSmsRepDvVerifySuccess.setStatus(_A)
tptSmsRepDvVerifyFail=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,16))
tptSmsRepDvVerifyFail.setObjects(*((_B,_I),(_B,_E)))
if mibBuilder.loadTexts:tptSmsRepDvVerifyFail.setStatus(_A)
tptSmsTest=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,17))
tptSmsTest.setObjects((_B,_E))
if mibBuilder.loadTexts:tptSmsTest.setStatus(_A)
tptSmsRebootingDevice=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,18))
tptSmsRebootingDevice.setObjects((_B,_E))
if mibBuilder.loadTexts:tptSmsRebootingDevice.setStatus(_A)
tptDeviceNonComm=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,19))
tptDeviceNonComm.setObjects((_B,_E))
if mibBuilder.loadTexts:tptDeviceNonComm.setStatus(_A)
tptDeviceBooted=NotificationType((1,3,6,1,4,1,10734,3,4,3,0,20))
tptDeviceBooted.setObjects((_B,_E))
if mibBuilder.loadTexts:tptDeviceBooted.setStatus(_A)
tptSmsQuarantineNotifyGroup=NotificationGroup((1,3,6,1,4,1,10734,3,4,1,1,2))
tptSmsQuarantineNotifyGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:tptSmsQuarantineNotifyGroup.setStatus(_A)
tptSmsQuarantineNotifyAckGroup=NotificationGroup((1,3,6,1,4,1,10734,3,4,1,1,3))
tptSmsQuarantineNotifyAckGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:tptSmsQuarantineNotifyAckGroup.setStatus(_A)
tptSmsQuarantineRequestGroup=NotificationGroup((1,3,6,1,4,1,10734,3,4,1,1,4))
tptSmsQuarantineRequestGroup.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:tptSmsQuarantineRequestGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tptSmsQuarantineDataGroup':tptSmsQuarantineDataGroup,'tptSmsQuarantineNotifyGroup':tptSmsQuarantineNotifyGroup,'tptSmsQuarantineNotifyAckGroup':tptSmsQuarantineNotifyAckGroup,'tptSmsQuarantineRequestGroup':tptSmsQuarantineRequestGroup,_M:tptSmsQuarantineRequest,_P:tptSmsQuarantineAck,_N:tptSmsQuarantineReleaseRequest,_Q:tptSmsQuarantineReleaseAck,_O:tptSmsQuarantinePolicyNotification,_S:tptSmsUnQuarantineRequest,'tptSmsBoot':tptSmsBoot,'tptSmsReboot':tptSmsReboot,'tptSmsShuttingDown':tptSmsShuttingDown,'tptSmsReady':tptSmsReady,'tptSmsAuthenticationError':tptSmsAuthenticationError,'tptSmsEgpNeighborDownstate':tptSmsEgpNeighborDownstate,'tptSmsSystemRestart':tptSmsSystemRestart,_R:tptSmsQuarantineCommand,'tptSmsRepDvVerifySuccess':tptSmsRepDvVerifySuccess,'tptSmsRepDvVerifyFail':tptSmsRepDvVerifyFail,'tptSmsTest':tptSmsTest,'tptSmsRebootingDevice':tptSmsRebootingDevice,'tptDeviceNonComm':tptDeviceNonComm,'tptDeviceBooted':tptDeviceBooted,_D:tptSmsQuarantineNotifyId,_F:tptSmsQuarantineNotifyData,_G:tptSmsQuarantinePolicyMatchData,'tptSmsQuarantineNotifyType':tptSmsQuarantineNotifyType,_H:tptSmsQuarantineDeviceIP,_K:tptSmsQuarantineDeviceMAC,'tptSmsQuarantineSwitchPort':tptSmsQuarantineSwitchPort,'tptSmsQuarantineEndpointUser':tptSmsQuarantineEndpointUser,'tptSmsQuarantineNotifyActionList':tptSmsQuarantineNotifyActionList,'tptSmsQuarantineNotifyParamList':tptSmsQuarantineNotifyParamList,'tptSmsQuarantineNotifyOptionList':tptSmsQuarantineNotifyOptionList,_L:tptSmsQuarantinePolicyName,_I:tptSmsRepDvVersion,_E:tptSmsMessage,'tptSmsTrapsModule':tptSmsTrapsModule})