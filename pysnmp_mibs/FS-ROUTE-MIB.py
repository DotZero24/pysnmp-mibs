_Af='fsipCidrRouteMibGroup'
_Ae='fsRouteFilteringMibGroup'
_Ad='fsRouteRedistributeMIBGroup'
_Ac='fsRouteMapMIBGroup'
_Ab='fsRouteInfoMIBGroup'
_Aa='fsRouteMIBGroup'
_AZ='fsipCidrOspfRouteType'
_AY='fsipCidrRouteStatus'
_AX='fsipCidrRouteMetric5'
_AW='fsipCidrRouteMetric4'
_AV='fsipCidrRouteMetric3'
_AU='fsipCidrRouteMetric2'
_AT='fsipCidrRouteMetric1'
_AS='fsipCidrRouteNextHopAS'
_AR='fsipCidrRouteInfo'
_AQ='fsipCidrRouteAge'
_AP='fsipCidrRouteProto'
_AO='fsipCidrRouteType'
_AN='fsipCidrRouteIfIndex'
_AM='fsDistributeListStatus'
_AL='fsDistributeListPrefixIpPrefixName'
_AK='fsDistributeListGateWayIpPrefixName'
_AJ='fsDistributeListAclName'
_AI='fsDistributeListFilterType'
_AH='fsIpPrefixListStatus'
_AG='fsIpPrefixListMaximumPrefixLength'
_AF='fsIpPrefixListMinimumPrefixLength'
_AE='fsIpPrefixListMaskLength'
_AD='fsIpPrefixListIpAddress'
_AC='fsIpPrefixListOperMethod'
_AB='fsRouteRedistributeStatus'
_AA='fsRouteRedistributeRouteMapName'
_A9='fsRouteRedistributeTagValue'
_A8='fsRouteRedistributeMetricType'
_A7='fsRouteRedistributeMetricValue'
_A6='fsRouteMapMatchInterfaceStatus'
_A5='fsRouteMapMatchTagStatus'
_A4='fsRouteMapMatchIpAddressStatus'
_A3='fsRouteMapStatus'
_A2='fsRouteMapSetMetricType'
_A1='fsRouteMapSetLevel'
_A0='fsRouteMapSetMetric'
_z='fsRouteMapMetricValueType'
_y='fsRouteMapMatchRouteType'
_x='fsRouteMapMatchMetric'
_w='fsRouteMapOperType'
_v='fsDefRoutingCfgStatus'
_u='fsDefRoutingCfgRouteMap'
_t='fsDefRoutingCfgMetricType'
_s='fsDefRoutingCfgMetric'
_r='fsDefRoutingCfgAlways'
_q='fsRoutingProtoInfoLastUpdate'
_p='fsRoutingProtoInfoDistance'
_o='fsRouteServiceStatus'
_n='noOper'
_m='external'
_l='internal'
_k='permit'
_j='netmgmt'
_i='TruthValue'
_h='ConfigStatus'
_g='fsRouteMapSetNexthopSt'
_f='fsipCidrRouteNextHop'
_e='fsipCidrRouteTos'
_d='fsipCidrRouteMask'
_c='fsipCidrRouteDest'
_b='fsDistributeListFilteringProtocol'
_a='fsDistributeListDirection'
_Z='fsDistributeListIfIndex'
_Y='fsDistributeListCfgProtoType'
_X='fsIpPrefixListSequence'
_W='fsIpPrefixListName'
_V='fsRouteRedistributeProtocol'
_U='fsRouteRedistributeProtocolCfg'
_T='fsRouteMapMatchInterfaceIfIndex'
_S='fsRouteMapMatchTagValue'
_R='fsRouteMapMatchIpAddressAclName'
_Q='fsRouteMapMatchType'
_P='type2'
_O='type1'
_N='fsDefRoutingCfgRoutingProtoType'
_M='fsRoutingProtoInfoGateWay'
_L='fsRoutingProtoInfoProtoType'
_K='local'
_J='other'
_I='fsRouteMapSequenceNumber'
_H='fsRouteMapName'
_G='DisplayString'
_F='Unsigned32'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='current'
_A='FS-ROUTE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('FS-TC',_h,'IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention',_i)
fsRouteMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,20))
if mibBuilder.loadTexts:fsRouteMIB.setRevisions(('2002-03-20 00:00',))
class FSRouteProtoType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_J,1),(_K,2),(_j,3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('isis',9),('esis',10),('ciscoigrp',11),('bbnspfigp',12),('ospf',13),('bgp',14),('idpr',15),('ciscoeigrp',16),('max',17)))
_FsRouteMIBObjects_ObjectIdentity=ObjectIdentity
fsRouteMIBObjects=_FsRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,20,1))
_FsRouteServiceStatus_Type=EnabledStatus
_FsRouteServiceStatus_Object=MibScalar
fsRouteServiceStatus=_FsRouteServiceStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,1),_FsRouteServiceStatus_Type())
fsRouteServiceStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsRouteServiceStatus.setStatus(_B)
_FsRoutingProtoInfoTable_Object=MibTable
fsRoutingProtoInfoTable=_FsRoutingProtoInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,2))
if mibBuilder.loadTexts:fsRoutingProtoInfoTable.setStatus(_B)
_FsRoutingProtoInfoEntry_Object=MibTableRow
fsRoutingProtoInfoEntry=_FsRoutingProtoInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,2,1))
fsRoutingProtoInfoEntry.setIndexNames((0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:fsRoutingProtoInfoEntry.setStatus(_B)
_FsRoutingProtoInfoProtoType_Type=FSRouteProtoType
_FsRoutingProtoInfoProtoType_Object=MibTableColumn
fsRoutingProtoInfoProtoType=_FsRoutingProtoInfoProtoType_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,2,1,1),_FsRoutingProtoInfoProtoType_Type())
fsRoutingProtoInfoProtoType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoutingProtoInfoProtoType.setStatus(_B)
_FsRoutingProtoInfoGateWay_Type=IpAddress
_FsRoutingProtoInfoGateWay_Object=MibTableColumn
fsRoutingProtoInfoGateWay=_FsRoutingProtoInfoGateWay_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,2,1,2),_FsRoutingProtoInfoGateWay_Type())
fsRoutingProtoInfoGateWay.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoutingProtoInfoGateWay.setStatus(_B)
_FsRoutingProtoInfoDistance_Type=Unsigned32
_FsRoutingProtoInfoDistance_Object=MibTableColumn
fsRoutingProtoInfoDistance=_FsRoutingProtoInfoDistance_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,2,1,3),_FsRoutingProtoInfoDistance_Type())
fsRoutingProtoInfoDistance.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoutingProtoInfoDistance.setStatus(_B)
_FsRoutingProtoInfoLastUpdate_Type=TimeTicks
_FsRoutingProtoInfoLastUpdate_Object=MibTableColumn
fsRoutingProtoInfoLastUpdate=_FsRoutingProtoInfoLastUpdate_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,2,1,4),_FsRoutingProtoInfoLastUpdate_Type())
fsRoutingProtoInfoLastUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoutingProtoInfoLastUpdate.setStatus(_B)
_FsDefRoutingCfgTable_Object=MibTable
fsDefRoutingCfgTable=_FsDefRoutingCfgTable_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,3))
if mibBuilder.loadTexts:fsDefRoutingCfgTable.setStatus(_B)
_FsDefRoutingCfgEntry_Object=MibTableRow
fsDefRoutingCfgEntry=_FsDefRoutingCfgEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,3,1))
fsDefRoutingCfgEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:fsDefRoutingCfgEntry.setStatus(_B)
_FsDefRoutingCfgRoutingProtoType_Type=FSRouteProtoType
_FsDefRoutingCfgRoutingProtoType_Object=MibTableColumn
fsDefRoutingCfgRoutingProtoType=_FsDefRoutingCfgRoutingProtoType_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,3,1,1),_FsDefRoutingCfgRoutingProtoType_Type())
fsDefRoutingCfgRoutingProtoType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDefRoutingCfgRoutingProtoType.setStatus(_B)
class _FsDefRoutingCfgAlways_Type(TruthValue):defaultValue=2
_FsDefRoutingCfgAlways_Type.__name__=_i
_FsDefRoutingCfgAlways_Object=MibTableColumn
fsDefRoutingCfgAlways=_FsDefRoutingCfgAlways_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,3,1,2),_FsDefRoutingCfgAlways_Type())
fsDefRoutingCfgAlways.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDefRoutingCfgAlways.setStatus(_B)
class _FsDefRoutingCfgMetric_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777214))
_FsDefRoutingCfgMetric_Type.__name__=_F
_FsDefRoutingCfgMetric_Object=MibTableColumn
fsDefRoutingCfgMetric=_FsDefRoutingCfgMetric_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,3,1,3),_FsDefRoutingCfgMetric_Type())
fsDefRoutingCfgMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDefRoutingCfgMetric.setStatus(_B)
class _FsDefRoutingCfgMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_FsDefRoutingCfgMetricType_Type.__name__=_E
_FsDefRoutingCfgMetricType_Object=MibTableColumn
fsDefRoutingCfgMetricType=_FsDefRoutingCfgMetricType_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,3,1,4),_FsDefRoutingCfgMetricType_Type())
fsDefRoutingCfgMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDefRoutingCfgMetricType.setStatus(_B)
class _FsDefRoutingCfgRouteMap_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsDefRoutingCfgRouteMap_Type.__name__=_G
_FsDefRoutingCfgRouteMap_Object=MibTableColumn
fsDefRoutingCfgRouteMap=_FsDefRoutingCfgRouteMap_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,3,1,5),_FsDefRoutingCfgRouteMap_Type())
fsDefRoutingCfgRouteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDefRoutingCfgRouteMap.setStatus(_B)
_FsDefRoutingCfgStatus_Type=RowStatus
_FsDefRoutingCfgStatus_Object=MibTableColumn
fsDefRoutingCfgStatus=_FsDefRoutingCfgStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,20,1,3,1,6),_FsDefRoutingCfgStatus_Type())
fsDefRoutingCfgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDefRoutingCfgStatus.setStatus(_B)
_FsRouteMapMIBObjects_ObjectIdentity=ObjectIdentity
fsRouteMapMIBObjects=_FsRouteMapMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,20,2))
_FsRouteMapTable_Object=MibTable
fsRouteMapTable=_FsRouteMapTable_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1))
if mibBuilder.loadTexts:fsRouteMapTable.setStatus(_B)
_FsRouteMapEntry_Object=MibTableRow
fsRouteMapEntry=_FsRouteMapEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1,1))
fsRouteMapEntry.setIndexNames((0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:fsRouteMapEntry.setStatus(_B)
class _FsRouteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsRouteMapName_Type.__name__=_G
_FsRouteMapName_Object=MibTableColumn
fsRouteMapName=_FsRouteMapName_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1,1,1),_FsRouteMapName_Type())
fsRouteMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRouteMapName.setStatus(_B)
class _FsRouteMapSequenceNumber_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsRouteMapSequenceNumber_Type.__name__=_F
_FsRouteMapSequenceNumber_Object=MibTableColumn
fsRouteMapSequenceNumber=_FsRouteMapSequenceNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1,1,2),_FsRouteMapSequenceNumber_Type())
fsRouteMapSequenceNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRouteMapSequenceNumber.setStatus(_B)
class _FsRouteMapOperType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),('deny',2)))
_FsRouteMapOperType_Type.__name__=_E
_FsRouteMapOperType_Object=MibTableColumn
fsRouteMapOperType=_FsRouteMapOperType_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1,1,3),_FsRouteMapOperType_Type())
fsRouteMapOperType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRouteMapOperType.setStatus(_B)
class _FsRouteMapMatchMetric_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsRouteMapMatchMetric_Type.__name__=_F
_FsRouteMapMatchMetric_Object=MibTableColumn
fsRouteMapMatchMetric=_FsRouteMapMatchMetric_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1,1,4),_FsRouteMapMatchMetric_Type())
fsRouteMapMatchMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapMatchMetric.setStatus(_B)
class _FsRouteMapMatchRouteType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('notMatch',0),(_l,1),(_m,2),('external-type1',3),('external-type2',4)))
_FsRouteMapMatchRouteType_Type.__name__=_E
_FsRouteMapMatchRouteType_Object=MibTableColumn
fsRouteMapMatchRouteType=_FsRouteMapMatchRouteType_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1,1,5),_FsRouteMapMatchRouteType_Type())
fsRouteMapMatchRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapMatchRouteType.setStatus(_B)
class _FsRouteMapMetricValueType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_n,0),('replace',1),('add',2),('reduce',3)))
_FsRouteMapMetricValueType_Type.__name__=_E
_FsRouteMapMetricValueType_Object=MibTableColumn
fsRouteMapMetricValueType=_FsRouteMapMetricValueType_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1,1,6),_FsRouteMapMetricValueType_Type())
fsRouteMapMetricValueType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapMetricValueType.setStatus(_B)
class _FsRouteMapSetMetric_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsRouteMapSetMetric_Type.__name__=_F
_FsRouteMapSetMetric_Object=MibTableColumn
fsRouteMapSetMetric=_FsRouteMapSetMetric_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1,1,7),_FsRouteMapSetMetric_Type())
fsRouteMapSetMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetMetric.setStatus(_B)
class _FsRouteMapSetLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('all',0),('stubarea',1),('backbone',2)))
_FsRouteMapSetLevel_Type.__name__=_E
_FsRouteMapSetLevel_Object=MibTableColumn
fsRouteMapSetLevel=_FsRouteMapSetLevel_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1,1,8),_FsRouteMapSetLevel_Type())
fsRouteMapSetLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetLevel.setStatus(_B)
class _FsRouteMapSetMetricType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_n,0),(_l,1),(_m,2),(_O,3),(_P,4)))
_FsRouteMapSetMetricType_Type.__name__=_E
_FsRouteMapSetMetricType_Object=MibTableColumn
fsRouteMapSetMetricType=_FsRouteMapSetMetricType_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1,1,9),_FsRouteMapSetMetricType_Type())
fsRouteMapSetMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetMetricType.setStatus(_B)
class _FsRouteMapSetNexthopSt_Type(ConfigStatus):defaultValue=2
_FsRouteMapSetNexthopSt_Type.__name__=_h
_FsRouteMapSetNexthopSt_Object=MibTableColumn
fsRouteMapSetNexthopSt=_FsRouteMapSetNexthopSt_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1,1,10),_FsRouteMapSetNexthopSt_Type())
fsRouteMapSetNexthopSt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetNexthopSt.setStatus(_B)
_FsRouteMapSetNexthop_Type=IpAddress
_FsRouteMapSetNexthop_Object=MibTableColumn
fsRouteMapSetNexthop=_FsRouteMapSetNexthop_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1,1,11),_FsRouteMapSetNexthop_Type())
fsRouteMapSetNexthop.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetNexthop.setStatus(_B)
_FsRouteMapStatus_Type=RowStatus
_FsRouteMapStatus_Object=MibTableColumn
fsRouteMapStatus=_FsRouteMapStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,1,1,12),_FsRouteMapStatus_Type())
fsRouteMapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapStatus.setStatus(_B)
_FsRouteMapMatchIpAddressTable_Object=MibTable
fsRouteMapMatchIpAddressTable=_FsRouteMapMatchIpAddressTable_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,2))
if mibBuilder.loadTexts:fsRouteMapMatchIpAddressTable.setStatus(_B)
_FsRouteMapMatchIpAddressEntry_Object=MibTableRow
fsRouteMapMatchIpAddressEntry=_FsRouteMapMatchIpAddressEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,2,1))
fsRouteMapMatchIpAddressEntry.setIndexNames((0,_A,_H),(0,_A,_I),(0,_A,_Q),(0,_A,_R))
if mibBuilder.loadTexts:fsRouteMapMatchIpAddressEntry.setStatus(_B)
class _FsRouteMapMatchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('destination',1),('nextHop',2),('source',3)))
_FsRouteMapMatchType_Type.__name__=_E
_FsRouteMapMatchType_Object=MibTableColumn
fsRouteMapMatchType=_FsRouteMapMatchType_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,2,1,1),_FsRouteMapMatchType_Type())
fsRouteMapMatchType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRouteMapMatchType.setStatus(_B)
class _FsRouteMapMatchIpAddressAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsRouteMapMatchIpAddressAclName_Type.__name__=_G
_FsRouteMapMatchIpAddressAclName_Object=MibTableColumn
fsRouteMapMatchIpAddressAclName=_FsRouteMapMatchIpAddressAclName_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,2,1,2),_FsRouteMapMatchIpAddressAclName_Type())
fsRouteMapMatchIpAddressAclName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRouteMapMatchIpAddressAclName.setStatus(_B)
_FsRouteMapMatchIpAddressStatus_Type=RowStatus
_FsRouteMapMatchIpAddressStatus_Object=MibTableColumn
fsRouteMapMatchIpAddressStatus=_FsRouteMapMatchIpAddressStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,2,1,3),_FsRouteMapMatchIpAddressStatus_Type())
fsRouteMapMatchIpAddressStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapMatchIpAddressStatus.setStatus(_B)
_FsRouteMapMatchTagTable_Object=MibTable
fsRouteMapMatchTagTable=_FsRouteMapMatchTagTable_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,3))
if mibBuilder.loadTexts:fsRouteMapMatchTagTable.setStatus(_B)
_FsRouteMapMatchTagEntry_Object=MibTableRow
fsRouteMapMatchTagEntry=_FsRouteMapMatchTagEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,3,1))
fsRouteMapMatchTagEntry.setIndexNames((0,_A,_H),(0,_A,_I),(0,_A,_S))
if mibBuilder.loadTexts:fsRouteMapMatchTagEntry.setStatus(_B)
class _FsRouteMapMatchTagValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsRouteMapMatchTagValue_Type.__name__=_F
_FsRouteMapMatchTagValue_Object=MibTableColumn
fsRouteMapMatchTagValue=_FsRouteMapMatchTagValue_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,3,1,1),_FsRouteMapMatchTagValue_Type())
fsRouteMapMatchTagValue.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRouteMapMatchTagValue.setStatus(_B)
_FsRouteMapMatchTagStatus_Type=RowStatus
_FsRouteMapMatchTagStatus_Object=MibTableColumn
fsRouteMapMatchTagStatus=_FsRouteMapMatchTagStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,3,1,2),_FsRouteMapMatchTagStatus_Type())
fsRouteMapMatchTagStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapMatchTagStatus.setStatus(_B)
_FsRouteMapMatchInterfaceTable_Object=MibTable
fsRouteMapMatchInterfaceTable=_FsRouteMapMatchInterfaceTable_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,4))
if mibBuilder.loadTexts:fsRouteMapMatchInterfaceTable.setStatus(_B)
_FsRouteMapMatchInterfaceEntry_Object=MibTableRow
fsRouteMapMatchInterfaceEntry=_FsRouteMapMatchInterfaceEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,4,1))
fsRouteMapMatchInterfaceEntry.setIndexNames((0,_A,_H),(0,_A,_I),(0,_A,_T))
if mibBuilder.loadTexts:fsRouteMapMatchInterfaceEntry.setStatus(_B)
_FsRouteMapMatchInterfaceIfIndex_Type=IfIndex
_FsRouteMapMatchInterfaceIfIndex_Object=MibTableColumn
fsRouteMapMatchInterfaceIfIndex=_FsRouteMapMatchInterfaceIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,4,1,1),_FsRouteMapMatchInterfaceIfIndex_Type())
fsRouteMapMatchInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRouteMapMatchInterfaceIfIndex.setStatus(_B)
_FsRouteMapMatchInterfaceStatus_Type=RowStatus
_FsRouteMapMatchInterfaceStatus_Object=MibTableColumn
fsRouteMapMatchInterfaceStatus=_FsRouteMapMatchInterfaceStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,20,2,4,1,2),_FsRouteMapMatchInterfaceStatus_Type())
fsRouteMapMatchInterfaceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapMatchInterfaceStatus.setStatus(_B)
_FsRouteRedistributeMIBObjects_ObjectIdentity=ObjectIdentity
fsRouteRedistributeMIBObjects=_FsRouteRedistributeMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,20,3))
_FsRouteRedistributeTable_Object=MibTable
fsRouteRedistributeTable=_FsRouteRedistributeTable_Object((1,3,6,1,4,1,52642,1,1,10,2,20,3,1))
if mibBuilder.loadTexts:fsRouteRedistributeTable.setStatus(_B)
_FsRouteRedistributeEntry_Object=MibTableRow
fsRouteRedistributeEntry=_FsRouteRedistributeEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,20,3,1,1))
fsRouteRedistributeEntry.setIndexNames((0,_A,_U),(0,_A,_V))
if mibBuilder.loadTexts:fsRouteRedistributeEntry.setStatus(_B)
_FsRouteRedistributeProtocolCfg_Type=FSRouteProtoType
_FsRouteRedistributeProtocolCfg_Object=MibTableColumn
fsRouteRedistributeProtocolCfg=_FsRouteRedistributeProtocolCfg_Object((1,3,6,1,4,1,52642,1,1,10,2,20,3,1,1,1),_FsRouteRedistributeProtocolCfg_Type())
fsRouteRedistributeProtocolCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRouteRedistributeProtocolCfg.setStatus(_B)
_FsRouteRedistributeProtocol_Type=FSRouteProtoType
_FsRouteRedistributeProtocol_Object=MibTableColumn
fsRouteRedistributeProtocol=_FsRouteRedistributeProtocol_Object((1,3,6,1,4,1,52642,1,1,10,2,20,3,1,1,2),_FsRouteRedistributeProtocol_Type())
fsRouteRedistributeProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRouteRedistributeProtocol.setStatus(_B)
class _FsRouteRedistributeMetricValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777214))
_FsRouteRedistributeMetricValue_Type.__name__=_F
_FsRouteRedistributeMetricValue_Object=MibTableColumn
fsRouteRedistributeMetricValue=_FsRouteRedistributeMetricValue_Object((1,3,6,1,4,1,52642,1,1,10,2,20,3,1,1,3),_FsRouteRedistributeMetricValue_Type())
fsRouteRedistributeMetricValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteRedistributeMetricValue.setStatus(_B)
class _FsRouteRedistributeMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_FsRouteRedistributeMetricType_Type.__name__=_E
_FsRouteRedistributeMetricType_Object=MibTableColumn
fsRouteRedistributeMetricType=_FsRouteRedistributeMetricType_Object((1,3,6,1,4,1,52642,1,1,10,2,20,3,1,1,4),_FsRouteRedistributeMetricType_Type())
fsRouteRedistributeMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteRedistributeMetricType.setStatus(_B)
class _FsRouteRedistributeTagValue_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsRouteRedistributeTagValue_Type.__name__=_F
_FsRouteRedistributeTagValue_Object=MibTableColumn
fsRouteRedistributeTagValue=_FsRouteRedistributeTagValue_Object((1,3,6,1,4,1,52642,1,1,10,2,20,3,1,1,5),_FsRouteRedistributeTagValue_Type())
fsRouteRedistributeTagValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteRedistributeTagValue.setStatus(_B)
class _FsRouteRedistributeRouteMapName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsRouteRedistributeRouteMapName_Type.__name__=_G
_FsRouteRedistributeRouteMapName_Object=MibTableColumn
fsRouteRedistributeRouteMapName=_FsRouteRedistributeRouteMapName_Object((1,3,6,1,4,1,52642,1,1,10,2,20,3,1,1,6),_FsRouteRedistributeRouteMapName_Type())
fsRouteRedistributeRouteMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteRedistributeRouteMapName.setStatus(_B)
_FsRouteRedistributeStatus_Type=RowStatus
_FsRouteRedistributeStatus_Object=MibTableColumn
fsRouteRedistributeStatus=_FsRouteRedistributeStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,20,3,1,1,7),_FsRouteRedistributeStatus_Type())
fsRouteRedistributeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteRedistributeStatus.setStatus(_B)
_FsRouteFilteringMIBObjects_ObjectIdentity=ObjectIdentity
fsRouteFilteringMIBObjects=_FsRouteFilteringMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,20,4))
_FsIpPrefixListTable_Object=MibTable
fsIpPrefixListTable=_FsIpPrefixListTable_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,1))
if mibBuilder.loadTexts:fsIpPrefixListTable.setStatus(_B)
_FsIpPrefixListEntry_Object=MibTableRow
fsIpPrefixListEntry=_FsIpPrefixListEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,1,1))
fsIpPrefixListEntry.setIndexNames((0,_A,_W),(0,_A,_X))
if mibBuilder.loadTexts:fsIpPrefixListEntry.setStatus(_B)
class _FsIpPrefixListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsIpPrefixListName_Type.__name__=_G
_FsIpPrefixListName_Object=MibTableColumn
fsIpPrefixListName=_FsIpPrefixListName_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,1,1,1),_FsIpPrefixListName_Type())
fsIpPrefixListName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpPrefixListName.setStatus(_B)
class _FsIpPrefixListSequence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsIpPrefixListSequence_Type.__name__=_F
_FsIpPrefixListSequence_Object=MibTableColumn
fsIpPrefixListSequence=_FsIpPrefixListSequence_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,1,1,2),_FsIpPrefixListSequence_Type())
fsIpPrefixListSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpPrefixListSequence.setStatus(_B)
class _FsIpPrefixListOperMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),('deny',2)))
_FsIpPrefixListOperMethod_Type.__name__=_E
_FsIpPrefixListOperMethod_Object=MibTableColumn
fsIpPrefixListOperMethod=_FsIpPrefixListOperMethod_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,1,1,3),_FsIpPrefixListOperMethod_Type())
fsIpPrefixListOperMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpPrefixListOperMethod.setStatus(_B)
_FsIpPrefixListIpAddress_Type=IpAddress
_FsIpPrefixListIpAddress_Object=MibTableColumn
fsIpPrefixListIpAddress=_FsIpPrefixListIpAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,1,1,4),_FsIpPrefixListIpAddress_Type())
fsIpPrefixListIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpPrefixListIpAddress.setStatus(_B)
class _FsIpPrefixListMaskLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_FsIpPrefixListMaskLength_Type.__name__=_F
_FsIpPrefixListMaskLength_Object=MibTableColumn
fsIpPrefixListMaskLength=_FsIpPrefixListMaskLength_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,1,1,5),_FsIpPrefixListMaskLength_Type())
fsIpPrefixListMaskLength.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpPrefixListMaskLength.setStatus(_B)
class _FsIpPrefixListMinimumPrefixLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_FsIpPrefixListMinimumPrefixLength_Type.__name__=_F
_FsIpPrefixListMinimumPrefixLength_Object=MibTableColumn
fsIpPrefixListMinimumPrefixLength=_FsIpPrefixListMinimumPrefixLength_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,1,1,6),_FsIpPrefixListMinimumPrefixLength_Type())
fsIpPrefixListMinimumPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpPrefixListMinimumPrefixLength.setStatus(_B)
class _FsIpPrefixListMaximumPrefixLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_FsIpPrefixListMaximumPrefixLength_Type.__name__=_F
_FsIpPrefixListMaximumPrefixLength_Object=MibTableColumn
fsIpPrefixListMaximumPrefixLength=_FsIpPrefixListMaximumPrefixLength_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,1,1,7),_FsIpPrefixListMaximumPrefixLength_Type())
fsIpPrefixListMaximumPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpPrefixListMaximumPrefixLength.setStatus(_B)
_FsIpPrefixListStatus_Type=RowStatus
_FsIpPrefixListStatus_Object=MibTableColumn
fsIpPrefixListStatus=_FsIpPrefixListStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,1,1,8),_FsIpPrefixListStatus_Type())
fsIpPrefixListStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpPrefixListStatus.setStatus(_B)
_FsDistributeListTable_Object=MibTable
fsDistributeListTable=_FsDistributeListTable_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,2))
if mibBuilder.loadTexts:fsDistributeListTable.setStatus(_B)
_FsDistributeListEntry_Object=MibTableRow
fsDistributeListEntry=_FsDistributeListEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,2,1))
fsDistributeListEntry.setIndexNames((0,_A,_Y),(0,_A,_Z),(0,_A,_a),(0,_A,_b))
if mibBuilder.loadTexts:fsDistributeListEntry.setStatus(_B)
_FsDistributeListCfgProtoType_Type=FSRouteProtoType
_FsDistributeListCfgProtoType_Object=MibTableColumn
fsDistributeListCfgProtoType=_FsDistributeListCfgProtoType_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,2,1,1),_FsDistributeListCfgProtoType_Type())
fsDistributeListCfgProtoType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDistributeListCfgProtoType.setStatus(_B)
_FsDistributeListIfIndex_Type=Unsigned32
_FsDistributeListIfIndex_Object=MibTableColumn
fsDistributeListIfIndex=_FsDistributeListIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,2,1,2),_FsDistributeListIfIndex_Type())
fsDistributeListIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDistributeListIfIndex.setStatus(_B)
class _FsDistributeListDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('out',1),('in',2)))
_FsDistributeListDirection_Type.__name__=_E
_FsDistributeListDirection_Object=MibTableColumn
fsDistributeListDirection=_FsDistributeListDirection_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,2,1,3),_FsDistributeListDirection_Type())
fsDistributeListDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDistributeListDirection.setStatus(_B)
_FsDistributeListFilteringProtocol_Type=Unsigned32
_FsDistributeListFilteringProtocol_Object=MibTableColumn
fsDistributeListFilteringProtocol=_FsDistributeListFilteringProtocol_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,2,1,4),_FsDistributeListFilteringProtocol_Type())
fsDistributeListFilteringProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDistributeListFilteringProtocol.setStatus(_B)
class _FsDistributeListFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('acl',1),('gateway',2),('prefix',3),('prefix-gateway',4)))
_FsDistributeListFilterType_Type.__name__=_E
_FsDistributeListFilterType_Object=MibTableColumn
fsDistributeListFilterType=_FsDistributeListFilterType_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,2,1,5),_FsDistributeListFilterType_Type())
fsDistributeListFilterType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDistributeListFilterType.setStatus(_B)
class _FsDistributeListAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsDistributeListAclName_Type.__name__=_G
_FsDistributeListAclName_Object=MibTableColumn
fsDistributeListAclName=_FsDistributeListAclName_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,2,1,6),_FsDistributeListAclName_Type())
fsDistributeListAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDistributeListAclName.setStatus(_B)
class _FsDistributeListGateWayIpPrefixName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsDistributeListGateWayIpPrefixName_Type.__name__=_G
_FsDistributeListGateWayIpPrefixName_Object=MibTableColumn
fsDistributeListGateWayIpPrefixName=_FsDistributeListGateWayIpPrefixName_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,2,1,7),_FsDistributeListGateWayIpPrefixName_Type())
fsDistributeListGateWayIpPrefixName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDistributeListGateWayIpPrefixName.setStatus(_B)
class _FsDistributeListPrefixIpPrefixName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsDistributeListPrefixIpPrefixName_Type.__name__=_G
_FsDistributeListPrefixIpPrefixName_Object=MibTableColumn
fsDistributeListPrefixIpPrefixName=_FsDistributeListPrefixIpPrefixName_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,2,1,8),_FsDistributeListPrefixIpPrefixName_Type())
fsDistributeListPrefixIpPrefixName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDistributeListPrefixIpPrefixName.setStatus(_B)
_FsDistributeListStatus_Type=RowStatus
_FsDistributeListStatus_Object=MibTableColumn
fsDistributeListStatus=_FsDistributeListStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,20,4,2,1,9),_FsDistributeListStatus_Type())
fsDistributeListStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDistributeListStatus.setStatus(_B)
_FsipCidrRouteExtendMIBObjects_ObjectIdentity=ObjectIdentity
fsipCidrRouteExtendMIBObjects=_FsipCidrRouteExtendMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,20,5))
_FsipCidrRouteTable_Object=MibTable
fsipCidrRouteTable=_FsipCidrRouteTable_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1))
if mibBuilder.loadTexts:fsipCidrRouteTable.setStatus(_B)
_FsipCidrRouteEntry_Object=MibTableRow
fsipCidrRouteEntry=_FsipCidrRouteEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1))
fsipCidrRouteEntry.setIndexNames((0,_A,_c),(0,_A,_d),(0,_A,_e),(0,_A,_f))
if mibBuilder.loadTexts:fsipCidrRouteEntry.setStatus(_B)
_FsipCidrRouteDest_Type=IpAddress
_FsipCidrRouteDest_Object=MibTableColumn
fsipCidrRouteDest=_FsipCidrRouteDest_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,1),_FsipCidrRouteDest_Type())
fsipCidrRouteDest.setMaxAccess(_D)
if mibBuilder.loadTexts:fsipCidrRouteDest.setStatus(_B)
_FsipCidrRouteMask_Type=IpAddress
_FsipCidrRouteMask_Object=MibTableColumn
fsipCidrRouteMask=_FsipCidrRouteMask_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,2),_FsipCidrRouteMask_Type())
fsipCidrRouteMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fsipCidrRouteMask.setStatus(_B)
_FsipCidrRouteTos_Type=Integer32
_FsipCidrRouteTos_Object=MibTableColumn
fsipCidrRouteTos=_FsipCidrRouteTos_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,3),_FsipCidrRouteTos_Type())
fsipCidrRouteTos.setMaxAccess(_D)
if mibBuilder.loadTexts:fsipCidrRouteTos.setStatus(_B)
_FsipCidrRouteNextHop_Type=IpAddress
_FsipCidrRouteNextHop_Object=MibTableColumn
fsipCidrRouteNextHop=_FsipCidrRouteNextHop_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,4),_FsipCidrRouteNextHop_Type())
fsipCidrRouteNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:fsipCidrRouteNextHop.setStatus(_B)
class _FsipCidrRouteIfIndex_Type(Integer32):defaultValue=0
_FsipCidrRouteIfIndex_Type.__name__=_E
_FsipCidrRouteIfIndex_Object=MibTableColumn
fsipCidrRouteIfIndex=_FsipCidrRouteIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,5),_FsipCidrRouteIfIndex_Type())
fsipCidrRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipCidrRouteIfIndex.setStatus(_B)
class _FsipCidrRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('reject',2),(_K,3),('remote',4)))
_FsipCidrRouteType_Type.__name__=_E
_FsipCidrRouteType_Object=MibTableColumn
fsipCidrRouteType=_FsipCidrRouteType_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,6),_FsipCidrRouteType_Type())
fsipCidrRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipCidrRouteType.setStatus(_B)
class _FsipCidrRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_J,1),(_K,2),(_j,3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('isIs',9),('esIs',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14),('idpr',15),('ciscoEigrp',16),('policy',17)))
_FsipCidrRouteProto_Type.__name__=_E
_FsipCidrRouteProto_Object=MibTableColumn
fsipCidrRouteProto=_FsipCidrRouteProto_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,7),_FsipCidrRouteProto_Type())
fsipCidrRouteProto.setMaxAccess(_D)
if mibBuilder.loadTexts:fsipCidrRouteProto.setStatus(_B)
class _FsipCidrRouteAge_Type(Integer32):defaultValue=0
_FsipCidrRouteAge_Type.__name__=_E
_FsipCidrRouteAge_Object=MibTableColumn
fsipCidrRouteAge=_FsipCidrRouteAge_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,8),_FsipCidrRouteAge_Type())
fsipCidrRouteAge.setMaxAccess(_D)
if mibBuilder.loadTexts:fsipCidrRouteAge.setStatus(_B)
_FsipCidrRouteInfo_Type=ObjectIdentifier
_FsipCidrRouteInfo_Object=MibTableColumn
fsipCidrRouteInfo=_FsipCidrRouteInfo_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,9),_FsipCidrRouteInfo_Type())
fsipCidrRouteInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipCidrRouteInfo.setStatus(_B)
class _FsipCidrRouteNextHopAS_Type(Integer32):defaultValue=0
_FsipCidrRouteNextHopAS_Type.__name__=_E
_FsipCidrRouteNextHopAS_Object=MibTableColumn
fsipCidrRouteNextHopAS=_FsipCidrRouteNextHopAS_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,10),_FsipCidrRouteNextHopAS_Type())
fsipCidrRouteNextHopAS.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipCidrRouteNextHopAS.setStatus(_B)
class _FsipCidrRouteMetric1_Type(Integer32):defaultValue=-1
_FsipCidrRouteMetric1_Type.__name__=_E
_FsipCidrRouteMetric1_Object=MibTableColumn
fsipCidrRouteMetric1=_FsipCidrRouteMetric1_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,11),_FsipCidrRouteMetric1_Type())
fsipCidrRouteMetric1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipCidrRouteMetric1.setStatus(_B)
class _FsipCidrRouteMetric2_Type(Integer32):defaultValue=-1
_FsipCidrRouteMetric2_Type.__name__=_E
_FsipCidrRouteMetric2_Object=MibTableColumn
fsipCidrRouteMetric2=_FsipCidrRouteMetric2_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,12),_FsipCidrRouteMetric2_Type())
fsipCidrRouteMetric2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipCidrRouteMetric2.setStatus(_B)
class _FsipCidrRouteMetric3_Type(Integer32):defaultValue=-1
_FsipCidrRouteMetric3_Type.__name__=_E
_FsipCidrRouteMetric3_Object=MibTableColumn
fsipCidrRouteMetric3=_FsipCidrRouteMetric3_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,13),_FsipCidrRouteMetric3_Type())
fsipCidrRouteMetric3.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipCidrRouteMetric3.setStatus(_B)
class _FsipCidrRouteMetric4_Type(Integer32):defaultValue=-1
_FsipCidrRouteMetric4_Type.__name__=_E
_FsipCidrRouteMetric4_Object=MibTableColumn
fsipCidrRouteMetric4=_FsipCidrRouteMetric4_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,14),_FsipCidrRouteMetric4_Type())
fsipCidrRouteMetric4.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipCidrRouteMetric4.setStatus(_B)
class _FsipCidrRouteMetric5_Type(Integer32):defaultValue=-1
_FsipCidrRouteMetric5_Type.__name__=_E
_FsipCidrRouteMetric5_Object=MibTableColumn
fsipCidrRouteMetric5=_FsipCidrRouteMetric5_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,15),_FsipCidrRouteMetric5_Type())
fsipCidrRouteMetric5.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipCidrRouteMetric5.setStatus(_B)
_FsipCidrRouteStatus_Type=RowStatus
_FsipCidrRouteStatus_Object=MibTableColumn
fsipCidrRouteStatus=_FsipCidrRouteStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,16),_FsipCidrRouteStatus_Type())
fsipCidrRouteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsipCidrRouteStatus.setStatus(_B)
class _FsipCidrOspfRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('ospf-route',0),('ospf-ia-route',1),('ospf-n1-route',2),('ospf-n2-route',3),('ospf-e1-route',4),('ospf-e2-route',5)))
_FsipCidrOspfRouteType_Type.__name__=_E
_FsipCidrOspfRouteType_Object=MibTableColumn
fsipCidrOspfRouteType=_FsipCidrOspfRouteType_Object((1,3,6,1,4,1,52642,1,1,10,2,20,5,1,1,17),_FsipCidrOspfRouteType_Type())
fsipCidrOspfRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsipCidrOspfRouteType.setStatus(_B)
_FsRouteMIBConformance_ObjectIdentity=ObjectIdentity
fsRouteMIBConformance=_FsRouteMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,20,6))
_FsRouteMIBCompliances_ObjectIdentity=ObjectIdentity
fsRouteMIBCompliances=_FsRouteMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,20,6,1))
_FsRouteMIBGroups_ObjectIdentity=ObjectIdentity
fsRouteMIBGroups=_FsRouteMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,20,6,2))
fsRouteMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,20,6,2,1))
fsRouteMIBGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:fsRouteMIBGroup.setStatus(_B)
fsRouteInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,20,6,2,2))
fsRouteInfoMIBGroup.setObjects(*((_A,_L),(_A,_M),(_A,_p),(_A,_q),(_A,_N),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:fsRouteInfoMIBGroup.setStatus(_B)
fsRouteMapMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,20,6,2,3))
fsRouteMapMIBGroup.setObjects(*((_A,_H),(_A,_I),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_g),(_A,_g),(_A,_A3),(_A,_R),(_A,_Q),(_A,_A4),(_A,_S),(_A,_A5),(_A,_T),(_A,_A6)))
if mibBuilder.loadTexts:fsRouteMapMIBGroup.setStatus(_B)
fsRouteRedistributeMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,20,6,2,4))
fsRouteRedistributeMIBGroup.setObjects(*((_A,_U),(_A,_V),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:fsRouteRedistributeMIBGroup.setStatus(_B)
fsRouteFilteringMibGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,20,6,2,5))
fsRouteFilteringMibGroup.setObjects(*((_A,_W),(_A,_X),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_Y),(_A,_Z),(_A,_AI),(_A,_a),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_b),(_A,_AM)))
if mibBuilder.loadTexts:fsRouteFilteringMibGroup.setStatus(_B)
fsipCidrRouteMibGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,20,6,2,6))
fsipCidrRouteMibGroup.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:fsipCidrRouteMibGroup.setStatus(_B)
fsRouteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,20,6,1,1))
fsRouteMIBCompliance.setObjects(*((_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:fsRouteMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'FSRouteProtoType':FSRouteProtoType,'fsRouteMIB':fsRouteMIB,'fsRouteMIBObjects':fsRouteMIBObjects,_o:fsRouteServiceStatus,'fsRoutingProtoInfoTable':fsRoutingProtoInfoTable,'fsRoutingProtoInfoEntry':fsRoutingProtoInfoEntry,_L:fsRoutingProtoInfoProtoType,_M:fsRoutingProtoInfoGateWay,_p:fsRoutingProtoInfoDistance,_q:fsRoutingProtoInfoLastUpdate,'fsDefRoutingCfgTable':fsDefRoutingCfgTable,'fsDefRoutingCfgEntry':fsDefRoutingCfgEntry,_N:fsDefRoutingCfgRoutingProtoType,_r:fsDefRoutingCfgAlways,_s:fsDefRoutingCfgMetric,_t:fsDefRoutingCfgMetricType,_u:fsDefRoutingCfgRouteMap,_v:fsDefRoutingCfgStatus,'fsRouteMapMIBObjects':fsRouteMapMIBObjects,'fsRouteMapTable':fsRouteMapTable,'fsRouteMapEntry':fsRouteMapEntry,_H:fsRouteMapName,_I:fsRouteMapSequenceNumber,_w:fsRouteMapOperType,_x:fsRouteMapMatchMetric,_y:fsRouteMapMatchRouteType,_z:fsRouteMapMetricValueType,_A0:fsRouteMapSetMetric,_A1:fsRouteMapSetLevel,_A2:fsRouteMapSetMetricType,_g:fsRouteMapSetNexthopSt,'fsRouteMapSetNexthop':fsRouteMapSetNexthop,_A3:fsRouteMapStatus,'fsRouteMapMatchIpAddressTable':fsRouteMapMatchIpAddressTable,'fsRouteMapMatchIpAddressEntry':fsRouteMapMatchIpAddressEntry,_Q:fsRouteMapMatchType,_R:fsRouteMapMatchIpAddressAclName,_A4:fsRouteMapMatchIpAddressStatus,'fsRouteMapMatchTagTable':fsRouteMapMatchTagTable,'fsRouteMapMatchTagEntry':fsRouteMapMatchTagEntry,_S:fsRouteMapMatchTagValue,_A5:fsRouteMapMatchTagStatus,'fsRouteMapMatchInterfaceTable':fsRouteMapMatchInterfaceTable,'fsRouteMapMatchInterfaceEntry':fsRouteMapMatchInterfaceEntry,_T:fsRouteMapMatchInterfaceIfIndex,_A6:fsRouteMapMatchInterfaceStatus,'fsRouteRedistributeMIBObjects':fsRouteRedistributeMIBObjects,'fsRouteRedistributeTable':fsRouteRedistributeTable,'fsRouteRedistributeEntry':fsRouteRedistributeEntry,_U:fsRouteRedistributeProtocolCfg,_V:fsRouteRedistributeProtocol,_A7:fsRouteRedistributeMetricValue,_A8:fsRouteRedistributeMetricType,_A9:fsRouteRedistributeTagValue,_AA:fsRouteRedistributeRouteMapName,_AB:fsRouteRedistributeStatus,'fsRouteFilteringMIBObjects':fsRouteFilteringMIBObjects,'fsIpPrefixListTable':fsIpPrefixListTable,'fsIpPrefixListEntry':fsIpPrefixListEntry,_W:fsIpPrefixListName,_X:fsIpPrefixListSequence,_AC:fsIpPrefixListOperMethod,_AD:fsIpPrefixListIpAddress,_AE:fsIpPrefixListMaskLength,_AF:fsIpPrefixListMinimumPrefixLength,_AG:fsIpPrefixListMaximumPrefixLength,_AH:fsIpPrefixListStatus,'fsDistributeListTable':fsDistributeListTable,'fsDistributeListEntry':fsDistributeListEntry,_Y:fsDistributeListCfgProtoType,_Z:fsDistributeListIfIndex,_a:fsDistributeListDirection,_b:fsDistributeListFilteringProtocol,_AI:fsDistributeListFilterType,_AJ:fsDistributeListAclName,_AK:fsDistributeListGateWayIpPrefixName,_AL:fsDistributeListPrefixIpPrefixName,_AM:fsDistributeListStatus,'fsipCidrRouteExtendMIBObjects':fsipCidrRouteExtendMIBObjects,'fsipCidrRouteTable':fsipCidrRouteTable,'fsipCidrRouteEntry':fsipCidrRouteEntry,_c:fsipCidrRouteDest,_d:fsipCidrRouteMask,_e:fsipCidrRouteTos,_f:fsipCidrRouteNextHop,_AN:fsipCidrRouteIfIndex,_AO:fsipCidrRouteType,_AP:fsipCidrRouteProto,_AQ:fsipCidrRouteAge,_AR:fsipCidrRouteInfo,_AS:fsipCidrRouteNextHopAS,_AT:fsipCidrRouteMetric1,_AU:fsipCidrRouteMetric2,_AV:fsipCidrRouteMetric3,_AW:fsipCidrRouteMetric4,_AX:fsipCidrRouteMetric5,_AY:fsipCidrRouteStatus,_AZ:fsipCidrOspfRouteType,'fsRouteMIBConformance':fsRouteMIBConformance,'fsRouteMIBCompliances':fsRouteMIBCompliances,'fsRouteMIBCompliance':fsRouteMIBCompliance,'fsRouteMIBGroups':fsRouteMIBGroups,_Aa:fsRouteMIBGroup,_Ab:fsRouteInfoMIBGroup,_Ac:fsRouteMapMIBGroup,_Ad:fsRouteRedistributeMIBGroup,_Ae:fsRouteFilteringMibGroup,_Af:fsipCidrRouteMibGroup})