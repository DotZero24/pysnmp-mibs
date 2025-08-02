_Ad='raisecomOspfVirtNbrState'
_Ac='raisecomOspfNbrState'
_Ab='raisecomOspfNbrAddressLessIndex'
_Aa='raisecomOspfVirtIfState'
_AZ='raisecomOspfIfState'
_AY='raisecomOspfDistrOutProcessId'
_AX='raisecomOspfDistrOutProtocol'
_AW='raisecomOspfBdrRouteNextHop'
_AV='raisecomOspfBdrRouteDest'
_AU='raisecomOspfBdrRouteArea'
_AT='raisecomOspfBdrRouteRtrType'
_AS='raisecomOspfRouteType'
_AR='raisecomOspfRouteMask'
_AQ='raisecomOspfRouteDest'
_AP='raisecomOspfPacketIoStatisPktType'
_AO='raisecomOspfPacketIoStatisIoType'
_AN='raisecomOspfAreaLsaCountLsaType'
_AM='raisecomOspfAreaLsaCountAreaId'
_AL='raisecomOspfAsLsdbRouterId'
_AK='raisecomOspfAsLsdbLsId'
_AJ='raisecomOspfAsLsdbType'
_AI='raisecomOspfExternalAggregateMask'
_AH='raisecomOspfExternalAggregateNet'
_AG='raisecomOspfAreaAggregateMask'
_AF='raisecomOspfAreaAggregateNet'
_AE='raisecomOspfAreaAggregateLsdbType'
_AD='raisecomOspfAreaAggregateAreaID'
_AC='raisecomOspfNbmaCfgNbrIpAddr'
_AB='exchangeStart'
_AA='raisecomOspfNssaAreaId'
_A9='raisecomOspfStubAreaId'
_A8='raisecomOspfMask'
_A7='raisecomOspfNet'
_A6='advertise'
_A5='doNotAdvertise'
_A4='dbDescript'
_A3='Unsigned32'
_A2='raisecomOspfRedistributeRouteLimit'
_A1='raisecomOspfVirtIfAuthKeyChain'
_A0='raisecomOspfIfAuthKeyChain'
_z='raisecomOspfExtLsdbLimit'
_y='raisecomOspfNbrRtrId'
_x='not-accessible'
_w='raisecomOspfVirtNbrRtrId'
_v='raisecomOspfVirtNbrArea'
_u='raisecomOspfNbrIpAddr'
_t='HelloRange'
_s='pointToPoint'
_r='raisecomOspfAreaId'
_q='TruthValue'
_p='IpAddress'
_o='raisecomOspfPacketSrc'
_n='raisecomOspfRedistributeProcessId'
_m='raisecomOspfRedistributeProtocol'
_l='areaOpaqueLink'
_k='multicastLink'
_j='asExternalLink'
_i='asSummaryLink'
_h='networkLink'
_g='routerLink'
_f='raisecomOspfLsdbAreaId'
_e='cipher'
_d='plain'
_c='down'
_b='DesignatedRouterPriority'
_a='00000000'
_Z='OspfAuthenticationType'
_Y='raisecomOspfConfigErrorType'
_X='nssaExternalLink'
_W='summaryLink'
_V='UpToMaxAge'
_U='BigMetric'
_T='EnableVar'
_S='raisecomOspfLsdbRouterId'
_R='raisecomOspfLsdbLsId'
_Q='raisecomOspfLsdbType'
_P='PositiveInteger'
_O='d-0'
_N='raisecomOspfIfIpAddress'
_M='raisecomOspfPacketType'
_L='raisecomOspfVirtIfNeighbor'
_K='raisecomOspfVirtIfAreaId'
_J='raisecomOspfAddressLessIf'
_I='seconds'
_H='OctetString'
_G='raisecomOspfRouterId'
_F='raisecomOspfProcessId'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='RAISECOM-OSPFV2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,_p,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_A3,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_q)
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_T)
raisecomOspf=ModuleIdentity((1,3,6,1,4,1,8886,1,47))
if mibBuilder.loadTexts:raisecomOspf.setRevisions(('2011-09-14 00:00',))
class ProcessID(TextualConvention,Unsigned32):status=_A;displayHint=_O;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
class AreaID(TextualConvention,IpAddress):status=_A
class RouterID(TextualConvention,IpAddress):status=_A
class Metric(TextualConvention,Integer32):status=_A;displayHint=_O;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class BigMetric(TextualConvention,Integer32):status=_A;displayHint=_O;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
class Status(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
class PositiveInteger(TextualConvention,Integer32):status=_A;displayHint=_O;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class HelloRange(TextualConvention,Integer32):status=_A;displayHint=_O;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class UpToMaxAge(TextualConvention,Integer32):status=_A;displayHint=_O;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
class DesignatedRouterPriority(TextualConvention,Integer32):status=_A;displayHint=_O;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class OspfAuthenticationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('simplePassword',1),('md5',2)))
_RaisecomOspfNotifications_ObjectIdentity=ObjectIdentity
raisecomOspfNotifications=_RaisecomOspfNotifications_ObjectIdentity((1,3,6,1,4,1,8886,1,47,1))
_RaisecomOspfTrapControlTable_Object=MibTable
raisecomOspfTrapControlTable=_RaisecomOspfTrapControlTable_Object((1,3,6,1,4,1,8886,1,47,1,1))
if mibBuilder.loadTexts:raisecomOspfTrapControlTable.setStatus(_A)
_RaisecomOspfTrapControlEntry_Object=MibTableRow
raisecomOspfTrapControlEntry=_RaisecomOspfTrapControlEntry_Object((1,3,6,1,4,1,8886,1,47,1,1,1))
raisecomOspfTrapControlEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:raisecomOspfTrapControlEntry.setStatus(_A)
class _RaisecomOspfSetTrap_Type(EnableVar):defaultValue=2
_RaisecomOspfSetTrap_Type.__name__=_T
_RaisecomOspfSetTrap_Object=MibTableColumn
raisecomOspfSetTrap=_RaisecomOspfSetTrap_Object((1,3,6,1,4,1,8886,1,47,1,1,1,1),_RaisecomOspfSetTrap_Type())
raisecomOspfSetTrap.setMaxAccess('read-write')
if mibBuilder.loadTexts:raisecomOspfSetTrap.setStatus(_A)
class _RaisecomOspfConfigErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('badVersion',1),('areaMismatch',2),('unknownNbmaNbr',3),('unknownVirtualNbr',4),('authTypeMismatch',5),('authFailure',6),('netMaskMismatch',7),('helloIntervalMismatch',8),('deadIntervalMismatch',9),('optionMismatch',10)))
_RaisecomOspfConfigErrorType_Type.__name__=_E
_RaisecomOspfConfigErrorType_Object=MibTableColumn
raisecomOspfConfigErrorType=_RaisecomOspfConfigErrorType_Object((1,3,6,1,4,1,8886,1,47,1,1,1,2),_RaisecomOspfConfigErrorType_Type())
raisecomOspfConfigErrorType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfConfigErrorType.setStatus(_A)
class _RaisecomOspfPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('hello',1),(_A4,2),('lsReq',3),('lsUpdate',4),('lsAck',5)))
_RaisecomOspfPacketType_Type.__name__=_E
_RaisecomOspfPacketType_Object=MibTableColumn
raisecomOspfPacketType=_RaisecomOspfPacketType_Object((1,3,6,1,4,1,8886,1,47,1,1,1,3),_RaisecomOspfPacketType_Type())
raisecomOspfPacketType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfPacketType.setStatus(_A)
_RaisecomOspfPacketSrc_Type=IpAddress
_RaisecomOspfPacketSrc_Object=MibTableColumn
raisecomOspfPacketSrc=_RaisecomOspfPacketSrc_Object((1,3,6,1,4,1,8886,1,47,1,1,1,4),_RaisecomOspfPacketSrc_Type())
raisecomOspfPacketSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfPacketSrc.setStatus(_A)
_RaisecomOspfTraps_ObjectIdentity=ObjectIdentity
raisecomOspfTraps=_RaisecomOspfTraps_ObjectIdentity((1,3,6,1,4,1,8886,1,47,1,2))
_RaisecomOspfObjects_ObjectIdentity=ObjectIdentity
raisecomOspfObjects=_RaisecomOspfObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,47,2))
_RaisecomOspfGlobalTable_Object=MibTable
raisecomOspfGlobalTable=_RaisecomOspfGlobalTable_Object((1,3,6,1,4,1,8886,1,47,2,1))
if mibBuilder.loadTexts:raisecomOspfGlobalTable.setStatus(_A)
_RaisecomOspfGlobalEntry_Object=MibTableRow
raisecomOspfGlobalEntry=_RaisecomOspfGlobalEntry_Object((1,3,6,1,4,1,8886,1,47,2,1,1))
raisecomOspfGlobalEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:raisecomOspfGlobalEntry.setStatus(_A)
_RaisecomOspfProcessId_Type=ProcessID
_RaisecomOspfProcessId_Object=MibTableColumn
raisecomOspfProcessId=_RaisecomOspfProcessId_Object((1,3,6,1,4,1,8886,1,47,2,1,1,1),_RaisecomOspfProcessId_Type())
raisecomOspfProcessId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfProcessId.setStatus(_A)
_RaisecomOspfRouterId_Type=RouterID
_RaisecomOspfRouterId_Object=MibTableColumn
raisecomOspfRouterId=_RaisecomOspfRouterId_Object((1,3,6,1,4,1,8886,1,47,2,1,1,2),_RaisecomOspfRouterId_Type())
raisecomOspfRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfRouterId.setStatus(_A)
class _RaisecomOspfAdminStat_Type(EnableVar):defaultValue=2
_RaisecomOspfAdminStat_Type.__name__=_T
_RaisecomOspfAdminStat_Object=MibTableColumn
raisecomOspfAdminStat=_RaisecomOspfAdminStat_Object((1,3,6,1,4,1,8886,1,47,2,1,1,3),_RaisecomOspfAdminStat_Type())
raisecomOspfAdminStat.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAdminStat.setStatus(_A)
class _RaisecomOspfVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('version2',2))
_RaisecomOspfVersionNumber_Type.__name__=_E
_RaisecomOspfVersionNumber_Object=MibTableColumn
raisecomOspfVersionNumber=_RaisecomOspfVersionNumber_Object((1,3,6,1,4,1,8886,1,47,2,1,1,4),_RaisecomOspfVersionNumber_Type())
raisecomOspfVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVersionNumber.setStatus(_A)
_RaisecomOspfAreaBdrRtrStatus_Type=TruthValue
_RaisecomOspfAreaBdrRtrStatus_Object=MibTableColumn
raisecomOspfAreaBdrRtrStatus=_RaisecomOspfAreaBdrRtrStatus_Object((1,3,6,1,4,1,8886,1,47,2,1,1,5),_RaisecomOspfAreaBdrRtrStatus_Type())
raisecomOspfAreaBdrRtrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaBdrRtrStatus.setStatus(_A)
_RaisecomOspfASBdrRtrStatus_Type=TruthValue
_RaisecomOspfASBdrRtrStatus_Object=MibTableColumn
raisecomOspfASBdrRtrStatus=_RaisecomOspfASBdrRtrStatus_Object((1,3,6,1,4,1,8886,1,47,2,1,1,6),_RaisecomOspfASBdrRtrStatus_Type())
raisecomOspfASBdrRtrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfASBdrRtrStatus.setStatus(_A)
_RaisecomOspfExternLsaCount_Type=Gauge32
_RaisecomOspfExternLsaCount_Object=MibTableColumn
raisecomOspfExternLsaCount=_RaisecomOspfExternLsaCount_Object((1,3,6,1,4,1,8886,1,47,2,1,1,7),_RaisecomOspfExternLsaCount_Type())
raisecomOspfExternLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfExternLsaCount.setStatus(_A)
_RaisecomOspfExternLsaCksumSum_Type=Integer32
_RaisecomOspfExternLsaCksumSum_Object=MibTableColumn
raisecomOspfExternLsaCksumSum=_RaisecomOspfExternLsaCksumSum_Object((1,3,6,1,4,1,8886,1,47,2,1,1,8),_RaisecomOspfExternLsaCksumSum_Type())
raisecomOspfExternLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfExternLsaCksumSum.setStatus(_A)
_RaisecomOspfOriginateNewLsas_Type=Counter32
_RaisecomOspfOriginateNewLsas_Object=MibTableColumn
raisecomOspfOriginateNewLsas=_RaisecomOspfOriginateNewLsas_Object((1,3,6,1,4,1,8886,1,47,2,1,1,9),_RaisecomOspfOriginateNewLsas_Type())
raisecomOspfOriginateNewLsas.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfOriginateNewLsas.setStatus(_A)
_RaisecomOspfRxNewLsas_Type=Counter32
_RaisecomOspfRxNewLsas_Object=MibTableColumn
raisecomOspfRxNewLsas=_RaisecomOspfRxNewLsas_Object((1,3,6,1,4,1,8886,1,47,2,1,1,10),_RaisecomOspfRxNewLsas_Type())
raisecomOspfRxNewLsas.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfRxNewLsas.setStatus(_A)
class _RaisecomOspfExtLsdbLimit_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_RaisecomOspfExtLsdbLimit_Type.__name__=_E
_RaisecomOspfExtLsdbLimit_Object=MibTableColumn
raisecomOspfExtLsdbLimit=_RaisecomOspfExtLsdbLimit_Object((1,3,6,1,4,1,8886,1,47,2,1,1,11),_RaisecomOspfExtLsdbLimit_Type())
raisecomOspfExtLsdbLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfExtLsdbLimit.setStatus(_A)
class _RaisecomOspfExitOverflowInterval_Type(PositiveInteger):defaultValue=0
_RaisecomOspfExitOverflowInterval_Type.__name__=_P
_RaisecomOspfExitOverflowInterval_Object=MibTableColumn
raisecomOspfExitOverflowInterval=_RaisecomOspfExitOverflowInterval_Object((1,3,6,1,4,1,8886,1,47,2,1,1,12),_RaisecomOspfExitOverflowInterval_Type())
raisecomOspfExitOverflowInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfExitOverflowInterval.setStatus(_A)
class _RaisecomOspfReferenceBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4296967))
_RaisecomOspfReferenceBandwidth_Type.__name__=_A3
_RaisecomOspfReferenceBandwidth_Object=MibTableColumn
raisecomOspfReferenceBandwidth=_RaisecomOspfReferenceBandwidth_Object((1,3,6,1,4,1,8886,1,47,2,1,1,13),_RaisecomOspfReferenceBandwidth_Type())
raisecomOspfReferenceBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfReferenceBandwidth.setStatus(_A)
if mibBuilder.loadTexts:raisecomOspfReferenceBandwidth.setUnits('millionbits per second')
_RaisecomOspfAsLsaCount_Type=Gauge32
_RaisecomOspfAsLsaCount_Object=MibTableColumn
raisecomOspfAsLsaCount=_RaisecomOspfAsLsaCount_Object((1,3,6,1,4,1,8886,1,47,2,1,1,14),_RaisecomOspfAsLsaCount_Type())
raisecomOspfAsLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAsLsaCount.setStatus(_A)
_RaisecomOspfAsLsaCksumSum_Type=Unsigned32
_RaisecomOspfAsLsaCksumSum_Object=MibTableColumn
raisecomOspfAsLsaCksumSum=_RaisecomOspfAsLsaCksumSum_Object((1,3,6,1,4,1,8886,1,47,2,1,1,15),_RaisecomOspfAsLsaCksumSum_Type())
raisecomOspfAsLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAsLsaCksumSum.setStatus(_A)
_RaisecomOspfStubRouterSupport_Type=TruthValue
_RaisecomOspfStubRouterSupport_Object=MibTableColumn
raisecomOspfStubRouterSupport=_RaisecomOspfStubRouterSupport_Object((1,3,6,1,4,1,8886,1,47,2,1,1,16),_RaisecomOspfStubRouterSupport_Type())
raisecomOspfStubRouterSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfStubRouterSupport.setStatus(_A)
class _RaisecomOspfStubRouterAdvertisement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A5,1),(_A6,2)))
_RaisecomOspfStubRouterAdvertisement_Type.__name__=_E
_RaisecomOspfStubRouterAdvertisement_Object=MibTableColumn
raisecomOspfStubRouterAdvertisement=_RaisecomOspfStubRouterAdvertisement_Object((1,3,6,1,4,1,8886,1,47,2,1,1,17),_RaisecomOspfStubRouterAdvertisement_Type())
raisecomOspfStubRouterAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfStubRouterAdvertisement.setStatus(_A)
class _RaisecomOspfAdminDistance_Type(Integer32):defaultValue=110;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RaisecomOspfAdminDistance_Type.__name__=_E
_RaisecomOspfAdminDistance_Object=MibTableColumn
raisecomOspfAdminDistance=_RaisecomOspfAdminDistance_Object((1,3,6,1,4,1,8886,1,47,2,1,1,18),_RaisecomOspfAdminDistance_Type())
raisecomOspfAdminDistance.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfAdminDistance.setStatus(_A)
class _RaisecomOspfSpfInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_RaisecomOspfSpfInterval_Type.__name__=_E
_RaisecomOspfSpfInterval_Object=MibTableColumn
raisecomOspfSpfInterval=_RaisecomOspfSpfInterval_Object((1,3,6,1,4,1,8886,1,47,2,1,1,19),_RaisecomOspfSpfInterval_Type())
raisecomOspfSpfInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfSpfInterval.setStatus(_A)
class _RaisecomOspfReset_Type(TruthValue):defaultValue=2
_RaisecomOspfReset_Type.__name__=_q
_RaisecomOspfReset_Object=MibTableColumn
raisecomOspfReset=_RaisecomOspfReset_Object((1,3,6,1,4,1,8886,1,47,2,1,1,20),_RaisecomOspfReset_Type())
raisecomOspfReset.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfReset.setStatus(_A)
class _RaisecomOspfExportMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_RaisecomOspfExportMetric_Type.__name__=_E
_RaisecomOspfExportMetric_Object=MibTableColumn
raisecomOspfExportMetric=_RaisecomOspfExportMetric_Object((1,3,6,1,4,1,8886,1,47,2,1,1,21),_RaisecomOspfExportMetric_Type())
raisecomOspfExportMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfExportMetric.setStatus(_A)
_RaisecomOspfExportTag_Type=Integer32
_RaisecomOspfExportTag_Object=MibTableColumn
raisecomOspfExportTag=_RaisecomOspfExportTag_Object((1,3,6,1,4,1,8886,1,47,2,1,1,22),_RaisecomOspfExportTag_Type())
raisecomOspfExportTag.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfExportTag.setStatus(_A)
class _RaisecomOspfExportType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('type1',1),('type2',2)))
_RaisecomOspfExportType_Type.__name__=_E
_RaisecomOspfExportType_Object=MibTableColumn
raisecomOspfExportType=_RaisecomOspfExportType_Object((1,3,6,1,4,1,8886,1,47,2,1,1,23),_RaisecomOspfExportType_Type())
raisecomOspfExportType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfExportType.setStatus(_A)
_RaisecomOspfNetCounts_Type=Integer32
_RaisecomOspfNetCounts_Object=MibTableColumn
raisecomOspfNetCounts=_RaisecomOspfNetCounts_Object((1,3,6,1,4,1,8886,1,47,2,1,1,24),_RaisecomOspfNetCounts_Type())
raisecomOspfNetCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNetCounts.setStatus(_A)
_RaisecomOspfAreaCounts_Type=Integer32
_RaisecomOspfAreaCounts_Object=MibTableColumn
raisecomOspfAreaCounts=_RaisecomOspfAreaCounts_Object((1,3,6,1,4,1,8886,1,47,2,1,1,25),_RaisecomOspfAreaCounts_Type())
raisecomOspfAreaCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaCounts.setStatus(_A)
_RaisecomOspfNssaAreaCounts_Type=Integer32
_RaisecomOspfNssaAreaCounts_Object=MibTableColumn
raisecomOspfNssaAreaCounts=_RaisecomOspfNssaAreaCounts_Object((1,3,6,1,4,1,8886,1,47,2,1,1,26),_RaisecomOspfNssaAreaCounts_Type())
raisecomOspfNssaAreaCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNssaAreaCounts.setStatus(_A)
_RaisecomOspfSpfCounts_Type=Integer32
_RaisecomOspfSpfCounts_Object=MibTableColumn
raisecomOspfSpfCounts=_RaisecomOspfSpfCounts_Object((1,3,6,1,4,1,8886,1,47,2,1,1,27),_RaisecomOspfSpfCounts_Type())
raisecomOspfSpfCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfSpfCounts.setStatus(_A)
_RaisecomOspfGlobalStatus_Type=RowStatus
_RaisecomOspfGlobalStatus_Object=MibTableColumn
raisecomOspfGlobalStatus=_RaisecomOspfGlobalStatus_Object((1,3,6,1,4,1,8886,1,47,2,1,1,28),_RaisecomOspfGlobalStatus_Type())
raisecomOspfGlobalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfGlobalStatus.setStatus(_A)
class _RaisecomOspfRedistributeRouteLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RaisecomOspfRedistributeRouteLimit_Type.__name__=_E
_RaisecomOspfRedistributeRouteLimit_Object=MibTableColumn
raisecomOspfRedistributeRouteLimit=_RaisecomOspfRedistributeRouteLimit_Object((1,3,6,1,4,1,8886,1,47,2,1,1,29),_RaisecomOspfRedistributeRouteLimit_Type())
raisecomOspfRedistributeRouteLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfRedistributeRouteLimit.setStatus(_A)
_RaisecomOspfAreaTable_Object=MibTable
raisecomOspfAreaTable=_RaisecomOspfAreaTable_Object((1,3,6,1,4,1,8886,1,47,2,2))
if mibBuilder.loadTexts:raisecomOspfAreaTable.setStatus(_A)
_RaisecomOspfAreaEntry_Object=MibTableRow
raisecomOspfAreaEntry=_RaisecomOspfAreaEntry_Object((1,3,6,1,4,1,8886,1,47,2,2,1))
raisecomOspfAreaEntry.setIndexNames((0,_B,_F),(0,_B,_r))
if mibBuilder.loadTexts:raisecomOspfAreaEntry.setStatus(_A)
_RaisecomOspfAreaId_Type=AreaID
_RaisecomOspfAreaId_Object=MibTableColumn
raisecomOspfAreaId=_RaisecomOspfAreaId_Object((1,3,6,1,4,1,8886,1,47,2,2,1,1),_RaisecomOspfAreaId_Type())
raisecomOspfAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaId.setStatus(_A)
class _RaisecomOspfAuthType_Type(OspfAuthenticationType):defaultValue=0
_RaisecomOspfAuthType_Type.__name__=_Z
_RaisecomOspfAuthType_Object=MibTableColumn
raisecomOspfAuthType=_RaisecomOspfAuthType_Object((1,3,6,1,4,1,8886,1,47,2,2,1,2),_RaisecomOspfAuthType_Type())
raisecomOspfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfAuthType.setStatus(_A)
class _RaisecomOspfImportAsExtern_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('importExternal',1),('importNoExternal',2),('importNssa',3)))
_RaisecomOspfImportAsExtern_Type.__name__=_E
_RaisecomOspfImportAsExtern_Object=MibTableColumn
raisecomOspfImportAsExtern=_RaisecomOspfImportAsExtern_Object((1,3,6,1,4,1,8886,1,47,2,2,1,3),_RaisecomOspfImportAsExtern_Type())
raisecomOspfImportAsExtern.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfImportAsExtern.setStatus(_A)
_RaisecomOspfSpfRuns_Type=Counter32
_RaisecomOspfSpfRuns_Object=MibTableColumn
raisecomOspfSpfRuns=_RaisecomOspfSpfRuns_Object((1,3,6,1,4,1,8886,1,47,2,2,1,4),_RaisecomOspfSpfRuns_Type())
raisecomOspfSpfRuns.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfSpfRuns.setStatus(_A)
_RaisecomOspfAreaBdrRtrCount_Type=Gauge32
_RaisecomOspfAreaBdrRtrCount_Object=MibTableColumn
raisecomOspfAreaBdrRtrCount=_RaisecomOspfAreaBdrRtrCount_Object((1,3,6,1,4,1,8886,1,47,2,2,1,5),_RaisecomOspfAreaBdrRtrCount_Type())
raisecomOspfAreaBdrRtrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaBdrRtrCount.setStatus(_A)
_RaisecomOspfAsBdrRtrCount_Type=Gauge32
_RaisecomOspfAsBdrRtrCount_Object=MibTableColumn
raisecomOspfAsBdrRtrCount=_RaisecomOspfAsBdrRtrCount_Object((1,3,6,1,4,1,8886,1,47,2,2,1,6),_RaisecomOspfAsBdrRtrCount_Type())
raisecomOspfAsBdrRtrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAsBdrRtrCount.setStatus(_A)
_RaisecomOspfAreaLsaCount_Type=Gauge32
_RaisecomOspfAreaLsaCount_Object=MibTableColumn
raisecomOspfAreaLsaCount=_RaisecomOspfAreaLsaCount_Object((1,3,6,1,4,1,8886,1,47,2,2,1,7),_RaisecomOspfAreaLsaCount_Type())
raisecomOspfAreaLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaLsaCount.setStatus(_A)
class _RaisecomOspfAreaLsaCksumSum_Type(Integer32):defaultValue=0
_RaisecomOspfAreaLsaCksumSum_Type.__name__=_E
_RaisecomOspfAreaLsaCksumSum_Object=MibTableColumn
raisecomOspfAreaLsaCksumSum=_RaisecomOspfAreaLsaCksumSum_Object((1,3,6,1,4,1,8886,1,47,2,2,1,8),_RaisecomOspfAreaLsaCksumSum_Type())
raisecomOspfAreaLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaLsaCksumSum.setStatus(_A)
class _RaisecomOspfAreaSummary_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAreaSummary',1),('sendAreaSummary',2)))
_RaisecomOspfAreaSummary_Type.__name__=_E
_RaisecomOspfAreaSummary_Object=MibTableColumn
raisecomOspfAreaSummary=_RaisecomOspfAreaSummary_Object((1,3,6,1,4,1,8886,1,47,2,2,1,9),_RaisecomOspfAreaSummary_Type())
raisecomOspfAreaSummary.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfAreaSummary.setStatus(_A)
class _RaisecomOspfAreaNssaTranslatorRole_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('always',1),('candidate',2)))
_RaisecomOspfAreaNssaTranslatorRole_Type.__name__=_E
_RaisecomOspfAreaNssaTranslatorRole_Object=MibTableColumn
raisecomOspfAreaNssaTranslatorRole=_RaisecomOspfAreaNssaTranslatorRole_Object((1,3,6,1,4,1,8886,1,47,2,2,1,10),_RaisecomOspfAreaNssaTranslatorRole_Type())
raisecomOspfAreaNssaTranslatorRole.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfAreaNssaTranslatorRole.setStatus(_A)
class _RaisecomOspfAreaNssaTranslatorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('elected',2),('disabled',3)))
_RaisecomOspfAreaNssaTranslatorState_Type.__name__=_E
_RaisecomOspfAreaNssaTranslatorState_Object=MibTableColumn
raisecomOspfAreaNssaTranslatorState=_RaisecomOspfAreaNssaTranslatorState_Object((1,3,6,1,4,1,8886,1,47,2,2,1,11),_RaisecomOspfAreaNssaTranslatorState_Type())
raisecomOspfAreaNssaTranslatorState.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaNssaTranslatorState.setStatus(_A)
class _RaisecomOspfAreaNssaTranslatorStabilityInterval_Type(PositiveInteger):defaultValue=40
_RaisecomOspfAreaNssaTranslatorStabilityInterval_Type.__name__=_P
_RaisecomOspfAreaNssaTranslatorStabilityInterval_Object=MibTableColumn
raisecomOspfAreaNssaTranslatorStabilityInterval=_RaisecomOspfAreaNssaTranslatorStabilityInterval_Object((1,3,6,1,4,1,8886,1,47,2,2,1,12),_RaisecomOspfAreaNssaTranslatorStabilityInterval_Type())
raisecomOspfAreaNssaTranslatorStabilityInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfAreaNssaTranslatorStabilityInterval.setStatus(_A)
if mibBuilder.loadTexts:raisecomOspfAreaNssaTranslatorStabilityInterval.setUnits(_I)
_RaisecomOspfAreaNssaTranslatorEvents_Type=Counter32
_RaisecomOspfAreaNssaTranslatorEvents_Object=MibTableColumn
raisecomOspfAreaNssaTranslatorEvents=_RaisecomOspfAreaNssaTranslatorEvents_Object((1,3,6,1,4,1,8886,1,47,2,2,1,13),_RaisecomOspfAreaNssaTranslatorEvents_Type())
raisecomOspfAreaNssaTranslatorEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaNssaTranslatorEvents.setStatus(_A)
class _RaisecomOspfAreaDefaultCost_Type(BigMetric):defaultValue=1
_RaisecomOspfAreaDefaultCost_Type.__name__=_U
_RaisecomOspfAreaDefaultCost_Object=MibTableColumn
raisecomOspfAreaDefaultCost=_RaisecomOspfAreaDefaultCost_Object((1,3,6,1,4,1,8886,1,47,2,2,1,14),_RaisecomOspfAreaDefaultCost_Type())
raisecomOspfAreaDefaultCost.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfAreaDefaultCost.setStatus(_A)
class _RaisecomOspfAreaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('backbone',1),('normal',2),('stub',3),('nssa',4),('transmit',5)))
_RaisecomOspfAreaType_Type.__name__=_E
_RaisecomOspfAreaType_Object=MibTableColumn
raisecomOspfAreaType=_RaisecomOspfAreaType_Object((1,3,6,1,4,1,8886,1,47,2,2,1,15),_RaisecomOspfAreaType_Type())
raisecomOspfAreaType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaType.setStatus(_A)
_RaisecomOspfAreaAbrCount_Type=Integer32
_RaisecomOspfAreaAbrCount_Object=MibTableColumn
raisecomOspfAreaAbrCount=_RaisecomOspfAreaAbrCount_Object((1,3,6,1,4,1,8886,1,47,2,2,1,16),_RaisecomOspfAreaAbrCount_Type())
raisecomOspfAreaAbrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaAbrCount.setStatus(_A)
_RaisecomOspfAreaAsbrCount_Type=Integer32
_RaisecomOspfAreaAsbrCount_Object=MibTableColumn
raisecomOspfAreaAsbrCount=_RaisecomOspfAreaAsbrCount_Object((1,3,6,1,4,1,8886,1,47,2,2,1,17),_RaisecomOspfAreaAsbrCount_Type())
raisecomOspfAreaAsbrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaAsbrCount.setStatus(_A)
_RaisecomOspfAreaStatus_Type=RowStatus
_RaisecomOspfAreaStatus_Object=MibTableColumn
raisecomOspfAreaStatus=_RaisecomOspfAreaStatus_Object((1,3,6,1,4,1,8886,1,47,2,2,1,18),_RaisecomOspfAreaStatus_Type())
raisecomOspfAreaStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfAreaStatus.setStatus(_A)
class _RaisecomOspfAreaFilterInIpPrefixListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_RaisecomOspfAreaFilterInIpPrefixListName_Type.__name__=_H
_RaisecomOspfAreaFilterInIpPrefixListName_Object=MibTableColumn
raisecomOspfAreaFilterInIpPrefixListName=_RaisecomOspfAreaFilterInIpPrefixListName_Object((1,3,6,1,4,1,8886,1,47,2,2,1,19),_RaisecomOspfAreaFilterInIpPrefixListName_Type())
raisecomOspfAreaFilterInIpPrefixListName.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfAreaFilterInIpPrefixListName.setStatus(_A)
class _RaisecomOspfAreaFilterOutIpPrefixListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_RaisecomOspfAreaFilterOutIpPrefixListName_Type.__name__=_H
_RaisecomOspfAreaFilterOutIpPrefixListName_Object=MibTableColumn
raisecomOspfAreaFilterOutIpPrefixListName=_RaisecomOspfAreaFilterOutIpPrefixListName_Object((1,3,6,1,4,1,8886,1,47,2,2,1,20),_RaisecomOspfAreaFilterOutIpPrefixListName_Type())
raisecomOspfAreaFilterOutIpPrefixListName.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfAreaFilterOutIpPrefixListName.setStatus(_A)
_RaisecomOspfNetWorkTable_Object=MibTable
raisecomOspfNetWorkTable=_RaisecomOspfNetWorkTable_Object((1,3,6,1,4,1,8886,1,47,2,3))
if mibBuilder.loadTexts:raisecomOspfNetWorkTable.setStatus(_A)
_RaisecomOspfNetWorkEntry_Object=MibTableRow
raisecomOspfNetWorkEntry=_RaisecomOspfNetWorkEntry_Object((1,3,6,1,4,1,8886,1,47,2,3,1))
raisecomOspfNetWorkEntry.setIndexNames((0,_B,_F),(0,_B,_r),(0,_B,_A7),(0,_B,_A8))
if mibBuilder.loadTexts:raisecomOspfNetWorkEntry.setStatus(_A)
_RaisecomOspfNet_Type=IpAddress
_RaisecomOspfNet_Object=MibTableColumn
raisecomOspfNet=_RaisecomOspfNet_Object((1,3,6,1,4,1,8886,1,47,2,3,1,1),_RaisecomOspfNet_Type())
raisecomOspfNet.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNet.setStatus(_A)
_RaisecomOspfMask_Type=IpAddress
_RaisecomOspfMask_Object=MibTableColumn
raisecomOspfMask=_RaisecomOspfMask_Object((1,3,6,1,4,1,8886,1,47,2,3,1,2),_RaisecomOspfMask_Type())
raisecomOspfMask.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfMask.setStatus(_A)
_RaisecomOspfNetWorkStatus_Type=RowStatus
_RaisecomOspfNetWorkStatus_Object=MibTableColumn
raisecomOspfNetWorkStatus=_RaisecomOspfNetWorkStatus_Object((1,3,6,1,4,1,8886,1,47,2,3,1,3),_RaisecomOspfNetWorkStatus_Type())
raisecomOspfNetWorkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfNetWorkStatus.setStatus(_A)
_RaisecomOspfStubAreaTable_Object=MibTable
raisecomOspfStubAreaTable=_RaisecomOspfStubAreaTable_Object((1,3,6,1,4,1,8886,1,47,2,4))
if mibBuilder.loadTexts:raisecomOspfStubAreaTable.setStatus(_A)
_RaisecomOspfStubAreaEntry_Object=MibTableRow
raisecomOspfStubAreaEntry=_RaisecomOspfStubAreaEntry_Object((1,3,6,1,4,1,8886,1,47,2,4,1))
raisecomOspfStubAreaEntry.setIndexNames((0,_B,_F),(0,_B,_A9))
if mibBuilder.loadTexts:raisecomOspfStubAreaEntry.setStatus(_A)
_RaisecomOspfStubAreaId_Type=AreaID
_RaisecomOspfStubAreaId_Object=MibTableColumn
raisecomOspfStubAreaId=_RaisecomOspfStubAreaId_Object((1,3,6,1,4,1,8886,1,47,2,4,1,1),_RaisecomOspfStubAreaId_Type())
raisecomOspfStubAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfStubAreaId.setStatus(_A)
_RaisecomOspfStubAreaOption_Type=TruthValue
_RaisecomOspfStubAreaOption_Object=MibTableColumn
raisecomOspfStubAreaOption=_RaisecomOspfStubAreaOption_Object((1,3,6,1,4,1,8886,1,47,2,4,1,2),_RaisecomOspfStubAreaOption_Type())
raisecomOspfStubAreaOption.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfStubAreaOption.setStatus(_A)
_RaisecomOspfStubAreaStatus_Type=RowStatus
_RaisecomOspfStubAreaStatus_Object=MibTableColumn
raisecomOspfStubAreaStatus=_RaisecomOspfStubAreaStatus_Object((1,3,6,1,4,1,8886,1,47,2,4,1,3),_RaisecomOspfStubAreaStatus_Type())
raisecomOspfStubAreaStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfStubAreaStatus.setStatus(_A)
_RaisecomOspfNssaAreaTable_Object=MibTable
raisecomOspfNssaAreaTable=_RaisecomOspfNssaAreaTable_Object((1,3,6,1,4,1,8886,1,47,2,5))
if mibBuilder.loadTexts:raisecomOspfNssaAreaTable.setStatus(_A)
_RaisecomOspfNssaAreaEntry_Object=MibTableRow
raisecomOspfNssaAreaEntry=_RaisecomOspfNssaAreaEntry_Object((1,3,6,1,4,1,8886,1,47,2,5,1))
raisecomOspfNssaAreaEntry.setIndexNames((0,_B,_F),(0,_B,_AA))
if mibBuilder.loadTexts:raisecomOspfNssaAreaEntry.setStatus(_A)
_RaisecomOspfNssaAreaId_Type=AreaID
_RaisecomOspfNssaAreaId_Object=MibTableColumn
raisecomOspfNssaAreaId=_RaisecomOspfNssaAreaId_Object((1,3,6,1,4,1,8886,1,47,2,5,1,1),_RaisecomOspfNssaAreaId_Type())
raisecomOspfNssaAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNssaAreaId.setStatus(_A)
class _RaisecomOspfNssaAreaOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomOspfNssaAreaOption_Type.__name__=_E
_RaisecomOspfNssaAreaOption_Object=MibTableColumn
raisecomOspfNssaAreaOption=_RaisecomOspfNssaAreaOption_Object((1,3,6,1,4,1,8886,1,47,2,5,1,2),_RaisecomOspfNssaAreaOption_Type())
raisecomOspfNssaAreaOption.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfNssaAreaOption.setStatus(_A)
_RaisecomOspfNssaAreaStatus_Type=RowStatus
_RaisecomOspfNssaAreaStatus_Object=MibTableColumn
raisecomOspfNssaAreaStatus=_RaisecomOspfNssaAreaStatus_Object((1,3,6,1,4,1,8886,1,47,2,5,1,3),_RaisecomOspfNssaAreaStatus_Type())
raisecomOspfNssaAreaStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfNssaAreaStatus.setStatus(_A)
_RaisecomOspfIfTable_Object=MibTable
raisecomOspfIfTable=_RaisecomOspfIfTable_Object((1,3,6,1,4,1,8886,1,47,2,6))
if mibBuilder.loadTexts:raisecomOspfIfTable.setStatus(_A)
_RaisecomOspfIfEntry_Object=MibTableRow
raisecomOspfIfEntry=_RaisecomOspfIfEntry_Object((1,3,6,1,4,1,8886,1,47,2,6,1))
raisecomOspfIfEntry.setIndexNames((0,_B,_F),(0,_B,_J))
if mibBuilder.loadTexts:raisecomOspfIfEntry.setStatus(_A)
_RaisecomOspfAddressLessIf_Type=InterfaceIndexOrZero
_RaisecomOspfAddressLessIf_Object=MibTableColumn
raisecomOspfAddressLessIf=_RaisecomOspfAddressLessIf_Object((1,3,6,1,4,1,8886,1,47,2,6,1,1),_RaisecomOspfAddressLessIf_Type())
raisecomOspfAddressLessIf.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAddressLessIf.setStatus(_A)
_RaisecomOspfIfIpAddress_Type=IpAddress
_RaisecomOspfIfIpAddress_Object=MibTableColumn
raisecomOspfIfIpAddress=_RaisecomOspfIfIpAddress_Object((1,3,6,1,4,1,8886,1,47,2,6,1,2),_RaisecomOspfIfIpAddress_Type())
raisecomOspfIfIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfIfIpAddress.setStatus(_A)
class _RaisecomOspfIfAreaId_Type(AreaID):defaultHexValue=_a
_RaisecomOspfIfAreaId_Type.__name__='AreaID'
_RaisecomOspfIfAreaId_Object=MibTableColumn
raisecomOspfIfAreaId=_RaisecomOspfIfAreaId_Object((1,3,6,1,4,1,8886,1,47,2,6,1,3),_RaisecomOspfIfAreaId_Type())
raisecomOspfIfAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfIfAreaId.setStatus(_A)
class _RaisecomOspfIfType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*(('broadcast',1),('nbma',2),(_s,3),('pointToMultipoint',5)))
_RaisecomOspfIfType_Type.__name__=_E
_RaisecomOspfIfType_Object=MibTableColumn
raisecomOspfIfType=_RaisecomOspfIfType_Object((1,3,6,1,4,1,8886,1,47,2,6,1,4),_RaisecomOspfIfType_Type())
raisecomOspfIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfType.setStatus(_A)
class _RaisecomOspfIfAdminStat_Type(Status):defaultValue=1
_RaisecomOspfIfAdminStat_Type.__name__='Status'
_RaisecomOspfIfAdminStat_Object=MibTableColumn
raisecomOspfIfAdminStat=_RaisecomOspfIfAdminStat_Object((1,3,6,1,4,1,8886,1,47,2,6,1,5),_RaisecomOspfIfAdminStat_Type())
raisecomOspfIfAdminStat.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfIfAdminStat.setStatus(_A)
class _RaisecomOspfIfRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_RaisecomOspfIfRtrPriority_Type.__name__=_b
_RaisecomOspfIfRtrPriority_Object=MibTableColumn
raisecomOspfIfRtrPriority=_RaisecomOspfIfRtrPriority_Object((1,3,6,1,4,1,8886,1,47,2,6,1,6),_RaisecomOspfIfRtrPriority_Type())
raisecomOspfIfRtrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfRtrPriority.setStatus(_A)
class _RaisecomOspfIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_RaisecomOspfIfTransitDelay_Type.__name__=_V
_RaisecomOspfIfTransitDelay_Object=MibTableColumn
raisecomOspfIfTransitDelay=_RaisecomOspfIfTransitDelay_Object((1,3,6,1,4,1,8886,1,47,2,6,1,7),_RaisecomOspfIfTransitDelay_Type())
raisecomOspfIfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfTransitDelay.setStatus(_A)
if mibBuilder.loadTexts:raisecomOspfIfTransitDelay.setUnits(_I)
class _RaisecomOspfIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_RaisecomOspfIfRetransInterval_Type.__name__=_V
_RaisecomOspfIfRetransInterval_Object=MibTableColumn
raisecomOspfIfRetransInterval=_RaisecomOspfIfRetransInterval_Object((1,3,6,1,4,1,8886,1,47,2,6,1,8),_RaisecomOspfIfRetransInterval_Type())
raisecomOspfIfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfRetransInterval.setStatus(_A)
if mibBuilder.loadTexts:raisecomOspfIfRetransInterval.setUnits(_I)
class _RaisecomOspfIfHelloInterval_Type(HelloRange):defaultValue=10
_RaisecomOspfIfHelloInterval_Type.__name__=_t
_RaisecomOspfIfHelloInterval_Object=MibTableColumn
raisecomOspfIfHelloInterval=_RaisecomOspfIfHelloInterval_Object((1,3,6,1,4,1,8886,1,47,2,6,1,9),_RaisecomOspfIfHelloInterval_Type())
raisecomOspfIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:raisecomOspfIfHelloInterval.setUnits(_I)
class _RaisecomOspfIfRtrDeadInterval_Type(PositiveInteger):defaultValue=40
_RaisecomOspfIfRtrDeadInterval_Type.__name__=_P
_RaisecomOspfIfRtrDeadInterval_Object=MibTableColumn
raisecomOspfIfRtrDeadInterval=_RaisecomOspfIfRtrDeadInterval_Object((1,3,6,1,4,1,8886,1,47,2,6,1,10),_RaisecomOspfIfRtrDeadInterval_Type())
raisecomOspfIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfRtrDeadInterval.setStatus(_A)
if mibBuilder.loadTexts:raisecomOspfIfRtrDeadInterval.setUnits(_I)
class _RaisecomOspfIfPollInterval_Type(PositiveInteger):defaultValue=120
_RaisecomOspfIfPollInterval_Type.__name__=_P
_RaisecomOspfIfPollInterval_Object=MibTableColumn
raisecomOspfIfPollInterval=_RaisecomOspfIfPollInterval_Object((1,3,6,1,4,1,8886,1,47,2,6,1,11),_RaisecomOspfIfPollInterval_Type())
raisecomOspfIfPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfPollInterval.setStatus(_A)
if mibBuilder.loadTexts:raisecomOspfIfPollInterval.setUnits(_I)
class _RaisecomOspfIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_c,1),('loopback',2),('waiting',3),(_s,4),('designatedRouter',5),('backupDesignatedRouter',6),('otherDesignatedRouter',7)))
_RaisecomOspfIfState_Type.__name__=_E
_RaisecomOspfIfState_Object=MibTableColumn
raisecomOspfIfState=_RaisecomOspfIfState_Object((1,3,6,1,4,1,8886,1,47,2,6,1,12),_RaisecomOspfIfState_Type())
raisecomOspfIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfIfState.setStatus(_A)
class _RaisecomOspfIfDesignatedRouter_Type(IpAddress):defaultHexValue=_a
_RaisecomOspfIfDesignatedRouter_Type.__name__=_p
_RaisecomOspfIfDesignatedRouter_Object=MibTableColumn
raisecomOspfIfDesignatedRouter=_RaisecomOspfIfDesignatedRouter_Object((1,3,6,1,4,1,8886,1,47,2,6,1,13),_RaisecomOspfIfDesignatedRouter_Type())
raisecomOspfIfDesignatedRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfIfDesignatedRouter.setStatus(_A)
class _RaisecomOspfIfBackupDesignatedRouter_Type(IpAddress):defaultHexValue=_a
_RaisecomOspfIfBackupDesignatedRouter_Type.__name__=_p
_RaisecomOspfIfBackupDesignatedRouter_Object=MibTableColumn
raisecomOspfIfBackupDesignatedRouter=_RaisecomOspfIfBackupDesignatedRouter_Object((1,3,6,1,4,1,8886,1,47,2,6,1,14),_RaisecomOspfIfBackupDesignatedRouter_Type())
raisecomOspfIfBackupDesignatedRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfIfBackupDesignatedRouter.setStatus(_A)
_RaisecomOspfIfEvents_Type=Counter32
_RaisecomOspfIfEvents_Object=MibTableColumn
raisecomOspfIfEvents=_RaisecomOspfIfEvents_Object((1,3,6,1,4,1,8886,1,47,2,6,1,15),_RaisecomOspfIfEvents_Type())
raisecomOspfIfEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfIfEvents.setStatus(_A)
class _RaisecomOspfIfAuthKeyId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomOspfIfAuthKeyId_Type.__name__=_E
_RaisecomOspfIfAuthKeyId_Object=MibTableColumn
raisecomOspfIfAuthKeyId=_RaisecomOspfIfAuthKeyId_Object((1,3,6,1,4,1,8886,1,47,2,6,1,16),_RaisecomOspfIfAuthKeyId_Type())
raisecomOspfIfAuthKeyId.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfAuthKeyId.setStatus(_A)
class _RaisecomOspfIfAuthSimpleKeyType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,7)));namedValues=NamedValues(*((_d,0),(_e,7)))
_RaisecomOspfIfAuthSimpleKeyType_Type.__name__=_E
_RaisecomOspfIfAuthSimpleKeyType_Object=MibTableColumn
raisecomOspfIfAuthSimpleKeyType=_RaisecomOspfIfAuthSimpleKeyType_Object((1,3,6,1,4,1,8886,1,47,2,6,1,17),_RaisecomOspfIfAuthSimpleKeyType_Type())
raisecomOspfIfAuthSimpleKeyType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfAuthSimpleKeyType.setStatus(_A)
class _RaisecomOspfIfAuthMd5KeyType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,7)));namedValues=NamedValues(*((_d,0),(_e,7)))
_RaisecomOspfIfAuthMd5KeyType_Type.__name__=_E
_RaisecomOspfIfAuthMd5KeyType_Object=MibTableColumn
raisecomOspfIfAuthMd5KeyType=_RaisecomOspfIfAuthMd5KeyType_Object((1,3,6,1,4,1,8886,1,47,2,6,1,18),_RaisecomOspfIfAuthMd5KeyType_Type())
raisecomOspfIfAuthMd5KeyType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfAuthMd5KeyType.setStatus(_A)
class _RaisecomOspfIfAuthSimpleKey_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,68))
_RaisecomOspfIfAuthSimpleKey_Type.__name__=_H
_RaisecomOspfIfAuthSimpleKey_Object=MibTableColumn
raisecomOspfIfAuthSimpleKey=_RaisecomOspfIfAuthSimpleKey_Object((1,3,6,1,4,1,8886,1,47,2,6,1,19),_RaisecomOspfIfAuthSimpleKey_Type())
raisecomOspfIfAuthSimpleKey.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfAuthSimpleKey.setStatus(_A)
class _RaisecomOspfIfAuthMd5Key_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,68))
_RaisecomOspfIfAuthMd5Key_Type.__name__=_H
_RaisecomOspfIfAuthMd5Key_Object=MibTableColumn
raisecomOspfIfAuthMd5Key=_RaisecomOspfIfAuthMd5Key_Object((1,3,6,1,4,1,8886,1,47,2,6,1,20),_RaisecomOspfIfAuthMd5Key_Type())
raisecomOspfIfAuthMd5Key.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfAuthMd5Key.setStatus(_A)
class _RaisecomOspfIfAuthKeyChain_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RaisecomOspfIfAuthKeyChain_Type.__name__=_H
_RaisecomOspfIfAuthKeyChain_Object=MibTableColumn
raisecomOspfIfAuthKeyChain=_RaisecomOspfIfAuthKeyChain_Object((1,3,6,1,4,1,8886,1,47,2,6,1,21),_RaisecomOspfIfAuthKeyChain_Type())
raisecomOspfIfAuthKeyChain.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfAuthKeyChain.setStatus(_A)
class _RaisecomOspfIfAuthType_Type(OspfAuthenticationType):defaultValue=0
_RaisecomOspfIfAuthType_Type.__name__=_Z
_RaisecomOspfIfAuthType_Object=MibTableColumn
raisecomOspfIfAuthType=_RaisecomOspfIfAuthType_Object((1,3,6,1,4,1,8886,1,47,2,6,1,22),_RaisecomOspfIfAuthType_Type())
raisecomOspfIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfAuthType.setStatus(_A)
_RaisecomOspfIfLsaCount_Type=Gauge32
_RaisecomOspfIfLsaCount_Object=MibTableColumn
raisecomOspfIfLsaCount=_RaisecomOspfIfLsaCount_Object((1,3,6,1,4,1,8886,1,47,2,6,1,23),_RaisecomOspfIfLsaCount_Type())
raisecomOspfIfLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfIfLsaCount.setStatus(_A)
_RaisecomOspfIfLsaCksumSum_Type=Unsigned32
_RaisecomOspfIfLsaCksumSum_Object=MibTableColumn
raisecomOspfIfLsaCksumSum=_RaisecomOspfIfLsaCksumSum_Object((1,3,6,1,4,1,8886,1,47,2,6,1,24),_RaisecomOspfIfLsaCksumSum_Type())
raisecomOspfIfLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfIfLsaCksumSum.setStatus(_A)
_RaisecomOspfIfDesignatedRouterId_Type=RouterID
_RaisecomOspfIfDesignatedRouterId_Object=MibTableColumn
raisecomOspfIfDesignatedRouterId=_RaisecomOspfIfDesignatedRouterId_Object((1,3,6,1,4,1,8886,1,47,2,6,1,25),_RaisecomOspfIfDesignatedRouterId_Type())
raisecomOspfIfDesignatedRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfIfDesignatedRouterId.setStatus(_A)
_RaisecomOspfIfBackupDesignatedRouterId_Type=RouterID
_RaisecomOspfIfBackupDesignatedRouterId_Object=MibTableColumn
raisecomOspfIfBackupDesignatedRouterId=_RaisecomOspfIfBackupDesignatedRouterId_Object((1,3,6,1,4,1,8886,1,47,2,6,1,26),_RaisecomOspfIfBackupDesignatedRouterId_Type())
raisecomOspfIfBackupDesignatedRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfIfBackupDesignatedRouterId.setStatus(_A)
class _RaisecomOspfIfPassive_Type(EnableVar):defaultValue=2
_RaisecomOspfIfPassive_Type.__name__=_T
_RaisecomOspfIfPassive_Object=MibTableColumn
raisecomOspfIfPassive=_RaisecomOspfIfPassive_Object((1,3,6,1,4,1,8886,1,47,2,6,1,27),_RaisecomOspfIfPassive_Type())
raisecomOspfIfPassive.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfPassive.setStatus(_A)
class _RaisecomOspfIfMtu_Type(EnableVar):defaultValue=1
_RaisecomOspfIfMtu_Type.__name__=_T
_RaisecomOspfIfMtu_Object=MibTableColumn
raisecomOspfIfMtu=_RaisecomOspfIfMtu_Object((1,3,6,1,4,1,8886,1,47,2,6,1,28),_RaisecomOspfIfMtu_Type())
raisecomOspfIfMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfMtu.setStatus(_A)
_RaisecomOspfIfMetric_Type=Metric
_RaisecomOspfIfMetric_Object=MibTableColumn
raisecomOspfIfMetric=_RaisecomOspfIfMetric_Object((1,3,6,1,4,1,8886,1,47,2,6,1,29),_RaisecomOspfIfMetric_Type())
raisecomOspfIfMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfIfMetric.setStatus(_A)
_RaisecomOspfVirtIfTable_Object=MibTable
raisecomOspfVirtIfTable=_RaisecomOspfVirtIfTable_Object((1,3,6,1,4,1,8886,1,47,2,7))
if mibBuilder.loadTexts:raisecomOspfVirtIfTable.setStatus(_A)
_RaisecomOspfVirtIfEntry_Object=MibTableRow
raisecomOspfVirtIfEntry=_RaisecomOspfVirtIfEntry_Object((1,3,6,1,4,1,8886,1,47,2,7,1))
raisecomOspfVirtIfEntry.setIndexNames((0,_B,_F),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:raisecomOspfVirtIfEntry.setStatus(_A)
_RaisecomOspfVirtIfAreaId_Type=AreaID
_RaisecomOspfVirtIfAreaId_Object=MibTableColumn
raisecomOspfVirtIfAreaId=_RaisecomOspfVirtIfAreaId_Object((1,3,6,1,4,1,8886,1,47,2,7,1,1),_RaisecomOspfVirtIfAreaId_Type())
raisecomOspfVirtIfAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtIfAreaId.setStatus(_A)
_RaisecomOspfVirtIfNeighbor_Type=RouterID
_RaisecomOspfVirtIfNeighbor_Object=MibTableColumn
raisecomOspfVirtIfNeighbor=_RaisecomOspfVirtIfNeighbor_Object((1,3,6,1,4,1,8886,1,47,2,7,1,2),_RaisecomOspfVirtIfNeighbor_Type())
raisecomOspfVirtIfNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtIfNeighbor.setStatus(_A)
class _RaisecomOspfVirtIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_RaisecomOspfVirtIfTransitDelay_Type.__name__=_V
_RaisecomOspfVirtIfTransitDelay_Object=MibTableColumn
raisecomOspfVirtIfTransitDelay=_RaisecomOspfVirtIfTransitDelay_Object((1,3,6,1,4,1,8886,1,47,2,7,1,3),_RaisecomOspfVirtIfTransitDelay_Type())
raisecomOspfVirtIfTransitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfVirtIfTransitDelay.setStatus(_A)
if mibBuilder.loadTexts:raisecomOspfVirtIfTransitDelay.setUnits(_I)
class _RaisecomOspfVirtIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_RaisecomOspfVirtIfRetransInterval_Type.__name__=_V
_RaisecomOspfVirtIfRetransInterval_Object=MibTableColumn
raisecomOspfVirtIfRetransInterval=_RaisecomOspfVirtIfRetransInterval_Object((1,3,6,1,4,1,8886,1,47,2,7,1,4),_RaisecomOspfVirtIfRetransInterval_Type())
raisecomOspfVirtIfRetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfVirtIfRetransInterval.setStatus(_A)
if mibBuilder.loadTexts:raisecomOspfVirtIfRetransInterval.setUnits(_I)
class _RaisecomOspfVirtIfHelloInterval_Type(HelloRange):defaultValue=10
_RaisecomOspfVirtIfHelloInterval_Type.__name__=_t
_RaisecomOspfVirtIfHelloInterval_Object=MibTableColumn
raisecomOspfVirtIfHelloInterval=_RaisecomOspfVirtIfHelloInterval_Object((1,3,6,1,4,1,8886,1,47,2,7,1,5),_RaisecomOspfVirtIfHelloInterval_Type())
raisecomOspfVirtIfHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfVirtIfHelloInterval.setStatus(_A)
if mibBuilder.loadTexts:raisecomOspfVirtIfHelloInterval.setUnits(_I)
class _RaisecomOspfVirtIfRtrDeadInterval_Type(PositiveInteger):defaultValue=60
_RaisecomOspfVirtIfRtrDeadInterval_Type.__name__=_P
_RaisecomOspfVirtIfRtrDeadInterval_Object=MibTableColumn
raisecomOspfVirtIfRtrDeadInterval=_RaisecomOspfVirtIfRtrDeadInterval_Object((1,3,6,1,4,1,8886,1,47,2,7,1,6),_RaisecomOspfVirtIfRtrDeadInterval_Type())
raisecomOspfVirtIfRtrDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfVirtIfRtrDeadInterval.setStatus(_A)
if mibBuilder.loadTexts:raisecomOspfVirtIfRtrDeadInterval.setUnits(_I)
class _RaisecomOspfVirtIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_c,1),(_s,4)))
_RaisecomOspfVirtIfState_Type.__name__=_E
_RaisecomOspfVirtIfState_Object=MibTableColumn
raisecomOspfVirtIfState=_RaisecomOspfVirtIfState_Object((1,3,6,1,4,1,8886,1,47,2,7,1,7),_RaisecomOspfVirtIfState_Type())
raisecomOspfVirtIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtIfState.setStatus(_A)
_RaisecomOspfVirtIfEvents_Type=Counter32
_RaisecomOspfVirtIfEvents_Object=MibTableColumn
raisecomOspfVirtIfEvents=_RaisecomOspfVirtIfEvents_Object((1,3,6,1,4,1,8886,1,47,2,7,1,8),_RaisecomOspfVirtIfEvents_Type())
raisecomOspfVirtIfEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtIfEvents.setStatus(_A)
class _RaisecomOspfVirtIfAuthKeyId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomOspfVirtIfAuthKeyId_Type.__name__=_E
_RaisecomOspfVirtIfAuthKeyId_Object=MibTableColumn
raisecomOspfVirtIfAuthKeyId=_RaisecomOspfVirtIfAuthKeyId_Object((1,3,6,1,4,1,8886,1,47,2,7,1,9),_RaisecomOspfVirtIfAuthKeyId_Type())
raisecomOspfVirtIfAuthKeyId.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfVirtIfAuthKeyId.setStatus(_A)
class _RaisecomOspfVirtIfAuthSimpleKeyType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,7)));namedValues=NamedValues(*((_d,0),(_e,7)))
_RaisecomOspfVirtIfAuthSimpleKeyType_Type.__name__=_E
_RaisecomOspfVirtIfAuthSimpleKeyType_Object=MibTableColumn
raisecomOspfVirtIfAuthSimpleKeyType=_RaisecomOspfVirtIfAuthSimpleKeyType_Object((1,3,6,1,4,1,8886,1,47,2,7,1,10),_RaisecomOspfVirtIfAuthSimpleKeyType_Type())
raisecomOspfVirtIfAuthSimpleKeyType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfVirtIfAuthSimpleKeyType.setStatus(_A)
class _RaisecomOspfVirtIfAuthMd5KeyType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,7)));namedValues=NamedValues(*((_d,0),(_e,7)))
_RaisecomOspfVirtIfAuthMd5KeyType_Type.__name__=_E
_RaisecomOspfVirtIfAuthMd5KeyType_Object=MibTableColumn
raisecomOspfVirtIfAuthMd5KeyType=_RaisecomOspfVirtIfAuthMd5KeyType_Object((1,3,6,1,4,1,8886,1,47,2,7,1,11),_RaisecomOspfVirtIfAuthMd5KeyType_Type())
raisecomOspfVirtIfAuthMd5KeyType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfVirtIfAuthMd5KeyType.setStatus(_A)
class _RaisecomOspfVirtIfAuthSimpleKey_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,68))
_RaisecomOspfVirtIfAuthSimpleKey_Type.__name__=_H
_RaisecomOspfVirtIfAuthSimpleKey_Object=MibTableColumn
raisecomOspfVirtIfAuthSimpleKey=_RaisecomOspfVirtIfAuthSimpleKey_Object((1,3,6,1,4,1,8886,1,47,2,7,1,12),_RaisecomOspfVirtIfAuthSimpleKey_Type())
raisecomOspfVirtIfAuthSimpleKey.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfVirtIfAuthSimpleKey.setStatus(_A)
class _RaisecomOspfVirtIfAuthMd5Key_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,68))
_RaisecomOspfVirtIfAuthMd5Key_Type.__name__=_H
_RaisecomOspfVirtIfAuthMd5Key_Object=MibTableColumn
raisecomOspfVirtIfAuthMd5Key=_RaisecomOspfVirtIfAuthMd5Key_Object((1,3,6,1,4,1,8886,1,47,2,7,1,13),_RaisecomOspfVirtIfAuthMd5Key_Type())
raisecomOspfVirtIfAuthMd5Key.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfVirtIfAuthMd5Key.setStatus(_A)
class _RaisecomOspfVirtIfAuthKeyChain_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RaisecomOspfVirtIfAuthKeyChain_Type.__name__=_H
_RaisecomOspfVirtIfAuthKeyChain_Object=MibTableColumn
raisecomOspfVirtIfAuthKeyChain=_RaisecomOspfVirtIfAuthKeyChain_Object((1,3,6,1,4,1,8886,1,47,2,7,1,14),_RaisecomOspfVirtIfAuthKeyChain_Type())
raisecomOspfVirtIfAuthKeyChain.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfVirtIfAuthKeyChain.setStatus(_A)
class _RaisecomOspfVirtIfAuthType_Type(OspfAuthenticationType):defaultValue=0
_RaisecomOspfVirtIfAuthType_Type.__name__=_Z
_RaisecomOspfVirtIfAuthType_Object=MibTableColumn
raisecomOspfVirtIfAuthType=_RaisecomOspfVirtIfAuthType_Object((1,3,6,1,4,1,8886,1,47,2,7,1,15),_RaisecomOspfVirtIfAuthType_Type())
raisecomOspfVirtIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfVirtIfAuthType.setStatus(_A)
_RaisecomOspfVirtIfLsaCount_Type=Gauge32
_RaisecomOspfVirtIfLsaCount_Object=MibTableColumn
raisecomOspfVirtIfLsaCount=_RaisecomOspfVirtIfLsaCount_Object((1,3,6,1,4,1,8886,1,47,2,7,1,16),_RaisecomOspfVirtIfLsaCount_Type())
raisecomOspfVirtIfLsaCount.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtIfLsaCount.setStatus(_A)
_RaisecomOspfVirtIfLsaCksumSum_Type=Unsigned32
_RaisecomOspfVirtIfLsaCksumSum_Object=MibTableColumn
raisecomOspfVirtIfLsaCksumSum=_RaisecomOspfVirtIfLsaCksumSum_Object((1,3,6,1,4,1,8886,1,47,2,7,1,17),_RaisecomOspfVirtIfLsaCksumSum_Type())
raisecomOspfVirtIfLsaCksumSum.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtIfLsaCksumSum.setStatus(_A)
class _RaisecomOspfVirtIfCost_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RaisecomOspfVirtIfCost_Type.__name__=_E
_RaisecomOspfVirtIfCost_Object=MibTableColumn
raisecomOspfVirtIfCost=_RaisecomOspfVirtIfCost_Object((1,3,6,1,4,1,8886,1,47,2,7,1,18),_RaisecomOspfVirtIfCost_Type())
raisecomOspfVirtIfCost.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtIfCost.setStatus(_A)
_RaisecomOspfVirtIfStatus_Type=RowStatus
_RaisecomOspfVirtIfStatus_Object=MibTableColumn
raisecomOspfVirtIfStatus=_RaisecomOspfVirtIfStatus_Object((1,3,6,1,4,1,8886,1,47,2,7,1,19),_RaisecomOspfVirtIfStatus_Type())
raisecomOspfVirtIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfVirtIfStatus.setStatus(_A)
_RaisecomOspfNbrTable_Object=MibTable
raisecomOspfNbrTable=_RaisecomOspfNbrTable_Object((1,3,6,1,4,1,8886,1,47,2,8))
if mibBuilder.loadTexts:raisecomOspfNbrTable.setStatus(_A)
_RaisecomOspfNbrEntry_Object=MibTableRow
raisecomOspfNbrEntry=_RaisecomOspfNbrEntry_Object((1,3,6,1,4,1,8886,1,47,2,8,1))
raisecomOspfNbrEntry.setIndexNames((0,_B,_F),(0,_B,_u))
if mibBuilder.loadTexts:raisecomOspfNbrEntry.setStatus(_A)
_RaisecomOspfNbrIpAddr_Type=IpAddress
_RaisecomOspfNbrIpAddr_Object=MibTableColumn
raisecomOspfNbrIpAddr=_RaisecomOspfNbrIpAddr_Object((1,3,6,1,4,1,8886,1,47,2,8,1,1),_RaisecomOspfNbrIpAddr_Type())
raisecomOspfNbrIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNbrIpAddr.setStatus(_A)
_RaisecomOspfNbrAddressLessIndex_Type=InterfaceIndexOrZero
_RaisecomOspfNbrAddressLessIndex_Object=MibTableColumn
raisecomOspfNbrAddressLessIndex=_RaisecomOspfNbrAddressLessIndex_Object((1,3,6,1,4,1,8886,1,47,2,8,1,2),_RaisecomOspfNbrAddressLessIndex_Type())
raisecomOspfNbrAddressLessIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNbrAddressLessIndex.setStatus(_A)
class _RaisecomOspfNbrRtrId_Type(RouterID):defaultHexValue=_a
_RaisecomOspfNbrRtrId_Type.__name__='RouterID'
_RaisecomOspfNbrRtrId_Object=MibTableColumn
raisecomOspfNbrRtrId=_RaisecomOspfNbrRtrId_Object((1,3,6,1,4,1,8886,1,47,2,8,1,3),_RaisecomOspfNbrRtrId_Type())
raisecomOspfNbrRtrId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNbrRtrId.setStatus(_A)
class _RaisecomOspfNbrOptions_Type(Integer32):defaultValue=0
_RaisecomOspfNbrOptions_Type.__name__=_E
_RaisecomOspfNbrOptions_Object=MibTableColumn
raisecomOspfNbrOptions=_RaisecomOspfNbrOptions_Object((1,3,6,1,4,1,8886,1,47,2,8,1,4),_RaisecomOspfNbrOptions_Type())
raisecomOspfNbrOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNbrOptions.setStatus(_A)
class _RaisecomOspfNbrPriority_Type(DesignatedRouterPriority):defaultValue=1
_RaisecomOspfNbrPriority_Type.__name__=_b
_RaisecomOspfNbrPriority_Object=MibTableColumn
raisecomOspfNbrPriority=_RaisecomOspfNbrPriority_Object((1,3,6,1,4,1,8886,1,47,2,8,1,5),_RaisecomOspfNbrPriority_Type())
raisecomOspfNbrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNbrPriority.setStatus(_A)
class _RaisecomOspfNbrState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_c,1),('attempt',2),('init',3),('twoWay',4),(_AB,5),('exchange',6),('loading',7),('full',8)))
_RaisecomOspfNbrState_Type.__name__=_E
_RaisecomOspfNbrState_Object=MibTableColumn
raisecomOspfNbrState=_RaisecomOspfNbrState_Object((1,3,6,1,4,1,8886,1,47,2,8,1,6),_RaisecomOspfNbrState_Type())
raisecomOspfNbrState.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNbrState.setStatus(_A)
_RaisecomOspfNbrEvents_Type=Counter32
_RaisecomOspfNbrEvents_Object=MibTableColumn
raisecomOspfNbrEvents=_RaisecomOspfNbrEvents_Object((1,3,6,1,4,1,8886,1,47,2,8,1,7),_RaisecomOspfNbrEvents_Type())
raisecomOspfNbrEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNbrEvents.setStatus(_A)
_RaisecomOspfNbrLsRetransQLen_Type=Gauge32
_RaisecomOspfNbrLsRetransQLen_Object=MibTableColumn
raisecomOspfNbrLsRetransQLen=_RaisecomOspfNbrLsRetransQLen_Object((1,3,6,1,4,1,8886,1,47,2,8,1,8),_RaisecomOspfNbrLsRetransQLen_Type())
raisecomOspfNbrLsRetransQLen.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNbrLsRetransQLen.setStatus(_A)
class _RaisecomOspfNbrMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('slave',1),('master',2)))
_RaisecomOspfNbrMode_Type.__name__=_E
_RaisecomOspfNbrMode_Object=MibTableColumn
raisecomOspfNbrMode=_RaisecomOspfNbrMode_Object((1,3,6,1,4,1,8886,1,47,2,8,1,9),_RaisecomOspfNbrMode_Type())
raisecomOspfNbrMode.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNbrMode.setStatus(_A)
_RaisecomOspfNbmaCfgNbrTable_Object=MibTable
raisecomOspfNbmaCfgNbrTable=_RaisecomOspfNbmaCfgNbrTable_Object((1,3,6,1,4,1,8886,1,47,2,9))
if mibBuilder.loadTexts:raisecomOspfNbmaCfgNbrTable.setStatus(_A)
_RaisecomOspfNbmaCfgNbrEntry_Object=MibTableRow
raisecomOspfNbmaCfgNbrEntry=_RaisecomOspfNbmaCfgNbrEntry_Object((1,3,6,1,4,1,8886,1,47,2,9,1))
raisecomOspfNbmaCfgNbrEntry.setIndexNames((0,_B,_F),(0,_B,_AC))
if mibBuilder.loadTexts:raisecomOspfNbmaCfgNbrEntry.setStatus(_A)
_RaisecomOspfNbmaCfgNbrIpAddr_Type=IpAddress
_RaisecomOspfNbmaCfgNbrIpAddr_Object=MibTableColumn
raisecomOspfNbmaCfgNbrIpAddr=_RaisecomOspfNbmaCfgNbrIpAddr_Object((1,3,6,1,4,1,8886,1,47,2,9,1,1),_RaisecomOspfNbmaCfgNbrIpAddr_Type())
raisecomOspfNbmaCfgNbrIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfNbmaCfgNbrIpAddr.setStatus(_A)
class _RaisecomOspfNbmaCfgNbrPriority_Type(DesignatedRouterPriority):defaultValue=1
_RaisecomOspfNbmaCfgNbrPriority_Type.__name__=_b
_RaisecomOspfNbmaCfgNbrPriority_Object=MibTableColumn
raisecomOspfNbmaCfgNbrPriority=_RaisecomOspfNbmaCfgNbrPriority_Object((1,3,6,1,4,1,8886,1,47,2,9,1,2),_RaisecomOspfNbmaCfgNbrPriority_Type())
raisecomOspfNbmaCfgNbrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfNbmaCfgNbrPriority.setStatus(_A)
_RaisecomOspfNbmaCfgNbrStatus_Type=RowStatus
_RaisecomOspfNbmaCfgNbrStatus_Object=MibTableColumn
raisecomOspfNbmaCfgNbrStatus=_RaisecomOspfNbmaCfgNbrStatus_Object((1,3,6,1,4,1,8886,1,47,2,9,1,3),_RaisecomOspfNbmaCfgNbrStatus_Type())
raisecomOspfNbmaCfgNbrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfNbmaCfgNbrStatus.setStatus(_A)
_RaisecomOspfVirtNbrTable_Object=MibTable
raisecomOspfVirtNbrTable=_RaisecomOspfVirtNbrTable_Object((1,3,6,1,4,1,8886,1,47,2,10))
if mibBuilder.loadTexts:raisecomOspfVirtNbrTable.setStatus(_A)
_RaisecomOspfVirtNbrEntry_Object=MibTableRow
raisecomOspfVirtNbrEntry=_RaisecomOspfVirtNbrEntry_Object((1,3,6,1,4,1,8886,1,47,2,10,1))
raisecomOspfVirtNbrEntry.setIndexNames((0,_B,_F),(0,_B,_v),(0,_B,_w))
if mibBuilder.loadTexts:raisecomOspfVirtNbrEntry.setStatus(_A)
_RaisecomOspfVirtNbrArea_Type=AreaID
_RaisecomOspfVirtNbrArea_Object=MibTableColumn
raisecomOspfVirtNbrArea=_RaisecomOspfVirtNbrArea_Object((1,3,6,1,4,1,8886,1,47,2,10,1,1),_RaisecomOspfVirtNbrArea_Type())
raisecomOspfVirtNbrArea.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtNbrArea.setStatus(_A)
_RaisecomOspfVirtNbrRtrId_Type=RouterID
_RaisecomOspfVirtNbrRtrId_Object=MibTableColumn
raisecomOspfVirtNbrRtrId=_RaisecomOspfVirtNbrRtrId_Object((1,3,6,1,4,1,8886,1,47,2,10,1,2),_RaisecomOspfVirtNbrRtrId_Type())
raisecomOspfVirtNbrRtrId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtNbrRtrId.setStatus(_A)
_RaisecomOspfVirtNbrIpAddr_Type=IpAddress
_RaisecomOspfVirtNbrIpAddr_Object=MibTableColumn
raisecomOspfVirtNbrIpAddr=_RaisecomOspfVirtNbrIpAddr_Object((1,3,6,1,4,1,8886,1,47,2,10,1,3),_RaisecomOspfVirtNbrIpAddr_Type())
raisecomOspfVirtNbrIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtNbrIpAddr.setStatus(_A)
_RaisecomOspfVirtNbrOptions_Type=Integer32
_RaisecomOspfVirtNbrOptions_Object=MibTableColumn
raisecomOspfVirtNbrOptions=_RaisecomOspfVirtNbrOptions_Object((1,3,6,1,4,1,8886,1,47,2,10,1,4),_RaisecomOspfVirtNbrOptions_Type())
raisecomOspfVirtNbrOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtNbrOptions.setStatus(_A)
class _RaisecomOspfVirtNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_c,1),('attempt',2),('init',3),('twoWay',4),(_AB,5),('exchange',6),('loading',7),('full',8)))
_RaisecomOspfVirtNbrState_Type.__name__=_E
_RaisecomOspfVirtNbrState_Object=MibTableColumn
raisecomOspfVirtNbrState=_RaisecomOspfVirtNbrState_Object((1,3,6,1,4,1,8886,1,47,2,10,1,5),_RaisecomOspfVirtNbrState_Type())
raisecomOspfVirtNbrState.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtNbrState.setStatus(_A)
_RaisecomOspfVirtNbrEvents_Type=Counter32
_RaisecomOspfVirtNbrEvents_Object=MibTableColumn
raisecomOspfVirtNbrEvents=_RaisecomOspfVirtNbrEvents_Object((1,3,6,1,4,1,8886,1,47,2,10,1,6),_RaisecomOspfVirtNbrEvents_Type())
raisecomOspfVirtNbrEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtNbrEvents.setStatus(_A)
_RaisecomOspfVirtNbrLsRetransQLen_Type=Gauge32
_RaisecomOspfVirtNbrLsRetransQLen_Object=MibTableColumn
raisecomOspfVirtNbrLsRetransQLen=_RaisecomOspfVirtNbrLsRetransQLen_Object((1,3,6,1,4,1,8886,1,47,2,10,1,7),_RaisecomOspfVirtNbrLsRetransQLen_Type())
raisecomOspfVirtNbrLsRetransQLen.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtNbrLsRetransQLen.setStatus(_A)
_RaisecomOspfVirtNbrLessIf_Type=Integer32
_RaisecomOspfVirtNbrLessIf_Object=MibTableColumn
raisecomOspfVirtNbrLessIf=_RaisecomOspfVirtNbrLessIf_Object((1,3,6,1,4,1,8886,1,47,2,10,1,8),_RaisecomOspfVirtNbrLessIf_Type())
raisecomOspfVirtNbrLessIf.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtNbrLessIf.setStatus(_A)
class _RaisecomOspfVirtNbrMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('slave',1),('master',2)))
_RaisecomOspfVirtNbrMode_Type.__name__=_E
_RaisecomOspfVirtNbrMode_Object=MibTableColumn
raisecomOspfVirtNbrMode=_RaisecomOspfVirtNbrMode_Object((1,3,6,1,4,1,8886,1,47,2,10,1,9),_RaisecomOspfVirtNbrMode_Type())
raisecomOspfVirtNbrMode.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfVirtNbrMode.setStatus(_A)
_RaisecomOspfAreaAggregateTable_Object=MibTable
raisecomOspfAreaAggregateTable=_RaisecomOspfAreaAggregateTable_Object((1,3,6,1,4,1,8886,1,47,2,11))
if mibBuilder.loadTexts:raisecomOspfAreaAggregateTable.setStatus(_A)
_RaisecomOspfAreaAggregateEntry_Object=MibTableRow
raisecomOspfAreaAggregateEntry=_RaisecomOspfAreaAggregateEntry_Object((1,3,6,1,4,1,8886,1,47,2,11,1))
raisecomOspfAreaAggregateEntry.setIndexNames((0,_B,_F),(0,_B,_AD),(0,_B,_AE),(0,_B,_AF),(0,_B,_AG))
if mibBuilder.loadTexts:raisecomOspfAreaAggregateEntry.setStatus(_A)
_RaisecomOspfAreaAggregateAreaID_Type=AreaID
_RaisecomOspfAreaAggregateAreaID_Object=MibTableColumn
raisecomOspfAreaAggregateAreaID=_RaisecomOspfAreaAggregateAreaID_Object((1,3,6,1,4,1,8886,1,47,2,11,1,1),_RaisecomOspfAreaAggregateAreaID_Type())
raisecomOspfAreaAggregateAreaID.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaAggregateAreaID.setStatus(_A)
class _RaisecomOspfAreaAggregateLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,7)));namedValues=NamedValues(*((_W,3),(_X,7)))
_RaisecomOspfAreaAggregateLsdbType_Type.__name__=_E
_RaisecomOspfAreaAggregateLsdbType_Object=MibTableColumn
raisecomOspfAreaAggregateLsdbType=_RaisecomOspfAreaAggregateLsdbType_Object((1,3,6,1,4,1,8886,1,47,2,11,1,2),_RaisecomOspfAreaAggregateLsdbType_Type())
raisecomOspfAreaAggregateLsdbType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaAggregateLsdbType.setStatus(_A)
_RaisecomOspfAreaAggregateNet_Type=IpAddress
_RaisecomOspfAreaAggregateNet_Object=MibTableColumn
raisecomOspfAreaAggregateNet=_RaisecomOspfAreaAggregateNet_Object((1,3,6,1,4,1,8886,1,47,2,11,1,3),_RaisecomOspfAreaAggregateNet_Type())
raisecomOspfAreaAggregateNet.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaAggregateNet.setStatus(_A)
_RaisecomOspfAreaAggregateMask_Type=IpAddress
_RaisecomOspfAreaAggregateMask_Object=MibTableColumn
raisecomOspfAreaAggregateMask=_RaisecomOspfAreaAggregateMask_Object((1,3,6,1,4,1,8886,1,47,2,11,1,4),_RaisecomOspfAreaAggregateMask_Type())
raisecomOspfAreaAggregateMask.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaAggregateMask.setStatus(_A)
class _RaisecomOspfAreaAggregateEffect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('advertiseMatching',1),('doNotAdvertiseMatching',2)))
_RaisecomOspfAreaAggregateEffect_Type.__name__=_E
_RaisecomOspfAreaAggregateEffect_Object=MibTableColumn
raisecomOspfAreaAggregateEffect=_RaisecomOspfAreaAggregateEffect_Object((1,3,6,1,4,1,8886,1,47,2,11,1,5),_RaisecomOspfAreaAggregateEffect_Type())
raisecomOspfAreaAggregateEffect.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfAreaAggregateEffect.setStatus(_A)
_RaisecomOspfAreaAggregateStatus_Type=RowStatus
_RaisecomOspfAreaAggregateStatus_Object=MibTableColumn
raisecomOspfAreaAggregateStatus=_RaisecomOspfAreaAggregateStatus_Object((1,3,6,1,4,1,8886,1,47,2,11,1,6),_RaisecomOspfAreaAggregateStatus_Type())
raisecomOspfAreaAggregateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfAreaAggregateStatus.setStatus(_A)
_RaisecomOspfExternalAggregateTable_Object=MibTable
raisecomOspfExternalAggregateTable=_RaisecomOspfExternalAggregateTable_Object((1,3,6,1,4,1,8886,1,47,2,12))
if mibBuilder.loadTexts:raisecomOspfExternalAggregateTable.setStatus(_A)
_RaisecomOspfExternalAggregateEntry_Object=MibTableRow
raisecomOspfExternalAggregateEntry=_RaisecomOspfExternalAggregateEntry_Object((1,3,6,1,4,1,8886,1,47,2,12,1))
raisecomOspfExternalAggregateEntry.setIndexNames((0,_B,_F),(0,_B,_AH),(0,_B,_AI))
if mibBuilder.loadTexts:raisecomOspfExternalAggregateEntry.setStatus(_A)
_RaisecomOspfExternalAggregateNet_Type=IpAddress
_RaisecomOspfExternalAggregateNet_Object=MibTableColumn
raisecomOspfExternalAggregateNet=_RaisecomOspfExternalAggregateNet_Object((1,3,6,1,4,1,8886,1,47,2,12,1,1),_RaisecomOspfExternalAggregateNet_Type())
raisecomOspfExternalAggregateNet.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfExternalAggregateNet.setStatus(_A)
_RaisecomOspfExternalAggregateMask_Type=IpAddress
_RaisecomOspfExternalAggregateMask_Object=MibTableColumn
raisecomOspfExternalAggregateMask=_RaisecomOspfExternalAggregateMask_Object((1,3,6,1,4,1,8886,1,47,2,12,1,2),_RaisecomOspfExternalAggregateMask_Type())
raisecomOspfExternalAggregateMask.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfExternalAggregateMask.setStatus(_A)
class _RaisecomOspfExternalAggregateEffect_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A5,1),(_A6,2)))
_RaisecomOspfExternalAggregateEffect_Type.__name__=_E
_RaisecomOspfExternalAggregateEffect_Object=MibTableColumn
raisecomOspfExternalAggregateEffect=_RaisecomOspfExternalAggregateEffect_Object((1,3,6,1,4,1,8886,1,47,2,12,1,3),_RaisecomOspfExternalAggregateEffect_Type())
raisecomOspfExternalAggregateEffect.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfExternalAggregateEffect.setStatus(_A)
class _RaisecomOspfExternalAggregateCost_Type(BigMetric):defaultValue=1
_RaisecomOspfExternalAggregateCost_Type.__name__=_U
_RaisecomOspfExternalAggregateCost_Object=MibTableColumn
raisecomOspfExternalAggregateCost=_RaisecomOspfExternalAggregateCost_Object((1,3,6,1,4,1,8886,1,47,2,12,1,4),_RaisecomOspfExternalAggregateCost_Type())
raisecomOspfExternalAggregateCost.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfExternalAggregateCost.setStatus(_A)
_RaisecomOspfExternalAggregateStatus_Type=RowStatus
_RaisecomOspfExternalAggregateStatus_Object=MibTableColumn
raisecomOspfExternalAggregateStatus=_RaisecomOspfExternalAggregateStatus_Object((1,3,6,1,4,1,8886,1,47,2,12,1,5),_RaisecomOspfExternalAggregateStatus_Type())
raisecomOspfExternalAggregateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfExternalAggregateStatus.setStatus(_A)
_RaisecomOspfLsdbTable_Object=MibTable
raisecomOspfLsdbTable=_RaisecomOspfLsdbTable_Object((1,3,6,1,4,1,8886,1,47,2,13))
if mibBuilder.loadTexts:raisecomOspfLsdbTable.setStatus(_A)
_RaisecomOspfLsdbEntry_Object=MibTableRow
raisecomOspfLsdbEntry=_RaisecomOspfLsdbEntry_Object((1,3,6,1,4,1,8886,1,47,2,13,1))
raisecomOspfLsdbEntry.setIndexNames((0,_B,_F),(0,_B,_f),(0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:raisecomOspfLsdbEntry.setStatus(_A)
_RaisecomOspfLsdbAreaId_Type=AreaID
_RaisecomOspfLsdbAreaId_Object=MibTableColumn
raisecomOspfLsdbAreaId=_RaisecomOspfLsdbAreaId_Object((1,3,6,1,4,1,8886,1,47,2,13,1,1),_RaisecomOspfLsdbAreaId_Type())
raisecomOspfLsdbAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfLsdbAreaId.setStatus(_A)
class _RaisecomOspfLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,10)));namedValues=NamedValues(*((_g,1),(_h,2),(_W,3),(_i,4),(_j,5),(_k,6),(_X,7),(_l,10)))
_RaisecomOspfLsdbType_Type.__name__=_E
_RaisecomOspfLsdbType_Object=MibTableColumn
raisecomOspfLsdbType=_RaisecomOspfLsdbType_Object((1,3,6,1,4,1,8886,1,47,2,13,1,2),_RaisecomOspfLsdbType_Type())
raisecomOspfLsdbType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfLsdbType.setStatus(_A)
_RaisecomOspfLsdbLsId_Type=IpAddress
_RaisecomOspfLsdbLsId_Object=MibTableColumn
raisecomOspfLsdbLsId=_RaisecomOspfLsdbLsId_Object((1,3,6,1,4,1,8886,1,47,2,13,1,3),_RaisecomOspfLsdbLsId_Type())
raisecomOspfLsdbLsId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfLsdbLsId.setStatus(_A)
_RaisecomOspfLsdbRouterId_Type=RouterID
_RaisecomOspfLsdbRouterId_Object=MibTableColumn
raisecomOspfLsdbRouterId=_RaisecomOspfLsdbRouterId_Object((1,3,6,1,4,1,8886,1,47,2,13,1,4),_RaisecomOspfLsdbRouterId_Type())
raisecomOspfLsdbRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfLsdbRouterId.setStatus(_A)
_RaisecomOspfLsdbSequence_Type=Integer32
_RaisecomOspfLsdbSequence_Object=MibTableColumn
raisecomOspfLsdbSequence=_RaisecomOspfLsdbSequence_Object((1,3,6,1,4,1,8886,1,47,2,13,1,5),_RaisecomOspfLsdbSequence_Type())
raisecomOspfLsdbSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfLsdbSequence.setStatus(_A)
_RaisecomOspfLsdbAge_Type=Integer32
_RaisecomOspfLsdbAge_Object=MibTableColumn
raisecomOspfLsdbAge=_RaisecomOspfLsdbAge_Object((1,3,6,1,4,1,8886,1,47,2,13,1,6),_RaisecomOspfLsdbAge_Type())
raisecomOspfLsdbAge.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:raisecomOspfLsdbAge.setUnits(_I)
_RaisecomOspfLsdbChecksum_Type=Integer32
_RaisecomOspfLsdbChecksum_Object=MibTableColumn
raisecomOspfLsdbChecksum=_RaisecomOspfLsdbChecksum_Object((1,3,6,1,4,1,8886,1,47,2,13,1,7),_RaisecomOspfLsdbChecksum_Type())
raisecomOspfLsdbChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfLsdbChecksum.setStatus(_A)
class _RaisecomOspfLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_RaisecomOspfLsdbAdvertisement_Type.__name__=_H
_RaisecomOspfLsdbAdvertisement_Object=MibTableColumn
raisecomOspfLsdbAdvertisement=_RaisecomOspfLsdbAdvertisement_Object((1,3,6,1,4,1,8886,1,47,2,13,1,8),_RaisecomOspfLsdbAdvertisement_Type())
raisecomOspfLsdbAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfLsdbAdvertisement.setStatus(_A)
_RaisecomOspfAsLsdbTable_Object=MibTable
raisecomOspfAsLsdbTable=_RaisecomOspfAsLsdbTable_Object((1,3,6,1,4,1,8886,1,47,2,14))
if mibBuilder.loadTexts:raisecomOspfAsLsdbTable.setStatus(_A)
_RaisecomOspfAsLsdbEntry_Object=MibTableRow
raisecomOspfAsLsdbEntry=_RaisecomOspfAsLsdbEntry_Object((1,3,6,1,4,1,8886,1,47,2,14,1))
raisecomOspfAsLsdbEntry.setIndexNames((0,_B,_F),(0,_B,_AJ),(0,_B,_AK),(0,_B,_AL))
if mibBuilder.loadTexts:raisecomOspfAsLsdbEntry.setStatus(_A)
class _RaisecomOspfAsLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues((_j,5))
_RaisecomOspfAsLsdbType_Type.__name__=_E
_RaisecomOspfAsLsdbType_Object=MibTableColumn
raisecomOspfAsLsdbType=_RaisecomOspfAsLsdbType_Object((1,3,6,1,4,1,8886,1,47,2,14,1,1),_RaisecomOspfAsLsdbType_Type())
raisecomOspfAsLsdbType.setMaxAccess(_x)
if mibBuilder.loadTexts:raisecomOspfAsLsdbType.setStatus(_A)
_RaisecomOspfAsLsdbLsId_Type=IpAddress
_RaisecomOspfAsLsdbLsId_Object=MibTableColumn
raisecomOspfAsLsdbLsId=_RaisecomOspfAsLsdbLsId_Object((1,3,6,1,4,1,8886,1,47,2,14,1,2),_RaisecomOspfAsLsdbLsId_Type())
raisecomOspfAsLsdbLsId.setMaxAccess(_x)
if mibBuilder.loadTexts:raisecomOspfAsLsdbLsId.setStatus(_A)
_RaisecomOspfAsLsdbRouterId_Type=RouterID
_RaisecomOspfAsLsdbRouterId_Object=MibTableColumn
raisecomOspfAsLsdbRouterId=_RaisecomOspfAsLsdbRouterId_Object((1,3,6,1,4,1,8886,1,47,2,14,1,3),_RaisecomOspfAsLsdbRouterId_Type())
raisecomOspfAsLsdbRouterId.setMaxAccess(_x)
if mibBuilder.loadTexts:raisecomOspfAsLsdbRouterId.setStatus(_A)
_RaisecomOspfAsLsdbSequence_Type=Integer32
_RaisecomOspfAsLsdbSequence_Object=MibTableColumn
raisecomOspfAsLsdbSequence=_RaisecomOspfAsLsdbSequence_Object((1,3,6,1,4,1,8886,1,47,2,14,1,4),_RaisecomOspfAsLsdbSequence_Type())
raisecomOspfAsLsdbSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAsLsdbSequence.setStatus(_A)
_RaisecomOspfAsLsdbAge_Type=Integer32
_RaisecomOspfAsLsdbAge_Object=MibTableColumn
raisecomOspfAsLsdbAge=_RaisecomOspfAsLsdbAge_Object((1,3,6,1,4,1,8886,1,47,2,14,1,5),_RaisecomOspfAsLsdbAge_Type())
raisecomOspfAsLsdbAge.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAsLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:raisecomOspfAsLsdbAge.setUnits(_I)
_RaisecomOspfAsLsdbChecksum_Type=Integer32
_RaisecomOspfAsLsdbChecksum_Object=MibTableColumn
raisecomOspfAsLsdbChecksum=_RaisecomOspfAsLsdbChecksum_Object((1,3,6,1,4,1,8886,1,47,2,14,1,6),_RaisecomOspfAsLsdbChecksum_Type())
raisecomOspfAsLsdbChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAsLsdbChecksum.setStatus(_A)
class _RaisecomOspfAsLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_RaisecomOspfAsLsdbAdvertisement_Type.__name__=_H
_RaisecomOspfAsLsdbAdvertisement_Object=MibTableColumn
raisecomOspfAsLsdbAdvertisement=_RaisecomOspfAsLsdbAdvertisement_Object((1,3,6,1,4,1,8886,1,47,2,14,1,7),_RaisecomOspfAsLsdbAdvertisement_Type())
raisecomOspfAsLsdbAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAsLsdbAdvertisement.setStatus(_A)
_RaisecomOspfAreaLsaCountTable_Object=MibTable
raisecomOspfAreaLsaCountTable=_RaisecomOspfAreaLsaCountTable_Object((1,3,6,1,4,1,8886,1,47,2,15))
if mibBuilder.loadTexts:raisecomOspfAreaLsaCountTable.setStatus(_A)
_RaisecomOspfAreaLsaCountEntry_Object=MibTableRow
raisecomOspfAreaLsaCountEntry=_RaisecomOspfAreaLsaCountEntry_Object((1,3,6,1,4,1,8886,1,47,2,15,1))
raisecomOspfAreaLsaCountEntry.setIndexNames((0,_B,_F),(0,_B,_AM),(0,_B,_AN))
if mibBuilder.loadTexts:raisecomOspfAreaLsaCountEntry.setStatus(_A)
_RaisecomOspfAreaLsaCountAreaId_Type=AreaID
_RaisecomOspfAreaLsaCountAreaId_Object=MibTableColumn
raisecomOspfAreaLsaCountAreaId=_RaisecomOspfAreaLsaCountAreaId_Object((1,3,6,1,4,1,8886,1,47,2,15,1,1),_RaisecomOspfAreaLsaCountAreaId_Type())
raisecomOspfAreaLsaCountAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaLsaCountAreaId.setStatus(_A)
class _RaisecomOspfAreaLsaCountLsaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6,7,10)));namedValues=NamedValues(*((_g,1),(_h,2),(_W,3),(_i,4),(_k,6),(_X,7),(_l,10)))
_RaisecomOspfAreaLsaCountLsaType_Type.__name__=_E
_RaisecomOspfAreaLsaCountLsaType_Object=MibTableColumn
raisecomOspfAreaLsaCountLsaType=_RaisecomOspfAreaLsaCountLsaType_Object((1,3,6,1,4,1,8886,1,47,2,15,1,2),_RaisecomOspfAreaLsaCountLsaType_Type())
raisecomOspfAreaLsaCountLsaType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaLsaCountLsaType.setStatus(_A)
_RaisecomOspfAreaLsaCountNumber_Type=Gauge32
_RaisecomOspfAreaLsaCountNumber_Object=MibTableColumn
raisecomOspfAreaLsaCountNumber=_RaisecomOspfAreaLsaCountNumber_Object((1,3,6,1,4,1,8886,1,47,2,15,1,3),_RaisecomOspfAreaLsaCountNumber_Type())
raisecomOspfAreaLsaCountNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfAreaLsaCountNumber.setStatus(_A)
_RaisecomOspfRedistributeTable_Object=MibTable
raisecomOspfRedistributeTable=_RaisecomOspfRedistributeTable_Object((1,3,6,1,4,1,8886,1,47,2,16))
if mibBuilder.loadTexts:raisecomOspfRedistributeTable.setStatus(_A)
_RaisecomOspfRedistributeEntry_Object=MibTableRow
raisecomOspfRedistributeEntry=_RaisecomOspfRedistributeEntry_Object((1,3,6,1,4,1,8886,1,47,2,16,1))
raisecomOspfRedistributeEntry.setIndexNames((0,_B,_F),(0,_B,_m),(0,_B,_n))
if mibBuilder.loadTexts:raisecomOspfRedistributeEntry.setStatus(_A)
class _RaisecomOspfRedistributeProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,8,13)));namedValues=NamedValues(*(('local',2),('netmgmt',3),('rip',8),('ospf',13)))
_RaisecomOspfRedistributeProtocol_Type.__name__=_E
_RaisecomOspfRedistributeProtocol_Object=MibTableColumn
raisecomOspfRedistributeProtocol=_RaisecomOspfRedistributeProtocol_Object((1,3,6,1,4,1,8886,1,47,2,16,1,1),_RaisecomOspfRedistributeProtocol_Type())
raisecomOspfRedistributeProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfRedistributeProtocol.setStatus(_A)
_RaisecomOspfRedistributeProcessId_Type=ProcessID
_RaisecomOspfRedistributeProcessId_Object=MibTableColumn
raisecomOspfRedistributeProcessId=_RaisecomOspfRedistributeProcessId_Object((1,3,6,1,4,1,8886,1,47,2,16,1,2),_RaisecomOspfRedistributeProcessId_Type())
raisecomOspfRedistributeProcessId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfRedistributeProcessId.setStatus(_A)
class _RaisecomOspfRedistributeCost_Type(BigMetric):defaultValue=1
_RaisecomOspfRedistributeCost_Type.__name__=_U
_RaisecomOspfRedistributeCost_Object=MibTableColumn
raisecomOspfRedistributeCost=_RaisecomOspfRedistributeCost_Object((1,3,6,1,4,1,8886,1,47,2,16,1,3),_RaisecomOspfRedistributeCost_Type())
raisecomOspfRedistributeCost.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfRedistributeCost.setStatus(_A)
class _RaisecomOspfRedistributeType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('e1',1),('e2',2)))
_RaisecomOspfRedistributeType_Type.__name__=_E
_RaisecomOspfRedistributeType_Object=MibTableColumn
raisecomOspfRedistributeType=_RaisecomOspfRedistributeType_Object((1,3,6,1,4,1,8886,1,47,2,16,1,4),_RaisecomOspfRedistributeType_Type())
raisecomOspfRedistributeType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfRedistributeType.setStatus(_A)
_RaisecomOspfRedistributeStatus_Type=RowStatus
_RaisecomOspfRedistributeStatus_Object=MibTableColumn
raisecomOspfRedistributeStatus=_RaisecomOspfRedistributeStatus_Object((1,3,6,1,4,1,8886,1,47,2,16,1,5),_RaisecomOspfRedistributeStatus_Type())
raisecomOspfRedistributeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfRedistributeStatus.setStatus(_A)
class _RaisecomOspfRedistributeRouteMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_RaisecomOspfRedistributeRouteMapName_Type.__name__=_H
_RaisecomOspfRedistributeRouteMapName_Object=MibTableColumn
raisecomOspfRedistributeRouteMapName=_RaisecomOspfRedistributeRouteMapName_Object((1,3,6,1,4,1,8886,1,47,2,16,1,6),_RaisecomOspfRedistributeRouteMapName_Type())
raisecomOspfRedistributeRouteMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfRedistributeRouteMapName.setStatus(_A)
class _RaisecomOspfRedistributeTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RaisecomOspfRedistributeTag_Type.__name__=_E
_RaisecomOspfRedistributeTag_Object=MibTableColumn
raisecomOspfRedistributeTag=_RaisecomOspfRedistributeTag_Object((1,3,6,1,4,1,8886,1,47,2,16,1,7),_RaisecomOspfRedistributeTag_Type())
raisecomOspfRedistributeTag.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfRedistributeTag.setStatus(_A)
_RaisecomOspfDefaultInfoTable_Object=MibTable
raisecomOspfDefaultInfoTable=_RaisecomOspfDefaultInfoTable_Object((1,3,6,1,4,1,8886,1,47,2,17))
if mibBuilder.loadTexts:raisecomOspfDefaultInfoTable.setStatus(_A)
_RaisecomOspfDefaultInfoEntry_Object=MibTableRow
raisecomOspfDefaultInfoEntry=_RaisecomOspfDefaultInfoEntry_Object((1,3,6,1,4,1,8886,1,47,2,17,1))
raisecomOspfDefaultInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:raisecomOspfDefaultInfoEntry.setStatus(_A)
class _RaisecomOspfDefaultInfoAlways_Type(TruthValue):defaultValue=2
_RaisecomOspfDefaultInfoAlways_Type.__name__=_q
_RaisecomOspfDefaultInfoAlways_Object=MibTableColumn
raisecomOspfDefaultInfoAlways=_RaisecomOspfDefaultInfoAlways_Object((1,3,6,1,4,1,8886,1,47,2,17,1,1),_RaisecomOspfDefaultInfoAlways_Type())
raisecomOspfDefaultInfoAlways.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfDefaultInfoAlways.setStatus(_A)
class _RaisecomOspfDefaultInfoCost_Type(BigMetric):defaultValue=1
_RaisecomOspfDefaultInfoCost_Type.__name__=_U
_RaisecomOspfDefaultInfoCost_Object=MibTableColumn
raisecomOspfDefaultInfoCost=_RaisecomOspfDefaultInfoCost_Object((1,3,6,1,4,1,8886,1,47,2,17,1,2),_RaisecomOspfDefaultInfoCost_Type())
raisecomOspfDefaultInfoCost.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfDefaultInfoCost.setStatus(_A)
class _RaisecomOspfDefaultInfoType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('e1',1),('e2',2)))
_RaisecomOspfDefaultInfoType_Type.__name__=_E
_RaisecomOspfDefaultInfoType_Object=MibTableColumn
raisecomOspfDefaultInfoType=_RaisecomOspfDefaultInfoType_Object((1,3,6,1,4,1,8886,1,47,2,17,1,3),_RaisecomOspfDefaultInfoType_Type())
raisecomOspfDefaultInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfDefaultInfoType.setStatus(_A)
_RaisecomOspfDefaultInfoStatus_Type=RowStatus
_RaisecomOspfDefaultInfoStatus_Object=MibTableColumn
raisecomOspfDefaultInfoStatus=_RaisecomOspfDefaultInfoStatus_Object((1,3,6,1,4,1,8886,1,47,2,17,1,4),_RaisecomOspfDefaultInfoStatus_Type())
raisecomOspfDefaultInfoStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfDefaultInfoStatus.setStatus(_A)
_RaisecomOspfPacketIoStatisTable_Object=MibTable
raisecomOspfPacketIoStatisTable=_RaisecomOspfPacketIoStatisTable_Object((1,3,6,1,4,1,8886,1,47,2,18))
if mibBuilder.loadTexts:raisecomOspfPacketIoStatisTable.setStatus(_A)
_RaisecomOspfPacketIoStatisEntry_Object=MibTableRow
raisecomOspfPacketIoStatisEntry=_RaisecomOspfPacketIoStatisEntry_Object((1,3,6,1,4,1,8886,1,47,2,18,1))
raisecomOspfPacketIoStatisEntry.setIndexNames((0,_B,_F),(0,_B,_AO),(0,_B,_AP))
if mibBuilder.loadTexts:raisecomOspfPacketIoStatisEntry.setStatus(_A)
class _RaisecomOspfPacketIoStatisIoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('input',1),('output',2)))
_RaisecomOspfPacketIoStatisIoType_Type.__name__=_E
_RaisecomOspfPacketIoStatisIoType_Object=MibTableColumn
raisecomOspfPacketIoStatisIoType=_RaisecomOspfPacketIoStatisIoType_Object((1,3,6,1,4,1,8886,1,47,2,18,1,1),_RaisecomOspfPacketIoStatisIoType_Type())
raisecomOspfPacketIoStatisIoType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfPacketIoStatisIoType.setStatus(_A)
class _RaisecomOspfPacketIoStatisPktType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('hello',1),(_A4,2),('lsReq',3),('lsUpdate',4),('lsAck',5)))
_RaisecomOspfPacketIoStatisPktType_Type.__name__=_E
_RaisecomOspfPacketIoStatisPktType_Object=MibTableColumn
raisecomOspfPacketIoStatisPktType=_RaisecomOspfPacketIoStatisPktType_Object((1,3,6,1,4,1,8886,1,47,2,18,1,2),_RaisecomOspfPacketIoStatisPktType_Type())
raisecomOspfPacketIoStatisPktType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfPacketIoStatisPktType.setStatus(_A)
_RaisecomOspfPacketIoStatisNumber_Type=Integer32
_RaisecomOspfPacketIoStatisNumber_Object=MibTableColumn
raisecomOspfPacketIoStatisNumber=_RaisecomOspfPacketIoStatisNumber_Object((1,3,6,1,4,1,8886,1,47,2,18,1,3),_RaisecomOspfPacketIoStatisNumber_Type())
raisecomOspfPacketIoStatisNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfPacketIoStatisNumber.setStatus(_A)
_RaisecomOspfRouteTable_Object=MibTable
raisecomOspfRouteTable=_RaisecomOspfRouteTable_Object((1,3,6,1,4,1,8886,1,47,2,19))
if mibBuilder.loadTexts:raisecomOspfRouteTable.setStatus(_A)
_RaisecomOspfRouteEntry_Object=MibTableRow
raisecomOspfRouteEntry=_RaisecomOspfRouteEntry_Object((1,3,6,1,4,1,8886,1,47,2,19,1))
raisecomOspfRouteEntry.setIndexNames((0,_B,_F),(0,_B,_AQ),(0,_B,_AR),(0,_B,_AS))
if mibBuilder.loadTexts:raisecomOspfRouteEntry.setStatus(_A)
_RaisecomOspfRouteDest_Type=IpAddress
_RaisecomOspfRouteDest_Object=MibTableColumn
raisecomOspfRouteDest=_RaisecomOspfRouteDest_Object((1,3,6,1,4,1,8886,1,47,2,19,1,1),_RaisecomOspfRouteDest_Type())
raisecomOspfRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfRouteDest.setStatus(_A)
_RaisecomOspfRouteMask_Type=IpAddress
_RaisecomOspfRouteMask_Object=MibTableColumn
raisecomOspfRouteMask=_RaisecomOspfRouteMask_Object((1,3,6,1,4,1,8886,1,47,2,19,1,2),_RaisecomOspfRouteMask_Type())
raisecomOspfRouteMask.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfRouteMask.setStatus(_A)
class _RaisecomOspfRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('network',1),('ase',2),('nssa',3)))
_RaisecomOspfRouteType_Type.__name__=_E
_RaisecomOspfRouteType_Object=MibTableColumn
raisecomOspfRouteType=_RaisecomOspfRouteType_Object((1,3,6,1,4,1,8886,1,47,2,19,1,3),_RaisecomOspfRouteType_Type())
raisecomOspfRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfRouteType.setStatus(_A)
class _RaisecomOspfRouteLsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,10)));namedValues=NamedValues(*(('stub',0),(_g,1),(_h,2),(_W,3),(_i,4),(_j,5),(_k,6),(_X,7),(_l,10)))
_RaisecomOspfRouteLsType_Type.__name__=_E
_RaisecomOspfRouteLsType_Object=MibTableColumn
raisecomOspfRouteLsType=_RaisecomOspfRouteLsType_Object((1,3,6,1,4,1,8886,1,47,2,19,1,4),_RaisecomOspfRouteLsType_Type())
raisecomOspfRouteLsType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfRouteLsType.setStatus(_A)
_RaisecomOspfRouteMetric_Type=Integer32
_RaisecomOspfRouteMetric_Object=MibTableColumn
raisecomOspfRouteMetric=_RaisecomOspfRouteMetric_Object((1,3,6,1,4,1,8886,1,47,2,19,1,5),_RaisecomOspfRouteMetric_Type())
raisecomOspfRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfRouteMetric.setStatus(_A)
_RaisecomOspfRouteNextHop_Type=IpAddress
_RaisecomOspfRouteNextHop_Object=MibTableColumn
raisecomOspfRouteNextHop=_RaisecomOspfRouteNextHop_Object((1,3,6,1,4,1,8886,1,47,2,19,1,6),_RaisecomOspfRouteNextHop_Type())
raisecomOspfRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfRouteNextHop.setStatus(_A)
_RaisecomOspfRouteAdvRtr_Type=IpAddress
_RaisecomOspfRouteAdvRtr_Object=MibTableColumn
raisecomOspfRouteAdvRtr=_RaisecomOspfRouteAdvRtr_Object((1,3,6,1,4,1,8886,1,47,2,19,1,7),_RaisecomOspfRouteAdvRtr_Type())
raisecomOspfRouteAdvRtr.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfRouteAdvRtr.setStatus(_A)
_RaisecomOspfRouteArea_Type=Integer32
_RaisecomOspfRouteArea_Object=MibTableColumn
raisecomOspfRouteArea=_RaisecomOspfRouteArea_Object((1,3,6,1,4,1,8886,1,47,2,19,1,8),_RaisecomOspfRouteArea_Type())
raisecomOspfRouteArea.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfRouteArea.setStatus(_A)
_RaisecomOspfBdrRouteTable_Object=MibTable
raisecomOspfBdrRouteTable=_RaisecomOspfBdrRouteTable_Object((1,3,6,1,4,1,8886,1,47,2,20))
if mibBuilder.loadTexts:raisecomOspfBdrRouteTable.setStatus(_A)
_RaisecomOspfBdrRouteEntry_Object=MibTableRow
raisecomOspfBdrRouteEntry=_RaisecomOspfBdrRouteEntry_Object((1,3,6,1,4,1,8886,1,47,2,20,1))
raisecomOspfBdrRouteEntry.setIndexNames((0,_B,_F),(0,_B,_AT),(0,_B,_AU),(0,_B,_AV),(0,_B,_AW))
if mibBuilder.loadTexts:raisecomOspfBdrRouteEntry.setStatus(_A)
class _RaisecomOspfBdrRouteRtrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('asbr',1),('abr',2),('sumasbr',3)))
_RaisecomOspfBdrRouteRtrType_Type.__name__=_E
_RaisecomOspfBdrRouteRtrType_Object=MibTableColumn
raisecomOspfBdrRouteRtrType=_RaisecomOspfBdrRouteRtrType_Object((1,3,6,1,4,1,8886,1,47,2,20,1,1),_RaisecomOspfBdrRouteRtrType_Type())
raisecomOspfBdrRouteRtrType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfBdrRouteRtrType.setStatus(_A)
_RaisecomOspfBdrRouteArea_Type=IpAddress
_RaisecomOspfBdrRouteArea_Object=MibTableColumn
raisecomOspfBdrRouteArea=_RaisecomOspfBdrRouteArea_Object((1,3,6,1,4,1,8886,1,47,2,20,1,2),_RaisecomOspfBdrRouteArea_Type())
raisecomOspfBdrRouteArea.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfBdrRouteArea.setStatus(_A)
_RaisecomOspfBdrRouteDest_Type=IpAddress
_RaisecomOspfBdrRouteDest_Object=MibTableColumn
raisecomOspfBdrRouteDest=_RaisecomOspfBdrRouteDest_Object((1,3,6,1,4,1,8886,1,47,2,20,1,3),_RaisecomOspfBdrRouteDest_Type())
raisecomOspfBdrRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfBdrRouteDest.setStatus(_A)
_RaisecomOspfBdrRouteNextHop_Type=IpAddress
_RaisecomOspfBdrRouteNextHop_Object=MibTableColumn
raisecomOspfBdrRouteNextHop=_RaisecomOspfBdrRouteNextHop_Object((1,3,6,1,4,1,8886,1,47,2,20,1,4),_RaisecomOspfBdrRouteNextHop_Type())
raisecomOspfBdrRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfBdrRouteNextHop.setStatus(_A)
class _RaisecomOspfBdrRouteLsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,10)));namedValues=NamedValues(*((_g,1),(_h,2),(_W,3),(_i,4),(_j,5),(_k,6),(_X,7),(_l,10)))
_RaisecomOspfBdrRouteLsType_Type.__name__=_E
_RaisecomOspfBdrRouteLsType_Object=MibTableColumn
raisecomOspfBdrRouteLsType=_RaisecomOspfBdrRouteLsType_Object((1,3,6,1,4,1,8886,1,47,2,20,1,5),_RaisecomOspfBdrRouteLsType_Type())
raisecomOspfBdrRouteLsType.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfBdrRouteLsType.setStatus(_A)
_RaisecomOspfBdrRouteMetric_Type=Integer32
_RaisecomOspfBdrRouteMetric_Object=MibTableColumn
raisecomOspfBdrRouteMetric=_RaisecomOspfBdrRouteMetric_Object((1,3,6,1,4,1,8886,1,47,2,20,1,6),_RaisecomOspfBdrRouteMetric_Type())
raisecomOspfBdrRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfBdrRouteMetric.setStatus(_A)
_RaisecomOspfDistributeListGroup_ObjectIdentity=ObjectIdentity
raisecomOspfDistributeListGroup=_RaisecomOspfDistributeListGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,47,2,21))
_RaisecomOspfDistributeListInTable_Object=MibTable
raisecomOspfDistributeListInTable=_RaisecomOspfDistributeListInTable_Object((1,3,6,1,4,1,8886,1,47,2,21,1))
if mibBuilder.loadTexts:raisecomOspfDistributeListInTable.setStatus(_A)
_RaisecomOspfDistributeListInEntry_Object=MibTableRow
raisecomOspfDistributeListInEntry=_RaisecomOspfDistributeListInEntry_Object((1,3,6,1,4,1,8886,1,47,2,21,1,1))
raisecomOspfDistributeListInEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:raisecomOspfDistributeListInEntry.setStatus(_A)
class _RaisecomOspfDistrInIpPrefixListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_RaisecomOspfDistrInIpPrefixListName_Type.__name__=_H
_RaisecomOspfDistrInIpPrefixListName_Object=MibTableColumn
raisecomOspfDistrInIpPrefixListName=_RaisecomOspfDistrInIpPrefixListName_Object((1,3,6,1,4,1,8886,1,47,2,21,1,1,1),_RaisecomOspfDistrInIpPrefixListName_Type())
raisecomOspfDistrInIpPrefixListName.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfDistrInIpPrefixListName.setStatus(_A)
_RaisecomOspfDistrInAclNum_Type=Integer32
_RaisecomOspfDistrInAclNum_Object=MibTableColumn
raisecomOspfDistrInAclNum=_RaisecomOspfDistrInAclNum_Object((1,3,6,1,4,1,8886,1,47,2,21,1,1,2),_RaisecomOspfDistrInAclNum_Type())
raisecomOspfDistrInAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfDistrInAclNum.setStatus(_A)
_RaisecomOspfDistrInRowStatus_Type=RowStatus
_RaisecomOspfDistrInRowStatus_Object=MibTableColumn
raisecomOspfDistrInRowStatus=_RaisecomOspfDistrInRowStatus_Object((1,3,6,1,4,1,8886,1,47,2,21,1,1,3),_RaisecomOspfDistrInRowStatus_Type())
raisecomOspfDistrInRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfDistrInRowStatus.setStatus(_A)
_RaisecomOspfDistributeListOutTable_Object=MibTable
raisecomOspfDistributeListOutTable=_RaisecomOspfDistributeListOutTable_Object((1,3,6,1,4,1,8886,1,47,2,21,2))
if mibBuilder.loadTexts:raisecomOspfDistributeListOutTable.setStatus(_A)
_RaisecomOspfDistributeListOutEntry_Object=MibTableRow
raisecomOspfDistributeListOutEntry=_RaisecomOspfDistributeListOutEntry_Object((1,3,6,1,4,1,8886,1,47,2,21,2,1))
raisecomOspfDistributeListOutEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:raisecomOspfDistributeListOutEntry.setStatus(_A)
class _RaisecomOspfDistrOutIpPrefixListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_RaisecomOspfDistrOutIpPrefixListName_Type.__name__=_H
_RaisecomOspfDistrOutIpPrefixListName_Object=MibTableColumn
raisecomOspfDistrOutIpPrefixListName=_RaisecomOspfDistrOutIpPrefixListName_Object((1,3,6,1,4,1,8886,1,47,2,21,2,1,1),_RaisecomOspfDistrOutIpPrefixListName_Type())
raisecomOspfDistrOutIpPrefixListName.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfDistrOutIpPrefixListName.setStatus(_A)
_RaisecomOspfDistrOutAclNum_Type=Integer32
_RaisecomOspfDistrOutAclNum_Object=MibTableColumn
raisecomOspfDistrOutAclNum=_RaisecomOspfDistrOutAclNum_Object((1,3,6,1,4,1,8886,1,47,2,21,2,1,2),_RaisecomOspfDistrOutAclNum_Type())
raisecomOspfDistrOutAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfDistrOutAclNum.setStatus(_A)
_RaisecomOspfDistrOutRowStatus_Type=RowStatus
_RaisecomOspfDistrOutRowStatus_Object=MibTableColumn
raisecomOspfDistrOutRowStatus=_RaisecomOspfDistrOutRowStatus_Object((1,3,6,1,4,1,8886,1,47,2,21,2,1,3),_RaisecomOspfDistrOutRowStatus_Type())
raisecomOspfDistrOutRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfDistrOutRowStatus.setStatus(_A)
_RaisecomOspfDistributeListOutProtocolTable_Object=MibTable
raisecomOspfDistributeListOutProtocolTable=_RaisecomOspfDistributeListOutProtocolTable_Object((1,3,6,1,4,1,8886,1,47,2,21,3))
if mibBuilder.loadTexts:raisecomOspfDistributeListOutProtocolTable.setStatus(_A)
_RaisecomOspfDistributeListOutProtocolEntry_Object=MibTableRow
raisecomOspfDistributeListOutProtocolEntry=_RaisecomOspfDistributeListOutProtocolEntry_Object((1,3,6,1,4,1,8886,1,47,2,21,3,1))
raisecomOspfDistributeListOutProtocolEntry.setIndexNames((0,_B,_F),(0,_B,_AX),(0,_B,_AY))
if mibBuilder.loadTexts:raisecomOspfDistributeListOutProtocolEntry.setStatus(_A)
class _RaisecomOspfDistrOutProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,8,13)));namedValues=NamedValues(*(('local',2),('netmgmt',3),('rip',8),('ospf',13)))
_RaisecomOspfDistrOutProtocol_Type.__name__=_E
_RaisecomOspfDistrOutProtocol_Object=MibTableColumn
raisecomOspfDistrOutProtocol=_RaisecomOspfDistrOutProtocol_Object((1,3,6,1,4,1,8886,1,47,2,21,3,1,1),_RaisecomOspfDistrOutProtocol_Type())
raisecomOspfDistrOutProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfDistrOutProtocol.setStatus(_A)
_RaisecomOspfDistrOutProcessId_Type=ProcessID
_RaisecomOspfDistrOutProcessId_Object=MibTableColumn
raisecomOspfDistrOutProcessId=_RaisecomOspfDistrOutProcessId_Object((1,3,6,1,4,1,8886,1,47,2,21,3,1,2),_RaisecomOspfDistrOutProcessId_Type())
raisecomOspfDistrOutProcessId.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomOspfDistrOutProcessId.setStatus(_A)
class _RaisecomOspfDistrOutProIpPrefixListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_RaisecomOspfDistrOutProIpPrefixListName_Type.__name__=_H
_RaisecomOspfDistrOutProIpPrefixListName_Object=MibTableColumn
raisecomOspfDistrOutProIpPrefixListName=_RaisecomOspfDistrOutProIpPrefixListName_Object((1,3,6,1,4,1,8886,1,47,2,21,3,1,3),_RaisecomOspfDistrOutProIpPrefixListName_Type())
raisecomOspfDistrOutProIpPrefixListName.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfDistrOutProIpPrefixListName.setStatus(_A)
_RaisecomOspfDistrOutProAclNum_Type=Integer32
_RaisecomOspfDistrOutProAclNum_Object=MibTableColumn
raisecomOspfDistrOutProAclNum=_RaisecomOspfDistrOutProAclNum_Object((1,3,6,1,4,1,8886,1,47,2,21,3,1,4),_RaisecomOspfDistrOutProAclNum_Type())
raisecomOspfDistrOutProAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfDistrOutProAclNum.setStatus(_A)
_RaisecomOspfDistrOutProRowStatus_Type=RowStatus
_RaisecomOspfDistrOutProRowStatus_Object=MibTableColumn
raisecomOspfDistrOutProRowStatus=_RaisecomOspfDistrOutProRowStatus_Object((1,3,6,1,4,1,8886,1,47,2,21,3,1,5),_RaisecomOspfDistrOutProRowStatus_Type())
raisecomOspfDistrOutProRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomOspfDistrOutProRowStatus.setStatus(_A)
_RaisecomOspfConformance_ObjectIdentity=ObjectIdentity
raisecomOspfConformance=_RaisecomOspfConformance_ObjectIdentity((1,3,6,1,4,1,8886,1,47,3))
raisecomOspfIfStateChange=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,1))
raisecomOspfIfStateChange.setObjects(*((_B,_F),(_B,_G),(_B,_N),(_B,_J),(_B,_AZ)))
if mibBuilder.loadTexts:raisecomOspfIfStateChange.setStatus(_A)
raisecomOspfVirtIfStateChange=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,2))
raisecomOspfVirtIfStateChange.setObjects(*((_B,_F),(_B,_G),(_B,_K),(_B,_L),(_B,_Aa)))
if mibBuilder.loadTexts:raisecomOspfVirtIfStateChange.setStatus(_A)
raisecomOspfNbrStateChange=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,3))
raisecomOspfNbrStateChange.setObjects(*((_B,_F),(_B,_G),(_B,_u),(_B,_Ab),(_B,_y),(_B,_Ac)))
if mibBuilder.loadTexts:raisecomOspfNbrStateChange.setStatus(_A)
raisecomOspfVirtNbrStateChange=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,4))
raisecomOspfVirtNbrStateChange.setObjects(*((_B,_F),(_B,_G),(_B,_v),(_B,_w),(_B,_Ad)))
if mibBuilder.loadTexts:raisecomOspfVirtNbrStateChange.setStatus(_A)
raisecomOspfIfConfigError=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,5))
raisecomOspfIfConfigError.setObjects(*((_B,_F),(_B,_G),(_B,_N),(_B,_J),(_B,_o),(_B,_Y),(_B,_M)))
if mibBuilder.loadTexts:raisecomOspfIfConfigError.setStatus(_A)
raisecomOspfVirtIfConfigError=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,6))
raisecomOspfVirtIfConfigError.setObjects(*((_B,_F),(_B,_G),(_B,_K),(_B,_L),(_B,_Y),(_B,_M)))
if mibBuilder.loadTexts:raisecomOspfVirtIfConfigError.setStatus(_A)
raisecomOspfIfAuthFailure=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,7))
raisecomOspfIfAuthFailure.setObjects(*((_B,_F),(_B,_G),(_B,_N),(_B,_J),(_B,_o),(_B,_Y),(_B,_M)))
if mibBuilder.loadTexts:raisecomOspfIfAuthFailure.setStatus(_A)
raisecomOspfVirtIfAuthFailure=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,8))
raisecomOspfVirtIfAuthFailure.setObjects(*((_B,_F),(_B,_G),(_B,_K),(_B,_L),(_B,_Y),(_B,_M)))
if mibBuilder.loadTexts:raisecomOspfVirtIfAuthFailure.setStatus(_A)
raisecomOspfIfRxBadPacket=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,9))
raisecomOspfIfRxBadPacket.setObjects(*((_B,_F),(_B,_G),(_B,_N),(_B,_J),(_B,_o),(_B,_M)))
if mibBuilder.loadTexts:raisecomOspfIfRxBadPacket.setStatus(_A)
raisecomOspfVirtIfRxBadPacket=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,10))
raisecomOspfVirtIfRxBadPacket.setObjects(*((_B,_F),(_B,_G),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:raisecomOspfVirtIfRxBadPacket.setStatus(_A)
raisecomOspfTxRetransmit=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,11))
raisecomOspfTxRetransmit.setObjects(*((_B,_F),(_B,_G),(_B,_N),(_B,_J),(_B,_y),(_B,_M),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:raisecomOspfTxRetransmit.setStatus(_A)
raisecomOspfVirtIfTxRetransmit=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,12))
raisecomOspfVirtIfTxRetransmit.setObjects(*((_B,_F),(_B,_G),(_B,_K),(_B,_L),(_B,_M),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:raisecomOspfVirtIfTxRetransmit.setStatus(_A)
raisecomOspfOriginateLsa=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,13))
raisecomOspfOriginateLsa.setObjects(*((_B,_F),(_B,_G),(_B,_f),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:raisecomOspfOriginateLsa.setStatus(_A)
raisecomOspfMaxAgeLsa=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,14))
raisecomOspfMaxAgeLsa.setObjects(*((_B,_F),(_B,_G),(_B,_f),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:raisecomOspfMaxAgeLsa.setStatus(_A)
raisecomOspfLsdbOverflow=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,15))
raisecomOspfLsdbOverflow.setObjects(*((_B,_F),(_B,_G),(_B,_z)))
if mibBuilder.loadTexts:raisecomOspfLsdbOverflow.setStatus(_A)
raisecomOspfLsdbApproachingOverflow=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,16))
raisecomOspfLsdbApproachingOverflow.setObjects(*((_B,_F),(_B,_G),(_B,_z)))
if mibBuilder.loadTexts:raisecomOspfLsdbApproachingOverflow.setStatus(_A)
raisecomOspfIfKeyValid=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,17))
raisecomOspfIfKeyValid.setObjects(*((_B,_F),(_B,_G),(_B,_N),(_B,_J),(_B,_A0)))
if mibBuilder.loadTexts:raisecomOspfIfKeyValid.setStatus(_A)
raisecomOspfIfLastKeyExpiration=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,18))
raisecomOspfIfLastKeyExpiration.setObjects(*((_B,_F),(_B,_G),(_B,_N),(_B,_J),(_B,_A0)))
if mibBuilder.loadTexts:raisecomOspfIfLastKeyExpiration.setStatus(_A)
raisecomOspfVirtIfKeyValid=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,19))
raisecomOspfVirtIfKeyValid.setObjects(*((_B,_F),(_B,_G),(_B,_K),(_B,_L),(_B,_A1)))
if mibBuilder.loadTexts:raisecomOspfVirtIfKeyValid.setStatus(_A)
raisecomOspfVirtIfLastKeyExpiration=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,20))
raisecomOspfVirtIfLastKeyExpiration.setObjects(*((_B,_F),(_B,_G),(_B,_K),(_B,_L),(_B,_A1)))
if mibBuilder.loadTexts:raisecomOspfVirtIfLastKeyExpiration.setStatus(_A)
raisecomOspfRedistributeOverflow=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,21))
raisecomOspfRedistributeOverflow.setObjects(*((_B,_F),(_B,_m),(_B,_n),(_B,_A2)))
if mibBuilder.loadTexts:raisecomOspfRedistributeOverflow.setStatus(_A)
raisecomOspfRedistributeNotOverflow=NotificationType((1,3,6,1,4,1,8886,1,47,1,2,22))
raisecomOspfRedistributeNotOverflow.setObjects(*((_B,_F),(_B,_m),(_B,_n),(_B,_A2)))
if mibBuilder.loadTexts:raisecomOspfRedistributeNotOverflow.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ProcessID':ProcessID,'AreaID':AreaID,'RouterID':RouterID,'Metric':Metric,_U:BigMetric,'Status':Status,_P:PositiveInteger,_t:HelloRange,_V:UpToMaxAge,_b:DesignatedRouterPriority,_Z:OspfAuthenticationType,'raisecomOspf':raisecomOspf,'raisecomOspfNotifications':raisecomOspfNotifications,'raisecomOspfTrapControlTable':raisecomOspfTrapControlTable,'raisecomOspfTrapControlEntry':raisecomOspfTrapControlEntry,'raisecomOspfSetTrap':raisecomOspfSetTrap,_Y:raisecomOspfConfigErrorType,_M:raisecomOspfPacketType,_o:raisecomOspfPacketSrc,'raisecomOspfTraps':raisecomOspfTraps,'raisecomOspfIfStateChange':raisecomOspfIfStateChange,'raisecomOspfVirtIfStateChange':raisecomOspfVirtIfStateChange,'raisecomOspfNbrStateChange':raisecomOspfNbrStateChange,'raisecomOspfVirtNbrStateChange':raisecomOspfVirtNbrStateChange,'raisecomOspfIfConfigError':raisecomOspfIfConfigError,'raisecomOspfVirtIfConfigError':raisecomOspfVirtIfConfigError,'raisecomOspfIfAuthFailure':raisecomOspfIfAuthFailure,'raisecomOspfVirtIfAuthFailure':raisecomOspfVirtIfAuthFailure,'raisecomOspfIfRxBadPacket':raisecomOspfIfRxBadPacket,'raisecomOspfVirtIfRxBadPacket':raisecomOspfVirtIfRxBadPacket,'raisecomOspfTxRetransmit':raisecomOspfTxRetransmit,'raisecomOspfVirtIfTxRetransmit':raisecomOspfVirtIfTxRetransmit,'raisecomOspfOriginateLsa':raisecomOspfOriginateLsa,'raisecomOspfMaxAgeLsa':raisecomOspfMaxAgeLsa,'raisecomOspfLsdbOverflow':raisecomOspfLsdbOverflow,'raisecomOspfLsdbApproachingOverflow':raisecomOspfLsdbApproachingOverflow,'raisecomOspfIfKeyValid':raisecomOspfIfKeyValid,'raisecomOspfIfLastKeyExpiration':raisecomOspfIfLastKeyExpiration,'raisecomOspfVirtIfKeyValid':raisecomOspfVirtIfKeyValid,'raisecomOspfVirtIfLastKeyExpiration':raisecomOspfVirtIfLastKeyExpiration,'raisecomOspfRedistributeOverflow':raisecomOspfRedistributeOverflow,'raisecomOspfRedistributeNotOverflow':raisecomOspfRedistributeNotOverflow,'raisecomOspfObjects':raisecomOspfObjects,'raisecomOspfGlobalTable':raisecomOspfGlobalTable,'raisecomOspfGlobalEntry':raisecomOspfGlobalEntry,_F:raisecomOspfProcessId,_G:raisecomOspfRouterId,'raisecomOspfAdminStat':raisecomOspfAdminStat,'raisecomOspfVersionNumber':raisecomOspfVersionNumber,'raisecomOspfAreaBdrRtrStatus':raisecomOspfAreaBdrRtrStatus,'raisecomOspfASBdrRtrStatus':raisecomOspfASBdrRtrStatus,'raisecomOspfExternLsaCount':raisecomOspfExternLsaCount,'raisecomOspfExternLsaCksumSum':raisecomOspfExternLsaCksumSum,'raisecomOspfOriginateNewLsas':raisecomOspfOriginateNewLsas,'raisecomOspfRxNewLsas':raisecomOspfRxNewLsas,_z:raisecomOspfExtLsdbLimit,'raisecomOspfExitOverflowInterval':raisecomOspfExitOverflowInterval,'raisecomOspfReferenceBandwidth':raisecomOspfReferenceBandwidth,'raisecomOspfAsLsaCount':raisecomOspfAsLsaCount,'raisecomOspfAsLsaCksumSum':raisecomOspfAsLsaCksumSum,'raisecomOspfStubRouterSupport':raisecomOspfStubRouterSupport,'raisecomOspfStubRouterAdvertisement':raisecomOspfStubRouterAdvertisement,'raisecomOspfAdminDistance':raisecomOspfAdminDistance,'raisecomOspfSpfInterval':raisecomOspfSpfInterval,'raisecomOspfReset':raisecomOspfReset,'raisecomOspfExportMetric':raisecomOspfExportMetric,'raisecomOspfExportTag':raisecomOspfExportTag,'raisecomOspfExportType':raisecomOspfExportType,'raisecomOspfNetCounts':raisecomOspfNetCounts,'raisecomOspfAreaCounts':raisecomOspfAreaCounts,'raisecomOspfNssaAreaCounts':raisecomOspfNssaAreaCounts,'raisecomOspfSpfCounts':raisecomOspfSpfCounts,'raisecomOspfGlobalStatus':raisecomOspfGlobalStatus,_A2:raisecomOspfRedistributeRouteLimit,'raisecomOspfAreaTable':raisecomOspfAreaTable,'raisecomOspfAreaEntry':raisecomOspfAreaEntry,_r:raisecomOspfAreaId,'raisecomOspfAuthType':raisecomOspfAuthType,'raisecomOspfImportAsExtern':raisecomOspfImportAsExtern,'raisecomOspfSpfRuns':raisecomOspfSpfRuns,'raisecomOspfAreaBdrRtrCount':raisecomOspfAreaBdrRtrCount,'raisecomOspfAsBdrRtrCount':raisecomOspfAsBdrRtrCount,'raisecomOspfAreaLsaCount':raisecomOspfAreaLsaCount,'raisecomOspfAreaLsaCksumSum':raisecomOspfAreaLsaCksumSum,'raisecomOspfAreaSummary':raisecomOspfAreaSummary,'raisecomOspfAreaNssaTranslatorRole':raisecomOspfAreaNssaTranslatorRole,'raisecomOspfAreaNssaTranslatorState':raisecomOspfAreaNssaTranslatorState,'raisecomOspfAreaNssaTranslatorStabilityInterval':raisecomOspfAreaNssaTranslatorStabilityInterval,'raisecomOspfAreaNssaTranslatorEvents':raisecomOspfAreaNssaTranslatorEvents,'raisecomOspfAreaDefaultCost':raisecomOspfAreaDefaultCost,'raisecomOspfAreaType':raisecomOspfAreaType,'raisecomOspfAreaAbrCount':raisecomOspfAreaAbrCount,'raisecomOspfAreaAsbrCount':raisecomOspfAreaAsbrCount,'raisecomOspfAreaStatus':raisecomOspfAreaStatus,'raisecomOspfAreaFilterInIpPrefixListName':raisecomOspfAreaFilterInIpPrefixListName,'raisecomOspfAreaFilterOutIpPrefixListName':raisecomOspfAreaFilterOutIpPrefixListName,'raisecomOspfNetWorkTable':raisecomOspfNetWorkTable,'raisecomOspfNetWorkEntry':raisecomOspfNetWorkEntry,_A7:raisecomOspfNet,_A8:raisecomOspfMask,'raisecomOspfNetWorkStatus':raisecomOspfNetWorkStatus,'raisecomOspfStubAreaTable':raisecomOspfStubAreaTable,'raisecomOspfStubAreaEntry':raisecomOspfStubAreaEntry,_A9:raisecomOspfStubAreaId,'raisecomOspfStubAreaOption':raisecomOspfStubAreaOption,'raisecomOspfStubAreaStatus':raisecomOspfStubAreaStatus,'raisecomOspfNssaAreaTable':raisecomOspfNssaAreaTable,'raisecomOspfNssaAreaEntry':raisecomOspfNssaAreaEntry,_AA:raisecomOspfNssaAreaId,'raisecomOspfNssaAreaOption':raisecomOspfNssaAreaOption,'raisecomOspfNssaAreaStatus':raisecomOspfNssaAreaStatus,'raisecomOspfIfTable':raisecomOspfIfTable,'raisecomOspfIfEntry':raisecomOspfIfEntry,_J:raisecomOspfAddressLessIf,_N:raisecomOspfIfIpAddress,'raisecomOspfIfAreaId':raisecomOspfIfAreaId,'raisecomOspfIfType':raisecomOspfIfType,'raisecomOspfIfAdminStat':raisecomOspfIfAdminStat,'raisecomOspfIfRtrPriority':raisecomOspfIfRtrPriority,'raisecomOspfIfTransitDelay':raisecomOspfIfTransitDelay,'raisecomOspfIfRetransInterval':raisecomOspfIfRetransInterval,'raisecomOspfIfHelloInterval':raisecomOspfIfHelloInterval,'raisecomOspfIfRtrDeadInterval':raisecomOspfIfRtrDeadInterval,'raisecomOspfIfPollInterval':raisecomOspfIfPollInterval,_AZ:raisecomOspfIfState,'raisecomOspfIfDesignatedRouter':raisecomOspfIfDesignatedRouter,'raisecomOspfIfBackupDesignatedRouter':raisecomOspfIfBackupDesignatedRouter,'raisecomOspfIfEvents':raisecomOspfIfEvents,'raisecomOspfIfAuthKeyId':raisecomOspfIfAuthKeyId,'raisecomOspfIfAuthSimpleKeyType':raisecomOspfIfAuthSimpleKeyType,'raisecomOspfIfAuthMd5KeyType':raisecomOspfIfAuthMd5KeyType,'raisecomOspfIfAuthSimpleKey':raisecomOspfIfAuthSimpleKey,'raisecomOspfIfAuthMd5Key':raisecomOspfIfAuthMd5Key,_A0:raisecomOspfIfAuthKeyChain,'raisecomOspfIfAuthType':raisecomOspfIfAuthType,'raisecomOspfIfLsaCount':raisecomOspfIfLsaCount,'raisecomOspfIfLsaCksumSum':raisecomOspfIfLsaCksumSum,'raisecomOspfIfDesignatedRouterId':raisecomOspfIfDesignatedRouterId,'raisecomOspfIfBackupDesignatedRouterId':raisecomOspfIfBackupDesignatedRouterId,'raisecomOspfIfPassive':raisecomOspfIfPassive,'raisecomOspfIfMtu':raisecomOspfIfMtu,'raisecomOspfIfMetric':raisecomOspfIfMetric,'raisecomOspfVirtIfTable':raisecomOspfVirtIfTable,'raisecomOspfVirtIfEntry':raisecomOspfVirtIfEntry,_K:raisecomOspfVirtIfAreaId,_L:raisecomOspfVirtIfNeighbor,'raisecomOspfVirtIfTransitDelay':raisecomOspfVirtIfTransitDelay,'raisecomOspfVirtIfRetransInterval':raisecomOspfVirtIfRetransInterval,'raisecomOspfVirtIfHelloInterval':raisecomOspfVirtIfHelloInterval,'raisecomOspfVirtIfRtrDeadInterval':raisecomOspfVirtIfRtrDeadInterval,_Aa:raisecomOspfVirtIfState,'raisecomOspfVirtIfEvents':raisecomOspfVirtIfEvents,'raisecomOspfVirtIfAuthKeyId':raisecomOspfVirtIfAuthKeyId,'raisecomOspfVirtIfAuthSimpleKeyType':raisecomOspfVirtIfAuthSimpleKeyType,'raisecomOspfVirtIfAuthMd5KeyType':raisecomOspfVirtIfAuthMd5KeyType,'raisecomOspfVirtIfAuthSimpleKey':raisecomOspfVirtIfAuthSimpleKey,'raisecomOspfVirtIfAuthMd5Key':raisecomOspfVirtIfAuthMd5Key,_A1:raisecomOspfVirtIfAuthKeyChain,'raisecomOspfVirtIfAuthType':raisecomOspfVirtIfAuthType,'raisecomOspfVirtIfLsaCount':raisecomOspfVirtIfLsaCount,'raisecomOspfVirtIfLsaCksumSum':raisecomOspfVirtIfLsaCksumSum,'raisecomOspfVirtIfCost':raisecomOspfVirtIfCost,'raisecomOspfVirtIfStatus':raisecomOspfVirtIfStatus,'raisecomOspfNbrTable':raisecomOspfNbrTable,'raisecomOspfNbrEntry':raisecomOspfNbrEntry,_u:raisecomOspfNbrIpAddr,_Ab:raisecomOspfNbrAddressLessIndex,_y:raisecomOspfNbrRtrId,'raisecomOspfNbrOptions':raisecomOspfNbrOptions,'raisecomOspfNbrPriority':raisecomOspfNbrPriority,_Ac:raisecomOspfNbrState,'raisecomOspfNbrEvents':raisecomOspfNbrEvents,'raisecomOspfNbrLsRetransQLen':raisecomOspfNbrLsRetransQLen,'raisecomOspfNbrMode':raisecomOspfNbrMode,'raisecomOspfNbmaCfgNbrTable':raisecomOspfNbmaCfgNbrTable,'raisecomOspfNbmaCfgNbrEntry':raisecomOspfNbmaCfgNbrEntry,_AC:raisecomOspfNbmaCfgNbrIpAddr,'raisecomOspfNbmaCfgNbrPriority':raisecomOspfNbmaCfgNbrPriority,'raisecomOspfNbmaCfgNbrStatus':raisecomOspfNbmaCfgNbrStatus,'raisecomOspfVirtNbrTable':raisecomOspfVirtNbrTable,'raisecomOspfVirtNbrEntry':raisecomOspfVirtNbrEntry,_v:raisecomOspfVirtNbrArea,_w:raisecomOspfVirtNbrRtrId,'raisecomOspfVirtNbrIpAddr':raisecomOspfVirtNbrIpAddr,'raisecomOspfVirtNbrOptions':raisecomOspfVirtNbrOptions,_Ad:raisecomOspfVirtNbrState,'raisecomOspfVirtNbrEvents':raisecomOspfVirtNbrEvents,'raisecomOspfVirtNbrLsRetransQLen':raisecomOspfVirtNbrLsRetransQLen,'raisecomOspfVirtNbrLessIf':raisecomOspfVirtNbrLessIf,'raisecomOspfVirtNbrMode':raisecomOspfVirtNbrMode,'raisecomOspfAreaAggregateTable':raisecomOspfAreaAggregateTable,'raisecomOspfAreaAggregateEntry':raisecomOspfAreaAggregateEntry,_AD:raisecomOspfAreaAggregateAreaID,_AE:raisecomOspfAreaAggregateLsdbType,_AF:raisecomOspfAreaAggregateNet,_AG:raisecomOspfAreaAggregateMask,'raisecomOspfAreaAggregateEffect':raisecomOspfAreaAggregateEffect,'raisecomOspfAreaAggregateStatus':raisecomOspfAreaAggregateStatus,'raisecomOspfExternalAggregateTable':raisecomOspfExternalAggregateTable,'raisecomOspfExternalAggregateEntry':raisecomOspfExternalAggregateEntry,_AH:raisecomOspfExternalAggregateNet,_AI:raisecomOspfExternalAggregateMask,'raisecomOspfExternalAggregateEffect':raisecomOspfExternalAggregateEffect,'raisecomOspfExternalAggregateCost':raisecomOspfExternalAggregateCost,'raisecomOspfExternalAggregateStatus':raisecomOspfExternalAggregateStatus,'raisecomOspfLsdbTable':raisecomOspfLsdbTable,'raisecomOspfLsdbEntry':raisecomOspfLsdbEntry,_f:raisecomOspfLsdbAreaId,_Q:raisecomOspfLsdbType,_R:raisecomOspfLsdbLsId,_S:raisecomOspfLsdbRouterId,'raisecomOspfLsdbSequence':raisecomOspfLsdbSequence,'raisecomOspfLsdbAge':raisecomOspfLsdbAge,'raisecomOspfLsdbChecksum':raisecomOspfLsdbChecksum,'raisecomOspfLsdbAdvertisement':raisecomOspfLsdbAdvertisement,'raisecomOspfAsLsdbTable':raisecomOspfAsLsdbTable,'raisecomOspfAsLsdbEntry':raisecomOspfAsLsdbEntry,_AJ:raisecomOspfAsLsdbType,_AK:raisecomOspfAsLsdbLsId,_AL:raisecomOspfAsLsdbRouterId,'raisecomOspfAsLsdbSequence':raisecomOspfAsLsdbSequence,'raisecomOspfAsLsdbAge':raisecomOspfAsLsdbAge,'raisecomOspfAsLsdbChecksum':raisecomOspfAsLsdbChecksum,'raisecomOspfAsLsdbAdvertisement':raisecomOspfAsLsdbAdvertisement,'raisecomOspfAreaLsaCountTable':raisecomOspfAreaLsaCountTable,'raisecomOspfAreaLsaCountEntry':raisecomOspfAreaLsaCountEntry,_AM:raisecomOspfAreaLsaCountAreaId,_AN:raisecomOspfAreaLsaCountLsaType,'raisecomOspfAreaLsaCountNumber':raisecomOspfAreaLsaCountNumber,'raisecomOspfRedistributeTable':raisecomOspfRedistributeTable,'raisecomOspfRedistributeEntry':raisecomOspfRedistributeEntry,_m:raisecomOspfRedistributeProtocol,_n:raisecomOspfRedistributeProcessId,'raisecomOspfRedistributeCost':raisecomOspfRedistributeCost,'raisecomOspfRedistributeType':raisecomOspfRedistributeType,'raisecomOspfRedistributeStatus':raisecomOspfRedistributeStatus,'raisecomOspfRedistributeRouteMapName':raisecomOspfRedistributeRouteMapName,'raisecomOspfRedistributeTag':raisecomOspfRedistributeTag,'raisecomOspfDefaultInfoTable':raisecomOspfDefaultInfoTable,'raisecomOspfDefaultInfoEntry':raisecomOspfDefaultInfoEntry,'raisecomOspfDefaultInfoAlways':raisecomOspfDefaultInfoAlways,'raisecomOspfDefaultInfoCost':raisecomOspfDefaultInfoCost,'raisecomOspfDefaultInfoType':raisecomOspfDefaultInfoType,'raisecomOspfDefaultInfoStatus':raisecomOspfDefaultInfoStatus,'raisecomOspfPacketIoStatisTable':raisecomOspfPacketIoStatisTable,'raisecomOspfPacketIoStatisEntry':raisecomOspfPacketIoStatisEntry,_AO:raisecomOspfPacketIoStatisIoType,_AP:raisecomOspfPacketIoStatisPktType,'raisecomOspfPacketIoStatisNumber':raisecomOspfPacketIoStatisNumber,'raisecomOspfRouteTable':raisecomOspfRouteTable,'raisecomOspfRouteEntry':raisecomOspfRouteEntry,_AQ:raisecomOspfRouteDest,_AR:raisecomOspfRouteMask,_AS:raisecomOspfRouteType,'raisecomOspfRouteLsType':raisecomOspfRouteLsType,'raisecomOspfRouteMetric':raisecomOspfRouteMetric,'raisecomOspfRouteNextHop':raisecomOspfRouteNextHop,'raisecomOspfRouteAdvRtr':raisecomOspfRouteAdvRtr,'raisecomOspfRouteArea':raisecomOspfRouteArea,'raisecomOspfBdrRouteTable':raisecomOspfBdrRouteTable,'raisecomOspfBdrRouteEntry':raisecomOspfBdrRouteEntry,_AT:raisecomOspfBdrRouteRtrType,_AU:raisecomOspfBdrRouteArea,_AV:raisecomOspfBdrRouteDest,_AW:raisecomOspfBdrRouteNextHop,'raisecomOspfBdrRouteLsType':raisecomOspfBdrRouteLsType,'raisecomOspfBdrRouteMetric':raisecomOspfBdrRouteMetric,'raisecomOspfDistributeListGroup':raisecomOspfDistributeListGroup,'raisecomOspfDistributeListInTable':raisecomOspfDistributeListInTable,'raisecomOspfDistributeListInEntry':raisecomOspfDistributeListInEntry,'raisecomOspfDistrInIpPrefixListName':raisecomOspfDistrInIpPrefixListName,'raisecomOspfDistrInAclNum':raisecomOspfDistrInAclNum,'raisecomOspfDistrInRowStatus':raisecomOspfDistrInRowStatus,'raisecomOspfDistributeListOutTable':raisecomOspfDistributeListOutTable,'raisecomOspfDistributeListOutEntry':raisecomOspfDistributeListOutEntry,'raisecomOspfDistrOutIpPrefixListName':raisecomOspfDistrOutIpPrefixListName,'raisecomOspfDistrOutAclNum':raisecomOspfDistrOutAclNum,'raisecomOspfDistrOutRowStatus':raisecomOspfDistrOutRowStatus,'raisecomOspfDistributeListOutProtocolTable':raisecomOspfDistributeListOutProtocolTable,'raisecomOspfDistributeListOutProtocolEntry':raisecomOspfDistributeListOutProtocolEntry,_AX:raisecomOspfDistrOutProtocol,_AY:raisecomOspfDistrOutProcessId,'raisecomOspfDistrOutProIpPrefixListName':raisecomOspfDistrOutProIpPrefixListName,'raisecomOspfDistrOutProAclNum':raisecomOspfDistrOutProAclNum,'raisecomOspfDistrOutProRowStatus':raisecomOspfDistrOutProRowStatus,'raisecomOspfConformance':raisecomOspfConformance})