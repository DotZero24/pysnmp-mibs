_Q='mitelAccResTableTrapped'
_P='forward'
_O='filter'
_N='ifIndex'
_M='IF-MIB'
_L='read-only'
_K='mitelAccResTableOrder'
_J='mitelAccResTableIfIndex'
_I='one'
_H='zero'
_G='any'
_F='MITEL-IPFILTER-MIB'
_E='disabled'
_D='enabled'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_M,_N)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mitelIpGrpFilterGroup=ModuleIdentity((1,3,6,1,4,1,1027,4,8,1,1,1))
if mibBuilder.loadTexts:mitelIpGrpFilterGroup.setRevisions(('2003-03-24 09:25','1999-03-01 00:00'))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelIdentification_ObjectIdentity=ObjectIdentity
mitelIdentification=_MitelIdentification_ObjectIdentity((1,3,6,1,4,1,1027,1))
_MitelIdCallServers_ObjectIdentity=ObjectIdentity
mitelIdCallServers=_MitelIdCallServers_ObjectIdentity((1,3,6,1,4,1,1027,1,2))
_MitelIdCsIpera1000_ObjectIdentity=ObjectIdentity
mitelIdCsIpera1000=_MitelIdCsIpera1000_ObjectIdentity((1,3,6,1,4,1,1027,1,2,4))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelPropIpNetworking_ObjectIdentity=ObjectIdentity
mitelPropIpNetworking=_MitelPropIpNetworking_ObjectIdentity((1,3,6,1,4,1,1027,4,8))
_MitelIpNetRouter_ObjectIdentity=ObjectIdentity
mitelIpNetRouter=_MitelIpNetRouter_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1))
_MitelRouterIpGroup_ObjectIdentity=ObjectIdentity
mitelRouterIpGroup=_MitelRouterIpGroup_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1,1))
class _MitelFltGrpAccessRestrictEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelFltGrpAccessRestrictEnable_Type.__name__=_C
_MitelFltGrpAccessRestrictEnable_Object=MibScalar
mitelFltGrpAccessRestrictEnable=_MitelFltGrpAccessRestrictEnable_Object((1,3,6,1,4,1,1027,4,8,1,1,1,1),_MitelFltGrpAccessRestrictEnable_Type())
mitelFltGrpAccessRestrictEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelFltGrpAccessRestrictEnable.setStatus(_A)
_MitelFltGrpLogicalTable_Object=MibTable
mitelFltGrpLogicalTable=_MitelFltGrpLogicalTable_Object((1,3,6,1,4,1,1027,4,8,1,1,1,2))
if mibBuilder.loadTexts:mitelFltGrpLogicalTable.setStatus(_A)
_MitelFltGrpLogicalEntry_Object=MibTableRow
mitelFltGrpLogicalEntry=_MitelFltGrpLogicalEntry_Object((1,3,6,1,4,1,1027,4,8,1,1,1,2,1))
mitelFltGrpLogicalEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:mitelFltGrpLogicalEntry.setStatus(_A)
class _MitelLogTableAccessDef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_MitelLogTableAccessDef_Type.__name__=_C
_MitelLogTableAccessDef_Object=MibTableColumn
mitelLogTableAccessDef=_MitelLogTableAccessDef_Object((1,3,6,1,4,1,1027,4,8,1,1,1,2,1,1),_MitelLogTableAccessDef_Type())
mitelLogTableAccessDef.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelLogTableAccessDef.setStatus(_A)
class _MitelLogTableAllowSrcRouting_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelLogTableAllowSrcRouting_Type.__name__=_C
_MitelLogTableAllowSrcRouting_Object=MibTableColumn
mitelLogTableAllowSrcRouting=_MitelLogTableAllowSrcRouting_Object((1,3,6,1,4,1,1027,4,8,1,1,1,2,1,2),_MitelLogTableAllowSrcRouting_Type())
mitelLogTableAllowSrcRouting.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelLogTableAllowSrcRouting.setStatus(_A)
_MitelFltGrpAccessRestrictTable_Object=MibTable
mitelFltGrpAccessRestrictTable=_MitelFltGrpAccessRestrictTable_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3))
if mibBuilder.loadTexts:mitelFltGrpAccessRestrictTable.setStatus(_A)
_MitelFltGrpAccessRestrictEntry_Object=MibTableRow
mitelFltGrpAccessRestrictEntry=_MitelFltGrpAccessRestrictEntry_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1))
mitelFltGrpAccessRestrictEntry.setIndexNames((0,_F,_J),(0,_F,_K))
if mibBuilder.loadTexts:mitelFltGrpAccessRestrictEntry.setStatus(_A)
_MitelAccResTableIfIndex_Type=Integer32
_MitelAccResTableIfIndex_Object=MibTableColumn
mitelAccResTableIfIndex=_MitelAccResTableIfIndex_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,1),_MitelAccResTableIfIndex_Type())
mitelAccResTableIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:mitelAccResTableIfIndex.setStatus(_A)
_MitelAccResTableOrder_Type=Integer32
_MitelAccResTableOrder_Object=MibTableColumn
mitelAccResTableOrder=_MitelAccResTableOrder_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,2),_MitelAccResTableOrder_Type())
mitelAccResTableOrder.setMaxAccess(_L)
if mibBuilder.loadTexts:mitelAccResTableOrder.setStatus(_A)
class _MitelAccResTableType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),('neither',3)))
_MitelAccResTableType_Type.__name__=_C
_MitelAccResTableType_Object=MibTableColumn
mitelAccResTableType=_MitelAccResTableType_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,3),_MitelAccResTableType_Type())
mitelAccResTableType.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableType.setStatus(_A)
_MitelAccResTableSrcAddrFrom_Type=IpAddress
_MitelAccResTableSrcAddrFrom_Object=MibTableColumn
mitelAccResTableSrcAddrFrom=_MitelAccResTableSrcAddrFrom_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,4),_MitelAccResTableSrcAddrFrom_Type())
mitelAccResTableSrcAddrFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableSrcAddrFrom.setStatus(_A)
_MitelAccResTableSrcAddrTo_Type=IpAddress
_MitelAccResTableSrcAddrTo_Object=MibTableColumn
mitelAccResTableSrcAddrTo=_MitelAccResTableSrcAddrTo_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,5),_MitelAccResTableSrcAddrTo_Type())
mitelAccResTableSrcAddrTo.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableSrcAddrTo.setStatus(_A)
class _MitelAccResTableSrcAddrOutsideRange_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelAccResTableSrcAddrOutsideRange_Type.__name__=_C
_MitelAccResTableSrcAddrOutsideRange_Object=MibTableColumn
mitelAccResTableSrcAddrOutsideRange=_MitelAccResTableSrcAddrOutsideRange_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,6),_MitelAccResTableSrcAddrOutsideRange_Type())
mitelAccResTableSrcAddrOutsideRange.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableSrcAddrOutsideRange.setStatus(_A)
_MitelAccResTableDstAddrFrom_Type=IpAddress
_MitelAccResTableDstAddrFrom_Object=MibTableColumn
mitelAccResTableDstAddrFrom=_MitelAccResTableDstAddrFrom_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,7),_MitelAccResTableDstAddrFrom_Type())
mitelAccResTableDstAddrFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableDstAddrFrom.setStatus(_A)
_MitelAccResTableDstAddrTo_Type=IpAddress
_MitelAccResTableDstAddrTo_Object=MibTableColumn
mitelAccResTableDstAddrTo=_MitelAccResTableDstAddrTo_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,8),_MitelAccResTableDstAddrTo_Type())
mitelAccResTableDstAddrTo.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableDstAddrTo.setStatus(_A)
class _MitelAccResTableDstAddrOutsideRange_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelAccResTableDstAddrOutsideRange_Type.__name__=_C
_MitelAccResTableDstAddrOutsideRange_Object=MibTableColumn
mitelAccResTableDstAddrOutsideRange=_MitelAccResTableDstAddrOutsideRange_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,9),_MitelAccResTableDstAddrOutsideRange_Type())
mitelAccResTableDstAddrOutsideRange.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableDstAddrOutsideRange.setStatus(_A)
class _MitelAccResTableProtocolFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MitelAccResTableProtocolFrom_Type.__name__=_C
_MitelAccResTableProtocolFrom_Object=MibTableColumn
mitelAccResTableProtocolFrom=_MitelAccResTableProtocolFrom_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,10),_MitelAccResTableProtocolFrom_Type())
mitelAccResTableProtocolFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableProtocolFrom.setStatus(_A)
class _MitelAccResTableProtocolTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MitelAccResTableProtocolTo_Type.__name__=_C
_MitelAccResTableProtocolTo_Object=MibTableColumn
mitelAccResTableProtocolTo=_MitelAccResTableProtocolTo_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,11),_MitelAccResTableProtocolTo_Type())
mitelAccResTableProtocolTo.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableProtocolTo.setStatus(_A)
class _MitelAccResTableProtocolOutsideRange_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelAccResTableProtocolOutsideRange_Type.__name__=_C
_MitelAccResTableProtocolOutsideRange_Object=MibTableColumn
mitelAccResTableProtocolOutsideRange=_MitelAccResTableProtocolOutsideRange_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,12),_MitelAccResTableProtocolOutsideRange_Type())
mitelAccResTableProtocolOutsideRange.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableProtocolOutsideRange.setStatus(_A)
class _MitelAccResTableSrcPortFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MitelAccResTableSrcPortFrom_Type.__name__=_C
_MitelAccResTableSrcPortFrom_Object=MibTableColumn
mitelAccResTableSrcPortFrom=_MitelAccResTableSrcPortFrom_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,13),_MitelAccResTableSrcPortFrom_Type())
mitelAccResTableSrcPortFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableSrcPortFrom.setStatus(_A)
class _MitelAccResTableSrcPortTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MitelAccResTableSrcPortTo_Type.__name__=_C
_MitelAccResTableSrcPortTo_Object=MibTableColumn
mitelAccResTableSrcPortTo=_MitelAccResTableSrcPortTo_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,14),_MitelAccResTableSrcPortTo_Type())
mitelAccResTableSrcPortTo.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableSrcPortTo.setStatus(_A)
class _MitelAccResTableSrcPortOutsideRange_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelAccResTableSrcPortOutsideRange_Type.__name__=_C
_MitelAccResTableSrcPortOutsideRange_Object=MibTableColumn
mitelAccResTableSrcPortOutsideRange=_MitelAccResTableSrcPortOutsideRange_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,15),_MitelAccResTableSrcPortOutsideRange_Type())
mitelAccResTableSrcPortOutsideRange.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableSrcPortOutsideRange.setStatus(_A)
class _MitelAccResTableDstPortFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MitelAccResTableDstPortFrom_Type.__name__=_C
_MitelAccResTableDstPortFrom_Object=MibTableColumn
mitelAccResTableDstPortFrom=_MitelAccResTableDstPortFrom_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,16),_MitelAccResTableDstPortFrom_Type())
mitelAccResTableDstPortFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableDstPortFrom.setStatus(_A)
class _MitelAccResTableDstPortTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MitelAccResTableDstPortTo_Type.__name__=_C
_MitelAccResTableDstPortTo_Object=MibTableColumn
mitelAccResTableDstPortTo=_MitelAccResTableDstPortTo_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,17),_MitelAccResTableDstPortTo_Type())
mitelAccResTableDstPortTo.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableDstPortTo.setStatus(_A)
class _MitelAccResTableDstPortOutsideRange_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelAccResTableDstPortOutsideRange_Type.__name__=_C
_MitelAccResTableDstPortOutsideRange_Object=MibTableColumn
mitelAccResTableDstPortOutsideRange=_MitelAccResTableDstPortOutsideRange_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,18),_MitelAccResTableDstPortOutsideRange_Type())
mitelAccResTableDstPortOutsideRange.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableDstPortOutsideRange.setStatus(_A)
class _MitelAccResTableTcpSyn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_MitelAccResTableTcpSyn_Type.__name__=_C
_MitelAccResTableTcpSyn_Object=MibTableColumn
mitelAccResTableTcpSyn=_MitelAccResTableTcpSyn_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,19),_MitelAccResTableTcpSyn_Type())
mitelAccResTableTcpSyn.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableTcpSyn.setStatus(_A)
class _MitelAccResTableTcpAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_MitelAccResTableTcpAck_Type.__name__=_C
_MitelAccResTableTcpAck_Object=MibTableColumn
mitelAccResTableTcpAck=_MitelAccResTableTcpAck_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,20),_MitelAccResTableTcpAck_Type())
mitelAccResTableTcpAck.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableTcpAck.setStatus(_A)
class _MitelAccResTableTcpFin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_MitelAccResTableTcpFin_Type.__name__=_C
_MitelAccResTableTcpFin_Object=MibTableColumn
mitelAccResTableTcpFin=_MitelAccResTableTcpFin_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,21),_MitelAccResTableTcpFin_Type())
mitelAccResTableTcpFin.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableTcpFin.setStatus(_A)
class _MitelAccResTableTcpRst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_MitelAccResTableTcpRst_Type.__name__=_C
_MitelAccResTableTcpRst_Object=MibTableColumn
mitelAccResTableTcpRst=_MitelAccResTableTcpRst_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,22),_MitelAccResTableTcpRst_Type())
mitelAccResTableTcpRst.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableTcpRst.setStatus(_A)
class _MitelAccResTableMatchIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelAccResTableMatchIn_Type.__name__=_C
_MitelAccResTableMatchIn_Object=MibTableColumn
mitelAccResTableMatchIn=_MitelAccResTableMatchIn_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,23),_MitelAccResTableMatchIn_Type())
mitelAccResTableMatchIn.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableMatchIn.setStatus(_A)
class _MitelAccResTableMatchOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelAccResTableMatchOut_Type.__name__=_C
_MitelAccResTableMatchOut_Object=MibTableColumn
mitelAccResTableMatchOut=_MitelAccResTableMatchOut_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,24),_MitelAccResTableMatchOut_Type())
mitelAccResTableMatchOut.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableMatchOut.setStatus(_A)
class _MitelAccResTableLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelAccResTableLog_Type.__name__=_C
_MitelAccResTableLog_Object=MibTableColumn
mitelAccResTableLog=_MitelAccResTableLog_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,25),_MitelAccResTableLog_Type())
mitelAccResTableLog.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableLog.setStatus(_A)
class _MitelAccResTableTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelAccResTableTrap_Type.__name__=_C
_MitelAccResTableTrap_Object=MibTableColumn
mitelAccResTableTrap=_MitelAccResTableTrap_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,26),_MitelAccResTableTrap_Type())
mitelAccResTableTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelAccResTableTrap.setStatus(_A)
_MitelAccResTableStatus_Type=RowStatus
_MitelAccResTableStatus_Object=MibTableColumn
mitelAccResTableStatus=_MitelAccResTableStatus_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,27),_MitelAccResTableStatus_Type())
mitelAccResTableStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:mitelAccResTableStatus.setStatus(_A)
_MitelAccResTableCount_Type=Integer32
_MitelAccResTableCount_Object=MibTableColumn
mitelAccResTableCount=_MitelAccResTableCount_Object((1,3,6,1,4,1,1027,4,8,1,1,1,3,1,28),_MitelAccResTableCount_Type())
mitelAccResTableCount.setMaxAccess(_L)
if mibBuilder.loadTexts:mitelAccResTableCount.setStatus(_A)
mitelAccResTableTrapped=NotificationType((1,3,6,1,4,1,1027,1,2,4,0,402))
mitelAccResTableTrapped.setObjects(*((_F,_J),(_F,_K)))
if mibBuilder.loadTexts:mitelAccResTableTrapped.setStatus(_A)
mitelIpera1000Notifications=NotificationGroup((1,3,6,1,4,1,1027,1,2,4,0))
mitelIpera1000Notifications.setObjects((_F,_Q))
if mibBuilder.loadTexts:mitelIpera1000Notifications.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'mitel':mitel,'mitelIdentification':mitelIdentification,'mitelIdCallServers':mitelIdCallServers,'mitelIdCsIpera1000':mitelIdCsIpera1000,'mitelIpera1000Notifications':mitelIpera1000Notifications,_Q:mitelAccResTableTrapped,'mitelProprietary':mitelProprietary,'mitelPropIpNetworking':mitelPropIpNetworking,'mitelIpNetRouter':mitelIpNetRouter,'mitelRouterIpGroup':mitelRouterIpGroup,'mitelIpGrpFilterGroup':mitelIpGrpFilterGroup,'mitelFltGrpAccessRestrictEnable':mitelFltGrpAccessRestrictEnable,'mitelFltGrpLogicalTable':mitelFltGrpLogicalTable,'mitelFltGrpLogicalEntry':mitelFltGrpLogicalEntry,'mitelLogTableAccessDef':mitelLogTableAccessDef,'mitelLogTableAllowSrcRouting':mitelLogTableAllowSrcRouting,'mitelFltGrpAccessRestrictTable':mitelFltGrpAccessRestrictTable,'mitelFltGrpAccessRestrictEntry':mitelFltGrpAccessRestrictEntry,_J:mitelAccResTableIfIndex,_K:mitelAccResTableOrder,'mitelAccResTableType':mitelAccResTableType,'mitelAccResTableSrcAddrFrom':mitelAccResTableSrcAddrFrom,'mitelAccResTableSrcAddrTo':mitelAccResTableSrcAddrTo,'mitelAccResTableSrcAddrOutsideRange':mitelAccResTableSrcAddrOutsideRange,'mitelAccResTableDstAddrFrom':mitelAccResTableDstAddrFrom,'mitelAccResTableDstAddrTo':mitelAccResTableDstAddrTo,'mitelAccResTableDstAddrOutsideRange':mitelAccResTableDstAddrOutsideRange,'mitelAccResTableProtocolFrom':mitelAccResTableProtocolFrom,'mitelAccResTableProtocolTo':mitelAccResTableProtocolTo,'mitelAccResTableProtocolOutsideRange':mitelAccResTableProtocolOutsideRange,'mitelAccResTableSrcPortFrom':mitelAccResTableSrcPortFrom,'mitelAccResTableSrcPortTo':mitelAccResTableSrcPortTo,'mitelAccResTableSrcPortOutsideRange':mitelAccResTableSrcPortOutsideRange,'mitelAccResTableDstPortFrom':mitelAccResTableDstPortFrom,'mitelAccResTableDstPortTo':mitelAccResTableDstPortTo,'mitelAccResTableDstPortOutsideRange':mitelAccResTableDstPortOutsideRange,'mitelAccResTableTcpSyn':mitelAccResTableTcpSyn,'mitelAccResTableTcpAck':mitelAccResTableTcpAck,'mitelAccResTableTcpFin':mitelAccResTableTcpFin,'mitelAccResTableTcpRst':mitelAccResTableTcpRst,'mitelAccResTableMatchIn':mitelAccResTableMatchIn,'mitelAccResTableMatchOut':mitelAccResTableMatchOut,'mitelAccResTableLog':mitelAccResTableLog,'mitelAccResTableTrap':mitelAccResTableTrap,'mitelAccResTableStatus':mitelAccResTableStatus,'mitelAccResTableCount':mitelAccResTableCount})