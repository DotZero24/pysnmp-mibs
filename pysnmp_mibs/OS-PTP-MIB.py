_n='osPtpNotificationsGroup'
_m='osPtpMibMandatoryGroup'
_l='osPtpMIBSlaveAlarm'
_k='osPtpSlaveOutClkFrequency'
_j='osPtpSlaveDomainIndex'
_i='osPtpSlaveDirection'
_h='osPtpSlavePortTxMode'
_g='osPtpSlaveTodUartBaudRate'
_f='osPtpSlaveSyncInterval'
_e='osPtpSlaveAnnounceInterval'
_d='osPtpSlaveDelayRequestInterval'
_c='osPtpSlaveDirectMasterAddress'
_b='osPtpSlaveDirectMasterOnly'
_a='osPtpSlavePortAddress'
_Z='osPtpSlavePortAddrPrefixLength'
_Y='osPtpSlaveAddressType'
_X='osPtpSlaveGatewayAddress'
_W='osPtpSlavePortVifName'
_V='osPtpSlaveAdminStatus'
_U='osPtpSlaveNumOfDirectMasterRows'
_T='osPtpSlaveAddressTypesSupported'
_S='osPtpSlaveSupported'
_R='osPtpSlaveDirectMasterId'
_Q='ClockDomainType'
_P='ClockTxModeType'
_O='TruthValue'
_N='InetAddressType'
_M='InetAddressPrefixLength'
_L='InetAddress'
_K='osPtpSlaveEventDescription'
_J='osPtpSlaveEventReason'
_I='osPtpSlaveLastEvent'
_H='DisplayString'
_G='ClockIntervalBase2'
_F='unknown'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='OS-PTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_L,_M,_N)
oaOptiSwitch,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention',_O)
osPtpMIB=ModuleIdentity((1,3,6,1,4,1,6926,2,22))
if mibBuilder.loadTexts:osPtpMIB.setRevisions(('2012-08-08 00:00',))
class ClockDomainType(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class ClockIntervalBase2(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
class ClockStateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),('freerun',1),('holdover',2),('acquiring',3),('frequencyLocked',4),('phaseAligned',5)))
class ClockTxModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),('unicast',1),('multicast',2),('multicastmix',3)))
_OsPtpMIBNotifications_ObjectIdentity=ObjectIdentity
osPtpMIBNotifications=_OsPtpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6926,2,22,0))
_OsPtpMIBObjects_ObjectIdentity=ObjectIdentity
osPtpMIBObjects=_OsPtpMIBObjects_ObjectIdentity((1,3,6,1,4,1,6926,2,22,1))
_OsPtpMIBInfo_ObjectIdentity=ObjectIdentity
osPtpMIBInfo=_OsPtpMIBInfo_ObjectIdentity((1,3,6,1,4,1,6926,2,22,1,2))
_OsPtpMIBEventParams_ObjectIdentity=ObjectIdentity
osPtpMIBEventParams=_OsPtpMIBEventParams_ObjectIdentity((1,3,6,1,4,1,6926,2,22,1,2,1))
class _OsPtpSlaveLastEvent_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*(('none',0),('inHoldover',1),('noCurrentMaster',2),('noClockInput',3),('noTimeOfDayInput',4),('toPSyncTimeNotTAI',5),('ptpPortNotOperational',6),('visibleMasterRefusedSyncGrantRequest',7),('visibleMasterIgnoredSyncGrantRequest',8),('visibleMasterRefusedDlyRespGrantRequest',9),('visibleMasterIgnoredDlyRespGrantRequest',10),('visibleMasterTooFewSyncMessages',11),('visibleMasterTooFewFollowUpMessages',12),('visibleMasterTooFewDelayResponseMessages',13),('accMasterRefusedAnnounceGrantRequest',14),('accMasterIgnoredAnnounceGrantRequest',15),('acceptableMasterTooFewAnnounceMessages',16),('currentMasterTooManySyncsWithoutFollowUp',17),('currentMasterTooManyFollowUpsWithoutSync',18),('currentMasterTooManyMissingDlyResponses',19),('m2SPacketDelayVaration',20),('s2MPacketDelayVaration',21),('toPSyncUTCOffsetUnknown',22)))
_OsPtpSlaveLastEvent_Type.__name__=_D
_OsPtpSlaveLastEvent_Object=MibScalar
osPtpSlaveLastEvent=_OsPtpSlaveLastEvent_Object((1,3,6,1,4,1,6926,2,22,1,2,1,1),_OsPtpSlaveLastEvent_Type())
osPtpSlaveLastEvent.setMaxAccess(_E)
if mibBuilder.loadTexts:osPtpSlaveLastEvent.setStatus(_A)
class _OsPtpSlaveEventReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alarmSet',1),('alarmClear',2)))
_OsPtpSlaveEventReason_Type.__name__=_D
_OsPtpSlaveEventReason_Object=MibScalar
osPtpSlaveEventReason=_OsPtpSlaveEventReason_Object((1,3,6,1,4,1,6926,2,22,1,2,1,2),_OsPtpSlaveEventReason_Type())
osPtpSlaveEventReason.setMaxAccess(_E)
if mibBuilder.loadTexts:osPtpSlaveEventReason.setStatus(_A)
class _OsPtpSlaveEventDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,120))
_OsPtpSlaveEventDescription_Type.__name__=_H
_OsPtpSlaveEventDescription_Object=MibScalar
osPtpSlaveEventDescription=_OsPtpSlaveEventDescription_Object((1,3,6,1,4,1,6926,2,22,1,2,1,3),_OsPtpSlaveEventDescription_Type())
osPtpSlaveEventDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:osPtpSlaveEventDescription.setStatus(_A)
_OsPtpMIBSlaveInfo_ObjectIdentity=ObjectIdentity
osPtpMIBSlaveInfo=_OsPtpMIBSlaveInfo_ObjectIdentity((1,3,6,1,4,1,6926,2,22,1,2,2))
_OsPtpMIBCfg_ObjectIdentity=ObjectIdentity
osPtpMIBCfg=_OsPtpMIBCfg_ObjectIdentity((1,3,6,1,4,1,6926,2,22,1,3))
_OsPtpMIBSlaveCfg_ObjectIdentity=ObjectIdentity
osPtpMIBSlaveCfg=_OsPtpMIBSlaveCfg_ObjectIdentity((1,3,6,1,4,1,6926,2,22,1,3,2))
_OsPtpMIBSlaveCfgGen_ObjectIdentity=ObjectIdentity
osPtpMIBSlaveCfgGen=_OsPtpMIBSlaveCfgGen_ObjectIdentity((1,3,6,1,4,1,6926,2,22,1,3,2,1))
class _OsPtpSlaveAdminStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('clear',2),('enabled',3),('disabled',4)))
_OsPtpSlaveAdminStatus_Type.__name__=_D
_OsPtpSlaveAdminStatus_Object=MibScalar
osPtpSlaveAdminStatus=_OsPtpSlaveAdminStatus_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,1),_OsPtpSlaveAdminStatus_Type())
osPtpSlaveAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlaveAdminStatus.setStatus(_A)
class _OsPtpSlavePortVifName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_OsPtpSlavePortVifName_Type.__name__=_H
_OsPtpSlavePortVifName_Object=MibScalar
osPtpSlavePortVifName=_OsPtpSlavePortVifName_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,2),_OsPtpSlavePortVifName_Type())
osPtpSlavePortVifName.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlavePortVifName.setStatus(_A)
class _OsPtpSlaveAddressType_Type(InetAddressType):defaultValue=1
_OsPtpSlaveAddressType_Type.__name__=_N
_OsPtpSlaveAddressType_Object=MibScalar
osPtpSlaveAddressType=_OsPtpSlaveAddressType_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,3),_OsPtpSlaveAddressType_Type())
osPtpSlaveAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlaveAddressType.setStatus(_A)
class _OsPtpSlaveGatewayAddress_Type(InetAddress):defaultValue=OctetString('')
_OsPtpSlaveGatewayAddress_Type.__name__=_L
_OsPtpSlaveGatewayAddress_Object=MibScalar
osPtpSlaveGatewayAddress=_OsPtpSlaveGatewayAddress_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,4),_OsPtpSlaveGatewayAddress_Type())
osPtpSlaveGatewayAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlaveGatewayAddress.setStatus(_A)
class _OsPtpSlavePortAddrPrefixLength_Type(InetAddressPrefixLength):defaultValue=24
_OsPtpSlavePortAddrPrefixLength_Type.__name__=_M
_OsPtpSlavePortAddrPrefixLength_Object=MibScalar
osPtpSlavePortAddrPrefixLength=_OsPtpSlavePortAddrPrefixLength_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,5),_OsPtpSlavePortAddrPrefixLength_Type())
osPtpSlavePortAddrPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlavePortAddrPrefixLength.setStatus(_A)
_OsPtpSlavePortAddress_Type=InetAddress
_OsPtpSlavePortAddress_Object=MibScalar
osPtpSlavePortAddress=_OsPtpSlavePortAddress_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,6),_OsPtpSlavePortAddress_Type())
osPtpSlavePortAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlavePortAddress.setStatus(_A)
class _OsPtpSlaveDelayRequestInterval_Type(ClockIntervalBase2):defaultValue=-5
_OsPtpSlaveDelayRequestInterval_Type.__name__=_G
_OsPtpSlaveDelayRequestInterval_Object=MibScalar
osPtpSlaveDelayRequestInterval=_OsPtpSlaveDelayRequestInterval_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,10),_OsPtpSlaveDelayRequestInterval_Type())
osPtpSlaveDelayRequestInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlaveDelayRequestInterval.setStatus(_A)
class _OsPtpSlaveAnnounceInterval_Type(ClockIntervalBase2):defaultValue=1
_OsPtpSlaveAnnounceInterval_Type.__name__=_G
_OsPtpSlaveAnnounceInterval_Object=MibScalar
osPtpSlaveAnnounceInterval=_OsPtpSlaveAnnounceInterval_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,11),_OsPtpSlaveAnnounceInterval_Type())
osPtpSlaveAnnounceInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlaveAnnounceInterval.setStatus(_A)
class _OsPtpSlaveSyncInterval_Type(ClockIntervalBase2):defaultValue=-5
_OsPtpSlaveSyncInterval_Type.__name__=_G
_OsPtpSlaveSyncInterval_Object=MibScalar
osPtpSlaveSyncInterval=_OsPtpSlaveSyncInterval_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,12),_OsPtpSlaveSyncInterval_Type())
osPtpSlaveSyncInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlaveSyncInterval.setStatus(_A)
class _OsPtpSlaveTodUartBaudRate_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_F,0),('none',1),('baud1200',2),('baud2400',3),('baud4800',4),('baud9600',5),('baud19200',6)))
_OsPtpSlaveTodUartBaudRate_Type.__name__=_D
_OsPtpSlaveTodUartBaudRate_Object=MibScalar
osPtpSlaveTodUartBaudRate=_OsPtpSlaveTodUartBaudRate_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,20),_OsPtpSlaveTodUartBaudRate_Type())
osPtpSlaveTodUartBaudRate.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlaveTodUartBaudRate.setStatus(_A)
class _OsPtpSlavePortTxMode_Type(ClockTxModeType):defaultValue=1
_OsPtpSlavePortTxMode_Type.__name__=_P
_OsPtpSlavePortTxMode_Object=MibScalar
osPtpSlavePortTxMode=_OsPtpSlavePortTxMode_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,21),_OsPtpSlavePortTxMode_Type())
osPtpSlavePortTxMode.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlavePortTxMode.setStatus(_A)
class _OsPtpSlaveDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),('both',1),('slaveToMaster',2),('masterToSlave',3)))
_OsPtpSlaveDirection_Type.__name__=_D
_OsPtpSlaveDirection_Object=MibScalar
osPtpSlaveDirection=_OsPtpSlaveDirection_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,22),_OsPtpSlaveDirection_Type())
osPtpSlaveDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlaveDirection.setStatus(_A)
class _OsPtpSlaveDomainIndex_Type(ClockDomainType):defaultValue=0
_OsPtpSlaveDomainIndex_Type.__name__=_Q
_OsPtpSlaveDomainIndex_Object=MibScalar
osPtpSlaveDomainIndex=_OsPtpSlaveDomainIndex_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,23),_OsPtpSlaveDomainIndex_Type())
osPtpSlaveDomainIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlaveDomainIndex.setStatus(_A)
class _OsPtpSlaveOutClkFrequency_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,170000))
_OsPtpSlaveOutClkFrequency_Type.__name__=_D
_OsPtpSlaveOutClkFrequency_Object=MibScalar
osPtpSlaveOutClkFrequency=_OsPtpSlaveOutClkFrequency_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,24),_OsPtpSlaveOutClkFrequency_Type())
osPtpSlaveOutClkFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlaveOutClkFrequency.setStatus(_A)
class _OsPtpSlaveDirectMasterOnly_Type(TruthValue):defaultValue=2
_OsPtpSlaveDirectMasterOnly_Type.__name__=_O
_OsPtpSlaveDirectMasterOnly_Object=MibScalar
osPtpSlaveDirectMasterOnly=_OsPtpSlaveDirectMasterOnly_Object((1,3,6,1,4,1,6926,2,22,1,3,2,1,30),_OsPtpSlaveDirectMasterOnly_Type())
osPtpSlaveDirectMasterOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlaveDirectMasterOnly.setStatus(_A)
_OsPtpMIBSlaveCfgTbl_ObjectIdentity=ObjectIdentity
osPtpMIBSlaveCfgTbl=_OsPtpMIBSlaveCfgTbl_ObjectIdentity((1,3,6,1,4,1,6926,2,22,1,3,2,2))
_OsPtpSlaveDirectMasterTable_Object=MibTable
osPtpSlaveDirectMasterTable=_OsPtpSlaveDirectMasterTable_Object((1,3,6,1,4,1,6926,2,22,1,3,2,2,1))
if mibBuilder.loadTexts:osPtpSlaveDirectMasterTable.setStatus(_A)
_OsPtpSlaveDirectMasterEntry_Object=MibTableRow
osPtpSlaveDirectMasterEntry=_OsPtpSlaveDirectMasterEntry_Object((1,3,6,1,4,1,6926,2,22,1,3,2,2,1,1))
osPtpSlaveDirectMasterEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:osPtpSlaveDirectMasterEntry.setStatus(_A)
class _OsPtpSlaveDirectMasterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OsPtpSlaveDirectMasterId_Type.__name__=_D
_OsPtpSlaveDirectMasterId_Object=MibTableColumn
osPtpSlaveDirectMasterId=_OsPtpSlaveDirectMasterId_Object((1,3,6,1,4,1,6926,2,22,1,3,2,2,1,1,1),_OsPtpSlaveDirectMasterId_Type())
osPtpSlaveDirectMasterId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:osPtpSlaveDirectMasterId.setStatus(_A)
_OsPtpSlaveDirectMasterAddress_Type=InetAddress
_OsPtpSlaveDirectMasterAddress_Object=MibTableColumn
osPtpSlaveDirectMasterAddress=_OsPtpSlaveDirectMasterAddress_Object((1,3,6,1,4,1,6926,2,22,1,3,2,2,1,1,2),_OsPtpSlaveDirectMasterAddress_Type())
osPtpSlaveDirectMasterAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:osPtpSlaveDirectMasterAddress.setStatus(_A)
_OsPtpMIBCapabilities_ObjectIdentity=ObjectIdentity
osPtpMIBCapabilities=_OsPtpMIBCapabilities_ObjectIdentity((1,3,6,1,4,1,6926,2,22,3))
_OsPtpSlaveSupported_Type=TruthValue
_OsPtpSlaveSupported_Object=MibScalar
osPtpSlaveSupported=_OsPtpSlaveSupported_Object((1,3,6,1,4,1,6926,2,22,3,1),_OsPtpSlaveSupported_Type())
osPtpSlaveSupported.setMaxAccess(_E)
if mibBuilder.loadTexts:osPtpSlaveSupported.setStatus(_A)
class _OsPtpSlaveAddressTypesSupported_Type(Bits):namedValues=NamedValues(*(('ipv4',0),('ipv6',1),('ipv4z',2),('ipv6z',3)))
_OsPtpSlaveAddressTypesSupported_Type.__name__='Bits'
_OsPtpSlaveAddressTypesSupported_Object=MibScalar
osPtpSlaveAddressTypesSupported=_OsPtpSlaveAddressTypesSupported_Object((1,3,6,1,4,1,6926,2,22,3,2),_OsPtpSlaveAddressTypesSupported_Type())
osPtpSlaveAddressTypesSupported.setMaxAccess(_E)
if mibBuilder.loadTexts:osPtpSlaveAddressTypesSupported.setStatus(_A)
_OsPtpSlaveNumOfDirectMasterRows_Type=Unsigned32
_OsPtpSlaveNumOfDirectMasterRows_Object=MibScalar
osPtpSlaveNumOfDirectMasterRows=_OsPtpSlaveNumOfDirectMasterRows_Object((1,3,6,1,4,1,6926,2,22,3,3),_OsPtpSlaveNumOfDirectMasterRows_Type())
osPtpSlaveNumOfDirectMasterRows.setMaxAccess(_E)
if mibBuilder.loadTexts:osPtpSlaveNumOfDirectMasterRows.setStatus(_A)
if mibBuilder.loadTexts:osPtpSlaveNumOfDirectMasterRows.setUnits('rows')
_OsPtpMIBConformance_ObjectIdentity=ObjectIdentity
osPtpMIBConformance=_OsPtpMIBConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,22,100))
_OsPtpMIBCompliances_ObjectIdentity=ObjectIdentity
osPtpMIBCompliances=_OsPtpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,22,100,1))
_OsPtpMIBGroups_ObjectIdentity=ObjectIdentity
osPtpMIBGroups=_OsPtpMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,22,100,2))
osPtpMibMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,22,100,2,1))
osPtpMibMandatoryGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:osPtpMibMandatoryGroup.setStatus(_A)
osPtpMIBSlaveAlarm=NotificationType((1,3,6,1,4,1,6926,2,22,0,1))
osPtpMIBSlaveAlarm.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:osPtpMIBSlaveAlarm.setStatus(_A)
osPtpNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6926,2,22,100,2,2))
osPtpNotificationsGroup.setObjects((_B,_l))
if mibBuilder.loadTexts:osPtpNotificationsGroup.setStatus(_A)
osPtpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,22,100,1,1))
osPtpMIBCompliance.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:osPtpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_Q:ClockDomainType,_G:ClockIntervalBase2,'ClockStateType':ClockStateType,_P:ClockTxModeType,'osPtpMIB':osPtpMIB,'osPtpMIBNotifications':osPtpMIBNotifications,_l:osPtpMIBSlaveAlarm,'osPtpMIBObjects':osPtpMIBObjects,'osPtpMIBInfo':osPtpMIBInfo,'osPtpMIBEventParams':osPtpMIBEventParams,_I:osPtpSlaveLastEvent,_J:osPtpSlaveEventReason,_K:osPtpSlaveEventDescription,'osPtpMIBSlaveInfo':osPtpMIBSlaveInfo,'osPtpMIBCfg':osPtpMIBCfg,'osPtpMIBSlaveCfg':osPtpMIBSlaveCfg,'osPtpMIBSlaveCfgGen':osPtpMIBSlaveCfgGen,_V:osPtpSlaveAdminStatus,_W:osPtpSlavePortVifName,_Y:osPtpSlaveAddressType,_X:osPtpSlaveGatewayAddress,_Z:osPtpSlavePortAddrPrefixLength,_a:osPtpSlavePortAddress,_d:osPtpSlaveDelayRequestInterval,_e:osPtpSlaveAnnounceInterval,_f:osPtpSlaveSyncInterval,_g:osPtpSlaveTodUartBaudRate,_h:osPtpSlavePortTxMode,_i:osPtpSlaveDirection,_j:osPtpSlaveDomainIndex,_k:osPtpSlaveOutClkFrequency,_b:osPtpSlaveDirectMasterOnly,'osPtpMIBSlaveCfgTbl':osPtpMIBSlaveCfgTbl,'osPtpSlaveDirectMasterTable':osPtpSlaveDirectMasterTable,'osPtpSlaveDirectMasterEntry':osPtpSlaveDirectMasterEntry,_R:osPtpSlaveDirectMasterId,_c:osPtpSlaveDirectMasterAddress,'osPtpMIBCapabilities':osPtpMIBCapabilities,_S:osPtpSlaveSupported,_T:osPtpSlaveAddressTypesSupported,_U:osPtpSlaveNumOfDirectMasterRows,'osPtpMIBConformance':osPtpMIBConformance,'osPtpMIBCompliances':osPtpMIBCompliances,'osPtpMIBCompliance':osPtpMIBCompliance,'osPtpMIBGroups':osPtpMIBGroups,_m:osPtpMibMandatoryGroup,_n:osPtpNotificationsGroup})