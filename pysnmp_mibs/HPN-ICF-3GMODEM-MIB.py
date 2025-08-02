_l='hpnicfSmsContentBind'
_k='hpnicfSmsEncodeBind'
_j='hpnicfSmsTimeBind'
_i='hpnicfSmsSrcNumberBind'
_h='hpnicfSmsSendStatus'
_g='hpnicfAccessMedia'
_f='hpnicfUIMPin'
_e='hpnicfUIMOldPin'
_d='hpnicfUIMIndex'
_c='not-accessible'
_b='hpnicfWirelessCardOnlineTime'
_a='HpnicfSmsEncodeType'
_Z='tdscdma'
_Y='home'
_X='roaming'
_W='lowPower'
_V='emergency'
_U='available'
_T='Unsigned32'
_S='OctetString'
_R='hpnicf3GImsiBind'
_Q='hpnicf3GCurrentRssiBind'
_P='hpnicf3GCurrentService'
_O='noService'
_N='hpnicfUIMImsi'
_M='hpnicfWirelessCardSerialNumber'
_L='hpnicfDevSerialNumber'
_K='hpnicfDeviceOUI'
_J='accessible-for-notify'
_I='dBm'
_H='read-write'
_G='hpnicfWirelessCardIndex'
_F='unknown'
_E='SnmpAdminString'
_D='Integer32'
_C='read-only'
_B='HPN-ICF-3GMODEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_T,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpnicf3GModem=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,98))
if mibBuilder.loadTexts:hpnicf3GModem.setRevisions(('2009-04-30 12:00',))
class HpnicfUIMStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('absent',1),('initial',2),('fault',3),('unprotected',4),('protected',5),('pinLocked',6),('pukLocked',7),('selfDestruct',8)))
class HpnicfSmsEncodeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ascii',1),('ucs2',2)))
_Hpnicf3GModemObjects_ObjectIdentity=ObjectIdentity
hpnicf3GModemObjects=_Hpnicf3GModemObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,98,1))
_HpnicfWirelessCard_ObjectIdentity=ObjectIdentity
hpnicfWirelessCard=_HpnicfWirelessCard_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1))
_HpnicfWirelessCardTable_Object=MibTable
hpnicfWirelessCardTable=_HpnicfWirelessCardTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1))
if mibBuilder.loadTexts:hpnicfWirelessCardTable.setStatus(_A)
_HpnicfWirelessCardEntry_Object=MibTableRow
hpnicfWirelessCardEntry=_HpnicfWirelessCardEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1))
hpnicfWirelessCardEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpnicfWirelessCardEntry.setStatus(_A)
class _HpnicfWirelessCardIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfWirelessCardIndex_Type.__name__=_D
_HpnicfWirelessCardIndex_Object=MibTableColumn
hpnicfWirelessCardIndex=_HpnicfWirelessCardIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1,1),_HpnicfWirelessCardIndex_Type())
hpnicfWirelessCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardIndex.setStatus(_A)
class _HpnicfWirelessCardModelName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfWirelessCardModelName_Type.__name__=_E
_HpnicfWirelessCardModelName_Object=MibTableColumn
hpnicfWirelessCardModelName=_HpnicfWirelessCardModelName_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1,2),_HpnicfWirelessCardModelName_Type())
hpnicfWirelessCardModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardModelName.setStatus(_A)
class _HpnicfWirelessCardMfgName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfWirelessCardMfgName_Type.__name__=_E
_HpnicfWirelessCardMfgName_Object=MibTableColumn
hpnicfWirelessCardMfgName=_HpnicfWirelessCardMfgName_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1,3),_HpnicfWirelessCardMfgName_Type())
hpnicfWirelessCardMfgName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardMfgName.setStatus(_A)
class _HpnicfWirelessCardDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfWirelessCardDescription_Type.__name__=_E
_HpnicfWirelessCardDescription_Object=MibTableColumn
hpnicfWirelessCardDescription=_HpnicfWirelessCardDescription_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1,4),_HpnicfWirelessCardDescription_Type())
hpnicfWirelessCardDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardDescription.setStatus(_A)
class _HpnicfWirelessCardSerialNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfWirelessCardSerialNumber_Type.__name__=_E
_HpnicfWirelessCardSerialNumber_Object=MibTableColumn
hpnicfWirelessCardSerialNumber=_HpnicfWirelessCardSerialNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1,5),_HpnicfWirelessCardSerialNumber_Type())
hpnicfWirelessCardSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardSerialNumber.setStatus(_A)
class _HpnicfWirelessCardCMIIID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfWirelessCardCMIIID_Type.__name__=_E
_HpnicfWirelessCardCMIIID_Object=MibTableColumn
hpnicfWirelessCardCMIIID=_HpnicfWirelessCardCMIIID_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1,6),_HpnicfWirelessCardCMIIID_Type())
hpnicfWirelessCardCMIIID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardCMIIID.setStatus(_A)
class _HpnicfWirelessCardHardwareVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfWirelessCardHardwareVersion_Type.__name__=_E
_HpnicfWirelessCardHardwareVersion_Object=MibTableColumn
hpnicfWirelessCardHardwareVersion=_HpnicfWirelessCardHardwareVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1,7),_HpnicfWirelessCardHardwareVersion_Type())
hpnicfWirelessCardHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardHardwareVersion.setStatus(_A)
class _HpnicfWirelessCardFirmwareVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfWirelessCardFirmwareVersion_Type.__name__=_E
_HpnicfWirelessCardFirmwareVersion_Object=MibTableColumn
hpnicfWirelessCardFirmwareVersion=_HpnicfWirelessCardFirmwareVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1,8),_HpnicfWirelessCardFirmwareVersion_Type())
hpnicfWirelessCardFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardFirmwareVersion.setStatus(_A)
class _HpnicfWirelessCardPRLVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfWirelessCardPRLVersion_Type.__name__=_E
_HpnicfWirelessCardPRLVersion_Object=MibTableColumn
hpnicfWirelessCardPRLVersion=_HpnicfWirelessCardPRLVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1,9),_HpnicfWirelessCardPRLVersion_Type())
hpnicfWirelessCardPRLVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardPRLVersion.setStatus(_A)
_HpnicfWirelessCardInterfaceIndex_Type=InterfaceIndex
_HpnicfWirelessCardInterfaceIndex_Object=MibTableColumn
hpnicfWirelessCardInterfaceIndex=_HpnicfWirelessCardInterfaceIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1,10),_HpnicfWirelessCardInterfaceIndex_Type())
hpnicfWirelessCardInterfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardInterfaceIndex.setStatus(_A)
class _HpnicfWirelessCardModemStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('onLine',2),('offLine',3)))
_HpnicfWirelessCardModemStatus_Type.__name__=_D
_HpnicfWirelessCardModemStatus_Object=MibTableColumn
hpnicfWirelessCardModemStatus=_HpnicfWirelessCardModemStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1,11),_HpnicfWirelessCardModemStatus_Type())
hpnicfWirelessCardModemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardModemStatus.setStatus(_A)
class _HpnicfWirelessCardModemMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_Z,2),('wcdma',3),('cdma',4)))
_HpnicfWirelessCardModemMode_Type.__name__=_D
_HpnicfWirelessCardModemMode_Object=MibTableColumn
hpnicfWirelessCardModemMode=_HpnicfWirelessCardModemMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1,12),_HpnicfWirelessCardModemMode_Type())
hpnicfWirelessCardModemMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardModemMode.setStatus(_A)
class _HpnicfWirelessCardCurNetConn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_F,1),(_O,2),('gsm',3),('gprs',4),('edge',5),('hsdpa',6),('hsupa',7),('hsupaAndhsdpa',8),('hspaPlus',9),('umts',10),('dchspaPlus',11),('lte',12),('onexrtt',13),('evdo',14),('onexrttAndevdo',15),(_Z,16)))
_HpnicfWirelessCardCurNetConn_Type.__name__=_D
_HpnicfWirelessCardCurNetConn_Object=MibTableColumn
hpnicfWirelessCardCurNetConn=_HpnicfWirelessCardCurNetConn_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,1,1,13),_HpnicfWirelessCardCurNetConn_Type())
hpnicfWirelessCardCurNetConn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardCurNetConn.setStatus(_A)
_HpnicfSmsGroup_ObjectIdentity=ObjectIdentity
hpnicfSmsGroup=_HpnicfSmsGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,2))
_HpnicfSmsScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfSmsScalarObjects=_HpnicfSmsScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,2,1))
_HpnicfSmsRxNotifSwitch_Type=TruthValue
_HpnicfSmsRxNotifSwitch_Object=MibScalar
hpnicfSmsRxNotifSwitch=_HpnicfSmsRxNotifSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,2,1,1),_HpnicfSmsRxNotifSwitch_Type())
hpnicfSmsRxNotifSwitch.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSmsRxNotifSwitch.setStatus(_A)
_HpnicfSmsOperationTable_Object=MibTable
hpnicfSmsOperationTable=_HpnicfSmsOperationTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,2,2))
if mibBuilder.loadTexts:hpnicfSmsOperationTable.setStatus(_A)
_HpnicfSmsOperationEntry_Object=MibTableRow
hpnicfSmsOperationEntry=_HpnicfSmsOperationEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,2,2,1))
hpnicfSmsOperationEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpnicfSmsOperationEntry.setStatus(_A)
class _HpnicfSmsDestNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_HpnicfSmsDestNumber_Type.__name__=_E
_HpnicfSmsDestNumber_Object=MibTableColumn
hpnicfSmsDestNumber=_HpnicfSmsDestNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,2,2,1,1),_HpnicfSmsDestNumber_Type())
hpnicfSmsDestNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSmsDestNumber.setStatus(_A)
class _HpnicfSmsEncode_Type(HpnicfSmsEncodeType):defaultValue=1
_HpnicfSmsEncode_Type.__name__=_a
_HpnicfSmsEncode_Object=MibTableColumn
hpnicfSmsEncode=_HpnicfSmsEncode_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,2,2,1,2),_HpnicfSmsEncode_Type())
hpnicfSmsEncode.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSmsEncode.setStatus(_A)
class _HpnicfSmsContent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSmsContent_Type.__name__=_S
_HpnicfSmsContent_Object=MibTableColumn
hpnicfSmsContent=_HpnicfSmsContent_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,2,2,1,3),_HpnicfSmsContent_Type())
hpnicfSmsContent.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSmsContent.setStatus(_A)
class _HpnicfSmsSendStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('set2Send',1),('ready2Send',2),('sending',3),('sentAlready',4),('telnumberInvalid',5),('paramInvalid',6),('contentTooLong',7),('codeError',8),(_F,9),('busy',10),('notPresent',11),('notSupport',12),('initializing',13),('noCenterNum',14),('noSim',15),('simNotReady',16),('sendAtFailed',17),('sendDisable',18)))
_HpnicfSmsSendStatus_Type.__name__=_D
_HpnicfSmsSendStatus_Object=MibTableColumn
hpnicfSmsSendStatus=_HpnicfSmsSendStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,2,2,1,4),_HpnicfSmsSendStatus_Type())
hpnicfSmsSendStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSmsSendStatus.setStatus(_A)
_HpnicfWirelessCardOnlineTable_Object=MibTable
hpnicfWirelessCardOnlineTable=_HpnicfWirelessCardOnlineTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,3))
if mibBuilder.loadTexts:hpnicfWirelessCardOnlineTable.setStatus(_A)
_HpnicfWirelessCardOnlineEntry_Object=MibTableRow
hpnicfWirelessCardOnlineEntry=_HpnicfWirelessCardOnlineEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,3,1))
hpnicfWirelessCardOnlineEntry.setIndexNames((0,_B,_G),(0,_B,_b))
if mibBuilder.loadTexts:hpnicfWirelessCardOnlineEntry.setStatus(_A)
_HpnicfWirelessCardOnlineTime_Type=Unsigned32
_HpnicfWirelessCardOnlineTime_Object=MibTableColumn
hpnicfWirelessCardOnlineTime=_HpnicfWirelessCardOnlineTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,3,1,1),_HpnicfWirelessCardOnlineTime_Type())
hpnicfWirelessCardOnlineTime.setMaxAccess(_c)
if mibBuilder.loadTexts:hpnicfWirelessCardOnlineTime.setStatus(_A)
class _HpnicfWirelessCardOnlineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HpnicfWirelessCardOnlineType_Type.__name__=_D
_HpnicfWirelessCardOnlineType_Object=MibTableColumn
hpnicfWirelessCardOnlineType=_HpnicfWirelessCardOnlineType_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,1,3,1,2),_HpnicfWirelessCardOnlineType_Type())
hpnicfWirelessCardOnlineType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWirelessCardOnlineType.setStatus(_A)
_HpnicfUIM_ObjectIdentity=ObjectIdentity
hpnicfUIM=_HpnicfUIM_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,98,1,2))
_HpnicfUIMInfoTable_Object=MibTable
hpnicfUIMInfoTable=_HpnicfUIMInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,2,1))
if mibBuilder.loadTexts:hpnicfUIMInfoTable.setStatus(_A)
_HpnicfUIMInfoEntry_Object=MibTableRow
hpnicfUIMInfoEntry=_HpnicfUIMInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,2,1,1))
hpnicfUIMInfoEntry.setIndexNames((0,_B,_G),(0,_B,_d))
if mibBuilder.loadTexts:hpnicfUIMInfoEntry.setStatus(_A)
class _HpnicfUIMIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfUIMIndex_Type.__name__=_D
_HpnicfUIMIndex_Object=MibTableColumn
hpnicfUIMIndex=_HpnicfUIMIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,2,1,1,1),_HpnicfUIMIndex_Type())
hpnicfUIMIndex.setMaxAccess(_c)
if mibBuilder.loadTexts:hpnicfUIMIndex.setStatus(_A)
_HpnicfUIMStatus_Type=HpnicfUIMStatusType
_HpnicfUIMStatus_Object=MibTableColumn
hpnicfUIMStatus=_HpnicfUIMStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,2,1,1,2),_HpnicfUIMStatus_Type())
hpnicfUIMStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUIMStatus.setStatus(_A)
class _HpnicfUIMImsi_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfUIMImsi_Type.__name__=_E
_HpnicfUIMImsi_Object=MibTableColumn
hpnicfUIMImsi=_HpnicfUIMImsi_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,2,1,1,3),_HpnicfUIMImsi_Type())
hpnicfUIMImsi.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUIMImsi.setStatus(_A)
class _HpnicfUIMPin_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_HpnicfUIMPin_Type.__name__=_E
_HpnicfUIMPin_Object=MibTableColumn
hpnicfUIMPin=_HpnicfUIMPin_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,2,1,1,4),_HpnicfUIMPin_Type())
hpnicfUIMPin.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUIMPin.setStatus(_A)
class _HpnicfUIMVoltage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpnicfUIMVoltage_Type.__name__=_T
_HpnicfUIMVoltage_Object=MibTableColumn
hpnicfUIMVoltage=_HpnicfUIMVoltage_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,2,1,1,5),_HpnicfUIMVoltage_Type())
hpnicfUIMVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUIMVoltage.setStatus(_A)
if mibBuilder.loadTexts:hpnicfUIMVoltage.setUnits('milli-volt')
class _HpnicfUIMProvider_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfUIMProvider_Type.__name__=_E
_HpnicfUIMProvider_Object=MibTableColumn
hpnicfUIMProvider=_HpnicfUIMProvider_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,2,1,1,6),_HpnicfUIMProvider_Type())
hpnicfUIMProvider.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUIMProvider.setStatus(_A)
class _HpnicfUIMSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31),ValueRangeConstraint(99,99))
_HpnicfUIMSignal_Type.__name__=_D
_HpnicfUIMSignal_Object=MibTableColumn
hpnicfUIMSignal=_HpnicfUIMSignal_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,2,1,1,7),_HpnicfUIMSignal_Type())
hpnicfUIMSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUIMSignal.setStatus(_A)
class _HpnicfUIMTryPinPukTimes_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpnicfUIMTryPinPukTimes_Type.__name__=_T
_HpnicfUIMTryPinPukTimes_Object=MibTableColumn
hpnicfUIMTryPinPukTimes=_HpnicfUIMTryPinPukTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,2,1,1,8),_HpnicfUIMTryPinPukTimes_Type())
hpnicfUIMTryPinPukTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUIMTryPinPukTimes.setStatus(_A)
class _HpnicfUIMOldPin_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_HpnicfUIMOldPin_Type.__name__=_E
_HpnicfUIMOldPin_Object=MibTableColumn
hpnicfUIMOldPin=_HpnicfUIMOldPin_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,2,1,1,9),_HpnicfUIMOldPin_Type())
hpnicfUIMOldPin.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfUIMOldPin.setStatus(_A)
_Hpnicf3GCdma_ObjectIdentity=ObjectIdentity
hpnicf3GCdma=_Hpnicf3GCdma_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3))
_Hpnicf3GCdma1xRttTable_Object=MibTable
hpnicf3GCdma1xRttTable=_Hpnicf3GCdma1xRttTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,1))
if mibBuilder.loadTexts:hpnicf3GCdma1xRttTable.setStatus(_A)
_Hpnicf3GCdma1xRttEntry_Object=MibTableRow
hpnicf3GCdma1xRttEntry=_Hpnicf3GCdma1xRttEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,1,1))
hpnicf3GCdma1xRttEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpnicf3GCdma1xRttEntry.setStatus(_A)
class _Hpnicf3GCdma1xRttCurrentRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,-2147483648),ValueRangeConstraint(-150,0))
_Hpnicf3GCdma1xRttCurrentRssi_Type.__name__=_D
_Hpnicf3GCdma1xRttCurrentRssi_Object=MibTableColumn
hpnicf3GCdma1xRttCurrentRssi=_Hpnicf3GCdma1xRttCurrentRssi_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,1,1,1),_Hpnicf3GCdma1xRttCurrentRssi_Type())
hpnicf3GCdma1xRttCurrentRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GCdma1xRttCurrentRssi.setStatus(_A)
if mibBuilder.loadTexts:hpnicf3GCdma1xRttCurrentRssi.setUnits(_I)
class _Hpnicf3GCdma1xRttRssiMediumThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_Hpnicf3GCdma1xRttRssiMediumThreshold_Type.__name__=_D
_Hpnicf3GCdma1xRttRssiMediumThreshold_Object=MibTableColumn
hpnicf3GCdma1xRttRssiMediumThreshold=_Hpnicf3GCdma1xRttRssiMediumThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,1,1,2),_Hpnicf3GCdma1xRttRssiMediumThreshold_Type())
hpnicf3GCdma1xRttRssiMediumThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicf3GCdma1xRttRssiMediumThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicf3GCdma1xRttRssiMediumThreshold.setUnits(_I)
class _Hpnicf3GCdma1xRttRssiWeakThreshold_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_Hpnicf3GCdma1xRttRssiWeakThreshold_Type.__name__=_D
_Hpnicf3GCdma1xRttRssiWeakThreshold_Object=MibTableColumn
hpnicf3GCdma1xRttRssiWeakThreshold=_Hpnicf3GCdma1xRttRssiWeakThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,1,1,3),_Hpnicf3GCdma1xRttRssiWeakThreshold_Type())
hpnicf3GCdma1xRttRssiWeakThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicf3GCdma1xRttRssiWeakThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicf3GCdma1xRttRssiWeakThreshold.setUnits(_I)
class _Hpnicf3GCdma1xRttCurServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_U,2),(_V,3),(_W,4),(_O,5)))
_Hpnicf3GCdma1xRttCurServiceStatus_Type.__name__=_D
_Hpnicf3GCdma1xRttCurServiceStatus_Object=MibTableColumn
hpnicf3GCdma1xRttCurServiceStatus=_Hpnicf3GCdma1xRttCurServiceStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,1,1,4),_Hpnicf3GCdma1xRttCurServiceStatus_Type())
hpnicf3GCdma1xRttCurServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GCdma1xRttCurServiceStatus.setStatus(_A)
class _Hpnicf3GCdma1xRttCurRoamingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_X,2),(_Y,3)))
_Hpnicf3GCdma1xRttCurRoamingStatus_Type.__name__=_D
_Hpnicf3GCdma1xRttCurRoamingStatus_Object=MibTableColumn
hpnicf3GCdma1xRttCurRoamingStatus=_Hpnicf3GCdma1xRttCurRoamingStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,1,1,5),_Hpnicf3GCdma1xRttCurRoamingStatus_Type())
hpnicf3GCdma1xRttCurRoamingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GCdma1xRttCurRoamingStatus.setStatus(_A)
_Hpnicf3GCdmaEvDoTable_Object=MibTable
hpnicf3GCdmaEvDoTable=_Hpnicf3GCdmaEvDoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,2))
if mibBuilder.loadTexts:hpnicf3GCdmaEvDoTable.setStatus(_A)
_Hpnicf3GCdmaEvDoEntry_Object=MibTableRow
hpnicf3GCdmaEvDoEntry=_Hpnicf3GCdmaEvDoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,2,1))
hpnicf3GCdmaEvDoEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpnicf3GCdmaEvDoEntry.setStatus(_A)
class _Hpnicf3GCdmaEvDoCurrentRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,-2147483648),ValueRangeConstraint(-150,0))
_Hpnicf3GCdmaEvDoCurrentRssi_Type.__name__=_D
_Hpnicf3GCdmaEvDoCurrentRssi_Object=MibTableColumn
hpnicf3GCdmaEvDoCurrentRssi=_Hpnicf3GCdmaEvDoCurrentRssi_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,2,1,1),_Hpnicf3GCdmaEvDoCurrentRssi_Type())
hpnicf3GCdmaEvDoCurrentRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GCdmaEvDoCurrentRssi.setStatus(_A)
if mibBuilder.loadTexts:hpnicf3GCdmaEvDoCurrentRssi.setUnits(_I)
class _Hpnicf3GCdmaEvDoRssiMediumThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_Hpnicf3GCdmaEvDoRssiMediumThreshold_Type.__name__=_D
_Hpnicf3GCdmaEvDoRssiMediumThreshold_Object=MibTableColumn
hpnicf3GCdmaEvDoRssiMediumThreshold=_Hpnicf3GCdmaEvDoRssiMediumThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,2,1,2),_Hpnicf3GCdmaEvDoRssiMediumThreshold_Type())
hpnicf3GCdmaEvDoRssiMediumThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicf3GCdmaEvDoRssiMediumThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicf3GCdmaEvDoRssiMediumThreshold.setUnits(_I)
class _Hpnicf3GCdmaEvDoRssiWeakThreshold_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_Hpnicf3GCdmaEvDoRssiWeakThreshold_Type.__name__=_D
_Hpnicf3GCdmaEvDoRssiWeakThreshold_Object=MibTableColumn
hpnicf3GCdmaEvDoRssiWeakThreshold=_Hpnicf3GCdmaEvDoRssiWeakThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,2,1,3),_Hpnicf3GCdmaEvDoRssiWeakThreshold_Type())
hpnicf3GCdmaEvDoRssiWeakThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicf3GCdmaEvDoRssiWeakThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicf3GCdmaEvDoRssiWeakThreshold.setUnits(_I)
class _Hpnicf3GCdmaEvDoCurServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_U,2),(_V,3),(_W,4),(_O,5)))
_Hpnicf3GCdmaEvDoCurServiceStatus_Type.__name__=_D
_Hpnicf3GCdmaEvDoCurServiceStatus_Object=MibTableColumn
hpnicf3GCdmaEvDoCurServiceStatus=_Hpnicf3GCdmaEvDoCurServiceStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,2,1,4),_Hpnicf3GCdmaEvDoCurServiceStatus_Type())
hpnicf3GCdmaEvDoCurServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GCdmaEvDoCurServiceStatus.setStatus(_A)
class _Hpnicf3GCdmaEvDoCurRoamingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_X,2),(_Y,3)))
_Hpnicf3GCdmaEvDoCurRoamingStatus_Type.__name__=_D
_Hpnicf3GCdmaEvDoCurRoamingStatus_Object=MibTableColumn
hpnicf3GCdmaEvDoCurRoamingStatus=_Hpnicf3GCdmaEvDoCurRoamingStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,3,2,1,5),_Hpnicf3GCdmaEvDoCurRoamingStatus_Type())
hpnicf3GCdmaEvDoCurRoamingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GCdmaEvDoCurRoamingStatus.setStatus(_A)
_Hpnicf3GGsm_ObjectIdentity=ObjectIdentity
hpnicf3GGsm=_Hpnicf3GGsm_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4))
_Hpnicf3GGsmInfoTable_Object=MibTable
hpnicf3GGsmInfoTable=_Hpnicf3GGsmInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1))
if mibBuilder.loadTexts:hpnicf3GGsmInfoTable.setStatus(_A)
_Hpnicf3GGsmInfoEntry_Object=MibTableRow
hpnicf3GGsmInfoEntry=_Hpnicf3GGsmInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1))
hpnicf3GGsmInfoEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpnicf3GGsmInfoEntry.setStatus(_A)
class _Hpnicf3GGsmCurrentRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,-2147483648),ValueRangeConstraint(-150,0))
_Hpnicf3GGsmCurrentRssi_Type.__name__=_D
_Hpnicf3GGsmCurrentRssi_Object=MibTableColumn
hpnicf3GGsmCurrentRssi=_Hpnicf3GGsmCurrentRssi_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,1),_Hpnicf3GGsmCurrentRssi_Type())
hpnicf3GGsmCurrentRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GGsmCurrentRssi.setStatus(_A)
if mibBuilder.loadTexts:hpnicf3GGsmCurrentRssi.setUnits(_I)
class _Hpnicf3GGsmRssiMediumThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_Hpnicf3GGsmRssiMediumThreshold_Type.__name__=_D
_Hpnicf3GGsmRssiMediumThreshold_Object=MibTableColumn
hpnicf3GGsmRssiMediumThreshold=_Hpnicf3GGsmRssiMediumThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,2),_Hpnicf3GGsmRssiMediumThreshold_Type())
hpnicf3GGsmRssiMediumThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicf3GGsmRssiMediumThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicf3GGsmRssiMediumThreshold.setUnits(_I)
class _Hpnicf3GGsmRssiWeakThreshold_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_Hpnicf3GGsmRssiWeakThreshold_Type.__name__=_D
_Hpnicf3GGsmRssiWeakThreshold_Object=MibTableColumn
hpnicf3GGsmRssiWeakThreshold=_Hpnicf3GGsmRssiWeakThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,3),_Hpnicf3GGsmRssiWeakThreshold_Type())
hpnicf3GGsmRssiWeakThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicf3GGsmRssiWeakThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicf3GGsmRssiWeakThreshold.setUnits(_I)
class _Hpnicf3GGsmImsi_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hpnicf3GGsmImsi_Type.__name__=_E
_Hpnicf3GGsmImsi_Object=MibTableColumn
hpnicf3GGsmImsi=_Hpnicf3GGsmImsi_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,4),_Hpnicf3GGsmImsi_Type())
hpnicf3GGsmImsi.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GGsmImsi.setStatus(_A)
class _Hpnicf3GGsmImei_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hpnicf3GGsmImei_Type.__name__=_E
_Hpnicf3GGsmImei_Object=MibTableColumn
hpnicf3GGsmImei=_Hpnicf3GGsmImei_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,5),_Hpnicf3GGsmImei_Type())
hpnicf3GGsmImei.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GGsmImei.setStatus(_A)
class _Hpnicf3GGsmApn_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_Hpnicf3GGsmApn_Type.__name__=_E
_Hpnicf3GGsmApn_Object=MibTableColumn
hpnicf3GGsmApn=_Hpnicf3GGsmApn_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,6),_Hpnicf3GGsmApn_Type())
hpnicf3GGsmApn.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicf3GGsmApn.setStatus(_A)
class _Hpnicf3GGsmPacketSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('active',2),('inactive',3)))
_Hpnicf3GGsmPacketSessionStatus_Type.__name__=_D
_Hpnicf3GGsmPacketSessionStatus_Object=MibTableColumn
hpnicf3GGsmPacketSessionStatus=_Hpnicf3GGsmPacketSessionStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,7),_Hpnicf3GGsmPacketSessionStatus_Type())
hpnicf3GGsmPacketSessionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GGsmPacketSessionStatus.setStatus(_A)
class _Hpnicf3GGsmNetworkSelectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('automatic',2),('manual',3)))
_Hpnicf3GGsmNetworkSelectionMode_Type.__name__=_D
_Hpnicf3GGsmNetworkSelectionMode_Object=MibTableColumn
hpnicf3GGsmNetworkSelectionMode=_Hpnicf3GGsmNetworkSelectionMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,8),_Hpnicf3GGsmNetworkSelectionMode_Type())
hpnicf3GGsmNetworkSelectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GGsmNetworkSelectionMode.setStatus(_A)
class _Hpnicf3GGsmMobileNetworkName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hpnicf3GGsmMobileNetworkName_Type.__name__=_E
_Hpnicf3GGsmMobileNetworkName_Object=MibTableColumn
hpnicf3GGsmMobileNetworkName=_Hpnicf3GGsmMobileNetworkName_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,9),_Hpnicf3GGsmMobileNetworkName_Type())
hpnicf3GGsmMobileNetworkName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GGsmMobileNetworkName.setStatus(_A)
class _Hpnicf3GGsmLac_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hpnicf3GGsmLac_Type.__name__=_E
_Hpnicf3GGsmLac_Object=MibTableColumn
hpnicf3GGsmLac=_Hpnicf3GGsmLac_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,10),_Hpnicf3GGsmLac_Type())
hpnicf3GGsmLac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GGsmLac.setStatus(_A)
class _Hpnicf3GGsmCellId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hpnicf3GGsmCellId_Type.__name__=_E
_Hpnicf3GGsmCellId_Object=MibTableColumn
hpnicf3GGsmCellId=_Hpnicf3GGsmCellId_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,11),_Hpnicf3GGsmCellId_Type())
hpnicf3GGsmCellId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GGsmCellId.setStatus(_A)
class _Hpnicf3GGsmSimStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('ok',2),('notInsert',3),('networkReject',4),('blocked',5)))
_Hpnicf3GGsmSimStatus_Type.__name__=_D
_Hpnicf3GGsmSimStatus_Object=MibTableColumn
hpnicf3GGsmSimStatus=_Hpnicf3GGsmSimStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,12),_Hpnicf3GGsmSimStatus_Type())
hpnicf3GGsmSimStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GGsmSimStatus.setStatus(_A)
class _Hpnicf3GGsmCurServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_U,2),(_V,3),(_W,4),(_O,5)))
_Hpnicf3GGsmCurServiceStatus_Type.__name__=_D
_Hpnicf3GGsmCurServiceStatus_Object=MibTableColumn
hpnicf3GGsmCurServiceStatus=_Hpnicf3GGsmCurServiceStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,13),_Hpnicf3GGsmCurServiceStatus_Type())
hpnicf3GGsmCurServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GGsmCurServiceStatus.setStatus(_A)
class _Hpnicf3GGsmCurRoamingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_X,2),(_Y,3)))
_Hpnicf3GGsmCurRoamingStatus_Type.__name__=_D
_Hpnicf3GGsmCurRoamingStatus_Object=MibTableColumn
hpnicf3GGsmCurRoamingStatus=_Hpnicf3GGsmCurRoamingStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,14),_Hpnicf3GGsmCurRoamingStatus_Type())
hpnicf3GGsmCurRoamingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GGsmCurRoamingStatus.setStatus(_A)
class _Hpnicf3GGsmMcc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hpnicf3GGsmMcc_Type.__name__=_E
_Hpnicf3GGsmMcc_Object=MibTableColumn
hpnicf3GGsmMcc=_Hpnicf3GGsmMcc_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,15),_Hpnicf3GGsmMcc_Type())
hpnicf3GGsmMcc.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GGsmMcc.setStatus(_A)
class _Hpnicf3GGsmMnc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hpnicf3GGsmMnc_Type.__name__=_E
_Hpnicf3GGsmMnc_Object=MibTableColumn
hpnicf3GGsmMnc=_Hpnicf3GGsmMnc_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,4,1,1,16),_Hpnicf3GGsmMnc_Type())
hpnicf3GGsmMnc.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicf3GGsmMnc.setStatus(_A)
_HpnicfLte_ObjectIdentity=ObjectIdentity
hpnicfLte=_HpnicfLte_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,98,1,5))
_HpnicfLteInfoTable_Object=MibTable
hpnicfLteInfoTable=_HpnicfLteInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,5,1))
if mibBuilder.loadTexts:hpnicfLteInfoTable.setStatus(_A)
_HpnicfLteInfoEntry_Object=MibTableRow
hpnicfLteInfoEntry=_HpnicfLteInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,5,1,1))
hpnicfLteInfoEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpnicfLteInfoEntry.setStatus(_A)
_HpnicfLteCurrentRsrp_Type=Integer32
_HpnicfLteCurrentRsrp_Object=MibTableColumn
hpnicfLteCurrentRsrp=_HpnicfLteCurrentRsrp_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,5,1,1,1),_HpnicfLteCurrentRsrp_Type())
hpnicfLteCurrentRsrp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfLteCurrentRsrp.setStatus(_A)
if mibBuilder.loadTexts:hpnicfLteCurrentRsrp.setUnits(_I)
_HpnicfLteCurrentRsrq_Type=Integer32
_HpnicfLteCurrentRsrq_Object=MibTableColumn
hpnicfLteCurrentRsrq=_HpnicfLteCurrentRsrq_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,5,1,1,2),_HpnicfLteCurrentRsrq_Type())
hpnicfLteCurrentRsrq.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfLteCurrentRsrq.setStatus(_A)
if mibBuilder.loadTexts:hpnicfLteCurrentRsrq.setUnits('dB')
_HpnicfLteCurrentSinr_Type=Integer32
_HpnicfLteCurrentSinr_Object=MibTableColumn
hpnicfLteCurrentSinr=_HpnicfLteCurrentSinr_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,5,1,1,3),_HpnicfLteCurrentSinr_Type())
hpnicfLteCurrentSinr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfLteCurrentSinr.setStatus(_A)
if mibBuilder.loadTexts:hpnicfLteCurrentSinr.setUnits('dB')
_HpnicfLteTxPower_Type=Integer32
_HpnicfLteTxPower_Object=MibTableColumn
hpnicfLteTxPower=_HpnicfLteTxPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,5,1,1,4),_HpnicfLteTxPower_Type())
hpnicfLteTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfLteTxPower.setStatus(_A)
if mibBuilder.loadTexts:hpnicfLteTxPower.setUnits('dB')
class _HpnicfLteCurrentRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,-2147483648),ValueRangeConstraint(-150,0))
_HpnicfLteCurrentRssi_Type.__name__=_D
_HpnicfLteCurrentRssi_Object=MibTableColumn
hpnicfLteCurrentRssi=_HpnicfLteCurrentRssi_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,5,1,1,5),_HpnicfLteCurrentRssi_Type())
hpnicfLteCurrentRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfLteCurrentRssi.setStatus(_A)
if mibBuilder.loadTexts:hpnicfLteCurrentRssi.setUnits(_I)
class _HpnicfLteRssiMediumThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_HpnicfLteRssiMediumThreshold_Type.__name__=_D
_HpnicfLteRssiMediumThreshold_Object=MibTableColumn
hpnicfLteRssiMediumThreshold=_HpnicfLteRssiMediumThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,5,1,1,6),_HpnicfLteRssiMediumThreshold_Type())
hpnicfLteRssiMediumThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfLteRssiMediumThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfLteRssiMediumThreshold.setUnits(_I)
class _HpnicfLteRssiWeakThreshold_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_HpnicfLteRssiWeakThreshold_Type.__name__=_D
_HpnicfLteRssiWeakThreshold_Object=MibTableColumn
hpnicfLteRssiWeakThreshold=_HpnicfLteRssiWeakThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,1,5,1,1,7),_HpnicfLteRssiWeakThreshold_Type())
hpnicfLteRssiWeakThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfLteRssiWeakThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfLteRssiWeakThreshold.setUnits(_I)
_Hpnicf3GModemTrap_ObjectIdentity=ObjectIdentity
hpnicf3GModemTrap=_Hpnicf3GModemTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,98,2))
class _HpnicfDevSerialNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfDevSerialNumber_Type.__name__=_E
_HpnicfDevSerialNumber_Object=MibScalar
hpnicfDevSerialNumber=_HpnicfDevSerialNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,2,1),_HpnicfDevSerialNumber_Type())
hpnicfDevSerialNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfDevSerialNumber.setStatus(_A)
class _HpnicfDeviceOUI_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfDeviceOUI_Type.__name__=_E
_HpnicfDeviceOUI_Object=MibScalar
hpnicfDeviceOUI=_HpnicfDeviceOUI_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,2,2),_HpnicfDeviceOUI_Type())
hpnicfDeviceOUI.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfDeviceOUI.setStatus(_A)
class _HpnicfAccessMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('air',2),('cable',3)))
_HpnicfAccessMedia_Type.__name__=_D
_HpnicfAccessMedia_Object=MibScalar
hpnicfAccessMedia=_HpnicfAccessMedia_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,2,3),_HpnicfAccessMedia_Type())
hpnicfAccessMedia.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfAccessMedia.setStatus(_A)
class _Hpnicf3GCurrentService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('oneXRtt',2),('evDo',3),('gsm',4),('lte',5)))
_Hpnicf3GCurrentService_Type.__name__=_D
_Hpnicf3GCurrentService_Object=MibScalar
hpnicf3GCurrentService=_Hpnicf3GCurrentService_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,2,4),_Hpnicf3GCurrentService_Type())
hpnicf3GCurrentService.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicf3GCurrentService.setStatus(_A)
class _Hpnicf3GCurrentRssiBind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,-2147483648),ValueRangeConstraint(-150,0))
_Hpnicf3GCurrentRssiBind_Type.__name__=_D
_Hpnicf3GCurrentRssiBind_Object=MibScalar
hpnicf3GCurrentRssiBind=_Hpnicf3GCurrentRssiBind_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,2,5),_Hpnicf3GCurrentRssiBind_Type())
hpnicf3GCurrentRssiBind.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicf3GCurrentRssiBind.setStatus(_A)
if mibBuilder.loadTexts:hpnicf3GCurrentRssiBind.setUnits(_I)
class _Hpnicf3GImsiBind_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hpnicf3GImsiBind_Type.__name__=_E
_Hpnicf3GImsiBind_Object=MibScalar
hpnicf3GImsiBind=_Hpnicf3GImsiBind_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,2,6),_Hpnicf3GImsiBind_Type())
hpnicf3GImsiBind.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicf3GImsiBind.setStatus(_A)
class _HpnicfSmsSrcNumberBind_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_HpnicfSmsSrcNumberBind_Type.__name__=_E
_HpnicfSmsSrcNumberBind_Object=MibScalar
hpnicfSmsSrcNumberBind=_HpnicfSmsSrcNumberBind_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,2,7),_HpnicfSmsSrcNumberBind_Type())
hpnicfSmsSrcNumberBind.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfSmsSrcNumberBind.setStatus(_A)
class _HpnicfSmsTimeBind_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpnicfSmsTimeBind_Type.__name__=_E
_HpnicfSmsTimeBind_Object=MibScalar
hpnicfSmsTimeBind=_HpnicfSmsTimeBind_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,2,8),_HpnicfSmsTimeBind_Type())
hpnicfSmsTimeBind.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfSmsTimeBind.setStatus(_A)
_HpnicfSmsEncodeBind_Type=HpnicfSmsEncodeType
_HpnicfSmsEncodeBind_Object=MibScalar
hpnicfSmsEncodeBind=_HpnicfSmsEncodeBind_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,2,9),_HpnicfSmsEncodeBind_Type())
hpnicfSmsEncodeBind.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfSmsEncodeBind.setStatus(_A)
class _HpnicfSmsContentBind_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_HpnicfSmsContentBind_Type.__name__=_S
_HpnicfSmsContentBind_Object=MibScalar
hpnicfSmsContentBind=_HpnicfSmsContentBind_Object((1,3,6,1,4,1,11,2,14,11,15,2,98,2,10),_HpnicfSmsContentBind_Type())
hpnicfSmsContentBind.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfSmsContentBind.setStatus(_A)
_Hpnicf3GModemTraps_ObjectIdentity=ObjectIdentity
hpnicf3GModemTraps=_Hpnicf3GModemTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,98,3))
_Hpnicf3GModemTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicf3GModemTrapPrefix=_Hpnicf3GModemTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,98,3,0))
hpnicfWirelessCardInserted=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,98,3,0,1))
hpnicfWirelessCardInserted.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpnicfWirelessCardInserted.setStatus(_A)
hpnicfWirelessCardPulledOut=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,98,3,0,2))
hpnicfWirelessCardPulledOut.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpnicfWirelessCardPulledOut.setStatus(_A)
hpnicfUIMPinInvalid=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,98,3,0,3))
hpnicfUIMPinInvalid.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpnicfUIMPinInvalid.setStatus(_A)
hpnicfUIMPinChanged=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,98,3,0,4))
hpnicfUIMPinChanged.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:hpnicfUIMPinChanged.setStatus(_A)
hpnicfAccessMediaChanged=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,98,3,0,5))
hpnicfAccessMediaChanged.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_g)))
if mibBuilder.loadTexts:hpnicfAccessMediaChanged.setStatus(_A)
hpnicf3GRssiStrongSignalTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,98,3,0,6))
hpnicf3GRssiStrongSignalTrap.setObjects(*((_B,_G),(_B,_K),(_B,_L),(_B,_M),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:hpnicf3GRssiStrongSignalTrap.setStatus(_A)
hpnicf3GRssiMediumSignalTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,98,3,0,7))
hpnicf3GRssiMediumSignalTrap.setObjects(*((_B,_G),(_B,_K),(_B,_L),(_B,_M),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:hpnicf3GRssiMediumSignalTrap.setStatus(_A)
hpnicf3GRssiWeakSignalTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,98,3,0,8))
hpnicf3GRssiWeakSignalTrap.setObjects(*((_B,_G),(_B,_K),(_B,_L),(_B,_M),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:hpnicf3GRssiWeakSignalTrap.setStatus(_A)
hpnicfSmsTxNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,98,3,0,9))
hpnicfSmsTxNotification.setObjects(*((_B,_G),(_B,_h)))
if mibBuilder.loadTexts:hpnicfSmsTxNotification.setStatus(_A)
hpnicfSmsRxNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,98,3,0,10))
hpnicfSmsRxNotification.setObjects(*((_B,_G),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:hpnicfSmsRxNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpnicfUIMStatusType':HpnicfUIMStatusType,_a:HpnicfSmsEncodeType,'hpnicf3GModem':hpnicf3GModem,'hpnicf3GModemObjects':hpnicf3GModemObjects,'hpnicfWirelessCard':hpnicfWirelessCard,'hpnicfWirelessCardTable':hpnicfWirelessCardTable,'hpnicfWirelessCardEntry':hpnicfWirelessCardEntry,_G:hpnicfWirelessCardIndex,'hpnicfWirelessCardModelName':hpnicfWirelessCardModelName,'hpnicfWirelessCardMfgName':hpnicfWirelessCardMfgName,'hpnicfWirelessCardDescription':hpnicfWirelessCardDescription,_M:hpnicfWirelessCardSerialNumber,'hpnicfWirelessCardCMIIID':hpnicfWirelessCardCMIIID,'hpnicfWirelessCardHardwareVersion':hpnicfWirelessCardHardwareVersion,'hpnicfWirelessCardFirmwareVersion':hpnicfWirelessCardFirmwareVersion,'hpnicfWirelessCardPRLVersion':hpnicfWirelessCardPRLVersion,'hpnicfWirelessCardInterfaceIndex':hpnicfWirelessCardInterfaceIndex,'hpnicfWirelessCardModemStatus':hpnicfWirelessCardModemStatus,'hpnicfWirelessCardModemMode':hpnicfWirelessCardModemMode,'hpnicfWirelessCardCurNetConn':hpnicfWirelessCardCurNetConn,'hpnicfSmsGroup':hpnicfSmsGroup,'hpnicfSmsScalarObjects':hpnicfSmsScalarObjects,'hpnicfSmsRxNotifSwitch':hpnicfSmsRxNotifSwitch,'hpnicfSmsOperationTable':hpnicfSmsOperationTable,'hpnicfSmsOperationEntry':hpnicfSmsOperationEntry,'hpnicfSmsDestNumber':hpnicfSmsDestNumber,'hpnicfSmsEncode':hpnicfSmsEncode,'hpnicfSmsContent':hpnicfSmsContent,_h:hpnicfSmsSendStatus,'hpnicfWirelessCardOnlineTable':hpnicfWirelessCardOnlineTable,'hpnicfWirelessCardOnlineEntry':hpnicfWirelessCardOnlineEntry,_b:hpnicfWirelessCardOnlineTime,'hpnicfWirelessCardOnlineType':hpnicfWirelessCardOnlineType,'hpnicfUIM':hpnicfUIM,'hpnicfUIMInfoTable':hpnicfUIMInfoTable,'hpnicfUIMInfoEntry':hpnicfUIMInfoEntry,_d:hpnicfUIMIndex,'hpnicfUIMStatus':hpnicfUIMStatus,_N:hpnicfUIMImsi,_f:hpnicfUIMPin,'hpnicfUIMVoltage':hpnicfUIMVoltage,'hpnicfUIMProvider':hpnicfUIMProvider,'hpnicfUIMSignal':hpnicfUIMSignal,'hpnicfUIMTryPinPukTimes':hpnicfUIMTryPinPukTimes,_e:hpnicfUIMOldPin,'hpnicf3GCdma':hpnicf3GCdma,'hpnicf3GCdma1xRttTable':hpnicf3GCdma1xRttTable,'hpnicf3GCdma1xRttEntry':hpnicf3GCdma1xRttEntry,'hpnicf3GCdma1xRttCurrentRssi':hpnicf3GCdma1xRttCurrentRssi,'hpnicf3GCdma1xRttRssiMediumThreshold':hpnicf3GCdma1xRttRssiMediumThreshold,'hpnicf3GCdma1xRttRssiWeakThreshold':hpnicf3GCdma1xRttRssiWeakThreshold,'hpnicf3GCdma1xRttCurServiceStatus':hpnicf3GCdma1xRttCurServiceStatus,'hpnicf3GCdma1xRttCurRoamingStatus':hpnicf3GCdma1xRttCurRoamingStatus,'hpnicf3GCdmaEvDoTable':hpnicf3GCdmaEvDoTable,'hpnicf3GCdmaEvDoEntry':hpnicf3GCdmaEvDoEntry,'hpnicf3GCdmaEvDoCurrentRssi':hpnicf3GCdmaEvDoCurrentRssi,'hpnicf3GCdmaEvDoRssiMediumThreshold':hpnicf3GCdmaEvDoRssiMediumThreshold,'hpnicf3GCdmaEvDoRssiWeakThreshold':hpnicf3GCdmaEvDoRssiWeakThreshold,'hpnicf3GCdmaEvDoCurServiceStatus':hpnicf3GCdmaEvDoCurServiceStatus,'hpnicf3GCdmaEvDoCurRoamingStatus':hpnicf3GCdmaEvDoCurRoamingStatus,'hpnicf3GGsm':hpnicf3GGsm,'hpnicf3GGsmInfoTable':hpnicf3GGsmInfoTable,'hpnicf3GGsmInfoEntry':hpnicf3GGsmInfoEntry,'hpnicf3GGsmCurrentRssi':hpnicf3GGsmCurrentRssi,'hpnicf3GGsmRssiMediumThreshold':hpnicf3GGsmRssiMediumThreshold,'hpnicf3GGsmRssiWeakThreshold':hpnicf3GGsmRssiWeakThreshold,'hpnicf3GGsmImsi':hpnicf3GGsmImsi,'hpnicf3GGsmImei':hpnicf3GGsmImei,'hpnicf3GGsmApn':hpnicf3GGsmApn,'hpnicf3GGsmPacketSessionStatus':hpnicf3GGsmPacketSessionStatus,'hpnicf3GGsmNetworkSelectionMode':hpnicf3GGsmNetworkSelectionMode,'hpnicf3GGsmMobileNetworkName':hpnicf3GGsmMobileNetworkName,'hpnicf3GGsmLac':hpnicf3GGsmLac,'hpnicf3GGsmCellId':hpnicf3GGsmCellId,'hpnicf3GGsmSimStatus':hpnicf3GGsmSimStatus,'hpnicf3GGsmCurServiceStatus':hpnicf3GGsmCurServiceStatus,'hpnicf3GGsmCurRoamingStatus':hpnicf3GGsmCurRoamingStatus,'hpnicf3GGsmMcc':hpnicf3GGsmMcc,'hpnicf3GGsmMnc':hpnicf3GGsmMnc,'hpnicfLte':hpnicfLte,'hpnicfLteInfoTable':hpnicfLteInfoTable,'hpnicfLteInfoEntry':hpnicfLteInfoEntry,'hpnicfLteCurrentRsrp':hpnicfLteCurrentRsrp,'hpnicfLteCurrentRsrq':hpnicfLteCurrentRsrq,'hpnicfLteCurrentSinr':hpnicfLteCurrentSinr,'hpnicfLteTxPower':hpnicfLteTxPower,'hpnicfLteCurrentRssi':hpnicfLteCurrentRssi,'hpnicfLteRssiMediumThreshold':hpnicfLteRssiMediumThreshold,'hpnicfLteRssiWeakThreshold':hpnicfLteRssiWeakThreshold,'hpnicf3GModemTrap':hpnicf3GModemTrap,_L:hpnicfDevSerialNumber,_K:hpnicfDeviceOUI,_g:hpnicfAccessMedia,_P:hpnicf3GCurrentService,_Q:hpnicf3GCurrentRssiBind,_R:hpnicf3GImsiBind,_i:hpnicfSmsSrcNumberBind,_j:hpnicfSmsTimeBind,_k:hpnicfSmsEncodeBind,_l:hpnicfSmsContentBind,'hpnicf3GModemTraps':hpnicf3GModemTraps,'hpnicf3GModemTrapPrefix':hpnicf3GModemTrapPrefix,'hpnicfWirelessCardInserted':hpnicfWirelessCardInserted,'hpnicfWirelessCardPulledOut':hpnicfWirelessCardPulledOut,'hpnicfUIMPinInvalid':hpnicfUIMPinInvalid,'hpnicfUIMPinChanged':hpnicfUIMPinChanged,'hpnicfAccessMediaChanged':hpnicfAccessMediaChanged,'hpnicf3GRssiStrongSignalTrap':hpnicf3GRssiStrongSignalTrap,'hpnicf3GRssiMediumSignalTrap':hpnicf3GRssiMediumSignalTrap,'hpnicf3GRssiWeakSignalTrap':hpnicf3GRssiWeakSignalTrap,'hpnicfSmsTxNotification':hpnicfSmsTxNotification,'hpnicfSmsRxNotification':hpnicfSmsRxNotification})