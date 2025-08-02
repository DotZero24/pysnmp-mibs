_r='hpnicfNqaStatisticsCtlEntry'
_q='hpnicfNqaCtlEntry'
_p='hpnicfNqaStatReactItemIndex'
_o='hpnicfNqaStatReactIndex'
_n='hpnicfNqaStatReactTestName'
_m='hpnicfNqaStatReactOwnerIndex'
_l='invalid'
_k='hpnicfNqaStatJitterIndex'
_j='hpnicfNqaStatResIndex'
_i='seconds'
_h='hpnicfNqaUdpServerPort'
_g='hpnicfNqaUdpServerIpAddress'
_f='hpnicfNqaTcpServerPort'
_e='hpnicfNqaTcpServerIpAddress'
_d='read-write'
_c='disable'
_b='enable'
_a='InetAddressType'
_Z='accessible-for-notify'
_Y='minutes'
_X='Counter32'
_W='InetAddress'
_V='SnmpAdminString'
_U='pingCtlTestName'
_T='pingCtlOwnerIndex'
_S='DisplayString'
_R='hpnicfNqaReactThresholdType'
_Q='hpnicfNqaReactCurrentStatus'
_P='pingCtlType'
_O='pingCtlTargetAddressType'
_N='pingCtlTargetAddress'
_M='pingCtlDescr'
_L='hpnicfNqaReactItemIndex'
_K='hpnicfNqaReactTestName'
_J='hpnicfNqaReactOwnerIndex'
_I='not-accessible'
_H='Unsigned32'
_G='Integer32'
_F='milliseconds'
_E='read-create'
_D='DISMAN-PING-MIB'
_C='HPN-ICF-NQA-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pingCtlDescr,pingCtlEntry,pingCtlOwnerIndex,pingCtlTargetAddress,pingCtlTargetAddressType,pingCtlTestName,pingCtlType=mibBuilder.importSymbols(_D,_M,'pingCtlEntry',_T,_N,_O,_U,_P)
hpnicfRhw,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfRhw')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_W,_a)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_V)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_X,'Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_S,'PhysAddress','RowStatus','TextualConvention')
hpnicfNqa=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,3))
_HpnicfNqaObjects_ObjectIdentity=ObjectIdentity
hpnicfNqaObjects=_HpnicfNqaObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,3,1))
_HpnicfNqaMIBVersion_Type=DisplayString
_HpnicfNqaMIBVersion_Object=MibScalar
hpnicfNqaMIBVersion=_HpnicfNqaMIBVersion_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,1),_HpnicfNqaMIBVersion_Type())
hpnicfNqaMIBVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaMIBVersion.setStatus(_A)
_HpnicfNqaCtlTable_Object=MibTable
hpnicfNqaCtlTable=_HpnicfNqaCtlTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2))
if mibBuilder.loadTexts:hpnicfNqaCtlTable.setStatus(_A)
_HpnicfNqaCtlEntry_Object=MibTableRow
hpnicfNqaCtlEntry=_HpnicfNqaCtlEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1))
if mibBuilder.loadTexts:hpnicfNqaCtlEntry.setStatus(_A)
class _HpnicfNqaCtlTargetPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_HpnicfNqaCtlTargetPort_Type.__name__=_G
_HpnicfNqaCtlTargetPort_Object=MibTableColumn
hpnicfNqaCtlTargetPort=_HpnicfNqaCtlTargetPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,1),_HpnicfNqaCtlTargetPort_Type())
hpnicfNqaCtlTargetPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlTargetPort.setStatus(_A)
class _HpnicfNqaCtlSourcePort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_HpnicfNqaCtlSourcePort_Type.__name__=_G
_HpnicfNqaCtlSourcePort_Object=MibTableColumn
hpnicfNqaCtlSourcePort=_HpnicfNqaCtlSourcePort_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,2),_HpnicfNqaCtlSourcePort_Type())
hpnicfNqaCtlSourcePort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlSourcePort.setStatus(_A)
class _HpnicfNqaCtlTTL_Type(Integer32):defaultValue=20
_HpnicfNqaCtlTTL_Type.__name__=_G
_HpnicfNqaCtlTTL_Object=MibTableColumn
hpnicfNqaCtlTTL=_HpnicfNqaCtlTTL_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,3),_HpnicfNqaCtlTTL_Type())
hpnicfNqaCtlTTL.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlTTL.setStatus(_A)
class _HpnicfNqaCtlJitterAdminInterval_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_HpnicfNqaCtlJitterAdminInterval_Type.__name__=_G
_HpnicfNqaCtlJitterAdminInterval_Object=MibTableColumn
hpnicfNqaCtlJitterAdminInterval=_HpnicfNqaCtlJitterAdminInterval_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,4),_HpnicfNqaCtlJitterAdminInterval_Type())
hpnicfNqaCtlJitterAdminInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlJitterAdminInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaCtlJitterAdminInterval.setUnits(_F)
class _HpnicfNqaCtlJitterAdminNumPackets_Type(Integer32):defaultValue=10
_HpnicfNqaCtlJitterAdminNumPackets_Type.__name__=_G
_HpnicfNqaCtlJitterAdminNumPackets_Object=MibTableColumn
hpnicfNqaCtlJitterAdminNumPackets=_HpnicfNqaCtlJitterAdminNumPackets_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,5),_HpnicfNqaCtlJitterAdminNumPackets_Type())
hpnicfNqaCtlJitterAdminNumPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlJitterAdminNumPackets.setStatus(_A)
class _HpnicfNqaCtlHttpOperationType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('get',1),('post',2),('raw',3)))
_HpnicfNqaCtlHttpOperationType_Type.__name__=_G
_HpnicfNqaCtlHttpOperationType_Object=MibTableColumn
hpnicfNqaCtlHttpOperationType=_HpnicfNqaCtlHttpOperationType_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,6),_HpnicfNqaCtlHttpOperationType_Type())
hpnicfNqaCtlHttpOperationType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlHttpOperationType.setStatus(_A)
class _HpnicfNqaCtlHttpOperationString_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
_HpnicfNqaCtlHttpOperationString_Type.__name__=_S
_HpnicfNqaCtlHttpOperationString_Object=MibTableColumn
hpnicfNqaCtlHttpOperationString=_HpnicfNqaCtlHttpOperationString_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,7),_HpnicfNqaCtlHttpOperationString_Type())
hpnicfNqaCtlHttpOperationString.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlHttpOperationString.setStatus(_A)
class _HpnicfNqaCtlFtpOperationType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('get',1),('put',2)))
_HpnicfNqaCtlFtpOperationType_Type.__name__=_G
_HpnicfNqaCtlFtpOperationType_Object=MibTableColumn
hpnicfNqaCtlFtpOperationType=_HpnicfNqaCtlFtpOperationType_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,8),_HpnicfNqaCtlFtpOperationType_Type())
hpnicfNqaCtlFtpOperationType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlFtpOperationType.setStatus(_A)
class _HpnicfNqaCtlFtpUsername_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfNqaCtlFtpUsername_Type.__name__=_S
_HpnicfNqaCtlFtpUsername_Object=MibTableColumn
hpnicfNqaCtlFtpUsername=_HpnicfNqaCtlFtpUsername_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,9),_HpnicfNqaCtlFtpUsername_Type())
hpnicfNqaCtlFtpUsername.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlFtpUsername.setStatus(_A)
class _HpnicfNqaCtlFtpPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfNqaCtlFtpPassword_Type.__name__=_S
_HpnicfNqaCtlFtpPassword_Object=MibTableColumn
hpnicfNqaCtlFtpPassword=_HpnicfNqaCtlFtpPassword_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,10),_HpnicfNqaCtlFtpPassword_Type())
hpnicfNqaCtlFtpPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlFtpPassword.setStatus(_A)
class _HpnicfNqaCtlFtpOperationString_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfNqaCtlFtpOperationString_Type.__name__=_S
_HpnicfNqaCtlFtpOperationString_Object=MibTableColumn
hpnicfNqaCtlFtpOperationString=_HpnicfNqaCtlFtpOperationString_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,11),_HpnicfNqaCtlFtpOperationString_Type())
hpnicfNqaCtlFtpOperationString.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlFtpOperationString.setStatus(_A)
class _HpnicfNqaCtlVPNInstance_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfNqaCtlVPNInstance_Type.__name__=_S
_HpnicfNqaCtlVPNInstance_Object=MibTableColumn
hpnicfNqaCtlVPNInstance=_HpnicfNqaCtlVPNInstance_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,12),_HpnicfNqaCtlVPNInstance_Type())
hpnicfNqaCtlVPNInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlVPNInstance.setStatus(_A)
class _HpnicfNqaCtlHistoryKeptTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_HpnicfNqaCtlHistoryKeptTime_Type.__name__=_G
_HpnicfNqaCtlHistoryKeptTime_Object=MibTableColumn
hpnicfNqaCtlHistoryKeptTime=_HpnicfNqaCtlHistoryKeptTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,13),_HpnicfNqaCtlHistoryKeptTime_Type())
hpnicfNqaCtlHistoryKeptTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlHistoryKeptTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaCtlHistoryKeptTime.setUnits(_Y)
class _HpnicfNqaCtlHistoryEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfNqaCtlHistoryEnable_Type.__name__=_G
_HpnicfNqaCtlHistoryEnable_Object=MibTableColumn
hpnicfNqaCtlHistoryEnable=_HpnicfNqaCtlHistoryEnable_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,14),_HpnicfNqaCtlHistoryEnable_Type())
hpnicfNqaCtlHistoryEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlHistoryEnable.setStatus(_A)
class _HpnicfNqaCtlICPIFAdvFactor_Type(Integer32):defaultValue=0
_HpnicfNqaCtlICPIFAdvFactor_Type.__name__=_G
_HpnicfNqaCtlICPIFAdvFactor_Object=MibTableColumn
hpnicfNqaCtlICPIFAdvFactor=_HpnicfNqaCtlICPIFAdvFactor_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,15),_HpnicfNqaCtlICPIFAdvFactor_Type())
hpnicfNqaCtlICPIFAdvFactor.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlICPIFAdvFactor.setStatus(_A)
class _HpnicfNqaCtlCodecType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notDefined',1),('g711Alaw',2),('g711Ulaw',3),('g729A',4),('icmpTimestamp',5)))
_HpnicfNqaCtlCodecType_Type.__name__=_G
_HpnicfNqaCtlCodecType_Object=MibTableColumn
hpnicfNqaCtlCodecType=_HpnicfNqaCtlCodecType_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,2,1,16),_HpnicfNqaCtlCodecType_Type())
hpnicfNqaCtlCodecType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlCodecType.setStatus(_A)
_HpnicfNqaResultsTable_Object=MibTable
hpnicfNqaResultsTable=_HpnicfNqaResultsTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3))
if mibBuilder.loadTexts:hpnicfNqaResultsTable.setStatus(_A)
_HpnicfNqaResultsEntry_Object=MibTableRow
hpnicfNqaResultsEntry=_HpnicfNqaResultsEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1))
hpnicfNqaResultsEntry.setIndexNames((0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:hpnicfNqaResultsEntry.setStatus(_A)
_HpnicfNqaResultsRttNumDisconnects_Type=Unsigned32
_HpnicfNqaResultsRttNumDisconnects_Object=MibTableColumn
hpnicfNqaResultsRttNumDisconnects=_HpnicfNqaResultsRttNumDisconnects_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,1),_HpnicfNqaResultsRttNumDisconnects_Type())
hpnicfNqaResultsRttNumDisconnects.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsRttNumDisconnects.setStatus(_A)
_HpnicfNqaResultsRttTimeouts_Type=Unsigned32
_HpnicfNqaResultsRttTimeouts_Object=MibTableColumn
hpnicfNqaResultsRttTimeouts=_HpnicfNqaResultsRttTimeouts_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,2),_HpnicfNqaResultsRttTimeouts_Type())
hpnicfNqaResultsRttTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsRttTimeouts.setStatus(_A)
_HpnicfNqaResultsRttBusies_Type=Unsigned32
_HpnicfNqaResultsRttBusies_Object=MibTableColumn
hpnicfNqaResultsRttBusies=_HpnicfNqaResultsRttBusies_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,3),_HpnicfNqaResultsRttBusies_Type())
hpnicfNqaResultsRttBusies.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsRttBusies.setStatus(_A)
_HpnicfNqaResultsRttNoConnections_Type=Unsigned32
_HpnicfNqaResultsRttNoConnections_Object=MibTableColumn
hpnicfNqaResultsRttNoConnections=_HpnicfNqaResultsRttNoConnections_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,4),_HpnicfNqaResultsRttNoConnections_Type())
hpnicfNqaResultsRttNoConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsRttNoConnections.setStatus(_A)
_HpnicfNqaResultsRttDrops_Type=Unsigned32
_HpnicfNqaResultsRttDrops_Object=MibTableColumn
hpnicfNqaResultsRttDrops=_HpnicfNqaResultsRttDrops_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,5),_HpnicfNqaResultsRttDrops_Type())
hpnicfNqaResultsRttDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsRttDrops.setStatus(_A)
_HpnicfNqaResultsRttSequenceErrors_Type=Unsigned32
_HpnicfNqaResultsRttSequenceErrors_Object=MibTableColumn
hpnicfNqaResultsRttSequenceErrors=_HpnicfNqaResultsRttSequenceErrors_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,6),_HpnicfNqaResultsRttSequenceErrors_Type())
hpnicfNqaResultsRttSequenceErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsRttSequenceErrors.setStatus(_A)
_HpnicfNqaResultsRttStatsErrors_Type=Unsigned32
_HpnicfNqaResultsRttStatsErrors_Object=MibTableColumn
hpnicfNqaResultsRttStatsErrors=_HpnicfNqaResultsRttStatsErrors_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,7),_HpnicfNqaResultsRttStatsErrors_Type())
hpnicfNqaResultsRttStatsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsRttStatsErrors.setStatus(_A)
_HpnicfNqaResultsMaxDelaySD_Type=Unsigned32
_HpnicfNqaResultsMaxDelaySD_Object=MibTableColumn
hpnicfNqaResultsMaxDelaySD=_HpnicfNqaResultsMaxDelaySD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,8),_HpnicfNqaResultsMaxDelaySD_Type())
hpnicfNqaResultsMaxDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsMaxDelaySD.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaResultsMaxDelaySD.setUnits(_F)
_HpnicfNqaResultsMaxDelayDS_Type=Unsigned32
_HpnicfNqaResultsMaxDelayDS_Object=MibTableColumn
hpnicfNqaResultsMaxDelayDS=_HpnicfNqaResultsMaxDelayDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,9),_HpnicfNqaResultsMaxDelayDS_Type())
hpnicfNqaResultsMaxDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsMaxDelayDS.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaResultsMaxDelayDS.setUnits(_F)
_HpnicfNqaResultsLostPacketRatio_Type=Unsigned32
_HpnicfNqaResultsLostPacketRatio_Object=MibTableColumn
hpnicfNqaResultsLostPacketRatio=_HpnicfNqaResultsLostPacketRatio_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,10),_HpnicfNqaResultsLostPacketRatio_Type())
hpnicfNqaResultsLostPacketRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsLostPacketRatio.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaResultsLostPacketRatio.setUnits(_F)
_HpnicfNqaResultsPacketLateArrival_Type=Unsigned32
_HpnicfNqaResultsPacketLateArrival_Object=MibTableColumn
hpnicfNqaResultsPacketLateArrival=_HpnicfNqaResultsPacketLateArrival_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,11),_HpnicfNqaResultsPacketLateArrival_Type())
hpnicfNqaResultsPacketLateArrival.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsPacketLateArrival.setStatus(_A)
_HpnicfNqaResultsRttSum_Type=Unsigned32
_HpnicfNqaResultsRttSum_Object=MibTableColumn
hpnicfNqaResultsRttSum=_HpnicfNqaResultsRttSum_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,12),_HpnicfNqaResultsRttSum_Type())
hpnicfNqaResultsRttSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsRttSum.setStatus(_A)
_HpnicfNqaResultsNumOfDelaySD_Type=Unsigned32
_HpnicfNqaResultsNumOfDelaySD_Object=MibTableColumn
hpnicfNqaResultsNumOfDelaySD=_HpnicfNqaResultsNumOfDelaySD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,13),_HpnicfNqaResultsNumOfDelaySD_Type())
hpnicfNqaResultsNumOfDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsNumOfDelaySD.setStatus(_A)
_HpnicfNqaResultsMinDelaySD_Type=Unsigned32
_HpnicfNqaResultsMinDelaySD_Object=MibTableColumn
hpnicfNqaResultsMinDelaySD=_HpnicfNqaResultsMinDelaySD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,14),_HpnicfNqaResultsMinDelaySD_Type())
hpnicfNqaResultsMinDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsMinDelaySD.setStatus(_A)
_HpnicfNqaResultsSumDelaySD_Type=Unsigned32
_HpnicfNqaResultsSumDelaySD_Object=MibTableColumn
hpnicfNqaResultsSumDelaySD=_HpnicfNqaResultsSumDelaySD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,15),_HpnicfNqaResultsSumDelaySD_Type())
hpnicfNqaResultsSumDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsSumDelaySD.setStatus(_A)
_HpnicfNqaResultsSum2DelaySD_Type=Unsigned32
_HpnicfNqaResultsSum2DelaySD_Object=MibTableColumn
hpnicfNqaResultsSum2DelaySD=_HpnicfNqaResultsSum2DelaySD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,16),_HpnicfNqaResultsSum2DelaySD_Type())
hpnicfNqaResultsSum2DelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsSum2DelaySD.setStatus(_A)
_HpnicfNqaResultsNumOfDelayDS_Type=Unsigned32
_HpnicfNqaResultsNumOfDelayDS_Object=MibTableColumn
hpnicfNqaResultsNumOfDelayDS=_HpnicfNqaResultsNumOfDelayDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,17),_HpnicfNqaResultsNumOfDelayDS_Type())
hpnicfNqaResultsNumOfDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsNumOfDelayDS.setStatus(_A)
_HpnicfNqaResultsMinDelayDS_Type=Unsigned32
_HpnicfNqaResultsMinDelayDS_Object=MibTableColumn
hpnicfNqaResultsMinDelayDS=_HpnicfNqaResultsMinDelayDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,18),_HpnicfNqaResultsMinDelayDS_Type())
hpnicfNqaResultsMinDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsMinDelayDS.setStatus(_A)
_HpnicfNqaResultsSumDelayDS_Type=Unsigned32
_HpnicfNqaResultsSumDelayDS_Object=MibTableColumn
hpnicfNqaResultsSumDelayDS=_HpnicfNqaResultsSumDelayDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,19),_HpnicfNqaResultsSumDelayDS_Type())
hpnicfNqaResultsSumDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsSumDelayDS.setStatus(_A)
_HpnicfNqaResultsSum2DelayDS_Type=Unsigned32
_HpnicfNqaResultsSum2DelayDS_Object=MibTableColumn
hpnicfNqaResultsSum2DelayDS=_HpnicfNqaResultsSum2DelayDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,3,1,20),_HpnicfNqaResultsSum2DelayDS_Type())
hpnicfNqaResultsSum2DelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaResultsSum2DelayDS.setStatus(_A)
_HpnicfNqaJitterStatsTable_Object=MibTable
hpnicfNqaJitterStatsTable=_HpnicfNqaJitterStatsTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4))
if mibBuilder.loadTexts:hpnicfNqaJitterStatsTable.setStatus(_A)
_HpnicfNqaJitterStatsEntry_Object=MibTableRow
hpnicfNqaJitterStatsEntry=_HpnicfNqaJitterStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1))
hpnicfNqaJitterStatsEntry.setIndexNames((0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:hpnicfNqaJitterStatsEntry.setStatus(_A)
_HpnicfNqaJitterStatsNumOfRTT_Type=Counter32
_HpnicfNqaJitterStatsNumOfRTT_Object=MibTableColumn
hpnicfNqaJitterStatsNumOfRTT=_HpnicfNqaJitterStatsNumOfRTT_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,1),_HpnicfNqaJitterStatsNumOfRTT_Type())
hpnicfNqaJitterStatsNumOfRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsNumOfRTT.setStatus(_A)
_HpnicfNqaJitterStatsMinOfPositivesSD_Type=Gauge32
_HpnicfNqaJitterStatsMinOfPositivesSD_Object=MibTableColumn
hpnicfNqaJitterStatsMinOfPositivesSD=_HpnicfNqaJitterStatsMinOfPositivesSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,2),_HpnicfNqaJitterStatsMinOfPositivesSD_Type())
hpnicfNqaJitterStatsMinOfPositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsMinOfPositivesSD.setStatus(_A)
_HpnicfNqaJitterStatsMaxOfPositivesSD_Type=Gauge32
_HpnicfNqaJitterStatsMaxOfPositivesSD_Object=MibTableColumn
hpnicfNqaJitterStatsMaxOfPositivesSD=_HpnicfNqaJitterStatsMaxOfPositivesSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,3),_HpnicfNqaJitterStatsMaxOfPositivesSD_Type())
hpnicfNqaJitterStatsMaxOfPositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsMaxOfPositivesSD.setStatus(_A)
_HpnicfNqaJitterStatsNumOfPositivesSD_Type=Gauge32
_HpnicfNqaJitterStatsNumOfPositivesSD_Object=MibTableColumn
hpnicfNqaJitterStatsNumOfPositivesSD=_HpnicfNqaJitterStatsNumOfPositivesSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,4),_HpnicfNqaJitterStatsNumOfPositivesSD_Type())
hpnicfNqaJitterStatsNumOfPositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsNumOfPositivesSD.setStatus(_A)
_HpnicfNqaJitterStatsSumOfPositivesSD_Type=Gauge32
_HpnicfNqaJitterStatsSumOfPositivesSD_Object=MibTableColumn
hpnicfNqaJitterStatsSumOfPositivesSD=_HpnicfNqaJitterStatsSumOfPositivesSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,5),_HpnicfNqaJitterStatsSumOfPositivesSD_Type())
hpnicfNqaJitterStatsSumOfPositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsSumOfPositivesSD.setStatus(_A)
_HpnicfNqaJitterStatsSum2PositivesSD_Type=Gauge32
_HpnicfNqaJitterStatsSum2PositivesSD_Object=MibTableColumn
hpnicfNqaJitterStatsSum2PositivesSD=_HpnicfNqaJitterStatsSum2PositivesSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,6),_HpnicfNqaJitterStatsSum2PositivesSD_Type())
hpnicfNqaJitterStatsSum2PositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsSum2PositivesSD.setStatus(_A)
_HpnicfNqaJitterStatsMinOfNegativesSD_Type=Gauge32
_HpnicfNqaJitterStatsMinOfNegativesSD_Object=MibTableColumn
hpnicfNqaJitterStatsMinOfNegativesSD=_HpnicfNqaJitterStatsMinOfNegativesSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,7),_HpnicfNqaJitterStatsMinOfNegativesSD_Type())
hpnicfNqaJitterStatsMinOfNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsMinOfNegativesSD.setStatus(_A)
_HpnicfNqaJitterStatsMaxOfNegativesSD_Type=Gauge32
_HpnicfNqaJitterStatsMaxOfNegativesSD_Object=MibTableColumn
hpnicfNqaJitterStatsMaxOfNegativesSD=_HpnicfNqaJitterStatsMaxOfNegativesSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,8),_HpnicfNqaJitterStatsMaxOfNegativesSD_Type())
hpnicfNqaJitterStatsMaxOfNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsMaxOfNegativesSD.setStatus(_A)
_HpnicfNqaJitterStatsNumOfNegativesSD_Type=Gauge32
_HpnicfNqaJitterStatsNumOfNegativesSD_Object=MibTableColumn
hpnicfNqaJitterStatsNumOfNegativesSD=_HpnicfNqaJitterStatsNumOfNegativesSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,9),_HpnicfNqaJitterStatsNumOfNegativesSD_Type())
hpnicfNqaJitterStatsNumOfNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsNumOfNegativesSD.setStatus(_A)
_HpnicfNqaJitterStatsSumOfNegativesSD_Type=Gauge32
_HpnicfNqaJitterStatsSumOfNegativesSD_Object=MibTableColumn
hpnicfNqaJitterStatsSumOfNegativesSD=_HpnicfNqaJitterStatsSumOfNegativesSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,10),_HpnicfNqaJitterStatsSumOfNegativesSD_Type())
hpnicfNqaJitterStatsSumOfNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsSumOfNegativesSD.setStatus(_A)
_HpnicfNqaJitterStatsSum2NegativesSD_Type=Gauge32
_HpnicfNqaJitterStatsSum2NegativesSD_Object=MibTableColumn
hpnicfNqaJitterStatsSum2NegativesSD=_HpnicfNqaJitterStatsSum2NegativesSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,11),_HpnicfNqaJitterStatsSum2NegativesSD_Type())
hpnicfNqaJitterStatsSum2NegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsSum2NegativesSD.setStatus(_A)
_HpnicfNqaJitterStatsMinOfPositivesDS_Type=Gauge32
_HpnicfNqaJitterStatsMinOfPositivesDS_Object=MibTableColumn
hpnicfNqaJitterStatsMinOfPositivesDS=_HpnicfNqaJitterStatsMinOfPositivesDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,12),_HpnicfNqaJitterStatsMinOfPositivesDS_Type())
hpnicfNqaJitterStatsMinOfPositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsMinOfPositivesDS.setStatus(_A)
_HpnicfNqaJitterStatsMaxOfPositivesDS_Type=Gauge32
_HpnicfNqaJitterStatsMaxOfPositivesDS_Object=MibTableColumn
hpnicfNqaJitterStatsMaxOfPositivesDS=_HpnicfNqaJitterStatsMaxOfPositivesDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,13),_HpnicfNqaJitterStatsMaxOfPositivesDS_Type())
hpnicfNqaJitterStatsMaxOfPositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsMaxOfPositivesDS.setStatus(_A)
_HpnicfNqaJitterStatsNumOfPositivesDS_Type=Gauge32
_HpnicfNqaJitterStatsNumOfPositivesDS_Object=MibTableColumn
hpnicfNqaJitterStatsNumOfPositivesDS=_HpnicfNqaJitterStatsNumOfPositivesDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,14),_HpnicfNqaJitterStatsNumOfPositivesDS_Type())
hpnicfNqaJitterStatsNumOfPositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsNumOfPositivesDS.setStatus(_A)
_HpnicfNqaJitterStatsSumOfPositivesDS_Type=Gauge32
_HpnicfNqaJitterStatsSumOfPositivesDS_Object=MibTableColumn
hpnicfNqaJitterStatsSumOfPositivesDS=_HpnicfNqaJitterStatsSumOfPositivesDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,15),_HpnicfNqaJitterStatsSumOfPositivesDS_Type())
hpnicfNqaJitterStatsSumOfPositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsSumOfPositivesDS.setStatus(_A)
_HpnicfNqaJitterStatsSum2PositivesDS_Type=Gauge32
_HpnicfNqaJitterStatsSum2PositivesDS_Object=MibTableColumn
hpnicfNqaJitterStatsSum2PositivesDS=_HpnicfNqaJitterStatsSum2PositivesDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,16),_HpnicfNqaJitterStatsSum2PositivesDS_Type())
hpnicfNqaJitterStatsSum2PositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsSum2PositivesDS.setStatus(_A)
_HpnicfNqaJitterStatsMinOfNegativesDS_Type=Gauge32
_HpnicfNqaJitterStatsMinOfNegativesDS_Object=MibTableColumn
hpnicfNqaJitterStatsMinOfNegativesDS=_HpnicfNqaJitterStatsMinOfNegativesDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,17),_HpnicfNqaJitterStatsMinOfNegativesDS_Type())
hpnicfNqaJitterStatsMinOfNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsMinOfNegativesDS.setStatus(_A)
_HpnicfNqaJitterStatsMaxOfNegativesDS_Type=Gauge32
_HpnicfNqaJitterStatsMaxOfNegativesDS_Object=MibTableColumn
hpnicfNqaJitterStatsMaxOfNegativesDS=_HpnicfNqaJitterStatsMaxOfNegativesDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,18),_HpnicfNqaJitterStatsMaxOfNegativesDS_Type())
hpnicfNqaJitterStatsMaxOfNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsMaxOfNegativesDS.setStatus(_A)
_HpnicfNqaJitterStatsNumOfNegativesDS_Type=Gauge32
_HpnicfNqaJitterStatsNumOfNegativesDS_Object=MibTableColumn
hpnicfNqaJitterStatsNumOfNegativesDS=_HpnicfNqaJitterStatsNumOfNegativesDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,19),_HpnicfNqaJitterStatsNumOfNegativesDS_Type())
hpnicfNqaJitterStatsNumOfNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsNumOfNegativesDS.setStatus(_A)
_HpnicfNqaJitterStatsSumOfNegativesDS_Type=Gauge32
_HpnicfNqaJitterStatsSumOfNegativesDS_Object=MibTableColumn
hpnicfNqaJitterStatsSumOfNegativesDS=_HpnicfNqaJitterStatsSumOfNegativesDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,20),_HpnicfNqaJitterStatsSumOfNegativesDS_Type())
hpnicfNqaJitterStatsSumOfNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsSumOfNegativesDS.setStatus(_A)
_HpnicfNqaJitterStatsSum2NegativesDS_Type=Gauge32
_HpnicfNqaJitterStatsSum2NegativesDS_Object=MibTableColumn
hpnicfNqaJitterStatsSum2NegativesDS=_HpnicfNqaJitterStatsSum2NegativesDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,21),_HpnicfNqaJitterStatsSum2NegativesDS_Type())
hpnicfNqaJitterStatsSum2NegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsSum2NegativesDS.setStatus(_A)
_HpnicfNqaJitterStatsPacketLossSD_Type=Gauge32
_HpnicfNqaJitterStatsPacketLossSD_Object=MibTableColumn
hpnicfNqaJitterStatsPacketLossSD=_HpnicfNqaJitterStatsPacketLossSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,22),_HpnicfNqaJitterStatsPacketLossSD_Type())
hpnicfNqaJitterStatsPacketLossSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsPacketLossSD.setStatus(_A)
_HpnicfNqaJitterStatsPacketLossDS_Type=Gauge32
_HpnicfNqaJitterStatsPacketLossDS_Object=MibTableColumn
hpnicfNqaJitterStatsPacketLossDS=_HpnicfNqaJitterStatsPacketLossDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,23),_HpnicfNqaJitterStatsPacketLossDS_Type())
hpnicfNqaJitterStatsPacketLossDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsPacketLossDS.setStatus(_A)
_HpnicfNqaJitterStatsAvePositivesSD_Type=Gauge32
_HpnicfNqaJitterStatsAvePositivesSD_Object=MibTableColumn
hpnicfNqaJitterStatsAvePositivesSD=_HpnicfNqaJitterStatsAvePositivesSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,24),_HpnicfNqaJitterStatsAvePositivesSD_Type())
hpnicfNqaJitterStatsAvePositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsAvePositivesSD.setStatus(_A)
_HpnicfNqaJitterStatsAveNegativesSD_Type=Gauge32
_HpnicfNqaJitterStatsAveNegativesSD_Object=MibTableColumn
hpnicfNqaJitterStatsAveNegativesSD=_HpnicfNqaJitterStatsAveNegativesSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,25),_HpnicfNqaJitterStatsAveNegativesSD_Type())
hpnicfNqaJitterStatsAveNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsAveNegativesSD.setStatus(_A)
_HpnicfNqaJitterStatsAvePositivesDS_Type=Gauge32
_HpnicfNqaJitterStatsAvePositivesDS_Object=MibTableColumn
hpnicfNqaJitterStatsAvePositivesDS=_HpnicfNqaJitterStatsAvePositivesDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,26),_HpnicfNqaJitterStatsAvePositivesDS_Type())
hpnicfNqaJitterStatsAvePositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsAvePositivesDS.setStatus(_A)
_HpnicfNqaJitterStatsAveNegativesDS_Type=Gauge32
_HpnicfNqaJitterStatsAveNegativesDS_Object=MibTableColumn
hpnicfNqaJitterStatsAveNegativesDS=_HpnicfNqaJitterStatsAveNegativesDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,27),_HpnicfNqaJitterStatsAveNegativesDS_Type())
hpnicfNqaJitterStatsAveNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsAveNegativesDS.setStatus(_A)
_HpnicfNqaJitterStatsPktLossUnknown_Type=Gauge32
_HpnicfNqaJitterStatsPktLossUnknown_Object=MibTableColumn
hpnicfNqaJitterStatsPktLossUnknown=_HpnicfNqaJitterStatsPktLossUnknown_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,28),_HpnicfNqaJitterStatsPktLossUnknown_Type())
hpnicfNqaJitterStatsPktLossUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsPktLossUnknown.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsPktLossUnknown.setUnits(_F)
_HpnicfNqaJitterStatsOperOfICPIF_Type=Gauge32
_HpnicfNqaJitterStatsOperOfICPIF_Object=MibTableColumn
hpnicfNqaJitterStatsOperOfICPIF=_HpnicfNqaJitterStatsOperOfICPIF_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,29),_HpnicfNqaJitterStatsOperOfICPIF_Type())
hpnicfNqaJitterStatsOperOfICPIF.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsOperOfICPIF.setStatus(_A)
_HpnicfNqaJitterStatsOperOfMOS_Type=Gauge32
_HpnicfNqaJitterStatsOperOfMOS_Object=MibTableColumn
hpnicfNqaJitterStatsOperOfMOS=_HpnicfNqaJitterStatsOperOfMOS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,4,1,30),_HpnicfNqaJitterStatsOperOfMOS_Type())
hpnicfNqaJitterStatsOperOfMOS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaJitterStatsOperOfMOS.setStatus(_A)
class _HpnicfNqaAgentEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_HpnicfNqaAgentEnable_Type.__name__=_G
_HpnicfNqaAgentEnable_Object=MibScalar
hpnicfNqaAgentEnable=_HpnicfNqaAgentEnable_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,5),_HpnicfNqaAgentEnable_Type())
hpnicfNqaAgentEnable.setMaxAccess(_d)
if mibBuilder.loadTexts:hpnicfNqaAgentEnable.setStatus(_A)
_HpnicfNqaTcpServerTable_Object=MibTable
hpnicfNqaTcpServerTable=_HpnicfNqaTcpServerTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,6))
if mibBuilder.loadTexts:hpnicfNqaTcpServerTable.setStatus(_A)
_HpnicfNqaTcpServerEntry_Object=MibTableRow
hpnicfNqaTcpServerEntry=_HpnicfNqaTcpServerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,6,1))
hpnicfNqaTcpServerEntry.setIndexNames((0,_C,_e),(0,_C,_f))
if mibBuilder.loadTexts:hpnicfNqaTcpServerEntry.setStatus(_A)
class _HpnicfNqaTcpServerIpAddress_Type(InetAddress):defaultHexValue=''
_HpnicfNqaTcpServerIpAddress_Type.__name__=_W
_HpnicfNqaTcpServerIpAddress_Object=MibTableColumn
hpnicfNqaTcpServerIpAddress=_HpnicfNqaTcpServerIpAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,6,1,1),_HpnicfNqaTcpServerIpAddress_Type())
hpnicfNqaTcpServerIpAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfNqaTcpServerIpAddress.setStatus(_A)
class _HpnicfNqaTcpServerPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_HpnicfNqaTcpServerPort_Type.__name__=_G
_HpnicfNqaTcpServerPort_Object=MibTableColumn
hpnicfNqaTcpServerPort=_HpnicfNqaTcpServerPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,6,1,2),_HpnicfNqaTcpServerPort_Type())
hpnicfNqaTcpServerPort.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfNqaTcpServerPort.setStatus(_A)
_HpnicfNqaTcpServerRowStatus_Type=RowStatus
_HpnicfNqaTcpServerRowStatus_Object=MibTableColumn
hpnicfNqaTcpServerRowStatus=_HpnicfNqaTcpServerRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,6,1,3),_HpnicfNqaTcpServerRowStatus_Type())
hpnicfNqaTcpServerRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaTcpServerRowStatus.setStatus(_A)
_HpnicfNqaUdpServerTable_Object=MibTable
hpnicfNqaUdpServerTable=_HpnicfNqaUdpServerTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,7))
if mibBuilder.loadTexts:hpnicfNqaUdpServerTable.setStatus(_A)
_HpnicfNqaUdpServerEntry_Object=MibTableRow
hpnicfNqaUdpServerEntry=_HpnicfNqaUdpServerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,7,1))
hpnicfNqaUdpServerEntry.setIndexNames((0,_C,_g),(0,_C,_h))
if mibBuilder.loadTexts:hpnicfNqaUdpServerEntry.setStatus(_A)
class _HpnicfNqaUdpServerIpAddress_Type(InetAddress):defaultHexValue=''
_HpnicfNqaUdpServerIpAddress_Type.__name__=_W
_HpnicfNqaUdpServerIpAddress_Object=MibTableColumn
hpnicfNqaUdpServerIpAddress=_HpnicfNqaUdpServerIpAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,7,1,1),_HpnicfNqaUdpServerIpAddress_Type())
hpnicfNqaUdpServerIpAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfNqaUdpServerIpAddress.setStatus(_A)
class _HpnicfNqaUdpServerPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_HpnicfNqaUdpServerPort_Type.__name__=_G
_HpnicfNqaUdpServerPort_Object=MibTableColumn
hpnicfNqaUdpServerPort=_HpnicfNqaUdpServerPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,7,1,2),_HpnicfNqaUdpServerPort_Type())
hpnicfNqaUdpServerPort.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfNqaUdpServerPort.setStatus(_A)
_HpnicfNqaUdpServerRowStatus_Type=RowStatus
_HpnicfNqaUdpServerRowStatus_Object=MibTableColumn
hpnicfNqaUdpServerRowStatus=_HpnicfNqaUdpServerRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,7,1,3),_HpnicfNqaUdpServerRowStatus_Type())
hpnicfNqaUdpServerRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaUdpServerRowStatus.setStatus(_A)
class _HpnicfNqaServerEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_HpnicfNqaServerEnable_Type.__name__=_G
_HpnicfNqaServerEnable_Object=MibScalar
hpnicfNqaServerEnable=_HpnicfNqaServerEnable_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,8),_HpnicfNqaServerEnable_Type())
hpnicfNqaServerEnable.setMaxAccess(_d)
if mibBuilder.loadTexts:hpnicfNqaServerEnable.setStatus(_A)
_HpnicfNqaStatsMaxGroupNumber_Type=Integer32
_HpnicfNqaStatsMaxGroupNumber_Object=MibScalar
hpnicfNqaStatsMaxGroupNumber=_HpnicfNqaStatsMaxGroupNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,9),_HpnicfNqaStatsMaxGroupNumber_Type())
hpnicfNqaStatsMaxGroupNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatsMaxGroupNumber.setStatus(_A)
_HpnicfNqaStatisticsCtlTable_Object=MibTable
hpnicfNqaStatisticsCtlTable=_HpnicfNqaStatisticsCtlTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,10))
if mibBuilder.loadTexts:hpnicfNqaStatisticsCtlTable.setStatus(_A)
_HpnicfNqaStatisticsCtlEntry_Object=MibTableRow
hpnicfNqaStatisticsCtlEntry=_HpnicfNqaStatisticsCtlEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,10,1))
if mibBuilder.loadTexts:hpnicfNqaStatisticsCtlEntry.setStatus(_A)
_HpnicfNqaCtlStatisticsInterval_Type=Unsigned32
_HpnicfNqaCtlStatisticsInterval_Object=MibTableColumn
hpnicfNqaCtlStatisticsInterval=_HpnicfNqaCtlStatisticsInterval_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,10,1,1),_HpnicfNqaCtlStatisticsInterval_Type())
hpnicfNqaCtlStatisticsInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlStatisticsInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaCtlStatisticsInterval.setUnits(_Y)
class _HpnicfNqaCtlStatisticsGroupNumber_Type(Unsigned32):defaultValue=2
_HpnicfNqaCtlStatisticsGroupNumber_Type.__name__=_H
_HpnicfNqaCtlStatisticsGroupNumber_Object=MibTableColumn
hpnicfNqaCtlStatisticsGroupNumber=_HpnicfNqaCtlStatisticsGroupNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,10,1,2),_HpnicfNqaCtlStatisticsGroupNumber_Type())
hpnicfNqaCtlStatisticsGroupNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlStatisticsGroupNumber.setStatus(_A)
class _HpnicfNqaCtlStatisticsKeptTime_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_HpnicfNqaCtlStatisticsKeptTime_Type.__name__=_H
_HpnicfNqaCtlStatisticsKeptTime_Object=MibTableColumn
hpnicfNqaCtlStatisticsKeptTime=_HpnicfNqaCtlStatisticsKeptTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,10,1,3),_HpnicfNqaCtlStatisticsKeptTime_Type())
hpnicfNqaCtlStatisticsKeptTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlStatisticsKeptTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaCtlStatisticsKeptTime.setUnits(_Y)
_HpnicfNqaCtlBeginTime_Type=DateAndTime
_HpnicfNqaCtlBeginTime_Object=MibTableColumn
hpnicfNqaCtlBeginTime=_HpnicfNqaCtlBeginTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,10,1,4),_HpnicfNqaCtlBeginTime_Type())
hpnicfNqaCtlBeginTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlBeginTime.setStatus(_A)
class _HpnicfNqaCtlLifeTime_Type(Unsigned32):defaultValue=0
_HpnicfNqaCtlLifeTime_Type.__name__=_H
_HpnicfNqaCtlLifeTime_Object=MibTableColumn
hpnicfNqaCtlLifeTime=_HpnicfNqaCtlLifeTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,10,1,5),_HpnicfNqaCtlLifeTime_Type())
hpnicfNqaCtlLifeTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaCtlLifeTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaCtlLifeTime.setUnits(_i)
_HpnicfNqaStatisticsResultsTable_Object=MibTable
hpnicfNqaStatisticsResultsTable=_HpnicfNqaStatisticsResultsTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11))
if mibBuilder.loadTexts:hpnicfNqaStatisticsResultsTable.setStatus(_A)
_HpnicfNqaStatisticsResultsEntry_Object=MibTableRow
hpnicfNqaStatisticsResultsEntry=_HpnicfNqaStatisticsResultsEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1))
hpnicfNqaStatisticsResultsEntry.setIndexNames((0,_D,_T),(0,_D,_U),(0,_C,_j))
if mibBuilder.loadTexts:hpnicfNqaStatisticsResultsEntry.setStatus(_A)
class _HpnicfNqaStatResIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfNqaStatResIndex_Type.__name__=_H
_HpnicfNqaStatResIndex_Object=MibTableColumn
hpnicfNqaStatResIndex=_HpnicfNqaStatResIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,1),_HpnicfNqaStatResIndex_Type())
hpnicfNqaStatResIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfNqaStatResIndex.setStatus(_A)
class _HpnicfNqaStatResIpTargetAddressType_Type(InetAddressType):defaultValue=0
_HpnicfNqaStatResIpTargetAddressType_Type.__name__=_a
_HpnicfNqaStatResIpTargetAddressType_Object=MibTableColumn
hpnicfNqaStatResIpTargetAddressType=_HpnicfNqaStatResIpTargetAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,2),_HpnicfNqaStatResIpTargetAddressType_Type())
hpnicfNqaStatResIpTargetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResIpTargetAddressType.setStatus(_A)
class _HpnicfNqaStatResIpTargetAddress_Type(InetAddress):defaultHexValue=''
_HpnicfNqaStatResIpTargetAddress_Type.__name__=_W
_HpnicfNqaStatResIpTargetAddress_Object=MibTableColumn
hpnicfNqaStatResIpTargetAddress=_HpnicfNqaStatResIpTargetAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,3),_HpnicfNqaStatResIpTargetAddress_Type())
hpnicfNqaStatResIpTargetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResIpTargetAddress.setStatus(_A)
_HpnicfNqaStatResMinRtt_Type=Gauge32
_HpnicfNqaStatResMinRtt_Object=MibTableColumn
hpnicfNqaStatResMinRtt=_HpnicfNqaStatResMinRtt_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,4),_HpnicfNqaStatResMinRtt_Type())
hpnicfNqaStatResMinRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResMinRtt.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatResMinRtt.setUnits(_F)
_HpnicfNqaStatResMaxRtt_Type=Gauge32
_HpnicfNqaStatResMaxRtt_Object=MibTableColumn
hpnicfNqaStatResMaxRtt=_HpnicfNqaStatResMaxRtt_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,5),_HpnicfNqaStatResMaxRtt_Type())
hpnicfNqaStatResMaxRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResMaxRtt.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatResMaxRtt.setUnits(_F)
_HpnicfNqaStatResAverageRtt_Type=Gauge32
_HpnicfNqaStatResAverageRtt_Object=MibTableColumn
hpnicfNqaStatResAverageRtt=_HpnicfNqaStatResAverageRtt_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,6),_HpnicfNqaStatResAverageRtt_Type())
hpnicfNqaStatResAverageRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResAverageRtt.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatResAverageRtt.setUnits(_F)
_HpnicfNqaStatResProbeResponses_Type=Counter32
_HpnicfNqaStatResProbeResponses_Object=MibTableColumn
hpnicfNqaStatResProbeResponses=_HpnicfNqaStatResProbeResponses_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,7),_HpnicfNqaStatResProbeResponses_Type())
hpnicfNqaStatResProbeResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResProbeResponses.setStatus(_A)
_HpnicfNqaStatResSentProbes_Type=Counter32
_HpnicfNqaStatResSentProbes_Object=MibTableColumn
hpnicfNqaStatResSentProbes=_HpnicfNqaStatResSentProbes_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,8),_HpnicfNqaStatResSentProbes_Type())
hpnicfNqaStatResSentProbes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResSentProbes.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatResSentProbes.setUnits('probes')
_HpnicfNqaStatResRttSumOfSquares_Type=Counter32
_HpnicfNqaStatResRttSumOfSquares_Object=MibTableColumn
hpnicfNqaStatResRttSumOfSquares=_HpnicfNqaStatResRttSumOfSquares_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,9),_HpnicfNqaStatResRttSumOfSquares_Type())
hpnicfNqaStatResRttSumOfSquares.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResRttSumOfSquares.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatResRttSumOfSquares.setUnits(_F)
_HpnicfNqaStatResStartTime_Type=DateAndTime
_HpnicfNqaStatResStartTime_Object=MibTableColumn
hpnicfNqaStatResStartTime=_HpnicfNqaStatResStartTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,10),_HpnicfNqaStatResStartTime_Type())
hpnicfNqaStatResStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResStartTime.setStatus(_A)
_HpnicfNqaStatResInterval_Type=Gauge32
_HpnicfNqaStatResInterval_Object=MibTableColumn
hpnicfNqaStatResInterval=_HpnicfNqaStatResInterval_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,11),_HpnicfNqaStatResInterval_Type())
hpnicfNqaStatResInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatResInterval.setUnits(_i)
_HpnicfNqaStatResRttNumDisconnects_Type=Counter32
_HpnicfNqaStatResRttNumDisconnects_Object=MibTableColumn
hpnicfNqaStatResRttNumDisconnects=_HpnicfNqaStatResRttNumDisconnects_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,12),_HpnicfNqaStatResRttNumDisconnects_Type())
hpnicfNqaStatResRttNumDisconnects.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResRttNumDisconnects.setStatus(_A)
_HpnicfNqaStatResRttTimeouts_Type=Counter32
_HpnicfNqaStatResRttTimeouts_Object=MibTableColumn
hpnicfNqaStatResRttTimeouts=_HpnicfNqaStatResRttTimeouts_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,13),_HpnicfNqaStatResRttTimeouts_Type())
hpnicfNqaStatResRttTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResRttTimeouts.setStatus(_A)
_HpnicfNqaStatResRttBusies_Type=Counter32
_HpnicfNqaStatResRttBusies_Object=MibTableColumn
hpnicfNqaStatResRttBusies=_HpnicfNqaStatResRttBusies_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,14),_HpnicfNqaStatResRttBusies_Type())
hpnicfNqaStatResRttBusies.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResRttBusies.setStatus(_A)
_HpnicfNqaStatResRttNoConnections_Type=Counter32
_HpnicfNqaStatResRttNoConnections_Object=MibTableColumn
hpnicfNqaStatResRttNoConnections=_HpnicfNqaStatResRttNoConnections_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,15),_HpnicfNqaStatResRttNoConnections_Type())
hpnicfNqaStatResRttNoConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResRttNoConnections.setStatus(_A)
_HpnicfNqaStatResRttDrops_Type=Counter32
_HpnicfNqaStatResRttDrops_Object=MibTableColumn
hpnicfNqaStatResRttDrops=_HpnicfNqaStatResRttDrops_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,16),_HpnicfNqaStatResRttDrops_Type())
hpnicfNqaStatResRttDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResRttDrops.setStatus(_A)
_HpnicfNqaStatResRttSequenceErrors_Type=Counter32
_HpnicfNqaStatResRttSequenceErrors_Object=MibTableColumn
hpnicfNqaStatResRttSequenceErrors=_HpnicfNqaStatResRttSequenceErrors_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,17),_HpnicfNqaStatResRttSequenceErrors_Type())
hpnicfNqaStatResRttSequenceErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResRttSequenceErrors.setStatus(_A)
_HpnicfNqaStatResRttErrors_Type=Counter32
_HpnicfNqaStatResRttErrors_Object=MibTableColumn
hpnicfNqaStatResRttErrors=_HpnicfNqaStatResRttErrors_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,18),_HpnicfNqaStatResRttErrors_Type())
hpnicfNqaStatResRttErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResRttErrors.setStatus(_A)
_HpnicfNqaStatResLostPacketRatio_Type=Gauge32
_HpnicfNqaStatResLostPacketRatio_Object=MibTableColumn
hpnicfNqaStatResLostPacketRatio=_HpnicfNqaStatResLostPacketRatio_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,19),_HpnicfNqaStatResLostPacketRatio_Type())
hpnicfNqaStatResLostPacketRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResLostPacketRatio.setStatus(_A)
_HpnicfNqaStatResPacketLateArrival_Type=Counter32
_HpnicfNqaStatResPacketLateArrival_Object=MibTableColumn
hpnicfNqaStatResPacketLateArrival=_HpnicfNqaStatResPacketLateArrival_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,20),_HpnicfNqaStatResPacketLateArrival_Type())
hpnicfNqaStatResPacketLateArrival.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResPacketLateArrival.setStatus(_A)
_HpnicfNqaStatResRttSum_Type=Counter32
_HpnicfNqaStatResRttSum_Object=MibTableColumn
hpnicfNqaStatResRttSum=_HpnicfNqaStatResRttSum_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,21),_HpnicfNqaStatResRttSum_Type())
hpnicfNqaStatResRttSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResRttSum.setStatus(_A)
_HpnicfNqaStatResNumOfDelaySD_Type=Counter32
_HpnicfNqaStatResNumOfDelaySD_Object=MibTableColumn
hpnicfNqaStatResNumOfDelaySD=_HpnicfNqaStatResNumOfDelaySD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,22),_HpnicfNqaStatResNumOfDelaySD_Type())
hpnicfNqaStatResNumOfDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResNumOfDelaySD.setStatus(_A)
_HpnicfNqaStatResMinDelaySD_Type=Gauge32
_HpnicfNqaStatResMinDelaySD_Object=MibTableColumn
hpnicfNqaStatResMinDelaySD=_HpnicfNqaStatResMinDelaySD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,23),_HpnicfNqaStatResMinDelaySD_Type())
hpnicfNqaStatResMinDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResMinDelaySD.setStatus(_A)
_HpnicfNqaStatResMaxDelaySD_Type=Gauge32
_HpnicfNqaStatResMaxDelaySD_Object=MibTableColumn
hpnicfNqaStatResMaxDelaySD=_HpnicfNqaStatResMaxDelaySD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,24),_HpnicfNqaStatResMaxDelaySD_Type())
hpnicfNqaStatResMaxDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResMaxDelaySD.setStatus(_A)
_HpnicfNqaStatResSumDelaySD_Type=Counter32
_HpnicfNqaStatResSumDelaySD_Object=MibTableColumn
hpnicfNqaStatResSumDelaySD=_HpnicfNqaStatResSumDelaySD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,25),_HpnicfNqaStatResSumDelaySD_Type())
hpnicfNqaStatResSumDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResSumDelaySD.setStatus(_A)
_HpnicfNqaStatResSum2DelaySD_Type=Counter32
_HpnicfNqaStatResSum2DelaySD_Object=MibTableColumn
hpnicfNqaStatResSum2DelaySD=_HpnicfNqaStatResSum2DelaySD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,26),_HpnicfNqaStatResSum2DelaySD_Type())
hpnicfNqaStatResSum2DelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResSum2DelaySD.setStatus(_A)
_HpnicfNqaStatResNumOfDelayDS_Type=Counter32
_HpnicfNqaStatResNumOfDelayDS_Object=MibTableColumn
hpnicfNqaStatResNumOfDelayDS=_HpnicfNqaStatResNumOfDelayDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,27),_HpnicfNqaStatResNumOfDelayDS_Type())
hpnicfNqaStatResNumOfDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResNumOfDelayDS.setStatus(_A)
_HpnicfNqaStatResMinDelayDS_Type=Gauge32
_HpnicfNqaStatResMinDelayDS_Object=MibTableColumn
hpnicfNqaStatResMinDelayDS=_HpnicfNqaStatResMinDelayDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,28),_HpnicfNqaStatResMinDelayDS_Type())
hpnicfNqaStatResMinDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResMinDelayDS.setStatus(_A)
_HpnicfNqaStatResMaxDelayDS_Type=Gauge32
_HpnicfNqaStatResMaxDelayDS_Object=MibTableColumn
hpnicfNqaStatResMaxDelayDS=_HpnicfNqaStatResMaxDelayDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,29),_HpnicfNqaStatResMaxDelayDS_Type())
hpnicfNqaStatResMaxDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResMaxDelayDS.setStatus(_A)
_HpnicfNqaStatResSumDelayDS_Type=Counter32
_HpnicfNqaStatResSumDelayDS_Object=MibTableColumn
hpnicfNqaStatResSumDelayDS=_HpnicfNqaStatResSumDelayDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,30),_HpnicfNqaStatResSumDelayDS_Type())
hpnicfNqaStatResSumDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResSumDelayDS.setStatus(_A)
_HpnicfNqaStatResSum2DelayDS_Type=Counter32
_HpnicfNqaStatResSum2DelayDS_Object=MibTableColumn
hpnicfNqaStatResSum2DelayDS=_HpnicfNqaStatResSum2DelayDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,11,1,31),_HpnicfNqaStatResSum2DelayDS_Type())
hpnicfNqaStatResSum2DelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatResSum2DelayDS.setStatus(_A)
_HpnicfNqaGroupStatsJitterTable_Object=MibTable
hpnicfNqaGroupStatsJitterTable=_HpnicfNqaGroupStatsJitterTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12))
if mibBuilder.loadTexts:hpnicfNqaGroupStatsJitterTable.setStatus(_A)
_HpnicfNqaGroupStatsJitterEntry_Object=MibTableRow
hpnicfNqaGroupStatsJitterEntry=_HpnicfNqaGroupStatsJitterEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1))
hpnicfNqaGroupStatsJitterEntry.setIndexNames((0,_D,_T),(0,_D,_U),(0,_C,_k))
if mibBuilder.loadTexts:hpnicfNqaGroupStatsJitterEntry.setStatus(_A)
class _HpnicfNqaStatJitterIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfNqaStatJitterIndex_Type.__name__=_H
_HpnicfNqaStatJitterIndex_Object=MibTableColumn
hpnicfNqaStatJitterIndex=_HpnicfNqaStatJitterIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,1),_HpnicfNqaStatJitterIndex_Type())
hpnicfNqaStatJitterIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfNqaStatJitterIndex.setStatus(_A)
_HpnicfNqaStatJitterMinOfPosSD_Type=Gauge32
_HpnicfNqaStatJitterMinOfPosSD_Object=MibTableColumn
hpnicfNqaStatJitterMinOfPosSD=_HpnicfNqaStatJitterMinOfPosSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,2),_HpnicfNqaStatJitterMinOfPosSD_Type())
hpnicfNqaStatJitterMinOfPosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMinOfPosSD.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMinOfPosSD.setUnits(_F)
_HpnicfNqaStatJitterMaxOfPosSD_Type=Gauge32
_HpnicfNqaStatJitterMaxOfPosSD_Object=MibTableColumn
hpnicfNqaStatJitterMaxOfPosSD=_HpnicfNqaStatJitterMaxOfPosSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,3),_HpnicfNqaStatJitterMaxOfPosSD_Type())
hpnicfNqaStatJitterMaxOfPosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMaxOfPosSD.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMaxOfPosSD.setUnits(_F)
_HpnicfNqaStatJitterNumOfPosSD_Type=Counter32
_HpnicfNqaStatJitterNumOfPosSD_Object=MibTableColumn
hpnicfNqaStatJitterNumOfPosSD=_HpnicfNqaStatJitterNumOfPosSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,4),_HpnicfNqaStatJitterNumOfPosSD_Type())
hpnicfNqaStatJitterNumOfPosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterNumOfPosSD.setStatus(_A)
_HpnicfNqaStatJitterSumOfPosSD_Type=Counter32
_HpnicfNqaStatJitterSumOfPosSD_Object=MibTableColumn
hpnicfNqaStatJitterSumOfPosSD=_HpnicfNqaStatJitterSumOfPosSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,5),_HpnicfNqaStatJitterSumOfPosSD_Type())
hpnicfNqaStatJitterSumOfPosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfPosSD.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfPosSD.setUnits(_F)
_HpnicfNqaStatJitterSumOfSquarePosSD_Type=Counter32
_HpnicfNqaStatJitterSumOfSquarePosSD_Object=MibTableColumn
hpnicfNqaStatJitterSumOfSquarePosSD=_HpnicfNqaStatJitterSumOfSquarePosSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,6),_HpnicfNqaStatJitterSumOfSquarePosSD_Type())
hpnicfNqaStatJitterSumOfSquarePosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfSquarePosSD.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfSquarePosSD.setUnits(_F)
_HpnicfNqaStatJitterMinOfNegSD_Type=Gauge32
_HpnicfNqaStatJitterMinOfNegSD_Object=MibTableColumn
hpnicfNqaStatJitterMinOfNegSD=_HpnicfNqaStatJitterMinOfNegSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,7),_HpnicfNqaStatJitterMinOfNegSD_Type())
hpnicfNqaStatJitterMinOfNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMinOfNegSD.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMinOfNegSD.setUnits(_F)
_HpnicfNqaStatJitterMaxOfNegSD_Type=Gauge32
_HpnicfNqaStatJitterMaxOfNegSD_Object=MibTableColumn
hpnicfNqaStatJitterMaxOfNegSD=_HpnicfNqaStatJitterMaxOfNegSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,8),_HpnicfNqaStatJitterMaxOfNegSD_Type())
hpnicfNqaStatJitterMaxOfNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMaxOfNegSD.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMaxOfNegSD.setUnits(_F)
_HpnicfNqaStatJitterNumOfNegSD_Type=Counter32
_HpnicfNqaStatJitterNumOfNegSD_Object=MibTableColumn
hpnicfNqaStatJitterNumOfNegSD=_HpnicfNqaStatJitterNumOfNegSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,9),_HpnicfNqaStatJitterNumOfNegSD_Type())
hpnicfNqaStatJitterNumOfNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterNumOfNegSD.setStatus(_A)
_HpnicfNqaStatJitterSumOfNegSD_Type=Counter32
_HpnicfNqaStatJitterSumOfNegSD_Object=MibTableColumn
hpnicfNqaStatJitterSumOfNegSD=_HpnicfNqaStatJitterSumOfNegSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,10),_HpnicfNqaStatJitterSumOfNegSD_Type())
hpnicfNqaStatJitterSumOfNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfNegSD.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfNegSD.setUnits(_F)
_HpnicfNqaStatJitterSumOfSquareNegSD_Type=Counter32
_HpnicfNqaStatJitterSumOfSquareNegSD_Object=MibTableColumn
hpnicfNqaStatJitterSumOfSquareNegSD=_HpnicfNqaStatJitterSumOfSquareNegSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,11),_HpnicfNqaStatJitterSumOfSquareNegSD_Type())
hpnicfNqaStatJitterSumOfSquareNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfSquareNegSD.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfSquareNegSD.setUnits(_F)
_HpnicfNqaStatJitterMinOfPosDS_Type=Gauge32
_HpnicfNqaStatJitterMinOfPosDS_Object=MibTableColumn
hpnicfNqaStatJitterMinOfPosDS=_HpnicfNqaStatJitterMinOfPosDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,12),_HpnicfNqaStatJitterMinOfPosDS_Type())
hpnicfNqaStatJitterMinOfPosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMinOfPosDS.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMinOfPosDS.setUnits(_F)
_HpnicfNqaStatJitterMaxOfPosDS_Type=Gauge32
_HpnicfNqaStatJitterMaxOfPosDS_Object=MibTableColumn
hpnicfNqaStatJitterMaxOfPosDS=_HpnicfNqaStatJitterMaxOfPosDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,13),_HpnicfNqaStatJitterMaxOfPosDS_Type())
hpnicfNqaStatJitterMaxOfPosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMaxOfPosDS.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMaxOfPosDS.setUnits(_F)
_HpnicfNqaStatJitterNumOfPosDS_Type=Counter32
_HpnicfNqaStatJitterNumOfPosDS_Object=MibTableColumn
hpnicfNqaStatJitterNumOfPosDS=_HpnicfNqaStatJitterNumOfPosDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,14),_HpnicfNqaStatJitterNumOfPosDS_Type())
hpnicfNqaStatJitterNumOfPosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterNumOfPosDS.setStatus(_A)
_HpnicfNqaStatJitterSumOfPosDS_Type=Counter32
_HpnicfNqaStatJitterSumOfPosDS_Object=MibTableColumn
hpnicfNqaStatJitterSumOfPosDS=_HpnicfNqaStatJitterSumOfPosDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,15),_HpnicfNqaStatJitterSumOfPosDS_Type())
hpnicfNqaStatJitterSumOfPosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfPosDS.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfPosDS.setUnits(_F)
_HpnicfNqaStatJitterSumOfSquarePosDS_Type=Counter32
_HpnicfNqaStatJitterSumOfSquarePosDS_Object=MibTableColumn
hpnicfNqaStatJitterSumOfSquarePosDS=_HpnicfNqaStatJitterSumOfSquarePosDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,16),_HpnicfNqaStatJitterSumOfSquarePosDS_Type())
hpnicfNqaStatJitterSumOfSquarePosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfSquarePosDS.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfSquarePosDS.setUnits(_F)
_HpnicfNqaStatJitterMinOfNegDS_Type=Gauge32
_HpnicfNqaStatJitterMinOfNegDS_Object=MibTableColumn
hpnicfNqaStatJitterMinOfNegDS=_HpnicfNqaStatJitterMinOfNegDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,17),_HpnicfNqaStatJitterMinOfNegDS_Type())
hpnicfNqaStatJitterMinOfNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMinOfNegDS.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMinOfNegDS.setUnits(_F)
_HpnicfNqaStatJitterMaxOfNegDS_Type=Gauge32
_HpnicfNqaStatJitterMaxOfNegDS_Object=MibTableColumn
hpnicfNqaStatJitterMaxOfNegDS=_HpnicfNqaStatJitterMaxOfNegDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,18),_HpnicfNqaStatJitterMaxOfNegDS_Type())
hpnicfNqaStatJitterMaxOfNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMaxOfNegDS.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMaxOfNegDS.setUnits(_F)
_HpnicfNqaStatJitterNumOfNegDS_Type=Counter32
_HpnicfNqaStatJitterNumOfNegDS_Object=MibTableColumn
hpnicfNqaStatJitterNumOfNegDS=_HpnicfNqaStatJitterNumOfNegDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,19),_HpnicfNqaStatJitterNumOfNegDS_Type())
hpnicfNqaStatJitterNumOfNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterNumOfNegDS.setStatus(_A)
_HpnicfNqaStatJitterSumOfNegDS_Type=Counter32
_HpnicfNqaStatJitterSumOfNegDS_Object=MibTableColumn
hpnicfNqaStatJitterSumOfNegDS=_HpnicfNqaStatJitterSumOfNegDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,20),_HpnicfNqaStatJitterSumOfNegDS_Type())
hpnicfNqaStatJitterSumOfNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfNegDS.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfNegDS.setUnits(_F)
_HpnicfNqaStatJitterSumOfSquareNegDS_Type=Counter32
_HpnicfNqaStatJitterSumOfSquareNegDS_Object=MibTableColumn
hpnicfNqaStatJitterSumOfSquareNegDS=_HpnicfNqaStatJitterSumOfSquareNegDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,21),_HpnicfNqaStatJitterSumOfSquareNegDS_Type())
hpnicfNqaStatJitterSumOfSquareNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfSquareNegDS.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterSumOfSquareNegDS.setUnits(_F)
_HpnicfNqaStatJitterPacketLossSD_Type=Counter32
_HpnicfNqaStatJitterPacketLossSD_Object=MibTableColumn
hpnicfNqaStatJitterPacketLossSD=_HpnicfNqaStatJitterPacketLossSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,22),_HpnicfNqaStatJitterPacketLossSD_Type())
hpnicfNqaStatJitterPacketLossSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterPacketLossSD.setStatus(_A)
_HpnicfNqaStatJitterPacketLossDS_Type=Counter32
_HpnicfNqaStatJitterPacketLossDS_Object=MibTableColumn
hpnicfNqaStatJitterPacketLossDS=_HpnicfNqaStatJitterPacketLossDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,23),_HpnicfNqaStatJitterPacketLossDS_Type())
hpnicfNqaStatJitterPacketLossDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterPacketLossDS.setStatus(_A)
_HpnicfNqaStatJitterAvePosSD_Type=Gauge32
_HpnicfNqaStatJitterAvePosSD_Object=MibTableColumn
hpnicfNqaStatJitterAvePosSD=_HpnicfNqaStatJitterAvePosSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,24),_HpnicfNqaStatJitterAvePosSD_Type())
hpnicfNqaStatJitterAvePosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterAvePosSD.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterAvePosSD.setUnits(_F)
_HpnicfNqaStatJitterAveNegSD_Type=Gauge32
_HpnicfNqaStatJitterAveNegSD_Object=MibTableColumn
hpnicfNqaStatJitterAveNegSD=_HpnicfNqaStatJitterAveNegSD_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,25),_HpnicfNqaStatJitterAveNegSD_Type())
hpnicfNqaStatJitterAveNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterAveNegSD.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterAveNegSD.setUnits(_F)
_HpnicfNqaStatJitterAvePosDS_Type=Gauge32
_HpnicfNqaStatJitterAvePosDS_Object=MibTableColumn
hpnicfNqaStatJitterAvePosDS=_HpnicfNqaStatJitterAvePosDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,26),_HpnicfNqaStatJitterAvePosDS_Type())
hpnicfNqaStatJitterAvePosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterAvePosDS.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterAvePosDS.setUnits(_F)
_HpnicfNqaStatJitterAveNegDS_Type=Gauge32
_HpnicfNqaStatJitterAveNegDS_Object=MibTableColumn
hpnicfNqaStatJitterAveNegDS=_HpnicfNqaStatJitterAveNegDS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,27),_HpnicfNqaStatJitterAveNegDS_Type())
hpnicfNqaStatJitterAveNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterAveNegDS.setStatus(_A)
if mibBuilder.loadTexts:hpnicfNqaStatJitterAveNegDS.setUnits(_F)
_HpnicfNqaStatJitterPktLossUnknown_Type=Counter32
_HpnicfNqaStatJitterPktLossUnknown_Object=MibTableColumn
hpnicfNqaStatJitterPktLossUnknown=_HpnicfNqaStatJitterPktLossUnknown_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,28),_HpnicfNqaStatJitterPktLossUnknown_Type())
hpnicfNqaStatJitterPktLossUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterPktLossUnknown.setStatus(_A)
_HpnicfNqaStatJitterMaxOfICPIF_Type=Gauge32
_HpnicfNqaStatJitterMaxOfICPIF_Object=MibTableColumn
hpnicfNqaStatJitterMaxOfICPIF=_HpnicfNqaStatJitterMaxOfICPIF_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,29),_HpnicfNqaStatJitterMaxOfICPIF_Type())
hpnicfNqaStatJitterMaxOfICPIF.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMaxOfICPIF.setStatus(_A)
_HpnicfNqaStatJitterMinOfICPIF_Type=Gauge32
_HpnicfNqaStatJitterMinOfICPIF_Object=MibTableColumn
hpnicfNqaStatJitterMinOfICPIF=_HpnicfNqaStatJitterMinOfICPIF_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,30),_HpnicfNqaStatJitterMinOfICPIF_Type())
hpnicfNqaStatJitterMinOfICPIF.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMinOfICPIF.setStatus(_A)
_HpnicfNqaStatJitterMaxOfMOS_Type=Gauge32
_HpnicfNqaStatJitterMaxOfMOS_Object=MibTableColumn
hpnicfNqaStatJitterMaxOfMOS=_HpnicfNqaStatJitterMaxOfMOS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,31),_HpnicfNqaStatJitterMaxOfMOS_Type())
hpnicfNqaStatJitterMaxOfMOS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMaxOfMOS.setStatus(_A)
_HpnicfNqaStatJitterMinOfMOS_Type=Gauge32
_HpnicfNqaStatJitterMinOfMOS_Object=MibTableColumn
hpnicfNqaStatJitterMinOfMOS=_HpnicfNqaStatJitterMinOfMOS_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,12,1,32),_HpnicfNqaStatJitterMinOfMOS_Type())
hpnicfNqaStatJitterMinOfMOS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatJitterMinOfMOS.setStatus(_A)
_HpnicfNqaReactionTable_Object=MibTable
hpnicfNqaReactionTable=_HpnicfNqaReactionTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13))
if mibBuilder.loadTexts:hpnicfNqaReactionTable.setStatus(_A)
_HpnicfNqaReactionEntry_Object=MibTableRow
hpnicfNqaReactionEntry=_HpnicfNqaReactionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1))
hpnicfNqaReactionEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:hpnicfNqaReactionEntry.setStatus(_A)
class _HpnicfNqaReactOwnerIndex_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfNqaReactOwnerIndex_Type.__name__=_V
_HpnicfNqaReactOwnerIndex_Object=MibTableColumn
hpnicfNqaReactOwnerIndex=_HpnicfNqaReactOwnerIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,1),_HpnicfNqaReactOwnerIndex_Type())
hpnicfNqaReactOwnerIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:hpnicfNqaReactOwnerIndex.setStatus(_A)
class _HpnicfNqaReactTestName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfNqaReactTestName_Type.__name__=_V
_HpnicfNqaReactTestName_Object=MibTableColumn
hpnicfNqaReactTestName=_HpnicfNqaReactTestName_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,2),_HpnicfNqaReactTestName_Type())
hpnicfNqaReactTestName.setMaxAccess(_Z)
if mibBuilder.loadTexts:hpnicfNqaReactTestName.setStatus(_A)
class _HpnicfNqaReactItemIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HpnicfNqaReactItemIndex_Type.__name__=_H
_HpnicfNqaReactItemIndex_Object=MibTableColumn
hpnicfNqaReactItemIndex=_HpnicfNqaReactItemIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,3),_HpnicfNqaReactItemIndex_Type())
hpnicfNqaReactItemIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:hpnicfNqaReactItemIndex.setStatus(_A)
class _HpnicfNqaReactCheckedElement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('probetime',1),('probefailure',2),('jitterrtt',3),('jitterpacketloss',4),('jittersd',5),('jitterds',6),('icpif',7),('mos',8),('jitterOwdSD',9),('jitterOwdDS',10)))
_HpnicfNqaReactCheckedElement_Type.__name__=_G
_HpnicfNqaReactCheckedElement_Object=MibTableColumn
hpnicfNqaReactCheckedElement=_HpnicfNqaReactCheckedElement_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,4),_HpnicfNqaReactCheckedElement_Type())
hpnicfNqaReactCheckedElement.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaReactCheckedElement.setStatus(_A)
class _HpnicfNqaReactThresholdUpperLimit_Type(Unsigned32):defaultValue=0
_HpnicfNqaReactThresholdUpperLimit_Type.__name__=_H
_HpnicfNqaReactThresholdUpperLimit_Object=MibTableColumn
hpnicfNqaReactThresholdUpperLimit=_HpnicfNqaReactThresholdUpperLimit_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,5),_HpnicfNqaReactThresholdUpperLimit_Type())
hpnicfNqaReactThresholdUpperLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaReactThresholdUpperLimit.setStatus(_A)
class _HpnicfNqaReactThresholdLowerLimit_Type(Unsigned32):defaultValue=0
_HpnicfNqaReactThresholdLowerLimit_Type.__name__=_H
_HpnicfNqaReactThresholdLowerLimit_Object=MibTableColumn
hpnicfNqaReactThresholdLowerLimit=_HpnicfNqaReactThresholdLowerLimit_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,6),_HpnicfNqaReactThresholdLowerLimit_Type())
hpnicfNqaReactThresholdLowerLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaReactThresholdLowerLimit.setStatus(_A)
class _HpnicfNqaReactThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_l,0),('average',1),('consecutive',2),('accumulative',3)))
_HpnicfNqaReactThresholdType_Type.__name__=_G
_HpnicfNqaReactThresholdType_Object=MibTableColumn
hpnicfNqaReactThresholdType=_HpnicfNqaReactThresholdType_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,7),_HpnicfNqaReactThresholdType_Type())
hpnicfNqaReactThresholdType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaReactThresholdType.setStatus(_A)
class _HpnicfNqaReactThresholdConsecNum_Type(Unsigned32):defaultValue=0
_HpnicfNqaReactThresholdConsecNum_Type.__name__=_H
_HpnicfNqaReactThresholdConsecNum_Object=MibTableColumn
hpnicfNqaReactThresholdConsecNum=_HpnicfNqaReactThresholdConsecNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,8),_HpnicfNqaReactThresholdConsecNum_Type())
hpnicfNqaReactThresholdConsecNum.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaReactThresholdConsecNum.setStatus(_A)
class _HpnicfNqaReactThresholdAccumNum_Type(Unsigned32):defaultValue=0
_HpnicfNqaReactThresholdAccumNum_Type.__name__=_H
_HpnicfNqaReactThresholdAccumNum_Object=MibTableColumn
hpnicfNqaReactThresholdAccumNum=_HpnicfNqaReactThresholdAccumNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,9),_HpnicfNqaReactThresholdAccumNum_Type())
hpnicfNqaReactThresholdAccumNum.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaReactThresholdAccumNum.setStatus(_A)
class _HpnicfNqaReactActionType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('trapOnly',1),('triggerOnly',2),('trapAndTrigger',3)))
_HpnicfNqaReactActionType_Type.__name__=_G
_HpnicfNqaReactActionType_Object=MibTableColumn
hpnicfNqaReactActionType=_HpnicfNqaReactActionType_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,10),_HpnicfNqaReactActionType_Type())
hpnicfNqaReactActionType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaReactActionType.setStatus(_A)
class _HpnicfNqaReactCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),('overThreshold',2),('belowThreshold',3)))
_HpnicfNqaReactCurrentStatus_Type.__name__=_G
_HpnicfNqaReactCurrentStatus_Object=MibTableColumn
hpnicfNqaReactCurrentStatus=_HpnicfNqaReactCurrentStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,11),_HpnicfNqaReactCurrentStatus_Type())
hpnicfNqaReactCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaReactCurrentStatus.setStatus(_A)
_HpnicfNqaReactRowStatus_Type=RowStatus
_HpnicfNqaReactRowStatus_Object=MibTableColumn
hpnicfNqaReactRowStatus=_HpnicfNqaReactRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,12),_HpnicfNqaReactRowStatus_Type())
hpnicfNqaReactRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfNqaReactRowStatus.setStatus(_A)
class _HpnicfNqaReactCheckedNum_Type(Unsigned32):defaultValue=0
_HpnicfNqaReactCheckedNum_Type.__name__=_H
_HpnicfNqaReactCheckedNum_Object=MibTableColumn
hpnicfNqaReactCheckedNum=_HpnicfNqaReactCheckedNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,13),_HpnicfNqaReactCheckedNum_Type())
hpnicfNqaReactCheckedNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaReactCheckedNum.setStatus(_A)
class _HpnicfNqaReactThresholdNum_Type(Unsigned32):defaultValue=0
_HpnicfNqaReactThresholdNum_Type.__name__=_H
_HpnicfNqaReactThresholdNum_Object=MibTableColumn
hpnicfNqaReactThresholdNum=_HpnicfNqaReactThresholdNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,13,1,14),_HpnicfNqaReactThresholdNum_Type())
hpnicfNqaReactThresholdNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaReactThresholdNum.setStatus(_A)
_HpnicfNqaStatisticsReactionTable_Object=MibTable
hpnicfNqaStatisticsReactionTable=_HpnicfNqaStatisticsReactionTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,14))
if mibBuilder.loadTexts:hpnicfNqaStatisticsReactionTable.setStatus(_A)
_HpnicfNqaStatisticsReactionEntry_Object=MibTableRow
hpnicfNqaStatisticsReactionEntry=_HpnicfNqaStatisticsReactionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,14,1))
hpnicfNqaStatisticsReactionEntry.setIndexNames((0,_C,_m),(0,_C,_n),(0,_C,_o),(0,_C,_p))
if mibBuilder.loadTexts:hpnicfNqaStatisticsReactionEntry.setStatus(_A)
class _HpnicfNqaStatReactOwnerIndex_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfNqaStatReactOwnerIndex_Type.__name__=_V
_HpnicfNqaStatReactOwnerIndex_Object=MibTableColumn
hpnicfNqaStatReactOwnerIndex=_HpnicfNqaStatReactOwnerIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,14,1,1),_HpnicfNqaStatReactOwnerIndex_Type())
hpnicfNqaStatReactOwnerIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfNqaStatReactOwnerIndex.setStatus(_A)
class _HpnicfNqaStatReactTestName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfNqaStatReactTestName_Type.__name__=_V
_HpnicfNqaStatReactTestName_Object=MibTableColumn
hpnicfNqaStatReactTestName=_HpnicfNqaStatReactTestName_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,14,1,2),_HpnicfNqaStatReactTestName_Type())
hpnicfNqaStatReactTestName.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfNqaStatReactTestName.setStatus(_A)
class _HpnicfNqaStatReactIndex_Type(Unsigned32):defaultValue=0
_HpnicfNqaStatReactIndex_Type.__name__=_H
_HpnicfNqaStatReactIndex_Object=MibTableColumn
hpnicfNqaStatReactIndex=_HpnicfNqaStatReactIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,14,1,3),_HpnicfNqaStatReactIndex_Type())
hpnicfNqaStatReactIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfNqaStatReactIndex.setStatus(_A)
class _HpnicfNqaStatReactItemIndex_Type(Unsigned32):defaultValue=0
_HpnicfNqaStatReactItemIndex_Type.__name__=_H
_HpnicfNqaStatReactItemIndex_Object=MibTableColumn
hpnicfNqaStatReactItemIndex=_HpnicfNqaStatReactItemIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,14,1,4),_HpnicfNqaStatReactItemIndex_Type())
hpnicfNqaStatReactItemIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfNqaStatReactItemIndex.setStatus(_A)
class _HpnicfNqaStatReactCheckedNum_Type(Counter32):defaultValue=0
_HpnicfNqaStatReactCheckedNum_Type.__name__=_X
_HpnicfNqaStatReactCheckedNum_Object=MibTableColumn
hpnicfNqaStatReactCheckedNum=_HpnicfNqaStatReactCheckedNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,14,1,5),_HpnicfNqaStatReactCheckedNum_Type())
hpnicfNqaStatReactCheckedNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatReactCheckedNum.setStatus(_A)
class _HpnicfNqaStatReactThresholdNum_Type(Counter32):defaultValue=0
_HpnicfNqaStatReactThresholdNum_Type.__name__=_X
_HpnicfNqaStatReactThresholdNum_Object=MibTableColumn
hpnicfNqaStatReactThresholdNum=_HpnicfNqaStatReactThresholdNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,3,1,14,1,6),_HpnicfNqaStatReactThresholdNum_Type())
hpnicfNqaStatReactThresholdNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNqaStatReactThresholdNum.setStatus(_A)
_HpnicfNqaImplementationTypeDomains_ObjectIdentity=ObjectIdentity
hpnicfNqaImplementationTypeDomains=_HpnicfNqaImplementationTypeDomains_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,3,2))
_HpnicfNqaUdpEcho_ObjectIdentity=ObjectIdentity
hpnicfNqaUdpEcho=_HpnicfNqaUdpEcho_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,3,2,1))
if mibBuilder.loadTexts:hpnicfNqaUdpEcho.setStatus(_A)
_HpnicfNqaTcpconnect_ObjectIdentity=ObjectIdentity
hpnicfNqaTcpconnect=_HpnicfNqaTcpconnect_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,3,2,2))
if mibBuilder.loadTexts:hpnicfNqaTcpconnect.setStatus(_A)
_HpnicfNqajitter_ObjectIdentity=ObjectIdentity
hpnicfNqajitter=_HpnicfNqajitter_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,3,2,3))
if mibBuilder.loadTexts:hpnicfNqajitter.setStatus(_A)
_HpnicfNqaHttp_ObjectIdentity=ObjectIdentity
hpnicfNqaHttp=_HpnicfNqaHttp_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,3,2,4))
if mibBuilder.loadTexts:hpnicfNqaHttp.setStatus(_A)
_HpnicfNqadlsw_ObjectIdentity=ObjectIdentity
hpnicfNqadlsw=_HpnicfNqadlsw_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,3,2,5))
if mibBuilder.loadTexts:hpnicfNqadlsw.setStatus(_A)
_HpnicfNqadhcp_ObjectIdentity=ObjectIdentity
hpnicfNqadhcp=_HpnicfNqadhcp_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,3,2,6))
if mibBuilder.loadTexts:hpnicfNqadhcp.setStatus(_A)
_HpnicfNqaftp_ObjectIdentity=ObjectIdentity
hpnicfNqaftp=_HpnicfNqaftp_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,3,2,7))
if mibBuilder.loadTexts:hpnicfNqaftp.setStatus(_A)
_HpnicfNqaNotifications_ObjectIdentity=ObjectIdentity
hpnicfNqaNotifications=_HpnicfNqaNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,3,3))
pingCtlEntry.registerAugmentions((_C,_q))
hpnicfNqaCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())
pingCtlEntry.registerAugmentions((_C,_r))
hpnicfNqaStatisticsCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())
hpnicfNqaProbeTimeOverThreshold=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,3,3,1))
hpnicfNqaProbeTimeOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:hpnicfNqaProbeTimeOverThreshold.setStatus(_A)
hpnicfNqaJitterRTTOverThreshold=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,3,3,2))
hpnicfNqaJitterRTTOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:hpnicfNqaJitterRTTOverThreshold.setStatus(_A)
hpnicfNqaProbeFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,3,3,3))
hpnicfNqaProbeFailure.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:hpnicfNqaProbeFailure.setStatus(_A)
hpnicfNqaJitterPacketLoss=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,3,3,4))
hpnicfNqaJitterPacketLoss.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:hpnicfNqaJitterPacketLoss.setStatus(_A)
hpnicfNqaJitterSDOverThreshold=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,3,3,5))
hpnicfNqaJitterSDOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:hpnicfNqaJitterSDOverThreshold.setStatus(_A)
hpnicfNqaJitterDSOverThreshold=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,3,3,6))
hpnicfNqaJitterDSOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:hpnicfNqaJitterDSOverThreshold.setStatus(_A)
hpnicfNqaICPIFOverThreshold=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,3,3,7))
hpnicfNqaICPIFOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_Q)))
if mibBuilder.loadTexts:hpnicfNqaICPIFOverThreshold.setStatus(_A)
hpnicfNqaMOSOverThreshold=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,3,3,8))
hpnicfNqaMOSOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_Q)))
if mibBuilder.loadTexts:hpnicfNqaMOSOverThreshold.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfNqa':hpnicfNqa,'hpnicfNqaObjects':hpnicfNqaObjects,'hpnicfNqaMIBVersion':hpnicfNqaMIBVersion,'hpnicfNqaCtlTable':hpnicfNqaCtlTable,_q:hpnicfNqaCtlEntry,'hpnicfNqaCtlTargetPort':hpnicfNqaCtlTargetPort,'hpnicfNqaCtlSourcePort':hpnicfNqaCtlSourcePort,'hpnicfNqaCtlTTL':hpnicfNqaCtlTTL,'hpnicfNqaCtlJitterAdminInterval':hpnicfNqaCtlJitterAdminInterval,'hpnicfNqaCtlJitterAdminNumPackets':hpnicfNqaCtlJitterAdminNumPackets,'hpnicfNqaCtlHttpOperationType':hpnicfNqaCtlHttpOperationType,'hpnicfNqaCtlHttpOperationString':hpnicfNqaCtlHttpOperationString,'hpnicfNqaCtlFtpOperationType':hpnicfNqaCtlFtpOperationType,'hpnicfNqaCtlFtpUsername':hpnicfNqaCtlFtpUsername,'hpnicfNqaCtlFtpPassword':hpnicfNqaCtlFtpPassword,'hpnicfNqaCtlFtpOperationString':hpnicfNqaCtlFtpOperationString,'hpnicfNqaCtlVPNInstance':hpnicfNqaCtlVPNInstance,'hpnicfNqaCtlHistoryKeptTime':hpnicfNqaCtlHistoryKeptTime,'hpnicfNqaCtlHistoryEnable':hpnicfNqaCtlHistoryEnable,'hpnicfNqaCtlICPIFAdvFactor':hpnicfNqaCtlICPIFAdvFactor,'hpnicfNqaCtlCodecType':hpnicfNqaCtlCodecType,'hpnicfNqaResultsTable':hpnicfNqaResultsTable,'hpnicfNqaResultsEntry':hpnicfNqaResultsEntry,'hpnicfNqaResultsRttNumDisconnects':hpnicfNqaResultsRttNumDisconnects,'hpnicfNqaResultsRttTimeouts':hpnicfNqaResultsRttTimeouts,'hpnicfNqaResultsRttBusies':hpnicfNqaResultsRttBusies,'hpnicfNqaResultsRttNoConnections':hpnicfNqaResultsRttNoConnections,'hpnicfNqaResultsRttDrops':hpnicfNqaResultsRttDrops,'hpnicfNqaResultsRttSequenceErrors':hpnicfNqaResultsRttSequenceErrors,'hpnicfNqaResultsRttStatsErrors':hpnicfNqaResultsRttStatsErrors,'hpnicfNqaResultsMaxDelaySD':hpnicfNqaResultsMaxDelaySD,'hpnicfNqaResultsMaxDelayDS':hpnicfNqaResultsMaxDelayDS,'hpnicfNqaResultsLostPacketRatio':hpnicfNqaResultsLostPacketRatio,'hpnicfNqaResultsPacketLateArrival':hpnicfNqaResultsPacketLateArrival,'hpnicfNqaResultsRttSum':hpnicfNqaResultsRttSum,'hpnicfNqaResultsNumOfDelaySD':hpnicfNqaResultsNumOfDelaySD,'hpnicfNqaResultsMinDelaySD':hpnicfNqaResultsMinDelaySD,'hpnicfNqaResultsSumDelaySD':hpnicfNqaResultsSumDelaySD,'hpnicfNqaResultsSum2DelaySD':hpnicfNqaResultsSum2DelaySD,'hpnicfNqaResultsNumOfDelayDS':hpnicfNqaResultsNumOfDelayDS,'hpnicfNqaResultsMinDelayDS':hpnicfNqaResultsMinDelayDS,'hpnicfNqaResultsSumDelayDS':hpnicfNqaResultsSumDelayDS,'hpnicfNqaResultsSum2DelayDS':hpnicfNqaResultsSum2DelayDS,'hpnicfNqaJitterStatsTable':hpnicfNqaJitterStatsTable,'hpnicfNqaJitterStatsEntry':hpnicfNqaJitterStatsEntry,'hpnicfNqaJitterStatsNumOfRTT':hpnicfNqaJitterStatsNumOfRTT,'hpnicfNqaJitterStatsMinOfPositivesSD':hpnicfNqaJitterStatsMinOfPositivesSD,'hpnicfNqaJitterStatsMaxOfPositivesSD':hpnicfNqaJitterStatsMaxOfPositivesSD,'hpnicfNqaJitterStatsNumOfPositivesSD':hpnicfNqaJitterStatsNumOfPositivesSD,'hpnicfNqaJitterStatsSumOfPositivesSD':hpnicfNqaJitterStatsSumOfPositivesSD,'hpnicfNqaJitterStatsSum2PositivesSD':hpnicfNqaJitterStatsSum2PositivesSD,'hpnicfNqaJitterStatsMinOfNegativesSD':hpnicfNqaJitterStatsMinOfNegativesSD,'hpnicfNqaJitterStatsMaxOfNegativesSD':hpnicfNqaJitterStatsMaxOfNegativesSD,'hpnicfNqaJitterStatsNumOfNegativesSD':hpnicfNqaJitterStatsNumOfNegativesSD,'hpnicfNqaJitterStatsSumOfNegativesSD':hpnicfNqaJitterStatsSumOfNegativesSD,'hpnicfNqaJitterStatsSum2NegativesSD':hpnicfNqaJitterStatsSum2NegativesSD,'hpnicfNqaJitterStatsMinOfPositivesDS':hpnicfNqaJitterStatsMinOfPositivesDS,'hpnicfNqaJitterStatsMaxOfPositivesDS':hpnicfNqaJitterStatsMaxOfPositivesDS,'hpnicfNqaJitterStatsNumOfPositivesDS':hpnicfNqaJitterStatsNumOfPositivesDS,'hpnicfNqaJitterStatsSumOfPositivesDS':hpnicfNqaJitterStatsSumOfPositivesDS,'hpnicfNqaJitterStatsSum2PositivesDS':hpnicfNqaJitterStatsSum2PositivesDS,'hpnicfNqaJitterStatsMinOfNegativesDS':hpnicfNqaJitterStatsMinOfNegativesDS,'hpnicfNqaJitterStatsMaxOfNegativesDS':hpnicfNqaJitterStatsMaxOfNegativesDS,'hpnicfNqaJitterStatsNumOfNegativesDS':hpnicfNqaJitterStatsNumOfNegativesDS,'hpnicfNqaJitterStatsSumOfNegativesDS':hpnicfNqaJitterStatsSumOfNegativesDS,'hpnicfNqaJitterStatsSum2NegativesDS':hpnicfNqaJitterStatsSum2NegativesDS,'hpnicfNqaJitterStatsPacketLossSD':hpnicfNqaJitterStatsPacketLossSD,'hpnicfNqaJitterStatsPacketLossDS':hpnicfNqaJitterStatsPacketLossDS,'hpnicfNqaJitterStatsAvePositivesSD':hpnicfNqaJitterStatsAvePositivesSD,'hpnicfNqaJitterStatsAveNegativesSD':hpnicfNqaJitterStatsAveNegativesSD,'hpnicfNqaJitterStatsAvePositivesDS':hpnicfNqaJitterStatsAvePositivesDS,'hpnicfNqaJitterStatsAveNegativesDS':hpnicfNqaJitterStatsAveNegativesDS,'hpnicfNqaJitterStatsPktLossUnknown':hpnicfNqaJitterStatsPktLossUnknown,'hpnicfNqaJitterStatsOperOfICPIF':hpnicfNqaJitterStatsOperOfICPIF,'hpnicfNqaJitterStatsOperOfMOS':hpnicfNqaJitterStatsOperOfMOS,'hpnicfNqaAgentEnable':hpnicfNqaAgentEnable,'hpnicfNqaTcpServerTable':hpnicfNqaTcpServerTable,'hpnicfNqaTcpServerEntry':hpnicfNqaTcpServerEntry,_e:hpnicfNqaTcpServerIpAddress,_f:hpnicfNqaTcpServerPort,'hpnicfNqaTcpServerRowStatus':hpnicfNqaTcpServerRowStatus,'hpnicfNqaUdpServerTable':hpnicfNqaUdpServerTable,'hpnicfNqaUdpServerEntry':hpnicfNqaUdpServerEntry,_g:hpnicfNqaUdpServerIpAddress,_h:hpnicfNqaUdpServerPort,'hpnicfNqaUdpServerRowStatus':hpnicfNqaUdpServerRowStatus,'hpnicfNqaServerEnable':hpnicfNqaServerEnable,'hpnicfNqaStatsMaxGroupNumber':hpnicfNqaStatsMaxGroupNumber,'hpnicfNqaStatisticsCtlTable':hpnicfNqaStatisticsCtlTable,_r:hpnicfNqaStatisticsCtlEntry,'hpnicfNqaCtlStatisticsInterval':hpnicfNqaCtlStatisticsInterval,'hpnicfNqaCtlStatisticsGroupNumber':hpnicfNqaCtlStatisticsGroupNumber,'hpnicfNqaCtlStatisticsKeptTime':hpnicfNqaCtlStatisticsKeptTime,'hpnicfNqaCtlBeginTime':hpnicfNqaCtlBeginTime,'hpnicfNqaCtlLifeTime':hpnicfNqaCtlLifeTime,'hpnicfNqaStatisticsResultsTable':hpnicfNqaStatisticsResultsTable,'hpnicfNqaStatisticsResultsEntry':hpnicfNqaStatisticsResultsEntry,_j:hpnicfNqaStatResIndex,'hpnicfNqaStatResIpTargetAddressType':hpnicfNqaStatResIpTargetAddressType,'hpnicfNqaStatResIpTargetAddress':hpnicfNqaStatResIpTargetAddress,'hpnicfNqaStatResMinRtt':hpnicfNqaStatResMinRtt,'hpnicfNqaStatResMaxRtt':hpnicfNqaStatResMaxRtt,'hpnicfNqaStatResAverageRtt':hpnicfNqaStatResAverageRtt,'hpnicfNqaStatResProbeResponses':hpnicfNqaStatResProbeResponses,'hpnicfNqaStatResSentProbes':hpnicfNqaStatResSentProbes,'hpnicfNqaStatResRttSumOfSquares':hpnicfNqaStatResRttSumOfSquares,'hpnicfNqaStatResStartTime':hpnicfNqaStatResStartTime,'hpnicfNqaStatResInterval':hpnicfNqaStatResInterval,'hpnicfNqaStatResRttNumDisconnects':hpnicfNqaStatResRttNumDisconnects,'hpnicfNqaStatResRttTimeouts':hpnicfNqaStatResRttTimeouts,'hpnicfNqaStatResRttBusies':hpnicfNqaStatResRttBusies,'hpnicfNqaStatResRttNoConnections':hpnicfNqaStatResRttNoConnections,'hpnicfNqaStatResRttDrops':hpnicfNqaStatResRttDrops,'hpnicfNqaStatResRttSequenceErrors':hpnicfNqaStatResRttSequenceErrors,'hpnicfNqaStatResRttErrors':hpnicfNqaStatResRttErrors,'hpnicfNqaStatResLostPacketRatio':hpnicfNqaStatResLostPacketRatio,'hpnicfNqaStatResPacketLateArrival':hpnicfNqaStatResPacketLateArrival,'hpnicfNqaStatResRttSum':hpnicfNqaStatResRttSum,'hpnicfNqaStatResNumOfDelaySD':hpnicfNqaStatResNumOfDelaySD,'hpnicfNqaStatResMinDelaySD':hpnicfNqaStatResMinDelaySD,'hpnicfNqaStatResMaxDelaySD':hpnicfNqaStatResMaxDelaySD,'hpnicfNqaStatResSumDelaySD':hpnicfNqaStatResSumDelaySD,'hpnicfNqaStatResSum2DelaySD':hpnicfNqaStatResSum2DelaySD,'hpnicfNqaStatResNumOfDelayDS':hpnicfNqaStatResNumOfDelayDS,'hpnicfNqaStatResMinDelayDS':hpnicfNqaStatResMinDelayDS,'hpnicfNqaStatResMaxDelayDS':hpnicfNqaStatResMaxDelayDS,'hpnicfNqaStatResSumDelayDS':hpnicfNqaStatResSumDelayDS,'hpnicfNqaStatResSum2DelayDS':hpnicfNqaStatResSum2DelayDS,'hpnicfNqaGroupStatsJitterTable':hpnicfNqaGroupStatsJitterTable,'hpnicfNqaGroupStatsJitterEntry':hpnicfNqaGroupStatsJitterEntry,_k:hpnicfNqaStatJitterIndex,'hpnicfNqaStatJitterMinOfPosSD':hpnicfNqaStatJitterMinOfPosSD,'hpnicfNqaStatJitterMaxOfPosSD':hpnicfNqaStatJitterMaxOfPosSD,'hpnicfNqaStatJitterNumOfPosSD':hpnicfNqaStatJitterNumOfPosSD,'hpnicfNqaStatJitterSumOfPosSD':hpnicfNqaStatJitterSumOfPosSD,'hpnicfNqaStatJitterSumOfSquarePosSD':hpnicfNqaStatJitterSumOfSquarePosSD,'hpnicfNqaStatJitterMinOfNegSD':hpnicfNqaStatJitterMinOfNegSD,'hpnicfNqaStatJitterMaxOfNegSD':hpnicfNqaStatJitterMaxOfNegSD,'hpnicfNqaStatJitterNumOfNegSD':hpnicfNqaStatJitterNumOfNegSD,'hpnicfNqaStatJitterSumOfNegSD':hpnicfNqaStatJitterSumOfNegSD,'hpnicfNqaStatJitterSumOfSquareNegSD':hpnicfNqaStatJitterSumOfSquareNegSD,'hpnicfNqaStatJitterMinOfPosDS':hpnicfNqaStatJitterMinOfPosDS,'hpnicfNqaStatJitterMaxOfPosDS':hpnicfNqaStatJitterMaxOfPosDS,'hpnicfNqaStatJitterNumOfPosDS':hpnicfNqaStatJitterNumOfPosDS,'hpnicfNqaStatJitterSumOfPosDS':hpnicfNqaStatJitterSumOfPosDS,'hpnicfNqaStatJitterSumOfSquarePosDS':hpnicfNqaStatJitterSumOfSquarePosDS,'hpnicfNqaStatJitterMinOfNegDS':hpnicfNqaStatJitterMinOfNegDS,'hpnicfNqaStatJitterMaxOfNegDS':hpnicfNqaStatJitterMaxOfNegDS,'hpnicfNqaStatJitterNumOfNegDS':hpnicfNqaStatJitterNumOfNegDS,'hpnicfNqaStatJitterSumOfNegDS':hpnicfNqaStatJitterSumOfNegDS,'hpnicfNqaStatJitterSumOfSquareNegDS':hpnicfNqaStatJitterSumOfSquareNegDS,'hpnicfNqaStatJitterPacketLossSD':hpnicfNqaStatJitterPacketLossSD,'hpnicfNqaStatJitterPacketLossDS':hpnicfNqaStatJitterPacketLossDS,'hpnicfNqaStatJitterAvePosSD':hpnicfNqaStatJitterAvePosSD,'hpnicfNqaStatJitterAveNegSD':hpnicfNqaStatJitterAveNegSD,'hpnicfNqaStatJitterAvePosDS':hpnicfNqaStatJitterAvePosDS,'hpnicfNqaStatJitterAveNegDS':hpnicfNqaStatJitterAveNegDS,'hpnicfNqaStatJitterPktLossUnknown':hpnicfNqaStatJitterPktLossUnknown,'hpnicfNqaStatJitterMaxOfICPIF':hpnicfNqaStatJitterMaxOfICPIF,'hpnicfNqaStatJitterMinOfICPIF':hpnicfNqaStatJitterMinOfICPIF,'hpnicfNqaStatJitterMaxOfMOS':hpnicfNqaStatJitterMaxOfMOS,'hpnicfNqaStatJitterMinOfMOS':hpnicfNqaStatJitterMinOfMOS,'hpnicfNqaReactionTable':hpnicfNqaReactionTable,'hpnicfNqaReactionEntry':hpnicfNqaReactionEntry,_J:hpnicfNqaReactOwnerIndex,_K:hpnicfNqaReactTestName,_L:hpnicfNqaReactItemIndex,'hpnicfNqaReactCheckedElement':hpnicfNqaReactCheckedElement,'hpnicfNqaReactThresholdUpperLimit':hpnicfNqaReactThresholdUpperLimit,'hpnicfNqaReactThresholdLowerLimit':hpnicfNqaReactThresholdLowerLimit,_R:hpnicfNqaReactThresholdType,'hpnicfNqaReactThresholdConsecNum':hpnicfNqaReactThresholdConsecNum,'hpnicfNqaReactThresholdAccumNum':hpnicfNqaReactThresholdAccumNum,'hpnicfNqaReactActionType':hpnicfNqaReactActionType,_Q:hpnicfNqaReactCurrentStatus,'hpnicfNqaReactRowStatus':hpnicfNqaReactRowStatus,'hpnicfNqaReactCheckedNum':hpnicfNqaReactCheckedNum,'hpnicfNqaReactThresholdNum':hpnicfNqaReactThresholdNum,'hpnicfNqaStatisticsReactionTable':hpnicfNqaStatisticsReactionTable,'hpnicfNqaStatisticsReactionEntry':hpnicfNqaStatisticsReactionEntry,_m:hpnicfNqaStatReactOwnerIndex,_n:hpnicfNqaStatReactTestName,_o:hpnicfNqaStatReactIndex,_p:hpnicfNqaStatReactItemIndex,'hpnicfNqaStatReactCheckedNum':hpnicfNqaStatReactCheckedNum,'hpnicfNqaStatReactThresholdNum':hpnicfNqaStatReactThresholdNum,'hpnicfNqaImplementationTypeDomains':hpnicfNqaImplementationTypeDomains,'hpnicfNqaUdpEcho':hpnicfNqaUdpEcho,'hpnicfNqaTcpconnect':hpnicfNqaTcpconnect,'hpnicfNqajitter':hpnicfNqajitter,'hpnicfNqaHttp':hpnicfNqaHttp,'hpnicfNqadlsw':hpnicfNqadlsw,'hpnicfNqadhcp':hpnicfNqadhcp,'hpnicfNqaftp':hpnicfNqaftp,'hpnicfNqaNotifications':hpnicfNqaNotifications,'hpnicfNqaProbeTimeOverThreshold':hpnicfNqaProbeTimeOverThreshold,'hpnicfNqaJitterRTTOverThreshold':hpnicfNqaJitterRTTOverThreshold,'hpnicfNqaProbeFailure':hpnicfNqaProbeFailure,'hpnicfNqaJitterPacketLoss':hpnicfNqaJitterPacketLoss,'hpnicfNqaJitterSDOverThreshold':hpnicfNqaJitterSDOverThreshold,'hpnicfNqaJitterDSOverThreshold':hpnicfNqaJitterDSOverThreshold,'hpnicfNqaICPIFOverThreshold':hpnicfNqaICPIFOverThreshold,'hpnicfNqaMOSOverThreshold':hpnicfNqaMOSOverThreshold})