_e='alaDvmrpIfConfigGroup'
_d='alaDvmrpTunnelXIfMIBGroup'
_c='alaDvmrpConfigMIBGroup'
_b='alaDvmrpIfMbrDefaultInfoStatus'
_a='alaDvmrpIfBfdStatus'
_Z='alaDvmrpLocalIfIndex'
_Y='alaDvmrpMbrOperStatus'
_X='alaDvmrpBfdAllInterfaceStatus'
_W='alaDvmrpBfdStatus'
_V='alaDvmrpInitNbrAsSubord'
_U='alaDvmrpGraftRetransmission'
_T='alaDvmrpPruneRetransmission'
_S='alaDvmrpPruneLifetime'
_R='alaDvmrpNeighborProbeInterval'
_Q='alaDvmrpRouteHoldDown'
_P='alaDvmrpRouteExpirationTimeout'
_O='alaDvmrpNeighborTimeout'
_N='alaDvmrpFlashUpdateInterval'
_M='alaDvmrpRouteReportInterval'
_L='alaDvmrpAdminStatus'
_K='alaDvmrpIfAugEntry'
_J='alaDvmrpTunnelIndex'
_I='TruthValue'
_H='read-only'
_G='disable'
_F='enable'
_E='seconds'
_D='read-write'
_C='Integer32'
_B='ALCATEL-ENT1-DVMRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Dvmrp,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','routingIND1Dvmrp')
dvmrpInterfaceEntry,=mibBuilder.importSymbols('DVMRP-STD-MIB','dvmrpInterfaceEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
alcatelIND1DVMRPMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,7,1))
if mibBuilder.loadTexts:alcatelIND1DVMRPMIB.setRevisions(('2007-04-03 00:00',))
_AlcatelIND1DVMRPMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1DVMRPMIBObjects=_AlcatelIND1DVMRPMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1))
_AlaDvmrpGlobalConfig_ObjectIdentity=ObjectIdentity
alaDvmrpGlobalConfig=_AlaDvmrpGlobalConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1))
class _AlaDvmrpAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),('unrestrictedEnable',3)))
_AlaDvmrpAdminStatus_Type.__name__=_C
_AlaDvmrpAdminStatus_Object=MibScalar
alaDvmrpAdminStatus=_AlaDvmrpAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,1),_AlaDvmrpAdminStatus_Type())
alaDvmrpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDvmrpAdminStatus.setStatus(_A)
class _AlaDvmrpRouteReportInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2000))
_AlaDvmrpRouteReportInterval_Type.__name__=_C
_AlaDvmrpRouteReportInterval_Object=MibScalar
alaDvmrpRouteReportInterval=_AlaDvmrpRouteReportInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,2),_AlaDvmrpRouteReportInterval_Type())
alaDvmrpRouteReportInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDvmrpRouteReportInterval.setStatus(_A)
if mibBuilder.loadTexts:alaDvmrpRouteReportInterval.setUnits(_E)
class _AlaDvmrpFlashUpdateInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_AlaDvmrpFlashUpdateInterval_Type.__name__=_C
_AlaDvmrpFlashUpdateInterval_Object=MibScalar
alaDvmrpFlashUpdateInterval=_AlaDvmrpFlashUpdateInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,3),_AlaDvmrpFlashUpdateInterval_Type())
alaDvmrpFlashUpdateInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDvmrpFlashUpdateInterval.setStatus(_A)
if mibBuilder.loadTexts:alaDvmrpFlashUpdateInterval.setUnits(_E)
class _AlaDvmrpNeighborTimeout_Type(Integer32):defaultValue=35;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_AlaDvmrpNeighborTimeout_Type.__name__=_C
_AlaDvmrpNeighborTimeout_Object=MibScalar
alaDvmrpNeighborTimeout=_AlaDvmrpNeighborTimeout_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,4),_AlaDvmrpNeighborTimeout_Type())
alaDvmrpNeighborTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDvmrpNeighborTimeout.setStatus(_A)
if mibBuilder.loadTexts:alaDvmrpNeighborTimeout.setUnits(_E)
class _AlaDvmrpRouteExpirationTimeout_Type(Integer32):defaultValue=140;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,4000))
_AlaDvmrpRouteExpirationTimeout_Type.__name__=_C
_AlaDvmrpRouteExpirationTimeout_Object=MibScalar
alaDvmrpRouteExpirationTimeout=_AlaDvmrpRouteExpirationTimeout_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,5),_AlaDvmrpRouteExpirationTimeout_Type())
alaDvmrpRouteExpirationTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDvmrpRouteExpirationTimeout.setStatus(_A)
if mibBuilder.loadTexts:alaDvmrpRouteExpirationTimeout.setUnits(_E)
class _AlaDvmrpRouteHoldDown_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_AlaDvmrpRouteHoldDown_Type.__name__=_C
_AlaDvmrpRouteHoldDown_Object=MibScalar
alaDvmrpRouteHoldDown=_AlaDvmrpRouteHoldDown_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,6),_AlaDvmrpRouteHoldDown_Type())
alaDvmrpRouteHoldDown.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDvmrpRouteHoldDown.setStatus(_A)
if mibBuilder.loadTexts:alaDvmrpRouteHoldDown.setUnits(_E)
class _AlaDvmrpNeighborProbeInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_AlaDvmrpNeighborProbeInterval_Type.__name__=_C
_AlaDvmrpNeighborProbeInterval_Object=MibScalar
alaDvmrpNeighborProbeInterval=_AlaDvmrpNeighborProbeInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,7),_AlaDvmrpNeighborProbeInterval_Type())
alaDvmrpNeighborProbeInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDvmrpNeighborProbeInterval.setStatus(_A)
if mibBuilder.loadTexts:alaDvmrpNeighborProbeInterval.setUnits(_E)
class _AlaDvmrpPruneLifetime_Type(Integer32):defaultValue=7200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(180,86400))
_AlaDvmrpPruneLifetime_Type.__name__=_C
_AlaDvmrpPruneLifetime_Object=MibScalar
alaDvmrpPruneLifetime=_AlaDvmrpPruneLifetime_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,8),_AlaDvmrpPruneLifetime_Type())
alaDvmrpPruneLifetime.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDvmrpPruneLifetime.setStatus(_A)
if mibBuilder.loadTexts:alaDvmrpPruneLifetime.setUnits(_E)
class _AlaDvmrpPruneRetransmission_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,86400))
_AlaDvmrpPruneRetransmission_Type.__name__=_C
_AlaDvmrpPruneRetransmission_Object=MibScalar
alaDvmrpPruneRetransmission=_AlaDvmrpPruneRetransmission_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,9),_AlaDvmrpPruneRetransmission_Type())
alaDvmrpPruneRetransmission.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDvmrpPruneRetransmission.setStatus(_A)
if mibBuilder.loadTexts:alaDvmrpPruneRetransmission.setUnits(_E)
class _AlaDvmrpGraftRetransmission_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_AlaDvmrpGraftRetransmission_Type.__name__=_C
_AlaDvmrpGraftRetransmission_Object=MibScalar
alaDvmrpGraftRetransmission=_AlaDvmrpGraftRetransmission_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,10),_AlaDvmrpGraftRetransmission_Type())
alaDvmrpGraftRetransmission.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDvmrpGraftRetransmission.setStatus(_A)
if mibBuilder.loadTexts:alaDvmrpGraftRetransmission.setUnits(_E)
class _AlaDvmrpInitNbrAsSubord_Type(TruthValue):defaultValue=1
_AlaDvmrpInitNbrAsSubord_Type.__name__=_I
_AlaDvmrpInitNbrAsSubord_Object=MibScalar
alaDvmrpInitNbrAsSubord=_AlaDvmrpInitNbrAsSubord_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,11),_AlaDvmrpInitNbrAsSubord_Type())
alaDvmrpInitNbrAsSubord.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDvmrpInitNbrAsSubord.setStatus(_A)
class _AlaDvmrpBfdStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaDvmrpBfdStatus_Type.__name__=_C
_AlaDvmrpBfdStatus_Object=MibScalar
alaDvmrpBfdStatus=_AlaDvmrpBfdStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,12),_AlaDvmrpBfdStatus_Type())
alaDvmrpBfdStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDvmrpBfdStatus.setStatus(_A)
class _AlaDvmrpBfdAllInterfaceStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaDvmrpBfdAllInterfaceStatus_Type.__name__=_C
_AlaDvmrpBfdAllInterfaceStatus_Object=MibScalar
alaDvmrpBfdAllInterfaceStatus=_AlaDvmrpBfdAllInterfaceStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,13),_AlaDvmrpBfdAllInterfaceStatus_Type())
alaDvmrpBfdAllInterfaceStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDvmrpBfdAllInterfaceStatus.setStatus(_A)
class _AlaDvmrpMbrOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaDvmrpMbrOperStatus_Type.__name__=_C
_AlaDvmrpMbrOperStatus_Object=MibScalar
alaDvmrpMbrOperStatus=_AlaDvmrpMbrOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,1,14),_AlaDvmrpMbrOperStatus_Type())
alaDvmrpMbrOperStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDvmrpMbrOperStatus.setStatus(_A)
_AlaDvmrpTunnelXIfTable_Object=MibTable
alaDvmrpTunnelXIfTable=_AlaDvmrpTunnelXIfTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,2))
if mibBuilder.loadTexts:alaDvmrpTunnelXIfTable.setStatus(_A)
_AlaDvmrpTunnelXIfEntry_Object=MibTableRow
alaDvmrpTunnelXIfEntry=_AlaDvmrpTunnelXIfEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,2,1))
alaDvmrpTunnelXIfEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:alaDvmrpTunnelXIfEntry.setStatus(_A)
_AlaDvmrpTunnelIndex_Type=Unsigned32
_AlaDvmrpTunnelIndex_Object=MibTableColumn
alaDvmrpTunnelIndex=_AlaDvmrpTunnelIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,2,1,1),_AlaDvmrpTunnelIndex_Type())
alaDvmrpTunnelIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:alaDvmrpTunnelIndex.setStatus(_A)
_AlaDvmrpLocalIfIndex_Type=Unsigned32
_AlaDvmrpLocalIfIndex_Object=MibTableColumn
alaDvmrpLocalIfIndex=_AlaDvmrpLocalIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,2,1,2),_AlaDvmrpLocalIfIndex_Type())
alaDvmrpLocalIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDvmrpLocalIfIndex.setStatus(_A)
_AlaDvmrpIfAugTable_Object=MibTable
alaDvmrpIfAugTable=_AlaDvmrpIfAugTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,4))
if mibBuilder.loadTexts:alaDvmrpIfAugTable.setStatus(_A)
_AlaDvmrpIfAugEntry_Object=MibTableRow
alaDvmrpIfAugEntry=_AlaDvmrpIfAugEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,4,1))
if mibBuilder.loadTexts:alaDvmrpIfAugEntry.setStatus(_A)
class _AlaDvmrpIfBfdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaDvmrpIfBfdStatus_Type.__name__=_C
_AlaDvmrpIfBfdStatus_Object=MibTableColumn
alaDvmrpIfBfdStatus=_AlaDvmrpIfBfdStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,4,1,1),_AlaDvmrpIfBfdStatus_Type())
alaDvmrpIfBfdStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDvmrpIfBfdStatus.setStatus(_A)
class _AlaDvmrpIfMbrDefaultInfoStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AlaDvmrpIfMbrDefaultInfoStatus_Type.__name__=_C
_AlaDvmrpIfMbrDefaultInfoStatus_Object=MibTableColumn
alaDvmrpIfMbrDefaultInfoStatus=_AlaDvmrpIfMbrDefaultInfoStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,1,4,1,2),_AlaDvmrpIfMbrDefaultInfoStatus_Type())
alaDvmrpIfMbrDefaultInfoStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:alaDvmrpIfMbrDefaultInfoStatus.setStatus(_A)
_AlcatelIND1DVMRPMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1DVMRPMIBConformance=_AlcatelIND1DVMRPMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,2))
_AlcatelIND1DVMRPMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1DVMRPMIBCompliances=_AlcatelIND1DVMRPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,2,1))
_AlcatelIND1DVMRPMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1DVMRPMIBGroups=_AlcatelIND1DVMRPMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,2,2))
dvmrpInterfaceEntry.registerAugmentions((_B,_K))
alaDvmrpIfAugEntry.setIndexNames(*dvmrpInterfaceEntry.getIndexNames())
alaDvmrpConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,2,2,1))
alaDvmrpConfigMIBGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:alaDvmrpConfigMIBGroup.setStatus(_A)
alaDvmrpTunnelXIfMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,2,2,2))
alaDvmrpTunnelXIfMIBGroup.setObjects((_B,_Z))
if mibBuilder.loadTexts:alaDvmrpTunnelXIfMIBGroup.setStatus(_A)
alaDvmrpIfConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,2,2,3))
alaDvmrpIfConfigGroup.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:alaDvmrpIfConfigGroup.setStatus(_A)
alaDvmrpCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,10,7,1,2,1,1))
alaDvmrpCompliance.setObjects(*((_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:alaDvmrpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1DVMRPMIB':alcatelIND1DVMRPMIB,'alcatelIND1DVMRPMIBObjects':alcatelIND1DVMRPMIBObjects,'alaDvmrpGlobalConfig':alaDvmrpGlobalConfig,_L:alaDvmrpAdminStatus,_M:alaDvmrpRouteReportInterval,_N:alaDvmrpFlashUpdateInterval,_O:alaDvmrpNeighborTimeout,_P:alaDvmrpRouteExpirationTimeout,_Q:alaDvmrpRouteHoldDown,_R:alaDvmrpNeighborProbeInterval,_S:alaDvmrpPruneLifetime,_T:alaDvmrpPruneRetransmission,_U:alaDvmrpGraftRetransmission,_V:alaDvmrpInitNbrAsSubord,_W:alaDvmrpBfdStatus,_X:alaDvmrpBfdAllInterfaceStatus,_Y:alaDvmrpMbrOperStatus,'alaDvmrpTunnelXIfTable':alaDvmrpTunnelXIfTable,'alaDvmrpTunnelXIfEntry':alaDvmrpTunnelXIfEntry,_J:alaDvmrpTunnelIndex,_Z:alaDvmrpLocalIfIndex,'alaDvmrpIfAugTable':alaDvmrpIfAugTable,_K:alaDvmrpIfAugEntry,_a:alaDvmrpIfBfdStatus,_b:alaDvmrpIfMbrDefaultInfoStatus,'alcatelIND1DVMRPMIBConformance':alcatelIND1DVMRPMIBConformance,'alcatelIND1DVMRPMIBCompliances':alcatelIND1DVMRPMIBCompliances,'alaDvmrpCompliance':alaDvmrpCompliance,'alcatelIND1DVMRPMIBGroups':alcatelIND1DVMRPMIBGroups,_c:alaDvmrpConfigMIBGroup,_d:alaDvmrpTunnelXIfMIBGroup,_e:alaDvmrpIfConfigGroup})