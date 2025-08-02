_Ah='etsysOspfExtLocalLsdbGroup'
_Ag='etsysOspfExtVirtNbrGroup'
_Af='etsysOspfExtNbrGroup'
_Ae='etsysOspfExtVirtIfGroup'
_Ad='etsysOspfExtIfGroup'
_Ac='etsysOspfExtAreaGroup'
_Ab='etsysOspfExtGlobalGroup'
_Aa='etsysOspfExtLocalLsdbAreaId'
_AZ='etsysOspfExtVirtNbrDeadTime'
_AY='etsysOspfExtVirtNbrNumRequests'
_AX='etsysOspfExtNbrAreaId'
_AW='etsysOspfExtNbrDeadTime'
_AV='etsysOspfExtNbrIfIpAddr'
_AU='etsysOspfExtNbrNumRequests'
_AT='etsysOspfExtNbrOperStatus'
_AS='etsysOspfExtNbrAdminStatus'
_AR='etsysOspfExtVirtIfMtuIgnore'
_AQ='etsysOspfExtVirtIfFastHelloMultiplier'
_AP='etsysOspfExtVirtIfMaxHtlssGracePeriod'
_AO='etsysOspfExtVirtIfHelperModePolicy'
_AN='etsysOspfExtVirtIfLsaRefreshIntvl'
_AM='etsysOspfExtVirtIfPassive'
_AL='etsysOspfExtVirtIfIPMaxPacketSize'
_AK='etsysOspfExtVirtIfTransmitTimerDelay'
_AJ='etsysOspfExtVirtIfOperStatus'
_AI='etsysOspfExtVirtIfAdminStatus'
_AH='etsysOspfExtIfMtuIgnore'
_AG='etsysOspfExtIfAutoDeleteNbr'
_AF='etsysOspfExtIfFastHelloMultiplier'
_AE='etsysOspfExtIfAuthUserData'
_AD='etsysOspfExtIfMaxHitlessGracePeriod'
_AC='etsysOspfExtIfHelperModePolicy'
_AB='etsysOspfExtIfLsaRefreshIntvl'
_AA='etsysOspfExtIfPassive'
_A9='etsysOspfExtIfIPMaxPacketSize'
_A8='etsysOspfExtIfTransmitTimerDelay'
_A7='etsysOspfExtIfNetMask'
_A6='etsysOspfExtIfOperStatus'
_A5='etsysOspfExtAreaOpLsaCksumSum'
_A4='etsysOspfExtAreaOpLsaCount'
_A3='etsysOspfExtAreaNssaLsaCksumSum'
_A2='etsysOspfExtAreaNssaLsaCount'
_A1='etsysOspfExtAreaSummAsLsaCksumSum'
_A0='etsysOspfExtAreaSummAsLsaCount'
_z='etsysOspfExtAreaSummLsaCksumSum'
_y='etsysOspfExtAreaSummLsaCount'
_x='etsysOspfExtAreaNetLsaCksumSum'
_w='etsysOspfExtAreaNetLsaCount'
_v='etsysOspfExtAreaRtrLsaCksumSum'
_u='etsysOspfExtAreaRtrLsaCount'
_t='etsysOspfExtAreaLsaRfshIntvl'
_s='etsysOspfExtAreaTransitCapability'
_r='etsysOspfExtAreaOperStatus'
_q='etsysOspfExtAreaAdminStatus'
_p='etsysOspfExtHitlessGracePeriod'
_o='etsysOspfExtDoGraceUnplannedHitless'
_n='etsysOspfExtDoGraceHitless'
_m='etsysOspfExtNumCksumsPending'
_l='etsysOspfExtNumUpdMerged'
_k='etsysOspfExtNumUpdPending'
_j='etsysOspfExtExternOpLsaCksumSum'
_i='etsysOspfExtExternOpLsaCount'
_h='etsysOspfExtExtLsaRfshIntvl'
_g='etsysOspfExtCheckAge'
_f='etsysOspfExtRteMaxEqCostPaths'
_e='etsysOspfExtCalcPauseFreq'
_d='etsysOspfExtCalcThrshIncSpfUpd'
_c='etsysOspfExtCalcThrshIncUpdates'
_b='etsysOspfExtCalcThrshUpdRestart'
_a='etsysOspfExtCalcThrshUpdStart'
_Z='etsysOspfExtCalcMaxDelay'
_Y='etsysOspfExtOperStatus'
_X='etsysOspfExtLocalLsdbEntry'
_W='etsysOspfExtVirtNbrEntry'
_V='etsysOspfExtNbrEntry'
_U='etsysOspfExtVirtIfEntry'
_T='etsysOspfExtIfEntry'
_S='etsysOspfExtAreaEntry'
_R='reasonSwitchToBackup'
_Q='reasonSoftwareReload'
_P='reasonSoftwareRestart'
_O='reasonUnknown'
_N='IpAddress'
_M='OctetString'
_L='milliseconds'
_K='Bits'
_J='Status'
_I='Integer32'
_H='seconds'
_G='TruthValue'
_F='read-write'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='ENTERASYS-OSPF-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
AreaID,Status,ospfAreaEntry,ospfIfEntry,ospfLocalLsdbEntry,ospfNbrEntry,ospfVirtIfEntry,ospfVirtNbrEntry=mibBuilder.importSymbols('OSPF-MIB','AreaID',_J,'ospfAreaEntry','ospfIfEntry','ospfLocalLsdbEntry','ospfNbrEntry','ospfVirtIfEntry','ospfVirtNbrEntry')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_K,_K,'Counter32','Counter64','Gauge32',_I,_N,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_G)
etsysOspfExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,65))
if mibBuilder.loadTexts:etsysOspfExtMIB.setRevisions(('2009-02-27 19:34',))
class EtsysOspfOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('operStatusUp',1),('operStatusDown',2),('operStatusGoingUp',3),('operStatusGoingDown',4),('operStatusActFailed',5)))
_EtsysOspfExtObjects_ObjectIdentity=ObjectIdentity
etsysOspfExtObjects=_EtsysOspfExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,65,1))
_EtsysOspfExtGlobals_ObjectIdentity=ObjectIdentity
etsysOspfExtGlobals=_EtsysOspfExtGlobals_ObjectIdentity((1,3,6,1,4,1,5624,1,2,65,1,1))
_EtsysOspfExtOperStatus_Type=EtsysOspfOperStatus
_EtsysOspfExtOperStatus_Object=MibScalar
etsysOspfExtOperStatus=_EtsysOspfExtOperStatus_Object((1,3,6,1,4,1,5624,1,2,65,1,1,1),_EtsysOspfExtOperStatus_Type())
etsysOspfExtOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtOperStatus.setStatus(_A)
class _EtsysOspfExtCalcMaxDelay_Type(Unsigned32):defaultValue=5000
_EtsysOspfExtCalcMaxDelay_Type.__name__=_E
_EtsysOspfExtCalcMaxDelay_Object=MibScalar
etsysOspfExtCalcMaxDelay=_EtsysOspfExtCalcMaxDelay_Object((1,3,6,1,4,1,5624,1,2,65,1,1,2),_EtsysOspfExtCalcMaxDelay_Type())
etsysOspfExtCalcMaxDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysOspfExtCalcMaxDelay.setStatus(_A)
if mibBuilder.loadTexts:etsysOspfExtCalcMaxDelay.setUnits(_L)
class _EtsysOspfExtCalcThrshUpdStart_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_EtsysOspfExtCalcThrshUpdStart_Type.__name__=_I
_EtsysOspfExtCalcThrshUpdStart_Object=MibScalar
etsysOspfExtCalcThrshUpdStart=_EtsysOspfExtCalcThrshUpdStart_Object((1,3,6,1,4,1,5624,1,2,65,1,1,3),_EtsysOspfExtCalcThrshUpdStart_Type())
etsysOspfExtCalcThrshUpdStart.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysOspfExtCalcThrshUpdStart.setStatus(_A)
class _EtsysOspfExtCalcThrshUpdRestart_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_EtsysOspfExtCalcThrshUpdRestart_Type.__name__=_I
_EtsysOspfExtCalcThrshUpdRestart_Object=MibScalar
etsysOspfExtCalcThrshUpdRestart=_EtsysOspfExtCalcThrshUpdRestart_Object((1,3,6,1,4,1,5624,1,2,65,1,1,4),_EtsysOspfExtCalcThrshUpdRestart_Type())
etsysOspfExtCalcThrshUpdRestart.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysOspfExtCalcThrshUpdRestart.setStatus(_A)
class _EtsysOspfExtCalcThrshIncUpdates_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_EtsysOspfExtCalcThrshIncUpdates_Type.__name__=_I
_EtsysOspfExtCalcThrshIncUpdates_Object=MibScalar
etsysOspfExtCalcThrshIncUpdates=_EtsysOspfExtCalcThrshIncUpdates_Object((1,3,6,1,4,1,5624,1,2,65,1,1,5),_EtsysOspfExtCalcThrshIncUpdates_Type())
etsysOspfExtCalcThrshIncUpdates.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysOspfExtCalcThrshIncUpdates.setStatus(_A)
class _EtsysOspfExtCalcThrshIncSpfUpd_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_EtsysOspfExtCalcThrshIncSpfUpd_Type.__name__=_I
_EtsysOspfExtCalcThrshIncSpfUpd_Object=MibScalar
etsysOspfExtCalcThrshIncSpfUpd=_EtsysOspfExtCalcThrshIncSpfUpd_Object((1,3,6,1,4,1,5624,1,2,65,1,1,6),_EtsysOspfExtCalcThrshIncSpfUpd_Type())
etsysOspfExtCalcThrshIncSpfUpd.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysOspfExtCalcThrshIncSpfUpd.setStatus(_A)
class _EtsysOspfExtCalcPauseFreq_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_EtsysOspfExtCalcPauseFreq_Type.__name__=_I
_EtsysOspfExtCalcPauseFreq_Object=MibScalar
etsysOspfExtCalcPauseFreq=_EtsysOspfExtCalcPauseFreq_Object((1,3,6,1,4,1,5624,1,2,65,1,1,7),_EtsysOspfExtCalcPauseFreq_Type())
etsysOspfExtCalcPauseFreq.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysOspfExtCalcPauseFreq.setStatus(_A)
class _EtsysOspfExtRteMaxEqCostPaths_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysOspfExtRteMaxEqCostPaths_Type.__name__=_E
_EtsysOspfExtRteMaxEqCostPaths_Object=MibScalar
etsysOspfExtRteMaxEqCostPaths=_EtsysOspfExtRteMaxEqCostPaths_Object((1,3,6,1,4,1,5624,1,2,65,1,1,8),_EtsysOspfExtRteMaxEqCostPaths_Type())
etsysOspfExtRteMaxEqCostPaths.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysOspfExtRteMaxEqCostPaths.setStatus(_A)
class _EtsysOspfExtCheckAge_Type(Unsigned32):defaultValue=300
_EtsysOspfExtCheckAge_Type.__name__=_E
_EtsysOspfExtCheckAge_Object=MibScalar
etsysOspfExtCheckAge=_EtsysOspfExtCheckAge_Object((1,3,6,1,4,1,5624,1,2,65,1,1,9),_EtsysOspfExtCheckAge_Type())
etsysOspfExtCheckAge.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysOspfExtCheckAge.setStatus(_A)
if mibBuilder.loadTexts:etsysOspfExtCheckAge.setUnits(_H)
class _EtsysOspfExtExtLsaRfshIntvl_Type(Unsigned32):defaultValue=1800;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3599))
_EtsysOspfExtExtLsaRfshIntvl_Type.__name__=_E
_EtsysOspfExtExtLsaRfshIntvl_Object=MibScalar
etsysOspfExtExtLsaRfshIntvl=_EtsysOspfExtExtLsaRfshIntvl_Object((1,3,6,1,4,1,5624,1,2,65,1,1,10),_EtsysOspfExtExtLsaRfshIntvl_Type())
etsysOspfExtExtLsaRfshIntvl.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysOspfExtExtLsaRfshIntvl.setStatus(_A)
if mibBuilder.loadTexts:etsysOspfExtExtLsaRfshIntvl.setUnits(_H)
_EtsysOspfExtExternOpLsaCount_Type=Gauge32
_EtsysOspfExtExternOpLsaCount_Object=MibScalar
etsysOspfExtExternOpLsaCount=_EtsysOspfExtExternOpLsaCount_Object((1,3,6,1,4,1,5624,1,2,65,1,1,11),_EtsysOspfExtExternOpLsaCount_Type())
etsysOspfExtExternOpLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtExternOpLsaCount.setStatus(_A)
_EtsysOspfExtExternOpLsaCksumSum_Type=Unsigned32
_EtsysOspfExtExternOpLsaCksumSum_Object=MibScalar
etsysOspfExtExternOpLsaCksumSum=_EtsysOspfExtExternOpLsaCksumSum_Object((1,3,6,1,4,1,5624,1,2,65,1,1,12),_EtsysOspfExtExternOpLsaCksumSum_Type())
etsysOspfExtExternOpLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtExternOpLsaCksumSum.setStatus(_A)
_EtsysOspfExtNumUpdPending_Type=Gauge32
_EtsysOspfExtNumUpdPending_Object=MibScalar
etsysOspfExtNumUpdPending=_EtsysOspfExtNumUpdPending_Object((1,3,6,1,4,1,5624,1,2,65,1,1,13),_EtsysOspfExtNumUpdPending_Type())
etsysOspfExtNumUpdPending.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtNumUpdPending.setStatus(_A)
_EtsysOspfExtNumUpdMerged_Type=Gauge32
_EtsysOspfExtNumUpdMerged_Object=MibScalar
etsysOspfExtNumUpdMerged=_EtsysOspfExtNumUpdMerged_Object((1,3,6,1,4,1,5624,1,2,65,1,1,14),_EtsysOspfExtNumUpdMerged_Type())
etsysOspfExtNumUpdMerged.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtNumUpdMerged.setStatus(_A)
_EtsysOspfExtNumCksumsPending_Type=Gauge32
_EtsysOspfExtNumCksumsPending_Object=MibScalar
etsysOspfExtNumCksumsPending=_EtsysOspfExtNumCksumsPending_Object((1,3,6,1,4,1,5624,1,2,65,1,1,15),_EtsysOspfExtNumCksumsPending_Type())
etsysOspfExtNumCksumsPending.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtNumCksumsPending.setStatus(_A)
class _EtsysOspfExtDoGraceHitless_Type(TruthValue):defaultValue=2
_EtsysOspfExtDoGraceHitless_Type.__name__=_G
_EtsysOspfExtDoGraceHitless_Object=MibScalar
etsysOspfExtDoGraceHitless=_EtsysOspfExtDoGraceHitless_Object((1,3,6,1,4,1,5624,1,2,65,1,1,16),_EtsysOspfExtDoGraceHitless_Type())
etsysOspfExtDoGraceHitless.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysOspfExtDoGraceHitless.setStatus(_A)
class _EtsysOspfExtDoGraceUnplannedHitless_Type(TruthValue):defaultValue=2
_EtsysOspfExtDoGraceUnplannedHitless_Type.__name__=_G
_EtsysOspfExtDoGraceUnplannedHitless_Object=MibScalar
etsysOspfExtDoGraceUnplannedHitless=_EtsysOspfExtDoGraceUnplannedHitless_Object((1,3,6,1,4,1,5624,1,2,65,1,1,17),_EtsysOspfExtDoGraceUnplannedHitless_Type())
etsysOspfExtDoGraceUnplannedHitless.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysOspfExtDoGraceUnplannedHitless.setStatus(_A)
class _EtsysOspfExtHitlessGracePeriod_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_EtsysOspfExtHitlessGracePeriod_Type.__name__=_E
_EtsysOspfExtHitlessGracePeriod_Object=MibScalar
etsysOspfExtHitlessGracePeriod=_EtsysOspfExtHitlessGracePeriod_Object((1,3,6,1,4,1,5624,1,2,65,1,1,18),_EtsysOspfExtHitlessGracePeriod_Type())
etsysOspfExtHitlessGracePeriod.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysOspfExtHitlessGracePeriod.setStatus(_A)
if mibBuilder.loadTexts:etsysOspfExtHitlessGracePeriod.setUnits(_H)
_EtsysOspfExtTables_ObjectIdentity=ObjectIdentity
etsysOspfExtTables=_EtsysOspfExtTables_ObjectIdentity((1,3,6,1,4,1,5624,1,2,65,1,2))
_EtsysOspfExtAreaTable_Object=MibTable
etsysOspfExtAreaTable=_EtsysOspfExtAreaTable_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1))
if mibBuilder.loadTexts:etsysOspfExtAreaTable.setStatus(_A)
_EtsysOspfExtAreaEntry_Object=MibTableRow
etsysOspfExtAreaEntry=_EtsysOspfExtAreaEntry_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1))
if mibBuilder.loadTexts:etsysOspfExtAreaEntry.setStatus(_A)
class _EtsysOspfExtAreaAdminStatus_Type(Status):defaultValue=1
_EtsysOspfExtAreaAdminStatus_Type.__name__=_J
_EtsysOspfExtAreaAdminStatus_Object=MibTableColumn
etsysOspfExtAreaAdminStatus=_EtsysOspfExtAreaAdminStatus_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,1),_EtsysOspfExtAreaAdminStatus_Type())
etsysOspfExtAreaAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtAreaAdminStatus.setStatus(_A)
_EtsysOspfExtAreaOperStatus_Type=EtsysOspfOperStatus
_EtsysOspfExtAreaOperStatus_Object=MibTableColumn
etsysOspfExtAreaOperStatus=_EtsysOspfExtAreaOperStatus_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,2),_EtsysOspfExtAreaOperStatus_Type())
etsysOspfExtAreaOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaOperStatus.setStatus(_A)
class _EtsysOspfExtAreaTransitCapability_Type(TruthValue):defaultValue=2
_EtsysOspfExtAreaTransitCapability_Type.__name__=_G
_EtsysOspfExtAreaTransitCapability_Object=MibTableColumn
etsysOspfExtAreaTransitCapability=_EtsysOspfExtAreaTransitCapability_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,3),_EtsysOspfExtAreaTransitCapability_Type())
etsysOspfExtAreaTransitCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaTransitCapability.setStatus(_A)
class _EtsysOspfExtAreaLsaRfshIntvl_Type(Unsigned32):defaultValue=1800;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3599))
_EtsysOspfExtAreaLsaRfshIntvl_Type.__name__=_E
_EtsysOspfExtAreaLsaRfshIntvl_Object=MibTableColumn
etsysOspfExtAreaLsaRfshIntvl=_EtsysOspfExtAreaLsaRfshIntvl_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,4),_EtsysOspfExtAreaLsaRfshIntvl_Type())
etsysOspfExtAreaLsaRfshIntvl.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtAreaLsaRfshIntvl.setStatus(_A)
if mibBuilder.loadTexts:etsysOspfExtAreaLsaRfshIntvl.setUnits(_H)
_EtsysOspfExtAreaRtrLsaCount_Type=Gauge32
_EtsysOspfExtAreaRtrLsaCount_Object=MibTableColumn
etsysOspfExtAreaRtrLsaCount=_EtsysOspfExtAreaRtrLsaCount_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,5),_EtsysOspfExtAreaRtrLsaCount_Type())
etsysOspfExtAreaRtrLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaRtrLsaCount.setStatus(_A)
_EtsysOspfExtAreaRtrLsaCksumSum_Type=Unsigned32
_EtsysOspfExtAreaRtrLsaCksumSum_Object=MibTableColumn
etsysOspfExtAreaRtrLsaCksumSum=_EtsysOspfExtAreaRtrLsaCksumSum_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,6),_EtsysOspfExtAreaRtrLsaCksumSum_Type())
etsysOspfExtAreaRtrLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaRtrLsaCksumSum.setStatus(_A)
_EtsysOspfExtAreaNetLsaCount_Type=Gauge32
_EtsysOspfExtAreaNetLsaCount_Object=MibTableColumn
etsysOspfExtAreaNetLsaCount=_EtsysOspfExtAreaNetLsaCount_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,7),_EtsysOspfExtAreaNetLsaCount_Type())
etsysOspfExtAreaNetLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaNetLsaCount.setStatus(_A)
_EtsysOspfExtAreaNetLsaCksumSum_Type=Unsigned32
_EtsysOspfExtAreaNetLsaCksumSum_Object=MibTableColumn
etsysOspfExtAreaNetLsaCksumSum=_EtsysOspfExtAreaNetLsaCksumSum_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,8),_EtsysOspfExtAreaNetLsaCksumSum_Type())
etsysOspfExtAreaNetLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaNetLsaCksumSum.setStatus(_A)
_EtsysOspfExtAreaSummLsaCount_Type=Gauge32
_EtsysOspfExtAreaSummLsaCount_Object=MibTableColumn
etsysOspfExtAreaSummLsaCount=_EtsysOspfExtAreaSummLsaCount_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,9),_EtsysOspfExtAreaSummLsaCount_Type())
etsysOspfExtAreaSummLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaSummLsaCount.setStatus(_A)
_EtsysOspfExtAreaSummLsaCksumSum_Type=Unsigned32
_EtsysOspfExtAreaSummLsaCksumSum_Object=MibTableColumn
etsysOspfExtAreaSummLsaCksumSum=_EtsysOspfExtAreaSummLsaCksumSum_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,10),_EtsysOspfExtAreaSummLsaCksumSum_Type())
etsysOspfExtAreaSummLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaSummLsaCksumSum.setStatus(_A)
_EtsysOspfExtAreaSummAsLsaCount_Type=Gauge32
_EtsysOspfExtAreaSummAsLsaCount_Object=MibTableColumn
etsysOspfExtAreaSummAsLsaCount=_EtsysOspfExtAreaSummAsLsaCount_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,11),_EtsysOspfExtAreaSummAsLsaCount_Type())
etsysOspfExtAreaSummAsLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaSummAsLsaCount.setStatus(_A)
_EtsysOspfExtAreaSummAsLsaCksumSum_Type=Unsigned32
_EtsysOspfExtAreaSummAsLsaCksumSum_Object=MibTableColumn
etsysOspfExtAreaSummAsLsaCksumSum=_EtsysOspfExtAreaSummAsLsaCksumSum_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,12),_EtsysOspfExtAreaSummAsLsaCksumSum_Type())
etsysOspfExtAreaSummAsLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaSummAsLsaCksumSum.setStatus(_A)
_EtsysOspfExtAreaNssaLsaCount_Type=Gauge32
_EtsysOspfExtAreaNssaLsaCount_Object=MibTableColumn
etsysOspfExtAreaNssaLsaCount=_EtsysOspfExtAreaNssaLsaCount_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,13),_EtsysOspfExtAreaNssaLsaCount_Type())
etsysOspfExtAreaNssaLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaNssaLsaCount.setStatus(_A)
_EtsysOspfExtAreaNssaLsaCksumSum_Type=Unsigned32
_EtsysOspfExtAreaNssaLsaCksumSum_Object=MibTableColumn
etsysOspfExtAreaNssaLsaCksumSum=_EtsysOspfExtAreaNssaLsaCksumSum_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,14),_EtsysOspfExtAreaNssaLsaCksumSum_Type())
etsysOspfExtAreaNssaLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaNssaLsaCksumSum.setStatus(_A)
_EtsysOspfExtAreaOpLsaCount_Type=Gauge32
_EtsysOspfExtAreaOpLsaCount_Object=MibTableColumn
etsysOspfExtAreaOpLsaCount=_EtsysOspfExtAreaOpLsaCount_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,15),_EtsysOspfExtAreaOpLsaCount_Type())
etsysOspfExtAreaOpLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaOpLsaCount.setStatus(_A)
_EtsysOspfExtAreaOpLsaCksumSum_Type=Unsigned32
_EtsysOspfExtAreaOpLsaCksumSum_Object=MibTableColumn
etsysOspfExtAreaOpLsaCksumSum=_EtsysOspfExtAreaOpLsaCksumSum_Object((1,3,6,1,4,1,5624,1,2,65,1,2,1,1,16),_EtsysOspfExtAreaOpLsaCksumSum_Type())
etsysOspfExtAreaOpLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtAreaOpLsaCksumSum.setStatus(_A)
_EtsysOspfExtIfTable_Object=MibTable
etsysOspfExtIfTable=_EtsysOspfExtIfTable_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2))
if mibBuilder.loadTexts:etsysOspfExtIfTable.setStatus(_A)
_EtsysOspfExtIfEntry_Object=MibTableRow
etsysOspfExtIfEntry=_EtsysOspfExtIfEntry_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2,1))
if mibBuilder.loadTexts:etsysOspfExtIfEntry.setStatus(_A)
_EtsysOspfExtIfOperStatus_Type=EtsysOspfOperStatus
_EtsysOspfExtIfOperStatus_Object=MibTableColumn
etsysOspfExtIfOperStatus=_EtsysOspfExtIfOperStatus_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2,1,1),_EtsysOspfExtIfOperStatus_Type())
etsysOspfExtIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtIfOperStatus.setStatus(_A)
_EtsysOspfExtIfNetMask_Type=IpAddress
_EtsysOspfExtIfNetMask_Object=MibTableColumn
etsysOspfExtIfNetMask=_EtsysOspfExtIfNetMask_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2,1,2),_EtsysOspfExtIfNetMask_Type())
etsysOspfExtIfNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtIfNetMask.setStatus(_A)
class _EtsysOspfExtIfTransmitTimerDelay_Type(Unsigned32):defaultValue=100
_EtsysOspfExtIfTransmitTimerDelay_Type.__name__=_E
_EtsysOspfExtIfTransmitTimerDelay_Object=MibTableColumn
etsysOspfExtIfTransmitTimerDelay=_EtsysOspfExtIfTransmitTimerDelay_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2,1,3),_EtsysOspfExtIfTransmitTimerDelay_Type())
etsysOspfExtIfTransmitTimerDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtIfTransmitTimerDelay.setStatus(_A)
if mibBuilder.loadTexts:etsysOspfExtIfTransmitTimerDelay.setUnits(_L)
class _EtsysOspfExtIfIPMaxPacketSize_Type(Unsigned32):defaultValue=576
_EtsysOspfExtIfIPMaxPacketSize_Type.__name__=_E
_EtsysOspfExtIfIPMaxPacketSize_Object=MibTableColumn
etsysOspfExtIfIPMaxPacketSize=_EtsysOspfExtIfIPMaxPacketSize_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2,1,4),_EtsysOspfExtIfIPMaxPacketSize_Type())
etsysOspfExtIfIPMaxPacketSize.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtIfIPMaxPacketSize.setStatus(_A)
class _EtsysOspfExtIfPassive_Type(TruthValue):defaultValue=2
_EtsysOspfExtIfPassive_Type.__name__=_G
_EtsysOspfExtIfPassive_Object=MibTableColumn
etsysOspfExtIfPassive=_EtsysOspfExtIfPassive_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2,1,5),_EtsysOspfExtIfPassive_Type())
etsysOspfExtIfPassive.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtIfPassive.setStatus(_A)
class _EtsysOspfExtIfLsaRefreshIntvl_Type(Unsigned32):defaultValue=1800;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3599))
_EtsysOspfExtIfLsaRefreshIntvl_Type.__name__=_E
_EtsysOspfExtIfLsaRefreshIntvl_Object=MibTableColumn
etsysOspfExtIfLsaRefreshIntvl=_EtsysOspfExtIfLsaRefreshIntvl_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2,1,6),_EtsysOspfExtIfLsaRefreshIntvl_Type())
etsysOspfExtIfLsaRefreshIntvl.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtIfLsaRefreshIntvl.setStatus(_A)
if mibBuilder.loadTexts:etsysOspfExtIfLsaRefreshIntvl.setUnits(_H)
class _EtsysOspfExtIfHelperModePolicy_Type(Bits):defaultBinValue='1111';namedValues=NamedValues(*((_O,0),(_P,1),(_Q,2),(_R,3)))
_EtsysOspfExtIfHelperModePolicy_Type.__name__=_K
_EtsysOspfExtIfHelperModePolicy_Object=MibTableColumn
etsysOspfExtIfHelperModePolicy=_EtsysOspfExtIfHelperModePolicy_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2,1,7),_EtsysOspfExtIfHelperModePolicy_Type())
etsysOspfExtIfHelperModePolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtIfHelperModePolicy.setStatus(_A)
class _EtsysOspfExtIfMaxHitlessGracePeriod_Type(Unsigned32):defaultValue=120
_EtsysOspfExtIfMaxHitlessGracePeriod_Type.__name__=_E
_EtsysOspfExtIfMaxHitlessGracePeriod_Object=MibTableColumn
etsysOspfExtIfMaxHitlessGracePeriod=_EtsysOspfExtIfMaxHitlessGracePeriod_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2,1,8),_EtsysOspfExtIfMaxHitlessGracePeriod_Type())
etsysOspfExtIfMaxHitlessGracePeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtIfMaxHitlessGracePeriod.setStatus(_A)
if mibBuilder.loadTexts:etsysOspfExtIfMaxHitlessGracePeriod.setUnits(_H)
class _EtsysOspfExtIfAuthUserData_Type(OctetString):defaultHexValue='00';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_EtsysOspfExtIfAuthUserData_Type.__name__=_M
_EtsysOspfExtIfAuthUserData_Object=MibTableColumn
etsysOspfExtIfAuthUserData=_EtsysOspfExtIfAuthUserData_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2,1,9),_EtsysOspfExtIfAuthUserData_Type())
etsysOspfExtIfAuthUserData.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtIfAuthUserData.setStatus(_A)
class _EtsysOspfExtIfFastHelloMultiplier_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,20))
_EtsysOspfExtIfFastHelloMultiplier_Type.__name__=_E
_EtsysOspfExtIfFastHelloMultiplier_Object=MibTableColumn
etsysOspfExtIfFastHelloMultiplier=_EtsysOspfExtIfFastHelloMultiplier_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2,1,10),_EtsysOspfExtIfFastHelloMultiplier_Type())
etsysOspfExtIfFastHelloMultiplier.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtIfFastHelloMultiplier.setStatus(_A)
class _EtsysOspfExtIfAutoDeleteNbr_Type(TruthValue):defaultValue=1
_EtsysOspfExtIfAutoDeleteNbr_Type.__name__=_G
_EtsysOspfExtIfAutoDeleteNbr_Object=MibTableColumn
etsysOspfExtIfAutoDeleteNbr=_EtsysOspfExtIfAutoDeleteNbr_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2,1,11),_EtsysOspfExtIfAutoDeleteNbr_Type())
etsysOspfExtIfAutoDeleteNbr.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtIfAutoDeleteNbr.setStatus(_A)
class _EtsysOspfExtIfMtuIgnore_Type(TruthValue):defaultValue=2
_EtsysOspfExtIfMtuIgnore_Type.__name__=_G
_EtsysOspfExtIfMtuIgnore_Object=MibTableColumn
etsysOspfExtIfMtuIgnore=_EtsysOspfExtIfMtuIgnore_Object((1,3,6,1,4,1,5624,1,2,65,1,2,2,1,12),_EtsysOspfExtIfMtuIgnore_Type())
etsysOspfExtIfMtuIgnore.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtIfMtuIgnore.setStatus(_A)
_EtsysOspfExtVirtIfTable_Object=MibTable
etsysOspfExtVirtIfTable=_EtsysOspfExtVirtIfTable_Object((1,3,6,1,4,1,5624,1,2,65,1,2,3))
if mibBuilder.loadTexts:etsysOspfExtVirtIfTable.setStatus(_A)
_EtsysOspfExtVirtIfEntry_Object=MibTableRow
etsysOspfExtVirtIfEntry=_EtsysOspfExtVirtIfEntry_Object((1,3,6,1,4,1,5624,1,2,65,1,2,3,1))
if mibBuilder.loadTexts:etsysOspfExtVirtIfEntry.setStatus(_A)
class _EtsysOspfExtVirtIfAdminStatus_Type(Status):defaultValue=1
_EtsysOspfExtVirtIfAdminStatus_Type.__name__=_J
_EtsysOspfExtVirtIfAdminStatus_Object=MibTableColumn
etsysOspfExtVirtIfAdminStatus=_EtsysOspfExtVirtIfAdminStatus_Object((1,3,6,1,4,1,5624,1,2,65,1,2,3,1,1),_EtsysOspfExtVirtIfAdminStatus_Type())
etsysOspfExtVirtIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtVirtIfAdminStatus.setStatus(_A)
_EtsysOspfExtVirtIfOperStatus_Type=EtsysOspfOperStatus
_EtsysOspfExtVirtIfOperStatus_Object=MibTableColumn
etsysOspfExtVirtIfOperStatus=_EtsysOspfExtVirtIfOperStatus_Object((1,3,6,1,4,1,5624,1,2,65,1,2,3,1,2),_EtsysOspfExtVirtIfOperStatus_Type())
etsysOspfExtVirtIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtVirtIfOperStatus.setStatus(_A)
class _EtsysOspfExtVirtIfTransmitTimerDelay_Type(Unsigned32):defaultValue=100
_EtsysOspfExtVirtIfTransmitTimerDelay_Type.__name__=_E
_EtsysOspfExtVirtIfTransmitTimerDelay_Object=MibTableColumn
etsysOspfExtVirtIfTransmitTimerDelay=_EtsysOspfExtVirtIfTransmitTimerDelay_Object((1,3,6,1,4,1,5624,1,2,65,1,2,3,1,3),_EtsysOspfExtVirtIfTransmitTimerDelay_Type())
etsysOspfExtVirtIfTransmitTimerDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtVirtIfTransmitTimerDelay.setStatus(_A)
if mibBuilder.loadTexts:etsysOspfExtVirtIfTransmitTimerDelay.setUnits(_L)
class _EtsysOspfExtVirtIfIPMaxPacketSize_Type(Unsigned32):defaultValue=576
_EtsysOspfExtVirtIfIPMaxPacketSize_Type.__name__=_E
_EtsysOspfExtVirtIfIPMaxPacketSize_Object=MibTableColumn
etsysOspfExtVirtIfIPMaxPacketSize=_EtsysOspfExtVirtIfIPMaxPacketSize_Object((1,3,6,1,4,1,5624,1,2,65,1,2,3,1,4),_EtsysOspfExtVirtIfIPMaxPacketSize_Type())
etsysOspfExtVirtIfIPMaxPacketSize.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtVirtIfIPMaxPacketSize.setStatus(_A)
class _EtsysOspfExtVirtIfPassive_Type(TruthValue):defaultValue=2
_EtsysOspfExtVirtIfPassive_Type.__name__=_G
_EtsysOspfExtVirtIfPassive_Object=MibTableColumn
etsysOspfExtVirtIfPassive=_EtsysOspfExtVirtIfPassive_Object((1,3,6,1,4,1,5624,1,2,65,1,2,3,1,5),_EtsysOspfExtVirtIfPassive_Type())
etsysOspfExtVirtIfPassive.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtVirtIfPassive.setStatus(_A)
class _EtsysOspfExtVirtIfLsaRefreshIntvl_Type(Unsigned32):defaultValue=1800;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3599))
_EtsysOspfExtVirtIfLsaRefreshIntvl_Type.__name__=_E
_EtsysOspfExtVirtIfLsaRefreshIntvl_Object=MibTableColumn
etsysOspfExtVirtIfLsaRefreshIntvl=_EtsysOspfExtVirtIfLsaRefreshIntvl_Object((1,3,6,1,4,1,5624,1,2,65,1,2,3,1,6),_EtsysOspfExtVirtIfLsaRefreshIntvl_Type())
etsysOspfExtVirtIfLsaRefreshIntvl.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtVirtIfLsaRefreshIntvl.setStatus(_A)
if mibBuilder.loadTexts:etsysOspfExtVirtIfLsaRefreshIntvl.setUnits(_H)
class _EtsysOspfExtVirtIfHelperModePolicy_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*((_O,0),(_P,1),(_Q,2),(_R,3)))
_EtsysOspfExtVirtIfHelperModePolicy_Type.__name__=_K
_EtsysOspfExtVirtIfHelperModePolicy_Object=MibTableColumn
etsysOspfExtVirtIfHelperModePolicy=_EtsysOspfExtVirtIfHelperModePolicy_Object((1,3,6,1,4,1,5624,1,2,65,1,2,3,1,7),_EtsysOspfExtVirtIfHelperModePolicy_Type())
etsysOspfExtVirtIfHelperModePolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtVirtIfHelperModePolicy.setStatus(_A)
class _EtsysOspfExtVirtIfMaxHtlssGracePeriod_Type(Unsigned32):defaultValue=120
_EtsysOspfExtVirtIfMaxHtlssGracePeriod_Type.__name__=_E
_EtsysOspfExtVirtIfMaxHtlssGracePeriod_Object=MibTableColumn
etsysOspfExtVirtIfMaxHtlssGracePeriod=_EtsysOspfExtVirtIfMaxHtlssGracePeriod_Object((1,3,6,1,4,1,5624,1,2,65,1,2,3,1,8),_EtsysOspfExtVirtIfMaxHtlssGracePeriod_Type())
etsysOspfExtVirtIfMaxHtlssGracePeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtVirtIfMaxHtlssGracePeriod.setStatus(_A)
if mibBuilder.loadTexts:etsysOspfExtVirtIfMaxHtlssGracePeriod.setUnits(_H)
class _EtsysOspfExtVirtIfFastHelloMultiplier_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,20))
_EtsysOspfExtVirtIfFastHelloMultiplier_Type.__name__=_E
_EtsysOspfExtVirtIfFastHelloMultiplier_Object=MibTableColumn
etsysOspfExtVirtIfFastHelloMultiplier=_EtsysOspfExtVirtIfFastHelloMultiplier_Object((1,3,6,1,4,1,5624,1,2,65,1,2,3,1,9),_EtsysOspfExtVirtIfFastHelloMultiplier_Type())
etsysOspfExtVirtIfFastHelloMultiplier.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtVirtIfFastHelloMultiplier.setStatus(_A)
class _EtsysOspfExtVirtIfMtuIgnore_Type(TruthValue):defaultValue=2
_EtsysOspfExtVirtIfMtuIgnore_Type.__name__=_G
_EtsysOspfExtVirtIfMtuIgnore_Object=MibTableColumn
etsysOspfExtVirtIfMtuIgnore=_EtsysOspfExtVirtIfMtuIgnore_Object((1,3,6,1,4,1,5624,1,2,65,1,2,3,1,10),_EtsysOspfExtVirtIfMtuIgnore_Type())
etsysOspfExtVirtIfMtuIgnore.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtVirtIfMtuIgnore.setStatus(_A)
_EtsysOspfExtNbrTable_Object=MibTable
etsysOspfExtNbrTable=_EtsysOspfExtNbrTable_Object((1,3,6,1,4,1,5624,1,2,65,1,2,4))
if mibBuilder.loadTexts:etsysOspfExtNbrTable.setStatus(_A)
_EtsysOspfExtNbrEntry_Object=MibTableRow
etsysOspfExtNbrEntry=_EtsysOspfExtNbrEntry_Object((1,3,6,1,4,1,5624,1,2,65,1,2,4,1))
if mibBuilder.loadTexts:etsysOspfExtNbrEntry.setStatus(_A)
class _EtsysOspfExtNbrAdminStatus_Type(Status):defaultValue=1
_EtsysOspfExtNbrAdminStatus_Type.__name__=_J
_EtsysOspfExtNbrAdminStatus_Object=MibTableColumn
etsysOspfExtNbrAdminStatus=_EtsysOspfExtNbrAdminStatus_Object((1,3,6,1,4,1,5624,1,2,65,1,2,4,1,1),_EtsysOspfExtNbrAdminStatus_Type())
etsysOspfExtNbrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtNbrAdminStatus.setStatus(_A)
_EtsysOspfExtNbrOperStatus_Type=EtsysOspfOperStatus
_EtsysOspfExtNbrOperStatus_Object=MibTableColumn
etsysOspfExtNbrOperStatus=_EtsysOspfExtNbrOperStatus_Object((1,3,6,1,4,1,5624,1,2,65,1,2,4,1,2),_EtsysOspfExtNbrOperStatus_Type())
etsysOspfExtNbrOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtNbrOperStatus.setStatus(_A)
_EtsysOspfExtNbrNumRequests_Type=Gauge32
_EtsysOspfExtNbrNumRequests_Object=MibTableColumn
etsysOspfExtNbrNumRequests=_EtsysOspfExtNbrNumRequests_Object((1,3,6,1,4,1,5624,1,2,65,1,2,4,1,3),_EtsysOspfExtNbrNumRequests_Type())
etsysOspfExtNbrNumRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtNbrNumRequests.setStatus(_A)
class _EtsysOspfExtNbrIfIpAddr_Type(IpAddress):defaultHexValue='00000000'
_EtsysOspfExtNbrIfIpAddr_Type.__name__=_N
_EtsysOspfExtNbrIfIpAddr_Object=MibTableColumn
etsysOspfExtNbrIfIpAddr=_EtsysOspfExtNbrIfIpAddr_Object((1,3,6,1,4,1,5624,1,2,65,1,2,4,1,4),_EtsysOspfExtNbrIfIpAddr_Type())
etsysOspfExtNbrIfIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysOspfExtNbrIfIpAddr.setStatus(_A)
class _EtsysOspfExtNbrDeadTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EtsysOspfExtNbrDeadTime_Type.__name__=_E
_EtsysOspfExtNbrDeadTime_Object=MibTableColumn
etsysOspfExtNbrDeadTime=_EtsysOspfExtNbrDeadTime_Object((1,3,6,1,4,1,5624,1,2,65,1,2,4,1,5),_EtsysOspfExtNbrDeadTime_Type())
etsysOspfExtNbrDeadTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtNbrDeadTime.setStatus(_A)
if mibBuilder.loadTexts:etsysOspfExtNbrDeadTime.setUnits(_H)
_EtsysOspfExtNbrAreaId_Type=AreaID
_EtsysOspfExtNbrAreaId_Object=MibTableColumn
etsysOspfExtNbrAreaId=_EtsysOspfExtNbrAreaId_Object((1,3,6,1,4,1,5624,1,2,65,1,2,4,1,6),_EtsysOspfExtNbrAreaId_Type())
etsysOspfExtNbrAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtNbrAreaId.setStatus(_A)
_EtsysOspfExtVirtNbrTable_Object=MibTable
etsysOspfExtVirtNbrTable=_EtsysOspfExtVirtNbrTable_Object((1,3,6,1,4,1,5624,1,2,65,1,2,5))
if mibBuilder.loadTexts:etsysOspfExtVirtNbrTable.setStatus(_A)
_EtsysOspfExtVirtNbrEntry_Object=MibTableRow
etsysOspfExtVirtNbrEntry=_EtsysOspfExtVirtNbrEntry_Object((1,3,6,1,4,1,5624,1,2,65,1,2,5,1))
if mibBuilder.loadTexts:etsysOspfExtVirtNbrEntry.setStatus(_A)
_EtsysOspfExtVirtNbrNumRequests_Type=Gauge32
_EtsysOspfExtVirtNbrNumRequests_Object=MibTableColumn
etsysOspfExtVirtNbrNumRequests=_EtsysOspfExtVirtNbrNumRequests_Object((1,3,6,1,4,1,5624,1,2,65,1,2,5,1,1),_EtsysOspfExtVirtNbrNumRequests_Type())
etsysOspfExtVirtNbrNumRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtVirtNbrNumRequests.setStatus(_A)
class _EtsysOspfExtVirtNbrDeadTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EtsysOspfExtVirtNbrDeadTime_Type.__name__=_E
_EtsysOspfExtVirtNbrDeadTime_Object=MibTableColumn
etsysOspfExtVirtNbrDeadTime=_EtsysOspfExtVirtNbrDeadTime_Object((1,3,6,1,4,1,5624,1,2,65,1,2,5,1,2),_EtsysOspfExtVirtNbrDeadTime_Type())
etsysOspfExtVirtNbrDeadTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtVirtNbrDeadTime.setStatus(_A)
_EtsysOspfExtLocalLsdbTable_Object=MibTable
etsysOspfExtLocalLsdbTable=_EtsysOspfExtLocalLsdbTable_Object((1,3,6,1,4,1,5624,1,2,65,1,2,6))
if mibBuilder.loadTexts:etsysOspfExtLocalLsdbTable.setStatus(_A)
_EtsysOspfExtLocalLsdbEntry_Object=MibTableRow
etsysOspfExtLocalLsdbEntry=_EtsysOspfExtLocalLsdbEntry_Object((1,3,6,1,4,1,5624,1,2,65,1,2,6,1))
if mibBuilder.loadTexts:etsysOspfExtLocalLsdbEntry.setStatus(_A)
_EtsysOspfExtLocalLsdbAreaId_Type=AreaID
_EtsysOspfExtLocalLsdbAreaId_Object=MibTableColumn
etsysOspfExtLocalLsdbAreaId=_EtsysOspfExtLocalLsdbAreaId_Object((1,3,6,1,4,1,5624,1,2,65,1,2,6,1,1),_EtsysOspfExtLocalLsdbAreaId_Type())
etsysOspfExtLocalLsdbAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOspfExtLocalLsdbAreaId.setStatus(_A)
_EtsysOspfExtConformance_ObjectIdentity=ObjectIdentity
etsysOspfExtConformance=_EtsysOspfExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,65,2))
_EtsysOspfExtGroups_ObjectIdentity=ObjectIdentity
etsysOspfExtGroups=_EtsysOspfExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,65,2,1))
_EtsysOspfExtCompliances_ObjectIdentity=ObjectIdentity
etsysOspfExtCompliances=_EtsysOspfExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,65,2,2))
ospfAreaEntry.registerAugmentions((_B,_S))
etsysOspfExtAreaEntry.setIndexNames(*ospfAreaEntry.getIndexNames())
ospfIfEntry.registerAugmentions((_B,_T))
etsysOspfExtIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions((_B,_U))
etsysOspfExtVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
ospfNbrEntry.registerAugmentions((_B,_V))
etsysOspfExtNbrEntry.setIndexNames(*ospfNbrEntry.getIndexNames())
ospfVirtNbrEntry.registerAugmentions((_B,_W))
etsysOspfExtVirtNbrEntry.setIndexNames(*ospfVirtNbrEntry.getIndexNames())
ospfLocalLsdbEntry.registerAugmentions((_B,_X))
etsysOspfExtLocalLsdbEntry.setIndexNames(*ospfLocalLsdbEntry.getIndexNames())
etsysOspfExtGlobalGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,65,2,1,1))
etsysOspfExtGlobalGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:etsysOspfExtGlobalGroup.setStatus(_A)
etsysOspfExtAreaGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,65,2,1,2))
etsysOspfExtAreaGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:etsysOspfExtAreaGroup.setStatus(_A)
etsysOspfExtIfGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,65,2,1,3))
etsysOspfExtIfGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:etsysOspfExtIfGroup.setStatus(_A)
etsysOspfExtVirtIfGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,65,2,1,4))
etsysOspfExtVirtIfGroup.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:etsysOspfExtVirtIfGroup.setStatus(_A)
etsysOspfExtNbrGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,65,2,1,5))
etsysOspfExtNbrGroup.setObjects(*((_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:etsysOspfExtNbrGroup.setStatus(_A)
etsysOspfExtVirtNbrGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,65,2,1,6))
etsysOspfExtVirtNbrGroup.setObjects(*((_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:etsysOspfExtVirtNbrGroup.setStatus(_A)
etsysOspfExtLocalLsdbGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,65,2,1,7))
etsysOspfExtLocalLsdbGroup.setObjects((_B,_Aa))
if mibBuilder.loadTexts:etsysOspfExtLocalLsdbGroup.setStatus(_A)
etsysOspfExtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,65,2,2,1))
etsysOspfExtCompliance.setObjects(*((_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah)))
if mibBuilder.loadTexts:etsysOspfExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EtsysOspfOperStatus':EtsysOspfOperStatus,'etsysOspfExtMIB':etsysOspfExtMIB,'etsysOspfExtObjects':etsysOspfExtObjects,'etsysOspfExtGlobals':etsysOspfExtGlobals,_Y:etsysOspfExtOperStatus,_Z:etsysOspfExtCalcMaxDelay,_a:etsysOspfExtCalcThrshUpdStart,_b:etsysOspfExtCalcThrshUpdRestart,_c:etsysOspfExtCalcThrshIncUpdates,_d:etsysOspfExtCalcThrshIncSpfUpd,_e:etsysOspfExtCalcPauseFreq,_f:etsysOspfExtRteMaxEqCostPaths,_g:etsysOspfExtCheckAge,_h:etsysOspfExtExtLsaRfshIntvl,_i:etsysOspfExtExternOpLsaCount,_j:etsysOspfExtExternOpLsaCksumSum,_k:etsysOspfExtNumUpdPending,_l:etsysOspfExtNumUpdMerged,_m:etsysOspfExtNumCksumsPending,_n:etsysOspfExtDoGraceHitless,_o:etsysOspfExtDoGraceUnplannedHitless,_p:etsysOspfExtHitlessGracePeriod,'etsysOspfExtTables':etsysOspfExtTables,'etsysOspfExtAreaTable':etsysOspfExtAreaTable,_S:etsysOspfExtAreaEntry,_q:etsysOspfExtAreaAdminStatus,_r:etsysOspfExtAreaOperStatus,_s:etsysOspfExtAreaTransitCapability,_t:etsysOspfExtAreaLsaRfshIntvl,_u:etsysOspfExtAreaRtrLsaCount,_v:etsysOspfExtAreaRtrLsaCksumSum,_w:etsysOspfExtAreaNetLsaCount,_x:etsysOspfExtAreaNetLsaCksumSum,_y:etsysOspfExtAreaSummLsaCount,_z:etsysOspfExtAreaSummLsaCksumSum,_A0:etsysOspfExtAreaSummAsLsaCount,_A1:etsysOspfExtAreaSummAsLsaCksumSum,_A2:etsysOspfExtAreaNssaLsaCount,_A3:etsysOspfExtAreaNssaLsaCksumSum,_A4:etsysOspfExtAreaOpLsaCount,_A5:etsysOspfExtAreaOpLsaCksumSum,'etsysOspfExtIfTable':etsysOspfExtIfTable,_T:etsysOspfExtIfEntry,_A6:etsysOspfExtIfOperStatus,_A7:etsysOspfExtIfNetMask,_A8:etsysOspfExtIfTransmitTimerDelay,_A9:etsysOspfExtIfIPMaxPacketSize,_AA:etsysOspfExtIfPassive,_AB:etsysOspfExtIfLsaRefreshIntvl,_AC:etsysOspfExtIfHelperModePolicy,_AD:etsysOspfExtIfMaxHitlessGracePeriod,_AE:etsysOspfExtIfAuthUserData,_AF:etsysOspfExtIfFastHelloMultiplier,_AG:etsysOspfExtIfAutoDeleteNbr,_AH:etsysOspfExtIfMtuIgnore,'etsysOspfExtVirtIfTable':etsysOspfExtVirtIfTable,_U:etsysOspfExtVirtIfEntry,_AI:etsysOspfExtVirtIfAdminStatus,_AJ:etsysOspfExtVirtIfOperStatus,_AK:etsysOspfExtVirtIfTransmitTimerDelay,_AL:etsysOspfExtVirtIfIPMaxPacketSize,_AM:etsysOspfExtVirtIfPassive,_AN:etsysOspfExtVirtIfLsaRefreshIntvl,_AO:etsysOspfExtVirtIfHelperModePolicy,_AP:etsysOspfExtVirtIfMaxHtlssGracePeriod,_AQ:etsysOspfExtVirtIfFastHelloMultiplier,_AR:etsysOspfExtVirtIfMtuIgnore,'etsysOspfExtNbrTable':etsysOspfExtNbrTable,_V:etsysOspfExtNbrEntry,_AS:etsysOspfExtNbrAdminStatus,_AT:etsysOspfExtNbrOperStatus,_AU:etsysOspfExtNbrNumRequests,_AV:etsysOspfExtNbrIfIpAddr,_AW:etsysOspfExtNbrDeadTime,_AX:etsysOspfExtNbrAreaId,'etsysOspfExtVirtNbrTable':etsysOspfExtVirtNbrTable,_W:etsysOspfExtVirtNbrEntry,_AY:etsysOspfExtVirtNbrNumRequests,_AZ:etsysOspfExtVirtNbrDeadTime,'etsysOspfExtLocalLsdbTable':etsysOspfExtLocalLsdbTable,_X:etsysOspfExtLocalLsdbEntry,_Aa:etsysOspfExtLocalLsdbAreaId,'etsysOspfExtConformance':etsysOspfExtConformance,'etsysOspfExtGroups':etsysOspfExtGroups,_Ab:etsysOspfExtGlobalGroup,_Ac:etsysOspfExtAreaGroup,_Ad:etsysOspfExtIfGroup,_Ae:etsysOspfExtVirtIfGroup,_Af:etsysOspfExtNbrGroup,_Ag:etsysOspfExtVirtNbrGroup,_Ah:etsysOspfExtLocalLsdbGroup,'etsysOspfExtCompliances':etsysOspfExtCompliances,'etsysOspfExtCompliance':etsysOspfExtCompliance})