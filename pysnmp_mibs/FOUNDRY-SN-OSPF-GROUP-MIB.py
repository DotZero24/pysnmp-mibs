_z='unUsed'
_y='snOspfRoutingInfoIndex'
_x='snOspfVirtIfStatusEntryIndex'
_w='snOspfIfStatusEntryIndex'
_v='snOspfAreaStatusEntryIndex'
_u='snOspfExtLsdbEntryIndex'
_t='asExternalLink'
_s='snOspfLsdbEntryIndex'
_r='snOspfVirtNbrEntryIndex'
_q='loading'
_p='exchange'
_o='exchangeStart'
_n='twoWay'
_m='attempt'
_l='RouterID'
_k='snOspfNbrEntryIndex'
_j='snOspfRedisIndex'
_i='snOspfVirtIfNeighbor'
_h='snOspfVirtIfAreaID'
_g='snOspfIf2Port'
_f='snOspfIfPort'
_e='snOspfAreaRangeNet'
_d='snOspfAreaRangeAreaID'
_c='snOspfAreaId'
_b='pointToPoint'
_a='RtrStatus'
_Z='IpAddress'
_Y='down'
_X='AreaID'
_W='Gauge32'
_V='DesignatedRouterPriority'
_U='PositiveInteger'
_T='HelloRange'
_S='00000000'
_R='modify'
_Q='create'
_P='delete'
_O='valid'
_N='invalid'
_M='0000000000000000'
_L='UpToMaxAge'
_K='ipAddress'
_J='integer'
_I='enabled'
_H='disabled'
_G='OctetString'
_F='FOUNDRY-SN-OSPF-GROUP-MIB'
_E='deprecated'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
router,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','router')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_W,_D,_Z,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snOspf=ModuleIdentity((1,3,6,1,4,1,1991,1,2,4))
if mibBuilder.loadTexts:snOspf.setRevisions(('2009-09-30 00:00','2017-08-07 00:00'))
class AreaID(TextualConvention,IpAddress):status=_A
class RouterID(TextualConvention,IpAddress):status=_A
class Metric(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class BigMetric(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
class TruthVal(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
class RtrStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
class PositiveInteger(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class HelloRange(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class UpToMaxAge(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
class DesignatedRouterPriority(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class TOSType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SnOspfGen_ObjectIdentity=ObjectIdentity
snOspfGen=_SnOspfGen_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,1))
_SnOspfRouterId_Type=RouterID
_SnOspfRouterId_Object=MibScalar
snOspfRouterId=_SnOspfRouterId_Object((1,3,6,1,4,1,1991,1,2,4,1,1),_SnOspfRouterId_Type())
snOspfRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfRouterId.setStatus(_A)
_SnOspfAdminStat_Type=RtrStatus
_SnOspfAdminStat_Object=MibScalar
snOspfAdminStat=_SnOspfAdminStat_Object((1,3,6,1,4,1,1991,1,2,4,1,2),_SnOspfAdminStat_Type())
snOspfAdminStat.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfAdminStat.setStatus(_A)
_SnOspfASBdrRtrStatus_Type=TruthVal
_SnOspfASBdrRtrStatus_Object=MibScalar
snOspfASBdrRtrStatus=_SnOspfASBdrRtrStatus_Object((1,3,6,1,4,1,1991,1,2,4,1,3),_SnOspfASBdrRtrStatus_Type())
snOspfASBdrRtrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfASBdrRtrStatus.setStatus(_A)
_SnOspfRedisMode_Type=RtrStatus
_SnOspfRedisMode_Object=MibScalar
snOspfRedisMode=_SnOspfRedisMode_Object((1,3,6,1,4,1,1991,1,2,4,1,4),_SnOspfRedisMode_Type())
snOspfRedisMode.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfRedisMode.setStatus(_A)
class _SnOspfDefaultOspfMetricValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnOspfDefaultOspfMetricValue_Type.__name__=_D
_SnOspfDefaultOspfMetricValue_Object=MibScalar
snOspfDefaultOspfMetricValue=_SnOspfDefaultOspfMetricValue_Object((1,3,6,1,4,1,1991,1,2,4,1,5),_SnOspfDefaultOspfMetricValue_Type())
snOspfDefaultOspfMetricValue.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfDefaultOspfMetricValue.setStatus(_A)
_SnOspfExternLSACount_Type=Gauge32
_SnOspfExternLSACount_Object=MibScalar
snOspfExternLSACount=_SnOspfExternLSACount_Object((1,3,6,1,4,1,1991,1,2,4,1,6),_SnOspfExternLSACount_Type())
snOspfExternLSACount.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfExternLSACount.setStatus(_A)
_SnOspfExternLSACksumSum_Type=Integer32
_SnOspfExternLSACksumSum_Object=MibScalar
snOspfExternLSACksumSum=_SnOspfExternLSACksumSum_Object((1,3,6,1,4,1,1991,1,2,4,1,7),_SnOspfExternLSACksumSum_Type())
snOspfExternLSACksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfExternLSACksumSum.setStatus(_A)
_SnOspfOriginateNewLSAs_Type=Counter32
_SnOspfOriginateNewLSAs_Object=MibScalar
snOspfOriginateNewLSAs=_SnOspfOriginateNewLSAs_Object((1,3,6,1,4,1,1991,1,2,4,1,8),_SnOspfOriginateNewLSAs_Type())
snOspfOriginateNewLSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfOriginateNewLSAs.setStatus(_A)
_SnOspfRxNewLSAs_Type=Counter32
_SnOspfRxNewLSAs_Object=MibScalar
snOspfRxNewLSAs=_SnOspfRxNewLSAs_Object((1,3,6,1,4,1,1991,1,2,4,1,9),_SnOspfRxNewLSAs_Type())
snOspfRxNewLSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfRxNewLSAs.setStatus(_A)
class _SnOspfOspfRedisMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('type1',1),('type2',2)))
_SnOspfOspfRedisMetricType_Type.__name__=_D
_SnOspfOspfRedisMetricType_Object=MibScalar
snOspfOspfRedisMetricType=_SnOspfOspfRedisMetricType_Object((1,3,6,1,4,1,1991,1,2,4,1,10),_SnOspfOspfRedisMetricType_Type())
snOspfOspfRedisMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfOspfRedisMetricType.setStatus(_A)
_SnOspfExtLsdbLimit_Type=Integer32
_SnOspfExtLsdbLimit_Object=MibScalar
snOspfExtLsdbLimit=_SnOspfExtLsdbLimit_Object((1,3,6,1,4,1,1991,1,2,4,1,11),_SnOspfExtLsdbLimit_Type())
snOspfExtLsdbLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfExtLsdbLimit.setStatus(_A)
class _SnOspfExitOverflowInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_SnOspfExitOverflowInterval_Type.__name__=_D
_SnOspfExitOverflowInterval_Object=MibScalar
snOspfExitOverflowInterval=_SnOspfExitOverflowInterval_Object((1,3,6,1,4,1,1991,1,2,4,1,12),_SnOspfExitOverflowInterval_Type())
snOspfExitOverflowInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfExitOverflowInterval.setStatus(_A)
class _SnOspfRfc1583Compatibility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SnOspfRfc1583Compatibility_Type.__name__=_D
_SnOspfRfc1583Compatibility_Object=MibScalar
snOspfRfc1583Compatibility=_SnOspfRfc1583Compatibility_Object((1,3,6,1,4,1,1991,1,2,4,1,13),_SnOspfRfc1583Compatibility_Type())
snOspfRfc1583Compatibility.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfRfc1583Compatibility.setStatus(_A)
class _SnOspfRouterIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_SnOspfRouterIdFormat_Type.__name__=_D
_SnOspfRouterIdFormat_Object=MibScalar
snOspfRouterIdFormat=_SnOspfRouterIdFormat_Object((1,3,6,1,4,1,1991,1,2,4,1,14),_SnOspfRouterIdFormat_Type())
snOspfRouterIdFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfRouterIdFormat.setStatus(_A)
class _SnOspfDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnOspfDistance_Type.__name__=_D
_SnOspfDistance_Object=MibScalar
snOspfDistance=_SnOspfDistance_Object((1,3,6,1,4,1,1991,1,2,4,1,15),_SnOspfDistance_Type())
snOspfDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfDistance.setStatus('obsolete')
class _SnOspfDistanceIntra_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SnOspfDistanceIntra_Type.__name__=_D
_SnOspfDistanceIntra_Object=MibScalar
snOspfDistanceIntra=_SnOspfDistanceIntra_Object((1,3,6,1,4,1,1991,1,2,4,1,16),_SnOspfDistanceIntra_Type())
snOspfDistanceIntra.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfDistanceIntra.setStatus(_A)
class _SnOspfDistanceInter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SnOspfDistanceInter_Type.__name__=_D
_SnOspfDistanceInter_Object=MibScalar
snOspfDistanceInter=_SnOspfDistanceInter_Object((1,3,6,1,4,1,1991,1,2,4,1,17),_SnOspfDistanceInter_Type())
snOspfDistanceInter.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfDistanceInter.setStatus(_A)
class _SnOspfDistanceExternal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SnOspfDistanceExternal_Type.__name__=_D
_SnOspfDistanceExternal_Object=MibScalar
snOspfDistanceExternal=_SnOspfDistanceExternal_Object((1,3,6,1,4,1,1991,1,2,4,1,18),_SnOspfDistanceExternal_Type())
snOspfDistanceExternal.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfDistanceExternal.setStatus(_A)
_SnOspfArea_ObjectIdentity=ObjectIdentity
snOspfArea=_SnOspfArea_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,2))
_SnOspfAreaTable_Object=MibTable
snOspfAreaTable=_SnOspfAreaTable_Object((1,3,6,1,4,1,1991,1,2,4,2,1))
if mibBuilder.loadTexts:snOspfAreaTable.setStatus(_A)
_SnOspfAreaEntry_Object=MibTableRow
snOspfAreaEntry=_SnOspfAreaEntry_Object((1,3,6,1,4,1,1991,1,2,4,2,1,1))
snOspfAreaEntry.setIndexNames((0,_F,_c))
if mibBuilder.loadTexts:snOspfAreaEntry.setStatus(_A)
_SnOspfAreaId_Type=AreaID
_SnOspfAreaId_Object=MibTableColumn
snOspfAreaId=_SnOspfAreaId_Object((1,3,6,1,4,1,1991,1,2,4,2,1,1,1),_SnOspfAreaId_Type())
snOspfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaId.setStatus(_A)
class _SnOspfImportASExtern_Type(Integer32):defaultValue=1
_SnOspfImportASExtern_Type.__name__=_D
_SnOspfImportASExtern_Object=MibTableColumn
snOspfImportASExtern=_SnOspfImportASExtern_Object((1,3,6,1,4,1,1991,1,2,4,2,1,1,2),_SnOspfImportASExtern_Type())
snOspfImportASExtern.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfImportASExtern.setStatus(_A)
_SnOspfStubMetric_Type=BigMetric
_SnOspfStubMetric_Object=MibTableColumn
snOspfStubMetric=_SnOspfStubMetric_Object((1,3,6,1,4,1,1991,1,2,4,2,1,1,3),_SnOspfStubMetric_Type())
snOspfStubMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfStubMetric.setStatus(_A)
class _SnOspfAreaRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_SnOspfAreaRowStatus_Type.__name__=_D
_SnOspfAreaRowStatus_Object=MibTableColumn
snOspfAreaRowStatus=_SnOspfAreaRowStatus_Object((1,3,6,1,4,1,1991,1,2,4,2,1,1,4),_SnOspfAreaRowStatus_Type())
snOspfAreaRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfAreaRowStatus.setStatus(_A)
class _SnOspfAreaIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_SnOspfAreaIdFormat_Type.__name__=_D
_SnOspfAreaIdFormat_Object=MibTableColumn
snOspfAreaIdFormat=_SnOspfAreaIdFormat_Object((1,3,6,1,4,1,1991,1,2,4,2,1,1,5),_SnOspfAreaIdFormat_Type())
snOspfAreaIdFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfAreaIdFormat.setStatus(_A)
_SnOspfAddrRange_ObjectIdentity=ObjectIdentity
snOspfAddrRange=_SnOspfAddrRange_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,3))
_SnOspfAreaRangeTable_Object=MibTable
snOspfAreaRangeTable=_SnOspfAreaRangeTable_Object((1,3,6,1,4,1,1991,1,2,4,3,1))
if mibBuilder.loadTexts:snOspfAreaRangeTable.setStatus(_A)
_SnOspfAreaRangeEntry_Object=MibTableRow
snOspfAreaRangeEntry=_SnOspfAreaRangeEntry_Object((1,3,6,1,4,1,1991,1,2,4,3,1,1))
snOspfAreaRangeEntry.setIndexNames((0,_F,_d),(0,_F,_e))
if mibBuilder.loadTexts:snOspfAreaRangeEntry.setStatus(_A)
_SnOspfAreaRangeAreaID_Type=AreaID
_SnOspfAreaRangeAreaID_Object=MibTableColumn
snOspfAreaRangeAreaID=_SnOspfAreaRangeAreaID_Object((1,3,6,1,4,1,1991,1,2,4,3,1,1,1),_SnOspfAreaRangeAreaID_Type())
snOspfAreaRangeAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaRangeAreaID.setStatus(_A)
_SnOspfAreaRangeNet_Type=IpAddress
_SnOspfAreaRangeNet_Object=MibTableColumn
snOspfAreaRangeNet=_SnOspfAreaRangeNet_Object((1,3,6,1,4,1,1991,1,2,4,3,1,1,2),_SnOspfAreaRangeNet_Type())
snOspfAreaRangeNet.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaRangeNet.setStatus(_A)
_SnOspfAreaRangeMask_Type=IpAddress
_SnOspfAreaRangeMask_Object=MibTableColumn
snOspfAreaRangeMask=_SnOspfAreaRangeMask_Object((1,3,6,1,4,1,1991,1,2,4,3,1,1,3),_SnOspfAreaRangeMask_Type())
snOspfAreaRangeMask.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfAreaRangeMask.setStatus(_A)
class _SnOspfAreaRangeRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_SnOspfAreaRangeRowStatus_Type.__name__=_D
_SnOspfAreaRangeRowStatus_Object=MibTableColumn
snOspfAreaRangeRowStatus=_SnOspfAreaRangeRowStatus_Object((1,3,6,1,4,1,1991,1,2,4,3,1,1,4),_SnOspfAreaRangeRowStatus_Type())
snOspfAreaRangeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfAreaRangeRowStatus.setStatus(_A)
class _SnOspfAreaRangeAreaIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_SnOspfAreaRangeAreaIdFormat_Type.__name__=_D
_SnOspfAreaRangeAreaIdFormat_Object=MibTableColumn
snOspfAreaRangeAreaIdFormat=_SnOspfAreaRangeAreaIdFormat_Object((1,3,6,1,4,1,1991,1,2,4,3,1,1,5),_SnOspfAreaRangeAreaIdFormat_Type())
snOspfAreaRangeAreaIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaRangeAreaIdFormat.setStatus(_A)
_SnOspfIntf_ObjectIdentity=ObjectIdentity
snOspfIntf=_SnOspfIntf_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,4))
_SnOspfIfTable_Object=MibTable
snOspfIfTable=_SnOspfIfTable_Object((1,3,6,1,4,1,1991,1,2,4,4,1))
if mibBuilder.loadTexts:snOspfIfTable.setStatus(_E)
_SnOspfIfEntry_Object=MibTableRow
snOspfIfEntry=_SnOspfIfEntry_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1))
snOspfIfEntry.setIndexNames((0,_F,_f))
if mibBuilder.loadTexts:snOspfIfEntry.setStatus(_E)
_SnOspfIfPort_Type=Integer32
_SnOspfIfPort_Object=MibTableColumn
snOspfIfPort=_SnOspfIfPort_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,1),_SnOspfIfPort_Type())
snOspfIfPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfPort.setStatus(_E)
class _SnOspfIfAreaId_Type(AreaID):defaultHexValue=_S
_SnOspfIfAreaId_Type.__name__=_X
_SnOspfIfAreaId_Object=MibTableColumn
snOspfIfAreaId=_SnOspfIfAreaId_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,2),_SnOspfIfAreaId_Type())
snOspfIfAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfAreaId.setStatus(_E)
class _SnOspfIfAdminStat_Type(RtrStatus):defaultValue=1
_SnOspfIfAdminStat_Type.__name__=_a
_SnOspfIfAdminStat_Object=MibTableColumn
snOspfIfAdminStat=_SnOspfIfAdminStat_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,3),_SnOspfIfAdminStat_Type())
snOspfIfAdminStat.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfAdminStat.setStatus(_E)
class _SnOspfIfRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_SnOspfIfRtrPriority_Type.__name__=_V
_SnOspfIfRtrPriority_Object=MibTableColumn
snOspfIfRtrPriority=_SnOspfIfRtrPriority_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,4),_SnOspfIfRtrPriority_Type())
snOspfIfRtrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfRtrPriority.setStatus(_E)
class _SnOspfIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_SnOspfIfTransitDelay_Type.__name__=_L
_SnOspfIfTransitDelay_Object=MibTableColumn
snOspfIfTransitDelay=_SnOspfIfTransitDelay_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,5),_SnOspfIfTransitDelay_Type())
snOspfIfTransitDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfTransitDelay.setStatus(_E)
class _SnOspfIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_SnOspfIfRetransInterval_Type.__name__=_L
_SnOspfIfRetransInterval_Object=MibTableColumn
snOspfIfRetransInterval=_SnOspfIfRetransInterval_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,6),_SnOspfIfRetransInterval_Type())
snOspfIfRetransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfRetransInterval.setStatus(_E)
class _SnOspfIfHelloInterval_Type(HelloRange):defaultValue=10
_SnOspfIfHelloInterval_Type.__name__=_T
_SnOspfIfHelloInterval_Object=MibTableColumn
snOspfIfHelloInterval=_SnOspfIfHelloInterval_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,7),_SnOspfIfHelloInterval_Type())
snOspfIfHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfHelloInterval.setStatus(_E)
class _SnOspfIfRtrDeadInterval_Type(PositiveInteger):defaultValue=40
_SnOspfIfRtrDeadInterval_Type.__name__=_U
_SnOspfIfRtrDeadInterval_Object=MibTableColumn
snOspfIfRtrDeadInterval=_SnOspfIfRtrDeadInterval_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,8),_SnOspfIfRtrDeadInterval_Type())
snOspfIfRtrDeadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfRtrDeadInterval.setStatus(_E)
class _SnOspfIfAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnOspfIfAuthType_Type.__name__=_D
_SnOspfIfAuthType_Object=MibTableColumn
snOspfIfAuthType=_SnOspfIfAuthType_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,9),_SnOspfIfAuthType_Type())
snOspfIfAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfAuthType.setStatus(_E)
class _SnOspfIfAuthKey_Type(OctetString):defaultHexValue=_M;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_SnOspfIfAuthKey_Type.__name__=_G
_SnOspfIfAuthKey_Object=MibTableColumn
snOspfIfAuthKey=_SnOspfIfAuthKey_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,10),_SnOspfIfAuthKey_Type())
snOspfIfAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfAuthKey.setStatus(_E)
class _SnOspfIfMetricValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnOspfIfMetricValue_Type.__name__=_D
_SnOspfIfMetricValue_Object=MibTableColumn
snOspfIfMetricValue=_SnOspfIfMetricValue_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,11),_SnOspfIfMetricValue_Type())
snOspfIfMetricValue.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfMetricValue.setStatus(_E)
class _SnOspfIfRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_SnOspfIfRowStatus_Type.__name__=_D
_SnOspfIfRowStatus_Object=MibTableColumn
snOspfIfRowStatus=_SnOspfIfRowStatus_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,12),_SnOspfIfRowStatus_Type())
snOspfIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfRowStatus.setStatus(_E)
class _SnOspfIfMd5AuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnOspfIfMd5AuthKeyId_Type.__name__=_D
_SnOspfIfMd5AuthKeyId_Object=MibTableColumn
snOspfIfMd5AuthKeyId=_SnOspfIfMd5AuthKeyId_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,13),_SnOspfIfMd5AuthKeyId_Type())
snOspfIfMd5AuthKeyId.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfMd5AuthKeyId.setStatus(_E)
class _SnOspfIfMd5AuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SnOspfIfMd5AuthKey_Type.__name__=_G
_SnOspfIfMd5AuthKey_Object=MibTableColumn
snOspfIfMd5AuthKey=_SnOspfIfMd5AuthKey_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,14),_SnOspfIfMd5AuthKey_Type())
snOspfIfMd5AuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfMd5AuthKey.setStatus(_E)
class _SnOspfIfMd5ActivationWaitTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14400))
_SnOspfIfMd5ActivationWaitTime_Type.__name__=_D
_SnOspfIfMd5ActivationWaitTime_Object=MibTableColumn
snOspfIfMd5ActivationWaitTime=_SnOspfIfMd5ActivationWaitTime_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,15),_SnOspfIfMd5ActivationWaitTime_Type())
snOspfIfMd5ActivationWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfMd5ActivationWaitTime.setStatus(_E)
class _SnOspfIfAreaIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_SnOspfIfAreaIdFormat_Type.__name__=_D
_SnOspfIfAreaIdFormat_Object=MibTableColumn
snOspfIfAreaIdFormat=_SnOspfIfAreaIdFormat_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,16),_SnOspfIfAreaIdFormat_Type())
snOspfIfAreaIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfAreaIdFormat.setStatus(_E)
class _SnOspfIfPassiveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SnOspfIfPassiveMode_Type.__name__=_D
_SnOspfIfPassiveMode_Object=MibTableColumn
snOspfIfPassiveMode=_SnOspfIfPassiveMode_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,17),_SnOspfIfPassiveMode_Type())
snOspfIfPassiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfPassiveMode.setStatus(_E)
class _SnOspfIfDatabaseFilterAllOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SnOspfIfDatabaseFilterAllOut_Type.__name__=_D
_SnOspfIfDatabaseFilterAllOut_Object=MibTableColumn
snOspfIfDatabaseFilterAllOut=_SnOspfIfDatabaseFilterAllOut_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,18),_SnOspfIfDatabaseFilterAllOut_Type())
snOspfIfDatabaseFilterAllOut.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfDatabaseFilterAllOut.setStatus(_E)
class _SnOspfIfMtuIgnore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SnOspfIfMtuIgnore_Type.__name__=_D
_SnOspfIfMtuIgnore_Object=MibTableColumn
snOspfIfMtuIgnore=_SnOspfIfMtuIgnore_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,19),_SnOspfIfMtuIgnore_Type())
snOspfIfMtuIgnore.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfMtuIgnore.setStatus(_E)
class _SnOspfIfNetworkP2mp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SnOspfIfNetworkP2mp_Type.__name__=_D
_SnOspfIfNetworkP2mp_Object=MibTableColumn
snOspfIfNetworkP2mp=_SnOspfIfNetworkP2mp_Object((1,3,6,1,4,1,1991,1,2,4,4,1,1,20),_SnOspfIfNetworkP2mp_Type())
snOspfIfNetworkP2mp.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIfNetworkP2mp.setStatus(_E)
_SnOspfIf2Table_Object=MibTable
snOspfIf2Table=_SnOspfIf2Table_Object((1,3,6,1,4,1,1991,1,2,4,4,2))
if mibBuilder.loadTexts:snOspfIf2Table.setStatus(_A)
_SnOspfIf2Entry_Object=MibTableRow
snOspfIf2Entry=_SnOspfIf2Entry_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1))
snOspfIf2Entry.setIndexNames((0,_F,_g))
if mibBuilder.loadTexts:snOspfIf2Entry.setStatus(_A)
_SnOspfIf2Port_Type=Integer32
_SnOspfIf2Port_Object=MibTableColumn
snOspfIf2Port=_SnOspfIf2Port_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,1),_SnOspfIf2Port_Type())
snOspfIf2Port.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIf2Port.setStatus(_A)
class _SnOspfIf2AreaId_Type(AreaID):defaultHexValue=_S
_SnOspfIf2AreaId_Type.__name__=_X
_SnOspfIf2AreaId_Object=MibTableColumn
snOspfIf2AreaId=_SnOspfIf2AreaId_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,2),_SnOspfIf2AreaId_Type())
snOspfIf2AreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2AreaId.setStatus(_A)
class _SnOspfIf2AdminStat_Type(RtrStatus):defaultValue=1
_SnOspfIf2AdminStat_Type.__name__=_a
_SnOspfIf2AdminStat_Object=MibTableColumn
snOspfIf2AdminStat=_SnOspfIf2AdminStat_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,3),_SnOspfIf2AdminStat_Type())
snOspfIf2AdminStat.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2AdminStat.setStatus(_A)
class _SnOspfIf2RtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_SnOspfIf2RtrPriority_Type.__name__=_V
_SnOspfIf2RtrPriority_Object=MibTableColumn
snOspfIf2RtrPriority=_SnOspfIf2RtrPriority_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,4),_SnOspfIf2RtrPriority_Type())
snOspfIf2RtrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2RtrPriority.setStatus(_A)
class _SnOspfIf2TransitDelay_Type(UpToMaxAge):defaultValue=1
_SnOspfIf2TransitDelay_Type.__name__=_L
_SnOspfIf2TransitDelay_Object=MibTableColumn
snOspfIf2TransitDelay=_SnOspfIf2TransitDelay_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,5),_SnOspfIf2TransitDelay_Type())
snOspfIf2TransitDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2TransitDelay.setStatus(_A)
class _SnOspfIf2RetransInterval_Type(UpToMaxAge):defaultValue=5
_SnOspfIf2RetransInterval_Type.__name__=_L
_SnOspfIf2RetransInterval_Object=MibTableColumn
snOspfIf2RetransInterval=_SnOspfIf2RetransInterval_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,6),_SnOspfIf2RetransInterval_Type())
snOspfIf2RetransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2RetransInterval.setStatus(_A)
class _SnOspfIf2HelloInterval_Type(HelloRange):defaultValue=10
_SnOspfIf2HelloInterval_Type.__name__=_T
_SnOspfIf2HelloInterval_Object=MibTableColumn
snOspfIf2HelloInterval=_SnOspfIf2HelloInterval_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,7),_SnOspfIf2HelloInterval_Type())
snOspfIf2HelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2HelloInterval.setStatus(_A)
class _SnOspfIf2RtrDeadInterval_Type(PositiveInteger):defaultValue=40
_SnOspfIf2RtrDeadInterval_Type.__name__=_U
_SnOspfIf2RtrDeadInterval_Object=MibTableColumn
snOspfIf2RtrDeadInterval=_SnOspfIf2RtrDeadInterval_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,8),_SnOspfIf2RtrDeadInterval_Type())
snOspfIf2RtrDeadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2RtrDeadInterval.setStatus(_A)
class _SnOspfIf2AuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnOspfIf2AuthType_Type.__name__=_D
_SnOspfIf2AuthType_Object=MibTableColumn
snOspfIf2AuthType=_SnOspfIf2AuthType_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,9),_SnOspfIf2AuthType_Type())
snOspfIf2AuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2AuthType.setStatus(_A)
class _SnOspfIf2AuthKey_Type(OctetString):defaultHexValue=_M;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_SnOspfIf2AuthKey_Type.__name__=_G
_SnOspfIf2AuthKey_Object=MibTableColumn
snOspfIf2AuthKey=_SnOspfIf2AuthKey_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,10),_SnOspfIf2AuthKey_Type())
snOspfIf2AuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2AuthKey.setStatus(_A)
class _SnOspfIf2MetricValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnOspfIf2MetricValue_Type.__name__=_D
_SnOspfIf2MetricValue_Object=MibTableColumn
snOspfIf2MetricValue=_SnOspfIf2MetricValue_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,11),_SnOspfIf2MetricValue_Type())
snOspfIf2MetricValue.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2MetricValue.setStatus(_A)
class _SnOspfIf2RowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_SnOspfIf2RowStatus_Type.__name__=_D
_SnOspfIf2RowStatus_Object=MibTableColumn
snOspfIf2RowStatus=_SnOspfIf2RowStatus_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,12),_SnOspfIf2RowStatus_Type())
snOspfIf2RowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2RowStatus.setStatus(_A)
class _SnOspfIf2Md5AuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnOspfIf2Md5AuthKeyId_Type.__name__=_D
_SnOspfIf2Md5AuthKeyId_Object=MibTableColumn
snOspfIf2Md5AuthKeyId=_SnOspfIf2Md5AuthKeyId_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,13),_SnOspfIf2Md5AuthKeyId_Type())
snOspfIf2Md5AuthKeyId.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2Md5AuthKeyId.setStatus(_A)
class _SnOspfIf2Md5AuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SnOspfIf2Md5AuthKey_Type.__name__=_G
_SnOspfIf2Md5AuthKey_Object=MibTableColumn
snOspfIf2Md5AuthKey=_SnOspfIf2Md5AuthKey_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,14),_SnOspfIf2Md5AuthKey_Type())
snOspfIf2Md5AuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2Md5AuthKey.setStatus(_A)
class _SnOspfIf2Md5ActivationWaitTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14400))
_SnOspfIf2Md5ActivationWaitTime_Type.__name__=_D
_SnOspfIf2Md5ActivationWaitTime_Object=MibTableColumn
snOspfIf2Md5ActivationWaitTime=_SnOspfIf2Md5ActivationWaitTime_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,15),_SnOspfIf2Md5ActivationWaitTime_Type())
snOspfIf2Md5ActivationWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2Md5ActivationWaitTime.setStatus(_A)
class _SnOspfIf2AreaIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_SnOspfIf2AreaIdFormat_Type.__name__=_D
_SnOspfIf2AreaIdFormat_Object=MibTableColumn
snOspfIf2AreaIdFormat=_SnOspfIf2AreaIdFormat_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,16),_SnOspfIf2AreaIdFormat_Type())
snOspfIf2AreaIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIf2AreaIdFormat.setStatus(_A)
class _SnOspfIf2PassiveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SnOspfIf2PassiveMode_Type.__name__=_D
_SnOspfIf2PassiveMode_Object=MibTableColumn
snOspfIf2PassiveMode=_SnOspfIf2PassiveMode_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,17),_SnOspfIf2PassiveMode_Type())
snOspfIf2PassiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2PassiveMode.setStatus(_A)
class _SnOspfIf2DatabaseFilterAllOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SnOspfIf2DatabaseFilterAllOut_Type.__name__=_D
_SnOspfIf2DatabaseFilterAllOut_Object=MibTableColumn
snOspfIf2DatabaseFilterAllOut=_SnOspfIf2DatabaseFilterAllOut_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,18),_SnOspfIf2DatabaseFilterAllOut_Type())
snOspfIf2DatabaseFilterAllOut.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2DatabaseFilterAllOut.setStatus(_A)
class _SnOspfIf2MtuIgnore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SnOspfIf2MtuIgnore_Type.__name__=_D
_SnOspfIf2MtuIgnore_Object=MibTableColumn
snOspfIf2MtuIgnore=_SnOspfIf2MtuIgnore_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,19),_SnOspfIf2MtuIgnore_Type())
snOspfIf2MtuIgnore.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2MtuIgnore.setStatus(_A)
class _SnOspfIf2NetworkP2mp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SnOspfIf2NetworkP2mp_Type.__name__=_D
_SnOspfIf2NetworkP2mp_Object=MibTableColumn
snOspfIf2NetworkP2mp=_SnOspfIf2NetworkP2mp_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,20),_SnOspfIf2NetworkP2mp_Type())
snOspfIf2NetworkP2mp.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2NetworkP2mp.setStatus(_A)
class _SnOspfIf2NetworkP2pt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SnOspfIf2NetworkP2pt_Type.__name__=_D
_SnOspfIf2NetworkP2pt_Object=MibTableColumn
snOspfIf2NetworkP2pt=_SnOspfIf2NetworkP2pt_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,21),_SnOspfIf2NetworkP2pt_Type())
snOspfIf2NetworkP2pt.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2NetworkP2pt.setStatus(_A)
class _SnOspfIf2NetworkNonBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SnOspfIf2NetworkNonBroadcast_Type.__name__=_D
_SnOspfIf2NetworkNonBroadcast_Object=MibTableColumn
snOspfIf2NetworkNonBroadcast=_SnOspfIf2NetworkNonBroadcast_Object((1,3,6,1,4,1,1991,1,2,4,4,2,1,22),_SnOspfIf2NetworkNonBroadcast_Type())
snOspfIf2NetworkNonBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfIf2NetworkNonBroadcast.setStatus(_A)
_SnOspfVirtIf_ObjectIdentity=ObjectIdentity
snOspfVirtIf=_SnOspfVirtIf_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,5))
_SnOspfVirtIfTable_Object=MibTable
snOspfVirtIfTable=_SnOspfVirtIfTable_Object((1,3,6,1,4,1,1991,1,2,4,5,1))
if mibBuilder.loadTexts:snOspfVirtIfTable.setStatus(_A)
_SnOspfVirtIfEntry_Object=MibTableRow
snOspfVirtIfEntry=_SnOspfVirtIfEntry_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1))
snOspfVirtIfEntry.setIndexNames((0,_F,_h),(0,_F,_i))
if mibBuilder.loadTexts:snOspfVirtIfEntry.setStatus(_A)
_SnOspfVirtIfAreaID_Type=AreaID
_SnOspfVirtIfAreaID_Object=MibTableColumn
snOspfVirtIfAreaID=_SnOspfVirtIfAreaID_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1,1),_SnOspfVirtIfAreaID_Type())
snOspfVirtIfAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfAreaID.setStatus(_A)
_SnOspfVirtIfNeighbor_Type=RouterID
_SnOspfVirtIfNeighbor_Object=MibTableColumn
snOspfVirtIfNeighbor=_SnOspfVirtIfNeighbor_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1,2),_SnOspfVirtIfNeighbor_Type())
snOspfVirtIfNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfNeighbor.setStatus(_A)
class _SnOspfVirtIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_SnOspfVirtIfTransitDelay_Type.__name__=_L
_SnOspfVirtIfTransitDelay_Object=MibTableColumn
snOspfVirtIfTransitDelay=_SnOspfVirtIfTransitDelay_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1,3),_SnOspfVirtIfTransitDelay_Type())
snOspfVirtIfTransitDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfVirtIfTransitDelay.setStatus(_A)
class _SnOspfVirtIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_SnOspfVirtIfRetransInterval_Type.__name__=_L
_SnOspfVirtIfRetransInterval_Object=MibTableColumn
snOspfVirtIfRetransInterval=_SnOspfVirtIfRetransInterval_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1,4),_SnOspfVirtIfRetransInterval_Type())
snOspfVirtIfRetransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfVirtIfRetransInterval.setStatus(_A)
class _SnOspfVirtIfHelloInterval_Type(HelloRange):defaultValue=10
_SnOspfVirtIfHelloInterval_Type.__name__=_T
_SnOspfVirtIfHelloInterval_Object=MibTableColumn
snOspfVirtIfHelloInterval=_SnOspfVirtIfHelloInterval_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1,5),_SnOspfVirtIfHelloInterval_Type())
snOspfVirtIfHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfVirtIfHelloInterval.setStatus(_A)
class _SnOspfVirtIfRtrDeadInterval_Type(PositiveInteger):defaultValue=60
_SnOspfVirtIfRtrDeadInterval_Type.__name__=_U
_SnOspfVirtIfRtrDeadInterval_Object=MibTableColumn
snOspfVirtIfRtrDeadInterval=_SnOspfVirtIfRtrDeadInterval_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1,6),_SnOspfVirtIfRtrDeadInterval_Type())
snOspfVirtIfRtrDeadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfVirtIfRtrDeadInterval.setStatus(_A)
class _SnOspfVirtIfAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnOspfVirtIfAuthType_Type.__name__=_D
_SnOspfVirtIfAuthType_Object=MibTableColumn
snOspfVirtIfAuthType=_SnOspfVirtIfAuthType_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1,7),_SnOspfVirtIfAuthType_Type())
snOspfVirtIfAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfVirtIfAuthType.setStatus(_A)
class _SnOspfVirtIfAuthKey_Type(OctetString):defaultHexValue=_M;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_SnOspfVirtIfAuthKey_Type.__name__=_G
_SnOspfVirtIfAuthKey_Object=MibTableColumn
snOspfVirtIfAuthKey=_SnOspfVirtIfAuthKey_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1,8),_SnOspfVirtIfAuthKey_Type())
snOspfVirtIfAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfVirtIfAuthKey.setStatus(_A)
class _SnOspfVirtIfRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_SnOspfVirtIfRowStatus_Type.__name__=_D
_SnOspfVirtIfRowStatus_Object=MibTableColumn
snOspfVirtIfRowStatus=_SnOspfVirtIfRowStatus_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1,9),_SnOspfVirtIfRowStatus_Type())
snOspfVirtIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfVirtIfRowStatus.setStatus(_A)
class _SnOspfVirtIfMd5AuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnOspfVirtIfMd5AuthKeyId_Type.__name__=_D
_SnOspfVirtIfMd5AuthKeyId_Object=MibTableColumn
snOspfVirtIfMd5AuthKeyId=_SnOspfVirtIfMd5AuthKeyId_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1,10),_SnOspfVirtIfMd5AuthKeyId_Type())
snOspfVirtIfMd5AuthKeyId.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfVirtIfMd5AuthKeyId.setStatus(_A)
class _SnOspfVirtIfMd5AuthKey_Type(OctetString):defaultHexValue=_M;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SnOspfVirtIfMd5AuthKey_Type.__name__=_G
_SnOspfVirtIfMd5AuthKey_Object=MibTableColumn
snOspfVirtIfMd5AuthKey=_SnOspfVirtIfMd5AuthKey_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1,11),_SnOspfVirtIfMd5AuthKey_Type())
snOspfVirtIfMd5AuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfVirtIfMd5AuthKey.setStatus(_A)
class _SnOspfVirtIfMd5ActivationWaitTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14400))
_SnOspfVirtIfMd5ActivationWaitTime_Type.__name__=_D
_SnOspfVirtIfMd5ActivationWaitTime_Object=MibTableColumn
snOspfVirtIfMd5ActivationWaitTime=_SnOspfVirtIfMd5ActivationWaitTime_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1,12),_SnOspfVirtIfMd5ActivationWaitTime_Type())
snOspfVirtIfMd5ActivationWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfVirtIfMd5ActivationWaitTime.setStatus(_A)
class _SnOspfVirtIfAreaIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_SnOspfVirtIfAreaIdFormat_Type.__name__=_D
_SnOspfVirtIfAreaIdFormat_Object=MibTableColumn
snOspfVirtIfAreaIdFormat=_SnOspfVirtIfAreaIdFormat_Object((1,3,6,1,4,1,1991,1,2,4,5,1,1,13),_SnOspfVirtIfAreaIdFormat_Type())
snOspfVirtIfAreaIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfAreaIdFormat.setStatus(_A)
_SnOspfRedis_ObjectIdentity=ObjectIdentity
snOspfRedis=_SnOspfRedis_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,6))
_SnOspfRedisTable_Object=MibTable
snOspfRedisTable=_SnOspfRedisTable_Object((1,3,6,1,4,1,1991,1,2,4,6,1))
if mibBuilder.loadTexts:snOspfRedisTable.setStatus(_A)
_SnOspfRedisEntry_Object=MibTableRow
snOspfRedisEntry=_SnOspfRedisEntry_Object((1,3,6,1,4,1,1991,1,2,4,6,1,1))
snOspfRedisEntry.setIndexNames((0,_F,_j))
if mibBuilder.loadTexts:snOspfRedisEntry.setStatus(_A)
class _SnOspfRedisIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_SnOspfRedisIndex_Type.__name__=_D
_SnOspfRedisIndex_Object=MibTableColumn
snOspfRedisIndex=_SnOspfRedisIndex_Object((1,3,6,1,4,1,1991,1,2,4,6,1,1,1),_SnOspfRedisIndex_Type())
snOspfRedisIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfRedisIndex.setStatus(_A)
_SnOspfRedisIpAddress_Type=IpAddress
_SnOspfRedisIpAddress_Object=MibTableColumn
snOspfRedisIpAddress=_SnOspfRedisIpAddress_Object((1,3,6,1,4,1,1991,1,2,4,6,1,1,2),_SnOspfRedisIpAddress_Type())
snOspfRedisIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfRedisIpAddress.setStatus(_A)
_SnOspfRedisMask_Type=IpAddress
_SnOspfRedisMask_Object=MibTableColumn
snOspfRedisMask=_SnOspfRedisMask_Object((1,3,6,1,4,1,1991,1,2,4,6,1,1,3),_SnOspfRedisMask_Type())
snOspfRedisMask.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfRedisMask.setStatus(_A)
class _SnOspfRedisAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noImport',0),('import',1)))
_SnOspfRedisAction_Type.__name__=_D
_SnOspfRedisAction_Object=MibTableColumn
snOspfRedisAction=_SnOspfRedisAction_Object((1,3,6,1,4,1,1991,1,2,4,6,1,1,4),_SnOspfRedisAction_Type())
snOspfRedisAction.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfRedisAction.setStatus(_A)
class _SnOspfRedisProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('rip',1),('all',2),('static',3),('bgp',4),('connected',5),('isis',6)))
_SnOspfRedisProtocol_Type.__name__=_D
_SnOspfRedisProtocol_Object=MibTableColumn
snOspfRedisProtocol=_SnOspfRedisProtocol_Object((1,3,6,1,4,1,1991,1,2,4,6,1,1,5),_SnOspfRedisProtocol_Type())
snOspfRedisProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfRedisProtocol.setStatus(_A)
class _SnOspfRedisSetOspfMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SnOspfRedisSetOspfMetric_Type.__name__=_D
_SnOspfRedisSetOspfMetric_Object=MibTableColumn
snOspfRedisSetOspfMetric=_SnOspfRedisSetOspfMetric_Object((1,3,6,1,4,1,1991,1,2,4,6,1,1,6),_SnOspfRedisSetOspfMetric_Type())
snOspfRedisSetOspfMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfRedisSetOspfMetric.setStatus(_A)
_SnOspfRedisOspfMetricValue_Type=Metric
_SnOspfRedisOspfMetricValue_Object=MibTableColumn
snOspfRedisOspfMetricValue=_SnOspfRedisOspfMetricValue_Object((1,3,6,1,4,1,1991,1,2,4,6,1,1,7),_SnOspfRedisOspfMetricValue_Type())
snOspfRedisOspfMetricValue.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfRedisOspfMetricValue.setStatus(_A)
class _SnOspfRedisMatchRipMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_SnOspfRedisMatchRipMetric_Type.__name__=_D
_SnOspfRedisMatchRipMetric_Object=MibTableColumn
snOspfRedisMatchRipMetric=_SnOspfRedisMatchRipMetric_Object((1,3,6,1,4,1,1991,1,2,4,6,1,1,8),_SnOspfRedisMatchRipMetric_Type())
snOspfRedisMatchRipMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfRedisMatchRipMetric.setStatus(_A)
class _SnOspfRedisRipMetricValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_SnOspfRedisRipMetricValue_Type.__name__=_D
_SnOspfRedisRipMetricValue_Object=MibTableColumn
snOspfRedisRipMetricValue=_SnOspfRedisRipMetricValue_Object((1,3,6,1,4,1,1991,1,2,4,6,1,1,9),_SnOspfRedisRipMetricValue_Type())
snOspfRedisRipMetricValue.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfRedisRipMetricValue.setStatus(_A)
class _SnOspfRedisRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_SnOspfRedisRowStatus_Type.__name__=_D
_SnOspfRedisRowStatus_Object=MibTableColumn
snOspfRedisRowStatus=_SnOspfRedisRowStatus_Object((1,3,6,1,4,1,1991,1,2,4,6,1,1,10),_SnOspfRedisRowStatus_Type())
snOspfRedisRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfRedisRowStatus.setStatus(_A)
_SnOspfNbr_ObjectIdentity=ObjectIdentity
snOspfNbr=_SnOspfNbr_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,7))
_SnOspfNbrTable_Object=MibTable
snOspfNbrTable=_SnOspfNbrTable_Object((1,3,6,1,4,1,1991,1,2,4,7,1))
if mibBuilder.loadTexts:snOspfNbrTable.setStatus(_A)
_SnOspfNbrEntry_Object=MibTableRow
snOspfNbrEntry=_SnOspfNbrEntry_Object((1,3,6,1,4,1,1991,1,2,4,7,1,1))
snOspfNbrEntry.setIndexNames((0,_F,_k))
if mibBuilder.loadTexts:snOspfNbrEntry.setStatus(_A)
_SnOspfNbrEntryIndex_Type=Integer32
_SnOspfNbrEntryIndex_Object=MibTableColumn
snOspfNbrEntryIndex=_SnOspfNbrEntryIndex_Object((1,3,6,1,4,1,1991,1,2,4,7,1,1,1),_SnOspfNbrEntryIndex_Type())
snOspfNbrEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfNbrEntryIndex.setStatus(_A)
_SnOspfNbrPort_Type=Integer32
_SnOspfNbrPort_Object=MibTableColumn
snOspfNbrPort=_SnOspfNbrPort_Object((1,3,6,1,4,1,1991,1,2,4,7,1,1,2),_SnOspfNbrPort_Type())
snOspfNbrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfNbrPort.setStatus(_A)
_SnOspfNbrIpAddr_Type=IpAddress
_SnOspfNbrIpAddr_Object=MibTableColumn
snOspfNbrIpAddr=_SnOspfNbrIpAddr_Object((1,3,6,1,4,1,1991,1,2,4,7,1,1,3),_SnOspfNbrIpAddr_Type())
snOspfNbrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfNbrIpAddr.setStatus(_A)
_SnOspfNbrIndex_Type=Integer32
_SnOspfNbrIndex_Object=MibTableColumn
snOspfNbrIndex=_SnOspfNbrIndex_Object((1,3,6,1,4,1,1991,1,2,4,7,1,1,4),_SnOspfNbrIndex_Type())
snOspfNbrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfNbrIndex.setStatus(_A)
class _SnOspfNbrRtrId_Type(RouterID):defaultHexValue=_S
_SnOspfNbrRtrId_Type.__name__=_l
_SnOspfNbrRtrId_Object=MibTableColumn
snOspfNbrRtrId=_SnOspfNbrRtrId_Object((1,3,6,1,4,1,1991,1,2,4,7,1,1,5),_SnOspfNbrRtrId_Type())
snOspfNbrRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfNbrRtrId.setStatus(_A)
class _SnOspfNbrOptions_Type(Integer32):defaultValue=0
_SnOspfNbrOptions_Type.__name__=_D
_SnOspfNbrOptions_Object=MibTableColumn
snOspfNbrOptions=_SnOspfNbrOptions_Object((1,3,6,1,4,1,1991,1,2,4,7,1,1,6),_SnOspfNbrOptions_Type())
snOspfNbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfNbrOptions.setStatus(_A)
class _SnOspfNbrPriority_Type(DesignatedRouterPriority):defaultValue=1
_SnOspfNbrPriority_Type.__name__=_V
_SnOspfNbrPriority_Object=MibTableColumn
snOspfNbrPriority=_SnOspfNbrPriority_Object((1,3,6,1,4,1,1991,1,2,4,7,1,1,7),_SnOspfNbrPriority_Type())
snOspfNbrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfNbrPriority.setStatus(_A)
class _SnOspfNbrState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_Y,1),(_m,2),('init',3),(_n,4),(_o,5),(_p,6),(_q,7),('full',8)))
_SnOspfNbrState_Type.__name__=_D
_SnOspfNbrState_Object=MibTableColumn
snOspfNbrState=_SnOspfNbrState_Object((1,3,6,1,4,1,1991,1,2,4,7,1,1,8),_SnOspfNbrState_Type())
snOspfNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfNbrState.setStatus(_A)
_SnOspfNbrEvents_Type=Counter32
_SnOspfNbrEvents_Object=MibTableColumn
snOspfNbrEvents=_SnOspfNbrEvents_Object((1,3,6,1,4,1,1991,1,2,4,7,1,1,9),_SnOspfNbrEvents_Type())
snOspfNbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfNbrEvents.setStatus(_A)
_SnOspfNbrLsRetransQLen_Type=Gauge32
_SnOspfNbrLsRetransQLen_Object=MibTableColumn
snOspfNbrLsRetransQLen=_SnOspfNbrLsRetransQLen_Object((1,3,6,1,4,1,1991,1,2,4,7,1,1,10),_SnOspfNbrLsRetransQLen_Type())
snOspfNbrLsRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfNbrLsRetransQLen.setStatus(_A)
_SnOspfVirtNbr_ObjectIdentity=ObjectIdentity
snOspfVirtNbr=_SnOspfVirtNbr_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,8))
_SnOspfVirtNbrTable_Object=MibTable
snOspfVirtNbrTable=_SnOspfVirtNbrTable_Object((1,3,6,1,4,1,1991,1,2,4,8,1))
if mibBuilder.loadTexts:snOspfVirtNbrTable.setStatus(_A)
_SnOspfVirtNbrEntry_Object=MibTableRow
snOspfVirtNbrEntry=_SnOspfVirtNbrEntry_Object((1,3,6,1,4,1,1991,1,2,4,8,1,1))
snOspfVirtNbrEntry.setIndexNames((0,_F,_r))
if mibBuilder.loadTexts:snOspfVirtNbrEntry.setStatus(_A)
_SnOspfVirtNbrEntryIndex_Type=Integer32
_SnOspfVirtNbrEntryIndex_Object=MibTableColumn
snOspfVirtNbrEntryIndex=_SnOspfVirtNbrEntryIndex_Object((1,3,6,1,4,1,1991,1,2,4,8,1,1,1),_SnOspfVirtNbrEntryIndex_Type())
snOspfVirtNbrEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtNbrEntryIndex.setStatus(_A)
_SnOspfVirtNbrArea_Type=AreaID
_SnOspfVirtNbrArea_Object=MibTableColumn
snOspfVirtNbrArea=_SnOspfVirtNbrArea_Object((1,3,6,1,4,1,1991,1,2,4,8,1,1,2),_SnOspfVirtNbrArea_Type())
snOspfVirtNbrArea.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtNbrArea.setStatus(_A)
_SnOspfVirtNbrRtrId_Type=RouterID
_SnOspfVirtNbrRtrId_Object=MibTableColumn
snOspfVirtNbrRtrId=_SnOspfVirtNbrRtrId_Object((1,3,6,1,4,1,1991,1,2,4,8,1,1,3),_SnOspfVirtNbrRtrId_Type())
snOspfVirtNbrRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtNbrRtrId.setStatus(_A)
_SnOspfVirtNbrIpAddr_Type=IpAddress
_SnOspfVirtNbrIpAddr_Object=MibTableColumn
snOspfVirtNbrIpAddr=_SnOspfVirtNbrIpAddr_Object((1,3,6,1,4,1,1991,1,2,4,8,1,1,4),_SnOspfVirtNbrIpAddr_Type())
snOspfVirtNbrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtNbrIpAddr.setStatus(_A)
_SnOspfVirtNbrOptions_Type=Integer32
_SnOspfVirtNbrOptions_Object=MibTableColumn
snOspfVirtNbrOptions=_SnOspfVirtNbrOptions_Object((1,3,6,1,4,1,1991,1,2,4,8,1,1,5),_SnOspfVirtNbrOptions_Type())
snOspfVirtNbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtNbrOptions.setStatus(_A)
class _SnOspfVirtNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_Y,1),(_m,2),('init',3),(_n,4),(_o,5),(_p,6),(_q,7),('full',8)))
_SnOspfVirtNbrState_Type.__name__=_D
_SnOspfVirtNbrState_Object=MibTableColumn
snOspfVirtNbrState=_SnOspfVirtNbrState_Object((1,3,6,1,4,1,1991,1,2,4,8,1,1,6),_SnOspfVirtNbrState_Type())
snOspfVirtNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtNbrState.setStatus(_A)
_SnOspfVirtNbrEvents_Type=Counter32
_SnOspfVirtNbrEvents_Object=MibTableColumn
snOspfVirtNbrEvents=_SnOspfVirtNbrEvents_Object((1,3,6,1,4,1,1991,1,2,4,8,1,1,7),_SnOspfVirtNbrEvents_Type())
snOspfVirtNbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtNbrEvents.setStatus(_A)
_SnOspfVirtNbrLSRetransQLen_Type=Gauge32
_SnOspfVirtNbrLSRetransQLen_Object=MibTableColumn
snOspfVirtNbrLSRetransQLen=_SnOspfVirtNbrLSRetransQLen_Object((1,3,6,1,4,1,1991,1,2,4,8,1,1,8),_SnOspfVirtNbrLSRetransQLen_Type())
snOspfVirtNbrLSRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtNbrLSRetransQLen.setStatus(_A)
class _SnOspfVirtNbrAreaIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_SnOspfVirtNbrAreaIdFormat_Type.__name__=_D
_SnOspfVirtNbrAreaIdFormat_Object=MibTableColumn
snOspfVirtNbrAreaIdFormat=_SnOspfVirtNbrAreaIdFormat_Object((1,3,6,1,4,1,1991,1,2,4,8,1,1,9),_SnOspfVirtNbrAreaIdFormat_Type())
snOspfVirtNbrAreaIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtNbrAreaIdFormat.setStatus(_A)
_SnOspfLsdb_ObjectIdentity=ObjectIdentity
snOspfLsdb=_SnOspfLsdb_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,9))
_SnOspfLsdbTable_Object=MibTable
snOspfLsdbTable=_SnOspfLsdbTable_Object((1,3,6,1,4,1,1991,1,2,4,9,1))
if mibBuilder.loadTexts:snOspfLsdbTable.setStatus(_A)
_SnOspfLsdbEntry_Object=MibTableRow
snOspfLsdbEntry=_SnOspfLsdbEntry_Object((1,3,6,1,4,1,1991,1,2,4,9,1,1))
snOspfLsdbEntry.setIndexNames((0,_F,_s))
if mibBuilder.loadTexts:snOspfLsdbEntry.setStatus(_A)
_SnOspfLsdbEntryIndex_Type=Integer32
_SnOspfLsdbEntryIndex_Object=MibTableColumn
snOspfLsdbEntryIndex=_SnOspfLsdbEntryIndex_Object((1,3,6,1,4,1,1991,1,2,4,9,1,1,1),_SnOspfLsdbEntryIndex_Type())
snOspfLsdbEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfLsdbEntryIndex.setStatus(_A)
_SnOspfLsdbAreaId_Type=AreaID
_SnOspfLsdbAreaId_Object=MibTableColumn
snOspfLsdbAreaId=_SnOspfLsdbAreaId_Object((1,3,6,1,4,1,1991,1,2,4,9,1,1,2),_SnOspfLsdbAreaId_Type())
snOspfLsdbAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfLsdbAreaId.setStatus(_A)
class _SnOspfLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,9,10,11)));namedValues=NamedValues(*(('routerLink',1),('networkLink',2),('summaryLink',3),('asSummaryLink',4),(_t,5),('multicastLink',6),('nssaExternalLink',7),('opaqueLink',9),('opaqueAreaLink',10),('opaqueAsLink',11)))
_SnOspfLsdbType_Type.__name__=_D
_SnOspfLsdbType_Object=MibTableColumn
snOspfLsdbType=_SnOspfLsdbType_Object((1,3,6,1,4,1,1991,1,2,4,9,1,1,3),_SnOspfLsdbType_Type())
snOspfLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfLsdbType.setStatus(_A)
_SnOspfLsdbLsId_Type=IpAddress
_SnOspfLsdbLsId_Object=MibTableColumn
snOspfLsdbLsId=_SnOspfLsdbLsId_Object((1,3,6,1,4,1,1991,1,2,4,9,1,1,4),_SnOspfLsdbLsId_Type())
snOspfLsdbLsId.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfLsdbLsId.setStatus(_A)
_SnOspfLsdbRouterId_Type=RouterID
_SnOspfLsdbRouterId_Object=MibTableColumn
snOspfLsdbRouterId=_SnOspfLsdbRouterId_Object((1,3,6,1,4,1,1991,1,2,4,9,1,1,5),_SnOspfLsdbRouterId_Type())
snOspfLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfLsdbRouterId.setStatus(_A)
_SnOspfLsdbSequence_Type=Integer32
_SnOspfLsdbSequence_Object=MibTableColumn
snOspfLsdbSequence=_SnOspfLsdbSequence_Object((1,3,6,1,4,1,1991,1,2,4,9,1,1,6),_SnOspfLsdbSequence_Type())
snOspfLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfLsdbSequence.setStatus(_A)
_SnOspfLsdbAge_Type=Integer32
_SnOspfLsdbAge_Object=MibTableColumn
snOspfLsdbAge=_SnOspfLsdbAge_Object((1,3,6,1,4,1,1991,1,2,4,9,1,1,7),_SnOspfLsdbAge_Type())
snOspfLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfLsdbAge.setStatus(_A)
_SnOspfLsdbChecksum_Type=Integer32
_SnOspfLsdbChecksum_Object=MibTableColumn
snOspfLsdbChecksum=_SnOspfLsdbChecksum_Object((1,3,6,1,4,1,1991,1,2,4,9,1,1,8),_SnOspfLsdbChecksum_Type())
snOspfLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfLsdbChecksum.setStatus(_A)
class _SnOspfLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_SnOspfLsdbAdvertisement_Type.__name__=_G
_SnOspfLsdbAdvertisement_Object=MibTableColumn
snOspfLsdbAdvertisement=_SnOspfLsdbAdvertisement_Object((1,3,6,1,4,1,1991,1,2,4,9,1,1,9),_SnOspfLsdbAdvertisement_Type())
snOspfLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfLsdbAdvertisement.setStatus(_A)
class _SnOspfLsdbAreaIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_SnOspfLsdbAreaIdFormat_Type.__name__=_D
_SnOspfLsdbAreaIdFormat_Object=MibTableColumn
snOspfLsdbAreaIdFormat=_SnOspfLsdbAreaIdFormat_Object((1,3,6,1,4,1,1991,1,2,4,9,1,1,10),_SnOspfLsdbAreaIdFormat_Type())
snOspfLsdbAreaIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfLsdbAreaIdFormat.setStatus(_A)
_SnOspfExtLsdb_ObjectIdentity=ObjectIdentity
snOspfExtLsdb=_SnOspfExtLsdb_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,10))
_SnOspfExtLsdbTable_Object=MibTable
snOspfExtLsdbTable=_SnOspfExtLsdbTable_Object((1,3,6,1,4,1,1991,1,2,4,10,1))
if mibBuilder.loadTexts:snOspfExtLsdbTable.setStatus(_A)
_SnOspfExtLsdbEntry_Object=MibTableRow
snOspfExtLsdbEntry=_SnOspfExtLsdbEntry_Object((1,3,6,1,4,1,1991,1,2,4,10,1,1))
snOspfExtLsdbEntry.setIndexNames((0,_F,_u))
if mibBuilder.loadTexts:snOspfExtLsdbEntry.setStatus(_A)
_SnOspfExtLsdbEntryIndex_Type=Integer32
_SnOspfExtLsdbEntryIndex_Object=MibTableColumn
snOspfExtLsdbEntryIndex=_SnOspfExtLsdbEntryIndex_Object((1,3,6,1,4,1,1991,1,2,4,10,1,1,1),_SnOspfExtLsdbEntryIndex_Type())
snOspfExtLsdbEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfExtLsdbEntryIndex.setStatus(_A)
class _SnOspfExtLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues((_t,5))
_SnOspfExtLsdbType_Type.__name__=_D
_SnOspfExtLsdbType_Object=MibTableColumn
snOspfExtLsdbType=_SnOspfExtLsdbType_Object((1,3,6,1,4,1,1991,1,2,4,10,1,1,2),_SnOspfExtLsdbType_Type())
snOspfExtLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfExtLsdbType.setStatus(_A)
_SnOspfExtLsdbLsId_Type=IpAddress
_SnOspfExtLsdbLsId_Object=MibTableColumn
snOspfExtLsdbLsId=_SnOspfExtLsdbLsId_Object((1,3,6,1,4,1,1991,1,2,4,10,1,1,3),_SnOspfExtLsdbLsId_Type())
snOspfExtLsdbLsId.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfExtLsdbLsId.setStatus(_A)
_SnOspfExtLsdbRouterId_Type=RouterID
_SnOspfExtLsdbRouterId_Object=MibTableColumn
snOspfExtLsdbRouterId=_SnOspfExtLsdbRouterId_Object((1,3,6,1,4,1,1991,1,2,4,10,1,1,4),_SnOspfExtLsdbRouterId_Type())
snOspfExtLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfExtLsdbRouterId.setStatus(_A)
_SnOspfExtLsdbSequence_Type=Integer32
_SnOspfExtLsdbSequence_Object=MibTableColumn
snOspfExtLsdbSequence=_SnOspfExtLsdbSequence_Object((1,3,6,1,4,1,1991,1,2,4,10,1,1,5),_SnOspfExtLsdbSequence_Type())
snOspfExtLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfExtLsdbSequence.setStatus(_A)
_SnOspfExtLsdbAge_Type=Integer32
_SnOspfExtLsdbAge_Object=MibTableColumn
snOspfExtLsdbAge=_SnOspfExtLsdbAge_Object((1,3,6,1,4,1,1991,1,2,4,10,1,1,6),_SnOspfExtLsdbAge_Type())
snOspfExtLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfExtLsdbAge.setStatus(_A)
_SnOspfExtLsdbChecksum_Type=Integer32
_SnOspfExtLsdbChecksum_Object=MibTableColumn
snOspfExtLsdbChecksum=_SnOspfExtLsdbChecksum_Object((1,3,6,1,4,1,1991,1,2,4,10,1,1,7),_SnOspfExtLsdbChecksum_Type())
snOspfExtLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfExtLsdbChecksum.setStatus(_A)
class _SnOspfExtLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(36,36));fixedLength=36
_SnOspfExtLsdbAdvertisement_Type.__name__=_G
_SnOspfExtLsdbAdvertisement_Object=MibTableColumn
snOspfExtLsdbAdvertisement=_SnOspfExtLsdbAdvertisement_Object((1,3,6,1,4,1,1991,1,2,4,10,1,1,8),_SnOspfExtLsdbAdvertisement_Type())
snOspfExtLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfExtLsdbAdvertisement.setStatus(_A)
_SnOspfAreaStatus_ObjectIdentity=ObjectIdentity
snOspfAreaStatus=_SnOspfAreaStatus_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,11))
_SnOspfAreaStatusTable_Object=MibTable
snOspfAreaStatusTable=_SnOspfAreaStatusTable_Object((1,3,6,1,4,1,1991,1,2,4,11,1))
if mibBuilder.loadTexts:snOspfAreaStatusTable.setStatus(_A)
_SnOspfAreaStatusEntry_Object=MibTableRow
snOspfAreaStatusEntry=_SnOspfAreaStatusEntry_Object((1,3,6,1,4,1,1991,1,2,4,11,1,1))
snOspfAreaStatusEntry.setIndexNames((0,_F,_v))
if mibBuilder.loadTexts:snOspfAreaStatusEntry.setStatus(_A)
_SnOspfAreaStatusEntryIndex_Type=Integer32
_SnOspfAreaStatusEntryIndex_Object=MibTableColumn
snOspfAreaStatusEntryIndex=_SnOspfAreaStatusEntryIndex_Object((1,3,6,1,4,1,1991,1,2,4,11,1,1,1),_SnOspfAreaStatusEntryIndex_Type())
snOspfAreaStatusEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaStatusEntryIndex.setStatus(_A)
_SnOspfAreaStatusAreaId_Type=AreaID
_SnOspfAreaStatusAreaId_Object=MibTableColumn
snOspfAreaStatusAreaId=_SnOspfAreaStatusAreaId_Object((1,3,6,1,4,1,1991,1,2,4,11,1,1,2),_SnOspfAreaStatusAreaId_Type())
snOspfAreaStatusAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaStatusAreaId.setStatus(_A)
class _SnOspfAreaStatusImportASExtern_Type(Integer32):defaultValue=1
_SnOspfAreaStatusImportASExtern_Type.__name__=_D
_SnOspfAreaStatusImportASExtern_Object=MibTableColumn
snOspfAreaStatusImportASExtern=_SnOspfAreaStatusImportASExtern_Object((1,3,6,1,4,1,1991,1,2,4,11,1,1,3),_SnOspfAreaStatusImportASExtern_Type())
snOspfAreaStatusImportASExtern.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaStatusImportASExtern.setStatus(_A)
_SnOspfAreaStatusStubMetric_Type=BigMetric
_SnOspfAreaStatusStubMetric_Object=MibTableColumn
snOspfAreaStatusStubMetric=_SnOspfAreaStatusStubMetric_Object((1,3,6,1,4,1,1991,1,2,4,11,1,1,4),_SnOspfAreaStatusStubMetric_Type())
snOspfAreaStatusStubMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaStatusStubMetric.setStatus(_A)
_SnOspfAreaStatusSpfRuns_Type=Counter32
_SnOspfAreaStatusSpfRuns_Object=MibTableColumn
snOspfAreaStatusSpfRuns=_SnOspfAreaStatusSpfRuns_Object((1,3,6,1,4,1,1991,1,2,4,11,1,1,5),_SnOspfAreaStatusSpfRuns_Type())
snOspfAreaStatusSpfRuns.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaStatusSpfRuns.setStatus(_A)
class _SnOspfAreaStatusAreaBdrRtrCount_Type(Gauge32):defaultValue=0
_SnOspfAreaStatusAreaBdrRtrCount_Type.__name__=_W
_SnOspfAreaStatusAreaBdrRtrCount_Object=MibTableColumn
snOspfAreaStatusAreaBdrRtrCount=_SnOspfAreaStatusAreaBdrRtrCount_Object((1,3,6,1,4,1,1991,1,2,4,11,1,1,6),_SnOspfAreaStatusAreaBdrRtrCount_Type())
snOspfAreaStatusAreaBdrRtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaStatusAreaBdrRtrCount.setStatus(_A)
class _SnOspfAreaStatusASBdrRtrCount_Type(Gauge32):defaultValue=0
_SnOspfAreaStatusASBdrRtrCount_Type.__name__=_W
_SnOspfAreaStatusASBdrRtrCount_Object=MibTableColumn
snOspfAreaStatusASBdrRtrCount=_SnOspfAreaStatusASBdrRtrCount_Object((1,3,6,1,4,1,1991,1,2,4,11,1,1,7),_SnOspfAreaStatusASBdrRtrCount_Type())
snOspfAreaStatusASBdrRtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaStatusASBdrRtrCount.setStatus(_A)
class _SnOspfAreaStatusLSACount_Type(Gauge32):defaultValue=0
_SnOspfAreaStatusLSACount_Type.__name__=_W
_SnOspfAreaStatusLSACount_Object=MibTableColumn
snOspfAreaStatusLSACount=_SnOspfAreaStatusLSACount_Object((1,3,6,1,4,1,1991,1,2,4,11,1,1,8),_SnOspfAreaStatusLSACount_Type())
snOspfAreaStatusLSACount.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaStatusLSACount.setStatus(_A)
class _SnOspfAreaStatusLSACksumSum_Type(Integer32):defaultValue=0
_SnOspfAreaStatusLSACksumSum_Type.__name__=_D
_SnOspfAreaStatusLSACksumSum_Object=MibTableColumn
snOspfAreaStatusLSACksumSum=_SnOspfAreaStatusLSACksumSum_Object((1,3,6,1,4,1,1991,1,2,4,11,1,1,9),_SnOspfAreaStatusLSACksumSum_Type())
snOspfAreaStatusLSACksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaStatusLSACksumSum.setStatus(_A)
class _SnOspfAreaStatusAreaIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_SnOspfAreaStatusAreaIdFormat_Type.__name__=_D
_SnOspfAreaStatusAreaIdFormat_Object=MibTableColumn
snOspfAreaStatusAreaIdFormat=_SnOspfAreaStatusAreaIdFormat_Object((1,3,6,1,4,1,1991,1,2,4,11,1,1,10),_SnOspfAreaStatusAreaIdFormat_Type())
snOspfAreaStatusAreaIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfAreaStatusAreaIdFormat.setStatus(_A)
_SnOspfIfStatus_ObjectIdentity=ObjectIdentity
snOspfIfStatus=_SnOspfIfStatus_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,12))
_SnOspfIfStatusTable_Object=MibTable
snOspfIfStatusTable=_SnOspfIfStatusTable_Object((1,3,6,1,4,1,1991,1,2,4,12,1))
if mibBuilder.loadTexts:snOspfIfStatusTable.setStatus(_A)
_SnOspfIfStatusEntry_Object=MibTableRow
snOspfIfStatusEntry=_SnOspfIfStatusEntry_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1))
snOspfIfStatusEntry.setIndexNames((0,_F,_w))
if mibBuilder.loadTexts:snOspfIfStatusEntry.setStatus(_A)
_SnOspfIfStatusEntryIndex_Type=Integer32
_SnOspfIfStatusEntryIndex_Object=MibTableColumn
snOspfIfStatusEntryIndex=_SnOspfIfStatusEntryIndex_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,1),_SnOspfIfStatusEntryIndex_Type())
snOspfIfStatusEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusEntryIndex.setStatus(_A)
_SnOspfIfStatusPort_Type=Integer32
_SnOspfIfStatusPort_Object=MibTableColumn
snOspfIfStatusPort=_SnOspfIfStatusPort_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,2),_SnOspfIfStatusPort_Type())
snOspfIfStatusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusPort.setStatus(_A)
_SnOspfIfStatusIpAddress_Type=IpAddress
_SnOspfIfStatusIpAddress_Object=MibTableColumn
snOspfIfStatusIpAddress=_SnOspfIfStatusIpAddress_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,3),_SnOspfIfStatusIpAddress_Type())
snOspfIfStatusIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusIpAddress.setStatus(_A)
class _SnOspfIfStatusAreaId_Type(AreaID):defaultHexValue=_S
_SnOspfIfStatusAreaId_Type.__name__=_X
_SnOspfIfStatusAreaId_Object=MibTableColumn
snOspfIfStatusAreaId=_SnOspfIfStatusAreaId_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,4),_SnOspfIfStatusAreaId_Type())
snOspfIfStatusAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusAreaId.setStatus(_A)
class _SnOspfIfStatusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('broadcast',1),('nbma',2),(_b,3)))
_SnOspfIfStatusType_Type.__name__=_D
_SnOspfIfStatusType_Object=MibTableColumn
snOspfIfStatusType=_SnOspfIfStatusType_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,5),_SnOspfIfStatusType_Type())
snOspfIfStatusType.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusType.setStatus(_A)
_SnOspfIfStatusAdminStat_Type=RtrStatus
_SnOspfIfStatusAdminStat_Object=MibTableColumn
snOspfIfStatusAdminStat=_SnOspfIfStatusAdminStat_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,6),_SnOspfIfStatusAdminStat_Type())
snOspfIfStatusAdminStat.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusAdminStat.setStatus(_A)
class _SnOspfIfStatusRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_SnOspfIfStatusRtrPriority_Type.__name__=_V
_SnOspfIfStatusRtrPriority_Object=MibTableColumn
snOspfIfStatusRtrPriority=_SnOspfIfStatusRtrPriority_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,7),_SnOspfIfStatusRtrPriority_Type())
snOspfIfStatusRtrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusRtrPriority.setStatus(_A)
class _SnOspfIfStatusTransitDelay_Type(UpToMaxAge):defaultValue=1
_SnOspfIfStatusTransitDelay_Type.__name__=_L
_SnOspfIfStatusTransitDelay_Object=MibTableColumn
snOspfIfStatusTransitDelay=_SnOspfIfStatusTransitDelay_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,8),_SnOspfIfStatusTransitDelay_Type())
snOspfIfStatusTransitDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusTransitDelay.setStatus(_A)
class _SnOspfIfStatusRetransInterval_Type(UpToMaxAge):defaultValue=5
_SnOspfIfStatusRetransInterval_Type.__name__=_L
_SnOspfIfStatusRetransInterval_Object=MibTableColumn
snOspfIfStatusRetransInterval=_SnOspfIfStatusRetransInterval_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,9),_SnOspfIfStatusRetransInterval_Type())
snOspfIfStatusRetransInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusRetransInterval.setStatus(_A)
class _SnOspfIfStatusHelloInterval_Type(HelloRange):defaultValue=10
_SnOspfIfStatusHelloInterval_Type.__name__=_T
_SnOspfIfStatusHelloInterval_Object=MibTableColumn
snOspfIfStatusHelloInterval=_SnOspfIfStatusHelloInterval_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,10),_SnOspfIfStatusHelloInterval_Type())
snOspfIfStatusHelloInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusHelloInterval.setStatus(_A)
class _SnOspfIfStatusRtrDeadInterval_Type(PositiveInteger):defaultValue=40
_SnOspfIfStatusRtrDeadInterval_Type.__name__=_U
_SnOspfIfStatusRtrDeadInterval_Object=MibTableColumn
snOspfIfStatusRtrDeadInterval=_SnOspfIfStatusRtrDeadInterval_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,11),_SnOspfIfStatusRtrDeadInterval_Type())
snOspfIfStatusRtrDeadInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusRtrDeadInterval.setStatus(_A)
class _SnOspfIfStatusState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Y,1),('loopback',2),('waiting',3),(_b,4),('designatedRouter',5),('backupDesignatedRouter',6),('otherDesignatedRouter',7)))
_SnOspfIfStatusState_Type.__name__=_D
_SnOspfIfStatusState_Object=MibTableColumn
snOspfIfStatusState=_SnOspfIfStatusState_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,12),_SnOspfIfStatusState_Type())
snOspfIfStatusState.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusState.setStatus(_A)
class _SnOspfIfStatusDesignatedRouter_Type(IpAddress):defaultHexValue=_S
_SnOspfIfStatusDesignatedRouter_Type.__name__=_Z
_SnOspfIfStatusDesignatedRouter_Object=MibTableColumn
snOspfIfStatusDesignatedRouter=_SnOspfIfStatusDesignatedRouter_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,13),_SnOspfIfStatusDesignatedRouter_Type())
snOspfIfStatusDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusDesignatedRouter.setStatus(_A)
class _SnOspfIfStatusBackupDesignatedRouter_Type(IpAddress):defaultHexValue=_S
_SnOspfIfStatusBackupDesignatedRouter_Type.__name__=_Z
_SnOspfIfStatusBackupDesignatedRouter_Object=MibTableColumn
snOspfIfStatusBackupDesignatedRouter=_SnOspfIfStatusBackupDesignatedRouter_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,14),_SnOspfIfStatusBackupDesignatedRouter_Type())
snOspfIfStatusBackupDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusBackupDesignatedRouter.setStatus(_A)
_SnOspfIfStatusEvents_Type=Counter32
_SnOspfIfStatusEvents_Object=MibTableColumn
snOspfIfStatusEvents=_SnOspfIfStatusEvents_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,15),_SnOspfIfStatusEvents_Type())
snOspfIfStatusEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusEvents.setStatus(_A)
class _SnOspfIfStatusAuthType_Type(Integer32):defaultValue=0
_SnOspfIfStatusAuthType_Type.__name__=_D
_SnOspfIfStatusAuthType_Object=MibTableColumn
snOspfIfStatusAuthType=_SnOspfIfStatusAuthType_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,16),_SnOspfIfStatusAuthType_Type())
snOspfIfStatusAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusAuthType.setStatus(_A)
class _SnOspfIfStatusAuthKey_Type(OctetString):defaultHexValue=_M;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_SnOspfIfStatusAuthKey_Type.__name__=_G
_SnOspfIfStatusAuthKey_Object=MibTableColumn
snOspfIfStatusAuthKey=_SnOspfIfStatusAuthKey_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,17),_SnOspfIfStatusAuthKey_Type())
snOspfIfStatusAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusAuthKey.setStatus(_A)
_SnOspfIfStatusMetricValue_Type=Metric
_SnOspfIfStatusMetricValue_Object=MibTableColumn
snOspfIfStatusMetricValue=_SnOspfIfStatusMetricValue_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,18),_SnOspfIfStatusMetricValue_Type())
snOspfIfStatusMetricValue.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusMetricValue.setStatus(_A)
class _SnOspfIfStatusMd5AuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnOspfIfStatusMd5AuthKeyId_Type.__name__=_D
_SnOspfIfStatusMd5AuthKeyId_Object=MibTableColumn
snOspfIfStatusMd5AuthKeyId=_SnOspfIfStatusMd5AuthKeyId_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,19),_SnOspfIfStatusMd5AuthKeyId_Type())
snOspfIfStatusMd5AuthKeyId.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusMd5AuthKeyId.setStatus(_A)
class _SnOspfIfStatusMd5AuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SnOspfIfStatusMd5AuthKey_Type.__name__=_G
_SnOspfIfStatusMd5AuthKey_Object=MibTableColumn
snOspfIfStatusMd5AuthKey=_SnOspfIfStatusMd5AuthKey_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,20),_SnOspfIfStatusMd5AuthKey_Type())
snOspfIfStatusMd5AuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusMd5AuthKey.setStatus(_A)
class _SnOspfIfStatusMd5ActivationWaitTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14400))
_SnOspfIfStatusMd5ActivationWaitTime_Type.__name__=_D
_SnOspfIfStatusMd5ActivationWaitTime_Object=MibTableColumn
snOspfIfStatusMd5ActivationWaitTime=_SnOspfIfStatusMd5ActivationWaitTime_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,21),_SnOspfIfStatusMd5ActivationWaitTime_Type())
snOspfIfStatusMd5ActivationWaitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusMd5ActivationWaitTime.setStatus(_A)
class _SnOspfIfStatusAreaIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_SnOspfIfStatusAreaIdFormat_Type.__name__=_D
_SnOspfIfStatusAreaIdFormat_Object=MibTableColumn
snOspfIfStatusAreaIdFormat=_SnOspfIfStatusAreaIdFormat_Object((1,3,6,1,4,1,1991,1,2,4,12,1,1,22),_SnOspfIfStatusAreaIdFormat_Type())
snOspfIfStatusAreaIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfIfStatusAreaIdFormat.setStatus(_A)
_SnOspfVirtIfStatus_ObjectIdentity=ObjectIdentity
snOspfVirtIfStatus=_SnOspfVirtIfStatus_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,13))
_SnOspfVirtIfStatusTable_Object=MibTable
snOspfVirtIfStatusTable=_SnOspfVirtIfStatusTable_Object((1,3,6,1,4,1,1991,1,2,4,13,1))
if mibBuilder.loadTexts:snOspfVirtIfStatusTable.setStatus(_A)
_SnOspfVirtIfStatusEntry_Object=MibTableRow
snOspfVirtIfStatusEntry=_SnOspfVirtIfStatusEntry_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1))
snOspfVirtIfStatusEntry.setIndexNames((0,_F,_x))
if mibBuilder.loadTexts:snOspfVirtIfStatusEntry.setStatus(_A)
_SnOspfVirtIfStatusEntryIndex_Type=Integer32
_SnOspfVirtIfStatusEntryIndex_Object=MibTableColumn
snOspfVirtIfStatusEntryIndex=_SnOspfVirtIfStatusEntryIndex_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,1),_SnOspfVirtIfStatusEntryIndex_Type())
snOspfVirtIfStatusEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusEntryIndex.setStatus(_A)
_SnOspfVirtIfStatusAreaID_Type=AreaID
_SnOspfVirtIfStatusAreaID_Object=MibTableColumn
snOspfVirtIfStatusAreaID=_SnOspfVirtIfStatusAreaID_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,2),_SnOspfVirtIfStatusAreaID_Type())
snOspfVirtIfStatusAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusAreaID.setStatus(_A)
_SnOspfVirtIfStatusNeighbor_Type=RouterID
_SnOspfVirtIfStatusNeighbor_Object=MibTableColumn
snOspfVirtIfStatusNeighbor=_SnOspfVirtIfStatusNeighbor_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,3),_SnOspfVirtIfStatusNeighbor_Type())
snOspfVirtIfStatusNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusNeighbor.setStatus(_A)
class _SnOspfVirtIfStatusTransitDelay_Type(UpToMaxAge):defaultValue=1
_SnOspfVirtIfStatusTransitDelay_Type.__name__=_L
_SnOspfVirtIfStatusTransitDelay_Object=MibTableColumn
snOspfVirtIfStatusTransitDelay=_SnOspfVirtIfStatusTransitDelay_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,4),_SnOspfVirtIfStatusTransitDelay_Type())
snOspfVirtIfStatusTransitDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusTransitDelay.setStatus(_A)
class _SnOspfVirtIfStatusRetransInterval_Type(UpToMaxAge):defaultValue=5
_SnOspfVirtIfStatusRetransInterval_Type.__name__=_L
_SnOspfVirtIfStatusRetransInterval_Object=MibTableColumn
snOspfVirtIfStatusRetransInterval=_SnOspfVirtIfStatusRetransInterval_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,5),_SnOspfVirtIfStatusRetransInterval_Type())
snOspfVirtIfStatusRetransInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusRetransInterval.setStatus(_A)
class _SnOspfVirtIfStatusHelloInterval_Type(HelloRange):defaultValue=10
_SnOspfVirtIfStatusHelloInterval_Type.__name__=_T
_SnOspfVirtIfStatusHelloInterval_Object=MibTableColumn
snOspfVirtIfStatusHelloInterval=_SnOspfVirtIfStatusHelloInterval_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,6),_SnOspfVirtIfStatusHelloInterval_Type())
snOspfVirtIfStatusHelloInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusHelloInterval.setStatus(_A)
class _SnOspfVirtIfStatusRtrDeadInterval_Type(PositiveInteger):defaultValue=60
_SnOspfVirtIfStatusRtrDeadInterval_Type.__name__=_U
_SnOspfVirtIfStatusRtrDeadInterval_Object=MibTableColumn
snOspfVirtIfStatusRtrDeadInterval=_SnOspfVirtIfStatusRtrDeadInterval_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,7),_SnOspfVirtIfStatusRtrDeadInterval_Type())
snOspfVirtIfStatusRtrDeadInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusRtrDeadInterval.setStatus(_A)
class _SnOspfVirtIfStatusState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_Y,1),(_b,4)))
_SnOspfVirtIfStatusState_Type.__name__=_D
_SnOspfVirtIfStatusState_Object=MibTableColumn
snOspfVirtIfStatusState=_SnOspfVirtIfStatusState_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,8),_SnOspfVirtIfStatusState_Type())
snOspfVirtIfStatusState.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusState.setStatus(_A)
_SnOspfVirtIfStatusEvents_Type=Counter32
_SnOspfVirtIfStatusEvents_Object=MibTableColumn
snOspfVirtIfStatusEvents=_SnOspfVirtIfStatusEvents_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,9),_SnOspfVirtIfStatusEvents_Type())
snOspfVirtIfStatusEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusEvents.setStatus(_A)
class _SnOspfVirtIfStatusAuthType_Type(Integer32):defaultValue=0
_SnOspfVirtIfStatusAuthType_Type.__name__=_D
_SnOspfVirtIfStatusAuthType_Object=MibTableColumn
snOspfVirtIfStatusAuthType=_SnOspfVirtIfStatusAuthType_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,10),_SnOspfVirtIfStatusAuthType_Type())
snOspfVirtIfStatusAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusAuthType.setStatus(_A)
class _SnOspfVirtIfStatusAuthKey_Type(OctetString):defaultHexValue=_M;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_SnOspfVirtIfStatusAuthKey_Type.__name__=_G
_SnOspfVirtIfStatusAuthKey_Object=MibTableColumn
snOspfVirtIfStatusAuthKey=_SnOspfVirtIfStatusAuthKey_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,11),_SnOspfVirtIfStatusAuthKey_Type())
snOspfVirtIfStatusAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusAuthKey.setStatus(_A)
class _SnOspfVirtIfStatusMd5AuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnOspfVirtIfStatusMd5AuthKeyId_Type.__name__=_D
_SnOspfVirtIfStatusMd5AuthKeyId_Object=MibTableColumn
snOspfVirtIfStatusMd5AuthKeyId=_SnOspfVirtIfStatusMd5AuthKeyId_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,12),_SnOspfVirtIfStatusMd5AuthKeyId_Type())
snOspfVirtIfStatusMd5AuthKeyId.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusMd5AuthKeyId.setStatus(_A)
class _SnOspfVirtIfStatusMd5AuthKey_Type(OctetString):defaultHexValue=_M;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SnOspfVirtIfStatusMd5AuthKey_Type.__name__=_G
_SnOspfVirtIfStatusMd5AuthKey_Object=MibTableColumn
snOspfVirtIfStatusMd5AuthKey=_SnOspfVirtIfStatusMd5AuthKey_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,13),_SnOspfVirtIfStatusMd5AuthKey_Type())
snOspfVirtIfStatusMd5AuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusMd5AuthKey.setStatus(_A)
class _SnOspfVirtIfStatusMd5ActivationWaitTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14400))
_SnOspfVirtIfStatusMd5ActivationWaitTime_Type.__name__=_D
_SnOspfVirtIfStatusMd5ActivationWaitTime_Object=MibTableColumn
snOspfVirtIfStatusMd5ActivationWaitTime=_SnOspfVirtIfStatusMd5ActivationWaitTime_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,14),_SnOspfVirtIfStatusMd5ActivationWaitTime_Type())
snOspfVirtIfStatusMd5ActivationWaitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusMd5ActivationWaitTime.setStatus(_A)
class _SnOspfVirtIfStatusAreaIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_SnOspfVirtIfStatusAreaIdFormat_Type.__name__=_D
_SnOspfVirtIfStatusAreaIdFormat_Object=MibTableColumn
snOspfVirtIfStatusAreaIdFormat=_SnOspfVirtIfStatusAreaIdFormat_Object((1,3,6,1,4,1,1991,1,2,4,13,1,1,15),_SnOspfVirtIfStatusAreaIdFormat_Type())
snOspfVirtIfStatusAreaIdFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfVirtIfStatusAreaIdFormat.setStatus(_A)
_SnOspfRoutingInfo_ObjectIdentity=ObjectIdentity
snOspfRoutingInfo=_SnOspfRoutingInfo_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,14))
_SnOspfRoutingInfoTable_Object=MibTable
snOspfRoutingInfoTable=_SnOspfRoutingInfoTable_Object((1,3,6,1,4,1,1991,1,2,4,14,1))
if mibBuilder.loadTexts:snOspfRoutingInfoTable.setStatus(_A)
_SnOspfRoutingInfoEntry_Object=MibTableRow
snOspfRoutingInfoEntry=_SnOspfRoutingInfoEntry_Object((1,3,6,1,4,1,1991,1,2,4,14,1,1))
snOspfRoutingInfoEntry.setIndexNames((0,_F,_y))
if mibBuilder.loadTexts:snOspfRoutingInfoEntry.setStatus(_A)
_SnOspfRoutingInfoIndex_Type=Integer32
_SnOspfRoutingInfoIndex_Object=MibTableColumn
snOspfRoutingInfoIndex=_SnOspfRoutingInfoIndex_Object((1,3,6,1,4,1,1991,1,2,4,14,1,1,1),_SnOspfRoutingInfoIndex_Type())
snOspfRoutingInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfRoutingInfoIndex.setStatus(_A)
_SnOspfRoutingInfoRouterID_Type=RouterID
_SnOspfRoutingInfoRouterID_Object=MibTableColumn
snOspfRoutingInfoRouterID=_SnOspfRoutingInfoRouterID_Object((1,3,6,1,4,1,1991,1,2,4,14,1,1,2),_SnOspfRoutingInfoRouterID_Type())
snOspfRoutingInfoRouterID.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfRoutingInfoRouterID.setStatus(_A)
class _SnOspfRoutingInfoRouterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('abr',1),('asbr',2),('abrANDasbr',3)))
_SnOspfRoutingInfoRouterType_Type.__name__=_D
_SnOspfRoutingInfoRouterType_Object=MibTableColumn
snOspfRoutingInfoRouterType=_SnOspfRoutingInfoRouterType_Object((1,3,6,1,4,1,1991,1,2,4,14,1,1,3),_SnOspfRoutingInfoRouterType_Type())
snOspfRoutingInfoRouterType.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfRoutingInfoRouterType.setStatus(_A)
_SnOspfRoutingInfoNextHopRouterID_Type=RouterID
_SnOspfRoutingInfoNextHopRouterID_Object=MibTableColumn
snOspfRoutingInfoNextHopRouterID=_SnOspfRoutingInfoNextHopRouterID_Object((1,3,6,1,4,1,1991,1,2,4,14,1,1,4),_SnOspfRoutingInfoNextHopRouterID_Type())
snOspfRoutingInfoNextHopRouterID.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfRoutingInfoNextHopRouterID.setStatus(_A)
_SnOspfRoutingInfoOutgoingInterface_Type=Integer32
_SnOspfRoutingInfoOutgoingInterface_Object=MibTableColumn
snOspfRoutingInfoOutgoingInterface=_SnOspfRoutingInfoOutgoingInterface_Object((1,3,6,1,4,1,1991,1,2,4,14,1,1,5),_SnOspfRoutingInfoOutgoingInterface_Type())
snOspfRoutingInfoOutgoingInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfRoutingInfoOutgoingInterface.setStatus(_A)
_SnOspfTrapControl_ObjectIdentity=ObjectIdentity
snOspfTrapControl=_SnOspfTrapControl_ObjectIdentity((1,3,6,1,4,1,1991,1,2,4,15))
class _SnOspfSetTrap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SnOspfSetTrap_Type.__name__=_G
_SnOspfSetTrap_Object=MibScalar
snOspfSetTrap=_SnOspfSetTrap_Object((1,3,6,1,4,1,1991,1,2,4,15,1),_SnOspfSetTrap_Type())
snOspfSetTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfSetTrap.setStatus(_A)
class _SnOspfConfigErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_z,0),('badVersion',1),('areaMismatch',2),('unknownNbmaNbr',3),('unknownVirtualNbr',4),('authTypeMismatch',5),('authFailure',6),('netMaskMismatch',7),('helloIntervalMismatch',8),('deadIntervalMismatch',9),('optionMismatch',10)))
_SnOspfConfigErrorType_Type.__name__=_D
_SnOspfConfigErrorType_Object=MibScalar
snOspfConfigErrorType=_SnOspfConfigErrorType_Object((1,3,6,1,4,1,1991,1,2,4,15,2),_SnOspfConfigErrorType_Type())
snOspfConfigErrorType.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfConfigErrorType.setStatus(_A)
class _SnOspfPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_z,0),('hello',1),('dbDescript',2),('lsReq',3),('lsUpdate',4),('lsAck',5)))
_SnOspfPacketType_Type.__name__=_D
_SnOspfPacketType_Object=MibScalar
snOspfPacketType=_SnOspfPacketType_Object((1,3,6,1,4,1,1991,1,2,4,15,3),_SnOspfPacketType_Type())
snOspfPacketType.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfPacketType.setStatus(_A)
_SnOspfPacketSrc_Type=IpAddress
_SnOspfPacketSrc_Object=MibScalar
snOspfPacketSrc=_SnOspfPacketSrc_Object((1,3,6,1,4,1,1991,1,2,4,15,4),_SnOspfPacketSrc_Type())
snOspfPacketSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:snOspfPacketSrc.setStatus(_A)
_SnOspfTrapsGenerationMode_Type=RtrStatus
_SnOspfTrapsGenerationMode_Object=MibScalar
snOspfTrapsGenerationMode=_SnOspfTrapsGenerationMode_Object((1,3,6,1,4,1,1991,1,2,4,15,5),_SnOspfTrapsGenerationMode_Type())
snOspfTrapsGenerationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:snOspfTrapsGenerationMode.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_X:AreaID,_l:RouterID,'Metric':Metric,'BigMetric':BigMetric,'TruthVal':TruthVal,_a:RtrStatus,_U:PositiveInteger,_T:HelloRange,_L:UpToMaxAge,_V:DesignatedRouterPriority,'TOSType':TOSType,'snOspf':snOspf,'snOspfGen':snOspfGen,'snOspfRouterId':snOspfRouterId,'snOspfAdminStat':snOspfAdminStat,'snOspfASBdrRtrStatus':snOspfASBdrRtrStatus,'snOspfRedisMode':snOspfRedisMode,'snOspfDefaultOspfMetricValue':snOspfDefaultOspfMetricValue,'snOspfExternLSACount':snOspfExternLSACount,'snOspfExternLSACksumSum':snOspfExternLSACksumSum,'snOspfOriginateNewLSAs':snOspfOriginateNewLSAs,'snOspfRxNewLSAs':snOspfRxNewLSAs,'snOspfOspfRedisMetricType':snOspfOspfRedisMetricType,'snOspfExtLsdbLimit':snOspfExtLsdbLimit,'snOspfExitOverflowInterval':snOspfExitOverflowInterval,'snOspfRfc1583Compatibility':snOspfRfc1583Compatibility,'snOspfRouterIdFormat':snOspfRouterIdFormat,'snOspfDistance':snOspfDistance,'snOspfDistanceIntra':snOspfDistanceIntra,'snOspfDistanceInter':snOspfDistanceInter,'snOspfDistanceExternal':snOspfDistanceExternal,'snOspfArea':snOspfArea,'snOspfAreaTable':snOspfAreaTable,'snOspfAreaEntry':snOspfAreaEntry,_c:snOspfAreaId,'snOspfImportASExtern':snOspfImportASExtern,'snOspfStubMetric':snOspfStubMetric,'snOspfAreaRowStatus':snOspfAreaRowStatus,'snOspfAreaIdFormat':snOspfAreaIdFormat,'snOspfAddrRange':snOspfAddrRange,'snOspfAreaRangeTable':snOspfAreaRangeTable,'snOspfAreaRangeEntry':snOspfAreaRangeEntry,_d:snOspfAreaRangeAreaID,_e:snOspfAreaRangeNet,'snOspfAreaRangeMask':snOspfAreaRangeMask,'snOspfAreaRangeRowStatus':snOspfAreaRangeRowStatus,'snOspfAreaRangeAreaIdFormat':snOspfAreaRangeAreaIdFormat,'snOspfIntf':snOspfIntf,'snOspfIfTable':snOspfIfTable,'snOspfIfEntry':snOspfIfEntry,_f:snOspfIfPort,'snOspfIfAreaId':snOspfIfAreaId,'snOspfIfAdminStat':snOspfIfAdminStat,'snOspfIfRtrPriority':snOspfIfRtrPriority,'snOspfIfTransitDelay':snOspfIfTransitDelay,'snOspfIfRetransInterval':snOspfIfRetransInterval,'snOspfIfHelloInterval':snOspfIfHelloInterval,'snOspfIfRtrDeadInterval':snOspfIfRtrDeadInterval,'snOspfIfAuthType':snOspfIfAuthType,'snOspfIfAuthKey':snOspfIfAuthKey,'snOspfIfMetricValue':snOspfIfMetricValue,'snOspfIfRowStatus':snOspfIfRowStatus,'snOspfIfMd5AuthKeyId':snOspfIfMd5AuthKeyId,'snOspfIfMd5AuthKey':snOspfIfMd5AuthKey,'snOspfIfMd5ActivationWaitTime':snOspfIfMd5ActivationWaitTime,'snOspfIfAreaIdFormat':snOspfIfAreaIdFormat,'snOspfIfPassiveMode':snOspfIfPassiveMode,'snOspfIfDatabaseFilterAllOut':snOspfIfDatabaseFilterAllOut,'snOspfIfMtuIgnore':snOspfIfMtuIgnore,'snOspfIfNetworkP2mp':snOspfIfNetworkP2mp,'snOspfIf2Table':snOspfIf2Table,'snOspfIf2Entry':snOspfIf2Entry,_g:snOspfIf2Port,'snOspfIf2AreaId':snOspfIf2AreaId,'snOspfIf2AdminStat':snOspfIf2AdminStat,'snOspfIf2RtrPriority':snOspfIf2RtrPriority,'snOspfIf2TransitDelay':snOspfIf2TransitDelay,'snOspfIf2RetransInterval':snOspfIf2RetransInterval,'snOspfIf2HelloInterval':snOspfIf2HelloInterval,'snOspfIf2RtrDeadInterval':snOspfIf2RtrDeadInterval,'snOspfIf2AuthType':snOspfIf2AuthType,'snOspfIf2AuthKey':snOspfIf2AuthKey,'snOspfIf2MetricValue':snOspfIf2MetricValue,'snOspfIf2RowStatus':snOspfIf2RowStatus,'snOspfIf2Md5AuthKeyId':snOspfIf2Md5AuthKeyId,'snOspfIf2Md5AuthKey':snOspfIf2Md5AuthKey,'snOspfIf2Md5ActivationWaitTime':snOspfIf2Md5ActivationWaitTime,'snOspfIf2AreaIdFormat':snOspfIf2AreaIdFormat,'snOspfIf2PassiveMode':snOspfIf2PassiveMode,'snOspfIf2DatabaseFilterAllOut':snOspfIf2DatabaseFilterAllOut,'snOspfIf2MtuIgnore':snOspfIf2MtuIgnore,'snOspfIf2NetworkP2mp':snOspfIf2NetworkP2mp,'snOspfIf2NetworkP2pt':snOspfIf2NetworkP2pt,'snOspfIf2NetworkNonBroadcast':snOspfIf2NetworkNonBroadcast,'snOspfVirtIf':snOspfVirtIf,'snOspfVirtIfTable':snOspfVirtIfTable,'snOspfVirtIfEntry':snOspfVirtIfEntry,_h:snOspfVirtIfAreaID,_i:snOspfVirtIfNeighbor,'snOspfVirtIfTransitDelay':snOspfVirtIfTransitDelay,'snOspfVirtIfRetransInterval':snOspfVirtIfRetransInterval,'snOspfVirtIfHelloInterval':snOspfVirtIfHelloInterval,'snOspfVirtIfRtrDeadInterval':snOspfVirtIfRtrDeadInterval,'snOspfVirtIfAuthType':snOspfVirtIfAuthType,'snOspfVirtIfAuthKey':snOspfVirtIfAuthKey,'snOspfVirtIfRowStatus':snOspfVirtIfRowStatus,'snOspfVirtIfMd5AuthKeyId':snOspfVirtIfMd5AuthKeyId,'snOspfVirtIfMd5AuthKey':snOspfVirtIfMd5AuthKey,'snOspfVirtIfMd5ActivationWaitTime':snOspfVirtIfMd5ActivationWaitTime,'snOspfVirtIfAreaIdFormat':snOspfVirtIfAreaIdFormat,'snOspfRedis':snOspfRedis,'snOspfRedisTable':snOspfRedisTable,'snOspfRedisEntry':snOspfRedisEntry,_j:snOspfRedisIndex,'snOspfRedisIpAddress':snOspfRedisIpAddress,'snOspfRedisMask':snOspfRedisMask,'snOspfRedisAction':snOspfRedisAction,'snOspfRedisProtocol':snOspfRedisProtocol,'snOspfRedisSetOspfMetric':snOspfRedisSetOspfMetric,'snOspfRedisOspfMetricValue':snOspfRedisOspfMetricValue,'snOspfRedisMatchRipMetric':snOspfRedisMatchRipMetric,'snOspfRedisRipMetricValue':snOspfRedisRipMetricValue,'snOspfRedisRowStatus':snOspfRedisRowStatus,'snOspfNbr':snOspfNbr,'snOspfNbrTable':snOspfNbrTable,'snOspfNbrEntry':snOspfNbrEntry,_k:snOspfNbrEntryIndex,'snOspfNbrPort':snOspfNbrPort,'snOspfNbrIpAddr':snOspfNbrIpAddr,'snOspfNbrIndex':snOspfNbrIndex,'snOspfNbrRtrId':snOspfNbrRtrId,'snOspfNbrOptions':snOspfNbrOptions,'snOspfNbrPriority':snOspfNbrPriority,'snOspfNbrState':snOspfNbrState,'snOspfNbrEvents':snOspfNbrEvents,'snOspfNbrLsRetransQLen':snOspfNbrLsRetransQLen,'snOspfVirtNbr':snOspfVirtNbr,'snOspfVirtNbrTable':snOspfVirtNbrTable,'snOspfVirtNbrEntry':snOspfVirtNbrEntry,_r:snOspfVirtNbrEntryIndex,'snOspfVirtNbrArea':snOspfVirtNbrArea,'snOspfVirtNbrRtrId':snOspfVirtNbrRtrId,'snOspfVirtNbrIpAddr':snOspfVirtNbrIpAddr,'snOspfVirtNbrOptions':snOspfVirtNbrOptions,'snOspfVirtNbrState':snOspfVirtNbrState,'snOspfVirtNbrEvents':snOspfVirtNbrEvents,'snOspfVirtNbrLSRetransQLen':snOspfVirtNbrLSRetransQLen,'snOspfVirtNbrAreaIdFormat':snOspfVirtNbrAreaIdFormat,'snOspfLsdb':snOspfLsdb,'snOspfLsdbTable':snOspfLsdbTable,'snOspfLsdbEntry':snOspfLsdbEntry,_s:snOspfLsdbEntryIndex,'snOspfLsdbAreaId':snOspfLsdbAreaId,'snOspfLsdbType':snOspfLsdbType,'snOspfLsdbLsId':snOspfLsdbLsId,'snOspfLsdbRouterId':snOspfLsdbRouterId,'snOspfLsdbSequence':snOspfLsdbSequence,'snOspfLsdbAge':snOspfLsdbAge,'snOspfLsdbChecksum':snOspfLsdbChecksum,'snOspfLsdbAdvertisement':snOspfLsdbAdvertisement,'snOspfLsdbAreaIdFormat':snOspfLsdbAreaIdFormat,'snOspfExtLsdb':snOspfExtLsdb,'snOspfExtLsdbTable':snOspfExtLsdbTable,'snOspfExtLsdbEntry':snOspfExtLsdbEntry,_u:snOspfExtLsdbEntryIndex,'snOspfExtLsdbType':snOspfExtLsdbType,'snOspfExtLsdbLsId':snOspfExtLsdbLsId,'snOspfExtLsdbRouterId':snOspfExtLsdbRouterId,'snOspfExtLsdbSequence':snOspfExtLsdbSequence,'snOspfExtLsdbAge':snOspfExtLsdbAge,'snOspfExtLsdbChecksum':snOspfExtLsdbChecksum,'snOspfExtLsdbAdvertisement':snOspfExtLsdbAdvertisement,'snOspfAreaStatus':snOspfAreaStatus,'snOspfAreaStatusTable':snOspfAreaStatusTable,'snOspfAreaStatusEntry':snOspfAreaStatusEntry,_v:snOspfAreaStatusEntryIndex,'snOspfAreaStatusAreaId':snOspfAreaStatusAreaId,'snOspfAreaStatusImportASExtern':snOspfAreaStatusImportASExtern,'snOspfAreaStatusStubMetric':snOspfAreaStatusStubMetric,'snOspfAreaStatusSpfRuns':snOspfAreaStatusSpfRuns,'snOspfAreaStatusAreaBdrRtrCount':snOspfAreaStatusAreaBdrRtrCount,'snOspfAreaStatusASBdrRtrCount':snOspfAreaStatusASBdrRtrCount,'snOspfAreaStatusLSACount':snOspfAreaStatusLSACount,'snOspfAreaStatusLSACksumSum':snOspfAreaStatusLSACksumSum,'snOspfAreaStatusAreaIdFormat':snOspfAreaStatusAreaIdFormat,'snOspfIfStatus':snOspfIfStatus,'snOspfIfStatusTable':snOspfIfStatusTable,'snOspfIfStatusEntry':snOspfIfStatusEntry,_w:snOspfIfStatusEntryIndex,'snOspfIfStatusPort':snOspfIfStatusPort,'snOspfIfStatusIpAddress':snOspfIfStatusIpAddress,'snOspfIfStatusAreaId':snOspfIfStatusAreaId,'snOspfIfStatusType':snOspfIfStatusType,'snOspfIfStatusAdminStat':snOspfIfStatusAdminStat,'snOspfIfStatusRtrPriority':snOspfIfStatusRtrPriority,'snOspfIfStatusTransitDelay':snOspfIfStatusTransitDelay,'snOspfIfStatusRetransInterval':snOspfIfStatusRetransInterval,'snOspfIfStatusHelloInterval':snOspfIfStatusHelloInterval,'snOspfIfStatusRtrDeadInterval':snOspfIfStatusRtrDeadInterval,'snOspfIfStatusState':snOspfIfStatusState,'snOspfIfStatusDesignatedRouter':snOspfIfStatusDesignatedRouter,'snOspfIfStatusBackupDesignatedRouter':snOspfIfStatusBackupDesignatedRouter,'snOspfIfStatusEvents':snOspfIfStatusEvents,'snOspfIfStatusAuthType':snOspfIfStatusAuthType,'snOspfIfStatusAuthKey':snOspfIfStatusAuthKey,'snOspfIfStatusMetricValue':snOspfIfStatusMetricValue,'snOspfIfStatusMd5AuthKeyId':snOspfIfStatusMd5AuthKeyId,'snOspfIfStatusMd5AuthKey':snOspfIfStatusMd5AuthKey,'snOspfIfStatusMd5ActivationWaitTime':snOspfIfStatusMd5ActivationWaitTime,'snOspfIfStatusAreaIdFormat':snOspfIfStatusAreaIdFormat,'snOspfVirtIfStatus':snOspfVirtIfStatus,'snOspfVirtIfStatusTable':snOspfVirtIfStatusTable,'snOspfVirtIfStatusEntry':snOspfVirtIfStatusEntry,_x:snOspfVirtIfStatusEntryIndex,'snOspfVirtIfStatusAreaID':snOspfVirtIfStatusAreaID,'snOspfVirtIfStatusNeighbor':snOspfVirtIfStatusNeighbor,'snOspfVirtIfStatusTransitDelay':snOspfVirtIfStatusTransitDelay,'snOspfVirtIfStatusRetransInterval':snOspfVirtIfStatusRetransInterval,'snOspfVirtIfStatusHelloInterval':snOspfVirtIfStatusHelloInterval,'snOspfVirtIfStatusRtrDeadInterval':snOspfVirtIfStatusRtrDeadInterval,'snOspfVirtIfStatusState':snOspfVirtIfStatusState,'snOspfVirtIfStatusEvents':snOspfVirtIfStatusEvents,'snOspfVirtIfStatusAuthType':snOspfVirtIfStatusAuthType,'snOspfVirtIfStatusAuthKey':snOspfVirtIfStatusAuthKey,'snOspfVirtIfStatusMd5AuthKeyId':snOspfVirtIfStatusMd5AuthKeyId,'snOspfVirtIfStatusMd5AuthKey':snOspfVirtIfStatusMd5AuthKey,'snOspfVirtIfStatusMd5ActivationWaitTime':snOspfVirtIfStatusMd5ActivationWaitTime,'snOspfVirtIfStatusAreaIdFormat':snOspfVirtIfStatusAreaIdFormat,'snOspfRoutingInfo':snOspfRoutingInfo,'snOspfRoutingInfoTable':snOspfRoutingInfoTable,'snOspfRoutingInfoEntry':snOspfRoutingInfoEntry,_y:snOspfRoutingInfoIndex,'snOspfRoutingInfoRouterID':snOspfRoutingInfoRouterID,'snOspfRoutingInfoRouterType':snOspfRoutingInfoRouterType,'snOspfRoutingInfoNextHopRouterID':snOspfRoutingInfoNextHopRouterID,'snOspfRoutingInfoOutgoingInterface':snOspfRoutingInfoOutgoingInterface,'snOspfTrapControl':snOspfTrapControl,'snOspfSetTrap':snOspfSetTrap,'snOspfConfigErrorType':snOspfConfigErrorType,'snOspfPacketType':snOspfPacketType,'snOspfPacketSrc':snOspfPacketSrc,'snOspfTrapsGenerationMode':snOspfTrapsGenerationMode})