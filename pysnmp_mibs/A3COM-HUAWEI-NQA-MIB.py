_r='hwNqaStatisticsCtlEntry'
_q='hwNqaCtlEntry'
_p='hwNqaStatReactItemIndex'
_o='hwNqaStatReactIndex'
_n='hwNqaStatReactTestName'
_m='hwNqaStatReactOwnerIndex'
_l='invalid'
_k='hwNqaStatJitterIndex'
_j='hwNqaStatResIndex'
_i='seconds'
_h='hwNqaUdpServerPort'
_g='hwNqaUdpServerIpAddress'
_f='hwNqaTcpServerPort'
_e='hwNqaTcpServerIpAddress'
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
_R='hwNqaReactThresholdType'
_Q='hwNqaReactCurrentStatus'
_P='pingCtlType'
_O='pingCtlTargetAddressType'
_N='pingCtlTargetAddress'
_M='pingCtlDescr'
_L='hwNqaReactItemIndex'
_K='hwNqaReactTestName'
_J='hwNqaReactOwnerIndex'
_I='not-accessible'
_H='Unsigned32'
_G='Integer32'
_F='milliseconds'
_E='read-create'
_D='DISMAN-PING-MIB'
_C='A3COM-HUAWEI-NQA-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huaweiDatacomm,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','huaweiDatacomm')
pingCtlDescr,pingCtlEntry,pingCtlOwnerIndex,pingCtlTargetAddress,pingCtlTargetAddressType,pingCtlTestName,pingCtlType=mibBuilder.importSymbols(_D,_M,'pingCtlEntry',_T,_N,_O,_U,_P)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_W,_a)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_V)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_X,'Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_S,'PhysAddress','RowStatus','TextualConvention')
hwNqa=ModuleIdentity((1,3,6,1,4,1,43,45,1,5,25,28))
_HwNqaObjects_ObjectIdentity=ObjectIdentity
hwNqaObjects=_HwNqaObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,28,1))
_HwNqaMIBVersion_Type=DisplayString
_HwNqaMIBVersion_Object=MibScalar
hwNqaMIBVersion=_HwNqaMIBVersion_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,1),_HwNqaMIBVersion_Type())
hwNqaMIBVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaMIBVersion.setStatus(_A)
_HwNqaCtlTable_Object=MibTable
hwNqaCtlTable=_HwNqaCtlTable_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2))
if mibBuilder.loadTexts:hwNqaCtlTable.setStatus(_A)
_HwNqaCtlEntry_Object=MibTableRow
hwNqaCtlEntry=_HwNqaCtlEntry_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1))
if mibBuilder.loadTexts:hwNqaCtlEntry.setStatus(_A)
class _HwNqaCtlTargetPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_HwNqaCtlTargetPort_Type.__name__=_G
_HwNqaCtlTargetPort_Object=MibTableColumn
hwNqaCtlTargetPort=_HwNqaCtlTargetPort_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,1),_HwNqaCtlTargetPort_Type())
hwNqaCtlTargetPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlTargetPort.setStatus(_A)
class _HwNqaCtlSourcePort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_HwNqaCtlSourcePort_Type.__name__=_G
_HwNqaCtlSourcePort_Object=MibTableColumn
hwNqaCtlSourcePort=_HwNqaCtlSourcePort_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,2),_HwNqaCtlSourcePort_Type())
hwNqaCtlSourcePort.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlSourcePort.setStatus(_A)
class _HwNqaCtlTTL_Type(Integer32):defaultValue=20
_HwNqaCtlTTL_Type.__name__=_G
_HwNqaCtlTTL_Object=MibTableColumn
hwNqaCtlTTL=_HwNqaCtlTTL_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,3),_HwNqaCtlTTL_Type())
hwNqaCtlTTL.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlTTL.setStatus(_A)
class _HwNqaCtlJitterAdminInterval_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_HwNqaCtlJitterAdminInterval_Type.__name__=_G
_HwNqaCtlJitterAdminInterval_Object=MibTableColumn
hwNqaCtlJitterAdminInterval=_HwNqaCtlJitterAdminInterval_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,4),_HwNqaCtlJitterAdminInterval_Type())
hwNqaCtlJitterAdminInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlJitterAdminInterval.setStatus(_A)
if mibBuilder.loadTexts:hwNqaCtlJitterAdminInterval.setUnits(_F)
class _HwNqaCtlJitterAdminNumPackets_Type(Integer32):defaultValue=10
_HwNqaCtlJitterAdminNumPackets_Type.__name__=_G
_HwNqaCtlJitterAdminNumPackets_Object=MibTableColumn
hwNqaCtlJitterAdminNumPackets=_HwNqaCtlJitterAdminNumPackets_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,5),_HwNqaCtlJitterAdminNumPackets_Type())
hwNqaCtlJitterAdminNumPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlJitterAdminNumPackets.setStatus(_A)
class _HwNqaCtlHttpOperationType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('get',1),('post',2)))
_HwNqaCtlHttpOperationType_Type.__name__=_G
_HwNqaCtlHttpOperationType_Object=MibTableColumn
hwNqaCtlHttpOperationType=_HwNqaCtlHttpOperationType_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,6),_HwNqaCtlHttpOperationType_Type())
hwNqaCtlHttpOperationType.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlHttpOperationType.setStatus(_A)
class _HwNqaCtlHttpOperationString_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwNqaCtlHttpOperationString_Type.__name__=_S
_HwNqaCtlHttpOperationString_Object=MibTableColumn
hwNqaCtlHttpOperationString=_HwNqaCtlHttpOperationString_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,7),_HwNqaCtlHttpOperationString_Type())
hwNqaCtlHttpOperationString.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlHttpOperationString.setStatus(_A)
class _HwNqaCtlFtpOperationType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('get',1),('put',2)))
_HwNqaCtlFtpOperationType_Type.__name__=_G
_HwNqaCtlFtpOperationType_Object=MibTableColumn
hwNqaCtlFtpOperationType=_HwNqaCtlFtpOperationType_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,8),_HwNqaCtlFtpOperationType_Type())
hwNqaCtlFtpOperationType.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlFtpOperationType.setStatus(_A)
class _HwNqaCtlFtpUsername_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HwNqaCtlFtpUsername_Type.__name__=_S
_HwNqaCtlFtpUsername_Object=MibTableColumn
hwNqaCtlFtpUsername=_HwNqaCtlFtpUsername_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,9),_HwNqaCtlFtpUsername_Type())
hwNqaCtlFtpUsername.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlFtpUsername.setStatus(_A)
class _HwNqaCtlFtpPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HwNqaCtlFtpPassword_Type.__name__=_S
_HwNqaCtlFtpPassword_Object=MibTableColumn
hwNqaCtlFtpPassword=_HwNqaCtlFtpPassword_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,10),_HwNqaCtlFtpPassword_Type())
hwNqaCtlFtpPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlFtpPassword.setStatus(_A)
class _HwNqaCtlFtpOperationString_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwNqaCtlFtpOperationString_Type.__name__=_S
_HwNqaCtlFtpOperationString_Object=MibTableColumn
hwNqaCtlFtpOperationString=_HwNqaCtlFtpOperationString_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,11),_HwNqaCtlFtpOperationString_Type())
hwNqaCtlFtpOperationString.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlFtpOperationString.setStatus(_A)
class _HwNqaCtlVPNInstance_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwNqaCtlVPNInstance_Type.__name__=_S
_HwNqaCtlVPNInstance_Object=MibTableColumn
hwNqaCtlVPNInstance=_HwNqaCtlVPNInstance_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,12),_HwNqaCtlVPNInstance_Type())
hwNqaCtlVPNInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlVPNInstance.setStatus(_A)
class _HwNqaCtlHistoryKeptTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_HwNqaCtlHistoryKeptTime_Type.__name__=_G
_HwNqaCtlHistoryKeptTime_Object=MibTableColumn
hwNqaCtlHistoryKeptTime=_HwNqaCtlHistoryKeptTime_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,13),_HwNqaCtlHistoryKeptTime_Type())
hwNqaCtlHistoryKeptTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlHistoryKeptTime.setStatus(_A)
if mibBuilder.loadTexts:hwNqaCtlHistoryKeptTime.setUnits(_Y)
class _HwNqaCtlHistoryEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HwNqaCtlHistoryEnable_Type.__name__=_G
_HwNqaCtlHistoryEnable_Object=MibTableColumn
hwNqaCtlHistoryEnable=_HwNqaCtlHistoryEnable_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,14),_HwNqaCtlHistoryEnable_Type())
hwNqaCtlHistoryEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlHistoryEnable.setStatus(_A)
class _HwNqaCtlICPIFAdvFactor_Type(Integer32):defaultValue=0
_HwNqaCtlICPIFAdvFactor_Type.__name__=_G
_HwNqaCtlICPIFAdvFactor_Object=MibTableColumn
hwNqaCtlICPIFAdvFactor=_HwNqaCtlICPIFAdvFactor_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,15),_HwNqaCtlICPIFAdvFactor_Type())
hwNqaCtlICPIFAdvFactor.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlICPIFAdvFactor.setStatus(_A)
class _HwNqaCtlCodecType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notDefined',1),('g711Alaw',2),('g711Ulaw',3),('g729A',4),('icmpTimestamp',5)))
_HwNqaCtlCodecType_Type.__name__=_G
_HwNqaCtlCodecType_Object=MibTableColumn
hwNqaCtlCodecType=_HwNqaCtlCodecType_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,2,1,16),_HwNqaCtlCodecType_Type())
hwNqaCtlCodecType.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlCodecType.setStatus(_A)
_HwNqaResultsTable_Object=MibTable
hwNqaResultsTable=_HwNqaResultsTable_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3))
if mibBuilder.loadTexts:hwNqaResultsTable.setStatus(_A)
_HwNqaResultsEntry_Object=MibTableRow
hwNqaResultsEntry=_HwNqaResultsEntry_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1))
hwNqaResultsEntry.setIndexNames((0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:hwNqaResultsEntry.setStatus(_A)
_HwNqaResultsRttNumDisconnects_Type=Unsigned32
_HwNqaResultsRttNumDisconnects_Object=MibTableColumn
hwNqaResultsRttNumDisconnects=_HwNqaResultsRttNumDisconnects_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,1),_HwNqaResultsRttNumDisconnects_Type())
hwNqaResultsRttNumDisconnects.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsRttNumDisconnects.setStatus(_A)
_HwNqaResultsRttTimeouts_Type=Unsigned32
_HwNqaResultsRttTimeouts_Object=MibTableColumn
hwNqaResultsRttTimeouts=_HwNqaResultsRttTimeouts_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,2),_HwNqaResultsRttTimeouts_Type())
hwNqaResultsRttTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsRttTimeouts.setStatus(_A)
_HwNqaResultsRttBusies_Type=Unsigned32
_HwNqaResultsRttBusies_Object=MibTableColumn
hwNqaResultsRttBusies=_HwNqaResultsRttBusies_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,3),_HwNqaResultsRttBusies_Type())
hwNqaResultsRttBusies.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsRttBusies.setStatus(_A)
_HwNqaResultsRttNoConnections_Type=Unsigned32
_HwNqaResultsRttNoConnections_Object=MibTableColumn
hwNqaResultsRttNoConnections=_HwNqaResultsRttNoConnections_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,4),_HwNqaResultsRttNoConnections_Type())
hwNqaResultsRttNoConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsRttNoConnections.setStatus(_A)
_HwNqaResultsRttDrops_Type=Unsigned32
_HwNqaResultsRttDrops_Object=MibTableColumn
hwNqaResultsRttDrops=_HwNqaResultsRttDrops_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,5),_HwNqaResultsRttDrops_Type())
hwNqaResultsRttDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsRttDrops.setStatus(_A)
_HwNqaResultsRttSequenceErrors_Type=Unsigned32
_HwNqaResultsRttSequenceErrors_Object=MibTableColumn
hwNqaResultsRttSequenceErrors=_HwNqaResultsRttSequenceErrors_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,6),_HwNqaResultsRttSequenceErrors_Type())
hwNqaResultsRttSequenceErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsRttSequenceErrors.setStatus(_A)
_HwNqaResultsRttStatsErrors_Type=Unsigned32
_HwNqaResultsRttStatsErrors_Object=MibTableColumn
hwNqaResultsRttStatsErrors=_HwNqaResultsRttStatsErrors_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,7),_HwNqaResultsRttStatsErrors_Type())
hwNqaResultsRttStatsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsRttStatsErrors.setStatus(_A)
_HwNqaResultsMaxDelaySD_Type=Unsigned32
_HwNqaResultsMaxDelaySD_Object=MibTableColumn
hwNqaResultsMaxDelaySD=_HwNqaResultsMaxDelaySD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,8),_HwNqaResultsMaxDelaySD_Type())
hwNqaResultsMaxDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsMaxDelaySD.setStatus(_A)
if mibBuilder.loadTexts:hwNqaResultsMaxDelaySD.setUnits(_F)
_HwNqaResultsMaxDelayDS_Type=Unsigned32
_HwNqaResultsMaxDelayDS_Object=MibTableColumn
hwNqaResultsMaxDelayDS=_HwNqaResultsMaxDelayDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,9),_HwNqaResultsMaxDelayDS_Type())
hwNqaResultsMaxDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsMaxDelayDS.setStatus(_A)
if mibBuilder.loadTexts:hwNqaResultsMaxDelayDS.setUnits(_F)
_HwNqaResultsLostPacketRatio_Type=Unsigned32
_HwNqaResultsLostPacketRatio_Object=MibTableColumn
hwNqaResultsLostPacketRatio=_HwNqaResultsLostPacketRatio_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,10),_HwNqaResultsLostPacketRatio_Type())
hwNqaResultsLostPacketRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsLostPacketRatio.setStatus(_A)
if mibBuilder.loadTexts:hwNqaResultsLostPacketRatio.setUnits(_F)
_HwNqaResultsPacketLateArrival_Type=Unsigned32
_HwNqaResultsPacketLateArrival_Object=MibTableColumn
hwNqaResultsPacketLateArrival=_HwNqaResultsPacketLateArrival_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,11),_HwNqaResultsPacketLateArrival_Type())
hwNqaResultsPacketLateArrival.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsPacketLateArrival.setStatus(_A)
_HwNqaResultsRttSum_Type=Unsigned32
_HwNqaResultsRttSum_Object=MibTableColumn
hwNqaResultsRttSum=_HwNqaResultsRttSum_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,12),_HwNqaResultsRttSum_Type())
hwNqaResultsRttSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsRttSum.setStatus(_A)
_HwNqaResultsNumOfDelaySD_Type=Unsigned32
_HwNqaResultsNumOfDelaySD_Object=MibTableColumn
hwNqaResultsNumOfDelaySD=_HwNqaResultsNumOfDelaySD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,13),_HwNqaResultsNumOfDelaySD_Type())
hwNqaResultsNumOfDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsNumOfDelaySD.setStatus(_A)
_HwNqaResultsMinDelaySD_Type=Unsigned32
_HwNqaResultsMinDelaySD_Object=MibTableColumn
hwNqaResultsMinDelaySD=_HwNqaResultsMinDelaySD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,14),_HwNqaResultsMinDelaySD_Type())
hwNqaResultsMinDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsMinDelaySD.setStatus(_A)
_HwNqaResultsSumDelaySD_Type=Unsigned32
_HwNqaResultsSumDelaySD_Object=MibTableColumn
hwNqaResultsSumDelaySD=_HwNqaResultsSumDelaySD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,15),_HwNqaResultsSumDelaySD_Type())
hwNqaResultsSumDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsSumDelaySD.setStatus(_A)
_HwNqaResultsSum2DelaySD_Type=Unsigned32
_HwNqaResultsSum2DelaySD_Object=MibTableColumn
hwNqaResultsSum2DelaySD=_HwNqaResultsSum2DelaySD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,16),_HwNqaResultsSum2DelaySD_Type())
hwNqaResultsSum2DelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsSum2DelaySD.setStatus(_A)
_HwNqaResultsNumOfDelayDS_Type=Unsigned32
_HwNqaResultsNumOfDelayDS_Object=MibTableColumn
hwNqaResultsNumOfDelayDS=_HwNqaResultsNumOfDelayDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,17),_HwNqaResultsNumOfDelayDS_Type())
hwNqaResultsNumOfDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsNumOfDelayDS.setStatus(_A)
_HwNqaResultsMinDelayDS_Type=Unsigned32
_HwNqaResultsMinDelayDS_Object=MibTableColumn
hwNqaResultsMinDelayDS=_HwNqaResultsMinDelayDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,18),_HwNqaResultsMinDelayDS_Type())
hwNqaResultsMinDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsMinDelayDS.setStatus(_A)
_HwNqaResultsSumDelayDS_Type=Unsigned32
_HwNqaResultsSumDelayDS_Object=MibTableColumn
hwNqaResultsSumDelayDS=_HwNqaResultsSumDelayDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,19),_HwNqaResultsSumDelayDS_Type())
hwNqaResultsSumDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsSumDelayDS.setStatus(_A)
_HwNqaResultsSum2DelayDS_Type=Unsigned32
_HwNqaResultsSum2DelayDS_Object=MibTableColumn
hwNqaResultsSum2DelayDS=_HwNqaResultsSum2DelayDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,3,1,20),_HwNqaResultsSum2DelayDS_Type())
hwNqaResultsSum2DelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaResultsSum2DelayDS.setStatus(_A)
_HwNqaJitterStatsTable_Object=MibTable
hwNqaJitterStatsTable=_HwNqaJitterStatsTable_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4))
if mibBuilder.loadTexts:hwNqaJitterStatsTable.setStatus(_A)
_HwNqaJitterStatsEntry_Object=MibTableRow
hwNqaJitterStatsEntry=_HwNqaJitterStatsEntry_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1))
hwNqaJitterStatsEntry.setIndexNames((0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:hwNqaJitterStatsEntry.setStatus(_A)
_HwNqaJitterStatsNumOfRTT_Type=Counter32
_HwNqaJitterStatsNumOfRTT_Object=MibTableColumn
hwNqaJitterStatsNumOfRTT=_HwNqaJitterStatsNumOfRTT_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,1),_HwNqaJitterStatsNumOfRTT_Type())
hwNqaJitterStatsNumOfRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsNumOfRTT.setStatus(_A)
_HwNqaJitterStatsMinOfPositivesSD_Type=Gauge32
_HwNqaJitterStatsMinOfPositivesSD_Object=MibTableColumn
hwNqaJitterStatsMinOfPositivesSD=_HwNqaJitterStatsMinOfPositivesSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,2),_HwNqaJitterStatsMinOfPositivesSD_Type())
hwNqaJitterStatsMinOfPositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsMinOfPositivesSD.setStatus(_A)
_HwNqaJitterStatsMaxOfPositivesSD_Type=Gauge32
_HwNqaJitterStatsMaxOfPositivesSD_Object=MibTableColumn
hwNqaJitterStatsMaxOfPositivesSD=_HwNqaJitterStatsMaxOfPositivesSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,3),_HwNqaJitterStatsMaxOfPositivesSD_Type())
hwNqaJitterStatsMaxOfPositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsMaxOfPositivesSD.setStatus(_A)
_HwNqaJitterStatsNumOfPositivesSD_Type=Gauge32
_HwNqaJitterStatsNumOfPositivesSD_Object=MibTableColumn
hwNqaJitterStatsNumOfPositivesSD=_HwNqaJitterStatsNumOfPositivesSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,4),_HwNqaJitterStatsNumOfPositivesSD_Type())
hwNqaJitterStatsNumOfPositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsNumOfPositivesSD.setStatus(_A)
_HwNqaJitterStatsSumOfPositivesSD_Type=Gauge32
_HwNqaJitterStatsSumOfPositivesSD_Object=MibTableColumn
hwNqaJitterStatsSumOfPositivesSD=_HwNqaJitterStatsSumOfPositivesSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,5),_HwNqaJitterStatsSumOfPositivesSD_Type())
hwNqaJitterStatsSumOfPositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsSumOfPositivesSD.setStatus(_A)
_HwNqaJitterStatsSum2PositivesSD_Type=Gauge32
_HwNqaJitterStatsSum2PositivesSD_Object=MibTableColumn
hwNqaJitterStatsSum2PositivesSD=_HwNqaJitterStatsSum2PositivesSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,6),_HwNqaJitterStatsSum2PositivesSD_Type())
hwNqaJitterStatsSum2PositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsSum2PositivesSD.setStatus(_A)
_HwNqaJitterStatsMinOfNegativesSD_Type=Gauge32
_HwNqaJitterStatsMinOfNegativesSD_Object=MibTableColumn
hwNqaJitterStatsMinOfNegativesSD=_HwNqaJitterStatsMinOfNegativesSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,7),_HwNqaJitterStatsMinOfNegativesSD_Type())
hwNqaJitterStatsMinOfNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsMinOfNegativesSD.setStatus(_A)
_HwNqaJitterStatsMaxOfNegativesSD_Type=Gauge32
_HwNqaJitterStatsMaxOfNegativesSD_Object=MibTableColumn
hwNqaJitterStatsMaxOfNegativesSD=_HwNqaJitterStatsMaxOfNegativesSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,8),_HwNqaJitterStatsMaxOfNegativesSD_Type())
hwNqaJitterStatsMaxOfNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsMaxOfNegativesSD.setStatus(_A)
_HwNqaJitterStatsNumOfNegativesSD_Type=Gauge32
_HwNqaJitterStatsNumOfNegativesSD_Object=MibTableColumn
hwNqaJitterStatsNumOfNegativesSD=_HwNqaJitterStatsNumOfNegativesSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,9),_HwNqaJitterStatsNumOfNegativesSD_Type())
hwNqaJitterStatsNumOfNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsNumOfNegativesSD.setStatus(_A)
_HwNqaJitterStatsSumOfNegativesSD_Type=Gauge32
_HwNqaJitterStatsSumOfNegativesSD_Object=MibTableColumn
hwNqaJitterStatsSumOfNegativesSD=_HwNqaJitterStatsSumOfNegativesSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,10),_HwNqaJitterStatsSumOfNegativesSD_Type())
hwNqaJitterStatsSumOfNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsSumOfNegativesSD.setStatus(_A)
_HwNqaJitterStatsSum2NegativesSD_Type=Gauge32
_HwNqaJitterStatsSum2NegativesSD_Object=MibTableColumn
hwNqaJitterStatsSum2NegativesSD=_HwNqaJitterStatsSum2NegativesSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,11),_HwNqaJitterStatsSum2NegativesSD_Type())
hwNqaJitterStatsSum2NegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsSum2NegativesSD.setStatus(_A)
_HwNqaJitterStatsMinOfPositivesDS_Type=Gauge32
_HwNqaJitterStatsMinOfPositivesDS_Object=MibTableColumn
hwNqaJitterStatsMinOfPositivesDS=_HwNqaJitterStatsMinOfPositivesDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,12),_HwNqaJitterStatsMinOfPositivesDS_Type())
hwNqaJitterStatsMinOfPositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsMinOfPositivesDS.setStatus(_A)
_HwNqaJitterStatsMaxOfPositivesDS_Type=Gauge32
_HwNqaJitterStatsMaxOfPositivesDS_Object=MibTableColumn
hwNqaJitterStatsMaxOfPositivesDS=_HwNqaJitterStatsMaxOfPositivesDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,13),_HwNqaJitterStatsMaxOfPositivesDS_Type())
hwNqaJitterStatsMaxOfPositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsMaxOfPositivesDS.setStatus(_A)
_HwNqaJitterStatsNumOfPositivesDS_Type=Gauge32
_HwNqaJitterStatsNumOfPositivesDS_Object=MibTableColumn
hwNqaJitterStatsNumOfPositivesDS=_HwNqaJitterStatsNumOfPositivesDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,14),_HwNqaJitterStatsNumOfPositivesDS_Type())
hwNqaJitterStatsNumOfPositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsNumOfPositivesDS.setStatus(_A)
_HwNqaJitterStatsSumOfPositivesDS_Type=Gauge32
_HwNqaJitterStatsSumOfPositivesDS_Object=MibTableColumn
hwNqaJitterStatsSumOfPositivesDS=_HwNqaJitterStatsSumOfPositivesDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,15),_HwNqaJitterStatsSumOfPositivesDS_Type())
hwNqaJitterStatsSumOfPositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsSumOfPositivesDS.setStatus(_A)
_HwNqaJitterStatsSum2PositivesDS_Type=Gauge32
_HwNqaJitterStatsSum2PositivesDS_Object=MibTableColumn
hwNqaJitterStatsSum2PositivesDS=_HwNqaJitterStatsSum2PositivesDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,16),_HwNqaJitterStatsSum2PositivesDS_Type())
hwNqaJitterStatsSum2PositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsSum2PositivesDS.setStatus(_A)
_HwNqaJitterStatsMinOfNegativesDS_Type=Gauge32
_HwNqaJitterStatsMinOfNegativesDS_Object=MibTableColumn
hwNqaJitterStatsMinOfNegativesDS=_HwNqaJitterStatsMinOfNegativesDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,17),_HwNqaJitterStatsMinOfNegativesDS_Type())
hwNqaJitterStatsMinOfNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsMinOfNegativesDS.setStatus(_A)
_HwNqaJitterStatsMaxOfNegativesDS_Type=Gauge32
_HwNqaJitterStatsMaxOfNegativesDS_Object=MibTableColumn
hwNqaJitterStatsMaxOfNegativesDS=_HwNqaJitterStatsMaxOfNegativesDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,18),_HwNqaJitterStatsMaxOfNegativesDS_Type())
hwNqaJitterStatsMaxOfNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsMaxOfNegativesDS.setStatus(_A)
_HwNqaJitterStatsNumOfNegativesDS_Type=Gauge32
_HwNqaJitterStatsNumOfNegativesDS_Object=MibTableColumn
hwNqaJitterStatsNumOfNegativesDS=_HwNqaJitterStatsNumOfNegativesDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,19),_HwNqaJitterStatsNumOfNegativesDS_Type())
hwNqaJitterStatsNumOfNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsNumOfNegativesDS.setStatus(_A)
_HwNqaJitterStatsSumOfNegativesDS_Type=Gauge32
_HwNqaJitterStatsSumOfNegativesDS_Object=MibTableColumn
hwNqaJitterStatsSumOfNegativesDS=_HwNqaJitterStatsSumOfNegativesDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,20),_HwNqaJitterStatsSumOfNegativesDS_Type())
hwNqaJitterStatsSumOfNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsSumOfNegativesDS.setStatus(_A)
_HwNqaJitterStatsSum2NegativesDS_Type=Gauge32
_HwNqaJitterStatsSum2NegativesDS_Object=MibTableColumn
hwNqaJitterStatsSum2NegativesDS=_HwNqaJitterStatsSum2NegativesDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,21),_HwNqaJitterStatsSum2NegativesDS_Type())
hwNqaJitterStatsSum2NegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsSum2NegativesDS.setStatus(_A)
_HwNqaJitterStatsPacketLossSD_Type=Gauge32
_HwNqaJitterStatsPacketLossSD_Object=MibTableColumn
hwNqaJitterStatsPacketLossSD=_HwNqaJitterStatsPacketLossSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,22),_HwNqaJitterStatsPacketLossSD_Type())
hwNqaJitterStatsPacketLossSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsPacketLossSD.setStatus(_A)
_HwNqaJitterStatsPacketLossDS_Type=Gauge32
_HwNqaJitterStatsPacketLossDS_Object=MibTableColumn
hwNqaJitterStatsPacketLossDS=_HwNqaJitterStatsPacketLossDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,23),_HwNqaJitterStatsPacketLossDS_Type())
hwNqaJitterStatsPacketLossDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsPacketLossDS.setStatus(_A)
_HwNqaJitterStatsAvePositivesSD_Type=Gauge32
_HwNqaJitterStatsAvePositivesSD_Object=MibTableColumn
hwNqaJitterStatsAvePositivesSD=_HwNqaJitterStatsAvePositivesSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,24),_HwNqaJitterStatsAvePositivesSD_Type())
hwNqaJitterStatsAvePositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsAvePositivesSD.setStatus(_A)
_HwNqaJitterStatsAveNegativesSD_Type=Gauge32
_HwNqaJitterStatsAveNegativesSD_Object=MibTableColumn
hwNqaJitterStatsAveNegativesSD=_HwNqaJitterStatsAveNegativesSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,25),_HwNqaJitterStatsAveNegativesSD_Type())
hwNqaJitterStatsAveNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsAveNegativesSD.setStatus(_A)
_HwNqaJitterStatsAvePositivesDS_Type=Gauge32
_HwNqaJitterStatsAvePositivesDS_Object=MibTableColumn
hwNqaJitterStatsAvePositivesDS=_HwNqaJitterStatsAvePositivesDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,26),_HwNqaJitterStatsAvePositivesDS_Type())
hwNqaJitterStatsAvePositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsAvePositivesDS.setStatus(_A)
_HwNqaJitterStatsAveNegativesDS_Type=Gauge32
_HwNqaJitterStatsAveNegativesDS_Object=MibTableColumn
hwNqaJitterStatsAveNegativesDS=_HwNqaJitterStatsAveNegativesDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,27),_HwNqaJitterStatsAveNegativesDS_Type())
hwNqaJitterStatsAveNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsAveNegativesDS.setStatus(_A)
_HwNqaJitterStatsPktLossUnknown_Type=Gauge32
_HwNqaJitterStatsPktLossUnknown_Object=MibTableColumn
hwNqaJitterStatsPktLossUnknown=_HwNqaJitterStatsPktLossUnknown_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,28),_HwNqaJitterStatsPktLossUnknown_Type())
hwNqaJitterStatsPktLossUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsPktLossUnknown.setStatus(_A)
if mibBuilder.loadTexts:hwNqaJitterStatsPktLossUnknown.setUnits(_F)
_HwNqaJitterStatsOperOfICPIF_Type=Gauge32
_HwNqaJitterStatsOperOfICPIF_Object=MibTableColumn
hwNqaJitterStatsOperOfICPIF=_HwNqaJitterStatsOperOfICPIF_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,29),_HwNqaJitterStatsOperOfICPIF_Type())
hwNqaJitterStatsOperOfICPIF.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsOperOfICPIF.setStatus(_A)
_HwNqaJitterStatsOperOfMOS_Type=Gauge32
_HwNqaJitterStatsOperOfMOS_Object=MibTableColumn
hwNqaJitterStatsOperOfMOS=_HwNqaJitterStatsOperOfMOS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,4,1,30),_HwNqaJitterStatsOperOfMOS_Type())
hwNqaJitterStatsOperOfMOS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaJitterStatsOperOfMOS.setStatus(_A)
class _HwNqaAgentEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_HwNqaAgentEnable_Type.__name__=_G
_HwNqaAgentEnable_Object=MibScalar
hwNqaAgentEnable=_HwNqaAgentEnable_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,5),_HwNqaAgentEnable_Type())
hwNqaAgentEnable.setMaxAccess(_d)
if mibBuilder.loadTexts:hwNqaAgentEnable.setStatus(_A)
_HwNqaTcpServerTable_Object=MibTable
hwNqaTcpServerTable=_HwNqaTcpServerTable_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,6))
if mibBuilder.loadTexts:hwNqaTcpServerTable.setStatus(_A)
_HwNqaTcpServerEntry_Object=MibTableRow
hwNqaTcpServerEntry=_HwNqaTcpServerEntry_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,6,1))
hwNqaTcpServerEntry.setIndexNames((0,_C,_e),(0,_C,_f))
if mibBuilder.loadTexts:hwNqaTcpServerEntry.setStatus(_A)
class _HwNqaTcpServerIpAddress_Type(InetAddress):defaultHexValue=''
_HwNqaTcpServerIpAddress_Type.__name__=_W
_HwNqaTcpServerIpAddress_Object=MibTableColumn
hwNqaTcpServerIpAddress=_HwNqaTcpServerIpAddress_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,6,1,1),_HwNqaTcpServerIpAddress_Type())
hwNqaTcpServerIpAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:hwNqaTcpServerIpAddress.setStatus(_A)
class _HwNqaTcpServerPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_HwNqaTcpServerPort_Type.__name__=_G
_HwNqaTcpServerPort_Object=MibTableColumn
hwNqaTcpServerPort=_HwNqaTcpServerPort_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,6,1,2),_HwNqaTcpServerPort_Type())
hwNqaTcpServerPort.setMaxAccess(_I)
if mibBuilder.loadTexts:hwNqaTcpServerPort.setStatus(_A)
_HwNqaTcpServerRowStatus_Type=RowStatus
_HwNqaTcpServerRowStatus_Object=MibTableColumn
hwNqaTcpServerRowStatus=_HwNqaTcpServerRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,6,1,3),_HwNqaTcpServerRowStatus_Type())
hwNqaTcpServerRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaTcpServerRowStatus.setStatus(_A)
_HwNqaUdpServerTable_Object=MibTable
hwNqaUdpServerTable=_HwNqaUdpServerTable_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,7))
if mibBuilder.loadTexts:hwNqaUdpServerTable.setStatus(_A)
_HwNqaUdpServerEntry_Object=MibTableRow
hwNqaUdpServerEntry=_HwNqaUdpServerEntry_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,7,1))
hwNqaUdpServerEntry.setIndexNames((0,_C,_g),(0,_C,_h))
if mibBuilder.loadTexts:hwNqaUdpServerEntry.setStatus(_A)
class _HwNqaUdpServerIpAddress_Type(InetAddress):defaultHexValue=''
_HwNqaUdpServerIpAddress_Type.__name__=_W
_HwNqaUdpServerIpAddress_Object=MibTableColumn
hwNqaUdpServerIpAddress=_HwNqaUdpServerIpAddress_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,7,1,1),_HwNqaUdpServerIpAddress_Type())
hwNqaUdpServerIpAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:hwNqaUdpServerIpAddress.setStatus(_A)
class _HwNqaUdpServerPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_HwNqaUdpServerPort_Type.__name__=_G
_HwNqaUdpServerPort_Object=MibTableColumn
hwNqaUdpServerPort=_HwNqaUdpServerPort_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,7,1,2),_HwNqaUdpServerPort_Type())
hwNqaUdpServerPort.setMaxAccess(_I)
if mibBuilder.loadTexts:hwNqaUdpServerPort.setStatus(_A)
_HwNqaUdpServerRowStatus_Type=RowStatus
_HwNqaUdpServerRowStatus_Object=MibTableColumn
hwNqaUdpServerRowStatus=_HwNqaUdpServerRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,7,1,3),_HwNqaUdpServerRowStatus_Type())
hwNqaUdpServerRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaUdpServerRowStatus.setStatus(_A)
class _HwNqaServerEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_HwNqaServerEnable_Type.__name__=_G
_HwNqaServerEnable_Object=MibScalar
hwNqaServerEnable=_HwNqaServerEnable_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,8),_HwNqaServerEnable_Type())
hwNqaServerEnable.setMaxAccess(_d)
if mibBuilder.loadTexts:hwNqaServerEnable.setStatus(_A)
_HwNqaStatsMaxGroupNumber_Type=Integer32
_HwNqaStatsMaxGroupNumber_Object=MibScalar
hwNqaStatsMaxGroupNumber=_HwNqaStatsMaxGroupNumber_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,9),_HwNqaStatsMaxGroupNumber_Type())
hwNqaStatsMaxGroupNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatsMaxGroupNumber.setStatus(_A)
_HwNqaStatisticsCtlTable_Object=MibTable
hwNqaStatisticsCtlTable=_HwNqaStatisticsCtlTable_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,10))
if mibBuilder.loadTexts:hwNqaStatisticsCtlTable.setStatus(_A)
_HwNqaStatisticsCtlEntry_Object=MibTableRow
hwNqaStatisticsCtlEntry=_HwNqaStatisticsCtlEntry_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,10,1))
if mibBuilder.loadTexts:hwNqaStatisticsCtlEntry.setStatus(_A)
_HwNqaCtlStatisticsInterval_Type=Unsigned32
_HwNqaCtlStatisticsInterval_Object=MibTableColumn
hwNqaCtlStatisticsInterval=_HwNqaCtlStatisticsInterval_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,10,1,1),_HwNqaCtlStatisticsInterval_Type())
hwNqaCtlStatisticsInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlStatisticsInterval.setStatus(_A)
if mibBuilder.loadTexts:hwNqaCtlStatisticsInterval.setUnits(_Y)
class _HwNqaCtlStatisticsGroupNumber_Type(Unsigned32):defaultValue=2
_HwNqaCtlStatisticsGroupNumber_Type.__name__=_H
_HwNqaCtlStatisticsGroupNumber_Object=MibTableColumn
hwNqaCtlStatisticsGroupNumber=_HwNqaCtlStatisticsGroupNumber_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,10,1,2),_HwNqaCtlStatisticsGroupNumber_Type())
hwNqaCtlStatisticsGroupNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlStatisticsGroupNumber.setStatus(_A)
class _HwNqaCtlStatisticsKeptTime_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_HwNqaCtlStatisticsKeptTime_Type.__name__=_H
_HwNqaCtlStatisticsKeptTime_Object=MibTableColumn
hwNqaCtlStatisticsKeptTime=_HwNqaCtlStatisticsKeptTime_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,10,1,3),_HwNqaCtlStatisticsKeptTime_Type())
hwNqaCtlStatisticsKeptTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlStatisticsKeptTime.setStatus(_A)
if mibBuilder.loadTexts:hwNqaCtlStatisticsKeptTime.setUnits(_Y)
_HwNqaCtlBeginTime_Type=DateAndTime
_HwNqaCtlBeginTime_Object=MibTableColumn
hwNqaCtlBeginTime=_HwNqaCtlBeginTime_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,10,1,4),_HwNqaCtlBeginTime_Type())
hwNqaCtlBeginTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlBeginTime.setStatus(_A)
class _HwNqaCtlLifeTime_Type(Unsigned32):defaultValue=0
_HwNqaCtlLifeTime_Type.__name__=_H
_HwNqaCtlLifeTime_Object=MibTableColumn
hwNqaCtlLifeTime=_HwNqaCtlLifeTime_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,10,1,5),_HwNqaCtlLifeTime_Type())
hwNqaCtlLifeTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaCtlLifeTime.setStatus(_A)
if mibBuilder.loadTexts:hwNqaCtlLifeTime.setUnits(_i)
_HwNqaStatisticsResultsTable_Object=MibTable
hwNqaStatisticsResultsTable=_HwNqaStatisticsResultsTable_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11))
if mibBuilder.loadTexts:hwNqaStatisticsResultsTable.setStatus(_A)
_HwNqaStatisticsResultsEntry_Object=MibTableRow
hwNqaStatisticsResultsEntry=_HwNqaStatisticsResultsEntry_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1))
hwNqaStatisticsResultsEntry.setIndexNames((0,_D,_T),(0,_D,_U),(0,_C,_j))
if mibBuilder.loadTexts:hwNqaStatisticsResultsEntry.setStatus(_A)
class _HwNqaStatResIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HwNqaStatResIndex_Type.__name__=_H
_HwNqaStatResIndex_Object=MibTableColumn
hwNqaStatResIndex=_HwNqaStatResIndex_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,1),_HwNqaStatResIndex_Type())
hwNqaStatResIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hwNqaStatResIndex.setStatus(_A)
class _HwNqaStatResIpTargetAddressType_Type(InetAddressType):defaultValue=0
_HwNqaStatResIpTargetAddressType_Type.__name__=_a
_HwNqaStatResIpTargetAddressType_Object=MibTableColumn
hwNqaStatResIpTargetAddressType=_HwNqaStatResIpTargetAddressType_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,2),_HwNqaStatResIpTargetAddressType_Type())
hwNqaStatResIpTargetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResIpTargetAddressType.setStatus(_A)
class _HwNqaStatResIpTargetAddress_Type(InetAddress):defaultHexValue=''
_HwNqaStatResIpTargetAddress_Type.__name__=_W
_HwNqaStatResIpTargetAddress_Object=MibTableColumn
hwNqaStatResIpTargetAddress=_HwNqaStatResIpTargetAddress_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,3),_HwNqaStatResIpTargetAddress_Type())
hwNqaStatResIpTargetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResIpTargetAddress.setStatus(_A)
_HwNqaStatResMinRtt_Type=Gauge32
_HwNqaStatResMinRtt_Object=MibTableColumn
hwNqaStatResMinRtt=_HwNqaStatResMinRtt_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,4),_HwNqaStatResMinRtt_Type())
hwNqaStatResMinRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResMinRtt.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatResMinRtt.setUnits(_F)
_HwNqaStatResMaxRtt_Type=Gauge32
_HwNqaStatResMaxRtt_Object=MibTableColumn
hwNqaStatResMaxRtt=_HwNqaStatResMaxRtt_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,5),_HwNqaStatResMaxRtt_Type())
hwNqaStatResMaxRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResMaxRtt.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatResMaxRtt.setUnits(_F)
_HwNqaStatResAverageRtt_Type=Gauge32
_HwNqaStatResAverageRtt_Object=MibTableColumn
hwNqaStatResAverageRtt=_HwNqaStatResAverageRtt_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,6),_HwNqaStatResAverageRtt_Type())
hwNqaStatResAverageRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResAverageRtt.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatResAverageRtt.setUnits(_F)
_HwNqaStatResProbeResponses_Type=Counter32
_HwNqaStatResProbeResponses_Object=MibTableColumn
hwNqaStatResProbeResponses=_HwNqaStatResProbeResponses_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,7),_HwNqaStatResProbeResponses_Type())
hwNqaStatResProbeResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResProbeResponses.setStatus(_A)
_HwNqaStatResSentProbes_Type=Counter32
_HwNqaStatResSentProbes_Object=MibTableColumn
hwNqaStatResSentProbes=_HwNqaStatResSentProbes_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,8),_HwNqaStatResSentProbes_Type())
hwNqaStatResSentProbes.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResSentProbes.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatResSentProbes.setUnits('probes')
_HwNqaStatResRttSumOfSquares_Type=Counter32
_HwNqaStatResRttSumOfSquares_Object=MibTableColumn
hwNqaStatResRttSumOfSquares=_HwNqaStatResRttSumOfSquares_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,9),_HwNqaStatResRttSumOfSquares_Type())
hwNqaStatResRttSumOfSquares.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResRttSumOfSquares.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatResRttSumOfSquares.setUnits(_F)
_HwNqaStatResStartTime_Type=DateAndTime
_HwNqaStatResStartTime_Object=MibTableColumn
hwNqaStatResStartTime=_HwNqaStatResStartTime_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,10),_HwNqaStatResStartTime_Type())
hwNqaStatResStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResStartTime.setStatus(_A)
_HwNqaStatResInterval_Type=Gauge32
_HwNqaStatResInterval_Object=MibTableColumn
hwNqaStatResInterval=_HwNqaStatResInterval_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,11),_HwNqaStatResInterval_Type())
hwNqaStatResInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResInterval.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatResInterval.setUnits(_i)
_HwNqaStatResRttNumDisconnects_Type=Counter32
_HwNqaStatResRttNumDisconnects_Object=MibTableColumn
hwNqaStatResRttNumDisconnects=_HwNqaStatResRttNumDisconnects_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,12),_HwNqaStatResRttNumDisconnects_Type())
hwNqaStatResRttNumDisconnects.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResRttNumDisconnects.setStatus(_A)
_HwNqaStatResRttTimeouts_Type=Counter32
_HwNqaStatResRttTimeouts_Object=MibTableColumn
hwNqaStatResRttTimeouts=_HwNqaStatResRttTimeouts_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,13),_HwNqaStatResRttTimeouts_Type())
hwNqaStatResRttTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResRttTimeouts.setStatus(_A)
_HwNqaStatResRttBusies_Type=Counter32
_HwNqaStatResRttBusies_Object=MibTableColumn
hwNqaStatResRttBusies=_HwNqaStatResRttBusies_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,14),_HwNqaStatResRttBusies_Type())
hwNqaStatResRttBusies.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResRttBusies.setStatus(_A)
_HwNqaStatResRttNoConnections_Type=Counter32
_HwNqaStatResRttNoConnections_Object=MibTableColumn
hwNqaStatResRttNoConnections=_HwNqaStatResRttNoConnections_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,15),_HwNqaStatResRttNoConnections_Type())
hwNqaStatResRttNoConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResRttNoConnections.setStatus(_A)
_HwNqaStatResRttDrops_Type=Counter32
_HwNqaStatResRttDrops_Object=MibTableColumn
hwNqaStatResRttDrops=_HwNqaStatResRttDrops_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,16),_HwNqaStatResRttDrops_Type())
hwNqaStatResRttDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResRttDrops.setStatus(_A)
_HwNqaStatResRttSequenceErrors_Type=Counter32
_HwNqaStatResRttSequenceErrors_Object=MibTableColumn
hwNqaStatResRttSequenceErrors=_HwNqaStatResRttSequenceErrors_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,17),_HwNqaStatResRttSequenceErrors_Type())
hwNqaStatResRttSequenceErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResRttSequenceErrors.setStatus(_A)
_HwNqaStatResRttErrors_Type=Counter32
_HwNqaStatResRttErrors_Object=MibTableColumn
hwNqaStatResRttErrors=_HwNqaStatResRttErrors_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,18),_HwNqaStatResRttErrors_Type())
hwNqaStatResRttErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResRttErrors.setStatus(_A)
_HwNqaStatResLostPacketRatio_Type=Gauge32
_HwNqaStatResLostPacketRatio_Object=MibTableColumn
hwNqaStatResLostPacketRatio=_HwNqaStatResLostPacketRatio_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,19),_HwNqaStatResLostPacketRatio_Type())
hwNqaStatResLostPacketRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResLostPacketRatio.setStatus(_A)
_HwNqaStatResPacketLateArrival_Type=Counter32
_HwNqaStatResPacketLateArrival_Object=MibTableColumn
hwNqaStatResPacketLateArrival=_HwNqaStatResPacketLateArrival_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,20),_HwNqaStatResPacketLateArrival_Type())
hwNqaStatResPacketLateArrival.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResPacketLateArrival.setStatus(_A)
_HwNqaStatResRttSum_Type=Counter32
_HwNqaStatResRttSum_Object=MibTableColumn
hwNqaStatResRttSum=_HwNqaStatResRttSum_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,21),_HwNqaStatResRttSum_Type())
hwNqaStatResRttSum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResRttSum.setStatus(_A)
_HwNqaStatResNumOfDelaySD_Type=Counter32
_HwNqaStatResNumOfDelaySD_Object=MibTableColumn
hwNqaStatResNumOfDelaySD=_HwNqaStatResNumOfDelaySD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,22),_HwNqaStatResNumOfDelaySD_Type())
hwNqaStatResNumOfDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResNumOfDelaySD.setStatus(_A)
_HwNqaStatResMinDelaySD_Type=Gauge32
_HwNqaStatResMinDelaySD_Object=MibTableColumn
hwNqaStatResMinDelaySD=_HwNqaStatResMinDelaySD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,23),_HwNqaStatResMinDelaySD_Type())
hwNqaStatResMinDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResMinDelaySD.setStatus(_A)
_HwNqaStatResMaxDelaySD_Type=Gauge32
_HwNqaStatResMaxDelaySD_Object=MibTableColumn
hwNqaStatResMaxDelaySD=_HwNqaStatResMaxDelaySD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,24),_HwNqaStatResMaxDelaySD_Type())
hwNqaStatResMaxDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResMaxDelaySD.setStatus(_A)
_HwNqaStatResSumDelaySD_Type=Counter32
_HwNqaStatResSumDelaySD_Object=MibTableColumn
hwNqaStatResSumDelaySD=_HwNqaStatResSumDelaySD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,25),_HwNqaStatResSumDelaySD_Type())
hwNqaStatResSumDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResSumDelaySD.setStatus(_A)
_HwNqaStatResSum2DelaySD_Type=Counter32
_HwNqaStatResSum2DelaySD_Object=MibTableColumn
hwNqaStatResSum2DelaySD=_HwNqaStatResSum2DelaySD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,26),_HwNqaStatResSum2DelaySD_Type())
hwNqaStatResSum2DelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResSum2DelaySD.setStatus(_A)
_HwNqaStatResNumOfDelayDS_Type=Counter32
_HwNqaStatResNumOfDelayDS_Object=MibTableColumn
hwNqaStatResNumOfDelayDS=_HwNqaStatResNumOfDelayDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,27),_HwNqaStatResNumOfDelayDS_Type())
hwNqaStatResNumOfDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResNumOfDelayDS.setStatus(_A)
_HwNqaStatResMinDelayDS_Type=Gauge32
_HwNqaStatResMinDelayDS_Object=MibTableColumn
hwNqaStatResMinDelayDS=_HwNqaStatResMinDelayDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,28),_HwNqaStatResMinDelayDS_Type())
hwNqaStatResMinDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResMinDelayDS.setStatus(_A)
_HwNqaStatResMaxDelayDS_Type=Gauge32
_HwNqaStatResMaxDelayDS_Object=MibTableColumn
hwNqaStatResMaxDelayDS=_HwNqaStatResMaxDelayDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,29),_HwNqaStatResMaxDelayDS_Type())
hwNqaStatResMaxDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResMaxDelayDS.setStatus(_A)
_HwNqaStatResSumDelayDS_Type=Counter32
_HwNqaStatResSumDelayDS_Object=MibTableColumn
hwNqaStatResSumDelayDS=_HwNqaStatResSumDelayDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,30),_HwNqaStatResSumDelayDS_Type())
hwNqaStatResSumDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResSumDelayDS.setStatus(_A)
_HwNqaStatResSum2DelayDS_Type=Counter32
_HwNqaStatResSum2DelayDS_Object=MibTableColumn
hwNqaStatResSum2DelayDS=_HwNqaStatResSum2DelayDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,11,1,31),_HwNqaStatResSum2DelayDS_Type())
hwNqaStatResSum2DelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatResSum2DelayDS.setStatus(_A)
_HwNqaGroupStatsJitterTable_Object=MibTable
hwNqaGroupStatsJitterTable=_HwNqaGroupStatsJitterTable_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12))
if mibBuilder.loadTexts:hwNqaGroupStatsJitterTable.setStatus(_A)
_HwNqaGroupStatsJitterEntry_Object=MibTableRow
hwNqaGroupStatsJitterEntry=_HwNqaGroupStatsJitterEntry_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1))
hwNqaGroupStatsJitterEntry.setIndexNames((0,_D,_T),(0,_D,_U),(0,_C,_k))
if mibBuilder.loadTexts:hwNqaGroupStatsJitterEntry.setStatus(_A)
class _HwNqaStatJitterIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HwNqaStatJitterIndex_Type.__name__=_H
_HwNqaStatJitterIndex_Object=MibTableColumn
hwNqaStatJitterIndex=_HwNqaStatJitterIndex_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,1),_HwNqaStatJitterIndex_Type())
hwNqaStatJitterIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hwNqaStatJitterIndex.setStatus(_A)
_HwNqaStatJitterMinOfPosSD_Type=Gauge32
_HwNqaStatJitterMinOfPosSD_Object=MibTableColumn
hwNqaStatJitterMinOfPosSD=_HwNqaStatJitterMinOfPosSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,2),_HwNqaStatJitterMinOfPosSD_Type())
hwNqaStatJitterMinOfPosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterMinOfPosSD.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterMinOfPosSD.setUnits(_F)
_HwNqaStatJitterMaxOfPosSD_Type=Gauge32
_HwNqaStatJitterMaxOfPosSD_Object=MibTableColumn
hwNqaStatJitterMaxOfPosSD=_HwNqaStatJitterMaxOfPosSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,3),_HwNqaStatJitterMaxOfPosSD_Type())
hwNqaStatJitterMaxOfPosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterMaxOfPosSD.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterMaxOfPosSD.setUnits(_F)
_HwNqaStatJitterNumOfPosSD_Type=Counter32
_HwNqaStatJitterNumOfPosSD_Object=MibTableColumn
hwNqaStatJitterNumOfPosSD=_HwNqaStatJitterNumOfPosSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,4),_HwNqaStatJitterNumOfPosSD_Type())
hwNqaStatJitterNumOfPosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterNumOfPosSD.setStatus(_A)
_HwNqaStatJitterSumOfPosSD_Type=Counter32
_HwNqaStatJitterSumOfPosSD_Object=MibTableColumn
hwNqaStatJitterSumOfPosSD=_HwNqaStatJitterSumOfPosSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,5),_HwNqaStatJitterSumOfPosSD_Type())
hwNqaStatJitterSumOfPosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfPosSD.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfPosSD.setUnits(_F)
_HwNqaStatJitterSumOfSquarePosSD_Type=Counter32
_HwNqaStatJitterSumOfSquarePosSD_Object=MibTableColumn
hwNqaStatJitterSumOfSquarePosSD=_HwNqaStatJitterSumOfSquarePosSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,6),_HwNqaStatJitterSumOfSquarePosSD_Type())
hwNqaStatJitterSumOfSquarePosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfSquarePosSD.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfSquarePosSD.setUnits(_F)
_HwNqaStatJitterMinOfNegSD_Type=Gauge32
_HwNqaStatJitterMinOfNegSD_Object=MibTableColumn
hwNqaStatJitterMinOfNegSD=_HwNqaStatJitterMinOfNegSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,7),_HwNqaStatJitterMinOfNegSD_Type())
hwNqaStatJitterMinOfNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterMinOfNegSD.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterMinOfNegSD.setUnits(_F)
_HwNqaStatJitterMaxOfNegSD_Type=Gauge32
_HwNqaStatJitterMaxOfNegSD_Object=MibTableColumn
hwNqaStatJitterMaxOfNegSD=_HwNqaStatJitterMaxOfNegSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,8),_HwNqaStatJitterMaxOfNegSD_Type())
hwNqaStatJitterMaxOfNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterMaxOfNegSD.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterMaxOfNegSD.setUnits(_F)
_HwNqaStatJitterNumOfNegSD_Type=Counter32
_HwNqaStatJitterNumOfNegSD_Object=MibTableColumn
hwNqaStatJitterNumOfNegSD=_HwNqaStatJitterNumOfNegSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,9),_HwNqaStatJitterNumOfNegSD_Type())
hwNqaStatJitterNumOfNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterNumOfNegSD.setStatus(_A)
_HwNqaStatJitterSumOfNegSD_Type=Counter32
_HwNqaStatJitterSumOfNegSD_Object=MibTableColumn
hwNqaStatJitterSumOfNegSD=_HwNqaStatJitterSumOfNegSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,10),_HwNqaStatJitterSumOfNegSD_Type())
hwNqaStatJitterSumOfNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfNegSD.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfNegSD.setUnits(_F)
_HwNqaStatJitterSumOfSquareNegSD_Type=Counter32
_HwNqaStatJitterSumOfSquareNegSD_Object=MibTableColumn
hwNqaStatJitterSumOfSquareNegSD=_HwNqaStatJitterSumOfSquareNegSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,11),_HwNqaStatJitterSumOfSquareNegSD_Type())
hwNqaStatJitterSumOfSquareNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfSquareNegSD.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfSquareNegSD.setUnits(_F)
_HwNqaStatJitterMinOfPosDS_Type=Gauge32
_HwNqaStatJitterMinOfPosDS_Object=MibTableColumn
hwNqaStatJitterMinOfPosDS=_HwNqaStatJitterMinOfPosDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,12),_HwNqaStatJitterMinOfPosDS_Type())
hwNqaStatJitterMinOfPosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterMinOfPosDS.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterMinOfPosDS.setUnits(_F)
_HwNqaStatJitterMaxOfPosDS_Type=Gauge32
_HwNqaStatJitterMaxOfPosDS_Object=MibTableColumn
hwNqaStatJitterMaxOfPosDS=_HwNqaStatJitterMaxOfPosDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,13),_HwNqaStatJitterMaxOfPosDS_Type())
hwNqaStatJitterMaxOfPosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterMaxOfPosDS.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterMaxOfPosDS.setUnits(_F)
_HwNqaStatJitterNumOfPosDS_Type=Counter32
_HwNqaStatJitterNumOfPosDS_Object=MibTableColumn
hwNqaStatJitterNumOfPosDS=_HwNqaStatJitterNumOfPosDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,14),_HwNqaStatJitterNumOfPosDS_Type())
hwNqaStatJitterNumOfPosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterNumOfPosDS.setStatus(_A)
_HwNqaStatJitterSumOfPosDS_Type=Counter32
_HwNqaStatJitterSumOfPosDS_Object=MibTableColumn
hwNqaStatJitterSumOfPosDS=_HwNqaStatJitterSumOfPosDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,15),_HwNqaStatJitterSumOfPosDS_Type())
hwNqaStatJitterSumOfPosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfPosDS.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfPosDS.setUnits(_F)
_HwNqaStatJitterSumOfSquarePosDS_Type=Counter32
_HwNqaStatJitterSumOfSquarePosDS_Object=MibTableColumn
hwNqaStatJitterSumOfSquarePosDS=_HwNqaStatJitterSumOfSquarePosDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,16),_HwNqaStatJitterSumOfSquarePosDS_Type())
hwNqaStatJitterSumOfSquarePosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfSquarePosDS.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfSquarePosDS.setUnits(_F)
_HwNqaStatJitterMinOfNegDS_Type=Gauge32
_HwNqaStatJitterMinOfNegDS_Object=MibTableColumn
hwNqaStatJitterMinOfNegDS=_HwNqaStatJitterMinOfNegDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,17),_HwNqaStatJitterMinOfNegDS_Type())
hwNqaStatJitterMinOfNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterMinOfNegDS.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterMinOfNegDS.setUnits(_F)
_HwNqaStatJitterMaxOfNegDS_Type=Gauge32
_HwNqaStatJitterMaxOfNegDS_Object=MibTableColumn
hwNqaStatJitterMaxOfNegDS=_HwNqaStatJitterMaxOfNegDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,18),_HwNqaStatJitterMaxOfNegDS_Type())
hwNqaStatJitterMaxOfNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterMaxOfNegDS.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterMaxOfNegDS.setUnits(_F)
_HwNqaStatJitterNumOfNegDS_Type=Counter32
_HwNqaStatJitterNumOfNegDS_Object=MibTableColumn
hwNqaStatJitterNumOfNegDS=_HwNqaStatJitterNumOfNegDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,19),_HwNqaStatJitterNumOfNegDS_Type())
hwNqaStatJitterNumOfNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterNumOfNegDS.setStatus(_A)
_HwNqaStatJitterSumOfNegDS_Type=Counter32
_HwNqaStatJitterSumOfNegDS_Object=MibTableColumn
hwNqaStatJitterSumOfNegDS=_HwNqaStatJitterSumOfNegDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,20),_HwNqaStatJitterSumOfNegDS_Type())
hwNqaStatJitterSumOfNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfNegDS.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfNegDS.setUnits(_F)
_HwNqaStatJitterSumOfSquareNegDS_Type=Counter32
_HwNqaStatJitterSumOfSquareNegDS_Object=MibTableColumn
hwNqaStatJitterSumOfSquareNegDS=_HwNqaStatJitterSumOfSquareNegDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,21),_HwNqaStatJitterSumOfSquareNegDS_Type())
hwNqaStatJitterSumOfSquareNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfSquareNegDS.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterSumOfSquareNegDS.setUnits(_F)
_HwNqaStatJitterPacketLossSD_Type=Counter32
_HwNqaStatJitterPacketLossSD_Object=MibTableColumn
hwNqaStatJitterPacketLossSD=_HwNqaStatJitterPacketLossSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,22),_HwNqaStatJitterPacketLossSD_Type())
hwNqaStatJitterPacketLossSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterPacketLossSD.setStatus(_A)
_HwNqaStatJitterPacketLossDS_Type=Counter32
_HwNqaStatJitterPacketLossDS_Object=MibTableColumn
hwNqaStatJitterPacketLossDS=_HwNqaStatJitterPacketLossDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,23),_HwNqaStatJitterPacketLossDS_Type())
hwNqaStatJitterPacketLossDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterPacketLossDS.setStatus(_A)
_HwNqaStatJitterAvePosSD_Type=Gauge32
_HwNqaStatJitterAvePosSD_Object=MibTableColumn
hwNqaStatJitterAvePosSD=_HwNqaStatJitterAvePosSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,24),_HwNqaStatJitterAvePosSD_Type())
hwNqaStatJitterAvePosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterAvePosSD.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterAvePosSD.setUnits(_F)
_HwNqaStatJitterAveNegSD_Type=Gauge32
_HwNqaStatJitterAveNegSD_Object=MibTableColumn
hwNqaStatJitterAveNegSD=_HwNqaStatJitterAveNegSD_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,25),_HwNqaStatJitterAveNegSD_Type())
hwNqaStatJitterAveNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterAveNegSD.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterAveNegSD.setUnits(_F)
_HwNqaStatJitterAvePosDS_Type=Gauge32
_HwNqaStatJitterAvePosDS_Object=MibTableColumn
hwNqaStatJitterAvePosDS=_HwNqaStatJitterAvePosDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,26),_HwNqaStatJitterAvePosDS_Type())
hwNqaStatJitterAvePosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterAvePosDS.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterAvePosDS.setUnits(_F)
_HwNqaStatJitterAveNegDS_Type=Gauge32
_HwNqaStatJitterAveNegDS_Object=MibTableColumn
hwNqaStatJitterAveNegDS=_HwNqaStatJitterAveNegDS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,27),_HwNqaStatJitterAveNegDS_Type())
hwNqaStatJitterAveNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterAveNegDS.setStatus(_A)
if mibBuilder.loadTexts:hwNqaStatJitterAveNegDS.setUnits(_F)
_HwNqaStatJitterPktLossUnknown_Type=Counter32
_HwNqaStatJitterPktLossUnknown_Object=MibTableColumn
hwNqaStatJitterPktLossUnknown=_HwNqaStatJitterPktLossUnknown_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,28),_HwNqaStatJitterPktLossUnknown_Type())
hwNqaStatJitterPktLossUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterPktLossUnknown.setStatus(_A)
_HwNqaStatJitterMaxOfICPIF_Type=Gauge32
_HwNqaStatJitterMaxOfICPIF_Object=MibTableColumn
hwNqaStatJitterMaxOfICPIF=_HwNqaStatJitterMaxOfICPIF_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,29),_HwNqaStatJitterMaxOfICPIF_Type())
hwNqaStatJitterMaxOfICPIF.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterMaxOfICPIF.setStatus(_A)
_HwNqaStatJitterMinOfICPIF_Type=Gauge32
_HwNqaStatJitterMinOfICPIF_Object=MibTableColumn
hwNqaStatJitterMinOfICPIF=_HwNqaStatJitterMinOfICPIF_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,30),_HwNqaStatJitterMinOfICPIF_Type())
hwNqaStatJitterMinOfICPIF.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterMinOfICPIF.setStatus(_A)
_HwNqaStatJitterMaxOfMOS_Type=Gauge32
_HwNqaStatJitterMaxOfMOS_Object=MibTableColumn
hwNqaStatJitterMaxOfMOS=_HwNqaStatJitterMaxOfMOS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,31),_HwNqaStatJitterMaxOfMOS_Type())
hwNqaStatJitterMaxOfMOS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterMaxOfMOS.setStatus(_A)
_HwNqaStatJitterMinOfMOS_Type=Gauge32
_HwNqaStatJitterMinOfMOS_Object=MibTableColumn
hwNqaStatJitterMinOfMOS=_HwNqaStatJitterMinOfMOS_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,12,1,32),_HwNqaStatJitterMinOfMOS_Type())
hwNqaStatJitterMinOfMOS.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatJitterMinOfMOS.setStatus(_A)
_HwNqaReactionTable_Object=MibTable
hwNqaReactionTable=_HwNqaReactionTable_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13))
if mibBuilder.loadTexts:hwNqaReactionTable.setStatus(_A)
_HwNqaReactionEntry_Object=MibTableRow
hwNqaReactionEntry=_HwNqaReactionEntry_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1))
hwNqaReactionEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:hwNqaReactionEntry.setStatus(_A)
class _HwNqaReactOwnerIndex_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HwNqaReactOwnerIndex_Type.__name__=_V
_HwNqaReactOwnerIndex_Object=MibTableColumn
hwNqaReactOwnerIndex=_HwNqaReactOwnerIndex_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,1),_HwNqaReactOwnerIndex_Type())
hwNqaReactOwnerIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:hwNqaReactOwnerIndex.setStatus(_A)
class _HwNqaReactTestName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HwNqaReactTestName_Type.__name__=_V
_HwNqaReactTestName_Object=MibTableColumn
hwNqaReactTestName=_HwNqaReactTestName_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,2),_HwNqaReactTestName_Type())
hwNqaReactTestName.setMaxAccess(_Z)
if mibBuilder.loadTexts:hwNqaReactTestName.setStatus(_A)
class _HwNqaReactItemIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HwNqaReactItemIndex_Type.__name__=_H
_HwNqaReactItemIndex_Object=MibTableColumn
hwNqaReactItemIndex=_HwNqaReactItemIndex_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,3),_HwNqaReactItemIndex_Type())
hwNqaReactItemIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:hwNqaReactItemIndex.setStatus(_A)
class _HwNqaReactCheckedElement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('probetime',1),('probefailure',2),('jitterrtt',3),('jitterpacketloss',4),('jittersd',5),('jitterds',6),('icpif',7),('mos',8),('jitterOwdSD',9),('jitterOwdDS',10)))
_HwNqaReactCheckedElement_Type.__name__=_G
_HwNqaReactCheckedElement_Object=MibTableColumn
hwNqaReactCheckedElement=_HwNqaReactCheckedElement_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,4),_HwNqaReactCheckedElement_Type())
hwNqaReactCheckedElement.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaReactCheckedElement.setStatus(_A)
class _HwNqaReactThresholdUpperLimit_Type(Unsigned32):defaultValue=0
_HwNqaReactThresholdUpperLimit_Type.__name__=_H
_HwNqaReactThresholdUpperLimit_Object=MibTableColumn
hwNqaReactThresholdUpperLimit=_HwNqaReactThresholdUpperLimit_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,5),_HwNqaReactThresholdUpperLimit_Type())
hwNqaReactThresholdUpperLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaReactThresholdUpperLimit.setStatus(_A)
class _HwNqaReactThresholdLowerLimit_Type(Unsigned32):defaultValue=0
_HwNqaReactThresholdLowerLimit_Type.__name__=_H
_HwNqaReactThresholdLowerLimit_Object=MibTableColumn
hwNqaReactThresholdLowerLimit=_HwNqaReactThresholdLowerLimit_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,6),_HwNqaReactThresholdLowerLimit_Type())
hwNqaReactThresholdLowerLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaReactThresholdLowerLimit.setStatus(_A)
class _HwNqaReactThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_l,0),('average',1),('consecutive',2),('accumulative',3)))
_HwNqaReactThresholdType_Type.__name__=_G
_HwNqaReactThresholdType_Object=MibTableColumn
hwNqaReactThresholdType=_HwNqaReactThresholdType_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,7),_HwNqaReactThresholdType_Type())
hwNqaReactThresholdType.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaReactThresholdType.setStatus(_A)
class _HwNqaReactThresholdConsecNum_Type(Unsigned32):defaultValue=0
_HwNqaReactThresholdConsecNum_Type.__name__=_H
_HwNqaReactThresholdConsecNum_Object=MibTableColumn
hwNqaReactThresholdConsecNum=_HwNqaReactThresholdConsecNum_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,8),_HwNqaReactThresholdConsecNum_Type())
hwNqaReactThresholdConsecNum.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaReactThresholdConsecNum.setStatus(_A)
class _HwNqaReactThresholdAccumNum_Type(Unsigned32):defaultValue=0
_HwNqaReactThresholdAccumNum_Type.__name__=_H
_HwNqaReactThresholdAccumNum_Object=MibTableColumn
hwNqaReactThresholdAccumNum=_HwNqaReactThresholdAccumNum_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,9),_HwNqaReactThresholdAccumNum_Type())
hwNqaReactThresholdAccumNum.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaReactThresholdAccumNum.setStatus(_A)
class _HwNqaReactActionType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('trapOnly',1),('triggerOnly',2),('trapAndTrigger',3)))
_HwNqaReactActionType_Type.__name__=_G
_HwNqaReactActionType_Object=MibTableColumn
hwNqaReactActionType=_HwNqaReactActionType_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,10),_HwNqaReactActionType_Type())
hwNqaReactActionType.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaReactActionType.setStatus(_A)
class _HwNqaReactCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),('overThreshold',2),('belowThreshold',3)))
_HwNqaReactCurrentStatus_Type.__name__=_G
_HwNqaReactCurrentStatus_Object=MibTableColumn
hwNqaReactCurrentStatus=_HwNqaReactCurrentStatus_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,11),_HwNqaReactCurrentStatus_Type())
hwNqaReactCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaReactCurrentStatus.setStatus(_A)
_HwNqaReactRowStatus_Type=RowStatus
_HwNqaReactRowStatus_Object=MibTableColumn
hwNqaReactRowStatus=_HwNqaReactRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,12),_HwNqaReactRowStatus_Type())
hwNqaReactRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwNqaReactRowStatus.setStatus(_A)
class _HwNqaReactCheckedNum_Type(Unsigned32):defaultValue=0
_HwNqaReactCheckedNum_Type.__name__=_H
_HwNqaReactCheckedNum_Object=MibTableColumn
hwNqaReactCheckedNum=_HwNqaReactCheckedNum_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,13),_HwNqaReactCheckedNum_Type())
hwNqaReactCheckedNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaReactCheckedNum.setStatus(_A)
class _HwNqaReactThresholdNum_Type(Unsigned32):defaultValue=0
_HwNqaReactThresholdNum_Type.__name__=_H
_HwNqaReactThresholdNum_Object=MibTableColumn
hwNqaReactThresholdNum=_HwNqaReactThresholdNum_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,13,1,14),_HwNqaReactThresholdNum_Type())
hwNqaReactThresholdNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaReactThresholdNum.setStatus(_A)
_HwNqaStatisticsReactionTable_Object=MibTable
hwNqaStatisticsReactionTable=_HwNqaStatisticsReactionTable_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,14))
if mibBuilder.loadTexts:hwNqaStatisticsReactionTable.setStatus(_A)
_HwNqaStatisticsReactionEntry_Object=MibTableRow
hwNqaStatisticsReactionEntry=_HwNqaStatisticsReactionEntry_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,14,1))
hwNqaStatisticsReactionEntry.setIndexNames((0,_C,_m),(0,_C,_n),(0,_C,_o),(0,_C,_p))
if mibBuilder.loadTexts:hwNqaStatisticsReactionEntry.setStatus(_A)
class _HwNqaStatReactOwnerIndex_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HwNqaStatReactOwnerIndex_Type.__name__=_V
_HwNqaStatReactOwnerIndex_Object=MibTableColumn
hwNqaStatReactOwnerIndex=_HwNqaStatReactOwnerIndex_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,14,1,1),_HwNqaStatReactOwnerIndex_Type())
hwNqaStatReactOwnerIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hwNqaStatReactOwnerIndex.setStatus(_A)
class _HwNqaStatReactTestName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HwNqaStatReactTestName_Type.__name__=_V
_HwNqaStatReactTestName_Object=MibTableColumn
hwNqaStatReactTestName=_HwNqaStatReactTestName_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,14,1,2),_HwNqaStatReactTestName_Type())
hwNqaStatReactTestName.setMaxAccess(_I)
if mibBuilder.loadTexts:hwNqaStatReactTestName.setStatus(_A)
class _HwNqaStatReactIndex_Type(Unsigned32):defaultValue=0
_HwNqaStatReactIndex_Type.__name__=_H
_HwNqaStatReactIndex_Object=MibTableColumn
hwNqaStatReactIndex=_HwNqaStatReactIndex_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,14,1,3),_HwNqaStatReactIndex_Type())
hwNqaStatReactIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hwNqaStatReactIndex.setStatus(_A)
class _HwNqaStatReactItemIndex_Type(Unsigned32):defaultValue=0
_HwNqaStatReactItemIndex_Type.__name__=_H
_HwNqaStatReactItemIndex_Object=MibTableColumn
hwNqaStatReactItemIndex=_HwNqaStatReactItemIndex_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,14,1,4),_HwNqaStatReactItemIndex_Type())
hwNqaStatReactItemIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hwNqaStatReactItemIndex.setStatus(_A)
class _HwNqaStatReactCheckedNum_Type(Counter32):defaultValue=0
_HwNqaStatReactCheckedNum_Type.__name__=_X
_HwNqaStatReactCheckedNum_Object=MibTableColumn
hwNqaStatReactCheckedNum=_HwNqaStatReactCheckedNum_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,14,1,5),_HwNqaStatReactCheckedNum_Type())
hwNqaStatReactCheckedNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatReactCheckedNum.setStatus(_A)
class _HwNqaStatReactThresholdNum_Type(Counter32):defaultValue=0
_HwNqaStatReactThresholdNum_Type.__name__=_X
_HwNqaStatReactThresholdNum_Object=MibTableColumn
hwNqaStatReactThresholdNum=_HwNqaStatReactThresholdNum_Object((1,3,6,1,4,1,43,45,1,5,25,28,1,14,1,6),_HwNqaStatReactThresholdNum_Type())
hwNqaStatReactThresholdNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwNqaStatReactThresholdNum.setStatus(_A)
_HwNqaImplementationTypeDomains_ObjectIdentity=ObjectIdentity
hwNqaImplementationTypeDomains=_HwNqaImplementationTypeDomains_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,28,2))
_HwNqaUdpEcho_ObjectIdentity=ObjectIdentity
hwNqaUdpEcho=_HwNqaUdpEcho_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,28,2,1))
if mibBuilder.loadTexts:hwNqaUdpEcho.setStatus(_A)
_HwNqaTcpconnect_ObjectIdentity=ObjectIdentity
hwNqaTcpconnect=_HwNqaTcpconnect_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,28,2,2))
if mibBuilder.loadTexts:hwNqaTcpconnect.setStatus(_A)
_HwNqajitter_ObjectIdentity=ObjectIdentity
hwNqajitter=_HwNqajitter_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,28,2,3))
if mibBuilder.loadTexts:hwNqajitter.setStatus(_A)
_HwNqaHttp_ObjectIdentity=ObjectIdentity
hwNqaHttp=_HwNqaHttp_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,28,2,4))
if mibBuilder.loadTexts:hwNqaHttp.setStatus(_A)
_HwNqadlsw_ObjectIdentity=ObjectIdentity
hwNqadlsw=_HwNqadlsw_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,28,2,5))
if mibBuilder.loadTexts:hwNqadlsw.setStatus(_A)
_HwNqadhcp_ObjectIdentity=ObjectIdentity
hwNqadhcp=_HwNqadhcp_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,28,2,6))
if mibBuilder.loadTexts:hwNqadhcp.setStatus(_A)
_HwNqaftp_ObjectIdentity=ObjectIdentity
hwNqaftp=_HwNqaftp_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,28,2,7))
if mibBuilder.loadTexts:hwNqaftp.setStatus(_A)
_HwNqaNotifications_ObjectIdentity=ObjectIdentity
hwNqaNotifications=_HwNqaNotifications_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,28,3))
pingCtlEntry.registerAugmentions((_C,_q))
hwNqaCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())
pingCtlEntry.registerAugmentions((_C,_r))
hwNqaStatisticsCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())
hwNqaProbeTimeOverThreshold=NotificationType((1,3,6,1,4,1,43,45,1,5,25,28,3,1))
hwNqaProbeTimeOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:hwNqaProbeTimeOverThreshold.setStatus(_A)
hwNqaJitterRTTOverThreshold=NotificationType((1,3,6,1,4,1,43,45,1,5,25,28,3,2))
hwNqaJitterRTTOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:hwNqaJitterRTTOverThreshold.setStatus(_A)
hwNqaProbeFailure=NotificationType((1,3,6,1,4,1,43,45,1,5,25,28,3,3))
hwNqaProbeFailure.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:hwNqaProbeFailure.setStatus(_A)
hwNqaJitterPacketLoss=NotificationType((1,3,6,1,4,1,43,45,1,5,25,28,3,4))
hwNqaJitterPacketLoss.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:hwNqaJitterPacketLoss.setStatus(_A)
hwNqaJitterSDOverThreshold=NotificationType((1,3,6,1,4,1,43,45,1,5,25,28,3,5))
hwNqaJitterSDOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:hwNqaJitterSDOverThreshold.setStatus(_A)
hwNqaJitterDSOverThreshold=NotificationType((1,3,6,1,4,1,43,45,1,5,25,28,3,6))
hwNqaJitterDSOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:hwNqaJitterDSOverThreshold.setStatus(_A)
hwNqaICPIFOverThreshold=NotificationType((1,3,6,1,4,1,43,45,1,5,25,28,3,7))
hwNqaICPIFOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_Q)))
if mibBuilder.loadTexts:hwNqaICPIFOverThreshold.setStatus(_A)
hwNqaMOSOverThreshold=NotificationType((1,3,6,1,4,1,43,45,1,5,25,28,3,8))
hwNqaMOSOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_D,_O),(_D,_N),(_D,_P),(_D,_M),(_C,_Q)))
if mibBuilder.loadTexts:hwNqaMOSOverThreshold.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hwNqa':hwNqa,'hwNqaObjects':hwNqaObjects,'hwNqaMIBVersion':hwNqaMIBVersion,'hwNqaCtlTable':hwNqaCtlTable,_q:hwNqaCtlEntry,'hwNqaCtlTargetPort':hwNqaCtlTargetPort,'hwNqaCtlSourcePort':hwNqaCtlSourcePort,'hwNqaCtlTTL':hwNqaCtlTTL,'hwNqaCtlJitterAdminInterval':hwNqaCtlJitterAdminInterval,'hwNqaCtlJitterAdminNumPackets':hwNqaCtlJitterAdminNumPackets,'hwNqaCtlHttpOperationType':hwNqaCtlHttpOperationType,'hwNqaCtlHttpOperationString':hwNqaCtlHttpOperationString,'hwNqaCtlFtpOperationType':hwNqaCtlFtpOperationType,'hwNqaCtlFtpUsername':hwNqaCtlFtpUsername,'hwNqaCtlFtpPassword':hwNqaCtlFtpPassword,'hwNqaCtlFtpOperationString':hwNqaCtlFtpOperationString,'hwNqaCtlVPNInstance':hwNqaCtlVPNInstance,'hwNqaCtlHistoryKeptTime':hwNqaCtlHistoryKeptTime,'hwNqaCtlHistoryEnable':hwNqaCtlHistoryEnable,'hwNqaCtlICPIFAdvFactor':hwNqaCtlICPIFAdvFactor,'hwNqaCtlCodecType':hwNqaCtlCodecType,'hwNqaResultsTable':hwNqaResultsTable,'hwNqaResultsEntry':hwNqaResultsEntry,'hwNqaResultsRttNumDisconnects':hwNqaResultsRttNumDisconnects,'hwNqaResultsRttTimeouts':hwNqaResultsRttTimeouts,'hwNqaResultsRttBusies':hwNqaResultsRttBusies,'hwNqaResultsRttNoConnections':hwNqaResultsRttNoConnections,'hwNqaResultsRttDrops':hwNqaResultsRttDrops,'hwNqaResultsRttSequenceErrors':hwNqaResultsRttSequenceErrors,'hwNqaResultsRttStatsErrors':hwNqaResultsRttStatsErrors,'hwNqaResultsMaxDelaySD':hwNqaResultsMaxDelaySD,'hwNqaResultsMaxDelayDS':hwNqaResultsMaxDelayDS,'hwNqaResultsLostPacketRatio':hwNqaResultsLostPacketRatio,'hwNqaResultsPacketLateArrival':hwNqaResultsPacketLateArrival,'hwNqaResultsRttSum':hwNqaResultsRttSum,'hwNqaResultsNumOfDelaySD':hwNqaResultsNumOfDelaySD,'hwNqaResultsMinDelaySD':hwNqaResultsMinDelaySD,'hwNqaResultsSumDelaySD':hwNqaResultsSumDelaySD,'hwNqaResultsSum2DelaySD':hwNqaResultsSum2DelaySD,'hwNqaResultsNumOfDelayDS':hwNqaResultsNumOfDelayDS,'hwNqaResultsMinDelayDS':hwNqaResultsMinDelayDS,'hwNqaResultsSumDelayDS':hwNqaResultsSumDelayDS,'hwNqaResultsSum2DelayDS':hwNqaResultsSum2DelayDS,'hwNqaJitterStatsTable':hwNqaJitterStatsTable,'hwNqaJitterStatsEntry':hwNqaJitterStatsEntry,'hwNqaJitterStatsNumOfRTT':hwNqaJitterStatsNumOfRTT,'hwNqaJitterStatsMinOfPositivesSD':hwNqaJitterStatsMinOfPositivesSD,'hwNqaJitterStatsMaxOfPositivesSD':hwNqaJitterStatsMaxOfPositivesSD,'hwNqaJitterStatsNumOfPositivesSD':hwNqaJitterStatsNumOfPositivesSD,'hwNqaJitterStatsSumOfPositivesSD':hwNqaJitterStatsSumOfPositivesSD,'hwNqaJitterStatsSum2PositivesSD':hwNqaJitterStatsSum2PositivesSD,'hwNqaJitterStatsMinOfNegativesSD':hwNqaJitterStatsMinOfNegativesSD,'hwNqaJitterStatsMaxOfNegativesSD':hwNqaJitterStatsMaxOfNegativesSD,'hwNqaJitterStatsNumOfNegativesSD':hwNqaJitterStatsNumOfNegativesSD,'hwNqaJitterStatsSumOfNegativesSD':hwNqaJitterStatsSumOfNegativesSD,'hwNqaJitterStatsSum2NegativesSD':hwNqaJitterStatsSum2NegativesSD,'hwNqaJitterStatsMinOfPositivesDS':hwNqaJitterStatsMinOfPositivesDS,'hwNqaJitterStatsMaxOfPositivesDS':hwNqaJitterStatsMaxOfPositivesDS,'hwNqaJitterStatsNumOfPositivesDS':hwNqaJitterStatsNumOfPositivesDS,'hwNqaJitterStatsSumOfPositivesDS':hwNqaJitterStatsSumOfPositivesDS,'hwNqaJitterStatsSum2PositivesDS':hwNqaJitterStatsSum2PositivesDS,'hwNqaJitterStatsMinOfNegativesDS':hwNqaJitterStatsMinOfNegativesDS,'hwNqaJitterStatsMaxOfNegativesDS':hwNqaJitterStatsMaxOfNegativesDS,'hwNqaJitterStatsNumOfNegativesDS':hwNqaJitterStatsNumOfNegativesDS,'hwNqaJitterStatsSumOfNegativesDS':hwNqaJitterStatsSumOfNegativesDS,'hwNqaJitterStatsSum2NegativesDS':hwNqaJitterStatsSum2NegativesDS,'hwNqaJitterStatsPacketLossSD':hwNqaJitterStatsPacketLossSD,'hwNqaJitterStatsPacketLossDS':hwNqaJitterStatsPacketLossDS,'hwNqaJitterStatsAvePositivesSD':hwNqaJitterStatsAvePositivesSD,'hwNqaJitterStatsAveNegativesSD':hwNqaJitterStatsAveNegativesSD,'hwNqaJitterStatsAvePositivesDS':hwNqaJitterStatsAvePositivesDS,'hwNqaJitterStatsAveNegativesDS':hwNqaJitterStatsAveNegativesDS,'hwNqaJitterStatsPktLossUnknown':hwNqaJitterStatsPktLossUnknown,'hwNqaJitterStatsOperOfICPIF':hwNqaJitterStatsOperOfICPIF,'hwNqaJitterStatsOperOfMOS':hwNqaJitterStatsOperOfMOS,'hwNqaAgentEnable':hwNqaAgentEnable,'hwNqaTcpServerTable':hwNqaTcpServerTable,'hwNqaTcpServerEntry':hwNqaTcpServerEntry,_e:hwNqaTcpServerIpAddress,_f:hwNqaTcpServerPort,'hwNqaTcpServerRowStatus':hwNqaTcpServerRowStatus,'hwNqaUdpServerTable':hwNqaUdpServerTable,'hwNqaUdpServerEntry':hwNqaUdpServerEntry,_g:hwNqaUdpServerIpAddress,_h:hwNqaUdpServerPort,'hwNqaUdpServerRowStatus':hwNqaUdpServerRowStatus,'hwNqaServerEnable':hwNqaServerEnable,'hwNqaStatsMaxGroupNumber':hwNqaStatsMaxGroupNumber,'hwNqaStatisticsCtlTable':hwNqaStatisticsCtlTable,_r:hwNqaStatisticsCtlEntry,'hwNqaCtlStatisticsInterval':hwNqaCtlStatisticsInterval,'hwNqaCtlStatisticsGroupNumber':hwNqaCtlStatisticsGroupNumber,'hwNqaCtlStatisticsKeptTime':hwNqaCtlStatisticsKeptTime,'hwNqaCtlBeginTime':hwNqaCtlBeginTime,'hwNqaCtlLifeTime':hwNqaCtlLifeTime,'hwNqaStatisticsResultsTable':hwNqaStatisticsResultsTable,'hwNqaStatisticsResultsEntry':hwNqaStatisticsResultsEntry,_j:hwNqaStatResIndex,'hwNqaStatResIpTargetAddressType':hwNqaStatResIpTargetAddressType,'hwNqaStatResIpTargetAddress':hwNqaStatResIpTargetAddress,'hwNqaStatResMinRtt':hwNqaStatResMinRtt,'hwNqaStatResMaxRtt':hwNqaStatResMaxRtt,'hwNqaStatResAverageRtt':hwNqaStatResAverageRtt,'hwNqaStatResProbeResponses':hwNqaStatResProbeResponses,'hwNqaStatResSentProbes':hwNqaStatResSentProbes,'hwNqaStatResRttSumOfSquares':hwNqaStatResRttSumOfSquares,'hwNqaStatResStartTime':hwNqaStatResStartTime,'hwNqaStatResInterval':hwNqaStatResInterval,'hwNqaStatResRttNumDisconnects':hwNqaStatResRttNumDisconnects,'hwNqaStatResRttTimeouts':hwNqaStatResRttTimeouts,'hwNqaStatResRttBusies':hwNqaStatResRttBusies,'hwNqaStatResRttNoConnections':hwNqaStatResRttNoConnections,'hwNqaStatResRttDrops':hwNqaStatResRttDrops,'hwNqaStatResRttSequenceErrors':hwNqaStatResRttSequenceErrors,'hwNqaStatResRttErrors':hwNqaStatResRttErrors,'hwNqaStatResLostPacketRatio':hwNqaStatResLostPacketRatio,'hwNqaStatResPacketLateArrival':hwNqaStatResPacketLateArrival,'hwNqaStatResRttSum':hwNqaStatResRttSum,'hwNqaStatResNumOfDelaySD':hwNqaStatResNumOfDelaySD,'hwNqaStatResMinDelaySD':hwNqaStatResMinDelaySD,'hwNqaStatResMaxDelaySD':hwNqaStatResMaxDelaySD,'hwNqaStatResSumDelaySD':hwNqaStatResSumDelaySD,'hwNqaStatResSum2DelaySD':hwNqaStatResSum2DelaySD,'hwNqaStatResNumOfDelayDS':hwNqaStatResNumOfDelayDS,'hwNqaStatResMinDelayDS':hwNqaStatResMinDelayDS,'hwNqaStatResMaxDelayDS':hwNqaStatResMaxDelayDS,'hwNqaStatResSumDelayDS':hwNqaStatResSumDelayDS,'hwNqaStatResSum2DelayDS':hwNqaStatResSum2DelayDS,'hwNqaGroupStatsJitterTable':hwNqaGroupStatsJitterTable,'hwNqaGroupStatsJitterEntry':hwNqaGroupStatsJitterEntry,_k:hwNqaStatJitterIndex,'hwNqaStatJitterMinOfPosSD':hwNqaStatJitterMinOfPosSD,'hwNqaStatJitterMaxOfPosSD':hwNqaStatJitterMaxOfPosSD,'hwNqaStatJitterNumOfPosSD':hwNqaStatJitterNumOfPosSD,'hwNqaStatJitterSumOfPosSD':hwNqaStatJitterSumOfPosSD,'hwNqaStatJitterSumOfSquarePosSD':hwNqaStatJitterSumOfSquarePosSD,'hwNqaStatJitterMinOfNegSD':hwNqaStatJitterMinOfNegSD,'hwNqaStatJitterMaxOfNegSD':hwNqaStatJitterMaxOfNegSD,'hwNqaStatJitterNumOfNegSD':hwNqaStatJitterNumOfNegSD,'hwNqaStatJitterSumOfNegSD':hwNqaStatJitterSumOfNegSD,'hwNqaStatJitterSumOfSquareNegSD':hwNqaStatJitterSumOfSquareNegSD,'hwNqaStatJitterMinOfPosDS':hwNqaStatJitterMinOfPosDS,'hwNqaStatJitterMaxOfPosDS':hwNqaStatJitterMaxOfPosDS,'hwNqaStatJitterNumOfPosDS':hwNqaStatJitterNumOfPosDS,'hwNqaStatJitterSumOfPosDS':hwNqaStatJitterSumOfPosDS,'hwNqaStatJitterSumOfSquarePosDS':hwNqaStatJitterSumOfSquarePosDS,'hwNqaStatJitterMinOfNegDS':hwNqaStatJitterMinOfNegDS,'hwNqaStatJitterMaxOfNegDS':hwNqaStatJitterMaxOfNegDS,'hwNqaStatJitterNumOfNegDS':hwNqaStatJitterNumOfNegDS,'hwNqaStatJitterSumOfNegDS':hwNqaStatJitterSumOfNegDS,'hwNqaStatJitterSumOfSquareNegDS':hwNqaStatJitterSumOfSquareNegDS,'hwNqaStatJitterPacketLossSD':hwNqaStatJitterPacketLossSD,'hwNqaStatJitterPacketLossDS':hwNqaStatJitterPacketLossDS,'hwNqaStatJitterAvePosSD':hwNqaStatJitterAvePosSD,'hwNqaStatJitterAveNegSD':hwNqaStatJitterAveNegSD,'hwNqaStatJitterAvePosDS':hwNqaStatJitterAvePosDS,'hwNqaStatJitterAveNegDS':hwNqaStatJitterAveNegDS,'hwNqaStatJitterPktLossUnknown':hwNqaStatJitterPktLossUnknown,'hwNqaStatJitterMaxOfICPIF':hwNqaStatJitterMaxOfICPIF,'hwNqaStatJitterMinOfICPIF':hwNqaStatJitterMinOfICPIF,'hwNqaStatJitterMaxOfMOS':hwNqaStatJitterMaxOfMOS,'hwNqaStatJitterMinOfMOS':hwNqaStatJitterMinOfMOS,'hwNqaReactionTable':hwNqaReactionTable,'hwNqaReactionEntry':hwNqaReactionEntry,_J:hwNqaReactOwnerIndex,_K:hwNqaReactTestName,_L:hwNqaReactItemIndex,'hwNqaReactCheckedElement':hwNqaReactCheckedElement,'hwNqaReactThresholdUpperLimit':hwNqaReactThresholdUpperLimit,'hwNqaReactThresholdLowerLimit':hwNqaReactThresholdLowerLimit,_R:hwNqaReactThresholdType,'hwNqaReactThresholdConsecNum':hwNqaReactThresholdConsecNum,'hwNqaReactThresholdAccumNum':hwNqaReactThresholdAccumNum,'hwNqaReactActionType':hwNqaReactActionType,_Q:hwNqaReactCurrentStatus,'hwNqaReactRowStatus':hwNqaReactRowStatus,'hwNqaReactCheckedNum':hwNqaReactCheckedNum,'hwNqaReactThresholdNum':hwNqaReactThresholdNum,'hwNqaStatisticsReactionTable':hwNqaStatisticsReactionTable,'hwNqaStatisticsReactionEntry':hwNqaStatisticsReactionEntry,_m:hwNqaStatReactOwnerIndex,_n:hwNqaStatReactTestName,_o:hwNqaStatReactIndex,_p:hwNqaStatReactItemIndex,'hwNqaStatReactCheckedNum':hwNqaStatReactCheckedNum,'hwNqaStatReactThresholdNum':hwNqaStatReactThresholdNum,'hwNqaImplementationTypeDomains':hwNqaImplementationTypeDomains,'hwNqaUdpEcho':hwNqaUdpEcho,'hwNqaTcpconnect':hwNqaTcpconnect,'hwNqajitter':hwNqajitter,'hwNqaHttp':hwNqaHttp,'hwNqadlsw':hwNqadlsw,'hwNqadhcp':hwNqadhcp,'hwNqaftp':hwNqaftp,'hwNqaNotifications':hwNqaNotifications,'hwNqaProbeTimeOverThreshold':hwNqaProbeTimeOverThreshold,'hwNqaJitterRTTOverThreshold':hwNqaJitterRTTOverThreshold,'hwNqaProbeFailure':hwNqaProbeFailure,'hwNqaJitterPacketLoss':hwNqaJitterPacketLoss,'hwNqaJitterSDOverThreshold':hwNqaJitterSDOverThreshold,'hwNqaJitterDSOverThreshold':hwNqaJitterDSOverThreshold,'hwNqaICPIFOverThreshold':hwNqaICPIFOverThreshold,'hwNqaMOSOverThreshold':hwNqaMOSOverThreshold})