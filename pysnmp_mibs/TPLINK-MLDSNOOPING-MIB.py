_P='tpMldStaticVlanID'
_O='tpMldStaticMulticastIP'
_N='tpMldVlanID'
_M='tpMldMulticastIP'
_L='tpMldVlanId'
_K='ifIndex'
_J='IF-MIB'
_I='TPLINK-MLDSNOOPING-MIB'
_H='enable'
_G='disable'
_F='OctetString'
_E='read-only'
_D='read-write'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkMldSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,43))
if mibBuilder.loadTexts:tplinkMldSnoopingMIB.setRevisions(('2012-12-14 14:32',))
_TplinkMldSnoopingMIBObjects_ObjectIdentity=ObjectIdentity
tplinkMldSnoopingMIBObjects=_TplinkMldSnoopingMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,43,1))
_TpMldSnooping_ObjectIdentity=ObjectIdentity
tpMldSnooping=_TpMldSnooping_ObjectIdentity((1,3,6,1,4,1,11863,6,43,1,1))
_TpMldSnoopingGlobalConfig_ObjectIdentity=ObjectIdentity
tpMldSnoopingGlobalConfig=_TpMldSnoopingGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,43,1,1,1))
class _TpMldSnoopingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_TpMldSnoopingEnable_Type.__name__=_B
_TpMldSnoopingEnable_Object=MibScalar
tpMldSnoopingEnable=_TpMldSnoopingEnable_Object((1,3,6,1,4,1,11863,6,43,1,1,1,1),_TpMldSnoopingEnable_Type())
tpMldSnoopingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMldSnoopingEnable.setStatus(_A)
class _TpMldUnknownMulticastPacket_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('forward',0),('discard',1)))
_TpMldUnknownMulticastPacket_Type.__name__=_B
_TpMldUnknownMulticastPacket_Object=MibScalar
tpMldUnknownMulticastPacket=_TpMldUnknownMulticastPacket_Object((1,3,6,1,4,1,11863,6,43,1,1,1,2),_TpMldUnknownMulticastPacket_Type())
tpMldUnknownMulticastPacket.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMldUnknownMulticastPacket.setStatus(_A)
_TpMldPortConfig_ObjectIdentity=ObjectIdentity
tpMldPortConfig=_TpMldPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,43,1,1,2))
_TpMldPortTable_Object=MibTable
tpMldPortTable=_TpMldPortTable_Object((1,3,6,1,4,1,11863,6,43,1,1,2,1))
if mibBuilder.loadTexts:tpMldPortTable.setStatus(_A)
_TpMldPortEntry_Object=MibTableRow
tpMldPortEntry=_TpMldPortEntry_Object((1,3,6,1,4,1,11863,6,43,1,1,2,1,1))
tpMldPortEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:tpMldPortEntry.setStatus(_A)
class _TpMldSnoopingPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_TpMldSnoopingPortEnable_Type.__name__=_B
_TpMldSnoopingPortEnable_Object=MibTableColumn
tpMldSnoopingPortEnable=_TpMldSnoopingPortEnable_Object((1,3,6,1,4,1,11863,6,43,1,1,2,1,1,2),_TpMldSnoopingPortEnable_Type())
tpMldSnoopingPortEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMldSnoopingPortEnable.setStatus(_A)
class _TpMldFastLeavePortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_TpMldFastLeavePortEnable_Type.__name__=_B
_TpMldFastLeavePortEnable_Object=MibTableColumn
tpMldFastLeavePortEnable=_TpMldFastLeavePortEnable_Object((1,3,6,1,4,1,11863,6,43,1,1,2,1,1,3),_TpMldFastLeavePortEnable_Type())
tpMldFastLeavePortEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMldFastLeavePortEnable.setStatus(_A)
class _TpMldPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpMldPortLag_Type.__name__=_F
_TpMldPortLag_Object=MibTableColumn
tpMldPortLag=_TpMldPortLag_Object((1,3,6,1,4,1,11863,6,43,1,1,2,1,1,4),_TpMldPortLag_Type())
tpMldPortLag.setMaxAccess(_E)
if mibBuilder.loadTexts:tpMldPortLag.setStatus(_A)
_TpMldVlanConfig_ObjectIdentity=ObjectIdentity
tpMldVlanConfig=_TpMldVlanConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,43,1,1,3))
_TpMldVlanTable_Object=MibTable
tpMldVlanTable=_TpMldVlanTable_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1))
if mibBuilder.loadTexts:tpMldVlanTable.setStatus(_A)
_TpMldVlanEntry_Object=MibTableRow
tpMldVlanEntry=_TpMldVlanEntry_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1))
tpMldVlanEntry.setIndexNames((0,_I,_L))
if mibBuilder.loadTexts:tpMldVlanEntry.setStatus(_A)
class _TpMldVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_TpMldVlanId_Type.__name__=_B
_TpMldVlanId_Object=MibTableColumn
tpMldVlanId=_TpMldVlanId_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,1),_TpMldVlanId_Type())
tpMldVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:tpMldVlanId.setStatus(_A)
class _TpMldVlanEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_TpMldVlanEnable_Type.__name__=_B
_TpMldVlanEnable_Object=MibTableColumn
tpMldVlanEnable=_TpMldVlanEnable_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,2),_TpMldVlanEnable_Type())
tpMldVlanEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMldVlanEnable.setStatus(_A)
class _TpMldVlanFastLeave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_TpMldVlanFastLeave_Type.__name__=_B
_TpMldVlanFastLeave_Object=MibTableColumn
tpMldVlanFastLeave=_TpMldVlanFastLeave_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,3),_TpMldVlanFastLeave_Type())
tpMldVlanFastLeave.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMldVlanFastLeave.setStatus(_A)
class _TpMldVlanReportSuppression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_TpMldVlanReportSuppression_Type.__name__=_B
_TpMldVlanReportSuppression_Object=MibTableColumn
tpMldVlanReportSuppression=_TpMldVlanReportSuppression_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,4),_TpMldVlanReportSuppression_Type())
tpMldVlanReportSuppression.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMldVlanReportSuppression.setStatus(_A)
class _TpMldRouterTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_TpMldRouterTime_Type.__name__=_B
_TpMldRouterTime_Object=MibTableColumn
tpMldRouterTime=_TpMldRouterTime_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,5),_TpMldRouterTime_Type())
tpMldRouterTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldRouterTime.setStatus(_A)
class _TpMldMemberTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_TpMldMemberTime_Type.__name__=_B
_TpMldMemberTime_Object=MibTableColumn
tpMldMemberTime=_TpMldMemberTime_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,6),_TpMldMemberTime_Type())
tpMldMemberTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldMemberTime.setStatus(_A)
class _TpMldLeaveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_TpMldLeaveTime_Type.__name__=_B
_TpMldLeaveTime_Object=MibTableColumn
tpMldLeaveTime=_TpMldLeaveTime_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,7),_TpMldLeaveTime_Type())
tpMldLeaveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldLeaveTime.setStatus(_A)
class _TpMldRouterPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpMldRouterPort_Type.__name__=_F
_TpMldRouterPort_Object=MibTableColumn
tpMldRouterPort=_TpMldRouterPort_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,8),_TpMldRouterPort_Type())
tpMldRouterPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldRouterPort.setStatus(_A)
class _TpMldForbiddenRouterPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpMldForbiddenRouterPort_Type.__name__=_F
_TpMldForbiddenRouterPort_Object=MibTableColumn
tpMldForbiddenRouterPort=_TpMldForbiddenRouterPort_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,9),_TpMldForbiddenRouterPort_Type())
tpMldForbiddenRouterPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldForbiddenRouterPort.setStatus(_A)
class _TpMldQueryEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_TpMldQueryEnable_Type.__name__=_B
_TpMldQueryEnable_Object=MibTableColumn
tpMldQueryEnable=_TpMldQueryEnable_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,10),_TpMldQueryEnable_Type())
tpMldQueryEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMldQueryEnable.setStatus(_A)
class _TpMldQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_TpMldQueryInterval_Type.__name__=_B
_TpMldQueryInterval_Object=MibTableColumn
tpMldQueryInterval=_TpMldQueryInterval_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,11),_TpMldQueryInterval_Type())
tpMldQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldQueryInterval.setStatus(_A)
class _TpMldQueryMaxResponseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_TpMldQueryMaxResponseTime_Type.__name__=_B
_TpMldQueryMaxResponseTime_Object=MibTableColumn
tpMldQueryMaxResponseTime=_TpMldQueryMaxResponseTime_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,12),_TpMldQueryMaxResponseTime_Type())
tpMldQueryMaxResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldQueryMaxResponseTime.setStatus(_A)
_TpMldQueryGeneralSrcIp_Type=OctetString
_TpMldQueryGeneralSrcIp_Object=MibTableColumn
tpMldQueryGeneralSrcIp=_TpMldQueryGeneralSrcIp_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,13),_TpMldQueryGeneralSrcIp_Type())
tpMldQueryGeneralSrcIp.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldQueryGeneralSrcIp.setStatus(_A)
class _TpMldQueryLastMemberCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_TpMldQueryLastMemberCount_Type.__name__=_B
_TpMldQueryLastMemberCount_Object=MibTableColumn
tpMldQueryLastMemberCount=_TpMldQueryLastMemberCount_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,14),_TpMldQueryLastMemberCount_Type())
tpMldQueryLastMemberCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldQueryLastMemberCount.setStatus(_A)
class _TpMldQueryLastMemberInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_TpMldQueryLastMemberInterval_Type.__name__=_B
_TpMldQueryLastMemberInterval_Object=MibTableColumn
tpMldQueryLastMemberInterval=_TpMldQueryLastMemberInterval_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,15),_TpMldQueryLastMemberInterval_Type())
tpMldQueryLastMemberInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldQueryLastMemberInterval.setStatus(_A)
_TpMldVlanStatus_Type=TPRowStatus
_TpMldVlanStatus_Object=MibTableColumn
tpMldVlanStatus=_TpMldVlanStatus_Object((1,3,6,1,4,1,11863,6,43,1,1,3,1,1,16),_TpMldVlanStatus_Type())
tpMldVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldVlanStatus.setStatus(_A)
_TpMldFilter_ObjectIdentity=ObjectIdentity
tpMldFilter=_TpMldFilter_ObjectIdentity((1,3,6,1,4,1,11863,6,43,1,2))
_TpMldPortFilterConfig_ObjectIdentity=ObjectIdentity
tpMldPortFilterConfig=_TpMldPortFilterConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,43,1,2,1))
_TpMldFilterPortTable_Object=MibTable
tpMldFilterPortTable=_TpMldFilterPortTable_Object((1,3,6,1,4,1,11863,6,43,1,2,1,1))
if mibBuilder.loadTexts:tpMldFilterPortTable.setStatus(_A)
_TpMldFilterPortEntry_Object=MibTableRow
tpMldFilterPortEntry=_TpMldFilterPortEntry_Object((1,3,6,1,4,1,11863,6,43,1,2,1,1,1))
tpMldFilterPortEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:tpMldFilterPortEntry.setStatus(_A)
class _TpMldFilterMaxGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_TpMldFilterMaxGroup_Type.__name__=_B
_TpMldFilterMaxGroup_Object=MibTableColumn
tpMldFilterMaxGroup=_TpMldFilterMaxGroup_Object((1,3,6,1,4,1,11863,6,43,1,2,1,1,1,2),_TpMldFilterMaxGroup_Type())
tpMldFilterMaxGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMldFilterMaxGroup.setStatus(_A)
class _TpMldFilterMaxGroupAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('drop',0),('replace',1)))
_TpMldFilterMaxGroupAction_Type.__name__=_B
_TpMldFilterMaxGroupAction_Object=MibTableColumn
tpMldFilterMaxGroupAction=_TpMldFilterMaxGroupAction_Object((1,3,6,1,4,1,11863,6,43,1,2,1,1,1,3),_TpMldFilterMaxGroupAction_Type())
tpMldFilterMaxGroupAction.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMldFilterMaxGroupAction.setStatus(_A)
class _TpMldFilterBindAddrId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_TpMldFilterBindAddrId_Type.__name__=_F
_TpMldFilterBindAddrId_Object=MibTableColumn
tpMldFilterBindAddrId=_TpMldFilterBindAddrId_Object((1,3,6,1,4,1,11863,6,43,1,2,1,1,1,4),_TpMldFilterBindAddrId_Type())
tpMldFilterBindAddrId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMldFilterBindAddrId.setStatus(_A)
class _TpMldFilterPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpMldFilterPortLag_Type.__name__=_F
_TpMldFilterPortLag_Object=MibTableColumn
tpMldFilterPortLag=_TpMldFilterPortLag_Object((1,3,6,1,4,1,11863,6,43,1,2,1,1,1,5),_TpMldFilterPortLag_Type())
tpMldFilterPortLag.setMaxAccess(_E)
if mibBuilder.loadTexts:tpMldFilterPortLag.setStatus(_A)
_TpMldPacketStatistic_ObjectIdentity=ObjectIdentity
tpMldPacketStatistic=_TpMldPacketStatistic_ObjectIdentity((1,3,6,1,4,1,11863,6,43,1,3))
_TpMldPktStat_ObjectIdentity=ObjectIdentity
tpMldPktStat=_TpMldPktStat_ObjectIdentity((1,3,6,1,4,1,11863,6,43,1,3,1))
_TpMldPktStatTable_Object=MibTable
tpMldPktStatTable=_TpMldPktStatTable_Object((1,3,6,1,4,1,11863,6,43,1,3,1,1))
if mibBuilder.loadTexts:tpMldPktStatTable.setStatus(_A)
_TpMldPktStatEntry_Object=MibTableRow
tpMldPktStatEntry=_TpMldPktStatEntry_Object((1,3,6,1,4,1,11863,6,43,1,3,1,1,1))
tpMldPktStatEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:tpMldPktStatEntry.setStatus(_A)
_TpMldQueryPktStat_Type=Integer32
_TpMldQueryPktStat_Object=MibTableColumn
tpMldQueryPktStat=_TpMldQueryPktStat_Object((1,3,6,1,4,1,11863,6,43,1,3,1,1,1,2),_TpMldQueryPktStat_Type())
tpMldQueryPktStat.setMaxAccess(_E)
if mibBuilder.loadTexts:tpMldQueryPktStat.setStatus(_A)
_TpMldReportV1PktStat_Type=Integer32
_TpMldReportV1PktStat_Object=MibTableColumn
tpMldReportV1PktStat=_TpMldReportV1PktStat_Object((1,3,6,1,4,1,11863,6,43,1,3,1,1,1,3),_TpMldReportV1PktStat_Type())
tpMldReportV1PktStat.setMaxAccess(_E)
if mibBuilder.loadTexts:tpMldReportV1PktStat.setStatus(_A)
_TpMldReportV2PktStat_Type=Integer32
_TpMldReportV2PktStat_Object=MibTableColumn
tpMldReportV2PktStat=_TpMldReportV2PktStat_Object((1,3,6,1,4,1,11863,6,43,1,3,1,1,1,4),_TpMldReportV2PktStat_Type())
tpMldReportV2PktStat.setMaxAccess(_E)
if mibBuilder.loadTexts:tpMldReportV2PktStat.setStatus(_A)
_TpMldDonePktStat_Type=Integer32
_TpMldDonePktStat_Object=MibTableColumn
tpMldDonePktStat=_TpMldDonePktStat_Object((1,3,6,1,4,1,11863,6,43,1,3,1,1,1,6),_TpMldDonePktStat_Type())
tpMldDonePktStat.setMaxAccess(_E)
if mibBuilder.loadTexts:tpMldDonePktStat.setStatus(_A)
_TpMldErrorPktStat_Type=Integer32
_TpMldErrorPktStat_Object=MibTableColumn
tpMldErrorPktStat=_TpMldErrorPktStat_Object((1,3,6,1,4,1,11863,6,43,1,3,1,1,1,7),_TpMldErrorPktStat_Type())
tpMldErrorPktStat.setMaxAccess(_E)
if mibBuilder.loadTexts:tpMldErrorPktStat.setStatus(_A)
class _TpIpMldPktStatClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('commit',1))
_TpIpMldPktStatClear_Type.__name__=_B
_TpIpMldPktStatClear_Object=MibScalar
tpIpMldPktStatClear=_TpIpMldPktStatClear_Object((1,3,6,1,4,1,11863,6,43,1,3,1,2),_TpIpMldPktStatClear_Type())
tpIpMldPktStatClear.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIpMldPktStatClear.setStatus(_A)
_TpMldMultigroup_ObjectIdentity=ObjectIdentity
tpMldMultigroup=_TpMldMultigroup_ObjectIdentity((1,3,6,1,4,1,11863,6,43,1,4))
_TpMldMulticastGroups_ObjectIdentity=ObjectIdentity
tpMldMulticastGroups=_TpMldMulticastGroups_ObjectIdentity((1,3,6,1,4,1,11863,6,43,1,4,1))
_TpMldMulticastGroupTable_Object=MibTable
tpMldMulticastGroupTable=_TpMldMulticastGroupTable_Object((1,3,6,1,4,1,11863,6,43,1,4,1,1))
if mibBuilder.loadTexts:tpMldMulticastGroupTable.setStatus(_A)
_TpMldMulticastGroupEntry_Object=MibTableRow
tpMldMulticastGroupEntry=_TpMldMulticastGroupEntry_Object((1,3,6,1,4,1,11863,6,43,1,4,1,1,1))
tpMldMulticastGroupEntry.setIndexNames((0,_I,_M),(0,_I,_N))
if mibBuilder.loadTexts:tpMldMulticastGroupEntry.setStatus(_A)
_TpMldMulticastIP_Type=OctetString
_TpMldMulticastIP_Object=MibTableColumn
tpMldMulticastIP=_TpMldMulticastIP_Object((1,3,6,1,4,1,11863,6,43,1,4,1,1,1,1),_TpMldMulticastIP_Type())
tpMldMulticastIP.setMaxAccess(_E)
if mibBuilder.loadTexts:tpMldMulticastIP.setStatus(_A)
_TpMldVlanID_Type=Integer32
_TpMldVlanID_Object=MibTableColumn
tpMldVlanID=_TpMldVlanID_Object((1,3,6,1,4,1,11863,6,43,1,4,1,1,1,2),_TpMldVlanID_Type())
tpMldVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:tpMldVlanID.setStatus(_A)
class _TpMldForwardPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_TpMldForwardPorts_Type.__name__=_F
_TpMldForwardPorts_Object=MibTableColumn
tpMldForwardPorts=_TpMldForwardPorts_Object((1,3,6,1,4,1,11863,6,43,1,4,1,1,1,3),_TpMldForwardPorts_Type())
tpMldForwardPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:tpMldForwardPorts.setStatus(_A)
class _TpMldGrouptype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('static',0),('dynamic',1)))
_TpMldGrouptype_Type.__name__=_B
_TpMldGrouptype_Object=MibTableColumn
tpMldGrouptype=_TpMldGrouptype_Object((1,3,6,1,4,1,11863,6,43,1,4,1,1,1,4),_TpMldGrouptype_Type())
tpMldGrouptype.setMaxAccess(_E)
if mibBuilder.loadTexts:tpMldGrouptype.setStatus(_A)
_TpMldStaticMultigroup_ObjectIdentity=ObjectIdentity
tpMldStaticMultigroup=_TpMldStaticMultigroup_ObjectIdentity((1,3,6,1,4,1,11863,6,43,1,5))
_TpMldMulticastStaticGroups_ObjectIdentity=ObjectIdentity
tpMldMulticastStaticGroups=_TpMldMulticastStaticGroups_ObjectIdentity((1,3,6,1,4,1,11863,6,43,1,5,1))
_TpMldMulticastStaticGroupTable_Object=MibTable
tpMldMulticastStaticGroupTable=_TpMldMulticastStaticGroupTable_Object((1,3,6,1,4,1,11863,6,43,1,5,1,1))
if mibBuilder.loadTexts:tpMldMulticastStaticGroupTable.setStatus(_A)
_TpMldMulticastStaticGroupEntry_Object=MibTableRow
tpMldMulticastStaticGroupEntry=_TpMldMulticastStaticGroupEntry_Object((1,3,6,1,4,1,11863,6,43,1,5,1,1,1))
tpMldMulticastStaticGroupEntry.setIndexNames((0,_I,_O),(0,_I,_P))
if mibBuilder.loadTexts:tpMldMulticastStaticGroupEntry.setStatus(_A)
_TpMldStaticMulticastIP_Type=OctetString
_TpMldStaticMulticastIP_Object=MibTableColumn
tpMldStaticMulticastIP=_TpMldStaticMulticastIP_Object((1,3,6,1,4,1,11863,6,43,1,5,1,1,1,1),_TpMldStaticMulticastIP_Type())
tpMldStaticMulticastIP.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldStaticMulticastIP.setStatus(_A)
_TpMldStaticVlanID_Type=Integer32
_TpMldStaticVlanID_Object=MibTableColumn
tpMldStaticVlanID=_TpMldStaticVlanID_Object((1,3,6,1,4,1,11863,6,43,1,5,1,1,1,2),_TpMldStaticVlanID_Type())
tpMldStaticVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldStaticVlanID.setStatus(_A)
class _TpMldStaticForwardPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_TpMldStaticForwardPorts_Type.__name__=_F
_TpMldStaticForwardPorts_Object=MibTableColumn
tpMldStaticForwardPorts=_TpMldStaticForwardPorts_Object((1,3,6,1,4,1,11863,6,43,1,5,1,1,1,3),_TpMldStaticForwardPorts_Type())
tpMldStaticForwardPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldStaticForwardPorts.setStatus(_A)
_TpMldStaticGroupStatus_Type=TPRowStatus
_TpMldStaticGroupStatus_Object=MibTableColumn
tpMldStaticGroupStatus=_TpMldStaticGroupStatus_Object((1,3,6,1,4,1,11863,6,43,1,5,1,1,1,4),_TpMldStaticGroupStatus_Type())
tpMldStaticGroupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMldStaticGroupStatus.setStatus(_A)
_TplinkMldSnoopingNotifications_ObjectIdentity=ObjectIdentity
tplinkMldSnoopingNotifications=_TplinkMldSnoopingNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,43,2))
mibBuilder.exportSymbols(_I,**{'tplinkMldSnoopingMIB':tplinkMldSnoopingMIB,'tplinkMldSnoopingMIBObjects':tplinkMldSnoopingMIBObjects,'tpMldSnooping':tpMldSnooping,'tpMldSnoopingGlobalConfig':tpMldSnoopingGlobalConfig,'tpMldSnoopingEnable':tpMldSnoopingEnable,'tpMldUnknownMulticastPacket':tpMldUnknownMulticastPacket,'tpMldPortConfig':tpMldPortConfig,'tpMldPortTable':tpMldPortTable,'tpMldPortEntry':tpMldPortEntry,'tpMldSnoopingPortEnable':tpMldSnoopingPortEnable,'tpMldFastLeavePortEnable':tpMldFastLeavePortEnable,'tpMldPortLag':tpMldPortLag,'tpMldVlanConfig':tpMldVlanConfig,'tpMldVlanTable':tpMldVlanTable,'tpMldVlanEntry':tpMldVlanEntry,_L:tpMldVlanId,'tpMldVlanEnable':tpMldVlanEnable,'tpMldVlanFastLeave':tpMldVlanFastLeave,'tpMldVlanReportSuppression':tpMldVlanReportSuppression,'tpMldRouterTime':tpMldRouterTime,'tpMldMemberTime':tpMldMemberTime,'tpMldLeaveTime':tpMldLeaveTime,'tpMldRouterPort':tpMldRouterPort,'tpMldForbiddenRouterPort':tpMldForbiddenRouterPort,'tpMldQueryEnable':tpMldQueryEnable,'tpMldQueryInterval':tpMldQueryInterval,'tpMldQueryMaxResponseTime':tpMldQueryMaxResponseTime,'tpMldQueryGeneralSrcIp':tpMldQueryGeneralSrcIp,'tpMldQueryLastMemberCount':tpMldQueryLastMemberCount,'tpMldQueryLastMemberInterval':tpMldQueryLastMemberInterval,'tpMldVlanStatus':tpMldVlanStatus,'tpMldFilter':tpMldFilter,'tpMldPortFilterConfig':tpMldPortFilterConfig,'tpMldFilterPortTable':tpMldFilterPortTable,'tpMldFilterPortEntry':tpMldFilterPortEntry,'tpMldFilterMaxGroup':tpMldFilterMaxGroup,'tpMldFilterMaxGroupAction':tpMldFilterMaxGroupAction,'tpMldFilterBindAddrId':tpMldFilterBindAddrId,'tpMldFilterPortLag':tpMldFilterPortLag,'tpMldPacketStatistic':tpMldPacketStatistic,'tpMldPktStat':tpMldPktStat,'tpMldPktStatTable':tpMldPktStatTable,'tpMldPktStatEntry':tpMldPktStatEntry,'tpMldQueryPktStat':tpMldQueryPktStat,'tpMldReportV1PktStat':tpMldReportV1PktStat,'tpMldReportV2PktStat':tpMldReportV2PktStat,'tpMldDonePktStat':tpMldDonePktStat,'tpMldErrorPktStat':tpMldErrorPktStat,'tpIpMldPktStatClear':tpIpMldPktStatClear,'tpMldMultigroup':tpMldMultigroup,'tpMldMulticastGroups':tpMldMulticastGroups,'tpMldMulticastGroupTable':tpMldMulticastGroupTable,'tpMldMulticastGroupEntry':tpMldMulticastGroupEntry,_M:tpMldMulticastIP,_N:tpMldVlanID,'tpMldForwardPorts':tpMldForwardPorts,'tpMldGrouptype':tpMldGrouptype,'tpMldStaticMultigroup':tpMldStaticMultigroup,'tpMldMulticastStaticGroups':tpMldMulticastStaticGroups,'tpMldMulticastStaticGroupTable':tpMldMulticastStaticGroupTable,'tpMldMulticastStaticGroupEntry':tpMldMulticastStaticGroupEntry,_O:tpMldStaticMulticastIP,_P:tpMldStaticVlanID,'tpMldStaticForwardPorts':tpMldStaticForwardPorts,'tpMldStaticGroupStatus':tpMldStaticGroupStatus,'tplinkMldSnoopingNotifications':tplinkMldSnoopingNotifications})