_h='ogdataEventState'
_g='ogdataEventDevice'
_f='ogdataEventSeconds'
_e='ogdataEventBytes'
_d='ognupsEventType'
_c='ognupsEventName'
_b='ogfovrEventSecondary'
_a='ogfovrEventPrimary'
_Z='oghostEventPort'
_Y='oghostEventProtocol'
_X='oghostEventDescription'
_W='oghostEventAddress'
_V='oghostEventType'
_U='oghostEventUsername'
_T='ogsensStatusValue'
_S='ogsensStatusType'
_R='ogsensStatusDevType'
_Q='ogsensStatusName'
_P='ogpatnEventPortLabel'
_O='ogpatnEventPortNumber'
_N='ogpatnEventText'
_M='ogpatnEventDescription'
_L='ogsgnlEventPortLabel'
_K='ogsgnlEventPortNumber'
_J='ogsgnlEventState'
_I='ogsgnlEventType'
_H='ogconnEventPortLabel'
_G='ogconnEventPortNumber'
_F='ogconnEventType'
_E='ogconnEventUsername'
_D='NotificationType'
_C='mandatory'
_B='read-only'
_A='OGTRAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_D,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_D,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Opengear_ObjectIdentity=ObjectIdentity
opengear=_Opengear_ObjectIdentity((1,3,6,1,4,1,25049))
_OgLegacyMgmt_ObjectIdentity=ObjectIdentity
ogLegacyMgmt=_OgLegacyMgmt_ObjectIdentity((1,3,6,1,4,1,25049,2))
_OgConnectMib_ObjectIdentity=ObjectIdentity
ogConnectMib=_OgConnectMib_ObjectIdentity((1,3,6,1,4,1,25049,2,10))
_OgConnectMibObjects_ObjectIdentity=ObjectIdentity
ogConnectMibObjects=_OgConnectMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,2,10,10))
_OgconnEvent_ObjectIdentity=ObjectIdentity
ogconnEvent=_OgconnEvent_ObjectIdentity((1,3,6,1,4,1,25049,2,10,10,1))
_OgconnEventTable_ObjectIdentity=ObjectIdentity
ogconnEventTable=_OgconnEventTable_ObjectIdentity((1,3,6,1,4,1,25049,2,10,10,1,1))
_OgconnEventEntry_ObjectIdentity=ObjectIdentity
ogconnEventEntry=_OgconnEventEntry_ObjectIdentity((1,3,6,1,4,1,25049,2,10,10,1,1,1))
_OgconnEventUsername_Type=OctetString
_OgconnEventUsername_Object=MibScalar
ogconnEventUsername=_OgconnEventUsername_Object((1,3,6,1,4,1,25049,2,10,10,1,1,1,10),_OgconnEventUsername_Type())
ogconnEventUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:ogconnEventUsername.setStatus(_C)
_OgconnEventType_Type=OctetString
_OgconnEventType_Object=MibScalar
ogconnEventType=_OgconnEventType_Object((1,3,6,1,4,1,25049,2,10,10,1,1,1,11),_OgconnEventType_Type())
ogconnEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:ogconnEventType.setStatus(_C)
_OgconnEventPortNumber_Type=Integer32
_OgconnEventPortNumber_Object=MibScalar
ogconnEventPortNumber=_OgconnEventPortNumber_Object((1,3,6,1,4,1,25049,2,10,10,1,1,1,12),_OgconnEventPortNumber_Type())
ogconnEventPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ogconnEventPortNumber.setStatus(_C)
_OgconnEventPortLabel_Type=OctetString
_OgconnEventPortLabel_Object=MibScalar
ogconnEventPortLabel=_OgconnEventPortLabel_Object((1,3,6,1,4,1,25049,2,10,10,1,1,1,13),_OgconnEventPortLabel_Type())
ogconnEventPortLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:ogconnEventPortLabel.setStatus(_C)
_OgSignalMib_ObjectIdentity=ObjectIdentity
ogSignalMib=_OgSignalMib_ObjectIdentity((1,3,6,1,4,1,25049,2,11))
_OgSignalMibObjects_ObjectIdentity=ObjectIdentity
ogSignalMibObjects=_OgSignalMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,2,11,10))
_OgsgnlEvent_ObjectIdentity=ObjectIdentity
ogsgnlEvent=_OgsgnlEvent_ObjectIdentity((1,3,6,1,4,1,25049,2,11,10,1))
_OgsgnlEventTable_ObjectIdentity=ObjectIdentity
ogsgnlEventTable=_OgsgnlEventTable_ObjectIdentity((1,3,6,1,4,1,25049,2,11,10,1,1))
_OgsgnlEventEntry_ObjectIdentity=ObjectIdentity
ogsgnlEventEntry=_OgsgnlEventEntry_ObjectIdentity((1,3,6,1,4,1,25049,2,11,10,1,1,1))
_OgsgnlEventType_Type=OctetString
_OgsgnlEventType_Object=MibScalar
ogsgnlEventType=_OgsgnlEventType_Object((1,3,6,1,4,1,25049,2,11,10,1,1,1,10),_OgsgnlEventType_Type())
ogsgnlEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:ogsgnlEventType.setStatus(_C)
_OgsgnlEventState_Type=OctetString
_OgsgnlEventState_Object=MibScalar
ogsgnlEventState=_OgsgnlEventState_Object((1,3,6,1,4,1,25049,2,11,10,1,1,1,11),_OgsgnlEventState_Type())
ogsgnlEventState.setMaxAccess(_B)
if mibBuilder.loadTexts:ogsgnlEventState.setStatus(_C)
_OgsgnlEventPortNumber_Type=Integer32
_OgsgnlEventPortNumber_Object=MibScalar
ogsgnlEventPortNumber=_OgsgnlEventPortNumber_Object((1,3,6,1,4,1,25049,2,11,10,1,1,1,12),_OgsgnlEventPortNumber_Type())
ogsgnlEventPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ogsgnlEventPortNumber.setStatus(_C)
_OgsgnlEventPortLabel_Type=OctetString
_OgsgnlEventPortLabel_Object=MibScalar
ogsgnlEventPortLabel=_OgsgnlEventPortLabel_Object((1,3,6,1,4,1,25049,2,11,10,1,1,1,13),_OgsgnlEventPortLabel_Type())
ogsgnlEventPortLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:ogsgnlEventPortLabel.setStatus(_C)
_OgPatternMib_ObjectIdentity=ObjectIdentity
ogPatternMib=_OgPatternMib_ObjectIdentity((1,3,6,1,4,1,25049,2,12))
_OgPatternMibObjects_ObjectIdentity=ObjectIdentity
ogPatternMibObjects=_OgPatternMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,2,12,10))
_OgpatnEvent_ObjectIdentity=ObjectIdentity
ogpatnEvent=_OgpatnEvent_ObjectIdentity((1,3,6,1,4,1,25049,2,12,10,1))
_OgpatnEventTable_ObjectIdentity=ObjectIdentity
ogpatnEventTable=_OgpatnEventTable_ObjectIdentity((1,3,6,1,4,1,25049,2,12,10,1,1))
_OgpatnEventEntry_ObjectIdentity=ObjectIdentity
ogpatnEventEntry=_OgpatnEventEntry_ObjectIdentity((1,3,6,1,4,1,25049,2,12,10,1,1,1))
_OgpatnEventDescription_Type=OctetString
_OgpatnEventDescription_Object=MibScalar
ogpatnEventDescription=_OgpatnEventDescription_Object((1,3,6,1,4,1,25049,2,12,10,1,1,1,10),_OgpatnEventDescription_Type())
ogpatnEventDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:ogpatnEventDescription.setStatus(_C)
_OgpatnEventText_Type=OctetString
_OgpatnEventText_Object=MibScalar
ogpatnEventText=_OgpatnEventText_Object((1,3,6,1,4,1,25049,2,12,10,1,1,1,11),_OgpatnEventText_Type())
ogpatnEventText.setMaxAccess(_B)
if mibBuilder.loadTexts:ogpatnEventText.setStatus(_C)
_OgpatnEventPortNumber_Type=Integer32
_OgpatnEventPortNumber_Object=MibScalar
ogpatnEventPortNumber=_OgpatnEventPortNumber_Object((1,3,6,1,4,1,25049,2,12,10,1,1,1,12),_OgpatnEventPortNumber_Type())
ogpatnEventPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ogpatnEventPortNumber.setStatus(_C)
_OgpatnEventPortLabel_Type=OctetString
_OgpatnEventPortLabel_Object=MibScalar
ogpatnEventPortLabel=_OgpatnEventPortLabel_Object((1,3,6,1,4,1,25049,2,12,10,1,1,1,13),_OgpatnEventPortLabel_Type())
ogpatnEventPortLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:ogpatnEventPortLabel.setStatus(_C)
_OgSensorMib_ObjectIdentity=ObjectIdentity
ogSensorMib=_OgSensorMib_ObjectIdentity((1,3,6,1,4,1,25049,2,13))
_OgSensorMibObjects_ObjectIdentity=ObjectIdentity
ogSensorMibObjects=_OgSensorMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,2,13,10))
_OgsensStatus_ObjectIdentity=ObjectIdentity
ogsensStatus=_OgsensStatus_ObjectIdentity((1,3,6,1,4,1,25049,2,13,10,1))
_OgsensStatusTable_ObjectIdentity=ObjectIdentity
ogsensStatusTable=_OgsensStatusTable_ObjectIdentity((1,3,6,1,4,1,25049,2,13,10,1,1))
_OgsensStatusEntry_ObjectIdentity=ObjectIdentity
ogsensStatusEntry=_OgsensStatusEntry_ObjectIdentity((1,3,6,1,4,1,25049,2,13,10,1,1,1))
_OgsensStatusName_Type=OctetString
_OgsensStatusName_Object=MibScalar
ogsensStatusName=_OgsensStatusName_Object((1,3,6,1,4,1,25049,2,13,10,1,1,1,10),_OgsensStatusName_Type())
ogsensStatusName.setMaxAccess(_B)
if mibBuilder.loadTexts:ogsensStatusName.setStatus(_C)
_OgsensStatusDevType_Type=OctetString
_OgsensStatusDevType_Object=MibScalar
ogsensStatusDevType=_OgsensStatusDevType_Object((1,3,6,1,4,1,25049,2,13,10,1,1,1,11),_OgsensStatusDevType_Type())
ogsensStatusDevType.setMaxAccess(_B)
if mibBuilder.loadTexts:ogsensStatusDevType.setStatus(_C)
_OgsensStatusType_Type=OctetString
_OgsensStatusType_Object=MibScalar
ogsensStatusType=_OgsensStatusType_Object((1,3,6,1,4,1,25049,2,13,10,1,1,1,12),_OgsensStatusType_Type())
ogsensStatusType.setMaxAccess(_B)
if mibBuilder.loadTexts:ogsensStatusType.setStatus(_C)
_OgsensStatusValue_Type=Integer32
_OgsensStatusValue_Object=MibScalar
ogsensStatusValue=_OgsensStatusValue_Object((1,3,6,1,4,1,25049,2,13,10,1,1,1,13),_OgsensStatusValue_Type())
ogsensStatusValue.setMaxAccess(_B)
if mibBuilder.loadTexts:ogsensStatusValue.setStatus(_C)
_OgHostMib_ObjectIdentity=ObjectIdentity
ogHostMib=_OgHostMib_ObjectIdentity((1,3,6,1,4,1,25049,2,14))
_OgHostMibObjects_ObjectIdentity=ObjectIdentity
ogHostMibObjects=_OgHostMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,2,14,10))
_OghostEvent_ObjectIdentity=ObjectIdentity
oghostEvent=_OghostEvent_ObjectIdentity((1,3,6,1,4,1,25049,2,14,10,1))
_OghostEventTable_ObjectIdentity=ObjectIdentity
oghostEventTable=_OghostEventTable_ObjectIdentity((1,3,6,1,4,1,25049,2,14,10,1,1))
_OghostEventEntry_ObjectIdentity=ObjectIdentity
oghostEventEntry=_OghostEventEntry_ObjectIdentity((1,3,6,1,4,1,25049,2,14,10,1,1,1))
_OghostEventUsername_Type=OctetString
_OghostEventUsername_Object=MibScalar
oghostEventUsername=_OghostEventUsername_Object((1,3,6,1,4,1,25049,2,14,10,1,1,1,10),_OghostEventUsername_Type())
oghostEventUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:oghostEventUsername.setStatus(_C)
_OghostEventType_Type=OctetString
_OghostEventType_Object=MibScalar
oghostEventType=_OghostEventType_Object((1,3,6,1,4,1,25049,2,14,10,1,1,1,11),_OghostEventType_Type())
oghostEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:oghostEventType.setStatus(_C)
_OghostEventAddress_Type=OctetString
_OghostEventAddress_Object=MibScalar
oghostEventAddress=_OghostEventAddress_Object((1,3,6,1,4,1,25049,2,14,10,1,1,1,12),_OghostEventAddress_Type())
oghostEventAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oghostEventAddress.setStatus(_C)
_OghostEventDescription_Type=OctetString
_OghostEventDescription_Object=MibScalar
oghostEventDescription=_OghostEventDescription_Object((1,3,6,1,4,1,25049,2,14,10,1,1,1,13),_OghostEventDescription_Type())
oghostEventDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:oghostEventDescription.setStatus(_C)
_OghostEventProtocol_Type=OctetString
_OghostEventProtocol_Object=MibScalar
oghostEventProtocol=_OghostEventProtocol_Object((1,3,6,1,4,1,25049,2,14,10,1,1,1,14),_OghostEventProtocol_Type())
oghostEventProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:oghostEventProtocol.setStatus(_C)
_OghostEventPort_Type=Integer32
_OghostEventPort_Object=MibScalar
oghostEventPort=_OghostEventPort_Object((1,3,6,1,4,1,25049,2,14,10,1,1,1,15),_OghostEventPort_Type())
oghostEventPort.setMaxAccess(_B)
if mibBuilder.loadTexts:oghostEventPort.setStatus(_C)
_OgFailoverMib_ObjectIdentity=ObjectIdentity
ogFailoverMib=_OgFailoverMib_ObjectIdentity((1,3,6,1,4,1,25049,2,15))
_OgFailoverMibObjects_ObjectIdentity=ObjectIdentity
ogFailoverMibObjects=_OgFailoverMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,2,15,10))
_OgfovrEvent_ObjectIdentity=ObjectIdentity
ogfovrEvent=_OgfovrEvent_ObjectIdentity((1,3,6,1,4,1,25049,2,15,10,1))
_OgfovrEventTable_ObjectIdentity=ObjectIdentity
ogfovrEventTable=_OgfovrEventTable_ObjectIdentity((1,3,6,1,4,1,25049,2,15,10,1,1))
_OgfovrEventEntry_ObjectIdentity=ObjectIdentity
ogfovrEventEntry=_OgfovrEventEntry_ObjectIdentity((1,3,6,1,4,1,25049,2,15,10,1,1,1))
_OgfovrEventPrimary_Type=OctetString
_OgfovrEventPrimary_Object=MibScalar
ogfovrEventPrimary=_OgfovrEventPrimary_Object((1,3,6,1,4,1,25049,2,15,10,1,1,1,10),_OgfovrEventPrimary_Type())
ogfovrEventPrimary.setMaxAccess(_B)
if mibBuilder.loadTexts:ogfovrEventPrimary.setStatus(_C)
_OgfovrEventSecondary_Type=OctetString
_OgfovrEventSecondary_Object=MibScalar
ogfovrEventSecondary=_OgfovrEventSecondary_Object((1,3,6,1,4,1,25049,2,15,10,1,1,1,11),_OgfovrEventSecondary_Type())
ogfovrEventSecondary.setMaxAccess(_B)
if mibBuilder.loadTexts:ogfovrEventSecondary.setStatus(_C)
_OgNetUpsMib_ObjectIdentity=ObjectIdentity
ogNetUpsMib=_OgNetUpsMib_ObjectIdentity((1,3,6,1,4,1,25049,2,16))
_OgNetUpsMibObjects_ObjectIdentity=ObjectIdentity
ogNetUpsMibObjects=_OgNetUpsMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,2,16,10))
_OgnupsEvent_ObjectIdentity=ObjectIdentity
ognupsEvent=_OgnupsEvent_ObjectIdentity((1,3,6,1,4,1,25049,2,16,10,1))
_OgnupsEventTable_ObjectIdentity=ObjectIdentity
ognupsEventTable=_OgnupsEventTable_ObjectIdentity((1,3,6,1,4,1,25049,2,16,10,1,1))
_OgnupsEventEntry_ObjectIdentity=ObjectIdentity
ognupsEventEntry=_OgnupsEventEntry_ObjectIdentity((1,3,6,1,4,1,25049,2,16,10,1,1,1))
_OgnupsEventName_Type=OctetString
_OgnupsEventName_Object=MibScalar
ognupsEventName=_OgnupsEventName_Object((1,3,6,1,4,1,25049,2,16,10,1,1,1,10),_OgnupsEventName_Type())
ognupsEventName.setMaxAccess(_B)
if mibBuilder.loadTexts:ognupsEventName.setStatus(_C)
_OgnupsEventType_Type=OctetString
_OgnupsEventType_Object=MibScalar
ognupsEventType=_OgnupsEventType_Object((1,3,6,1,4,1,25049,2,16,10,1,1,1,11),_OgnupsEventType_Type())
ognupsEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:ognupsEventType.setStatus(_C)
_OgDataMib_ObjectIdentity=ObjectIdentity
ogDataMib=_OgDataMib_ObjectIdentity((1,3,6,1,4,1,25049,2,17))
_OgDataMibObjects_ObjectIdentity=ObjectIdentity
ogDataMibObjects=_OgDataMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,2,17,10))
_OgdataEvent_ObjectIdentity=ObjectIdentity
ogdataEvent=_OgdataEvent_ObjectIdentity((1,3,6,1,4,1,25049,2,17,10,1))
_OgdataEventTable_ObjectIdentity=ObjectIdentity
ogdataEventTable=_OgdataEventTable_ObjectIdentity((1,3,6,1,4,1,25049,2,17,10,1,1))
_OgdataEventEntry_ObjectIdentity=ObjectIdentity
ogdataEventEntry=_OgdataEventEntry_ObjectIdentity((1,3,6,1,4,1,25049,2,17,10,1,1,1))
_OgdataEventBytes_Type=Integer32
_OgdataEventBytes_Object=MibScalar
ogdataEventBytes=_OgdataEventBytes_Object((1,3,6,1,4,1,25049,2,17,10,1,1,1,10),_OgdataEventBytes_Type())
ogdataEventBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ogdataEventBytes.setStatus(_C)
_OgdataEventSeconds_Type=Integer32
_OgdataEventSeconds_Object=MibScalar
ogdataEventSeconds=_OgdataEventSeconds_Object((1,3,6,1,4,1,25049,2,17,10,1,1,1,11),_OgdataEventSeconds_Type())
ogdataEventSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:ogdataEventSeconds.setStatus(_C)
_OgdataEventDevice_Type=OctetString
_OgdataEventDevice_Object=MibScalar
ogdataEventDevice=_OgdataEventDevice_Object((1,3,6,1,4,1,25049,2,17,10,1,1,1,12),_OgdataEventDevice_Type())
ogdataEventDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:ogdataEventDevice.setStatus(_C)
_OgdataEventState_Type=Integer32
_OgdataEventState_Object=MibScalar
ogdataEventState=_OgdataEventState_Object((1,3,6,1,4,1,25049,2,17,10,1,1,1,13),_OgdataEventState_Type())
ogdataEventState.setMaxAccess(_B)
if mibBuilder.loadTexts:ogdataEventState.setStatus(_C)
ogconnEventOccurred=NotificationType((1,3,6,1,4,1,25049,0,1001))
ogconnEventOccurred.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ogconnEventOccurred.setStatus('')
ogsgnlEventOccurred=NotificationType((1,3,6,1,4,1,25049,0,1002))
ogsgnlEventOccurred.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ogsgnlEventOccurred.setStatus('')
ogpatnEventOccurred=NotificationType((1,3,6,1,4,1,25049,0,1003))
ogpatnEventOccurred.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ogpatnEventOccurred.setStatus('')
ogsensStatusOccurred=NotificationType((1,3,6,1,4,1,25049,0,1004))
ogsensStatusOccurred.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ogsensStatusOccurred.setStatus('')
oghostEventOccurred=NotificationType((1,3,6,1,4,1,25049,0,2001))
oghostEventOccurred.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:oghostEventOccurred.setStatus('')
ogfovrEventOccurred=NotificationType((1,3,6,1,4,1,25049,0,2002))
ogfovrEventOccurred.setObjects(*((_A,_a),(_A,_b)))
if mibBuilder.loadTexts:ogfovrEventOccurred.setStatus('')
ognupsEventOccurred=NotificationType((1,3,6,1,4,1,25049,0,2003))
ognupsEventOccurred.setObjects(*((_A,_c),(_A,_d)))
if mibBuilder.loadTexts:ognupsEventOccurred.setStatus('')
ogdataEventOccurred=NotificationType((1,3,6,1,4,1,25049,0,2004))
ogdataEventOccurred.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:ogdataEventOccurred.setStatus('')
mibBuilder.exportSymbols(_A,**{'opengear':opengear,'ogconnEventOccurred':ogconnEventOccurred,'ogsgnlEventOccurred':ogsgnlEventOccurred,'ogpatnEventOccurred':ogpatnEventOccurred,'ogsensStatusOccurred':ogsensStatusOccurred,'oghostEventOccurred':oghostEventOccurred,'ogfovrEventOccurred':ogfovrEventOccurred,'ognupsEventOccurred':ognupsEventOccurred,'ogdataEventOccurred':ogdataEventOccurred,'ogLegacyMgmt':ogLegacyMgmt,'ogConnectMib':ogConnectMib,'ogConnectMibObjects':ogConnectMibObjects,'ogconnEvent':ogconnEvent,'ogconnEventTable':ogconnEventTable,'ogconnEventEntry':ogconnEventEntry,_E:ogconnEventUsername,_F:ogconnEventType,_G:ogconnEventPortNumber,_H:ogconnEventPortLabel,'ogSignalMib':ogSignalMib,'ogSignalMibObjects':ogSignalMibObjects,'ogsgnlEvent':ogsgnlEvent,'ogsgnlEventTable':ogsgnlEventTable,'ogsgnlEventEntry':ogsgnlEventEntry,_I:ogsgnlEventType,_J:ogsgnlEventState,_K:ogsgnlEventPortNumber,_L:ogsgnlEventPortLabel,'ogPatternMib':ogPatternMib,'ogPatternMibObjects':ogPatternMibObjects,'ogpatnEvent':ogpatnEvent,'ogpatnEventTable':ogpatnEventTable,'ogpatnEventEntry':ogpatnEventEntry,_M:ogpatnEventDescription,_N:ogpatnEventText,_O:ogpatnEventPortNumber,_P:ogpatnEventPortLabel,'ogSensorMib':ogSensorMib,'ogSensorMibObjects':ogSensorMibObjects,'ogsensStatus':ogsensStatus,'ogsensStatusTable':ogsensStatusTable,'ogsensStatusEntry':ogsensStatusEntry,_Q:ogsensStatusName,_R:ogsensStatusDevType,_S:ogsensStatusType,_T:ogsensStatusValue,'ogHostMib':ogHostMib,'ogHostMibObjects':ogHostMibObjects,'oghostEvent':oghostEvent,'oghostEventTable':oghostEventTable,'oghostEventEntry':oghostEventEntry,_U:oghostEventUsername,_V:oghostEventType,_W:oghostEventAddress,_X:oghostEventDescription,_Y:oghostEventProtocol,_Z:oghostEventPort,'ogFailoverMib':ogFailoverMib,'ogFailoverMibObjects':ogFailoverMibObjects,'ogfovrEvent':ogfovrEvent,'ogfovrEventTable':ogfovrEventTable,'ogfovrEventEntry':ogfovrEventEntry,_a:ogfovrEventPrimary,_b:ogfovrEventSecondary,'ogNetUpsMib':ogNetUpsMib,'ogNetUpsMibObjects':ogNetUpsMibObjects,'ognupsEvent':ognupsEvent,'ognupsEventTable':ognupsEventTable,'ognupsEventEntry':ognupsEventEntry,_c:ognupsEventName,_d:ognupsEventType,'ogDataMib':ogDataMib,'ogDataMibObjects':ogDataMibObjects,'ogdataEvent':ogdataEvent,'ogdataEventTable':ogdataEventTable,'ogdataEventEntry':ogdataEventEntry,_e:ogdataEventBytes,_f:ogdataEventSeconds,_g:ogdataEventDevice,_h:ogdataEventState})