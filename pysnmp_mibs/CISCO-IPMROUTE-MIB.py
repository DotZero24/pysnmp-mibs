_A3='ciscoIpMRouteMIBIfGroup'
_A2='ciscoIpMRouteMIBGroupV12R28S'
_A1='ciscoIpMRouteMIBGroupV12R00S'
_A0='ciscoIpMRouteMIBGroupV11R01'
_z='ciscoIpMRouteMIBGroup'
_y='ciscoIpMRouteMissingHeartBeats'
_x='ciscoIpMRouteIfHCOutMcastPkts'
_w='ciscoIpMRouteIfOutMcastPkts'
_v='ciscoIpMRouteIfHCInMcastPkts'
_u='ciscoIpMRouteIfInMcastPkts'
_t='ciscoIpMRouteHeartBeatStatus'
_s='ciscoIpMRouteHeartBeatAlertTime'
_r='ciscoIpMRouteHeartBeatMinimum'
_q='ciscoIpMRouteInLimit'
_p='ciscoIpMRouteInterfaceEntry'
_o='ciscoIpMRouteNextHopEntry'
_n='ciscoIpMRouteEntry'
_m='ciscoIpMRouteHeartBeatGroupAddr'
_l='ciscoIpMRouteIfOutMcastOctets'
_k='ciscoIpMRouteIfInMcastOctets'
_j='ciscoIpMRouteNextHopPkts'
_i='ciscoIpMRouteMetric2'
_h='ciscoIpMRouteBps2'
_g='ciscoIpMRouteOctets'
_f='ciscoIpMRouteDifferentInIfPkts'
_e='ciscoIpMRoutePkts'
_d='ciscoIpMRouteNumberOfEntries'
_c='ciscoIpMRouteHeartBeatCount'
_b='ciscoIpMRouteHeartBeatWindowSize'
_a='ciscoIpMRouteHeartBeatInterval'
_Z='ciscoIpMRouteHeartBeatSourceAddr'
_Y='ciscoIpMRouteMetric'
_X='ciscoIpMRouteBps'
_W='Kbits/second'
_V='obsolete'
_U='ciscoIpMRouteProxyJoinFlag'
_T='ciscoIpMRouteMsdpFlag'
_S='ciscoIpMRouteJoinFlag'
_R='ciscoIpMRouteInLimit2'
_Q='read-create'
_P='ciscoIpMRouteNextHopMacHdr'
_O='ciscoIpMRouteNextHopOutLimit'
_N='ciscoIpMRouteLastUsed'
_M='ciscoIpMRouteMetricPreference'
_L='ciscoIpMRouteSptFlag'
_K='ciscoIpMRouteRpFlag'
_J='ciscoIpMRouteRegisterFlag'
_I='ciscoIpMRouteLocalFlag'
_H='ciscoIpMRouteConnectedFlag'
_G='ciscoIpMRouteSparseFlag'
_F='ciscoIpMRoutePruneFlag'
_E='deprecated'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-IPMROUTE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ipMRouteEntry,ipMRouteInterfaceEntry,ipMRouteNextHopEntry=mibBuilder.importSymbols('IPMROUTE-STD-MIB','ipMRouteEntry','ipMRouteInterfaceEntry','ipMRouteNextHopEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
ciscoIpMRouteMIB=ModuleIdentity((1,3,6,1,4,1,9,10,2))
if mibBuilder.loadTexts:ciscoIpMRouteMIB.setRevisions(('2005-03-07 00:00','2000-12-22 00:00','2000-05-15 00:00','1999-02-08 00:00','1996-10-11 00:00'))
_CiscoIpMRouteMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpMRouteMIBObjects=_CiscoIpMRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,2,1))
_CiscoIpMRoute_ObjectIdentity=ObjectIdentity
ciscoIpMRoute=_CiscoIpMRoute_ObjectIdentity((1,3,6,1,4,1,9,10,2,1,1))
_CiscoIpMRouteNumberOfEntries_Type=Gauge32
_CiscoIpMRouteNumberOfEntries_Object=MibScalar
ciscoIpMRouteNumberOfEntries=_CiscoIpMRouteNumberOfEntries_Object((1,3,6,1,4,1,9,10,2,1,1,1),_CiscoIpMRouteNumberOfEntries_Type())
ciscoIpMRouteNumberOfEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteNumberOfEntries.setStatus(_B)
_CiscoIpMRouteTable_Object=MibTable
ciscoIpMRouteTable=_CiscoIpMRouteTable_Object((1,3,6,1,4,1,9,10,2,1,1,2))
if mibBuilder.loadTexts:ciscoIpMRouteTable.setStatus(_B)
_CiscoIpMRouteEntry_Object=MibTableRow
ciscoIpMRouteEntry=_CiscoIpMRouteEntry_Object((1,3,6,1,4,1,9,10,2,1,1,2,1))
if mibBuilder.loadTexts:ciscoIpMRouteEntry.setStatus(_B)
_CiscoIpMRoutePruneFlag_Type=TruthValue
_CiscoIpMRoutePruneFlag_Object=MibTableColumn
ciscoIpMRoutePruneFlag=_CiscoIpMRoutePruneFlag_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,12),_CiscoIpMRoutePruneFlag_Type())
ciscoIpMRoutePruneFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRoutePruneFlag.setStatus(_B)
_CiscoIpMRouteSparseFlag_Type=TruthValue
_CiscoIpMRouteSparseFlag_Object=MibTableColumn
ciscoIpMRouteSparseFlag=_CiscoIpMRouteSparseFlag_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,13),_CiscoIpMRouteSparseFlag_Type())
ciscoIpMRouteSparseFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteSparseFlag.setStatus(_B)
_CiscoIpMRouteConnectedFlag_Type=TruthValue
_CiscoIpMRouteConnectedFlag_Object=MibTableColumn
ciscoIpMRouteConnectedFlag=_CiscoIpMRouteConnectedFlag_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,14),_CiscoIpMRouteConnectedFlag_Type())
ciscoIpMRouteConnectedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteConnectedFlag.setStatus(_B)
_CiscoIpMRouteLocalFlag_Type=TruthValue
_CiscoIpMRouteLocalFlag_Object=MibTableColumn
ciscoIpMRouteLocalFlag=_CiscoIpMRouteLocalFlag_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,15),_CiscoIpMRouteLocalFlag_Type())
ciscoIpMRouteLocalFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteLocalFlag.setStatus(_B)
_CiscoIpMRouteRegisterFlag_Type=TruthValue
_CiscoIpMRouteRegisterFlag_Object=MibTableColumn
ciscoIpMRouteRegisterFlag=_CiscoIpMRouteRegisterFlag_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,16),_CiscoIpMRouteRegisterFlag_Type())
ciscoIpMRouteRegisterFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteRegisterFlag.setStatus(_B)
_CiscoIpMRouteRpFlag_Type=TruthValue
_CiscoIpMRouteRpFlag_Object=MibTableColumn
ciscoIpMRouteRpFlag=_CiscoIpMRouteRpFlag_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,17),_CiscoIpMRouteRpFlag_Type())
ciscoIpMRouteRpFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteRpFlag.setStatus(_B)
_CiscoIpMRouteSptFlag_Type=TruthValue
_CiscoIpMRouteSptFlag_Object=MibTableColumn
ciscoIpMRouteSptFlag=_CiscoIpMRouteSptFlag_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,18),_CiscoIpMRouteSptFlag_Type())
ciscoIpMRouteSptFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteSptFlag.setStatus(_B)
_CiscoIpMRouteBps_Type=Gauge32
_CiscoIpMRouteBps_Object=MibTableColumn
ciscoIpMRouteBps=_CiscoIpMRouteBps_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,19),_CiscoIpMRouteBps_Type())
ciscoIpMRouteBps.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteBps.setStatus(_E)
class _CiscoIpMRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoIpMRouteMetric_Type.__name__=_D
_CiscoIpMRouteMetric_Object=MibTableColumn
ciscoIpMRouteMetric=_CiscoIpMRouteMetric_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,20),_CiscoIpMRouteMetric_Type())
ciscoIpMRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteMetric.setStatus(_E)
class _CiscoIpMRouteMetricPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoIpMRouteMetricPreference_Type.__name__=_D
_CiscoIpMRouteMetricPreference_Object=MibTableColumn
ciscoIpMRouteMetricPreference=_CiscoIpMRouteMetricPreference_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,21),_CiscoIpMRouteMetricPreference_Type())
ciscoIpMRouteMetricPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteMetricPreference.setStatus(_B)
class _CiscoIpMRouteInLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoIpMRouteInLimit_Type.__name__=_D
_CiscoIpMRouteInLimit_Object=MibTableColumn
ciscoIpMRouteInLimit=_CiscoIpMRouteInLimit_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,22),_CiscoIpMRouteInLimit_Type())
ciscoIpMRouteInLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteInLimit.setStatus(_V)
if mibBuilder.loadTexts:ciscoIpMRouteInLimit.setUnits(_W)
_CiscoIpMRouteLastUsed_Type=TimeTicks
_CiscoIpMRouteLastUsed_Object=MibTableColumn
ciscoIpMRouteLastUsed=_CiscoIpMRouteLastUsed_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,23),_CiscoIpMRouteLastUsed_Type())
ciscoIpMRouteLastUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteLastUsed.setStatus(_B)
_CiscoIpMRouteInLimit2_Type=Gauge32
_CiscoIpMRouteInLimit2_Object=MibTableColumn
ciscoIpMRouteInLimit2=_CiscoIpMRouteInLimit2_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,24),_CiscoIpMRouteInLimit2_Type())
ciscoIpMRouteInLimit2.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteInLimit2.setStatus(_B)
if mibBuilder.loadTexts:ciscoIpMRouteInLimit2.setUnits(_W)
_CiscoIpMRouteJoinFlag_Type=TruthValue
_CiscoIpMRouteJoinFlag_Object=MibTableColumn
ciscoIpMRouteJoinFlag=_CiscoIpMRouteJoinFlag_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,25),_CiscoIpMRouteJoinFlag_Type())
ciscoIpMRouteJoinFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteJoinFlag.setStatus(_B)
_CiscoIpMRouteMsdpFlag_Type=TruthValue
_CiscoIpMRouteMsdpFlag_Object=MibTableColumn
ciscoIpMRouteMsdpFlag=_CiscoIpMRouteMsdpFlag_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,26),_CiscoIpMRouteMsdpFlag_Type())
ciscoIpMRouteMsdpFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteMsdpFlag.setStatus(_B)
_CiscoIpMRouteProxyJoinFlag_Type=TruthValue
_CiscoIpMRouteProxyJoinFlag_Object=MibTableColumn
ciscoIpMRouteProxyJoinFlag=_CiscoIpMRouteProxyJoinFlag_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,27),_CiscoIpMRouteProxyJoinFlag_Type())
ciscoIpMRouteProxyJoinFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteProxyJoinFlag.setStatus(_B)
_CiscoIpMRoutePkts_Type=Counter64
_CiscoIpMRoutePkts_Object=MibTableColumn
ciscoIpMRoutePkts=_CiscoIpMRoutePkts_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,28),_CiscoIpMRoutePkts_Type())
ciscoIpMRoutePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRoutePkts.setStatus(_B)
_CiscoIpMRouteDifferentInIfPkts_Type=Counter64
_CiscoIpMRouteDifferentInIfPkts_Object=MibTableColumn
ciscoIpMRouteDifferentInIfPkts=_CiscoIpMRouteDifferentInIfPkts_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,29),_CiscoIpMRouteDifferentInIfPkts_Type())
ciscoIpMRouteDifferentInIfPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteDifferentInIfPkts.setStatus(_B)
_CiscoIpMRouteOctets_Type=Counter64
_CiscoIpMRouteOctets_Object=MibTableColumn
ciscoIpMRouteOctets=_CiscoIpMRouteOctets_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,30),_CiscoIpMRouteOctets_Type())
ciscoIpMRouteOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteOctets.setStatus(_B)
_CiscoIpMRouteBps2_Type=CounterBasedGauge64
_CiscoIpMRouteBps2_Object=MibTableColumn
ciscoIpMRouteBps2=_CiscoIpMRouteBps2_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,31),_CiscoIpMRouteBps2_Type())
ciscoIpMRouteBps2.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteBps2.setStatus(_B)
_CiscoIpMRouteMetric2_Type=Unsigned32
_CiscoIpMRouteMetric2_Object=MibTableColumn
ciscoIpMRouteMetric2=_CiscoIpMRouteMetric2_Object((1,3,6,1,4,1,9,10,2,1,1,2,1,32),_CiscoIpMRouteMetric2_Type())
ciscoIpMRouteMetric2.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteMetric2.setStatus(_B)
_CiscoIpMRouteNextHopTable_Object=MibTable
ciscoIpMRouteNextHopTable=_CiscoIpMRouteNextHopTable_Object((1,3,6,1,4,1,9,10,2,1,1,3))
if mibBuilder.loadTexts:ciscoIpMRouteNextHopTable.setStatus(_B)
_CiscoIpMRouteNextHopEntry_Object=MibTableRow
ciscoIpMRouteNextHopEntry=_CiscoIpMRouteNextHopEntry_Object((1,3,6,1,4,1,9,10,2,1,1,3,1))
if mibBuilder.loadTexts:ciscoIpMRouteNextHopEntry.setStatus(_B)
_CiscoIpMRouteNextHopOutLimit_Type=Gauge32
_CiscoIpMRouteNextHopOutLimit_Object=MibTableColumn
ciscoIpMRouteNextHopOutLimit=_CiscoIpMRouteNextHopOutLimit_Object((1,3,6,1,4,1,9,10,2,1,1,3,1,9),_CiscoIpMRouteNextHopOutLimit_Type())
ciscoIpMRouteNextHopOutLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteNextHopOutLimit.setStatus(_B)
if mibBuilder.loadTexts:ciscoIpMRouteNextHopOutLimit.setUnits(_W)
_CiscoIpMRouteNextHopMacHdr_Type=OctetString
_CiscoIpMRouteNextHopMacHdr_Object=MibTableColumn
ciscoIpMRouteNextHopMacHdr=_CiscoIpMRouteNextHopMacHdr_Object((1,3,6,1,4,1,9,10,2,1,1,3,1,10),_CiscoIpMRouteNextHopMacHdr_Type())
ciscoIpMRouteNextHopMacHdr.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteNextHopMacHdr.setStatus(_B)
_CiscoIpMRouteNextHopPkts_Type=Counter64
_CiscoIpMRouteNextHopPkts_Object=MibTableColumn
ciscoIpMRouteNextHopPkts=_CiscoIpMRouteNextHopPkts_Object((1,3,6,1,4,1,9,10,2,1,1,3,1,11),_CiscoIpMRouteNextHopPkts_Type())
ciscoIpMRouteNextHopPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteNextHopPkts.setStatus(_B)
_CiscoIpMRouteHeartBeatTable_Object=MibTable
ciscoIpMRouteHeartBeatTable=_CiscoIpMRouteHeartBeatTable_Object((1,3,6,1,4,1,9,10,2,1,1,4))
if mibBuilder.loadTexts:ciscoIpMRouteHeartBeatTable.setStatus(_B)
_CiscoIpMRouteHeartBeatEntry_Object=MibTableRow
ciscoIpMRouteHeartBeatEntry=_CiscoIpMRouteHeartBeatEntry_Object((1,3,6,1,4,1,9,10,2,1,1,4,1))
ciscoIpMRouteHeartBeatEntry.setIndexNames((0,_A,_m))
if mibBuilder.loadTexts:ciscoIpMRouteHeartBeatEntry.setStatus(_B)
_CiscoIpMRouteHeartBeatGroupAddr_Type=IpAddress
_CiscoIpMRouteHeartBeatGroupAddr_Object=MibTableColumn
ciscoIpMRouteHeartBeatGroupAddr=_CiscoIpMRouteHeartBeatGroupAddr_Object((1,3,6,1,4,1,9,10,2,1,1,4,1,1),_CiscoIpMRouteHeartBeatGroupAddr_Type())
ciscoIpMRouteHeartBeatGroupAddr.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoIpMRouteHeartBeatGroupAddr.setStatus(_B)
_CiscoIpMRouteHeartBeatSourceAddr_Type=IpAddress
_CiscoIpMRouteHeartBeatSourceAddr_Object=MibTableColumn
ciscoIpMRouteHeartBeatSourceAddr=_CiscoIpMRouteHeartBeatSourceAddr_Object((1,3,6,1,4,1,9,10,2,1,1,4,1,2),_CiscoIpMRouteHeartBeatSourceAddr_Type())
ciscoIpMRouteHeartBeatSourceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteHeartBeatSourceAddr.setStatus(_B)
class _CiscoIpMRouteHeartBeatInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3600))
_CiscoIpMRouteHeartBeatInterval_Type.__name__=_D
_CiscoIpMRouteHeartBeatInterval_Object=MibTableColumn
ciscoIpMRouteHeartBeatInterval=_CiscoIpMRouteHeartBeatInterval_Object((1,3,6,1,4,1,9,10,2,1,1,4,1,3),_CiscoIpMRouteHeartBeatInterval_Type())
ciscoIpMRouteHeartBeatInterval.setMaxAccess(_Q)
if mibBuilder.loadTexts:ciscoIpMRouteHeartBeatInterval.setStatus(_B)
if mibBuilder.loadTexts:ciscoIpMRouteHeartBeatInterval.setUnits('seconds')
class _CiscoIpMRouteHeartBeatWindowSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CiscoIpMRouteHeartBeatWindowSize_Type.__name__=_D
_CiscoIpMRouteHeartBeatWindowSize_Object=MibTableColumn
ciscoIpMRouteHeartBeatWindowSize=_CiscoIpMRouteHeartBeatWindowSize_Object((1,3,6,1,4,1,9,10,2,1,1,4,1,4),_CiscoIpMRouteHeartBeatWindowSize_Type())
ciscoIpMRouteHeartBeatWindowSize.setMaxAccess(_Q)
if mibBuilder.loadTexts:ciscoIpMRouteHeartBeatWindowSize.setStatus(_B)
_CiscoIpMRouteHeartBeatCount_Type=Gauge32
_CiscoIpMRouteHeartBeatCount_Object=MibTableColumn
ciscoIpMRouteHeartBeatCount=_CiscoIpMRouteHeartBeatCount_Object((1,3,6,1,4,1,9,10,2,1,1,4,1,5),_CiscoIpMRouteHeartBeatCount_Type())
ciscoIpMRouteHeartBeatCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteHeartBeatCount.setStatus(_B)
class _CiscoIpMRouteHeartBeatMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CiscoIpMRouteHeartBeatMinimum_Type.__name__=_D
_CiscoIpMRouteHeartBeatMinimum_Object=MibTableColumn
ciscoIpMRouteHeartBeatMinimum=_CiscoIpMRouteHeartBeatMinimum_Object((1,3,6,1,4,1,9,10,2,1,1,4,1,6),_CiscoIpMRouteHeartBeatMinimum_Type())
ciscoIpMRouteHeartBeatMinimum.setMaxAccess(_Q)
if mibBuilder.loadTexts:ciscoIpMRouteHeartBeatMinimum.setStatus(_B)
_CiscoIpMRouteHeartBeatAlertTime_Type=TimeStamp
_CiscoIpMRouteHeartBeatAlertTime_Object=MibTableColumn
ciscoIpMRouteHeartBeatAlertTime=_CiscoIpMRouteHeartBeatAlertTime_Object((1,3,6,1,4,1,9,10,2,1,1,4,1,7),_CiscoIpMRouteHeartBeatAlertTime_Type())
ciscoIpMRouteHeartBeatAlertTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteHeartBeatAlertTime.setStatus(_B)
_CiscoIpMRouteHeartBeatStatus_Type=RowStatus
_CiscoIpMRouteHeartBeatStatus_Object=MibTableColumn
ciscoIpMRouteHeartBeatStatus=_CiscoIpMRouteHeartBeatStatus_Object((1,3,6,1,4,1,9,10,2,1,1,4,1,8),_CiscoIpMRouteHeartBeatStatus_Type())
ciscoIpMRouteHeartBeatStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:ciscoIpMRouteHeartBeatStatus.setStatus(_B)
_CiscoIpMRouteInterfaceTable_Object=MibTable
ciscoIpMRouteInterfaceTable=_CiscoIpMRouteInterfaceTable_Object((1,3,6,1,4,1,9,10,2,1,1,5))
if mibBuilder.loadTexts:ciscoIpMRouteInterfaceTable.setStatus(_B)
_CiscoIpMRouteInterfaceEntry_Object=MibTableRow
ciscoIpMRouteInterfaceEntry=_CiscoIpMRouteInterfaceEntry_Object((1,3,6,1,4,1,9,10,2,1,1,5,1))
if mibBuilder.loadTexts:ciscoIpMRouteInterfaceEntry.setStatus(_B)
_CiscoIpMRouteIfInMcastOctets_Type=Counter64
_CiscoIpMRouteIfInMcastOctets_Object=MibTableColumn
ciscoIpMRouteIfInMcastOctets=_CiscoIpMRouteIfInMcastOctets_Object((1,3,6,1,4,1,9,10,2,1,1,5,1,1),_CiscoIpMRouteIfInMcastOctets_Type())
ciscoIpMRouteIfInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteIfInMcastOctets.setStatus(_B)
_CiscoIpMRouteIfOutMcastOctets_Type=Counter64
_CiscoIpMRouteIfOutMcastOctets_Object=MibTableColumn
ciscoIpMRouteIfOutMcastOctets=_CiscoIpMRouteIfOutMcastOctets_Object((1,3,6,1,4,1,9,10,2,1,1,5,1,2),_CiscoIpMRouteIfOutMcastOctets_Type())
ciscoIpMRouteIfOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteIfOutMcastOctets.setStatus(_B)
_CiscoIpMRouteIfInMcastPkts_Type=Counter32
_CiscoIpMRouteIfInMcastPkts_Object=MibTableColumn
ciscoIpMRouteIfInMcastPkts=_CiscoIpMRouteIfInMcastPkts_Object((1,3,6,1,4,1,9,10,2,1,1,5,1,3),_CiscoIpMRouteIfInMcastPkts_Type())
ciscoIpMRouteIfInMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteIfInMcastPkts.setStatus(_B)
_CiscoIpMRouteIfHCInMcastPkts_Type=Counter64
_CiscoIpMRouteIfHCInMcastPkts_Object=MibTableColumn
ciscoIpMRouteIfHCInMcastPkts=_CiscoIpMRouteIfHCInMcastPkts_Object((1,3,6,1,4,1,9,10,2,1,1,5,1,4),_CiscoIpMRouteIfHCInMcastPkts_Type())
ciscoIpMRouteIfHCInMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteIfHCInMcastPkts.setStatus(_B)
_CiscoIpMRouteIfOutMcastPkts_Type=Counter32
_CiscoIpMRouteIfOutMcastPkts_Object=MibTableColumn
ciscoIpMRouteIfOutMcastPkts=_CiscoIpMRouteIfOutMcastPkts_Object((1,3,6,1,4,1,9,10,2,1,1,5,1,5),_CiscoIpMRouteIfOutMcastPkts_Type())
ciscoIpMRouteIfOutMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteIfOutMcastPkts.setStatus(_B)
_CiscoIpMRouteIfHCOutMcastPkts_Type=Counter64
_CiscoIpMRouteIfHCOutMcastPkts_Object=MibTableColumn
ciscoIpMRouteIfHCOutMcastPkts=_CiscoIpMRouteIfHCOutMcastPkts_Object((1,3,6,1,4,1,9,10,2,1,1,5,1,6),_CiscoIpMRouteIfHCOutMcastPkts_Type())
ciscoIpMRouteIfHCOutMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoIpMRouteIfHCOutMcastPkts.setStatus(_B)
_CiscoIpMRouteMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIpMRouteMIBConformance=_CiscoIpMRouteMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,2,2))
_CiscoIpMRouteMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIpMRouteMIBCompliances=_CiscoIpMRouteMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,2,2,1))
_CiscoIpMRouteMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpMRouteMIBGroups=_CiscoIpMRouteMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,2,2,2))
_CiscoIpMRouteNotifications_ObjectIdentity=ObjectIdentity
ciscoIpMRouteNotifications=_CiscoIpMRouteNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,2,3))
_CiscoIpMRouteMissingHeartBeatsNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoIpMRouteMissingHeartBeatsNotificationPrefix=_CiscoIpMRouteMissingHeartBeatsNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,2,3,1))
_CiscoIpMRouteMissingHeartBeatsNotifications_ObjectIdentity=ObjectIdentity
ciscoIpMRouteMissingHeartBeatsNotifications=_CiscoIpMRouteMissingHeartBeatsNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,2,3,1,0))
ipMRouteEntry.registerAugmentions((_A,_n))
ciscoIpMRouteEntry.setIndexNames(*ipMRouteEntry.getIndexNames())
ipMRouteNextHopEntry.registerAugmentions((_A,_o))
ciscoIpMRouteNextHopEntry.setIndexNames(*ipMRouteNextHopEntry.getIndexNames())
ipMRouteInterfaceEntry.registerAugmentions((_A,_p))
ciscoIpMRouteInterfaceEntry.setIndexNames(*ipMRouteInterfaceEntry.getIndexNames())
ciscoIpMRouteMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,2,2,2,1))
ciscoIpMRouteMIBGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_X),(_A,_Y),(_A,_M),(_A,_q),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ciscoIpMRouteMIBGroup.setStatus(_V)
ciscoIpMRouteMIBGroupV11R01=ObjectGroup((1,3,6,1,4,1,9,10,2,2,2,2))
ciscoIpMRouteMIBGroupV11R01.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_X),(_A,_Y),(_A,_M),(_A,_N),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ciscoIpMRouteMIBGroupV11R01.setStatus(_E)
ciscoIpMRouteMIBHeartBeatGroup=ObjectGroup((1,3,6,1,4,1,9,10,2,2,2,3))
ciscoIpMRouteMIBHeartBeatGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:ciscoIpMRouteMIBHeartBeatGroup.setStatus(_B)
ciscoIpMRouteMIBGroupV12R00S=ObjectGroup((1,3,6,1,4,1,9,10,2,2,2,4))
ciscoIpMRouteMIBGroupV12R00S.setObjects(*((_A,_d),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_O),(_A,_P),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:ciscoIpMRouteMIBGroupV12R00S.setStatus(_E)
ciscoIpMRouteMIBGroupV12R28S=ObjectGroup((1,3,6,1,4,1,9,10,2,2,2,6))
ciscoIpMRouteMIBGroupV12R28S.setObjects(*((_A,_d),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_O),(_A,_P),(_A,_j)))
if mibBuilder.loadTexts:ciscoIpMRouteMIBGroupV12R28S.setStatus(_B)
ciscoIpMRouteMIBIfGroup=ObjectGroup((1,3,6,1,4,1,9,10,2,2,2,7))
ciscoIpMRouteMIBIfGroup.setObjects(*((_A,_k),(_A,_l),(_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:ciscoIpMRouteMIBIfGroup.setStatus(_B)
ciscoIpMRouteMissingHeartBeats=NotificationType((1,3,6,1,4,1,9,10,2,3,1,0,1))
ciscoIpMRouteMissingHeartBeats.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:ciscoIpMRouteMissingHeartBeats.setStatus(_B)
ciscoIpMRouteMIBNotifGroup=NotificationGroup((1,3,6,1,4,1,9,10,2,2,2,5))
ciscoIpMRouteMIBNotifGroup.setObjects((_A,_y))
if mibBuilder.loadTexts:ciscoIpMRouteMIBNotifGroup.setStatus(_B)
ciscoIpMRouteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,2,2,1,1))
ciscoIpMRouteMIBCompliance.setObjects((_A,_z))
if mibBuilder.loadTexts:ciscoIpMRouteMIBCompliance.setStatus(_V)
ciscoIpMRouteMIBComplianceV11R01=ModuleCompliance((1,3,6,1,4,1,9,10,2,2,1,2))
ciscoIpMRouteMIBComplianceV11R01.setObjects((_A,_A0))
if mibBuilder.loadTexts:ciscoIpMRouteMIBComplianceV11R01.setStatus(_E)
ciscoIpMRouteMIBComplianceV12R00S=ModuleCompliance((1,3,6,1,4,1,9,10,2,2,1,3))
ciscoIpMRouteMIBComplianceV12R00S.setObjects((_A,_A1))
if mibBuilder.loadTexts:ciscoIpMRouteMIBComplianceV12R00S.setStatus(_E)
ciscoIpMRouteMIBComplianceV12R28S=ModuleCompliance((1,3,6,1,4,1,9,10,2,2,1,4))
ciscoIpMRouteMIBComplianceV12R28S.setObjects(*((_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:ciscoIpMRouteMIBComplianceV12R28S.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoIpMRouteMIB':ciscoIpMRouteMIB,'ciscoIpMRouteMIBObjects':ciscoIpMRouteMIBObjects,'ciscoIpMRoute':ciscoIpMRoute,_d:ciscoIpMRouteNumberOfEntries,'ciscoIpMRouteTable':ciscoIpMRouteTable,_n:ciscoIpMRouteEntry,_F:ciscoIpMRoutePruneFlag,_G:ciscoIpMRouteSparseFlag,_H:ciscoIpMRouteConnectedFlag,_I:ciscoIpMRouteLocalFlag,_J:ciscoIpMRouteRegisterFlag,_K:ciscoIpMRouteRpFlag,_L:ciscoIpMRouteSptFlag,_X:ciscoIpMRouteBps,_Y:ciscoIpMRouteMetric,_M:ciscoIpMRouteMetricPreference,_q:ciscoIpMRouteInLimit,_N:ciscoIpMRouteLastUsed,_R:ciscoIpMRouteInLimit2,_S:ciscoIpMRouteJoinFlag,_T:ciscoIpMRouteMsdpFlag,_U:ciscoIpMRouteProxyJoinFlag,_e:ciscoIpMRoutePkts,_f:ciscoIpMRouteDifferentInIfPkts,_g:ciscoIpMRouteOctets,_h:ciscoIpMRouteBps2,_i:ciscoIpMRouteMetric2,'ciscoIpMRouteNextHopTable':ciscoIpMRouteNextHopTable,_o:ciscoIpMRouteNextHopEntry,_O:ciscoIpMRouteNextHopOutLimit,_P:ciscoIpMRouteNextHopMacHdr,_j:ciscoIpMRouteNextHopPkts,'ciscoIpMRouteHeartBeatTable':ciscoIpMRouteHeartBeatTable,'ciscoIpMRouteHeartBeatEntry':ciscoIpMRouteHeartBeatEntry,_m:ciscoIpMRouteHeartBeatGroupAddr,_Z:ciscoIpMRouteHeartBeatSourceAddr,_a:ciscoIpMRouteHeartBeatInterval,_b:ciscoIpMRouteHeartBeatWindowSize,_c:ciscoIpMRouteHeartBeatCount,_r:ciscoIpMRouteHeartBeatMinimum,_s:ciscoIpMRouteHeartBeatAlertTime,_t:ciscoIpMRouteHeartBeatStatus,'ciscoIpMRouteInterfaceTable':ciscoIpMRouteInterfaceTable,_p:ciscoIpMRouteInterfaceEntry,_k:ciscoIpMRouteIfInMcastOctets,_l:ciscoIpMRouteIfOutMcastOctets,_u:ciscoIpMRouteIfInMcastPkts,_v:ciscoIpMRouteIfHCInMcastPkts,_w:ciscoIpMRouteIfOutMcastPkts,_x:ciscoIpMRouteIfHCOutMcastPkts,'ciscoIpMRouteMIBConformance':ciscoIpMRouteMIBConformance,'ciscoIpMRouteMIBCompliances':ciscoIpMRouteMIBCompliances,'ciscoIpMRouteMIBCompliance':ciscoIpMRouteMIBCompliance,'ciscoIpMRouteMIBComplianceV11R01':ciscoIpMRouteMIBComplianceV11R01,'ciscoIpMRouteMIBComplianceV12R00S':ciscoIpMRouteMIBComplianceV12R00S,'ciscoIpMRouteMIBComplianceV12R28S':ciscoIpMRouteMIBComplianceV12R28S,'ciscoIpMRouteMIBGroups':ciscoIpMRouteMIBGroups,_z:ciscoIpMRouteMIBGroup,_A0:ciscoIpMRouteMIBGroupV11R01,'ciscoIpMRouteMIBHeartBeatGroup':ciscoIpMRouteMIBHeartBeatGroup,_A1:ciscoIpMRouteMIBGroupV12R00S,'ciscoIpMRouteMIBNotifGroup':ciscoIpMRouteMIBNotifGroup,_A2:ciscoIpMRouteMIBGroupV12R28S,_A3:ciscoIpMRouteMIBIfGroup,'ciscoIpMRouteNotifications':ciscoIpMRouteNotifications,'ciscoIpMRouteMissingHeartBeatsNotificationPrefix':ciscoIpMRouteMissingHeartBeatsNotificationPrefix,'ciscoIpMRouteMissingHeartBeatsNotifications':ciscoIpMRouteMissingHeartBeatsNotifications,_y:ciscoIpMRouteMissingHeartBeats})