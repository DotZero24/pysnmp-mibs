_A5='fsMIStdOspfAreaAggregateMask'
_A4='fsMIStdOspfAreaAggregateNet'
_A3='fsMIStdOspfAreaAggregateLsdbType'
_A2='fsMIStdOspfAreaAggregateAreaID'
_A1='fsMIStdOspfExtLsdbRouterId'
_A0='fsMIStdOspfExtLsdbLsid'
_z='fsMIStdOspfExtLsdbType'
_y='fsMIStdOspfVirtNbrRtrId'
_x='fsMIStdOspfVirtNbrArea'
_w='loading'
_v='exchange'
_u='exchangeStart'
_t='twoWay'
_s='attempt'
_r='RouterID'
_q='fsMIStdOspfNbrAddressLessIndex'
_p='fsMIStdOspfNbrIpAddr'
_o='fsMIStdOspfVirtIfNeighbor'
_n='fsMIStdOspfVirtIfAreaId'
_m='fsMIStdOspfIfMetricTOS'
_l='fsMIStdOspfIfMetricAddressLessIf'
_k='fsMIStdOspfIfMetricIpAddress'
_j='0000000000000000'
_i='Status'
_h='AreaID'
_g='fsMIStdOspfAddressLessIf'
_f='fsMIStdOspfIfIpAddress'
_e='fsMIStdOspfHostTOS'
_d='fsMIStdOspfHostIpAddress'
_c='nssaExternalLink'
_b='asExternalLink'
_a='summaryLink'
_Z='fsMIStdOspfLsdbRouterId'
_Y='fsMIStdOspfLsdbLsid'
_X='fsMIStdOspfLsdbType'
_W='fsMIStdOspfLsdbAreaId'
_V='fsMIStdOspfStubTOS'
_U='fsMIStdOspfStubAreaId'
_T='fsMIStdOspfAreaId'
_S='TruthValue'
_R='HelloRange'
_Q='DesignatedRouterPriority'
_P='pointToPoint'
_O='IpAddress'
_N='down'
_M='00000000'
_L='UpToMaxAge'
_K='PositiveInteger'
_J='OctetString'
_I='d'
_H='read-write'
_G='fsMIStdOspfContextId'
_F='not-accessible'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='SUPERMICRO-MISTDOSPF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,_O,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_S)
fsMIStdOspf=ModuleIdentity((1,3,6,1,4,1,10876,101,1,146))
if mibBuilder.loadTexts:fsMIStdOspf.setRevisions(('2012-09-05 00:00',))
class AreaID(TextualConvention,IpAddress):status=_A
class RouterID(TextualConvention,IpAddress):status=_A
class Metric(TextualConvention,Integer32):status=_A;displayHint=_I;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class BigMetric(TextualConvention,Integer32):status=_A;displayHint=_I;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
class Status(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
class PositiveInteger(TextualConvention,Integer32):status=_A;displayHint=_I;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class HelloRange(TextualConvention,Integer32):status=_A;displayHint=_I;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class UpToMaxAge(TextualConvention,Integer32):status=_A;displayHint=_I;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
class DesignatedRouterPriority(TextualConvention,Integer32):status=_A;displayHint=_I;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class TOSType(TextualConvention,Integer32):status=_A;displayHint=_I;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_FsMIStdOspfGeneralGroup_ObjectIdentity=ObjectIdentity
fsMIStdOspfGeneralGroup=_FsMIStdOspfGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,146,1))
_FsMIStdOspfTable_Object=MibTable
fsMIStdOspfTable=_FsMIStdOspfTable_Object((1,3,6,1,4,1,10876,101,1,146,1,1))
if mibBuilder.loadTexts:fsMIStdOspfTable.setStatus(_A)
_FsMIStdOspfEntry_Object=MibTableRow
fsMIStdOspfEntry=_FsMIStdOspfEntry_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1))
fsMIStdOspfEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:fsMIStdOspfEntry.setStatus(_A)
class _FsMIStdOspfContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIStdOspfContextId_Type.__name__=_E
_FsMIStdOspfContextId_Object=MibTableColumn
fsMIStdOspfContextId=_FsMIStdOspfContextId_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,1),_FsMIStdOspfContextId_Type())
fsMIStdOspfContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfContextId.setStatus(_A)
_FsMIStdOspfRouterId_Type=RouterID
_FsMIStdOspfRouterId_Object=MibTableColumn
fsMIStdOspfRouterId=_FsMIStdOspfRouterId_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,2),_FsMIStdOspfRouterId_Type())
fsMIStdOspfRouterId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfRouterId.setStatus(_A)
_FsMIStdOspfAdminStat_Type=Status
_FsMIStdOspfAdminStat_Object=MibTableColumn
fsMIStdOspfAdminStat=_FsMIStdOspfAdminStat_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,3),_FsMIStdOspfAdminStat_Type())
fsMIStdOspfAdminStat.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfAdminStat.setStatus(_A)
class _FsMIStdOspfVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('version2',2))
_FsMIStdOspfVersionNumber_Type.__name__=_E
_FsMIStdOspfVersionNumber_Object=MibTableColumn
fsMIStdOspfVersionNumber=_FsMIStdOspfVersionNumber_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,4),_FsMIStdOspfVersionNumber_Type())
fsMIStdOspfVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfVersionNumber.setStatus(_A)
_FsMIStdOspfAreaBdrRtrStatus_Type=TruthValue
_FsMIStdOspfAreaBdrRtrStatus_Object=MibTableColumn
fsMIStdOspfAreaBdrRtrStatus=_FsMIStdOspfAreaBdrRtrStatus_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,5),_FsMIStdOspfAreaBdrRtrStatus_Type())
fsMIStdOspfAreaBdrRtrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfAreaBdrRtrStatus.setStatus(_A)
_FsMIStdOspfASBdrRtrStatus_Type=TruthValue
_FsMIStdOspfASBdrRtrStatus_Object=MibTableColumn
fsMIStdOspfASBdrRtrStatus=_FsMIStdOspfASBdrRtrStatus_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,6),_FsMIStdOspfASBdrRtrStatus_Type())
fsMIStdOspfASBdrRtrStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfASBdrRtrStatus.setStatus(_A)
_FsMIStdOspfExternLsaCount_Type=Gauge32
_FsMIStdOspfExternLsaCount_Object=MibTableColumn
fsMIStdOspfExternLsaCount=_FsMIStdOspfExternLsaCount_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,7),_FsMIStdOspfExternLsaCount_Type())
fsMIStdOspfExternLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfExternLsaCount.setStatus(_A)
_FsMIStdOspfExternLsaCksumSum_Type=Integer32
_FsMIStdOspfExternLsaCksumSum_Object=MibTableColumn
fsMIStdOspfExternLsaCksumSum=_FsMIStdOspfExternLsaCksumSum_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,8),_FsMIStdOspfExternLsaCksumSum_Type())
fsMIStdOspfExternLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfExternLsaCksumSum.setStatus(_A)
_FsMIStdOspfTOSSupport_Type=TruthValue
_FsMIStdOspfTOSSupport_Object=MibTableColumn
fsMIStdOspfTOSSupport=_FsMIStdOspfTOSSupport_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,9),_FsMIStdOspfTOSSupport_Type())
fsMIStdOspfTOSSupport.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfTOSSupport.setStatus(_A)
_FsMIStdOspfOriginateNewLsas_Type=Counter32
_FsMIStdOspfOriginateNewLsas_Object=MibTableColumn
fsMIStdOspfOriginateNewLsas=_FsMIStdOspfOriginateNewLsas_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,10),_FsMIStdOspfOriginateNewLsas_Type())
fsMIStdOspfOriginateNewLsas.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfOriginateNewLsas.setStatus(_A)
_FsMIStdOspfRxNewLsas_Type=Counter32
_FsMIStdOspfRxNewLsas_Object=MibTableColumn
fsMIStdOspfRxNewLsas=_FsMIStdOspfRxNewLsas_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,11),_FsMIStdOspfRxNewLsas_Type())
fsMIStdOspfRxNewLsas.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfRxNewLsas.setStatus(_A)
class _FsMIStdOspfExtLsdbLimit_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_FsMIStdOspfExtLsdbLimit_Type.__name__=_E
_FsMIStdOspfExtLsdbLimit_Object=MibTableColumn
fsMIStdOspfExtLsdbLimit=_FsMIStdOspfExtLsdbLimit_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,12),_FsMIStdOspfExtLsdbLimit_Type())
fsMIStdOspfExtLsdbLimit.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfExtLsdbLimit.setStatus(_A)
class _FsMIStdOspfMulticastExtensions_Type(Integer32):defaultValue=0
_FsMIStdOspfMulticastExtensions_Type.__name__=_E
_FsMIStdOspfMulticastExtensions_Object=MibTableColumn
fsMIStdOspfMulticastExtensions=_FsMIStdOspfMulticastExtensions_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,13),_FsMIStdOspfMulticastExtensions_Type())
fsMIStdOspfMulticastExtensions.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfMulticastExtensions.setStatus(_A)
class _FsMIStdOspfExitOverflowInterval_Type(PositiveInteger):defaultValue=0
_FsMIStdOspfExitOverflowInterval_Type.__name__=_K
_FsMIStdOspfExitOverflowInterval_Object=MibTableColumn
fsMIStdOspfExitOverflowInterval=_FsMIStdOspfExitOverflowInterval_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,14),_FsMIStdOspfExitOverflowInterval_Type())
fsMIStdOspfExitOverflowInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfExitOverflowInterval.setStatus(_A)
_FsMIStdOspfDemandExtensions_Type=TruthValue
_FsMIStdOspfDemandExtensions_Object=MibTableColumn
fsMIStdOspfDemandExtensions=_FsMIStdOspfDemandExtensions_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,15),_FsMIStdOspfDemandExtensions_Type())
fsMIStdOspfDemandExtensions.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfDemandExtensions.setStatus(_A)
_FsMIStdOspfStatus_Type=RowStatus
_FsMIStdOspfStatus_Object=MibTableColumn
fsMIStdOspfStatus=_FsMIStdOspfStatus_Object((1,3,6,1,4,1,10876,101,1,146,1,1,1,16),_FsMIStdOspfStatus_Type())
fsMIStdOspfStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdOspfStatus.setStatus(_A)
_FsMIStdOspfAreaTable_Object=MibTable
fsMIStdOspfAreaTable=_FsMIStdOspfAreaTable_Object((1,3,6,1,4,1,10876,101,1,146,2))
if mibBuilder.loadTexts:fsMIStdOspfAreaTable.setStatus(_A)
_FsMIStdOspfAreaEntry_Object=MibTableRow
fsMIStdOspfAreaEntry=_FsMIStdOspfAreaEntry_Object((1,3,6,1,4,1,10876,101,1,146,2,1))
fsMIStdOspfAreaEntry.setIndexNames((0,_B,_G),(0,_B,_T))
if mibBuilder.loadTexts:fsMIStdOspfAreaEntry.setStatus(_A)
_FsMIStdOspfAreaId_Type=AreaID
_FsMIStdOspfAreaId_Object=MibTableColumn
fsMIStdOspfAreaId=_FsMIStdOspfAreaId_Object((1,3,6,1,4,1,10876,101,1,146,2,1,1),_FsMIStdOspfAreaId_Type())
fsMIStdOspfAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfAreaId.setStatus(_A)
class _FsMIStdOspfImportAsExtern_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('importExternal',1),('importNoExternal',2),('importNssa',3)))
_FsMIStdOspfImportAsExtern_Type.__name__=_E
_FsMIStdOspfImportAsExtern_Object=MibTableColumn
fsMIStdOspfImportAsExtern=_FsMIStdOspfImportAsExtern_Object((1,3,6,1,4,1,10876,101,1,146,2,1,3),_FsMIStdOspfImportAsExtern_Type())
fsMIStdOspfImportAsExtern.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfImportAsExtern.setStatus(_A)
_FsMIStdOspfSpfRuns_Type=Counter32
_FsMIStdOspfSpfRuns_Object=MibTableColumn
fsMIStdOspfSpfRuns=_FsMIStdOspfSpfRuns_Object((1,3,6,1,4,1,10876,101,1,146,2,1,4),_FsMIStdOspfSpfRuns_Type())
fsMIStdOspfSpfRuns.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfSpfRuns.setStatus(_A)
_FsMIStdOspfAreaBdrRtrCount_Type=Gauge32
_FsMIStdOspfAreaBdrRtrCount_Object=MibTableColumn
fsMIStdOspfAreaBdrRtrCount=_FsMIStdOspfAreaBdrRtrCount_Object((1,3,6,1,4,1,10876,101,1,146,2,1,5),_FsMIStdOspfAreaBdrRtrCount_Type())
fsMIStdOspfAreaBdrRtrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfAreaBdrRtrCount.setStatus(_A)
_FsMIStdOspfAsBdrRtrCount_Type=Gauge32
_FsMIStdOspfAsBdrRtrCount_Object=MibTableColumn
fsMIStdOspfAsBdrRtrCount=_FsMIStdOspfAsBdrRtrCount_Object((1,3,6,1,4,1,10876,101,1,146,2,1,6),_FsMIStdOspfAsBdrRtrCount_Type())
fsMIStdOspfAsBdrRtrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfAsBdrRtrCount.setStatus(_A)
_FsMIStdOspfAreaLsaCount_Type=Gauge32
_FsMIStdOspfAreaLsaCount_Object=MibTableColumn
fsMIStdOspfAreaLsaCount=_FsMIStdOspfAreaLsaCount_Object((1,3,6,1,4,1,10876,101,1,146,2,1,7),_FsMIStdOspfAreaLsaCount_Type())
fsMIStdOspfAreaLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfAreaLsaCount.setStatus(_A)
class _FsMIStdOspfAreaLsaCksumSum_Type(Integer32):defaultValue=0
_FsMIStdOspfAreaLsaCksumSum_Type.__name__=_E
_FsMIStdOspfAreaLsaCksumSum_Object=MibTableColumn
fsMIStdOspfAreaLsaCksumSum=_FsMIStdOspfAreaLsaCksumSum_Object((1,3,6,1,4,1,10876,101,1,146,2,1,8),_FsMIStdOspfAreaLsaCksumSum_Type())
fsMIStdOspfAreaLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfAreaLsaCksumSum.setStatus(_A)
class _FsMIStdOspfAreaSummary_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAreaSummary',1),('sendAreaSummary',2)))
_FsMIStdOspfAreaSummary_Type.__name__=_E
_FsMIStdOspfAreaSummary_Object=MibTableColumn
fsMIStdOspfAreaSummary=_FsMIStdOspfAreaSummary_Object((1,3,6,1,4,1,10876,101,1,146,2,1,9),_FsMIStdOspfAreaSummary_Type())
fsMIStdOspfAreaSummary.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfAreaSummary.setStatus(_A)
_FsMIStdOspfAreaStatus_Type=RowStatus
_FsMIStdOspfAreaStatus_Object=MibTableColumn
fsMIStdOspfAreaStatus=_FsMIStdOspfAreaStatus_Object((1,3,6,1,4,1,10876,101,1,146,2,1,10),_FsMIStdOspfAreaStatus_Type())
fsMIStdOspfAreaStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfAreaStatus.setStatus(_A)
_FsMIStdOspfStubAreaTable_Object=MibTable
fsMIStdOspfStubAreaTable=_FsMIStdOspfStubAreaTable_Object((1,3,6,1,4,1,10876,101,1,146,3))
if mibBuilder.loadTexts:fsMIStdOspfStubAreaTable.setStatus(_A)
_FsMIStdOspfStubAreaEntry_Object=MibTableRow
fsMIStdOspfStubAreaEntry=_FsMIStdOspfStubAreaEntry_Object((1,3,6,1,4,1,10876,101,1,146,3,1))
fsMIStdOspfStubAreaEntry.setIndexNames((0,_B,_G),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:fsMIStdOspfStubAreaEntry.setStatus(_A)
_FsMIStdOspfStubAreaId_Type=AreaID
_FsMIStdOspfStubAreaId_Object=MibTableColumn
fsMIStdOspfStubAreaId=_FsMIStdOspfStubAreaId_Object((1,3,6,1,4,1,10876,101,1,146,3,1,1),_FsMIStdOspfStubAreaId_Type())
fsMIStdOspfStubAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfStubAreaId.setStatus(_A)
_FsMIStdOspfStubTOS_Type=TOSType
_FsMIStdOspfStubTOS_Object=MibTableColumn
fsMIStdOspfStubTOS=_FsMIStdOspfStubTOS_Object((1,3,6,1,4,1,10876,101,1,146,3,1,2),_FsMIStdOspfStubTOS_Type())
fsMIStdOspfStubTOS.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfStubTOS.setStatus(_A)
_FsMIStdOspfStubMetric_Type=BigMetric
_FsMIStdOspfStubMetric_Object=MibTableColumn
fsMIStdOspfStubMetric=_FsMIStdOspfStubMetric_Object((1,3,6,1,4,1,10876,101,1,146,3,1,3),_FsMIStdOspfStubMetric_Type())
fsMIStdOspfStubMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfStubMetric.setStatus(_A)
_FsMIStdOspfStubStatus_Type=RowStatus
_FsMIStdOspfStubStatus_Object=MibTableColumn
fsMIStdOspfStubStatus=_FsMIStdOspfStubStatus_Object((1,3,6,1,4,1,10876,101,1,146,3,1,4),_FsMIStdOspfStubStatus_Type())
fsMIStdOspfStubStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfStubStatus.setStatus(_A)
class _FsMIStdOspfStubMetricType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ospfMetric',1),('comparableCost',2),('nonComparable',3)))
_FsMIStdOspfStubMetricType_Type.__name__=_E
_FsMIStdOspfStubMetricType_Object=MibTableColumn
fsMIStdOspfStubMetricType=_FsMIStdOspfStubMetricType_Object((1,3,6,1,4,1,10876,101,1,146,3,1,5),_FsMIStdOspfStubMetricType_Type())
fsMIStdOspfStubMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfStubMetricType.setStatus(_A)
_FsMIStdOspfLsdbTable_Object=MibTable
fsMIStdOspfLsdbTable=_FsMIStdOspfLsdbTable_Object((1,3,6,1,4,1,10876,101,1,146,4))
if mibBuilder.loadTexts:fsMIStdOspfLsdbTable.setStatus(_A)
_FsMIStdOspfLsdbEntry_Object=MibTableRow
fsMIStdOspfLsdbEntry=_FsMIStdOspfLsdbEntry_Object((1,3,6,1,4,1,10876,101,1,146,4,1))
fsMIStdOspfLsdbEntry.setIndexNames((0,_B,_G),(0,_B,_W),(0,_B,_X),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:fsMIStdOspfLsdbEntry.setStatus(_A)
_FsMIStdOspfLsdbAreaId_Type=AreaID
_FsMIStdOspfLsdbAreaId_Object=MibTableColumn
fsMIStdOspfLsdbAreaId=_FsMIStdOspfLsdbAreaId_Object((1,3,6,1,4,1,10876,101,1,146,4,1,1),_FsMIStdOspfLsdbAreaId_Type())
fsMIStdOspfLsdbAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfLsdbAreaId.setStatus(_A)
class _FsMIStdOspfLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('routerLink',1),('networkLink',2),(_a,3),('asSummaryLink',4),(_b,5),('multicastLink',6),(_c,7)))
_FsMIStdOspfLsdbType_Type.__name__=_E
_FsMIStdOspfLsdbType_Object=MibTableColumn
fsMIStdOspfLsdbType=_FsMIStdOspfLsdbType_Object((1,3,6,1,4,1,10876,101,1,146,4,1,2),_FsMIStdOspfLsdbType_Type())
fsMIStdOspfLsdbType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfLsdbType.setStatus(_A)
_FsMIStdOspfLsdbLsid_Type=IpAddress
_FsMIStdOspfLsdbLsid_Object=MibTableColumn
fsMIStdOspfLsdbLsid=_FsMIStdOspfLsdbLsid_Object((1,3,6,1,4,1,10876,101,1,146,4,1,3),_FsMIStdOspfLsdbLsid_Type())
fsMIStdOspfLsdbLsid.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfLsdbLsid.setStatus(_A)
_FsMIStdOspfLsdbRouterId_Type=RouterID
_FsMIStdOspfLsdbRouterId_Object=MibTableColumn
fsMIStdOspfLsdbRouterId=_FsMIStdOspfLsdbRouterId_Object((1,3,6,1,4,1,10876,101,1,146,4,1,4),_FsMIStdOspfLsdbRouterId_Type())
fsMIStdOspfLsdbRouterId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfLsdbRouterId.setStatus(_A)
_FsMIStdOspfLsdbSequence_Type=Integer32
_FsMIStdOspfLsdbSequence_Object=MibTableColumn
fsMIStdOspfLsdbSequence=_FsMIStdOspfLsdbSequence_Object((1,3,6,1,4,1,10876,101,1,146,4,1,5),_FsMIStdOspfLsdbSequence_Type())
fsMIStdOspfLsdbSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfLsdbSequence.setStatus(_A)
_FsMIStdOspfLsdbAge_Type=Integer32
_FsMIStdOspfLsdbAge_Object=MibTableColumn
fsMIStdOspfLsdbAge=_FsMIStdOspfLsdbAge_Object((1,3,6,1,4,1,10876,101,1,146,4,1,6),_FsMIStdOspfLsdbAge_Type())
fsMIStdOspfLsdbAge.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfLsdbAge.setStatus(_A)
_FsMIStdOspfLsdbChecksum_Type=Integer32
_FsMIStdOspfLsdbChecksum_Object=MibTableColumn
fsMIStdOspfLsdbChecksum=_FsMIStdOspfLsdbChecksum_Object((1,3,6,1,4,1,10876,101,1,146,4,1,7),_FsMIStdOspfLsdbChecksum_Type())
fsMIStdOspfLsdbChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfLsdbChecksum.setStatus(_A)
class _FsMIStdOspfLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_FsMIStdOspfLsdbAdvertisement_Type.__name__=_J
_FsMIStdOspfLsdbAdvertisement_Object=MibTableColumn
fsMIStdOspfLsdbAdvertisement=_FsMIStdOspfLsdbAdvertisement_Object((1,3,6,1,4,1,10876,101,1,146,4,1,8),_FsMIStdOspfLsdbAdvertisement_Type())
fsMIStdOspfLsdbAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfLsdbAdvertisement.setStatus(_A)
_FsMIStdOspfHostTable_Object=MibTable
fsMIStdOspfHostTable=_FsMIStdOspfHostTable_Object((1,3,6,1,4,1,10876,101,1,146,5))
if mibBuilder.loadTexts:fsMIStdOspfHostTable.setStatus(_A)
_FsMIStdOspfHostEntry_Object=MibTableRow
fsMIStdOspfHostEntry=_FsMIStdOspfHostEntry_Object((1,3,6,1,4,1,10876,101,1,146,5,1))
fsMIStdOspfHostEntry.setIndexNames((0,_B,_G),(0,_B,_d),(0,_B,_e))
if mibBuilder.loadTexts:fsMIStdOspfHostEntry.setStatus(_A)
_FsMIStdOspfHostIpAddress_Type=IpAddress
_FsMIStdOspfHostIpAddress_Object=MibTableColumn
fsMIStdOspfHostIpAddress=_FsMIStdOspfHostIpAddress_Object((1,3,6,1,4,1,10876,101,1,146,5,1,1),_FsMIStdOspfHostIpAddress_Type())
fsMIStdOspfHostIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfHostIpAddress.setStatus(_A)
_FsMIStdOspfHostTOS_Type=TOSType
_FsMIStdOspfHostTOS_Object=MibTableColumn
fsMIStdOspfHostTOS=_FsMIStdOspfHostTOS_Object((1,3,6,1,4,1,10876,101,1,146,5,1,2),_FsMIStdOspfHostTOS_Type())
fsMIStdOspfHostTOS.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfHostTOS.setStatus(_A)
_FsMIStdOspfHostMetric_Type=Metric
_FsMIStdOspfHostMetric_Object=MibTableColumn
fsMIStdOspfHostMetric=_FsMIStdOspfHostMetric_Object((1,3,6,1,4,1,10876,101,1,146,5,1,3),_FsMIStdOspfHostMetric_Type())
fsMIStdOspfHostMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfHostMetric.setStatus(_A)
_FsMIStdOspfHostStatus_Type=RowStatus
_FsMIStdOspfHostStatus_Object=MibTableColumn
fsMIStdOspfHostStatus=_FsMIStdOspfHostStatus_Object((1,3,6,1,4,1,10876,101,1,146,5,1,4),_FsMIStdOspfHostStatus_Type())
fsMIStdOspfHostStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfHostStatus.setStatus(_A)
_FsMIStdOspfHostAreaID_Type=AreaID
_FsMIStdOspfHostAreaID_Object=MibTableColumn
fsMIStdOspfHostAreaID=_FsMIStdOspfHostAreaID_Object((1,3,6,1,4,1,10876,101,1,146,5,1,5),_FsMIStdOspfHostAreaID_Type())
fsMIStdOspfHostAreaID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfHostAreaID.setStatus(_A)
_FsMIStdOspfIfTable_Object=MibTable
fsMIStdOspfIfTable=_FsMIStdOspfIfTable_Object((1,3,6,1,4,1,10876,101,1,146,6))
if mibBuilder.loadTexts:fsMIStdOspfIfTable.setStatus(_A)
_FsMIStdOspfIfEntry_Object=MibTableRow
fsMIStdOspfIfEntry=_FsMIStdOspfIfEntry_Object((1,3,6,1,4,1,10876,101,1,146,6,1))
fsMIStdOspfIfEntry.setIndexNames((0,_B,_G),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:fsMIStdOspfIfEntry.setStatus(_A)
_FsMIStdOspfIfIpAddress_Type=IpAddress
_FsMIStdOspfIfIpAddress_Object=MibTableColumn
fsMIStdOspfIfIpAddress=_FsMIStdOspfIfIpAddress_Object((1,3,6,1,4,1,10876,101,1,146,6,1,1),_FsMIStdOspfIfIpAddress_Type())
fsMIStdOspfIfIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfIfIpAddress.setStatus(_A)
class _FsMIStdOspfAddressLessIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIStdOspfAddressLessIf_Type.__name__=_E
_FsMIStdOspfAddressLessIf_Object=MibTableColumn
fsMIStdOspfAddressLessIf=_FsMIStdOspfAddressLessIf_Object((1,3,6,1,4,1,10876,101,1,146,6,1,2),_FsMIStdOspfAddressLessIf_Type())
fsMIStdOspfAddressLessIf.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfAddressLessIf.setStatus(_A)
class _FsMIStdOspfIfAreaId_Type(AreaID):defaultHexValue=_M
_FsMIStdOspfIfAreaId_Type.__name__=_h
_FsMIStdOspfIfAreaId_Object=MibTableColumn
fsMIStdOspfIfAreaId=_FsMIStdOspfIfAreaId_Object((1,3,6,1,4,1,10876,101,1,146,6,1,3),_FsMIStdOspfIfAreaId_Type())
fsMIStdOspfIfAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfAreaId.setStatus(_A)
class _FsMIStdOspfIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*(('broadcast',1),('nbma',2),(_P,3),('pointToMultipoint',5)))
_FsMIStdOspfIfType_Type.__name__=_E
_FsMIStdOspfIfType_Object=MibTableColumn
fsMIStdOspfIfType=_FsMIStdOspfIfType_Object((1,3,6,1,4,1,10876,101,1,146,6,1,4),_FsMIStdOspfIfType_Type())
fsMIStdOspfIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfType.setStatus(_A)
class _FsMIStdOspfIfAdminStat_Type(Status):defaultValue=1
_FsMIStdOspfIfAdminStat_Type.__name__=_i
_FsMIStdOspfIfAdminStat_Object=MibTableColumn
fsMIStdOspfIfAdminStat=_FsMIStdOspfIfAdminStat_Object((1,3,6,1,4,1,10876,101,1,146,6,1,5),_FsMIStdOspfIfAdminStat_Type())
fsMIStdOspfIfAdminStat.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfAdminStat.setStatus(_A)
class _FsMIStdOspfIfRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_FsMIStdOspfIfRtrPriority_Type.__name__=_Q
_FsMIStdOspfIfRtrPriority_Object=MibTableColumn
fsMIStdOspfIfRtrPriority=_FsMIStdOspfIfRtrPriority_Object((1,3,6,1,4,1,10876,101,1,146,6,1,6),_FsMIStdOspfIfRtrPriority_Type())
fsMIStdOspfIfRtrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfRtrPriority.setStatus(_A)
class _FsMIStdOspfIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_FsMIStdOspfIfTransitDelay_Type.__name__=_L
_FsMIStdOspfIfTransitDelay_Object=MibTableColumn
fsMIStdOspfIfTransitDelay=_FsMIStdOspfIfTransitDelay_Object((1,3,6,1,4,1,10876,101,1,146,6,1,7),_FsMIStdOspfIfTransitDelay_Type())
fsMIStdOspfIfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfTransitDelay.setStatus(_A)
class _FsMIStdOspfIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_FsMIStdOspfIfRetransInterval_Type.__name__=_L
_FsMIStdOspfIfRetransInterval_Object=MibTableColumn
fsMIStdOspfIfRetransInterval=_FsMIStdOspfIfRetransInterval_Object((1,3,6,1,4,1,10876,101,1,146,6,1,8),_FsMIStdOspfIfRetransInterval_Type())
fsMIStdOspfIfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfRetransInterval.setStatus(_A)
class _FsMIStdOspfIfHelloInterval_Type(HelloRange):defaultValue=10
_FsMIStdOspfIfHelloInterval_Type.__name__=_R
_FsMIStdOspfIfHelloInterval_Object=MibTableColumn
fsMIStdOspfIfHelloInterval=_FsMIStdOspfIfHelloInterval_Object((1,3,6,1,4,1,10876,101,1,146,6,1,9),_FsMIStdOspfIfHelloInterval_Type())
fsMIStdOspfIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfHelloInterval.setStatus(_A)
class _FsMIStdOspfIfRtrDeadInterval_Type(PositiveInteger):defaultValue=40
_FsMIStdOspfIfRtrDeadInterval_Type.__name__=_K
_FsMIStdOspfIfRtrDeadInterval_Object=MibTableColumn
fsMIStdOspfIfRtrDeadInterval=_FsMIStdOspfIfRtrDeadInterval_Object((1,3,6,1,4,1,10876,101,1,146,6,1,10),_FsMIStdOspfIfRtrDeadInterval_Type())
fsMIStdOspfIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfRtrDeadInterval.setStatus(_A)
class _FsMIStdOspfIfPollInterval_Type(PositiveInteger):defaultValue=120
_FsMIStdOspfIfPollInterval_Type.__name__=_K
_FsMIStdOspfIfPollInterval_Object=MibTableColumn
fsMIStdOspfIfPollInterval=_FsMIStdOspfIfPollInterval_Object((1,3,6,1,4,1,10876,101,1,146,6,1,11),_FsMIStdOspfIfPollInterval_Type())
fsMIStdOspfIfPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfPollInterval.setStatus(_A)
class _FsMIStdOspfIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,1),('loopback',2),('waiting',3),(_P,4),('designatedRouter',5),('backupDesignatedRouter',6),('otherDesignatedRouter',7)))
_FsMIStdOspfIfState_Type.__name__=_E
_FsMIStdOspfIfState_Object=MibTableColumn
fsMIStdOspfIfState=_FsMIStdOspfIfState_Object((1,3,6,1,4,1,10876,101,1,146,6,1,12),_FsMIStdOspfIfState_Type())
fsMIStdOspfIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfIfState.setStatus(_A)
class _FsMIStdOspfIfDesignatedRouter_Type(IpAddress):defaultHexValue=_M
_FsMIStdOspfIfDesignatedRouter_Type.__name__=_O
_FsMIStdOspfIfDesignatedRouter_Object=MibTableColumn
fsMIStdOspfIfDesignatedRouter=_FsMIStdOspfIfDesignatedRouter_Object((1,3,6,1,4,1,10876,101,1,146,6,1,13),_FsMIStdOspfIfDesignatedRouter_Type())
fsMIStdOspfIfDesignatedRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfIfDesignatedRouter.setStatus(_A)
class _FsMIStdOspfIfBackupDesignatedRouter_Type(IpAddress):defaultHexValue=_M
_FsMIStdOspfIfBackupDesignatedRouter_Type.__name__=_O
_FsMIStdOspfIfBackupDesignatedRouter_Object=MibTableColumn
fsMIStdOspfIfBackupDesignatedRouter=_FsMIStdOspfIfBackupDesignatedRouter_Object((1,3,6,1,4,1,10876,101,1,146,6,1,14),_FsMIStdOspfIfBackupDesignatedRouter_Type())
fsMIStdOspfIfBackupDesignatedRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfIfBackupDesignatedRouter.setStatus(_A)
_FsMIStdOspfIfEvents_Type=Counter32
_FsMIStdOspfIfEvents_Object=MibTableColumn
fsMIStdOspfIfEvents=_FsMIStdOspfIfEvents_Object((1,3,6,1,4,1,10876,101,1,146,6,1,15),_FsMIStdOspfIfEvents_Type())
fsMIStdOspfIfEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfIfEvents.setStatus(_A)
class _FsMIStdOspfIfAuthKey_Type(OctetString):defaultHexValue=_j;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_FsMIStdOspfIfAuthKey_Type.__name__=_J
_FsMIStdOspfIfAuthKey_Object=MibTableColumn
fsMIStdOspfIfAuthKey=_FsMIStdOspfIfAuthKey_Object((1,3,6,1,4,1,10876,101,1,146,6,1,16),_FsMIStdOspfIfAuthKey_Type())
fsMIStdOspfIfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfAuthKey.setStatus(_A)
_FsMIStdOspfIfStatus_Type=RowStatus
_FsMIStdOspfIfStatus_Object=MibTableColumn
fsMIStdOspfIfStatus=_FsMIStdOspfIfStatus_Object((1,3,6,1,4,1,10876,101,1,146,6,1,17),_FsMIStdOspfIfStatus_Type())
fsMIStdOspfIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfStatus.setStatus(_A)
class _FsMIStdOspfIfMulticastForwarding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('blocked',1),('multicast',2),('unicast',3)))
_FsMIStdOspfIfMulticastForwarding_Type.__name__=_E
_FsMIStdOspfIfMulticastForwarding_Object=MibTableColumn
fsMIStdOspfIfMulticastForwarding=_FsMIStdOspfIfMulticastForwarding_Object((1,3,6,1,4,1,10876,101,1,146,6,1,18),_FsMIStdOspfIfMulticastForwarding_Type())
fsMIStdOspfIfMulticastForwarding.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfMulticastForwarding.setStatus(_A)
class _FsMIStdOspfIfDemand_Type(TruthValue):defaultValue=2
_FsMIStdOspfIfDemand_Type.__name__=_S
_FsMIStdOspfIfDemand_Object=MibTableColumn
fsMIStdOspfIfDemand=_FsMIStdOspfIfDemand_Object((1,3,6,1,4,1,10876,101,1,146,6,1,19),_FsMIStdOspfIfDemand_Type())
fsMIStdOspfIfDemand.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfDemand.setStatus(_A)
class _FsMIStdOspfIfAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIStdOspfIfAuthType_Type.__name__=_E
_FsMIStdOspfIfAuthType_Object=MibTableColumn
fsMIStdOspfIfAuthType=_FsMIStdOspfIfAuthType_Object((1,3,6,1,4,1,10876,101,1,146,6,1,20),_FsMIStdOspfIfAuthType_Type())
fsMIStdOspfIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfAuthType.setStatus(_A)
class _FsMIStdOspfIfCryptoAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIStdOspfIfCryptoAuthType_Type.__name__=_E
_FsMIStdOspfIfCryptoAuthType_Object=MibTableColumn
fsMIStdOspfIfCryptoAuthType=_FsMIStdOspfIfCryptoAuthType_Object((1,3,6,1,4,1,10876,101,1,146,6,1,21),_FsMIStdOspfIfCryptoAuthType_Type())
fsMIStdOspfIfCryptoAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfCryptoAuthType.setStatus(_A)
_FsMIStdOspfIfMetricTable_Object=MibTable
fsMIStdOspfIfMetricTable=_FsMIStdOspfIfMetricTable_Object((1,3,6,1,4,1,10876,101,1,146,7))
if mibBuilder.loadTexts:fsMIStdOspfIfMetricTable.setStatus(_A)
_FsMIStdOspfIfMetricEntry_Object=MibTableRow
fsMIStdOspfIfMetricEntry=_FsMIStdOspfIfMetricEntry_Object((1,3,6,1,4,1,10876,101,1,146,7,1))
fsMIStdOspfIfMetricEntry.setIndexNames((0,_B,_G),(0,_B,_k),(0,_B,_l),(0,_B,_m))
if mibBuilder.loadTexts:fsMIStdOspfIfMetricEntry.setStatus(_A)
_FsMIStdOspfIfMetricIpAddress_Type=IpAddress
_FsMIStdOspfIfMetricIpAddress_Object=MibTableColumn
fsMIStdOspfIfMetricIpAddress=_FsMIStdOspfIfMetricIpAddress_Object((1,3,6,1,4,1,10876,101,1,146,7,1,1),_FsMIStdOspfIfMetricIpAddress_Type())
fsMIStdOspfIfMetricIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfIfMetricIpAddress.setStatus(_A)
class _FsMIStdOspfIfMetricAddressLessIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIStdOspfIfMetricAddressLessIf_Type.__name__=_E
_FsMIStdOspfIfMetricAddressLessIf_Object=MibTableColumn
fsMIStdOspfIfMetricAddressLessIf=_FsMIStdOspfIfMetricAddressLessIf_Object((1,3,6,1,4,1,10876,101,1,146,7,1,2),_FsMIStdOspfIfMetricAddressLessIf_Type())
fsMIStdOspfIfMetricAddressLessIf.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfIfMetricAddressLessIf.setStatus(_A)
_FsMIStdOspfIfMetricTOS_Type=TOSType
_FsMIStdOspfIfMetricTOS_Object=MibTableColumn
fsMIStdOspfIfMetricTOS=_FsMIStdOspfIfMetricTOS_Object((1,3,6,1,4,1,10876,101,1,146,7,1,3),_FsMIStdOspfIfMetricTOS_Type())
fsMIStdOspfIfMetricTOS.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfIfMetricTOS.setStatus(_A)
_FsMIStdOspfIfMetricValue_Type=Metric
_FsMIStdOspfIfMetricValue_Object=MibTableColumn
fsMIStdOspfIfMetricValue=_FsMIStdOspfIfMetricValue_Object((1,3,6,1,4,1,10876,101,1,146,7,1,4),_FsMIStdOspfIfMetricValue_Type())
fsMIStdOspfIfMetricValue.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfMetricValue.setStatus(_A)
_FsMIStdOspfIfMetricStatus_Type=RowStatus
_FsMIStdOspfIfMetricStatus_Object=MibTableColumn
fsMIStdOspfIfMetricStatus=_FsMIStdOspfIfMetricStatus_Object((1,3,6,1,4,1,10876,101,1,146,7,1,5),_FsMIStdOspfIfMetricStatus_Type())
fsMIStdOspfIfMetricStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfIfMetricStatus.setStatus(_A)
_FsMIStdOspfVirtIfTable_Object=MibTable
fsMIStdOspfVirtIfTable=_FsMIStdOspfVirtIfTable_Object((1,3,6,1,4,1,10876,101,1,146,8))
if mibBuilder.loadTexts:fsMIStdOspfVirtIfTable.setStatus(_A)
_FsMIStdOspfVirtIfEntry_Object=MibTableRow
fsMIStdOspfVirtIfEntry=_FsMIStdOspfVirtIfEntry_Object((1,3,6,1,4,1,10876,101,1,146,8,1))
fsMIStdOspfVirtIfEntry.setIndexNames((0,_B,_G),(0,_B,_n),(0,_B,_o))
if mibBuilder.loadTexts:fsMIStdOspfVirtIfEntry.setStatus(_A)
_FsMIStdOspfVirtIfAreaId_Type=AreaID
_FsMIStdOspfVirtIfAreaId_Object=MibTableColumn
fsMIStdOspfVirtIfAreaId=_FsMIStdOspfVirtIfAreaId_Object((1,3,6,1,4,1,10876,101,1,146,8,1,1),_FsMIStdOspfVirtIfAreaId_Type())
fsMIStdOspfVirtIfAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfVirtIfAreaId.setStatus(_A)
_FsMIStdOspfVirtIfNeighbor_Type=RouterID
_FsMIStdOspfVirtIfNeighbor_Object=MibTableColumn
fsMIStdOspfVirtIfNeighbor=_FsMIStdOspfVirtIfNeighbor_Object((1,3,6,1,4,1,10876,101,1,146,8,1,2),_FsMIStdOspfVirtIfNeighbor_Type())
fsMIStdOspfVirtIfNeighbor.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfVirtIfNeighbor.setStatus(_A)
class _FsMIStdOspfVirtIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_FsMIStdOspfVirtIfTransitDelay_Type.__name__=_L
_FsMIStdOspfVirtIfTransitDelay_Object=MibTableColumn
fsMIStdOspfVirtIfTransitDelay=_FsMIStdOspfVirtIfTransitDelay_Object((1,3,6,1,4,1,10876,101,1,146,8,1,3),_FsMIStdOspfVirtIfTransitDelay_Type())
fsMIStdOspfVirtIfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfVirtIfTransitDelay.setStatus(_A)
class _FsMIStdOspfVirtIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_FsMIStdOspfVirtIfRetransInterval_Type.__name__=_L
_FsMIStdOspfVirtIfRetransInterval_Object=MibTableColumn
fsMIStdOspfVirtIfRetransInterval=_FsMIStdOspfVirtIfRetransInterval_Object((1,3,6,1,4,1,10876,101,1,146,8,1,4),_FsMIStdOspfVirtIfRetransInterval_Type())
fsMIStdOspfVirtIfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfVirtIfRetransInterval.setStatus(_A)
class _FsMIStdOspfVirtIfHelloInterval_Type(HelloRange):defaultValue=10
_FsMIStdOspfVirtIfHelloInterval_Type.__name__=_R
_FsMIStdOspfVirtIfHelloInterval_Object=MibTableColumn
fsMIStdOspfVirtIfHelloInterval=_FsMIStdOspfVirtIfHelloInterval_Object((1,3,6,1,4,1,10876,101,1,146,8,1,5),_FsMIStdOspfVirtIfHelloInterval_Type())
fsMIStdOspfVirtIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfVirtIfHelloInterval.setStatus(_A)
class _FsMIStdOspfVirtIfRtrDeadInterval_Type(PositiveInteger):defaultValue=60
_FsMIStdOspfVirtIfRtrDeadInterval_Type.__name__=_K
_FsMIStdOspfVirtIfRtrDeadInterval_Object=MibTableColumn
fsMIStdOspfVirtIfRtrDeadInterval=_FsMIStdOspfVirtIfRtrDeadInterval_Object((1,3,6,1,4,1,10876,101,1,146,8,1,6),_FsMIStdOspfVirtIfRtrDeadInterval_Type())
fsMIStdOspfVirtIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfVirtIfRtrDeadInterval.setStatus(_A)
class _FsMIStdOspfVirtIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_N,1),(_P,4)))
_FsMIStdOspfVirtIfState_Type.__name__=_E
_FsMIStdOspfVirtIfState_Object=MibTableColumn
fsMIStdOspfVirtIfState=_FsMIStdOspfVirtIfState_Object((1,3,6,1,4,1,10876,101,1,146,8,1,7),_FsMIStdOspfVirtIfState_Type())
fsMIStdOspfVirtIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfVirtIfState.setStatus(_A)
_FsMIStdOspfVirtIfEvents_Type=Counter32
_FsMIStdOspfVirtIfEvents_Object=MibTableColumn
fsMIStdOspfVirtIfEvents=_FsMIStdOspfVirtIfEvents_Object((1,3,6,1,4,1,10876,101,1,146,8,1,8),_FsMIStdOspfVirtIfEvents_Type())
fsMIStdOspfVirtIfEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfVirtIfEvents.setStatus(_A)
class _FsMIStdOspfVirtIfAuthKey_Type(OctetString):defaultHexValue=_j;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_FsMIStdOspfVirtIfAuthKey_Type.__name__=_J
_FsMIStdOspfVirtIfAuthKey_Object=MibTableColumn
fsMIStdOspfVirtIfAuthKey=_FsMIStdOspfVirtIfAuthKey_Object((1,3,6,1,4,1,10876,101,1,146,8,1,9),_FsMIStdOspfVirtIfAuthKey_Type())
fsMIStdOspfVirtIfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfVirtIfAuthKey.setStatus(_A)
_FsMIStdOspfVirtIfStatus_Type=RowStatus
_FsMIStdOspfVirtIfStatus_Object=MibTableColumn
fsMIStdOspfVirtIfStatus=_FsMIStdOspfVirtIfStatus_Object((1,3,6,1,4,1,10876,101,1,146,8,1,10),_FsMIStdOspfVirtIfStatus_Type())
fsMIStdOspfVirtIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfVirtIfStatus.setStatus(_A)
class _FsMIStdOspfVirtIfAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIStdOspfVirtIfAuthType_Type.__name__=_E
_FsMIStdOspfVirtIfAuthType_Object=MibTableColumn
fsMIStdOspfVirtIfAuthType=_FsMIStdOspfVirtIfAuthType_Object((1,3,6,1,4,1,10876,101,1,146,8,1,11),_FsMIStdOspfVirtIfAuthType_Type())
fsMIStdOspfVirtIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfVirtIfAuthType.setStatus(_A)
class _FsMIStdOspfVirtIfCryptoAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIStdOspfVirtIfCryptoAuthType_Type.__name__=_E
_FsMIStdOspfVirtIfCryptoAuthType_Object=MibTableColumn
fsMIStdOspfVirtIfCryptoAuthType=_FsMIStdOspfVirtIfCryptoAuthType_Object((1,3,6,1,4,1,10876,101,1,146,8,1,12),_FsMIStdOspfVirtIfCryptoAuthType_Type())
fsMIStdOspfVirtIfCryptoAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfVirtIfCryptoAuthType.setStatus(_A)
_FsMIStdOspfNbrTable_Object=MibTable
fsMIStdOspfNbrTable=_FsMIStdOspfNbrTable_Object((1,3,6,1,4,1,10876,101,1,146,9))
if mibBuilder.loadTexts:fsMIStdOspfNbrTable.setStatus(_A)
_FsMIStdOspfNbrEntry_Object=MibTableRow
fsMIStdOspfNbrEntry=_FsMIStdOspfNbrEntry_Object((1,3,6,1,4,1,10876,101,1,146,9,1))
fsMIStdOspfNbrEntry.setIndexNames((0,_B,_G),(0,_B,_p),(0,_B,_q))
if mibBuilder.loadTexts:fsMIStdOspfNbrEntry.setStatus(_A)
_FsMIStdOspfNbrIpAddr_Type=IpAddress
_FsMIStdOspfNbrIpAddr_Object=MibTableColumn
fsMIStdOspfNbrIpAddr=_FsMIStdOspfNbrIpAddr_Object((1,3,6,1,4,1,10876,101,1,146,9,1,1),_FsMIStdOspfNbrIpAddr_Type())
fsMIStdOspfNbrIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfNbrIpAddr.setStatus(_A)
class _FsMIStdOspfNbrAddressLessIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIStdOspfNbrAddressLessIndex_Type.__name__=_E
_FsMIStdOspfNbrAddressLessIndex_Object=MibTableColumn
fsMIStdOspfNbrAddressLessIndex=_FsMIStdOspfNbrAddressLessIndex_Object((1,3,6,1,4,1,10876,101,1,146,9,1,2),_FsMIStdOspfNbrAddressLessIndex_Type())
fsMIStdOspfNbrAddressLessIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfNbrAddressLessIndex.setStatus(_A)
class _FsMIStdOspfNbrRtrId_Type(RouterID):defaultHexValue=_M
_FsMIStdOspfNbrRtrId_Type.__name__=_r
_FsMIStdOspfNbrRtrId_Object=MibTableColumn
fsMIStdOspfNbrRtrId=_FsMIStdOspfNbrRtrId_Object((1,3,6,1,4,1,10876,101,1,146,9,1,3),_FsMIStdOspfNbrRtrId_Type())
fsMIStdOspfNbrRtrId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfNbrRtrId.setStatus(_A)
class _FsMIStdOspfNbrOptions_Type(Integer32):defaultValue=0
_FsMIStdOspfNbrOptions_Type.__name__=_E
_FsMIStdOspfNbrOptions_Object=MibTableColumn
fsMIStdOspfNbrOptions=_FsMIStdOspfNbrOptions_Object((1,3,6,1,4,1,10876,101,1,146,9,1,4),_FsMIStdOspfNbrOptions_Type())
fsMIStdOspfNbrOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfNbrOptions.setStatus(_A)
class _FsMIStdOspfNbrPriority_Type(DesignatedRouterPriority):defaultValue=1
_FsMIStdOspfNbrPriority_Type.__name__=_Q
_FsMIStdOspfNbrPriority_Object=MibTableColumn
fsMIStdOspfNbrPriority=_FsMIStdOspfNbrPriority_Object((1,3,6,1,4,1,10876,101,1,146,9,1,5),_FsMIStdOspfNbrPriority_Type())
fsMIStdOspfNbrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfNbrPriority.setStatus(_A)
class _FsMIStdOspfNbrState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_N,1),(_s,2),('init',3),(_t,4),(_u,5),(_v,6),(_w,7),('full',8)))
_FsMIStdOspfNbrState_Type.__name__=_E
_FsMIStdOspfNbrState_Object=MibTableColumn
fsMIStdOspfNbrState=_FsMIStdOspfNbrState_Object((1,3,6,1,4,1,10876,101,1,146,9,1,6),_FsMIStdOspfNbrState_Type())
fsMIStdOspfNbrState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfNbrState.setStatus(_A)
_FsMIStdOspfNbrEvents_Type=Counter32
_FsMIStdOspfNbrEvents_Object=MibTableColumn
fsMIStdOspfNbrEvents=_FsMIStdOspfNbrEvents_Object((1,3,6,1,4,1,10876,101,1,146,9,1,7),_FsMIStdOspfNbrEvents_Type())
fsMIStdOspfNbrEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfNbrEvents.setStatus(_A)
_FsMIStdOspfNbrLsRetransQLen_Type=Gauge32
_FsMIStdOspfNbrLsRetransQLen_Object=MibTableColumn
fsMIStdOspfNbrLsRetransQLen=_FsMIStdOspfNbrLsRetransQLen_Object((1,3,6,1,4,1,10876,101,1,146,9,1,8),_FsMIStdOspfNbrLsRetransQLen_Type())
fsMIStdOspfNbrLsRetransQLen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfNbrLsRetransQLen.setStatus(_A)
_FsMIStdOspfNbmaNbrStatus_Type=RowStatus
_FsMIStdOspfNbmaNbrStatus_Object=MibTableColumn
fsMIStdOspfNbmaNbrStatus=_FsMIStdOspfNbmaNbrStatus_Object((1,3,6,1,4,1,10876,101,1,146,9,1,9),_FsMIStdOspfNbmaNbrStatus_Type())
fsMIStdOspfNbmaNbrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfNbmaNbrStatus.setStatus(_A)
class _FsMIStdOspfNbmaNbrPermanence_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('permanent',2)))
_FsMIStdOspfNbmaNbrPermanence_Type.__name__=_E
_FsMIStdOspfNbmaNbrPermanence_Object=MibTableColumn
fsMIStdOspfNbmaNbrPermanence=_FsMIStdOspfNbmaNbrPermanence_Object((1,3,6,1,4,1,10876,101,1,146,9,1,10),_FsMIStdOspfNbmaNbrPermanence_Type())
fsMIStdOspfNbmaNbrPermanence.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfNbmaNbrPermanence.setStatus(_A)
_FsMIStdOspfNbrHelloSuppressed_Type=TruthValue
_FsMIStdOspfNbrHelloSuppressed_Object=MibTableColumn
fsMIStdOspfNbrHelloSuppressed=_FsMIStdOspfNbrHelloSuppressed_Object((1,3,6,1,4,1,10876,101,1,146,9,1,11),_FsMIStdOspfNbrHelloSuppressed_Type())
fsMIStdOspfNbrHelloSuppressed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfNbrHelloSuppressed.setStatus(_A)
_FsMIStdOspfVirtNbrTable_Object=MibTable
fsMIStdOspfVirtNbrTable=_FsMIStdOspfVirtNbrTable_Object((1,3,6,1,4,1,10876,101,1,146,10))
if mibBuilder.loadTexts:fsMIStdOspfVirtNbrTable.setStatus(_A)
_FsMIStdOspfVirtNbrEntry_Object=MibTableRow
fsMIStdOspfVirtNbrEntry=_FsMIStdOspfVirtNbrEntry_Object((1,3,6,1,4,1,10876,101,1,146,10,1))
fsMIStdOspfVirtNbrEntry.setIndexNames((0,_B,_G),(0,_B,_x),(0,_B,_y))
if mibBuilder.loadTexts:fsMIStdOspfVirtNbrEntry.setStatus(_A)
_FsMIStdOspfVirtNbrArea_Type=AreaID
_FsMIStdOspfVirtNbrArea_Object=MibTableColumn
fsMIStdOspfVirtNbrArea=_FsMIStdOspfVirtNbrArea_Object((1,3,6,1,4,1,10876,101,1,146,10,1,1),_FsMIStdOspfVirtNbrArea_Type())
fsMIStdOspfVirtNbrArea.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfVirtNbrArea.setStatus(_A)
_FsMIStdOspfVirtNbrRtrId_Type=RouterID
_FsMIStdOspfVirtNbrRtrId_Object=MibTableColumn
fsMIStdOspfVirtNbrRtrId=_FsMIStdOspfVirtNbrRtrId_Object((1,3,6,1,4,1,10876,101,1,146,10,1,2),_FsMIStdOspfVirtNbrRtrId_Type())
fsMIStdOspfVirtNbrRtrId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfVirtNbrRtrId.setStatus(_A)
_FsMIStdOspfVirtNbrIpAddr_Type=IpAddress
_FsMIStdOspfVirtNbrIpAddr_Object=MibTableColumn
fsMIStdOspfVirtNbrIpAddr=_FsMIStdOspfVirtNbrIpAddr_Object((1,3,6,1,4,1,10876,101,1,146,10,1,3),_FsMIStdOspfVirtNbrIpAddr_Type())
fsMIStdOspfVirtNbrIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfVirtNbrIpAddr.setStatus(_A)
_FsMIStdOspfVirtNbrOptions_Type=Integer32
_FsMIStdOspfVirtNbrOptions_Object=MibTableColumn
fsMIStdOspfVirtNbrOptions=_FsMIStdOspfVirtNbrOptions_Object((1,3,6,1,4,1,10876,101,1,146,10,1,4),_FsMIStdOspfVirtNbrOptions_Type())
fsMIStdOspfVirtNbrOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfVirtNbrOptions.setStatus(_A)
class _FsMIStdOspfVirtNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_N,1),(_s,2),('init',3),(_t,4),(_u,5),(_v,6),(_w,7),('full',8)))
_FsMIStdOspfVirtNbrState_Type.__name__=_E
_FsMIStdOspfVirtNbrState_Object=MibTableColumn
fsMIStdOspfVirtNbrState=_FsMIStdOspfVirtNbrState_Object((1,3,6,1,4,1,10876,101,1,146,10,1,5),_FsMIStdOspfVirtNbrState_Type())
fsMIStdOspfVirtNbrState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfVirtNbrState.setStatus(_A)
_FsMIStdOspfVirtNbrEvents_Type=Counter32
_FsMIStdOspfVirtNbrEvents_Object=MibTableColumn
fsMIStdOspfVirtNbrEvents=_FsMIStdOspfVirtNbrEvents_Object((1,3,6,1,4,1,10876,101,1,146,10,1,6),_FsMIStdOspfVirtNbrEvents_Type())
fsMIStdOspfVirtNbrEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfVirtNbrEvents.setStatus(_A)
_FsMIStdOspfVirtNbrLsRetransQLen_Type=Gauge32
_FsMIStdOspfVirtNbrLsRetransQLen_Object=MibTableColumn
fsMIStdOspfVirtNbrLsRetransQLen=_FsMIStdOspfVirtNbrLsRetransQLen_Object((1,3,6,1,4,1,10876,101,1,146,10,1,7),_FsMIStdOspfVirtNbrLsRetransQLen_Type())
fsMIStdOspfVirtNbrLsRetransQLen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfVirtNbrLsRetransQLen.setStatus(_A)
_FsMIStdOspfVirtNbrHelloSuppressed_Type=TruthValue
_FsMIStdOspfVirtNbrHelloSuppressed_Object=MibTableColumn
fsMIStdOspfVirtNbrHelloSuppressed=_FsMIStdOspfVirtNbrHelloSuppressed_Object((1,3,6,1,4,1,10876,101,1,146,10,1,8),_FsMIStdOspfVirtNbrHelloSuppressed_Type())
fsMIStdOspfVirtNbrHelloSuppressed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfVirtNbrHelloSuppressed.setStatus(_A)
_FsMIStdOspfExtLsdbTable_Object=MibTable
fsMIStdOspfExtLsdbTable=_FsMIStdOspfExtLsdbTable_Object((1,3,6,1,4,1,10876,101,1,146,11))
if mibBuilder.loadTexts:fsMIStdOspfExtLsdbTable.setStatus(_A)
_FsMIStdOspfExtLsdbEntry_Object=MibTableRow
fsMIStdOspfExtLsdbEntry=_FsMIStdOspfExtLsdbEntry_Object((1,3,6,1,4,1,10876,101,1,146,11,1))
fsMIStdOspfExtLsdbEntry.setIndexNames((0,_B,_G),(0,_B,_z),(0,_B,_A0),(0,_B,_A1))
if mibBuilder.loadTexts:fsMIStdOspfExtLsdbEntry.setStatus(_A)
class _FsMIStdOspfExtLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues((_b,5))
_FsMIStdOspfExtLsdbType_Type.__name__=_E
_FsMIStdOspfExtLsdbType_Object=MibTableColumn
fsMIStdOspfExtLsdbType=_FsMIStdOspfExtLsdbType_Object((1,3,6,1,4,1,10876,101,1,146,11,1,1),_FsMIStdOspfExtLsdbType_Type())
fsMIStdOspfExtLsdbType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfExtLsdbType.setStatus(_A)
_FsMIStdOspfExtLsdbLsid_Type=IpAddress
_FsMIStdOspfExtLsdbLsid_Object=MibTableColumn
fsMIStdOspfExtLsdbLsid=_FsMIStdOspfExtLsdbLsid_Object((1,3,6,1,4,1,10876,101,1,146,11,1,2),_FsMIStdOspfExtLsdbLsid_Type())
fsMIStdOspfExtLsdbLsid.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfExtLsdbLsid.setStatus(_A)
_FsMIStdOspfExtLsdbRouterId_Type=RouterID
_FsMIStdOspfExtLsdbRouterId_Object=MibTableColumn
fsMIStdOspfExtLsdbRouterId=_FsMIStdOspfExtLsdbRouterId_Object((1,3,6,1,4,1,10876,101,1,146,11,1,3),_FsMIStdOspfExtLsdbRouterId_Type())
fsMIStdOspfExtLsdbRouterId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfExtLsdbRouterId.setStatus(_A)
_FsMIStdOspfExtLsdbSequence_Type=Integer32
_FsMIStdOspfExtLsdbSequence_Object=MibTableColumn
fsMIStdOspfExtLsdbSequence=_FsMIStdOspfExtLsdbSequence_Object((1,3,6,1,4,1,10876,101,1,146,11,1,4),_FsMIStdOspfExtLsdbSequence_Type())
fsMIStdOspfExtLsdbSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfExtLsdbSequence.setStatus(_A)
_FsMIStdOspfExtLsdbAge_Type=Integer32
_FsMIStdOspfExtLsdbAge_Object=MibTableColumn
fsMIStdOspfExtLsdbAge=_FsMIStdOspfExtLsdbAge_Object((1,3,6,1,4,1,10876,101,1,146,11,1,5),_FsMIStdOspfExtLsdbAge_Type())
fsMIStdOspfExtLsdbAge.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfExtLsdbAge.setStatus(_A)
_FsMIStdOspfExtLsdbChecksum_Type=Integer32
_FsMIStdOspfExtLsdbChecksum_Object=MibTableColumn
fsMIStdOspfExtLsdbChecksum=_FsMIStdOspfExtLsdbChecksum_Object((1,3,6,1,4,1,10876,101,1,146,11,1,6),_FsMIStdOspfExtLsdbChecksum_Type())
fsMIStdOspfExtLsdbChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfExtLsdbChecksum.setStatus(_A)
class _FsMIStdOspfExtLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(36,36));fixedLength=36
_FsMIStdOspfExtLsdbAdvertisement_Type.__name__=_J
_FsMIStdOspfExtLsdbAdvertisement_Object=MibTableColumn
fsMIStdOspfExtLsdbAdvertisement=_FsMIStdOspfExtLsdbAdvertisement_Object((1,3,6,1,4,1,10876,101,1,146,11,1,7),_FsMIStdOspfExtLsdbAdvertisement_Type())
fsMIStdOspfExtLsdbAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdOspfExtLsdbAdvertisement.setStatus(_A)
_FsMIStdOspfRouteGroup_ObjectIdentity=ObjectIdentity
fsMIStdOspfRouteGroup=_FsMIStdOspfRouteGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,146,12))
_FsMIStdOspfIntraArea_ObjectIdentity=ObjectIdentity
fsMIStdOspfIntraArea=_FsMIStdOspfIntraArea_ObjectIdentity((1,3,6,1,4,1,10876,101,1,146,12,1))
_FsMIStdOspfInterArea_ObjectIdentity=ObjectIdentity
fsMIStdOspfInterArea=_FsMIStdOspfInterArea_ObjectIdentity((1,3,6,1,4,1,10876,101,1,146,12,2))
_FsMIStdOspfExternalType1_ObjectIdentity=ObjectIdentity
fsMIStdOspfExternalType1=_FsMIStdOspfExternalType1_ObjectIdentity((1,3,6,1,4,1,10876,101,1,146,12,3))
_FsMIStdOspfExternalType2_ObjectIdentity=ObjectIdentity
fsMIStdOspfExternalType2=_FsMIStdOspfExternalType2_ObjectIdentity((1,3,6,1,4,1,10876,101,1,146,12,4))
_FsMIStdOspfAreaAggregateTable_Object=MibTable
fsMIStdOspfAreaAggregateTable=_FsMIStdOspfAreaAggregateTable_Object((1,3,6,1,4,1,10876,101,1,146,13))
if mibBuilder.loadTexts:fsMIStdOspfAreaAggregateTable.setStatus(_A)
_FsMIStdOspfAreaAggregateEntry_Object=MibTableRow
fsMIStdOspfAreaAggregateEntry=_FsMIStdOspfAreaAggregateEntry_Object((1,3,6,1,4,1,10876,101,1,146,13,1))
fsMIStdOspfAreaAggregateEntry.setIndexNames((0,_B,_G),(0,_B,_A2),(0,_B,_A3),(0,_B,_A4),(0,_B,_A5))
if mibBuilder.loadTexts:fsMIStdOspfAreaAggregateEntry.setStatus(_A)
_FsMIStdOspfAreaAggregateAreaID_Type=AreaID
_FsMIStdOspfAreaAggregateAreaID_Object=MibTableColumn
fsMIStdOspfAreaAggregateAreaID=_FsMIStdOspfAreaAggregateAreaID_Object((1,3,6,1,4,1,10876,101,1,146,13,1,1),_FsMIStdOspfAreaAggregateAreaID_Type())
fsMIStdOspfAreaAggregateAreaID.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfAreaAggregateAreaID.setStatus(_A)
class _FsMIStdOspfAreaAggregateLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,7)));namedValues=NamedValues(*((_a,3),(_c,7)))
_FsMIStdOspfAreaAggregateLsdbType_Type.__name__=_E
_FsMIStdOspfAreaAggregateLsdbType_Object=MibTableColumn
fsMIStdOspfAreaAggregateLsdbType=_FsMIStdOspfAreaAggregateLsdbType_Object((1,3,6,1,4,1,10876,101,1,146,13,1,2),_FsMIStdOspfAreaAggregateLsdbType_Type())
fsMIStdOspfAreaAggregateLsdbType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfAreaAggregateLsdbType.setStatus(_A)
_FsMIStdOspfAreaAggregateNet_Type=IpAddress
_FsMIStdOspfAreaAggregateNet_Object=MibTableColumn
fsMIStdOspfAreaAggregateNet=_FsMIStdOspfAreaAggregateNet_Object((1,3,6,1,4,1,10876,101,1,146,13,1,3),_FsMIStdOspfAreaAggregateNet_Type())
fsMIStdOspfAreaAggregateNet.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfAreaAggregateNet.setStatus(_A)
_FsMIStdOspfAreaAggregateMask_Type=IpAddress
_FsMIStdOspfAreaAggregateMask_Object=MibTableColumn
fsMIStdOspfAreaAggregateMask=_FsMIStdOspfAreaAggregateMask_Object((1,3,6,1,4,1,10876,101,1,146,13,1,4),_FsMIStdOspfAreaAggregateMask_Type())
fsMIStdOspfAreaAggregateMask.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIStdOspfAreaAggregateMask.setStatus(_A)
_FsMIStdOspfAreaAggregateStatus_Type=RowStatus
_FsMIStdOspfAreaAggregateStatus_Object=MibTableColumn
fsMIStdOspfAreaAggregateStatus=_FsMIStdOspfAreaAggregateStatus_Object((1,3,6,1,4,1,10876,101,1,146,13,1,5),_FsMIStdOspfAreaAggregateStatus_Type())
fsMIStdOspfAreaAggregateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfAreaAggregateStatus.setStatus(_A)
class _FsMIStdOspfAreaAggregateEffect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('advertiseMatching',1),('doNotAdvertiseMatching',2)))
_FsMIStdOspfAreaAggregateEffect_Type.__name__=_E
_FsMIStdOspfAreaAggregateEffect_Object=MibTableColumn
fsMIStdOspfAreaAggregateEffect=_FsMIStdOspfAreaAggregateEffect_Object((1,3,6,1,4,1,10876,101,1,146,13,1,6),_FsMIStdOspfAreaAggregateEffect_Type())
fsMIStdOspfAreaAggregateEffect.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIStdOspfAreaAggregateEffect.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_h:AreaID,_r:RouterID,'Metric':Metric,'BigMetric':BigMetric,_i:Status,_K:PositiveInteger,_R:HelloRange,_L:UpToMaxAge,_Q:DesignatedRouterPriority,'TOSType':TOSType,'fsMIStdOspf':fsMIStdOspf,'fsMIStdOspfGeneralGroup':fsMIStdOspfGeneralGroup,'fsMIStdOspfTable':fsMIStdOspfTable,'fsMIStdOspfEntry':fsMIStdOspfEntry,_G:fsMIStdOspfContextId,'fsMIStdOspfRouterId':fsMIStdOspfRouterId,'fsMIStdOspfAdminStat':fsMIStdOspfAdminStat,'fsMIStdOspfVersionNumber':fsMIStdOspfVersionNumber,'fsMIStdOspfAreaBdrRtrStatus':fsMIStdOspfAreaBdrRtrStatus,'fsMIStdOspfASBdrRtrStatus':fsMIStdOspfASBdrRtrStatus,'fsMIStdOspfExternLsaCount':fsMIStdOspfExternLsaCount,'fsMIStdOspfExternLsaCksumSum':fsMIStdOspfExternLsaCksumSum,'fsMIStdOspfTOSSupport':fsMIStdOspfTOSSupport,'fsMIStdOspfOriginateNewLsas':fsMIStdOspfOriginateNewLsas,'fsMIStdOspfRxNewLsas':fsMIStdOspfRxNewLsas,'fsMIStdOspfExtLsdbLimit':fsMIStdOspfExtLsdbLimit,'fsMIStdOspfMulticastExtensions':fsMIStdOspfMulticastExtensions,'fsMIStdOspfExitOverflowInterval':fsMIStdOspfExitOverflowInterval,'fsMIStdOspfDemandExtensions':fsMIStdOspfDemandExtensions,'fsMIStdOspfStatus':fsMIStdOspfStatus,'fsMIStdOspfAreaTable':fsMIStdOspfAreaTable,'fsMIStdOspfAreaEntry':fsMIStdOspfAreaEntry,_T:fsMIStdOspfAreaId,'fsMIStdOspfImportAsExtern':fsMIStdOspfImportAsExtern,'fsMIStdOspfSpfRuns':fsMIStdOspfSpfRuns,'fsMIStdOspfAreaBdrRtrCount':fsMIStdOspfAreaBdrRtrCount,'fsMIStdOspfAsBdrRtrCount':fsMIStdOspfAsBdrRtrCount,'fsMIStdOspfAreaLsaCount':fsMIStdOspfAreaLsaCount,'fsMIStdOspfAreaLsaCksumSum':fsMIStdOspfAreaLsaCksumSum,'fsMIStdOspfAreaSummary':fsMIStdOspfAreaSummary,'fsMIStdOspfAreaStatus':fsMIStdOspfAreaStatus,'fsMIStdOspfStubAreaTable':fsMIStdOspfStubAreaTable,'fsMIStdOspfStubAreaEntry':fsMIStdOspfStubAreaEntry,_U:fsMIStdOspfStubAreaId,_V:fsMIStdOspfStubTOS,'fsMIStdOspfStubMetric':fsMIStdOspfStubMetric,'fsMIStdOspfStubStatus':fsMIStdOspfStubStatus,'fsMIStdOspfStubMetricType':fsMIStdOspfStubMetricType,'fsMIStdOspfLsdbTable':fsMIStdOspfLsdbTable,'fsMIStdOspfLsdbEntry':fsMIStdOspfLsdbEntry,_W:fsMIStdOspfLsdbAreaId,_X:fsMIStdOspfLsdbType,_Y:fsMIStdOspfLsdbLsid,_Z:fsMIStdOspfLsdbRouterId,'fsMIStdOspfLsdbSequence':fsMIStdOspfLsdbSequence,'fsMIStdOspfLsdbAge':fsMIStdOspfLsdbAge,'fsMIStdOspfLsdbChecksum':fsMIStdOspfLsdbChecksum,'fsMIStdOspfLsdbAdvertisement':fsMIStdOspfLsdbAdvertisement,'fsMIStdOspfHostTable':fsMIStdOspfHostTable,'fsMIStdOspfHostEntry':fsMIStdOspfHostEntry,_d:fsMIStdOspfHostIpAddress,_e:fsMIStdOspfHostTOS,'fsMIStdOspfHostMetric':fsMIStdOspfHostMetric,'fsMIStdOspfHostStatus':fsMIStdOspfHostStatus,'fsMIStdOspfHostAreaID':fsMIStdOspfHostAreaID,'fsMIStdOspfIfTable':fsMIStdOspfIfTable,'fsMIStdOspfIfEntry':fsMIStdOspfIfEntry,_f:fsMIStdOspfIfIpAddress,_g:fsMIStdOspfAddressLessIf,'fsMIStdOspfIfAreaId':fsMIStdOspfIfAreaId,'fsMIStdOspfIfType':fsMIStdOspfIfType,'fsMIStdOspfIfAdminStat':fsMIStdOspfIfAdminStat,'fsMIStdOspfIfRtrPriority':fsMIStdOspfIfRtrPriority,'fsMIStdOspfIfTransitDelay':fsMIStdOspfIfTransitDelay,'fsMIStdOspfIfRetransInterval':fsMIStdOspfIfRetransInterval,'fsMIStdOspfIfHelloInterval':fsMIStdOspfIfHelloInterval,'fsMIStdOspfIfRtrDeadInterval':fsMIStdOspfIfRtrDeadInterval,'fsMIStdOspfIfPollInterval':fsMIStdOspfIfPollInterval,'fsMIStdOspfIfState':fsMIStdOspfIfState,'fsMIStdOspfIfDesignatedRouter':fsMIStdOspfIfDesignatedRouter,'fsMIStdOspfIfBackupDesignatedRouter':fsMIStdOspfIfBackupDesignatedRouter,'fsMIStdOspfIfEvents':fsMIStdOspfIfEvents,'fsMIStdOspfIfAuthKey':fsMIStdOspfIfAuthKey,'fsMIStdOspfIfStatus':fsMIStdOspfIfStatus,'fsMIStdOspfIfMulticastForwarding':fsMIStdOspfIfMulticastForwarding,'fsMIStdOspfIfDemand':fsMIStdOspfIfDemand,'fsMIStdOspfIfAuthType':fsMIStdOspfIfAuthType,'fsMIStdOspfIfCryptoAuthType':fsMIStdOspfIfCryptoAuthType,'fsMIStdOspfIfMetricTable':fsMIStdOspfIfMetricTable,'fsMIStdOspfIfMetricEntry':fsMIStdOspfIfMetricEntry,_k:fsMIStdOspfIfMetricIpAddress,_l:fsMIStdOspfIfMetricAddressLessIf,_m:fsMIStdOspfIfMetricTOS,'fsMIStdOspfIfMetricValue':fsMIStdOspfIfMetricValue,'fsMIStdOspfIfMetricStatus':fsMIStdOspfIfMetricStatus,'fsMIStdOspfVirtIfTable':fsMIStdOspfVirtIfTable,'fsMIStdOspfVirtIfEntry':fsMIStdOspfVirtIfEntry,_n:fsMIStdOspfVirtIfAreaId,_o:fsMIStdOspfVirtIfNeighbor,'fsMIStdOspfVirtIfTransitDelay':fsMIStdOspfVirtIfTransitDelay,'fsMIStdOspfVirtIfRetransInterval':fsMIStdOspfVirtIfRetransInterval,'fsMIStdOspfVirtIfHelloInterval':fsMIStdOspfVirtIfHelloInterval,'fsMIStdOspfVirtIfRtrDeadInterval':fsMIStdOspfVirtIfRtrDeadInterval,'fsMIStdOspfVirtIfState':fsMIStdOspfVirtIfState,'fsMIStdOspfVirtIfEvents':fsMIStdOspfVirtIfEvents,'fsMIStdOspfVirtIfAuthKey':fsMIStdOspfVirtIfAuthKey,'fsMIStdOspfVirtIfStatus':fsMIStdOspfVirtIfStatus,'fsMIStdOspfVirtIfAuthType':fsMIStdOspfVirtIfAuthType,'fsMIStdOspfVirtIfCryptoAuthType':fsMIStdOspfVirtIfCryptoAuthType,'fsMIStdOspfNbrTable':fsMIStdOspfNbrTable,'fsMIStdOspfNbrEntry':fsMIStdOspfNbrEntry,_p:fsMIStdOspfNbrIpAddr,_q:fsMIStdOspfNbrAddressLessIndex,'fsMIStdOspfNbrRtrId':fsMIStdOspfNbrRtrId,'fsMIStdOspfNbrOptions':fsMIStdOspfNbrOptions,'fsMIStdOspfNbrPriority':fsMIStdOspfNbrPriority,'fsMIStdOspfNbrState':fsMIStdOspfNbrState,'fsMIStdOspfNbrEvents':fsMIStdOspfNbrEvents,'fsMIStdOspfNbrLsRetransQLen':fsMIStdOspfNbrLsRetransQLen,'fsMIStdOspfNbmaNbrStatus':fsMIStdOspfNbmaNbrStatus,'fsMIStdOspfNbmaNbrPermanence':fsMIStdOspfNbmaNbrPermanence,'fsMIStdOspfNbrHelloSuppressed':fsMIStdOspfNbrHelloSuppressed,'fsMIStdOspfVirtNbrTable':fsMIStdOspfVirtNbrTable,'fsMIStdOspfVirtNbrEntry':fsMIStdOspfVirtNbrEntry,_x:fsMIStdOspfVirtNbrArea,_y:fsMIStdOspfVirtNbrRtrId,'fsMIStdOspfVirtNbrIpAddr':fsMIStdOspfVirtNbrIpAddr,'fsMIStdOspfVirtNbrOptions':fsMIStdOspfVirtNbrOptions,'fsMIStdOspfVirtNbrState':fsMIStdOspfVirtNbrState,'fsMIStdOspfVirtNbrEvents':fsMIStdOspfVirtNbrEvents,'fsMIStdOspfVirtNbrLsRetransQLen':fsMIStdOspfVirtNbrLsRetransQLen,'fsMIStdOspfVirtNbrHelloSuppressed':fsMIStdOspfVirtNbrHelloSuppressed,'fsMIStdOspfExtLsdbTable':fsMIStdOspfExtLsdbTable,'fsMIStdOspfExtLsdbEntry':fsMIStdOspfExtLsdbEntry,_z:fsMIStdOspfExtLsdbType,_A0:fsMIStdOspfExtLsdbLsid,_A1:fsMIStdOspfExtLsdbRouterId,'fsMIStdOspfExtLsdbSequence':fsMIStdOspfExtLsdbSequence,'fsMIStdOspfExtLsdbAge':fsMIStdOspfExtLsdbAge,'fsMIStdOspfExtLsdbChecksum':fsMIStdOspfExtLsdbChecksum,'fsMIStdOspfExtLsdbAdvertisement':fsMIStdOspfExtLsdbAdvertisement,'fsMIStdOspfRouteGroup':fsMIStdOspfRouteGroup,'fsMIStdOspfIntraArea':fsMIStdOspfIntraArea,'fsMIStdOspfInterArea':fsMIStdOspfInterArea,'fsMIStdOspfExternalType1':fsMIStdOspfExternalType1,'fsMIStdOspfExternalType2':fsMIStdOspfExternalType2,'fsMIStdOspfAreaAggregateTable':fsMIStdOspfAreaAggregateTable,'fsMIStdOspfAreaAggregateEntry':fsMIStdOspfAreaAggregateEntry,_A2:fsMIStdOspfAreaAggregateAreaID,_A3:fsMIStdOspfAreaAggregateLsdbType,_A4:fsMIStdOspfAreaAggregateNet,_A5:fsMIStdOspfAreaAggregateMask,'fsMIStdOspfAreaAggregateStatus':fsMIStdOspfAreaAggregateStatus,'fsMIStdOspfAreaAggregateEffect':fsMIStdOspfAreaAggregateEffect})