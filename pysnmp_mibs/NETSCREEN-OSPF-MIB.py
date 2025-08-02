_AB='nsOspfAreaAggregateVRID'
_AA='nsOspfAreaAggregateMask'
_A9='nsOspfAreaAggregateNet'
_A8='nsOspfAreaAggregateLsdbType'
_A7='nsOspfAreaAggregateAreaID'
_A6='nsOspfExtLsdbVRID'
_A5='nsOspfExtLsdbRouterId'
_A4='nsOspfExtLsdbLsid'
_A3='nsOspfExtLsdbType'
_A2='nsOspfVirtNbrVRID'
_A1='nsOspfVirtNbrRtrId'
_A0='nsOspfVirtNbrArea'
_z='exchangeStart'
_y='twoWay'
_x='attempt'
_w='RouterID'
_v='nsOspfNbrVRID'
_u='nsOspfNbrAddressLessIndex'
_t='nsOspfNbrIpAddr'
_s='nsOspfVirtIfVRID'
_r='nsOspfVirtIfNeighbor'
_q='nsOspfVirtIfAreaId'
_p='nsOspfIfMetricVRID'
_o='nsOspfIfMetricTOS'
_n='nsOspfIfMetricAddressLessIf'
_m='nsOspfIfMetricIpAddress'
_l='0000000000000000'
_k='Status'
_j='AreaID'
_i='nsOspfIfVRID'
_h='nsOspfAddressLessIf'
_g='nsOspfIfIpAddress'
_f='nsOspfHostVRID'
_e='nsOspfHostTOS'
_d='nsOspfHostIpAddress'
_c='nssaExternalLink'
_b='asExternalLink'
_a='summaryLink'
_Z='nsOspfLsdbVRID'
_Y='nsOspfLsdbRouterId'
_X='nsOspfLsdbLsid'
_W='nsOspfLsdbType'
_V='nsOspfLsdbAreaId'
_U='nsOspfStubVRID'
_T='nsOspfStubTOS'
_S='nsOspfStubAreaId'
_R='nsOspfAreaVRID'
_Q='nsOspfAreaId'
_P='nsOspfGeneralVRID'
_O='TruthValue'
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
_C='NETSCREEN-OSPF-MIB'
_B='read-only'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVR,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVR')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,_K,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_O)
nsOspf=ModuleIdentity((1,3,6,1,4,1,3224,18,2))
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
_NsOspfGeneralTable_Object=MibTable
nsOspfGeneralTable=_NsOspfGeneralTable_Object((1,3,6,1,4,1,3224,18,2,1))
if mibBuilder.loadTexts:nsOspfGeneralTable.setStatus(_A)
_NsOspfGeneralEntry_Object=MibTableRow
nsOspfGeneralEntry=_NsOspfGeneralEntry_Object((1,3,6,1,4,1,3224,18,2,1,1))
nsOspfGeneralEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:nsOspfGeneralEntry.setStatus(_A)
_NsOspfRouterId_Type=RouterID
_NsOspfRouterId_Object=MibTableColumn
nsOspfRouterId=_NsOspfRouterId_Object((1,3,6,1,4,1,3224,18,2,1,1,1),_NsOspfRouterId_Type())
nsOspfRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfRouterId.setStatus(_A)
_NsOspfAdminStat_Type=Status
_NsOspfAdminStat_Object=MibTableColumn
nsOspfAdminStat=_NsOspfAdminStat_Object((1,3,6,1,4,1,3224,18,2,1,1,2),_NsOspfAdminStat_Type())
nsOspfAdminStat.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAdminStat.setStatus(_A)
class _NsOspfVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('version2',2))
_NsOspfVersionNumber_Type.__name__=_E
_NsOspfVersionNumber_Object=MibTableColumn
nsOspfVersionNumber=_NsOspfVersionNumber_Object((1,3,6,1,4,1,3224,18,2,1,1,3),_NsOspfVersionNumber_Type())
nsOspfVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVersionNumber.setStatus(_A)
_NsOspfAreaBdrRtrStatus_Type=TruthValue
_NsOspfAreaBdrRtrStatus_Object=MibTableColumn
nsOspfAreaBdrRtrStatus=_NsOspfAreaBdrRtrStatus_Object((1,3,6,1,4,1,3224,18,2,1,1,4),_NsOspfAreaBdrRtrStatus_Type())
nsOspfAreaBdrRtrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAreaBdrRtrStatus.setStatus(_A)
_NsOspfASBdrRtrStatus_Type=TruthValue
_NsOspfASBdrRtrStatus_Object=MibTableColumn
nsOspfASBdrRtrStatus=_NsOspfASBdrRtrStatus_Object((1,3,6,1,4,1,3224,18,2,1,1,5),_NsOspfASBdrRtrStatus_Type())
nsOspfASBdrRtrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfASBdrRtrStatus.setStatus(_A)
_NsOspfExternLsaCount_Type=Gauge32
_NsOspfExternLsaCount_Object=MibTableColumn
nsOspfExternLsaCount=_NsOspfExternLsaCount_Object((1,3,6,1,4,1,3224,18,2,1,1,6),_NsOspfExternLsaCount_Type())
nsOspfExternLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfExternLsaCount.setStatus(_A)
_NsOspfExternLsaCksumSum_Type=Integer32
_NsOspfExternLsaCksumSum_Object=MibTableColumn
nsOspfExternLsaCksumSum=_NsOspfExternLsaCksumSum_Object((1,3,6,1,4,1,3224,18,2,1,1,7),_NsOspfExternLsaCksumSum_Type())
nsOspfExternLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfExternLsaCksumSum.setStatus(_A)
_NsOspfTOSSupport_Type=TruthValue
_NsOspfTOSSupport_Object=MibTableColumn
nsOspfTOSSupport=_NsOspfTOSSupport_Object((1,3,6,1,4,1,3224,18,2,1,1,8),_NsOspfTOSSupport_Type())
nsOspfTOSSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfTOSSupport.setStatus(_A)
_NsOspfOriginateNewLsas_Type=Counter32
_NsOspfOriginateNewLsas_Object=MibTableColumn
nsOspfOriginateNewLsas=_NsOspfOriginateNewLsas_Object((1,3,6,1,4,1,3224,18,2,1,1,9),_NsOspfOriginateNewLsas_Type())
nsOspfOriginateNewLsas.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfOriginateNewLsas.setStatus(_A)
_NsOspfRxNewLsas_Type=Counter32
_NsOspfRxNewLsas_Object=MibTableColumn
nsOspfRxNewLsas=_NsOspfRxNewLsas_Object((1,3,6,1,4,1,3224,18,2,1,1,10),_NsOspfRxNewLsas_Type())
nsOspfRxNewLsas.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfRxNewLsas.setStatus(_A)
class _NsOspfExtLsdbLimit_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_NsOspfExtLsdbLimit_Type.__name__=_E
_NsOspfExtLsdbLimit_Object=MibTableColumn
nsOspfExtLsdbLimit=_NsOspfExtLsdbLimit_Object((1,3,6,1,4,1,3224,18,2,1,1,11),_NsOspfExtLsdbLimit_Type())
nsOspfExtLsdbLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfExtLsdbLimit.setStatus(_A)
class _NsOspfMulticastExtensions_Type(Integer32):defaultValue=0
_NsOspfMulticastExtensions_Type.__name__=_E
_NsOspfMulticastExtensions_Object=MibTableColumn
nsOspfMulticastExtensions=_NsOspfMulticastExtensions_Object((1,3,6,1,4,1,3224,18,2,1,1,12),_NsOspfMulticastExtensions_Type())
nsOspfMulticastExtensions.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfMulticastExtensions.setStatus(_A)
class _NsOspfExitOverflowInterval_Type(PositiveInteger):defaultValue=0
_NsOspfExitOverflowInterval_Type.__name__=_G
_NsOspfExitOverflowInterval_Object=MibTableColumn
nsOspfExitOverflowInterval=_NsOspfExitOverflowInterval_Object((1,3,6,1,4,1,3224,18,2,1,1,13),_NsOspfExitOverflowInterval_Type())
nsOspfExitOverflowInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfExitOverflowInterval.setStatus(_A)
_NsOspfDemandExtensions_Type=TruthValue
_NsOspfDemandExtensions_Object=MibTableColumn
nsOspfDemandExtensions=_NsOspfDemandExtensions_Object((1,3,6,1,4,1,3224,18,2,1,1,14),_NsOspfDemandExtensions_Type())
nsOspfDemandExtensions.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfDemandExtensions.setStatus(_A)
class _NsOspfGeneralVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsOspfGeneralVRID_Type.__name__=_E
_NsOspfGeneralVRID_Object=MibTableColumn
nsOspfGeneralVRID=_NsOspfGeneralVRID_Object((1,3,6,1,4,1,3224,18,2,1,1,15),_NsOspfGeneralVRID_Type())
nsOspfGeneralVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfGeneralVRID.setStatus(_A)
_NsOspfAreaTable_Object=MibTable
nsOspfAreaTable=_NsOspfAreaTable_Object((1,3,6,1,4,1,3224,18,2,2))
if mibBuilder.loadTexts:nsOspfAreaTable.setStatus(_A)
_NsOspfAreaEntry_Object=MibTableRow
nsOspfAreaEntry=_NsOspfAreaEntry_Object((1,3,6,1,4,1,3224,18,2,2,1))
nsOspfAreaEntry.setIndexNames((0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:nsOspfAreaEntry.setStatus(_A)
_NsOspfAreaId_Type=AreaID
_NsOspfAreaId_Object=MibTableColumn
nsOspfAreaId=_NsOspfAreaId_Object((1,3,6,1,4,1,3224,18,2,2,1,1),_NsOspfAreaId_Type())
nsOspfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAreaId.setStatus(_A)
class _NsOspfImportAsExtern_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('importExternal',1),('importNoExternal',2),('importNssa',3)))
_NsOspfImportAsExtern_Type.__name__=_E
_NsOspfImportAsExtern_Object=MibTableColumn
nsOspfImportAsExtern=_NsOspfImportAsExtern_Object((1,3,6,1,4,1,3224,18,2,2,1,3),_NsOspfImportAsExtern_Type())
nsOspfImportAsExtern.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfImportAsExtern.setStatus(_A)
_NsOspfSpfRuns_Type=Counter32
_NsOspfSpfRuns_Object=MibTableColumn
nsOspfSpfRuns=_NsOspfSpfRuns_Object((1,3,6,1,4,1,3224,18,2,2,1,4),_NsOspfSpfRuns_Type())
nsOspfSpfRuns.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfSpfRuns.setStatus(_A)
_NsOspfAreaBdrRtrCount_Type=Gauge32
_NsOspfAreaBdrRtrCount_Object=MibTableColumn
nsOspfAreaBdrRtrCount=_NsOspfAreaBdrRtrCount_Object((1,3,6,1,4,1,3224,18,2,2,1,5),_NsOspfAreaBdrRtrCount_Type())
nsOspfAreaBdrRtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAreaBdrRtrCount.setStatus(_A)
_NsOspfAsBdrRtrCount_Type=Gauge32
_NsOspfAsBdrRtrCount_Object=MibTableColumn
nsOspfAsBdrRtrCount=_NsOspfAsBdrRtrCount_Object((1,3,6,1,4,1,3224,18,2,2,1,6),_NsOspfAsBdrRtrCount_Type())
nsOspfAsBdrRtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAsBdrRtrCount.setStatus(_A)
_NsOspfAreaLsaCount_Type=Gauge32
_NsOspfAreaLsaCount_Object=MibTableColumn
nsOspfAreaLsaCount=_NsOspfAreaLsaCount_Object((1,3,6,1,4,1,3224,18,2,2,1,7),_NsOspfAreaLsaCount_Type())
nsOspfAreaLsaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAreaLsaCount.setStatus(_A)
class _NsOspfAreaLsaCksumSum_Type(Integer32):defaultValue=0
_NsOspfAreaLsaCksumSum_Type.__name__=_E
_NsOspfAreaLsaCksumSum_Object=MibTableColumn
nsOspfAreaLsaCksumSum=_NsOspfAreaLsaCksumSum_Object((1,3,6,1,4,1,3224,18,2,2,1,8),_NsOspfAreaLsaCksumSum_Type())
nsOspfAreaLsaCksumSum.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAreaLsaCksumSum.setStatus(_A)
class _NsOspfAreaSummary_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAreaSummary',1),('sendAreaSummary',2)))
_NsOspfAreaSummary_Type.__name__=_E
_NsOspfAreaSummary_Object=MibTableColumn
nsOspfAreaSummary=_NsOspfAreaSummary_Object((1,3,6,1,4,1,3224,18,2,2,1,9),_NsOspfAreaSummary_Type())
nsOspfAreaSummary.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfAreaSummary.setStatus(_A)
_NsOspfAreaStatus_Type=RowStatus
_NsOspfAreaStatus_Object=MibTableColumn
nsOspfAreaStatus=_NsOspfAreaStatus_Object((1,3,6,1,4,1,3224,18,2,2,1,10),_NsOspfAreaStatus_Type())
nsOspfAreaStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfAreaStatus.setStatus(_A)
class _NsOspfAreaVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsOspfAreaVRID_Type.__name__=_E
_NsOspfAreaVRID_Object=MibTableColumn
nsOspfAreaVRID=_NsOspfAreaVRID_Object((1,3,6,1,4,1,3224,18,2,2,1,11),_NsOspfAreaVRID_Type())
nsOspfAreaVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAreaVRID.setStatus(_A)
_NsOspfStubAreaTable_Object=MibTable
nsOspfStubAreaTable=_NsOspfStubAreaTable_Object((1,3,6,1,4,1,3224,18,2,3))
if mibBuilder.loadTexts:nsOspfStubAreaTable.setStatus(_A)
_NsOspfStubAreaEntry_Object=MibTableRow
nsOspfStubAreaEntry=_NsOspfStubAreaEntry_Object((1,3,6,1,4,1,3224,18,2,3,1))
nsOspfStubAreaEntry.setIndexNames((0,_C,_S),(0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:nsOspfStubAreaEntry.setStatus(_A)
_NsOspfStubAreaId_Type=AreaID
_NsOspfStubAreaId_Object=MibTableColumn
nsOspfStubAreaId=_NsOspfStubAreaId_Object((1,3,6,1,4,1,3224,18,2,3,1,1),_NsOspfStubAreaId_Type())
nsOspfStubAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfStubAreaId.setStatus(_A)
_NsOspfStubTOS_Type=TOSType
_NsOspfStubTOS_Object=MibTableColumn
nsOspfStubTOS=_NsOspfStubTOS_Object((1,3,6,1,4,1,3224,18,2,3,1,2),_NsOspfStubTOS_Type())
nsOspfStubTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfStubTOS.setStatus(_A)
_NsOspfStubMetric_Type=BigMetric
_NsOspfStubMetric_Object=MibTableColumn
nsOspfStubMetric=_NsOspfStubMetric_Object((1,3,6,1,4,1,3224,18,2,3,1,3),_NsOspfStubMetric_Type())
nsOspfStubMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfStubMetric.setStatus(_A)
_NsOspfStubStatus_Type=RowStatus
_NsOspfStubStatus_Object=MibTableColumn
nsOspfStubStatus=_NsOspfStubStatus_Object((1,3,6,1,4,1,3224,18,2,3,1,4),_NsOspfStubStatus_Type())
nsOspfStubStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfStubStatus.setStatus(_A)
class _NsOspfStubMetricType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nsOspfMetric',1),('comparableCost',2),('nonComparable',3)))
_NsOspfStubMetricType_Type.__name__=_E
_NsOspfStubMetricType_Object=MibTableColumn
nsOspfStubMetricType=_NsOspfStubMetricType_Object((1,3,6,1,4,1,3224,18,2,3,1,5),_NsOspfStubMetricType_Type())
nsOspfStubMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfStubMetricType.setStatus(_A)
class _NsOspfStubVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsOspfStubVRID_Type.__name__=_E
_NsOspfStubVRID_Object=MibTableColumn
nsOspfStubVRID=_NsOspfStubVRID_Object((1,3,6,1,4,1,3224,18,2,3,1,6),_NsOspfStubVRID_Type())
nsOspfStubVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfStubVRID.setStatus(_A)
_NsOspfLsdbTable_Object=MibTable
nsOspfLsdbTable=_NsOspfLsdbTable_Object((1,3,6,1,4,1,3224,18,2,4))
if mibBuilder.loadTexts:nsOspfLsdbTable.setStatus(_A)
_NsOspfLsdbEntry_Object=MibTableRow
nsOspfLsdbEntry=_NsOspfLsdbEntry_Object((1,3,6,1,4,1,3224,18,2,4,1))
nsOspfLsdbEntry.setIndexNames((0,_C,_V),(0,_C,_W),(0,_C,_X),(0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:nsOspfLsdbEntry.setStatus(_A)
_NsOspfLsdbAreaId_Type=AreaID
_NsOspfLsdbAreaId_Object=MibTableColumn
nsOspfLsdbAreaId=_NsOspfLsdbAreaId_Object((1,3,6,1,4,1,3224,18,2,4,1,1),_NsOspfLsdbAreaId_Type())
nsOspfLsdbAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfLsdbAreaId.setStatus(_A)
class _NsOspfLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('routerLink',1),('networkLink',2),(_a,3),('asSummaryLink',4),(_b,5),('multicastLink',6),(_c,7)))
_NsOspfLsdbType_Type.__name__=_E
_NsOspfLsdbType_Object=MibTableColumn
nsOspfLsdbType=_NsOspfLsdbType_Object((1,3,6,1,4,1,3224,18,2,4,1,2),_NsOspfLsdbType_Type())
nsOspfLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfLsdbType.setStatus(_A)
_NsOspfLsdbLsid_Type=IpAddress
_NsOspfLsdbLsid_Object=MibTableColumn
nsOspfLsdbLsid=_NsOspfLsdbLsid_Object((1,3,6,1,4,1,3224,18,2,4,1,3),_NsOspfLsdbLsid_Type())
nsOspfLsdbLsid.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfLsdbLsid.setStatus(_A)
_NsOspfLsdbRouterId_Type=RouterID
_NsOspfLsdbRouterId_Object=MibTableColumn
nsOspfLsdbRouterId=_NsOspfLsdbRouterId_Object((1,3,6,1,4,1,3224,18,2,4,1,4),_NsOspfLsdbRouterId_Type())
nsOspfLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfLsdbRouterId.setStatus(_A)
_NsOspfLsdbSequence_Type=Integer32
_NsOspfLsdbSequence_Object=MibTableColumn
nsOspfLsdbSequence=_NsOspfLsdbSequence_Object((1,3,6,1,4,1,3224,18,2,4,1,5),_NsOspfLsdbSequence_Type())
nsOspfLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfLsdbSequence.setStatus(_A)
_NsOspfLsdbAge_Type=Integer32
_NsOspfLsdbAge_Object=MibTableColumn
nsOspfLsdbAge=_NsOspfLsdbAge_Object((1,3,6,1,4,1,3224,18,2,4,1,6),_NsOspfLsdbAge_Type())
nsOspfLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfLsdbAge.setStatus(_A)
_NsOspfLsdbChecksum_Type=Integer32
_NsOspfLsdbChecksum_Object=MibTableColumn
nsOspfLsdbChecksum=_NsOspfLsdbChecksum_Object((1,3,6,1,4,1,3224,18,2,4,1,7),_NsOspfLsdbChecksum_Type())
nsOspfLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfLsdbChecksum.setStatus(_A)
class _NsOspfLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_NsOspfLsdbAdvertisement_Type.__name__=_F
_NsOspfLsdbAdvertisement_Object=MibTableColumn
nsOspfLsdbAdvertisement=_NsOspfLsdbAdvertisement_Object((1,3,6,1,4,1,3224,18,2,4,1,8),_NsOspfLsdbAdvertisement_Type())
nsOspfLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfLsdbAdvertisement.setStatus(_A)
class _NsOspfLsdbVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsOspfLsdbVRID_Type.__name__=_E
_NsOspfLsdbVRID_Object=MibTableColumn
nsOspfLsdbVRID=_NsOspfLsdbVRID_Object((1,3,6,1,4,1,3224,18,2,4,1,9),_NsOspfLsdbVRID_Type())
nsOspfLsdbVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfLsdbVRID.setStatus(_A)
_NsOspfHostTable_Object=MibTable
nsOspfHostTable=_NsOspfHostTable_Object((1,3,6,1,4,1,3224,18,2,6))
if mibBuilder.loadTexts:nsOspfHostTable.setStatus(_A)
_NsOspfHostEntry_Object=MibTableRow
nsOspfHostEntry=_NsOspfHostEntry_Object((1,3,6,1,4,1,3224,18,2,6,1))
nsOspfHostEntry.setIndexNames((0,_C,_d),(0,_C,_e),(0,_C,_f))
if mibBuilder.loadTexts:nsOspfHostEntry.setStatus(_A)
_NsOspfHostIpAddress_Type=IpAddress
_NsOspfHostIpAddress_Object=MibTableColumn
nsOspfHostIpAddress=_NsOspfHostIpAddress_Object((1,3,6,1,4,1,3224,18,2,6,1,1),_NsOspfHostIpAddress_Type())
nsOspfHostIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfHostIpAddress.setStatus(_A)
_NsOspfHostTOS_Type=TOSType
_NsOspfHostTOS_Object=MibTableColumn
nsOspfHostTOS=_NsOspfHostTOS_Object((1,3,6,1,4,1,3224,18,2,6,1,2),_NsOspfHostTOS_Type())
nsOspfHostTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfHostTOS.setStatus(_A)
_NsOspfHostMetric_Type=Metric
_NsOspfHostMetric_Object=MibTableColumn
nsOspfHostMetric=_NsOspfHostMetric_Object((1,3,6,1,4,1,3224,18,2,6,1,3),_NsOspfHostMetric_Type())
nsOspfHostMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfHostMetric.setStatus(_A)
_NsOspfHostStatus_Type=RowStatus
_NsOspfHostStatus_Object=MibTableColumn
nsOspfHostStatus=_NsOspfHostStatus_Object((1,3,6,1,4,1,3224,18,2,6,1,4),_NsOspfHostStatus_Type())
nsOspfHostStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfHostStatus.setStatus(_A)
_NsOspfHostAreaID_Type=AreaID
_NsOspfHostAreaID_Object=MibTableColumn
nsOspfHostAreaID=_NsOspfHostAreaID_Object((1,3,6,1,4,1,3224,18,2,6,1,5),_NsOspfHostAreaID_Type())
nsOspfHostAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfHostAreaID.setStatus(_A)
class _NsOspfHostVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsOspfHostVRID_Type.__name__=_E
_NsOspfHostVRID_Object=MibTableColumn
nsOspfHostVRID=_NsOspfHostVRID_Object((1,3,6,1,4,1,3224,18,2,6,1,6),_NsOspfHostVRID_Type())
nsOspfHostVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfHostVRID.setStatus(_A)
_NsOspfIfTable_Object=MibTable
nsOspfIfTable=_NsOspfIfTable_Object((1,3,6,1,4,1,3224,18,2,7))
if mibBuilder.loadTexts:nsOspfIfTable.setStatus(_A)
_NsOspfIfEntry_Object=MibTableRow
nsOspfIfEntry=_NsOspfIfEntry_Object((1,3,6,1,4,1,3224,18,2,7,1))
nsOspfIfEntry.setIndexNames((0,_C,_g),(0,_C,_h),(0,_C,_i))
if mibBuilder.loadTexts:nsOspfIfEntry.setStatus(_A)
_NsOspfIfIpAddress_Type=IpAddress
_NsOspfIfIpAddress_Object=MibTableColumn
nsOspfIfIpAddress=_NsOspfIfIpAddress_Object((1,3,6,1,4,1,3224,18,2,7,1,1),_NsOspfIfIpAddress_Type())
nsOspfIfIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfIfIpAddress.setStatus(_A)
_NsOspfAddressLessIf_Type=Integer32
_NsOspfAddressLessIf_Object=MibTableColumn
nsOspfAddressLessIf=_NsOspfAddressLessIf_Object((1,3,6,1,4,1,3224,18,2,7,1,2),_NsOspfAddressLessIf_Type())
nsOspfAddressLessIf.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAddressLessIf.setStatus(_A)
class _NsOspfIfAreaId_Type(AreaID):defaultHexValue=_I
_NsOspfIfAreaId_Type.__name__=_j
_NsOspfIfAreaId_Object=MibTableColumn
nsOspfIfAreaId=_NsOspfIfAreaId_Object((1,3,6,1,4,1,3224,18,2,7,1,3),_NsOspfIfAreaId_Type())
nsOspfIfAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfAreaId.setStatus(_A)
class _NsOspfIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*(('broadcast',1),('nbma',2),(_L,3),('pointToMultipoint',5)))
_NsOspfIfType_Type.__name__=_E
_NsOspfIfType_Object=MibTableColumn
nsOspfIfType=_NsOspfIfType_Object((1,3,6,1,4,1,3224,18,2,7,1,4),_NsOspfIfType_Type())
nsOspfIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfType.setStatus(_A)
class _NsOspfIfAdminStat_Type(Status):defaultValue=1
_NsOspfIfAdminStat_Type.__name__=_k
_NsOspfIfAdminStat_Object=MibTableColumn
nsOspfIfAdminStat=_NsOspfIfAdminStat_Object((1,3,6,1,4,1,3224,18,2,7,1,5),_NsOspfIfAdminStat_Type())
nsOspfIfAdminStat.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfAdminStat.setStatus(_A)
class _NsOspfIfRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_NsOspfIfRtrPriority_Type.__name__=_M
_NsOspfIfRtrPriority_Object=MibTableColumn
nsOspfIfRtrPriority=_NsOspfIfRtrPriority_Object((1,3,6,1,4,1,3224,18,2,7,1,6),_NsOspfIfRtrPriority_Type())
nsOspfIfRtrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfRtrPriority.setStatus(_A)
class _NsOspfIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_NsOspfIfTransitDelay_Type.__name__=_H
_NsOspfIfTransitDelay_Object=MibTableColumn
nsOspfIfTransitDelay=_NsOspfIfTransitDelay_Object((1,3,6,1,4,1,3224,18,2,7,1,7),_NsOspfIfTransitDelay_Type())
nsOspfIfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfTransitDelay.setStatus(_A)
class _NsOspfIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_NsOspfIfRetransInterval_Type.__name__=_H
_NsOspfIfRetransInterval_Object=MibTableColumn
nsOspfIfRetransInterval=_NsOspfIfRetransInterval_Object((1,3,6,1,4,1,3224,18,2,7,1,8),_NsOspfIfRetransInterval_Type())
nsOspfIfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfRetransInterval.setStatus(_A)
class _NsOspfIfHelloInterval_Type(HelloRange):defaultValue=10
_NsOspfIfHelloInterval_Type.__name__=_N
_NsOspfIfHelloInterval_Object=MibTableColumn
nsOspfIfHelloInterval=_NsOspfIfHelloInterval_Object((1,3,6,1,4,1,3224,18,2,7,1,9),_NsOspfIfHelloInterval_Type())
nsOspfIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfHelloInterval.setStatus(_A)
class _NsOspfIfRtrDeadInterval_Type(PositiveInteger):defaultValue=40
_NsOspfIfRtrDeadInterval_Type.__name__=_G
_NsOspfIfRtrDeadInterval_Object=MibTableColumn
nsOspfIfRtrDeadInterval=_NsOspfIfRtrDeadInterval_Object((1,3,6,1,4,1,3224,18,2,7,1,10),_NsOspfIfRtrDeadInterval_Type())
nsOspfIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfRtrDeadInterval.setStatus(_A)
class _NsOspfIfPollInterval_Type(PositiveInteger):defaultValue=120
_NsOspfIfPollInterval_Type.__name__=_G
_NsOspfIfPollInterval_Object=MibTableColumn
nsOspfIfPollInterval=_NsOspfIfPollInterval_Object((1,3,6,1,4,1,3224,18,2,7,1,11),_NsOspfIfPollInterval_Type())
nsOspfIfPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfPollInterval.setStatus(_A)
class _NsOspfIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,1),('loopback',2),('waiting',3),(_L,4),('designatedRouter',5),('backupDesignatedRouter',6),('otherDesignatedRouter',7)))
_NsOspfIfState_Type.__name__=_E
_NsOspfIfState_Object=MibTableColumn
nsOspfIfState=_NsOspfIfState_Object((1,3,6,1,4,1,3224,18,2,7,1,12),_NsOspfIfState_Type())
nsOspfIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfIfState.setStatus(_A)
class _NsOspfIfDesignatedRouter_Type(IpAddress):defaultHexValue=_I
_NsOspfIfDesignatedRouter_Type.__name__=_K
_NsOspfIfDesignatedRouter_Object=MibTableColumn
nsOspfIfDesignatedRouter=_NsOspfIfDesignatedRouter_Object((1,3,6,1,4,1,3224,18,2,7,1,13),_NsOspfIfDesignatedRouter_Type())
nsOspfIfDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfIfDesignatedRouter.setStatus(_A)
class _NsOspfIfBackupDesignatedRouter_Type(IpAddress):defaultHexValue=_I
_NsOspfIfBackupDesignatedRouter_Type.__name__=_K
_NsOspfIfBackupDesignatedRouter_Object=MibTableColumn
nsOspfIfBackupDesignatedRouter=_NsOspfIfBackupDesignatedRouter_Object((1,3,6,1,4,1,3224,18,2,7,1,14),_NsOspfIfBackupDesignatedRouter_Type())
nsOspfIfBackupDesignatedRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfIfBackupDesignatedRouter.setStatus(_A)
_NsOspfIfEvents_Type=Counter32
_NsOspfIfEvents_Object=MibTableColumn
nsOspfIfEvents=_NsOspfIfEvents_Object((1,3,6,1,4,1,3224,18,2,7,1,15),_NsOspfIfEvents_Type())
nsOspfIfEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfIfEvents.setStatus(_A)
class _NsOspfIfAuthKey_Type(OctetString):defaultHexValue=_l;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_NsOspfIfAuthKey_Type.__name__=_F
_NsOspfIfAuthKey_Object=MibTableColumn
nsOspfIfAuthKey=_NsOspfIfAuthKey_Object((1,3,6,1,4,1,3224,18,2,7,1,16),_NsOspfIfAuthKey_Type())
nsOspfIfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfAuthKey.setStatus(_A)
_NsOspfIfStatus_Type=RowStatus
_NsOspfIfStatus_Object=MibTableColumn
nsOspfIfStatus=_NsOspfIfStatus_Object((1,3,6,1,4,1,3224,18,2,7,1,17),_NsOspfIfStatus_Type())
nsOspfIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfStatus.setStatus(_A)
class _NsOspfIfMulticastForwarding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('blocked',1),('multicast',2),('unicast',3)))
_NsOspfIfMulticastForwarding_Type.__name__=_E
_NsOspfIfMulticastForwarding_Object=MibTableColumn
nsOspfIfMulticastForwarding=_NsOspfIfMulticastForwarding_Object((1,3,6,1,4,1,3224,18,2,7,1,18),_NsOspfIfMulticastForwarding_Type())
nsOspfIfMulticastForwarding.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfMulticastForwarding.setStatus(_A)
class _NsOspfIfDemand_Type(TruthValue):defaultValue=2
_NsOspfIfDemand_Type.__name__=_O
_NsOspfIfDemand_Object=MibTableColumn
nsOspfIfDemand=_NsOspfIfDemand_Object((1,3,6,1,4,1,3224,18,2,7,1,19),_NsOspfIfDemand_Type())
nsOspfIfDemand.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfDemand.setStatus(_A)
class _NsOspfIfAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NsOspfIfAuthType_Type.__name__=_E
_NsOspfIfAuthType_Object=MibTableColumn
nsOspfIfAuthType=_NsOspfIfAuthType_Object((1,3,6,1,4,1,3224,18,2,7,1,20),_NsOspfIfAuthType_Type())
nsOspfIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfAuthType.setStatus(_A)
class _NsOspfIfVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsOspfIfVRID_Type.__name__=_E
_NsOspfIfVRID_Object=MibTableColumn
nsOspfIfVRID=_NsOspfIfVRID_Object((1,3,6,1,4,1,3224,18,2,7,1,21),_NsOspfIfVRID_Type())
nsOspfIfVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfIfVRID.setStatus(_A)
_NsOspfIfMetricTable_Object=MibTable
nsOspfIfMetricTable=_NsOspfIfMetricTable_Object((1,3,6,1,4,1,3224,18,2,8))
if mibBuilder.loadTexts:nsOspfIfMetricTable.setStatus(_A)
_NsOspfIfMetricEntry_Object=MibTableRow
nsOspfIfMetricEntry=_NsOspfIfMetricEntry_Object((1,3,6,1,4,1,3224,18,2,8,1))
nsOspfIfMetricEntry.setIndexNames((0,_C,_m),(0,_C,_n),(0,_C,_o),(0,_C,_p))
if mibBuilder.loadTexts:nsOspfIfMetricEntry.setStatus(_A)
_NsOspfIfMetricIpAddress_Type=IpAddress
_NsOspfIfMetricIpAddress_Object=MibTableColumn
nsOspfIfMetricIpAddress=_NsOspfIfMetricIpAddress_Object((1,3,6,1,4,1,3224,18,2,8,1,1),_NsOspfIfMetricIpAddress_Type())
nsOspfIfMetricIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfIfMetricIpAddress.setStatus(_A)
_NsOspfIfMetricAddressLessIf_Type=Integer32
_NsOspfIfMetricAddressLessIf_Object=MibTableColumn
nsOspfIfMetricAddressLessIf=_NsOspfIfMetricAddressLessIf_Object((1,3,6,1,4,1,3224,18,2,8,1,2),_NsOspfIfMetricAddressLessIf_Type())
nsOspfIfMetricAddressLessIf.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfIfMetricAddressLessIf.setStatus(_A)
_NsOspfIfMetricTOS_Type=TOSType
_NsOspfIfMetricTOS_Object=MibTableColumn
nsOspfIfMetricTOS=_NsOspfIfMetricTOS_Object((1,3,6,1,4,1,3224,18,2,8,1,3),_NsOspfIfMetricTOS_Type())
nsOspfIfMetricTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfIfMetricTOS.setStatus(_A)
_NsOspfIfMetricValue_Type=Metric
_NsOspfIfMetricValue_Object=MibTableColumn
nsOspfIfMetricValue=_NsOspfIfMetricValue_Object((1,3,6,1,4,1,3224,18,2,8,1,4),_NsOspfIfMetricValue_Type())
nsOspfIfMetricValue.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfMetricValue.setStatus(_A)
_NsOspfIfMetricStatus_Type=RowStatus
_NsOspfIfMetricStatus_Object=MibTableColumn
nsOspfIfMetricStatus=_NsOspfIfMetricStatus_Object((1,3,6,1,4,1,3224,18,2,8,1,5),_NsOspfIfMetricStatus_Type())
nsOspfIfMetricStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfIfMetricStatus.setStatus(_A)
class _NsOspfIfMetricVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsOspfIfMetricVRID_Type.__name__=_E
_NsOspfIfMetricVRID_Object=MibTableColumn
nsOspfIfMetricVRID=_NsOspfIfMetricVRID_Object((1,3,6,1,4,1,3224,18,2,8,1,6),_NsOspfIfMetricVRID_Type())
nsOspfIfMetricVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfIfMetricVRID.setStatus(_A)
_NsOspfVirtIfTable_Object=MibTable
nsOspfVirtIfTable=_NsOspfVirtIfTable_Object((1,3,6,1,4,1,3224,18,2,9))
if mibBuilder.loadTexts:nsOspfVirtIfTable.setStatus(_A)
_NsOspfVirtIfEntry_Object=MibTableRow
nsOspfVirtIfEntry=_NsOspfVirtIfEntry_Object((1,3,6,1,4,1,3224,18,2,9,1))
nsOspfVirtIfEntry.setIndexNames((0,_C,_q),(0,_C,_r),(0,_C,_s))
if mibBuilder.loadTexts:nsOspfVirtIfEntry.setStatus(_A)
_NsOspfVirtIfAreaId_Type=AreaID
_NsOspfVirtIfAreaId_Object=MibTableColumn
nsOspfVirtIfAreaId=_NsOspfVirtIfAreaId_Object((1,3,6,1,4,1,3224,18,2,9,1,1),_NsOspfVirtIfAreaId_Type())
nsOspfVirtIfAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtIfAreaId.setStatus(_A)
_NsOspfVirtIfNeighbor_Type=RouterID
_NsOspfVirtIfNeighbor_Object=MibTableColumn
nsOspfVirtIfNeighbor=_NsOspfVirtIfNeighbor_Object((1,3,6,1,4,1,3224,18,2,9,1,2),_NsOspfVirtIfNeighbor_Type())
nsOspfVirtIfNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtIfNeighbor.setStatus(_A)
class _NsOspfVirtIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_NsOspfVirtIfTransitDelay_Type.__name__=_H
_NsOspfVirtIfTransitDelay_Object=MibTableColumn
nsOspfVirtIfTransitDelay=_NsOspfVirtIfTransitDelay_Object((1,3,6,1,4,1,3224,18,2,9,1,3),_NsOspfVirtIfTransitDelay_Type())
nsOspfVirtIfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfVirtIfTransitDelay.setStatus(_A)
class _NsOspfVirtIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_NsOspfVirtIfRetransInterval_Type.__name__=_H
_NsOspfVirtIfRetransInterval_Object=MibTableColumn
nsOspfVirtIfRetransInterval=_NsOspfVirtIfRetransInterval_Object((1,3,6,1,4,1,3224,18,2,9,1,4),_NsOspfVirtIfRetransInterval_Type())
nsOspfVirtIfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfVirtIfRetransInterval.setStatus(_A)
class _NsOspfVirtIfHelloInterval_Type(HelloRange):defaultValue=10
_NsOspfVirtIfHelloInterval_Type.__name__=_N
_NsOspfVirtIfHelloInterval_Object=MibTableColumn
nsOspfVirtIfHelloInterval=_NsOspfVirtIfHelloInterval_Object((1,3,6,1,4,1,3224,18,2,9,1,5),_NsOspfVirtIfHelloInterval_Type())
nsOspfVirtIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfVirtIfHelloInterval.setStatus(_A)
class _NsOspfVirtIfRtrDeadInterval_Type(PositiveInteger):defaultValue=60
_NsOspfVirtIfRtrDeadInterval_Type.__name__=_G
_NsOspfVirtIfRtrDeadInterval_Object=MibTableColumn
nsOspfVirtIfRtrDeadInterval=_NsOspfVirtIfRtrDeadInterval_Object((1,3,6,1,4,1,3224,18,2,9,1,6),_NsOspfVirtIfRtrDeadInterval_Type())
nsOspfVirtIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfVirtIfRtrDeadInterval.setStatus(_A)
class _NsOspfVirtIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_J,1),(_L,4)))
_NsOspfVirtIfState_Type.__name__=_E
_NsOspfVirtIfState_Object=MibTableColumn
nsOspfVirtIfState=_NsOspfVirtIfState_Object((1,3,6,1,4,1,3224,18,2,9,1,7),_NsOspfVirtIfState_Type())
nsOspfVirtIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtIfState.setStatus(_A)
_NsOspfVirtIfEvents_Type=Counter32
_NsOspfVirtIfEvents_Object=MibTableColumn
nsOspfVirtIfEvents=_NsOspfVirtIfEvents_Object((1,3,6,1,4,1,3224,18,2,9,1,8),_NsOspfVirtIfEvents_Type())
nsOspfVirtIfEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtIfEvents.setStatus(_A)
class _NsOspfVirtIfAuthKey_Type(OctetString):defaultHexValue=_l;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_NsOspfVirtIfAuthKey_Type.__name__=_F
_NsOspfVirtIfAuthKey_Object=MibTableColumn
nsOspfVirtIfAuthKey=_NsOspfVirtIfAuthKey_Object((1,3,6,1,4,1,3224,18,2,9,1,9),_NsOspfVirtIfAuthKey_Type())
nsOspfVirtIfAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfVirtIfAuthKey.setStatus(_A)
_NsOspfVirtIfStatus_Type=RowStatus
_NsOspfVirtIfStatus_Object=MibTableColumn
nsOspfVirtIfStatus=_NsOspfVirtIfStatus_Object((1,3,6,1,4,1,3224,18,2,9,1,10),_NsOspfVirtIfStatus_Type())
nsOspfVirtIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfVirtIfStatus.setStatus(_A)
class _NsOspfVirtIfAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NsOspfVirtIfAuthType_Type.__name__=_E
_NsOspfVirtIfAuthType_Object=MibTableColumn
nsOspfVirtIfAuthType=_NsOspfVirtIfAuthType_Object((1,3,6,1,4,1,3224,18,2,9,1,11),_NsOspfVirtIfAuthType_Type())
nsOspfVirtIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfVirtIfAuthType.setStatus(_A)
class _NsOspfVirtIfVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsOspfVirtIfVRID_Type.__name__=_E
_NsOspfVirtIfVRID_Object=MibTableColumn
nsOspfVirtIfVRID=_NsOspfVirtIfVRID_Object((1,3,6,1,4,1,3224,18,2,9,1,12),_NsOspfVirtIfVRID_Type())
nsOspfVirtIfVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtIfVRID.setStatus(_A)
_NsOspfNbrTable_Object=MibTable
nsOspfNbrTable=_NsOspfNbrTable_Object((1,3,6,1,4,1,3224,18,2,10))
if mibBuilder.loadTexts:nsOspfNbrTable.setStatus(_A)
_NsOspfNbrEntry_Object=MibTableRow
nsOspfNbrEntry=_NsOspfNbrEntry_Object((1,3,6,1,4,1,3224,18,2,10,1))
nsOspfNbrEntry.setIndexNames((0,_C,_t),(0,_C,_u),(0,_C,_v))
if mibBuilder.loadTexts:nsOspfNbrEntry.setStatus(_A)
_NsOspfNbrIpAddr_Type=IpAddress
_NsOspfNbrIpAddr_Object=MibTableColumn
nsOspfNbrIpAddr=_NsOspfNbrIpAddr_Object((1,3,6,1,4,1,3224,18,2,10,1,1),_NsOspfNbrIpAddr_Type())
nsOspfNbrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfNbrIpAddr.setStatus(_A)
_NsOspfNbrAddressLessIndex_Type=InterfaceIndex
_NsOspfNbrAddressLessIndex_Object=MibTableColumn
nsOspfNbrAddressLessIndex=_NsOspfNbrAddressLessIndex_Object((1,3,6,1,4,1,3224,18,2,10,1,2),_NsOspfNbrAddressLessIndex_Type())
nsOspfNbrAddressLessIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfNbrAddressLessIndex.setStatus(_A)
class _NsOspfNbrRtrId_Type(RouterID):defaultHexValue=_I
_NsOspfNbrRtrId_Type.__name__=_w
_NsOspfNbrRtrId_Object=MibTableColumn
nsOspfNbrRtrId=_NsOspfNbrRtrId_Object((1,3,6,1,4,1,3224,18,2,10,1,3),_NsOspfNbrRtrId_Type())
nsOspfNbrRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfNbrRtrId.setStatus(_A)
class _NsOspfNbrOptions_Type(Integer32):defaultValue=0
_NsOspfNbrOptions_Type.__name__=_E
_NsOspfNbrOptions_Object=MibTableColumn
nsOspfNbrOptions=_NsOspfNbrOptions_Object((1,3,6,1,4,1,3224,18,2,10,1,4),_NsOspfNbrOptions_Type())
nsOspfNbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfNbrOptions.setStatus(_A)
class _NsOspfNbrPriority_Type(DesignatedRouterPriority):defaultValue=1
_NsOspfNbrPriority_Type.__name__=_M
_NsOspfNbrPriority_Object=MibTableColumn
nsOspfNbrPriority=_NsOspfNbrPriority_Object((1,3,6,1,4,1,3224,18,2,10,1,5),_NsOspfNbrPriority_Type())
nsOspfNbrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfNbrPriority.setStatus(_A)
class _NsOspfNbrState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_x,2),('init',3),(_y,4),(_z,5),('exchange',6),('loading',7),('full',8)))
_NsOspfNbrState_Type.__name__=_E
_NsOspfNbrState_Object=MibTableColumn
nsOspfNbrState=_NsOspfNbrState_Object((1,3,6,1,4,1,3224,18,2,10,1,6),_NsOspfNbrState_Type())
nsOspfNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfNbrState.setStatus(_A)
_NsOspfNbrEvents_Type=Counter32
_NsOspfNbrEvents_Object=MibTableColumn
nsOspfNbrEvents=_NsOspfNbrEvents_Object((1,3,6,1,4,1,3224,18,2,10,1,7),_NsOspfNbrEvents_Type())
nsOspfNbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfNbrEvents.setStatus(_A)
_NsOspfNbrLsRetransQLen_Type=Gauge32
_NsOspfNbrLsRetransQLen_Object=MibTableColumn
nsOspfNbrLsRetransQLen=_NsOspfNbrLsRetransQLen_Object((1,3,6,1,4,1,3224,18,2,10,1,8),_NsOspfNbrLsRetransQLen_Type())
nsOspfNbrLsRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfNbrLsRetransQLen.setStatus(_A)
_NsOspfNbmaNbrStatus_Type=RowStatus
_NsOspfNbmaNbrStatus_Object=MibTableColumn
nsOspfNbmaNbrStatus=_NsOspfNbmaNbrStatus_Object((1,3,6,1,4,1,3224,18,2,10,1,9),_NsOspfNbmaNbrStatus_Type())
nsOspfNbmaNbrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfNbmaNbrStatus.setStatus(_A)
class _NsOspfNbmaNbrPermanence_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('permanent',2)))
_NsOspfNbmaNbrPermanence_Type.__name__=_E
_NsOspfNbmaNbrPermanence_Object=MibTableColumn
nsOspfNbmaNbrPermanence=_NsOspfNbmaNbrPermanence_Object((1,3,6,1,4,1,3224,18,2,10,1,10),_NsOspfNbmaNbrPermanence_Type())
nsOspfNbmaNbrPermanence.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfNbmaNbrPermanence.setStatus(_A)
_NsOspfNbrHelloSuppressed_Type=TruthValue
_NsOspfNbrHelloSuppressed_Object=MibTableColumn
nsOspfNbrHelloSuppressed=_NsOspfNbrHelloSuppressed_Object((1,3,6,1,4,1,3224,18,2,10,1,11),_NsOspfNbrHelloSuppressed_Type())
nsOspfNbrHelloSuppressed.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfNbrHelloSuppressed.setStatus(_A)
class _NsOspfNbrVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsOspfNbrVRID_Type.__name__=_E
_NsOspfNbrVRID_Object=MibTableColumn
nsOspfNbrVRID=_NsOspfNbrVRID_Object((1,3,6,1,4,1,3224,18,2,10,1,12),_NsOspfNbrVRID_Type())
nsOspfNbrVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfNbrVRID.setStatus(_A)
_NsOspfVirtNbrTable_Object=MibTable
nsOspfVirtNbrTable=_NsOspfVirtNbrTable_Object((1,3,6,1,4,1,3224,18,2,11))
if mibBuilder.loadTexts:nsOspfVirtNbrTable.setStatus(_A)
_NsOspfVirtNbrEntry_Object=MibTableRow
nsOspfVirtNbrEntry=_NsOspfVirtNbrEntry_Object((1,3,6,1,4,1,3224,18,2,11,1))
nsOspfVirtNbrEntry.setIndexNames((0,_C,_A0),(0,_C,_A1),(0,_C,_A2))
if mibBuilder.loadTexts:nsOspfVirtNbrEntry.setStatus(_A)
_NsOspfVirtNbrArea_Type=AreaID
_NsOspfVirtNbrArea_Object=MibTableColumn
nsOspfVirtNbrArea=_NsOspfVirtNbrArea_Object((1,3,6,1,4,1,3224,18,2,11,1,1),_NsOspfVirtNbrArea_Type())
nsOspfVirtNbrArea.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtNbrArea.setStatus(_A)
_NsOspfVirtNbrRtrId_Type=RouterID
_NsOspfVirtNbrRtrId_Object=MibTableColumn
nsOspfVirtNbrRtrId=_NsOspfVirtNbrRtrId_Object((1,3,6,1,4,1,3224,18,2,11,1,2),_NsOspfVirtNbrRtrId_Type())
nsOspfVirtNbrRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtNbrRtrId.setStatus(_A)
_NsOspfVirtNbrIpAddr_Type=IpAddress
_NsOspfVirtNbrIpAddr_Object=MibTableColumn
nsOspfVirtNbrIpAddr=_NsOspfVirtNbrIpAddr_Object((1,3,6,1,4,1,3224,18,2,11,1,3),_NsOspfVirtNbrIpAddr_Type())
nsOspfVirtNbrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtNbrIpAddr.setStatus(_A)
_NsOspfVirtNbrOptions_Type=Integer32
_NsOspfVirtNbrOptions_Object=MibTableColumn
nsOspfVirtNbrOptions=_NsOspfVirtNbrOptions_Object((1,3,6,1,4,1,3224,18,2,11,1,4),_NsOspfVirtNbrOptions_Type())
nsOspfVirtNbrOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtNbrOptions.setStatus(_A)
class _NsOspfVirtNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_x,2),('init',3),(_y,4),(_z,5),('exchange',6),('loading',7),('full',8)))
_NsOspfVirtNbrState_Type.__name__=_E
_NsOspfVirtNbrState_Object=MibTableColumn
nsOspfVirtNbrState=_NsOspfVirtNbrState_Object((1,3,6,1,4,1,3224,18,2,11,1,5),_NsOspfVirtNbrState_Type())
nsOspfVirtNbrState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtNbrState.setStatus(_A)
_NsOspfVirtNbrEvents_Type=Counter32
_NsOspfVirtNbrEvents_Object=MibTableColumn
nsOspfVirtNbrEvents=_NsOspfVirtNbrEvents_Object((1,3,6,1,4,1,3224,18,2,11,1,6),_NsOspfVirtNbrEvents_Type())
nsOspfVirtNbrEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtNbrEvents.setStatus(_A)
_NsOspfVirtNbrLsRetransQLen_Type=Gauge32
_NsOspfVirtNbrLsRetransQLen_Object=MibTableColumn
nsOspfVirtNbrLsRetransQLen=_NsOspfVirtNbrLsRetransQLen_Object((1,3,6,1,4,1,3224,18,2,11,1,7),_NsOspfVirtNbrLsRetransQLen_Type())
nsOspfVirtNbrLsRetransQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtNbrLsRetransQLen.setStatus(_A)
_NsOspfVirtNbrHelloSuppressed_Type=TruthValue
_NsOspfVirtNbrHelloSuppressed_Object=MibTableColumn
nsOspfVirtNbrHelloSuppressed=_NsOspfVirtNbrHelloSuppressed_Object((1,3,6,1,4,1,3224,18,2,11,1,8),_NsOspfVirtNbrHelloSuppressed_Type())
nsOspfVirtNbrHelloSuppressed.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtNbrHelloSuppressed.setStatus(_A)
class _NsOspfVirtNbrVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsOspfVirtNbrVRID_Type.__name__=_E
_NsOspfVirtNbrVRID_Object=MibTableColumn
nsOspfVirtNbrVRID=_NsOspfVirtNbrVRID_Object((1,3,6,1,4,1,3224,18,2,11,1,9),_NsOspfVirtNbrVRID_Type())
nsOspfVirtNbrVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfVirtNbrVRID.setStatus(_A)
_NsOspfExtLsdbTable_Object=MibTable
nsOspfExtLsdbTable=_NsOspfExtLsdbTable_Object((1,3,6,1,4,1,3224,18,2,12))
if mibBuilder.loadTexts:nsOspfExtLsdbTable.setStatus(_A)
_NsOspfExtLsdbEntry_Object=MibTableRow
nsOspfExtLsdbEntry=_NsOspfExtLsdbEntry_Object((1,3,6,1,4,1,3224,18,2,12,1))
nsOspfExtLsdbEntry.setIndexNames((0,_C,_A3),(0,_C,_A4),(0,_C,_A5),(0,_C,_A6))
if mibBuilder.loadTexts:nsOspfExtLsdbEntry.setStatus(_A)
class _NsOspfExtLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues((_b,5))
_NsOspfExtLsdbType_Type.__name__=_E
_NsOspfExtLsdbType_Object=MibTableColumn
nsOspfExtLsdbType=_NsOspfExtLsdbType_Object((1,3,6,1,4,1,3224,18,2,12,1,1),_NsOspfExtLsdbType_Type())
nsOspfExtLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfExtLsdbType.setStatus(_A)
_NsOspfExtLsdbLsid_Type=IpAddress
_NsOspfExtLsdbLsid_Object=MibTableColumn
nsOspfExtLsdbLsid=_NsOspfExtLsdbLsid_Object((1,3,6,1,4,1,3224,18,2,12,1,2),_NsOspfExtLsdbLsid_Type())
nsOspfExtLsdbLsid.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfExtLsdbLsid.setStatus(_A)
_NsOspfExtLsdbRouterId_Type=RouterID
_NsOspfExtLsdbRouterId_Object=MibTableColumn
nsOspfExtLsdbRouterId=_NsOspfExtLsdbRouterId_Object((1,3,6,1,4,1,3224,18,2,12,1,3),_NsOspfExtLsdbRouterId_Type())
nsOspfExtLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfExtLsdbRouterId.setStatus(_A)
_NsOspfExtLsdbSequence_Type=Integer32
_NsOspfExtLsdbSequence_Object=MibTableColumn
nsOspfExtLsdbSequence=_NsOspfExtLsdbSequence_Object((1,3,6,1,4,1,3224,18,2,12,1,4),_NsOspfExtLsdbSequence_Type())
nsOspfExtLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfExtLsdbSequence.setStatus(_A)
_NsOspfExtLsdbAge_Type=Integer32
_NsOspfExtLsdbAge_Object=MibTableColumn
nsOspfExtLsdbAge=_NsOspfExtLsdbAge_Object((1,3,6,1,4,1,3224,18,2,12,1,5),_NsOspfExtLsdbAge_Type())
nsOspfExtLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfExtLsdbAge.setStatus(_A)
_NsOspfExtLsdbChecksum_Type=Integer32
_NsOspfExtLsdbChecksum_Object=MibTableColumn
nsOspfExtLsdbChecksum=_NsOspfExtLsdbChecksum_Object((1,3,6,1,4,1,3224,18,2,12,1,6),_NsOspfExtLsdbChecksum_Type())
nsOspfExtLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfExtLsdbChecksum.setStatus(_A)
class _NsOspfExtLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(36,36));fixedLength=36
_NsOspfExtLsdbAdvertisement_Type.__name__=_F
_NsOspfExtLsdbAdvertisement_Object=MibTableColumn
nsOspfExtLsdbAdvertisement=_NsOspfExtLsdbAdvertisement_Object((1,3,6,1,4,1,3224,18,2,12,1,7),_NsOspfExtLsdbAdvertisement_Type())
nsOspfExtLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfExtLsdbAdvertisement.setStatus(_A)
class _NsOspfExtLsdbVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsOspfExtLsdbVRID_Type.__name__=_E
_NsOspfExtLsdbVRID_Object=MibTableColumn
nsOspfExtLsdbVRID=_NsOspfExtLsdbVRID_Object((1,3,6,1,4,1,3224,18,2,12,1,8),_NsOspfExtLsdbVRID_Type())
nsOspfExtLsdbVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfExtLsdbVRID.setStatus(_A)
_NsOspfAreaAggregateTable_Object=MibTable
nsOspfAreaAggregateTable=_NsOspfAreaAggregateTable_Object((1,3,6,1,4,1,3224,18,2,14))
if mibBuilder.loadTexts:nsOspfAreaAggregateTable.setStatus(_A)
_NsOspfAreaAggregateEntry_Object=MibTableRow
nsOspfAreaAggregateEntry=_NsOspfAreaAggregateEntry_Object((1,3,6,1,4,1,3224,18,2,14,1))
nsOspfAreaAggregateEntry.setIndexNames((0,_C,_A7),(0,_C,_A8),(0,_C,_A9),(0,_C,_AA),(0,_C,_AB))
if mibBuilder.loadTexts:nsOspfAreaAggregateEntry.setStatus(_A)
_NsOspfAreaAggregateAreaID_Type=AreaID
_NsOspfAreaAggregateAreaID_Object=MibTableColumn
nsOspfAreaAggregateAreaID=_NsOspfAreaAggregateAreaID_Object((1,3,6,1,4,1,3224,18,2,14,1,1),_NsOspfAreaAggregateAreaID_Type())
nsOspfAreaAggregateAreaID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAreaAggregateAreaID.setStatus(_A)
class _NsOspfAreaAggregateLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,7)));namedValues=NamedValues(*((_a,3),(_c,7)))
_NsOspfAreaAggregateLsdbType_Type.__name__=_E
_NsOspfAreaAggregateLsdbType_Object=MibTableColumn
nsOspfAreaAggregateLsdbType=_NsOspfAreaAggregateLsdbType_Object((1,3,6,1,4,1,3224,18,2,14,1,2),_NsOspfAreaAggregateLsdbType_Type())
nsOspfAreaAggregateLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAreaAggregateLsdbType.setStatus(_A)
_NsOspfAreaAggregateNet_Type=IpAddress
_NsOspfAreaAggregateNet_Object=MibTableColumn
nsOspfAreaAggregateNet=_NsOspfAreaAggregateNet_Object((1,3,6,1,4,1,3224,18,2,14,1,3),_NsOspfAreaAggregateNet_Type())
nsOspfAreaAggregateNet.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAreaAggregateNet.setStatus(_A)
_NsOspfAreaAggregateMask_Type=IpAddress
_NsOspfAreaAggregateMask_Object=MibTableColumn
nsOspfAreaAggregateMask=_NsOspfAreaAggregateMask_Object((1,3,6,1,4,1,3224,18,2,14,1,4),_NsOspfAreaAggregateMask_Type())
nsOspfAreaAggregateMask.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAreaAggregateMask.setStatus(_A)
_NsOspfAreaAggregateStatus_Type=RowStatus
_NsOspfAreaAggregateStatus_Object=MibTableColumn
nsOspfAreaAggregateStatus=_NsOspfAreaAggregateStatus_Object((1,3,6,1,4,1,3224,18,2,14,1,5),_NsOspfAreaAggregateStatus_Type())
nsOspfAreaAggregateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfAreaAggregateStatus.setStatus(_A)
class _NsOspfAreaAggregateEffect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('advertiseMatching',1),('doNotAdvertiseMatching',2)))
_NsOspfAreaAggregateEffect_Type.__name__=_E
_NsOspfAreaAggregateEffect_Object=MibTableColumn
nsOspfAreaAggregateEffect=_NsOspfAreaAggregateEffect_Object((1,3,6,1,4,1,3224,18,2,14,1,6),_NsOspfAreaAggregateEffect_Type())
nsOspfAreaAggregateEffect.setMaxAccess(_D)
if mibBuilder.loadTexts:nsOspfAreaAggregateEffect.setStatus(_A)
class _NsOspfAreaAggregateVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsOspfAreaAggregateVRID_Type.__name__=_E
_NsOspfAreaAggregateVRID_Object=MibTableColumn
nsOspfAreaAggregateVRID=_NsOspfAreaAggregateVRID_Object((1,3,6,1,4,1,3224,18,2,14,1,7),_NsOspfAreaAggregateVRID_Type())
nsOspfAreaAggregateVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsOspfAreaAggregateVRID.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_j:AreaID,_w:RouterID,'Metric':Metric,'BigMetric':BigMetric,_k:Status,_G:PositiveInteger,_N:HelloRange,_H:UpToMaxAge,'InterfaceIndex':InterfaceIndex,_M:DesignatedRouterPriority,'TOSType':TOSType,'nsOspf':nsOspf,'nsOspfGeneralTable':nsOspfGeneralTable,'nsOspfGeneralEntry':nsOspfGeneralEntry,'nsOspfRouterId':nsOspfRouterId,'nsOspfAdminStat':nsOspfAdminStat,'nsOspfVersionNumber':nsOspfVersionNumber,'nsOspfAreaBdrRtrStatus':nsOspfAreaBdrRtrStatus,'nsOspfASBdrRtrStatus':nsOspfASBdrRtrStatus,'nsOspfExternLsaCount':nsOspfExternLsaCount,'nsOspfExternLsaCksumSum':nsOspfExternLsaCksumSum,'nsOspfTOSSupport':nsOspfTOSSupport,'nsOspfOriginateNewLsas':nsOspfOriginateNewLsas,'nsOspfRxNewLsas':nsOspfRxNewLsas,'nsOspfExtLsdbLimit':nsOspfExtLsdbLimit,'nsOspfMulticastExtensions':nsOspfMulticastExtensions,'nsOspfExitOverflowInterval':nsOspfExitOverflowInterval,'nsOspfDemandExtensions':nsOspfDemandExtensions,_P:nsOspfGeneralVRID,'nsOspfAreaTable':nsOspfAreaTable,'nsOspfAreaEntry':nsOspfAreaEntry,_Q:nsOspfAreaId,'nsOspfImportAsExtern':nsOspfImportAsExtern,'nsOspfSpfRuns':nsOspfSpfRuns,'nsOspfAreaBdrRtrCount':nsOspfAreaBdrRtrCount,'nsOspfAsBdrRtrCount':nsOspfAsBdrRtrCount,'nsOspfAreaLsaCount':nsOspfAreaLsaCount,'nsOspfAreaLsaCksumSum':nsOspfAreaLsaCksumSum,'nsOspfAreaSummary':nsOspfAreaSummary,'nsOspfAreaStatus':nsOspfAreaStatus,_R:nsOspfAreaVRID,'nsOspfStubAreaTable':nsOspfStubAreaTable,'nsOspfStubAreaEntry':nsOspfStubAreaEntry,_S:nsOspfStubAreaId,_T:nsOspfStubTOS,'nsOspfStubMetric':nsOspfStubMetric,'nsOspfStubStatus':nsOspfStubStatus,'nsOspfStubMetricType':nsOspfStubMetricType,_U:nsOspfStubVRID,'nsOspfLsdbTable':nsOspfLsdbTable,'nsOspfLsdbEntry':nsOspfLsdbEntry,_V:nsOspfLsdbAreaId,_W:nsOspfLsdbType,_X:nsOspfLsdbLsid,_Y:nsOspfLsdbRouterId,'nsOspfLsdbSequence':nsOspfLsdbSequence,'nsOspfLsdbAge':nsOspfLsdbAge,'nsOspfLsdbChecksum':nsOspfLsdbChecksum,'nsOspfLsdbAdvertisement':nsOspfLsdbAdvertisement,_Z:nsOspfLsdbVRID,'nsOspfHostTable':nsOspfHostTable,'nsOspfHostEntry':nsOspfHostEntry,_d:nsOspfHostIpAddress,_e:nsOspfHostTOS,'nsOspfHostMetric':nsOspfHostMetric,'nsOspfHostStatus':nsOspfHostStatus,'nsOspfHostAreaID':nsOspfHostAreaID,_f:nsOspfHostVRID,'nsOspfIfTable':nsOspfIfTable,'nsOspfIfEntry':nsOspfIfEntry,_g:nsOspfIfIpAddress,_h:nsOspfAddressLessIf,'nsOspfIfAreaId':nsOspfIfAreaId,'nsOspfIfType':nsOspfIfType,'nsOspfIfAdminStat':nsOspfIfAdminStat,'nsOspfIfRtrPriority':nsOspfIfRtrPriority,'nsOspfIfTransitDelay':nsOspfIfTransitDelay,'nsOspfIfRetransInterval':nsOspfIfRetransInterval,'nsOspfIfHelloInterval':nsOspfIfHelloInterval,'nsOspfIfRtrDeadInterval':nsOspfIfRtrDeadInterval,'nsOspfIfPollInterval':nsOspfIfPollInterval,'nsOspfIfState':nsOspfIfState,'nsOspfIfDesignatedRouter':nsOspfIfDesignatedRouter,'nsOspfIfBackupDesignatedRouter':nsOspfIfBackupDesignatedRouter,'nsOspfIfEvents':nsOspfIfEvents,'nsOspfIfAuthKey':nsOspfIfAuthKey,'nsOspfIfStatus':nsOspfIfStatus,'nsOspfIfMulticastForwarding':nsOspfIfMulticastForwarding,'nsOspfIfDemand':nsOspfIfDemand,'nsOspfIfAuthType':nsOspfIfAuthType,_i:nsOspfIfVRID,'nsOspfIfMetricTable':nsOspfIfMetricTable,'nsOspfIfMetricEntry':nsOspfIfMetricEntry,_m:nsOspfIfMetricIpAddress,_n:nsOspfIfMetricAddressLessIf,_o:nsOspfIfMetricTOS,'nsOspfIfMetricValue':nsOspfIfMetricValue,'nsOspfIfMetricStatus':nsOspfIfMetricStatus,_p:nsOspfIfMetricVRID,'nsOspfVirtIfTable':nsOspfVirtIfTable,'nsOspfVirtIfEntry':nsOspfVirtIfEntry,_q:nsOspfVirtIfAreaId,_r:nsOspfVirtIfNeighbor,'nsOspfVirtIfTransitDelay':nsOspfVirtIfTransitDelay,'nsOspfVirtIfRetransInterval':nsOspfVirtIfRetransInterval,'nsOspfVirtIfHelloInterval':nsOspfVirtIfHelloInterval,'nsOspfVirtIfRtrDeadInterval':nsOspfVirtIfRtrDeadInterval,'nsOspfVirtIfState':nsOspfVirtIfState,'nsOspfVirtIfEvents':nsOspfVirtIfEvents,'nsOspfVirtIfAuthKey':nsOspfVirtIfAuthKey,'nsOspfVirtIfStatus':nsOspfVirtIfStatus,'nsOspfVirtIfAuthType':nsOspfVirtIfAuthType,_s:nsOspfVirtIfVRID,'nsOspfNbrTable':nsOspfNbrTable,'nsOspfNbrEntry':nsOspfNbrEntry,_t:nsOspfNbrIpAddr,_u:nsOspfNbrAddressLessIndex,'nsOspfNbrRtrId':nsOspfNbrRtrId,'nsOspfNbrOptions':nsOspfNbrOptions,'nsOspfNbrPriority':nsOspfNbrPriority,'nsOspfNbrState':nsOspfNbrState,'nsOspfNbrEvents':nsOspfNbrEvents,'nsOspfNbrLsRetransQLen':nsOspfNbrLsRetransQLen,'nsOspfNbmaNbrStatus':nsOspfNbmaNbrStatus,'nsOspfNbmaNbrPermanence':nsOspfNbmaNbrPermanence,'nsOspfNbrHelloSuppressed':nsOspfNbrHelloSuppressed,_v:nsOspfNbrVRID,'nsOspfVirtNbrTable':nsOspfVirtNbrTable,'nsOspfVirtNbrEntry':nsOspfVirtNbrEntry,_A0:nsOspfVirtNbrArea,_A1:nsOspfVirtNbrRtrId,'nsOspfVirtNbrIpAddr':nsOspfVirtNbrIpAddr,'nsOspfVirtNbrOptions':nsOspfVirtNbrOptions,'nsOspfVirtNbrState':nsOspfVirtNbrState,'nsOspfVirtNbrEvents':nsOspfVirtNbrEvents,'nsOspfVirtNbrLsRetransQLen':nsOspfVirtNbrLsRetransQLen,'nsOspfVirtNbrHelloSuppressed':nsOspfVirtNbrHelloSuppressed,_A2:nsOspfVirtNbrVRID,'nsOspfExtLsdbTable':nsOspfExtLsdbTable,'nsOspfExtLsdbEntry':nsOspfExtLsdbEntry,_A3:nsOspfExtLsdbType,_A4:nsOspfExtLsdbLsid,_A5:nsOspfExtLsdbRouterId,'nsOspfExtLsdbSequence':nsOspfExtLsdbSequence,'nsOspfExtLsdbAge':nsOspfExtLsdbAge,'nsOspfExtLsdbChecksum':nsOspfExtLsdbChecksum,'nsOspfExtLsdbAdvertisement':nsOspfExtLsdbAdvertisement,_A6:nsOspfExtLsdbVRID,'nsOspfAreaAggregateTable':nsOspfAreaAggregateTable,'nsOspfAreaAggregateEntry':nsOspfAreaAggregateEntry,_A7:nsOspfAreaAggregateAreaID,_A8:nsOspfAreaAggregateLsdbType,_A9:nsOspfAreaAggregateNet,_AA:nsOspfAreaAggregateMask,'nsOspfAreaAggregateStatus':nsOspfAreaAggregateStatus,'nsOspfAreaAggregateEffect':nsOspfAreaAggregateEffect,_AB:nsOspfAreaAggregateVRID})