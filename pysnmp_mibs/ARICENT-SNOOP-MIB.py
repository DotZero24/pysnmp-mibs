_AO='fsSnoopTrapHwErrType'
_AN='fsSnoopTrapObjectsEntry'
_AM='fsXSnoopRtrPortEntry'
_AL='fsSnoopVlanFilterXEntry'
_AK='fsSnoopRtrPortInetAddressType'
_AJ='fsSnoopRtrPortVlanId'
_AI='fsSnoopRtrPortIndex'
_AH='fsSnoopEnhPortInetAddressType'
_AG='fsSnoopEnhPortInnerVlanId'
_AF='fsSnoopEnhPortIndex'
_AE='normalleave'
_AD='fastleave'
_AC='explicithosttrack'
_AB='fsSnoopPortInetAddressType'
_AA='fsSnoopPortIndex'
_A9='fsSnoopStatsInetAddressType'
_A8='fsSnoopStatsVlanId'
_A7='fsSnoopStatsInstId'
_A6='fsSnoopVlanStaticMcastGrpGroupAddress'
_A5='fsSnoopVlanStaticMcastGrpSourceAddress'
_A4='fsSnoopVlanStaticMcastGrpAddressType'
_A3='fsSnoopVlanStaticMcastGrpVlanId'
_A2='fsSnoopVlanStaticMcastGrpInstId'
_A1='fsSnoopVlanIpFwdInnerVlanId'
_A0='fsSnoopVlanIpFwdGroupAddress'
_z='fsSnoopVlanIpFwdSourceAddress'
_y='fsSnoopVlanIpFwdInetAddressType'
_x='fsSnoopVlanIpFwdOuterVlanId'
_w='fsSnoopVlanIpFwdInstanceId'
_v='fsSnoopVlanMcastReceiverSourceAddress'
_u='fsSnoopVlanMcastReceiverHostAddress'
_t='fsSnoopVlanMcastReceiverPortIndex'
_s='seconds'
_r='fsSnoopVlanFilterInetAddressType'
_q='fsSnoopVlanFilterVlanId'
_p='fsSnoopVlanFilterInstId'
_o='fsSnoopVlanRouterInetAddressType'
_n='fsSnoopVlanRouterVlanId'
_m='fsSnoopVlanRouterInstId'
_l='fsSnoopVlanMcastIpFwdGroupAddress'
_k='fsSnoopVlanMcastIpFwdSourceAddress'
_j='fsSnoopVlanMcastIpFwdAddressType'
_i='fsSnoopVlanMcastIpFwdVlanId'
_h='fsSnoopVlanMcastIpFwdInstId'
_g='fsSnoopVlanMcastMacFwdGroupAddress'
_f='fsSnoopVlanMcastMacFwdInetAddressType'
_e='fsSnoopVlanMcastMacFwdVlanId'
_d='fsSnoopVlanMcastMacFwdInstId'
_c='fsSnoopInetAddressType'
_b='fsSnoopInstanceConfigInstId'
_a='disable'
_Z='enable'
_Y='fsSnoopInstanceGlobalInstId'
_X='channels'
_W='groups'
_V='fsSnoopVlanMcastGroupInnerVlanId'
_U='fsSnoopVlanMcastGroupAddress'
_T='fsSnoopVlanMcastGroupInetAddressType'
_S='fsSnoopVlanMcastGroupOuterVlanId'
_R='fsSnoopVlanMcastGroupInstanceId'
_Q='allports'
_P='none'
_O='v3'
_N='v2'
_M='v1'
_L='read-create'
_K='InetAddress'
_J='Unsigned32'
_I='deprecated'
_H='disabled'
_G='enabled'
_F='read-only'
_E='not-accessible'
_D='read-write'
_C='ARICENT-SNOOP-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_K,'InetAddressType')
PortList,VlanIndex=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fssnoop=ModuleIdentity((1,3,6,1,4,1,2076,105))
if mibBuilder.loadTexts:fssnoop.setRevisions(('2012-09-05 00:00',))
class InnerVlanIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_FsSnoopSystem_ObjectIdentity=ObjectIdentity
fsSnoopSystem=_FsSnoopSystem_ObjectIdentity((1,3,6,1,4,1,2076,105,1))
_FsSnoopInst_ObjectIdentity=ObjectIdentity
fsSnoopInst=_FsSnoopInst_ObjectIdentity((1,3,6,1,4,1,2076,105,2))
_FsSnoopInstanceGlobalTable_Object=MibTable
fsSnoopInstanceGlobalTable=_FsSnoopInstanceGlobalTable_Object((1,3,6,1,4,1,2076,105,2,1))
if mibBuilder.loadTexts:fsSnoopInstanceGlobalTable.setStatus(_A)
_FsSnoopInstanceGlobalEntry_Object=MibTableRow
fsSnoopInstanceGlobalEntry=_FsSnoopInstanceGlobalEntry_Object((1,3,6,1,4,1,2076,105,2,1,1))
fsSnoopInstanceGlobalEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:fsSnoopInstanceGlobalEntry.setStatus(_A)
class _FsSnoopInstanceGlobalInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsSnoopInstanceGlobalInstId_Type.__name__=_B
_FsSnoopInstanceGlobalInstId_Object=MibTableColumn
fsSnoopInstanceGlobalInstId=_FsSnoopInstanceGlobalInstId_Object((1,3,6,1,4,1,2076,105,2,1,1,1),_FsSnoopInstanceGlobalInstId_Type())
fsSnoopInstanceGlobalInstId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopInstanceGlobalInstId.setStatus(_A)
class _FsSnoopInstanceGlobalMcastFwdMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipbased',1),('macbased',2)))
_FsSnoopInstanceGlobalMcastFwdMode_Type.__name__=_B
_FsSnoopInstanceGlobalMcastFwdMode_Object=MibTableColumn
fsSnoopInstanceGlobalMcastFwdMode=_FsSnoopInstanceGlobalMcastFwdMode_Object((1,3,6,1,4,1,2076,105,2,1,1,2),_FsSnoopInstanceGlobalMcastFwdMode_Type())
fsSnoopInstanceGlobalMcastFwdMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopInstanceGlobalMcastFwdMode.setStatus(_A)
class _FsSnoopInstanceGlobalSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsSnoopInstanceGlobalSystemControl_Type.__name__=_B
_FsSnoopInstanceGlobalSystemControl_Object=MibTableColumn
fsSnoopInstanceGlobalSystemControl=_FsSnoopInstanceGlobalSystemControl_Object((1,3,6,1,4,1,2076,105,2,1,1,3),_FsSnoopInstanceGlobalSystemControl_Type())
fsSnoopInstanceGlobalSystemControl.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopInstanceGlobalSystemControl.setStatus(_A)
class _FsSnoopInstanceGlobalLeaveConfigLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlanbased',1),('portbased',2)))
_FsSnoopInstanceGlobalLeaveConfigLevel_Type.__name__=_B
_FsSnoopInstanceGlobalLeaveConfigLevel_Object=MibTableColumn
fsSnoopInstanceGlobalLeaveConfigLevel=_FsSnoopInstanceGlobalLeaveConfigLevel_Object((1,3,6,1,4,1,2076,105,2,1,1,4),_FsSnoopInstanceGlobalLeaveConfigLevel_Type())
fsSnoopInstanceGlobalLeaveConfigLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopInstanceGlobalLeaveConfigLevel.setStatus(_A)
class _FsSnoopInstanceGlobalEnhancedMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_FsSnoopInstanceGlobalEnhancedMode_Type.__name__=_B
_FsSnoopInstanceGlobalEnhancedMode_Object=MibTableColumn
fsSnoopInstanceGlobalEnhancedMode=_FsSnoopInstanceGlobalEnhancedMode_Object((1,3,6,1,4,1,2076,105,2,1,1,5),_FsSnoopInstanceGlobalEnhancedMode_Type())
fsSnoopInstanceGlobalEnhancedMode.setMaxAccess(_L)
if mibBuilder.loadTexts:fsSnoopInstanceGlobalEnhancedMode.setStatus(_A)
class _FsSnoopInstanceGlobalReportProcessConfigLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonrouterports',1),(_Q,2)))
_FsSnoopInstanceGlobalReportProcessConfigLevel_Type.__name__=_B
_FsSnoopInstanceGlobalReportProcessConfigLevel_Object=MibTableColumn
fsSnoopInstanceGlobalReportProcessConfigLevel=_FsSnoopInstanceGlobalReportProcessConfigLevel_Object((1,3,6,1,4,1,2076,105,2,1,1,6),_FsSnoopInstanceGlobalReportProcessConfigLevel_Type())
fsSnoopInstanceGlobalReportProcessConfigLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopInstanceGlobalReportProcessConfigLevel.setStatus(_A)
class _FsSnoopInstanceGlobalSparseMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_FsSnoopInstanceGlobalSparseMode_Type.__name__=_B
_FsSnoopInstanceGlobalSparseMode_Object=MibTableColumn
fsSnoopInstanceGlobalSparseMode=_FsSnoopInstanceGlobalSparseMode_Object((1,3,6,1,4,1,2076,105,2,1,1,7),_FsSnoopInstanceGlobalSparseMode_Type())
fsSnoopInstanceGlobalSparseMode.setMaxAccess(_L)
if mibBuilder.loadTexts:fsSnoopInstanceGlobalSparseMode.setStatus(_A)
_FsSnoopInstanceConfigTable_Object=MibTable
fsSnoopInstanceConfigTable=_FsSnoopInstanceConfigTable_Object((1,3,6,1,4,1,2076,105,2,2))
if mibBuilder.loadTexts:fsSnoopInstanceConfigTable.setStatus(_A)
_FsSnoopInstanceConfigEntry_Object=MibTableRow
fsSnoopInstanceConfigEntry=_FsSnoopInstanceConfigEntry_Object((1,3,6,1,4,1,2076,105,2,2,1))
fsSnoopInstanceConfigEntry.setIndexNames((0,_C,_b),(0,_C,_c))
if mibBuilder.loadTexts:fsSnoopInstanceConfigEntry.setStatus(_A)
class _FsSnoopInstanceConfigInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsSnoopInstanceConfigInstId_Type.__name__=_B
_FsSnoopInstanceConfigInstId_Object=MibTableColumn
fsSnoopInstanceConfigInstId=_FsSnoopInstanceConfigInstId_Object((1,3,6,1,4,1,2076,105,2,2,1,1),_FsSnoopInstanceConfigInstId_Type())
fsSnoopInstanceConfigInstId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopInstanceConfigInstId.setStatus(_A)
_FsSnoopInetAddressType_Type=InetAddressType
_FsSnoopInetAddressType_Object=MibTableColumn
fsSnoopInetAddressType=_FsSnoopInetAddressType_Object((1,3,6,1,4,1,2076,105,2,2,1,2),_FsSnoopInetAddressType_Type())
fsSnoopInetAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopInetAddressType.setStatus(_A)
class _FsSnoopStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSnoopStatus_Type.__name__=_B
_FsSnoopStatus_Object=MibTableColumn
fsSnoopStatus=_FsSnoopStatus_Object((1,3,6,1,4,1,2076,105,2,2,1,3),_FsSnoopStatus_Type())
fsSnoopStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopStatus.setStatus(_A)
class _FsSnoopProxyReportingStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSnoopProxyReportingStatus_Type.__name__=_B
_FsSnoopProxyReportingStatus_Object=MibTableColumn
fsSnoopProxyReportingStatus=_FsSnoopProxyReportingStatus_Object((1,3,6,1,4,1,2076,105,2,2,1,4),_FsSnoopProxyReportingStatus_Type())
fsSnoopProxyReportingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopProxyReportingStatus.setStatus(_A)
class _FsSnoopRouterPortPurgeInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_FsSnoopRouterPortPurgeInterval_Type.__name__=_B
_FsSnoopRouterPortPurgeInterval_Object=MibTableColumn
fsSnoopRouterPortPurgeInterval=_FsSnoopRouterPortPurgeInterval_Object((1,3,6,1,4,1,2076,105,2,2,1,5),_FsSnoopRouterPortPurgeInterval_Type())
fsSnoopRouterPortPurgeInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopRouterPortPurgeInterval.setStatus(_I)
class _FsSnoopPortPurgeInterval_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(130,1225))
_FsSnoopPortPurgeInterval_Type.__name__=_B
_FsSnoopPortPurgeInterval_Object=MibTableColumn
fsSnoopPortPurgeInterval=_FsSnoopPortPurgeInterval_Object((1,3,6,1,4,1,2076,105,2,2,1,6),_FsSnoopPortPurgeInterval_Type())
fsSnoopPortPurgeInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopPortPurgeInterval.setStatus(_I)
class _FsSnoopReportForwardInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_FsSnoopReportForwardInterval_Type.__name__=_B
_FsSnoopReportForwardInterval_Object=MibTableColumn
fsSnoopReportForwardInterval=_FsSnoopReportForwardInterval_Object((1,3,6,1,4,1,2076,105,2,2,1,7),_FsSnoopReportForwardInterval_Type())
fsSnoopReportForwardInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopReportForwardInterval.setStatus(_A)
class _FsSnoopRetryCount_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_FsSnoopRetryCount_Type.__name__=_B
_FsSnoopRetryCount_Object=MibTableColumn
fsSnoopRetryCount=_FsSnoopRetryCount_Object((1,3,6,1,4,1,2076,105,2,2,1,8),_FsSnoopRetryCount_Type())
fsSnoopRetryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopRetryCount.setStatus(_A)
class _FsSnoopGrpQueryInterval_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,5))
_FsSnoopGrpQueryInterval_Type.__name__=_B
_FsSnoopGrpQueryInterval_Object=MibTableColumn
fsSnoopGrpQueryInterval=_FsSnoopGrpQueryInterval_Object((1,3,6,1,4,1,2076,105,2,2,1,9),_FsSnoopGrpQueryInterval_Type())
fsSnoopGrpQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopGrpQueryInterval.setStatus(_A)
class _FsSnoopReportFwdOnAllPorts_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('rtrports',2),('nonedgeports',3)))
_FsSnoopReportFwdOnAllPorts_Type.__name__=_B
_FsSnoopReportFwdOnAllPorts_Object=MibTableColumn
fsSnoopReportFwdOnAllPorts=_FsSnoopReportFwdOnAllPorts_Object((1,3,6,1,4,1,2076,105,2,2,1,10),_FsSnoopReportFwdOnAllPorts_Type())
fsSnoopReportFwdOnAllPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopReportFwdOnAllPorts.setStatus(_A)
_FsSnoopTraceOption_Type=Integer32
_FsSnoopTraceOption_Object=MibTableColumn
fsSnoopTraceOption=_FsSnoopTraceOption_Object((1,3,6,1,4,1,2076,105,2,2,1,11),_FsSnoopTraceOption_Type())
fsSnoopTraceOption.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopTraceOption.setStatus(_A)
class _FsSnoopOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSnoopOperStatus_Type.__name__=_B
_FsSnoopOperStatus_Object=MibTableColumn
fsSnoopOperStatus=_FsSnoopOperStatus_Object((1,3,6,1,4,1,2076,105,2,2,1,12),_FsSnoopOperStatus_Type())
fsSnoopOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopOperStatus.setStatus(_A)
class _FsSnoopSendQueryOnTopoChange_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSnoopSendQueryOnTopoChange_Type.__name__=_B
_FsSnoopSendQueryOnTopoChange_Object=MibTableColumn
fsSnoopSendQueryOnTopoChange=_FsSnoopSendQueryOnTopoChange_Object((1,3,6,1,4,1,2076,105,2,2,1,13),_FsSnoopSendQueryOnTopoChange_Type())
fsSnoopSendQueryOnTopoChange.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopSendQueryOnTopoChange.setStatus(_A)
class _FsSnoopSendLeaveOnTopoChange_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSnoopSendLeaveOnTopoChange_Type.__name__=_B
_FsSnoopSendLeaveOnTopoChange_Object=MibTableColumn
fsSnoopSendLeaveOnTopoChange=_FsSnoopSendLeaveOnTopoChange_Object((1,3,6,1,4,1,2076,105,2,2,1,14),_FsSnoopSendLeaveOnTopoChange_Type())
fsSnoopSendLeaveOnTopoChange.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopSendLeaveOnTopoChange.setStatus(_A)
class _FsSnoopFilterStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSnoopFilterStatus_Type.__name__=_B
_FsSnoopFilterStatus_Object=MibTableColumn
fsSnoopFilterStatus=_FsSnoopFilterStatus_Object((1,3,6,1,4,1,2076,105,2,2,1,15),_FsSnoopFilterStatus_Type())
fsSnoopFilterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopFilterStatus.setStatus(_A)
class _FsSnoopMulticastVlanStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSnoopMulticastVlanStatus_Type.__name__=_B
_FsSnoopMulticastVlanStatus_Object=MibTableColumn
fsSnoopMulticastVlanStatus=_FsSnoopMulticastVlanStatus_Object((1,3,6,1,4,1,2076,105,2,2,1,16),_FsSnoopMulticastVlanStatus_Type())
fsSnoopMulticastVlanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopMulticastVlanStatus.setStatus(_A)
class _FsSnoopProxyStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSnoopProxyStatus_Type.__name__=_B
_FsSnoopProxyStatus_Object=MibTableColumn
fsSnoopProxyStatus=_FsSnoopProxyStatus_Object((1,3,6,1,4,1,2076,105,2,2,1,17),_FsSnoopProxyStatus_Type())
fsSnoopProxyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopProxyStatus.setStatus(_A)
class _FsSnoopQueryFwdOnAllPorts_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('nonrtrports',2)))
_FsSnoopQueryFwdOnAllPorts_Type.__name__=_B
_FsSnoopQueryFwdOnAllPorts_Object=MibTableColumn
fsSnoopQueryFwdOnAllPorts=_FsSnoopQueryFwdOnAllPorts_Object((1,3,6,1,4,1,2076,105,2,2,1,18),_FsSnoopQueryFwdOnAllPorts_Type())
fsSnoopQueryFwdOnAllPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopQueryFwdOnAllPorts.setStatus(_A)
_FsSnoopFwdGroupsCnt_Type=Integer32
_FsSnoopFwdGroupsCnt_Object=MibTableColumn
fsSnoopFwdGroupsCnt=_FsSnoopFwdGroupsCnt_Object((1,3,6,1,4,1,2076,105,2,2,1,19),_FsSnoopFwdGroupsCnt_Type())
fsSnoopFwdGroupsCnt.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopFwdGroupsCnt.setStatus(_A)
_FsSnoopDebugOption_Type=Integer32
_FsSnoopDebugOption_Object=MibTableColumn
fsSnoopDebugOption=_FsSnoopDebugOption_Object((1,3,6,1,4,1,2076,105,2,2,1,20),_FsSnoopDebugOption_Type())
fsSnoopDebugOption.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopDebugOption.setStatus(_A)
_FsSnoopVlan_ObjectIdentity=ObjectIdentity
fsSnoopVlan=_FsSnoopVlan_ObjectIdentity((1,3,6,1,4,1,2076,105,3))
_FsSnoopVlanMcastMacFwdTable_Object=MibTable
fsSnoopVlanMcastMacFwdTable=_FsSnoopVlanMcastMacFwdTable_Object((1,3,6,1,4,1,2076,105,3,1))
if mibBuilder.loadTexts:fsSnoopVlanMcastMacFwdTable.setStatus(_A)
_FsSnoopVlanMcastMacFwdEntry_Object=MibTableRow
fsSnoopVlanMcastMacFwdEntry=_FsSnoopVlanMcastMacFwdEntry_Object((1,3,6,1,4,1,2076,105,3,1,1))
fsSnoopVlanMcastMacFwdEntry.setIndexNames((0,_C,_d),(0,_C,_e),(0,_C,_f),(0,_C,_g))
if mibBuilder.loadTexts:fsSnoopVlanMcastMacFwdEntry.setStatus(_A)
class _FsSnoopVlanMcastMacFwdInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsSnoopVlanMcastMacFwdInstId_Type.__name__=_B
_FsSnoopVlanMcastMacFwdInstId_Object=MibTableColumn
fsSnoopVlanMcastMacFwdInstId=_FsSnoopVlanMcastMacFwdInstId_Object((1,3,6,1,4,1,2076,105,3,1,1,1),_FsSnoopVlanMcastMacFwdInstId_Type())
fsSnoopVlanMcastMacFwdInstId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastMacFwdInstId.setStatus(_A)
class _FsSnoopVlanMcastMacFwdVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsSnoopVlanMcastMacFwdVlanId_Type.__name__=_B
_FsSnoopVlanMcastMacFwdVlanId_Object=MibTableColumn
fsSnoopVlanMcastMacFwdVlanId=_FsSnoopVlanMcastMacFwdVlanId_Object((1,3,6,1,4,1,2076,105,3,1,1,2),_FsSnoopVlanMcastMacFwdVlanId_Type())
fsSnoopVlanMcastMacFwdVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastMacFwdVlanId.setStatus(_A)
_FsSnoopVlanMcastMacFwdInetAddressType_Type=InetAddressType
_FsSnoopVlanMcastMacFwdInetAddressType_Object=MibTableColumn
fsSnoopVlanMcastMacFwdInetAddressType=_FsSnoopVlanMcastMacFwdInetAddressType_Object((1,3,6,1,4,1,2076,105,3,1,1,3),_FsSnoopVlanMcastMacFwdInetAddressType_Type())
fsSnoopVlanMcastMacFwdInetAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastMacFwdInetAddressType.setStatus(_A)
_FsSnoopVlanMcastMacFwdGroupAddress_Type=MacAddress
_FsSnoopVlanMcastMacFwdGroupAddress_Object=MibTableColumn
fsSnoopVlanMcastMacFwdGroupAddress=_FsSnoopVlanMcastMacFwdGroupAddress_Object((1,3,6,1,4,1,2076,105,3,1,1,4),_FsSnoopVlanMcastMacFwdGroupAddress_Type())
fsSnoopVlanMcastMacFwdGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastMacFwdGroupAddress.setStatus(_A)
_FsSnoopVlanMcastMacFwdPortList_Type=PortList
_FsSnoopVlanMcastMacFwdPortList_Object=MibTableColumn
fsSnoopVlanMcastMacFwdPortList=_FsSnoopVlanMcastMacFwdPortList_Object((1,3,6,1,4,1,2076,105,3,1,1,5),_FsSnoopVlanMcastMacFwdPortList_Type())
fsSnoopVlanMcastMacFwdPortList.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanMcastMacFwdPortList.setStatus(_A)
_FsSnoopVlanMcastMacFwdLocalPortList_Type=PortList
_FsSnoopVlanMcastMacFwdLocalPortList_Object=MibTableColumn
fsSnoopVlanMcastMacFwdLocalPortList=_FsSnoopVlanMcastMacFwdLocalPortList_Object((1,3,6,1,4,1,2076,105,3,1,1,6),_FsSnoopVlanMcastMacFwdLocalPortList_Type())
fsSnoopVlanMcastMacFwdLocalPortList.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanMcastMacFwdLocalPortList.setStatus(_A)
_FsSnoopVlanMcastMacFwdEntryFlag_Type=Integer32
_FsSnoopVlanMcastMacFwdEntryFlag_Object=MibTableColumn
fsSnoopVlanMcastMacFwdEntryFlag=_FsSnoopVlanMcastMacFwdEntryFlag_Object((1,3,6,1,4,1,2076,105,3,1,1,7),_FsSnoopVlanMcastMacFwdEntryFlag_Type())
fsSnoopVlanMcastMacFwdEntryFlag.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanMcastMacFwdEntryFlag.setStatus(_A)
_FsSnoopVlanMcastIpFwdTable_Object=MibTable
fsSnoopVlanMcastIpFwdTable=_FsSnoopVlanMcastIpFwdTable_Object((1,3,6,1,4,1,2076,105,3,2))
if mibBuilder.loadTexts:fsSnoopVlanMcastIpFwdTable.setStatus(_I)
_FsSnoopVlanMcastIpFwdEntry_Object=MibTableRow
fsSnoopVlanMcastIpFwdEntry=_FsSnoopVlanMcastIpFwdEntry_Object((1,3,6,1,4,1,2076,105,3,2,1))
fsSnoopVlanMcastIpFwdEntry.setIndexNames((0,_C,_h),(0,_C,_i),(0,_C,_j),(0,_C,_k),(0,_C,_l))
if mibBuilder.loadTexts:fsSnoopVlanMcastIpFwdEntry.setStatus(_I)
class _FsSnoopVlanMcastIpFwdInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsSnoopVlanMcastIpFwdInstId_Type.__name__=_B
_FsSnoopVlanMcastIpFwdInstId_Object=MibTableColumn
fsSnoopVlanMcastIpFwdInstId=_FsSnoopVlanMcastIpFwdInstId_Object((1,3,6,1,4,1,2076,105,3,2,1,1),_FsSnoopVlanMcastIpFwdInstId_Type())
fsSnoopVlanMcastIpFwdInstId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastIpFwdInstId.setStatus(_I)
class _FsSnoopVlanMcastIpFwdVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsSnoopVlanMcastIpFwdVlanId_Type.__name__=_B
_FsSnoopVlanMcastIpFwdVlanId_Object=MibTableColumn
fsSnoopVlanMcastIpFwdVlanId=_FsSnoopVlanMcastIpFwdVlanId_Object((1,3,6,1,4,1,2076,105,3,2,1,2),_FsSnoopVlanMcastIpFwdVlanId_Type())
fsSnoopVlanMcastIpFwdVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastIpFwdVlanId.setStatus(_I)
_FsSnoopVlanMcastIpFwdAddressType_Type=InetAddressType
_FsSnoopVlanMcastIpFwdAddressType_Object=MibTableColumn
fsSnoopVlanMcastIpFwdAddressType=_FsSnoopVlanMcastIpFwdAddressType_Object((1,3,6,1,4,1,2076,105,3,2,1,3),_FsSnoopVlanMcastIpFwdAddressType_Type())
fsSnoopVlanMcastIpFwdAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastIpFwdAddressType.setStatus(_I)
class _FsSnoopVlanMcastIpFwdSourceAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsSnoopVlanMcastIpFwdSourceAddress_Type.__name__=_K
_FsSnoopVlanMcastIpFwdSourceAddress_Object=MibTableColumn
fsSnoopVlanMcastIpFwdSourceAddress=_FsSnoopVlanMcastIpFwdSourceAddress_Object((1,3,6,1,4,1,2076,105,3,2,1,4),_FsSnoopVlanMcastIpFwdSourceAddress_Type())
fsSnoopVlanMcastIpFwdSourceAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastIpFwdSourceAddress.setStatus(_I)
class _FsSnoopVlanMcastIpFwdGroupAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsSnoopVlanMcastIpFwdGroupAddress_Type.__name__=_K
_FsSnoopVlanMcastIpFwdGroupAddress_Object=MibTableColumn
fsSnoopVlanMcastIpFwdGroupAddress=_FsSnoopVlanMcastIpFwdGroupAddress_Object((1,3,6,1,4,1,2076,105,3,2,1,5),_FsSnoopVlanMcastIpFwdGroupAddress_Type())
fsSnoopVlanMcastIpFwdGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastIpFwdGroupAddress.setStatus(_I)
_FsSnoopVlanMcastIpFwdPortList_Type=PortList
_FsSnoopVlanMcastIpFwdPortList_Object=MibTableColumn
fsSnoopVlanMcastIpFwdPortList=_FsSnoopVlanMcastIpFwdPortList_Object((1,3,6,1,4,1,2076,105,3,2,1,6),_FsSnoopVlanMcastIpFwdPortList_Type())
fsSnoopVlanMcastIpFwdPortList.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanMcastIpFwdPortList.setStatus(_I)
_FsSnoopVlanMcastIpFwdEntryFlag_Type=Integer32
_FsSnoopVlanMcastIpFwdEntryFlag_Object=MibTableColumn
fsSnoopVlanMcastIpFwdEntryFlag=_FsSnoopVlanMcastIpFwdEntryFlag_Object((1,3,6,1,4,1,2076,105,3,2,1,7),_FsSnoopVlanMcastIpFwdEntryFlag_Type())
fsSnoopVlanMcastIpFwdEntryFlag.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanMcastIpFwdEntryFlag.setStatus(_A)
_FsSnoopVlanRouterTable_Object=MibTable
fsSnoopVlanRouterTable=_FsSnoopVlanRouterTable_Object((1,3,6,1,4,1,2076,105,3,3))
if mibBuilder.loadTexts:fsSnoopVlanRouterTable.setStatus(_A)
_FsSnoopVlanRouterEntry_Object=MibTableRow
fsSnoopVlanRouterEntry=_FsSnoopVlanRouterEntry_Object((1,3,6,1,4,1,2076,105,3,3,1))
fsSnoopVlanRouterEntry.setIndexNames((0,_C,_m),(0,_C,_n),(0,_C,_o))
if mibBuilder.loadTexts:fsSnoopVlanRouterEntry.setStatus(_A)
class _FsSnoopVlanRouterInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsSnoopVlanRouterInstId_Type.__name__=_B
_FsSnoopVlanRouterInstId_Object=MibTableColumn
fsSnoopVlanRouterInstId=_FsSnoopVlanRouterInstId_Object((1,3,6,1,4,1,2076,105,3,3,1,1),_FsSnoopVlanRouterInstId_Type())
fsSnoopVlanRouterInstId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanRouterInstId.setStatus(_A)
class _FsSnoopVlanRouterVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsSnoopVlanRouterVlanId_Type.__name__=_B
_FsSnoopVlanRouterVlanId_Object=MibTableColumn
fsSnoopVlanRouterVlanId=_FsSnoopVlanRouterVlanId_Object((1,3,6,1,4,1,2076,105,3,3,1,2),_FsSnoopVlanRouterVlanId_Type())
fsSnoopVlanRouterVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanRouterVlanId.setStatus(_A)
_FsSnoopVlanRouterInetAddressType_Type=InetAddressType
_FsSnoopVlanRouterInetAddressType_Object=MibTableColumn
fsSnoopVlanRouterInetAddressType=_FsSnoopVlanRouterInetAddressType_Object((1,3,6,1,4,1,2076,105,3,3,1,3),_FsSnoopVlanRouterInetAddressType_Type())
fsSnoopVlanRouterInetAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanRouterInetAddressType.setStatus(_A)
_FsSnoopVlanRouterPortList_Type=PortList
_FsSnoopVlanRouterPortList_Object=MibTableColumn
fsSnoopVlanRouterPortList=_FsSnoopVlanRouterPortList_Object((1,3,6,1,4,1,2076,105,3,3,1,4),_FsSnoopVlanRouterPortList_Type())
fsSnoopVlanRouterPortList.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanRouterPortList.setStatus(_A)
_FsSnoopVlanRouterLocalPortList_Type=PortList
_FsSnoopVlanRouterLocalPortList_Object=MibTableColumn
fsSnoopVlanRouterLocalPortList=_FsSnoopVlanRouterLocalPortList_Object((1,3,6,1,4,1,2076,105,3,3,1,5),_FsSnoopVlanRouterLocalPortList_Type())
fsSnoopVlanRouterLocalPortList.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanRouterLocalPortList.setStatus(_A)
_FsSnoopVlanFilterTable_Object=MibTable
fsSnoopVlanFilterTable=_FsSnoopVlanFilterTable_Object((1,3,6,1,4,1,2076,105,3,4))
if mibBuilder.loadTexts:fsSnoopVlanFilterTable.setStatus(_A)
_FsSnoopVlanFilterEntry_Object=MibTableRow
fsSnoopVlanFilterEntry=_FsSnoopVlanFilterEntry_Object((1,3,6,1,4,1,2076,105,3,4,1))
fsSnoopVlanFilterEntry.setIndexNames((0,_C,_p),(0,_C,_q),(0,_C,_r))
if mibBuilder.loadTexts:fsSnoopVlanFilterEntry.setStatus(_A)
class _FsSnoopVlanFilterInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsSnoopVlanFilterInstId_Type.__name__=_B
_FsSnoopVlanFilterInstId_Object=MibTableColumn
fsSnoopVlanFilterInstId=_FsSnoopVlanFilterInstId_Object((1,3,6,1,4,1,2076,105,3,4,1,1),_FsSnoopVlanFilterInstId_Type())
fsSnoopVlanFilterInstId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanFilterInstId.setStatus(_A)
class _FsSnoopVlanFilterVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsSnoopVlanFilterVlanId_Type.__name__=_B
_FsSnoopVlanFilterVlanId_Object=MibTableColumn
fsSnoopVlanFilterVlanId=_FsSnoopVlanFilterVlanId_Object((1,3,6,1,4,1,2076,105,3,4,1,2),_FsSnoopVlanFilterVlanId_Type())
fsSnoopVlanFilterVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanFilterVlanId.setStatus(_A)
_FsSnoopVlanFilterInetAddressType_Type=InetAddressType
_FsSnoopVlanFilterInetAddressType_Object=MibTableColumn
fsSnoopVlanFilterInetAddressType=_FsSnoopVlanFilterInetAddressType_Object((1,3,6,1,4,1,2076,105,3,4,1,3),_FsSnoopVlanFilterInetAddressType_Type())
fsSnoopVlanFilterInetAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanFilterInetAddressType.setStatus(_A)
class _FsSnoopVlanSnoopStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSnoopVlanSnoopStatus_Type.__name__=_B
_FsSnoopVlanSnoopStatus_Object=MibTableColumn
fsSnoopVlanSnoopStatus=_FsSnoopVlanSnoopStatus_Object((1,3,6,1,4,1,2076,105,3,4,1,4),_FsSnoopVlanSnoopStatus_Type())
fsSnoopVlanSnoopStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanSnoopStatus.setStatus(_A)
class _FsSnoopVlanOperatingVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_FsSnoopVlanOperatingVersion_Type.__name__=_B
_FsSnoopVlanOperatingVersion_Object=MibTableColumn
fsSnoopVlanOperatingVersion=_FsSnoopVlanOperatingVersion_Object((1,3,6,1,4,1,2076,105,3,4,1,5),_FsSnoopVlanOperatingVersion_Type())
fsSnoopVlanOperatingVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanOperatingVersion.setStatus(_I)
class _FsSnoopVlanCfgOperVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_FsSnoopVlanCfgOperVersion_Type.__name__=_B
_FsSnoopVlanCfgOperVersion_Object=MibTableColumn
fsSnoopVlanCfgOperVersion=_FsSnoopVlanCfgOperVersion_Object((1,3,6,1,4,1,2076,105,3,4,1,6),_FsSnoopVlanCfgOperVersion_Type())
fsSnoopVlanCfgOperVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanCfgOperVersion.setStatus(_I)
class _FsSnoopVlanFastLeave_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSnoopVlanFastLeave_Type.__name__=_B
_FsSnoopVlanFastLeave_Object=MibTableColumn
fsSnoopVlanFastLeave=_FsSnoopVlanFastLeave_Object((1,3,6,1,4,1,2076,105,3,4,1,7),_FsSnoopVlanFastLeave_Type())
fsSnoopVlanFastLeave.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanFastLeave.setStatus(_A)
class _FsSnoopVlanQuerier_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSnoopVlanQuerier_Type.__name__=_B
_FsSnoopVlanQuerier_Object=MibTableColumn
fsSnoopVlanQuerier=_FsSnoopVlanQuerier_Object((1,3,6,1,4,1,2076,105,3,4,1,8),_FsSnoopVlanQuerier_Type())
fsSnoopVlanQuerier.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanQuerier.setStatus(_A)
class _FsSnoopVlanCfgQuerier_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSnoopVlanCfgQuerier_Type.__name__=_B
_FsSnoopVlanCfgQuerier_Object=MibTableColumn
fsSnoopVlanCfgQuerier=_FsSnoopVlanCfgQuerier_Object((1,3,6,1,4,1,2076,105,3,4,1,9),_FsSnoopVlanCfgQuerier_Type())
fsSnoopVlanCfgQuerier.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanCfgQuerier.setStatus(_A)
class _FsSnoopVlanQueryInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_FsSnoopVlanQueryInterval_Type.__name__=_B
_FsSnoopVlanQueryInterval_Object=MibTableColumn
fsSnoopVlanQueryInterval=_FsSnoopVlanQueryInterval_Object((1,3,6,1,4,1,2076,105,3,4,1,10),_FsSnoopVlanQueryInterval_Type())
fsSnoopVlanQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanQueryInterval.setStatus(_A)
_FsSnoopVlanRtrPortList_Type=PortList
_FsSnoopVlanRtrPortList_Object=MibTableColumn
fsSnoopVlanRtrPortList=_FsSnoopVlanRtrPortList_Object((1,3,6,1,4,1,2076,105,3,4,1,11),_FsSnoopVlanRtrPortList_Type())
fsSnoopVlanRtrPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanRtrPortList.setStatus(_A)
_FsSnoopVlanRowStatus_Type=RowStatus
_FsSnoopVlanRowStatus_Object=MibTableColumn
fsSnoopVlanRowStatus=_FsSnoopVlanRowStatus_Object((1,3,6,1,4,1,2076,105,3,4,1,12),_FsSnoopVlanRowStatus_Type())
fsSnoopVlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanRowStatus.setStatus(_A)
class _FsSnoopVlanStartupQueryCount_Type(Integer32):defaultValue=2
_FsSnoopVlanStartupQueryCount_Type.__name__=_B
_FsSnoopVlanStartupQueryCount_Object=MibTableColumn
fsSnoopVlanStartupQueryCount=_FsSnoopVlanStartupQueryCount_Object((1,3,6,1,4,1,2076,105,3,4,1,13),_FsSnoopVlanStartupQueryCount_Type())
fsSnoopVlanStartupQueryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanStartupQueryCount.setStatus(_A)
class _FsSnoopVlanStartupQueryInterval_Type(Integer32):defaultValue=31;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,150))
_FsSnoopVlanStartupQueryInterval_Type.__name__=_B
_FsSnoopVlanStartupQueryInterval_Object=MibTableColumn
fsSnoopVlanStartupQueryInterval=_FsSnoopVlanStartupQueryInterval_Object((1,3,6,1,4,1,2076,105,3,4,1,14),_FsSnoopVlanStartupQueryInterval_Type())
fsSnoopVlanStartupQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanStartupQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:fsSnoopVlanStartupQueryInterval.setUnits(_s)
class _FsSnoopVlanOtherQuerierPresentInterval_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(120,1235))
_FsSnoopVlanOtherQuerierPresentInterval_Type.__name__=_B
_FsSnoopVlanOtherQuerierPresentInterval_Object=MibTableColumn
fsSnoopVlanOtherQuerierPresentInterval=_FsSnoopVlanOtherQuerierPresentInterval_Object((1,3,6,1,4,1,2076,105,3,4,1,15),_FsSnoopVlanOtherQuerierPresentInterval_Type())
fsSnoopVlanOtherQuerierPresentInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanOtherQuerierPresentInterval.setStatus(_A)
if mibBuilder.loadTexts:fsSnoopVlanOtherQuerierPresentInterval.setUnits(_s)
_FsSnoopVlanQuerierIpAddress_Type=IpAddress
_FsSnoopVlanQuerierIpAddress_Object=MibTableColumn
fsSnoopVlanQuerierIpAddress=_FsSnoopVlanQuerierIpAddress_Object((1,3,6,1,4,1,2076,105,3,4,1,16),_FsSnoopVlanQuerierIpAddress_Type())
fsSnoopVlanQuerierIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanQuerierIpAddress.setStatus(_A)
class _FsSnoopVlanQuerierIpFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsSnoopVlanQuerierIpFlag_Type.__name__=_B
_FsSnoopVlanQuerierIpFlag_Object=MibTableColumn
fsSnoopVlanQuerierIpFlag=_FsSnoopVlanQuerierIpFlag_Object((1,3,6,1,4,1,2076,105,3,4,1,17),_FsSnoopVlanQuerierIpFlag_Type())
fsSnoopVlanQuerierIpFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanQuerierIpFlag.setStatus(_A)
_FsSnoopVlanElectedQuerier_Type=IpAddress
_FsSnoopVlanElectedQuerier_Object=MibTableColumn
fsSnoopVlanElectedQuerier=_FsSnoopVlanElectedQuerier_Object((1,3,6,1,4,1,2076,105,3,4,1,18),_FsSnoopVlanElectedQuerier_Type())
fsSnoopVlanElectedQuerier.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanElectedQuerier.setStatus(_A)
_FsSnoopVlanMcastGroupTable_Object=MibTable
fsSnoopVlanMcastGroupTable=_FsSnoopVlanMcastGroupTable_Object((1,3,6,1,4,1,2076,105,3,5))
if mibBuilder.loadTexts:fsSnoopVlanMcastGroupTable.setStatus(_A)
_FsSnoopVlanMcastGroupEntry_Object=MibTableRow
fsSnoopVlanMcastGroupEntry=_FsSnoopVlanMcastGroupEntry_Object((1,3,6,1,4,1,2076,105,3,5,1))
fsSnoopVlanMcastGroupEntry.setIndexNames((0,_C,_R),(0,_C,_S),(0,_C,_T),(0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:fsSnoopVlanMcastGroupEntry.setStatus(_A)
class _FsSnoopVlanMcastGroupInstanceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsSnoopVlanMcastGroupInstanceId_Type.__name__=_B
_FsSnoopVlanMcastGroupInstanceId_Object=MibTableColumn
fsSnoopVlanMcastGroupInstanceId=_FsSnoopVlanMcastGroupInstanceId_Object((1,3,6,1,4,1,2076,105,3,5,1,1),_FsSnoopVlanMcastGroupInstanceId_Type())
fsSnoopVlanMcastGroupInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastGroupInstanceId.setStatus(_A)
_FsSnoopVlanMcastGroupOuterVlanId_Type=VlanIndex
_FsSnoopVlanMcastGroupOuterVlanId_Object=MibTableColumn
fsSnoopVlanMcastGroupOuterVlanId=_FsSnoopVlanMcastGroupOuterVlanId_Object((1,3,6,1,4,1,2076,105,3,5,1,2),_FsSnoopVlanMcastGroupOuterVlanId_Type())
fsSnoopVlanMcastGroupOuterVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastGroupOuterVlanId.setStatus(_A)
_FsSnoopVlanMcastGroupInetAddressType_Type=InetAddressType
_FsSnoopVlanMcastGroupInetAddressType_Object=MibTableColumn
fsSnoopVlanMcastGroupInetAddressType=_FsSnoopVlanMcastGroupInetAddressType_Object((1,3,6,1,4,1,2076,105,3,5,1,3),_FsSnoopVlanMcastGroupInetAddressType_Type())
fsSnoopVlanMcastGroupInetAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastGroupInetAddressType.setStatus(_A)
class _FsSnoopVlanMcastGroupAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsSnoopVlanMcastGroupAddress_Type.__name__=_K
_FsSnoopVlanMcastGroupAddress_Object=MibTableColumn
fsSnoopVlanMcastGroupAddress=_FsSnoopVlanMcastGroupAddress_Object((1,3,6,1,4,1,2076,105,3,5,1,4),_FsSnoopVlanMcastGroupAddress_Type())
fsSnoopVlanMcastGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastGroupAddress.setStatus(_A)
_FsSnoopVlanMcastGroupInnerVlanId_Type=InnerVlanIndex
_FsSnoopVlanMcastGroupInnerVlanId_Object=MibTableColumn
fsSnoopVlanMcastGroupInnerVlanId=_FsSnoopVlanMcastGroupInnerVlanId_Object((1,3,6,1,4,1,2076,105,3,5,1,5),_FsSnoopVlanMcastGroupInnerVlanId_Type())
fsSnoopVlanMcastGroupInnerVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastGroupInnerVlanId.setStatus(_A)
_FsSnoopVlanMcastGroupPortList_Type=PortList
_FsSnoopVlanMcastGroupPortList_Object=MibTableColumn
fsSnoopVlanMcastGroupPortList=_FsSnoopVlanMcastGroupPortList_Object((1,3,6,1,4,1,2076,105,3,5,1,6),_FsSnoopVlanMcastGroupPortList_Type())
fsSnoopVlanMcastGroupPortList.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanMcastGroupPortList.setStatus(_A)
_FsSnoopVlanMcastGroupLocalPortList_Type=PortList
_FsSnoopVlanMcastGroupLocalPortList_Object=MibTableColumn
fsSnoopVlanMcastGroupLocalPortList=_FsSnoopVlanMcastGroupLocalPortList_Object((1,3,6,1,4,1,2076,105,3,5,1,7),_FsSnoopVlanMcastGroupLocalPortList_Type())
fsSnoopVlanMcastGroupLocalPortList.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanMcastGroupLocalPortList.setStatus(_A)
_FsSnoopVlanMcastReceiverTable_Object=MibTable
fsSnoopVlanMcastReceiverTable=_FsSnoopVlanMcastReceiverTable_Object((1,3,6,1,4,1,2076,105,3,6))
if mibBuilder.loadTexts:fsSnoopVlanMcastReceiverTable.setStatus(_A)
_FsSnoopVlanMcastReceiverEntry_Object=MibTableRow
fsSnoopVlanMcastReceiverEntry=_FsSnoopVlanMcastReceiverEntry_Object((1,3,6,1,4,1,2076,105,3,6,1))
fsSnoopVlanMcastReceiverEntry.setIndexNames((0,_C,_R),(0,_C,_S),(0,_C,_T),(0,_C,_U),(0,_C,_V),(0,_C,_t),(0,_C,_u),(0,_C,_v))
if mibBuilder.loadTexts:fsSnoopVlanMcastReceiverEntry.setStatus(_A)
_FsSnoopVlanMcastReceiverPortIndex_Type=InterfaceIndex
_FsSnoopVlanMcastReceiverPortIndex_Object=MibTableColumn
fsSnoopVlanMcastReceiverPortIndex=_FsSnoopVlanMcastReceiverPortIndex_Object((1,3,6,1,4,1,2076,105,3,6,1,1),_FsSnoopVlanMcastReceiverPortIndex_Type())
fsSnoopVlanMcastReceiverPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastReceiverPortIndex.setStatus(_A)
class _FsSnoopVlanMcastReceiverHostAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsSnoopVlanMcastReceiverHostAddress_Type.__name__=_K
_FsSnoopVlanMcastReceiverHostAddress_Object=MibTableColumn
fsSnoopVlanMcastReceiverHostAddress=_FsSnoopVlanMcastReceiverHostAddress_Object((1,3,6,1,4,1,2076,105,3,6,1,2),_FsSnoopVlanMcastReceiverHostAddress_Type())
fsSnoopVlanMcastReceiverHostAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastReceiverHostAddress.setStatus(_A)
class _FsSnoopVlanMcastReceiverSourceAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsSnoopVlanMcastReceiverSourceAddress_Type.__name__=_K
_FsSnoopVlanMcastReceiverSourceAddress_Object=MibTableColumn
fsSnoopVlanMcastReceiverSourceAddress=_FsSnoopVlanMcastReceiverSourceAddress_Object((1,3,6,1,4,1,2076,105,3,6,1,3),_FsSnoopVlanMcastReceiverSourceAddress_Type())
fsSnoopVlanMcastReceiverSourceAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanMcastReceiverSourceAddress.setStatus(_A)
class _FsSnoopVlanMcastReceiverFilterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('include',1),('exclude',2)))
_FsSnoopVlanMcastReceiverFilterMode_Type.__name__=_B
_FsSnoopVlanMcastReceiverFilterMode_Object=MibTableColumn
fsSnoopVlanMcastReceiverFilterMode=_FsSnoopVlanMcastReceiverFilterMode_Object((1,3,6,1,4,1,2076,105,3,6,1,4),_FsSnoopVlanMcastReceiverFilterMode_Type())
fsSnoopVlanMcastReceiverFilterMode.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanMcastReceiverFilterMode.setStatus(_A)
_FsSnoopVlanIpFwdTable_Object=MibTable
fsSnoopVlanIpFwdTable=_FsSnoopVlanIpFwdTable_Object((1,3,6,1,4,1,2076,105,3,7))
if mibBuilder.loadTexts:fsSnoopVlanIpFwdTable.setStatus(_A)
_FsSnoopVlanIpFwdEntry_Object=MibTableRow
fsSnoopVlanIpFwdEntry=_FsSnoopVlanIpFwdEntry_Object((1,3,6,1,4,1,2076,105,3,7,1))
fsSnoopVlanIpFwdEntry.setIndexNames((0,_C,_w),(0,_C,_x),(0,_C,_y),(0,_C,_z),(0,_C,_A0),(0,_C,_A1))
if mibBuilder.loadTexts:fsSnoopVlanIpFwdEntry.setStatus(_A)
class _FsSnoopVlanIpFwdInstanceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsSnoopVlanIpFwdInstanceId_Type.__name__=_B
_FsSnoopVlanIpFwdInstanceId_Object=MibTableColumn
fsSnoopVlanIpFwdInstanceId=_FsSnoopVlanIpFwdInstanceId_Object((1,3,6,1,4,1,2076,105,3,7,1,1),_FsSnoopVlanIpFwdInstanceId_Type())
fsSnoopVlanIpFwdInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanIpFwdInstanceId.setStatus(_A)
_FsSnoopVlanIpFwdOuterVlanId_Type=VlanIndex
_FsSnoopVlanIpFwdOuterVlanId_Object=MibTableColumn
fsSnoopVlanIpFwdOuterVlanId=_FsSnoopVlanIpFwdOuterVlanId_Object((1,3,6,1,4,1,2076,105,3,7,1,2),_FsSnoopVlanIpFwdOuterVlanId_Type())
fsSnoopVlanIpFwdOuterVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanIpFwdOuterVlanId.setStatus(_A)
_FsSnoopVlanIpFwdInetAddressType_Type=InetAddressType
_FsSnoopVlanIpFwdInetAddressType_Object=MibTableColumn
fsSnoopVlanIpFwdInetAddressType=_FsSnoopVlanIpFwdInetAddressType_Object((1,3,6,1,4,1,2076,105,3,7,1,3),_FsSnoopVlanIpFwdInetAddressType_Type())
fsSnoopVlanIpFwdInetAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanIpFwdInetAddressType.setStatus(_A)
_FsSnoopVlanIpFwdSourceAddress_Type=InetAddress
_FsSnoopVlanIpFwdSourceAddress_Object=MibTableColumn
fsSnoopVlanIpFwdSourceAddress=_FsSnoopVlanIpFwdSourceAddress_Object((1,3,6,1,4,1,2076,105,3,7,1,4),_FsSnoopVlanIpFwdSourceAddress_Type())
fsSnoopVlanIpFwdSourceAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanIpFwdSourceAddress.setStatus(_A)
_FsSnoopVlanIpFwdGroupAddress_Type=InetAddress
_FsSnoopVlanIpFwdGroupAddress_Object=MibTableColumn
fsSnoopVlanIpFwdGroupAddress=_FsSnoopVlanIpFwdGroupAddress_Object((1,3,6,1,4,1,2076,105,3,7,1,5),_FsSnoopVlanIpFwdGroupAddress_Type())
fsSnoopVlanIpFwdGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanIpFwdGroupAddress.setStatus(_A)
_FsSnoopVlanIpFwdInnerVlanId_Type=InnerVlanIndex
_FsSnoopVlanIpFwdInnerVlanId_Object=MibTableColumn
fsSnoopVlanIpFwdInnerVlanId=_FsSnoopVlanIpFwdInnerVlanId_Object((1,3,6,1,4,1,2076,105,3,7,1,6),_FsSnoopVlanIpFwdInnerVlanId_Type())
fsSnoopVlanIpFwdInnerVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanIpFwdInnerVlanId.setStatus(_A)
_FsSnoopVlanIpFwdPortList_Type=PortList
_FsSnoopVlanIpFwdPortList_Object=MibTableColumn
fsSnoopVlanIpFwdPortList=_FsSnoopVlanIpFwdPortList_Object((1,3,6,1,4,1,2076,105,3,7,1,7),_FsSnoopVlanIpFwdPortList_Type())
fsSnoopVlanIpFwdPortList.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanIpFwdPortList.setStatus(_A)
_FsSnoopVlanIpFwdLocalPortList_Type=PortList
_FsSnoopVlanIpFwdLocalPortList_Object=MibTableColumn
fsSnoopVlanIpFwdLocalPortList=_FsSnoopVlanIpFwdLocalPortList_Object((1,3,6,1,4,1,2076,105,3,7,1,8),_FsSnoopVlanIpFwdLocalPortList_Type())
fsSnoopVlanIpFwdLocalPortList.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanIpFwdLocalPortList.setStatus(_A)
_FsSnoopVlanFilterXTable_Object=MibTable
fsSnoopVlanFilterXTable=_FsSnoopVlanFilterXTable_Object((1,3,6,1,4,1,2076,105,3,8))
if mibBuilder.loadTexts:fsSnoopVlanFilterXTable.setStatus(_A)
_FsSnoopVlanFilterXEntry_Object=MibTableRow
fsSnoopVlanFilterXEntry=_FsSnoopVlanFilterXEntry_Object((1,3,6,1,4,1,2076,105,3,8,1))
if mibBuilder.loadTexts:fsSnoopVlanFilterXEntry.setStatus(_A)
_FsSnoopVlanBlkRtrPortList_Type=PortList
_FsSnoopVlanBlkRtrPortList_Object=MibTableColumn
fsSnoopVlanBlkRtrPortList=_FsSnoopVlanBlkRtrPortList_Object((1,3,6,1,4,1,2076,105,3,8,1,1),_FsSnoopVlanBlkRtrPortList_Type())
fsSnoopVlanBlkRtrPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanBlkRtrPortList.setStatus(_A)
class _FsSnoopVlanFilterMaxLimitType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_W,1),(_X,2)))
_FsSnoopVlanFilterMaxLimitType_Type.__name__=_B
_FsSnoopVlanFilterMaxLimitType_Object=MibTableColumn
fsSnoopVlanFilterMaxLimitType=_FsSnoopVlanFilterMaxLimitType_Object((1,3,6,1,4,1,2076,105,3,8,1,2),_FsSnoopVlanFilterMaxLimitType_Type())
fsSnoopVlanFilterMaxLimitType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanFilterMaxLimitType.setStatus(_A)
class _FsSnoopVlanFilterMaxLimit_Type(Unsigned32):defaultValue=0
_FsSnoopVlanFilterMaxLimit_Type.__name__=_J
_FsSnoopVlanFilterMaxLimit_Object=MibTableColumn
fsSnoopVlanFilterMaxLimit=_FsSnoopVlanFilterMaxLimit_Object((1,3,6,1,4,1,2076,105,3,8,1,3),_FsSnoopVlanFilterMaxLimit_Type())
fsSnoopVlanFilterMaxLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanFilterMaxLimit.setStatus(_A)
class _FsSnoopVlanFilter8021pPriority_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsSnoopVlanFilter8021pPriority_Type.__name__=_B
_FsSnoopVlanFilter8021pPriority_Object=MibTableColumn
fsSnoopVlanFilter8021pPriority=_FsSnoopVlanFilter8021pPriority_Object((1,3,6,1,4,1,2076,105,3,8,1,4),_FsSnoopVlanFilter8021pPriority_Type())
fsSnoopVlanFilter8021pPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanFilter8021pPriority.setStatus(_A)
class _FsSnoopVlanFilterDropReports_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),('igmpv1',1),('igmpv2',2),('all',3)))
_FsSnoopVlanFilterDropReports_Type.__name__=_B
_FsSnoopVlanFilterDropReports_Object=MibTableColumn
fsSnoopVlanFilterDropReports=_FsSnoopVlanFilterDropReports_Object((1,3,6,1,4,1,2076,105,3,8,1,5),_FsSnoopVlanFilterDropReports_Type())
fsSnoopVlanFilterDropReports.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanFilterDropReports.setStatus(_A)
class _FsSnoopVlanMulticastProfileId_Type(Unsigned32):defaultValue=0
_FsSnoopVlanMulticastProfileId_Type.__name__=_J
_FsSnoopVlanMulticastProfileId_Object=MibTableColumn
fsSnoopVlanMulticastProfileId=_FsSnoopVlanMulticastProfileId_Object((1,3,6,1,4,1,2076,105,3,8,1,6),_FsSnoopVlanMulticastProfileId_Type())
fsSnoopVlanMulticastProfileId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanMulticastProfileId.setStatus(_A)
_FsSnoopVlanPortPurgeInterval_Type=Integer32
_FsSnoopVlanPortPurgeInterval_Object=MibTableColumn
fsSnoopVlanPortPurgeInterval=_FsSnoopVlanPortPurgeInterval_Object((1,3,6,1,4,1,2076,105,3,8,1,7),_FsSnoopVlanPortPurgeInterval_Type())
fsSnoopVlanPortPurgeInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopVlanPortPurgeInterval.setStatus(_A)
class _FsSnoopVlanMaxResponseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65025))
_FsSnoopVlanMaxResponseTime_Type.__name__=_B
_FsSnoopVlanMaxResponseTime_Object=MibTableColumn
fsSnoopVlanMaxResponseTime=_FsSnoopVlanMaxResponseTime_Object((1,3,6,1,4,1,2076,105,3,8,1,8),_FsSnoopVlanMaxResponseTime_Type())
fsSnoopVlanMaxResponseTime.setMaxAccess(_L)
if mibBuilder.loadTexts:fsSnoopVlanMaxResponseTime.setStatus(_A)
_FsSnoopVlanRtrLocalPortList_Type=PortList
_FsSnoopVlanRtrLocalPortList_Object=MibTableColumn
fsSnoopVlanRtrLocalPortList=_FsSnoopVlanRtrLocalPortList_Object((1,3,6,1,4,1,2076,105,3,8,1,9),_FsSnoopVlanRtrLocalPortList_Type())
fsSnoopVlanRtrLocalPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanRtrLocalPortList.setStatus(_A)
_FsSnoopVlanBlkRtrLocalPortList_Type=PortList
_FsSnoopVlanBlkRtrLocalPortList_Object=MibTableColumn
fsSnoopVlanBlkRtrLocalPortList=_FsSnoopVlanBlkRtrLocalPortList_Object((1,3,6,1,4,1,2076,105,3,8,1,10),_FsSnoopVlanBlkRtrLocalPortList_Type())
fsSnoopVlanBlkRtrLocalPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanBlkRtrLocalPortList.setStatus(_A)
_FsSnoopVlanStaticMcastGrpTable_Object=MibTable
fsSnoopVlanStaticMcastGrpTable=_FsSnoopVlanStaticMcastGrpTable_Object((1,3,6,1,4,1,2076,105,3,9))
if mibBuilder.loadTexts:fsSnoopVlanStaticMcastGrpTable.setStatus(_A)
_FsSnoopVlanStaticMcastGrpEntry_Object=MibTableRow
fsSnoopVlanStaticMcastGrpEntry=_FsSnoopVlanStaticMcastGrpEntry_Object((1,3,6,1,4,1,2076,105,3,9,1))
fsSnoopVlanStaticMcastGrpEntry.setIndexNames((0,_C,_A2),(0,_C,_A3),(0,_C,_A4),(0,_C,_A5),(0,_C,_A6))
if mibBuilder.loadTexts:fsSnoopVlanStaticMcastGrpEntry.setStatus(_A)
class _FsSnoopVlanStaticMcastGrpInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsSnoopVlanStaticMcastGrpInstId_Type.__name__=_B
_FsSnoopVlanStaticMcastGrpInstId_Object=MibTableColumn
fsSnoopVlanStaticMcastGrpInstId=_FsSnoopVlanStaticMcastGrpInstId_Object((1,3,6,1,4,1,2076,105,3,9,1,1),_FsSnoopVlanStaticMcastGrpInstId_Type())
fsSnoopVlanStaticMcastGrpInstId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanStaticMcastGrpInstId.setStatus(_A)
class _FsSnoopVlanStaticMcastGrpVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsSnoopVlanStaticMcastGrpVlanId_Type.__name__=_B
_FsSnoopVlanStaticMcastGrpVlanId_Object=MibTableColumn
fsSnoopVlanStaticMcastGrpVlanId=_FsSnoopVlanStaticMcastGrpVlanId_Object((1,3,6,1,4,1,2076,105,3,9,1,2),_FsSnoopVlanStaticMcastGrpVlanId_Type())
fsSnoopVlanStaticMcastGrpVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanStaticMcastGrpVlanId.setStatus(_A)
_FsSnoopVlanStaticMcastGrpAddressType_Type=InetAddressType
_FsSnoopVlanStaticMcastGrpAddressType_Object=MibTableColumn
fsSnoopVlanStaticMcastGrpAddressType=_FsSnoopVlanStaticMcastGrpAddressType_Object((1,3,6,1,4,1,2076,105,3,9,1,3),_FsSnoopVlanStaticMcastGrpAddressType_Type())
fsSnoopVlanStaticMcastGrpAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanStaticMcastGrpAddressType.setStatus(_A)
_FsSnoopVlanStaticMcastGrpSourceAddress_Type=InetAddress
_FsSnoopVlanStaticMcastGrpSourceAddress_Object=MibTableColumn
fsSnoopVlanStaticMcastGrpSourceAddress=_FsSnoopVlanStaticMcastGrpSourceAddress_Object((1,3,6,1,4,1,2076,105,3,9,1,4),_FsSnoopVlanStaticMcastGrpSourceAddress_Type())
fsSnoopVlanStaticMcastGrpSourceAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanStaticMcastGrpSourceAddress.setStatus(_A)
_FsSnoopVlanStaticMcastGrpGroupAddress_Type=InetAddress
_FsSnoopVlanStaticMcastGrpGroupAddress_Object=MibTableColumn
fsSnoopVlanStaticMcastGrpGroupAddress=_FsSnoopVlanStaticMcastGrpGroupAddress_Object((1,3,6,1,4,1,2076,105,3,9,1,5),_FsSnoopVlanStaticMcastGrpGroupAddress_Type())
fsSnoopVlanStaticMcastGrpGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopVlanStaticMcastGrpGroupAddress.setStatus(_A)
_FsSnoopVlanStaticMcastGrpPortList_Type=PortList
_FsSnoopVlanStaticMcastGrpPortList_Object=MibTableColumn
fsSnoopVlanStaticMcastGrpPortList=_FsSnoopVlanStaticMcastGrpPortList_Object((1,3,6,1,4,1,2076,105,3,9,1,6),_FsSnoopVlanStaticMcastGrpPortList_Type())
fsSnoopVlanStaticMcastGrpPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopVlanStaticMcastGrpPortList.setStatus(_A)
_FsSnoopVlanStaticMcastGrpRowStatus_Type=RowStatus
_FsSnoopVlanStaticMcastGrpRowStatus_Object=MibTableColumn
fsSnoopVlanStaticMcastGrpRowStatus=_FsSnoopVlanStaticMcastGrpRowStatus_Object((1,3,6,1,4,1,2076,105,3,9,1,7),_FsSnoopVlanStaticMcastGrpRowStatus_Type())
fsSnoopVlanStaticMcastGrpRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:fsSnoopVlanStaticMcastGrpRowStatus.setStatus(_A)
_FsSnoopStats_ObjectIdentity=ObjectIdentity
fsSnoopStats=_FsSnoopStats_ObjectIdentity((1,3,6,1,4,1,2076,105,4))
_FsSnoopStatsTable_Object=MibTable
fsSnoopStatsTable=_FsSnoopStatsTable_Object((1,3,6,1,4,1,2076,105,4,1))
if mibBuilder.loadTexts:fsSnoopStatsTable.setStatus(_A)
_FsSnoopStatsEntry_Object=MibTableRow
fsSnoopStatsEntry=_FsSnoopStatsEntry_Object((1,3,6,1,4,1,2076,105,4,1,1))
fsSnoopStatsEntry.setIndexNames((0,_C,_A7),(0,_C,_A8),(0,_C,_A9))
if mibBuilder.loadTexts:fsSnoopStatsEntry.setStatus(_A)
class _FsSnoopStatsInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsSnoopStatsInstId_Type.__name__=_B
_FsSnoopStatsInstId_Object=MibTableColumn
fsSnoopStatsInstId=_FsSnoopStatsInstId_Object((1,3,6,1,4,1,2076,105,4,1,1,1),_FsSnoopStatsInstId_Type())
fsSnoopStatsInstId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopStatsInstId.setStatus(_A)
class _FsSnoopStatsVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsSnoopStatsVlanId_Type.__name__=_B
_FsSnoopStatsVlanId_Object=MibTableColumn
fsSnoopStatsVlanId=_FsSnoopStatsVlanId_Object((1,3,6,1,4,1,2076,105,4,1,1,2),_FsSnoopStatsVlanId_Type())
fsSnoopStatsVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopStatsVlanId.setStatus(_A)
_FsSnoopStatsInetAddressType_Type=InetAddressType
_FsSnoopStatsInetAddressType_Object=MibTableColumn
fsSnoopStatsInetAddressType=_FsSnoopStatsInetAddressType_Object((1,3,6,1,4,1,2076,105,4,1,1,3),_FsSnoopStatsInetAddressType_Type())
fsSnoopStatsInetAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopStatsInetAddressType.setStatus(_A)
_FsSnoopStatsRxGenQueries_Type=Counter32
_FsSnoopStatsRxGenQueries_Object=MibTableColumn
fsSnoopStatsRxGenQueries=_FsSnoopStatsRxGenQueries_Object((1,3,6,1,4,1,2076,105,4,1,1,4),_FsSnoopStatsRxGenQueries_Type())
fsSnoopStatsRxGenQueries.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsRxGenQueries.setStatus(_A)
_FsSnoopStatsRxGrpQueries_Type=Counter32
_FsSnoopStatsRxGrpQueries_Object=MibTableColumn
fsSnoopStatsRxGrpQueries=_FsSnoopStatsRxGrpQueries_Object((1,3,6,1,4,1,2076,105,4,1,1,5),_FsSnoopStatsRxGrpQueries_Type())
fsSnoopStatsRxGrpQueries.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsRxGrpQueries.setStatus(_A)
_FsSnoopStatsRxGrpAndSrcQueries_Type=Counter32
_FsSnoopStatsRxGrpAndSrcQueries_Object=MibTableColumn
fsSnoopStatsRxGrpAndSrcQueries=_FsSnoopStatsRxGrpAndSrcQueries_Object((1,3,6,1,4,1,2076,105,4,1,1,6),_FsSnoopStatsRxGrpAndSrcQueries_Type())
fsSnoopStatsRxGrpAndSrcQueries.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsRxGrpAndSrcQueries.setStatus(_A)
_FsSnoopStatsRxAsmReports_Type=Counter32
_FsSnoopStatsRxAsmReports_Object=MibTableColumn
fsSnoopStatsRxAsmReports=_FsSnoopStatsRxAsmReports_Object((1,3,6,1,4,1,2076,105,4,1,1,7),_FsSnoopStatsRxAsmReports_Type())
fsSnoopStatsRxAsmReports.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsRxAsmReports.setStatus(_A)
_FsSnoopStatsRxSsmReports_Type=Counter32
_FsSnoopStatsRxSsmReports_Object=MibTableColumn
fsSnoopStatsRxSsmReports=_FsSnoopStatsRxSsmReports_Object((1,3,6,1,4,1,2076,105,4,1,1,8),_FsSnoopStatsRxSsmReports_Type())
fsSnoopStatsRxSsmReports.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsRxSsmReports.setStatus(_A)
_FsSnoopStatsRxSsmIsInMsgs_Type=Counter32
_FsSnoopStatsRxSsmIsInMsgs_Object=MibTableColumn
fsSnoopStatsRxSsmIsInMsgs=_FsSnoopStatsRxSsmIsInMsgs_Object((1,3,6,1,4,1,2076,105,4,1,1,9),_FsSnoopStatsRxSsmIsInMsgs_Type())
fsSnoopStatsRxSsmIsInMsgs.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsRxSsmIsInMsgs.setStatus(_A)
_FsSnoopStatsRxSsmIsExMsgs_Type=Counter32
_FsSnoopStatsRxSsmIsExMsgs_Object=MibTableColumn
fsSnoopStatsRxSsmIsExMsgs=_FsSnoopStatsRxSsmIsExMsgs_Object((1,3,6,1,4,1,2076,105,4,1,1,10),_FsSnoopStatsRxSsmIsExMsgs_Type())
fsSnoopStatsRxSsmIsExMsgs.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsRxSsmIsExMsgs.setStatus(_A)
_FsSnoopStatsRxSsmToInMsgs_Type=Counter32
_FsSnoopStatsRxSsmToInMsgs_Object=MibTableColumn
fsSnoopStatsRxSsmToInMsgs=_FsSnoopStatsRxSsmToInMsgs_Object((1,3,6,1,4,1,2076,105,4,1,1,11),_FsSnoopStatsRxSsmToInMsgs_Type())
fsSnoopStatsRxSsmToInMsgs.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsRxSsmToInMsgs.setStatus(_A)
_FsSnoopStatsRxSsmToExMsgs_Type=Counter32
_FsSnoopStatsRxSsmToExMsgs_Object=MibTableColumn
fsSnoopStatsRxSsmToExMsgs=_FsSnoopStatsRxSsmToExMsgs_Object((1,3,6,1,4,1,2076,105,4,1,1,12),_FsSnoopStatsRxSsmToExMsgs_Type())
fsSnoopStatsRxSsmToExMsgs.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsRxSsmToExMsgs.setStatus(_A)
_FsSnoopStatsRxSsmAllowMsgs_Type=Counter32
_FsSnoopStatsRxSsmAllowMsgs_Object=MibTableColumn
fsSnoopStatsRxSsmAllowMsgs=_FsSnoopStatsRxSsmAllowMsgs_Object((1,3,6,1,4,1,2076,105,4,1,1,13),_FsSnoopStatsRxSsmAllowMsgs_Type())
fsSnoopStatsRxSsmAllowMsgs.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsRxSsmAllowMsgs.setStatus(_A)
_FsSnoopStatsRxSsmBlockMsgs_Type=Counter32
_FsSnoopStatsRxSsmBlockMsgs_Object=MibTableColumn
fsSnoopStatsRxSsmBlockMsgs=_FsSnoopStatsRxSsmBlockMsgs_Object((1,3,6,1,4,1,2076,105,4,1,1,14),_FsSnoopStatsRxSsmBlockMsgs_Type())
fsSnoopStatsRxSsmBlockMsgs.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsRxSsmBlockMsgs.setStatus(_A)
_FsSnoopStatsRxAsmLeaves_Type=Counter32
_FsSnoopStatsRxAsmLeaves_Object=MibTableColumn
fsSnoopStatsRxAsmLeaves=_FsSnoopStatsRxAsmLeaves_Object((1,3,6,1,4,1,2076,105,4,1,1,15),_FsSnoopStatsRxAsmLeaves_Type())
fsSnoopStatsRxAsmLeaves.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsRxAsmLeaves.setStatus(_A)
_FsSnoopStatsTxGenQueries_Type=Counter32
_FsSnoopStatsTxGenQueries_Object=MibTableColumn
fsSnoopStatsTxGenQueries=_FsSnoopStatsTxGenQueries_Object((1,3,6,1,4,1,2076,105,4,1,1,16),_FsSnoopStatsTxGenQueries_Type())
fsSnoopStatsTxGenQueries.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsTxGenQueries.setStatus(_A)
_FsSnoopStatsTxGrpQueries_Type=Counter32
_FsSnoopStatsTxGrpQueries_Object=MibTableColumn
fsSnoopStatsTxGrpQueries=_FsSnoopStatsTxGrpQueries_Object((1,3,6,1,4,1,2076,105,4,1,1,17),_FsSnoopStatsTxGrpQueries_Type())
fsSnoopStatsTxGrpQueries.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsTxGrpQueries.setStatus(_A)
_FsSnoopStatsTxGrpAndSrcQueries_Type=Counter32
_FsSnoopStatsTxGrpAndSrcQueries_Object=MibTableColumn
fsSnoopStatsTxGrpAndSrcQueries=_FsSnoopStatsTxGrpAndSrcQueries_Object((1,3,6,1,4,1,2076,105,4,1,1,18),_FsSnoopStatsTxGrpAndSrcQueries_Type())
fsSnoopStatsTxGrpAndSrcQueries.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsTxGrpAndSrcQueries.setStatus(_A)
_FsSnoopStatsTxAsmReports_Type=Counter32
_FsSnoopStatsTxAsmReports_Object=MibTableColumn
fsSnoopStatsTxAsmReports=_FsSnoopStatsTxAsmReports_Object((1,3,6,1,4,1,2076,105,4,1,1,19),_FsSnoopStatsTxAsmReports_Type())
fsSnoopStatsTxAsmReports.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsTxAsmReports.setStatus(_A)
_FsSnoopStatsTxSsmReports_Type=Counter32
_FsSnoopStatsTxSsmReports_Object=MibTableColumn
fsSnoopStatsTxSsmReports=_FsSnoopStatsTxSsmReports_Object((1,3,6,1,4,1,2076,105,4,1,1,20),_FsSnoopStatsTxSsmReports_Type())
fsSnoopStatsTxSsmReports.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsTxSsmReports.setStatus(_A)
_FsSnoopStatsTxAsmLeaves_Type=Counter32
_FsSnoopStatsTxAsmLeaves_Object=MibTableColumn
fsSnoopStatsTxAsmLeaves=_FsSnoopStatsTxAsmLeaves_Object((1,3,6,1,4,1,2076,105,4,1,1,21),_FsSnoopStatsTxAsmLeaves_Type())
fsSnoopStatsTxAsmLeaves.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsTxAsmLeaves.setStatus(_A)
_FsSnoopStatsDroppedPkts_Type=Counter32
_FsSnoopStatsDroppedPkts_Object=MibTableColumn
fsSnoopStatsDroppedPkts=_FsSnoopStatsDroppedPkts_Object((1,3,6,1,4,1,2076,105,4,1,1,22),_FsSnoopStatsDroppedPkts_Type())
fsSnoopStatsDroppedPkts.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsDroppedPkts.setStatus(_A)
_FsSnoopStatsUnsuccessfulJoins_Type=Counter32
_FsSnoopStatsUnsuccessfulJoins_Object=MibTableColumn
fsSnoopStatsUnsuccessfulJoins=_FsSnoopStatsUnsuccessfulJoins_Object((1,3,6,1,4,1,2076,105,4,1,1,23),_FsSnoopStatsUnsuccessfulJoins_Type())
fsSnoopStatsUnsuccessfulJoins.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsUnsuccessfulJoins.setStatus(_A)
_FsSnoopStatsActiveJoins_Type=Counter32
_FsSnoopStatsActiveJoins_Object=MibTableColumn
fsSnoopStatsActiveJoins=_FsSnoopStatsActiveJoins_Object((1,3,6,1,4,1,2076,105,4,1,1,24),_FsSnoopStatsActiveJoins_Type())
fsSnoopStatsActiveJoins.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsActiveJoins.setStatus(_A)
_FsSnoopStatsActiveGroups_Type=Counter32
_FsSnoopStatsActiveGroups_Object=MibTableColumn
fsSnoopStatsActiveGroups=_FsSnoopStatsActiveGroups_Object((1,3,6,1,4,1,2076,105,4,1,1,25),_FsSnoopStatsActiveGroups_Type())
fsSnoopStatsActiveGroups.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopStatsActiveGroups.setStatus(_A)
_FsSnoopPort_ObjectIdentity=ObjectIdentity
fsSnoopPort=_FsSnoopPort_ObjectIdentity((1,3,6,1,4,1,2076,105,5))
_FsSnoopPortTable_Object=MibTable
fsSnoopPortTable=_FsSnoopPortTable_Object((1,3,6,1,4,1,2076,105,5,1))
if mibBuilder.loadTexts:fsSnoopPortTable.setStatus(_A)
_FsSnoopPortEntry_Object=MibTableRow
fsSnoopPortEntry=_FsSnoopPortEntry_Object((1,3,6,1,4,1,2076,105,5,1,1))
fsSnoopPortEntry.setIndexNames((0,_C,_AA),(0,_C,_AB))
if mibBuilder.loadTexts:fsSnoopPortEntry.setStatus(_A)
_FsSnoopPortIndex_Type=InterfaceIndex
_FsSnoopPortIndex_Object=MibTableColumn
fsSnoopPortIndex=_FsSnoopPortIndex_Object((1,3,6,1,4,1,2076,105,5,1,1,1),_FsSnoopPortIndex_Type())
fsSnoopPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopPortIndex.setStatus(_A)
_FsSnoopPortInetAddressType_Type=InetAddressType
_FsSnoopPortInetAddressType_Object=MibTableColumn
fsSnoopPortInetAddressType=_FsSnoopPortInetAddressType_Object((1,3,6,1,4,1,2076,105,5,1,1,2),_FsSnoopPortInetAddressType_Type())
fsSnoopPortInetAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopPortInetAddressType.setStatus(_A)
class _FsSnoopPortLeaveMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AC,1),(_AD,2),(_AE,3)))
_FsSnoopPortLeaveMode_Type.__name__=_B
_FsSnoopPortLeaveMode_Object=MibTableColumn
fsSnoopPortLeaveMode=_FsSnoopPortLeaveMode_Object((1,3,6,1,4,1,2076,105,5,1,1,3),_FsSnoopPortLeaveMode_Type())
fsSnoopPortLeaveMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopPortLeaveMode.setStatus(_A)
class _FsSnoopPortRateLimit_Type(Unsigned32):defaultValue=4294967295
_FsSnoopPortRateLimit_Type.__name__=_J
_FsSnoopPortRateLimit_Object=MibTableColumn
fsSnoopPortRateLimit=_FsSnoopPortRateLimit_Object((1,3,6,1,4,1,2076,105,5,1,1,4),_FsSnoopPortRateLimit_Type())
fsSnoopPortRateLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopPortRateLimit.setStatus(_A)
class _FsSnoopPortMaxLimitType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_W,1),(_X,2)))
_FsSnoopPortMaxLimitType_Type.__name__=_B
_FsSnoopPortMaxLimitType_Object=MibTableColumn
fsSnoopPortMaxLimitType=_FsSnoopPortMaxLimitType_Object((1,3,6,1,4,1,2076,105,5,1,1,5),_FsSnoopPortMaxLimitType_Type())
fsSnoopPortMaxLimitType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopPortMaxLimitType.setStatus(_A)
class _FsSnoopPortMaxLimit_Type(Unsigned32):defaultValue=0
_FsSnoopPortMaxLimit_Type.__name__=_J
_FsSnoopPortMaxLimit_Object=MibTableColumn
fsSnoopPortMaxLimit=_FsSnoopPortMaxLimit_Object((1,3,6,1,4,1,2076,105,5,1,1,6),_FsSnoopPortMaxLimit_Type())
fsSnoopPortMaxLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopPortMaxLimit.setStatus(_A)
class _FsSnoopPortProfileId_Type(Unsigned32):defaultValue=0
_FsSnoopPortProfileId_Type.__name__=_J
_FsSnoopPortProfileId_Object=MibTableColumn
fsSnoopPortProfileId=_FsSnoopPortProfileId_Object((1,3,6,1,4,1,2076,105,5,1,1,7),_FsSnoopPortProfileId_Type())
fsSnoopPortProfileId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopPortProfileId.setStatus(_A)
_FsSnoopPortMemberCnt_Type=Unsigned32
_FsSnoopPortMemberCnt_Object=MibTableColumn
fsSnoopPortMemberCnt=_FsSnoopPortMemberCnt_Object((1,3,6,1,4,1,2076,105,5,1,1,8),_FsSnoopPortMemberCnt_Type())
fsSnoopPortMemberCnt.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopPortMemberCnt.setStatus(_A)
_FsSnoopPortMaxBandwidthLimit_Type=Unsigned32
_FsSnoopPortMaxBandwidthLimit_Object=MibTableColumn
fsSnoopPortMaxBandwidthLimit=_FsSnoopPortMaxBandwidthLimit_Object((1,3,6,1,4,1,2076,105,5,1,1,9),_FsSnoopPortMaxBandwidthLimit_Type())
fsSnoopPortMaxBandwidthLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopPortMaxBandwidthLimit.setStatus(_A)
class _FsSnoopPortDropReports_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('drop',2)))
_FsSnoopPortDropReports_Type.__name__=_B
_FsSnoopPortDropReports_Object=MibTableColumn
fsSnoopPortDropReports=_FsSnoopPortDropReports_Object((1,3,6,1,4,1,2076,105,5,1,1,10),_FsSnoopPortDropReports_Type())
fsSnoopPortDropReports.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopPortDropReports.setStatus(_A)
_FsSnoopPortRowStatus_Type=RowStatus
_FsSnoopPortRowStatus_Object=MibTableColumn
fsSnoopPortRowStatus=_FsSnoopPortRowStatus_Object((1,3,6,1,4,1,2076,105,5,1,1,11),_FsSnoopPortRowStatus_Type())
fsSnoopPortRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:fsSnoopPortRowStatus.setStatus(_A)
_FsSnoopEnhPortTable_Object=MibTable
fsSnoopEnhPortTable=_FsSnoopEnhPortTable_Object((1,3,6,1,4,1,2076,105,5,2))
if mibBuilder.loadTexts:fsSnoopEnhPortTable.setStatus(_A)
_FsSnoopEnhPortEntry_Object=MibTableRow
fsSnoopEnhPortEntry=_FsSnoopEnhPortEntry_Object((1,3,6,1,4,1,2076,105,5,2,1))
fsSnoopEnhPortEntry.setIndexNames((0,_C,_AF),(0,_C,_AG),(0,_C,_AH))
if mibBuilder.loadTexts:fsSnoopEnhPortEntry.setStatus(_A)
_FsSnoopEnhPortIndex_Type=InterfaceIndex
_FsSnoopEnhPortIndex_Object=MibTableColumn
fsSnoopEnhPortIndex=_FsSnoopEnhPortIndex_Object((1,3,6,1,4,1,2076,105,5,2,1,1),_FsSnoopEnhPortIndex_Type())
fsSnoopEnhPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopEnhPortIndex.setStatus(_A)
_FsSnoopEnhPortInnerVlanId_Type=InnerVlanIndex
_FsSnoopEnhPortInnerVlanId_Object=MibTableColumn
fsSnoopEnhPortInnerVlanId=_FsSnoopEnhPortInnerVlanId_Object((1,3,6,1,4,1,2076,105,5,2,1,2),_FsSnoopEnhPortInnerVlanId_Type())
fsSnoopEnhPortInnerVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopEnhPortInnerVlanId.setStatus(_A)
_FsSnoopEnhPortInetAddressType_Type=InetAddressType
_FsSnoopEnhPortInetAddressType_Object=MibTableColumn
fsSnoopEnhPortInetAddressType=_FsSnoopEnhPortInetAddressType_Object((1,3,6,1,4,1,2076,105,5,2,1,3),_FsSnoopEnhPortInetAddressType_Type())
fsSnoopEnhPortInetAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopEnhPortInetAddressType.setStatus(_A)
class _FsSnoopEnhPortLeaveMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AC,1),(_AD,2),(_AE,3)))
_FsSnoopEnhPortLeaveMode_Type.__name__=_B
_FsSnoopEnhPortLeaveMode_Object=MibTableColumn
fsSnoopEnhPortLeaveMode=_FsSnoopEnhPortLeaveMode_Object((1,3,6,1,4,1,2076,105,5,2,1,4),_FsSnoopEnhPortLeaveMode_Type())
fsSnoopEnhPortLeaveMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopEnhPortLeaveMode.setStatus(_A)
class _FsSnoopEnhPortRateLimit_Type(Unsigned32):defaultValue=4294967295
_FsSnoopEnhPortRateLimit_Type.__name__=_J
_FsSnoopEnhPortRateLimit_Object=MibTableColumn
fsSnoopEnhPortRateLimit=_FsSnoopEnhPortRateLimit_Object((1,3,6,1,4,1,2076,105,5,2,1,5),_FsSnoopEnhPortRateLimit_Type())
fsSnoopEnhPortRateLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopEnhPortRateLimit.setStatus(_A)
class _FsSnoopEnhPortMaxLimitType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_W,1),(_X,2)))
_FsSnoopEnhPortMaxLimitType_Type.__name__=_B
_FsSnoopEnhPortMaxLimitType_Object=MibTableColumn
fsSnoopEnhPortMaxLimitType=_FsSnoopEnhPortMaxLimitType_Object((1,3,6,1,4,1,2076,105,5,2,1,6),_FsSnoopEnhPortMaxLimitType_Type())
fsSnoopEnhPortMaxLimitType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopEnhPortMaxLimitType.setStatus(_A)
class _FsSnoopEnhPortMaxLimit_Type(Unsigned32):defaultValue=0
_FsSnoopEnhPortMaxLimit_Type.__name__=_J
_FsSnoopEnhPortMaxLimit_Object=MibTableColumn
fsSnoopEnhPortMaxLimit=_FsSnoopEnhPortMaxLimit_Object((1,3,6,1,4,1,2076,105,5,2,1,7),_FsSnoopEnhPortMaxLimit_Type())
fsSnoopEnhPortMaxLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopEnhPortMaxLimit.setStatus(_A)
class _FsSnoopEnhPortProfileId_Type(Unsigned32):defaultValue=0
_FsSnoopEnhPortProfileId_Type.__name__=_J
_FsSnoopEnhPortProfileId_Object=MibTableColumn
fsSnoopEnhPortProfileId=_FsSnoopEnhPortProfileId_Object((1,3,6,1,4,1,2076,105,5,2,1,8),_FsSnoopEnhPortProfileId_Type())
fsSnoopEnhPortProfileId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopEnhPortProfileId.setStatus(_A)
_FsSnoopEnhPortMemberCnt_Type=Unsigned32
_FsSnoopEnhPortMemberCnt_Object=MibTableColumn
fsSnoopEnhPortMemberCnt=_FsSnoopEnhPortMemberCnt_Object((1,3,6,1,4,1,2076,105,5,2,1,9),_FsSnoopEnhPortMemberCnt_Type())
fsSnoopEnhPortMemberCnt.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopEnhPortMemberCnt.setStatus(_A)
_FsSnoopEnhPortMaxBandwidthLimit_Type=Unsigned32
_FsSnoopEnhPortMaxBandwidthLimit_Object=MibTableColumn
fsSnoopEnhPortMaxBandwidthLimit=_FsSnoopEnhPortMaxBandwidthLimit_Object((1,3,6,1,4,1,2076,105,5,2,1,10),_FsSnoopEnhPortMaxBandwidthLimit_Type())
fsSnoopEnhPortMaxBandwidthLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopEnhPortMaxBandwidthLimit.setStatus(_A)
class _FsSnoopEnhPortDropReports_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('drop',2)))
_FsSnoopEnhPortDropReports_Type.__name__=_B
_FsSnoopEnhPortDropReports_Object=MibTableColumn
fsSnoopEnhPortDropReports=_FsSnoopEnhPortDropReports_Object((1,3,6,1,4,1,2076,105,5,2,1,11),_FsSnoopEnhPortDropReports_Type())
fsSnoopEnhPortDropReports.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopEnhPortDropReports.setStatus(_A)
_FsSnoopEnhPortRowStatus_Type=RowStatus
_FsSnoopEnhPortRowStatus_Object=MibTableColumn
fsSnoopEnhPortRowStatus=_FsSnoopEnhPortRowStatus_Object((1,3,6,1,4,1,2076,105,5,2,1,12),_FsSnoopEnhPortRowStatus_Type())
fsSnoopEnhPortRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:fsSnoopEnhPortRowStatus.setStatus(_A)
_FsSnoopRtrPortTable_Object=MibTable
fsSnoopRtrPortTable=_FsSnoopRtrPortTable_Object((1,3,6,1,4,1,2076,105,5,3))
if mibBuilder.loadTexts:fsSnoopRtrPortTable.setStatus(_A)
_FsSnoopRtrPortEntry_Object=MibTableRow
fsSnoopRtrPortEntry=_FsSnoopRtrPortEntry_Object((1,3,6,1,4,1,2076,105,5,3,1))
fsSnoopRtrPortEntry.setIndexNames((0,_C,_AI),(0,_C,_AJ),(0,_C,_AK))
if mibBuilder.loadTexts:fsSnoopRtrPortEntry.setStatus(_A)
_FsSnoopRtrPortIndex_Type=InterfaceIndex
_FsSnoopRtrPortIndex_Object=MibTableColumn
fsSnoopRtrPortIndex=_FsSnoopRtrPortIndex_Object((1,3,6,1,4,1,2076,105,5,3,1,1),_FsSnoopRtrPortIndex_Type())
fsSnoopRtrPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopRtrPortIndex.setStatus(_A)
_FsSnoopRtrPortVlanId_Type=VlanIndex
_FsSnoopRtrPortVlanId_Object=MibTableColumn
fsSnoopRtrPortVlanId=_FsSnoopRtrPortVlanId_Object((1,3,6,1,4,1,2076,105,5,3,1,2),_FsSnoopRtrPortVlanId_Type())
fsSnoopRtrPortVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopRtrPortVlanId.setStatus(_A)
_FsSnoopRtrPortInetAddressType_Type=InetAddressType
_FsSnoopRtrPortInetAddressType_Object=MibTableColumn
fsSnoopRtrPortInetAddressType=_FsSnoopRtrPortInetAddressType_Object((1,3,6,1,4,1,2076,105,5,3,1,3),_FsSnoopRtrPortInetAddressType_Type())
fsSnoopRtrPortInetAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSnoopRtrPortInetAddressType.setStatus(_A)
class _FsSnoopRtrPortOperVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_FsSnoopRtrPortOperVersion_Type.__name__=_B
_FsSnoopRtrPortOperVersion_Object=MibTableColumn
fsSnoopRtrPortOperVersion=_FsSnoopRtrPortOperVersion_Object((1,3,6,1,4,1,2076,105,5,3,1,4),_FsSnoopRtrPortOperVersion_Type())
fsSnoopRtrPortOperVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopRtrPortOperVersion.setStatus(_A)
class _FsSnoopRtrPortCfgOperVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_FsSnoopRtrPortCfgOperVersion_Type.__name__=_B
_FsSnoopRtrPortCfgOperVersion_Object=MibTableColumn
fsSnoopRtrPortCfgOperVersion=_FsSnoopRtrPortCfgOperVersion_Object((1,3,6,1,4,1,2076,105,5,3,1,5),_FsSnoopRtrPortCfgOperVersion_Type())
fsSnoopRtrPortCfgOperVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopRtrPortCfgOperVersion.setStatus(_A)
class _FsSnoopOlderQuerierInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_FsSnoopOlderQuerierInterval_Type.__name__=_B
_FsSnoopOlderQuerierInterval_Object=MibTableColumn
fsSnoopOlderQuerierInterval=_FsSnoopOlderQuerierInterval_Object((1,3,6,1,4,1,2076,105,5,3,1,6),_FsSnoopOlderQuerierInterval_Type())
fsSnoopOlderQuerierInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSnoopOlderQuerierInterval.setStatus(_A)
_FsSnoopV3QuerierInterval_Type=Integer32
_FsSnoopV3QuerierInterval_Object=MibTableColumn
fsSnoopV3QuerierInterval=_FsSnoopV3QuerierInterval_Object((1,3,6,1,4,1,2076,105,5,3,1,7),_FsSnoopV3QuerierInterval_Type())
fsSnoopV3QuerierInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopV3QuerierInterval.setStatus(_A)
_FsXSnoopRtrPortTable_Object=MibTable
fsXSnoopRtrPortTable=_FsXSnoopRtrPortTable_Object((1,3,6,1,4,1,2076,105,5,4))
if mibBuilder.loadTexts:fsXSnoopRtrPortTable.setStatus(_A)
_FsXSnoopRtrPortEntry_Object=MibTableRow
fsXSnoopRtrPortEntry=_FsXSnoopRtrPortEntry_Object((1,3,6,1,4,1,2076,105,5,4,1))
if mibBuilder.loadTexts:fsXSnoopRtrPortEntry.setStatus(_A)
_FsXSnoopRtrPortRowStatus_Type=RowStatus
_FsXSnoopRtrPortRowStatus_Object=MibTableColumn
fsXSnoopRtrPortRowStatus=_FsXSnoopRtrPortRowStatus_Object((1,3,6,1,4,1,2076,105,5,4,1,1),_FsXSnoopRtrPortRowStatus_Type())
fsXSnoopRtrPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsXSnoopRtrPortRowStatus.setStatus(_A)
_FsSnoopTrapObjects_ObjectIdentity=ObjectIdentity
fsSnoopTrapObjects=_FsSnoopTrapObjects_ObjectIdentity((1,3,6,1,4,1,2076,105,6))
_FsSnoopTrapObjectsTable_Object=MibTable
fsSnoopTrapObjectsTable=_FsSnoopTrapObjectsTable_Object((1,3,6,1,4,1,2076,105,6,5))
if mibBuilder.loadTexts:fsSnoopTrapObjectsTable.setStatus(_A)
_FsSnoopTrapObjectsEntry_Object=MibTableRow
fsSnoopTrapObjectsEntry=_FsSnoopTrapObjectsEntry_Object((1,3,6,1,4,1,2076,105,6,5,1))
if mibBuilder.loadTexts:fsSnoopTrapObjectsEntry.setStatus(_A)
class _FsSnoopTrapHwErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('hardwareCreate',0),('hardwareDelete',1),('hardwarePortAdd',2),('hardwarePortDelete',3)))
_FsSnoopTrapHwErrType_Type.__name__=_B
_FsSnoopTrapHwErrType_Object=MibTableColumn
fsSnoopTrapHwErrType=_FsSnoopTrapHwErrType_Object((1,3,6,1,4,1,2076,105,6,5,1,1),_FsSnoopTrapHwErrType_Type())
fsSnoopTrapHwErrType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsSnoopTrapHwErrType.setStatus(_A)
_FsSnoopNotifications_ObjectIdentity=ObjectIdentity
fsSnoopNotifications=_FsSnoopNotifications_ObjectIdentity((1,3,6,1,4,1,2076,105,7))
_FsSnoopTraps_ObjectIdentity=ObjectIdentity
fsSnoopTraps=_FsSnoopTraps_ObjectIdentity((1,3,6,1,4,1,2076,105,7,0))
fsSnoopVlanFilterEntry.registerAugmentions((_C,_AL))
fsSnoopVlanFilterXEntry.setIndexNames(*fsSnoopVlanFilterEntry.getIndexNames())
fsSnoopRtrPortEntry.registerAugmentions((_C,_AM))
fsXSnoopRtrPortEntry.setIndexNames(*fsSnoopRtrPortEntry.getIndexNames())
fsSnoopVlanIpFwdEntry.registerAugmentions((_C,_AN))
fsSnoopTrapObjectsEntry.setIndexNames(*fsSnoopVlanIpFwdEntry.getIndexNames())
fsSnoopHwFailureTrap=NotificationType((1,3,6,1,4,1,2076,105,7,0,1))
fsSnoopHwFailureTrap.setObjects((_C,_AO))
if mibBuilder.loadTexts:fsSnoopHwFailureTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'InnerVlanIndex':InnerVlanIndex,'fssnoop':fssnoop,'fsSnoopSystem':fsSnoopSystem,'fsSnoopInst':fsSnoopInst,'fsSnoopInstanceGlobalTable':fsSnoopInstanceGlobalTable,'fsSnoopInstanceGlobalEntry':fsSnoopInstanceGlobalEntry,_Y:fsSnoopInstanceGlobalInstId,'fsSnoopInstanceGlobalMcastFwdMode':fsSnoopInstanceGlobalMcastFwdMode,'fsSnoopInstanceGlobalSystemControl':fsSnoopInstanceGlobalSystemControl,'fsSnoopInstanceGlobalLeaveConfigLevel':fsSnoopInstanceGlobalLeaveConfigLevel,'fsSnoopInstanceGlobalEnhancedMode':fsSnoopInstanceGlobalEnhancedMode,'fsSnoopInstanceGlobalReportProcessConfigLevel':fsSnoopInstanceGlobalReportProcessConfigLevel,'fsSnoopInstanceGlobalSparseMode':fsSnoopInstanceGlobalSparseMode,'fsSnoopInstanceConfigTable':fsSnoopInstanceConfigTable,'fsSnoopInstanceConfigEntry':fsSnoopInstanceConfigEntry,_b:fsSnoopInstanceConfigInstId,_c:fsSnoopInetAddressType,'fsSnoopStatus':fsSnoopStatus,'fsSnoopProxyReportingStatus':fsSnoopProxyReportingStatus,'fsSnoopRouterPortPurgeInterval':fsSnoopRouterPortPurgeInterval,'fsSnoopPortPurgeInterval':fsSnoopPortPurgeInterval,'fsSnoopReportForwardInterval':fsSnoopReportForwardInterval,'fsSnoopRetryCount':fsSnoopRetryCount,'fsSnoopGrpQueryInterval':fsSnoopGrpQueryInterval,'fsSnoopReportFwdOnAllPorts':fsSnoopReportFwdOnAllPorts,'fsSnoopTraceOption':fsSnoopTraceOption,'fsSnoopOperStatus':fsSnoopOperStatus,'fsSnoopSendQueryOnTopoChange':fsSnoopSendQueryOnTopoChange,'fsSnoopSendLeaveOnTopoChange':fsSnoopSendLeaveOnTopoChange,'fsSnoopFilterStatus':fsSnoopFilterStatus,'fsSnoopMulticastVlanStatus':fsSnoopMulticastVlanStatus,'fsSnoopProxyStatus':fsSnoopProxyStatus,'fsSnoopQueryFwdOnAllPorts':fsSnoopQueryFwdOnAllPorts,'fsSnoopFwdGroupsCnt':fsSnoopFwdGroupsCnt,'fsSnoopDebugOption':fsSnoopDebugOption,'fsSnoopVlan':fsSnoopVlan,'fsSnoopVlanMcastMacFwdTable':fsSnoopVlanMcastMacFwdTable,'fsSnoopVlanMcastMacFwdEntry':fsSnoopVlanMcastMacFwdEntry,_d:fsSnoopVlanMcastMacFwdInstId,_e:fsSnoopVlanMcastMacFwdVlanId,_f:fsSnoopVlanMcastMacFwdInetAddressType,_g:fsSnoopVlanMcastMacFwdGroupAddress,'fsSnoopVlanMcastMacFwdPortList':fsSnoopVlanMcastMacFwdPortList,'fsSnoopVlanMcastMacFwdLocalPortList':fsSnoopVlanMcastMacFwdLocalPortList,'fsSnoopVlanMcastMacFwdEntryFlag':fsSnoopVlanMcastMacFwdEntryFlag,'fsSnoopVlanMcastIpFwdTable':fsSnoopVlanMcastIpFwdTable,'fsSnoopVlanMcastIpFwdEntry':fsSnoopVlanMcastIpFwdEntry,_h:fsSnoopVlanMcastIpFwdInstId,_i:fsSnoopVlanMcastIpFwdVlanId,_j:fsSnoopVlanMcastIpFwdAddressType,_k:fsSnoopVlanMcastIpFwdSourceAddress,_l:fsSnoopVlanMcastIpFwdGroupAddress,'fsSnoopVlanMcastIpFwdPortList':fsSnoopVlanMcastIpFwdPortList,'fsSnoopVlanMcastIpFwdEntryFlag':fsSnoopVlanMcastIpFwdEntryFlag,'fsSnoopVlanRouterTable':fsSnoopVlanRouterTable,'fsSnoopVlanRouterEntry':fsSnoopVlanRouterEntry,_m:fsSnoopVlanRouterInstId,_n:fsSnoopVlanRouterVlanId,_o:fsSnoopVlanRouterInetAddressType,'fsSnoopVlanRouterPortList':fsSnoopVlanRouterPortList,'fsSnoopVlanRouterLocalPortList':fsSnoopVlanRouterLocalPortList,'fsSnoopVlanFilterTable':fsSnoopVlanFilterTable,'fsSnoopVlanFilterEntry':fsSnoopVlanFilterEntry,_p:fsSnoopVlanFilterInstId,_q:fsSnoopVlanFilterVlanId,_r:fsSnoopVlanFilterInetAddressType,'fsSnoopVlanSnoopStatus':fsSnoopVlanSnoopStatus,'fsSnoopVlanOperatingVersion':fsSnoopVlanOperatingVersion,'fsSnoopVlanCfgOperVersion':fsSnoopVlanCfgOperVersion,'fsSnoopVlanFastLeave':fsSnoopVlanFastLeave,'fsSnoopVlanQuerier':fsSnoopVlanQuerier,'fsSnoopVlanCfgQuerier':fsSnoopVlanCfgQuerier,'fsSnoopVlanQueryInterval':fsSnoopVlanQueryInterval,'fsSnoopVlanRtrPortList':fsSnoopVlanRtrPortList,'fsSnoopVlanRowStatus':fsSnoopVlanRowStatus,'fsSnoopVlanStartupQueryCount':fsSnoopVlanStartupQueryCount,'fsSnoopVlanStartupQueryInterval':fsSnoopVlanStartupQueryInterval,'fsSnoopVlanOtherQuerierPresentInterval':fsSnoopVlanOtherQuerierPresentInterval,'fsSnoopVlanQuerierIpAddress':fsSnoopVlanQuerierIpAddress,'fsSnoopVlanQuerierIpFlag':fsSnoopVlanQuerierIpFlag,'fsSnoopVlanElectedQuerier':fsSnoopVlanElectedQuerier,'fsSnoopVlanMcastGroupTable':fsSnoopVlanMcastGroupTable,'fsSnoopVlanMcastGroupEntry':fsSnoopVlanMcastGroupEntry,_R:fsSnoopVlanMcastGroupInstanceId,_S:fsSnoopVlanMcastGroupOuterVlanId,_T:fsSnoopVlanMcastGroupInetAddressType,_U:fsSnoopVlanMcastGroupAddress,_V:fsSnoopVlanMcastGroupInnerVlanId,'fsSnoopVlanMcastGroupPortList':fsSnoopVlanMcastGroupPortList,'fsSnoopVlanMcastGroupLocalPortList':fsSnoopVlanMcastGroupLocalPortList,'fsSnoopVlanMcastReceiverTable':fsSnoopVlanMcastReceiverTable,'fsSnoopVlanMcastReceiverEntry':fsSnoopVlanMcastReceiverEntry,_t:fsSnoopVlanMcastReceiverPortIndex,_u:fsSnoopVlanMcastReceiverHostAddress,_v:fsSnoopVlanMcastReceiverSourceAddress,'fsSnoopVlanMcastReceiverFilterMode':fsSnoopVlanMcastReceiverFilterMode,'fsSnoopVlanIpFwdTable':fsSnoopVlanIpFwdTable,'fsSnoopVlanIpFwdEntry':fsSnoopVlanIpFwdEntry,_w:fsSnoopVlanIpFwdInstanceId,_x:fsSnoopVlanIpFwdOuterVlanId,_y:fsSnoopVlanIpFwdInetAddressType,_z:fsSnoopVlanIpFwdSourceAddress,_A0:fsSnoopVlanIpFwdGroupAddress,_A1:fsSnoopVlanIpFwdInnerVlanId,'fsSnoopVlanIpFwdPortList':fsSnoopVlanIpFwdPortList,'fsSnoopVlanIpFwdLocalPortList':fsSnoopVlanIpFwdLocalPortList,'fsSnoopVlanFilterXTable':fsSnoopVlanFilterXTable,_AL:fsSnoopVlanFilterXEntry,'fsSnoopVlanBlkRtrPortList':fsSnoopVlanBlkRtrPortList,'fsSnoopVlanFilterMaxLimitType':fsSnoopVlanFilterMaxLimitType,'fsSnoopVlanFilterMaxLimit':fsSnoopVlanFilterMaxLimit,'fsSnoopVlanFilter8021pPriority':fsSnoopVlanFilter8021pPriority,'fsSnoopVlanFilterDropReports':fsSnoopVlanFilterDropReports,'fsSnoopVlanMulticastProfileId':fsSnoopVlanMulticastProfileId,'fsSnoopVlanPortPurgeInterval':fsSnoopVlanPortPurgeInterval,'fsSnoopVlanMaxResponseTime':fsSnoopVlanMaxResponseTime,'fsSnoopVlanRtrLocalPortList':fsSnoopVlanRtrLocalPortList,'fsSnoopVlanBlkRtrLocalPortList':fsSnoopVlanBlkRtrLocalPortList,'fsSnoopVlanStaticMcastGrpTable':fsSnoopVlanStaticMcastGrpTable,'fsSnoopVlanStaticMcastGrpEntry':fsSnoopVlanStaticMcastGrpEntry,_A2:fsSnoopVlanStaticMcastGrpInstId,_A3:fsSnoopVlanStaticMcastGrpVlanId,_A4:fsSnoopVlanStaticMcastGrpAddressType,_A5:fsSnoopVlanStaticMcastGrpSourceAddress,_A6:fsSnoopVlanStaticMcastGrpGroupAddress,'fsSnoopVlanStaticMcastGrpPortList':fsSnoopVlanStaticMcastGrpPortList,'fsSnoopVlanStaticMcastGrpRowStatus':fsSnoopVlanStaticMcastGrpRowStatus,'fsSnoopStats':fsSnoopStats,'fsSnoopStatsTable':fsSnoopStatsTable,'fsSnoopStatsEntry':fsSnoopStatsEntry,_A7:fsSnoopStatsInstId,_A8:fsSnoopStatsVlanId,_A9:fsSnoopStatsInetAddressType,'fsSnoopStatsRxGenQueries':fsSnoopStatsRxGenQueries,'fsSnoopStatsRxGrpQueries':fsSnoopStatsRxGrpQueries,'fsSnoopStatsRxGrpAndSrcQueries':fsSnoopStatsRxGrpAndSrcQueries,'fsSnoopStatsRxAsmReports':fsSnoopStatsRxAsmReports,'fsSnoopStatsRxSsmReports':fsSnoopStatsRxSsmReports,'fsSnoopStatsRxSsmIsInMsgs':fsSnoopStatsRxSsmIsInMsgs,'fsSnoopStatsRxSsmIsExMsgs':fsSnoopStatsRxSsmIsExMsgs,'fsSnoopStatsRxSsmToInMsgs':fsSnoopStatsRxSsmToInMsgs,'fsSnoopStatsRxSsmToExMsgs':fsSnoopStatsRxSsmToExMsgs,'fsSnoopStatsRxSsmAllowMsgs':fsSnoopStatsRxSsmAllowMsgs,'fsSnoopStatsRxSsmBlockMsgs':fsSnoopStatsRxSsmBlockMsgs,'fsSnoopStatsRxAsmLeaves':fsSnoopStatsRxAsmLeaves,'fsSnoopStatsTxGenQueries':fsSnoopStatsTxGenQueries,'fsSnoopStatsTxGrpQueries':fsSnoopStatsTxGrpQueries,'fsSnoopStatsTxGrpAndSrcQueries':fsSnoopStatsTxGrpAndSrcQueries,'fsSnoopStatsTxAsmReports':fsSnoopStatsTxAsmReports,'fsSnoopStatsTxSsmReports':fsSnoopStatsTxSsmReports,'fsSnoopStatsTxAsmLeaves':fsSnoopStatsTxAsmLeaves,'fsSnoopStatsDroppedPkts':fsSnoopStatsDroppedPkts,'fsSnoopStatsUnsuccessfulJoins':fsSnoopStatsUnsuccessfulJoins,'fsSnoopStatsActiveJoins':fsSnoopStatsActiveJoins,'fsSnoopStatsActiveGroups':fsSnoopStatsActiveGroups,'fsSnoopPort':fsSnoopPort,'fsSnoopPortTable':fsSnoopPortTable,'fsSnoopPortEntry':fsSnoopPortEntry,_AA:fsSnoopPortIndex,_AB:fsSnoopPortInetAddressType,'fsSnoopPortLeaveMode':fsSnoopPortLeaveMode,'fsSnoopPortRateLimit':fsSnoopPortRateLimit,'fsSnoopPortMaxLimitType':fsSnoopPortMaxLimitType,'fsSnoopPortMaxLimit':fsSnoopPortMaxLimit,'fsSnoopPortProfileId':fsSnoopPortProfileId,'fsSnoopPortMemberCnt':fsSnoopPortMemberCnt,'fsSnoopPortMaxBandwidthLimit':fsSnoopPortMaxBandwidthLimit,'fsSnoopPortDropReports':fsSnoopPortDropReports,'fsSnoopPortRowStatus':fsSnoopPortRowStatus,'fsSnoopEnhPortTable':fsSnoopEnhPortTable,'fsSnoopEnhPortEntry':fsSnoopEnhPortEntry,_AF:fsSnoopEnhPortIndex,_AG:fsSnoopEnhPortInnerVlanId,_AH:fsSnoopEnhPortInetAddressType,'fsSnoopEnhPortLeaveMode':fsSnoopEnhPortLeaveMode,'fsSnoopEnhPortRateLimit':fsSnoopEnhPortRateLimit,'fsSnoopEnhPortMaxLimitType':fsSnoopEnhPortMaxLimitType,'fsSnoopEnhPortMaxLimit':fsSnoopEnhPortMaxLimit,'fsSnoopEnhPortProfileId':fsSnoopEnhPortProfileId,'fsSnoopEnhPortMemberCnt':fsSnoopEnhPortMemberCnt,'fsSnoopEnhPortMaxBandwidthLimit':fsSnoopEnhPortMaxBandwidthLimit,'fsSnoopEnhPortDropReports':fsSnoopEnhPortDropReports,'fsSnoopEnhPortRowStatus':fsSnoopEnhPortRowStatus,'fsSnoopRtrPortTable':fsSnoopRtrPortTable,'fsSnoopRtrPortEntry':fsSnoopRtrPortEntry,_AI:fsSnoopRtrPortIndex,_AJ:fsSnoopRtrPortVlanId,_AK:fsSnoopRtrPortInetAddressType,'fsSnoopRtrPortOperVersion':fsSnoopRtrPortOperVersion,'fsSnoopRtrPortCfgOperVersion':fsSnoopRtrPortCfgOperVersion,'fsSnoopOlderQuerierInterval':fsSnoopOlderQuerierInterval,'fsSnoopV3QuerierInterval':fsSnoopV3QuerierInterval,'fsXSnoopRtrPortTable':fsXSnoopRtrPortTable,_AM:fsXSnoopRtrPortEntry,'fsXSnoopRtrPortRowStatus':fsXSnoopRtrPortRowStatus,'fsSnoopTrapObjects':fsSnoopTrapObjects,'fsSnoopTrapObjectsTable':fsSnoopTrapObjectsTable,_AN:fsSnoopTrapObjectsEntry,_AO:fsSnoopTrapHwErrType,'fsSnoopNotifications':fsSnoopNotifications,'fsSnoopTraps':fsSnoopTraps,'fsSnoopHwFailureTrap':fsSnoopHwFailureTrap})