_AB='nsVrOspfAreaAggregateMask'
_AA='nsVrOspfAreaAggregateNet'
_A9='nsVrOspfAreaAggregateLsdbType'
_A8='nsVrOspfAreaAggregateAreaID'
_A7='nsVrOspfAreaAggregateVRID'
_A6='nsVrOspfExtLsdbRouterId'
_A5='nsVrOspfExtLsdbLsid'
_A4='nsVrOspfExtLsdbType'
_A3='nsVrOspfExtLsdbVRID'
_A2='nsVrOspfVirtNbrRtrId'
_A1='nsVrOspfVirtNbrArea'
_A0='nsVrOspfVirtNbrVRID'
_z='exchangeStart'
_y='twoWay'
_x='attempt'
_w='RouterID'
_v='nsVrOspfNbrAddressLessIndex'
_u='nsVrOspfNbrIpAddr'
_t='nsVrOspfNbrVRID'
_s='nsVrOspfVirtIfNeighbor'
_r='nsVrOspfVirtIfAreaId'
_q='nsVrOspfVirtIfVRID'
_p='nsVrOspfIfMetricTOS'
_o='nsVrOspfIfMetricAddressLessIf'
_n='nsVrOspfIfMetricIpAddress'
_m='0000000000000000'
_l='Status'
_k='AreaID'
_j='nsVrOspfAddressLessIf'
_i='nsVrOspfIfIpAddress'
_h='nsVrOspfIfVRID'
_g='nsVrOspfHostTOS'
_f='nsVrOspfHostIpAddress'
_e='nsVrOspfHostVRID'
_d='nssaExternalLink'
_c='asExternalLink'
_b='summaryLink'
_a='nsVrOspfLsdbRouterId'
_Z='nsVrOspfLsdbLsid'
_Y='nsVrOspfLsdbType'
_X='nsVrOspfLsdbAreaId'
_W='nsVrOspfLsdbVRID'
_V='nsVrOspfStubTOS'
_U='nsVrOspfStubAreaId'
_T='nsVrOspfStubVRID'
_S='nsVrOspfAreaId'
_R='nsVrOspfAreaVRID'
_Q='nsVrOspfGeneralVRID'
_P='TruthValue'
_O='nsVrOspfIfMetricVRID'
_N='HelloRange'
_M='DesignatedRouterPriority'
_L='pointToPoint'
_K='IpAddress'
_J='down'
_I='00000000'
_H='UpToMaxAge'
_G='PositiveInteger'
_F='OctetString'
_E='Integer32'
_D='read-create'
_C='NETSCREEN-VR-OSPF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVR,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVR')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,_K,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_P)
nsVrOspf=ModuleIdentity((1,3,6,1,4,1,3224,18,5))
class AreaID(TextualConvention,IpAddress):status=_A
class RouterID(TextualConvention,IpAddress):status=_A
class Metric(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class BigMetric(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
class Status(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
class PositiveInteger(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class HelloRange(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class UpToMaxAge(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
class InterfaceIndex(TextualConvention,Integer32):status=_A
class DesignatedRouterPriority(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class TOSType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_NsVrOspfGeneralTable_Object=MibTable
nsVrOspfGeneralTable=_NsVrOspfGeneralTable_Object((1,3,6,1,4,1,3224,18,5,1))
if mibBuilder.loadTexts:nsVrOspfGeneralTable.setStatus(_A)
_NsVrOspfGeneralEntry_Object=MibTableRow
nsVrOspfGeneralEntry=_NsVrOspfGeneralEntry_Object((1,3,6,1,4,1,3224,18,5,1,1))
nsVrOspfGeneralEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:nsVrOspfGeneralEntry.setStatus(_A)
_NsVrOspfRouterId_Type=RouterID
_NsVrOspfRouterId_Object=MibTableColumn
nsVrOspfRouterId=_NsVrOspfRouterId_Object((1,3,6,1,4,1,3224,18,5,1,1,1),_NsVrOspfRouterId_Type())
nsVrOspfRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfRouterId.setStatus(_A)
_NsVrOspfAdminStat_Type=Status
_NsVrOspfAdminStat_Object=MibTableColumn
nsVrOspfAdminStat=_NsVrOspfAdminStat_Object((1,3,6,1,4,1,3224,18,5,1,1,2),_NsVrOspfAdminStat_Type())
nsVrOspfAdminStat.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAdminStat.setStatus(_A)
class _NsVrOspfVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('version2',2))
_NsVrOspfVersionNumber_Type.__name__=_E
_NsVrOspfVersionNumber_Object=MibTableColumn
nsVrOspfVersionNumber=_NsVrOspfVersionNumber_Object((1,3,6,1,4,1,3224,18,5,1,1,3),_NsVrOspfVersionNumber_Type())
nsVrOspfVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVersionNumber.setStatus(_A)
_NsVrOspfAreaBdrRtrStatus_Type=TruthValue
_NsVrOspfAreaBdrRtrStatus_Object=MibTableColumn
nsVrOspfAreaBdrRtrStatus=_NsVrOspfAreaBdrRtrStatus_Object((1,3,6,1,4,1,3224,18,5,1,1,4),_NsVrOspfAreaBdrRtrStatus_Type())
nsVrOspfAreaBdrRtrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAreaBdrRtrStatus.setStatus(_A)
_NsVrOspfASBdrRtrStatus_Type=TruthValue
_NsVrOspfASBdrRtrStatus_Object=MibTableColumn
nsVrOspfASBdrRtrStatus=_NsVrOspfASBdrRtrStatus_Object((1,3,6,1,4,1,3224,18,5,1,1,5),_NsVrOspfASBdrRtrStatus_Type())
nsVrOspfASBdrRtrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfASBdrRtrStatus.setStatus(_A)
_NsVrOspfExternLsaCount_Type=Gauge32
_NsVrOspfExternLsaCount_Object=MibTableColumn
nsVrOspfExternLsaCount=_NsVrOspfExternLsaCount_Object((1,3,6,1,4,1,3224,18,5,1,1,6),_NsVrOspfExternLsaCount_Type())
nsVrOspfExternLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfExternLsaCount.setStatus(_A)
_NsVrOspfExternLsaCksumSum_Type=Integer32
_NsVrOspfExternLsaCksumSum_Object=MibTableColumn
nsVrOspfExternLsaCksumSum=_NsVrOspfExternLsaCksumSum_Object((1,3,6,1,4,1,3224,18,5,1,1,7),_NsVrOspfExternLsaCksumSum_Type())
nsVrOspfExternLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfExternLsaCksumSum.setStatus(_A)
_NsVrOspfTOSSupport_Type=TruthValue
_NsVrOspfTOSSupport_Object=MibTableColumn
nsVrOspfTOSSupport=_NsVrOspfTOSSupport_Object((1,3,6,1,4,1,3224,18,5,1,1,8),_NsVrOspfTOSSupport_Type())
nsVrOspfTOSSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfTOSSupport.setStatus(_A)
_NsVrOspfOriginateNewLsas_Type=Counter32
_NsVrOspfOriginateNewLsas_Object=MibTableColumn
nsVrOspfOriginateNewLsas=_NsVrOspfOriginateNewLsas_Object((1,3,6,1,4,1,3224,18,5,1,1,9),_NsVrOspfOriginateNewLsas_Type())
nsVrOspfOriginateNewLsas.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfOriginateNewLsas.setStatus(_A)
_NsVrOspfRxNewLsas_Type=Counter32
_NsVrOspfRxNewLsas_Object=MibTableColumn
nsVrOspfRxNewLsas=_NsVrOspfRxNewLsas_Object((1,3,6,1,4,1,3224,18,5,1,1,10),_NsVrOspfRxNewLsas_Type())
nsVrOspfRxNewLsas.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfRxNewLsas.setStatus(_A)
class _NsVrOspfExtLsdbLimit_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_NsVrOspfExtLsdbLimit_Type.__name__=_E
_NsVrOspfExtLsdbLimit_Object=MibTableColumn
nsVrOspfExtLsdbLimit=_NsVrOspfExtLsdbLimit_Object((1,3,6,1,4,1,3224,18,5,1,1,11),_NsVrOspfExtLsdbLimit_Type())
nsVrOspfExtLsdbLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfExtLsdbLimit.setStatus(_A)
class _NsVrOspfMulticastExtensions_Type(Integer32):defaultValue=0
_NsVrOspfMulticastExtensions_Type.__name__=_E
_NsVrOspfMulticastExtensions_Object=MibTableColumn
nsVrOspfMulticastExtensions=_NsVrOspfMulticastExtensions_Object((1,3,6,1,4,1,3224,18,5,1,1,12),_NsVrOspfMulticastExtensions_Type())
nsVrOspfMulticastExtensions.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfMulticastExtensions.setStatus(_A)
class _NsVrOspfExitOverflowInterval_Type(PositiveInteger):defaultValue=0
_NsVrOspfExitOverflowInterval_Type.__name__=_G
_NsVrOspfExitOverflowInterval_Object=MibTableColumn
nsVrOspfExitOverflowInterval=_NsVrOspfExitOverflowInterval_Object((1,3,6,1,4,1,3224,18,5,1,1,13),_NsVrOspfExitOverflowInterval_Type())
nsVrOspfExitOverflowInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfExitOverflowInterval.setStatus(_A)
_NsVrOspfDemandExtensions_Type=TruthValue
_NsVrOspfDemandExtensions_Object=MibTableColumn
nsVrOspfDemandExtensions=_NsVrOspfDemandExtensions_Object((1,3,6,1,4,1,3224,18,5,1,1,14),_NsVrOspfDemandExtensions_Type())
nsVrOspfDemandExtensions.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfDemandExtensions.setStatus(_A)
class _NsVrOspfGeneralVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrOspfGeneralVRID_Type.__name__=_E
_NsVrOspfGeneralVRID_Object=MibTableColumn
nsVrOspfGeneralVRID=_NsVrOspfGeneralVRID_Object((1,3,6,1,4,1,3224,18,5,1,1,15),_NsVrOspfGeneralVRID_Type())
nsVrOspfGeneralVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfGeneralVRID.setStatus(_A)
_NsVrOspfAreaTable_Object=MibTable
nsVrOspfAreaTable=_NsVrOspfAreaTable_Object((1,3,6,1,4,1,3224,18,5,2))
if mibBuilder.loadTexts:nsVrOspfAreaTable.setStatus(_A)
_NsVrOspfAreaEntry_Object=MibTableRow
nsVrOspfAreaEntry=_NsVrOspfAreaEntry_Object((1,3,6,1,4,1,3224,18,5,2,1))
nsVrOspfAreaEntry.setIndexNames((0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:nsVrOspfAreaEntry.setStatus(_A)
_NsVrOspfAreaId_Type=AreaID
_NsVrOspfAreaId_Object=MibTableColumn
nsVrOspfAreaId=_NsVrOspfAreaId_Object((1,3,6,1,4,1,3224,18,5,2,1,1),_NsVrOspfAreaId_Type())
nsVrOspfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAreaId.setStatus(_A)
class _NsVrOspfImportAsExtern_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('importExternal',1),('importNoExternal',2),('importNssa',3)))
_NsVrOspfImportAsExtern_Type.__name__=_E
_NsVrOspfImportAsExtern_Object=MibTableColumn
nsVrOspfImportAsExtern=_NsVrOspfImportAsExtern_Object((1,3,6,1,4,1,3224,18,5,2,1,3),_NsVrOspfImportAsExtern_Type())
nsVrOspfImportAsExtern.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfImportAsExtern.setStatus(_A)
_NsVrOspfSpfRuns_Type=Counter32
_NsVrOspfSpfRuns_Object=MibTableColumn
nsVrOspfSpfRuns=_NsVrOspfSpfRuns_Object((1,3,6,1,4,1,3224,18,5,2,1,4),_NsVrOspfSpfRuns_Type())
nsVrOspfSpfRuns.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfSpfRuns.setStatus(_A)
_NsVrOspfAreaBdrRtrCount_Type=Gauge32
_NsVrOspfAreaBdrRtrCount_Object=MibTableColumn
nsVrOspfAreaBdrRtrCount=_NsVrOspfAreaBdrRtrCount_Object((1,3,6,1,4,1,3224,18,5,2,1,5),_NsVrOspfAreaBdrRtrCount_Type())
nsVrOspfAreaBdrRtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAreaBdrRtrCount.setStatus(_A)
_NsVrOspfAsBdrRtrCount_Type=Gauge32
_NsVrOspfAsBdrRtrCount_Object=MibTableColumn
nsVrOspfAsBdrRtrCount=_NsVrOspfAsBdrRtrCount_Object((1,3,6,1,4,1,3224,18,5,2,1,6),_NsVrOspfAsBdrRtrCount_Type())
nsVrOspfAsBdrRtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAsBdrRtrCount.setStatus(_A)
_NsVrOspfAreaLsaCount_Type=Gauge32
_NsVrOspfAreaLsaCount_Object=MibTableColumn
nsVrOspfAreaLsaCount=_NsVrOspfAreaLsaCount_Object((1,3,6,1,4,1,3224,18,5,2,1,7),_NsVrOspfAreaLsaCount_Type())
nsVrOspfAreaLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAreaLsaCount.setStatus(_A)
class _NsVrOspfAreaLsaCksumSum_Type(Integer32):defaultValue=0
_NsVrOspfAreaLsaCksumSum_Type.__name__=_E
_NsVrOspfAreaLsaCksumSum_Object=MibTableColumn
nsVrOspfAreaLsaCksumSum=_NsVrOspfAreaLsaCksumSum_Object((1,3,6,1,4,1,3224,18,5,2,1,8),_NsVrOspfAreaLsaCksumSum_Type())
nsVrOspfAreaLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAreaLsaCksumSum.setStatus(_A)
class _NsVrOspfAreaSummary_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAreaSummary',1),('sendAreaSummary',2)))
_NsVrOspfAreaSummary_Type.__name__=_E
_NsVrOspfAreaSummary_Object=MibTableColumn
nsVrOspfAreaSummary=_NsVrOspfAreaSummary_Object((1,3,6,1,4,1,3224,18,5,2,1,9),_NsVrOspfAreaSummary_Type())
nsVrOspfAreaSummary.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfAreaSummary.setStatus(_A)
_NsVrOspfAreaStatus_Type=RowStatus
_NsVrOspfAreaStatus_Object=MibTableColumn
nsVrOspfAreaStatus=_NsVrOspfAreaStatus_Object((1,3,6,1,4,1,3224,18,5,2,1,10),_NsVrOspfAreaStatus_Type())
nsVrOspfAreaStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfAreaStatus.setStatus(_A)
class _NsVrOspfAreaVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrOspfAreaVRID_Type.__name__=_E
_NsVrOspfAreaVRID_Object=MibTableColumn
nsVrOspfAreaVRID=_NsVrOspfAreaVRID_Object((1,3,6,1,4,1,3224,18,5,2,1,11),_NsVrOspfAreaVRID_Type())
nsVrOspfAreaVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAreaVRID.setStatus(_A)
_NsVrOspfStubAreaTable_Object=MibTable
nsVrOspfStubAreaTable=_NsVrOspfStubAreaTable_Object((1,3,6,1,4,1,3224,18,5,3))
if mibBuilder.loadTexts:nsVrOspfStubAreaTable.setStatus(_A)
_NsVrOspfStubAreaEntry_Object=MibTableRow
nsVrOspfStubAreaEntry=_NsVrOspfStubAreaEntry_Object((1,3,6,1,4,1,3224,18,5,3,1))
nsVrOspfStubAreaEntry.setIndexNames((0,_C,_T),(0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:nsVrOspfStubAreaEntry.setStatus(_A)
_NsVrOspfStubAreaId_Type=AreaID
_NsVrOspfStubAreaId_Object=MibTableColumn
nsVrOspfStubAreaId=_NsVrOspfStubAreaId_Object((1,3,6,1,4,1,3224,18,5,3,1,1),_NsVrOspfStubAreaId_Type())
nsVrOspfStubAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfStubAreaId.setStatus(_A)
_NsVrOspfStubTOS_Type=TOSType
_NsVrOspfStubTOS_Object=MibTableColumn
nsVrOspfStubTOS=_NsVrOspfStubTOS_Object((1,3,6,1,4,1,3224,18,5,3,1,2),_NsVrOspfStubTOS_Type())
nsVrOspfStubTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfStubTOS.setStatus(_A)
_NsVrOspfStubMetric_Type=BigMetric
_NsVrOspfStubMetric_Object=MibTableColumn
nsVrOspfStubMetric=_NsVrOspfStubMetric_Object((1,3,6,1,4,1,3224,18,5,3,1,3),_NsVrOspfStubMetric_Type())
nsVrOspfStubMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfStubMetric.setStatus(_A)
_NsVrOspfStubStatus_Type=RowStatus
_NsVrOspfStubStatus_Object=MibTableColumn
nsVrOspfStubStatus=_NsVrOspfStubStatus_Object((1,3,6,1,4,1,3224,18,5,3,1,4),_NsVrOspfStubStatus_Type())
nsVrOspfStubStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfStubStatus.setStatus(_A)
class _NsVrOspfStubMetricType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nsVrOspfMetric',1),('comparableCost',2),('nonComparable',3)))
_NsVrOspfStubMetricType_Type.__name__=_E
_NsVrOspfStubMetricType_Object=MibTableColumn
nsVrOspfStubMetricType=_NsVrOspfStubMetricType_Object((1,3,6,1,4,1,3224,18,5,3,1,5),_NsVrOspfStubMetricType_Type())
nsVrOspfStubMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfStubMetricType.setStatus(_A)
class _NsVrOspfStubVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrOspfStubVRID_Type.__name__=_E
_NsVrOspfStubVRID_Object=MibTableColumn
nsVrOspfStubVRID=_NsVrOspfStubVRID_Object((1,3,6,1,4,1,3224,18,5,3,1,6),_NsVrOspfStubVRID_Type())
nsVrOspfStubVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfStubVRID.setStatus(_A)
_NsVrOspfLsdbTable_Object=MibTable
nsVrOspfLsdbTable=_NsVrOspfLsdbTable_Object((1,3,6,1,4,1,3224,18,5,4))
if mibBuilder.loadTexts:nsVrOspfLsdbTable.setStatus(_A)
_NsVrOspfLsdbEntry_Object=MibTableRow
nsVrOspfLsdbEntry=_NsVrOspfLsdbEntry_Object((1,3,6,1,4,1,3224,18,5,4,1))
nsVrOspfLsdbEntry.setIndexNames((0,_C,_W),(0,_C,_X),(0,_C,_Y),(0,_C,_Z),(0,_C,_a))
if mibBuilder.loadTexts:nsVrOspfLsdbEntry.setStatus(_A)
_NsVrOspfLsdbAreaId_Type=AreaID
_NsVrOspfLsdbAreaId_Object=MibTableColumn
nsVrOspfLsdbAreaId=_NsVrOspfLsdbAreaId_Object((1,3,6,1,4,1,3224,18,5,4,1,1),_NsVrOspfLsdbAreaId_Type())
nsVrOspfLsdbAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfLsdbAreaId.setStatus(_A)
class _NsVrOspfLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('routerLink',1),('networkLink',2),(_b,3),('asSummaryLink',4),(_c,5),('multicastLink',6),(_d,7)))
_NsVrOspfLsdbType_Type.__name__=_E
_NsVrOspfLsdbType_Object=MibTableColumn
nsVrOspfLsdbType=_NsVrOspfLsdbType_Object((1,3,6,1,4,1,3224,18,5,4,1,2),_NsVrOspfLsdbType_Type())
nsVrOspfLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfLsdbType.setStatus(_A)
_NsVrOspfLsdbLsid_Type=IpAddress
_NsVrOspfLsdbLsid_Object=MibTableColumn
nsVrOspfLsdbLsid=_NsVrOspfLsdbLsid_Object((1,3,6,1,4,1,3224,18,5,4,1,3),_NsVrOspfLsdbLsid_Type())
nsVrOspfLsdbLsid.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfLsdbLsid.setStatus(_A)
_NsVrOspfLsdbRouterId_Type=RouterID
_NsVrOspfLsdbRouterId_Object=MibTableColumn
nsVrOspfLsdbRouterId=_NsVrOspfLsdbRouterId_Object((1,3,6,1,4,1,3224,18,5,4,1,4),_NsVrOspfLsdbRouterId_Type())
nsVrOspfLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfLsdbRouterId.setStatus(_A)
_NsVrOspfLsdbSequence_Type=Integer32
_NsVrOspfLsdbSequence_Object=MibTableColumn
nsVrOspfLsdbSequence=_NsVrOspfLsdbSequence_Object((1,3,6,1,4,1,3224,18,5,4,1,5),_NsVrOspfLsdbSequence_Type())
nsVrOspfLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfLsdbSequence.setStatus(_A)
_NsVrOspfLsdbAge_Type=Integer32
_NsVrOspfLsdbAge_Object=MibTableColumn
nsVrOspfLsdbAge=_NsVrOspfLsdbAge_Object((1,3,6,1,4,1,3224,18,5,4,1,6),_NsVrOspfLsdbAge_Type())
nsVrOspfLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfLsdbAge.setStatus(_A)
_NsVrOspfLsdbChecksum_Type=Integer32
_NsVrOspfLsdbChecksum_Object=MibTableColumn
nsVrOspfLsdbChecksum=_NsVrOspfLsdbChecksum_Object((1,3,6,1,4,1,3224,18,5,4,1,7),_NsVrOspfLsdbChecksum_Type())
nsVrOspfLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfLsdbChecksum.setStatus(_A)
class _NsVrOspfLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_NsVrOspfLsdbAdvertisement_Type.__name__=_F
_NsVrOspfLsdbAdvertisement_Object=MibTableColumn
nsVrOspfLsdbAdvertisement=_NsVrOspfLsdbAdvertisement_Object((1,3,6,1,4,1,3224,18,5,4,1,8),_NsVrOspfLsdbAdvertisement_Type())
nsVrOspfLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfLsdbAdvertisement.setStatus(_A)
class _NsVrOspfLsdbVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrOspfLsdbVRID_Type.__name__=_E
_NsVrOspfLsdbVRID_Object=MibTableColumn
nsVrOspfLsdbVRID=_NsVrOspfLsdbVRID_Object((1,3,6,1,4,1,3224,18,5,4,1,9),_NsVrOspfLsdbVRID_Type())
nsVrOspfLsdbVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfLsdbVRID.setStatus(_A)
_NsVrOspfHostTable_Object=MibTable
nsVrOspfHostTable=_NsVrOspfHostTable_Object((1,3,6,1,4,1,3224,18,5,6))
if mibBuilder.loadTexts:nsVrOspfHostTable.setStatus(_A)
_NsVrOspfHostEntry_Object=MibTableRow
nsVrOspfHostEntry=_NsVrOspfHostEntry_Object((1,3,6,1,4,1,3224,18,5,6,1))
nsVrOspfHostEntry.setIndexNames((0,_C,_e),(0,_C,_f),(0,_C,_g))
if mibBuilder.loadTexts:nsVrOspfHostEntry.setStatus(_A)
_NsVrOspfHostIpAddress_Type=IpAddress
_NsVrOspfHostIpAddress_Object=MibTableColumn
nsVrOspfHostIpAddress=_NsVrOspfHostIpAddress_Object((1,3,6,1,4,1,3224,18,5,6,1,1),_NsVrOspfHostIpAddress_Type())
nsVrOspfHostIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfHostIpAddress.setStatus(_A)
_NsVrOspfHostTOS_Type=TOSType
_NsVrOspfHostTOS_Object=MibTableColumn
nsVrOspfHostTOS=_NsVrOspfHostTOS_Object((1,3,6,1,4,1,3224,18,5,6,1,2),_NsVrOspfHostTOS_Type())
nsVrOspfHostTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfHostTOS.setStatus(_A)
_NsVrOspfHostMetric_Type=Metric
_NsVrOspfHostMetric_Object=MibTableColumn
nsVrOspfHostMetric=_NsVrOspfHostMetric_Object((1,3,6,1,4,1,3224,18,5,6,1,3),_NsVrOspfHostMetric_Type())
nsVrOspfHostMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfHostMetric.setStatus(_A)
_NsVrOspfHostStatus_Type=RowStatus
_NsVrOspfHostStatus_Object=MibTableColumn
nsVrOspfHostStatus=_NsVrOspfHostStatus_Object((1,3,6,1,4,1,3224,18,5,6,1,4),_NsVrOspfHostStatus_Type())
nsVrOspfHostStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfHostStatus.setStatus(_A)
_NsVrOspfHostAreaID_Type=AreaID
_NsVrOspfHostAreaID_Object=MibTableColumn
nsVrOspfHostAreaID=_NsVrOspfHostAreaID_Object((1,3,6,1,4,1,3224,18,5,6,1,5),_NsVrOspfHostAreaID_Type())
nsVrOspfHostAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfHostAreaID.setStatus(_A)
class _NsVrOspfHostVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrOspfHostVRID_Type.__name__=_E
_NsVrOspfHostVRID_Object=MibTableColumn
nsVrOspfHostVRID=_NsVrOspfHostVRID_Object((1,3,6,1,4,1,3224,18,5,6,1,6),_NsVrOspfHostVRID_Type())
nsVrOspfHostVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfHostVRID.setStatus(_A)
_NsVrOspfIfTable_Object=MibTable
nsVrOspfIfTable=_NsVrOspfIfTable_Object((1,3,6,1,4,1,3224,18,5,7))
if mibBuilder.loadTexts:nsVrOspfIfTable.setStatus(_A)
_NsVrOspfIfEntry_Object=MibTableRow
nsVrOspfIfEntry=_NsVrOspfIfEntry_Object((1,3,6,1,4,1,3224,18,5,7,1))
nsVrOspfIfEntry.setIndexNames((0,_C,_h),(0,_C,_i),(0,_C,_j))
if mibBuilder.loadTexts:nsVrOspfIfEntry.setStatus(_A)
_NsVrOspfIfIpAddress_Type=IpAddress
_NsVrOspfIfIpAddress_Object=MibTableColumn
nsVrOspfIfIpAddress=_NsVrOspfIfIpAddress_Object((1,3,6,1,4,1,3224,18,5,7,1,1),_NsVrOspfIfIpAddress_Type())
nsVrOspfIfIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfIfIpAddress.setStatus(_A)
_NsVrOspfAddressLessIf_Type=Integer32
_NsVrOspfAddressLessIf_Object=MibTableColumn
nsVrOspfAddressLessIf=_NsVrOspfAddressLessIf_Object((1,3,6,1,4,1,3224,18,5,7,1,2),_NsVrOspfAddressLessIf_Type())
nsVrOspfAddressLessIf.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAddressLessIf.setStatus(_A)
class _NsVrOspfIfAreaId_Type(AreaID):defaultHexValue=_I
_NsVrOspfIfAreaId_Type.__name__=_k
_NsVrOspfIfAreaId_Object=MibTableColumn
nsVrOspfIfAreaId=_NsVrOspfIfAreaId_Object((1,3,6,1,4,1,3224,18,5,7,1,3),_NsVrOspfIfAreaId_Type())
nsVrOspfIfAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfAreaId.setStatus(_A)
class _NsVrOspfIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*(('broadcast',1),('nbma',2),(_L,3),('pointToMultipoint',5)))
_NsVrOspfIfType_Type.__name__=_E
_NsVrOspfIfType_Object=MibTableColumn
nsVrOspfIfType=_NsVrOspfIfType_Object((1,3,6,1,4,1,3224,18,5,7,1,4),_NsVrOspfIfType_Type())
nsVrOspfIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfType.setStatus(_A)
class _NsVrOspfIfAdminStat_Type(Status):defaultValue=1
_NsVrOspfIfAdminStat_Type.__name__=_l
_NsVrOspfIfAdminStat_Object=MibTableColumn
nsVrOspfIfAdminStat=_NsVrOspfIfAdminStat_Object((1,3,6,1,4,1,3224,18,5,7,1,5),_NsVrOspfIfAdminStat_Type())
nsVrOspfIfAdminStat.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfAdminStat.setStatus(_A)
class _NsVrOspfIfRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_NsVrOspfIfRtrPriority_Type.__name__=_M
_NsVrOspfIfRtrPriority_Object=MibTableColumn
nsVrOspfIfRtrPriority=_NsVrOspfIfRtrPriority_Object((1,3,6,1,4,1,3224,18,5,7,1,6),_NsVrOspfIfRtrPriority_Type())
nsVrOspfIfRtrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfRtrPriority.setStatus(_A)
class _NsVrOspfIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_NsVrOspfIfTransitDelay_Type.__name__=_H
_NsVrOspfIfTransitDelay_Object=MibTableColumn
nsVrOspfIfTransitDelay=_NsVrOspfIfTransitDelay_Object((1,3,6,1,4,1,3224,18,5,7,1,7),_NsVrOspfIfTransitDelay_Type())
nsVrOspfIfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfTransitDelay.setStatus(_A)
class _NsVrOspfIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_NsVrOspfIfRetransInterval_Type.__name__=_H
_NsVrOspfIfRetransInterval_Object=MibTableColumn
nsVrOspfIfRetransInterval=_NsVrOspfIfRetransInterval_Object((1,3,6,1,4,1,3224,18,5,7,1,8),_NsVrOspfIfRetransInterval_Type())
nsVrOspfIfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfRetransInterval.setStatus(_A)
class _NsVrOspfIfHelloInterval_Type(HelloRange):defaultValue=10
_NsVrOspfIfHelloInterval_Type.__name__=_N
_NsVrOspfIfHelloInterval_Object=MibTableColumn
nsVrOspfIfHelloInterval=_NsVrOspfIfHelloInterval_Object((1,3,6,1,4,1,3224,18,5,7,1,9),_NsVrOspfIfHelloInterval_Type())
nsVrOspfIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfHelloInterval.setStatus(_A)
class _NsVrOspfIfRtrDeadInterval_Type(PositiveInteger):defaultValue=40
_NsVrOspfIfRtrDeadInterval_Type.__name__=_G
_NsVrOspfIfRtrDeadInterval_Object=MibTableColumn
nsVrOspfIfRtrDeadInterval=_NsVrOspfIfRtrDeadInterval_Object((1,3,6,1,4,1,3224,18,5,7,1,10),_NsVrOspfIfRtrDeadInterval_Type())
nsVrOspfIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfRtrDeadInterval.setStatus(_A)
class _NsVrOspfIfPollInterval_Type(PositiveInteger):defaultValue=120
_NsVrOspfIfPollInterval_Type.__name__=_G
_NsVrOspfIfPollInterval_Object=MibTableColumn
nsVrOspfIfPollInterval=_NsVrOspfIfPollInterval_Object((1,3,6,1,4,1,3224,18,5,7,1,11),_NsVrOspfIfPollInterval_Type())
nsVrOspfIfPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfPollInterval.setStatus(_A)
class _NsVrOspfIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,1),('loopback',2),('waiting',3),(_L,4),('designatedRouter',5),('backupDesignatedRouter',6),('otherDesignatedRouter',7)))
_NsVrOspfIfState_Type.__name__=_E
_NsVrOspfIfState_Object=MibTableColumn
nsVrOspfIfState=_NsVrOspfIfState_Object((1,3,6,1,4,1,3224,18,5,7,1,12),_NsVrOspfIfState_Type())
nsVrOspfIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfIfState.setStatus(_A)
class _NsVrOspfIfDesignatedRouter_Type(IpAddress):defaultHexValue=_I
_NsVrOspfIfDesignatedRouter_Type.__name__=_K
_NsVrOspfIfDesignatedRouter_Object=MibTableColumn
nsVrOspfIfDesignatedRouter=_NsVrOspfIfDesignatedRouter_Object((1,3,6,1,4,1,3224,18,5,7,1,13),_NsVrOspfIfDesignatedRouter_Type())
nsVrOspfIfDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfIfDesignatedRouter.setStatus(_A)
class _NsVrOspfIfBackupDesignatedRouter_Type(IpAddress):defaultHexValue=_I
_NsVrOspfIfBackupDesignatedRouter_Type.__name__=_K
_NsVrOspfIfBackupDesignatedRouter_Object=MibTableColumn
nsVrOspfIfBackupDesignatedRouter=_NsVrOspfIfBackupDesignatedRouter_Object((1,3,6,1,4,1,3224,18,5,7,1,14),_NsVrOspfIfBackupDesignatedRouter_Type())
nsVrOspfIfBackupDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfIfBackupDesignatedRouter.setStatus(_A)
_NsVrOspfIfEvents_Type=Counter32
_NsVrOspfIfEvents_Object=MibTableColumn
nsVrOspfIfEvents=_NsVrOspfIfEvents_Object((1,3,6,1,4,1,3224,18,5,7,1,15),_NsVrOspfIfEvents_Type())
nsVrOspfIfEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfIfEvents.setStatus(_A)
class _NsVrOspfIfAuthKey_Type(OctetString):defaultHexValue=_m;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_NsVrOspfIfAuthKey_Type.__name__=_F
_NsVrOspfIfAuthKey_Object=MibTableColumn
nsVrOspfIfAuthKey=_NsVrOspfIfAuthKey_Object((1,3,6,1,4,1,3224,18,5,7,1,16),_NsVrOspfIfAuthKey_Type())
nsVrOspfIfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfAuthKey.setStatus(_A)
_NsVrOspfIfStatus_Type=RowStatus
_NsVrOspfIfStatus_Object=MibTableColumn
nsVrOspfIfStatus=_NsVrOspfIfStatus_Object((1,3,6,1,4,1,3224,18,5,7,1,17),_NsVrOspfIfStatus_Type())
nsVrOspfIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfStatus.setStatus(_A)
class _NsVrOspfIfMulticastForwarding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('blocked',1),('multicast',2),('unicast',3)))
_NsVrOspfIfMulticastForwarding_Type.__name__=_E
_NsVrOspfIfMulticastForwarding_Object=MibTableColumn
nsVrOspfIfMulticastForwarding=_NsVrOspfIfMulticastForwarding_Object((1,3,6,1,4,1,3224,18,5,7,1,18),_NsVrOspfIfMulticastForwarding_Type())
nsVrOspfIfMulticastForwarding.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfMulticastForwarding.setStatus(_A)
class _NsVrOspfIfDemand_Type(TruthValue):defaultValue=2
_NsVrOspfIfDemand_Type.__name__=_P
_NsVrOspfIfDemand_Object=MibTableColumn
nsVrOspfIfDemand=_NsVrOspfIfDemand_Object((1,3,6,1,4,1,3224,18,5,7,1,19),_NsVrOspfIfDemand_Type())
nsVrOspfIfDemand.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfDemand.setStatus(_A)
class _NsVrOspfIfAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NsVrOspfIfAuthType_Type.__name__=_E
_NsVrOspfIfAuthType_Object=MibTableColumn
nsVrOspfIfAuthType=_NsVrOspfIfAuthType_Object((1,3,6,1,4,1,3224,18,5,7,1,20),_NsVrOspfIfAuthType_Type())
nsVrOspfIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfAuthType.setStatus(_A)
class _NsVrOspfIfVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrOspfIfVRID_Type.__name__=_E
_NsVrOspfIfVRID_Object=MibTableColumn
nsVrOspfIfVRID=_NsVrOspfIfVRID_Object((1,3,6,1,4,1,3224,18,5,7,1,21),_NsVrOspfIfVRID_Type())
nsVrOspfIfVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfIfVRID.setStatus(_A)
_NsVrOspfIfMetricTable_Object=MibTable
nsVrOspfIfMetricTable=_NsVrOspfIfMetricTable_Object((1,3,6,1,4,1,3224,18,5,8))
if mibBuilder.loadTexts:nsVrOspfIfMetricTable.setStatus(_A)
_NsVrOspfIfMetricEntry_Object=MibTableRow
nsVrOspfIfMetricEntry=_NsVrOspfIfMetricEntry_Object((1,3,6,1,4,1,3224,18,5,8,1))
nsVrOspfIfMetricEntry.setIndexNames((0,_C,_O),(0,_C,_n),(0,_C,_o),(0,_C,_p),(0,_C,_O))
if mibBuilder.loadTexts:nsVrOspfIfMetricEntry.setStatus(_A)
_NsVrOspfIfMetricIpAddress_Type=IpAddress
_NsVrOspfIfMetricIpAddress_Object=MibTableColumn
nsVrOspfIfMetricIpAddress=_NsVrOspfIfMetricIpAddress_Object((1,3,6,1,4,1,3224,18,5,8,1,1),_NsVrOspfIfMetricIpAddress_Type())
nsVrOspfIfMetricIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfIfMetricIpAddress.setStatus(_A)
_NsVrOspfIfMetricAddressLessIf_Type=Integer32
_NsVrOspfIfMetricAddressLessIf_Object=MibTableColumn
nsVrOspfIfMetricAddressLessIf=_NsVrOspfIfMetricAddressLessIf_Object((1,3,6,1,4,1,3224,18,5,8,1,2),_NsVrOspfIfMetricAddressLessIf_Type())
nsVrOspfIfMetricAddressLessIf.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfIfMetricAddressLessIf.setStatus(_A)
_NsVrOspfIfMetricTOS_Type=TOSType
_NsVrOspfIfMetricTOS_Object=MibTableColumn
nsVrOspfIfMetricTOS=_NsVrOspfIfMetricTOS_Object((1,3,6,1,4,1,3224,18,5,8,1,3),_NsVrOspfIfMetricTOS_Type())
nsVrOspfIfMetricTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfIfMetricTOS.setStatus(_A)
_NsVrOspfIfMetricValue_Type=Metric
_NsVrOspfIfMetricValue_Object=MibTableColumn
nsVrOspfIfMetricValue=_NsVrOspfIfMetricValue_Object((1,3,6,1,4,1,3224,18,5,8,1,4),_NsVrOspfIfMetricValue_Type())
nsVrOspfIfMetricValue.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfMetricValue.setStatus(_A)
_NsVrOspfIfMetricStatus_Type=RowStatus
_NsVrOspfIfMetricStatus_Object=MibTableColumn
nsVrOspfIfMetricStatus=_NsVrOspfIfMetricStatus_Object((1,3,6,1,4,1,3224,18,5,8,1,5),_NsVrOspfIfMetricStatus_Type())
nsVrOspfIfMetricStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfIfMetricStatus.setStatus(_A)
class _NsVrOspfIfMetricVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrOspfIfMetricVRID_Type.__name__=_E
_NsVrOspfIfMetricVRID_Object=MibTableColumn
nsVrOspfIfMetricVRID=_NsVrOspfIfMetricVRID_Object((1,3,6,1,4,1,3224,18,5,8,1,6),_NsVrOspfIfMetricVRID_Type())
nsVrOspfIfMetricVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfIfMetricVRID.setStatus(_A)
_NsVrOspfVirtIfTable_Object=MibTable
nsVrOspfVirtIfTable=_NsVrOspfVirtIfTable_Object((1,3,6,1,4,1,3224,18,5,9))
if mibBuilder.loadTexts:nsVrOspfVirtIfTable.setStatus(_A)
_NsVrOspfVirtIfEntry_Object=MibTableRow
nsVrOspfVirtIfEntry=_NsVrOspfVirtIfEntry_Object((1,3,6,1,4,1,3224,18,5,9,1))
nsVrOspfVirtIfEntry.setIndexNames((0,_C,_q),(0,_C,_r),(0,_C,_s))
if mibBuilder.loadTexts:nsVrOspfVirtIfEntry.setStatus(_A)
_NsVrOspfVirtIfAreaId_Type=AreaID
_NsVrOspfVirtIfAreaId_Object=MibTableColumn
nsVrOspfVirtIfAreaId=_NsVrOspfVirtIfAreaId_Object((1,3,6,1,4,1,3224,18,5,9,1,1),_NsVrOspfVirtIfAreaId_Type())
nsVrOspfVirtIfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtIfAreaId.setStatus(_A)
_NsVrOspfVirtIfNeighbor_Type=RouterID
_NsVrOspfVirtIfNeighbor_Object=MibTableColumn
nsVrOspfVirtIfNeighbor=_NsVrOspfVirtIfNeighbor_Object((1,3,6,1,4,1,3224,18,5,9,1,2),_NsVrOspfVirtIfNeighbor_Type())
nsVrOspfVirtIfNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtIfNeighbor.setStatus(_A)
class _NsVrOspfVirtIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_NsVrOspfVirtIfTransitDelay_Type.__name__=_H
_NsVrOspfVirtIfTransitDelay_Object=MibTableColumn
nsVrOspfVirtIfTransitDelay=_NsVrOspfVirtIfTransitDelay_Object((1,3,6,1,4,1,3224,18,5,9,1,3),_NsVrOspfVirtIfTransitDelay_Type())
nsVrOspfVirtIfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfVirtIfTransitDelay.setStatus(_A)
class _NsVrOspfVirtIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_NsVrOspfVirtIfRetransInterval_Type.__name__=_H
_NsVrOspfVirtIfRetransInterval_Object=MibTableColumn
nsVrOspfVirtIfRetransInterval=_NsVrOspfVirtIfRetransInterval_Object((1,3,6,1,4,1,3224,18,5,9,1,4),_NsVrOspfVirtIfRetransInterval_Type())
nsVrOspfVirtIfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfVirtIfRetransInterval.setStatus(_A)
class _NsVrOspfVirtIfHelloInterval_Type(HelloRange):defaultValue=10
_NsVrOspfVirtIfHelloInterval_Type.__name__=_N
_NsVrOspfVirtIfHelloInterval_Object=MibTableColumn
nsVrOspfVirtIfHelloInterval=_NsVrOspfVirtIfHelloInterval_Object((1,3,6,1,4,1,3224,18,5,9,1,5),_NsVrOspfVirtIfHelloInterval_Type())
nsVrOspfVirtIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfVirtIfHelloInterval.setStatus(_A)
class _NsVrOspfVirtIfRtrDeadInterval_Type(PositiveInteger):defaultValue=60
_NsVrOspfVirtIfRtrDeadInterval_Type.__name__=_G
_NsVrOspfVirtIfRtrDeadInterval_Object=MibTableColumn
nsVrOspfVirtIfRtrDeadInterval=_NsVrOspfVirtIfRtrDeadInterval_Object((1,3,6,1,4,1,3224,18,5,9,1,6),_NsVrOspfVirtIfRtrDeadInterval_Type())
nsVrOspfVirtIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfVirtIfRtrDeadInterval.setStatus(_A)
class _NsVrOspfVirtIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_J,1),(_L,4)))
_NsVrOspfVirtIfState_Type.__name__=_E
_NsVrOspfVirtIfState_Object=MibTableColumn
nsVrOspfVirtIfState=_NsVrOspfVirtIfState_Object((1,3,6,1,4,1,3224,18,5,9,1,7),_NsVrOspfVirtIfState_Type())
nsVrOspfVirtIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtIfState.setStatus(_A)
_NsVrOspfVirtIfEvents_Type=Counter32
_NsVrOspfVirtIfEvents_Object=MibTableColumn
nsVrOspfVirtIfEvents=_NsVrOspfVirtIfEvents_Object((1,3,6,1,4,1,3224,18,5,9,1,8),_NsVrOspfVirtIfEvents_Type())
nsVrOspfVirtIfEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtIfEvents.setStatus(_A)
class _NsVrOspfVirtIfAuthKey_Type(OctetString):defaultHexValue=_m;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_NsVrOspfVirtIfAuthKey_Type.__name__=_F
_NsVrOspfVirtIfAuthKey_Object=MibTableColumn
nsVrOspfVirtIfAuthKey=_NsVrOspfVirtIfAuthKey_Object((1,3,6,1,4,1,3224,18,5,9,1,9),_NsVrOspfVirtIfAuthKey_Type())
nsVrOspfVirtIfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfVirtIfAuthKey.setStatus(_A)
_NsVrOspfVirtIfStatus_Type=RowStatus
_NsVrOspfVirtIfStatus_Object=MibTableColumn
nsVrOspfVirtIfStatus=_NsVrOspfVirtIfStatus_Object((1,3,6,1,4,1,3224,18,5,9,1,10),_NsVrOspfVirtIfStatus_Type())
nsVrOspfVirtIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfVirtIfStatus.setStatus(_A)
class _NsVrOspfVirtIfAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NsVrOspfVirtIfAuthType_Type.__name__=_E
_NsVrOspfVirtIfAuthType_Object=MibTableColumn
nsVrOspfVirtIfAuthType=_NsVrOspfVirtIfAuthType_Object((1,3,6,1,4,1,3224,18,5,9,1,11),_NsVrOspfVirtIfAuthType_Type())
nsVrOspfVirtIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfVirtIfAuthType.setStatus(_A)
class _NsVrOspfVirtIfVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrOspfVirtIfVRID_Type.__name__=_E
_NsVrOspfVirtIfVRID_Object=MibTableColumn
nsVrOspfVirtIfVRID=_NsVrOspfVirtIfVRID_Object((1,3,6,1,4,1,3224,18,5,9,1,12),_NsVrOspfVirtIfVRID_Type())
nsVrOspfVirtIfVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtIfVRID.setStatus(_A)
_NsVrOspfNbrTable_Object=MibTable
nsVrOspfNbrTable=_NsVrOspfNbrTable_Object((1,3,6,1,4,1,3224,18,5,10))
if mibBuilder.loadTexts:nsVrOspfNbrTable.setStatus(_A)
_NsVrOspfNbrEntry_Object=MibTableRow
nsVrOspfNbrEntry=_NsVrOspfNbrEntry_Object((1,3,6,1,4,1,3224,18,5,10,1))
nsVrOspfNbrEntry.setIndexNames((0,_C,_t),(0,_C,_u),(0,_C,_v))
if mibBuilder.loadTexts:nsVrOspfNbrEntry.setStatus(_A)
_NsVrOspfNbrIpAddr_Type=IpAddress
_NsVrOspfNbrIpAddr_Object=MibTableColumn
nsVrOspfNbrIpAddr=_NsVrOspfNbrIpAddr_Object((1,3,6,1,4,1,3224,18,5,10,1,1),_NsVrOspfNbrIpAddr_Type())
nsVrOspfNbrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfNbrIpAddr.setStatus(_A)
_NsVrOspfNbrAddressLessIndex_Type=InterfaceIndex
_NsVrOspfNbrAddressLessIndex_Object=MibTableColumn
nsVrOspfNbrAddressLessIndex=_NsVrOspfNbrAddressLessIndex_Object((1,3,6,1,4,1,3224,18,5,10,1,2),_NsVrOspfNbrAddressLessIndex_Type())
nsVrOspfNbrAddressLessIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfNbrAddressLessIndex.setStatus(_A)
class _NsVrOspfNbrRtrId_Type(RouterID):defaultHexValue=_I
_NsVrOspfNbrRtrId_Type.__name__=_w
_NsVrOspfNbrRtrId_Object=MibTableColumn
nsVrOspfNbrRtrId=_NsVrOspfNbrRtrId_Object((1,3,6,1,4,1,3224,18,5,10,1,3),_NsVrOspfNbrRtrId_Type())
nsVrOspfNbrRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfNbrRtrId.setStatus(_A)
class _NsVrOspfNbrOptions_Type(Integer32):defaultValue=0
_NsVrOspfNbrOptions_Type.__name__=_E
_NsVrOspfNbrOptions_Object=MibTableColumn
nsVrOspfNbrOptions=_NsVrOspfNbrOptions_Object((1,3,6,1,4,1,3224,18,5,10,1,4),_NsVrOspfNbrOptions_Type())
nsVrOspfNbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfNbrOptions.setStatus(_A)
class _NsVrOspfNbrPriority_Type(DesignatedRouterPriority):defaultValue=1
_NsVrOspfNbrPriority_Type.__name__=_M
_NsVrOspfNbrPriority_Object=MibTableColumn
nsVrOspfNbrPriority=_NsVrOspfNbrPriority_Object((1,3,6,1,4,1,3224,18,5,10,1,5),_NsVrOspfNbrPriority_Type())
nsVrOspfNbrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfNbrPriority.setStatus(_A)
class _NsVrOspfNbrState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_x,2),('init',3),(_y,4),(_z,5),('exchange',6),('loading',7),('full',8)))
_NsVrOspfNbrState_Type.__name__=_E
_NsVrOspfNbrState_Object=MibTableColumn
nsVrOspfNbrState=_NsVrOspfNbrState_Object((1,3,6,1,4,1,3224,18,5,10,1,6),_NsVrOspfNbrState_Type())
nsVrOspfNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfNbrState.setStatus(_A)
_NsVrOspfNbrEvents_Type=Counter32
_NsVrOspfNbrEvents_Object=MibTableColumn
nsVrOspfNbrEvents=_NsVrOspfNbrEvents_Object((1,3,6,1,4,1,3224,18,5,10,1,7),_NsVrOspfNbrEvents_Type())
nsVrOspfNbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfNbrEvents.setStatus(_A)
_NsVrOspfNbrLsRetransQLen_Type=Gauge32
_NsVrOspfNbrLsRetransQLen_Object=MibTableColumn
nsVrOspfNbrLsRetransQLen=_NsVrOspfNbrLsRetransQLen_Object((1,3,6,1,4,1,3224,18,5,10,1,8),_NsVrOspfNbrLsRetransQLen_Type())
nsVrOspfNbrLsRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfNbrLsRetransQLen.setStatus(_A)
_NsVrOspfNbmaNbrStatus_Type=RowStatus
_NsVrOspfNbmaNbrStatus_Object=MibTableColumn
nsVrOspfNbmaNbrStatus=_NsVrOspfNbmaNbrStatus_Object((1,3,6,1,4,1,3224,18,5,10,1,9),_NsVrOspfNbmaNbrStatus_Type())
nsVrOspfNbmaNbrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfNbmaNbrStatus.setStatus(_A)
class _NsVrOspfNbmaNbrPermanence_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('permanent',2)))
_NsVrOspfNbmaNbrPermanence_Type.__name__=_E
_NsVrOspfNbmaNbrPermanence_Object=MibTableColumn
nsVrOspfNbmaNbrPermanence=_NsVrOspfNbmaNbrPermanence_Object((1,3,6,1,4,1,3224,18,5,10,1,10),_NsVrOspfNbmaNbrPermanence_Type())
nsVrOspfNbmaNbrPermanence.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfNbmaNbrPermanence.setStatus(_A)
_NsVrOspfNbrHelloSuppressed_Type=TruthValue
_NsVrOspfNbrHelloSuppressed_Object=MibTableColumn
nsVrOspfNbrHelloSuppressed=_NsVrOspfNbrHelloSuppressed_Object((1,3,6,1,4,1,3224,18,5,10,1,11),_NsVrOspfNbrHelloSuppressed_Type())
nsVrOspfNbrHelloSuppressed.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfNbrHelloSuppressed.setStatus(_A)
class _NsVrOspfNbrVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrOspfNbrVRID_Type.__name__=_E
_NsVrOspfNbrVRID_Object=MibTableColumn
nsVrOspfNbrVRID=_NsVrOspfNbrVRID_Object((1,3,6,1,4,1,3224,18,5,10,1,12),_NsVrOspfNbrVRID_Type())
nsVrOspfNbrVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfNbrVRID.setStatus(_A)
_NsVrOspfVirtNbrTable_Object=MibTable
nsVrOspfVirtNbrTable=_NsVrOspfVirtNbrTable_Object((1,3,6,1,4,1,3224,18,5,11))
if mibBuilder.loadTexts:nsVrOspfVirtNbrTable.setStatus(_A)
_NsVrOspfVirtNbrEntry_Object=MibTableRow
nsVrOspfVirtNbrEntry=_NsVrOspfVirtNbrEntry_Object((1,3,6,1,4,1,3224,18,5,11,1))
nsVrOspfVirtNbrEntry.setIndexNames((0,_C,_A0),(0,_C,_A1),(0,_C,_A2))
if mibBuilder.loadTexts:nsVrOspfVirtNbrEntry.setStatus(_A)
_NsVrOspfVirtNbrArea_Type=AreaID
_NsVrOspfVirtNbrArea_Object=MibTableColumn
nsVrOspfVirtNbrArea=_NsVrOspfVirtNbrArea_Object((1,3,6,1,4,1,3224,18,5,11,1,1),_NsVrOspfVirtNbrArea_Type())
nsVrOspfVirtNbrArea.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtNbrArea.setStatus(_A)
_NsVrOspfVirtNbrRtrId_Type=RouterID
_NsVrOspfVirtNbrRtrId_Object=MibTableColumn
nsVrOspfVirtNbrRtrId=_NsVrOspfVirtNbrRtrId_Object((1,3,6,1,4,1,3224,18,5,11,1,2),_NsVrOspfVirtNbrRtrId_Type())
nsVrOspfVirtNbrRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtNbrRtrId.setStatus(_A)
_NsVrOspfVirtNbrIpAddr_Type=IpAddress
_NsVrOspfVirtNbrIpAddr_Object=MibTableColumn
nsVrOspfVirtNbrIpAddr=_NsVrOspfVirtNbrIpAddr_Object((1,3,6,1,4,1,3224,18,5,11,1,3),_NsVrOspfVirtNbrIpAddr_Type())
nsVrOspfVirtNbrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtNbrIpAddr.setStatus(_A)
_NsVrOspfVirtNbrOptions_Type=Integer32
_NsVrOspfVirtNbrOptions_Object=MibTableColumn
nsVrOspfVirtNbrOptions=_NsVrOspfVirtNbrOptions_Object((1,3,6,1,4,1,3224,18,5,11,1,4),_NsVrOspfVirtNbrOptions_Type())
nsVrOspfVirtNbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtNbrOptions.setStatus(_A)
class _NsVrOspfVirtNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_x,2),('init',3),(_y,4),(_z,5),('exchange',6),('loading',7),('full',8)))
_NsVrOspfVirtNbrState_Type.__name__=_E
_NsVrOspfVirtNbrState_Object=MibTableColumn
nsVrOspfVirtNbrState=_NsVrOspfVirtNbrState_Object((1,3,6,1,4,1,3224,18,5,11,1,5),_NsVrOspfVirtNbrState_Type())
nsVrOspfVirtNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtNbrState.setStatus(_A)
_NsVrOspfVirtNbrEvents_Type=Counter32
_NsVrOspfVirtNbrEvents_Object=MibTableColumn
nsVrOspfVirtNbrEvents=_NsVrOspfVirtNbrEvents_Object((1,3,6,1,4,1,3224,18,5,11,1,6),_NsVrOspfVirtNbrEvents_Type())
nsVrOspfVirtNbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtNbrEvents.setStatus(_A)
_NsVrOspfVirtNbrLsRetransQLen_Type=Gauge32
_NsVrOspfVirtNbrLsRetransQLen_Object=MibTableColumn
nsVrOspfVirtNbrLsRetransQLen=_NsVrOspfVirtNbrLsRetransQLen_Object((1,3,6,1,4,1,3224,18,5,11,1,7),_NsVrOspfVirtNbrLsRetransQLen_Type())
nsVrOspfVirtNbrLsRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtNbrLsRetransQLen.setStatus(_A)
_NsVrOspfVirtNbrHelloSuppressed_Type=TruthValue
_NsVrOspfVirtNbrHelloSuppressed_Object=MibTableColumn
nsVrOspfVirtNbrHelloSuppressed=_NsVrOspfVirtNbrHelloSuppressed_Object((1,3,6,1,4,1,3224,18,5,11,1,8),_NsVrOspfVirtNbrHelloSuppressed_Type())
nsVrOspfVirtNbrHelloSuppressed.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtNbrHelloSuppressed.setStatus(_A)
class _NsVrOspfVirtNbrVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrOspfVirtNbrVRID_Type.__name__=_E
_NsVrOspfVirtNbrVRID_Object=MibTableColumn
nsVrOspfVirtNbrVRID=_NsVrOspfVirtNbrVRID_Object((1,3,6,1,4,1,3224,18,5,11,1,9),_NsVrOspfVirtNbrVRID_Type())
nsVrOspfVirtNbrVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfVirtNbrVRID.setStatus(_A)
_NsVrOspfExtLsdbTable_Object=MibTable
nsVrOspfExtLsdbTable=_NsVrOspfExtLsdbTable_Object((1,3,6,1,4,1,3224,18,5,12))
if mibBuilder.loadTexts:nsVrOspfExtLsdbTable.setStatus(_A)
_NsVrOspfExtLsdbEntry_Object=MibTableRow
nsVrOspfExtLsdbEntry=_NsVrOspfExtLsdbEntry_Object((1,3,6,1,4,1,3224,18,5,12,1))
nsVrOspfExtLsdbEntry.setIndexNames((0,_C,_A3),(0,_C,_A4),(0,_C,_A5),(0,_C,_A6))
if mibBuilder.loadTexts:nsVrOspfExtLsdbEntry.setStatus(_A)
class _NsVrOspfExtLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues((_c,5))
_NsVrOspfExtLsdbType_Type.__name__=_E
_NsVrOspfExtLsdbType_Object=MibTableColumn
nsVrOspfExtLsdbType=_NsVrOspfExtLsdbType_Object((1,3,6,1,4,1,3224,18,5,12,1,1),_NsVrOspfExtLsdbType_Type())
nsVrOspfExtLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfExtLsdbType.setStatus(_A)
_NsVrOspfExtLsdbLsid_Type=IpAddress
_NsVrOspfExtLsdbLsid_Object=MibTableColumn
nsVrOspfExtLsdbLsid=_NsVrOspfExtLsdbLsid_Object((1,3,6,1,4,1,3224,18,5,12,1,2),_NsVrOspfExtLsdbLsid_Type())
nsVrOspfExtLsdbLsid.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfExtLsdbLsid.setStatus(_A)
_NsVrOspfExtLsdbRouterId_Type=RouterID
_NsVrOspfExtLsdbRouterId_Object=MibTableColumn
nsVrOspfExtLsdbRouterId=_NsVrOspfExtLsdbRouterId_Object((1,3,6,1,4,1,3224,18,5,12,1,3),_NsVrOspfExtLsdbRouterId_Type())
nsVrOspfExtLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfExtLsdbRouterId.setStatus(_A)
_NsVrOspfExtLsdbSequence_Type=Integer32
_NsVrOspfExtLsdbSequence_Object=MibTableColumn
nsVrOspfExtLsdbSequence=_NsVrOspfExtLsdbSequence_Object((1,3,6,1,4,1,3224,18,5,12,1,4),_NsVrOspfExtLsdbSequence_Type())
nsVrOspfExtLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfExtLsdbSequence.setStatus(_A)
_NsVrOspfExtLsdbAge_Type=Integer32
_NsVrOspfExtLsdbAge_Object=MibTableColumn
nsVrOspfExtLsdbAge=_NsVrOspfExtLsdbAge_Object((1,3,6,1,4,1,3224,18,5,12,1,5),_NsVrOspfExtLsdbAge_Type())
nsVrOspfExtLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfExtLsdbAge.setStatus(_A)
_NsVrOspfExtLsdbChecksum_Type=Integer32
_NsVrOspfExtLsdbChecksum_Object=MibTableColumn
nsVrOspfExtLsdbChecksum=_NsVrOspfExtLsdbChecksum_Object((1,3,6,1,4,1,3224,18,5,12,1,6),_NsVrOspfExtLsdbChecksum_Type())
nsVrOspfExtLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfExtLsdbChecksum.setStatus(_A)
class _NsVrOspfExtLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(36,36));fixedLength=36
_NsVrOspfExtLsdbAdvertisement_Type.__name__=_F
_NsVrOspfExtLsdbAdvertisement_Object=MibTableColumn
nsVrOspfExtLsdbAdvertisement=_NsVrOspfExtLsdbAdvertisement_Object((1,3,6,1,4,1,3224,18,5,12,1,7),_NsVrOspfExtLsdbAdvertisement_Type())
nsVrOspfExtLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfExtLsdbAdvertisement.setStatus(_A)
class _NsVrOspfExtLsdbVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrOspfExtLsdbVRID_Type.__name__=_E
_NsVrOspfExtLsdbVRID_Object=MibTableColumn
nsVrOspfExtLsdbVRID=_NsVrOspfExtLsdbVRID_Object((1,3,6,1,4,1,3224,18,5,12,1,8),_NsVrOspfExtLsdbVRID_Type())
nsVrOspfExtLsdbVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfExtLsdbVRID.setStatus(_A)
_NsVrOspfAreaAggregateTable_Object=MibTable
nsVrOspfAreaAggregateTable=_NsVrOspfAreaAggregateTable_Object((1,3,6,1,4,1,3224,18,5,14))
if mibBuilder.loadTexts:nsVrOspfAreaAggregateTable.setStatus(_A)
_NsVrOspfAreaAggregateEntry_Object=MibTableRow
nsVrOspfAreaAggregateEntry=_NsVrOspfAreaAggregateEntry_Object((1,3,6,1,4,1,3224,18,5,14,1))
nsVrOspfAreaAggregateEntry.setIndexNames((0,_C,_A7),(0,_C,_A8),(0,_C,_A9),(0,_C,_AA),(0,_C,_AB))
if mibBuilder.loadTexts:nsVrOspfAreaAggregateEntry.setStatus(_A)
_NsVrOspfAreaAggregateAreaID_Type=AreaID
_NsVrOspfAreaAggregateAreaID_Object=MibTableColumn
nsVrOspfAreaAggregateAreaID=_NsVrOspfAreaAggregateAreaID_Object((1,3,6,1,4,1,3224,18,5,14,1,1),_NsVrOspfAreaAggregateAreaID_Type())
nsVrOspfAreaAggregateAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAreaAggregateAreaID.setStatus(_A)
class _NsVrOspfAreaAggregateLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,7)));namedValues=NamedValues(*((_b,3),(_d,7)))
_NsVrOspfAreaAggregateLsdbType_Type.__name__=_E
_NsVrOspfAreaAggregateLsdbType_Object=MibTableColumn
nsVrOspfAreaAggregateLsdbType=_NsVrOspfAreaAggregateLsdbType_Object((1,3,6,1,4,1,3224,18,5,14,1,2),_NsVrOspfAreaAggregateLsdbType_Type())
nsVrOspfAreaAggregateLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAreaAggregateLsdbType.setStatus(_A)
_NsVrOspfAreaAggregateNet_Type=IpAddress
_NsVrOspfAreaAggregateNet_Object=MibTableColumn
nsVrOspfAreaAggregateNet=_NsVrOspfAreaAggregateNet_Object((1,3,6,1,4,1,3224,18,5,14,1,3),_NsVrOspfAreaAggregateNet_Type())
nsVrOspfAreaAggregateNet.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAreaAggregateNet.setStatus(_A)
_NsVrOspfAreaAggregateMask_Type=IpAddress
_NsVrOspfAreaAggregateMask_Object=MibTableColumn
nsVrOspfAreaAggregateMask=_NsVrOspfAreaAggregateMask_Object((1,3,6,1,4,1,3224,18,5,14,1,4),_NsVrOspfAreaAggregateMask_Type())
nsVrOspfAreaAggregateMask.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAreaAggregateMask.setStatus(_A)
_NsVrOspfAreaAggregateStatus_Type=RowStatus
_NsVrOspfAreaAggregateStatus_Object=MibTableColumn
nsVrOspfAreaAggregateStatus=_NsVrOspfAreaAggregateStatus_Object((1,3,6,1,4,1,3224,18,5,14,1,5),_NsVrOspfAreaAggregateStatus_Type())
nsVrOspfAreaAggregateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfAreaAggregateStatus.setStatus(_A)
class _NsVrOspfAreaAggregateEffect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('advertiseMatching',1),('doNotAdvertiseMatching',2)))
_NsVrOspfAreaAggregateEffect_Type.__name__=_E
_NsVrOspfAreaAggregateEffect_Object=MibTableColumn
nsVrOspfAreaAggregateEffect=_NsVrOspfAreaAggregateEffect_Object((1,3,6,1,4,1,3224,18,5,14,1,6),_NsVrOspfAreaAggregateEffect_Type())
nsVrOspfAreaAggregateEffect.setMaxAccess(_D)
if mibBuilder.loadTexts:nsVrOspfAreaAggregateEffect.setStatus(_A)
class _NsVrOspfAreaAggregateVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrOspfAreaAggregateVRID_Type.__name__=_E
_NsVrOspfAreaAggregateVRID_Object=MibTableColumn
nsVrOspfAreaAggregateVRID=_NsVrOspfAreaAggregateVRID_Object((1,3,6,1,4,1,3224,18,5,14,1,7),_NsVrOspfAreaAggregateVRID_Type())
nsVrOspfAreaAggregateVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrOspfAreaAggregateVRID.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_k:AreaID,_w:RouterID,'Metric':Metric,'BigMetric':BigMetric,_l:Status,_G:PositiveInteger,_N:HelloRange,_H:UpToMaxAge,'InterfaceIndex':InterfaceIndex,_M:DesignatedRouterPriority,'TOSType':TOSType,'nsVrOspf':nsVrOspf,'nsVrOspfGeneralTable':nsVrOspfGeneralTable,'nsVrOspfGeneralEntry':nsVrOspfGeneralEntry,'nsVrOspfRouterId':nsVrOspfRouterId,'nsVrOspfAdminStat':nsVrOspfAdminStat,'nsVrOspfVersionNumber':nsVrOspfVersionNumber,'nsVrOspfAreaBdrRtrStatus':nsVrOspfAreaBdrRtrStatus,'nsVrOspfASBdrRtrStatus':nsVrOspfASBdrRtrStatus,'nsVrOspfExternLsaCount':nsVrOspfExternLsaCount,'nsVrOspfExternLsaCksumSum':nsVrOspfExternLsaCksumSum,'nsVrOspfTOSSupport':nsVrOspfTOSSupport,'nsVrOspfOriginateNewLsas':nsVrOspfOriginateNewLsas,'nsVrOspfRxNewLsas':nsVrOspfRxNewLsas,'nsVrOspfExtLsdbLimit':nsVrOspfExtLsdbLimit,'nsVrOspfMulticastExtensions':nsVrOspfMulticastExtensions,'nsVrOspfExitOverflowInterval':nsVrOspfExitOverflowInterval,'nsVrOspfDemandExtensions':nsVrOspfDemandExtensions,_Q:nsVrOspfGeneralVRID,'nsVrOspfAreaTable':nsVrOspfAreaTable,'nsVrOspfAreaEntry':nsVrOspfAreaEntry,_S:nsVrOspfAreaId,'nsVrOspfImportAsExtern':nsVrOspfImportAsExtern,'nsVrOspfSpfRuns':nsVrOspfSpfRuns,'nsVrOspfAreaBdrRtrCount':nsVrOspfAreaBdrRtrCount,'nsVrOspfAsBdrRtrCount':nsVrOspfAsBdrRtrCount,'nsVrOspfAreaLsaCount':nsVrOspfAreaLsaCount,'nsVrOspfAreaLsaCksumSum':nsVrOspfAreaLsaCksumSum,'nsVrOspfAreaSummary':nsVrOspfAreaSummary,'nsVrOspfAreaStatus':nsVrOspfAreaStatus,_R:nsVrOspfAreaVRID,'nsVrOspfStubAreaTable':nsVrOspfStubAreaTable,'nsVrOspfStubAreaEntry':nsVrOspfStubAreaEntry,_U:nsVrOspfStubAreaId,_V:nsVrOspfStubTOS,'nsVrOspfStubMetric':nsVrOspfStubMetric,'nsVrOspfStubStatus':nsVrOspfStubStatus,'nsVrOspfStubMetricType':nsVrOspfStubMetricType,_T:nsVrOspfStubVRID,'nsVrOspfLsdbTable':nsVrOspfLsdbTable,'nsVrOspfLsdbEntry':nsVrOspfLsdbEntry,_X:nsVrOspfLsdbAreaId,_Y:nsVrOspfLsdbType,_Z:nsVrOspfLsdbLsid,_a:nsVrOspfLsdbRouterId,'nsVrOspfLsdbSequence':nsVrOspfLsdbSequence,'nsVrOspfLsdbAge':nsVrOspfLsdbAge,'nsVrOspfLsdbChecksum':nsVrOspfLsdbChecksum,'nsVrOspfLsdbAdvertisement':nsVrOspfLsdbAdvertisement,_W:nsVrOspfLsdbVRID,'nsVrOspfHostTable':nsVrOspfHostTable,'nsVrOspfHostEntry':nsVrOspfHostEntry,_f:nsVrOspfHostIpAddress,_g:nsVrOspfHostTOS,'nsVrOspfHostMetric':nsVrOspfHostMetric,'nsVrOspfHostStatus':nsVrOspfHostStatus,'nsVrOspfHostAreaID':nsVrOspfHostAreaID,_e:nsVrOspfHostVRID,'nsVrOspfIfTable':nsVrOspfIfTable,'nsVrOspfIfEntry':nsVrOspfIfEntry,_i:nsVrOspfIfIpAddress,_j:nsVrOspfAddressLessIf,'nsVrOspfIfAreaId':nsVrOspfIfAreaId,'nsVrOspfIfType':nsVrOspfIfType,'nsVrOspfIfAdminStat':nsVrOspfIfAdminStat,'nsVrOspfIfRtrPriority':nsVrOspfIfRtrPriority,'nsVrOspfIfTransitDelay':nsVrOspfIfTransitDelay,'nsVrOspfIfRetransInterval':nsVrOspfIfRetransInterval,'nsVrOspfIfHelloInterval':nsVrOspfIfHelloInterval,'nsVrOspfIfRtrDeadInterval':nsVrOspfIfRtrDeadInterval,'nsVrOspfIfPollInterval':nsVrOspfIfPollInterval,'nsVrOspfIfState':nsVrOspfIfState,'nsVrOspfIfDesignatedRouter':nsVrOspfIfDesignatedRouter,'nsVrOspfIfBackupDesignatedRouter':nsVrOspfIfBackupDesignatedRouter,'nsVrOspfIfEvents':nsVrOspfIfEvents,'nsVrOspfIfAuthKey':nsVrOspfIfAuthKey,'nsVrOspfIfStatus':nsVrOspfIfStatus,'nsVrOspfIfMulticastForwarding':nsVrOspfIfMulticastForwarding,'nsVrOspfIfDemand':nsVrOspfIfDemand,'nsVrOspfIfAuthType':nsVrOspfIfAuthType,_h:nsVrOspfIfVRID,'nsVrOspfIfMetricTable':nsVrOspfIfMetricTable,'nsVrOspfIfMetricEntry':nsVrOspfIfMetricEntry,_n:nsVrOspfIfMetricIpAddress,_o:nsVrOspfIfMetricAddressLessIf,_p:nsVrOspfIfMetricTOS,'nsVrOspfIfMetricValue':nsVrOspfIfMetricValue,'nsVrOspfIfMetricStatus':nsVrOspfIfMetricStatus,_O:nsVrOspfIfMetricVRID,'nsVrOspfVirtIfTable':nsVrOspfVirtIfTable,'nsVrOspfVirtIfEntry':nsVrOspfVirtIfEntry,_r:nsVrOspfVirtIfAreaId,_s:nsVrOspfVirtIfNeighbor,'nsVrOspfVirtIfTransitDelay':nsVrOspfVirtIfTransitDelay,'nsVrOspfVirtIfRetransInterval':nsVrOspfVirtIfRetransInterval,'nsVrOspfVirtIfHelloInterval':nsVrOspfVirtIfHelloInterval,'nsVrOspfVirtIfRtrDeadInterval':nsVrOspfVirtIfRtrDeadInterval,'nsVrOspfVirtIfState':nsVrOspfVirtIfState,'nsVrOspfVirtIfEvents':nsVrOspfVirtIfEvents,'nsVrOspfVirtIfAuthKey':nsVrOspfVirtIfAuthKey,'nsVrOspfVirtIfStatus':nsVrOspfVirtIfStatus,'nsVrOspfVirtIfAuthType':nsVrOspfVirtIfAuthType,_q:nsVrOspfVirtIfVRID,'nsVrOspfNbrTable':nsVrOspfNbrTable,'nsVrOspfNbrEntry':nsVrOspfNbrEntry,_u:nsVrOspfNbrIpAddr,_v:nsVrOspfNbrAddressLessIndex,'nsVrOspfNbrRtrId':nsVrOspfNbrRtrId,'nsVrOspfNbrOptions':nsVrOspfNbrOptions,'nsVrOspfNbrPriority':nsVrOspfNbrPriority,'nsVrOspfNbrState':nsVrOspfNbrState,'nsVrOspfNbrEvents':nsVrOspfNbrEvents,'nsVrOspfNbrLsRetransQLen':nsVrOspfNbrLsRetransQLen,'nsVrOspfNbmaNbrStatus':nsVrOspfNbmaNbrStatus,'nsVrOspfNbmaNbrPermanence':nsVrOspfNbmaNbrPermanence,'nsVrOspfNbrHelloSuppressed':nsVrOspfNbrHelloSuppressed,_t:nsVrOspfNbrVRID,'nsVrOspfVirtNbrTable':nsVrOspfVirtNbrTable,'nsVrOspfVirtNbrEntry':nsVrOspfVirtNbrEntry,_A1:nsVrOspfVirtNbrArea,_A2:nsVrOspfVirtNbrRtrId,'nsVrOspfVirtNbrIpAddr':nsVrOspfVirtNbrIpAddr,'nsVrOspfVirtNbrOptions':nsVrOspfVirtNbrOptions,'nsVrOspfVirtNbrState':nsVrOspfVirtNbrState,'nsVrOspfVirtNbrEvents':nsVrOspfVirtNbrEvents,'nsVrOspfVirtNbrLsRetransQLen':nsVrOspfVirtNbrLsRetransQLen,'nsVrOspfVirtNbrHelloSuppressed':nsVrOspfVirtNbrHelloSuppressed,_A0:nsVrOspfVirtNbrVRID,'nsVrOspfExtLsdbTable':nsVrOspfExtLsdbTable,'nsVrOspfExtLsdbEntry':nsVrOspfExtLsdbEntry,_A4:nsVrOspfExtLsdbType,_A5:nsVrOspfExtLsdbLsid,_A6:nsVrOspfExtLsdbRouterId,'nsVrOspfExtLsdbSequence':nsVrOspfExtLsdbSequence,'nsVrOspfExtLsdbAge':nsVrOspfExtLsdbAge,'nsVrOspfExtLsdbChecksum':nsVrOspfExtLsdbChecksum,'nsVrOspfExtLsdbAdvertisement':nsVrOspfExtLsdbAdvertisement,_A3:nsVrOspfExtLsdbVRID,'nsVrOspfAreaAggregateTable':nsVrOspfAreaAggregateTable,'nsVrOspfAreaAggregateEntry':nsVrOspfAreaAggregateEntry,_A8:nsVrOspfAreaAggregateAreaID,_A9:nsVrOspfAreaAggregateLsdbType,_AA:nsVrOspfAreaAggregateNet,_AB:nsVrOspfAreaAggregateMask,'nsVrOspfAreaAggregateStatus':nsVrOspfAreaAggregateStatus,'nsVrOspfAreaAggregateEffect':nsVrOspfAreaAggregateEffect,_A7:nsVrOspfAreaAggregateVRID})