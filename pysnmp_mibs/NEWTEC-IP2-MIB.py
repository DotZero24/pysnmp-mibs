_e='ntcIP2ConfGrpV1Standard'
_d='ntcIP2AlmGwUnreachable'
_c='ntcIP2AlmInconsistent'
_b='ntcIP2CfgIgmpVersion'
_a='ntcIP2IPRouteState'
_Z='ntcIP2IPRouteGateway'
_Y='ntcIP2IPRouteIfName'
_X='ntcIP2IPRouteDstSubnet'
_W='ntcIP2CfgIPRouteRowStatus'
_V='ntcIP2MCastIfSrcAddrB'
_U='ntcIP2MCastIfState'
_T='ntcIP2MCastIfSrcAddr'
_S='ntcIP2MCastIfIPAddr'
_R='ntcIP2MCastIfName'
_Q='ntcIP2CfgMCastIfRowStatus'
_P='ntcIP2IfState'
_O='ntcIP2IfIPAddr'
_N='ntcIP2IfPhysIPAddr'
_M='ntcIP2CfgIPIfRowStatus'
_L='ntcIP2CfgIPRouteName'
_K='ntcIP2CfgMCastIfName'
_J='ntcIP2CfgIPIfInterface'
_I='off'
_H='not-accessible'
_G='OctetString'
_F='DisplayString'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='NEWTEC-IP2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcNetworkAddress=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState','NtcNetworkAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
ntcIp2=ModuleIdentity((1,3,6,1,4,1,5835,5,2,450))
if mibBuilder.loadTexts:ntcIp2.setRevisions(('2017-07-10 12:00','2015-09-25 11:00','2014-09-23 07:00','2014-09-09 09:00','2014-07-08 09:00'))
_NtcIP2Objects_ObjectIdentity=ObjectIdentity
ntcIP2Objects=_NtcIP2Objects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,450,1))
if mibBuilder.loadTexts:ntcIP2Objects.setStatus(_A)
_NtcIP2Cfg_ObjectIdentity=ObjectIdentity
ntcIP2Cfg=_NtcIP2Cfg_ObjectIdentity((1,3,6,1,4,1,5835,5,2,450,1,1))
if mibBuilder.loadTexts:ntcIP2Cfg.setStatus(_A)
_NtcIP2CfgIPIfTable_Object=MibTable
ntcIP2CfgIPIfTable=_NtcIP2CfgIPIfTable_Object((1,3,6,1,4,1,5835,5,2,450,1,1,1))
if mibBuilder.loadTexts:ntcIP2CfgIPIfTable.setStatus(_A)
_NtcIP2CfgIPIfEntry_Object=MibTableRow
ntcIP2CfgIPIfEntry=_NtcIP2CfgIPIfEntry_Object((1,3,6,1,4,1,5835,5,2,450,1,1,1,1))
ntcIP2CfgIPIfEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:ntcIP2CfgIPIfEntry.setStatus(_A)
class _NtcIP2CfgIPIfInterface_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_NtcIP2CfgIPIfInterface_Type.__name__=_F
_NtcIP2CfgIPIfInterface_Object=MibTableColumn
ntcIP2CfgIPIfInterface=_NtcIP2CfgIPIfInterface_Object((1,3,6,1,4,1,5835,5,2,450,1,1,1,1,1),_NtcIP2CfgIPIfInterface_Type())
ntcIP2CfgIPIfInterface.setMaxAccess(_H)
if mibBuilder.loadTexts:ntcIP2CfgIPIfInterface.setStatus(_A)
_NtcIP2CfgIPIfRowStatus_Type=RowStatus
_NtcIP2CfgIPIfRowStatus_Object=MibTableColumn
ntcIP2CfgIPIfRowStatus=_NtcIP2CfgIPIfRowStatus_Object((1,3,6,1,4,1,5835,5,2,450,1,1,1,1,2),_NtcIP2CfgIPIfRowStatus_Type())
ntcIP2CfgIPIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIP2CfgIPIfRowStatus.setStatus(_A)
_NtcIP2IfPhysIPAddr_Type=NtcNetworkAddress
_NtcIP2IfPhysIPAddr_Object=MibTableColumn
ntcIP2IfPhysIPAddr=_NtcIP2IfPhysIPAddr_Object((1,3,6,1,4,1,5835,5,2,450,1,1,1,1,3),_NtcIP2IfPhysIPAddr_Type())
ntcIP2IfPhysIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIP2IfPhysIPAddr.setStatus(_A)
_NtcIP2IfIPAddr_Type=NtcNetworkAddress
_NtcIP2IfIPAddr_Object=MibTableColumn
ntcIP2IfIPAddr=_NtcIP2IfIPAddr_Object((1,3,6,1,4,1,5835,5,2,450,1,1,1,1,4),_NtcIP2IfIPAddr_Type())
ntcIP2IfIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIP2IfIPAddr.setStatus(_A)
class _NtcIP2IfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('on',1)))
_NtcIP2IfState_Type.__name__=_D
_NtcIP2IfState_Object=MibTableColumn
ntcIP2IfState=_NtcIP2IfState_Object((1,3,6,1,4,1,5835,5,2,450,1,1,1,1,5),_NtcIP2IfState_Type())
ntcIP2IfState.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcIP2IfState.setStatus(_A)
_NtcIP2CfgMCastIfTable_Object=MibTable
ntcIP2CfgMCastIfTable=_NtcIP2CfgMCastIfTable_Object((1,3,6,1,4,1,5835,5,2,450,1,1,2))
if mibBuilder.loadTexts:ntcIP2CfgMCastIfTable.setStatus(_A)
_NtcIP2CfgMCastIfEntry_Object=MibTableRow
ntcIP2CfgMCastIfEntry=_NtcIP2CfgMCastIfEntry_Object((1,3,6,1,4,1,5835,5,2,450,1,1,2,1))
ntcIP2CfgMCastIfEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:ntcIP2CfgMCastIfEntry.setStatus(_A)
class _NtcIP2CfgMCastIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_NtcIP2CfgMCastIfName_Type.__name__=_F
_NtcIP2CfgMCastIfName_Object=MibTableColumn
ntcIP2CfgMCastIfName=_NtcIP2CfgMCastIfName_Object((1,3,6,1,4,1,5835,5,2,450,1,1,2,1,1),_NtcIP2CfgMCastIfName_Type())
ntcIP2CfgMCastIfName.setMaxAccess(_H)
if mibBuilder.loadTexts:ntcIP2CfgMCastIfName.setStatus(_A)
_NtcIP2CfgMCastIfRowStatus_Type=RowStatus
_NtcIP2CfgMCastIfRowStatus_Object=MibTableColumn
ntcIP2CfgMCastIfRowStatus=_NtcIP2CfgMCastIfRowStatus_Object((1,3,6,1,4,1,5835,5,2,450,1,1,2,1,2),_NtcIP2CfgMCastIfRowStatus_Type())
ntcIP2CfgMCastIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIP2CfgMCastIfRowStatus.setStatus(_A)
class _NtcIP2MCastIfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NtcIP2MCastIfName_Type.__name__=_G
_NtcIP2MCastIfName_Object=MibTableColumn
ntcIP2MCastIfName=_NtcIP2MCastIfName_Object((1,3,6,1,4,1,5835,5,2,450,1,1,2,1,3),_NtcIP2MCastIfName_Type())
ntcIP2MCastIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIP2MCastIfName.setStatus(_A)
_NtcIP2MCastIfIPAddr_Type=IpAddress
_NtcIP2MCastIfIPAddr_Object=MibTableColumn
ntcIP2MCastIfIPAddr=_NtcIP2MCastIfIPAddr_Object((1,3,6,1,4,1,5835,5,2,450,1,1,2,1,4),_NtcIP2MCastIfIPAddr_Type())
ntcIP2MCastIfIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIP2MCastIfIPAddr.setStatus(_A)
_NtcIP2MCastIfSrcAddr_Type=IpAddress
_NtcIP2MCastIfSrcAddr_Object=MibTableColumn
ntcIP2MCastIfSrcAddr=_NtcIP2MCastIfSrcAddr_Object((1,3,6,1,4,1,5835,5,2,450,1,1,2,1,5),_NtcIP2MCastIfSrcAddr_Type())
ntcIP2MCastIfSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIP2MCastIfSrcAddr.setStatus(_A)
class _NtcIP2MCastIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('on',1)))
_NtcIP2MCastIfState_Type.__name__=_D
_NtcIP2MCastIfState_Object=MibTableColumn
ntcIP2MCastIfState=_NtcIP2MCastIfState_Object((1,3,6,1,4,1,5835,5,2,450,1,1,2,1,6),_NtcIP2MCastIfState_Type())
ntcIP2MCastIfState.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcIP2MCastIfState.setStatus(_A)
_NtcIP2MCastIfSrcAddrB_Type=IpAddress
_NtcIP2MCastIfSrcAddrB_Object=MibTableColumn
ntcIP2MCastIfSrcAddrB=_NtcIP2MCastIfSrcAddrB_Object((1,3,6,1,4,1,5835,5,2,450,1,1,2,1,7),_NtcIP2MCastIfSrcAddrB_Type())
ntcIP2MCastIfSrcAddrB.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIP2MCastIfSrcAddrB.setStatus(_A)
_NtcIP2CfgIPRouteTable_Object=MibTable
ntcIP2CfgIPRouteTable=_NtcIP2CfgIPRouteTable_Object((1,3,6,1,4,1,5835,5,2,450,1,1,3))
if mibBuilder.loadTexts:ntcIP2CfgIPRouteTable.setStatus(_A)
_NtcIP2CfgIPRouteEntry_Object=MibTableRow
ntcIP2CfgIPRouteEntry=_NtcIP2CfgIPRouteEntry_Object((1,3,6,1,4,1,5835,5,2,450,1,1,3,1))
ntcIP2CfgIPRouteEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:ntcIP2CfgIPRouteEntry.setStatus(_A)
class _NtcIP2CfgIPRouteName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_NtcIP2CfgIPRouteName_Type.__name__=_F
_NtcIP2CfgIPRouteName_Object=MibTableColumn
ntcIP2CfgIPRouteName=_NtcIP2CfgIPRouteName_Object((1,3,6,1,4,1,5835,5,2,450,1,1,3,1,1),_NtcIP2CfgIPRouteName_Type())
ntcIP2CfgIPRouteName.setMaxAccess(_H)
if mibBuilder.loadTexts:ntcIP2CfgIPRouteName.setStatus(_A)
_NtcIP2CfgIPRouteRowStatus_Type=RowStatus
_NtcIP2CfgIPRouteRowStatus_Object=MibTableColumn
ntcIP2CfgIPRouteRowStatus=_NtcIP2CfgIPRouteRowStatus_Object((1,3,6,1,4,1,5835,5,2,450,1,1,3,1,2),_NtcIP2CfgIPRouteRowStatus_Type())
ntcIP2CfgIPRouteRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIP2CfgIPRouteRowStatus.setStatus(_A)
_NtcIP2IPRouteDstSubnet_Type=NtcNetworkAddress
_NtcIP2IPRouteDstSubnet_Object=MibTableColumn
ntcIP2IPRouteDstSubnet=_NtcIP2IPRouteDstSubnet_Object((1,3,6,1,4,1,5835,5,2,450,1,1,3,1,3),_NtcIP2IPRouteDstSubnet_Type())
ntcIP2IPRouteDstSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIP2IPRouteDstSubnet.setStatus(_A)
class _NtcIP2IPRouteIfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NtcIP2IPRouteIfName_Type.__name__=_G
_NtcIP2IPRouteIfName_Object=MibTableColumn
ntcIP2IPRouteIfName=_NtcIP2IPRouteIfName_Object((1,3,6,1,4,1,5835,5,2,450,1,1,3,1,4),_NtcIP2IPRouteIfName_Type())
ntcIP2IPRouteIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIP2IPRouteIfName.setStatus(_A)
_NtcIP2IPRouteGateway_Type=IpAddress
_NtcIP2IPRouteGateway_Object=MibTableColumn
ntcIP2IPRouteGateway=_NtcIP2IPRouteGateway_Object((1,3,6,1,4,1,5835,5,2,450,1,1,3,1,5),_NtcIP2IPRouteGateway_Type())
ntcIP2IPRouteGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIP2IPRouteGateway.setStatus(_A)
class _NtcIP2IPRouteState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('on',1)))
_NtcIP2IPRouteState_Type.__name__=_D
_NtcIP2IPRouteState_Object=MibTableColumn
ntcIP2IPRouteState=_NtcIP2IPRouteState_Object((1,3,6,1,4,1,5835,5,2,450,1,1,3,1,6),_NtcIP2IPRouteState_Type())
ntcIP2IPRouteState.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcIP2IPRouteState.setStatus(_A)
_NtcIP2CfgIgmp_ObjectIdentity=ObjectIdentity
ntcIP2CfgIgmp=_NtcIP2CfgIgmp_ObjectIdentity((1,3,6,1,4,1,5835,5,2,450,1,1,4))
if mibBuilder.loadTexts:ntcIP2CfgIgmp.setStatus(_A)
class _NtcIP2CfgIgmpVersion_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('v2',0),('v3',1)))
_NtcIP2CfgIgmpVersion_Type.__name__=_D
_NtcIP2CfgIgmpVersion_Object=MibScalar
ntcIP2CfgIgmpVersion=_NtcIP2CfgIgmpVersion_Object((1,3,6,1,4,1,5835,5,2,450,1,1,4,1),_NtcIP2CfgIgmpVersion_Type())
ntcIP2CfgIgmpVersion.setMaxAccess('read-write')
if mibBuilder.loadTexts:ntcIP2CfgIgmpVersion.setStatus(_A)
_NtcIP2Alarm_ObjectIdentity=ObjectIdentity
ntcIP2Alarm=_NtcIP2Alarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,450,1,2))
if mibBuilder.loadTexts:ntcIP2Alarm.setStatus(_A)
_NtcIP2AlmInconsistent_Type=NtcAlarmState
_NtcIP2AlmInconsistent_Object=MibScalar
ntcIP2AlmInconsistent=_NtcIP2AlmInconsistent_Object((1,3,6,1,4,1,5835,5,2,450,1,2,1),_NtcIP2AlmInconsistent_Type())
ntcIP2AlmInconsistent.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcIP2AlmInconsistent.setStatus(_A)
_NtcIP2AlmGwUnreachable_Type=NtcAlarmState
_NtcIP2AlmGwUnreachable_Object=MibScalar
ntcIP2AlmGwUnreachable=_NtcIP2AlmGwUnreachable_Object((1,3,6,1,4,1,5835,5,2,450,1,2,2),_NtcIP2AlmGwUnreachable_Type())
ntcIP2AlmGwUnreachable.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcIP2AlmGwUnreachable.setStatus(_A)
_NtcIP2Conformance_ObjectIdentity=ObjectIdentity
ntcIP2Conformance=_NtcIP2Conformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,450,2))
if mibBuilder.loadTexts:ntcIP2Conformance.setStatus(_A)
_NtcIP2ConfCompliance_ObjectIdentity=ObjectIdentity
ntcIP2ConfCompliance=_NtcIP2ConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,450,2,1))
if mibBuilder.loadTexts:ntcIP2ConfCompliance.setStatus(_A)
_NtcIP2ConfGroup_ObjectIdentity=ObjectIdentity
ntcIP2ConfGroup=_NtcIP2ConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,450,2,2))
if mibBuilder.loadTexts:ntcIP2ConfGroup.setStatus(_A)
ntcIP2ConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,450,2,2,1))
ntcIP2ConfGrpV1Standard.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ntcIP2ConfGrpV1Standard.setStatus(_A)
ntcIP2ConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,450,2,1,1))
ntcIP2ConfCompV1Standard.setObjects((_B,_e))
if mibBuilder.loadTexts:ntcIP2ConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcIp2':ntcIp2,'ntcIP2Objects':ntcIP2Objects,'ntcIP2Cfg':ntcIP2Cfg,'ntcIP2CfgIPIfTable':ntcIP2CfgIPIfTable,'ntcIP2CfgIPIfEntry':ntcIP2CfgIPIfEntry,_J:ntcIP2CfgIPIfInterface,_M:ntcIP2CfgIPIfRowStatus,_N:ntcIP2IfPhysIPAddr,_O:ntcIP2IfIPAddr,_P:ntcIP2IfState,'ntcIP2CfgMCastIfTable':ntcIP2CfgMCastIfTable,'ntcIP2CfgMCastIfEntry':ntcIP2CfgMCastIfEntry,_K:ntcIP2CfgMCastIfName,_Q:ntcIP2CfgMCastIfRowStatus,_R:ntcIP2MCastIfName,_S:ntcIP2MCastIfIPAddr,_T:ntcIP2MCastIfSrcAddr,_U:ntcIP2MCastIfState,_V:ntcIP2MCastIfSrcAddrB,'ntcIP2CfgIPRouteTable':ntcIP2CfgIPRouteTable,'ntcIP2CfgIPRouteEntry':ntcIP2CfgIPRouteEntry,_L:ntcIP2CfgIPRouteName,_W:ntcIP2CfgIPRouteRowStatus,_X:ntcIP2IPRouteDstSubnet,_Y:ntcIP2IPRouteIfName,_Z:ntcIP2IPRouteGateway,_a:ntcIP2IPRouteState,'ntcIP2CfgIgmp':ntcIP2CfgIgmp,_b:ntcIP2CfgIgmpVersion,'ntcIP2Alarm':ntcIP2Alarm,_c:ntcIP2AlmInconsistent,_d:ntcIP2AlmGwUnreachable,'ntcIP2Conformance':ntcIP2Conformance,'ntcIP2ConfCompliance':ntcIP2ConfCompliance,'ntcIP2ConfCompV1Standard':ntcIP2ConfCompV1Standard,'ntcIP2ConfGroup':ntcIP2ConfGroup,_e:ntcIP2ConfGrpV1Standard})