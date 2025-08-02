_A2='fsRMapTrapSeqNum'
_A1='fsRMapTrapName'
_A0='accessible-for-notify'
_z='enable'
_y='remote'
_x='fsRMapMatchOrigin'
_w='fsRMapMatchLocalPref'
_v='fsRMapMatchCommunity'
_u='fsRMapMatchASPathTag'
_t='fsRMapMatchRouteType'
_s='fsRMapMatchMetricType'
_r='fsRMapMatchTag'
_q='fsRMapMatchMetric'
_p='fsRMapMatchInterface'
_o='fsRMapMatchNextHopInetAddr'
_n='fsRMapMatchNextHopInetType'
_m='fsRMapMatchSourceInetPrefix'
_l='fsRMapMatchSourceInetAddress'
_k='fsRMapMatchSourceInetType'
_j='fsRMapMatchDestInetPrefix'
_i='fsRMapMatchDestInetAddress'
_h='fsRMapMatchDestInetType'
_g='fsRouteMapMatchLocalPreference'
_f='fsRouteMapMatchOrigin'
_e='fsRouteMapMatchCommunity'
_d='fsRouteMapMatchASPathTag'
_c='fsRouteMapMatchMetricType'
_b='fsRouteMapMatchRouteType'
_a='fsRouteMapMatchTag'
_Z='fsRouteMapMatchMetric'
_Y='fsRouteMapMatchIpNextHop'
_X='fsRouteMapMatchIpAddrMask'
_W='fsRouteMapMatchIpAddress'
_V='fsRouteMapMatchInterface'
_U='permit'
_T='internal'
_S='local'
_R='externaltype2'
_Q='externaltype1'
_P='fsRMapSeqNum'
_O='fsRMapName'
_N='incomplete'
_M='egp'
_L='igp'
_K='fsRouteMapSeqNum'
_J='fsRouteMapName'
_I='DisplayString'
_H='InetAddress'
_G='Unsigned32'
_F='Integer32'
_E='not-accessible'
_D='deprecated'
_C='read-write'
_B='SUPERMICRO-ROUTEMAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,'InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention')
futureroutemap=ModuleIdentity((1,3,6,1,4,1,10876,101,1,155))
if mibBuilder.loadTexts:futureroutemap.setRevisions(('2012-09-05 00:00',))
_FsRouteMap_ObjectIdentity=ObjectIdentity
fsRouteMap=_FsRouteMap_ObjectIdentity((1,3,6,1,4,1,10876,101,1,155,1))
_FsRouteMapTable_Object=MibTable
fsRouteMapTable=_FsRouteMapTable_Object((1,3,6,1,4,1,10876,101,1,155,1,1))
if mibBuilder.loadTexts:fsRouteMapTable.setStatus(_D)
_FsRouteMapEntry_Object=MibTableRow
fsRouteMapEntry=_FsRouteMapEntry_Object((1,3,6,1,4,1,10876,101,1,155,1,1,1))
fsRouteMapEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:fsRouteMapEntry.setStatus(_D)
class _FsRouteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FsRouteMapName_Type.__name__=_I
_FsRouteMapName_Object=MibTableColumn
fsRouteMapName=_FsRouteMapName_Object((1,3,6,1,4,1,10876,101,1,155,1,1,1,1),_FsRouteMapName_Type())
fsRouteMapName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapName.setStatus(_D)
class _FsRouteMapSeqNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsRouteMapSeqNum_Type.__name__=_G
_FsRouteMapSeqNum_Object=MibTableColumn
fsRouteMapSeqNum=_FsRouteMapSeqNum_Object((1,3,6,1,4,1,10876,101,1,155,1,1,1,2),_FsRouteMapSeqNum_Type())
fsRouteMapSeqNum.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapSeqNum.setStatus(_D)
class _FsRouteMapAccess_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),('deny',2)))
_FsRouteMapAccess_Type.__name__=_F
_FsRouteMapAccess_Object=MibTableColumn
fsRouteMapAccess=_FsRouteMapAccess_Object((1,3,6,1,4,1,10876,101,1,155,1,1,1,3),_FsRouteMapAccess_Type())
fsRouteMapAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapAccess.setStatus(_D)
_FsRouteMapRowStatus_Type=RowStatus
_FsRouteMapRowStatus_Object=MibTableColumn
fsRouteMapRowStatus=_FsRouteMapRowStatus_Object((1,3,6,1,4,1,10876,101,1,155,1,1,1,4),_FsRouteMapRowStatus_Type())
fsRouteMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapRowStatus.setStatus(_D)
_FsRouteMapMatchTable_Object=MibTable
fsRouteMapMatchTable=_FsRouteMapMatchTable_Object((1,3,6,1,4,1,10876,101,1,155,1,2))
if mibBuilder.loadTexts:fsRouteMapMatchTable.setStatus(_D)
_FsRouteMapMatchEntry_Object=MibTableRow
fsRouteMapMatchEntry=_FsRouteMapMatchEntry_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1))
fsRouteMapMatchEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_V),(0,_B,_W),(0,_B,_X),(0,_B,_Y),(0,_B,_Z),(0,_B,_a),(0,_B,_b),(0,_B,_c),(0,_B,_d),(0,_B,_e),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:fsRouteMapMatchEntry.setStatus(_D)
_FsRouteMapMatchInterface_Type=InterfaceIndex
_FsRouteMapMatchInterface_Object=MibTableColumn
fsRouteMapMatchInterface=_FsRouteMapMatchInterface_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1,1),_FsRouteMapMatchInterface_Type())
fsRouteMapMatchInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapMatchInterface.setStatus(_D)
_FsRouteMapMatchIpAddress_Type=IpAddress
_FsRouteMapMatchIpAddress_Object=MibTableColumn
fsRouteMapMatchIpAddress=_FsRouteMapMatchIpAddress_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1,2),_FsRouteMapMatchIpAddress_Type())
fsRouteMapMatchIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapMatchIpAddress.setStatus(_D)
_FsRouteMapMatchIpAddrMask_Type=IpAddress
_FsRouteMapMatchIpAddrMask_Object=MibTableColumn
fsRouteMapMatchIpAddrMask=_FsRouteMapMatchIpAddrMask_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1,3),_FsRouteMapMatchIpAddrMask_Type())
fsRouteMapMatchIpAddrMask.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapMatchIpAddrMask.setStatus(_D)
_FsRouteMapMatchIpNextHop_Type=IpAddress
_FsRouteMapMatchIpNextHop_Object=MibTableColumn
fsRouteMapMatchIpNextHop=_FsRouteMapMatchIpNextHop_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1,4),_FsRouteMapMatchIpNextHop_Type())
fsRouteMapMatchIpNextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapMatchIpNextHop.setStatus(_D)
class _FsRouteMapMatchMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsRouteMapMatchMetric_Type.__name__=_F
_FsRouteMapMatchMetric_Object=MibTableColumn
fsRouteMapMatchMetric=_FsRouteMapMatchMetric_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1,5),_FsRouteMapMatchMetric_Type())
fsRouteMapMatchMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapMatchMetric.setStatus(_D)
_FsRouteMapMatchTag_Type=Unsigned32
_FsRouteMapMatchTag_Object=MibTableColumn
fsRouteMapMatchTag=_FsRouteMapMatchTag_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1,6),_FsRouteMapMatchTag_Type())
fsRouteMapMatchTag.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapMatchTag.setStatus(_D)
class _FsRouteMapMatchRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,4)))
_FsRouteMapMatchRouteType_Type.__name__=_F
_FsRouteMapMatchRouteType_Object=MibTableColumn
fsRouteMapMatchRouteType=_FsRouteMapMatchRouteType_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1,7),_FsRouteMapMatchRouteType_Type())
fsRouteMapMatchRouteType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapMatchRouteType.setStatus(_D)
class _FsRouteMapMatchMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_T,3)))
_FsRouteMapMatchMetricType_Type.__name__=_F
_FsRouteMapMatchMetricType_Object=MibTableColumn
fsRouteMapMatchMetricType=_FsRouteMapMatchMetricType_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1,8),_FsRouteMapMatchMetricType_Type())
fsRouteMapMatchMetricType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapMatchMetricType.setStatus(_D)
class _FsRouteMapMatchASPathTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsRouteMapMatchASPathTag_Type.__name__=_G
_FsRouteMapMatchASPathTag_Object=MibTableColumn
fsRouteMapMatchASPathTag=_FsRouteMapMatchASPathTag_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1,9),_FsRouteMapMatchASPathTag_Type())
fsRouteMapMatchASPathTag.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapMatchASPathTag.setStatus(_D)
_FsRouteMapMatchCommunity_Type=Unsigned32
_FsRouteMapMatchCommunity_Object=MibTableColumn
fsRouteMapMatchCommunity=_FsRouteMapMatchCommunity_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1,10),_FsRouteMapMatchCommunity_Type())
fsRouteMapMatchCommunity.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapMatchCommunity.setStatus(_D)
class _FsRouteMapMatchOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_FsRouteMapMatchOrigin_Type.__name__=_F
_FsRouteMapMatchOrigin_Object=MibTableColumn
fsRouteMapMatchOrigin=_FsRouteMapMatchOrigin_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1,11),_FsRouteMapMatchOrigin_Type())
fsRouteMapMatchOrigin.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapMatchOrigin.setStatus(_D)
class _FsRouteMapMatchLocalPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214748367))
_FsRouteMapMatchLocalPreference_Type.__name__=_F
_FsRouteMapMatchLocalPreference_Object=MibTableColumn
fsRouteMapMatchLocalPreference=_FsRouteMapMatchLocalPreference_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1,12),_FsRouteMapMatchLocalPreference_Type())
fsRouteMapMatchLocalPreference.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRouteMapMatchLocalPreference.setStatus(_D)
_FsRouteMapMatchRowStatus_Type=RowStatus
_FsRouteMapMatchRowStatus_Object=MibTableColumn
fsRouteMapMatchRowStatus=_FsRouteMapMatchRowStatus_Object((1,3,6,1,4,1,10876,101,1,155,1,2,1,13),_FsRouteMapMatchRowStatus_Type())
fsRouteMapMatchRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapMatchRowStatus.setStatus(_D)
_FsRouteMapSetTable_Object=MibTable
fsRouteMapSetTable=_FsRouteMapSetTable_Object((1,3,6,1,4,1,10876,101,1,155,1,3))
if mibBuilder.loadTexts:fsRouteMapSetTable.setStatus(_D)
_FsRouteMapSetEntry_Object=MibTableRow
fsRouteMapSetEntry=_FsRouteMapSetEntry_Object((1,3,6,1,4,1,10876,101,1,155,1,3,1))
fsRouteMapSetEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:fsRouteMapSetEntry.setStatus(_D)
_FsRouteMapSetInterface_Type=InterfaceIndex
_FsRouteMapSetInterface_Object=MibTableColumn
fsRouteMapSetInterface=_FsRouteMapSetInterface_Object((1,3,6,1,4,1,10876,101,1,155,1,3,1,1),_FsRouteMapSetInterface_Type())
fsRouteMapSetInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetInterface.setStatus(_D)
_FsRouteMapSetIpNextHop_Type=IpAddress
_FsRouteMapSetIpNextHop_Object=MibTableColumn
fsRouteMapSetIpNextHop=_FsRouteMapSetIpNextHop_Object((1,3,6,1,4,1,10876,101,1,155,1,3,1,2),_FsRouteMapSetIpNextHop_Type())
fsRouteMapSetIpNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetIpNextHop.setStatus(_D)
_FsRouteMapSetMetric_Type=Integer32
_FsRouteMapSetMetric_Object=MibTableColumn
fsRouteMapSetMetric=_FsRouteMapSetMetric_Object((1,3,6,1,4,1,10876,101,1,155,1,3,1,3),_FsRouteMapSetMetric_Type())
fsRouteMapSetMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetMetric.setStatus(_D)
class _FsRouteMapSetTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214748367))
_FsRouteMapSetTag_Type.__name__=_G
_FsRouteMapSetTag_Object=MibTableColumn
fsRouteMapSetTag=_FsRouteMapSetTag_Object((1,3,6,1,4,1,10876,101,1,155,1,3,1,4),_FsRouteMapSetTag_Type())
fsRouteMapSetTag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetTag.setStatus(_D)
class _FsRouteMapSetMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_T,3)))
_FsRouteMapSetMetricType_Type.__name__=_F
_FsRouteMapSetMetricType_Object=MibTableColumn
fsRouteMapSetMetricType=_FsRouteMapSetMetricType_Object((1,3,6,1,4,1,10876,101,1,155,1,3,1,5),_FsRouteMapSetMetricType_Type())
fsRouteMapSetMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetMetricType.setStatus(_D)
class _FsRouteMapSetASPathTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsRouteMapSetASPathTag_Type.__name__=_G
_FsRouteMapSetASPathTag_Object=MibTableColumn
fsRouteMapSetASPathTag=_FsRouteMapSetASPathTag_Object((1,3,6,1,4,1,10876,101,1,155,1,3,1,6),_FsRouteMapSetASPathTag_Type())
fsRouteMapSetASPathTag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetASPathTag.setStatus(_D)
_FsRouteMapSetCommunity_Type=Unsigned32
_FsRouteMapSetCommunity_Object=MibTableColumn
fsRouteMapSetCommunity=_FsRouteMapSetCommunity_Object((1,3,6,1,4,1,10876,101,1,155,1,3,1,7),_FsRouteMapSetCommunity_Type())
fsRouteMapSetCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetCommunity.setStatus(_D)
class _FsRouteMapSetOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_FsRouteMapSetOrigin_Type.__name__=_F
_FsRouteMapSetOrigin_Object=MibTableColumn
fsRouteMapSetOrigin=_FsRouteMapSetOrigin_Object((1,3,6,1,4,1,10876,101,1,155,1,3,1,8),_FsRouteMapSetOrigin_Type())
fsRouteMapSetOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetOrigin.setStatus(_D)
class _FsRouteMapSetOriginASNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsRouteMapSetOriginASNum_Type.__name__=_G
_FsRouteMapSetOriginASNum_Object=MibTableColumn
fsRouteMapSetOriginASNum=_FsRouteMapSetOriginASNum_Object((1,3,6,1,4,1,10876,101,1,155,1,3,1,9),_FsRouteMapSetOriginASNum_Type())
fsRouteMapSetOriginASNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetOriginASNum.setStatus(_D)
class _FsRouteMapSetLocalPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214748367))
_FsRouteMapSetLocalPreference_Type.__name__=_F
_FsRouteMapSetLocalPreference_Object=MibTableColumn
fsRouteMapSetLocalPreference=_FsRouteMapSetLocalPreference_Object((1,3,6,1,4,1,10876,101,1,155,1,3,1,10),_FsRouteMapSetLocalPreference_Type())
fsRouteMapSetLocalPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetLocalPreference.setStatus(_D)
_FsRouteMapSetRowStatus_Type=RowStatus
_FsRouteMapSetRowStatus_Object=MibTableColumn
fsRouteMapSetRowStatus=_FsRouteMapSetRowStatus_Object((1,3,6,1,4,1,10876,101,1,155,1,3,1,11),_FsRouteMapSetRowStatus_Type())
fsRouteMapSetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRouteMapSetRowStatus.setStatus(_D)
_FsRMapGroup_ObjectIdentity=ObjectIdentity
fsRMapGroup=_FsRMapGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,155,2))
_FsRMapTable_Object=MibTable
fsRMapTable=_FsRMapTable_Object((1,3,6,1,4,1,10876,101,1,155,2,1))
if mibBuilder.loadTexts:fsRMapTable.setStatus(_A)
_FsRMapEntry_Object=MibTableRow
fsRMapEntry=_FsRMapEntry_Object((1,3,6,1,4,1,10876,101,1,155,2,1,1))
fsRMapEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:fsRMapEntry.setStatus(_A)
class _FsRMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FsRMapName_Type.__name__=_I
_FsRMapName_Object=MibTableColumn
fsRMapName=_FsRMapName_Object((1,3,6,1,4,1,10876,101,1,155,2,1,1,1),_FsRMapName_Type())
fsRMapName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapName.setStatus(_A)
class _FsRMapSeqNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsRMapSeqNum_Type.__name__=_G
_FsRMapSeqNum_Object=MibTableColumn
fsRMapSeqNum=_FsRMapSeqNum_Object((1,3,6,1,4,1,10876,101,1,155,2,1,1,2),_FsRMapSeqNum_Type())
fsRMapSeqNum.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapSeqNum.setStatus(_A)
class _FsRMapAccess_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),('deny',2)))
_FsRMapAccess_Type.__name__=_F
_FsRMapAccess_Object=MibTableColumn
fsRMapAccess=_FsRMapAccess_Object((1,3,6,1,4,1,10876,101,1,155,2,1,1,3),_FsRMapAccess_Type())
fsRMapAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapAccess.setStatus(_A)
_FsRMapRowStatus_Type=RowStatus
_FsRMapRowStatus_Object=MibTableColumn
fsRMapRowStatus=_FsRMapRowStatus_Object((1,3,6,1,4,1,10876,101,1,155,2,1,1,4),_FsRMapRowStatus_Type())
fsRMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapRowStatus.setStatus(_A)
class _FsRMapIsIpPrefixList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('true',1))
_FsRMapIsIpPrefixList_Type.__name__=_F
_FsRMapIsIpPrefixList_Object=MibTableColumn
fsRMapIsIpPrefixList=_FsRMapIsIpPrefixList_Object((1,3,6,1,4,1,10876,101,1,155,2,1,1,5),_FsRMapIsIpPrefixList_Type())
fsRMapIsIpPrefixList.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapIsIpPrefixList.setStatus(_A)
_FsRMapMatchTable_Object=MibTable
fsRMapMatchTable=_FsRMapMatchTable_Object((1,3,6,1,4,1,10876,101,1,155,2,2))
if mibBuilder.loadTexts:fsRMapMatchTable.setStatus(_A)
_FsRMapMatchEntry_Object=MibTableRow
fsRMapMatchEntry=_FsRMapMatchEntry_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1))
fsRMapMatchEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_h),(0,_B,_i),(0,_B,_j),(0,_B,_k),(0,_B,_l),(0,_B,_m),(0,_B,_n),(0,_B,_o),(0,_B,_p),(0,_B,_q),(0,_B,_r),(0,_B,_s),(0,_B,_t),(0,_B,_u),(0,_B,_v),(0,_B,_w),(0,_B,_x))
if mibBuilder.loadTexts:fsRMapMatchEntry.setStatus(_A)
_FsRMapMatchDestInetType_Type=InetAddressType
_FsRMapMatchDestInetType_Object=MibTableColumn
fsRMapMatchDestInetType=_FsRMapMatchDestInetType_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,1),_FsRMapMatchDestInetType_Type())
fsRMapMatchDestInetType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchDestInetType.setStatus(_A)
class _FsRMapMatchDestInetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_FsRMapMatchDestInetAddress_Type.__name__=_H
_FsRMapMatchDestInetAddress_Object=MibTableColumn
fsRMapMatchDestInetAddress=_FsRMapMatchDestInetAddress_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,2),_FsRMapMatchDestInetAddress_Type())
fsRMapMatchDestInetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchDestInetAddress.setStatus(_A)
_FsRMapMatchDestInetPrefix_Type=InetAddressPrefixLength
_FsRMapMatchDestInetPrefix_Object=MibTableColumn
fsRMapMatchDestInetPrefix=_FsRMapMatchDestInetPrefix_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,3),_FsRMapMatchDestInetPrefix_Type())
fsRMapMatchDestInetPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchDestInetPrefix.setStatus(_A)
_FsRMapMatchSourceInetType_Type=InetAddressType
_FsRMapMatchSourceInetType_Object=MibTableColumn
fsRMapMatchSourceInetType=_FsRMapMatchSourceInetType_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,4),_FsRMapMatchSourceInetType_Type())
fsRMapMatchSourceInetType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchSourceInetType.setStatus(_A)
class _FsRMapMatchSourceInetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_FsRMapMatchSourceInetAddress_Type.__name__=_H
_FsRMapMatchSourceInetAddress_Object=MibTableColumn
fsRMapMatchSourceInetAddress=_FsRMapMatchSourceInetAddress_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,5),_FsRMapMatchSourceInetAddress_Type())
fsRMapMatchSourceInetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchSourceInetAddress.setStatus(_A)
_FsRMapMatchSourceInetPrefix_Type=InetAddressPrefixLength
_FsRMapMatchSourceInetPrefix_Object=MibTableColumn
fsRMapMatchSourceInetPrefix=_FsRMapMatchSourceInetPrefix_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,6),_FsRMapMatchSourceInetPrefix_Type())
fsRMapMatchSourceInetPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchSourceInetPrefix.setStatus(_A)
_FsRMapMatchNextHopInetType_Type=InetAddressType
_FsRMapMatchNextHopInetType_Object=MibTableColumn
fsRMapMatchNextHopInetType=_FsRMapMatchNextHopInetType_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,7),_FsRMapMatchNextHopInetType_Type())
fsRMapMatchNextHopInetType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchNextHopInetType.setStatus(_A)
class _FsRMapMatchNextHopInetAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_FsRMapMatchNextHopInetAddr_Type.__name__=_H
_FsRMapMatchNextHopInetAddr_Object=MibTableColumn
fsRMapMatchNextHopInetAddr=_FsRMapMatchNextHopInetAddr_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,8),_FsRMapMatchNextHopInetAddr_Type())
fsRMapMatchNextHopInetAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchNextHopInetAddr.setStatus(_A)
_FsRMapMatchInterface_Type=InterfaceIndex
_FsRMapMatchInterface_Object=MibTableColumn
fsRMapMatchInterface=_FsRMapMatchInterface_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,9),_FsRMapMatchInterface_Type())
fsRMapMatchInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchInterface.setStatus(_A)
class _FsRMapMatchMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsRMapMatchMetric_Type.__name__=_F
_FsRMapMatchMetric_Object=MibTableColumn
fsRMapMatchMetric=_FsRMapMatchMetric_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,10),_FsRMapMatchMetric_Type())
fsRMapMatchMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchMetric.setStatus(_A)
_FsRMapMatchTag_Type=Unsigned32
_FsRMapMatchTag_Object=MibTableColumn
fsRMapMatchTag=_FsRMapMatchTag_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,11),_FsRMapMatchTag_Type())
fsRMapMatchTag.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchTag.setStatus(_A)
class _FsRMapMatchMetricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('intraarea',1),('interarea',2),('type1ext',3),('type2ext',4)))
_FsRMapMatchMetricType_Type.__name__=_F
_FsRMapMatchMetricType_Object=MibTableColumn
fsRMapMatchMetricType=_FsRMapMatchMetricType_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,12),_FsRMapMatchMetricType_Type())
fsRMapMatchMetricType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchMetricType.setStatus(_A)
class _FsRMapMatchRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_S,3),(_y,4)))
_FsRMapMatchRouteType_Type.__name__=_F
_FsRMapMatchRouteType_Object=MibTableColumn
fsRMapMatchRouteType=_FsRMapMatchRouteType_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,13),_FsRMapMatchRouteType_Type())
fsRMapMatchRouteType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchRouteType.setStatus(_A)
class _FsRMapMatchASPathTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsRMapMatchASPathTag_Type.__name__=_G
_FsRMapMatchASPathTag_Object=MibTableColumn
fsRMapMatchASPathTag=_FsRMapMatchASPathTag_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,14),_FsRMapMatchASPathTag_Type())
fsRMapMatchASPathTag.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchASPathTag.setStatus(_A)
_FsRMapMatchCommunity_Type=Unsigned32
_FsRMapMatchCommunity_Object=MibTableColumn
fsRMapMatchCommunity=_FsRMapMatchCommunity_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,15),_FsRMapMatchCommunity_Type())
fsRMapMatchCommunity.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchCommunity.setStatus(_A)
class _FsRMapMatchLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214748367))
_FsRMapMatchLocalPref_Type.__name__=_F
_FsRMapMatchLocalPref_Object=MibTableColumn
fsRMapMatchLocalPref=_FsRMapMatchLocalPref_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,16),_FsRMapMatchLocalPref_Type())
fsRMapMatchLocalPref.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchLocalPref.setStatus(_A)
class _FsRMapMatchOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_FsRMapMatchOrigin_Type.__name__=_F
_FsRMapMatchOrigin_Object=MibTableColumn
fsRMapMatchOrigin=_FsRMapMatchOrigin_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,17),_FsRMapMatchOrigin_Type())
fsRMapMatchOrigin.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRMapMatchOrigin.setStatus(_A)
_FsRMapMatchRowStatus_Type=RowStatus
_FsRMapMatchRowStatus_Object=MibTableColumn
fsRMapMatchRowStatus=_FsRMapMatchRowStatus_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,18),_FsRMapMatchRowStatus_Type())
fsRMapMatchRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapMatchRowStatus.setStatus(_A)
_FsRMapMatchDestMaxPrefixLen_Type=Unsigned32
_FsRMapMatchDestMaxPrefixLen_Object=MibTableColumn
fsRMapMatchDestMaxPrefixLen=_FsRMapMatchDestMaxPrefixLen_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,19),_FsRMapMatchDestMaxPrefixLen_Type())
fsRMapMatchDestMaxPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapMatchDestMaxPrefixLen.setStatus(_A)
_FsRMapMatchDestMinPrefixLen_Type=Unsigned32
_FsRMapMatchDestMinPrefixLen_Object=MibTableColumn
fsRMapMatchDestMinPrefixLen=_FsRMapMatchDestMinPrefixLen_Object((1,3,6,1,4,1,10876,101,1,155,2,2,1,20),_FsRMapMatchDestMinPrefixLen_Type())
fsRMapMatchDestMinPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapMatchDestMinPrefixLen.setStatus(_A)
_FsRMapSetTable_Object=MibTable
fsRMapSetTable=_FsRMapSetTable_Object((1,3,6,1,4,1,10876,101,1,155,2,3))
if mibBuilder.loadTexts:fsRMapSetTable.setStatus(_A)
_FsRMapSetEntry_Object=MibTableRow
fsRMapSetEntry=_FsRMapSetEntry_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1))
fsRMapSetEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:fsRMapSetEntry.setStatus(_A)
_FsRMapSetNextHopInetType_Type=InetAddressType
_FsRMapSetNextHopInetType_Object=MibTableColumn
fsRMapSetNextHopInetType=_FsRMapSetNextHopInetType_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,1),_FsRMapSetNextHopInetType_Type())
fsRMapSetNextHopInetType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetNextHopInetType.setStatus(_A)
_FsRMapSetNextHopInetAddr_Type=InetAddress
_FsRMapSetNextHopInetAddr_Object=MibTableColumn
fsRMapSetNextHopInetAddr=_FsRMapSetNextHopInetAddr_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,2),_FsRMapSetNextHopInetAddr_Type())
fsRMapSetNextHopInetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetNextHopInetAddr.setStatus(_A)
_FsRMapSetInterface_Type=InterfaceIndex
_FsRMapSetInterface_Object=MibTableColumn
fsRMapSetInterface=_FsRMapSetInterface_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,3),_FsRMapSetInterface_Type())
fsRMapSetInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetInterface.setStatus(_A)
_FsRMapSetMetric_Type=Integer32
_FsRMapSetMetric_Object=MibTableColumn
fsRMapSetMetric=_FsRMapSetMetric_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,4),_FsRMapSetMetric_Type())
fsRMapSetMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetMetric.setStatus(_A)
class _FsRMapSetTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214748367))
_FsRMapSetTag_Type.__name__=_G
_FsRMapSetTag_Object=MibTableColumn
fsRMapSetTag=_FsRMapSetTag_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,5),_FsRMapSetTag_Type())
fsRMapSetTag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetTag.setStatus(_A)
class _FsRMapSetRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_S,3),(_y,4)))
_FsRMapSetRouteType_Type.__name__=_F
_FsRMapSetRouteType_Object=MibTableColumn
fsRMapSetRouteType=_FsRMapSetRouteType_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,6),_FsRMapSetRouteType_Type())
fsRMapSetRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetRouteType.setStatus(_A)
class _FsRMapSetASPathTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsRMapSetASPathTag_Type.__name__=_G
_FsRMapSetASPathTag_Object=MibTableColumn
fsRMapSetASPathTag=_FsRMapSetASPathTag_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,7),_FsRMapSetASPathTag_Type())
fsRMapSetASPathTag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetASPathTag.setStatus(_A)
_FsRMapSetCommunity_Type=Unsigned32
_FsRMapSetCommunity_Object=MibTableColumn
fsRMapSetCommunity=_FsRMapSetCommunity_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,8),_FsRMapSetCommunity_Type())
fsRMapSetCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetCommunity.setStatus(_A)
class _FsRMapSetLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,214748367))
_FsRMapSetLocalPref_Type.__name__=_F
_FsRMapSetLocalPref_Object=MibTableColumn
fsRMapSetLocalPref=_FsRMapSetLocalPref_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,9),_FsRMapSetLocalPref_Type())
fsRMapSetLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetLocalPref.setStatus(_A)
class _FsRMapSetOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_FsRMapSetOrigin_Type.__name__=_F
_FsRMapSetOrigin_Object=MibTableColumn
fsRMapSetOrigin=_FsRMapSetOrigin_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,10),_FsRMapSetOrigin_Type())
fsRMapSetOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetOrigin.setStatus(_A)
class _FsRMapSetWeight_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsRMapSetWeight_Type.__name__=_G
_FsRMapSetWeight_Object=MibTableColumn
fsRMapSetWeight=_FsRMapSetWeight_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,11),_FsRMapSetWeight_Type())
fsRMapSetWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetWeight.setStatus(_A)
class _FsRMapSetEnableAutoTag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_z,1),('disable',2)))
_FsRMapSetEnableAutoTag_Type.__name__=_F
_FsRMapSetEnableAutoTag_Object=MibTableColumn
fsRMapSetEnableAutoTag=_FsRMapSetEnableAutoTag_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,12),_FsRMapSetEnableAutoTag_Type())
fsRMapSetEnableAutoTag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetEnableAutoTag.setStatus(_A)
class _FsRMapSetLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('level1',1),('level2',2),('level12',3),('stubarea',4),('backbone',5)))
_FsRMapSetLevel_Type.__name__=_F
_FsRMapSetLevel_Object=MibTableColumn
fsRMapSetLevel=_FsRMapSetLevel_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,13),_FsRMapSetLevel_Type())
fsRMapSetLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetLevel.setStatus(_A)
_FsRMapSetRowStatus_Type=RowStatus
_FsRMapSetRowStatus_Object=MibTableColumn
fsRMapSetRowStatus=_FsRMapSetRowStatus_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,14),_FsRMapSetRowStatus_Type())
fsRMapSetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetRowStatus.setStatus(_A)
class _FsRMapSetExtCommId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsRMapSetExtCommId_Type.__name__=_G
_FsRMapSetExtCommId_Object=MibTableColumn
fsRMapSetExtCommId=_FsRMapSetExtCommId_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,15),_FsRMapSetExtCommId_Type())
fsRMapSetExtCommId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetExtCommId.setStatus(_A)
_FsRMapSetExtCommPOI_Type=Unsigned32
_FsRMapSetExtCommPOI_Object=MibTableColumn
fsRMapSetExtCommPOI=_FsRMapSetExtCommPOI_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,16),_FsRMapSetExtCommPOI_Type())
fsRMapSetExtCommPOI.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsRMapSetExtCommPOI.setStatus(_A)
_FsRMapSetExtCommCost_Type=Unsigned32
_FsRMapSetExtCommCost_Object=MibTableColumn
fsRMapSetExtCommCost=_FsRMapSetExtCommCost_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,17),_FsRMapSetExtCommCost_Type())
fsRMapSetExtCommCost.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetExtCommCost.setStatus(_A)
class _FsRMapSetCommunityAdditive_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('replace',1),('additive',2)))
_FsRMapSetCommunityAdditive_Type.__name__=_F
_FsRMapSetCommunityAdditive_Object=MibTableColumn
fsRMapSetCommunityAdditive=_FsRMapSetCommunityAdditive_Object((1,3,6,1,4,1,10876,101,1,155,2,3,1,18),_FsRMapSetCommunityAdditive_Type())
fsRMapSetCommunityAdditive.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRMapSetCommunityAdditive.setStatus(_A)
_FsRMapTrapCfgGroup_ObjectIdentity=ObjectIdentity
fsRMapTrapCfgGroup=_FsRMapTrapCfgGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,155,3))
class _FsRmapTrapCfgEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_z,1),('disable',2)))
_FsRmapTrapCfgEnable_Type.__name__=_F
_FsRmapTrapCfgEnable_Object=MibScalar
fsRmapTrapCfgEnable=_FsRmapTrapCfgEnable_Object((1,3,6,1,4,1,10876,101,1,155,3,1),_FsRmapTrapCfgEnable_Type())
fsRmapTrapCfgEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRmapTrapCfgEnable.setStatus(_A)
_FsRMapTrapGroup_ObjectIdentity=ObjectIdentity
fsRMapTrapGroup=_FsRMapTrapGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,155,4))
_FsRMapTrapNotifications_ObjectIdentity=ObjectIdentity
fsRMapTrapNotifications=_FsRMapTrapNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,1,155,4,0))
class _FsRMapTrapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FsRMapTrapName_Type.__name__=_I
_FsRMapTrapName_Object=MibScalar
fsRMapTrapName=_FsRMapTrapName_Object((1,3,6,1,4,1,10876,101,1,155,4,1),_FsRMapTrapName_Type())
fsRMapTrapName.setMaxAccess(_A0)
if mibBuilder.loadTexts:fsRMapTrapName.setStatus(_A)
class _FsRMapTrapSeqNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsRMapTrapSeqNum_Type.__name__=_G
_FsRMapTrapSeqNum_Object=MibScalar
fsRMapTrapSeqNum=_FsRMapTrapSeqNum_Object((1,3,6,1,4,1,10876,101,1,155,4,2),_FsRMapTrapSeqNum_Type())
fsRMapTrapSeqNum.setMaxAccess(_A0)
if mibBuilder.loadTexts:fsRMapTrapSeqNum.setStatus(_A)
fsRMapTrapMatch=NotificationType((1,3,6,1,4,1,10876,101,1,155,4,0,1))
fsRMapTrapMatch.setObjects(*((_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:fsRMapTrapMatch.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'futureroutemap':futureroutemap,'fsRouteMap':fsRouteMap,'fsRouteMapTable':fsRouteMapTable,'fsRouteMapEntry':fsRouteMapEntry,_J:fsRouteMapName,_K:fsRouteMapSeqNum,'fsRouteMapAccess':fsRouteMapAccess,'fsRouteMapRowStatus':fsRouteMapRowStatus,'fsRouteMapMatchTable':fsRouteMapMatchTable,'fsRouteMapMatchEntry':fsRouteMapMatchEntry,_V:fsRouteMapMatchInterface,_W:fsRouteMapMatchIpAddress,_X:fsRouteMapMatchIpAddrMask,_Y:fsRouteMapMatchIpNextHop,_Z:fsRouteMapMatchMetric,_a:fsRouteMapMatchTag,_b:fsRouteMapMatchRouteType,_c:fsRouteMapMatchMetricType,_d:fsRouteMapMatchASPathTag,_e:fsRouteMapMatchCommunity,_f:fsRouteMapMatchOrigin,_g:fsRouteMapMatchLocalPreference,'fsRouteMapMatchRowStatus':fsRouteMapMatchRowStatus,'fsRouteMapSetTable':fsRouteMapSetTable,'fsRouteMapSetEntry':fsRouteMapSetEntry,'fsRouteMapSetInterface':fsRouteMapSetInterface,'fsRouteMapSetIpNextHop':fsRouteMapSetIpNextHop,'fsRouteMapSetMetric':fsRouteMapSetMetric,'fsRouteMapSetTag':fsRouteMapSetTag,'fsRouteMapSetMetricType':fsRouteMapSetMetricType,'fsRouteMapSetASPathTag':fsRouteMapSetASPathTag,'fsRouteMapSetCommunity':fsRouteMapSetCommunity,'fsRouteMapSetOrigin':fsRouteMapSetOrigin,'fsRouteMapSetOriginASNum':fsRouteMapSetOriginASNum,'fsRouteMapSetLocalPreference':fsRouteMapSetLocalPreference,'fsRouteMapSetRowStatus':fsRouteMapSetRowStatus,'fsRMapGroup':fsRMapGroup,'fsRMapTable':fsRMapTable,'fsRMapEntry':fsRMapEntry,_O:fsRMapName,_P:fsRMapSeqNum,'fsRMapAccess':fsRMapAccess,'fsRMapRowStatus':fsRMapRowStatus,'fsRMapIsIpPrefixList':fsRMapIsIpPrefixList,'fsRMapMatchTable':fsRMapMatchTable,'fsRMapMatchEntry':fsRMapMatchEntry,_h:fsRMapMatchDestInetType,_i:fsRMapMatchDestInetAddress,_j:fsRMapMatchDestInetPrefix,_k:fsRMapMatchSourceInetType,_l:fsRMapMatchSourceInetAddress,_m:fsRMapMatchSourceInetPrefix,_n:fsRMapMatchNextHopInetType,_o:fsRMapMatchNextHopInetAddr,_p:fsRMapMatchInterface,_q:fsRMapMatchMetric,_r:fsRMapMatchTag,_s:fsRMapMatchMetricType,_t:fsRMapMatchRouteType,_u:fsRMapMatchASPathTag,_v:fsRMapMatchCommunity,_w:fsRMapMatchLocalPref,_x:fsRMapMatchOrigin,'fsRMapMatchRowStatus':fsRMapMatchRowStatus,'fsRMapMatchDestMaxPrefixLen':fsRMapMatchDestMaxPrefixLen,'fsRMapMatchDestMinPrefixLen':fsRMapMatchDestMinPrefixLen,'fsRMapSetTable':fsRMapSetTable,'fsRMapSetEntry':fsRMapSetEntry,'fsRMapSetNextHopInetType':fsRMapSetNextHopInetType,'fsRMapSetNextHopInetAddr':fsRMapSetNextHopInetAddr,'fsRMapSetInterface':fsRMapSetInterface,'fsRMapSetMetric':fsRMapSetMetric,'fsRMapSetTag':fsRMapSetTag,'fsRMapSetRouteType':fsRMapSetRouteType,'fsRMapSetASPathTag':fsRMapSetASPathTag,'fsRMapSetCommunity':fsRMapSetCommunity,'fsRMapSetLocalPref':fsRMapSetLocalPref,'fsRMapSetOrigin':fsRMapSetOrigin,'fsRMapSetWeight':fsRMapSetWeight,'fsRMapSetEnableAutoTag':fsRMapSetEnableAutoTag,'fsRMapSetLevel':fsRMapSetLevel,'fsRMapSetRowStatus':fsRMapSetRowStatus,'fsRMapSetExtCommId':fsRMapSetExtCommId,'fsRMapSetExtCommPOI':fsRMapSetExtCommPOI,'fsRMapSetExtCommCost':fsRMapSetExtCommCost,'fsRMapSetCommunityAdditive':fsRMapSetCommunityAdditive,'fsRMapTrapCfgGroup':fsRMapTrapCfgGroup,'fsRmapTrapCfgEnable':fsRmapTrapCfgEnable,'fsRMapTrapGroup':fsRMapTrapGroup,'fsRMapTrapNotifications':fsRMapTrapNotifications,'fsRMapTrapMatch':fsRMapTrapMatch,_A1:fsRMapTrapName,_A2:fsRMapTrapSeqNum})