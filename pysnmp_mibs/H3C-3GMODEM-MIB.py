_m='h3cSmsContentBind'
_l='h3cSmsEncodeBind'
_k='h3cSmsTimeBind'
_j='h3cSmsSrcNumberBind'
_i='h3cSmsSendStatus'
_h='h3cAccessMedia'
_g='h3cUIMPin'
_f='h3cUIMOldPin'
_e='h3cUIMIndex'
_d='not-accessible'
_c='h3cWirelessCardOnlineTime'
_b='H3cSmsEncodeType'
_a='tdscdma'
_Z='home'
_Y='roaming'
_X='lowPower'
_W='emergency'
_V='available'
_U='lte'
_T='OctetString'
_S='h3c3GImsiBind'
_R='h3c3GCurrentRssiBind'
_Q='h3c3GCurrentService'
_P='noService'
_O='h3cUIMImsi'
_N='Unsigned32'
_M='h3cWirelessCardSerialNumber'
_L='h3cDevSerialNumber'
_K='h3cDeviceOUI'
_J='accessible-for-notify'
_I='dBm'
_H='read-write'
_G='h3cWirelessCardIndex'
_F='unknown'
_E='SnmpAdminString'
_D='Integer32'
_C='read-only'
_B='H3C-3GMODEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_T,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
h3c3GModem=ModuleIdentity((1,3,6,1,4,1,2011,10,2,98))
if mibBuilder.loadTexts:h3c3GModem.setRevisions(('2015-12-01 12:00','2014-09-09 12:00','2009-04-30 12:00'))
class H3cUIMStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('absent',1),('initial',2),('fault',3),('unprotected',4),('protected',5),('pinLocked',6),('pukLocked',7),('selfDestruct',8)))
class H3cSmsEncodeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ascii',1),('ucs2',2)))
_H3c3GModemObjects_ObjectIdentity=ObjectIdentity
h3c3GModemObjects=_H3c3GModemObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,98,1))
_H3cWirelessCard_ObjectIdentity=ObjectIdentity
h3cWirelessCard=_H3cWirelessCard_ObjectIdentity((1,3,6,1,4,1,2011,10,2,98,1,1))
_H3cWirelessCardTable_Object=MibTable
h3cWirelessCardTable=_H3cWirelessCardTable_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1))
if mibBuilder.loadTexts:h3cWirelessCardTable.setStatus(_A)
_H3cWirelessCardEntry_Object=MibTableRow
h3cWirelessCardEntry=_H3cWirelessCardEntry_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1))
h3cWirelessCardEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3cWirelessCardEntry.setStatus(_A)
class _H3cWirelessCardIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cWirelessCardIndex_Type.__name__=_D
_H3cWirelessCardIndex_Object=MibTableColumn
h3cWirelessCardIndex=_H3cWirelessCardIndex_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1,1),_H3cWirelessCardIndex_Type())
h3cWirelessCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardIndex.setStatus(_A)
class _H3cWirelessCardModelName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cWirelessCardModelName_Type.__name__=_E
_H3cWirelessCardModelName_Object=MibTableColumn
h3cWirelessCardModelName=_H3cWirelessCardModelName_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1,2),_H3cWirelessCardModelName_Type())
h3cWirelessCardModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardModelName.setStatus(_A)
class _H3cWirelessCardMfgName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cWirelessCardMfgName_Type.__name__=_E
_H3cWirelessCardMfgName_Object=MibTableColumn
h3cWirelessCardMfgName=_H3cWirelessCardMfgName_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1,3),_H3cWirelessCardMfgName_Type())
h3cWirelessCardMfgName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardMfgName.setStatus(_A)
class _H3cWirelessCardDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cWirelessCardDescription_Type.__name__=_E
_H3cWirelessCardDescription_Object=MibTableColumn
h3cWirelessCardDescription=_H3cWirelessCardDescription_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1,4),_H3cWirelessCardDescription_Type())
h3cWirelessCardDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardDescription.setStatus(_A)
class _H3cWirelessCardSerialNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cWirelessCardSerialNumber_Type.__name__=_E
_H3cWirelessCardSerialNumber_Object=MibTableColumn
h3cWirelessCardSerialNumber=_H3cWirelessCardSerialNumber_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1,5),_H3cWirelessCardSerialNumber_Type())
h3cWirelessCardSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardSerialNumber.setStatus(_A)
class _H3cWirelessCardCMIIID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cWirelessCardCMIIID_Type.__name__=_E
_H3cWirelessCardCMIIID_Object=MibTableColumn
h3cWirelessCardCMIIID=_H3cWirelessCardCMIIID_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1,6),_H3cWirelessCardCMIIID_Type())
h3cWirelessCardCMIIID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardCMIIID.setStatus(_A)
class _H3cWirelessCardHardwareVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cWirelessCardHardwareVersion_Type.__name__=_E
_H3cWirelessCardHardwareVersion_Object=MibTableColumn
h3cWirelessCardHardwareVersion=_H3cWirelessCardHardwareVersion_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1,7),_H3cWirelessCardHardwareVersion_Type())
h3cWirelessCardHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardHardwareVersion.setStatus(_A)
class _H3cWirelessCardFirmwareVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cWirelessCardFirmwareVersion_Type.__name__=_E
_H3cWirelessCardFirmwareVersion_Object=MibTableColumn
h3cWirelessCardFirmwareVersion=_H3cWirelessCardFirmwareVersion_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1,8),_H3cWirelessCardFirmwareVersion_Type())
h3cWirelessCardFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardFirmwareVersion.setStatus(_A)
class _H3cWirelessCardPRLVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cWirelessCardPRLVersion_Type.__name__=_E
_H3cWirelessCardPRLVersion_Object=MibTableColumn
h3cWirelessCardPRLVersion=_H3cWirelessCardPRLVersion_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1,9),_H3cWirelessCardPRLVersion_Type())
h3cWirelessCardPRLVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardPRLVersion.setStatus(_A)
_H3cWirelessCardInterfaceIndex_Type=InterfaceIndex
_H3cWirelessCardInterfaceIndex_Object=MibTableColumn
h3cWirelessCardInterfaceIndex=_H3cWirelessCardInterfaceIndex_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1,10),_H3cWirelessCardInterfaceIndex_Type())
h3cWirelessCardInterfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardInterfaceIndex.setStatus(_A)
class _H3cWirelessCardModemStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('onLine',2),('offLine',3)))
_H3cWirelessCardModemStatus_Type.__name__=_D
_H3cWirelessCardModemStatus_Object=MibTableColumn
h3cWirelessCardModemStatus=_H3cWirelessCardModemStatus_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1,11),_H3cWirelessCardModemStatus_Type())
h3cWirelessCardModemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardModemStatus.setStatus(_A)
class _H3cWirelessCardModemMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_a,2),('wcdma',3),('cdma',4),(_U,5)))
_H3cWirelessCardModemMode_Type.__name__=_D
_H3cWirelessCardModemMode_Object=MibTableColumn
h3cWirelessCardModemMode=_H3cWirelessCardModemMode_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1,12),_H3cWirelessCardModemMode_Type())
h3cWirelessCardModemMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardModemMode.setStatus(_A)
class _H3cWirelessCardCurNetConn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_F,1),(_P,2),('gsm',3),('gprs',4),('edge',5),('hsdpa',6),('hsupa',7),('hsupaAndhsdpa',8),('hspaPlus',9),('umts',10),('dchspaPlus',11),(_U,12),('onexrtt',13),('evdo',14),('onexrttAndevdo',15),(_a,16)))
_H3cWirelessCardCurNetConn_Type.__name__=_D
_H3cWirelessCardCurNetConn_Object=MibTableColumn
h3cWirelessCardCurNetConn=_H3cWirelessCardCurNetConn_Object((1,3,6,1,4,1,2011,10,2,98,1,1,1,1,13),_H3cWirelessCardCurNetConn_Type())
h3cWirelessCardCurNetConn.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardCurNetConn.setStatus(_A)
_H3cSmsGroup_ObjectIdentity=ObjectIdentity
h3cSmsGroup=_H3cSmsGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,98,1,1,2))
_H3cSmsScalarObjects_ObjectIdentity=ObjectIdentity
h3cSmsScalarObjects=_H3cSmsScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,98,1,1,2,1))
_H3cSmsRxNotifSwitch_Type=TruthValue
_H3cSmsRxNotifSwitch_Object=MibScalar
h3cSmsRxNotifSwitch=_H3cSmsRxNotifSwitch_Object((1,3,6,1,4,1,2011,10,2,98,1,1,2,1,1),_H3cSmsRxNotifSwitch_Type())
h3cSmsRxNotifSwitch.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSmsRxNotifSwitch.setStatus(_A)
_H3cSmsOperationTable_Object=MibTable
h3cSmsOperationTable=_H3cSmsOperationTable_Object((1,3,6,1,4,1,2011,10,2,98,1,1,2,2))
if mibBuilder.loadTexts:h3cSmsOperationTable.setStatus(_A)
_H3cSmsOperationEntry_Object=MibTableRow
h3cSmsOperationEntry=_H3cSmsOperationEntry_Object((1,3,6,1,4,1,2011,10,2,98,1,1,2,2,1))
h3cSmsOperationEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3cSmsOperationEntry.setStatus(_A)
class _H3cSmsDestNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_H3cSmsDestNumber_Type.__name__=_E
_H3cSmsDestNumber_Object=MibTableColumn
h3cSmsDestNumber=_H3cSmsDestNumber_Object((1,3,6,1,4,1,2011,10,2,98,1,1,2,2,1,1),_H3cSmsDestNumber_Type())
h3cSmsDestNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSmsDestNumber.setStatus(_A)
class _H3cSmsEncode_Type(H3cSmsEncodeType):defaultValue=1
_H3cSmsEncode_Type.__name__=_b
_H3cSmsEncode_Object=MibTableColumn
h3cSmsEncode=_H3cSmsEncode_Object((1,3,6,1,4,1,2011,10,2,98,1,1,2,2,1,2),_H3cSmsEncode_Type())
h3cSmsEncode.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSmsEncode.setStatus(_A)
class _H3cSmsContent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSmsContent_Type.__name__=_T
_H3cSmsContent_Object=MibTableColumn
h3cSmsContent=_H3cSmsContent_Object((1,3,6,1,4,1,2011,10,2,98,1,1,2,2,1,3),_H3cSmsContent_Type())
h3cSmsContent.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSmsContent.setStatus(_A)
class _H3cSmsSendStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('set2Send',1),('ready2Send',2),('sending',3),('sentAlready',4),('telnumberInvalid',5),('paramInvalid',6),('contentTooLong',7),('codeError',8),(_F,9),('busy',10),('notPresent',11),('notSupport',12),('initializing',13),('noCenterNum',14),('noSim',15),('simNotReady',16),('sendAtFailed',17),('sendDisable',18)))
_H3cSmsSendStatus_Type.__name__=_D
_H3cSmsSendStatus_Object=MibTableColumn
h3cSmsSendStatus=_H3cSmsSendStatus_Object((1,3,6,1,4,1,2011,10,2,98,1,1,2,2,1,4),_H3cSmsSendStatus_Type())
h3cSmsSendStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSmsSendStatus.setStatus(_A)
_H3cWirelessCardOnlineTable_Object=MibTable
h3cWirelessCardOnlineTable=_H3cWirelessCardOnlineTable_Object((1,3,6,1,4,1,2011,10,2,98,1,1,3))
if mibBuilder.loadTexts:h3cWirelessCardOnlineTable.setStatus(_A)
_H3cWirelessCardOnlineEntry_Object=MibTableRow
h3cWirelessCardOnlineEntry=_H3cWirelessCardOnlineEntry_Object((1,3,6,1,4,1,2011,10,2,98,1,1,3,1))
h3cWirelessCardOnlineEntry.setIndexNames((0,_B,_G),(0,_B,_c))
if mibBuilder.loadTexts:h3cWirelessCardOnlineEntry.setStatus(_A)
_H3cWirelessCardOnlineTime_Type=Unsigned32
_H3cWirelessCardOnlineTime_Object=MibTableColumn
h3cWirelessCardOnlineTime=_H3cWirelessCardOnlineTime_Object((1,3,6,1,4,1,2011,10,2,98,1,1,3,1,1),_H3cWirelessCardOnlineTime_Type())
h3cWirelessCardOnlineTime.setMaxAccess(_d)
if mibBuilder.loadTexts:h3cWirelessCardOnlineTime.setStatus(_A)
class _H3cWirelessCardOnlineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_H3cWirelessCardOnlineType_Type.__name__=_D
_H3cWirelessCardOnlineType_Object=MibTableColumn
h3cWirelessCardOnlineType=_H3cWirelessCardOnlineType_Object((1,3,6,1,4,1,2011,10,2,98,1,1,3,1,2),_H3cWirelessCardOnlineType_Type())
h3cWirelessCardOnlineType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardOnlineType.setStatus(_A)
_H3cUIM_ObjectIdentity=ObjectIdentity
h3cUIM=_H3cUIM_ObjectIdentity((1,3,6,1,4,1,2011,10,2,98,1,2))
_H3cUIMInfoTable_Object=MibTable
h3cUIMInfoTable=_H3cUIMInfoTable_Object((1,3,6,1,4,1,2011,10,2,98,1,2,1))
if mibBuilder.loadTexts:h3cUIMInfoTable.setStatus(_A)
_H3cUIMInfoEntry_Object=MibTableRow
h3cUIMInfoEntry=_H3cUIMInfoEntry_Object((1,3,6,1,4,1,2011,10,2,98,1,2,1,1))
h3cUIMInfoEntry.setIndexNames((0,_B,_G),(0,_B,_e))
if mibBuilder.loadTexts:h3cUIMInfoEntry.setStatus(_A)
class _H3cUIMIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cUIMIndex_Type.__name__=_D
_H3cUIMIndex_Object=MibTableColumn
h3cUIMIndex=_H3cUIMIndex_Object((1,3,6,1,4,1,2011,10,2,98,1,2,1,1,1),_H3cUIMIndex_Type())
h3cUIMIndex.setMaxAccess(_d)
if mibBuilder.loadTexts:h3cUIMIndex.setStatus(_A)
_H3cUIMStatus_Type=H3cUIMStatusType
_H3cUIMStatus_Object=MibTableColumn
h3cUIMStatus=_H3cUIMStatus_Object((1,3,6,1,4,1,2011,10,2,98,1,2,1,1,2),_H3cUIMStatus_Type())
h3cUIMStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMStatus.setStatus(_A)
class _H3cUIMImsi_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cUIMImsi_Type.__name__=_E
_H3cUIMImsi_Object=MibTableColumn
h3cUIMImsi=_H3cUIMImsi_Object((1,3,6,1,4,1,2011,10,2,98,1,2,1,1,3),_H3cUIMImsi_Type())
h3cUIMImsi.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMImsi.setStatus(_A)
class _H3cUIMPin_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_H3cUIMPin_Type.__name__=_E
_H3cUIMPin_Object=MibTableColumn
h3cUIMPin=_H3cUIMPin_Object((1,3,6,1,4,1,2011,10,2,98,1,2,1,1,4),_H3cUIMPin_Type())
h3cUIMPin.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMPin.setStatus(_A)
class _H3cUIMVoltage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3cUIMVoltage_Type.__name__=_N
_H3cUIMVoltage_Object=MibTableColumn
h3cUIMVoltage=_H3cUIMVoltage_Object((1,3,6,1,4,1,2011,10,2,98,1,2,1,1,5),_H3cUIMVoltage_Type())
h3cUIMVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMVoltage.setStatus(_A)
if mibBuilder.loadTexts:h3cUIMVoltage.setUnits('milli-volt')
class _H3cUIMProvider_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cUIMProvider_Type.__name__=_E
_H3cUIMProvider_Object=MibTableColumn
h3cUIMProvider=_H3cUIMProvider_Object((1,3,6,1,4,1,2011,10,2,98,1,2,1,1,6),_H3cUIMProvider_Type())
h3cUIMProvider.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMProvider.setStatus(_A)
class _H3cUIMSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31),ValueRangeConstraint(99,99))
_H3cUIMSignal_Type.__name__=_D
_H3cUIMSignal_Object=MibTableColumn
h3cUIMSignal=_H3cUIMSignal_Object((1,3,6,1,4,1,2011,10,2,98,1,2,1,1,7),_H3cUIMSignal_Type())
h3cUIMSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMSignal.setStatus(_A)
class _H3cUIMTryPinPukTimes_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3cUIMTryPinPukTimes_Type.__name__=_N
_H3cUIMTryPinPukTimes_Object=MibTableColumn
h3cUIMTryPinPukTimes=_H3cUIMTryPinPukTimes_Object((1,3,6,1,4,1,2011,10,2,98,1,2,1,1,8),_H3cUIMTryPinPukTimes_Type())
h3cUIMTryPinPukTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMTryPinPukTimes.setStatus(_A)
class _H3cUIMOldPin_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_H3cUIMOldPin_Type.__name__=_E
_H3cUIMOldPin_Object=MibTableColumn
h3cUIMOldPin=_H3cUIMOldPin_Object((1,3,6,1,4,1,2011,10,2,98,1,2,1,1,9),_H3cUIMOldPin_Type())
h3cUIMOldPin.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cUIMOldPin.setStatus(_A)
_H3c3GCdma_ObjectIdentity=ObjectIdentity
h3c3GCdma=_H3c3GCdma_ObjectIdentity((1,3,6,1,4,1,2011,10,2,98,1,3))
_H3c3GCdma1xRttTable_Object=MibTable
h3c3GCdma1xRttTable=_H3c3GCdma1xRttTable_Object((1,3,6,1,4,1,2011,10,2,98,1,3,1))
if mibBuilder.loadTexts:h3c3GCdma1xRttTable.setStatus(_A)
_H3c3GCdma1xRttEntry_Object=MibTableRow
h3c3GCdma1xRttEntry=_H3c3GCdma1xRttEntry_Object((1,3,6,1,4,1,2011,10,2,98,1,3,1,1))
h3c3GCdma1xRttEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3c3GCdma1xRttEntry.setStatus(_A)
class _H3c3GCdma1xRttCurrentRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,-2147483648),ValueRangeConstraint(-150,0))
_H3c3GCdma1xRttCurrentRssi_Type.__name__=_D
_H3c3GCdma1xRttCurrentRssi_Object=MibTableColumn
h3c3GCdma1xRttCurrentRssi=_H3c3GCdma1xRttCurrentRssi_Object((1,3,6,1,4,1,2011,10,2,98,1,3,1,1,1),_H3c3GCdma1xRttCurrentRssi_Type())
h3c3GCdma1xRttCurrentRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GCdma1xRttCurrentRssi.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCdma1xRttCurrentRssi.setUnits(_I)
class _H3c3GCdma1xRttRssiMediumThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GCdma1xRttRssiMediumThreshold_Type.__name__=_D
_H3c3GCdma1xRttRssiMediumThreshold_Object=MibTableColumn
h3c3GCdma1xRttRssiMediumThreshold=_H3c3GCdma1xRttRssiMediumThreshold_Object((1,3,6,1,4,1,2011,10,2,98,1,3,1,1,2),_H3c3GCdma1xRttRssiMediumThreshold_Type())
h3c3GCdma1xRttRssiMediumThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:h3c3GCdma1xRttRssiMediumThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCdma1xRttRssiMediumThreshold.setUnits(_I)
class _H3c3GCdma1xRttRssiWeakThreshold_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GCdma1xRttRssiWeakThreshold_Type.__name__=_D
_H3c3GCdma1xRttRssiWeakThreshold_Object=MibTableColumn
h3c3GCdma1xRttRssiWeakThreshold=_H3c3GCdma1xRttRssiWeakThreshold_Object((1,3,6,1,4,1,2011,10,2,98,1,3,1,1,3),_H3c3GCdma1xRttRssiWeakThreshold_Type())
h3c3GCdma1xRttRssiWeakThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:h3c3GCdma1xRttRssiWeakThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCdma1xRttRssiWeakThreshold.setUnits(_I)
class _H3c3GCdma1xRttCurServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_V,2),(_W,3),(_X,4),(_P,5)))
_H3c3GCdma1xRttCurServiceStatus_Type.__name__=_D
_H3c3GCdma1xRttCurServiceStatus_Object=MibTableColumn
h3c3GCdma1xRttCurServiceStatus=_H3c3GCdma1xRttCurServiceStatus_Object((1,3,6,1,4,1,2011,10,2,98,1,3,1,1,4),_H3c3GCdma1xRttCurServiceStatus_Type())
h3c3GCdma1xRttCurServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GCdma1xRttCurServiceStatus.setStatus(_A)
class _H3c3GCdma1xRttCurRoamingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_Y,2),(_Z,3)))
_H3c3GCdma1xRttCurRoamingStatus_Type.__name__=_D
_H3c3GCdma1xRttCurRoamingStatus_Object=MibTableColumn
h3c3GCdma1xRttCurRoamingStatus=_H3c3GCdma1xRttCurRoamingStatus_Object((1,3,6,1,4,1,2011,10,2,98,1,3,1,1,5),_H3c3GCdma1xRttCurRoamingStatus_Type())
h3c3GCdma1xRttCurRoamingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GCdma1xRttCurRoamingStatus.setStatus(_A)
class _H3c3GCdma1xRttBID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3c3GCdma1xRttBID_Type.__name__=_N
_H3c3GCdma1xRttBID_Object=MibTableColumn
h3c3GCdma1xRttBID=_H3c3GCdma1xRttBID_Object((1,3,6,1,4,1,2011,10,2,98,1,3,1,1,6),_H3c3GCdma1xRttBID_Type())
h3c3GCdma1xRttBID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GCdma1xRttBID.setStatus(_A)
class _H3c3GCdma1xRttSID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3c3GCdma1xRttSID_Type.__name__=_N
_H3c3GCdma1xRttSID_Object=MibTableColumn
h3c3GCdma1xRttSID=_H3c3GCdma1xRttSID_Object((1,3,6,1,4,1,2011,10,2,98,1,3,1,1,7),_H3c3GCdma1xRttSID_Type())
h3c3GCdma1xRttSID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GCdma1xRttSID.setStatus(_A)
class _H3c3GCdma1xRttNID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3c3GCdma1xRttNID_Type.__name__=_N
_H3c3GCdma1xRttNID_Object=MibTableColumn
h3c3GCdma1xRttNID=_H3c3GCdma1xRttNID_Object((1,3,6,1,4,1,2011,10,2,98,1,3,1,1,8),_H3c3GCdma1xRttNID_Type())
h3c3GCdma1xRttNID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GCdma1xRttNID.setStatus(_A)
_H3c3GCdmaEvDoTable_Object=MibTable
h3c3GCdmaEvDoTable=_H3c3GCdmaEvDoTable_Object((1,3,6,1,4,1,2011,10,2,98,1,3,2))
if mibBuilder.loadTexts:h3c3GCdmaEvDoTable.setStatus(_A)
_H3c3GCdmaEvDoEntry_Object=MibTableRow
h3c3GCdmaEvDoEntry=_H3c3GCdmaEvDoEntry_Object((1,3,6,1,4,1,2011,10,2,98,1,3,2,1))
h3c3GCdmaEvDoEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3c3GCdmaEvDoEntry.setStatus(_A)
class _H3c3GCdmaEvDoCurrentRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,-2147483648),ValueRangeConstraint(-150,0))
_H3c3GCdmaEvDoCurrentRssi_Type.__name__=_D
_H3c3GCdmaEvDoCurrentRssi_Object=MibTableColumn
h3c3GCdmaEvDoCurrentRssi=_H3c3GCdmaEvDoCurrentRssi_Object((1,3,6,1,4,1,2011,10,2,98,1,3,2,1,1),_H3c3GCdmaEvDoCurrentRssi_Type())
h3c3GCdmaEvDoCurrentRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GCdmaEvDoCurrentRssi.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCdmaEvDoCurrentRssi.setUnits(_I)
class _H3c3GCdmaEvDoRssiMediumThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GCdmaEvDoRssiMediumThreshold_Type.__name__=_D
_H3c3GCdmaEvDoRssiMediumThreshold_Object=MibTableColumn
h3c3GCdmaEvDoRssiMediumThreshold=_H3c3GCdmaEvDoRssiMediumThreshold_Object((1,3,6,1,4,1,2011,10,2,98,1,3,2,1,2),_H3c3GCdmaEvDoRssiMediumThreshold_Type())
h3c3GCdmaEvDoRssiMediumThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:h3c3GCdmaEvDoRssiMediumThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCdmaEvDoRssiMediumThreshold.setUnits(_I)
class _H3c3GCdmaEvDoRssiWeakThreshold_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GCdmaEvDoRssiWeakThreshold_Type.__name__=_D
_H3c3GCdmaEvDoRssiWeakThreshold_Object=MibTableColumn
h3c3GCdmaEvDoRssiWeakThreshold=_H3c3GCdmaEvDoRssiWeakThreshold_Object((1,3,6,1,4,1,2011,10,2,98,1,3,2,1,3),_H3c3GCdmaEvDoRssiWeakThreshold_Type())
h3c3GCdmaEvDoRssiWeakThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:h3c3GCdmaEvDoRssiWeakThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCdmaEvDoRssiWeakThreshold.setUnits(_I)
class _H3c3GCdmaEvDoCurServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_V,2),(_W,3),(_X,4),(_P,5)))
_H3c3GCdmaEvDoCurServiceStatus_Type.__name__=_D
_H3c3GCdmaEvDoCurServiceStatus_Object=MibTableColumn
h3c3GCdmaEvDoCurServiceStatus=_H3c3GCdmaEvDoCurServiceStatus_Object((1,3,6,1,4,1,2011,10,2,98,1,3,2,1,4),_H3c3GCdmaEvDoCurServiceStatus_Type())
h3c3GCdmaEvDoCurServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GCdmaEvDoCurServiceStatus.setStatus(_A)
class _H3c3GCdmaEvDoCurRoamingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_Y,2),(_Z,3)))
_H3c3GCdmaEvDoCurRoamingStatus_Type.__name__=_D
_H3c3GCdmaEvDoCurRoamingStatus_Object=MibTableColumn
h3c3GCdmaEvDoCurRoamingStatus=_H3c3GCdmaEvDoCurRoamingStatus_Object((1,3,6,1,4,1,2011,10,2,98,1,3,2,1,5),_H3c3GCdmaEvDoCurRoamingStatus_Type())
h3c3GCdmaEvDoCurRoamingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GCdmaEvDoCurRoamingStatus.setStatus(_A)
class _H3c3GCdmaEvDoSubNetID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3c3GCdmaEvDoSubNetID_Type.__name__=_E
_H3c3GCdmaEvDoSubNetID_Object=MibTableColumn
h3c3GCdmaEvDoSubNetID=_H3c3GCdmaEvDoSubNetID_Object((1,3,6,1,4,1,2011,10,2,98,1,3,2,1,6),_H3c3GCdmaEvDoSubNetID_Type())
h3c3GCdmaEvDoSubNetID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GCdmaEvDoSubNetID.setStatus(_A)
_H3c3GGsm_ObjectIdentity=ObjectIdentity
h3c3GGsm=_H3c3GGsm_ObjectIdentity((1,3,6,1,4,1,2011,10,2,98,1,4))
_H3c3GGsmInfoTable_Object=MibTable
h3c3GGsmInfoTable=_H3c3GGsmInfoTable_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1))
if mibBuilder.loadTexts:h3c3GGsmInfoTable.setStatus(_A)
_H3c3GGsmInfoEntry_Object=MibTableRow
h3c3GGsmInfoEntry=_H3c3GGsmInfoEntry_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1))
h3c3GGsmInfoEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3c3GGsmInfoEntry.setStatus(_A)
class _H3c3GGsmCurrentRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,-2147483648),ValueRangeConstraint(-150,0))
_H3c3GGsmCurrentRssi_Type.__name__=_D
_H3c3GGsmCurrentRssi_Object=MibTableColumn
h3c3GGsmCurrentRssi=_H3c3GGsmCurrentRssi_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,1),_H3c3GGsmCurrentRssi_Type())
h3c3GGsmCurrentRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmCurrentRssi.setStatus(_A)
if mibBuilder.loadTexts:h3c3GGsmCurrentRssi.setUnits(_I)
class _H3c3GGsmRssiMediumThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GGsmRssiMediumThreshold_Type.__name__=_D
_H3c3GGsmRssiMediumThreshold_Object=MibTableColumn
h3c3GGsmRssiMediumThreshold=_H3c3GGsmRssiMediumThreshold_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,2),_H3c3GGsmRssiMediumThreshold_Type())
h3c3GGsmRssiMediumThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:h3c3GGsmRssiMediumThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3c3GGsmRssiMediumThreshold.setUnits(_I)
class _H3c3GGsmRssiWeakThreshold_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GGsmRssiWeakThreshold_Type.__name__=_D
_H3c3GGsmRssiWeakThreshold_Object=MibTableColumn
h3c3GGsmRssiWeakThreshold=_H3c3GGsmRssiWeakThreshold_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,3),_H3c3GGsmRssiWeakThreshold_Type())
h3c3GGsmRssiWeakThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:h3c3GGsmRssiWeakThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3c3GGsmRssiWeakThreshold.setUnits(_I)
class _H3c3GGsmImsi_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3c3GGsmImsi_Type.__name__=_E
_H3c3GGsmImsi_Object=MibTableColumn
h3c3GGsmImsi=_H3c3GGsmImsi_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,4),_H3c3GGsmImsi_Type())
h3c3GGsmImsi.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmImsi.setStatus(_A)
class _H3c3GGsmImei_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3c3GGsmImei_Type.__name__=_E
_H3c3GGsmImei_Object=MibTableColumn
h3c3GGsmImei=_H3c3GGsmImei_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,5),_H3c3GGsmImei_Type())
h3c3GGsmImei.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmImei.setStatus(_A)
class _H3c3GGsmApn_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_H3c3GGsmApn_Type.__name__=_E
_H3c3GGsmApn_Object=MibTableColumn
h3c3GGsmApn=_H3c3GGsmApn_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,6),_H3c3GGsmApn_Type())
h3c3GGsmApn.setMaxAccess(_H)
if mibBuilder.loadTexts:h3c3GGsmApn.setStatus(_A)
class _H3c3GGsmPacketSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('active',2),('inactive',3)))
_H3c3GGsmPacketSessionStatus_Type.__name__=_D
_H3c3GGsmPacketSessionStatus_Object=MibTableColumn
h3c3GGsmPacketSessionStatus=_H3c3GGsmPacketSessionStatus_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,7),_H3c3GGsmPacketSessionStatus_Type())
h3c3GGsmPacketSessionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmPacketSessionStatus.setStatus(_A)
class _H3c3GGsmNetworkSelectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('automatic',2),('manual',3)))
_H3c3GGsmNetworkSelectionMode_Type.__name__=_D
_H3c3GGsmNetworkSelectionMode_Object=MibTableColumn
h3c3GGsmNetworkSelectionMode=_H3c3GGsmNetworkSelectionMode_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,8),_H3c3GGsmNetworkSelectionMode_Type())
h3c3GGsmNetworkSelectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmNetworkSelectionMode.setStatus(_A)
class _H3c3GGsmMobileNetworkName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3c3GGsmMobileNetworkName_Type.__name__=_E
_H3c3GGsmMobileNetworkName_Object=MibTableColumn
h3c3GGsmMobileNetworkName=_H3c3GGsmMobileNetworkName_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,9),_H3c3GGsmMobileNetworkName_Type())
h3c3GGsmMobileNetworkName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmMobileNetworkName.setStatus(_A)
class _H3c3GGsmLac_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3c3GGsmLac_Type.__name__=_E
_H3c3GGsmLac_Object=MibTableColumn
h3c3GGsmLac=_H3c3GGsmLac_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,10),_H3c3GGsmLac_Type())
h3c3GGsmLac.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmLac.setStatus(_A)
class _H3c3GGsmCellId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3c3GGsmCellId_Type.__name__=_E
_H3c3GGsmCellId_Object=MibTableColumn
h3c3GGsmCellId=_H3c3GGsmCellId_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,11),_H3c3GGsmCellId_Type())
h3c3GGsmCellId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmCellId.setStatus(_A)
class _H3c3GGsmSimStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('ok',2),('notInsert',3),('networkReject',4),('blocked',5)))
_H3c3GGsmSimStatus_Type.__name__=_D
_H3c3GGsmSimStatus_Object=MibTableColumn
h3c3GGsmSimStatus=_H3c3GGsmSimStatus_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,12),_H3c3GGsmSimStatus_Type())
h3c3GGsmSimStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmSimStatus.setStatus(_A)
class _H3c3GGsmCurServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_V,2),(_W,3),(_X,4),(_P,5)))
_H3c3GGsmCurServiceStatus_Type.__name__=_D
_H3c3GGsmCurServiceStatus_Object=MibTableColumn
h3c3GGsmCurServiceStatus=_H3c3GGsmCurServiceStatus_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,13),_H3c3GGsmCurServiceStatus_Type())
h3c3GGsmCurServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmCurServiceStatus.setStatus(_A)
class _H3c3GGsmCurRoamingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_Y,2),(_Z,3)))
_H3c3GGsmCurRoamingStatus_Type.__name__=_D
_H3c3GGsmCurRoamingStatus_Object=MibTableColumn
h3c3GGsmCurRoamingStatus=_H3c3GGsmCurRoamingStatus_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,14),_H3c3GGsmCurRoamingStatus_Type())
h3c3GGsmCurRoamingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmCurRoamingStatus.setStatus(_A)
class _H3c3GGsmMcc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3c3GGsmMcc_Type.__name__=_E
_H3c3GGsmMcc_Object=MibTableColumn
h3c3GGsmMcc=_H3c3GGsmMcc_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,15),_H3c3GGsmMcc_Type())
h3c3GGsmMcc.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmMcc.setStatus(_A)
class _H3c3GGsmMnc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3c3GGsmMnc_Type.__name__=_E
_H3c3GGsmMnc_Object=MibTableColumn
h3c3GGsmMnc=_H3c3GGsmMnc_Object((1,3,6,1,4,1,2011,10,2,98,1,4,1,1,16),_H3c3GGsmMnc_Type())
h3c3GGsmMnc.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmMnc.setStatus(_A)
_H3cLte_ObjectIdentity=ObjectIdentity
h3cLte=_H3cLte_ObjectIdentity((1,3,6,1,4,1,2011,10,2,98,1,5))
_H3cLteInfoTable_Object=MibTable
h3cLteInfoTable=_H3cLteInfoTable_Object((1,3,6,1,4,1,2011,10,2,98,1,5,1))
if mibBuilder.loadTexts:h3cLteInfoTable.setStatus(_A)
_H3cLteInfoEntry_Object=MibTableRow
h3cLteInfoEntry=_H3cLteInfoEntry_Object((1,3,6,1,4,1,2011,10,2,98,1,5,1,1))
h3cLteInfoEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3cLteInfoEntry.setStatus(_A)
_H3cLteCurrentRsrp_Type=Integer32
_H3cLteCurrentRsrp_Object=MibTableColumn
h3cLteCurrentRsrp=_H3cLteCurrentRsrp_Object((1,3,6,1,4,1,2011,10,2,98,1,5,1,1,1),_H3cLteCurrentRsrp_Type())
h3cLteCurrentRsrp.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLteCurrentRsrp.setStatus(_A)
if mibBuilder.loadTexts:h3cLteCurrentRsrp.setUnits(_I)
_H3cLteCurrentRsrq_Type=Integer32
_H3cLteCurrentRsrq_Object=MibTableColumn
h3cLteCurrentRsrq=_H3cLteCurrentRsrq_Object((1,3,6,1,4,1,2011,10,2,98,1,5,1,1,2),_H3cLteCurrentRsrq_Type())
h3cLteCurrentRsrq.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLteCurrentRsrq.setStatus(_A)
if mibBuilder.loadTexts:h3cLteCurrentRsrq.setUnits('dB')
_H3cLteCurrentSinr_Type=Integer32
_H3cLteCurrentSinr_Object=MibTableColumn
h3cLteCurrentSinr=_H3cLteCurrentSinr_Object((1,3,6,1,4,1,2011,10,2,98,1,5,1,1,3),_H3cLteCurrentSinr_Type())
h3cLteCurrentSinr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLteCurrentSinr.setStatus(_A)
if mibBuilder.loadTexts:h3cLteCurrentSinr.setUnits('dB')
_H3cLteTxPower_Type=Integer32
_H3cLteTxPower_Object=MibTableColumn
h3cLteTxPower=_H3cLteTxPower_Object((1,3,6,1,4,1,2011,10,2,98,1,5,1,1,4),_H3cLteTxPower_Type())
h3cLteTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLteTxPower.setStatus(_A)
if mibBuilder.loadTexts:h3cLteTxPower.setUnits('dB')
class _H3cLteCurrentRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,-2147483648),ValueRangeConstraint(-150,0))
_H3cLteCurrentRssi_Type.__name__=_D
_H3cLteCurrentRssi_Object=MibTableColumn
h3cLteCurrentRssi=_H3cLteCurrentRssi_Object((1,3,6,1,4,1,2011,10,2,98,1,5,1,1,5),_H3cLteCurrentRssi_Type())
h3cLteCurrentRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cLteCurrentRssi.setStatus(_A)
if mibBuilder.loadTexts:h3cLteCurrentRssi.setUnits(_I)
class _H3cLteRssiMediumThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3cLteRssiMediumThreshold_Type.__name__=_D
_H3cLteRssiMediumThreshold_Object=MibTableColumn
h3cLteRssiMediumThreshold=_H3cLteRssiMediumThreshold_Object((1,3,6,1,4,1,2011,10,2,98,1,5,1,1,6),_H3cLteRssiMediumThreshold_Type())
h3cLteRssiMediumThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cLteRssiMediumThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cLteRssiMediumThreshold.setUnits(_I)
class _H3cLteRssiWeakThreshold_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3cLteRssiWeakThreshold_Type.__name__=_D
_H3cLteRssiWeakThreshold_Object=MibTableColumn
h3cLteRssiWeakThreshold=_H3cLteRssiWeakThreshold_Object((1,3,6,1,4,1,2011,10,2,98,1,5,1,1,7),_H3cLteRssiWeakThreshold_Type())
h3cLteRssiWeakThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cLteRssiWeakThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cLteRssiWeakThreshold.setUnits(_I)
_H3c3GModemTrap_ObjectIdentity=ObjectIdentity
h3c3GModemTrap=_H3c3GModemTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,98,2))
class _H3cDevSerialNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cDevSerialNumber_Type.__name__=_E
_H3cDevSerialNumber_Object=MibScalar
h3cDevSerialNumber=_H3cDevSerialNumber_Object((1,3,6,1,4,1,2011,10,2,98,2,1),_H3cDevSerialNumber_Type())
h3cDevSerialNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDevSerialNumber.setStatus(_A)
class _H3cDeviceOUI_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cDeviceOUI_Type.__name__=_E
_H3cDeviceOUI_Object=MibScalar
h3cDeviceOUI=_H3cDeviceOUI_Object((1,3,6,1,4,1,2011,10,2,98,2,2),_H3cDeviceOUI_Type())
h3cDeviceOUI.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDeviceOUI.setStatus(_A)
class _H3cAccessMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('air',2),('cable',3)))
_H3cAccessMedia_Type.__name__=_D
_H3cAccessMedia_Object=MibScalar
h3cAccessMedia=_H3cAccessMedia_Object((1,3,6,1,4,1,2011,10,2,98,2,3),_H3cAccessMedia_Type())
h3cAccessMedia.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cAccessMedia.setStatus(_A)
class _H3c3GCurrentService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('oneXRtt',2),('evDo',3),('gsm',4),(_U,5)))
_H3c3GCurrentService_Type.__name__=_D
_H3c3GCurrentService_Object=MibScalar
h3c3GCurrentService=_H3c3GCurrentService_Object((1,3,6,1,4,1,2011,10,2,98,2,4),_H3c3GCurrentService_Type())
h3c3GCurrentService.setMaxAccess(_J)
if mibBuilder.loadTexts:h3c3GCurrentService.setStatus(_A)
class _H3c3GCurrentRssiBind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,-2147483648),ValueRangeConstraint(-150,0))
_H3c3GCurrentRssiBind_Type.__name__=_D
_H3c3GCurrentRssiBind_Object=MibScalar
h3c3GCurrentRssiBind=_H3c3GCurrentRssiBind_Object((1,3,6,1,4,1,2011,10,2,98,2,5),_H3c3GCurrentRssiBind_Type())
h3c3GCurrentRssiBind.setMaxAccess(_J)
if mibBuilder.loadTexts:h3c3GCurrentRssiBind.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCurrentRssiBind.setUnits(_I)
class _H3c3GImsiBind_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3c3GImsiBind_Type.__name__=_E
_H3c3GImsiBind_Object=MibScalar
h3c3GImsiBind=_H3c3GImsiBind_Object((1,3,6,1,4,1,2011,10,2,98,2,6),_H3c3GImsiBind_Type())
h3c3GImsiBind.setMaxAccess(_J)
if mibBuilder.loadTexts:h3c3GImsiBind.setStatus(_A)
class _H3cSmsSrcNumberBind_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_H3cSmsSrcNumberBind_Type.__name__=_E
_H3cSmsSrcNumberBind_Object=MibScalar
h3cSmsSrcNumberBind=_H3cSmsSrcNumberBind_Object((1,3,6,1,4,1,2011,10,2,98,2,7),_H3cSmsSrcNumberBind_Type())
h3cSmsSrcNumberBind.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cSmsSrcNumberBind.setStatus(_A)
class _H3cSmsTimeBind_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_H3cSmsTimeBind_Type.__name__=_E
_H3cSmsTimeBind_Object=MibScalar
h3cSmsTimeBind=_H3cSmsTimeBind_Object((1,3,6,1,4,1,2011,10,2,98,2,8),_H3cSmsTimeBind_Type())
h3cSmsTimeBind.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cSmsTimeBind.setStatus(_A)
_H3cSmsEncodeBind_Type=H3cSmsEncodeType
_H3cSmsEncodeBind_Object=MibScalar
h3cSmsEncodeBind=_H3cSmsEncodeBind_Object((1,3,6,1,4,1,2011,10,2,98,2,9),_H3cSmsEncodeBind_Type())
h3cSmsEncodeBind.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cSmsEncodeBind.setStatus(_A)
class _H3cSmsContentBind_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_H3cSmsContentBind_Type.__name__=_T
_H3cSmsContentBind_Object=MibScalar
h3cSmsContentBind=_H3cSmsContentBind_Object((1,3,6,1,4,1,2011,10,2,98,2,10),_H3cSmsContentBind_Type())
h3cSmsContentBind.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cSmsContentBind.setStatus(_A)
_H3c3GModemTraps_ObjectIdentity=ObjectIdentity
h3c3GModemTraps=_H3c3GModemTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,98,3))
_H3c3GModemTrapPrefix_ObjectIdentity=ObjectIdentity
h3c3GModemTrapPrefix=_H3c3GModemTrapPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,98,3,0))
h3cWirelessCardInserted=NotificationType((1,3,6,1,4,1,2011,10,2,98,3,0,1))
h3cWirelessCardInserted.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:h3cWirelessCardInserted.setStatus(_A)
h3cWirelessCardPulledOut=NotificationType((1,3,6,1,4,1,2011,10,2,98,3,0,2))
h3cWirelessCardPulledOut.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:h3cWirelessCardPulledOut.setStatus(_A)
h3cUIMPinInvalid=NotificationType((1,3,6,1,4,1,2011,10,2,98,3,0,3))
h3cUIMPinInvalid.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:h3cUIMPinInvalid.setStatus(_A)
h3cUIMPinChanged=NotificationType((1,3,6,1,4,1,2011,10,2,98,3,0,4))
h3cUIMPinChanged.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_O),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:h3cUIMPinChanged.setStatus(_A)
h3cAccessMediaChanged=NotificationType((1,3,6,1,4,1,2011,10,2,98,3,0,5))
h3cAccessMediaChanged.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_O),(_B,_h)))
if mibBuilder.loadTexts:h3cAccessMediaChanged.setStatus(_A)
h3c3GRssiStrongSignalTrap=NotificationType((1,3,6,1,4,1,2011,10,2,98,3,0,6))
h3c3GRssiStrongSignalTrap.setObjects(*((_B,_G),(_B,_K),(_B,_L),(_B,_M),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:h3c3GRssiStrongSignalTrap.setStatus(_A)
h3c3GRssiMediumSignalTrap=NotificationType((1,3,6,1,4,1,2011,10,2,98,3,0,7))
h3c3GRssiMediumSignalTrap.setObjects(*((_B,_G),(_B,_K),(_B,_L),(_B,_M),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:h3c3GRssiMediumSignalTrap.setStatus(_A)
h3c3GRssiWeakSignalTrap=NotificationType((1,3,6,1,4,1,2011,10,2,98,3,0,8))
h3c3GRssiWeakSignalTrap.setObjects(*((_B,_G),(_B,_K),(_B,_L),(_B,_M),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:h3c3GRssiWeakSignalTrap.setStatus(_A)
h3cSmsTxNotification=NotificationType((1,3,6,1,4,1,2011,10,2,98,3,0,9))
h3cSmsTxNotification.setObjects(*((_B,_G),(_B,_i)))
if mibBuilder.loadTexts:h3cSmsTxNotification.setStatus(_A)
h3cSmsRxNotification=NotificationType((1,3,6,1,4,1,2011,10,2,98,3,0,10))
h3cSmsRxNotification.setObjects(*((_B,_G),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:h3cSmsRxNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'H3cUIMStatusType':H3cUIMStatusType,_b:H3cSmsEncodeType,'h3c3GModem':h3c3GModem,'h3c3GModemObjects':h3c3GModemObjects,'h3cWirelessCard':h3cWirelessCard,'h3cWirelessCardTable':h3cWirelessCardTable,'h3cWirelessCardEntry':h3cWirelessCardEntry,_G:h3cWirelessCardIndex,'h3cWirelessCardModelName':h3cWirelessCardModelName,'h3cWirelessCardMfgName':h3cWirelessCardMfgName,'h3cWirelessCardDescription':h3cWirelessCardDescription,_M:h3cWirelessCardSerialNumber,'h3cWirelessCardCMIIID':h3cWirelessCardCMIIID,'h3cWirelessCardHardwareVersion':h3cWirelessCardHardwareVersion,'h3cWirelessCardFirmwareVersion':h3cWirelessCardFirmwareVersion,'h3cWirelessCardPRLVersion':h3cWirelessCardPRLVersion,'h3cWirelessCardInterfaceIndex':h3cWirelessCardInterfaceIndex,'h3cWirelessCardModemStatus':h3cWirelessCardModemStatus,'h3cWirelessCardModemMode':h3cWirelessCardModemMode,'h3cWirelessCardCurNetConn':h3cWirelessCardCurNetConn,'h3cSmsGroup':h3cSmsGroup,'h3cSmsScalarObjects':h3cSmsScalarObjects,'h3cSmsRxNotifSwitch':h3cSmsRxNotifSwitch,'h3cSmsOperationTable':h3cSmsOperationTable,'h3cSmsOperationEntry':h3cSmsOperationEntry,'h3cSmsDestNumber':h3cSmsDestNumber,'h3cSmsEncode':h3cSmsEncode,'h3cSmsContent':h3cSmsContent,_i:h3cSmsSendStatus,'h3cWirelessCardOnlineTable':h3cWirelessCardOnlineTable,'h3cWirelessCardOnlineEntry':h3cWirelessCardOnlineEntry,_c:h3cWirelessCardOnlineTime,'h3cWirelessCardOnlineType':h3cWirelessCardOnlineType,'h3cUIM':h3cUIM,'h3cUIMInfoTable':h3cUIMInfoTable,'h3cUIMInfoEntry':h3cUIMInfoEntry,_e:h3cUIMIndex,'h3cUIMStatus':h3cUIMStatus,_O:h3cUIMImsi,_g:h3cUIMPin,'h3cUIMVoltage':h3cUIMVoltage,'h3cUIMProvider':h3cUIMProvider,'h3cUIMSignal':h3cUIMSignal,'h3cUIMTryPinPukTimes':h3cUIMTryPinPukTimes,_f:h3cUIMOldPin,'h3c3GCdma':h3c3GCdma,'h3c3GCdma1xRttTable':h3c3GCdma1xRttTable,'h3c3GCdma1xRttEntry':h3c3GCdma1xRttEntry,'h3c3GCdma1xRttCurrentRssi':h3c3GCdma1xRttCurrentRssi,'h3c3GCdma1xRttRssiMediumThreshold':h3c3GCdma1xRttRssiMediumThreshold,'h3c3GCdma1xRttRssiWeakThreshold':h3c3GCdma1xRttRssiWeakThreshold,'h3c3GCdma1xRttCurServiceStatus':h3c3GCdma1xRttCurServiceStatus,'h3c3GCdma1xRttCurRoamingStatus':h3c3GCdma1xRttCurRoamingStatus,'h3c3GCdma1xRttBID':h3c3GCdma1xRttBID,'h3c3GCdma1xRttSID':h3c3GCdma1xRttSID,'h3c3GCdma1xRttNID':h3c3GCdma1xRttNID,'h3c3GCdmaEvDoTable':h3c3GCdmaEvDoTable,'h3c3GCdmaEvDoEntry':h3c3GCdmaEvDoEntry,'h3c3GCdmaEvDoCurrentRssi':h3c3GCdmaEvDoCurrentRssi,'h3c3GCdmaEvDoRssiMediumThreshold':h3c3GCdmaEvDoRssiMediumThreshold,'h3c3GCdmaEvDoRssiWeakThreshold':h3c3GCdmaEvDoRssiWeakThreshold,'h3c3GCdmaEvDoCurServiceStatus':h3c3GCdmaEvDoCurServiceStatus,'h3c3GCdmaEvDoCurRoamingStatus':h3c3GCdmaEvDoCurRoamingStatus,'h3c3GCdmaEvDoSubNetID':h3c3GCdmaEvDoSubNetID,'h3c3GGsm':h3c3GGsm,'h3c3GGsmInfoTable':h3c3GGsmInfoTable,'h3c3GGsmInfoEntry':h3c3GGsmInfoEntry,'h3c3GGsmCurrentRssi':h3c3GGsmCurrentRssi,'h3c3GGsmRssiMediumThreshold':h3c3GGsmRssiMediumThreshold,'h3c3GGsmRssiWeakThreshold':h3c3GGsmRssiWeakThreshold,'h3c3GGsmImsi':h3c3GGsmImsi,'h3c3GGsmImei':h3c3GGsmImei,'h3c3GGsmApn':h3c3GGsmApn,'h3c3GGsmPacketSessionStatus':h3c3GGsmPacketSessionStatus,'h3c3GGsmNetworkSelectionMode':h3c3GGsmNetworkSelectionMode,'h3c3GGsmMobileNetworkName':h3c3GGsmMobileNetworkName,'h3c3GGsmLac':h3c3GGsmLac,'h3c3GGsmCellId':h3c3GGsmCellId,'h3c3GGsmSimStatus':h3c3GGsmSimStatus,'h3c3GGsmCurServiceStatus':h3c3GGsmCurServiceStatus,'h3c3GGsmCurRoamingStatus':h3c3GGsmCurRoamingStatus,'h3c3GGsmMcc':h3c3GGsmMcc,'h3c3GGsmMnc':h3c3GGsmMnc,'h3cLte':h3cLte,'h3cLteInfoTable':h3cLteInfoTable,'h3cLteInfoEntry':h3cLteInfoEntry,'h3cLteCurrentRsrp':h3cLteCurrentRsrp,'h3cLteCurrentRsrq':h3cLteCurrentRsrq,'h3cLteCurrentSinr':h3cLteCurrentSinr,'h3cLteTxPower':h3cLteTxPower,'h3cLteCurrentRssi':h3cLteCurrentRssi,'h3cLteRssiMediumThreshold':h3cLteRssiMediumThreshold,'h3cLteRssiWeakThreshold':h3cLteRssiWeakThreshold,'h3c3GModemTrap':h3c3GModemTrap,_L:h3cDevSerialNumber,_K:h3cDeviceOUI,_h:h3cAccessMedia,_Q:h3c3GCurrentService,_R:h3c3GCurrentRssiBind,_S:h3c3GImsiBind,_j:h3cSmsSrcNumberBind,_k:h3cSmsTimeBind,_l:h3cSmsEncodeBind,_m:h3cSmsContentBind,'h3c3GModemTraps':h3c3GModemTraps,'h3c3GModemTrapPrefix':h3c3GModemTrapPrefix,'h3cWirelessCardInserted':h3cWirelessCardInserted,'h3cWirelessCardPulledOut':h3cWirelessCardPulledOut,'h3cUIMPinInvalid':h3cUIMPinInvalid,'h3cUIMPinChanged':h3cUIMPinChanged,'h3cAccessMediaChanged':h3cAccessMediaChanged,'h3c3GRssiStrongSignalTrap':h3c3GRssiStrongSignalTrap,'h3c3GRssiMediumSignalTrap':h3c3GRssiMediumSignalTrap,'h3c3GRssiWeakSignalTrap':h3c3GRssiWeakSignalTrap,'h3cSmsTxNotification':h3cSmsTxNotification,'h3cSmsRxNotification':h3cSmsRxNotification})