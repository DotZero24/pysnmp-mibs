_Q='h3cSIPAuthenReqMethod'
_P='h3cSIPRegisterFailReason'
_O='h3cSIPMsgResponseIndex'
_N='not-accessible'
_M='h3cSIPMsgIndex'
_L='h3cSIPID'
_K='read-create'
_J='h3cSIPServerPort'
_I='h3cSIPServerIPAddress'
_H='h3cSIPServerIPAddressType'
_G='OctetString'
_F='accessible-for-notify'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='H3C-VOSIP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cVoice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cVoice')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cVoSIP=ModuleIdentity((1,3,6,1,4,1,2011,10,2,39,12))
if mibBuilder.loadTexts:h3cVoSIP.setRevisions(('2005-03-15 00:00',))
class SipMsgType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),('register',2),('invite',3),('ack',4),('prack',5),('cancel',6),('bye',7),('info',8)))
_H3cSIPClientMIB_ObjectIdentity=ObjectIdentity
h3cSIPClientMIB=_H3cSIPClientMIB_ObjectIdentity((1,3,6,1,4,1,2011,10,2,39,12,1))
_H3cSIPClientConfigObjects_ObjectIdentity=ObjectIdentity
h3cSIPClientConfigObjects=_H3cSIPClientConfigObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,39,12,1,1))
class _H3cSIPID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cSIPID_Type.__name__=_G
_H3cSIPID_Object=MibScalar
h3cSIPID=_H3cSIPID_Object((1,3,6,1,4,1,2011,10,2,39,12,1,1,1),_H3cSIPID_Type())
h3cSIPID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSIPID.setStatus(_A)
class _H3cSIPPasswordType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('simple',1),('cipher',2)))
_H3cSIPPasswordType_Type.__name__=_D
_H3cSIPPasswordType_Object=MibScalar
h3cSIPPasswordType=_H3cSIPPasswordType_Object((1,3,6,1,4,1,2011,10,2,39,12,1,1,2),_H3cSIPPasswordType_Type())
h3cSIPPasswordType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSIPPasswordType.setStatus(_A)
_H3cSIPPassword_Type=OctetString
_H3cSIPPassword_Object=MibScalar
h3cSIPPassword=_H3cSIPPassword_Object((1,3,6,1,4,1,2011,10,2,39,12,1,1,3),_H3cSIPPassword_Type())
h3cSIPPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSIPPassword.setStatus(_A)
_H3cSIPSourceIPAddressType_Type=InetAddressType
_H3cSIPSourceIPAddressType_Object=MibScalar
h3cSIPSourceIPAddressType=_H3cSIPSourceIPAddressType_Object((1,3,6,1,4,1,2011,10,2,39,12,1,1,4),_H3cSIPSourceIPAddressType_Type())
h3cSIPSourceIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSIPSourceIPAddressType.setStatus(_A)
_H3cSIPSourceIP_Type=InetAddress
_H3cSIPSourceIP_Object=MibScalar
h3cSIPSourceIP=_H3cSIPSourceIP_Object((1,3,6,1,4,1,2011,10,2,39,12,1,1,5),_H3cSIPSourceIP_Type())
h3cSIPSourceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSIPSourceIP.setStatus(_A)
class _H3cSIPRegisterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('gatewayAll',1),('gatewaySingle',2),('phoneNumber',3)))
_H3cSIPRegisterMode_Type.__name__=_D
_H3cSIPRegisterMode_Object=MibScalar
h3cSIPRegisterMode=_H3cSIPRegisterMode_Object((1,3,6,1,4,1,2011,10,2,39,12,1,1,6),_H3cSIPRegisterMode_Type())
h3cSIPRegisterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSIPRegisterMode.setStatus(_A)
_H3cSIPRegisterPhoneNumber_Type=OctetString
_H3cSIPRegisterPhoneNumber_Object=MibScalar
h3cSIPRegisterPhoneNumber=_H3cSIPRegisterPhoneNumber_Object((1,3,6,1,4,1,2011,10,2,39,12,1,1,7),_H3cSIPRegisterPhoneNumber_Type())
h3cSIPRegisterPhoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSIPRegisterPhoneNumber.setStatus(_A)
class _H3cSIPRegisterEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_H3cSIPRegisterEnable_Type.__name__=_D
_H3cSIPRegisterEnable_Object=MibScalar
h3cSIPRegisterEnable=_H3cSIPRegisterEnable_Object((1,3,6,1,4,1,2011,10,2,39,12,1,1,8),_H3cSIPRegisterEnable_Type())
h3cSIPRegisterEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSIPRegisterEnable.setStatus(_A)
class _H3cSIPTrapsControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_H3cSIPTrapsControl_Type.__name__=_D
_H3cSIPTrapsControl_Object=MibScalar
h3cSIPTrapsControl=_H3cSIPTrapsControl_Object((1,3,6,1,4,1,2011,10,2,39,12,1,1,9),_H3cSIPTrapsControl_Type())
h3cSIPTrapsControl.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSIPTrapsControl.setStatus(_A)
class _H3cSIPStatisticClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_H3cSIPStatisticClear_Type.__name__=_D
_H3cSIPStatisticClear_Object=MibScalar
h3cSIPStatisticClear=_H3cSIPStatisticClear_Object((1,3,6,1,4,1,2011,10,2,39,12,1,1,10),_H3cSIPStatisticClear_Type())
h3cSIPStatisticClear.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSIPStatisticClear.setStatus(_A)
_H3cSIPServerConfigTable_Object=MibTable
h3cSIPServerConfigTable=_H3cSIPServerConfigTable_Object((1,3,6,1,4,1,2011,10,2,39,12,1,2))
if mibBuilder.loadTexts:h3cSIPServerConfigTable.setStatus(_A)
_H3cSIPServerConfigEntry_Object=MibTableRow
h3cSIPServerConfigEntry=_H3cSIPServerConfigEntry_Object((1,3,6,1,4,1,2011,10,2,39,12,1,2,1))
h3cSIPServerConfigEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:h3cSIPServerConfigEntry.setStatus(_A)
_H3cSIPServerIPAddressType_Type=InetAddressType
_H3cSIPServerIPAddressType_Object=MibTableColumn
h3cSIPServerIPAddressType=_H3cSIPServerIPAddressType_Object((1,3,6,1,4,1,2011,10,2,39,12,1,2,1,1),_H3cSIPServerIPAddressType_Type())
h3cSIPServerIPAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSIPServerIPAddressType.setStatus(_A)
_H3cSIPServerIPAddress_Type=InetAddress
_H3cSIPServerIPAddress_Object=MibTableColumn
h3cSIPServerIPAddress=_H3cSIPServerIPAddress_Object((1,3,6,1,4,1,2011,10,2,39,12,1,2,1,2),_H3cSIPServerIPAddress_Type())
h3cSIPServerIPAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSIPServerIPAddress.setStatus(_A)
class _H3cSIPServerPort_Type(Integer32):defaultValue=5060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cSIPServerPort_Type.__name__=_D
_H3cSIPServerPort_Object=MibTableColumn
h3cSIPServerPort=_H3cSIPServerPort_Object((1,3,6,1,4,1,2011,10,2,39,12,1,2,1,3),_H3cSIPServerPort_Type())
h3cSIPServerPort.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSIPServerPort.setStatus(_A)
class _H3cSIPServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slave',2)))
_H3cSIPServerType_Type.__name__=_D
_H3cSIPServerType_Object=MibTableColumn
h3cSIPServerType=_H3cSIPServerType_Object((1,3,6,1,4,1,2011,10,2,39,12,1,2,1,4),_H3cSIPServerType_Type())
h3cSIPServerType.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cSIPServerType.setStatus(_A)
class _H3cSIPAcceptType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inbound',1),('all',2)))
_H3cSIPAcceptType_Type.__name__=_D
_H3cSIPAcceptType_Object=MibTableColumn
h3cSIPAcceptType=_H3cSIPAcceptType_Object((1,3,6,1,4,1,2011,10,2,39,12,1,2,1,5),_H3cSIPAcceptType_Type())
h3cSIPAcceptType.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cSIPAcceptType.setStatus(_A)
_H3cSIPServerStatus_Type=RowStatus
_H3cSIPServerStatus_Object=MibTableColumn
h3cSIPServerStatus=_H3cSIPServerStatus_Object((1,3,6,1,4,1,2011,10,2,39,12,1,2,1,6),_H3cSIPServerStatus_Type())
h3cSIPServerStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cSIPServerStatus.setStatus(_A)
_H3cSIPMsgStatTable_Object=MibTable
h3cSIPMsgStatTable=_H3cSIPMsgStatTable_Object((1,3,6,1,4,1,2011,10,2,39,12,1,3))
if mibBuilder.loadTexts:h3cSIPMsgStatTable.setStatus(_A)
_H3cSIPMsgStatEntry_Object=MibTableRow
h3cSIPMsgStatEntry=_H3cSIPMsgStatEntry_Object((1,3,6,1,4,1,2011,10,2,39,12,1,3,1))
h3cSIPMsgStatEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:h3cSIPMsgStatEntry.setStatus(_A)
_H3cSIPMsgIndex_Type=SipMsgType
_H3cSIPMsgIndex_Object=MibTableColumn
h3cSIPMsgIndex=_H3cSIPMsgIndex_Object((1,3,6,1,4,1,2011,10,2,39,12,1,3,1,1),_H3cSIPMsgIndex_Type())
h3cSIPMsgIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cSIPMsgIndex.setStatus(_A)
_H3cSIPMsgName_Type=OctetString
_H3cSIPMsgName_Object=MibTableColumn
h3cSIPMsgName=_H3cSIPMsgName_Object((1,3,6,1,4,1,2011,10,2,39,12,1,3,1,2),_H3cSIPMsgName_Type())
h3cSIPMsgName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSIPMsgName.setStatus(_A)
_H3cSIPMsgSend_Type=Counter32
_H3cSIPMsgSend_Object=MibTableColumn
h3cSIPMsgSend=_H3cSIPMsgSend_Object((1,3,6,1,4,1,2011,10,2,39,12,1,3,1,3),_H3cSIPMsgSend_Type())
h3cSIPMsgSend.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSIPMsgSend.setStatus(_A)
_H3cSIPMsgOKSend_Type=Counter32
_H3cSIPMsgOKSend_Object=MibTableColumn
h3cSIPMsgOKSend=_H3cSIPMsgOKSend_Object((1,3,6,1,4,1,2011,10,2,39,12,1,3,1,4),_H3cSIPMsgOKSend_Type())
h3cSIPMsgOKSend.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSIPMsgOKSend.setStatus(_A)
_H3cSIPMsgReceive_Type=Counter32
_H3cSIPMsgReceive_Object=MibTableColumn
h3cSIPMsgReceive=_H3cSIPMsgReceive_Object((1,3,6,1,4,1,2011,10,2,39,12,1,3,1,5),_H3cSIPMsgReceive_Type())
h3cSIPMsgReceive.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSIPMsgReceive.setStatus(_A)
_H3cSIPMsgOKReceive_Type=Counter32
_H3cSIPMsgOKReceive_Object=MibTableColumn
h3cSIPMsgOKReceive=_H3cSIPMsgOKReceive_Object((1,3,6,1,4,1,2011,10,2,39,12,1,3,1,6),_H3cSIPMsgOKReceive_Type())
h3cSIPMsgOKReceive.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSIPMsgOKReceive.setStatus(_A)
_H3cSIPMsgResponseStatTable_Object=MibTable
h3cSIPMsgResponseStatTable=_H3cSIPMsgResponseStatTable_Object((1,3,6,1,4,1,2011,10,2,39,12,1,4))
if mibBuilder.loadTexts:h3cSIPMsgResponseStatTable.setStatus(_A)
_H3cSIPMsgResponseStatEntry_Object=MibTableRow
h3cSIPMsgResponseStatEntry=_H3cSIPMsgResponseStatEntry_Object((1,3,6,1,4,1,2011,10,2,39,12,1,4,1))
h3cSIPMsgResponseStatEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:h3cSIPMsgResponseStatEntry.setStatus(_A)
_H3cSIPMsgResponseIndex_Type=Integer32
_H3cSIPMsgResponseIndex_Object=MibTableColumn
h3cSIPMsgResponseIndex=_H3cSIPMsgResponseIndex_Object((1,3,6,1,4,1,2011,10,2,39,12,1,4,1,1),_H3cSIPMsgResponseIndex_Type())
h3cSIPMsgResponseIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cSIPMsgResponseIndex.setStatus(_A)
_H3cSIPMsgResponseCode_Type=OctetString
_H3cSIPMsgResponseCode_Object=MibTableColumn
h3cSIPMsgResponseCode=_H3cSIPMsgResponseCode_Object((1,3,6,1,4,1,2011,10,2,39,12,1,4,1,2),_H3cSIPMsgResponseCode_Type())
h3cSIPMsgResponseCode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSIPMsgResponseCode.setStatus(_A)
_H3cSIPResCodeRecvCount_Type=Counter32
_H3cSIPResCodeRecvCount_Object=MibTableColumn
h3cSIPResCodeRecvCount=_H3cSIPResCodeRecvCount_Object((1,3,6,1,4,1,2011,10,2,39,12,1,4,1,3),_H3cSIPResCodeRecvCount_Type())
h3cSIPResCodeRecvCount.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSIPResCodeRecvCount.setStatus(_A)
_H3cSIPResCodeSendCount_Type=Counter32
_H3cSIPResCodeSendCount_Object=MibTableColumn
h3cSIPResCodeSendCount=_H3cSIPResCodeSendCount_Object((1,3,6,1,4,1,2011,10,2,39,12,1,4,1,4),_H3cSIPResCodeSendCount_Type())
h3cSIPResCodeSendCount.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSIPResCodeSendCount.setStatus(_A)
_H3cSIPTrapStubObjects_ObjectIdentity=ObjectIdentity
h3cSIPTrapStubObjects=_H3cSIPTrapStubObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,39,12,3))
class _H3cSIPRegisterFailReason_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_H3cSIPRegisterFailReason_Type.__name__=_G
_H3cSIPRegisterFailReason_Object=MibScalar
h3cSIPRegisterFailReason=_H3cSIPRegisterFailReason_Object((1,3,6,1,4,1,2011,10,2,39,12,3,1),_H3cSIPRegisterFailReason_Type())
h3cSIPRegisterFailReason.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSIPRegisterFailReason.setStatus(_A)
_H3cSIPAuthenReqMethod_Type=SipMsgType
_H3cSIPAuthenReqMethod_Object=MibScalar
h3cSIPAuthenReqMethod=_H3cSIPAuthenReqMethod_Object((1,3,6,1,4,1,2011,10,2,39,12,3,2),_H3cSIPAuthenReqMethod_Type())
h3cSIPAuthenReqMethod.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cSIPAuthenReqMethod.setStatus(_A)
_H3cSIPClientNotifications_ObjectIdentity=ObjectIdentity
h3cSIPClientNotifications=_H3cSIPClientNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,39,12,4))
h3cSIPRegisterFailure=NotificationType((1,3,6,1,4,1,2011,10,2,39,12,4,1))
h3cSIPRegisterFailure.setObjects(*((_B,_L),(_B,_H),(_B,_I),(_B,_J),(_B,_P)))
if mibBuilder.loadTexts:h3cSIPRegisterFailure.setStatus(_A)
h3cSIPAuthenticateFailure=NotificationType((1,3,6,1,4,1,2011,10,2,39,12,4,2))
h3cSIPAuthenticateFailure.setObjects(*((_B,_L),(_B,_Q)))
if mibBuilder.loadTexts:h3cSIPAuthenticateFailure.setStatus(_A)
h3cSIPServerSwitch=NotificationType((1,3,6,1,4,1,2011,10,2,39,12,4,3))
if mibBuilder.loadTexts:h3cSIPServerSwitch.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SipMsgType':SipMsgType,'h3cVoSIP':h3cVoSIP,'h3cSIPClientMIB':h3cSIPClientMIB,'h3cSIPClientConfigObjects':h3cSIPClientConfigObjects,_L:h3cSIPID,'h3cSIPPasswordType':h3cSIPPasswordType,'h3cSIPPassword':h3cSIPPassword,'h3cSIPSourceIPAddressType':h3cSIPSourceIPAddressType,'h3cSIPSourceIP':h3cSIPSourceIP,'h3cSIPRegisterMode':h3cSIPRegisterMode,'h3cSIPRegisterPhoneNumber':h3cSIPRegisterPhoneNumber,'h3cSIPRegisterEnable':h3cSIPRegisterEnable,'h3cSIPTrapsControl':h3cSIPTrapsControl,'h3cSIPStatisticClear':h3cSIPStatisticClear,'h3cSIPServerConfigTable':h3cSIPServerConfigTable,'h3cSIPServerConfigEntry':h3cSIPServerConfigEntry,_H:h3cSIPServerIPAddressType,_I:h3cSIPServerIPAddress,_J:h3cSIPServerPort,'h3cSIPServerType':h3cSIPServerType,'h3cSIPAcceptType':h3cSIPAcceptType,'h3cSIPServerStatus':h3cSIPServerStatus,'h3cSIPMsgStatTable':h3cSIPMsgStatTable,'h3cSIPMsgStatEntry':h3cSIPMsgStatEntry,_M:h3cSIPMsgIndex,'h3cSIPMsgName':h3cSIPMsgName,'h3cSIPMsgSend':h3cSIPMsgSend,'h3cSIPMsgOKSend':h3cSIPMsgOKSend,'h3cSIPMsgReceive':h3cSIPMsgReceive,'h3cSIPMsgOKReceive':h3cSIPMsgOKReceive,'h3cSIPMsgResponseStatTable':h3cSIPMsgResponseStatTable,'h3cSIPMsgResponseStatEntry':h3cSIPMsgResponseStatEntry,_O:h3cSIPMsgResponseIndex,'h3cSIPMsgResponseCode':h3cSIPMsgResponseCode,'h3cSIPResCodeRecvCount':h3cSIPResCodeRecvCount,'h3cSIPResCodeSendCount':h3cSIPResCodeSendCount,'h3cSIPTrapStubObjects':h3cSIPTrapStubObjects,_P:h3cSIPRegisterFailReason,_Q:h3cSIPAuthenReqMethod,'h3cSIPClientNotifications':h3cSIPClientNotifications,'h3cSIPRegisterFailure':h3cSIPRegisterFailure,'h3cSIPAuthenticateFailure':h3cSIPAuthenticateFailure,'h3cSIPServerSwitch':h3cSIPServerSwitch})