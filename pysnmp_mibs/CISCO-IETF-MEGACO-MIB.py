_A9='cmedTermGroup'
_A8='cmedNextIdGroup'
_A7='cmedGwyControllerGroup'
_A6='cmedStatsGroup'
_A5='cmedConfig'
_A4='cmedPropertyProfileRowStatus'
_A3='cmedPropertyProfileProperty'
_A2='cmedTermRowStatus'
_A1='cmedTermPropertyProfileId'
_A0='cmedTermInterfaceIdentifier'
_z='cmedTermOperStatus'
_y='cmedTermAdminStatus'
_x='cmedTermName'
_w='cmedNextLinkId'
_v='cmedNextTerminationId'
_u='cmedGwyControllerOperStatus'
_t='cmedGwyControllerAdminStatus'
_s='cmedGwyControllerPort'
_r='cmedGwyControllerIPAddress'
_q='cmedLastStatisticsReset'
_p='cmedTransportLastEventTime'
_o='cmedTransportLastEvent'
_n='cmedTransportTotalNumAlarms'
_m='cmedTransportNumSwitchover'
_l='cmedTransportNumLosses'
_k='cmedNumTimerRecovery'
_j='cmedNumErrors'
_i='cmedNumOutOctets'
_h='cmedNumOutMessages'
_g='cmedNumInOctets'
_f='cmedNumInMessages'
_e='cmedGatewayRowStatus'
_d='cmedGatewayResetStatistics'
_c='cmedGatewayLastStatusChange'
_b='cmedGatewayOperStatus'
_a='cmedGatewayAdminStatus'
_Z='cmedGatewaySigTptProtocol'
_Y='cmedGatewayProtocol'
_X='cmedGatewayEncodingScheme'
_W='cmedGatewayPort'
_V='cmedGatewayIPAddress'
_U='cmedGatewayLinkName'
_T='cmedPropertyProfileIndex'
_S='cmedPropertyProfileId'
_R='cmedTermId'
_Q='cmedGwyControllerId'
_P='notApplicable'
_O='SnmpAdminString'
_N='other'
_M='cmedGatewayLinkId'
_L='testing'
_K='down'
_J='up'
_I='read-write'
_H='Unsigned32'
_G='not-accessible'
_F='cmedGatewayId'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='CISCO-IETF-MEGACO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
AutonomousType,DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp')
ciscoIetfMegacoMIB=ModuleIdentity((1,3,6,1,4,1,9,10,99999))
if mibBuilder.loadTexts:ciscoIetfMegacoMIB.setRevisions(('2003-04-28 12:00',))
class CMediaGatewayId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class CMediaGatewayLinkId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class CMediaGatewayTermId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CiscoIetfMegacoMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIetfMegacoMIBNotifs=_CiscoIetfMegacoMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,10,99999,0))
_CiscoIetfMegacoMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIetfMegacoMIBObjects=_CiscoIetfMegacoMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,99999,1))
_CmedConfiguration_ObjectIdentity=ObjectIdentity
cmedConfiguration=_CmedConfiguration_ObjectIdentity((1,3,6,1,4,1,9,10,99999,1,1))
_CmedLinkIdTable_Object=MibTable
cmedLinkIdTable=_CmedLinkIdTable_Object((1,3,6,1,4,1,9,10,99999,1,1,1))
if mibBuilder.loadTexts:cmedLinkIdTable.setStatus(_A)
_CmedLinkIdEntry_Object=MibTableRow
cmedLinkIdEntry=_CmedLinkIdEntry_Object((1,3,6,1,4,1,9,10,99999,1,1,1,1))
cmedLinkIdEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cmedLinkIdEntry.setStatus(_A)
_CmedNextLinkId_Type=TestAndIncr
_CmedNextLinkId_Object=MibTableColumn
cmedNextLinkId=_CmedNextLinkId_Object((1,3,6,1,4,1,9,10,99999,1,1,1,1,1),_CmedNextLinkId_Type())
cmedNextLinkId.setMaxAccess(_I)
if mibBuilder.loadTexts:cmedNextLinkId.setStatus(_A)
_CmedGatewayConfigTable_Object=MibTable
cmedGatewayConfigTable=_CmedGatewayConfigTable_Object((1,3,6,1,4,1,9,10,99999,1,1,2))
if mibBuilder.loadTexts:cmedGatewayConfigTable.setStatus(_A)
_CmedGatewayConfigEntry_Object=MibTableRow
cmedGatewayConfigEntry=_CmedGatewayConfigEntry_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1))
cmedGatewayConfigEntry.setIndexNames((0,_B,_F),(0,_B,_M))
if mibBuilder.loadTexts:cmedGatewayConfigEntry.setStatus(_A)
_CmedGatewayId_Type=CMediaGatewayId
_CmedGatewayId_Object=MibTableColumn
cmedGatewayId=_CmedGatewayId_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1,1),_CmedGatewayId_Type())
cmedGatewayId.setMaxAccess(_G)
if mibBuilder.loadTexts:cmedGatewayId.setStatus(_A)
_CmedGatewayLinkId_Type=CMediaGatewayLinkId
_CmedGatewayLinkId_Object=MibTableColumn
cmedGatewayLinkId=_CmedGatewayLinkId_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1,2),_CmedGatewayLinkId_Type())
cmedGatewayLinkId.setMaxAccess(_G)
if mibBuilder.loadTexts:cmedGatewayLinkId.setStatus(_A)
class _CmedGatewayLinkName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CmedGatewayLinkName_Type.__name__=_O
_CmedGatewayLinkName_Object=MibTableColumn
cmedGatewayLinkName=_CmedGatewayLinkName_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1,3),_CmedGatewayLinkName_Type())
cmedGatewayLinkName.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedGatewayLinkName.setStatus(_A)
_CmedGatewayIPAddress_Type=IpAddress
_CmedGatewayIPAddress_Object=MibTableColumn
cmedGatewayIPAddress=_CmedGatewayIPAddress_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1,4),_CmedGatewayIPAddress_Type())
cmedGatewayIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedGatewayIPAddress.setStatus(_A)
class _CmedGatewayPort_Type(Integer32):defaultValue=2944;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CmedGatewayPort_Type.__name__=_E
_CmedGatewayPort_Object=MibTableColumn
cmedGatewayPort=_CmedGatewayPort_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1,5),_CmedGatewayPort_Type())
cmedGatewayPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedGatewayPort.setStatus(_A)
class _CmedGatewayEncodingScheme_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('text',1),('binary',2)))
_CmedGatewayEncodingScheme_Type.__name__=_E
_CmedGatewayEncodingScheme_Object=MibTableColumn
cmedGatewayEncodingScheme=_CmedGatewayEncodingScheme_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1,6),_CmedGatewayEncodingScheme_Type())
cmedGatewayEncodingScheme.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedGatewayEncodingScheme.setStatus(_A)
class _CmedGatewayProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,1),(_N,2),('dss1Ip',3),('ipdc',4),('megacov1',5),('megacov2',6),('mgcp',7)))
_CmedGatewayProtocol_Type.__name__=_E
_CmedGatewayProtocol_Object=MibTableColumn
cmedGatewayProtocol=_CmedGatewayProtocol_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1,7),_CmedGatewayProtocol_Type())
cmedGatewayProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedGatewayProtocol.setStatus(_A)
class _CmedGatewaySigTptProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tcp',1),('udp',2),('sctp',3),(_N,4)))
_CmedGatewaySigTptProtocol_Type.__name__=_E
_CmedGatewaySigTptProtocol_Object=MibTableColumn
cmedGatewaySigTptProtocol=_CmedGatewaySigTptProtocol_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1,8),_CmedGatewaySigTptProtocol_Type())
cmedGatewaySigTptProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedGatewaySigTptProtocol.setStatus(_A)
class _CmedGatewayAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_CmedGatewayAdminStatus_Type.__name__=_E
_CmedGatewayAdminStatus_Object=MibTableColumn
cmedGatewayAdminStatus=_CmedGatewayAdminStatus_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1,9),_CmedGatewayAdminStatus_Type())
cmedGatewayAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedGatewayAdminStatus.setStatus(_A)
class _CmedGatewayOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),('unknown',4)))
_CmedGatewayOperStatus_Type.__name__=_E
_CmedGatewayOperStatus_Object=MibTableColumn
cmedGatewayOperStatus=_CmedGatewayOperStatus_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1,10),_CmedGatewayOperStatus_Type())
cmedGatewayOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedGatewayOperStatus.setStatus(_A)
_CmedGatewayLastStatusChange_Type=TimeStamp
_CmedGatewayLastStatusChange_Object=MibTableColumn
cmedGatewayLastStatusChange=_CmedGatewayLastStatusChange_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1,11),_CmedGatewayLastStatusChange_Type())
cmedGatewayLastStatusChange.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedGatewayLastStatusChange.setStatus(_A)
class _CmedGatewayResetStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_N,2),('reset',3)))
_CmedGatewayResetStatistics_Type.__name__=_E
_CmedGatewayResetStatistics_Object=MibTableColumn
cmedGatewayResetStatistics=_CmedGatewayResetStatistics_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1,12),_CmedGatewayResetStatistics_Type())
cmedGatewayResetStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedGatewayResetStatistics.setStatus(_A)
_CmedGatewayRowStatus_Type=RowStatus
_CmedGatewayRowStatus_Object=MibTableColumn
cmedGatewayRowStatus=_CmedGatewayRowStatus_Object((1,3,6,1,4,1,9,10,99999,1,1,2,1,13),_CmedGatewayRowStatus_Type())
cmedGatewayRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedGatewayRowStatus.setStatus(_A)
_CmedGwyControllerTable_Object=MibTable
cmedGwyControllerTable=_CmedGwyControllerTable_Object((1,3,6,1,4,1,9,10,99999,1,1,3))
if mibBuilder.loadTexts:cmedGwyControllerTable.setStatus(_A)
_CmedGwyControllerEntry_Object=MibTableRow
cmedGwyControllerEntry=_CmedGwyControllerEntry_Object((1,3,6,1,4,1,9,10,99999,1,1,3,1))
cmedGwyControllerEntry.setIndexNames((0,_B,_F),(0,_B,_M),(0,_B,_Q))
if mibBuilder.loadTexts:cmedGwyControllerEntry.setStatus(_A)
class _CmedGwyControllerId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CmedGwyControllerId_Type.__name__=_H
_CmedGwyControllerId_Object=MibTableColumn
cmedGwyControllerId=_CmedGwyControllerId_Object((1,3,6,1,4,1,9,10,99999,1,1,3,1,1),_CmedGwyControllerId_Type())
cmedGwyControllerId.setMaxAccess(_G)
if mibBuilder.loadTexts:cmedGwyControllerId.setStatus(_A)
_CmedGwyControllerIPAddress_Type=IpAddress
_CmedGwyControllerIPAddress_Object=MibTableColumn
cmedGwyControllerIPAddress=_CmedGwyControllerIPAddress_Object((1,3,6,1,4,1,9,10,99999,1,1,3,1,2),_CmedGwyControllerIPAddress_Type())
cmedGwyControllerIPAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:cmedGwyControllerIPAddress.setStatus(_A)
class _CmedGwyControllerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CmedGwyControllerPort_Type.__name__=_E
_CmedGwyControllerPort_Object=MibTableColumn
cmedGwyControllerPort=_CmedGwyControllerPort_Object((1,3,6,1,4,1,9,10,99999,1,1,3,1,3),_CmedGwyControllerPort_Type())
cmedGwyControllerPort.setMaxAccess(_I)
if mibBuilder.loadTexts:cmedGwyControllerPort.setStatus(_A)
class _CmedGwyControllerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_CmedGwyControllerAdminStatus_Type.__name__=_E
_CmedGwyControllerAdminStatus_Object=MibTableColumn
cmedGwyControllerAdminStatus=_CmedGwyControllerAdminStatus_Object((1,3,6,1,4,1,9,10,99999,1,1,3,1,4),_CmedGwyControllerAdminStatus_Type())
cmedGwyControllerAdminStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:cmedGwyControllerAdminStatus.setStatus(_A)
class _CmedGwyControllerOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),('standby',3)))
_CmedGwyControllerOperStatus_Type.__name__=_E
_CmedGwyControllerOperStatus_Object=MibTableColumn
cmedGwyControllerOperStatus=_CmedGwyControllerOperStatus_Object((1,3,6,1,4,1,9,10,99999,1,1,3,1,5),_CmedGwyControllerOperStatus_Type())
cmedGwyControllerOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedGwyControllerOperStatus.setStatus(_A)
_CmedStatistics_ObjectIdentity=ObjectIdentity
cmedStatistics=_CmedStatistics_ObjectIdentity((1,3,6,1,4,1,9,10,99999,1,2))
_CmedGatewayStatsTable_Object=MibTable
cmedGatewayStatsTable=_CmedGatewayStatsTable_Object((1,3,6,1,4,1,9,10,99999,1,2,1))
if mibBuilder.loadTexts:cmedGatewayStatsTable.setStatus(_A)
_CmedGatewayStatsEntry_Object=MibTableRow
cmedGatewayStatsEntry=_CmedGatewayStatsEntry_Object((1,3,6,1,4,1,9,10,99999,1,2,1,1))
cmedGatewayStatsEntry.setIndexNames((0,_B,_F),(0,_B,_M))
if mibBuilder.loadTexts:cmedGatewayStatsEntry.setStatus(_A)
_CmedNumInMessages_Type=Counter32
_CmedNumInMessages_Object=MibTableColumn
cmedNumInMessages=_CmedNumInMessages_Object((1,3,6,1,4,1,9,10,99999,1,2,1,1,1),_CmedNumInMessages_Type())
cmedNumInMessages.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedNumInMessages.setStatus(_A)
_CmedNumInOctets_Type=Counter32
_CmedNumInOctets_Object=MibTableColumn
cmedNumInOctets=_CmedNumInOctets_Object((1,3,6,1,4,1,9,10,99999,1,2,1,1,2),_CmedNumInOctets_Type())
cmedNumInOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedNumInOctets.setStatus(_A)
_CmedNumOutMessages_Type=Counter32
_CmedNumOutMessages_Object=MibTableColumn
cmedNumOutMessages=_CmedNumOutMessages_Object((1,3,6,1,4,1,9,10,99999,1,2,1,1,3),_CmedNumOutMessages_Type())
cmedNumOutMessages.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedNumOutMessages.setStatus(_A)
_CmedNumOutOctets_Type=Counter32
_CmedNumOutOctets_Object=MibTableColumn
cmedNumOutOctets=_CmedNumOutOctets_Object((1,3,6,1,4,1,9,10,99999,1,2,1,1,4),_CmedNumOutOctets_Type())
cmedNumOutOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedNumOutOctets.setStatus(_A)
_CmedNumErrors_Type=Counter32
_CmedNumErrors_Object=MibTableColumn
cmedNumErrors=_CmedNumErrors_Object((1,3,6,1,4,1,9,10,99999,1,2,1,1,5),_CmedNumErrors_Type())
cmedNumErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedNumErrors.setStatus(_A)
_CmedNumTimerRecovery_Type=Counter32
_CmedNumTimerRecovery_Object=MibTableColumn
cmedNumTimerRecovery=_CmedNumTimerRecovery_Object((1,3,6,1,4,1,9,10,99999,1,2,1,1,6),_CmedNumTimerRecovery_Type())
cmedNumTimerRecovery.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedNumTimerRecovery.setStatus(_A)
_CmedTransportNumLosses_Type=Counter32
_CmedTransportNumLosses_Object=MibTableColumn
cmedTransportNumLosses=_CmedTransportNumLosses_Object((1,3,6,1,4,1,9,10,99999,1,2,1,1,7),_CmedTransportNumLosses_Type())
cmedTransportNumLosses.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedTransportNumLosses.setStatus(_A)
_CmedTransportNumSwitchover_Type=Counter32
_CmedTransportNumSwitchover_Object=MibTableColumn
cmedTransportNumSwitchover=_CmedTransportNumSwitchover_Object((1,3,6,1,4,1,9,10,99999,1,2,1,1,8),_CmedTransportNumSwitchover_Type())
cmedTransportNumSwitchover.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedTransportNumSwitchover.setStatus(_A)
_CmedTransportTotalNumAlarms_Type=Counter32
_CmedTransportTotalNumAlarms_Object=MibTableColumn
cmedTransportTotalNumAlarms=_CmedTransportTotalNumAlarms_Object((1,3,6,1,4,1,9,10,99999,1,2,1,1,9),_CmedTransportTotalNumAlarms_Type())
cmedTransportTotalNumAlarms.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedTransportTotalNumAlarms.setStatus(_A)
class _CmedTransportLastEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,1),(_N,2),('linkUp',3),('linkLoss',4),('persistentError',5),('linkShutdown',6),('switchOver',7)))
_CmedTransportLastEvent_Type.__name__=_E
_CmedTransportLastEvent_Object=MibTableColumn
cmedTransportLastEvent=_CmedTransportLastEvent_Object((1,3,6,1,4,1,9,10,99999,1,2,1,1,10),_CmedTransportLastEvent_Type())
cmedTransportLastEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedTransportLastEvent.setStatus(_A)
_CmedTransportLastEventTime_Type=TimeStamp
_CmedTransportLastEventTime_Object=MibTableColumn
cmedTransportLastEventTime=_CmedTransportLastEventTime_Object((1,3,6,1,4,1,9,10,99999,1,2,1,1,11),_CmedTransportLastEventTime_Type())
cmedTransportLastEventTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedTransportLastEventTime.setStatus(_A)
_CmedLastStatisticsReset_Type=TimeStamp
_CmedLastStatisticsReset_Object=MibTableColumn
cmedLastStatisticsReset=_CmedLastStatisticsReset_Object((1,3,6,1,4,1,9,10,99999,1,2,1,1,12),_CmedLastStatisticsReset_Type())
cmedLastStatisticsReset.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedLastStatisticsReset.setStatus(_A)
_CmedConnections_ObjectIdentity=ObjectIdentity
cmedConnections=_CmedConnections_ObjectIdentity((1,3,6,1,4,1,9,10,99999,1,3))
_CmedTermIdTable_Object=MibTable
cmedTermIdTable=_CmedTermIdTable_Object((1,3,6,1,4,1,9,10,99999,1,3,1))
if mibBuilder.loadTexts:cmedTermIdTable.setStatus(_A)
_CmedTermIdEntry_Object=MibTableRow
cmedTermIdEntry=_CmedTermIdEntry_Object((1,3,6,1,4,1,9,10,99999,1,3,1,1))
cmedTermIdEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cmedTermIdEntry.setStatus(_A)
_CmedNextTerminationId_Type=TestAndIncr
_CmedNextTerminationId_Object=MibTableColumn
cmedNextTerminationId=_CmedNextTerminationId_Object((1,3,6,1,4,1,9,10,99999,1,3,1,1,1),_CmedNextTerminationId_Type())
cmedNextTerminationId.setMaxAccess(_I)
if mibBuilder.loadTexts:cmedNextTerminationId.setStatus(_A)
_CmedTerminationsTable_Object=MibTable
cmedTerminationsTable=_CmedTerminationsTable_Object((1,3,6,1,4,1,9,10,99999,1,3,2))
if mibBuilder.loadTexts:cmedTerminationsTable.setStatus(_A)
_CmedTerminationsEntry_Object=MibTableRow
cmedTerminationsEntry=_CmedTerminationsEntry_Object((1,3,6,1,4,1,9,10,99999,1,3,2,1))
cmedTerminationsEntry.setIndexNames((0,_B,_F),(0,_B,_R))
if mibBuilder.loadTexts:cmedTerminationsEntry.setStatus(_A)
_CmedTermId_Type=CMediaGatewayTermId
_CmedTermId_Object=MibTableColumn
cmedTermId=_CmedTermId_Object((1,3,6,1,4,1,9,10,99999,1,3,2,1,1),_CmedTermId_Type())
cmedTermId.setMaxAccess(_G)
if mibBuilder.loadTexts:cmedTermId.setStatus(_A)
class _CmedTermName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmedTermName_Type.__name__=_O
_CmedTermName_Object=MibTableColumn
cmedTermName=_CmedTermName_Object((1,3,6,1,4,1,9,10,99999,1,3,2,1,2),_CmedTermName_Type())
cmedTermName.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedTermName.setStatus(_A)
class _CmedTermAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inService',1),('outOfService',2),(_L,3)))
_CmedTermAdminStatus_Type.__name__=_E
_CmedTermAdminStatus_Object=MibTableColumn
cmedTermAdminStatus=_CmedTermAdminStatus_Object((1,3,6,1,4,1,9,10,99999,1,3,2,1,3),_CmedTermAdminStatus_Type())
cmedTermAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedTermAdminStatus.setStatus(_A)
class _CmedTermOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_CmedTermOperStatus_Type.__name__=_E
_CmedTermOperStatus_Object=MibTableColumn
cmedTermOperStatus=_CmedTermOperStatus_Object((1,3,6,1,4,1,9,10,99999,1,3,2,1,4),_CmedTermOperStatus_Type())
cmedTermOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cmedTermOperStatus.setStatus(_A)
_CmedTermInterfaceIdentifier_Type=InterfaceIndex
_CmedTermInterfaceIdentifier_Object=MibTableColumn
cmedTermInterfaceIdentifier=_CmedTermInterfaceIdentifier_Object((1,3,6,1,4,1,9,10,99999,1,3,2,1,5),_CmedTermInterfaceIdentifier_Type())
cmedTermInterfaceIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedTermInterfaceIdentifier.setStatus(_A)
class _CmedTermPropertyProfileId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CmedTermPropertyProfileId_Type.__name__=_H
_CmedTermPropertyProfileId_Object=MibTableColumn
cmedTermPropertyProfileId=_CmedTermPropertyProfileId_Object((1,3,6,1,4,1,9,10,99999,1,3,2,1,6),_CmedTermPropertyProfileId_Type())
cmedTermPropertyProfileId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedTermPropertyProfileId.setStatus(_A)
_CmedTermRowStatus_Type=RowStatus
_CmedTermRowStatus_Object=MibTableColumn
cmedTermRowStatus=_CmedTermRowStatus_Object((1,3,6,1,4,1,9,10,99999,1,3,2,1,7),_CmedTermRowStatus_Type())
cmedTermRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedTermRowStatus.setStatus(_A)
_CmedPropertyProfileTable_Object=MibTable
cmedPropertyProfileTable=_CmedPropertyProfileTable_Object((1,3,6,1,4,1,9,10,99999,1,3,3))
if mibBuilder.loadTexts:cmedPropertyProfileTable.setStatus(_A)
_CmedPropertyProfileEntry_Object=MibTableRow
cmedPropertyProfileEntry=_CmedPropertyProfileEntry_Object((1,3,6,1,4,1,9,10,99999,1,3,3,1))
cmedPropertyProfileEntry.setIndexNames((0,_B,_F),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:cmedPropertyProfileEntry.setStatus(_A)
class _CmedPropertyProfileId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CmedPropertyProfileId_Type.__name__=_H
_CmedPropertyProfileId_Object=MibTableColumn
cmedPropertyProfileId=_CmedPropertyProfileId_Object((1,3,6,1,4,1,9,10,99999,1,3,3,1,1),_CmedPropertyProfileId_Type())
cmedPropertyProfileId.setMaxAccess(_G)
if mibBuilder.loadTexts:cmedPropertyProfileId.setStatus(_A)
class _CmedPropertyProfileIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CmedPropertyProfileIndex_Type.__name__=_H
_CmedPropertyProfileIndex_Object=MibTableColumn
cmedPropertyProfileIndex=_CmedPropertyProfileIndex_Object((1,3,6,1,4,1,9,10,99999,1,3,3,1,2),_CmedPropertyProfileIndex_Type())
cmedPropertyProfileIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cmedPropertyProfileIndex.setStatus(_A)
_CmedPropertyProfileProperty_Type=AutonomousType
_CmedPropertyProfileProperty_Object=MibTableColumn
cmedPropertyProfileProperty=_CmedPropertyProfileProperty_Object((1,3,6,1,4,1,9,10,99999,1,3,3,1,3),_CmedPropertyProfileProperty_Type())
cmedPropertyProfileProperty.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedPropertyProfileProperty.setStatus(_A)
_CmedPropertyProfileRowStatus_Type=RowStatus
_CmedPropertyProfileRowStatus_Object=MibTableColumn
cmedPropertyProfileRowStatus=_CmedPropertyProfileRowStatus_Object((1,3,6,1,4,1,9,10,99999,1,3,3,1,4),_CmedPropertyProfileRowStatus_Type())
cmedPropertyProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmedPropertyProfileRowStatus.setStatus(_A)
_CmedProperties_ObjectIdentity=ObjectIdentity
cmedProperties=_CmedProperties_ObjectIdentity((1,3,6,1,4,1,9,10,99999,1,4))
_CiscoIetfMegacoMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIetfMegacoMIBConformance=_CiscoIetfMegacoMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,99999,3))
_CmedCompliances_ObjectIdentity=ObjectIdentity
cmedCompliances=_CmedCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,99999,3,1))
_CmedConfigGroups_ObjectIdentity=ObjectIdentity
cmedConfigGroups=_CmedConfigGroups_ObjectIdentity((1,3,6,1,4,1,9,10,99999,3,2))
cmedConfig=ObjectGroup((1,3,6,1,4,1,9,10,99999,3,2,1))
cmedConfig.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:cmedConfig.setStatus(_A)
cmedStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,99999,3,2,2))
cmedStatsGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cmedStatsGroup.setStatus(_A)
cmedGwyControllerGroup=ObjectGroup((1,3,6,1,4,1,9,10,99999,3,2,3))
cmedGwyControllerGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:cmedGwyControllerGroup.setStatus(_A)
cmedNextIdGroup=ObjectGroup((1,3,6,1,4,1,9,10,99999,3,2,4))
cmedNextIdGroup.setObjects(*((_B,_v),(_B,_w)))
if mibBuilder.loadTexts:cmedNextIdGroup.setStatus(_A)
cmedTermGroup=ObjectGroup((1,3,6,1,4,1,9,10,99999,3,2,5))
cmedTermGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:cmedTermGroup.setStatus(_A)
cmedCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,99999,3,1,1))
cmedCompliance.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:cmedCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CMediaGatewayId':CMediaGatewayId,'CMediaGatewayLinkId':CMediaGatewayLinkId,'CMediaGatewayTermId':CMediaGatewayTermId,'ciscoIetfMegacoMIB':ciscoIetfMegacoMIB,'ciscoIetfMegacoMIBNotifs':ciscoIetfMegacoMIBNotifs,'ciscoIetfMegacoMIBObjects':ciscoIetfMegacoMIBObjects,'cmedConfiguration':cmedConfiguration,'cmedLinkIdTable':cmedLinkIdTable,'cmedLinkIdEntry':cmedLinkIdEntry,_w:cmedNextLinkId,'cmedGatewayConfigTable':cmedGatewayConfigTable,'cmedGatewayConfigEntry':cmedGatewayConfigEntry,_F:cmedGatewayId,_M:cmedGatewayLinkId,_U:cmedGatewayLinkName,_V:cmedGatewayIPAddress,_W:cmedGatewayPort,_X:cmedGatewayEncodingScheme,_Y:cmedGatewayProtocol,_Z:cmedGatewaySigTptProtocol,_a:cmedGatewayAdminStatus,_b:cmedGatewayOperStatus,_c:cmedGatewayLastStatusChange,_d:cmedGatewayResetStatistics,_e:cmedGatewayRowStatus,'cmedGwyControllerTable':cmedGwyControllerTable,'cmedGwyControllerEntry':cmedGwyControllerEntry,_Q:cmedGwyControllerId,_r:cmedGwyControllerIPAddress,_s:cmedGwyControllerPort,_t:cmedGwyControllerAdminStatus,_u:cmedGwyControllerOperStatus,'cmedStatistics':cmedStatistics,'cmedGatewayStatsTable':cmedGatewayStatsTable,'cmedGatewayStatsEntry':cmedGatewayStatsEntry,_f:cmedNumInMessages,_g:cmedNumInOctets,_h:cmedNumOutMessages,_i:cmedNumOutOctets,_j:cmedNumErrors,_k:cmedNumTimerRecovery,_l:cmedTransportNumLosses,_m:cmedTransportNumSwitchover,_n:cmedTransportTotalNumAlarms,_o:cmedTransportLastEvent,_p:cmedTransportLastEventTime,_q:cmedLastStatisticsReset,'cmedConnections':cmedConnections,'cmedTermIdTable':cmedTermIdTable,'cmedTermIdEntry':cmedTermIdEntry,_v:cmedNextTerminationId,'cmedTerminationsTable':cmedTerminationsTable,'cmedTerminationsEntry':cmedTerminationsEntry,_R:cmedTermId,_x:cmedTermName,_y:cmedTermAdminStatus,_z:cmedTermOperStatus,_A0:cmedTermInterfaceIdentifier,_A1:cmedTermPropertyProfileId,_A2:cmedTermRowStatus,'cmedPropertyProfileTable':cmedPropertyProfileTable,'cmedPropertyProfileEntry':cmedPropertyProfileEntry,_S:cmedPropertyProfileId,_T:cmedPropertyProfileIndex,_A3:cmedPropertyProfileProperty,_A4:cmedPropertyProfileRowStatus,'cmedProperties':cmedProperties,'ciscoIetfMegacoMIBConformance':ciscoIetfMegacoMIBConformance,'cmedCompliances':cmedCompliances,'cmedCompliance':cmedCompliance,'cmedConfigGroups':cmedConfigGroups,_A5:cmedConfig,_A6:cmedStatsGroup,_A7:cmedGwyControllerGroup,_A8:cmedNextIdGroup,_A9:cmedTermGroup})