_Af='qtechipCidrRouteMibGroup'
_Ae='qtechRouteFilteringMibGroup'
_Ad='qtechRouteRedistributeMIBGroup'
_Ac='qtechRouteMapMIBGroup'
_Ab='qtechRouteInfoMIBGroup'
_Aa='qtechRouteMIBGroup'
_AZ='qtechipCidrOspfRouteType'
_AY='qtechipCidrRouteStatus'
_AX='qtechipCidrRouteMetric5'
_AW='qtechipCidrRouteMetric4'
_AV='qtechipCidrRouteMetric3'
_AU='qtechipCidrRouteMetric2'
_AT='qtechipCidrRouteMetric1'
_AS='qtechipCidrRouteNextHopAS'
_AR='qtechipCidrRouteInfo'
_AQ='qtechipCidrRouteAge'
_AP='qtechipCidrRouteProto'
_AO='qtechipCidrRouteType'
_AN='qtechipCidrRouteIfIndex'
_AM='qtechDistributeListStatus'
_AL='qtechDistributeListPrefixIpPrefixName'
_AK='qtechDistributeListGateWayIpPrefixName'
_AJ='qtechDistributeListAclName'
_AI='qtechDistributeListFilterType'
_AH='qtechIpPrefixListStatus'
_AG='qtechIpPrefixListMaximumPrefixLength'
_AF='qtechIpPrefixListMinimumPrefixLength'
_AE='qtechIpPrefixListMaskLength'
_AD='qtechIpPrefixListIpAddress'
_AC='qtechIpPrefixListOperMethod'
_AB='qtechRouteRedistributeStatus'
_AA='qtechRouteRedistributeRouteMapName'
_A9='qtechRouteRedistributeTagValue'
_A8='qtechRouteRedistributeMetricType'
_A7='qtechRouteRedistributeMetricValue'
_A6='qtechRouteMapMatchInterfaceStatus'
_A5='qtechRouteMapMatchTagStatus'
_A4='qtechRouteMapMatchIpAddressStatus'
_A3='qtechRouteMapStatus'
_A2='qtechRouteMapSetMetricType'
_A1='qtechRouteMapSetLevel'
_A0='qtechRouteMapSetMetric'
_z='qtechRouteMapMetricValueType'
_y='qtechRouteMapMatchRouteType'
_x='qtechRouteMapMatchMetric'
_w='qtechRouteMapOperType'
_v='qtechDefRoutingCfgStatus'
_u='qtechDefRoutingCfgRouteMap'
_t='qtechDefRoutingCfgMetricType'
_s='qtechDefRoutingCfgMetric'
_r='qtechDefRoutingCfgAlways'
_q='qtechRoutingProtoInfoLastUpdate'
_p='qtechRoutingProtoInfoDistance'
_o='qtechRouteServiceStatus'
_n='noOper'
_m='external'
_l='internal'
_k='permit'
_j='netmgmt'
_i='TruthValue'
_h='ConfigStatus'
_g='qtechRouteMapSetNexthopSt'
_f='qtechipCidrRouteNextHop'
_e='qtechipCidrRouteTos'
_d='qtechipCidrRouteMask'
_c='qtechipCidrRouteDest'
_b='qtechDistributeListFilteringProtocol'
_a='qtechDistributeListDirection'
_Z='qtechDistributeListIfIndex'
_Y='qtechDistributeListCfgProtoType'
_X='qtechIpPrefixListSequence'
_W='qtechIpPrefixListName'
_V='qtechRouteRedistributeProtocol'
_U='qtechRouteRedistributeProtocolCfg'
_T='qtechRouteMapMatchInterfaceIfIndex'
_S='qtechRouteMapMatchTagValue'
_R='qtechRouteMapMatchIpAddressAclName'
_Q='qtechRouteMapMatchType'
_P='type2'
_O='type1'
_N='qtechDefRoutingCfgRoutingProtoType'
_M='qtechRoutingProtoInfoGateWay'
_L='qtechRoutingProtoInfoProtoType'
_K='local'
_J='other'
_I='qtechRouteMapSequenceNumber'
_H='qtechRouteMapName'
_G='DisplayString'
_F='Unsigned32'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='current'
_A='QTECH-ROUTE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('QTECH-TC',_h,'IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention',_i)
qtechRouteMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,20))
if mibBuilder.loadTexts:qtechRouteMIB.setRevisions(('2002-03-20 00:00',))
class QtechRouteProtoType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_J,1),(_K,2),(_j,3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('isis',9),('esis',10),('ciscoigrp',11),('bbnspfigp',12),('ospf',13),('bgp',14),('idpr',15),('ciscoeigrp',16),('max',17)))
_QtechRouteMIBObjects_ObjectIdentity=ObjectIdentity
qtechRouteMIBObjects=_QtechRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,20,1))
_QtechRouteServiceStatus_Type=EnabledStatus
_QtechRouteServiceStatus_Object=MibScalar
qtechRouteServiceStatus=_QtechRouteServiceStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,1),_QtechRouteServiceStatus_Type())
qtechRouteServiceStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:qtechRouteServiceStatus.setStatus(_B)
_QtechRoutingProtoInfoTable_Object=MibTable
qtechRoutingProtoInfoTable=_QtechRoutingProtoInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,2))
if mibBuilder.loadTexts:qtechRoutingProtoInfoTable.setStatus(_B)
_QtechRoutingProtoInfoEntry_Object=MibTableRow
qtechRoutingProtoInfoEntry=_QtechRoutingProtoInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,2,1))
qtechRoutingProtoInfoEntry.setIndexNames((0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:qtechRoutingProtoInfoEntry.setStatus(_B)
_QtechRoutingProtoInfoProtoType_Type=QtechRouteProtoType
_QtechRoutingProtoInfoProtoType_Object=MibTableColumn
qtechRoutingProtoInfoProtoType=_QtechRoutingProtoInfoProtoType_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,2,1,1),_QtechRoutingProtoInfoProtoType_Type())
qtechRoutingProtoInfoProtoType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoutingProtoInfoProtoType.setStatus(_B)
_QtechRoutingProtoInfoGateWay_Type=IpAddress
_QtechRoutingProtoInfoGateWay_Object=MibTableColumn
qtechRoutingProtoInfoGateWay=_QtechRoutingProtoInfoGateWay_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,2,1,2),_QtechRoutingProtoInfoGateWay_Type())
qtechRoutingProtoInfoGateWay.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoutingProtoInfoGateWay.setStatus(_B)
_QtechRoutingProtoInfoDistance_Type=Unsigned32
_QtechRoutingProtoInfoDistance_Object=MibTableColumn
qtechRoutingProtoInfoDistance=_QtechRoutingProtoInfoDistance_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,2,1,3),_QtechRoutingProtoInfoDistance_Type())
qtechRoutingProtoInfoDistance.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoutingProtoInfoDistance.setStatus(_B)
_QtechRoutingProtoInfoLastUpdate_Type=TimeTicks
_QtechRoutingProtoInfoLastUpdate_Object=MibTableColumn
qtechRoutingProtoInfoLastUpdate=_QtechRoutingProtoInfoLastUpdate_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,2,1,4),_QtechRoutingProtoInfoLastUpdate_Type())
qtechRoutingProtoInfoLastUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoutingProtoInfoLastUpdate.setStatus(_B)
_QtechDefRoutingCfgTable_Object=MibTable
qtechDefRoutingCfgTable=_QtechDefRoutingCfgTable_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,3))
if mibBuilder.loadTexts:qtechDefRoutingCfgTable.setStatus(_B)
_QtechDefRoutingCfgEntry_Object=MibTableRow
qtechDefRoutingCfgEntry=_QtechDefRoutingCfgEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,3,1))
qtechDefRoutingCfgEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:qtechDefRoutingCfgEntry.setStatus(_B)
_QtechDefRoutingCfgRoutingProtoType_Type=QtechRouteProtoType
_QtechDefRoutingCfgRoutingProtoType_Object=MibTableColumn
qtechDefRoutingCfgRoutingProtoType=_QtechDefRoutingCfgRoutingProtoType_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,3,1,1),_QtechDefRoutingCfgRoutingProtoType_Type())
qtechDefRoutingCfgRoutingProtoType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDefRoutingCfgRoutingProtoType.setStatus(_B)
class _QtechDefRoutingCfgAlways_Type(TruthValue):defaultValue=2
_QtechDefRoutingCfgAlways_Type.__name__=_i
_QtechDefRoutingCfgAlways_Object=MibTableColumn
qtechDefRoutingCfgAlways=_QtechDefRoutingCfgAlways_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,3,1,2),_QtechDefRoutingCfgAlways_Type())
qtechDefRoutingCfgAlways.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDefRoutingCfgAlways.setStatus(_B)
class _QtechDefRoutingCfgMetric_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777214))
_QtechDefRoutingCfgMetric_Type.__name__=_F
_QtechDefRoutingCfgMetric_Object=MibTableColumn
qtechDefRoutingCfgMetric=_QtechDefRoutingCfgMetric_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,3,1,3),_QtechDefRoutingCfgMetric_Type())
qtechDefRoutingCfgMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDefRoutingCfgMetric.setStatus(_B)
class _QtechDefRoutingCfgMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_QtechDefRoutingCfgMetricType_Type.__name__=_E
_QtechDefRoutingCfgMetricType_Object=MibTableColumn
qtechDefRoutingCfgMetricType=_QtechDefRoutingCfgMetricType_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,3,1,4),_QtechDefRoutingCfgMetricType_Type())
qtechDefRoutingCfgMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDefRoutingCfgMetricType.setStatus(_B)
class _QtechDefRoutingCfgRouteMap_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechDefRoutingCfgRouteMap_Type.__name__=_G
_QtechDefRoutingCfgRouteMap_Object=MibTableColumn
qtechDefRoutingCfgRouteMap=_QtechDefRoutingCfgRouteMap_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,3,1,5),_QtechDefRoutingCfgRouteMap_Type())
qtechDefRoutingCfgRouteMap.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDefRoutingCfgRouteMap.setStatus(_B)
_QtechDefRoutingCfgStatus_Type=RowStatus
_QtechDefRoutingCfgStatus_Object=MibTableColumn
qtechDefRoutingCfgStatus=_QtechDefRoutingCfgStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,20,1,3,1,6),_QtechDefRoutingCfgStatus_Type())
qtechDefRoutingCfgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDefRoutingCfgStatus.setStatus(_B)
_QtechRouteMapMIBObjects_ObjectIdentity=ObjectIdentity
qtechRouteMapMIBObjects=_QtechRouteMapMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,20,2))
_QtechRouteMapTable_Object=MibTable
qtechRouteMapTable=_QtechRouteMapTable_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1))
if mibBuilder.loadTexts:qtechRouteMapTable.setStatus(_B)
_QtechRouteMapEntry_Object=MibTableRow
qtechRouteMapEntry=_QtechRouteMapEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1,1))
qtechRouteMapEntry.setIndexNames((0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:qtechRouteMapEntry.setStatus(_B)
class _QtechRouteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechRouteMapName_Type.__name__=_G
_QtechRouteMapName_Object=MibTableColumn
qtechRouteMapName=_QtechRouteMapName_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1,1,1),_QtechRouteMapName_Type())
qtechRouteMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRouteMapName.setStatus(_B)
class _QtechRouteMapSequenceNumber_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechRouteMapSequenceNumber_Type.__name__=_F
_QtechRouteMapSequenceNumber_Object=MibTableColumn
qtechRouteMapSequenceNumber=_QtechRouteMapSequenceNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1,1,2),_QtechRouteMapSequenceNumber_Type())
qtechRouteMapSequenceNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRouteMapSequenceNumber.setStatus(_B)
class _QtechRouteMapOperType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),('deny',2)))
_QtechRouteMapOperType_Type.__name__=_E
_QtechRouteMapOperType_Object=MibTableColumn
qtechRouteMapOperType=_QtechRouteMapOperType_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1,1,3),_QtechRouteMapOperType_Type())
qtechRouteMapOperType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRouteMapOperType.setStatus(_B)
class _QtechRouteMapMatchMetric_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechRouteMapMatchMetric_Type.__name__=_F
_QtechRouteMapMatchMetric_Object=MibTableColumn
qtechRouteMapMatchMetric=_QtechRouteMapMatchMetric_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1,1,4),_QtechRouteMapMatchMetric_Type())
qtechRouteMapMatchMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteMapMatchMetric.setStatus(_B)
class _QtechRouteMapMatchRouteType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('notMatch',0),(_l,1),(_m,2),('external-type1',3),('external-type2',4)))
_QtechRouteMapMatchRouteType_Type.__name__=_E
_QtechRouteMapMatchRouteType_Object=MibTableColumn
qtechRouteMapMatchRouteType=_QtechRouteMapMatchRouteType_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1,1,5),_QtechRouteMapMatchRouteType_Type())
qtechRouteMapMatchRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteMapMatchRouteType.setStatus(_B)
class _QtechRouteMapMetricValueType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_n,0),('replace',1),('add',2),('reduce',3)))
_QtechRouteMapMetricValueType_Type.__name__=_E
_QtechRouteMapMetricValueType_Object=MibTableColumn
qtechRouteMapMetricValueType=_QtechRouteMapMetricValueType_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1,1,6),_QtechRouteMapMetricValueType_Type())
qtechRouteMapMetricValueType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteMapMetricValueType.setStatus(_B)
class _QtechRouteMapSetMetric_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechRouteMapSetMetric_Type.__name__=_F
_QtechRouteMapSetMetric_Object=MibTableColumn
qtechRouteMapSetMetric=_QtechRouteMapSetMetric_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1,1,7),_QtechRouteMapSetMetric_Type())
qtechRouteMapSetMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteMapSetMetric.setStatus(_B)
class _QtechRouteMapSetLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('all',0),('stubarea',1),('backbone',2)))
_QtechRouteMapSetLevel_Type.__name__=_E
_QtechRouteMapSetLevel_Object=MibTableColumn
qtechRouteMapSetLevel=_QtechRouteMapSetLevel_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1,1,8),_QtechRouteMapSetLevel_Type())
qtechRouteMapSetLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteMapSetLevel.setStatus(_B)
class _QtechRouteMapSetMetricType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_n,0),(_l,1),(_m,2),(_O,3),(_P,4)))
_QtechRouteMapSetMetricType_Type.__name__=_E
_QtechRouteMapSetMetricType_Object=MibTableColumn
qtechRouteMapSetMetricType=_QtechRouteMapSetMetricType_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1,1,9),_QtechRouteMapSetMetricType_Type())
qtechRouteMapSetMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteMapSetMetricType.setStatus(_B)
class _QtechRouteMapSetNexthopSt_Type(ConfigStatus):defaultValue=2
_QtechRouteMapSetNexthopSt_Type.__name__=_h
_QtechRouteMapSetNexthopSt_Object=MibTableColumn
qtechRouteMapSetNexthopSt=_QtechRouteMapSetNexthopSt_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1,1,10),_QtechRouteMapSetNexthopSt_Type())
qtechRouteMapSetNexthopSt.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteMapSetNexthopSt.setStatus(_B)
_QtechRouteMapSetNexthop_Type=IpAddress
_QtechRouteMapSetNexthop_Object=MibTableColumn
qtechRouteMapSetNexthop=_QtechRouteMapSetNexthop_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1,1,11),_QtechRouteMapSetNexthop_Type())
qtechRouteMapSetNexthop.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteMapSetNexthop.setStatus(_B)
_QtechRouteMapStatus_Type=RowStatus
_QtechRouteMapStatus_Object=MibTableColumn
qtechRouteMapStatus=_QtechRouteMapStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,1,1,12),_QtechRouteMapStatus_Type())
qtechRouteMapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteMapStatus.setStatus(_B)
_QtechRouteMapMatchIpAddressTable_Object=MibTable
qtechRouteMapMatchIpAddressTable=_QtechRouteMapMatchIpAddressTable_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,2))
if mibBuilder.loadTexts:qtechRouteMapMatchIpAddressTable.setStatus(_B)
_QtechRouteMapMatchIpAddressEntry_Object=MibTableRow
qtechRouteMapMatchIpAddressEntry=_QtechRouteMapMatchIpAddressEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,2,1))
qtechRouteMapMatchIpAddressEntry.setIndexNames((0,_A,_H),(0,_A,_I),(0,_A,_Q),(0,_A,_R))
if mibBuilder.loadTexts:qtechRouteMapMatchIpAddressEntry.setStatus(_B)
class _QtechRouteMapMatchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('destination',1),('nextHop',2),('source',3)))
_QtechRouteMapMatchType_Type.__name__=_E
_QtechRouteMapMatchType_Object=MibTableColumn
qtechRouteMapMatchType=_QtechRouteMapMatchType_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,2,1,1),_QtechRouteMapMatchType_Type())
qtechRouteMapMatchType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRouteMapMatchType.setStatus(_B)
class _QtechRouteMapMatchIpAddressAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechRouteMapMatchIpAddressAclName_Type.__name__=_G
_QtechRouteMapMatchIpAddressAclName_Object=MibTableColumn
qtechRouteMapMatchIpAddressAclName=_QtechRouteMapMatchIpAddressAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,2,1,2),_QtechRouteMapMatchIpAddressAclName_Type())
qtechRouteMapMatchIpAddressAclName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRouteMapMatchIpAddressAclName.setStatus(_B)
_QtechRouteMapMatchIpAddressStatus_Type=RowStatus
_QtechRouteMapMatchIpAddressStatus_Object=MibTableColumn
qtechRouteMapMatchIpAddressStatus=_QtechRouteMapMatchIpAddressStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,2,1,3),_QtechRouteMapMatchIpAddressStatus_Type())
qtechRouteMapMatchIpAddressStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteMapMatchIpAddressStatus.setStatus(_B)
_QtechRouteMapMatchTagTable_Object=MibTable
qtechRouteMapMatchTagTable=_QtechRouteMapMatchTagTable_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,3))
if mibBuilder.loadTexts:qtechRouteMapMatchTagTable.setStatus(_B)
_QtechRouteMapMatchTagEntry_Object=MibTableRow
qtechRouteMapMatchTagEntry=_QtechRouteMapMatchTagEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,3,1))
qtechRouteMapMatchTagEntry.setIndexNames((0,_A,_H),(0,_A,_I),(0,_A,_S))
if mibBuilder.loadTexts:qtechRouteMapMatchTagEntry.setStatus(_B)
class _QtechRouteMapMatchTagValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechRouteMapMatchTagValue_Type.__name__=_F
_QtechRouteMapMatchTagValue_Object=MibTableColumn
qtechRouteMapMatchTagValue=_QtechRouteMapMatchTagValue_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,3,1,1),_QtechRouteMapMatchTagValue_Type())
qtechRouteMapMatchTagValue.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRouteMapMatchTagValue.setStatus(_B)
_QtechRouteMapMatchTagStatus_Type=RowStatus
_QtechRouteMapMatchTagStatus_Object=MibTableColumn
qtechRouteMapMatchTagStatus=_QtechRouteMapMatchTagStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,3,1,2),_QtechRouteMapMatchTagStatus_Type())
qtechRouteMapMatchTagStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteMapMatchTagStatus.setStatus(_B)
_QtechRouteMapMatchInterfaceTable_Object=MibTable
qtechRouteMapMatchInterfaceTable=_QtechRouteMapMatchInterfaceTable_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,4))
if mibBuilder.loadTexts:qtechRouteMapMatchInterfaceTable.setStatus(_B)
_QtechRouteMapMatchInterfaceEntry_Object=MibTableRow
qtechRouteMapMatchInterfaceEntry=_QtechRouteMapMatchInterfaceEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,4,1))
qtechRouteMapMatchInterfaceEntry.setIndexNames((0,_A,_H),(0,_A,_I),(0,_A,_T))
if mibBuilder.loadTexts:qtechRouteMapMatchInterfaceEntry.setStatus(_B)
_QtechRouteMapMatchInterfaceIfIndex_Type=IfIndex
_QtechRouteMapMatchInterfaceIfIndex_Object=MibTableColumn
qtechRouteMapMatchInterfaceIfIndex=_QtechRouteMapMatchInterfaceIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,4,1,1),_QtechRouteMapMatchInterfaceIfIndex_Type())
qtechRouteMapMatchInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRouteMapMatchInterfaceIfIndex.setStatus(_B)
_QtechRouteMapMatchInterfaceStatus_Type=RowStatus
_QtechRouteMapMatchInterfaceStatus_Object=MibTableColumn
qtechRouteMapMatchInterfaceStatus=_QtechRouteMapMatchInterfaceStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,20,2,4,1,2),_QtechRouteMapMatchInterfaceStatus_Type())
qtechRouteMapMatchInterfaceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteMapMatchInterfaceStatus.setStatus(_B)
_QtechRouteRedistributeMIBObjects_ObjectIdentity=ObjectIdentity
qtechRouteRedistributeMIBObjects=_QtechRouteRedistributeMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,20,3))
_QtechRouteRedistributeTable_Object=MibTable
qtechRouteRedistributeTable=_QtechRouteRedistributeTable_Object((1,3,6,1,4,1,27514,1,1,10,2,20,3,1))
if mibBuilder.loadTexts:qtechRouteRedistributeTable.setStatus(_B)
_QtechRouteRedistributeEntry_Object=MibTableRow
qtechRouteRedistributeEntry=_QtechRouteRedistributeEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,20,3,1,1))
qtechRouteRedistributeEntry.setIndexNames((0,_A,_U),(0,_A,_V))
if mibBuilder.loadTexts:qtechRouteRedistributeEntry.setStatus(_B)
_QtechRouteRedistributeProtocolCfg_Type=QtechRouteProtoType
_QtechRouteRedistributeProtocolCfg_Object=MibTableColumn
qtechRouteRedistributeProtocolCfg=_QtechRouteRedistributeProtocolCfg_Object((1,3,6,1,4,1,27514,1,1,10,2,20,3,1,1,1),_QtechRouteRedistributeProtocolCfg_Type())
qtechRouteRedistributeProtocolCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRouteRedistributeProtocolCfg.setStatus(_B)
_QtechRouteRedistributeProtocol_Type=QtechRouteProtoType
_QtechRouteRedistributeProtocol_Object=MibTableColumn
qtechRouteRedistributeProtocol=_QtechRouteRedistributeProtocol_Object((1,3,6,1,4,1,27514,1,1,10,2,20,3,1,1,2),_QtechRouteRedistributeProtocol_Type())
qtechRouteRedistributeProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRouteRedistributeProtocol.setStatus(_B)
class _QtechRouteRedistributeMetricValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777214))
_QtechRouteRedistributeMetricValue_Type.__name__=_F
_QtechRouteRedistributeMetricValue_Object=MibTableColumn
qtechRouteRedistributeMetricValue=_QtechRouteRedistributeMetricValue_Object((1,3,6,1,4,1,27514,1,1,10,2,20,3,1,1,3),_QtechRouteRedistributeMetricValue_Type())
qtechRouteRedistributeMetricValue.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteRedistributeMetricValue.setStatus(_B)
class _QtechRouteRedistributeMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_QtechRouteRedistributeMetricType_Type.__name__=_E
_QtechRouteRedistributeMetricType_Object=MibTableColumn
qtechRouteRedistributeMetricType=_QtechRouteRedistributeMetricType_Object((1,3,6,1,4,1,27514,1,1,10,2,20,3,1,1,4),_QtechRouteRedistributeMetricType_Type())
qtechRouteRedistributeMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteRedistributeMetricType.setStatus(_B)
class _QtechRouteRedistributeTagValue_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_QtechRouteRedistributeTagValue_Type.__name__=_F
_QtechRouteRedistributeTagValue_Object=MibTableColumn
qtechRouteRedistributeTagValue=_QtechRouteRedistributeTagValue_Object((1,3,6,1,4,1,27514,1,1,10,2,20,3,1,1,5),_QtechRouteRedistributeTagValue_Type())
qtechRouteRedistributeTagValue.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteRedistributeTagValue.setStatus(_B)
class _QtechRouteRedistributeRouteMapName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechRouteRedistributeRouteMapName_Type.__name__=_G
_QtechRouteRedistributeRouteMapName_Object=MibTableColumn
qtechRouteRedistributeRouteMapName=_QtechRouteRedistributeRouteMapName_Object((1,3,6,1,4,1,27514,1,1,10,2,20,3,1,1,6),_QtechRouteRedistributeRouteMapName_Type())
qtechRouteRedistributeRouteMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteRedistributeRouteMapName.setStatus(_B)
_QtechRouteRedistributeStatus_Type=RowStatus
_QtechRouteRedistributeStatus_Object=MibTableColumn
qtechRouteRedistributeStatus=_QtechRouteRedistributeStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,20,3,1,1,7),_QtechRouteRedistributeStatus_Type())
qtechRouteRedistributeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRouteRedistributeStatus.setStatus(_B)
_QtechRouteFilteringMIBObjects_ObjectIdentity=ObjectIdentity
qtechRouteFilteringMIBObjects=_QtechRouteFilteringMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,20,4))
_QtechIpPrefixListTable_Object=MibTable
qtechIpPrefixListTable=_QtechIpPrefixListTable_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,1))
if mibBuilder.loadTexts:qtechIpPrefixListTable.setStatus(_B)
_QtechIpPrefixListEntry_Object=MibTableRow
qtechIpPrefixListEntry=_QtechIpPrefixListEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,1,1))
qtechIpPrefixListEntry.setIndexNames((0,_A,_W),(0,_A,_X))
if mibBuilder.loadTexts:qtechIpPrefixListEntry.setStatus(_B)
class _QtechIpPrefixListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechIpPrefixListName_Type.__name__=_G
_QtechIpPrefixListName_Object=MibTableColumn
qtechIpPrefixListName=_QtechIpPrefixListName_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,1,1,1),_QtechIpPrefixListName_Type())
qtechIpPrefixListName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIpPrefixListName.setStatus(_B)
class _QtechIpPrefixListSequence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechIpPrefixListSequence_Type.__name__=_F
_QtechIpPrefixListSequence_Object=MibTableColumn
qtechIpPrefixListSequence=_QtechIpPrefixListSequence_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,1,1,2),_QtechIpPrefixListSequence_Type())
qtechIpPrefixListSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIpPrefixListSequence.setStatus(_B)
class _QtechIpPrefixListOperMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),('deny',2)))
_QtechIpPrefixListOperMethod_Type.__name__=_E
_QtechIpPrefixListOperMethod_Object=MibTableColumn
qtechIpPrefixListOperMethod=_QtechIpPrefixListOperMethod_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,1,1,3),_QtechIpPrefixListOperMethod_Type())
qtechIpPrefixListOperMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpPrefixListOperMethod.setStatus(_B)
_QtechIpPrefixListIpAddress_Type=IpAddress
_QtechIpPrefixListIpAddress_Object=MibTableColumn
qtechIpPrefixListIpAddress=_QtechIpPrefixListIpAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,1,1,4),_QtechIpPrefixListIpAddress_Type())
qtechIpPrefixListIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpPrefixListIpAddress.setStatus(_B)
class _QtechIpPrefixListMaskLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_QtechIpPrefixListMaskLength_Type.__name__=_F
_QtechIpPrefixListMaskLength_Object=MibTableColumn
qtechIpPrefixListMaskLength=_QtechIpPrefixListMaskLength_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,1,1,5),_QtechIpPrefixListMaskLength_Type())
qtechIpPrefixListMaskLength.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpPrefixListMaskLength.setStatus(_B)
class _QtechIpPrefixListMinimumPrefixLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_QtechIpPrefixListMinimumPrefixLength_Type.__name__=_F
_QtechIpPrefixListMinimumPrefixLength_Object=MibTableColumn
qtechIpPrefixListMinimumPrefixLength=_QtechIpPrefixListMinimumPrefixLength_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,1,1,6),_QtechIpPrefixListMinimumPrefixLength_Type())
qtechIpPrefixListMinimumPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpPrefixListMinimumPrefixLength.setStatus(_B)
class _QtechIpPrefixListMaximumPrefixLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_QtechIpPrefixListMaximumPrefixLength_Type.__name__=_F
_QtechIpPrefixListMaximumPrefixLength_Object=MibTableColumn
qtechIpPrefixListMaximumPrefixLength=_QtechIpPrefixListMaximumPrefixLength_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,1,1,7),_QtechIpPrefixListMaximumPrefixLength_Type())
qtechIpPrefixListMaximumPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpPrefixListMaximumPrefixLength.setStatus(_B)
_QtechIpPrefixListStatus_Type=RowStatus
_QtechIpPrefixListStatus_Object=MibTableColumn
qtechIpPrefixListStatus=_QtechIpPrefixListStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,1,1,8),_QtechIpPrefixListStatus_Type())
qtechIpPrefixListStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpPrefixListStatus.setStatus(_B)
_QtechDistributeListTable_Object=MibTable
qtechDistributeListTable=_QtechDistributeListTable_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,2))
if mibBuilder.loadTexts:qtechDistributeListTable.setStatus(_B)
_QtechDistributeListEntry_Object=MibTableRow
qtechDistributeListEntry=_QtechDistributeListEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,2,1))
qtechDistributeListEntry.setIndexNames((0,_A,_Y),(0,_A,_Z),(0,_A,_a),(0,_A,_b))
if mibBuilder.loadTexts:qtechDistributeListEntry.setStatus(_B)
_QtechDistributeListCfgProtoType_Type=QtechRouteProtoType
_QtechDistributeListCfgProtoType_Object=MibTableColumn
qtechDistributeListCfgProtoType=_QtechDistributeListCfgProtoType_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,2,1,1),_QtechDistributeListCfgProtoType_Type())
qtechDistributeListCfgProtoType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDistributeListCfgProtoType.setStatus(_B)
_QtechDistributeListIfIndex_Type=Unsigned32
_QtechDistributeListIfIndex_Object=MibTableColumn
qtechDistributeListIfIndex=_QtechDistributeListIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,2,1,2),_QtechDistributeListIfIndex_Type())
qtechDistributeListIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDistributeListIfIndex.setStatus(_B)
class _QtechDistributeListDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('out',1),('in',2)))
_QtechDistributeListDirection_Type.__name__=_E
_QtechDistributeListDirection_Object=MibTableColumn
qtechDistributeListDirection=_QtechDistributeListDirection_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,2,1,3),_QtechDistributeListDirection_Type())
qtechDistributeListDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDistributeListDirection.setStatus(_B)
_QtechDistributeListFilteringProtocol_Type=Unsigned32
_QtechDistributeListFilteringProtocol_Object=MibTableColumn
qtechDistributeListFilteringProtocol=_QtechDistributeListFilteringProtocol_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,2,1,4),_QtechDistributeListFilteringProtocol_Type())
qtechDistributeListFilteringProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDistributeListFilteringProtocol.setStatus(_B)
class _QtechDistributeListFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('acl',1),('gateway',2),('prefix',3),('prefix-gateway',4)))
_QtechDistributeListFilterType_Type.__name__=_E
_QtechDistributeListFilterType_Object=MibTableColumn
qtechDistributeListFilterType=_QtechDistributeListFilterType_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,2,1,5),_QtechDistributeListFilterType_Type())
qtechDistributeListFilterType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDistributeListFilterType.setStatus(_B)
class _QtechDistributeListAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechDistributeListAclName_Type.__name__=_G
_QtechDistributeListAclName_Object=MibTableColumn
qtechDistributeListAclName=_QtechDistributeListAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,2,1,6),_QtechDistributeListAclName_Type())
qtechDistributeListAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDistributeListAclName.setStatus(_B)
class _QtechDistributeListGateWayIpPrefixName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechDistributeListGateWayIpPrefixName_Type.__name__=_G
_QtechDistributeListGateWayIpPrefixName_Object=MibTableColumn
qtechDistributeListGateWayIpPrefixName=_QtechDistributeListGateWayIpPrefixName_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,2,1,7),_QtechDistributeListGateWayIpPrefixName_Type())
qtechDistributeListGateWayIpPrefixName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDistributeListGateWayIpPrefixName.setStatus(_B)
class _QtechDistributeListPrefixIpPrefixName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechDistributeListPrefixIpPrefixName_Type.__name__=_G
_QtechDistributeListPrefixIpPrefixName_Object=MibTableColumn
qtechDistributeListPrefixIpPrefixName=_QtechDistributeListPrefixIpPrefixName_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,2,1,8),_QtechDistributeListPrefixIpPrefixName_Type())
qtechDistributeListPrefixIpPrefixName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDistributeListPrefixIpPrefixName.setStatus(_B)
_QtechDistributeListStatus_Type=RowStatus
_QtechDistributeListStatus_Object=MibTableColumn
qtechDistributeListStatus=_QtechDistributeListStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,20,4,2,1,9),_QtechDistributeListStatus_Type())
qtechDistributeListStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDistributeListStatus.setStatus(_B)
_QtechipCidrRouteExtendMIBObjects_ObjectIdentity=ObjectIdentity
qtechipCidrRouteExtendMIBObjects=_QtechipCidrRouteExtendMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,20,5))
_QtechipCidrRouteTable_Object=MibTable
qtechipCidrRouteTable=_QtechipCidrRouteTable_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1))
if mibBuilder.loadTexts:qtechipCidrRouteTable.setStatus(_B)
_QtechipCidrRouteEntry_Object=MibTableRow
qtechipCidrRouteEntry=_QtechipCidrRouteEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1))
qtechipCidrRouteEntry.setIndexNames((0,_A,_c),(0,_A,_d),(0,_A,_e),(0,_A,_f))
if mibBuilder.loadTexts:qtechipCidrRouteEntry.setStatus(_B)
_QtechipCidrRouteDest_Type=IpAddress
_QtechipCidrRouteDest_Object=MibTableColumn
qtechipCidrRouteDest=_QtechipCidrRouteDest_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,1),_QtechipCidrRouteDest_Type())
qtechipCidrRouteDest.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechipCidrRouteDest.setStatus(_B)
_QtechipCidrRouteMask_Type=IpAddress
_QtechipCidrRouteMask_Object=MibTableColumn
qtechipCidrRouteMask=_QtechipCidrRouteMask_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,2),_QtechipCidrRouteMask_Type())
qtechipCidrRouteMask.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechipCidrRouteMask.setStatus(_B)
_QtechipCidrRouteTos_Type=Integer32
_QtechipCidrRouteTos_Object=MibTableColumn
qtechipCidrRouteTos=_QtechipCidrRouteTos_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,3),_QtechipCidrRouteTos_Type())
qtechipCidrRouteTos.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechipCidrRouteTos.setStatus(_B)
_QtechipCidrRouteNextHop_Type=IpAddress
_QtechipCidrRouteNextHop_Object=MibTableColumn
qtechipCidrRouteNextHop=_QtechipCidrRouteNextHop_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,4),_QtechipCidrRouteNextHop_Type())
qtechipCidrRouteNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechipCidrRouteNextHop.setStatus(_B)
class _QtechipCidrRouteIfIndex_Type(Integer32):defaultValue=0
_QtechipCidrRouteIfIndex_Type.__name__=_E
_QtechipCidrRouteIfIndex_Object=MibTableColumn
qtechipCidrRouteIfIndex=_QtechipCidrRouteIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,5),_QtechipCidrRouteIfIndex_Type())
qtechipCidrRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechipCidrRouteIfIndex.setStatus(_B)
class _QtechipCidrRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('reject',2),(_K,3),('remote',4)))
_QtechipCidrRouteType_Type.__name__=_E
_QtechipCidrRouteType_Object=MibTableColumn
qtechipCidrRouteType=_QtechipCidrRouteType_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,6),_QtechipCidrRouteType_Type())
qtechipCidrRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechipCidrRouteType.setStatus(_B)
class _QtechipCidrRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_J,1),(_K,2),(_j,3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('isIs',9),('esIs',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14),('idpr',15),('ciscoEigrp',16),('policy',17)))
_QtechipCidrRouteProto_Type.__name__=_E
_QtechipCidrRouteProto_Object=MibTableColumn
qtechipCidrRouteProto=_QtechipCidrRouteProto_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,7),_QtechipCidrRouteProto_Type())
qtechipCidrRouteProto.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechipCidrRouteProto.setStatus(_B)
class _QtechipCidrRouteAge_Type(Integer32):defaultValue=0
_QtechipCidrRouteAge_Type.__name__=_E
_QtechipCidrRouteAge_Object=MibTableColumn
qtechipCidrRouteAge=_QtechipCidrRouteAge_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,8),_QtechipCidrRouteAge_Type())
qtechipCidrRouteAge.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechipCidrRouteAge.setStatus(_B)
_QtechipCidrRouteInfo_Type=ObjectIdentifier
_QtechipCidrRouteInfo_Object=MibTableColumn
qtechipCidrRouteInfo=_QtechipCidrRouteInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,9),_QtechipCidrRouteInfo_Type())
qtechipCidrRouteInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechipCidrRouteInfo.setStatus(_B)
class _QtechipCidrRouteNextHopAS_Type(Integer32):defaultValue=0
_QtechipCidrRouteNextHopAS_Type.__name__=_E
_QtechipCidrRouteNextHopAS_Object=MibTableColumn
qtechipCidrRouteNextHopAS=_QtechipCidrRouteNextHopAS_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,10),_QtechipCidrRouteNextHopAS_Type())
qtechipCidrRouteNextHopAS.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechipCidrRouteNextHopAS.setStatus(_B)
class _QtechipCidrRouteMetric1_Type(Integer32):defaultValue=-1
_QtechipCidrRouteMetric1_Type.__name__=_E
_QtechipCidrRouteMetric1_Object=MibTableColumn
qtechipCidrRouteMetric1=_QtechipCidrRouteMetric1_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,11),_QtechipCidrRouteMetric1_Type())
qtechipCidrRouteMetric1.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechipCidrRouteMetric1.setStatus(_B)
class _QtechipCidrRouteMetric2_Type(Integer32):defaultValue=-1
_QtechipCidrRouteMetric2_Type.__name__=_E
_QtechipCidrRouteMetric2_Object=MibTableColumn
qtechipCidrRouteMetric2=_QtechipCidrRouteMetric2_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,12),_QtechipCidrRouteMetric2_Type())
qtechipCidrRouteMetric2.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechipCidrRouteMetric2.setStatus(_B)
class _QtechipCidrRouteMetric3_Type(Integer32):defaultValue=-1
_QtechipCidrRouteMetric3_Type.__name__=_E
_QtechipCidrRouteMetric3_Object=MibTableColumn
qtechipCidrRouteMetric3=_QtechipCidrRouteMetric3_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,13),_QtechipCidrRouteMetric3_Type())
qtechipCidrRouteMetric3.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechipCidrRouteMetric3.setStatus(_B)
class _QtechipCidrRouteMetric4_Type(Integer32):defaultValue=-1
_QtechipCidrRouteMetric4_Type.__name__=_E
_QtechipCidrRouteMetric4_Object=MibTableColumn
qtechipCidrRouteMetric4=_QtechipCidrRouteMetric4_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,14),_QtechipCidrRouteMetric4_Type())
qtechipCidrRouteMetric4.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechipCidrRouteMetric4.setStatus(_B)
class _QtechipCidrRouteMetric5_Type(Integer32):defaultValue=-1
_QtechipCidrRouteMetric5_Type.__name__=_E
_QtechipCidrRouteMetric5_Object=MibTableColumn
qtechipCidrRouteMetric5=_QtechipCidrRouteMetric5_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,15),_QtechipCidrRouteMetric5_Type())
qtechipCidrRouteMetric5.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechipCidrRouteMetric5.setStatus(_B)
_QtechipCidrRouteStatus_Type=RowStatus
_QtechipCidrRouteStatus_Object=MibTableColumn
qtechipCidrRouteStatus=_QtechipCidrRouteStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,16),_QtechipCidrRouteStatus_Type())
qtechipCidrRouteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechipCidrRouteStatus.setStatus(_B)
class _QtechipCidrOspfRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('ospf-route',0),('ospf-ia-route',1),('ospf-n1-route',2),('ospf-n2-route',3),('ospf-e1-route',4),('ospf-e2-route',5)))
_QtechipCidrOspfRouteType_Type.__name__=_E
_QtechipCidrOspfRouteType_Object=MibTableColumn
qtechipCidrOspfRouteType=_QtechipCidrOspfRouteType_Object((1,3,6,1,4,1,27514,1,1,10,2,20,5,1,1,17),_QtechipCidrOspfRouteType_Type())
qtechipCidrOspfRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechipCidrOspfRouteType.setStatus(_B)
_QtechRouteMIBConformance_ObjectIdentity=ObjectIdentity
qtechRouteMIBConformance=_QtechRouteMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,20,6))
_QtechRouteMIBCompliances_ObjectIdentity=ObjectIdentity
qtechRouteMIBCompliances=_QtechRouteMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,20,6,1))
_QtechRouteMIBGroups_ObjectIdentity=ObjectIdentity
qtechRouteMIBGroups=_QtechRouteMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,20,6,2))
qtechRouteMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,20,6,2,1))
qtechRouteMIBGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:qtechRouteMIBGroup.setStatus(_B)
qtechRouteInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,20,6,2,2))
qtechRouteInfoMIBGroup.setObjects(*((_A,_L),(_A,_M),(_A,_p),(_A,_q),(_A,_N),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:qtechRouteInfoMIBGroup.setStatus(_B)
qtechRouteMapMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,20,6,2,3))
qtechRouteMapMIBGroup.setObjects(*((_A,_H),(_A,_I),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_g),(_A,_g),(_A,_A3),(_A,_R),(_A,_Q),(_A,_A4),(_A,_S),(_A,_A5),(_A,_T),(_A,_A6)))
if mibBuilder.loadTexts:qtechRouteMapMIBGroup.setStatus(_B)
qtechRouteRedistributeMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,20,6,2,4))
qtechRouteRedistributeMIBGroup.setObjects(*((_A,_U),(_A,_V),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:qtechRouteRedistributeMIBGroup.setStatus(_B)
qtechRouteFilteringMibGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,20,6,2,5))
qtechRouteFilteringMibGroup.setObjects(*((_A,_W),(_A,_X),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_Y),(_A,_Z),(_A,_AI),(_A,_a),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_b),(_A,_AM)))
if mibBuilder.loadTexts:qtechRouteFilteringMibGroup.setStatus(_B)
qtechipCidrRouteMibGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,20,6,2,6))
qtechipCidrRouteMibGroup.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:qtechipCidrRouteMibGroup.setStatus(_B)
qtechRouteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,20,6,1,1))
qtechRouteMIBCompliance.setObjects(*((_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:qtechRouteMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'QtechRouteProtoType':QtechRouteProtoType,'qtechRouteMIB':qtechRouteMIB,'qtechRouteMIBObjects':qtechRouteMIBObjects,_o:qtechRouteServiceStatus,'qtechRoutingProtoInfoTable':qtechRoutingProtoInfoTable,'qtechRoutingProtoInfoEntry':qtechRoutingProtoInfoEntry,_L:qtechRoutingProtoInfoProtoType,_M:qtechRoutingProtoInfoGateWay,_p:qtechRoutingProtoInfoDistance,_q:qtechRoutingProtoInfoLastUpdate,'qtechDefRoutingCfgTable':qtechDefRoutingCfgTable,'qtechDefRoutingCfgEntry':qtechDefRoutingCfgEntry,_N:qtechDefRoutingCfgRoutingProtoType,_r:qtechDefRoutingCfgAlways,_s:qtechDefRoutingCfgMetric,_t:qtechDefRoutingCfgMetricType,_u:qtechDefRoutingCfgRouteMap,_v:qtechDefRoutingCfgStatus,'qtechRouteMapMIBObjects':qtechRouteMapMIBObjects,'qtechRouteMapTable':qtechRouteMapTable,'qtechRouteMapEntry':qtechRouteMapEntry,_H:qtechRouteMapName,_I:qtechRouteMapSequenceNumber,_w:qtechRouteMapOperType,_x:qtechRouteMapMatchMetric,_y:qtechRouteMapMatchRouteType,_z:qtechRouteMapMetricValueType,_A0:qtechRouteMapSetMetric,_A1:qtechRouteMapSetLevel,_A2:qtechRouteMapSetMetricType,_g:qtechRouteMapSetNexthopSt,'qtechRouteMapSetNexthop':qtechRouteMapSetNexthop,_A3:qtechRouteMapStatus,'qtechRouteMapMatchIpAddressTable':qtechRouteMapMatchIpAddressTable,'qtechRouteMapMatchIpAddressEntry':qtechRouteMapMatchIpAddressEntry,_Q:qtechRouteMapMatchType,_R:qtechRouteMapMatchIpAddressAclName,_A4:qtechRouteMapMatchIpAddressStatus,'qtechRouteMapMatchTagTable':qtechRouteMapMatchTagTable,'qtechRouteMapMatchTagEntry':qtechRouteMapMatchTagEntry,_S:qtechRouteMapMatchTagValue,_A5:qtechRouteMapMatchTagStatus,'qtechRouteMapMatchInterfaceTable':qtechRouteMapMatchInterfaceTable,'qtechRouteMapMatchInterfaceEntry':qtechRouteMapMatchInterfaceEntry,_T:qtechRouteMapMatchInterfaceIfIndex,_A6:qtechRouteMapMatchInterfaceStatus,'qtechRouteRedistributeMIBObjects':qtechRouteRedistributeMIBObjects,'qtechRouteRedistributeTable':qtechRouteRedistributeTable,'qtechRouteRedistributeEntry':qtechRouteRedistributeEntry,_U:qtechRouteRedistributeProtocolCfg,_V:qtechRouteRedistributeProtocol,_A7:qtechRouteRedistributeMetricValue,_A8:qtechRouteRedistributeMetricType,_A9:qtechRouteRedistributeTagValue,_AA:qtechRouteRedistributeRouteMapName,_AB:qtechRouteRedistributeStatus,'qtechRouteFilteringMIBObjects':qtechRouteFilteringMIBObjects,'qtechIpPrefixListTable':qtechIpPrefixListTable,'qtechIpPrefixListEntry':qtechIpPrefixListEntry,_W:qtechIpPrefixListName,_X:qtechIpPrefixListSequence,_AC:qtechIpPrefixListOperMethod,_AD:qtechIpPrefixListIpAddress,_AE:qtechIpPrefixListMaskLength,_AF:qtechIpPrefixListMinimumPrefixLength,_AG:qtechIpPrefixListMaximumPrefixLength,_AH:qtechIpPrefixListStatus,'qtechDistributeListTable':qtechDistributeListTable,'qtechDistributeListEntry':qtechDistributeListEntry,_Y:qtechDistributeListCfgProtoType,_Z:qtechDistributeListIfIndex,_a:qtechDistributeListDirection,_b:qtechDistributeListFilteringProtocol,_AI:qtechDistributeListFilterType,_AJ:qtechDistributeListAclName,_AK:qtechDistributeListGateWayIpPrefixName,_AL:qtechDistributeListPrefixIpPrefixName,_AM:qtechDistributeListStatus,'qtechipCidrRouteExtendMIBObjects':qtechipCidrRouteExtendMIBObjects,'qtechipCidrRouteTable':qtechipCidrRouteTable,'qtechipCidrRouteEntry':qtechipCidrRouteEntry,_c:qtechipCidrRouteDest,_d:qtechipCidrRouteMask,_e:qtechipCidrRouteTos,_f:qtechipCidrRouteNextHop,_AN:qtechipCidrRouteIfIndex,_AO:qtechipCidrRouteType,_AP:qtechipCidrRouteProto,_AQ:qtechipCidrRouteAge,_AR:qtechipCidrRouteInfo,_AS:qtechipCidrRouteNextHopAS,_AT:qtechipCidrRouteMetric1,_AU:qtechipCidrRouteMetric2,_AV:qtechipCidrRouteMetric3,_AW:qtechipCidrRouteMetric4,_AX:qtechipCidrRouteMetric5,_AY:qtechipCidrRouteStatus,_AZ:qtechipCidrOspfRouteType,'qtechRouteMIBConformance':qtechRouteMIBConformance,'qtechRouteMIBCompliances':qtechRouteMIBCompliances,'qtechRouteMIBCompliance':qtechRouteMIBCompliance,'qtechRouteMIBGroups':qtechRouteMIBGroups,_Aa:qtechRouteMIBGroup,_Ab:qtechRouteInfoMIBGroup,_Ac:qtechRouteMapMIBGroup,_Ad:qtechRouteRedistributeMIBGroup,_Ae:qtechRouteFilteringMibGroup,_Af:qtechipCidrRouteMibGroup})