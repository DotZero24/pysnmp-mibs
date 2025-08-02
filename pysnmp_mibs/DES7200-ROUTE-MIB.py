_Ag='myipCidrRouteMibGroup'
_Af='myRouteFilteringMibGroup'
_Ae='myRouteRedistributeMIBGroup'
_Ad='myRouteMapMIBGroup'
_Ac='myRouteInfoMIBGroup'
_Ab='myRouteMIBGroup'
_Aa='myipCidrOspfRouteType'
_AZ='myipCidrRouteStatus'
_AY='myipCidrRouteMetric5'
_AX='myipCidrRouteMetric4'
_AW='myipCidrRouteMetric3'
_AV='myipCidrRouteMetric2'
_AU='myipCidrRouteMetric1'
_AT='myipCidrRouteNextHopAS'
_AS='myipCidrRouteInfo'
_AR='myipCidrRouteAge'
_AQ='myipCidrRouteProto'
_AP='myipCidrRouteType'
_AO='myipCidrRouteIfIndex'
_AN='myDistributeListStatus'
_AM='myDistributeListPrefixIpPrefixName'
_AL='myDistributeListGateWayIpPrefixName'
_AK='myDistributeListAclName'
_AJ='myDistributeListFilterType'
_AI='myIpPrefixListStatus'
_AH='myIpPrefixListMaximumPrefixLength'
_AG='myIpPrefixListMinimumPrefixLength'
_AF='myIpPrefixListMaskLength'
_AE='myIpPrefixListIpAddress'
_AD='myIpPrefixListOperMethod'
_AC='myRouteRedistributeStatus'
_AB='myRouteRedistributeRouteMapName'
_AA='myRouteRedistributeTagValue'
_A9='myRouteRedistributeMetricType'
_A8='myRouteRedistributeMetricValue'
_A7='myRouteMapMatchInterfaceStatus'
_A6='myRouteMapMatchTagStatus'
_A5='myRouteMapMatchIpAddressStatus'
_A4='myRouteMapStatus'
_A3='myRouteMapSetMetricType'
_A2='myRouteMapSetLevel'
_A1='myRouteMapSetMetric'
_A0='myRouteMapMetricValueType'
_z='myRouteMapMatchRouteType'
_y='myRouteMapMatchMetric'
_x='myRouteMapOperType'
_w='myDefRoutingCfgStatus'
_v='myDefRoutingCfgRouteMap'
_u='myDefRoutingCfgMetricType'
_t='myDefRoutingCfgMetric'
_s='myDefRoutingCfgAlways'
_r='myRoutingProtoInfoLastUpdate'
_q='myRoutingProtoInfoDistance'
_p='myRouteServiceStatus'
_o='noOper'
_n='external'
_m='internal'
_l='permit'
_k='netmgmt'
_j='TruthValue'
_i='ConfigStatus'
_h='myRouteMapSetNexthopSt'
_g='myipCidrRouteNextHop'
_f='myipCidrRouteTos'
_e='myipCidrRouteMask'
_d='myipCidrRouteDest'
_c='myDistributeListFilteringProtocol'
_b='myDistributeListDirection'
_a='myDistributeListIfIndex'
_Z='myDistributeListCfgProtoType'
_Y='myIpPrefixListSequence'
_X='myIpPrefixListName'
_W='myRouteRedistributeProtocol'
_V='myRouteRedistributeProtocolCfg'
_U='myRouteMapMatchInterfaceIfIndex'
_T='myRouteMapMatchTagValue'
_S='myRouteMapMatchIpAddressAclName'
_R='myRouteMapMatchType'
_Q='type2'
_P='type1'
_O='myDefRoutingCfgRoutingProtoType'
_N='myRoutingProtoInfoGateWay'
_M='myRoutingProtoInfoProtoType'
_L='local'
_K='other'
_J='myRouteMapSequenceNumber'
_I='myRouteMapName'
_H='DisplayString'
_G='read-write'
_F='Unsigned32'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='current'
_A='DES7200-ROUTE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('DES7200-TC',_i,'IfIndex')
BigMetric,=mibBuilder.importSymbols('OSPF-MIB','BigMetric')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention',_j)
myRouteMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,20))
if mibBuilder.loadTexts:myRouteMIB.setRevisions(('2002-03-20 00:00',))
class MyRouteProtoType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_K,1),(_L,2),(_k,3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('isis',9),('esis',10),('ciscoigrp',11),('bbnspfigp',12),('ospf',13),('bgp',14),('idpr',15),('ciscoeigrp',16),('max',17)))
_MyRouteMIBObjects_ObjectIdentity=ObjectIdentity
myRouteMIBObjects=_MyRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,20,1))
_MyRouteServiceStatus_Type=EnabledStatus
_MyRouteServiceStatus_Object=MibScalar
myRouteServiceStatus=_MyRouteServiceStatus_Object((1,3,6,1,4,1,171,10,97,2,20,1,1),_MyRouteServiceStatus_Type())
myRouteServiceStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:myRouteServiceStatus.setStatus(_B)
_MyRoutingProtoInfoTable_Object=MibTable
myRoutingProtoInfoTable=_MyRoutingProtoInfoTable_Object((1,3,6,1,4,1,171,10,97,2,20,1,2))
if mibBuilder.loadTexts:myRoutingProtoInfoTable.setStatus(_B)
_MyRoutingProtoInfoEntry_Object=MibTableRow
myRoutingProtoInfoEntry=_MyRoutingProtoInfoEntry_Object((1,3,6,1,4,1,171,10,97,2,20,1,2,1))
myRoutingProtoInfoEntry.setIndexNames((0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:myRoutingProtoInfoEntry.setStatus(_B)
_MyRoutingProtoInfoProtoType_Type=MyRouteProtoType
_MyRoutingProtoInfoProtoType_Object=MibTableColumn
myRoutingProtoInfoProtoType=_MyRoutingProtoInfoProtoType_Object((1,3,6,1,4,1,171,10,97,2,20,1,2,1,1),_MyRoutingProtoInfoProtoType_Type())
myRoutingProtoInfoProtoType.setMaxAccess(_D)
if mibBuilder.loadTexts:myRoutingProtoInfoProtoType.setStatus(_B)
_MyRoutingProtoInfoGateWay_Type=IpAddress
_MyRoutingProtoInfoGateWay_Object=MibTableColumn
myRoutingProtoInfoGateWay=_MyRoutingProtoInfoGateWay_Object((1,3,6,1,4,1,171,10,97,2,20,1,2,1,2),_MyRoutingProtoInfoGateWay_Type())
myRoutingProtoInfoGateWay.setMaxAccess(_D)
if mibBuilder.loadTexts:myRoutingProtoInfoGateWay.setStatus(_B)
_MyRoutingProtoInfoDistance_Type=Unsigned32
_MyRoutingProtoInfoDistance_Object=MibTableColumn
myRoutingProtoInfoDistance=_MyRoutingProtoInfoDistance_Object((1,3,6,1,4,1,171,10,97,2,20,1,2,1,3),_MyRoutingProtoInfoDistance_Type())
myRoutingProtoInfoDistance.setMaxAccess(_D)
if mibBuilder.loadTexts:myRoutingProtoInfoDistance.setStatus(_B)
_MyRoutingProtoInfoLastUpdate_Type=TimeTicks
_MyRoutingProtoInfoLastUpdate_Object=MibTableColumn
myRoutingProtoInfoLastUpdate=_MyRoutingProtoInfoLastUpdate_Object((1,3,6,1,4,1,171,10,97,2,20,1,2,1,4),_MyRoutingProtoInfoLastUpdate_Type())
myRoutingProtoInfoLastUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:myRoutingProtoInfoLastUpdate.setStatus(_B)
_MyDefRoutingCfgTable_Object=MibTable
myDefRoutingCfgTable=_MyDefRoutingCfgTable_Object((1,3,6,1,4,1,171,10,97,2,20,1,3))
if mibBuilder.loadTexts:myDefRoutingCfgTable.setStatus(_B)
_MyDefRoutingCfgEntry_Object=MibTableRow
myDefRoutingCfgEntry=_MyDefRoutingCfgEntry_Object((1,3,6,1,4,1,171,10,97,2,20,1,3,1))
myDefRoutingCfgEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:myDefRoutingCfgEntry.setStatus(_B)
_MyDefRoutingCfgRoutingProtoType_Type=MyRouteProtoType
_MyDefRoutingCfgRoutingProtoType_Object=MibTableColumn
myDefRoutingCfgRoutingProtoType=_MyDefRoutingCfgRoutingProtoType_Object((1,3,6,1,4,1,171,10,97,2,20,1,3,1,1),_MyDefRoutingCfgRoutingProtoType_Type())
myDefRoutingCfgRoutingProtoType.setMaxAccess(_D)
if mibBuilder.loadTexts:myDefRoutingCfgRoutingProtoType.setStatus(_B)
class _MyDefRoutingCfgAlways_Type(TruthValue):defaultValue=2
_MyDefRoutingCfgAlways_Type.__name__=_j
_MyDefRoutingCfgAlways_Object=MibTableColumn
myDefRoutingCfgAlways=_MyDefRoutingCfgAlways_Object((1,3,6,1,4,1,171,10,97,2,20,1,3,1,2),_MyDefRoutingCfgAlways_Type())
myDefRoutingCfgAlways.setMaxAccess(_C)
if mibBuilder.loadTexts:myDefRoutingCfgAlways.setStatus(_B)
class _MyDefRoutingCfgMetric_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777214))
_MyDefRoutingCfgMetric_Type.__name__=_F
_MyDefRoutingCfgMetric_Object=MibTableColumn
myDefRoutingCfgMetric=_MyDefRoutingCfgMetric_Object((1,3,6,1,4,1,171,10,97,2,20,1,3,1,3),_MyDefRoutingCfgMetric_Type())
myDefRoutingCfgMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:myDefRoutingCfgMetric.setStatus(_B)
class _MyDefRoutingCfgMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_MyDefRoutingCfgMetricType_Type.__name__=_E
_MyDefRoutingCfgMetricType_Object=MibTableColumn
myDefRoutingCfgMetricType=_MyDefRoutingCfgMetricType_Object((1,3,6,1,4,1,171,10,97,2,20,1,3,1,4),_MyDefRoutingCfgMetricType_Type())
myDefRoutingCfgMetricType.setMaxAccess(_G)
if mibBuilder.loadTexts:myDefRoutingCfgMetricType.setStatus(_B)
class _MyDefRoutingCfgRouteMap_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MyDefRoutingCfgRouteMap_Type.__name__=_H
_MyDefRoutingCfgRouteMap_Object=MibTableColumn
myDefRoutingCfgRouteMap=_MyDefRoutingCfgRouteMap_Object((1,3,6,1,4,1,171,10,97,2,20,1,3,1,5),_MyDefRoutingCfgRouteMap_Type())
myDefRoutingCfgRouteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:myDefRoutingCfgRouteMap.setStatus(_B)
_MyDefRoutingCfgStatus_Type=RowStatus
_MyDefRoutingCfgStatus_Object=MibTableColumn
myDefRoutingCfgStatus=_MyDefRoutingCfgStatus_Object((1,3,6,1,4,1,171,10,97,2,20,1,3,1,6),_MyDefRoutingCfgStatus_Type())
myDefRoutingCfgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myDefRoutingCfgStatus.setStatus(_B)
_MyRouteMapMIBObjects_ObjectIdentity=ObjectIdentity
myRouteMapMIBObjects=_MyRouteMapMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,20,2))
_MyRouteMapTable_Object=MibTable
myRouteMapTable=_MyRouteMapTable_Object((1,3,6,1,4,1,171,10,97,2,20,2,1))
if mibBuilder.loadTexts:myRouteMapTable.setStatus(_B)
_MyRouteMapEntry_Object=MibTableRow
myRouteMapEntry=_MyRouteMapEntry_Object((1,3,6,1,4,1,171,10,97,2,20,2,1,1))
myRouteMapEntry.setIndexNames((0,_A,_I),(0,_A,_J))
if mibBuilder.loadTexts:myRouteMapEntry.setStatus(_B)
class _MyRouteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyRouteMapName_Type.__name__=_H
_MyRouteMapName_Object=MibTableColumn
myRouteMapName=_MyRouteMapName_Object((1,3,6,1,4,1,171,10,97,2,20,2,1,1,1),_MyRouteMapName_Type())
myRouteMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:myRouteMapName.setStatus(_B)
class _MyRouteMapSequenceNumber_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MyRouteMapSequenceNumber_Type.__name__=_F
_MyRouteMapSequenceNumber_Object=MibTableColumn
myRouteMapSequenceNumber=_MyRouteMapSequenceNumber_Object((1,3,6,1,4,1,171,10,97,2,20,2,1,1,2),_MyRouteMapSequenceNumber_Type())
myRouteMapSequenceNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:myRouteMapSequenceNumber.setStatus(_B)
class _MyRouteMapOperType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),('deny',2)))
_MyRouteMapOperType_Type.__name__=_E
_MyRouteMapOperType_Object=MibTableColumn
myRouteMapOperType=_MyRouteMapOperType_Object((1,3,6,1,4,1,171,10,97,2,20,2,1,1,3),_MyRouteMapOperType_Type())
myRouteMapOperType.setMaxAccess(_D)
if mibBuilder.loadTexts:myRouteMapOperType.setStatus(_B)
class _MyRouteMapMatchMetric_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MyRouteMapMatchMetric_Type.__name__=_F
_MyRouteMapMatchMetric_Object=MibTableColumn
myRouteMapMatchMetric=_MyRouteMapMatchMetric_Object((1,3,6,1,4,1,171,10,97,2,20,2,1,1,4),_MyRouteMapMatchMetric_Type())
myRouteMapMatchMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteMapMatchMetric.setStatus(_B)
class _MyRouteMapMatchRouteType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('notMatch',0),(_m,1),(_n,2),('external-type1',3),('external-type2',4)))
_MyRouteMapMatchRouteType_Type.__name__=_E
_MyRouteMapMatchRouteType_Object=MibTableColumn
myRouteMapMatchRouteType=_MyRouteMapMatchRouteType_Object((1,3,6,1,4,1,171,10,97,2,20,2,1,1,5),_MyRouteMapMatchRouteType_Type())
myRouteMapMatchRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteMapMatchRouteType.setStatus(_B)
class _MyRouteMapMetricValueType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_o,0),('replace',1),('add',2),('reduce',3)))
_MyRouteMapMetricValueType_Type.__name__=_E
_MyRouteMapMetricValueType_Object=MibTableColumn
myRouteMapMetricValueType=_MyRouteMapMetricValueType_Object((1,3,6,1,4,1,171,10,97,2,20,2,1,1,6),_MyRouteMapMetricValueType_Type())
myRouteMapMetricValueType.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteMapMetricValueType.setStatus(_B)
class _MyRouteMapSetMetric_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MyRouteMapSetMetric_Type.__name__=_F
_MyRouteMapSetMetric_Object=MibTableColumn
myRouteMapSetMetric=_MyRouteMapSetMetric_Object((1,3,6,1,4,1,171,10,97,2,20,2,1,1,7),_MyRouteMapSetMetric_Type())
myRouteMapSetMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteMapSetMetric.setStatus(_B)
class _MyRouteMapSetLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('all',0),('stubarea',1),('backbone',2)))
_MyRouteMapSetLevel_Type.__name__=_E
_MyRouteMapSetLevel_Object=MibTableColumn
myRouteMapSetLevel=_MyRouteMapSetLevel_Object((1,3,6,1,4,1,171,10,97,2,20,2,1,1,8),_MyRouteMapSetLevel_Type())
myRouteMapSetLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteMapSetLevel.setStatus(_B)
class _MyRouteMapSetMetricType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_o,0),(_m,1),(_n,2),(_P,3),(_Q,4)))
_MyRouteMapSetMetricType_Type.__name__=_E
_MyRouteMapSetMetricType_Object=MibTableColumn
myRouteMapSetMetricType=_MyRouteMapSetMetricType_Object((1,3,6,1,4,1,171,10,97,2,20,2,1,1,9),_MyRouteMapSetMetricType_Type())
myRouteMapSetMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteMapSetMetricType.setStatus(_B)
class _MyRouteMapSetNexthopSt_Type(ConfigStatus):defaultValue=2
_MyRouteMapSetNexthopSt_Type.__name__=_i
_MyRouteMapSetNexthopSt_Object=MibTableColumn
myRouteMapSetNexthopSt=_MyRouteMapSetNexthopSt_Object((1,3,6,1,4,1,171,10,97,2,20,2,1,1,10),_MyRouteMapSetNexthopSt_Type())
myRouteMapSetNexthopSt.setMaxAccess(_G)
if mibBuilder.loadTexts:myRouteMapSetNexthopSt.setStatus(_B)
_MyRouteMapSetNexthop_Type=IpAddress
_MyRouteMapSetNexthop_Object=MibTableColumn
myRouteMapSetNexthop=_MyRouteMapSetNexthop_Object((1,3,6,1,4,1,171,10,97,2,20,2,1,1,11),_MyRouteMapSetNexthop_Type())
myRouteMapSetNexthop.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteMapSetNexthop.setStatus(_B)
_MyRouteMapStatus_Type=RowStatus
_MyRouteMapStatus_Object=MibTableColumn
myRouteMapStatus=_MyRouteMapStatus_Object((1,3,6,1,4,1,171,10,97,2,20,2,1,1,12),_MyRouteMapStatus_Type())
myRouteMapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteMapStatus.setStatus(_B)
_MyRouteMapMatchIpAddressTable_Object=MibTable
myRouteMapMatchIpAddressTable=_MyRouteMapMatchIpAddressTable_Object((1,3,6,1,4,1,171,10,97,2,20,2,2))
if mibBuilder.loadTexts:myRouteMapMatchIpAddressTable.setStatus(_B)
_MyRouteMapMatchIpAddressEntry_Object=MibTableRow
myRouteMapMatchIpAddressEntry=_MyRouteMapMatchIpAddressEntry_Object((1,3,6,1,4,1,171,10,97,2,20,2,2,1))
myRouteMapMatchIpAddressEntry.setIndexNames((0,_A,_I),(0,_A,_J),(0,_A,_R),(0,_A,_S))
if mibBuilder.loadTexts:myRouteMapMatchIpAddressEntry.setStatus(_B)
class _MyRouteMapMatchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('destination',1),('nextHop',2),('source',3)))
_MyRouteMapMatchType_Type.__name__=_E
_MyRouteMapMatchType_Object=MibTableColumn
myRouteMapMatchType=_MyRouteMapMatchType_Object((1,3,6,1,4,1,171,10,97,2,20,2,2,1,1),_MyRouteMapMatchType_Type())
myRouteMapMatchType.setMaxAccess(_D)
if mibBuilder.loadTexts:myRouteMapMatchType.setStatus(_B)
class _MyRouteMapMatchIpAddressAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyRouteMapMatchIpAddressAclName_Type.__name__=_H
_MyRouteMapMatchIpAddressAclName_Object=MibTableColumn
myRouteMapMatchIpAddressAclName=_MyRouteMapMatchIpAddressAclName_Object((1,3,6,1,4,1,171,10,97,2,20,2,2,1,2),_MyRouteMapMatchIpAddressAclName_Type())
myRouteMapMatchIpAddressAclName.setMaxAccess(_D)
if mibBuilder.loadTexts:myRouteMapMatchIpAddressAclName.setStatus(_B)
_MyRouteMapMatchIpAddressStatus_Type=RowStatus
_MyRouteMapMatchIpAddressStatus_Object=MibTableColumn
myRouteMapMatchIpAddressStatus=_MyRouteMapMatchIpAddressStatus_Object((1,3,6,1,4,1,171,10,97,2,20,2,2,1,3),_MyRouteMapMatchIpAddressStatus_Type())
myRouteMapMatchIpAddressStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteMapMatchIpAddressStatus.setStatus(_B)
_MyRouteMapMatchTagTable_Object=MibTable
myRouteMapMatchTagTable=_MyRouteMapMatchTagTable_Object((1,3,6,1,4,1,171,10,97,2,20,2,3))
if mibBuilder.loadTexts:myRouteMapMatchTagTable.setStatus(_B)
_MyRouteMapMatchTagEntry_Object=MibTableRow
myRouteMapMatchTagEntry=_MyRouteMapMatchTagEntry_Object((1,3,6,1,4,1,171,10,97,2,20,2,3,1))
myRouteMapMatchTagEntry.setIndexNames((0,_A,_I),(0,_A,_J),(0,_A,_T))
if mibBuilder.loadTexts:myRouteMapMatchTagEntry.setStatus(_B)
class _MyRouteMapMatchTagValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MyRouteMapMatchTagValue_Type.__name__=_F
_MyRouteMapMatchTagValue_Object=MibTableColumn
myRouteMapMatchTagValue=_MyRouteMapMatchTagValue_Object((1,3,6,1,4,1,171,10,97,2,20,2,3,1,1),_MyRouteMapMatchTagValue_Type())
myRouteMapMatchTagValue.setMaxAccess(_D)
if mibBuilder.loadTexts:myRouteMapMatchTagValue.setStatus(_B)
_MyRouteMapMatchTagStatus_Type=RowStatus
_MyRouteMapMatchTagStatus_Object=MibTableColumn
myRouteMapMatchTagStatus=_MyRouteMapMatchTagStatus_Object((1,3,6,1,4,1,171,10,97,2,20,2,3,1,2),_MyRouteMapMatchTagStatus_Type())
myRouteMapMatchTagStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteMapMatchTagStatus.setStatus(_B)
_MyRouteMapMatchInterfaceTable_Object=MibTable
myRouteMapMatchInterfaceTable=_MyRouteMapMatchInterfaceTable_Object((1,3,6,1,4,1,171,10,97,2,20,2,4))
if mibBuilder.loadTexts:myRouteMapMatchInterfaceTable.setStatus(_B)
_MyRouteMapMatchInterfaceEntry_Object=MibTableRow
myRouteMapMatchInterfaceEntry=_MyRouteMapMatchInterfaceEntry_Object((1,3,6,1,4,1,171,10,97,2,20,2,4,1))
myRouteMapMatchInterfaceEntry.setIndexNames((0,_A,_I),(0,_A,_J),(0,_A,_U))
if mibBuilder.loadTexts:myRouteMapMatchInterfaceEntry.setStatus(_B)
_MyRouteMapMatchInterfaceIfIndex_Type=IfIndex
_MyRouteMapMatchInterfaceIfIndex_Object=MibTableColumn
myRouteMapMatchInterfaceIfIndex=_MyRouteMapMatchInterfaceIfIndex_Object((1,3,6,1,4,1,171,10,97,2,20,2,4,1,1),_MyRouteMapMatchInterfaceIfIndex_Type())
myRouteMapMatchInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:myRouteMapMatchInterfaceIfIndex.setStatus(_B)
_MyRouteMapMatchInterfaceStatus_Type=RowStatus
_MyRouteMapMatchInterfaceStatus_Object=MibTableColumn
myRouteMapMatchInterfaceStatus=_MyRouteMapMatchInterfaceStatus_Object((1,3,6,1,4,1,171,10,97,2,20,2,4,1,2),_MyRouteMapMatchInterfaceStatus_Type())
myRouteMapMatchInterfaceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteMapMatchInterfaceStatus.setStatus(_B)
_MyRouteRedistributeMIBObjects_ObjectIdentity=ObjectIdentity
myRouteRedistributeMIBObjects=_MyRouteRedistributeMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,20,3))
_MyRouteRedistributeTable_Object=MibTable
myRouteRedistributeTable=_MyRouteRedistributeTable_Object((1,3,6,1,4,1,171,10,97,2,20,3,1))
if mibBuilder.loadTexts:myRouteRedistributeTable.setStatus(_B)
_MyRouteRedistributeEntry_Object=MibTableRow
myRouteRedistributeEntry=_MyRouteRedistributeEntry_Object((1,3,6,1,4,1,171,10,97,2,20,3,1,1))
myRouteRedistributeEntry.setIndexNames((0,_A,_V),(0,_A,_W))
if mibBuilder.loadTexts:myRouteRedistributeEntry.setStatus(_B)
_MyRouteRedistributeProtocolCfg_Type=MyRouteProtoType
_MyRouteRedistributeProtocolCfg_Object=MibTableColumn
myRouteRedistributeProtocolCfg=_MyRouteRedistributeProtocolCfg_Object((1,3,6,1,4,1,171,10,97,2,20,3,1,1,1),_MyRouteRedistributeProtocolCfg_Type())
myRouteRedistributeProtocolCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:myRouteRedistributeProtocolCfg.setStatus(_B)
_MyRouteRedistributeProtocol_Type=MyRouteProtoType
_MyRouteRedistributeProtocol_Object=MibTableColumn
myRouteRedistributeProtocol=_MyRouteRedistributeProtocol_Object((1,3,6,1,4,1,171,10,97,2,20,3,1,1,2),_MyRouteRedistributeProtocol_Type())
myRouteRedistributeProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:myRouteRedistributeProtocol.setStatus(_B)
class _MyRouteRedistributeMetricValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777214))
_MyRouteRedistributeMetricValue_Type.__name__=_F
_MyRouteRedistributeMetricValue_Object=MibTableColumn
myRouteRedistributeMetricValue=_MyRouteRedistributeMetricValue_Object((1,3,6,1,4,1,171,10,97,2,20,3,1,1,3),_MyRouteRedistributeMetricValue_Type())
myRouteRedistributeMetricValue.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteRedistributeMetricValue.setStatus(_B)
class _MyRouteRedistributeMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_MyRouteRedistributeMetricType_Type.__name__=_E
_MyRouteRedistributeMetricType_Object=MibTableColumn
myRouteRedistributeMetricType=_MyRouteRedistributeMetricType_Object((1,3,6,1,4,1,171,10,97,2,20,3,1,1,4),_MyRouteRedistributeMetricType_Type())
myRouteRedistributeMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteRedistributeMetricType.setStatus(_B)
class _MyRouteRedistributeTagValue_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MyRouteRedistributeTagValue_Type.__name__=_F
_MyRouteRedistributeTagValue_Object=MibTableColumn
myRouteRedistributeTagValue=_MyRouteRedistributeTagValue_Object((1,3,6,1,4,1,171,10,97,2,20,3,1,1,5),_MyRouteRedistributeTagValue_Type())
myRouteRedistributeTagValue.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteRedistributeTagValue.setStatus(_B)
class _MyRouteRedistributeRouteMapName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MyRouteRedistributeRouteMapName_Type.__name__=_H
_MyRouteRedistributeRouteMapName_Object=MibTableColumn
myRouteRedistributeRouteMapName=_MyRouteRedistributeRouteMapName_Object((1,3,6,1,4,1,171,10,97,2,20,3,1,1,6),_MyRouteRedistributeRouteMapName_Type())
myRouteRedistributeRouteMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteRedistributeRouteMapName.setStatus(_B)
_MyRouteRedistributeStatus_Type=RowStatus
_MyRouteRedistributeStatus_Object=MibTableColumn
myRouteRedistributeStatus=_MyRouteRedistributeStatus_Object((1,3,6,1,4,1,171,10,97,2,20,3,1,1,7),_MyRouteRedistributeStatus_Type())
myRouteRedistributeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myRouteRedistributeStatus.setStatus(_B)
_MyRouteFilteringMIBObjects_ObjectIdentity=ObjectIdentity
myRouteFilteringMIBObjects=_MyRouteFilteringMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,20,4))
_MyIpPrefixListTable_Object=MibTable
myIpPrefixListTable=_MyIpPrefixListTable_Object((1,3,6,1,4,1,171,10,97,2,20,4,1))
if mibBuilder.loadTexts:myIpPrefixListTable.setStatus(_B)
_MyIpPrefixListEntry_Object=MibTableRow
myIpPrefixListEntry=_MyIpPrefixListEntry_Object((1,3,6,1,4,1,171,10,97,2,20,4,1,1))
myIpPrefixListEntry.setIndexNames((0,_A,_X),(0,_A,_Y))
if mibBuilder.loadTexts:myIpPrefixListEntry.setStatus(_B)
class _MyIpPrefixListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyIpPrefixListName_Type.__name__=_H
_MyIpPrefixListName_Object=MibTableColumn
myIpPrefixListName=_MyIpPrefixListName_Object((1,3,6,1,4,1,171,10,97,2,20,4,1,1,1),_MyIpPrefixListName_Type())
myIpPrefixListName.setMaxAccess(_D)
if mibBuilder.loadTexts:myIpPrefixListName.setStatus(_B)
class _MyIpPrefixListSequence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MyIpPrefixListSequence_Type.__name__=_F
_MyIpPrefixListSequence_Object=MibTableColumn
myIpPrefixListSequence=_MyIpPrefixListSequence_Object((1,3,6,1,4,1,171,10,97,2,20,4,1,1,2),_MyIpPrefixListSequence_Type())
myIpPrefixListSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:myIpPrefixListSequence.setStatus(_B)
class _MyIpPrefixListOperMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),('deny',2)))
_MyIpPrefixListOperMethod_Type.__name__=_E
_MyIpPrefixListOperMethod_Object=MibTableColumn
myIpPrefixListOperMethod=_MyIpPrefixListOperMethod_Object((1,3,6,1,4,1,171,10,97,2,20,4,1,1,3),_MyIpPrefixListOperMethod_Type())
myIpPrefixListOperMethod.setMaxAccess(_G)
if mibBuilder.loadTexts:myIpPrefixListOperMethod.setStatus(_B)
_MyIpPrefixListIpAddress_Type=IpAddress
_MyIpPrefixListIpAddress_Object=MibTableColumn
myIpPrefixListIpAddress=_MyIpPrefixListIpAddress_Object((1,3,6,1,4,1,171,10,97,2,20,4,1,1,4),_MyIpPrefixListIpAddress_Type())
myIpPrefixListIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:myIpPrefixListIpAddress.setStatus(_B)
class _MyIpPrefixListMaskLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_MyIpPrefixListMaskLength_Type.__name__=_F
_MyIpPrefixListMaskLength_Object=MibTableColumn
myIpPrefixListMaskLength=_MyIpPrefixListMaskLength_Object((1,3,6,1,4,1,171,10,97,2,20,4,1,1,5),_MyIpPrefixListMaskLength_Type())
myIpPrefixListMaskLength.setMaxAccess(_G)
if mibBuilder.loadTexts:myIpPrefixListMaskLength.setStatus(_B)
class _MyIpPrefixListMinimumPrefixLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_MyIpPrefixListMinimumPrefixLength_Type.__name__=_F
_MyIpPrefixListMinimumPrefixLength_Object=MibTableColumn
myIpPrefixListMinimumPrefixLength=_MyIpPrefixListMinimumPrefixLength_Object((1,3,6,1,4,1,171,10,97,2,20,4,1,1,6),_MyIpPrefixListMinimumPrefixLength_Type())
myIpPrefixListMinimumPrefixLength.setMaxAccess(_G)
if mibBuilder.loadTexts:myIpPrefixListMinimumPrefixLength.setStatus(_B)
class _MyIpPrefixListMaximumPrefixLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_MyIpPrefixListMaximumPrefixLength_Type.__name__=_F
_MyIpPrefixListMaximumPrefixLength_Object=MibTableColumn
myIpPrefixListMaximumPrefixLength=_MyIpPrefixListMaximumPrefixLength_Object((1,3,6,1,4,1,171,10,97,2,20,4,1,1,7),_MyIpPrefixListMaximumPrefixLength_Type())
myIpPrefixListMaximumPrefixLength.setMaxAccess(_G)
if mibBuilder.loadTexts:myIpPrefixListMaximumPrefixLength.setStatus(_B)
_MyIpPrefixListStatus_Type=RowStatus
_MyIpPrefixListStatus_Object=MibTableColumn
myIpPrefixListStatus=_MyIpPrefixListStatus_Object((1,3,6,1,4,1,171,10,97,2,20,4,1,1,8),_MyIpPrefixListStatus_Type())
myIpPrefixListStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myIpPrefixListStatus.setStatus(_B)
_MyDistributeListTable_Object=MibTable
myDistributeListTable=_MyDistributeListTable_Object((1,3,6,1,4,1,171,10,97,2,20,4,2))
if mibBuilder.loadTexts:myDistributeListTable.setStatus(_B)
_MyDistributeListEntry_Object=MibTableRow
myDistributeListEntry=_MyDistributeListEntry_Object((1,3,6,1,4,1,171,10,97,2,20,4,2,1))
myDistributeListEntry.setIndexNames((0,_A,_Z),(0,_A,_a),(0,_A,_b),(0,_A,_c))
if mibBuilder.loadTexts:myDistributeListEntry.setStatus(_B)
_MyDistributeListCfgProtoType_Type=MyRouteProtoType
_MyDistributeListCfgProtoType_Object=MibTableColumn
myDistributeListCfgProtoType=_MyDistributeListCfgProtoType_Object((1,3,6,1,4,1,171,10,97,2,20,4,2,1,1),_MyDistributeListCfgProtoType_Type())
myDistributeListCfgProtoType.setMaxAccess(_D)
if mibBuilder.loadTexts:myDistributeListCfgProtoType.setStatus(_B)
_MyDistributeListIfIndex_Type=Unsigned32
_MyDistributeListIfIndex_Object=MibTableColumn
myDistributeListIfIndex=_MyDistributeListIfIndex_Object((1,3,6,1,4,1,171,10,97,2,20,4,2,1,2),_MyDistributeListIfIndex_Type())
myDistributeListIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:myDistributeListIfIndex.setStatus(_B)
class _MyDistributeListDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('out',1),('in',2)))
_MyDistributeListDirection_Type.__name__=_E
_MyDistributeListDirection_Object=MibTableColumn
myDistributeListDirection=_MyDistributeListDirection_Object((1,3,6,1,4,1,171,10,97,2,20,4,2,1,3),_MyDistributeListDirection_Type())
myDistributeListDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:myDistributeListDirection.setStatus(_B)
_MyDistributeListFilteringProtocol_Type=Unsigned32
_MyDistributeListFilteringProtocol_Object=MibTableColumn
myDistributeListFilteringProtocol=_MyDistributeListFilteringProtocol_Object((1,3,6,1,4,1,171,10,97,2,20,4,2,1,4),_MyDistributeListFilteringProtocol_Type())
myDistributeListFilteringProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:myDistributeListFilteringProtocol.setStatus(_B)
class _MyDistributeListFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('acl',1),('gateway',2),('prefix',3),('prefix-gateway',4)))
_MyDistributeListFilterType_Type.__name__=_E
_MyDistributeListFilterType_Object=MibTableColumn
myDistributeListFilterType=_MyDistributeListFilterType_Object((1,3,6,1,4,1,171,10,97,2,20,4,2,1,5),_MyDistributeListFilterType_Type())
myDistributeListFilterType.setMaxAccess(_G)
if mibBuilder.loadTexts:myDistributeListFilterType.setStatus(_B)
class _MyDistributeListAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MyDistributeListAclName_Type.__name__=_H
_MyDistributeListAclName_Object=MibTableColumn
myDistributeListAclName=_MyDistributeListAclName_Object((1,3,6,1,4,1,171,10,97,2,20,4,2,1,6),_MyDistributeListAclName_Type())
myDistributeListAclName.setMaxAccess(_G)
if mibBuilder.loadTexts:myDistributeListAclName.setStatus(_B)
class _MyDistributeListGateWayIpPrefixName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MyDistributeListGateWayIpPrefixName_Type.__name__=_H
_MyDistributeListGateWayIpPrefixName_Object=MibTableColumn
myDistributeListGateWayIpPrefixName=_MyDistributeListGateWayIpPrefixName_Object((1,3,6,1,4,1,171,10,97,2,20,4,2,1,7),_MyDistributeListGateWayIpPrefixName_Type())
myDistributeListGateWayIpPrefixName.setMaxAccess(_G)
if mibBuilder.loadTexts:myDistributeListGateWayIpPrefixName.setStatus(_B)
class _MyDistributeListPrefixIpPrefixName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MyDistributeListPrefixIpPrefixName_Type.__name__=_H
_MyDistributeListPrefixIpPrefixName_Object=MibTableColumn
myDistributeListPrefixIpPrefixName=_MyDistributeListPrefixIpPrefixName_Object((1,3,6,1,4,1,171,10,97,2,20,4,2,1,8),_MyDistributeListPrefixIpPrefixName_Type())
myDistributeListPrefixIpPrefixName.setMaxAccess(_G)
if mibBuilder.loadTexts:myDistributeListPrefixIpPrefixName.setStatus(_B)
_MyDistributeListStatus_Type=RowStatus
_MyDistributeListStatus_Object=MibTableColumn
myDistributeListStatus=_MyDistributeListStatus_Object((1,3,6,1,4,1,171,10,97,2,20,4,2,1,9),_MyDistributeListStatus_Type())
myDistributeListStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myDistributeListStatus.setStatus(_B)
_MyipCidrRouteExtendMIBObjects_ObjectIdentity=ObjectIdentity
myipCidrRouteExtendMIBObjects=_MyipCidrRouteExtendMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,20,5))
_MyipCidrRouteTable_Object=MibTable
myipCidrRouteTable=_MyipCidrRouteTable_Object((1,3,6,1,4,1,171,10,97,2,20,5,1))
if mibBuilder.loadTexts:myipCidrRouteTable.setStatus(_B)
_MyipCidrRouteEntry_Object=MibTableRow
myipCidrRouteEntry=_MyipCidrRouteEntry_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1))
myipCidrRouteEntry.setIndexNames((0,_A,_d),(0,_A,_e),(0,_A,_f),(0,_A,_g))
if mibBuilder.loadTexts:myipCidrRouteEntry.setStatus(_B)
_MyipCidrRouteDest_Type=IpAddress
_MyipCidrRouteDest_Object=MibTableColumn
myipCidrRouteDest=_MyipCidrRouteDest_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,1),_MyipCidrRouteDest_Type())
myipCidrRouteDest.setMaxAccess(_D)
if mibBuilder.loadTexts:myipCidrRouteDest.setStatus(_B)
_MyipCidrRouteMask_Type=IpAddress
_MyipCidrRouteMask_Object=MibTableColumn
myipCidrRouteMask=_MyipCidrRouteMask_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,2),_MyipCidrRouteMask_Type())
myipCidrRouteMask.setMaxAccess(_D)
if mibBuilder.loadTexts:myipCidrRouteMask.setStatus(_B)
_MyipCidrRouteTos_Type=Integer32
_MyipCidrRouteTos_Object=MibTableColumn
myipCidrRouteTos=_MyipCidrRouteTos_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,3),_MyipCidrRouteTos_Type())
myipCidrRouteTos.setMaxAccess(_D)
if mibBuilder.loadTexts:myipCidrRouteTos.setStatus(_B)
_MyipCidrRouteNextHop_Type=IpAddress
_MyipCidrRouteNextHop_Object=MibTableColumn
myipCidrRouteNextHop=_MyipCidrRouteNextHop_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,4),_MyipCidrRouteNextHop_Type())
myipCidrRouteNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:myipCidrRouteNextHop.setStatus(_B)
class _MyipCidrRouteIfIndex_Type(Integer32):defaultValue=0
_MyipCidrRouteIfIndex_Type.__name__=_E
_MyipCidrRouteIfIndex_Object=MibTableColumn
myipCidrRouteIfIndex=_MyipCidrRouteIfIndex_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,5),_MyipCidrRouteIfIndex_Type())
myipCidrRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myipCidrRouteIfIndex.setStatus(_B)
class _MyipCidrRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('reject',2),(_L,3),('remote',4)))
_MyipCidrRouteType_Type.__name__=_E
_MyipCidrRouteType_Object=MibTableColumn
myipCidrRouteType=_MyipCidrRouteType_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,6),_MyipCidrRouteType_Type())
myipCidrRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:myipCidrRouteType.setStatus(_B)
class _MyipCidrRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_K,1),(_L,2),(_k,3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('isIs',9),('esIs',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14),('idpr',15),('ciscoEigrp',16),('policy',17)))
_MyipCidrRouteProto_Type.__name__=_E
_MyipCidrRouteProto_Object=MibTableColumn
myipCidrRouteProto=_MyipCidrRouteProto_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,7),_MyipCidrRouteProto_Type())
myipCidrRouteProto.setMaxAccess(_D)
if mibBuilder.loadTexts:myipCidrRouteProto.setStatus(_B)
class _MyipCidrRouteAge_Type(Integer32):defaultValue=0
_MyipCidrRouteAge_Type.__name__=_E
_MyipCidrRouteAge_Object=MibTableColumn
myipCidrRouteAge=_MyipCidrRouteAge_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,8),_MyipCidrRouteAge_Type())
myipCidrRouteAge.setMaxAccess(_D)
if mibBuilder.loadTexts:myipCidrRouteAge.setStatus(_B)
_MyipCidrRouteInfo_Type=ObjectIdentifier
_MyipCidrRouteInfo_Object=MibTableColumn
myipCidrRouteInfo=_MyipCidrRouteInfo_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,9),_MyipCidrRouteInfo_Type())
myipCidrRouteInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:myipCidrRouteInfo.setStatus(_B)
class _MyipCidrRouteNextHopAS_Type(Integer32):defaultValue=0
_MyipCidrRouteNextHopAS_Type.__name__=_E
_MyipCidrRouteNextHopAS_Object=MibTableColumn
myipCidrRouteNextHopAS=_MyipCidrRouteNextHopAS_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,10),_MyipCidrRouteNextHopAS_Type())
myipCidrRouteNextHopAS.setMaxAccess(_C)
if mibBuilder.loadTexts:myipCidrRouteNextHopAS.setStatus(_B)
class _MyipCidrRouteMetric1_Type(Integer32):defaultValue=-1
_MyipCidrRouteMetric1_Type.__name__=_E
_MyipCidrRouteMetric1_Object=MibTableColumn
myipCidrRouteMetric1=_MyipCidrRouteMetric1_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,11),_MyipCidrRouteMetric1_Type())
myipCidrRouteMetric1.setMaxAccess(_C)
if mibBuilder.loadTexts:myipCidrRouteMetric1.setStatus(_B)
class _MyipCidrRouteMetric2_Type(Integer32):defaultValue=-1
_MyipCidrRouteMetric2_Type.__name__=_E
_MyipCidrRouteMetric2_Object=MibTableColumn
myipCidrRouteMetric2=_MyipCidrRouteMetric2_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,12),_MyipCidrRouteMetric2_Type())
myipCidrRouteMetric2.setMaxAccess(_C)
if mibBuilder.loadTexts:myipCidrRouteMetric2.setStatus(_B)
class _MyipCidrRouteMetric3_Type(Integer32):defaultValue=-1
_MyipCidrRouteMetric3_Type.__name__=_E
_MyipCidrRouteMetric3_Object=MibTableColumn
myipCidrRouteMetric3=_MyipCidrRouteMetric3_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,13),_MyipCidrRouteMetric3_Type())
myipCidrRouteMetric3.setMaxAccess(_C)
if mibBuilder.loadTexts:myipCidrRouteMetric3.setStatus(_B)
class _MyipCidrRouteMetric4_Type(Integer32):defaultValue=-1
_MyipCidrRouteMetric4_Type.__name__=_E
_MyipCidrRouteMetric4_Object=MibTableColumn
myipCidrRouteMetric4=_MyipCidrRouteMetric4_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,14),_MyipCidrRouteMetric4_Type())
myipCidrRouteMetric4.setMaxAccess(_C)
if mibBuilder.loadTexts:myipCidrRouteMetric4.setStatus(_B)
class _MyipCidrRouteMetric5_Type(Integer32):defaultValue=-1
_MyipCidrRouteMetric5_Type.__name__=_E
_MyipCidrRouteMetric5_Object=MibTableColumn
myipCidrRouteMetric5=_MyipCidrRouteMetric5_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,15),_MyipCidrRouteMetric5_Type())
myipCidrRouteMetric5.setMaxAccess(_C)
if mibBuilder.loadTexts:myipCidrRouteMetric5.setStatus(_B)
_MyipCidrRouteStatus_Type=RowStatus
_MyipCidrRouteStatus_Object=MibTableColumn
myipCidrRouteStatus=_MyipCidrRouteStatus_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,16),_MyipCidrRouteStatus_Type())
myipCidrRouteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myipCidrRouteStatus.setStatus(_B)
class _MyipCidrOspfRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('ospf-route',0),('ospf-ia-route',1),('ospf-n1-route',2),('ospf-n2-route',3),('ospf-e1-route',4),('ospf-e2-route',5)))
_MyipCidrOspfRouteType_Type.__name__=_E
_MyipCidrOspfRouteType_Object=MibTableColumn
myipCidrOspfRouteType=_MyipCidrOspfRouteType_Object((1,3,6,1,4,1,171,10,97,2,20,5,1,1,17),_MyipCidrOspfRouteType_Type())
myipCidrOspfRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:myipCidrOspfRouteType.setStatus(_B)
_MyRouteMIBConformance_ObjectIdentity=ObjectIdentity
myRouteMIBConformance=_MyRouteMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,20,6))
_MyRouteMIBCompliances_ObjectIdentity=ObjectIdentity
myRouteMIBCompliances=_MyRouteMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,20,6,1))
_MyRouteMIBGroups_ObjectIdentity=ObjectIdentity
myRouteMIBGroups=_MyRouteMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,20,6,2))
myRouteMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,20,6,2,1))
myRouteMIBGroup.setObjects((_A,_p))
if mibBuilder.loadTexts:myRouteMIBGroup.setStatus(_B)
myRouteInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,20,6,2,2))
myRouteInfoMIBGroup.setObjects(*((_A,_M),(_A,_N),(_A,_q),(_A,_r),(_A,_O),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:myRouteInfoMIBGroup.setStatus(_B)
myRouteMapMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,20,6,2,3))
myRouteMapMIBGroup.setObjects(*((_A,_I),(_A,_J),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_h),(_A,_h),(_A,_A4),(_A,_S),(_A,_R),(_A,_A5),(_A,_T),(_A,_A6),(_A,_U),(_A,_A7)))
if mibBuilder.loadTexts:myRouteMapMIBGroup.setStatus(_B)
myRouteRedistributeMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,20,6,2,4))
myRouteRedistributeMIBGroup.setObjects(*((_A,_V),(_A,_W),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:myRouteRedistributeMIBGroup.setStatus(_B)
myRouteFilteringMibGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,20,6,2,5))
myRouteFilteringMibGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_Z),(_A,_a),(_A,_AJ),(_A,_b),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_c),(_A,_AN)))
if mibBuilder.loadTexts:myRouteFilteringMibGroup.setStatus(_B)
myipCidrRouteMibGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,20,6,2,6))
myipCidrRouteMibGroup.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:myipCidrRouteMibGroup.setStatus(_B)
myRouteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,20,6,1,1))
myRouteMIBCompliance.setObjects(*((_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:myRouteMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'MyRouteProtoType':MyRouteProtoType,'myRouteMIB':myRouteMIB,'myRouteMIBObjects':myRouteMIBObjects,_p:myRouteServiceStatus,'myRoutingProtoInfoTable':myRoutingProtoInfoTable,'myRoutingProtoInfoEntry':myRoutingProtoInfoEntry,_M:myRoutingProtoInfoProtoType,_N:myRoutingProtoInfoGateWay,_q:myRoutingProtoInfoDistance,_r:myRoutingProtoInfoLastUpdate,'myDefRoutingCfgTable':myDefRoutingCfgTable,'myDefRoutingCfgEntry':myDefRoutingCfgEntry,_O:myDefRoutingCfgRoutingProtoType,_s:myDefRoutingCfgAlways,_t:myDefRoutingCfgMetric,_u:myDefRoutingCfgMetricType,_v:myDefRoutingCfgRouteMap,_w:myDefRoutingCfgStatus,'myRouteMapMIBObjects':myRouteMapMIBObjects,'myRouteMapTable':myRouteMapTable,'myRouteMapEntry':myRouteMapEntry,_I:myRouteMapName,_J:myRouteMapSequenceNumber,_x:myRouteMapOperType,_y:myRouteMapMatchMetric,_z:myRouteMapMatchRouteType,_A0:myRouteMapMetricValueType,_A1:myRouteMapSetMetric,_A2:myRouteMapSetLevel,_A3:myRouteMapSetMetricType,_h:myRouteMapSetNexthopSt,'myRouteMapSetNexthop':myRouteMapSetNexthop,_A4:myRouteMapStatus,'myRouteMapMatchIpAddressTable':myRouteMapMatchIpAddressTable,'myRouteMapMatchIpAddressEntry':myRouteMapMatchIpAddressEntry,_R:myRouteMapMatchType,_S:myRouteMapMatchIpAddressAclName,_A5:myRouteMapMatchIpAddressStatus,'myRouteMapMatchTagTable':myRouteMapMatchTagTable,'myRouteMapMatchTagEntry':myRouteMapMatchTagEntry,_T:myRouteMapMatchTagValue,_A6:myRouteMapMatchTagStatus,'myRouteMapMatchInterfaceTable':myRouteMapMatchInterfaceTable,'myRouteMapMatchInterfaceEntry':myRouteMapMatchInterfaceEntry,_U:myRouteMapMatchInterfaceIfIndex,_A7:myRouteMapMatchInterfaceStatus,'myRouteRedistributeMIBObjects':myRouteRedistributeMIBObjects,'myRouteRedistributeTable':myRouteRedistributeTable,'myRouteRedistributeEntry':myRouteRedistributeEntry,_V:myRouteRedistributeProtocolCfg,_W:myRouteRedistributeProtocol,_A8:myRouteRedistributeMetricValue,_A9:myRouteRedistributeMetricType,_AA:myRouteRedistributeTagValue,_AB:myRouteRedistributeRouteMapName,_AC:myRouteRedistributeStatus,'myRouteFilteringMIBObjects':myRouteFilteringMIBObjects,'myIpPrefixListTable':myIpPrefixListTable,'myIpPrefixListEntry':myIpPrefixListEntry,_X:myIpPrefixListName,_Y:myIpPrefixListSequence,_AD:myIpPrefixListOperMethod,_AE:myIpPrefixListIpAddress,_AF:myIpPrefixListMaskLength,_AG:myIpPrefixListMinimumPrefixLength,_AH:myIpPrefixListMaximumPrefixLength,_AI:myIpPrefixListStatus,'myDistributeListTable':myDistributeListTable,'myDistributeListEntry':myDistributeListEntry,_Z:myDistributeListCfgProtoType,_a:myDistributeListIfIndex,_b:myDistributeListDirection,_c:myDistributeListFilteringProtocol,_AJ:myDistributeListFilterType,_AK:myDistributeListAclName,_AL:myDistributeListGateWayIpPrefixName,_AM:myDistributeListPrefixIpPrefixName,_AN:myDistributeListStatus,'myipCidrRouteExtendMIBObjects':myipCidrRouteExtendMIBObjects,'myipCidrRouteTable':myipCidrRouteTable,'myipCidrRouteEntry':myipCidrRouteEntry,_d:myipCidrRouteDest,_e:myipCidrRouteMask,_f:myipCidrRouteTos,_g:myipCidrRouteNextHop,_AO:myipCidrRouteIfIndex,_AP:myipCidrRouteType,_AQ:myipCidrRouteProto,_AR:myipCidrRouteAge,_AS:myipCidrRouteInfo,_AT:myipCidrRouteNextHopAS,_AU:myipCidrRouteMetric1,_AV:myipCidrRouteMetric2,_AW:myipCidrRouteMetric3,_AX:myipCidrRouteMetric4,_AY:myipCidrRouteMetric5,_AZ:myipCidrRouteStatus,_Aa:myipCidrOspfRouteType,'myRouteMIBConformance':myRouteMIBConformance,'myRouteMIBCompliances':myRouteMIBCompliances,'myRouteMIBCompliance':myRouteMIBCompliance,'myRouteMIBGroups':myRouteMIBGroups,_Ab:myRouteMIBGroup,_Ac:myRouteInfoMIBGroup,_Ad:myRouteMapMIBGroup,_Ae:myRouteRedistributeMIBGroup,_Af:myRouteFilteringMibGroup,_Ag:myipCidrRouteMibGroup})