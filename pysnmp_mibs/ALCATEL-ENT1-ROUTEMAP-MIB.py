_m='alaRouteMapConfigMIBGroup'
_l='alaRouteMapRowStatus'
_k='alaRouteMapSequenceRowStatus'
_j='alaRouteMapSequenceAction'
_i='alaRouteMapNameRowStatus'
_h='alaRouteMapNameIndex'
_g='alaRouteMapAccessListRowStatus'
_f='alaRouteMapAccessListAction'
_e='alaRouteMapRedistStatus'
_d='alaRouteMapRedistRowStatus'
_c='alaRouteMapRedistAddressType'
_b='alaRouteMapAccessListRedistControl'
_a='alaRouteMapAccessListNameRowStatus'
_Z='alaRouteMapAccessListNameAddressType'
_Y='alaRouteMapAccessListNameIndex'
_X='alaRouteMapValue'
_W='alaRouteMapType'
_V='alaRouteMapSequence'
_U='alaRouteMapIndex'
_T='alaRouteMapSequenceNumber'
_S='alaRouteMapSequenceIndex'
_R='alaRouteMapName'
_Q='alaRouteMapAccessListPrefixLength'
_P='alaRouteMapAccessListAddress'
_O='alaRouteMapAccessListAddressType'
_N='alaRouteMapAccessListIndex'
_M='alaRouteMapAccessListName'
_L='ospfv3'
_K='alaRouteMapRedistRouteMapIndex'
_J='alaRouteMapRedistDestProtoId'
_I='alaRouteMapRedistSrcProtoId'
_H='read-only'
_G='Unsigned32'
_F='SnmpAdminString'
_E='Integer32'
_D='read-create'
_C='not-accessible'
_B='ALCATEL-ENT1-ROUTEMAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Iprm,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','routingIND1Iprm')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1RouteMapMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,3))
if mibBuilder.loadTexts:alcatelIND1RouteMapMIB.setRevisions(('2007-04-03 00:00',))
class AlaRouteMapType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,129,130,131,132,133,134,135,136)));namedValues=NamedValues(*(('matchIpAccesList',1),('matchIpAddress',2),('matchIpNextHopAccessList',3),('matchIpNextHopAddress',4),('matchIpv6AccessList',5),('matchIpv6Address',6),('matchIpv6nExtHopAccessList',7),('matchIpv6NextHopAddress',8),('matchTag',9),('matchIpv4Interface',10),('matchIpv6Interface',11),('matchMetric',12),('matchRouteType',13),('matchProtocol',14),('matchName',15),('setMetric',129),('setMetricType',130),('setTag',131),('setCommunity',132),('setLocalPreference',133),('setLevel',134),('setIpNexthop',135),('setIpv6Nexthop',136)))
class AlaRouteMapAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
class AlaRouteMapRedistControl(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('allSubnets',1),('noSubnets',2),('aggregate',3)))
_AlcatelIND1RouteMapMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1RouteMapMIBObjects=_AlcatelIND1RouteMapMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1))
_AlaRouteMapConfig_ObjectIdentity=ObjectIdentity
alaRouteMapConfig=_AlaRouteMapConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1))
_AlaRouteMapRedistProtoTable_Object=MibTable
alaRouteMapRedistProtoTable=_AlaRouteMapRedistProtoTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,1))
if mibBuilder.loadTexts:alaRouteMapRedistProtoTable.setStatus(_A)
_AlaRouteMapRedistProtoEntry_Object=MibTableRow
alaRouteMapRedistProtoEntry=_AlaRouteMapRedistProtoEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,1,1))
alaRouteMapRedistProtoEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:alaRouteMapRedistProtoEntry.setStatus(_A)
class _AlaRouteMapRedistSrcProtoId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('other',1),('local',2),('static',3),('rip',4),('ospf',5),('bgp',6),('ripng',7),(_L,8),('bgp6',9),('isis',10),('isis6',11),('import',12)))
_AlaRouteMapRedistSrcProtoId_Type.__name__=_E
_AlaRouteMapRedistSrcProtoId_Object=MibTableColumn
alaRouteMapRedistSrcProtoId=_AlaRouteMapRedistSrcProtoId_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,1,1,1),_AlaRouteMapRedistSrcProtoId_Type())
alaRouteMapRedistSrcProtoId.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapRedistSrcProtoId.setStatus(_A)
class _AlaRouteMapRedistDestProtoId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('rip',1),('ospf',2),('bgp',3),('ripng',4),(_L,5),('bgp6',6),('isis',7),('isis6',8)))
_AlaRouteMapRedistDestProtoId_Type.__name__=_E
_AlaRouteMapRedistDestProtoId_Object=MibTableColumn
alaRouteMapRedistDestProtoId=_AlaRouteMapRedistDestProtoId_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,1,1,2),_AlaRouteMapRedistDestProtoId_Type())
alaRouteMapRedistDestProtoId.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapRedistDestProtoId.setStatus(_A)
_AlaRouteMapRedistRouteMapIndex_Type=Unsigned32
_AlaRouteMapRedistRouteMapIndex_Object=MibTableColumn
alaRouteMapRedistRouteMapIndex=_AlaRouteMapRedistRouteMapIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,1,1,3),_AlaRouteMapRedistRouteMapIndex_Type())
alaRouteMapRedistRouteMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapRedistRouteMapIndex.setStatus(_A)
class _AlaRouteMapRedistStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AlaRouteMapRedistStatus_Type.__name__=_E
_AlaRouteMapRedistStatus_Object=MibTableColumn
alaRouteMapRedistStatus=_AlaRouteMapRedistStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,1,1,4),_AlaRouteMapRedistStatus_Type())
alaRouteMapRedistStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRouteMapRedistStatus.setStatus(_A)
_AlaRouteMapRedistAddressType_Type=InetAddressType
_AlaRouteMapRedistAddressType_Object=MibTableColumn
alaRouteMapRedistAddressType=_AlaRouteMapRedistAddressType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,1,1,5),_AlaRouteMapRedistAddressType_Type())
alaRouteMapRedistAddressType.setMaxAccess(_H)
if mibBuilder.loadTexts:alaRouteMapRedistAddressType.setStatus(_A)
_AlaRouteMapRedistRowStatus_Type=RowStatus
_AlaRouteMapRedistRowStatus_Object=MibTableColumn
alaRouteMapRedistRowStatus=_AlaRouteMapRedistRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,1,1,6),_AlaRouteMapRedistRowStatus_Type())
alaRouteMapRedistRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRouteMapRedistRowStatus.setStatus(_A)
_AlaRouteMapAccessListNameTable_Object=MibTable
alaRouteMapAccessListNameTable=_AlaRouteMapAccessListNameTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,2))
if mibBuilder.loadTexts:alaRouteMapAccessListNameTable.setStatus(_A)
_AlaRouteMapAccessListNameEntry_Object=MibTableRow
alaRouteMapAccessListNameEntry=_AlaRouteMapAccessListNameEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,2,1))
alaRouteMapAccessListNameEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:alaRouteMapAccessListNameEntry.setStatus(_A)
class _AlaRouteMapAccessListName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_AlaRouteMapAccessListName_Type.__name__=_F
_AlaRouteMapAccessListName_Object=MibTableColumn
alaRouteMapAccessListName=_AlaRouteMapAccessListName_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,2,1,1),_AlaRouteMapAccessListName_Type())
alaRouteMapAccessListName.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapAccessListName.setStatus(_A)
_AlaRouteMapAccessListNameIndex_Type=Unsigned32
_AlaRouteMapAccessListNameIndex_Object=MibTableColumn
alaRouteMapAccessListNameIndex=_AlaRouteMapAccessListNameIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,2,1,2),_AlaRouteMapAccessListNameIndex_Type())
alaRouteMapAccessListNameIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:alaRouteMapAccessListNameIndex.setStatus(_A)
_AlaRouteMapAccessListNameAddressType_Type=InetAddressType
_AlaRouteMapAccessListNameAddressType_Object=MibTableColumn
alaRouteMapAccessListNameAddressType=_AlaRouteMapAccessListNameAddressType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,2,1,3),_AlaRouteMapAccessListNameAddressType_Type())
alaRouteMapAccessListNameAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRouteMapAccessListNameAddressType.setStatus(_A)
_AlaRouteMapAccessListNameRowStatus_Type=RowStatus
_AlaRouteMapAccessListNameRowStatus_Object=MibTableColumn
alaRouteMapAccessListNameRowStatus=_AlaRouteMapAccessListNameRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,2,1,4),_AlaRouteMapAccessListNameRowStatus_Type())
alaRouteMapAccessListNameRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRouteMapAccessListNameRowStatus.setStatus(_A)
_AlaRouteMapAccessListTable_Object=MibTable
alaRouteMapAccessListTable=_AlaRouteMapAccessListTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,3))
if mibBuilder.loadTexts:alaRouteMapAccessListTable.setStatus(_A)
_AlaRouteMapAccessListEntry_Object=MibTableRow
alaRouteMapAccessListEntry=_AlaRouteMapAccessListEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,3,1))
alaRouteMapAccessListEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:alaRouteMapAccessListEntry.setStatus(_A)
class _AlaRouteMapAccessListIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaRouteMapAccessListIndex_Type.__name__=_G
_AlaRouteMapAccessListIndex_Object=MibTableColumn
alaRouteMapAccessListIndex=_AlaRouteMapAccessListIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,3,1,1),_AlaRouteMapAccessListIndex_Type())
alaRouteMapAccessListIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapAccessListIndex.setStatus(_A)
_AlaRouteMapAccessListAddressType_Type=InetAddressType
_AlaRouteMapAccessListAddressType_Object=MibTableColumn
alaRouteMapAccessListAddressType=_AlaRouteMapAccessListAddressType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,3,1,2),_AlaRouteMapAccessListAddressType_Type())
alaRouteMapAccessListAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapAccessListAddressType.setStatus(_A)
_AlaRouteMapAccessListAddress_Type=InetAddress
_AlaRouteMapAccessListAddress_Object=MibTableColumn
alaRouteMapAccessListAddress=_AlaRouteMapAccessListAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,3,1,3),_AlaRouteMapAccessListAddress_Type())
alaRouteMapAccessListAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapAccessListAddress.setStatus(_A)
class _AlaRouteMapAccessListPrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AlaRouteMapAccessListPrefixLength_Type.__name__=_E
_AlaRouteMapAccessListPrefixLength_Object=MibTableColumn
alaRouteMapAccessListPrefixLength=_AlaRouteMapAccessListPrefixLength_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,3,1,4),_AlaRouteMapAccessListPrefixLength_Type())
alaRouteMapAccessListPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapAccessListPrefixLength.setStatus(_A)
_AlaRouteMapAccessListRedistControl_Type=AlaRouteMapRedistControl
_AlaRouteMapAccessListRedistControl_Object=MibTableColumn
alaRouteMapAccessListRedistControl=_AlaRouteMapAccessListRedistControl_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,3,1,5),_AlaRouteMapAccessListRedistControl_Type())
alaRouteMapAccessListRedistControl.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRouteMapAccessListRedistControl.setStatus(_A)
_AlaRouteMapAccessListAction_Type=AlaRouteMapAction
_AlaRouteMapAccessListAction_Object=MibTableColumn
alaRouteMapAccessListAction=_AlaRouteMapAccessListAction_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,3,1,6),_AlaRouteMapAccessListAction_Type())
alaRouteMapAccessListAction.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRouteMapAccessListAction.setStatus(_A)
_AlaRouteMapAccessListRowStatus_Type=RowStatus
_AlaRouteMapAccessListRowStatus_Object=MibTableColumn
alaRouteMapAccessListRowStatus=_AlaRouteMapAccessListRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,3,1,7),_AlaRouteMapAccessListRowStatus_Type())
alaRouteMapAccessListRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRouteMapAccessListRowStatus.setStatus(_A)
_AlaRouteMapNameTable_Object=MibTable
alaRouteMapNameTable=_AlaRouteMapNameTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,4))
if mibBuilder.loadTexts:alaRouteMapNameTable.setStatus(_A)
_AlaRouteMapNameEntry_Object=MibTableRow
alaRouteMapNameEntry=_AlaRouteMapNameEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,4,1))
alaRouteMapNameEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:alaRouteMapNameEntry.setStatus(_A)
class _AlaRouteMapName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_AlaRouteMapName_Type.__name__=_F
_AlaRouteMapName_Object=MibTableColumn
alaRouteMapName=_AlaRouteMapName_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,4,1,1),_AlaRouteMapName_Type())
alaRouteMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapName.setStatus(_A)
_AlaRouteMapNameIndex_Type=Unsigned32
_AlaRouteMapNameIndex_Object=MibTableColumn
alaRouteMapNameIndex=_AlaRouteMapNameIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,4,1,2),_AlaRouteMapNameIndex_Type())
alaRouteMapNameIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:alaRouteMapNameIndex.setStatus(_A)
_AlaRouteMapNameRowStatus_Type=RowStatus
_AlaRouteMapNameRowStatus_Object=MibTableColumn
alaRouteMapNameRowStatus=_AlaRouteMapNameRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,4,1,3),_AlaRouteMapNameRowStatus_Type())
alaRouteMapNameRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRouteMapNameRowStatus.setStatus(_A)
_AlaRouteMapSequenceTable_Object=MibTable
alaRouteMapSequenceTable=_AlaRouteMapSequenceTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,5))
if mibBuilder.loadTexts:alaRouteMapSequenceTable.setStatus(_A)
_AlaRouteMapSequenceEntry_Object=MibTableRow
alaRouteMapSequenceEntry=_AlaRouteMapSequenceEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,5,1))
alaRouteMapSequenceEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:alaRouteMapSequenceEntry.setStatus(_A)
_AlaRouteMapSequenceIndex_Type=Unsigned32
_AlaRouteMapSequenceIndex_Object=MibTableColumn
alaRouteMapSequenceIndex=_AlaRouteMapSequenceIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,5,1,1),_AlaRouteMapSequenceIndex_Type())
alaRouteMapSequenceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapSequenceIndex.setStatus(_A)
class _AlaRouteMapSequenceNumber_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AlaRouteMapSequenceNumber_Type.__name__=_G
_AlaRouteMapSequenceNumber_Object=MibTableColumn
alaRouteMapSequenceNumber=_AlaRouteMapSequenceNumber_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,5,1,2),_AlaRouteMapSequenceNumber_Type())
alaRouteMapSequenceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapSequenceNumber.setStatus(_A)
_AlaRouteMapSequenceAction_Type=AlaRouteMapAction
_AlaRouteMapSequenceAction_Object=MibTableColumn
alaRouteMapSequenceAction=_AlaRouteMapSequenceAction_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,5,1,3),_AlaRouteMapSequenceAction_Type())
alaRouteMapSequenceAction.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRouteMapSequenceAction.setStatus(_A)
_AlaRouteMapSequenceRowStatus_Type=RowStatus
_AlaRouteMapSequenceRowStatus_Object=MibTableColumn
alaRouteMapSequenceRowStatus=_AlaRouteMapSequenceRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,5,1,4),_AlaRouteMapSequenceRowStatus_Type())
alaRouteMapSequenceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRouteMapSequenceRowStatus.setStatus(_A)
_AlaRouteMapTable_Object=MibTable
alaRouteMapTable=_AlaRouteMapTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,6))
if mibBuilder.loadTexts:alaRouteMapTable.setStatus(_A)
_AlaRouteMapEntry_Object=MibTableRow
alaRouteMapEntry=_AlaRouteMapEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,6,1))
alaRouteMapEntry.setIndexNames((0,_B,_U),(0,_B,_V),(0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:alaRouteMapEntry.setStatus(_A)
_AlaRouteMapIndex_Type=Unsigned32
_AlaRouteMapIndex_Object=MibTableColumn
alaRouteMapIndex=_AlaRouteMapIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,6,1,1),_AlaRouteMapIndex_Type())
alaRouteMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapIndex.setStatus(_A)
class _AlaRouteMapSequence_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AlaRouteMapSequence_Type.__name__=_G
_AlaRouteMapSequence_Object=MibTableColumn
alaRouteMapSequence=_AlaRouteMapSequence_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,6,1,2),_AlaRouteMapSequence_Type())
alaRouteMapSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapSequence.setStatus(_A)
_AlaRouteMapType_Type=AlaRouteMapType
_AlaRouteMapType_Object=MibTableColumn
alaRouteMapType=_AlaRouteMapType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,6,1,3),_AlaRouteMapType_Type())
alaRouteMapType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapType.setStatus(_A)
class _AlaRouteMapValue_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_AlaRouteMapValue_Type.__name__=_F
_AlaRouteMapValue_Object=MibTableColumn
alaRouteMapValue=_AlaRouteMapValue_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,6,1,4),_AlaRouteMapValue_Type())
alaRouteMapValue.setMaxAccess(_C)
if mibBuilder.loadTexts:alaRouteMapValue.setStatus(_A)
_AlaRouteMapRowStatus_Type=RowStatus
_AlaRouteMapRowStatus_Object=MibTableColumn
alaRouteMapRowStatus=_AlaRouteMapRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,1,1,6,1,5),_AlaRouteMapRowStatus_Type())
alaRouteMapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRouteMapRowStatus.setStatus(_A)
_AlcatelIND1RouteMapMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1RouteMapMIBConformance=_AlcatelIND1RouteMapMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,2))
_AlcatelIND1RouteMapMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1RouteMapMIBCompliances=_AlcatelIND1RouteMapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,2,1))
_AlcatelIND1RouteMapMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1RouteMapMIBGroups=_AlcatelIND1RouteMapMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,2,2))
alaRouteMapConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,2,2,1))
alaRouteMapConfigMIBGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:alaRouteMapConfigMIBGroup.setStatus(_A)
alaRouteMapCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,10,2,3,2,1,1))
alaRouteMapCompliance.setObjects((_B,_m))
if mibBuilder.loadTexts:alaRouteMapCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AlaRouteMapType':AlaRouteMapType,'AlaRouteMapAction':AlaRouteMapAction,'AlaRouteMapRedistControl':AlaRouteMapRedistControl,'alcatelIND1RouteMapMIB':alcatelIND1RouteMapMIB,'alcatelIND1RouteMapMIBObjects':alcatelIND1RouteMapMIBObjects,'alaRouteMapConfig':alaRouteMapConfig,'alaRouteMapRedistProtoTable':alaRouteMapRedistProtoTable,'alaRouteMapRedistProtoEntry':alaRouteMapRedistProtoEntry,_I:alaRouteMapRedistSrcProtoId,_J:alaRouteMapRedistDestProtoId,_K:alaRouteMapRedistRouteMapIndex,_e:alaRouteMapRedistStatus,_c:alaRouteMapRedistAddressType,_d:alaRouteMapRedistRowStatus,'alaRouteMapAccessListNameTable':alaRouteMapAccessListNameTable,'alaRouteMapAccessListNameEntry':alaRouteMapAccessListNameEntry,_M:alaRouteMapAccessListName,_Y:alaRouteMapAccessListNameIndex,_Z:alaRouteMapAccessListNameAddressType,_a:alaRouteMapAccessListNameRowStatus,'alaRouteMapAccessListTable':alaRouteMapAccessListTable,'alaRouteMapAccessListEntry':alaRouteMapAccessListEntry,_N:alaRouteMapAccessListIndex,_O:alaRouteMapAccessListAddressType,_P:alaRouteMapAccessListAddress,_Q:alaRouteMapAccessListPrefixLength,_b:alaRouteMapAccessListRedistControl,_f:alaRouteMapAccessListAction,_g:alaRouteMapAccessListRowStatus,'alaRouteMapNameTable':alaRouteMapNameTable,'alaRouteMapNameEntry':alaRouteMapNameEntry,_R:alaRouteMapName,_h:alaRouteMapNameIndex,_i:alaRouteMapNameRowStatus,'alaRouteMapSequenceTable':alaRouteMapSequenceTable,'alaRouteMapSequenceEntry':alaRouteMapSequenceEntry,_S:alaRouteMapSequenceIndex,_T:alaRouteMapSequenceNumber,_j:alaRouteMapSequenceAction,_k:alaRouteMapSequenceRowStatus,'alaRouteMapTable':alaRouteMapTable,'alaRouteMapEntry':alaRouteMapEntry,_U:alaRouteMapIndex,_V:alaRouteMapSequence,_W:alaRouteMapType,_X:alaRouteMapValue,_l:alaRouteMapRowStatus,'alcatelIND1RouteMapMIBConformance':alcatelIND1RouteMapMIBConformance,'alcatelIND1RouteMapMIBCompliances':alcatelIND1RouteMapMIBCompliances,'alaRouteMapCompliance':alaRouteMapCompliance,'alcatelIND1RouteMapMIBGroups':alcatelIND1RouteMapMIBGroups,_m:alaRouteMapConfigMIBGroup})