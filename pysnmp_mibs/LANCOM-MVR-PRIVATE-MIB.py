_N='mvrPortMembershipPortIfIndex'
_M='mvrPortMembershipGroupIPAddress'
_L='mvrGroupIPAddress'
_K='TimeInterval'
_J='VlanIndex'
_I='ifIndex'
_H='IF-MIB'
_G='LANCOM-MVR-PRIVATE-MIB'
_F='TruthValue'
_E='read-create'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_H,'InterfaceIndex',_I)
fastPath,=mibBuilder.importSymbols('LANCOM-REF-MIB','fastPath')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_K,_F)
fastpathMvr=ModuleIdentity((1,3,6,1,4,1,2356,16,1,50))
if mibBuilder.loadTexts:fastpathMvr.setRevisions(('2011-01-26 00:00','2009-10-21 00:00'))
_MvrGlobalConfig_ObjectIdentity=ObjectIdentity
mvrGlobalConfig=_MvrGlobalConfig_ObjectIdentity((1,3,6,1,4,1,2356,16,1,50,1))
class _MvrAdminMode_Type(TruthValue):defaultValue=2
_MvrAdminMode_Type.__name__=_F
_MvrAdminMode_Object=MibScalar
mvrAdminMode=_MvrAdminMode_Object((1,3,6,1,4,1,2356,16,1,50,1,1),_MvrAdminMode_Type())
mvrAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mvrAdminMode.setStatus(_A)
class _MvrModeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('compatible',1),('dynamic',2)))
_MvrModeType_Type.__name__=_D
_MvrModeType_Object=MibScalar
mvrModeType=_MvrModeType_Object((1,3,6,1,4,1,2356,16,1,50,1,2),_MvrModeType_Type())
mvrModeType.setMaxAccess(_C)
if mibBuilder.loadTexts:mvrModeType.setStatus(_A)
class _MvrMulticastVlanId_Type(VlanIndex):defaultValue=1
_MvrMulticastVlanId_Type.__name__=_J
_MvrMulticastVlanId_Object=MibScalar
mvrMulticastVlanId=_MvrMulticastVlanId_Object((1,3,6,1,4,1,2356,16,1,50,1,3),_MvrMulticastVlanId_Type())
mvrMulticastVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:mvrMulticastVlanId.setStatus(_A)
_MvrMaxMulticastGroupsCount_Type=Integer32
_MvrMaxMulticastGroupsCount_Object=MibScalar
mvrMaxMulticastGroupsCount=_MvrMaxMulticastGroupsCount_Object((1,3,6,1,4,1,2356,16,1,50,1,4),_MvrMaxMulticastGroupsCount_Type())
mvrMaxMulticastGroupsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrMaxMulticastGroupsCount.setStatus(_A)
_MvrCurrentMulticastGroupsCount_Type=Integer32
_MvrCurrentMulticastGroupsCount_Object=MibScalar
mvrCurrentMulticastGroupsCount=_MvrCurrentMulticastGroupsCount_Object((1,3,6,1,4,1,2356,16,1,50,1,5),_MvrCurrentMulticastGroupsCount_Type())
mvrCurrentMulticastGroupsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrCurrentMulticastGroupsCount.setStatus(_A)
class _MvrQueryTime_Type(TimeInterval):defaultValue=5;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_MvrQueryTime_Type.__name__=_K
_MvrQueryTime_Object=MibScalar
mvrQueryTime=_MvrQueryTime_Object((1,3,6,1,4,1,2356,16,1,50,1,6),_MvrQueryTime_Type())
mvrQueryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mvrQueryTime.setStatus(_A)
_MvrPortTable_Object=MibTable
mvrPortTable=_MvrPortTable_Object((1,3,6,1,4,1,2356,16,1,50,2))
if mibBuilder.loadTexts:mvrPortTable.setStatus(_A)
_MvrPortEntry_Object=MibTableRow
mvrPortEntry=_MvrPortEntry_Object((1,3,6,1,4,1,2356,16,1,50,2,1))
mvrPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:mvrPortEntry.setStatus(_A)
class _MvrPortMvrEnabled_Type(TruthValue):defaultValue=2
_MvrPortMvrEnabled_Type.__name__=_F
_MvrPortMvrEnabled_Object=MibTableColumn
mvrPortMvrEnabled=_MvrPortMvrEnabled_Object((1,3,6,1,4,1,2356,16,1,50,2,1,1),_MvrPortMvrEnabled_Type())
mvrPortMvrEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:mvrPortMvrEnabled.setStatus(_A)
class _MvrPortType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('source',1),('receiver',2),('none',3)))
_MvrPortType_Type.__name__=_D
_MvrPortType_Object=MibTableColumn
mvrPortType=_MvrPortType_Object((1,3,6,1,4,1,2356,16,1,50,2,1,2),_MvrPortType_Type())
mvrPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:mvrPortType.setStatus(_A)
class _MvrPortImmediateLeaveMode_Type(TruthValue):defaultValue=2
_MvrPortImmediateLeaveMode_Type.__name__=_F
_MvrPortImmediateLeaveMode_Object=MibTableColumn
mvrPortImmediateLeaveMode=_MvrPortImmediateLeaveMode_Object((1,3,6,1,4,1,2356,16,1,50,2,1,3),_MvrPortImmediateLeaveMode_Type())
mvrPortImmediateLeaveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mvrPortImmediateLeaveMode.setStatus(_A)
class _MvrPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('activeInVlan',1),('activeNotInVlan',2),('inactiveInVlan',3),('inactiveNotInVlan',4)))
_MvrPortStatus_Type.__name__=_D
_MvrPortStatus_Object=MibTableColumn
mvrPortStatus=_MvrPortStatus_Object((1,3,6,1,4,1,2356,16,1,50,2,1,4),_MvrPortStatus_Type())
mvrPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrPortStatus.setStatus(_A)
_MvrGroupsTable_Object=MibTable
mvrGroupsTable=_MvrGroupsTable_Object((1,3,6,1,4,1,2356,16,1,50,3))
if mibBuilder.loadTexts:mvrGroupsTable.setStatus(_A)
_MvrGroupEntry_Object=MibTableRow
mvrGroupEntry=_MvrGroupEntry_Object((1,3,6,1,4,1,2356,16,1,50,3,1))
mvrGroupEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:mvrGroupEntry.setStatus(_A)
_MvrGroupIPAddress_Type=IpAddress
_MvrGroupIPAddress_Object=MibTableColumn
mvrGroupIPAddress=_MvrGroupIPAddress_Object((1,3,6,1,4,1,2356,16,1,50,3,1,1),_MvrGroupIPAddress_Type())
mvrGroupIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:mvrGroupIPAddress.setStatus(_A)
class _MvrGroupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_MvrGroupStatus_Type.__name__=_D
_MvrGroupStatus_Object=MibTableColumn
mvrGroupStatus=_MvrGroupStatus_Object((1,3,6,1,4,1,2356,16,1,50,3,1,2),_MvrGroupStatus_Type())
mvrGroupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrGroupStatus.setStatus(_A)
_MvrGroupRowStatus_Type=RowStatus
_MvrGroupRowStatus_Object=MibTableColumn
mvrGroupRowStatus=_MvrGroupRowStatus_Object((1,3,6,1,4,1,2356,16,1,50,3,1,3),_MvrGroupRowStatus_Type())
mvrGroupRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mvrGroupRowStatus.setStatus(_A)
_MvrPortMembershipTable_Object=MibTable
mvrPortMembershipTable=_MvrPortMembershipTable_Object((1,3,6,1,4,1,2356,16,1,50,4))
if mibBuilder.loadTexts:mvrPortMembershipTable.setStatus(_A)
_MvrPortMembershipEntry_Object=MibTableRow
mvrPortMembershipEntry=_MvrPortMembershipEntry_Object((1,3,6,1,4,1,2356,16,1,50,4,1))
mvrPortMembershipEntry.setIndexNames((0,_G,_M),(0,_G,_N))
if mibBuilder.loadTexts:mvrPortMembershipEntry.setStatus(_A)
_MvrPortMembershipGroupIPAddress_Type=IpAddress
_MvrPortMembershipGroupIPAddress_Object=MibTableColumn
mvrPortMembershipGroupIPAddress=_MvrPortMembershipGroupIPAddress_Object((1,3,6,1,4,1,2356,16,1,50,4,1,1),_MvrPortMembershipGroupIPAddress_Type())
mvrPortMembershipGroupIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:mvrPortMembershipGroupIPAddress.setStatus(_A)
_MvrPortMembershipPortIfIndex_Type=InterfaceIndex
_MvrPortMembershipPortIfIndex_Object=MibTableColumn
mvrPortMembershipPortIfIndex=_MvrPortMembershipPortIfIndex_Object((1,3,6,1,4,1,2356,16,1,50,4,1,2),_MvrPortMembershipPortIfIndex_Type())
mvrPortMembershipPortIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mvrPortMembershipPortIfIndex.setStatus(_A)
_MvrPortMembershipRowStatus_Type=RowStatus
_MvrPortMembershipRowStatus_Object=MibTableColumn
mvrPortMembershipRowStatus=_MvrPortMembershipRowStatus_Object((1,3,6,1,4,1,2356,16,1,50,4,1,3),_MvrPortMembershipRowStatus_Type())
mvrPortMembershipRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mvrPortMembershipRowStatus.setStatus(_A)
_MvrStatistics_ObjectIdentity=ObjectIdentity
mvrStatistics=_MvrStatistics_ObjectIdentity((1,3,6,1,4,1,2356,16,1,50,5))
_MvrIGMPQueryReceived_Type=Unsigned32
_MvrIGMPQueryReceived_Object=MibScalar
mvrIGMPQueryReceived=_MvrIGMPQueryReceived_Object((1,3,6,1,4,1,2356,16,1,50,5,1),_MvrIGMPQueryReceived_Type())
mvrIGMPQueryReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrIGMPQueryReceived.setStatus(_A)
_MvrIGMPReportV1Received_Type=Unsigned32
_MvrIGMPReportV1Received_Object=MibScalar
mvrIGMPReportV1Received=_MvrIGMPReportV1Received_Object((1,3,6,1,4,1,2356,16,1,50,5,2),_MvrIGMPReportV1Received_Type())
mvrIGMPReportV1Received.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrIGMPReportV1Received.setStatus(_A)
_MvrIGMPReportV2Received_Type=Unsigned32
_MvrIGMPReportV2Received_Object=MibScalar
mvrIGMPReportV2Received=_MvrIGMPReportV2Received_Object((1,3,6,1,4,1,2356,16,1,50,5,3),_MvrIGMPReportV2Received_Type())
mvrIGMPReportV2Received.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrIGMPReportV2Received.setStatus(_A)
_MvrIGMPLeaveReceived_Type=Unsigned32
_MvrIGMPLeaveReceived_Object=MibScalar
mvrIGMPLeaveReceived=_MvrIGMPLeaveReceived_Object((1,3,6,1,4,1,2356,16,1,50,5,4),_MvrIGMPLeaveReceived_Type())
mvrIGMPLeaveReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrIGMPLeaveReceived.setStatus(_A)
_MvrIGMPQueryTransmitted_Type=Unsigned32
_MvrIGMPQueryTransmitted_Object=MibScalar
mvrIGMPQueryTransmitted=_MvrIGMPQueryTransmitted_Object((1,3,6,1,4,1,2356,16,1,50,5,5),_MvrIGMPQueryTransmitted_Type())
mvrIGMPQueryTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrIGMPQueryTransmitted.setStatus(_A)
_MvrIGMPReportV1Transmitted_Type=Unsigned32
_MvrIGMPReportV1Transmitted_Object=MibScalar
mvrIGMPReportV1Transmitted=_MvrIGMPReportV1Transmitted_Object((1,3,6,1,4,1,2356,16,1,50,5,6),_MvrIGMPReportV1Transmitted_Type())
mvrIGMPReportV1Transmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrIGMPReportV1Transmitted.setStatus(_A)
_MvrIGMPReportV2Transmitted_Type=Unsigned32
_MvrIGMPReportV2Transmitted_Object=MibScalar
mvrIGMPReportV2Transmitted=_MvrIGMPReportV2Transmitted_Object((1,3,6,1,4,1,2356,16,1,50,5,7),_MvrIGMPReportV2Transmitted_Type())
mvrIGMPReportV2Transmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrIGMPReportV2Transmitted.setStatus(_A)
_MvrIGMPLeaveTransmitted_Type=Unsigned32
_MvrIGMPLeaveTransmitted_Object=MibScalar
mvrIGMPLeaveTransmitted=_MvrIGMPLeaveTransmitted_Object((1,3,6,1,4,1,2356,16,1,50,5,8),_MvrIGMPLeaveTransmitted_Type())
mvrIGMPLeaveTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrIGMPLeaveTransmitted.setStatus(_A)
_MvrIGMPPacketReceiveFailures_Type=Unsigned32
_MvrIGMPPacketReceiveFailures_Object=MibScalar
mvrIGMPPacketReceiveFailures=_MvrIGMPPacketReceiveFailures_Object((1,3,6,1,4,1,2356,16,1,50,5,9),_MvrIGMPPacketReceiveFailures_Type())
mvrIGMPPacketReceiveFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrIGMPPacketReceiveFailures.setStatus(_A)
_MvrIGMPPacketTransmitFailures_Type=Unsigned32
_MvrIGMPPacketTransmitFailures_Object=MibScalar
mvrIGMPPacketTransmitFailures=_MvrIGMPPacketTransmitFailures_Object((1,3,6,1,4,1,2356,16,1,50,5,10),_MvrIGMPPacketTransmitFailures_Type())
mvrIGMPPacketTransmitFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:mvrIGMPPacketTransmitFailures.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'fastpathMvr':fastpathMvr,'mvrGlobalConfig':mvrGlobalConfig,'mvrAdminMode':mvrAdminMode,'mvrModeType':mvrModeType,'mvrMulticastVlanId':mvrMulticastVlanId,'mvrMaxMulticastGroupsCount':mvrMaxMulticastGroupsCount,'mvrCurrentMulticastGroupsCount':mvrCurrentMulticastGroupsCount,'mvrQueryTime':mvrQueryTime,'mvrPortTable':mvrPortTable,'mvrPortEntry':mvrPortEntry,'mvrPortMvrEnabled':mvrPortMvrEnabled,'mvrPortType':mvrPortType,'mvrPortImmediateLeaveMode':mvrPortImmediateLeaveMode,'mvrPortStatus':mvrPortStatus,'mvrGroupsTable':mvrGroupsTable,'mvrGroupEntry':mvrGroupEntry,_L:mvrGroupIPAddress,'mvrGroupStatus':mvrGroupStatus,'mvrGroupRowStatus':mvrGroupRowStatus,'mvrPortMembershipTable':mvrPortMembershipTable,'mvrPortMembershipEntry':mvrPortMembershipEntry,_M:mvrPortMembershipGroupIPAddress,_N:mvrPortMembershipPortIfIndex,'mvrPortMembershipRowStatus':mvrPortMembershipRowStatus,'mvrStatistics':mvrStatistics,'mvrIGMPQueryReceived':mvrIGMPQueryReceived,'mvrIGMPReportV1Received':mvrIGMPReportV1Received,'mvrIGMPReportV2Received':mvrIGMPReportV2Received,'mvrIGMPLeaveReceived':mvrIGMPLeaveReceived,'mvrIGMPQueryTransmitted':mvrIGMPQueryTransmitted,'mvrIGMPReportV1Transmitted':mvrIGMPReportV1Transmitted,'mvrIGMPReportV2Transmitted':mvrIGMPReportV2Transmitted,'mvrIGMPLeaveTransmitted':mvrIGMPLeaveTransmitted,'mvrIGMPPacketReceiveFailures':mvrIGMPPacketReceiveFailures,'mvrIGMPPacketTransmitFailures':mvrIGMPPacketTransmitFailures})