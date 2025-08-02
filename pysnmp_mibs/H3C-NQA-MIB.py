_A0='h3cNqaStatisticsCtlEntry'
_z='h3cNqaCtlEntry'
_y='h3cNqaUdpServerExtVPNInstance'
_x='h3cNqaUdpServerExtVPNType'
_w='h3cNqaUdpServerExtPort'
_v='h3cNqaUdpServerExtIpAddress'
_u='h3cNqaTcpServerExtVPNInstance'
_t='h3cNqaTcpServerExtVPNType'
_s='h3cNqaTcpServerExtPort'
_r='h3cNqaTcpServerExtIpAddress'
_q='h3cNqaStatReactItemIndex'
_p='h3cNqaStatReactIndex'
_o='h3cNqaStatReactTestName'
_n='h3cNqaStatReactOwnerIndex'
_m='invalid'
_l='h3cNqaStatJitterIndex'
_k='h3cNqaStatResIndex'
_j='seconds'
_i='h3cNqaUdpServerPort'
_h='h3cNqaUdpServerIpAddress'
_g='h3cNqaTcpServerPort'
_f='h3cNqaTcpServerIpAddress'
_e='read-write'
_d='disable'
_c='enable'
_b='InetAddressType'
_a='InetAddress'
_Z='accessible-for-notify'
_Y='minutes'
_X='Counter32'
_W='OctetString'
_V='SnmpAdminString'
_U='pingCtlTestName'
_T='pingCtlOwnerIndex'
_S='DisplayString'
_R='h3cNqaReactThresholdType'
_Q='h3cNqaReactCurrentStatus'
_P='pingCtlType'
_O='pingCtlTargetAddressType'
_N='pingCtlTargetAddress'
_M='pingCtlDescr'
_L='h3cNqaReactItemIndex'
_K='h3cNqaReactTestName'
_J='h3cNqaReactOwnerIndex'
_I='Unsigned32'
_H='not-accessible'
_G='Integer32'
_F='read-create'
_E='DISMAN-PING-MIB'
_D='milliseconds'
_C='H3C-NQA-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_W,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pingCtlDescr,pingCtlEntry,pingCtlOwnerIndex,pingCtlTargetAddress,pingCtlTargetAddressType,pingCtlTestName,pingCtlType=mibBuilder.importSymbols(_E,_M,'pingCtlEntry',_T,_N,_O,_U,_P)
h3cRhw,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cRhw')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_a,_b)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_V)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_X,'Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_S,'PhysAddress','RowStatus','TextualConvention')
h3cNqa=ModuleIdentity((1,3,6,1,4,1,2011,10,8,3))
if mibBuilder.loadTexts:h3cNqa.setRevisions(('2017-07-03 00:00',))
class VpnInstanceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('public',1),('vpn',2)))
_H3cNqaObjects_ObjectIdentity=ObjectIdentity
h3cNqaObjects=_H3cNqaObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,8,3,1))
_H3cNqaMIBVersion_Type=DisplayString
_H3cNqaMIBVersion_Object=MibScalar
h3cNqaMIBVersion=_H3cNqaMIBVersion_Object((1,3,6,1,4,1,2011,10,8,3,1,1),_H3cNqaMIBVersion_Type())
h3cNqaMIBVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaMIBVersion.setStatus(_A)
_H3cNqaCtlTable_Object=MibTable
h3cNqaCtlTable=_H3cNqaCtlTable_Object((1,3,6,1,4,1,2011,10,8,3,1,2))
if mibBuilder.loadTexts:h3cNqaCtlTable.setStatus(_A)
_H3cNqaCtlEntry_Object=MibTableRow
h3cNqaCtlEntry=_H3cNqaCtlEntry_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1))
if mibBuilder.loadTexts:h3cNqaCtlEntry.setStatus(_A)
class _H3cNqaCtlTargetPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_H3cNqaCtlTargetPort_Type.__name__=_G
_H3cNqaCtlTargetPort_Object=MibTableColumn
h3cNqaCtlTargetPort=_H3cNqaCtlTargetPort_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,1),_H3cNqaCtlTargetPort_Type())
h3cNqaCtlTargetPort.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlTargetPort.setStatus(_A)
class _H3cNqaCtlSourcePort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_H3cNqaCtlSourcePort_Type.__name__=_G
_H3cNqaCtlSourcePort_Object=MibTableColumn
h3cNqaCtlSourcePort=_H3cNqaCtlSourcePort_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,2),_H3cNqaCtlSourcePort_Type())
h3cNqaCtlSourcePort.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlSourcePort.setStatus(_A)
class _H3cNqaCtlTTL_Type(Integer32):defaultValue=20
_H3cNqaCtlTTL_Type.__name__=_G
_H3cNqaCtlTTL_Object=MibTableColumn
h3cNqaCtlTTL=_H3cNqaCtlTTL_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,3),_H3cNqaCtlTTL_Type())
h3cNqaCtlTTL.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlTTL.setStatus(_A)
class _H3cNqaCtlJitterAdminInterval_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_H3cNqaCtlJitterAdminInterval_Type.__name__=_G
_H3cNqaCtlJitterAdminInterval_Object=MibTableColumn
h3cNqaCtlJitterAdminInterval=_H3cNqaCtlJitterAdminInterval_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,4),_H3cNqaCtlJitterAdminInterval_Type())
h3cNqaCtlJitterAdminInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlJitterAdminInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaCtlJitterAdminInterval.setUnits(_D)
class _H3cNqaCtlJitterAdminNumPackets_Type(Integer32):defaultValue=10
_H3cNqaCtlJitterAdminNumPackets_Type.__name__=_G
_H3cNqaCtlJitterAdminNumPackets_Object=MibTableColumn
h3cNqaCtlJitterAdminNumPackets=_H3cNqaCtlJitterAdminNumPackets_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,5),_H3cNqaCtlJitterAdminNumPackets_Type())
h3cNqaCtlJitterAdminNumPackets.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlJitterAdminNumPackets.setStatus(_A)
class _H3cNqaCtlHttpOperationType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('get',1),('post',2),('raw',3)))
_H3cNqaCtlHttpOperationType_Type.__name__=_G
_H3cNqaCtlHttpOperationType_Object=MibTableColumn
h3cNqaCtlHttpOperationType=_H3cNqaCtlHttpOperationType_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,6),_H3cNqaCtlHttpOperationType_Type())
h3cNqaCtlHttpOperationType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlHttpOperationType.setStatus(_A)
class _H3cNqaCtlHttpOperationString_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
_H3cNqaCtlHttpOperationString_Type.__name__=_S
_H3cNqaCtlHttpOperationString_Object=MibTableColumn
h3cNqaCtlHttpOperationString=_H3cNqaCtlHttpOperationString_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,7),_H3cNqaCtlHttpOperationString_Type())
h3cNqaCtlHttpOperationString.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlHttpOperationString.setStatus(_A)
class _H3cNqaCtlFtpOperationType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('get',1),('put',2)))
_H3cNqaCtlFtpOperationType_Type.__name__=_G
_H3cNqaCtlFtpOperationType_Object=MibTableColumn
h3cNqaCtlFtpOperationType=_H3cNqaCtlFtpOperationType_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,8),_H3cNqaCtlFtpOperationType_Type())
h3cNqaCtlFtpOperationType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlFtpOperationType.setStatus(_A)
class _H3cNqaCtlFtpUsername_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cNqaCtlFtpUsername_Type.__name__=_S
_H3cNqaCtlFtpUsername_Object=MibTableColumn
h3cNqaCtlFtpUsername=_H3cNqaCtlFtpUsername_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,9),_H3cNqaCtlFtpUsername_Type())
h3cNqaCtlFtpUsername.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlFtpUsername.setStatus(_A)
class _H3cNqaCtlFtpPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cNqaCtlFtpPassword_Type.__name__=_S
_H3cNqaCtlFtpPassword_Object=MibTableColumn
h3cNqaCtlFtpPassword=_H3cNqaCtlFtpPassword_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,10),_H3cNqaCtlFtpPassword_Type())
h3cNqaCtlFtpPassword.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlFtpPassword.setStatus(_A)
class _H3cNqaCtlFtpOperationString_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cNqaCtlFtpOperationString_Type.__name__=_S
_H3cNqaCtlFtpOperationString_Object=MibTableColumn
h3cNqaCtlFtpOperationString=_H3cNqaCtlFtpOperationString_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,11),_H3cNqaCtlFtpOperationString_Type())
h3cNqaCtlFtpOperationString.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlFtpOperationString.setStatus(_A)
class _H3cNqaCtlVPNInstance_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cNqaCtlVPNInstance_Type.__name__=_S
_H3cNqaCtlVPNInstance_Object=MibTableColumn
h3cNqaCtlVPNInstance=_H3cNqaCtlVPNInstance_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,12),_H3cNqaCtlVPNInstance_Type())
h3cNqaCtlVPNInstance.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlVPNInstance.setStatus(_A)
class _H3cNqaCtlHistoryKeptTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_H3cNqaCtlHistoryKeptTime_Type.__name__=_G
_H3cNqaCtlHistoryKeptTime_Object=MibTableColumn
h3cNqaCtlHistoryKeptTime=_H3cNqaCtlHistoryKeptTime_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,13),_H3cNqaCtlHistoryKeptTime_Type())
h3cNqaCtlHistoryKeptTime.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlHistoryKeptTime.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaCtlHistoryKeptTime.setUnits(_Y)
class _H3cNqaCtlHistoryEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_H3cNqaCtlHistoryEnable_Type.__name__=_G
_H3cNqaCtlHistoryEnable_Object=MibTableColumn
h3cNqaCtlHistoryEnable=_H3cNqaCtlHistoryEnable_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,14),_H3cNqaCtlHistoryEnable_Type())
h3cNqaCtlHistoryEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlHistoryEnable.setStatus(_A)
class _H3cNqaCtlICPIFAdvFactor_Type(Integer32):defaultValue=0
_H3cNqaCtlICPIFAdvFactor_Type.__name__=_G
_H3cNqaCtlICPIFAdvFactor_Object=MibTableColumn
h3cNqaCtlICPIFAdvFactor=_H3cNqaCtlICPIFAdvFactor_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,15),_H3cNqaCtlICPIFAdvFactor_Type())
h3cNqaCtlICPIFAdvFactor.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlICPIFAdvFactor.setStatus(_A)
class _H3cNqaCtlCodecType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notDefined',1),('g711Alaw',2),('g711Ulaw',3),('g729A',4),('icmpTimestamp',5)))
_H3cNqaCtlCodecType_Type.__name__=_G
_H3cNqaCtlCodecType_Object=MibTableColumn
h3cNqaCtlCodecType=_H3cNqaCtlCodecType_Object((1,3,6,1,4,1,2011,10,8,3,1,2,1,16),_H3cNqaCtlCodecType_Type())
h3cNqaCtlCodecType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlCodecType.setStatus(_A)
_H3cNqaResultsTable_Object=MibTable
h3cNqaResultsTable=_H3cNqaResultsTable_Object((1,3,6,1,4,1,2011,10,8,3,1,3))
if mibBuilder.loadTexts:h3cNqaResultsTable.setStatus(_A)
_H3cNqaResultsEntry_Object=MibTableRow
h3cNqaResultsEntry=_H3cNqaResultsEntry_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1))
h3cNqaResultsEntry.setIndexNames((0,_E,_T),(0,_E,_U))
if mibBuilder.loadTexts:h3cNqaResultsEntry.setStatus(_A)
_H3cNqaResultsRttNumDisconnects_Type=Unsigned32
_H3cNqaResultsRttNumDisconnects_Object=MibTableColumn
h3cNqaResultsRttNumDisconnects=_H3cNqaResultsRttNumDisconnects_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,1),_H3cNqaResultsRttNumDisconnects_Type())
h3cNqaResultsRttNumDisconnects.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsRttNumDisconnects.setStatus(_A)
_H3cNqaResultsRttTimeouts_Type=Unsigned32
_H3cNqaResultsRttTimeouts_Object=MibTableColumn
h3cNqaResultsRttTimeouts=_H3cNqaResultsRttTimeouts_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,2),_H3cNqaResultsRttTimeouts_Type())
h3cNqaResultsRttTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsRttTimeouts.setStatus(_A)
_H3cNqaResultsRttBusies_Type=Unsigned32
_H3cNqaResultsRttBusies_Object=MibTableColumn
h3cNqaResultsRttBusies=_H3cNqaResultsRttBusies_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,3),_H3cNqaResultsRttBusies_Type())
h3cNqaResultsRttBusies.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsRttBusies.setStatus(_A)
_H3cNqaResultsRttNoConnections_Type=Unsigned32
_H3cNqaResultsRttNoConnections_Object=MibTableColumn
h3cNqaResultsRttNoConnections=_H3cNqaResultsRttNoConnections_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,4),_H3cNqaResultsRttNoConnections_Type())
h3cNqaResultsRttNoConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsRttNoConnections.setStatus(_A)
_H3cNqaResultsRttDrops_Type=Unsigned32
_H3cNqaResultsRttDrops_Object=MibTableColumn
h3cNqaResultsRttDrops=_H3cNqaResultsRttDrops_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,5),_H3cNqaResultsRttDrops_Type())
h3cNqaResultsRttDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsRttDrops.setStatus(_A)
_H3cNqaResultsRttSequenceErrors_Type=Unsigned32
_H3cNqaResultsRttSequenceErrors_Object=MibTableColumn
h3cNqaResultsRttSequenceErrors=_H3cNqaResultsRttSequenceErrors_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,6),_H3cNqaResultsRttSequenceErrors_Type())
h3cNqaResultsRttSequenceErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsRttSequenceErrors.setStatus(_A)
_H3cNqaResultsRttStatsErrors_Type=Unsigned32
_H3cNqaResultsRttStatsErrors_Object=MibTableColumn
h3cNqaResultsRttStatsErrors=_H3cNqaResultsRttStatsErrors_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,7),_H3cNqaResultsRttStatsErrors_Type())
h3cNqaResultsRttStatsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsRttStatsErrors.setStatus(_A)
_H3cNqaResultsMaxDelaySD_Type=Unsigned32
_H3cNqaResultsMaxDelaySD_Object=MibTableColumn
h3cNqaResultsMaxDelaySD=_H3cNqaResultsMaxDelaySD_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,8),_H3cNqaResultsMaxDelaySD_Type())
h3cNqaResultsMaxDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsMaxDelaySD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaResultsMaxDelaySD.setUnits(_D)
_H3cNqaResultsMaxDelayDS_Type=Unsigned32
_H3cNqaResultsMaxDelayDS_Object=MibTableColumn
h3cNqaResultsMaxDelayDS=_H3cNqaResultsMaxDelayDS_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,9),_H3cNqaResultsMaxDelayDS_Type())
h3cNqaResultsMaxDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsMaxDelayDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaResultsMaxDelayDS.setUnits(_D)
_H3cNqaResultsLostPacketRatio_Type=Unsigned32
_H3cNqaResultsLostPacketRatio_Object=MibTableColumn
h3cNqaResultsLostPacketRatio=_H3cNqaResultsLostPacketRatio_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,10),_H3cNqaResultsLostPacketRatio_Type())
h3cNqaResultsLostPacketRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsLostPacketRatio.setStatus(_A)
_H3cNqaResultsPacketLateArrival_Type=Unsigned32
_H3cNqaResultsPacketLateArrival_Object=MibTableColumn
h3cNqaResultsPacketLateArrival=_H3cNqaResultsPacketLateArrival_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,11),_H3cNqaResultsPacketLateArrival_Type())
h3cNqaResultsPacketLateArrival.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsPacketLateArrival.setStatus(_A)
_H3cNqaResultsRttSum_Type=Unsigned32
_H3cNqaResultsRttSum_Object=MibTableColumn
h3cNqaResultsRttSum=_H3cNqaResultsRttSum_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,12),_H3cNqaResultsRttSum_Type())
h3cNqaResultsRttSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsRttSum.setStatus(_A)
_H3cNqaResultsNumOfDelaySD_Type=Unsigned32
_H3cNqaResultsNumOfDelaySD_Object=MibTableColumn
h3cNqaResultsNumOfDelaySD=_H3cNqaResultsNumOfDelaySD_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,13),_H3cNqaResultsNumOfDelaySD_Type())
h3cNqaResultsNumOfDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsNumOfDelaySD.setStatus(_A)
_H3cNqaResultsMinDelaySD_Type=Unsigned32
_H3cNqaResultsMinDelaySD_Object=MibTableColumn
h3cNqaResultsMinDelaySD=_H3cNqaResultsMinDelaySD_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,14),_H3cNqaResultsMinDelaySD_Type())
h3cNqaResultsMinDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsMinDelaySD.setStatus(_A)
_H3cNqaResultsSumDelaySD_Type=Unsigned32
_H3cNqaResultsSumDelaySD_Object=MibTableColumn
h3cNqaResultsSumDelaySD=_H3cNqaResultsSumDelaySD_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,15),_H3cNqaResultsSumDelaySD_Type())
h3cNqaResultsSumDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsSumDelaySD.setStatus(_A)
_H3cNqaResultsSum2DelaySD_Type=Unsigned32
_H3cNqaResultsSum2DelaySD_Object=MibTableColumn
h3cNqaResultsSum2DelaySD=_H3cNqaResultsSum2DelaySD_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,16),_H3cNqaResultsSum2DelaySD_Type())
h3cNqaResultsSum2DelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsSum2DelaySD.setStatus(_A)
_H3cNqaResultsNumOfDelayDS_Type=Unsigned32
_H3cNqaResultsNumOfDelayDS_Object=MibTableColumn
h3cNqaResultsNumOfDelayDS=_H3cNqaResultsNumOfDelayDS_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,17),_H3cNqaResultsNumOfDelayDS_Type())
h3cNqaResultsNumOfDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsNumOfDelayDS.setStatus(_A)
_H3cNqaResultsMinDelayDS_Type=Unsigned32
_H3cNqaResultsMinDelayDS_Object=MibTableColumn
h3cNqaResultsMinDelayDS=_H3cNqaResultsMinDelayDS_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,18),_H3cNqaResultsMinDelayDS_Type())
h3cNqaResultsMinDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsMinDelayDS.setStatus(_A)
_H3cNqaResultsSumDelayDS_Type=Unsigned32
_H3cNqaResultsSumDelayDS_Object=MibTableColumn
h3cNqaResultsSumDelayDS=_H3cNqaResultsSumDelayDS_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,19),_H3cNqaResultsSumDelayDS_Type())
h3cNqaResultsSumDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsSumDelayDS.setStatus(_A)
_H3cNqaResultsSum2DelayDS_Type=Unsigned32
_H3cNqaResultsSum2DelayDS_Object=MibTableColumn
h3cNqaResultsSum2DelayDS=_H3cNqaResultsSum2DelayDS_Object((1,3,6,1,4,1,2011,10,8,3,1,3,1,20),_H3cNqaResultsSum2DelayDS_Type())
h3cNqaResultsSum2DelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaResultsSum2DelayDS.setStatus(_A)
_H3cNqaJitterStatsTable_Object=MibTable
h3cNqaJitterStatsTable=_H3cNqaJitterStatsTable_Object((1,3,6,1,4,1,2011,10,8,3,1,4))
if mibBuilder.loadTexts:h3cNqaJitterStatsTable.setStatus(_A)
_H3cNqaJitterStatsEntry_Object=MibTableRow
h3cNqaJitterStatsEntry=_H3cNqaJitterStatsEntry_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1))
h3cNqaJitterStatsEntry.setIndexNames((0,_E,_T),(0,_E,_U))
if mibBuilder.loadTexts:h3cNqaJitterStatsEntry.setStatus(_A)
_H3cNqaJitterStatsNumOfRTT_Type=Counter32
_H3cNqaJitterStatsNumOfRTT_Object=MibTableColumn
h3cNqaJitterStatsNumOfRTT=_H3cNqaJitterStatsNumOfRTT_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,1),_H3cNqaJitterStatsNumOfRTT_Type())
h3cNqaJitterStatsNumOfRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsNumOfRTT.setStatus(_A)
_H3cNqaJitterStatsMinOfPositivesSD_Type=Gauge32
_H3cNqaJitterStatsMinOfPositivesSD_Object=MibTableColumn
h3cNqaJitterStatsMinOfPositivesSD=_H3cNqaJitterStatsMinOfPositivesSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,2),_H3cNqaJitterStatsMinOfPositivesSD_Type())
h3cNqaJitterStatsMinOfPositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsMinOfPositivesSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsMinOfPositivesSD.setUnits(_D)
_H3cNqaJitterStatsMaxOfPositivesSD_Type=Gauge32
_H3cNqaJitterStatsMaxOfPositivesSD_Object=MibTableColumn
h3cNqaJitterStatsMaxOfPositivesSD=_H3cNqaJitterStatsMaxOfPositivesSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,3),_H3cNqaJitterStatsMaxOfPositivesSD_Type())
h3cNqaJitterStatsMaxOfPositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsMaxOfPositivesSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsMaxOfPositivesSD.setUnits(_D)
_H3cNqaJitterStatsNumOfPositivesSD_Type=Gauge32
_H3cNqaJitterStatsNumOfPositivesSD_Object=MibTableColumn
h3cNqaJitterStatsNumOfPositivesSD=_H3cNqaJitterStatsNumOfPositivesSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,4),_H3cNqaJitterStatsNumOfPositivesSD_Type())
h3cNqaJitterStatsNumOfPositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsNumOfPositivesSD.setStatus(_A)
_H3cNqaJitterStatsSumOfPositivesSD_Type=Gauge32
_H3cNqaJitterStatsSumOfPositivesSD_Object=MibTableColumn
h3cNqaJitterStatsSumOfPositivesSD=_H3cNqaJitterStatsSumOfPositivesSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,5),_H3cNqaJitterStatsSumOfPositivesSD_Type())
h3cNqaJitterStatsSumOfPositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsSumOfPositivesSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsSumOfPositivesSD.setUnits(_D)
_H3cNqaJitterStatsSum2PositivesSD_Type=Gauge32
_H3cNqaJitterStatsSum2PositivesSD_Object=MibTableColumn
h3cNqaJitterStatsSum2PositivesSD=_H3cNqaJitterStatsSum2PositivesSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,6),_H3cNqaJitterStatsSum2PositivesSD_Type())
h3cNqaJitterStatsSum2PositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsSum2PositivesSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsSum2PositivesSD.setUnits(_D)
_H3cNqaJitterStatsMinOfNegativesSD_Type=Gauge32
_H3cNqaJitterStatsMinOfNegativesSD_Object=MibTableColumn
h3cNqaJitterStatsMinOfNegativesSD=_H3cNqaJitterStatsMinOfNegativesSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,7),_H3cNqaJitterStatsMinOfNegativesSD_Type())
h3cNqaJitterStatsMinOfNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsMinOfNegativesSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsMinOfNegativesSD.setUnits(_D)
_H3cNqaJitterStatsMaxOfNegativesSD_Type=Gauge32
_H3cNqaJitterStatsMaxOfNegativesSD_Object=MibTableColumn
h3cNqaJitterStatsMaxOfNegativesSD=_H3cNqaJitterStatsMaxOfNegativesSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,8),_H3cNqaJitterStatsMaxOfNegativesSD_Type())
h3cNqaJitterStatsMaxOfNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsMaxOfNegativesSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsMaxOfNegativesSD.setUnits(_D)
_H3cNqaJitterStatsNumOfNegativesSD_Type=Gauge32
_H3cNqaJitterStatsNumOfNegativesSD_Object=MibTableColumn
h3cNqaJitterStatsNumOfNegativesSD=_H3cNqaJitterStatsNumOfNegativesSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,9),_H3cNqaJitterStatsNumOfNegativesSD_Type())
h3cNqaJitterStatsNumOfNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsNumOfNegativesSD.setStatus(_A)
_H3cNqaJitterStatsSumOfNegativesSD_Type=Gauge32
_H3cNqaJitterStatsSumOfNegativesSD_Object=MibTableColumn
h3cNqaJitterStatsSumOfNegativesSD=_H3cNqaJitterStatsSumOfNegativesSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,10),_H3cNqaJitterStatsSumOfNegativesSD_Type())
h3cNqaJitterStatsSumOfNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsSumOfNegativesSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsSumOfNegativesSD.setUnits(_D)
_H3cNqaJitterStatsSum2NegativesSD_Type=Gauge32
_H3cNqaJitterStatsSum2NegativesSD_Object=MibTableColumn
h3cNqaJitterStatsSum2NegativesSD=_H3cNqaJitterStatsSum2NegativesSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,11),_H3cNqaJitterStatsSum2NegativesSD_Type())
h3cNqaJitterStatsSum2NegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsSum2NegativesSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsSum2NegativesSD.setUnits(_D)
_H3cNqaJitterStatsMinOfPositivesDS_Type=Gauge32
_H3cNqaJitterStatsMinOfPositivesDS_Object=MibTableColumn
h3cNqaJitterStatsMinOfPositivesDS=_H3cNqaJitterStatsMinOfPositivesDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,12),_H3cNqaJitterStatsMinOfPositivesDS_Type())
h3cNqaJitterStatsMinOfPositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsMinOfPositivesDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsMinOfPositivesDS.setUnits(_D)
_H3cNqaJitterStatsMaxOfPositivesDS_Type=Gauge32
_H3cNqaJitterStatsMaxOfPositivesDS_Object=MibTableColumn
h3cNqaJitterStatsMaxOfPositivesDS=_H3cNqaJitterStatsMaxOfPositivesDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,13),_H3cNqaJitterStatsMaxOfPositivesDS_Type())
h3cNqaJitterStatsMaxOfPositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsMaxOfPositivesDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsMaxOfPositivesDS.setUnits(_D)
_H3cNqaJitterStatsNumOfPositivesDS_Type=Gauge32
_H3cNqaJitterStatsNumOfPositivesDS_Object=MibTableColumn
h3cNqaJitterStatsNumOfPositivesDS=_H3cNqaJitterStatsNumOfPositivesDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,14),_H3cNqaJitterStatsNumOfPositivesDS_Type())
h3cNqaJitterStatsNumOfPositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsNumOfPositivesDS.setStatus(_A)
_H3cNqaJitterStatsSumOfPositivesDS_Type=Gauge32
_H3cNqaJitterStatsSumOfPositivesDS_Object=MibTableColumn
h3cNqaJitterStatsSumOfPositivesDS=_H3cNqaJitterStatsSumOfPositivesDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,15),_H3cNqaJitterStatsSumOfPositivesDS_Type())
h3cNqaJitterStatsSumOfPositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsSumOfPositivesDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsSumOfPositivesDS.setUnits(_D)
_H3cNqaJitterStatsSum2PositivesDS_Type=Gauge32
_H3cNqaJitterStatsSum2PositivesDS_Object=MibTableColumn
h3cNqaJitterStatsSum2PositivesDS=_H3cNqaJitterStatsSum2PositivesDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,16),_H3cNqaJitterStatsSum2PositivesDS_Type())
h3cNqaJitterStatsSum2PositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsSum2PositivesDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsSum2PositivesDS.setUnits(_D)
_H3cNqaJitterStatsMinOfNegativesDS_Type=Gauge32
_H3cNqaJitterStatsMinOfNegativesDS_Object=MibTableColumn
h3cNqaJitterStatsMinOfNegativesDS=_H3cNqaJitterStatsMinOfNegativesDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,17),_H3cNqaJitterStatsMinOfNegativesDS_Type())
h3cNqaJitterStatsMinOfNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsMinOfNegativesDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsMinOfNegativesDS.setUnits(_D)
_H3cNqaJitterStatsMaxOfNegativesDS_Type=Gauge32
_H3cNqaJitterStatsMaxOfNegativesDS_Object=MibTableColumn
h3cNqaJitterStatsMaxOfNegativesDS=_H3cNqaJitterStatsMaxOfNegativesDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,18),_H3cNqaJitterStatsMaxOfNegativesDS_Type())
h3cNqaJitterStatsMaxOfNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsMaxOfNegativesDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsMaxOfNegativesDS.setUnits(_D)
_H3cNqaJitterStatsNumOfNegativesDS_Type=Gauge32
_H3cNqaJitterStatsNumOfNegativesDS_Object=MibTableColumn
h3cNqaJitterStatsNumOfNegativesDS=_H3cNqaJitterStatsNumOfNegativesDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,19),_H3cNqaJitterStatsNumOfNegativesDS_Type())
h3cNqaJitterStatsNumOfNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsNumOfNegativesDS.setStatus(_A)
_H3cNqaJitterStatsSumOfNegativesDS_Type=Gauge32
_H3cNqaJitterStatsSumOfNegativesDS_Object=MibTableColumn
h3cNqaJitterStatsSumOfNegativesDS=_H3cNqaJitterStatsSumOfNegativesDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,20),_H3cNqaJitterStatsSumOfNegativesDS_Type())
h3cNqaJitterStatsSumOfNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsSumOfNegativesDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsSumOfNegativesDS.setUnits(_D)
_H3cNqaJitterStatsSum2NegativesDS_Type=Gauge32
_H3cNqaJitterStatsSum2NegativesDS_Object=MibTableColumn
h3cNqaJitterStatsSum2NegativesDS=_H3cNqaJitterStatsSum2NegativesDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,21),_H3cNqaJitterStatsSum2NegativesDS_Type())
h3cNqaJitterStatsSum2NegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsSum2NegativesDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsSum2NegativesDS.setUnits(_D)
_H3cNqaJitterStatsPacketLossSD_Type=Gauge32
_H3cNqaJitterStatsPacketLossSD_Object=MibTableColumn
h3cNqaJitterStatsPacketLossSD=_H3cNqaJitterStatsPacketLossSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,22),_H3cNqaJitterStatsPacketLossSD_Type())
h3cNqaJitterStatsPacketLossSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsPacketLossSD.setStatus(_A)
_H3cNqaJitterStatsPacketLossDS_Type=Gauge32
_H3cNqaJitterStatsPacketLossDS_Object=MibTableColumn
h3cNqaJitterStatsPacketLossDS=_H3cNqaJitterStatsPacketLossDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,23),_H3cNqaJitterStatsPacketLossDS_Type())
h3cNqaJitterStatsPacketLossDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsPacketLossDS.setStatus(_A)
_H3cNqaJitterStatsAvePositivesSD_Type=Gauge32
_H3cNqaJitterStatsAvePositivesSD_Object=MibTableColumn
h3cNqaJitterStatsAvePositivesSD=_H3cNqaJitterStatsAvePositivesSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,24),_H3cNqaJitterStatsAvePositivesSD_Type())
h3cNqaJitterStatsAvePositivesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsAvePositivesSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsAvePositivesSD.setUnits(_D)
_H3cNqaJitterStatsAveNegativesSD_Type=Gauge32
_H3cNqaJitterStatsAveNegativesSD_Object=MibTableColumn
h3cNqaJitterStatsAveNegativesSD=_H3cNqaJitterStatsAveNegativesSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,25),_H3cNqaJitterStatsAveNegativesSD_Type())
h3cNqaJitterStatsAveNegativesSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsAveNegativesSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsAveNegativesSD.setUnits(_D)
_H3cNqaJitterStatsAvePositivesDS_Type=Gauge32
_H3cNqaJitterStatsAvePositivesDS_Object=MibTableColumn
h3cNqaJitterStatsAvePositivesDS=_H3cNqaJitterStatsAvePositivesDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,26),_H3cNqaJitterStatsAvePositivesDS_Type())
h3cNqaJitterStatsAvePositivesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsAvePositivesDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsAvePositivesDS.setUnits(_D)
_H3cNqaJitterStatsAveNegativesDS_Type=Gauge32
_H3cNqaJitterStatsAveNegativesDS_Object=MibTableColumn
h3cNqaJitterStatsAveNegativesDS=_H3cNqaJitterStatsAveNegativesDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,27),_H3cNqaJitterStatsAveNegativesDS_Type())
h3cNqaJitterStatsAveNegativesDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsAveNegativesDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsAveNegativesDS.setUnits(_D)
_H3cNqaJitterStatsPktLossUnknown_Type=Gauge32
_H3cNqaJitterStatsPktLossUnknown_Object=MibTableColumn
h3cNqaJitterStatsPktLossUnknown=_H3cNqaJitterStatsPktLossUnknown_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,28),_H3cNqaJitterStatsPktLossUnknown_Type())
h3cNqaJitterStatsPktLossUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsPktLossUnknown.setStatus(_A)
_H3cNqaJitterStatsOperOfICPIF_Type=Gauge32
_H3cNqaJitterStatsOperOfICPIF_Object=MibTableColumn
h3cNqaJitterStatsOperOfICPIF=_H3cNqaJitterStatsOperOfICPIF_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,29),_H3cNqaJitterStatsOperOfICPIF_Type())
h3cNqaJitterStatsOperOfICPIF.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsOperOfICPIF.setStatus(_A)
_H3cNqaJitterStatsOperOfMOS_Type=Gauge32
_H3cNqaJitterStatsOperOfMOS_Object=MibTableColumn
h3cNqaJitterStatsOperOfMOS=_H3cNqaJitterStatsOperOfMOS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,30),_H3cNqaJitterStatsOperOfMOS_Type())
h3cNqaJitterStatsOperOfMOS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsOperOfMOS.setStatus(_A)
_H3cNqaJitterStatsAveSD_Type=Gauge32
_H3cNqaJitterStatsAveSD_Object=MibTableColumn
h3cNqaJitterStatsAveSD=_H3cNqaJitterStatsAveSD_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,31),_H3cNqaJitterStatsAveSD_Type())
h3cNqaJitterStatsAveSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsAveSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsAveSD.setUnits(_D)
_H3cNqaJitterStatsAveDS_Type=Gauge32
_H3cNqaJitterStatsAveDS_Object=MibTableColumn
h3cNqaJitterStatsAveDS=_H3cNqaJitterStatsAveDS_Object((1,3,6,1,4,1,2011,10,8,3,1,4,1,32),_H3cNqaJitterStatsAveDS_Type())
h3cNqaJitterStatsAveDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaJitterStatsAveDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaJitterStatsAveDS.setUnits(_D)
class _H3cNqaAgentEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_H3cNqaAgentEnable_Type.__name__=_G
_H3cNqaAgentEnable_Object=MibScalar
h3cNqaAgentEnable=_H3cNqaAgentEnable_Object((1,3,6,1,4,1,2011,10,8,3,1,5),_H3cNqaAgentEnable_Type())
h3cNqaAgentEnable.setMaxAccess(_e)
if mibBuilder.loadTexts:h3cNqaAgentEnable.setStatus(_A)
_H3cNqaTcpServerTable_Object=MibTable
h3cNqaTcpServerTable=_H3cNqaTcpServerTable_Object((1,3,6,1,4,1,2011,10,8,3,1,6))
if mibBuilder.loadTexts:h3cNqaTcpServerTable.setStatus(_A)
_H3cNqaTcpServerEntry_Object=MibTableRow
h3cNqaTcpServerEntry=_H3cNqaTcpServerEntry_Object((1,3,6,1,4,1,2011,10,8,3,1,6,1))
h3cNqaTcpServerEntry.setIndexNames((0,_C,_f),(0,_C,_g))
if mibBuilder.loadTexts:h3cNqaTcpServerEntry.setStatus(_A)
_H3cNqaTcpServerIpAddress_Type=InetAddress
_H3cNqaTcpServerIpAddress_Object=MibTableColumn
h3cNqaTcpServerIpAddress=_H3cNqaTcpServerIpAddress_Object((1,3,6,1,4,1,2011,10,8,3,1,6,1,1),_H3cNqaTcpServerIpAddress_Type())
h3cNqaTcpServerIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaTcpServerIpAddress.setStatus(_A)
class _H3cNqaTcpServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_H3cNqaTcpServerPort_Type.__name__=_G
_H3cNqaTcpServerPort_Object=MibTableColumn
h3cNqaTcpServerPort=_H3cNqaTcpServerPort_Object((1,3,6,1,4,1,2011,10,8,3,1,6,1,2),_H3cNqaTcpServerPort_Type())
h3cNqaTcpServerPort.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaTcpServerPort.setStatus(_A)
_H3cNqaTcpServerRowStatus_Type=RowStatus
_H3cNqaTcpServerRowStatus_Object=MibTableColumn
h3cNqaTcpServerRowStatus=_H3cNqaTcpServerRowStatus_Object((1,3,6,1,4,1,2011,10,8,3,1,6,1,3),_H3cNqaTcpServerRowStatus_Type())
h3cNqaTcpServerRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaTcpServerRowStatus.setStatus(_A)
_H3cNqaUdpServerTable_Object=MibTable
h3cNqaUdpServerTable=_H3cNqaUdpServerTable_Object((1,3,6,1,4,1,2011,10,8,3,1,7))
if mibBuilder.loadTexts:h3cNqaUdpServerTable.setStatus(_A)
_H3cNqaUdpServerEntry_Object=MibTableRow
h3cNqaUdpServerEntry=_H3cNqaUdpServerEntry_Object((1,3,6,1,4,1,2011,10,8,3,1,7,1))
h3cNqaUdpServerEntry.setIndexNames((0,_C,_h),(0,_C,_i))
if mibBuilder.loadTexts:h3cNqaUdpServerEntry.setStatus(_A)
_H3cNqaUdpServerIpAddress_Type=InetAddress
_H3cNqaUdpServerIpAddress_Object=MibTableColumn
h3cNqaUdpServerIpAddress=_H3cNqaUdpServerIpAddress_Object((1,3,6,1,4,1,2011,10,8,3,1,7,1,1),_H3cNqaUdpServerIpAddress_Type())
h3cNqaUdpServerIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaUdpServerIpAddress.setStatus(_A)
class _H3cNqaUdpServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_H3cNqaUdpServerPort_Type.__name__=_G
_H3cNqaUdpServerPort_Object=MibTableColumn
h3cNqaUdpServerPort=_H3cNqaUdpServerPort_Object((1,3,6,1,4,1,2011,10,8,3,1,7,1,2),_H3cNqaUdpServerPort_Type())
h3cNqaUdpServerPort.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaUdpServerPort.setStatus(_A)
_H3cNqaUdpServerRowStatus_Type=RowStatus
_H3cNqaUdpServerRowStatus_Object=MibTableColumn
h3cNqaUdpServerRowStatus=_H3cNqaUdpServerRowStatus_Object((1,3,6,1,4,1,2011,10,8,3,1,7,1,3),_H3cNqaUdpServerRowStatus_Type())
h3cNqaUdpServerRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaUdpServerRowStatus.setStatus(_A)
class _H3cNqaServerEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_H3cNqaServerEnable_Type.__name__=_G
_H3cNqaServerEnable_Object=MibScalar
h3cNqaServerEnable=_H3cNqaServerEnable_Object((1,3,6,1,4,1,2011,10,8,3,1,8),_H3cNqaServerEnable_Type())
h3cNqaServerEnable.setMaxAccess(_e)
if mibBuilder.loadTexts:h3cNqaServerEnable.setStatus(_A)
_H3cNqaStatsMaxGroupNumber_Type=Integer32
_H3cNqaStatsMaxGroupNumber_Object=MibScalar
h3cNqaStatsMaxGroupNumber=_H3cNqaStatsMaxGroupNumber_Object((1,3,6,1,4,1,2011,10,8,3,1,9),_H3cNqaStatsMaxGroupNumber_Type())
h3cNqaStatsMaxGroupNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatsMaxGroupNumber.setStatus(_A)
_H3cNqaStatisticsCtlTable_Object=MibTable
h3cNqaStatisticsCtlTable=_H3cNqaStatisticsCtlTable_Object((1,3,6,1,4,1,2011,10,8,3,1,10))
if mibBuilder.loadTexts:h3cNqaStatisticsCtlTable.setStatus(_A)
_H3cNqaStatisticsCtlEntry_Object=MibTableRow
h3cNqaStatisticsCtlEntry=_H3cNqaStatisticsCtlEntry_Object((1,3,6,1,4,1,2011,10,8,3,1,10,1))
if mibBuilder.loadTexts:h3cNqaStatisticsCtlEntry.setStatus(_A)
_H3cNqaCtlStatisticsInterval_Type=Unsigned32
_H3cNqaCtlStatisticsInterval_Object=MibTableColumn
h3cNqaCtlStatisticsInterval=_H3cNqaCtlStatisticsInterval_Object((1,3,6,1,4,1,2011,10,8,3,1,10,1,1),_H3cNqaCtlStatisticsInterval_Type())
h3cNqaCtlStatisticsInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlStatisticsInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaCtlStatisticsInterval.setUnits(_Y)
class _H3cNqaCtlStatisticsGroupNumber_Type(Unsigned32):defaultValue=2
_H3cNqaCtlStatisticsGroupNumber_Type.__name__=_I
_H3cNqaCtlStatisticsGroupNumber_Object=MibTableColumn
h3cNqaCtlStatisticsGroupNumber=_H3cNqaCtlStatisticsGroupNumber_Object((1,3,6,1,4,1,2011,10,8,3,1,10,1,2),_H3cNqaCtlStatisticsGroupNumber_Type())
h3cNqaCtlStatisticsGroupNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlStatisticsGroupNumber.setStatus(_A)
class _H3cNqaCtlStatisticsKeptTime_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_H3cNqaCtlStatisticsKeptTime_Type.__name__=_I
_H3cNqaCtlStatisticsKeptTime_Object=MibTableColumn
h3cNqaCtlStatisticsKeptTime=_H3cNqaCtlStatisticsKeptTime_Object((1,3,6,1,4,1,2011,10,8,3,1,10,1,3),_H3cNqaCtlStatisticsKeptTime_Type())
h3cNqaCtlStatisticsKeptTime.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlStatisticsKeptTime.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaCtlStatisticsKeptTime.setUnits(_Y)
_H3cNqaCtlBeginTime_Type=DateAndTime
_H3cNqaCtlBeginTime_Object=MibTableColumn
h3cNqaCtlBeginTime=_H3cNqaCtlBeginTime_Object((1,3,6,1,4,1,2011,10,8,3,1,10,1,4),_H3cNqaCtlBeginTime_Type())
h3cNqaCtlBeginTime.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlBeginTime.setStatus(_A)
class _H3cNqaCtlLifeTime_Type(Unsigned32):defaultValue=0
_H3cNqaCtlLifeTime_Type.__name__=_I
_H3cNqaCtlLifeTime_Object=MibTableColumn
h3cNqaCtlLifeTime=_H3cNqaCtlLifeTime_Object((1,3,6,1,4,1,2011,10,8,3,1,10,1,5),_H3cNqaCtlLifeTime_Type())
h3cNqaCtlLifeTime.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaCtlLifeTime.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaCtlLifeTime.setUnits(_j)
_H3cNqaStatisticsResultsTable_Object=MibTable
h3cNqaStatisticsResultsTable=_H3cNqaStatisticsResultsTable_Object((1,3,6,1,4,1,2011,10,8,3,1,11))
if mibBuilder.loadTexts:h3cNqaStatisticsResultsTable.setStatus(_A)
_H3cNqaStatisticsResultsEntry_Object=MibTableRow
h3cNqaStatisticsResultsEntry=_H3cNqaStatisticsResultsEntry_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1))
h3cNqaStatisticsResultsEntry.setIndexNames((0,_E,_T),(0,_E,_U),(0,_C,_k))
if mibBuilder.loadTexts:h3cNqaStatisticsResultsEntry.setStatus(_A)
class _H3cNqaStatResIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cNqaStatResIndex_Type.__name__=_I
_H3cNqaStatResIndex_Object=MibTableColumn
h3cNqaStatResIndex=_H3cNqaStatResIndex_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,1),_H3cNqaStatResIndex_Type())
h3cNqaStatResIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaStatResIndex.setStatus(_A)
class _H3cNqaStatResIpTargetAddressType_Type(InetAddressType):defaultValue=0
_H3cNqaStatResIpTargetAddressType_Type.__name__=_b
_H3cNqaStatResIpTargetAddressType_Object=MibTableColumn
h3cNqaStatResIpTargetAddressType=_H3cNqaStatResIpTargetAddressType_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,2),_H3cNqaStatResIpTargetAddressType_Type())
h3cNqaStatResIpTargetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResIpTargetAddressType.setStatus(_A)
class _H3cNqaStatResIpTargetAddress_Type(InetAddress):defaultHexValue=''
_H3cNqaStatResIpTargetAddress_Type.__name__=_a
_H3cNqaStatResIpTargetAddress_Object=MibTableColumn
h3cNqaStatResIpTargetAddress=_H3cNqaStatResIpTargetAddress_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,3),_H3cNqaStatResIpTargetAddress_Type())
h3cNqaStatResIpTargetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResIpTargetAddress.setStatus(_A)
_H3cNqaStatResMinRtt_Type=Gauge32
_H3cNqaStatResMinRtt_Object=MibTableColumn
h3cNqaStatResMinRtt=_H3cNqaStatResMinRtt_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,4),_H3cNqaStatResMinRtt_Type())
h3cNqaStatResMinRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResMinRtt.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatResMinRtt.setUnits(_D)
_H3cNqaStatResMaxRtt_Type=Gauge32
_H3cNqaStatResMaxRtt_Object=MibTableColumn
h3cNqaStatResMaxRtt=_H3cNqaStatResMaxRtt_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,5),_H3cNqaStatResMaxRtt_Type())
h3cNqaStatResMaxRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResMaxRtt.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatResMaxRtt.setUnits(_D)
_H3cNqaStatResAverageRtt_Type=Gauge32
_H3cNqaStatResAverageRtt_Object=MibTableColumn
h3cNqaStatResAverageRtt=_H3cNqaStatResAverageRtt_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,6),_H3cNqaStatResAverageRtt_Type())
h3cNqaStatResAverageRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResAverageRtt.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatResAverageRtt.setUnits(_D)
_H3cNqaStatResProbeResponses_Type=Counter32
_H3cNqaStatResProbeResponses_Object=MibTableColumn
h3cNqaStatResProbeResponses=_H3cNqaStatResProbeResponses_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,7),_H3cNqaStatResProbeResponses_Type())
h3cNqaStatResProbeResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResProbeResponses.setStatus(_A)
_H3cNqaStatResSentProbes_Type=Counter32
_H3cNqaStatResSentProbes_Object=MibTableColumn
h3cNqaStatResSentProbes=_H3cNqaStatResSentProbes_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,8),_H3cNqaStatResSentProbes_Type())
h3cNqaStatResSentProbes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResSentProbes.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatResSentProbes.setUnits('probes')
_H3cNqaStatResRttSumOfSquares_Type=Counter32
_H3cNqaStatResRttSumOfSquares_Object=MibTableColumn
h3cNqaStatResRttSumOfSquares=_H3cNqaStatResRttSumOfSquares_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,9),_H3cNqaStatResRttSumOfSquares_Type())
h3cNqaStatResRttSumOfSquares.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResRttSumOfSquares.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatResRttSumOfSquares.setUnits(_D)
_H3cNqaStatResStartTime_Type=DateAndTime
_H3cNqaStatResStartTime_Object=MibTableColumn
h3cNqaStatResStartTime=_H3cNqaStatResStartTime_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,10),_H3cNqaStatResStartTime_Type())
h3cNqaStatResStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResStartTime.setStatus(_A)
_H3cNqaStatResInterval_Type=Gauge32
_H3cNqaStatResInterval_Object=MibTableColumn
h3cNqaStatResInterval=_H3cNqaStatResInterval_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,11),_H3cNqaStatResInterval_Type())
h3cNqaStatResInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatResInterval.setUnits(_j)
_H3cNqaStatResRttNumDisconnects_Type=Counter32
_H3cNqaStatResRttNumDisconnects_Object=MibTableColumn
h3cNqaStatResRttNumDisconnects=_H3cNqaStatResRttNumDisconnects_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,12),_H3cNqaStatResRttNumDisconnects_Type())
h3cNqaStatResRttNumDisconnects.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResRttNumDisconnects.setStatus(_A)
_H3cNqaStatResRttTimeouts_Type=Counter32
_H3cNqaStatResRttTimeouts_Object=MibTableColumn
h3cNqaStatResRttTimeouts=_H3cNqaStatResRttTimeouts_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,13),_H3cNqaStatResRttTimeouts_Type())
h3cNqaStatResRttTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResRttTimeouts.setStatus(_A)
_H3cNqaStatResRttBusies_Type=Counter32
_H3cNqaStatResRttBusies_Object=MibTableColumn
h3cNqaStatResRttBusies=_H3cNqaStatResRttBusies_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,14),_H3cNqaStatResRttBusies_Type())
h3cNqaStatResRttBusies.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResRttBusies.setStatus(_A)
_H3cNqaStatResRttNoConnections_Type=Counter32
_H3cNqaStatResRttNoConnections_Object=MibTableColumn
h3cNqaStatResRttNoConnections=_H3cNqaStatResRttNoConnections_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,15),_H3cNqaStatResRttNoConnections_Type())
h3cNqaStatResRttNoConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResRttNoConnections.setStatus(_A)
_H3cNqaStatResRttDrops_Type=Counter32
_H3cNqaStatResRttDrops_Object=MibTableColumn
h3cNqaStatResRttDrops=_H3cNqaStatResRttDrops_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,16),_H3cNqaStatResRttDrops_Type())
h3cNqaStatResRttDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResRttDrops.setStatus(_A)
_H3cNqaStatResRttSequenceErrors_Type=Counter32
_H3cNqaStatResRttSequenceErrors_Object=MibTableColumn
h3cNqaStatResRttSequenceErrors=_H3cNqaStatResRttSequenceErrors_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,17),_H3cNqaStatResRttSequenceErrors_Type())
h3cNqaStatResRttSequenceErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResRttSequenceErrors.setStatus(_A)
_H3cNqaStatResRttErrors_Type=Counter32
_H3cNqaStatResRttErrors_Object=MibTableColumn
h3cNqaStatResRttErrors=_H3cNqaStatResRttErrors_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,18),_H3cNqaStatResRttErrors_Type())
h3cNqaStatResRttErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResRttErrors.setStatus(_A)
_H3cNqaStatResLostPacketRatio_Type=Gauge32
_H3cNqaStatResLostPacketRatio_Object=MibTableColumn
h3cNqaStatResLostPacketRatio=_H3cNqaStatResLostPacketRatio_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,19),_H3cNqaStatResLostPacketRatio_Type())
h3cNqaStatResLostPacketRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResLostPacketRatio.setStatus(_A)
_H3cNqaStatResPacketLateArrival_Type=Counter32
_H3cNqaStatResPacketLateArrival_Object=MibTableColumn
h3cNqaStatResPacketLateArrival=_H3cNqaStatResPacketLateArrival_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,20),_H3cNqaStatResPacketLateArrival_Type())
h3cNqaStatResPacketLateArrival.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResPacketLateArrival.setStatus(_A)
_H3cNqaStatResRttSum_Type=Counter32
_H3cNqaStatResRttSum_Object=MibTableColumn
h3cNqaStatResRttSum=_H3cNqaStatResRttSum_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,21),_H3cNqaStatResRttSum_Type())
h3cNqaStatResRttSum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResRttSum.setStatus(_A)
_H3cNqaStatResNumOfDelaySD_Type=Counter32
_H3cNqaStatResNumOfDelaySD_Object=MibTableColumn
h3cNqaStatResNumOfDelaySD=_H3cNqaStatResNumOfDelaySD_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,22),_H3cNqaStatResNumOfDelaySD_Type())
h3cNqaStatResNumOfDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResNumOfDelaySD.setStatus(_A)
_H3cNqaStatResMinDelaySD_Type=Gauge32
_H3cNqaStatResMinDelaySD_Object=MibTableColumn
h3cNqaStatResMinDelaySD=_H3cNqaStatResMinDelaySD_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,23),_H3cNqaStatResMinDelaySD_Type())
h3cNqaStatResMinDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResMinDelaySD.setStatus(_A)
_H3cNqaStatResMaxDelaySD_Type=Gauge32
_H3cNqaStatResMaxDelaySD_Object=MibTableColumn
h3cNqaStatResMaxDelaySD=_H3cNqaStatResMaxDelaySD_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,24),_H3cNqaStatResMaxDelaySD_Type())
h3cNqaStatResMaxDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResMaxDelaySD.setStatus(_A)
_H3cNqaStatResSumDelaySD_Type=Counter32
_H3cNqaStatResSumDelaySD_Object=MibTableColumn
h3cNqaStatResSumDelaySD=_H3cNqaStatResSumDelaySD_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,25),_H3cNqaStatResSumDelaySD_Type())
h3cNqaStatResSumDelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResSumDelaySD.setStatus(_A)
_H3cNqaStatResSum2DelaySD_Type=Counter32
_H3cNqaStatResSum2DelaySD_Object=MibTableColumn
h3cNqaStatResSum2DelaySD=_H3cNqaStatResSum2DelaySD_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,26),_H3cNqaStatResSum2DelaySD_Type())
h3cNqaStatResSum2DelaySD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResSum2DelaySD.setStatus(_A)
_H3cNqaStatResNumOfDelayDS_Type=Counter32
_H3cNqaStatResNumOfDelayDS_Object=MibTableColumn
h3cNqaStatResNumOfDelayDS=_H3cNqaStatResNumOfDelayDS_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,27),_H3cNqaStatResNumOfDelayDS_Type())
h3cNqaStatResNumOfDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResNumOfDelayDS.setStatus(_A)
_H3cNqaStatResMinDelayDS_Type=Gauge32
_H3cNqaStatResMinDelayDS_Object=MibTableColumn
h3cNqaStatResMinDelayDS=_H3cNqaStatResMinDelayDS_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,28),_H3cNqaStatResMinDelayDS_Type())
h3cNqaStatResMinDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResMinDelayDS.setStatus(_A)
_H3cNqaStatResMaxDelayDS_Type=Gauge32
_H3cNqaStatResMaxDelayDS_Object=MibTableColumn
h3cNqaStatResMaxDelayDS=_H3cNqaStatResMaxDelayDS_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,29),_H3cNqaStatResMaxDelayDS_Type())
h3cNqaStatResMaxDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResMaxDelayDS.setStatus(_A)
_H3cNqaStatResSumDelayDS_Type=Counter32
_H3cNqaStatResSumDelayDS_Object=MibTableColumn
h3cNqaStatResSumDelayDS=_H3cNqaStatResSumDelayDS_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,30),_H3cNqaStatResSumDelayDS_Type())
h3cNqaStatResSumDelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResSumDelayDS.setStatus(_A)
_H3cNqaStatResSum2DelayDS_Type=Counter32
_H3cNqaStatResSum2DelayDS_Object=MibTableColumn
h3cNqaStatResSum2DelayDS=_H3cNqaStatResSum2DelayDS_Object((1,3,6,1,4,1,2011,10,8,3,1,11,1,31),_H3cNqaStatResSum2DelayDS_Type())
h3cNqaStatResSum2DelayDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatResSum2DelayDS.setStatus(_A)
_H3cNqaGroupStatsJitterTable_Object=MibTable
h3cNqaGroupStatsJitterTable=_H3cNqaGroupStatsJitterTable_Object((1,3,6,1,4,1,2011,10,8,3,1,12))
if mibBuilder.loadTexts:h3cNqaGroupStatsJitterTable.setStatus(_A)
_H3cNqaGroupStatsJitterEntry_Object=MibTableRow
h3cNqaGroupStatsJitterEntry=_H3cNqaGroupStatsJitterEntry_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1))
h3cNqaGroupStatsJitterEntry.setIndexNames((0,_E,_T),(0,_E,_U),(0,_C,_l))
if mibBuilder.loadTexts:h3cNqaGroupStatsJitterEntry.setStatus(_A)
class _H3cNqaStatJitterIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cNqaStatJitterIndex_Type.__name__=_I
_H3cNqaStatJitterIndex_Object=MibTableColumn
h3cNqaStatJitterIndex=_H3cNqaStatJitterIndex_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,1),_H3cNqaStatJitterIndex_Type())
h3cNqaStatJitterIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaStatJitterIndex.setStatus(_A)
_H3cNqaStatJitterMinOfPosSD_Type=Gauge32
_H3cNqaStatJitterMinOfPosSD_Object=MibTableColumn
h3cNqaStatJitterMinOfPosSD=_H3cNqaStatJitterMinOfPosSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,2),_H3cNqaStatJitterMinOfPosSD_Type())
h3cNqaStatJitterMinOfPosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterMinOfPosSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterMinOfPosSD.setUnits(_D)
_H3cNqaStatJitterMaxOfPosSD_Type=Gauge32
_H3cNqaStatJitterMaxOfPosSD_Object=MibTableColumn
h3cNqaStatJitterMaxOfPosSD=_H3cNqaStatJitterMaxOfPosSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,3),_H3cNqaStatJitterMaxOfPosSD_Type())
h3cNqaStatJitterMaxOfPosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterMaxOfPosSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterMaxOfPosSD.setUnits(_D)
_H3cNqaStatJitterNumOfPosSD_Type=Counter32
_H3cNqaStatJitterNumOfPosSD_Object=MibTableColumn
h3cNqaStatJitterNumOfPosSD=_H3cNqaStatJitterNumOfPosSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,4),_H3cNqaStatJitterNumOfPosSD_Type())
h3cNqaStatJitterNumOfPosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterNumOfPosSD.setStatus(_A)
_H3cNqaStatJitterSumOfPosSD_Type=Counter32
_H3cNqaStatJitterSumOfPosSD_Object=MibTableColumn
h3cNqaStatJitterSumOfPosSD=_H3cNqaStatJitterSumOfPosSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,5),_H3cNqaStatJitterSumOfPosSD_Type())
h3cNqaStatJitterSumOfPosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfPosSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfPosSD.setUnits(_D)
_H3cNqaStatJitterSumOfSquarePosSD_Type=Counter32
_H3cNqaStatJitterSumOfSquarePosSD_Object=MibTableColumn
h3cNqaStatJitterSumOfSquarePosSD=_H3cNqaStatJitterSumOfSquarePosSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,6),_H3cNqaStatJitterSumOfSquarePosSD_Type())
h3cNqaStatJitterSumOfSquarePosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfSquarePosSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfSquarePosSD.setUnits(_D)
_H3cNqaStatJitterMinOfNegSD_Type=Gauge32
_H3cNqaStatJitterMinOfNegSD_Object=MibTableColumn
h3cNqaStatJitterMinOfNegSD=_H3cNqaStatJitterMinOfNegSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,7),_H3cNqaStatJitterMinOfNegSD_Type())
h3cNqaStatJitterMinOfNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterMinOfNegSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterMinOfNegSD.setUnits(_D)
_H3cNqaStatJitterMaxOfNegSD_Type=Gauge32
_H3cNqaStatJitterMaxOfNegSD_Object=MibTableColumn
h3cNqaStatJitterMaxOfNegSD=_H3cNqaStatJitterMaxOfNegSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,8),_H3cNqaStatJitterMaxOfNegSD_Type())
h3cNqaStatJitterMaxOfNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterMaxOfNegSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterMaxOfNegSD.setUnits(_D)
_H3cNqaStatJitterNumOfNegSD_Type=Counter32
_H3cNqaStatJitterNumOfNegSD_Object=MibTableColumn
h3cNqaStatJitterNumOfNegSD=_H3cNqaStatJitterNumOfNegSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,9),_H3cNqaStatJitterNumOfNegSD_Type())
h3cNqaStatJitterNumOfNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterNumOfNegSD.setStatus(_A)
_H3cNqaStatJitterSumOfNegSD_Type=Counter32
_H3cNqaStatJitterSumOfNegSD_Object=MibTableColumn
h3cNqaStatJitterSumOfNegSD=_H3cNqaStatJitterSumOfNegSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,10),_H3cNqaStatJitterSumOfNegSD_Type())
h3cNqaStatJitterSumOfNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfNegSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfNegSD.setUnits(_D)
_H3cNqaStatJitterSumOfSquareNegSD_Type=Counter32
_H3cNqaStatJitterSumOfSquareNegSD_Object=MibTableColumn
h3cNqaStatJitterSumOfSquareNegSD=_H3cNqaStatJitterSumOfSquareNegSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,11),_H3cNqaStatJitterSumOfSquareNegSD_Type())
h3cNqaStatJitterSumOfSquareNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfSquareNegSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfSquareNegSD.setUnits(_D)
_H3cNqaStatJitterMinOfPosDS_Type=Gauge32
_H3cNqaStatJitterMinOfPosDS_Object=MibTableColumn
h3cNqaStatJitterMinOfPosDS=_H3cNqaStatJitterMinOfPosDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,12),_H3cNqaStatJitterMinOfPosDS_Type())
h3cNqaStatJitterMinOfPosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterMinOfPosDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterMinOfPosDS.setUnits(_D)
_H3cNqaStatJitterMaxOfPosDS_Type=Gauge32
_H3cNqaStatJitterMaxOfPosDS_Object=MibTableColumn
h3cNqaStatJitterMaxOfPosDS=_H3cNqaStatJitterMaxOfPosDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,13),_H3cNqaStatJitterMaxOfPosDS_Type())
h3cNqaStatJitterMaxOfPosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterMaxOfPosDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterMaxOfPosDS.setUnits(_D)
_H3cNqaStatJitterNumOfPosDS_Type=Counter32
_H3cNqaStatJitterNumOfPosDS_Object=MibTableColumn
h3cNqaStatJitterNumOfPosDS=_H3cNqaStatJitterNumOfPosDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,14),_H3cNqaStatJitterNumOfPosDS_Type())
h3cNqaStatJitterNumOfPosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterNumOfPosDS.setStatus(_A)
_H3cNqaStatJitterSumOfPosDS_Type=Counter32
_H3cNqaStatJitterSumOfPosDS_Object=MibTableColumn
h3cNqaStatJitterSumOfPosDS=_H3cNqaStatJitterSumOfPosDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,15),_H3cNqaStatJitterSumOfPosDS_Type())
h3cNqaStatJitterSumOfPosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfPosDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfPosDS.setUnits(_D)
_H3cNqaStatJitterSumOfSquarePosDS_Type=Counter32
_H3cNqaStatJitterSumOfSquarePosDS_Object=MibTableColumn
h3cNqaStatJitterSumOfSquarePosDS=_H3cNqaStatJitterSumOfSquarePosDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,16),_H3cNqaStatJitterSumOfSquarePosDS_Type())
h3cNqaStatJitterSumOfSquarePosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfSquarePosDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfSquarePosDS.setUnits(_D)
_H3cNqaStatJitterMinOfNegDS_Type=Gauge32
_H3cNqaStatJitterMinOfNegDS_Object=MibTableColumn
h3cNqaStatJitterMinOfNegDS=_H3cNqaStatJitterMinOfNegDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,17),_H3cNqaStatJitterMinOfNegDS_Type())
h3cNqaStatJitterMinOfNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterMinOfNegDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterMinOfNegDS.setUnits(_D)
_H3cNqaStatJitterMaxOfNegDS_Type=Gauge32
_H3cNqaStatJitterMaxOfNegDS_Object=MibTableColumn
h3cNqaStatJitterMaxOfNegDS=_H3cNqaStatJitterMaxOfNegDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,18),_H3cNqaStatJitterMaxOfNegDS_Type())
h3cNqaStatJitterMaxOfNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterMaxOfNegDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterMaxOfNegDS.setUnits(_D)
_H3cNqaStatJitterNumOfNegDS_Type=Counter32
_H3cNqaStatJitterNumOfNegDS_Object=MibTableColumn
h3cNqaStatJitterNumOfNegDS=_H3cNqaStatJitterNumOfNegDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,19),_H3cNqaStatJitterNumOfNegDS_Type())
h3cNqaStatJitterNumOfNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterNumOfNegDS.setStatus(_A)
_H3cNqaStatJitterSumOfNegDS_Type=Counter32
_H3cNqaStatJitterSumOfNegDS_Object=MibTableColumn
h3cNqaStatJitterSumOfNegDS=_H3cNqaStatJitterSumOfNegDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,20),_H3cNqaStatJitterSumOfNegDS_Type())
h3cNqaStatJitterSumOfNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfNegDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfNegDS.setUnits(_D)
_H3cNqaStatJitterSumOfSquareNegDS_Type=Counter32
_H3cNqaStatJitterSumOfSquareNegDS_Object=MibTableColumn
h3cNqaStatJitterSumOfSquareNegDS=_H3cNqaStatJitterSumOfSquareNegDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,21),_H3cNqaStatJitterSumOfSquareNegDS_Type())
h3cNqaStatJitterSumOfSquareNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfSquareNegDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterSumOfSquareNegDS.setUnits(_D)
_H3cNqaStatJitterPacketLossSD_Type=Counter32
_H3cNqaStatJitterPacketLossSD_Object=MibTableColumn
h3cNqaStatJitterPacketLossSD=_H3cNqaStatJitterPacketLossSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,22),_H3cNqaStatJitterPacketLossSD_Type())
h3cNqaStatJitterPacketLossSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterPacketLossSD.setStatus(_A)
_H3cNqaStatJitterPacketLossDS_Type=Counter32
_H3cNqaStatJitterPacketLossDS_Object=MibTableColumn
h3cNqaStatJitterPacketLossDS=_H3cNqaStatJitterPacketLossDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,23),_H3cNqaStatJitterPacketLossDS_Type())
h3cNqaStatJitterPacketLossDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterPacketLossDS.setStatus(_A)
_H3cNqaStatJitterAvePosSD_Type=Gauge32
_H3cNqaStatJitterAvePosSD_Object=MibTableColumn
h3cNqaStatJitterAvePosSD=_H3cNqaStatJitterAvePosSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,24),_H3cNqaStatJitterAvePosSD_Type())
h3cNqaStatJitterAvePosSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterAvePosSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterAvePosSD.setUnits(_D)
_H3cNqaStatJitterAveNegSD_Type=Gauge32
_H3cNqaStatJitterAveNegSD_Object=MibTableColumn
h3cNqaStatJitterAveNegSD=_H3cNqaStatJitterAveNegSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,25),_H3cNqaStatJitterAveNegSD_Type())
h3cNqaStatJitterAveNegSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterAveNegSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterAveNegSD.setUnits(_D)
_H3cNqaStatJitterAvePosDS_Type=Gauge32
_H3cNqaStatJitterAvePosDS_Object=MibTableColumn
h3cNqaStatJitterAvePosDS=_H3cNqaStatJitterAvePosDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,26),_H3cNqaStatJitterAvePosDS_Type())
h3cNqaStatJitterAvePosDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterAvePosDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterAvePosDS.setUnits(_D)
_H3cNqaStatJitterAveNegDS_Type=Gauge32
_H3cNqaStatJitterAveNegDS_Object=MibTableColumn
h3cNqaStatJitterAveNegDS=_H3cNqaStatJitterAveNegDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,27),_H3cNqaStatJitterAveNegDS_Type())
h3cNqaStatJitterAveNegDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterAveNegDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterAveNegDS.setUnits(_D)
_H3cNqaStatJitterPktLossUnknown_Type=Counter32
_H3cNqaStatJitterPktLossUnknown_Object=MibTableColumn
h3cNqaStatJitterPktLossUnknown=_H3cNqaStatJitterPktLossUnknown_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,28),_H3cNqaStatJitterPktLossUnknown_Type())
h3cNqaStatJitterPktLossUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterPktLossUnknown.setStatus(_A)
_H3cNqaStatJitterMaxOfICPIF_Type=Gauge32
_H3cNqaStatJitterMaxOfICPIF_Object=MibTableColumn
h3cNqaStatJitterMaxOfICPIF=_H3cNqaStatJitterMaxOfICPIF_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,29),_H3cNqaStatJitterMaxOfICPIF_Type())
h3cNqaStatJitterMaxOfICPIF.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterMaxOfICPIF.setStatus(_A)
_H3cNqaStatJitterMinOfICPIF_Type=Gauge32
_H3cNqaStatJitterMinOfICPIF_Object=MibTableColumn
h3cNqaStatJitterMinOfICPIF=_H3cNqaStatJitterMinOfICPIF_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,30),_H3cNqaStatJitterMinOfICPIF_Type())
h3cNqaStatJitterMinOfICPIF.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterMinOfICPIF.setStatus(_A)
_H3cNqaStatJitterMaxOfMOS_Type=Gauge32
_H3cNqaStatJitterMaxOfMOS_Object=MibTableColumn
h3cNqaStatJitterMaxOfMOS=_H3cNqaStatJitterMaxOfMOS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,31),_H3cNqaStatJitterMaxOfMOS_Type())
h3cNqaStatJitterMaxOfMOS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterMaxOfMOS.setStatus(_A)
_H3cNqaStatJitterMinOfMOS_Type=Gauge32
_H3cNqaStatJitterMinOfMOS_Object=MibTableColumn
h3cNqaStatJitterMinOfMOS=_H3cNqaStatJitterMinOfMOS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,32),_H3cNqaStatJitterMinOfMOS_Type())
h3cNqaStatJitterMinOfMOS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterMinOfMOS.setStatus(_A)
_H3cNqaStatJitterAveSD_Type=Gauge32
_H3cNqaStatJitterAveSD_Object=MibTableColumn
h3cNqaStatJitterAveSD=_H3cNqaStatJitterAveSD_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,33),_H3cNqaStatJitterAveSD_Type())
h3cNqaStatJitterAveSD.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterAveSD.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterAveSD.setUnits(_D)
_H3cNqaStatJitterAveDS_Type=Gauge32
_H3cNqaStatJitterAveDS_Object=MibTableColumn
h3cNqaStatJitterAveDS=_H3cNqaStatJitterAveDS_Object((1,3,6,1,4,1,2011,10,8,3,1,12,1,34),_H3cNqaStatJitterAveDS_Type())
h3cNqaStatJitterAveDS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatJitterAveDS.setStatus(_A)
if mibBuilder.loadTexts:h3cNqaStatJitterAveDS.setUnits(_D)
_H3cNqaReactionTable_Object=MibTable
h3cNqaReactionTable=_H3cNqaReactionTable_Object((1,3,6,1,4,1,2011,10,8,3,1,13))
if mibBuilder.loadTexts:h3cNqaReactionTable.setStatus(_A)
_H3cNqaReactionEntry_Object=MibTableRow
h3cNqaReactionEntry=_H3cNqaReactionEntry_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1))
h3cNqaReactionEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:h3cNqaReactionEntry.setStatus(_A)
class _H3cNqaReactOwnerIndex_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cNqaReactOwnerIndex_Type.__name__=_V
_H3cNqaReactOwnerIndex_Object=MibTableColumn
h3cNqaReactOwnerIndex=_H3cNqaReactOwnerIndex_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,1),_H3cNqaReactOwnerIndex_Type())
h3cNqaReactOwnerIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:h3cNqaReactOwnerIndex.setStatus(_A)
class _H3cNqaReactTestName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cNqaReactTestName_Type.__name__=_V
_H3cNqaReactTestName_Object=MibTableColumn
h3cNqaReactTestName=_H3cNqaReactTestName_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,2),_H3cNqaReactTestName_Type())
h3cNqaReactTestName.setMaxAccess(_Z)
if mibBuilder.loadTexts:h3cNqaReactTestName.setStatus(_A)
class _H3cNqaReactItemIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_H3cNqaReactItemIndex_Type.__name__=_I
_H3cNqaReactItemIndex_Object=MibTableColumn
h3cNqaReactItemIndex=_H3cNqaReactItemIndex_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,3),_H3cNqaReactItemIndex_Type())
h3cNqaReactItemIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:h3cNqaReactItemIndex.setStatus(_A)
class _H3cNqaReactCheckedElement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('probetime',1),('probefailure',2),('jitterrtt',3),('jitterpacketloss',4),('jittersd',5),('jitterds',6),('icpif',7),('mos',8),('jitterOwdSD',9),('jitterOwdDS',10)))
_H3cNqaReactCheckedElement_Type.__name__=_G
_H3cNqaReactCheckedElement_Object=MibTableColumn
h3cNqaReactCheckedElement=_H3cNqaReactCheckedElement_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,4),_H3cNqaReactCheckedElement_Type())
h3cNqaReactCheckedElement.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaReactCheckedElement.setStatus(_A)
class _H3cNqaReactThresholdUpperLimit_Type(Unsigned32):defaultValue=0
_H3cNqaReactThresholdUpperLimit_Type.__name__=_I
_H3cNqaReactThresholdUpperLimit_Object=MibTableColumn
h3cNqaReactThresholdUpperLimit=_H3cNqaReactThresholdUpperLimit_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,5),_H3cNqaReactThresholdUpperLimit_Type())
h3cNqaReactThresholdUpperLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaReactThresholdUpperLimit.setStatus(_A)
class _H3cNqaReactThresholdLowerLimit_Type(Unsigned32):defaultValue=0
_H3cNqaReactThresholdLowerLimit_Type.__name__=_I
_H3cNqaReactThresholdLowerLimit_Object=MibTableColumn
h3cNqaReactThresholdLowerLimit=_H3cNqaReactThresholdLowerLimit_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,6),_H3cNqaReactThresholdLowerLimit_Type())
h3cNqaReactThresholdLowerLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaReactThresholdLowerLimit.setStatus(_A)
class _H3cNqaReactThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_m,0),('average',1),('consecutive',2),('accumulative',3)))
_H3cNqaReactThresholdType_Type.__name__=_G
_H3cNqaReactThresholdType_Object=MibTableColumn
h3cNqaReactThresholdType=_H3cNqaReactThresholdType_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,7),_H3cNqaReactThresholdType_Type())
h3cNqaReactThresholdType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaReactThresholdType.setStatus(_A)
class _H3cNqaReactThresholdConsecNum_Type(Unsigned32):defaultValue=0
_H3cNqaReactThresholdConsecNum_Type.__name__=_I
_H3cNqaReactThresholdConsecNum_Object=MibTableColumn
h3cNqaReactThresholdConsecNum=_H3cNqaReactThresholdConsecNum_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,8),_H3cNqaReactThresholdConsecNum_Type())
h3cNqaReactThresholdConsecNum.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaReactThresholdConsecNum.setStatus(_A)
class _H3cNqaReactThresholdAccumNum_Type(Unsigned32):defaultValue=0
_H3cNqaReactThresholdAccumNum_Type.__name__=_I
_H3cNqaReactThresholdAccumNum_Object=MibTableColumn
h3cNqaReactThresholdAccumNum=_H3cNqaReactThresholdAccumNum_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,9),_H3cNqaReactThresholdAccumNum_Type())
h3cNqaReactThresholdAccumNum.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaReactThresholdAccumNum.setStatus(_A)
class _H3cNqaReactActionType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('trapOnly',1),('triggerOnly',2),('trapAndTrigger',3)))
_H3cNqaReactActionType_Type.__name__=_G
_H3cNqaReactActionType_Object=MibTableColumn
h3cNqaReactActionType=_H3cNqaReactActionType_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,10),_H3cNqaReactActionType_Type())
h3cNqaReactActionType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaReactActionType.setStatus(_A)
class _H3cNqaReactCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_m,1),('overThreshold',2),('belowThreshold',3)))
_H3cNqaReactCurrentStatus_Type.__name__=_G
_H3cNqaReactCurrentStatus_Object=MibTableColumn
h3cNqaReactCurrentStatus=_H3cNqaReactCurrentStatus_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,11),_H3cNqaReactCurrentStatus_Type())
h3cNqaReactCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaReactCurrentStatus.setStatus(_A)
_H3cNqaReactRowStatus_Type=RowStatus
_H3cNqaReactRowStatus_Object=MibTableColumn
h3cNqaReactRowStatus=_H3cNqaReactRowStatus_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,12),_H3cNqaReactRowStatus_Type())
h3cNqaReactRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaReactRowStatus.setStatus(_A)
class _H3cNqaReactCheckedNum_Type(Unsigned32):defaultValue=0
_H3cNqaReactCheckedNum_Type.__name__=_I
_H3cNqaReactCheckedNum_Object=MibTableColumn
h3cNqaReactCheckedNum=_H3cNqaReactCheckedNum_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,13),_H3cNqaReactCheckedNum_Type())
h3cNqaReactCheckedNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaReactCheckedNum.setStatus(_A)
class _H3cNqaReactThresholdNum_Type(Unsigned32):defaultValue=0
_H3cNqaReactThresholdNum_Type.__name__=_I
_H3cNqaReactThresholdNum_Object=MibTableColumn
h3cNqaReactThresholdNum=_H3cNqaReactThresholdNum_Object((1,3,6,1,4,1,2011,10,8,3,1,13,1,14),_H3cNqaReactThresholdNum_Type())
h3cNqaReactThresholdNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaReactThresholdNum.setStatus(_A)
_H3cNqaStatisticsReactionTable_Object=MibTable
h3cNqaStatisticsReactionTable=_H3cNqaStatisticsReactionTable_Object((1,3,6,1,4,1,2011,10,8,3,1,14))
if mibBuilder.loadTexts:h3cNqaStatisticsReactionTable.setStatus(_A)
_H3cNqaStatisticsReactionEntry_Object=MibTableRow
h3cNqaStatisticsReactionEntry=_H3cNqaStatisticsReactionEntry_Object((1,3,6,1,4,1,2011,10,8,3,1,14,1))
h3cNqaStatisticsReactionEntry.setIndexNames((0,_C,_n),(0,_C,_o),(0,_C,_p),(0,_C,_q))
if mibBuilder.loadTexts:h3cNqaStatisticsReactionEntry.setStatus(_A)
class _H3cNqaStatReactOwnerIndex_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cNqaStatReactOwnerIndex_Type.__name__=_V
_H3cNqaStatReactOwnerIndex_Object=MibTableColumn
h3cNqaStatReactOwnerIndex=_H3cNqaStatReactOwnerIndex_Object((1,3,6,1,4,1,2011,10,8,3,1,14,1,1),_H3cNqaStatReactOwnerIndex_Type())
h3cNqaStatReactOwnerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaStatReactOwnerIndex.setStatus(_A)
class _H3cNqaStatReactTestName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cNqaStatReactTestName_Type.__name__=_V
_H3cNqaStatReactTestName_Object=MibTableColumn
h3cNqaStatReactTestName=_H3cNqaStatReactTestName_Object((1,3,6,1,4,1,2011,10,8,3,1,14,1,2),_H3cNqaStatReactTestName_Type())
h3cNqaStatReactTestName.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaStatReactTestName.setStatus(_A)
class _H3cNqaStatReactIndex_Type(Unsigned32):defaultValue=0
_H3cNqaStatReactIndex_Type.__name__=_I
_H3cNqaStatReactIndex_Object=MibTableColumn
h3cNqaStatReactIndex=_H3cNqaStatReactIndex_Object((1,3,6,1,4,1,2011,10,8,3,1,14,1,3),_H3cNqaStatReactIndex_Type())
h3cNqaStatReactIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaStatReactIndex.setStatus(_A)
class _H3cNqaStatReactItemIndex_Type(Unsigned32):defaultValue=0
_H3cNqaStatReactItemIndex_Type.__name__=_I
_H3cNqaStatReactItemIndex_Object=MibTableColumn
h3cNqaStatReactItemIndex=_H3cNqaStatReactItemIndex_Object((1,3,6,1,4,1,2011,10,8,3,1,14,1,4),_H3cNqaStatReactItemIndex_Type())
h3cNqaStatReactItemIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaStatReactItemIndex.setStatus(_A)
class _H3cNqaStatReactCheckedNum_Type(Counter32):defaultValue=0
_H3cNqaStatReactCheckedNum_Type.__name__=_X
_H3cNqaStatReactCheckedNum_Object=MibTableColumn
h3cNqaStatReactCheckedNum=_H3cNqaStatReactCheckedNum_Object((1,3,6,1,4,1,2011,10,8,3,1,14,1,5),_H3cNqaStatReactCheckedNum_Type())
h3cNqaStatReactCheckedNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatReactCheckedNum.setStatus(_A)
class _H3cNqaStatReactThresholdNum_Type(Counter32):defaultValue=0
_H3cNqaStatReactThresholdNum_Type.__name__=_X
_H3cNqaStatReactThresholdNum_Object=MibTableColumn
h3cNqaStatReactThresholdNum=_H3cNqaStatReactThresholdNum_Object((1,3,6,1,4,1,2011,10,8,3,1,14,1,6),_H3cNqaStatReactThresholdNum_Type())
h3cNqaStatReactThresholdNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cNqaStatReactThresholdNum.setStatus(_A)
_H3cNqaTcpServerExtendTable_Object=MibTable
h3cNqaTcpServerExtendTable=_H3cNqaTcpServerExtendTable_Object((1,3,6,1,4,1,2011,10,8,3,1,15))
if mibBuilder.loadTexts:h3cNqaTcpServerExtendTable.setStatus(_A)
_H3cNqaTcpServerExtendEntry_Object=MibTableRow
h3cNqaTcpServerExtendEntry=_H3cNqaTcpServerExtendEntry_Object((1,3,6,1,4,1,2011,10,8,3,1,15,1))
h3cNqaTcpServerExtendEntry.setIndexNames((0,_C,_r),(0,_C,_s),(0,_C,_t),(0,_C,_u))
if mibBuilder.loadTexts:h3cNqaTcpServerExtendEntry.setStatus(_A)
_H3cNqaTcpServerExtIpAddress_Type=InetAddress
_H3cNqaTcpServerExtIpAddress_Object=MibTableColumn
h3cNqaTcpServerExtIpAddress=_H3cNqaTcpServerExtIpAddress_Object((1,3,6,1,4,1,2011,10,8,3,1,15,1,1),_H3cNqaTcpServerExtIpAddress_Type())
h3cNqaTcpServerExtIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaTcpServerExtIpAddress.setStatus(_A)
class _H3cNqaTcpServerExtPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_H3cNqaTcpServerExtPort_Type.__name__=_G
_H3cNqaTcpServerExtPort_Object=MibTableColumn
h3cNqaTcpServerExtPort=_H3cNqaTcpServerExtPort_Object((1,3,6,1,4,1,2011,10,8,3,1,15,1,2),_H3cNqaTcpServerExtPort_Type())
h3cNqaTcpServerExtPort.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaTcpServerExtPort.setStatus(_A)
_H3cNqaTcpServerExtVPNType_Type=VpnInstanceType
_H3cNqaTcpServerExtVPNType_Object=MibTableColumn
h3cNqaTcpServerExtVPNType=_H3cNqaTcpServerExtVPNType_Object((1,3,6,1,4,1,2011,10,8,3,1,15,1,3),_H3cNqaTcpServerExtVPNType_Type())
h3cNqaTcpServerExtVPNType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaTcpServerExtVPNType.setStatus(_A)
class _H3cNqaTcpServerExtVPNInstance_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_H3cNqaTcpServerExtVPNInstance_Type.__name__=_W
_H3cNqaTcpServerExtVPNInstance_Object=MibTableColumn
h3cNqaTcpServerExtVPNInstance=_H3cNqaTcpServerExtVPNInstance_Object((1,3,6,1,4,1,2011,10,8,3,1,15,1,4),_H3cNqaTcpServerExtVPNInstance_Type())
h3cNqaTcpServerExtVPNInstance.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaTcpServerExtVPNInstance.setStatus(_A)
class _H3cNqaTcpServerExtDSField_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cNqaTcpServerExtDSField_Type.__name__=_I
_H3cNqaTcpServerExtDSField_Object=MibTableColumn
h3cNqaTcpServerExtDSField=_H3cNqaTcpServerExtDSField_Object((1,3,6,1,4,1,2011,10,8,3,1,15,1,5),_H3cNqaTcpServerExtDSField_Type())
h3cNqaTcpServerExtDSField.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaTcpServerExtDSField.setStatus(_A)
_H3cNqaTcpServerExtRowStatus_Type=RowStatus
_H3cNqaTcpServerExtRowStatus_Object=MibTableColumn
h3cNqaTcpServerExtRowStatus=_H3cNqaTcpServerExtRowStatus_Object((1,3,6,1,4,1,2011,10,8,3,1,15,1,6),_H3cNqaTcpServerExtRowStatus_Type())
h3cNqaTcpServerExtRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaTcpServerExtRowStatus.setStatus(_A)
_H3cNqaUdpServerExtendTable_Object=MibTable
h3cNqaUdpServerExtendTable=_H3cNqaUdpServerExtendTable_Object((1,3,6,1,4,1,2011,10,8,3,1,16))
if mibBuilder.loadTexts:h3cNqaUdpServerExtendTable.setStatus(_A)
_H3cNqaUdpServerExtendEntry_Object=MibTableRow
h3cNqaUdpServerExtendEntry=_H3cNqaUdpServerExtendEntry_Object((1,3,6,1,4,1,2011,10,8,3,1,16,1))
h3cNqaUdpServerExtendEntry.setIndexNames((0,_C,_v),(0,_C,_w),(0,_C,_x),(0,_C,_y))
if mibBuilder.loadTexts:h3cNqaUdpServerExtendEntry.setStatus(_A)
_H3cNqaUdpServerExtIpAddress_Type=InetAddress
_H3cNqaUdpServerExtIpAddress_Object=MibTableColumn
h3cNqaUdpServerExtIpAddress=_H3cNqaUdpServerExtIpAddress_Object((1,3,6,1,4,1,2011,10,8,3,1,16,1,1),_H3cNqaUdpServerExtIpAddress_Type())
h3cNqaUdpServerExtIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaUdpServerExtIpAddress.setStatus(_A)
class _H3cNqaUdpServerExtPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_H3cNqaUdpServerExtPort_Type.__name__=_G
_H3cNqaUdpServerExtPort_Object=MibTableColumn
h3cNqaUdpServerExtPort=_H3cNqaUdpServerExtPort_Object((1,3,6,1,4,1,2011,10,8,3,1,16,1,2),_H3cNqaUdpServerExtPort_Type())
h3cNqaUdpServerExtPort.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaUdpServerExtPort.setStatus(_A)
_H3cNqaUdpServerExtVPNType_Type=VpnInstanceType
_H3cNqaUdpServerExtVPNType_Object=MibTableColumn
h3cNqaUdpServerExtVPNType=_H3cNqaUdpServerExtVPNType_Object((1,3,6,1,4,1,2011,10,8,3,1,16,1,3),_H3cNqaUdpServerExtVPNType_Type())
h3cNqaUdpServerExtVPNType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaUdpServerExtVPNType.setStatus(_A)
class _H3cNqaUdpServerExtVPNInstance_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_H3cNqaUdpServerExtVPNInstance_Type.__name__=_W
_H3cNqaUdpServerExtVPNInstance_Object=MibTableColumn
h3cNqaUdpServerExtVPNInstance=_H3cNqaUdpServerExtVPNInstance_Object((1,3,6,1,4,1,2011,10,8,3,1,16,1,4),_H3cNqaUdpServerExtVPNInstance_Type())
h3cNqaUdpServerExtVPNInstance.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cNqaUdpServerExtVPNInstance.setStatus(_A)
class _H3cNqaUdpServerExtDSField_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cNqaUdpServerExtDSField_Type.__name__=_I
_H3cNqaUdpServerExtDSField_Object=MibTableColumn
h3cNqaUdpServerExtDSField=_H3cNqaUdpServerExtDSField_Object((1,3,6,1,4,1,2011,10,8,3,1,16,1,5),_H3cNqaUdpServerExtDSField_Type())
h3cNqaUdpServerExtDSField.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaUdpServerExtDSField.setStatus(_A)
_H3cNqaUdpServerExtRowStatus_Type=RowStatus
_H3cNqaUdpServerExtRowStatus_Object=MibTableColumn
h3cNqaUdpServerExtRowStatus=_H3cNqaUdpServerExtRowStatus_Object((1,3,6,1,4,1,2011,10,8,3,1,16,1,6),_H3cNqaUdpServerExtRowStatus_Type())
h3cNqaUdpServerExtRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cNqaUdpServerExtRowStatus.setStatus(_A)
_H3cNqaImplementationTypeDomains_ObjectIdentity=ObjectIdentity
h3cNqaImplementationTypeDomains=_H3cNqaImplementationTypeDomains_ObjectIdentity((1,3,6,1,4,1,2011,10,8,3,2))
_H3cNqaUdpEcho_ObjectIdentity=ObjectIdentity
h3cNqaUdpEcho=_H3cNqaUdpEcho_ObjectIdentity((1,3,6,1,4,1,2011,10,8,3,2,1))
if mibBuilder.loadTexts:h3cNqaUdpEcho.setStatus(_A)
_H3cNqaTcpconnect_ObjectIdentity=ObjectIdentity
h3cNqaTcpconnect=_H3cNqaTcpconnect_ObjectIdentity((1,3,6,1,4,1,2011,10,8,3,2,2))
if mibBuilder.loadTexts:h3cNqaTcpconnect.setStatus(_A)
_H3cNqajitter_ObjectIdentity=ObjectIdentity
h3cNqajitter=_H3cNqajitter_ObjectIdentity((1,3,6,1,4,1,2011,10,8,3,2,3))
if mibBuilder.loadTexts:h3cNqajitter.setStatus(_A)
_H3cNqaHttp_ObjectIdentity=ObjectIdentity
h3cNqaHttp=_H3cNqaHttp_ObjectIdentity((1,3,6,1,4,1,2011,10,8,3,2,4))
if mibBuilder.loadTexts:h3cNqaHttp.setStatus(_A)
_H3cNqadlsw_ObjectIdentity=ObjectIdentity
h3cNqadlsw=_H3cNqadlsw_ObjectIdentity((1,3,6,1,4,1,2011,10,8,3,2,5))
if mibBuilder.loadTexts:h3cNqadlsw.setStatus(_A)
_H3cNqadhcp_ObjectIdentity=ObjectIdentity
h3cNqadhcp=_H3cNqadhcp_ObjectIdentity((1,3,6,1,4,1,2011,10,8,3,2,6))
if mibBuilder.loadTexts:h3cNqadhcp.setStatus(_A)
_H3cNqaftp_ObjectIdentity=ObjectIdentity
h3cNqaftp=_H3cNqaftp_ObjectIdentity((1,3,6,1,4,1,2011,10,8,3,2,7))
if mibBuilder.loadTexts:h3cNqaftp.setStatus(_A)
_H3cNqaNotifications_ObjectIdentity=ObjectIdentity
h3cNqaNotifications=_H3cNqaNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,8,3,3))
pingCtlEntry.registerAugmentions((_C,_z))
h3cNqaCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())
pingCtlEntry.registerAugmentions((_C,_A0))
h3cNqaStatisticsCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())
h3cNqaProbeTimeOverThreshold=NotificationType((1,3,6,1,4,1,2011,10,8,3,3,1))
h3cNqaProbeTimeOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_E,_O),(_E,_N),(_E,_P),(_E,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:h3cNqaProbeTimeOverThreshold.setStatus(_A)
h3cNqaJitterRTTOverThreshold=NotificationType((1,3,6,1,4,1,2011,10,8,3,3,2))
h3cNqaJitterRTTOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_E,_O),(_E,_N),(_E,_P),(_E,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:h3cNqaJitterRTTOverThreshold.setStatus(_A)
h3cNqaProbeFailure=NotificationType((1,3,6,1,4,1,2011,10,8,3,3,3))
h3cNqaProbeFailure.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_E,_O),(_E,_N),(_E,_P),(_E,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:h3cNqaProbeFailure.setStatus(_A)
h3cNqaJitterPacketLoss=NotificationType((1,3,6,1,4,1,2011,10,8,3,3,4))
h3cNqaJitterPacketLoss.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_E,_O),(_E,_N),(_E,_P),(_E,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:h3cNqaJitterPacketLoss.setStatus(_A)
h3cNqaJitterSDOverThreshold=NotificationType((1,3,6,1,4,1,2011,10,8,3,3,5))
h3cNqaJitterSDOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_E,_O),(_E,_N),(_E,_P),(_E,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:h3cNqaJitterSDOverThreshold.setStatus(_A)
h3cNqaJitterDSOverThreshold=NotificationType((1,3,6,1,4,1,2011,10,8,3,3,6))
h3cNqaJitterDSOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_E,_O),(_E,_N),(_E,_P),(_E,_M),(_C,_R),(_C,_Q)))
if mibBuilder.loadTexts:h3cNqaJitterDSOverThreshold.setStatus(_A)
h3cNqaICPIFOverThreshold=NotificationType((1,3,6,1,4,1,2011,10,8,3,3,7))
h3cNqaICPIFOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_E,_O),(_E,_N),(_E,_P),(_E,_M),(_C,_Q)))
if mibBuilder.loadTexts:h3cNqaICPIFOverThreshold.setStatus(_A)
h3cNqaMOSOverThreshold=NotificationType((1,3,6,1,4,1,2011,10,8,3,3,8))
h3cNqaMOSOverThreshold.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_E,_O),(_E,_N),(_E,_P),(_E,_M),(_C,_Q)))
if mibBuilder.loadTexts:h3cNqaMOSOverThreshold.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'VpnInstanceType':VpnInstanceType,'h3cNqa':h3cNqa,'h3cNqaObjects':h3cNqaObjects,'h3cNqaMIBVersion':h3cNqaMIBVersion,'h3cNqaCtlTable':h3cNqaCtlTable,_z:h3cNqaCtlEntry,'h3cNqaCtlTargetPort':h3cNqaCtlTargetPort,'h3cNqaCtlSourcePort':h3cNqaCtlSourcePort,'h3cNqaCtlTTL':h3cNqaCtlTTL,'h3cNqaCtlJitterAdminInterval':h3cNqaCtlJitterAdminInterval,'h3cNqaCtlJitterAdminNumPackets':h3cNqaCtlJitterAdminNumPackets,'h3cNqaCtlHttpOperationType':h3cNqaCtlHttpOperationType,'h3cNqaCtlHttpOperationString':h3cNqaCtlHttpOperationString,'h3cNqaCtlFtpOperationType':h3cNqaCtlFtpOperationType,'h3cNqaCtlFtpUsername':h3cNqaCtlFtpUsername,'h3cNqaCtlFtpPassword':h3cNqaCtlFtpPassword,'h3cNqaCtlFtpOperationString':h3cNqaCtlFtpOperationString,'h3cNqaCtlVPNInstance':h3cNqaCtlVPNInstance,'h3cNqaCtlHistoryKeptTime':h3cNqaCtlHistoryKeptTime,'h3cNqaCtlHistoryEnable':h3cNqaCtlHistoryEnable,'h3cNqaCtlICPIFAdvFactor':h3cNqaCtlICPIFAdvFactor,'h3cNqaCtlCodecType':h3cNqaCtlCodecType,'h3cNqaResultsTable':h3cNqaResultsTable,'h3cNqaResultsEntry':h3cNqaResultsEntry,'h3cNqaResultsRttNumDisconnects':h3cNqaResultsRttNumDisconnects,'h3cNqaResultsRttTimeouts':h3cNqaResultsRttTimeouts,'h3cNqaResultsRttBusies':h3cNqaResultsRttBusies,'h3cNqaResultsRttNoConnections':h3cNqaResultsRttNoConnections,'h3cNqaResultsRttDrops':h3cNqaResultsRttDrops,'h3cNqaResultsRttSequenceErrors':h3cNqaResultsRttSequenceErrors,'h3cNqaResultsRttStatsErrors':h3cNqaResultsRttStatsErrors,'h3cNqaResultsMaxDelaySD':h3cNqaResultsMaxDelaySD,'h3cNqaResultsMaxDelayDS':h3cNqaResultsMaxDelayDS,'h3cNqaResultsLostPacketRatio':h3cNqaResultsLostPacketRatio,'h3cNqaResultsPacketLateArrival':h3cNqaResultsPacketLateArrival,'h3cNqaResultsRttSum':h3cNqaResultsRttSum,'h3cNqaResultsNumOfDelaySD':h3cNqaResultsNumOfDelaySD,'h3cNqaResultsMinDelaySD':h3cNqaResultsMinDelaySD,'h3cNqaResultsSumDelaySD':h3cNqaResultsSumDelaySD,'h3cNqaResultsSum2DelaySD':h3cNqaResultsSum2DelaySD,'h3cNqaResultsNumOfDelayDS':h3cNqaResultsNumOfDelayDS,'h3cNqaResultsMinDelayDS':h3cNqaResultsMinDelayDS,'h3cNqaResultsSumDelayDS':h3cNqaResultsSumDelayDS,'h3cNqaResultsSum2DelayDS':h3cNqaResultsSum2DelayDS,'h3cNqaJitterStatsTable':h3cNqaJitterStatsTable,'h3cNqaJitterStatsEntry':h3cNqaJitterStatsEntry,'h3cNqaJitterStatsNumOfRTT':h3cNqaJitterStatsNumOfRTT,'h3cNqaJitterStatsMinOfPositivesSD':h3cNqaJitterStatsMinOfPositivesSD,'h3cNqaJitterStatsMaxOfPositivesSD':h3cNqaJitterStatsMaxOfPositivesSD,'h3cNqaJitterStatsNumOfPositivesSD':h3cNqaJitterStatsNumOfPositivesSD,'h3cNqaJitterStatsSumOfPositivesSD':h3cNqaJitterStatsSumOfPositivesSD,'h3cNqaJitterStatsSum2PositivesSD':h3cNqaJitterStatsSum2PositivesSD,'h3cNqaJitterStatsMinOfNegativesSD':h3cNqaJitterStatsMinOfNegativesSD,'h3cNqaJitterStatsMaxOfNegativesSD':h3cNqaJitterStatsMaxOfNegativesSD,'h3cNqaJitterStatsNumOfNegativesSD':h3cNqaJitterStatsNumOfNegativesSD,'h3cNqaJitterStatsSumOfNegativesSD':h3cNqaJitterStatsSumOfNegativesSD,'h3cNqaJitterStatsSum2NegativesSD':h3cNqaJitterStatsSum2NegativesSD,'h3cNqaJitterStatsMinOfPositivesDS':h3cNqaJitterStatsMinOfPositivesDS,'h3cNqaJitterStatsMaxOfPositivesDS':h3cNqaJitterStatsMaxOfPositivesDS,'h3cNqaJitterStatsNumOfPositivesDS':h3cNqaJitterStatsNumOfPositivesDS,'h3cNqaJitterStatsSumOfPositivesDS':h3cNqaJitterStatsSumOfPositivesDS,'h3cNqaJitterStatsSum2PositivesDS':h3cNqaJitterStatsSum2PositivesDS,'h3cNqaJitterStatsMinOfNegativesDS':h3cNqaJitterStatsMinOfNegativesDS,'h3cNqaJitterStatsMaxOfNegativesDS':h3cNqaJitterStatsMaxOfNegativesDS,'h3cNqaJitterStatsNumOfNegativesDS':h3cNqaJitterStatsNumOfNegativesDS,'h3cNqaJitterStatsSumOfNegativesDS':h3cNqaJitterStatsSumOfNegativesDS,'h3cNqaJitterStatsSum2NegativesDS':h3cNqaJitterStatsSum2NegativesDS,'h3cNqaJitterStatsPacketLossSD':h3cNqaJitterStatsPacketLossSD,'h3cNqaJitterStatsPacketLossDS':h3cNqaJitterStatsPacketLossDS,'h3cNqaJitterStatsAvePositivesSD':h3cNqaJitterStatsAvePositivesSD,'h3cNqaJitterStatsAveNegativesSD':h3cNqaJitterStatsAveNegativesSD,'h3cNqaJitterStatsAvePositivesDS':h3cNqaJitterStatsAvePositivesDS,'h3cNqaJitterStatsAveNegativesDS':h3cNqaJitterStatsAveNegativesDS,'h3cNqaJitterStatsPktLossUnknown':h3cNqaJitterStatsPktLossUnknown,'h3cNqaJitterStatsOperOfICPIF':h3cNqaJitterStatsOperOfICPIF,'h3cNqaJitterStatsOperOfMOS':h3cNqaJitterStatsOperOfMOS,'h3cNqaJitterStatsAveSD':h3cNqaJitterStatsAveSD,'h3cNqaJitterStatsAveDS':h3cNqaJitterStatsAveDS,'h3cNqaAgentEnable':h3cNqaAgentEnable,'h3cNqaTcpServerTable':h3cNqaTcpServerTable,'h3cNqaTcpServerEntry':h3cNqaTcpServerEntry,_f:h3cNqaTcpServerIpAddress,_g:h3cNqaTcpServerPort,'h3cNqaTcpServerRowStatus':h3cNqaTcpServerRowStatus,'h3cNqaUdpServerTable':h3cNqaUdpServerTable,'h3cNqaUdpServerEntry':h3cNqaUdpServerEntry,_h:h3cNqaUdpServerIpAddress,_i:h3cNqaUdpServerPort,'h3cNqaUdpServerRowStatus':h3cNqaUdpServerRowStatus,'h3cNqaServerEnable':h3cNqaServerEnable,'h3cNqaStatsMaxGroupNumber':h3cNqaStatsMaxGroupNumber,'h3cNqaStatisticsCtlTable':h3cNqaStatisticsCtlTable,_A0:h3cNqaStatisticsCtlEntry,'h3cNqaCtlStatisticsInterval':h3cNqaCtlStatisticsInterval,'h3cNqaCtlStatisticsGroupNumber':h3cNqaCtlStatisticsGroupNumber,'h3cNqaCtlStatisticsKeptTime':h3cNqaCtlStatisticsKeptTime,'h3cNqaCtlBeginTime':h3cNqaCtlBeginTime,'h3cNqaCtlLifeTime':h3cNqaCtlLifeTime,'h3cNqaStatisticsResultsTable':h3cNqaStatisticsResultsTable,'h3cNqaStatisticsResultsEntry':h3cNqaStatisticsResultsEntry,_k:h3cNqaStatResIndex,'h3cNqaStatResIpTargetAddressType':h3cNqaStatResIpTargetAddressType,'h3cNqaStatResIpTargetAddress':h3cNqaStatResIpTargetAddress,'h3cNqaStatResMinRtt':h3cNqaStatResMinRtt,'h3cNqaStatResMaxRtt':h3cNqaStatResMaxRtt,'h3cNqaStatResAverageRtt':h3cNqaStatResAverageRtt,'h3cNqaStatResProbeResponses':h3cNqaStatResProbeResponses,'h3cNqaStatResSentProbes':h3cNqaStatResSentProbes,'h3cNqaStatResRttSumOfSquares':h3cNqaStatResRttSumOfSquares,'h3cNqaStatResStartTime':h3cNqaStatResStartTime,'h3cNqaStatResInterval':h3cNqaStatResInterval,'h3cNqaStatResRttNumDisconnects':h3cNqaStatResRttNumDisconnects,'h3cNqaStatResRttTimeouts':h3cNqaStatResRttTimeouts,'h3cNqaStatResRttBusies':h3cNqaStatResRttBusies,'h3cNqaStatResRttNoConnections':h3cNqaStatResRttNoConnections,'h3cNqaStatResRttDrops':h3cNqaStatResRttDrops,'h3cNqaStatResRttSequenceErrors':h3cNqaStatResRttSequenceErrors,'h3cNqaStatResRttErrors':h3cNqaStatResRttErrors,'h3cNqaStatResLostPacketRatio':h3cNqaStatResLostPacketRatio,'h3cNqaStatResPacketLateArrival':h3cNqaStatResPacketLateArrival,'h3cNqaStatResRttSum':h3cNqaStatResRttSum,'h3cNqaStatResNumOfDelaySD':h3cNqaStatResNumOfDelaySD,'h3cNqaStatResMinDelaySD':h3cNqaStatResMinDelaySD,'h3cNqaStatResMaxDelaySD':h3cNqaStatResMaxDelaySD,'h3cNqaStatResSumDelaySD':h3cNqaStatResSumDelaySD,'h3cNqaStatResSum2DelaySD':h3cNqaStatResSum2DelaySD,'h3cNqaStatResNumOfDelayDS':h3cNqaStatResNumOfDelayDS,'h3cNqaStatResMinDelayDS':h3cNqaStatResMinDelayDS,'h3cNqaStatResMaxDelayDS':h3cNqaStatResMaxDelayDS,'h3cNqaStatResSumDelayDS':h3cNqaStatResSumDelayDS,'h3cNqaStatResSum2DelayDS':h3cNqaStatResSum2DelayDS,'h3cNqaGroupStatsJitterTable':h3cNqaGroupStatsJitterTable,'h3cNqaGroupStatsJitterEntry':h3cNqaGroupStatsJitterEntry,_l:h3cNqaStatJitterIndex,'h3cNqaStatJitterMinOfPosSD':h3cNqaStatJitterMinOfPosSD,'h3cNqaStatJitterMaxOfPosSD':h3cNqaStatJitterMaxOfPosSD,'h3cNqaStatJitterNumOfPosSD':h3cNqaStatJitterNumOfPosSD,'h3cNqaStatJitterSumOfPosSD':h3cNqaStatJitterSumOfPosSD,'h3cNqaStatJitterSumOfSquarePosSD':h3cNqaStatJitterSumOfSquarePosSD,'h3cNqaStatJitterMinOfNegSD':h3cNqaStatJitterMinOfNegSD,'h3cNqaStatJitterMaxOfNegSD':h3cNqaStatJitterMaxOfNegSD,'h3cNqaStatJitterNumOfNegSD':h3cNqaStatJitterNumOfNegSD,'h3cNqaStatJitterSumOfNegSD':h3cNqaStatJitterSumOfNegSD,'h3cNqaStatJitterSumOfSquareNegSD':h3cNqaStatJitterSumOfSquareNegSD,'h3cNqaStatJitterMinOfPosDS':h3cNqaStatJitterMinOfPosDS,'h3cNqaStatJitterMaxOfPosDS':h3cNqaStatJitterMaxOfPosDS,'h3cNqaStatJitterNumOfPosDS':h3cNqaStatJitterNumOfPosDS,'h3cNqaStatJitterSumOfPosDS':h3cNqaStatJitterSumOfPosDS,'h3cNqaStatJitterSumOfSquarePosDS':h3cNqaStatJitterSumOfSquarePosDS,'h3cNqaStatJitterMinOfNegDS':h3cNqaStatJitterMinOfNegDS,'h3cNqaStatJitterMaxOfNegDS':h3cNqaStatJitterMaxOfNegDS,'h3cNqaStatJitterNumOfNegDS':h3cNqaStatJitterNumOfNegDS,'h3cNqaStatJitterSumOfNegDS':h3cNqaStatJitterSumOfNegDS,'h3cNqaStatJitterSumOfSquareNegDS':h3cNqaStatJitterSumOfSquareNegDS,'h3cNqaStatJitterPacketLossSD':h3cNqaStatJitterPacketLossSD,'h3cNqaStatJitterPacketLossDS':h3cNqaStatJitterPacketLossDS,'h3cNqaStatJitterAvePosSD':h3cNqaStatJitterAvePosSD,'h3cNqaStatJitterAveNegSD':h3cNqaStatJitterAveNegSD,'h3cNqaStatJitterAvePosDS':h3cNqaStatJitterAvePosDS,'h3cNqaStatJitterAveNegDS':h3cNqaStatJitterAveNegDS,'h3cNqaStatJitterPktLossUnknown':h3cNqaStatJitterPktLossUnknown,'h3cNqaStatJitterMaxOfICPIF':h3cNqaStatJitterMaxOfICPIF,'h3cNqaStatJitterMinOfICPIF':h3cNqaStatJitterMinOfICPIF,'h3cNqaStatJitterMaxOfMOS':h3cNqaStatJitterMaxOfMOS,'h3cNqaStatJitterMinOfMOS':h3cNqaStatJitterMinOfMOS,'h3cNqaStatJitterAveSD':h3cNqaStatJitterAveSD,'h3cNqaStatJitterAveDS':h3cNqaStatJitterAveDS,'h3cNqaReactionTable':h3cNqaReactionTable,'h3cNqaReactionEntry':h3cNqaReactionEntry,_J:h3cNqaReactOwnerIndex,_K:h3cNqaReactTestName,_L:h3cNqaReactItemIndex,'h3cNqaReactCheckedElement':h3cNqaReactCheckedElement,'h3cNqaReactThresholdUpperLimit':h3cNqaReactThresholdUpperLimit,'h3cNqaReactThresholdLowerLimit':h3cNqaReactThresholdLowerLimit,_R:h3cNqaReactThresholdType,'h3cNqaReactThresholdConsecNum':h3cNqaReactThresholdConsecNum,'h3cNqaReactThresholdAccumNum':h3cNqaReactThresholdAccumNum,'h3cNqaReactActionType':h3cNqaReactActionType,_Q:h3cNqaReactCurrentStatus,'h3cNqaReactRowStatus':h3cNqaReactRowStatus,'h3cNqaReactCheckedNum':h3cNqaReactCheckedNum,'h3cNqaReactThresholdNum':h3cNqaReactThresholdNum,'h3cNqaStatisticsReactionTable':h3cNqaStatisticsReactionTable,'h3cNqaStatisticsReactionEntry':h3cNqaStatisticsReactionEntry,_n:h3cNqaStatReactOwnerIndex,_o:h3cNqaStatReactTestName,_p:h3cNqaStatReactIndex,_q:h3cNqaStatReactItemIndex,'h3cNqaStatReactCheckedNum':h3cNqaStatReactCheckedNum,'h3cNqaStatReactThresholdNum':h3cNqaStatReactThresholdNum,'h3cNqaTcpServerExtendTable':h3cNqaTcpServerExtendTable,'h3cNqaTcpServerExtendEntry':h3cNqaTcpServerExtendEntry,_r:h3cNqaTcpServerExtIpAddress,_s:h3cNqaTcpServerExtPort,_t:h3cNqaTcpServerExtVPNType,_u:h3cNqaTcpServerExtVPNInstance,'h3cNqaTcpServerExtDSField':h3cNqaTcpServerExtDSField,'h3cNqaTcpServerExtRowStatus':h3cNqaTcpServerExtRowStatus,'h3cNqaUdpServerExtendTable':h3cNqaUdpServerExtendTable,'h3cNqaUdpServerExtendEntry':h3cNqaUdpServerExtendEntry,_v:h3cNqaUdpServerExtIpAddress,_w:h3cNqaUdpServerExtPort,_x:h3cNqaUdpServerExtVPNType,_y:h3cNqaUdpServerExtVPNInstance,'h3cNqaUdpServerExtDSField':h3cNqaUdpServerExtDSField,'h3cNqaUdpServerExtRowStatus':h3cNqaUdpServerExtRowStatus,'h3cNqaImplementationTypeDomains':h3cNqaImplementationTypeDomains,'h3cNqaUdpEcho':h3cNqaUdpEcho,'h3cNqaTcpconnect':h3cNqaTcpconnect,'h3cNqajitter':h3cNqajitter,'h3cNqaHttp':h3cNqaHttp,'h3cNqadlsw':h3cNqadlsw,'h3cNqadhcp':h3cNqadhcp,'h3cNqaftp':h3cNqaftp,'h3cNqaNotifications':h3cNqaNotifications,'h3cNqaProbeTimeOverThreshold':h3cNqaProbeTimeOverThreshold,'h3cNqaJitterRTTOverThreshold':h3cNqaJitterRTTOverThreshold,'h3cNqaProbeFailure':h3cNqaProbeFailure,'h3cNqaJitterPacketLoss':h3cNqaJitterPacketLoss,'h3cNqaJitterSDOverThreshold':h3cNqaJitterSDOverThreshold,'h3cNqaJitterDSOverThreshold':h3cNqaJitterDSOverThreshold,'h3cNqaICPIFOverThreshold':h3cNqaICPIFOverThreshold,'h3cNqaMOSOverThreshold':h3cNqaMOSOverThreshold})