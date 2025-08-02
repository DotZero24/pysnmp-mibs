_P='tpIgmpStaticVlanID'
_O='tpIgmpStaticMulticastIP'
_N='tpIgmpVlanID'
_M='tpIgmpMulticastIP'
_L='tpIgmpVlanId'
_K='ifIndex'
_J='IF-MIB'
_I='TPLINK-IGMPSNOOPING-MIB'
_H='OctetString'
_G='enable'
_F='disable'
_E='read-create'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkIgmpSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,25))
if mibBuilder.loadTexts:tplinkIgmpSnoopingMIB.setRevisions(('2012-12-14 14:32',))
_TplinkIgmpSnoopingMIBObjects_ObjectIdentity=ObjectIdentity
tplinkIgmpSnoopingMIBObjects=_TplinkIgmpSnoopingMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1))
_TpIgmpSnooping_ObjectIdentity=ObjectIdentity
tpIgmpSnooping=_TpIgmpSnooping_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,1))
_TpIgmpSnoopingGlobalConfig_ObjectIdentity=ObjectIdentity
tpIgmpSnoopingGlobalConfig=_TpIgmpSnoopingGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,1,1))
class _TpIgmpSnoopingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIgmpSnoopingEnable_Type.__name__=_B
_TpIgmpSnoopingEnable_Object=MibScalar
tpIgmpSnoopingEnable=_TpIgmpSnoopingEnable_Object((1,3,6,1,4,1,11863,6,25,1,1,1,1),_TpIgmpSnoopingEnable_Type())
tpIgmpSnoopingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpSnoopingEnable.setStatus(_A)
class _TpIgmpSnoopingVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('igmpv1',0),('igmpv2',1),('igmpv3',2)))
_TpIgmpSnoopingVersion_Type.__name__=_B
_TpIgmpSnoopingVersion_Object=MibScalar
tpIgmpSnoopingVersion=_TpIgmpSnoopingVersion_Object((1,3,6,1,4,1,11863,6,25,1,1,1,2),_TpIgmpSnoopingVersion_Type())
tpIgmpSnoopingVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpSnoopingVersion.setStatus(_A)
class _TpUnknownMulticastPacket_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('forward',0),('discard',1)))
_TpUnknownMulticastPacket_Type.__name__=_B
_TpUnknownMulticastPacket_Object=MibScalar
tpUnknownMulticastPacket=_TpUnknownMulticastPacket_Object((1,3,6,1,4,1,11863,6,25,1,1,1,3),_TpUnknownMulticastPacket_Type())
tpUnknownMulticastPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:tpUnknownMulticastPacket.setStatus(_A)
class _TpIgmpHeaderValidation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIgmpHeaderValidation_Type.__name__=_B
_TpIgmpHeaderValidation_Object=MibScalar
tpIgmpHeaderValidation=_TpIgmpHeaderValidation_Object((1,3,6,1,4,1,11863,6,25,1,1,1,4),_TpIgmpHeaderValidation_Type())
tpIgmpHeaderValidation.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpHeaderValidation.setStatus(_A)
_TpIgmpPortConfig_ObjectIdentity=ObjectIdentity
tpIgmpPortConfig=_TpIgmpPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,1,2))
_TpIgmpPortTable_Object=MibTable
tpIgmpPortTable=_TpIgmpPortTable_Object((1,3,6,1,4,1,11863,6,25,1,1,2,1))
if mibBuilder.loadTexts:tpIgmpPortTable.setStatus(_A)
_TpIgmpPortEntry_Object=MibTableRow
tpIgmpPortEntry=_TpIgmpPortEntry_Object((1,3,6,1,4,1,11863,6,25,1,1,2,1,1))
tpIgmpPortEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:tpIgmpPortEntry.setStatus(_A)
class _TpIgmpSnoopingPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIgmpSnoopingPortEnable_Type.__name__=_B
_TpIgmpSnoopingPortEnable_Object=MibTableColumn
tpIgmpSnoopingPortEnable=_TpIgmpSnoopingPortEnable_Object((1,3,6,1,4,1,11863,6,25,1,1,2,1,1,2),_TpIgmpSnoopingPortEnable_Type())
tpIgmpSnoopingPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpSnoopingPortEnable.setStatus(_A)
class _TpIgmpFastLeavePortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIgmpFastLeavePortEnable_Type.__name__=_B
_TpIgmpFastLeavePortEnable_Object=MibTableColumn
tpIgmpFastLeavePortEnable=_TpIgmpFastLeavePortEnable_Object((1,3,6,1,4,1,11863,6,25,1,1,2,1,1,3),_TpIgmpFastLeavePortEnable_Type())
tpIgmpFastLeavePortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpFastLeavePortEnable.setStatus(_A)
class _TpIgmpPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpIgmpPortLag_Type.__name__=_H
_TpIgmpPortLag_Object=MibTableColumn
tpIgmpPortLag=_TpIgmpPortLag_Object((1,3,6,1,4,1,11863,6,25,1,1,2,1,1,4),_TpIgmpPortLag_Type())
tpIgmpPortLag.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpPortLag.setStatus(_A)
_TpIgmpVlanConfig_ObjectIdentity=ObjectIdentity
tpIgmpVlanConfig=_TpIgmpVlanConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,1,3))
_TpIgmpVlanTable_Object=MibTable
tpIgmpVlanTable=_TpIgmpVlanTable_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1))
if mibBuilder.loadTexts:tpIgmpVlanTable.setStatus(_A)
_TpIgmpVlanEntry_Object=MibTableRow
tpIgmpVlanEntry=_TpIgmpVlanEntry_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1))
tpIgmpVlanEntry.setIndexNames((0,_I,_L))
if mibBuilder.loadTexts:tpIgmpVlanEntry.setStatus(_A)
class _TpIgmpVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_TpIgmpVlanId_Type.__name__=_B
_TpIgmpVlanId_Object=MibTableColumn
tpIgmpVlanId=_TpIgmpVlanId_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,1),_TpIgmpVlanId_Type())
tpIgmpVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpVlanId.setStatus(_A)
class _TpIgmpVlanEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIgmpVlanEnable_Type.__name__=_B
_TpIgmpVlanEnable_Object=MibTableColumn
tpIgmpVlanEnable=_TpIgmpVlanEnable_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,2),_TpIgmpVlanEnable_Type())
tpIgmpVlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpVlanEnable.setStatus(_A)
class _TpIgmpVlanFastLeave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIgmpVlanFastLeave_Type.__name__=_B
_TpIgmpVlanFastLeave_Object=MibTableColumn
tpIgmpVlanFastLeave=_TpIgmpVlanFastLeave_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,3),_TpIgmpVlanFastLeave_Type())
tpIgmpVlanFastLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpVlanFastLeave.setStatus(_A)
class _TpIgmpVlanReportSuppression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIgmpVlanReportSuppression_Type.__name__=_B
_TpIgmpVlanReportSuppression_Object=MibTableColumn
tpIgmpVlanReportSuppression=_TpIgmpVlanReportSuppression_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,4),_TpIgmpVlanReportSuppression_Type())
tpIgmpVlanReportSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpVlanReportSuppression.setStatus(_A)
class _TpIgmpRouterTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_TpIgmpRouterTime_Type.__name__=_B
_TpIgmpRouterTime_Object=MibTableColumn
tpIgmpRouterTime=_TpIgmpRouterTime_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,5),_TpIgmpRouterTime_Type())
tpIgmpRouterTime.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIgmpRouterTime.setStatus(_A)
class _TpIgmpMemberTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_TpIgmpMemberTime_Type.__name__=_B
_TpIgmpMemberTime_Object=MibTableColumn
tpIgmpMemberTime=_TpIgmpMemberTime_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,6),_TpIgmpMemberTime_Type())
tpIgmpMemberTime.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIgmpMemberTime.setStatus(_A)
class _TpIgmpLeaveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_TpIgmpLeaveTime_Type.__name__=_B
_TpIgmpLeaveTime_Object=MibTableColumn
tpIgmpLeaveTime=_TpIgmpLeaveTime_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,7),_TpIgmpLeaveTime_Type())
tpIgmpLeaveTime.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIgmpLeaveTime.setStatus(_A)
class _TpIgmpRouterPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpIgmpRouterPort_Type.__name__=_H
_TpIgmpRouterPort_Object=MibTableColumn
tpIgmpRouterPort=_TpIgmpRouterPort_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,8),_TpIgmpRouterPort_Type())
tpIgmpRouterPort.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIgmpRouterPort.setStatus(_A)
class _TpIgmpForbiddenRouterPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpIgmpForbiddenRouterPort_Type.__name__=_H
_TpIgmpForbiddenRouterPort_Object=MibTableColumn
tpIgmpForbiddenRouterPort=_TpIgmpForbiddenRouterPort_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,9),_TpIgmpForbiddenRouterPort_Type())
tpIgmpForbiddenRouterPort.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIgmpForbiddenRouterPort.setStatus(_A)
class _TpIgmpQueryEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIgmpQueryEnable_Type.__name__=_B
_TpIgmpQueryEnable_Object=MibTableColumn
tpIgmpQueryEnable=_TpIgmpQueryEnable_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,10),_TpIgmpQueryEnable_Type())
tpIgmpQueryEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpQueryEnable.setStatus(_A)
class _TpIgmpQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_TpIgmpQueryInterval_Type.__name__=_B
_TpIgmpQueryInterval_Object=MibTableColumn
tpIgmpQueryInterval=_TpIgmpQueryInterval_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,11),_TpIgmpQueryInterval_Type())
tpIgmpQueryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIgmpQueryInterval.setStatus(_A)
class _TpIgmpQueryMaxResponseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_TpIgmpQueryMaxResponseTime_Type.__name__=_B
_TpIgmpQueryMaxResponseTime_Object=MibTableColumn
tpIgmpQueryMaxResponseTime=_TpIgmpQueryMaxResponseTime_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,12),_TpIgmpQueryMaxResponseTime_Type())
tpIgmpQueryMaxResponseTime.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIgmpQueryMaxResponseTime.setStatus(_A)
_TpIgmpQueryGeneralSrcIp_Type=IpAddress
_TpIgmpQueryGeneralSrcIp_Object=MibTableColumn
tpIgmpQueryGeneralSrcIp=_TpIgmpQueryGeneralSrcIp_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,13),_TpIgmpQueryGeneralSrcIp_Type())
tpIgmpQueryGeneralSrcIp.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIgmpQueryGeneralSrcIp.setStatus(_A)
class _TpIgmpQueryLastMemberCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_TpIgmpQueryLastMemberCount_Type.__name__=_B
_TpIgmpQueryLastMemberCount_Object=MibTableColumn
tpIgmpQueryLastMemberCount=_TpIgmpQueryLastMemberCount_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,14),_TpIgmpQueryLastMemberCount_Type())
tpIgmpQueryLastMemberCount.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIgmpQueryLastMemberCount.setStatus(_A)
class _TpIgmpQueryLastMemberInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_TpIgmpQueryLastMemberInterval_Type.__name__=_B
_TpIgmpQueryLastMemberInterval_Object=MibTableColumn
tpIgmpQueryLastMemberInterval=_TpIgmpQueryLastMemberInterval_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,15),_TpIgmpQueryLastMemberInterval_Type())
tpIgmpQueryLastMemberInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIgmpQueryLastMemberInterval.setStatus(_A)
_TpIgmpVlanStatus_Type=TPRowStatus
_TpIgmpVlanStatus_Object=MibTableColumn
tpIgmpVlanStatus=_TpIgmpVlanStatus_Object((1,3,6,1,4,1,11863,6,25,1,1,3,1,1,16),_TpIgmpVlanStatus_Type())
tpIgmpVlanStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIgmpVlanStatus.setStatus(_A)
_TpIgmpFilter_ObjectIdentity=ObjectIdentity
tpIgmpFilter=_TpIgmpFilter_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,2))
_TpIgmpPortFilterConfig_ObjectIdentity=ObjectIdentity
tpIgmpPortFilterConfig=_TpIgmpPortFilterConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,2,1))
_TpIgmpFilterPortTable_Object=MibTable
tpIgmpFilterPortTable=_TpIgmpFilterPortTable_Object((1,3,6,1,4,1,11863,6,25,1,2,1,1))
if mibBuilder.loadTexts:tpIgmpFilterPortTable.setStatus(_A)
_TpIgmpFilterPortEntry_Object=MibTableRow
tpIgmpFilterPortEntry=_TpIgmpFilterPortEntry_Object((1,3,6,1,4,1,11863,6,25,1,2,1,1,1))
tpIgmpFilterPortEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:tpIgmpFilterPortEntry.setStatus(_A)
class _TpIgmpFilterMaxGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_TpIgmpFilterMaxGroup_Type.__name__=_B
_TpIgmpFilterMaxGroup_Object=MibTableColumn
tpIgmpFilterMaxGroup=_TpIgmpFilterMaxGroup_Object((1,3,6,1,4,1,11863,6,25,1,2,1,1,1,2),_TpIgmpFilterMaxGroup_Type())
tpIgmpFilterMaxGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpFilterMaxGroup.setStatus(_A)
class _TpIgmpFilterMaxGroupAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('drop',0),('replace',1)))
_TpIgmpFilterMaxGroupAction_Type.__name__=_B
_TpIgmpFilterMaxGroupAction_Object=MibTableColumn
tpIgmpFilterMaxGroupAction=_TpIgmpFilterMaxGroupAction_Object((1,3,6,1,4,1,11863,6,25,1,2,1,1,1,3),_TpIgmpFilterMaxGroupAction_Type())
tpIgmpFilterMaxGroupAction.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpFilterMaxGroupAction.setStatus(_A)
class _TpIgmpFilterBindAddrId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_TpIgmpFilterBindAddrId_Type.__name__=_H
_TpIgmpFilterBindAddrId_Object=MibTableColumn
tpIgmpFilterBindAddrId=_TpIgmpFilterBindAddrId_Object((1,3,6,1,4,1,11863,6,25,1,2,1,1,1,4),_TpIgmpFilterBindAddrId_Type())
tpIgmpFilterBindAddrId.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpFilterBindAddrId.setStatus(_A)
class _TpIgmpFilterPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpIgmpFilterPortLag_Type.__name__=_H
_TpIgmpFilterPortLag_Object=MibTableColumn
tpIgmpFilterPortLag=_TpIgmpFilterPortLag_Object((1,3,6,1,4,1,11863,6,25,1,2,1,1,1,5),_TpIgmpFilterPortLag_Type())
tpIgmpFilterPortLag.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpFilterPortLag.setStatus(_A)
_TpIgmpAuth_ObjectIdentity=ObjectIdentity
tpIgmpAuth=_TpIgmpAuth_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,3))
_TpIgmpPortAuthConfig_ObjectIdentity=ObjectIdentity
tpIgmpPortAuthConfig=_TpIgmpPortAuthConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,3,1))
_TpIgmpAuthPortTable_Object=MibTable
tpIgmpAuthPortTable=_TpIgmpAuthPortTable_Object((1,3,6,1,4,1,11863,6,25,1,3,1,1))
if mibBuilder.loadTexts:tpIgmpAuthPortTable.setStatus(_A)
_TpIgmpAuthPortEntry_Object=MibTableRow
tpIgmpAuthPortEntry=_TpIgmpAuthPortEntry_Object((1,3,6,1,4,1,11863,6,25,1,3,1,1,1))
tpIgmpAuthPortEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:tpIgmpAuthPortEntry.setStatus(_A)
class _TpIgmpAuthEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIgmpAuthEnable_Type.__name__=_B
_TpIgmpAuthEnable_Object=MibTableColumn
tpIgmpAuthEnable=_TpIgmpAuthEnable_Object((1,3,6,1,4,1,11863,6,25,1,3,1,1,1,2),_TpIgmpAuthEnable_Type())
tpIgmpAuthEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpAuthEnable.setStatus(_A)
class _TpIgmpAuthPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpIgmpAuthPortLag_Type.__name__=_H
_TpIgmpAuthPortLag_Object=MibTableColumn
tpIgmpAuthPortLag=_TpIgmpAuthPortLag_Object((1,3,6,1,4,1,11863,6,25,1,3,1,1,1,3),_TpIgmpAuthPortLag_Type())
tpIgmpAuthPortLag.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpAuthPortLag.setStatus(_A)
_TpIgmpGlobalAuthAccountConfig_ObjectIdentity=ObjectIdentity
tpIgmpGlobalAuthAccountConfig=_TpIgmpGlobalAuthAccountConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,3,2))
class _TpIgmpGlobalAuthAccountConfigEable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIgmpGlobalAuthAccountConfigEable_Type.__name__=_B
_TpIgmpGlobalAuthAccountConfigEable_Object=MibScalar
tpIgmpGlobalAuthAccountConfigEable=_TpIgmpGlobalAuthAccountConfigEable_Object((1,3,6,1,4,1,11863,6,25,1,3,2,1),_TpIgmpGlobalAuthAccountConfigEable_Type())
tpIgmpGlobalAuthAccountConfigEable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIgmpGlobalAuthAccountConfigEable.setStatus(_A)
_TpIgmpPacketStatistic_ObjectIdentity=ObjectIdentity
tpIgmpPacketStatistic=_TpIgmpPacketStatistic_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,4))
_TpIgmpPktStat_ObjectIdentity=ObjectIdentity
tpIgmpPktStat=_TpIgmpPktStat_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,4,1))
_TpIgmpPktStatTable_Object=MibTable
tpIgmpPktStatTable=_TpIgmpPktStatTable_Object((1,3,6,1,4,1,11863,6,25,1,4,1,1))
if mibBuilder.loadTexts:tpIgmpPktStatTable.setStatus(_A)
_TpIgmpPktStatEntry_Object=MibTableRow
tpIgmpPktStatEntry=_TpIgmpPktStatEntry_Object((1,3,6,1,4,1,11863,6,25,1,4,1,1,1))
tpIgmpPktStatEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:tpIgmpPktStatEntry.setStatus(_A)
_TpIgmpQueryPktStat_Type=Integer32
_TpIgmpQueryPktStat_Object=MibTableColumn
tpIgmpQueryPktStat=_TpIgmpQueryPktStat_Object((1,3,6,1,4,1,11863,6,25,1,4,1,1,1,2),_TpIgmpQueryPktStat_Type())
tpIgmpQueryPktStat.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpQueryPktStat.setStatus(_A)
_TpIgmpReportV1PktStat_Type=Integer32
_TpIgmpReportV1PktStat_Object=MibTableColumn
tpIgmpReportV1PktStat=_TpIgmpReportV1PktStat_Object((1,3,6,1,4,1,11863,6,25,1,4,1,1,1,3),_TpIgmpReportV1PktStat_Type())
tpIgmpReportV1PktStat.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpReportV1PktStat.setStatus(_A)
_TpIgmpReportV2PktStat_Type=Integer32
_TpIgmpReportV2PktStat_Object=MibTableColumn
tpIgmpReportV2PktStat=_TpIgmpReportV2PktStat_Object((1,3,6,1,4,1,11863,6,25,1,4,1,1,1,4),_TpIgmpReportV2PktStat_Type())
tpIgmpReportV2PktStat.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpReportV2PktStat.setStatus(_A)
_TpIgmpReportV3PktStat_Type=Integer32
_TpIgmpReportV3PktStat_Object=MibTableColumn
tpIgmpReportV3PktStat=_TpIgmpReportV3PktStat_Object((1,3,6,1,4,1,11863,6,25,1,4,1,1,1,5),_TpIgmpReportV3PktStat_Type())
tpIgmpReportV3PktStat.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpReportV3PktStat.setStatus(_A)
_TpIgmpLeavePktStat_Type=Integer32
_TpIgmpLeavePktStat_Object=MibTableColumn
tpIgmpLeavePktStat=_TpIgmpLeavePktStat_Object((1,3,6,1,4,1,11863,6,25,1,4,1,1,1,6),_TpIgmpLeavePktStat_Type())
tpIgmpLeavePktStat.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpLeavePktStat.setStatus(_A)
_TpIgmpErrorPktStat_Type=Integer32
_TpIgmpErrorPktStat_Object=MibTableColumn
tpIgmpErrorPktStat=_TpIgmpErrorPktStat_Object((1,3,6,1,4,1,11863,6,25,1,4,1,1,1,7),_TpIgmpErrorPktStat_Type())
tpIgmpErrorPktStat.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpErrorPktStat.setStatus(_A)
class _TpIpIgmpPktStatClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('commit',1))
_TpIpIgmpPktStatClear_Type.__name__=_B
_TpIpIgmpPktStatClear_Object=MibScalar
tpIpIgmpPktStatClear=_TpIpIgmpPktStatClear_Object((1,3,6,1,4,1,11863,6,25,1,4,1,2),_TpIpIgmpPktStatClear_Type())
tpIpIgmpPktStatClear.setMaxAccess(_C)
if mibBuilder.loadTexts:tpIpIgmpPktStatClear.setStatus(_A)
_TpIgmpMultigroup_ObjectIdentity=ObjectIdentity
tpIgmpMultigroup=_TpIgmpMultigroup_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,5))
_TpIgmpMulticastGroups_ObjectIdentity=ObjectIdentity
tpIgmpMulticastGroups=_TpIgmpMulticastGroups_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,5,1))
_TpIgmpMulticastGroupTable_Object=MibTable
tpIgmpMulticastGroupTable=_TpIgmpMulticastGroupTable_Object((1,3,6,1,4,1,11863,6,25,1,5,1,1))
if mibBuilder.loadTexts:tpIgmpMulticastGroupTable.setStatus(_A)
_TpIgmpMulticastGroupEntry_Object=MibTableRow
tpIgmpMulticastGroupEntry=_TpIgmpMulticastGroupEntry_Object((1,3,6,1,4,1,11863,6,25,1,5,1,1,1))
tpIgmpMulticastGroupEntry.setIndexNames((0,_I,_M),(0,_I,_N))
if mibBuilder.loadTexts:tpIgmpMulticastGroupEntry.setStatus(_A)
_TpIgmpMulticastIP_Type=IpAddress
_TpIgmpMulticastIP_Object=MibTableColumn
tpIgmpMulticastIP=_TpIgmpMulticastIP_Object((1,3,6,1,4,1,11863,6,25,1,5,1,1,1,1),_TpIgmpMulticastIP_Type())
tpIgmpMulticastIP.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpMulticastIP.setStatus(_A)
_TpIgmpVlanID_Type=Integer32
_TpIgmpVlanID_Object=MibTableColumn
tpIgmpVlanID=_TpIgmpVlanID_Object((1,3,6,1,4,1,11863,6,25,1,5,1,1,1,2),_TpIgmpVlanID_Type())
tpIgmpVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpVlanID.setStatus(_A)
class _TpIgmpForwardPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_TpIgmpForwardPorts_Type.__name__=_H
_TpIgmpForwardPorts_Object=MibTableColumn
tpIgmpForwardPorts=_TpIgmpForwardPorts_Object((1,3,6,1,4,1,11863,6,25,1,5,1,1,1,3),_TpIgmpForwardPorts_Type())
tpIgmpForwardPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpForwardPorts.setStatus(_A)
class _TpIgmpGrouptype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('static',0),('dynamic',1)))
_TpIgmpGrouptype_Type.__name__=_B
_TpIgmpGrouptype_Object=MibTableColumn
tpIgmpGrouptype=_TpIgmpGrouptype_Object((1,3,6,1,4,1,11863,6,25,1,5,1,1,1,4),_TpIgmpGrouptype_Type())
tpIgmpGrouptype.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpGrouptype.setStatus(_A)
_TpIgmpStaticMultigroup_ObjectIdentity=ObjectIdentity
tpIgmpStaticMultigroup=_TpIgmpStaticMultigroup_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,6))
_TpIgmpMulticastStaticGroups_ObjectIdentity=ObjectIdentity
tpIgmpMulticastStaticGroups=_TpIgmpMulticastStaticGroups_ObjectIdentity((1,3,6,1,4,1,11863,6,25,1,6,1))
_TpIgmpMulticastStaticGroupTable_Object=MibTable
tpIgmpMulticastStaticGroupTable=_TpIgmpMulticastStaticGroupTable_Object((1,3,6,1,4,1,11863,6,25,1,6,1,1))
if mibBuilder.loadTexts:tpIgmpMulticastStaticGroupTable.setStatus(_A)
_TpIgmpMulticastStaticGroupEntry_Object=MibTableRow
tpIgmpMulticastStaticGroupEntry=_TpIgmpMulticastStaticGroupEntry_Object((1,3,6,1,4,1,11863,6,25,1,6,1,1,1))
tpIgmpMulticastStaticGroupEntry.setIndexNames((0,_I,_O),(0,_I,_P))
if mibBuilder.loadTexts:tpIgmpMulticastStaticGroupEntry.setStatus(_A)
_TpIgmpStaticMulticastIP_Type=IpAddress
_TpIgmpStaticMulticastIP_Object=MibTableColumn
tpIgmpStaticMulticastIP=_TpIgmpStaticMulticastIP_Object((1,3,6,1,4,1,11863,6,25,1,6,1,1,1,1),_TpIgmpStaticMulticastIP_Type())
tpIgmpStaticMulticastIP.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpStaticMulticastIP.setStatus(_A)
_TpIgmpStaticVlanID_Type=Integer32
_TpIgmpStaticVlanID_Object=MibTableColumn
tpIgmpStaticVlanID=_TpIgmpStaticVlanID_Object((1,3,6,1,4,1,11863,6,25,1,6,1,1,1,2),_TpIgmpStaticVlanID_Type())
tpIgmpStaticVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIgmpStaticVlanID.setStatus(_A)
class _TpIgmpStaticForwardPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_TpIgmpStaticForwardPorts_Type.__name__=_H
_TpIgmpStaticForwardPorts_Object=MibTableColumn
tpIgmpStaticForwardPorts=_TpIgmpStaticForwardPorts_Object((1,3,6,1,4,1,11863,6,25,1,6,1,1,1,3),_TpIgmpStaticForwardPorts_Type())
tpIgmpStaticForwardPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIgmpStaticForwardPorts.setStatus(_A)
_TpIgmpStaticGroupStatus_Type=TPRowStatus
_TpIgmpStaticGroupStatus_Object=MibTableColumn
tpIgmpStaticGroupStatus=_TpIgmpStaticGroupStatus_Object((1,3,6,1,4,1,11863,6,25,1,6,1,1,1,4),_TpIgmpStaticGroupStatus_Type())
tpIgmpStaticGroupStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIgmpStaticGroupStatus.setStatus(_A)
_TplinkIgmpSnoopingNotifications_ObjectIdentity=ObjectIdentity
tplinkIgmpSnoopingNotifications=_TplinkIgmpSnoopingNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,25,2))
mibBuilder.exportSymbols(_I,**{'tplinkIgmpSnoopingMIB':tplinkIgmpSnoopingMIB,'tplinkIgmpSnoopingMIBObjects':tplinkIgmpSnoopingMIBObjects,'tpIgmpSnooping':tpIgmpSnooping,'tpIgmpSnoopingGlobalConfig':tpIgmpSnoopingGlobalConfig,'tpIgmpSnoopingEnable':tpIgmpSnoopingEnable,'tpIgmpSnoopingVersion':tpIgmpSnoopingVersion,'tpUnknownMulticastPacket':tpUnknownMulticastPacket,'tpIgmpHeaderValidation':tpIgmpHeaderValidation,'tpIgmpPortConfig':tpIgmpPortConfig,'tpIgmpPortTable':tpIgmpPortTable,'tpIgmpPortEntry':tpIgmpPortEntry,'tpIgmpSnoopingPortEnable':tpIgmpSnoopingPortEnable,'tpIgmpFastLeavePortEnable':tpIgmpFastLeavePortEnable,'tpIgmpPortLag':tpIgmpPortLag,'tpIgmpVlanConfig':tpIgmpVlanConfig,'tpIgmpVlanTable':tpIgmpVlanTable,'tpIgmpVlanEntry':tpIgmpVlanEntry,_L:tpIgmpVlanId,'tpIgmpVlanEnable':tpIgmpVlanEnable,'tpIgmpVlanFastLeave':tpIgmpVlanFastLeave,'tpIgmpVlanReportSuppression':tpIgmpVlanReportSuppression,'tpIgmpRouterTime':tpIgmpRouterTime,'tpIgmpMemberTime':tpIgmpMemberTime,'tpIgmpLeaveTime':tpIgmpLeaveTime,'tpIgmpRouterPort':tpIgmpRouterPort,'tpIgmpForbiddenRouterPort':tpIgmpForbiddenRouterPort,'tpIgmpQueryEnable':tpIgmpQueryEnable,'tpIgmpQueryInterval':tpIgmpQueryInterval,'tpIgmpQueryMaxResponseTime':tpIgmpQueryMaxResponseTime,'tpIgmpQueryGeneralSrcIp':tpIgmpQueryGeneralSrcIp,'tpIgmpQueryLastMemberCount':tpIgmpQueryLastMemberCount,'tpIgmpQueryLastMemberInterval':tpIgmpQueryLastMemberInterval,'tpIgmpVlanStatus':tpIgmpVlanStatus,'tpIgmpFilter':tpIgmpFilter,'tpIgmpPortFilterConfig':tpIgmpPortFilterConfig,'tpIgmpFilterPortTable':tpIgmpFilterPortTable,'tpIgmpFilterPortEntry':tpIgmpFilterPortEntry,'tpIgmpFilterMaxGroup':tpIgmpFilterMaxGroup,'tpIgmpFilterMaxGroupAction':tpIgmpFilterMaxGroupAction,'tpIgmpFilterBindAddrId':tpIgmpFilterBindAddrId,'tpIgmpFilterPortLag':tpIgmpFilterPortLag,'tpIgmpAuth':tpIgmpAuth,'tpIgmpPortAuthConfig':tpIgmpPortAuthConfig,'tpIgmpAuthPortTable':tpIgmpAuthPortTable,'tpIgmpAuthPortEntry':tpIgmpAuthPortEntry,'tpIgmpAuthEnable':tpIgmpAuthEnable,'tpIgmpAuthPortLag':tpIgmpAuthPortLag,'tpIgmpGlobalAuthAccountConfig':tpIgmpGlobalAuthAccountConfig,'tpIgmpGlobalAuthAccountConfigEable':tpIgmpGlobalAuthAccountConfigEable,'tpIgmpPacketStatistic':tpIgmpPacketStatistic,'tpIgmpPktStat':tpIgmpPktStat,'tpIgmpPktStatTable':tpIgmpPktStatTable,'tpIgmpPktStatEntry':tpIgmpPktStatEntry,'tpIgmpQueryPktStat':tpIgmpQueryPktStat,'tpIgmpReportV1PktStat':tpIgmpReportV1PktStat,'tpIgmpReportV2PktStat':tpIgmpReportV2PktStat,'tpIgmpReportV3PktStat':tpIgmpReportV3PktStat,'tpIgmpLeavePktStat':tpIgmpLeavePktStat,'tpIgmpErrorPktStat':tpIgmpErrorPktStat,'tpIpIgmpPktStatClear':tpIpIgmpPktStatClear,'tpIgmpMultigroup':tpIgmpMultigroup,'tpIgmpMulticastGroups':tpIgmpMulticastGroups,'tpIgmpMulticastGroupTable':tpIgmpMulticastGroupTable,'tpIgmpMulticastGroupEntry':tpIgmpMulticastGroupEntry,_M:tpIgmpMulticastIP,_N:tpIgmpVlanID,'tpIgmpForwardPorts':tpIgmpForwardPorts,'tpIgmpGrouptype':tpIgmpGrouptype,'tpIgmpStaticMultigroup':tpIgmpStaticMultigroup,'tpIgmpMulticastStaticGroups':tpIgmpMulticastStaticGroups,'tpIgmpMulticastStaticGroupTable':tpIgmpMulticastStaticGroupTable,'tpIgmpMulticastStaticGroupEntry':tpIgmpMulticastStaticGroupEntry,_O:tpIgmpStaticMulticastIP,_P:tpIgmpStaticVlanID,'tpIgmpStaticForwardPorts':tpIgmpStaticForwardPorts,'tpIgmpStaticGroupStatus':tpIgmpStaticGroupStatus,'tplinkIgmpSnoopingNotifications':tplinkIgmpSnoopingNotifications})