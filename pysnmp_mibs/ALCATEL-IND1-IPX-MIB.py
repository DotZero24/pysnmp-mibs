_A7='alcatelIND1IPXMIBTimerGroup'
_A6='alcatelIND1IPXMIBType20Group'
_A5='alcatelIND1IPXMIBKeepaliveSpoofGroup'
_A4='alcatelIND1IPXMIBSerialFilterGroup'
_A3='alcatelIND1IPXMIBWatchdogSpoofGroup'
_A2='alcatelIND1IPXMIBRipSapFilterGroup'
_A1='alcatelIND1IPXMIBFlushGroup'
_A0='alcatelIND1IPXMIBExtMsgGroup'
_z='alcatelIND1IPXMIBDefRouteGroup'
_y='alcatelIND1IPXMIBStaticRouteGroup'
_x='alaIpxTimerRowStatus'
_w='alaIpxTimerSap'
_v='alaIpxTimerRip'
_u='alaIpxType20RowStatus'
_t='alaIpxType20Mode'
_s='alaSpxKeepaliveSpoofRowStatus'
_r='alaSpxKeepaliveSpoofMode'
_q='alaIpxSerialFilterRowStatus'
_p='alaIpxSerialFilterMode'
_o='alaIpxWatchdogSpoofRowStatus'
_n='alaIpxWatchdogSpoofMode'
_m='alaIpxRipSapFilterRowStatus'
_l='alaIpxRipSapFilterMode'
_k='alaIpxFlush'
_j='alaIpxExtMsgRowStatus'
_i='alaIpxExtMsgMode'
_h='alaIpxDefRouteRowStatus'
_g='alaIpxDefRouteNode'
_f='alaIpxDefRouteNet'
_e='alaIpxStaticRouteRowStatus'
_d='alaIpxStaticRouteHopCount'
_c='alaIpxStaticRouteTicks'
_b='alaIpxStaticRouteNextHopNode'
_a='alaIpxStaticRouteNextHopNet'
_Z='alaIpxTimerVlanId'
_Y='alaIpxType20VlanId'
_X='alaSpxKeepaliveSpoofVlanId'
_W='alaIpxSerialFilterVlanId'
_V='alaIpxWatchdogSpoofVlanId'
_U='alaIpxRipSapFilterSvcType'
_T='alaIpxRipSapFilterNodeMask'
_S='alaIpxRipSapFilterNode'
_R='alaIpxRipSapFilterNetMask'
_Q='alaIpxRipSapFilterNet'
_P='alaIpxRipSapFilterType'
_O='alaIpxRipSapFilterVlanId'
_N='alaIpxExtMsgVlanId'
_M='alaIpxDefRouteVlanId'
_L='alaIpxStaticRouteNetNum'
_K='000000000000'
_J='00000000'
_I='enabled'
_H='disabled'
_G='HostAddress'
_F='NetNumber'
_E='not-accessible'
_D='Integer32'
_C='read-create'
_B='ALCATEL-IND1-IPX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Ipx,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','routingIND1Ipx')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1IPXMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,8,1))
if mibBuilder.loadTexts:alcatelIND1IPXMIB.setRevisions(('2007-04-03 00:00',))
class NetNumber(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class HostAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_AlcatelIND1IPXMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1IPXMIBObjects=_AlcatelIND1IPXMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1))
_AlaIpxRoutingGroup_ObjectIdentity=ObjectIdentity
alaIpxRoutingGroup=_AlaIpxRoutingGroup_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1))
if mibBuilder.loadTexts:alaIpxRoutingGroup.setStatus(_A)
_AlaIpxStaticRouteTable_Object=MibTable
alaIpxStaticRouteTable=_AlaIpxStaticRouteTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,1))
if mibBuilder.loadTexts:alaIpxStaticRouteTable.setStatus(_A)
_AlaIpxStaticRouteEntry_Object=MibTableRow
alaIpxStaticRouteEntry=_AlaIpxStaticRouteEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,1,1))
alaIpxStaticRouteEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:alaIpxStaticRouteEntry.setStatus(_A)
class _AlaIpxStaticRouteNetNum_Type(NetNumber):defaultHexValue=_J
_AlaIpxStaticRouteNetNum_Type.__name__=_F
_AlaIpxStaticRouteNetNum_Object=MibTableColumn
alaIpxStaticRouteNetNum=_AlaIpxStaticRouteNetNum_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,1,1,1),_AlaIpxStaticRouteNetNum_Type())
alaIpxStaticRouteNetNum.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxStaticRouteNetNum.setStatus(_A)
class _AlaIpxStaticRouteNextHopNet_Type(NetNumber):defaultHexValue=_J
_AlaIpxStaticRouteNextHopNet_Type.__name__=_F
_AlaIpxStaticRouteNextHopNet_Object=MibTableColumn
alaIpxStaticRouteNextHopNet=_AlaIpxStaticRouteNextHopNet_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,1,1,2),_AlaIpxStaticRouteNextHopNet_Type())
alaIpxStaticRouteNextHopNet.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxStaticRouteNextHopNet.setStatus(_A)
class _AlaIpxStaticRouteNextHopNode_Type(HostAddress):defaultHexValue=_K
_AlaIpxStaticRouteNextHopNode_Type.__name__=_G
_AlaIpxStaticRouteNextHopNode_Object=MibTableColumn
alaIpxStaticRouteNextHopNode=_AlaIpxStaticRouteNextHopNode_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,1,1,3),_AlaIpxStaticRouteNextHopNode_Type())
alaIpxStaticRouteNextHopNode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxStaticRouteNextHopNode.setStatus(_A)
class _AlaIpxStaticRouteTicks_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaIpxStaticRouteTicks_Type.__name__=_D
_AlaIpxStaticRouteTicks_Object=MibTableColumn
alaIpxStaticRouteTicks=_AlaIpxStaticRouteTicks_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,1,1,4),_AlaIpxStaticRouteTicks_Type())
alaIpxStaticRouteTicks.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxStaticRouteTicks.setStatus(_A)
class _AlaIpxStaticRouteHopCount_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AlaIpxStaticRouteHopCount_Type.__name__=_D
_AlaIpxStaticRouteHopCount_Object=MibTableColumn
alaIpxStaticRouteHopCount=_AlaIpxStaticRouteHopCount_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,1,1,5),_AlaIpxStaticRouteHopCount_Type())
alaIpxStaticRouteHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxStaticRouteHopCount.setStatus(_A)
_AlaIpxStaticRouteRowStatus_Type=RowStatus
_AlaIpxStaticRouteRowStatus_Object=MibTableColumn
alaIpxStaticRouteRowStatus=_AlaIpxStaticRouteRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,1,1,6),_AlaIpxStaticRouteRowStatus_Type())
alaIpxStaticRouteRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxStaticRouteRowStatus.setStatus(_A)
_AlaIpxDefRouteTable_Object=MibTable
alaIpxDefRouteTable=_AlaIpxDefRouteTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,2))
if mibBuilder.loadTexts:alaIpxDefRouteTable.setStatus(_A)
_AlaIpxDefRouteEntry_Object=MibTableRow
alaIpxDefRouteEntry=_AlaIpxDefRouteEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,2,1))
alaIpxDefRouteEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:alaIpxDefRouteEntry.setStatus(_A)
class _AlaIpxDefRouteVlanId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AlaIpxDefRouteVlanId_Type.__name__=_D
_AlaIpxDefRouteVlanId_Object=MibTableColumn
alaIpxDefRouteVlanId=_AlaIpxDefRouteVlanId_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,2,1,1),_AlaIpxDefRouteVlanId_Type())
alaIpxDefRouteVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxDefRouteVlanId.setStatus(_A)
class _AlaIpxDefRouteNet_Type(NetNumber):defaultHexValue=_J
_AlaIpxDefRouteNet_Type.__name__=_F
_AlaIpxDefRouteNet_Object=MibTableColumn
alaIpxDefRouteNet=_AlaIpxDefRouteNet_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,2,1,2),_AlaIpxDefRouteNet_Type())
alaIpxDefRouteNet.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxDefRouteNet.setStatus(_A)
class _AlaIpxDefRouteNode_Type(HostAddress):defaultHexValue=_K
_AlaIpxDefRouteNode_Type.__name__=_G
_AlaIpxDefRouteNode_Object=MibTableColumn
alaIpxDefRouteNode=_AlaIpxDefRouteNode_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,2,1,3),_AlaIpxDefRouteNode_Type())
alaIpxDefRouteNode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxDefRouteNode.setStatus(_A)
_AlaIpxDefRouteRowStatus_Type=RowStatus
_AlaIpxDefRouteRowStatus_Object=MibTableColumn
alaIpxDefRouteRowStatus=_AlaIpxDefRouteRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,2,1,4),_AlaIpxDefRouteRowStatus_Type())
alaIpxDefRouteRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxDefRouteRowStatus.setStatus(_A)
_AlaIpxExtMsgTable_Object=MibTable
alaIpxExtMsgTable=_AlaIpxExtMsgTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,3))
if mibBuilder.loadTexts:alaIpxExtMsgTable.setStatus(_A)
_AlaIpxExtMsgEntry_Object=MibTableRow
alaIpxExtMsgEntry=_AlaIpxExtMsgEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,3,1))
alaIpxExtMsgEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:alaIpxExtMsgEntry.setStatus(_A)
class _AlaIpxExtMsgVlanId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AlaIpxExtMsgVlanId_Type.__name__=_D
_AlaIpxExtMsgVlanId_Object=MibTableColumn
alaIpxExtMsgVlanId=_AlaIpxExtMsgVlanId_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,3,1,1),_AlaIpxExtMsgVlanId_Type())
alaIpxExtMsgVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxExtMsgVlanId.setStatus(_A)
class _AlaIpxExtMsgMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaIpxExtMsgMode_Type.__name__=_D
_AlaIpxExtMsgMode_Object=MibTableColumn
alaIpxExtMsgMode=_AlaIpxExtMsgMode_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,3,1,2),_AlaIpxExtMsgMode_Type())
alaIpxExtMsgMode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxExtMsgMode.setStatus(_A)
_AlaIpxExtMsgRowStatus_Type=RowStatus
_AlaIpxExtMsgRowStatus_Object=MibTableColumn
alaIpxExtMsgRowStatus=_AlaIpxExtMsgRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,3,1,3),_AlaIpxExtMsgRowStatus_Type())
alaIpxExtMsgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxExtMsgRowStatus.setStatus(_A)
class _AlaIpxFlush_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rip',1),('sap',2),('both',3)))
_AlaIpxFlush_Type.__name__=_D
_AlaIpxFlush_Object=MibScalar
alaIpxFlush=_AlaIpxFlush_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,1,4),_AlaIpxFlush_Type())
alaIpxFlush.setMaxAccess('read-write')
if mibBuilder.loadTexts:alaIpxFlush.setStatus(_A)
_AlaIpxFilterGroup_ObjectIdentity=ObjectIdentity
alaIpxFilterGroup=_AlaIpxFilterGroup_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2))
if mibBuilder.loadTexts:alaIpxFilterGroup.setStatus(_A)
_AlaIpxRipSapFilterTable_Object=MibTable
alaIpxRipSapFilterTable=_AlaIpxRipSapFilterTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,1))
if mibBuilder.loadTexts:alaIpxRipSapFilterTable.setStatus(_A)
_AlaIpxRipSapFilterEntry_Object=MibTableRow
alaIpxRipSapFilterEntry=_AlaIpxRipSapFilterEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,1,1))
alaIpxRipSapFilterEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:alaIpxRipSapFilterEntry.setStatus(_A)
class _AlaIpxRipSapFilterVlanId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AlaIpxRipSapFilterVlanId_Type.__name__=_D
_AlaIpxRipSapFilterVlanId_Object=MibTableColumn
alaIpxRipSapFilterVlanId=_AlaIpxRipSapFilterVlanId_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,1,1,1),_AlaIpxRipSapFilterVlanId_Type())
alaIpxRipSapFilterVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxRipSapFilterVlanId.setStatus(_A)
class _AlaIpxRipSapFilterType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('sapOutput',1),('sapInput',2),('gnsOutput',3),('ripOutput',4),('ripInput',5)))
_AlaIpxRipSapFilterType_Type.__name__=_D
_AlaIpxRipSapFilterType_Object=MibTableColumn
alaIpxRipSapFilterType=_AlaIpxRipSapFilterType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,1,1,2),_AlaIpxRipSapFilterType_Type())
alaIpxRipSapFilterType.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxRipSapFilterType.setStatus(_A)
class _AlaIpxRipSapFilterNet_Type(NetNumber):defaultHexValue=_J
_AlaIpxRipSapFilterNet_Type.__name__=_F
_AlaIpxRipSapFilterNet_Object=MibTableColumn
alaIpxRipSapFilterNet=_AlaIpxRipSapFilterNet_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,1,1,3),_AlaIpxRipSapFilterNet_Type())
alaIpxRipSapFilterNet.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxRipSapFilterNet.setStatus(_A)
class _AlaIpxRipSapFilterNetMask_Type(NetNumber):defaultHexValue='ffffffff'
_AlaIpxRipSapFilterNetMask_Type.__name__=_F
_AlaIpxRipSapFilterNetMask_Object=MibTableColumn
alaIpxRipSapFilterNetMask=_AlaIpxRipSapFilterNetMask_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,1,1,4),_AlaIpxRipSapFilterNetMask_Type())
alaIpxRipSapFilterNetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxRipSapFilterNetMask.setStatus(_A)
class _AlaIpxRipSapFilterNode_Type(HostAddress):defaultHexValue=_K
_AlaIpxRipSapFilterNode_Type.__name__=_G
_AlaIpxRipSapFilterNode_Object=MibTableColumn
alaIpxRipSapFilterNode=_AlaIpxRipSapFilterNode_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,1,1,5),_AlaIpxRipSapFilterNode_Type())
alaIpxRipSapFilterNode.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxRipSapFilterNode.setStatus(_A)
class _AlaIpxRipSapFilterNodeMask_Type(HostAddress):defaultHexValue='ffffffffffff'
_AlaIpxRipSapFilterNodeMask_Type.__name__=_G
_AlaIpxRipSapFilterNodeMask_Object=MibTableColumn
alaIpxRipSapFilterNodeMask=_AlaIpxRipSapFilterNodeMask_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,1,1,6),_AlaIpxRipSapFilterNodeMask_Type())
alaIpxRipSapFilterNodeMask.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxRipSapFilterNodeMask.setStatus(_A)
class _AlaIpxRipSapFilterSvcType_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaIpxRipSapFilterSvcType_Type.__name__=_D
_AlaIpxRipSapFilterSvcType_Object=MibTableColumn
alaIpxRipSapFilterSvcType=_AlaIpxRipSapFilterSvcType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,1,1,7),_AlaIpxRipSapFilterSvcType_Type())
alaIpxRipSapFilterSvcType.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxRipSapFilterSvcType.setStatus(_A)
class _AlaIpxRipSapFilterMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('block',2)))
_AlaIpxRipSapFilterMode_Type.__name__=_D
_AlaIpxRipSapFilterMode_Object=MibTableColumn
alaIpxRipSapFilterMode=_AlaIpxRipSapFilterMode_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,1,1,8),_AlaIpxRipSapFilterMode_Type())
alaIpxRipSapFilterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxRipSapFilterMode.setStatus(_A)
_AlaIpxRipSapFilterRowStatus_Type=RowStatus
_AlaIpxRipSapFilterRowStatus_Object=MibTableColumn
alaIpxRipSapFilterRowStatus=_AlaIpxRipSapFilterRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,1,1,10),_AlaIpxRipSapFilterRowStatus_Type())
alaIpxRipSapFilterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxRipSapFilterRowStatus.setStatus(_A)
_AlaIpxWatchdogSpoofTable_Object=MibTable
alaIpxWatchdogSpoofTable=_AlaIpxWatchdogSpoofTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,2))
if mibBuilder.loadTexts:alaIpxWatchdogSpoofTable.setStatus(_A)
_AlaIpxWatchdogSpoofEntry_Object=MibTableRow
alaIpxWatchdogSpoofEntry=_AlaIpxWatchdogSpoofEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,2,1))
alaIpxWatchdogSpoofEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:alaIpxWatchdogSpoofEntry.setStatus(_A)
class _AlaIpxWatchdogSpoofVlanId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AlaIpxWatchdogSpoofVlanId_Type.__name__=_D
_AlaIpxWatchdogSpoofVlanId_Object=MibTableColumn
alaIpxWatchdogSpoofVlanId=_AlaIpxWatchdogSpoofVlanId_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,2,1,1),_AlaIpxWatchdogSpoofVlanId_Type())
alaIpxWatchdogSpoofVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxWatchdogSpoofVlanId.setStatus(_A)
class _AlaIpxWatchdogSpoofMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaIpxWatchdogSpoofMode_Type.__name__=_D
_AlaIpxWatchdogSpoofMode_Object=MibTableColumn
alaIpxWatchdogSpoofMode=_AlaIpxWatchdogSpoofMode_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,2,1,2),_AlaIpxWatchdogSpoofMode_Type())
alaIpxWatchdogSpoofMode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxWatchdogSpoofMode.setStatus(_A)
_AlaIpxWatchdogSpoofRowStatus_Type=RowStatus
_AlaIpxWatchdogSpoofRowStatus_Object=MibTableColumn
alaIpxWatchdogSpoofRowStatus=_AlaIpxWatchdogSpoofRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,2,1,3),_AlaIpxWatchdogSpoofRowStatus_Type())
alaIpxWatchdogSpoofRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxWatchdogSpoofRowStatus.setStatus(_A)
_AlaIpxSerialFilterTable_Object=MibTable
alaIpxSerialFilterTable=_AlaIpxSerialFilterTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,3))
if mibBuilder.loadTexts:alaIpxSerialFilterTable.setStatus(_A)
_AlaIpxSerialFilterEntry_Object=MibTableRow
alaIpxSerialFilterEntry=_AlaIpxSerialFilterEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,3,1))
alaIpxSerialFilterEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:alaIpxSerialFilterEntry.setStatus(_A)
class _AlaIpxSerialFilterVlanId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AlaIpxSerialFilterVlanId_Type.__name__=_D
_AlaIpxSerialFilterVlanId_Object=MibTableColumn
alaIpxSerialFilterVlanId=_AlaIpxSerialFilterVlanId_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,3,1,1),_AlaIpxSerialFilterVlanId_Type())
alaIpxSerialFilterVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxSerialFilterVlanId.setStatus(_A)
class _AlaIpxSerialFilterMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaIpxSerialFilterMode_Type.__name__=_D
_AlaIpxSerialFilterMode_Object=MibTableColumn
alaIpxSerialFilterMode=_AlaIpxSerialFilterMode_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,3,1,2),_AlaIpxSerialFilterMode_Type())
alaIpxSerialFilterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxSerialFilterMode.setStatus(_A)
_AlaIpxSerialFilterRowStatus_Type=RowStatus
_AlaIpxSerialFilterRowStatus_Object=MibTableColumn
alaIpxSerialFilterRowStatus=_AlaIpxSerialFilterRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,3,1,3),_AlaIpxSerialFilterRowStatus_Type())
alaIpxSerialFilterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxSerialFilterRowStatus.setStatus(_A)
_AlaSpxKeepaliveSpoofTable_Object=MibTable
alaSpxKeepaliveSpoofTable=_AlaSpxKeepaliveSpoofTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,4))
if mibBuilder.loadTexts:alaSpxKeepaliveSpoofTable.setStatus(_A)
_AlaSpxKeepaliveSpoofEntry_Object=MibTableRow
alaSpxKeepaliveSpoofEntry=_AlaSpxKeepaliveSpoofEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,4,1))
alaSpxKeepaliveSpoofEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:alaSpxKeepaliveSpoofEntry.setStatus(_A)
class _AlaSpxKeepaliveSpoofVlanId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AlaSpxKeepaliveSpoofVlanId_Type.__name__=_D
_AlaSpxKeepaliveSpoofVlanId_Object=MibTableColumn
alaSpxKeepaliveSpoofVlanId=_AlaSpxKeepaliveSpoofVlanId_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,4,1,1),_AlaSpxKeepaliveSpoofVlanId_Type())
alaSpxKeepaliveSpoofVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaSpxKeepaliveSpoofVlanId.setStatus(_A)
class _AlaSpxKeepaliveSpoofMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaSpxKeepaliveSpoofMode_Type.__name__=_D
_AlaSpxKeepaliveSpoofMode_Object=MibTableColumn
alaSpxKeepaliveSpoofMode=_AlaSpxKeepaliveSpoofMode_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,4,1,2),_AlaSpxKeepaliveSpoofMode_Type())
alaSpxKeepaliveSpoofMode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaSpxKeepaliveSpoofMode.setStatus(_A)
_AlaSpxKeepaliveSpoofRowStatus_Type=RowStatus
_AlaSpxKeepaliveSpoofRowStatus_Object=MibTableColumn
alaSpxKeepaliveSpoofRowStatus=_AlaSpxKeepaliveSpoofRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,4,1,3),_AlaSpxKeepaliveSpoofRowStatus_Type())
alaSpxKeepaliveSpoofRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaSpxKeepaliveSpoofRowStatus.setStatus(_A)
_AlaIpxType20Table_Object=MibTable
alaIpxType20Table=_AlaIpxType20Table_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,5))
if mibBuilder.loadTexts:alaIpxType20Table.setStatus(_A)
_AlaIpxType20Entry_Object=MibTableRow
alaIpxType20Entry=_AlaIpxType20Entry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,5,1))
alaIpxType20Entry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:alaIpxType20Entry.setStatus(_A)
class _AlaIpxType20VlanId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AlaIpxType20VlanId_Type.__name__=_D
_AlaIpxType20VlanId_Object=MibTableColumn
alaIpxType20VlanId=_AlaIpxType20VlanId_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,5,1,1),_AlaIpxType20VlanId_Type())
alaIpxType20VlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxType20VlanId.setStatus(_A)
class _AlaIpxType20Mode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaIpxType20Mode_Type.__name__=_D
_AlaIpxType20Mode_Object=MibTableColumn
alaIpxType20Mode=_AlaIpxType20Mode_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,5,1,2),_AlaIpxType20Mode_Type())
alaIpxType20Mode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxType20Mode.setStatus(_A)
_AlaIpxType20RowStatus_Type=RowStatus
_AlaIpxType20RowStatus_Object=MibTableColumn
alaIpxType20RowStatus=_AlaIpxType20RowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,2,5,1,3),_AlaIpxType20RowStatus_Type())
alaIpxType20RowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxType20RowStatus.setStatus(_A)
_AlaIpxTimerGroup_ObjectIdentity=ObjectIdentity
alaIpxTimerGroup=_AlaIpxTimerGroup_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,3))
if mibBuilder.loadTexts:alaIpxTimerGroup.setStatus(_A)
_AlaIpxTimerTable_Object=MibTable
alaIpxTimerTable=_AlaIpxTimerTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,3,1))
if mibBuilder.loadTexts:alaIpxTimerTable.setStatus(_A)
_AlaIpxTimerEntry_Object=MibTableRow
alaIpxTimerEntry=_AlaIpxTimerEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,3,1,1))
alaIpxTimerEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:alaIpxTimerEntry.setStatus(_A)
class _AlaIpxTimerVlanId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AlaIpxTimerVlanId_Type.__name__=_D
_AlaIpxTimerVlanId_Object=MibTableColumn
alaIpxTimerVlanId=_AlaIpxTimerVlanId_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,3,1,1,1),_AlaIpxTimerVlanId_Type())
alaIpxTimerVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaIpxTimerVlanId.setStatus(_A)
class _AlaIpxTimerSap_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,180))
_AlaIpxTimerSap_Type.__name__=_D
_AlaIpxTimerSap_Object=MibTableColumn
alaIpxTimerSap=_AlaIpxTimerSap_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,3,1,1,2),_AlaIpxTimerSap_Type())
alaIpxTimerSap.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxTimerSap.setStatus(_A)
class _AlaIpxTimerRip_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,180))
_AlaIpxTimerRip_Type.__name__=_D
_AlaIpxTimerRip_Object=MibTableColumn
alaIpxTimerRip=_AlaIpxTimerRip_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,3,1,1,3),_AlaIpxTimerRip_Type())
alaIpxTimerRip.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxTimerRip.setStatus(_A)
_AlaIpxTimerRowStatus_Type=RowStatus
_AlaIpxTimerRowStatus_Object=MibTableColumn
alaIpxTimerRowStatus=_AlaIpxTimerRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,1,3,1,1,4),_AlaIpxTimerRowStatus_Type())
alaIpxTimerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpxTimerRowStatus.setStatus(_A)
_AlcatelIND1IPXMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1IPXMIBConformance=_AlcatelIND1IPXMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2))
_AlcatelIND1IPXMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1IPXMIBCompliances=_AlcatelIND1IPXMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2,1))
_AlcatelIND1IPXMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1IPXMIBGroups=_AlcatelIND1IPXMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2,2))
alcatelIND1IPXMIBStaticRouteGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2,2,1))
alcatelIND1IPXMIBStaticRouteGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:alcatelIND1IPXMIBStaticRouteGroup.setStatus(_A)
alcatelIND1IPXMIBDefRouteGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2,2,2))
alcatelIND1IPXMIBDefRouteGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:alcatelIND1IPXMIBDefRouteGroup.setStatus(_A)
alcatelIND1IPXMIBExtMsgGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2,2,3))
alcatelIND1IPXMIBExtMsgGroup.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:alcatelIND1IPXMIBExtMsgGroup.setStatus(_A)
alcatelIND1IPXMIBFlushGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2,2,4))
alcatelIND1IPXMIBFlushGroup.setObjects((_B,_k))
if mibBuilder.loadTexts:alcatelIND1IPXMIBFlushGroup.setStatus(_A)
alcatelIND1IPXMIBRipSapFilterGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2,2,5))
alcatelIND1IPXMIBRipSapFilterGroup.setObjects(*((_B,_l),(_B,_m)))
if mibBuilder.loadTexts:alcatelIND1IPXMIBRipSapFilterGroup.setStatus(_A)
alcatelIND1IPXMIBWatchdogSpoofGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2,2,6))
alcatelIND1IPXMIBWatchdogSpoofGroup.setObjects(*((_B,_n),(_B,_o)))
if mibBuilder.loadTexts:alcatelIND1IPXMIBWatchdogSpoofGroup.setStatus(_A)
alcatelIND1IPXMIBSerialFilterGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2,2,7))
alcatelIND1IPXMIBSerialFilterGroup.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:alcatelIND1IPXMIBSerialFilterGroup.setStatus(_A)
alcatelIND1IPXMIBKeepaliveSpoofGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2,2,8))
alcatelIND1IPXMIBKeepaliveSpoofGroup.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:alcatelIND1IPXMIBKeepaliveSpoofGroup.setStatus(_A)
alcatelIND1IPXMIBType20Group=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2,2,9))
alcatelIND1IPXMIBType20Group.setObjects(*((_B,_t),(_B,_u)))
if mibBuilder.loadTexts:alcatelIND1IPXMIBType20Group.setStatus(_A)
alcatelIND1IPXMIBTimerGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2,2,10))
alcatelIND1IPXMIBTimerGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:alcatelIND1IPXMIBTimerGroup.setStatus(_A)
alcatelIND1IPXMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,8,1,2,1,1))
alcatelIND1IPXMIBCompliance.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:alcatelIND1IPXMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_F:NetNumber,_G:HostAddress,'alcatelIND1IPXMIB':alcatelIND1IPXMIB,'alcatelIND1IPXMIBObjects':alcatelIND1IPXMIBObjects,'alaIpxRoutingGroup':alaIpxRoutingGroup,'alaIpxStaticRouteTable':alaIpxStaticRouteTable,'alaIpxStaticRouteEntry':alaIpxStaticRouteEntry,_L:alaIpxStaticRouteNetNum,_a:alaIpxStaticRouteNextHopNet,_b:alaIpxStaticRouteNextHopNode,_c:alaIpxStaticRouteTicks,_d:alaIpxStaticRouteHopCount,_e:alaIpxStaticRouteRowStatus,'alaIpxDefRouteTable':alaIpxDefRouteTable,'alaIpxDefRouteEntry':alaIpxDefRouteEntry,_M:alaIpxDefRouteVlanId,_f:alaIpxDefRouteNet,_g:alaIpxDefRouteNode,_h:alaIpxDefRouteRowStatus,'alaIpxExtMsgTable':alaIpxExtMsgTable,'alaIpxExtMsgEntry':alaIpxExtMsgEntry,_N:alaIpxExtMsgVlanId,_i:alaIpxExtMsgMode,_j:alaIpxExtMsgRowStatus,_k:alaIpxFlush,'alaIpxFilterGroup':alaIpxFilterGroup,'alaIpxRipSapFilterTable':alaIpxRipSapFilterTable,'alaIpxRipSapFilterEntry':alaIpxRipSapFilterEntry,_O:alaIpxRipSapFilterVlanId,_P:alaIpxRipSapFilterType,_Q:alaIpxRipSapFilterNet,_R:alaIpxRipSapFilterNetMask,_S:alaIpxRipSapFilterNode,_T:alaIpxRipSapFilterNodeMask,_U:alaIpxRipSapFilterSvcType,_l:alaIpxRipSapFilterMode,_m:alaIpxRipSapFilterRowStatus,'alaIpxWatchdogSpoofTable':alaIpxWatchdogSpoofTable,'alaIpxWatchdogSpoofEntry':alaIpxWatchdogSpoofEntry,_V:alaIpxWatchdogSpoofVlanId,_n:alaIpxWatchdogSpoofMode,_o:alaIpxWatchdogSpoofRowStatus,'alaIpxSerialFilterTable':alaIpxSerialFilterTable,'alaIpxSerialFilterEntry':alaIpxSerialFilterEntry,_W:alaIpxSerialFilterVlanId,_p:alaIpxSerialFilterMode,_q:alaIpxSerialFilterRowStatus,'alaSpxKeepaliveSpoofTable':alaSpxKeepaliveSpoofTable,'alaSpxKeepaliveSpoofEntry':alaSpxKeepaliveSpoofEntry,_X:alaSpxKeepaliveSpoofVlanId,_r:alaSpxKeepaliveSpoofMode,_s:alaSpxKeepaliveSpoofRowStatus,'alaIpxType20Table':alaIpxType20Table,'alaIpxType20Entry':alaIpxType20Entry,_Y:alaIpxType20VlanId,_t:alaIpxType20Mode,_u:alaIpxType20RowStatus,'alaIpxTimerGroup':alaIpxTimerGroup,'alaIpxTimerTable':alaIpxTimerTable,'alaIpxTimerEntry':alaIpxTimerEntry,_Z:alaIpxTimerVlanId,_w:alaIpxTimerSap,_v:alaIpxTimerRip,_x:alaIpxTimerRowStatus,'alcatelIND1IPXMIBConformance':alcatelIND1IPXMIBConformance,'alcatelIND1IPXMIBCompliances':alcatelIND1IPXMIBCompliances,'alcatelIND1IPXMIBCompliance':alcatelIND1IPXMIBCompliance,'alcatelIND1IPXMIBGroups':alcatelIND1IPXMIBGroups,_y:alcatelIND1IPXMIBStaticRouteGroup,_z:alcatelIND1IPXMIBDefRouteGroup,_A0:alcatelIND1IPXMIBExtMsgGroup,_A1:alcatelIND1IPXMIBFlushGroup,_A2:alcatelIND1IPXMIBRipSapFilterGroup,_A3:alcatelIND1IPXMIBWatchdogSpoofGroup,_A4:alcatelIND1IPXMIBSerialFilterGroup,_A5:alcatelIND1IPXMIBKeepaliveSpoofGroup,_A6:alcatelIND1IPXMIBType20Group,_A7:alcatelIND1IPXMIBTimerGroup})