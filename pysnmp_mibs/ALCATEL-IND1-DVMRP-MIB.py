_t='alaDvmrpIfConfigGroup'
_s='alaDvmrpTunnelXIfMIBGroup'
_r='alaDvmrpDebugMIBGroup'
_q='alaDvmrpConfigMIBGroup'
_p='alaDvmrpIfBfdStatus'
_o='alaDvmrpLocalIfIndex'
_n='alaDvmrpDebugAll'
_m='alaDvmrpDebugMisc'
_l='alaDvmrpDebugIpmrm'
_k='alaDvmrpDebugTm'
_j='alaDvmrpDebugInit'
_i='alaDvmrpDebugMip'
_h='alaDvmrpDebugFlash'
_g='alaDvmrpDebugIgmp'
_f='alaDvmrpDebugTime'
_e='alaDvmrpDebugGrafts'
_d='alaDvmrpDebugPrunes'
_c='alaDvmrpDebugProbes'
_b='alaDvmrpDebugRoutes'
_a='alaDvmrpDebugNbr'
_Z='alaDvmrpDebugError'
_Y='alaDvmrpDebugLevel'
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
_H='seconds'
_G='deprecated'
_F='disable'
_E='enable'
_D='current'
_C='read-write'
_B='Integer32'
_A='ALCATEL-IND1-DVMRP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Dvmrp,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','routingIND1Dvmrp')
dvmrpInterfaceEntry,=mibBuilder.importSymbols('DVMRP-STD-MIB','dvmrpInterfaceEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
alcatelIND1DVMRPMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,7,1))
if mibBuilder.loadTexts:alcatelIND1DVMRPMIB.setRevisions(('2007-04-03 00:00',))
_AlcatelIND1DVMRPMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1DVMRPMIBObjects=_AlcatelIND1DVMRPMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1))
_AlaDvmrpGlobalConfig_ObjectIdentity=ObjectIdentity
alaDvmrpGlobalConfig=_AlaDvmrpGlobalConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1))
class _AlaDvmrpAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),('unrestrictedEnable',3)))
_AlaDvmrpAdminStatus_Type.__name__=_B
_AlaDvmrpAdminStatus_Object=MibScalar
alaDvmrpAdminStatus=_AlaDvmrpAdminStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1,1),_AlaDvmrpAdminStatus_Type())
alaDvmrpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpAdminStatus.setStatus(_D)
class _AlaDvmrpRouteReportInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2000))
_AlaDvmrpRouteReportInterval_Type.__name__=_B
_AlaDvmrpRouteReportInterval_Object=MibScalar
alaDvmrpRouteReportInterval=_AlaDvmrpRouteReportInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1,2),_AlaDvmrpRouteReportInterval_Type())
alaDvmrpRouteReportInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpRouteReportInterval.setStatus(_D)
if mibBuilder.loadTexts:alaDvmrpRouteReportInterval.setUnits(_H)
class _AlaDvmrpFlashUpdateInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_AlaDvmrpFlashUpdateInterval_Type.__name__=_B
_AlaDvmrpFlashUpdateInterval_Object=MibScalar
alaDvmrpFlashUpdateInterval=_AlaDvmrpFlashUpdateInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1,3),_AlaDvmrpFlashUpdateInterval_Type())
alaDvmrpFlashUpdateInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpFlashUpdateInterval.setStatus(_D)
if mibBuilder.loadTexts:alaDvmrpFlashUpdateInterval.setUnits(_H)
class _AlaDvmrpNeighborTimeout_Type(Integer32):defaultValue=35;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_AlaDvmrpNeighborTimeout_Type.__name__=_B
_AlaDvmrpNeighborTimeout_Object=MibScalar
alaDvmrpNeighborTimeout=_AlaDvmrpNeighborTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1,4),_AlaDvmrpNeighborTimeout_Type())
alaDvmrpNeighborTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpNeighborTimeout.setStatus(_D)
if mibBuilder.loadTexts:alaDvmrpNeighborTimeout.setUnits(_H)
class _AlaDvmrpRouteExpirationTimeout_Type(Integer32):defaultValue=140;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,4000))
_AlaDvmrpRouteExpirationTimeout_Type.__name__=_B
_AlaDvmrpRouteExpirationTimeout_Object=MibScalar
alaDvmrpRouteExpirationTimeout=_AlaDvmrpRouteExpirationTimeout_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1,5),_AlaDvmrpRouteExpirationTimeout_Type())
alaDvmrpRouteExpirationTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpRouteExpirationTimeout.setStatus(_D)
if mibBuilder.loadTexts:alaDvmrpRouteExpirationTimeout.setUnits(_H)
class _AlaDvmrpRouteHoldDown_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_AlaDvmrpRouteHoldDown_Type.__name__=_B
_AlaDvmrpRouteHoldDown_Object=MibScalar
alaDvmrpRouteHoldDown=_AlaDvmrpRouteHoldDown_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1,6),_AlaDvmrpRouteHoldDown_Type())
alaDvmrpRouteHoldDown.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpRouteHoldDown.setStatus(_D)
if mibBuilder.loadTexts:alaDvmrpRouteHoldDown.setUnits(_H)
class _AlaDvmrpNeighborProbeInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_AlaDvmrpNeighborProbeInterval_Type.__name__=_B
_AlaDvmrpNeighborProbeInterval_Object=MibScalar
alaDvmrpNeighborProbeInterval=_AlaDvmrpNeighborProbeInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1,7),_AlaDvmrpNeighborProbeInterval_Type())
alaDvmrpNeighborProbeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpNeighborProbeInterval.setStatus(_D)
if mibBuilder.loadTexts:alaDvmrpNeighborProbeInterval.setUnits(_H)
class _AlaDvmrpPruneLifetime_Type(Integer32):defaultValue=7200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(180,86400))
_AlaDvmrpPruneLifetime_Type.__name__=_B
_AlaDvmrpPruneLifetime_Object=MibScalar
alaDvmrpPruneLifetime=_AlaDvmrpPruneLifetime_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1,8),_AlaDvmrpPruneLifetime_Type())
alaDvmrpPruneLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpPruneLifetime.setStatus(_D)
if mibBuilder.loadTexts:alaDvmrpPruneLifetime.setUnits(_H)
class _AlaDvmrpPruneRetransmission_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,86400))
_AlaDvmrpPruneRetransmission_Type.__name__=_B
_AlaDvmrpPruneRetransmission_Object=MibScalar
alaDvmrpPruneRetransmission=_AlaDvmrpPruneRetransmission_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1,9),_AlaDvmrpPruneRetransmission_Type())
alaDvmrpPruneRetransmission.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpPruneRetransmission.setStatus(_D)
if mibBuilder.loadTexts:alaDvmrpPruneRetransmission.setUnits(_H)
class _AlaDvmrpGraftRetransmission_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_AlaDvmrpGraftRetransmission_Type.__name__=_B
_AlaDvmrpGraftRetransmission_Object=MibScalar
alaDvmrpGraftRetransmission=_AlaDvmrpGraftRetransmission_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1,10),_AlaDvmrpGraftRetransmission_Type())
alaDvmrpGraftRetransmission.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpGraftRetransmission.setStatus(_D)
if mibBuilder.loadTexts:alaDvmrpGraftRetransmission.setUnits(_H)
class _AlaDvmrpInitNbrAsSubord_Type(TruthValue):defaultValue=1
_AlaDvmrpInitNbrAsSubord_Type.__name__=_I
_AlaDvmrpInitNbrAsSubord_Object=MibScalar
alaDvmrpInitNbrAsSubord=_AlaDvmrpInitNbrAsSubord_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1,11),_AlaDvmrpInitNbrAsSubord_Type())
alaDvmrpInitNbrAsSubord.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpInitNbrAsSubord.setStatus(_D)
class _AlaDvmrpBfdStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpBfdStatus_Type.__name__=_B
_AlaDvmrpBfdStatus_Object=MibScalar
alaDvmrpBfdStatus=_AlaDvmrpBfdStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1,12),_AlaDvmrpBfdStatus_Type())
alaDvmrpBfdStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpBfdStatus.setStatus(_D)
class _AlaDvmrpBfdAllInterfaceStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpBfdAllInterfaceStatus_Type.__name__=_B
_AlaDvmrpBfdAllInterfaceStatus_Object=MibScalar
alaDvmrpBfdAllInterfaceStatus=_AlaDvmrpBfdAllInterfaceStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,1,13),_AlaDvmrpBfdAllInterfaceStatus_Type())
alaDvmrpBfdAllInterfaceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpBfdAllInterfaceStatus.setStatus(_D)
_AlaDvmrpDebugConfig_ObjectIdentity=ObjectIdentity
alaDvmrpDebugConfig=_AlaDvmrpDebugConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2))
class _AlaDvmrpDebugLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaDvmrpDebugLevel_Type.__name__=_B
_AlaDvmrpDebugLevel_Object=MibScalar
alaDvmrpDebugLevel=_AlaDvmrpDebugLevel_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,1),_AlaDvmrpDebugLevel_Type())
alaDvmrpDebugLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugLevel.setStatus(_G)
class _AlaDvmrpDebugError_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugError_Type.__name__=_B
_AlaDvmrpDebugError_Object=MibScalar
alaDvmrpDebugError=_AlaDvmrpDebugError_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,2),_AlaDvmrpDebugError_Type())
alaDvmrpDebugError.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugError.setStatus(_G)
class _AlaDvmrpDebugNbr_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugNbr_Type.__name__=_B
_AlaDvmrpDebugNbr_Object=MibScalar
alaDvmrpDebugNbr=_AlaDvmrpDebugNbr_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,3),_AlaDvmrpDebugNbr_Type())
alaDvmrpDebugNbr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugNbr.setStatus(_G)
class _AlaDvmrpDebugRoutes_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugRoutes_Type.__name__=_B
_AlaDvmrpDebugRoutes_Object=MibScalar
alaDvmrpDebugRoutes=_AlaDvmrpDebugRoutes_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,4),_AlaDvmrpDebugRoutes_Type())
alaDvmrpDebugRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugRoutes.setStatus(_G)
class _AlaDvmrpDebugProbes_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugProbes_Type.__name__=_B
_AlaDvmrpDebugProbes_Object=MibScalar
alaDvmrpDebugProbes=_AlaDvmrpDebugProbes_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,5),_AlaDvmrpDebugProbes_Type())
alaDvmrpDebugProbes.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugProbes.setStatus(_G)
class _AlaDvmrpDebugPrunes_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugPrunes_Type.__name__=_B
_AlaDvmrpDebugPrunes_Object=MibScalar
alaDvmrpDebugPrunes=_AlaDvmrpDebugPrunes_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,6),_AlaDvmrpDebugPrunes_Type())
alaDvmrpDebugPrunes.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugPrunes.setStatus(_G)
class _AlaDvmrpDebugGrafts_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugGrafts_Type.__name__=_B
_AlaDvmrpDebugGrafts_Object=MibScalar
alaDvmrpDebugGrafts=_AlaDvmrpDebugGrafts_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,7),_AlaDvmrpDebugGrafts_Type())
alaDvmrpDebugGrafts.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugGrafts.setStatus(_G)
class _AlaDvmrpDebugTime_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugTime_Type.__name__=_B
_AlaDvmrpDebugTime_Object=MibScalar
alaDvmrpDebugTime=_AlaDvmrpDebugTime_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,8),_AlaDvmrpDebugTime_Type())
alaDvmrpDebugTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugTime.setStatus(_G)
class _AlaDvmrpDebugIgmp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugIgmp_Type.__name__=_B
_AlaDvmrpDebugIgmp_Object=MibScalar
alaDvmrpDebugIgmp=_AlaDvmrpDebugIgmp_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,9),_AlaDvmrpDebugIgmp_Type())
alaDvmrpDebugIgmp.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugIgmp.setStatus(_G)
class _AlaDvmrpDebugFlash_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugFlash_Type.__name__=_B
_AlaDvmrpDebugFlash_Object=MibScalar
alaDvmrpDebugFlash=_AlaDvmrpDebugFlash_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,10),_AlaDvmrpDebugFlash_Type())
alaDvmrpDebugFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugFlash.setStatus(_G)
class _AlaDvmrpDebugMip_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugMip_Type.__name__=_B
_AlaDvmrpDebugMip_Object=MibScalar
alaDvmrpDebugMip=_AlaDvmrpDebugMip_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,11),_AlaDvmrpDebugMip_Type())
alaDvmrpDebugMip.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugMip.setStatus(_G)
class _AlaDvmrpDebugInit_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugInit_Type.__name__=_B
_AlaDvmrpDebugInit_Object=MibScalar
alaDvmrpDebugInit=_AlaDvmrpDebugInit_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,12),_AlaDvmrpDebugInit_Type())
alaDvmrpDebugInit.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugInit.setStatus(_G)
class _AlaDvmrpDebugTm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugTm_Type.__name__=_B
_AlaDvmrpDebugTm_Object=MibScalar
alaDvmrpDebugTm=_AlaDvmrpDebugTm_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,13),_AlaDvmrpDebugTm_Type())
alaDvmrpDebugTm.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugTm.setStatus(_G)
class _AlaDvmrpDebugIpmrm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugIpmrm_Type.__name__=_B
_AlaDvmrpDebugIpmrm_Object=MibScalar
alaDvmrpDebugIpmrm=_AlaDvmrpDebugIpmrm_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,14),_AlaDvmrpDebugIpmrm_Type())
alaDvmrpDebugIpmrm.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugIpmrm.setStatus(_G)
class _AlaDvmrpDebugMisc_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugMisc_Type.__name__=_B
_AlaDvmrpDebugMisc_Object=MibScalar
alaDvmrpDebugMisc=_AlaDvmrpDebugMisc_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,15),_AlaDvmrpDebugMisc_Type())
alaDvmrpDebugMisc.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugMisc.setStatus(_G)
class _AlaDvmrpDebugAll_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpDebugAll_Type.__name__=_B
_AlaDvmrpDebugAll_Object=MibScalar
alaDvmrpDebugAll=_AlaDvmrpDebugAll_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,2,16),_AlaDvmrpDebugAll_Type())
alaDvmrpDebugAll.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDvmrpDebugAll.setStatus(_G)
_AlaDvmrpTunnelXIfTable_Object=MibTable
alaDvmrpTunnelXIfTable=_AlaDvmrpTunnelXIfTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,3))
if mibBuilder.loadTexts:alaDvmrpTunnelXIfTable.setStatus(_D)
_AlaDvmrpTunnelXIfEntry_Object=MibTableRow
alaDvmrpTunnelXIfEntry=_AlaDvmrpTunnelXIfEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,3,1))
alaDvmrpTunnelXIfEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:alaDvmrpTunnelXIfEntry.setStatus(_D)
_AlaDvmrpTunnelIndex_Type=Unsigned32
_AlaDvmrpTunnelIndex_Object=MibTableColumn
alaDvmrpTunnelIndex=_AlaDvmrpTunnelIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,3,1,1),_AlaDvmrpTunnelIndex_Type())
alaDvmrpTunnelIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:alaDvmrpTunnelIndex.setStatus(_D)
_AlaDvmrpLocalIfIndex_Type=Unsigned32
_AlaDvmrpLocalIfIndex_Object=MibTableColumn
alaDvmrpLocalIfIndex=_AlaDvmrpLocalIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,3,1,2),_AlaDvmrpLocalIfIndex_Type())
alaDvmrpLocalIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:alaDvmrpLocalIfIndex.setStatus(_D)
_AlaDvmrpIfAugTable_Object=MibTable
alaDvmrpIfAugTable=_AlaDvmrpIfAugTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,4))
if mibBuilder.loadTexts:alaDvmrpIfAugTable.setStatus(_D)
_AlaDvmrpIfAugEntry_Object=MibTableRow
alaDvmrpIfAugEntry=_AlaDvmrpIfAugEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,4,1))
if mibBuilder.loadTexts:alaDvmrpIfAugEntry.setStatus(_D)
class _AlaDvmrpIfBfdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaDvmrpIfBfdStatus_Type.__name__=_B
_AlaDvmrpIfBfdStatus_Object=MibTableColumn
alaDvmrpIfBfdStatus=_AlaDvmrpIfBfdStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,1,4,1,1),_AlaDvmrpIfBfdStatus_Type())
alaDvmrpIfBfdStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:alaDvmrpIfBfdStatus.setStatus(_D)
_AlcatelIND1DVMRPMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1DVMRPMIBConformance=_AlcatelIND1DVMRPMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,2))
_AlcatelIND1DVMRPMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1DVMRPMIBCompliances=_AlcatelIND1DVMRPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,2,1))
_AlcatelIND1DVMRPMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1DVMRPMIBGroups=_AlcatelIND1DVMRPMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,2,2))
dvmrpInterfaceEntry.registerAugmentions((_A,_K))
alaDvmrpIfAugEntry.setIndexNames(*dvmrpInterfaceEntry.getIndexNames())
alaDvmrpConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,2,2,1))
alaDvmrpConfigMIBGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:alaDvmrpConfigMIBGroup.setStatus(_D)
alaDvmrpDebugMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,2,2,2))
alaDvmrpDebugMIBGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:alaDvmrpDebugMIBGroup.setStatus(_D)
alaDvmrpTunnelXIfMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,2,2,3))
alaDvmrpTunnelXIfMIBGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:alaDvmrpTunnelXIfMIBGroup.setStatus(_D)
alaDvmrpIfConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,2,2,4))
alaDvmrpIfConfigGroup.setObjects((_A,_p))
if mibBuilder.loadTexts:alaDvmrpIfConfigGroup.setStatus(_D)
alaDvmrpCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,7,1,2,1,1))
alaDvmrpCompliance.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:alaDvmrpCompliance.setStatus(_D)
mibBuilder.exportSymbols(_A,**{'alcatelIND1DVMRPMIB':alcatelIND1DVMRPMIB,'alcatelIND1DVMRPMIBObjects':alcatelIND1DVMRPMIBObjects,'alaDvmrpGlobalConfig':alaDvmrpGlobalConfig,_L:alaDvmrpAdminStatus,_M:alaDvmrpRouteReportInterval,_N:alaDvmrpFlashUpdateInterval,_O:alaDvmrpNeighborTimeout,_P:alaDvmrpRouteExpirationTimeout,_Q:alaDvmrpRouteHoldDown,_R:alaDvmrpNeighborProbeInterval,_S:alaDvmrpPruneLifetime,_T:alaDvmrpPruneRetransmission,_U:alaDvmrpGraftRetransmission,_V:alaDvmrpInitNbrAsSubord,_W:alaDvmrpBfdStatus,_X:alaDvmrpBfdAllInterfaceStatus,'alaDvmrpDebugConfig':alaDvmrpDebugConfig,_Y:alaDvmrpDebugLevel,_Z:alaDvmrpDebugError,_a:alaDvmrpDebugNbr,_b:alaDvmrpDebugRoutes,_c:alaDvmrpDebugProbes,_d:alaDvmrpDebugPrunes,_e:alaDvmrpDebugGrafts,_f:alaDvmrpDebugTime,_g:alaDvmrpDebugIgmp,_h:alaDvmrpDebugFlash,_i:alaDvmrpDebugMip,_j:alaDvmrpDebugInit,_k:alaDvmrpDebugTm,_l:alaDvmrpDebugIpmrm,_m:alaDvmrpDebugMisc,_n:alaDvmrpDebugAll,'alaDvmrpTunnelXIfTable':alaDvmrpTunnelXIfTable,'alaDvmrpTunnelXIfEntry':alaDvmrpTunnelXIfEntry,_J:alaDvmrpTunnelIndex,_o:alaDvmrpLocalIfIndex,'alaDvmrpIfAugTable':alaDvmrpIfAugTable,_K:alaDvmrpIfAugEntry,_p:alaDvmrpIfBfdStatus,'alcatelIND1DVMRPMIBConformance':alcatelIND1DVMRPMIBConformance,'alcatelIND1DVMRPMIBCompliances':alcatelIND1DVMRPMIBCompliances,'alaDvmrpCompliance':alaDvmrpCompliance,'alcatelIND1DVMRPMIBGroups':alcatelIND1DVMRPMIBGroups,_q:alaDvmrpConfigMIBGroup,_r:alaDvmrpDebugMIBGroup,_s:alaDvmrpTunnelXIfMIBGroup,_t:alaDvmrpIfConfigGroup})