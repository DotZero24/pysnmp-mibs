_AT='clabGREGroup'
_AS='clabGREFilterDscpMarkPolicy'
_AR='clabGREFilterVlanTag'
_AQ='clabGREFilterVlanIdExclude'
_AP='clabGREFilterVlanIdCheck'
_AO='clabGREFilterAllInterfaces'
_AN='clabGREFilterInterface'
_AM='clabGREFilterAlias'
_AL='clabGREFilterOrder'
_AK='clabGREFilterStatus'
_AJ='clabGREFilterEnable'
_AI='clabGREFilterRowStatus'
_AH='clabGRETunnelInterfaceStatsDiscardSequenceNumberReceived'
_AG='clabGRETunnelInterfaceStatsDiscardChecksumReceived'
_AF='clabGRETunnelInterfaceStatsErrorsReceived'
_AE='clabGRETunnelInterfaceStatsErrorsSent'
_AD='clabGRETunnelInterfaceStatsPacketsReceived'
_AC='clabGRETunnelInterfaceStatsPacketsSent'
_AB='clabGRETunnelInterfaceStatsBytesReceived'
_AA='clabGRETunnelInterfaceStatsBytesSent'
_A9='clabGRETunnelInterfaceUseSequenceNumber'
_A8='clabGRETunnelInterfaceKeyIdentifier'
_A7='clabGRETunnelInterfaceKeyIdentifierGenerationPolicy'
_A6='clabGRETunnelInterfaceUseChecksum'
_A5='clabGRETunnelInterfaceProtocolIdOverride'
_A4='clabGRETunnelInterfaceEnable'
_A3='clabGRETunnelInterfaceLowerLayers'
_A2='clabGRETunnelInterfaceLastChange'
_A1='clabGRETunnelInterfaceName'
_A0='clabGRETunnelInterfaceAlias'
_z='clabGRETunnelInterfaceStatus'
_y='clabGRETunnelInterfaceRowStatus'
_x='clabGRETunnelStatsErrorsReceived'
_w='clabGRETunnelStatsErrorsSent'
_v='clabGRETunnelStatsPacketsReceived'
_u='clabGRETunnelStatsPacketsSent'
_t='clabGRETunnelStatsBytesReceived'
_s='clabGRETunnelStatsBytesSent'
_r='clabGRETunnelStatsKeepAliveReceived'
_q='clabGRETunnelStatsKeepAliveSent'
_p='clabGRETunnnelRemoteEndpointConnectivityState'
_o='clabGRETunnelConcentratorServiceName'
_n='clabGRETunnelTcpMssClamping'
_m='clabGRETunnelInterfaceNumberOfEntries'
_l='clabGRETunnelConnectedRemoteEndpoint'
_k='clabGRETunnelDefaultDscpMark'
_j='clabGRETunnelDeliveryHeaderProtocol'
_i='clabGRETunnelKeepAliveRecoverInterval'
_h='clabGRETunnelKeepAliveFailureInterval'
_g='clabGRETunnelKeepAliveInterval'
_f='clabGRETunnelKeepAliveCount'
_e='clabGRETunnelKeepAliveThreshold'
_d='clabGRETunnelKeepAliveTimeout'
_c='clabGRETunnelKeepAlivePolicy'
_b='clabGRETunnelRemoteEndpoints'
_a='clabGRETunnelAlias'
_Z='clabGRETunnelStatus'
_Y='clabGRETunnelEnable'
_X='clabGRETunnelRowStatus'
_W='clabGREFilterNumberOfEntries'
_V='clabGRETunnelNumberOfEntries'
_U='clabGRETunnelInterfaceStatsEntry'
_T='clabGRETunnelStatsEntry'
_S='clabGREFilterIndex'
_R='clabGRETunnelInterfaceIndex'
_Q='errorMisconfigured'
_P='enabled'
_O='error'
_N='disabled'
_M='not-accessible'
_L='clabGRETunnelIndex'
_K='OctetString'
_J='bytes'
_I='seconds'
_H='TruthValue'
_G='Integer32'
_F='packets'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='CLAB-GRE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabCommonMibs,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabCommonMibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_H)
clabGREMib=ModuleIdentity((1,3,6,1,4,1,4491,4,3))
if mibBuilder.loadTexts:clabGREMib.setRevisions(('2017-10-19 00:00','2015-02-04 00:00'))
_ClabGREObjects_ObjectIdentity=ObjectIdentity
clabGREObjects=_ClabGREObjects_ObjectIdentity((1,3,6,1,4,1,4491,4,3,1))
class _ClabGRETunnelNumberOfEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_ClabGRETunnelNumberOfEntries_Type.__name__=_E
_ClabGRETunnelNumberOfEntries_Object=MibScalar
clabGRETunnelNumberOfEntries=_ClabGRETunnelNumberOfEntries_Object((1,3,6,1,4,1,4491,4,3,1,1),_ClabGRETunnelNumberOfEntries_Type())
clabGRETunnelNumberOfEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelNumberOfEntries.setStatus(_A)
class _ClabGREFilterNumberOfEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_ClabGREFilterNumberOfEntries_Type.__name__=_E
_ClabGREFilterNumberOfEntries_Object=MibScalar
clabGREFilterNumberOfEntries=_ClabGREFilterNumberOfEntries_Object((1,3,6,1,4,1,4491,4,3,1,2),_ClabGREFilterNumberOfEntries_Type())
clabGREFilterNumberOfEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGREFilterNumberOfEntries.setStatus(_A)
_ClabGRETunnelTable_Object=MibTable
clabGRETunnelTable=_ClabGRETunnelTable_Object((1,3,6,1,4,1,4491,4,3,1,3))
if mibBuilder.loadTexts:clabGRETunnelTable.setStatus(_A)
_ClabGRETunnelEntry_Object=MibTableRow
clabGRETunnelEntry=_ClabGRETunnelEntry_Object((1,3,6,1,4,1,4491,4,3,1,3,1))
clabGRETunnelEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:clabGRETunnelEntry.setStatus(_A)
class _ClabGRETunnelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,499))
_ClabGRETunnelIndex_Type.__name__=_E
_ClabGRETunnelIndex_Object=MibTableColumn
clabGRETunnelIndex=_ClabGRETunnelIndex_Object((1,3,6,1,4,1,4491,4,3,1,3,1,1),_ClabGRETunnelIndex_Type())
clabGRETunnelIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:clabGRETunnelIndex.setStatus(_A)
_ClabGRETunnelRowStatus_Type=RowStatus
_ClabGRETunnelRowStatus_Object=MibTableColumn
clabGRETunnelRowStatus=_ClabGRETunnelRowStatus_Object((1,3,6,1,4,1,4491,4,3,1,3,1,2),_ClabGRETunnelRowStatus_Type())
clabGRETunnelRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelRowStatus.setStatus(_A)
_ClabGRETunnelEnable_Type=TruthValue
_ClabGRETunnelEnable_Object=MibTableColumn
clabGRETunnelEnable=_ClabGRETunnelEnable_Object((1,3,6,1,4,1,4491,4,3,1,3,1,3),_ClabGRETunnelEnable_Type())
clabGRETunnelEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelEnable.setStatus(_A)
class _ClabGRETunnelStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_P,2),(_O,3),(_Q,4),('retryWait',5)))
_ClabGRETunnelStatus_Type.__name__=_G
_ClabGRETunnelStatus_Object=MibTableColumn
clabGRETunnelStatus=_ClabGRETunnelStatus_Object((1,3,6,1,4,1,4491,4,3,1,3,1,4),_ClabGRETunnelStatus_Type())
clabGRETunnelStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelStatus.setStatus(_A)
_ClabGRETunnelAlias_Type=SnmpAdminString
_ClabGRETunnelAlias_Object=MibTableColumn
clabGRETunnelAlias=_ClabGRETunnelAlias_Object((1,3,6,1,4,1,4491,4,3,1,3,1,5),_ClabGRETunnelAlias_Type())
clabGRETunnelAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelAlias.setStatus(_A)
class _ClabGRETunnelRemoteEndpoints_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1040))
_ClabGRETunnelRemoteEndpoints_Type.__name__=_K
_ClabGRETunnelRemoteEndpoints_Object=MibTableColumn
clabGRETunnelRemoteEndpoints=_ClabGRETunnelRemoteEndpoints_Object((1,3,6,1,4,1,4491,4,3,1,3,1,6),_ClabGRETunnelRemoteEndpoints_Type())
clabGRETunnelRemoteEndpoints.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelRemoteEndpoints.setStatus(_A)
class _ClabGRETunnelKeepAlivePolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('icmp',1),('none',2)))
_ClabGRETunnelKeepAlivePolicy_Type.__name__=_G
_ClabGRETunnelKeepAlivePolicy_Object=MibTableColumn
clabGRETunnelKeepAlivePolicy=_ClabGRETunnelKeepAlivePolicy_Object((1,3,6,1,4,1,4491,4,3,1,3,1,7),_ClabGRETunnelKeepAlivePolicy_Type())
clabGRETunnelKeepAlivePolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelKeepAlivePolicy.setStatus(_A)
class _ClabGRETunnelKeepAliveTimeout_Type(Unsigned32):defaultValue=10
_ClabGRETunnelKeepAliveTimeout_Type.__name__=_E
_ClabGRETunnelKeepAliveTimeout_Object=MibTableColumn
clabGRETunnelKeepAliveTimeout=_ClabGRETunnelKeepAliveTimeout_Object((1,3,6,1,4,1,4491,4,3,1,3,1,8),_ClabGRETunnelKeepAliveTimeout_Type())
clabGRETunnelKeepAliveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelKeepAliveTimeout.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelKeepAliveTimeout.setUnits(_I)
class _ClabGRETunnelKeepAliveThreshold_Type(Unsigned32):defaultValue=3
_ClabGRETunnelKeepAliveThreshold_Type.__name__=_E
_ClabGRETunnelKeepAliveThreshold_Object=MibTableColumn
clabGRETunnelKeepAliveThreshold=_ClabGRETunnelKeepAliveThreshold_Object((1,3,6,1,4,1,4491,4,3,1,3,1,9),_ClabGRETunnelKeepAliveThreshold_Type())
clabGRETunnelKeepAliveThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelKeepAliveThreshold.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelKeepAliveThreshold.setUnits('errors')
class _ClabGRETunnelKeepAliveCount_Type(Unsigned32):defaultValue=3
_ClabGRETunnelKeepAliveCount_Type.__name__=_E
_ClabGRETunnelKeepAliveCount_Object=MibTableColumn
clabGRETunnelKeepAliveCount=_ClabGRETunnelKeepAliveCount_Object((1,3,6,1,4,1,4491,4,3,1,3,1,10),_ClabGRETunnelKeepAliveCount_Type())
clabGRETunnelKeepAliveCount.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelKeepAliveCount.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelKeepAliveCount.setUnits(_F)
class _ClabGRETunnelKeepAliveInterval_Type(Unsigned32):defaultValue=60
_ClabGRETunnelKeepAliveInterval_Type.__name__=_E
_ClabGRETunnelKeepAliveInterval_Object=MibTableColumn
clabGRETunnelKeepAliveInterval=_ClabGRETunnelKeepAliveInterval_Object((1,3,6,1,4,1,4491,4,3,1,3,1,11),_ClabGRETunnelKeepAliveInterval_Type())
clabGRETunnelKeepAliveInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelKeepAliveInterval.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelKeepAliveInterval.setUnits(_I)
class _ClabGRETunnelKeepAliveFailureInterval_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ClabGRETunnelKeepAliveFailureInterval_Type.__name__=_E
_ClabGRETunnelKeepAliveFailureInterval_Object=MibTableColumn
clabGRETunnelKeepAliveFailureInterval=_ClabGRETunnelKeepAliveFailureInterval_Object((1,3,6,1,4,1,4491,4,3,1,3,1,12),_ClabGRETunnelKeepAliveFailureInterval_Type())
clabGRETunnelKeepAliveFailureInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelKeepAliveFailureInterval.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelKeepAliveFailureInterval.setUnits(_I)
class _ClabGRETunnelKeepAliveRecoverInterval_Type(Unsigned32):defaultValue=43200
_ClabGRETunnelKeepAliveRecoverInterval_Type.__name__=_E
_ClabGRETunnelKeepAliveRecoverInterval_Object=MibTableColumn
clabGRETunnelKeepAliveRecoverInterval=_ClabGRETunnelKeepAliveRecoverInterval_Object((1,3,6,1,4,1,4491,4,3,1,3,1,13),_ClabGRETunnelKeepAliveRecoverInterval_Type())
clabGRETunnelKeepAliveRecoverInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelKeepAliveRecoverInterval.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelKeepAliveRecoverInterval.setUnits(_I)
class _ClabGRETunnelDeliveryHeaderProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_ClabGRETunnelDeliveryHeaderProtocol_Type.__name__=_G
_ClabGRETunnelDeliveryHeaderProtocol_Object=MibTableColumn
clabGRETunnelDeliveryHeaderProtocol=_ClabGRETunnelDeliveryHeaderProtocol_Object((1,3,6,1,4,1,4491,4,3,1,3,1,14),_ClabGRETunnelDeliveryHeaderProtocol_Type())
clabGRETunnelDeliveryHeaderProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelDeliveryHeaderProtocol.setStatus(_A)
_ClabGRETunnelDefaultDscpMark_Type=Unsigned32
_ClabGRETunnelDefaultDscpMark_Object=MibTableColumn
clabGRETunnelDefaultDscpMark=_ClabGRETunnelDefaultDscpMark_Object((1,3,6,1,4,1,4491,4,3,1,3,1,15),_ClabGRETunnelDefaultDscpMark_Type())
clabGRETunnelDefaultDscpMark.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelDefaultDscpMark.setStatus(_A)
_ClabGRETunnelConnectedRemoteEndpoint_Type=SnmpAdminString
_ClabGRETunnelConnectedRemoteEndpoint_Object=MibTableColumn
clabGRETunnelConnectedRemoteEndpoint=_ClabGRETunnelConnectedRemoteEndpoint_Object((1,3,6,1,4,1,4491,4,3,1,3,1,16),_ClabGRETunnelConnectedRemoteEndpoint_Type())
clabGRETunnelConnectedRemoteEndpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelConnectedRemoteEndpoint.setStatus(_A)
class _ClabGRETunnelInterfaceNumberOfEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_ClabGRETunnelInterfaceNumberOfEntries_Type.__name__=_E
_ClabGRETunnelInterfaceNumberOfEntries_Object=MibTableColumn
clabGRETunnelInterfaceNumberOfEntries=_ClabGRETunnelInterfaceNumberOfEntries_Object((1,3,6,1,4,1,4491,4,3,1,3,1,17),_ClabGRETunnelInterfaceNumberOfEntries_Type())
clabGRETunnelInterfaceNumberOfEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelInterfaceNumberOfEntries.setStatus(_A)
class _ClabGRETunnelTcpMssClamping_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1420))
_ClabGRETunnelTcpMssClamping_Type.__name__=_E
_ClabGRETunnelTcpMssClamping_Object=MibTableColumn
clabGRETunnelTcpMssClamping=_ClabGRETunnelTcpMssClamping_Object((1,3,6,1,4,1,4491,4,3,1,3,1,18),_ClabGRETunnelTcpMssClamping_Type())
clabGRETunnelTcpMssClamping.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelTcpMssClamping.setStatus(_A)
_ClabGRETunnelConcentratorServiceName_Type=SnmpAdminString
_ClabGRETunnelConcentratorServiceName_Object=MibTableColumn
clabGRETunnelConcentratorServiceName=_ClabGRETunnelConcentratorServiceName_Object((1,3,6,1,4,1,4491,4,3,1,3,1,19),_ClabGRETunnelConcentratorServiceName_Type())
clabGRETunnelConcentratorServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelConcentratorServiceName.setStatus(_A)
class _ClabGRETunnnelRemoteEndpointConnectivityState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_ClabGRETunnnelRemoteEndpointConnectivityState_Type.__name__=_K
_ClabGRETunnnelRemoteEndpointConnectivityState_Object=MibTableColumn
clabGRETunnnelRemoteEndpointConnectivityState=_ClabGRETunnnelRemoteEndpointConnectivityState_Object((1,3,6,1,4,1,4491,4,3,1,3,1,20),_ClabGRETunnnelRemoteEndpointConnectivityState_Type())
clabGRETunnnelRemoteEndpointConnectivityState.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnnelRemoteEndpointConnectivityState.setStatus(_A)
_ClabGRETunnelStatsTable_Object=MibTable
clabGRETunnelStatsTable=_ClabGRETunnelStatsTable_Object((1,3,6,1,4,1,4491,4,3,1,4))
if mibBuilder.loadTexts:clabGRETunnelStatsTable.setStatus(_A)
_ClabGRETunnelStatsEntry_Object=MibTableRow
clabGRETunnelStatsEntry=_ClabGRETunnelStatsEntry_Object((1,3,6,1,4,1,4491,4,3,1,4,1))
if mibBuilder.loadTexts:clabGRETunnelStatsEntry.setStatus(_A)
_ClabGRETunnelStatsKeepAliveSent_Type=Counter64
_ClabGRETunnelStatsKeepAliveSent_Object=MibTableColumn
clabGRETunnelStatsKeepAliveSent=_ClabGRETunnelStatsKeepAliveSent_Object((1,3,6,1,4,1,4491,4,3,1,4,1,1),_ClabGRETunnelStatsKeepAliveSent_Type())
clabGRETunnelStatsKeepAliveSent.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelStatsKeepAliveSent.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelStatsKeepAliveSent.setUnits(_F)
_ClabGRETunnelStatsKeepAliveReceived_Type=Counter64
_ClabGRETunnelStatsKeepAliveReceived_Object=MibTableColumn
clabGRETunnelStatsKeepAliveReceived=_ClabGRETunnelStatsKeepAliveReceived_Object((1,3,6,1,4,1,4491,4,3,1,4,1,2),_ClabGRETunnelStatsKeepAliveReceived_Type())
clabGRETunnelStatsKeepAliveReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelStatsKeepAliveReceived.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelStatsKeepAliveReceived.setUnits(_F)
_ClabGRETunnelStatsBytesSent_Type=Counter64
_ClabGRETunnelStatsBytesSent_Object=MibTableColumn
clabGRETunnelStatsBytesSent=_ClabGRETunnelStatsBytesSent_Object((1,3,6,1,4,1,4491,4,3,1,4,1,3),_ClabGRETunnelStatsBytesSent_Type())
clabGRETunnelStatsBytesSent.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelStatsBytesSent.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelStatsBytesSent.setUnits(_J)
_ClabGRETunnelStatsBytesReceived_Type=Counter64
_ClabGRETunnelStatsBytesReceived_Object=MibTableColumn
clabGRETunnelStatsBytesReceived=_ClabGRETunnelStatsBytesReceived_Object((1,3,6,1,4,1,4491,4,3,1,4,1,4),_ClabGRETunnelStatsBytesReceived_Type())
clabGRETunnelStatsBytesReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelStatsBytesReceived.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelStatsBytesReceived.setUnits(_J)
_ClabGRETunnelStatsPacketsSent_Type=Counter64
_ClabGRETunnelStatsPacketsSent_Object=MibTableColumn
clabGRETunnelStatsPacketsSent=_ClabGRETunnelStatsPacketsSent_Object((1,3,6,1,4,1,4491,4,3,1,4,1,5),_ClabGRETunnelStatsPacketsSent_Type())
clabGRETunnelStatsPacketsSent.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelStatsPacketsSent.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelStatsPacketsSent.setUnits(_F)
_ClabGRETunnelStatsPacketsReceived_Type=Counter64
_ClabGRETunnelStatsPacketsReceived_Object=MibTableColumn
clabGRETunnelStatsPacketsReceived=_ClabGRETunnelStatsPacketsReceived_Object((1,3,6,1,4,1,4491,4,3,1,4,1,6),_ClabGRETunnelStatsPacketsReceived_Type())
clabGRETunnelStatsPacketsReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelStatsPacketsReceived.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelStatsPacketsReceived.setUnits(_F)
_ClabGRETunnelStatsErrorsSent_Type=Counter64
_ClabGRETunnelStatsErrorsSent_Object=MibTableColumn
clabGRETunnelStatsErrorsSent=_ClabGRETunnelStatsErrorsSent_Object((1,3,6,1,4,1,4491,4,3,1,4,1,7),_ClabGRETunnelStatsErrorsSent_Type())
clabGRETunnelStatsErrorsSent.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelStatsErrorsSent.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelStatsErrorsSent.setUnits(_F)
_ClabGRETunnelStatsErrorsReceived_Type=Counter64
_ClabGRETunnelStatsErrorsReceived_Object=MibTableColumn
clabGRETunnelStatsErrorsReceived=_ClabGRETunnelStatsErrorsReceived_Object((1,3,6,1,4,1,4491,4,3,1,4,1,8),_ClabGRETunnelStatsErrorsReceived_Type())
clabGRETunnelStatsErrorsReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelStatsErrorsReceived.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelStatsErrorsReceived.setUnits(_F)
_ClabGRETunnelInterfaceTable_Object=MibTable
clabGRETunnelInterfaceTable=_ClabGRETunnelInterfaceTable_Object((1,3,6,1,4,1,4491,4,3,1,5))
if mibBuilder.loadTexts:clabGRETunnelInterfaceTable.setStatus(_A)
_ClabGRETunnelInterfaceEntry_Object=MibTableRow
clabGRETunnelInterfaceEntry=_ClabGRETunnelInterfaceEntry_Object((1,3,6,1,4,1,4491,4,3,1,5,1))
clabGRETunnelInterfaceEntry.setIndexNames((0,_B,_L),(0,_B,_R))
if mibBuilder.loadTexts:clabGRETunnelInterfaceEntry.setStatus(_A)
class _ClabGRETunnelInterfaceIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_ClabGRETunnelInterfaceIndex_Type.__name__=_E
_ClabGRETunnelInterfaceIndex_Object=MibTableColumn
clabGRETunnelInterfaceIndex=_ClabGRETunnelInterfaceIndex_Object((1,3,6,1,4,1,4491,4,3,1,5,1,1),_ClabGRETunnelInterfaceIndex_Type())
clabGRETunnelInterfaceIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:clabGRETunnelInterfaceIndex.setStatus(_A)
_ClabGRETunnelInterfaceRowStatus_Type=RowStatus
_ClabGRETunnelInterfaceRowStatus_Object=MibTableColumn
clabGRETunnelInterfaceRowStatus=_ClabGRETunnelInterfaceRowStatus_Object((1,3,6,1,4,1,4491,4,3,1,5,1,2),_ClabGRETunnelInterfaceRowStatus_Type())
clabGRETunnelInterfaceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelInterfaceRowStatus.setStatus(_A)
_ClabGRETunnelInterfaceEnable_Type=TruthValue
_ClabGRETunnelInterfaceEnable_Object=MibTableColumn
clabGRETunnelInterfaceEnable=_ClabGRETunnelInterfaceEnable_Object((1,3,6,1,4,1,4491,4,3,1,5,1,3),_ClabGRETunnelInterfaceEnable_Type())
clabGRETunnelInterfaceEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelInterfaceEnable.setStatus(_A)
class _ClabGRETunnelInterfaceStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('down',1),('up',2),('unknown',3),('dormant',4),('notPresent',5),('lowerLayerDown',6),(_O,7)))
_ClabGRETunnelInterfaceStatus_Type.__name__=_G
_ClabGRETunnelInterfaceStatus_Object=MibTableColumn
clabGRETunnelInterfaceStatus=_ClabGRETunnelInterfaceStatus_Object((1,3,6,1,4,1,4491,4,3,1,5,1,4),_ClabGRETunnelInterfaceStatus_Type())
clabGRETunnelInterfaceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatus.setStatus(_A)
_ClabGRETunnelInterfaceAlias_Type=SnmpAdminString
_ClabGRETunnelInterfaceAlias_Object=MibTableColumn
clabGRETunnelInterfaceAlias=_ClabGRETunnelInterfaceAlias_Object((1,3,6,1,4,1,4491,4,3,1,5,1,5),_ClabGRETunnelInterfaceAlias_Type())
clabGRETunnelInterfaceAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelInterfaceAlias.setStatus(_A)
_ClabGRETunnelInterfaceName_Type=SnmpAdminString
_ClabGRETunnelInterfaceName_Object=MibTableColumn
clabGRETunnelInterfaceName=_ClabGRETunnelInterfaceName_Object((1,3,6,1,4,1,4491,4,3,1,5,1,6),_ClabGRETunnelInterfaceName_Type())
clabGRETunnelInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelInterfaceName.setStatus(_A)
_ClabGRETunnelInterfaceLastChange_Type=Unsigned32
_ClabGRETunnelInterfaceLastChange_Object=MibTableColumn
clabGRETunnelInterfaceLastChange=_ClabGRETunnelInterfaceLastChange_Object((1,3,6,1,4,1,4491,4,3,1,5,1,7),_ClabGRETunnelInterfaceLastChange_Type())
clabGRETunnelInterfaceLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelInterfaceLastChange.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelInterfaceLastChange.setUnits(_I)
_ClabGRETunnelInterfaceLowerLayers_Type=SnmpAdminString
_ClabGRETunnelInterfaceLowerLayers_Object=MibTableColumn
clabGRETunnelInterfaceLowerLayers=_ClabGRETunnelInterfaceLowerLayers_Object((1,3,6,1,4,1,4491,4,3,1,5,1,8),_ClabGRETunnelInterfaceLowerLayers_Type())
clabGRETunnelInterfaceLowerLayers.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelInterfaceLowerLayers.setStatus(_A)
_ClabGRETunnelInterfaceProtocolIdOverride_Type=Unsigned32
_ClabGRETunnelInterfaceProtocolIdOverride_Object=MibTableColumn
clabGRETunnelInterfaceProtocolIdOverride=_ClabGRETunnelInterfaceProtocolIdOverride_Object((1,3,6,1,4,1,4491,4,3,1,5,1,9),_ClabGRETunnelInterfaceProtocolIdOverride_Type())
clabGRETunnelInterfaceProtocolIdOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelInterfaceProtocolIdOverride.setStatus(_A)
class _ClabGRETunnelInterfaceUseChecksum_Type(TruthValue):defaultValue=2
_ClabGRETunnelInterfaceUseChecksum_Type.__name__=_H
_ClabGRETunnelInterfaceUseChecksum_Object=MibTableColumn
clabGRETunnelInterfaceUseChecksum=_ClabGRETunnelInterfaceUseChecksum_Object((1,3,6,1,4,1,4491,4,3,1,5,1,10),_ClabGRETunnelInterfaceUseChecksum_Type())
clabGRETunnelInterfaceUseChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelInterfaceUseChecksum.setStatus(_A)
class _ClabGRETunnelInterfaceKeyIdentifierGenerationPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('provisioned',2),('generated',3)))
_ClabGRETunnelInterfaceKeyIdentifierGenerationPolicy_Type.__name__=_G
_ClabGRETunnelInterfaceKeyIdentifierGenerationPolicy_Object=MibTableColumn
clabGRETunnelInterfaceKeyIdentifierGenerationPolicy=_ClabGRETunnelInterfaceKeyIdentifierGenerationPolicy_Object((1,3,6,1,4,1,4491,4,3,1,5,1,11),_ClabGRETunnelInterfaceKeyIdentifierGenerationPolicy_Type())
clabGRETunnelInterfaceKeyIdentifierGenerationPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelInterfaceKeyIdentifierGenerationPolicy.setStatus(_A)
_ClabGRETunnelInterfaceKeyIdentifier_Type=Unsigned32
_ClabGRETunnelInterfaceKeyIdentifier_Object=MibTableColumn
clabGRETunnelInterfaceKeyIdentifier=_ClabGRETunnelInterfaceKeyIdentifier_Object((1,3,6,1,4,1,4491,4,3,1,5,1,12),_ClabGRETunnelInterfaceKeyIdentifier_Type())
clabGRETunnelInterfaceKeyIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelInterfaceKeyIdentifier.setStatus(_A)
class _ClabGRETunnelInterfaceUseSequenceNumber_Type(TruthValue):defaultValue=2
_ClabGRETunnelInterfaceUseSequenceNumber_Type.__name__=_H
_ClabGRETunnelInterfaceUseSequenceNumber_Object=MibTableColumn
clabGRETunnelInterfaceUseSequenceNumber=_ClabGRETunnelInterfaceUseSequenceNumber_Object((1,3,6,1,4,1,4491,4,3,1,5,1,13),_ClabGRETunnelInterfaceUseSequenceNumber_Type())
clabGRETunnelInterfaceUseSequenceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGRETunnelInterfaceUseSequenceNumber.setStatus(_A)
_ClabGRETunnelInterfaceStatsTable_Object=MibTable
clabGRETunnelInterfaceStatsTable=_ClabGRETunnelInterfaceStatsTable_Object((1,3,6,1,4,1,4491,4,3,1,6))
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsTable.setStatus(_A)
_ClabGRETunnelInterfaceStatsEntry_Object=MibTableRow
clabGRETunnelInterfaceStatsEntry=_ClabGRETunnelInterfaceStatsEntry_Object((1,3,6,1,4,1,4491,4,3,1,6,1))
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsEntry.setStatus(_A)
_ClabGRETunnelInterfaceStatsBytesSent_Type=Counter64
_ClabGRETunnelInterfaceStatsBytesSent_Object=MibTableColumn
clabGRETunnelInterfaceStatsBytesSent=_ClabGRETunnelInterfaceStatsBytesSent_Object((1,3,6,1,4,1,4491,4,3,1,6,1,1),_ClabGRETunnelInterfaceStatsBytesSent_Type())
clabGRETunnelInterfaceStatsBytesSent.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsBytesSent.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsBytesSent.setUnits(_J)
_ClabGRETunnelInterfaceStatsBytesReceived_Type=Counter64
_ClabGRETunnelInterfaceStatsBytesReceived_Object=MibTableColumn
clabGRETunnelInterfaceStatsBytesReceived=_ClabGRETunnelInterfaceStatsBytesReceived_Object((1,3,6,1,4,1,4491,4,3,1,6,1,2),_ClabGRETunnelInterfaceStatsBytesReceived_Type())
clabGRETunnelInterfaceStatsBytesReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsBytesReceived.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsBytesReceived.setUnits(_J)
_ClabGRETunnelInterfaceStatsPacketsSent_Type=Counter64
_ClabGRETunnelInterfaceStatsPacketsSent_Object=MibTableColumn
clabGRETunnelInterfaceStatsPacketsSent=_ClabGRETunnelInterfaceStatsPacketsSent_Object((1,3,6,1,4,1,4491,4,3,1,6,1,3),_ClabGRETunnelInterfaceStatsPacketsSent_Type())
clabGRETunnelInterfaceStatsPacketsSent.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsPacketsSent.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsPacketsSent.setUnits(_F)
_ClabGRETunnelInterfaceStatsPacketsReceived_Type=Counter64
_ClabGRETunnelInterfaceStatsPacketsReceived_Object=MibTableColumn
clabGRETunnelInterfaceStatsPacketsReceived=_ClabGRETunnelInterfaceStatsPacketsReceived_Object((1,3,6,1,4,1,4491,4,3,1,6,1,4),_ClabGRETunnelInterfaceStatsPacketsReceived_Type())
clabGRETunnelInterfaceStatsPacketsReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsPacketsReceived.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsPacketsReceived.setUnits(_F)
_ClabGRETunnelInterfaceStatsErrorsSent_Type=Counter64
_ClabGRETunnelInterfaceStatsErrorsSent_Object=MibTableColumn
clabGRETunnelInterfaceStatsErrorsSent=_ClabGRETunnelInterfaceStatsErrorsSent_Object((1,3,6,1,4,1,4491,4,3,1,6,1,5),_ClabGRETunnelInterfaceStatsErrorsSent_Type())
clabGRETunnelInterfaceStatsErrorsSent.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsErrorsSent.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsErrorsSent.setUnits(_F)
_ClabGRETunnelInterfaceStatsErrorsReceived_Type=Counter64
_ClabGRETunnelInterfaceStatsErrorsReceived_Object=MibTableColumn
clabGRETunnelInterfaceStatsErrorsReceived=_ClabGRETunnelInterfaceStatsErrorsReceived_Object((1,3,6,1,4,1,4491,4,3,1,6,1,6),_ClabGRETunnelInterfaceStatsErrorsReceived_Type())
clabGRETunnelInterfaceStatsErrorsReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsErrorsReceived.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsErrorsReceived.setUnits(_F)
_ClabGRETunnelInterfaceStatsDiscardChecksumReceived_Type=Counter64
_ClabGRETunnelInterfaceStatsDiscardChecksumReceived_Object=MibTableColumn
clabGRETunnelInterfaceStatsDiscardChecksumReceived=_ClabGRETunnelInterfaceStatsDiscardChecksumReceived_Object((1,3,6,1,4,1,4491,4,3,1,6,1,7),_ClabGRETunnelInterfaceStatsDiscardChecksumReceived_Type())
clabGRETunnelInterfaceStatsDiscardChecksumReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsDiscardChecksumReceived.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsDiscardChecksumReceived.setUnits(_F)
_ClabGRETunnelInterfaceStatsDiscardSequenceNumberReceived_Type=Counter64
_ClabGRETunnelInterfaceStatsDiscardSequenceNumberReceived_Object=MibTableColumn
clabGRETunnelInterfaceStatsDiscardSequenceNumberReceived=_ClabGRETunnelInterfaceStatsDiscardSequenceNumberReceived_Object((1,3,6,1,4,1,4491,4,3,1,6,1,8),_ClabGRETunnelInterfaceStatsDiscardSequenceNumberReceived_Type())
clabGRETunnelInterfaceStatsDiscardSequenceNumberReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsDiscardSequenceNumberReceived.setStatus(_A)
if mibBuilder.loadTexts:clabGRETunnelInterfaceStatsDiscardSequenceNumberReceived.setUnits(_F)
_ClabGREFilterTable_Object=MibTable
clabGREFilterTable=_ClabGREFilterTable_Object((1,3,6,1,4,1,4491,4,3,1,7))
if mibBuilder.loadTexts:clabGREFilterTable.setStatus(_A)
_ClabGREFilterEntry_Object=MibTableRow
clabGREFilterEntry=_ClabGREFilterEntry_Object((1,3,6,1,4,1,4491,4,3,1,7,1))
clabGREFilterEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:clabGREFilterEntry.setStatus(_A)
class _ClabGREFilterIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_ClabGREFilterIndex_Type.__name__=_E
_ClabGREFilterIndex_Object=MibTableColumn
clabGREFilterIndex=_ClabGREFilterIndex_Object((1,3,6,1,4,1,4491,4,3,1,7,1,1),_ClabGREFilterIndex_Type())
clabGREFilterIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:clabGREFilterIndex.setStatus(_A)
_ClabGREFilterRowStatus_Type=RowStatus
_ClabGREFilterRowStatus_Object=MibTableColumn
clabGREFilterRowStatus=_ClabGREFilterRowStatus_Object((1,3,6,1,4,1,4491,4,3,1,7,1,2),_ClabGREFilterRowStatus_Type())
clabGREFilterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGREFilterRowStatus.setStatus(_A)
class _ClabGREFilterEnable_Type(TruthValue):defaultValue=2
_ClabGREFilterEnable_Type.__name__=_H
_ClabGREFilterEnable_Object=MibTableColumn
clabGREFilterEnable=_ClabGREFilterEnable_Object((1,3,6,1,4,1,4491,4,3,1,7,1,3),_ClabGREFilterEnable_Type())
clabGREFilterEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGREFilterEnable.setStatus(_A)
class _ClabGREFilterStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_P,2),(_Q,3),(_O,4)))
_ClabGREFilterStatus_Type.__name__=_G
_ClabGREFilterStatus_Object=MibTableColumn
clabGREFilterStatus=_ClabGREFilterStatus_Object((1,3,6,1,4,1,4491,4,3,1,7,1,4),_ClabGREFilterStatus_Type())
clabGREFilterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGREFilterStatus.setStatus(_A)
class _ClabGREFilterOrder_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_ClabGREFilterOrder_Type.__name__=_E
_ClabGREFilterOrder_Object=MibTableColumn
clabGREFilterOrder=_ClabGREFilterOrder_Object((1,3,6,1,4,1,4491,4,3,1,7,1,5),_ClabGREFilterOrder_Type())
clabGREFilterOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGREFilterOrder.setStatus(_A)
_ClabGREFilterAlias_Type=SnmpAdminString
_ClabGREFilterAlias_Object=MibTableColumn
clabGREFilterAlias=_ClabGREFilterAlias_Object((1,3,6,1,4,1,4491,4,3,1,7,1,6),_ClabGREFilterAlias_Type())
clabGREFilterAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGREFilterAlias.setStatus(_A)
_ClabGREFilterInterface_Type=SnmpAdminString
_ClabGREFilterInterface_Object=MibTableColumn
clabGREFilterInterface=_ClabGREFilterInterface_Object((1,3,6,1,4,1,4491,4,3,1,7,1,7),_ClabGREFilterInterface_Type())
clabGREFilterInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGREFilterInterface.setStatus(_A)
_ClabGREFilterAllInterfaces_Type=TruthValue
_ClabGREFilterAllInterfaces_Object=MibTableColumn
clabGREFilterAllInterfaces=_ClabGREFilterAllInterfaces_Object((1,3,6,1,4,1,4491,4,3,1,7,1,8),_ClabGREFilterAllInterfaces_Type())
clabGREFilterAllInterfaces.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGREFilterAllInterfaces.setStatus(_A)
class _ClabGREFilterVlanIdCheck_Type(Integer32):defaultValue=-1
_ClabGREFilterVlanIdCheck_Type.__name__=_G
_ClabGREFilterVlanIdCheck_Object=MibTableColumn
clabGREFilterVlanIdCheck=_ClabGREFilterVlanIdCheck_Object((1,3,6,1,4,1,4491,4,3,1,7,1,9),_ClabGREFilterVlanIdCheck_Type())
clabGREFilterVlanIdCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGREFilterVlanIdCheck.setStatus(_A)
class _ClabGREFilterVlanIdExclude_Type(TruthValue):defaultValue=2
_ClabGREFilterVlanIdExclude_Type.__name__=_H
_ClabGREFilterVlanIdExclude_Object=MibTableColumn
clabGREFilterVlanIdExclude=_ClabGREFilterVlanIdExclude_Object((1,3,6,1,4,1,4491,4,3,1,7,1,10),_ClabGREFilterVlanIdExclude_Type())
clabGREFilterVlanIdExclude.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGREFilterVlanIdExclude.setStatus(_A)
class _ClabGREFilterDscpMarkPolicy_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,63))
_ClabGREFilterDscpMarkPolicy_Type.__name__=_G
_ClabGREFilterDscpMarkPolicy_Object=MibTableColumn
clabGREFilterDscpMarkPolicy=_ClabGREFilterDscpMarkPolicy_Object((1,3,6,1,4,1,4491,4,3,1,7,1,11),_ClabGREFilterDscpMarkPolicy_Type())
clabGREFilterDscpMarkPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGREFilterDscpMarkPolicy.setStatus(_A)
class _ClabGREFilterVlanTag_Type(Unsigned32):defaultValue=0
_ClabGREFilterVlanTag_Type.__name__=_E
_ClabGREFilterVlanTag_Object=MibTableColumn
clabGREFilterVlanTag=_ClabGREFilterVlanTag_Object((1,3,6,1,4,1,4491,4,3,1,7,1,12),_ClabGREFilterVlanTag_Type())
clabGREFilterVlanTag.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGREFilterVlanTag.setStatus(_A)
_ClabGREMibConformance_ObjectIdentity=ObjectIdentity
clabGREMibConformance=_ClabGREMibConformance_ObjectIdentity((1,3,6,1,4,1,4491,4,3,2))
_ClabGREMibCompliances_ObjectIdentity=ObjectIdentity
clabGREMibCompliances=_ClabGREMibCompliances_ObjectIdentity((1,3,6,1,4,1,4491,4,3,2,1))
_ClabGREMibGroups_ObjectIdentity=ObjectIdentity
clabGREMibGroups=_ClabGREMibGroups_ObjectIdentity((1,3,6,1,4,1,4491,4,3,2,2))
clabGRETunnelEntry.registerAugmentions((_B,_T))
clabGRETunnelStatsEntry.setIndexNames(*clabGRETunnelEntry.getIndexNames())
clabGRETunnelInterfaceEntry.registerAugmentions((_B,_U))
clabGRETunnelInterfaceStatsEntry.setIndexNames(*clabGRETunnelInterfaceEntry.getIndexNames())
clabGREGroup=ObjectGroup((1,3,6,1,4,1,4491,4,3,2,2,1))
clabGREGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:clabGREGroup.setStatus(_A)
clabGRECompliance=ModuleCompliance((1,3,6,1,4,1,4491,4,3,2,1,1))
clabGRECompliance.setObjects((_B,_AT))
if mibBuilder.loadTexts:clabGRECompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'clabGREMib':clabGREMib,'clabGREObjects':clabGREObjects,_V:clabGRETunnelNumberOfEntries,_W:clabGREFilterNumberOfEntries,'clabGRETunnelTable':clabGRETunnelTable,'clabGRETunnelEntry':clabGRETunnelEntry,_L:clabGRETunnelIndex,_X:clabGRETunnelRowStatus,_Y:clabGRETunnelEnable,_Z:clabGRETunnelStatus,_a:clabGRETunnelAlias,_b:clabGRETunnelRemoteEndpoints,_c:clabGRETunnelKeepAlivePolicy,_d:clabGRETunnelKeepAliveTimeout,_e:clabGRETunnelKeepAliveThreshold,_f:clabGRETunnelKeepAliveCount,_g:clabGRETunnelKeepAliveInterval,_h:clabGRETunnelKeepAliveFailureInterval,_i:clabGRETunnelKeepAliveRecoverInterval,_j:clabGRETunnelDeliveryHeaderProtocol,_k:clabGRETunnelDefaultDscpMark,_l:clabGRETunnelConnectedRemoteEndpoint,_m:clabGRETunnelInterfaceNumberOfEntries,_n:clabGRETunnelTcpMssClamping,_o:clabGRETunnelConcentratorServiceName,_p:clabGRETunnnelRemoteEndpointConnectivityState,'clabGRETunnelStatsTable':clabGRETunnelStatsTable,_T:clabGRETunnelStatsEntry,_q:clabGRETunnelStatsKeepAliveSent,_r:clabGRETunnelStatsKeepAliveReceived,_s:clabGRETunnelStatsBytesSent,_t:clabGRETunnelStatsBytesReceived,_u:clabGRETunnelStatsPacketsSent,_v:clabGRETunnelStatsPacketsReceived,_w:clabGRETunnelStatsErrorsSent,_x:clabGRETunnelStatsErrorsReceived,'clabGRETunnelInterfaceTable':clabGRETunnelInterfaceTable,'clabGRETunnelInterfaceEntry':clabGRETunnelInterfaceEntry,_R:clabGRETunnelInterfaceIndex,_y:clabGRETunnelInterfaceRowStatus,_A4:clabGRETunnelInterfaceEnable,_z:clabGRETunnelInterfaceStatus,_A0:clabGRETunnelInterfaceAlias,_A1:clabGRETunnelInterfaceName,_A2:clabGRETunnelInterfaceLastChange,_A3:clabGRETunnelInterfaceLowerLayers,_A5:clabGRETunnelInterfaceProtocolIdOverride,_A6:clabGRETunnelInterfaceUseChecksum,_A7:clabGRETunnelInterfaceKeyIdentifierGenerationPolicy,_A8:clabGRETunnelInterfaceKeyIdentifier,_A9:clabGRETunnelInterfaceUseSequenceNumber,'clabGRETunnelInterfaceStatsTable':clabGRETunnelInterfaceStatsTable,_U:clabGRETunnelInterfaceStatsEntry,_AA:clabGRETunnelInterfaceStatsBytesSent,_AB:clabGRETunnelInterfaceStatsBytesReceived,_AC:clabGRETunnelInterfaceStatsPacketsSent,_AD:clabGRETunnelInterfaceStatsPacketsReceived,_AE:clabGRETunnelInterfaceStatsErrorsSent,_AF:clabGRETunnelInterfaceStatsErrorsReceived,_AG:clabGRETunnelInterfaceStatsDiscardChecksumReceived,_AH:clabGRETunnelInterfaceStatsDiscardSequenceNumberReceived,'clabGREFilterTable':clabGREFilterTable,'clabGREFilterEntry':clabGREFilterEntry,_S:clabGREFilterIndex,_AI:clabGREFilterRowStatus,_AJ:clabGREFilterEnable,_AK:clabGREFilterStatus,_AL:clabGREFilterOrder,_AM:clabGREFilterAlias,_AN:clabGREFilterInterface,_AO:clabGREFilterAllInterfaces,_AP:clabGREFilterVlanIdCheck,_AQ:clabGREFilterVlanIdExclude,_AS:clabGREFilterDscpMarkPolicy,_AR:clabGREFilterVlanTag,'clabGREMibConformance':clabGREMibConformance,'clabGREMibCompliances':clabGREMibCompliances,'clabGRECompliance':clabGRECompliance,'clabGREMibGroups':clabGREMibGroups,_AT:clabGREGroup})