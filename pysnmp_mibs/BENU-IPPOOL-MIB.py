_X='bIPv6PoolUsedPrefixHighThreshold'
_W='bIPv6PoolUsedPrefixLowThreshold'
_V='bIPPoolUsedAddrHighThreshold'
_U='bIPPoolUsedAddrLowThreshold'
_T='bIPv6PoolClientIndex'
_S='bIPv6PoolGlobalStatsInterval'
_R='bIPv6PoolGroupIndex'
_Q='bIPv6PoolGroupStatsInterval'
_P='bIPv6PoolIndex'
_O='bIPv6PoolStatsInterval'
_N='bIPPoolClientIndex'
_M='bIPPoolGlobalStatsInterval'
_L='bIPPoolGroupIndex'
_K='bIPPoolGroupStatsInterval'
_J='bIPPoolIndex'
_I='bIPPoolStatsInterval'
_H='bIPv6PoolTotalPrefixes'
_G='bIPv6PoolName'
_F='bIPPoolTotalAddresses'
_E='bIPPoolName'
_D='not-accessible'
_C='BENU-IPPOOL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
benuWAG,=mibBuilder.importSymbols('BENU-WAG-MIB','benuWAG')
InetAddress,InetAddressIPv4,InetAddressIPv6,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv4','InetAddressIPv6','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
benuIPPoolMIB=ModuleIdentity((1,3,6,1,4,1,39406,2,1,5))
if mibBuilder.loadTexts:benuIPPoolMIB.setRevisions(('2015-08-11 00:00','2015-01-05 00:00','2013-10-21 00:00'))
_BIPPoolNotifications_ObjectIdentity=ObjectIdentity
bIPPoolNotifications=_BIPPoolNotifications_ObjectIdentity((1,3,6,1,4,1,39406,2,1,5,0))
if mibBuilder.loadTexts:bIPPoolNotifications.setStatus(_A)
_BIPv4PoolMIBObjects_ObjectIdentity=ObjectIdentity
bIPv4PoolMIBObjects=_BIPv4PoolMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,5,1))
if mibBuilder.loadTexts:bIPv4PoolMIBObjects.setStatus(_A)
_BIPPoolTable_Object=MibTable
bIPPoolTable=_BIPPoolTable_Object((1,3,6,1,4,1,39406,2,1,5,1,1))
if mibBuilder.loadTexts:bIPPoolTable.setStatus(_A)
_BIPPoolEntry_Object=MibTableRow
bIPPoolEntry=_BIPPoolEntry_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1))
bIPPoolEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:bIPPoolEntry.setStatus(_A)
_BIPPoolStatsInterval_Type=Integer32
_BIPPoolStatsInterval_Object=MibTableColumn
bIPPoolStatsInterval=_BIPPoolStatsInterval_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1,1),_BIPPoolStatsInterval_Type())
bIPPoolStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bIPPoolStatsInterval.setStatus(_A)
_BIPPoolIndex_Type=Integer32
_BIPPoolIndex_Object=MibTableColumn
bIPPoolIndex=_BIPPoolIndex_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1,2),_BIPPoolIndex_Type())
bIPPoolIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bIPPoolIndex.setStatus(_A)
_BIPPoolIntervalDuration_Type=Integer32
_BIPPoolIntervalDuration_Object=MibTableColumn
bIPPoolIntervalDuration=_BIPPoolIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1,3),_BIPPoolIntervalDuration_Type())
bIPPoolIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolIntervalDuration.setStatus(_A)
_BIPPoolName_Type=DisplayString
_BIPPoolName_Object=MibTableColumn
bIPPoolName=_BIPPoolName_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1,4),_BIPPoolName_Type())
bIPPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolName.setStatus(_A)
_BIPPoolStartAddress_Type=InetAddressIPv4
_BIPPoolStartAddress_Object=MibTableColumn
bIPPoolStartAddress=_BIPPoolStartAddress_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1,5),_BIPPoolStartAddress_Type())
bIPPoolStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolStartAddress.setStatus(_A)
_BIPPoolEndAddress_Type=InetAddressIPv4
_BIPPoolEndAddress_Object=MibTableColumn
bIPPoolEndAddress=_BIPPoolEndAddress_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1,6),_BIPPoolEndAddress_Type())
bIPPoolEndAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolEndAddress.setStatus(_A)
_BIPPoolTotalAddresses_Type=Unsigned32
_BIPPoolTotalAddresses_Object=MibTableColumn
bIPPoolTotalAddresses=_BIPPoolTotalAddresses_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1,7),_BIPPoolTotalAddresses_Type())
bIPPoolTotalAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolTotalAddresses.setStatus(_A)
_BIPPoolReservedAddresses_Type=Unsigned32
_BIPPoolReservedAddresses_Object=MibTableColumn
bIPPoolReservedAddresses=_BIPPoolReservedAddresses_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1,8),_BIPPoolReservedAddresses_Type())
bIPPoolReservedAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolReservedAddresses.setStatus(_A)
_BIPPoolPeakFreeAddresses_Type=Unsigned32
_BIPPoolPeakFreeAddresses_Object=MibTableColumn
bIPPoolPeakFreeAddresses=_BIPPoolPeakFreeAddresses_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1,9),_BIPPoolPeakFreeAddresses_Type())
bIPPoolPeakFreeAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolPeakFreeAddresses.setStatus(_A)
_BIPPoolPeakUsedAddresses_Type=Unsigned32
_BIPPoolPeakUsedAddresses_Object=MibTableColumn
bIPPoolPeakUsedAddresses=_BIPPoolPeakUsedAddresses_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1,10),_BIPPoolPeakUsedAddresses_Type())
bIPPoolPeakUsedAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolPeakUsedAddresses.setStatus(_A)
_BIPPoolUsedAddrLowThreshold_Type=Unsigned32
_BIPPoolUsedAddrLowThreshold_Object=MibTableColumn
bIPPoolUsedAddrLowThreshold=_BIPPoolUsedAddrLowThreshold_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1,11),_BIPPoolUsedAddrLowThreshold_Type())
bIPPoolUsedAddrLowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolUsedAddrLowThreshold.setStatus(_A)
_BIPPoolUsedAddrHighThreshold_Type=Unsigned32
_BIPPoolUsedAddrHighThreshold_Object=MibTableColumn
bIPPoolUsedAddrHighThreshold=_BIPPoolUsedAddrHighThreshold_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1,12),_BIPPoolUsedAddrHighThreshold_Type())
bIPPoolUsedAddrHighThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolUsedAddrHighThreshold.setStatus(_A)
_BIPPoolGrpName_Type=DisplayString
_BIPPoolGrpName_Object=MibTableColumn
bIPPoolGrpName=_BIPPoolGrpName_Object((1,3,6,1,4,1,39406,2,1,5,1,1,1,13),_BIPPoolGrpName_Type())
bIPPoolGrpName.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGrpName.setStatus(_A)
_BIPPoolGroupTable_Object=MibTable
bIPPoolGroupTable=_BIPPoolGroupTable_Object((1,3,6,1,4,1,39406,2,1,5,1,2))
if mibBuilder.loadTexts:bIPPoolGroupTable.setStatus(_A)
_BIPPoolGroupEntry_Object=MibTableRow
bIPPoolGroupEntry=_BIPPoolGroupEntry_Object((1,3,6,1,4,1,39406,2,1,5,1,2,1))
bIPPoolGroupEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:bIPPoolGroupEntry.setStatus(_A)
_BIPPoolGroupStatsInterval_Type=Integer32
_BIPPoolGroupStatsInterval_Object=MibTableColumn
bIPPoolGroupStatsInterval=_BIPPoolGroupStatsInterval_Object((1,3,6,1,4,1,39406,2,1,5,1,2,1,1),_BIPPoolGroupStatsInterval_Type())
bIPPoolGroupStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bIPPoolGroupStatsInterval.setStatus(_A)
_BIPPoolGroupIndex_Type=Integer32
_BIPPoolGroupIndex_Object=MibTableColumn
bIPPoolGroupIndex=_BIPPoolGroupIndex_Object((1,3,6,1,4,1,39406,2,1,5,1,2,1,2),_BIPPoolGroupIndex_Type())
bIPPoolGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bIPPoolGroupIndex.setStatus(_A)
_BIPPoolGroupIntervalDuration_Type=Integer32
_BIPPoolGroupIntervalDuration_Object=MibTableColumn
bIPPoolGroupIntervalDuration=_BIPPoolGroupIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,5,1,2,1,3),_BIPPoolGroupIntervalDuration_Type())
bIPPoolGroupIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGroupIntervalDuration.setStatus(_A)
_BIPPoolGroupName_Type=DisplayString
_BIPPoolGroupName_Object=MibTableColumn
bIPPoolGroupName=_BIPPoolGroupName_Object((1,3,6,1,4,1,39406,2,1,5,1,2,1,4),_BIPPoolGroupName_Type())
bIPPoolGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGroupName.setStatus(_A)
_BIPPoolGroupTotalAddresses_Type=Unsigned32
_BIPPoolGroupTotalAddresses_Object=MibTableColumn
bIPPoolGroupTotalAddresses=_BIPPoolGroupTotalAddresses_Object((1,3,6,1,4,1,39406,2,1,5,1,2,1,5),_BIPPoolGroupTotalAddresses_Type())
bIPPoolGroupTotalAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGroupTotalAddresses.setStatus(_A)
_BIPPoolGroupReservedAddresses_Type=Unsigned32
_BIPPoolGroupReservedAddresses_Object=MibTableColumn
bIPPoolGroupReservedAddresses=_BIPPoolGroupReservedAddresses_Object((1,3,6,1,4,1,39406,2,1,5,1,2,1,6),_BIPPoolGroupReservedAddresses_Type())
bIPPoolGroupReservedAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGroupReservedAddresses.setStatus(_A)
_BIPPoolGroupPeakFreeAddresses_Type=Unsigned32
_BIPPoolGroupPeakFreeAddresses_Object=MibTableColumn
bIPPoolGroupPeakFreeAddresses=_BIPPoolGroupPeakFreeAddresses_Object((1,3,6,1,4,1,39406,2,1,5,1,2,1,7),_BIPPoolGroupPeakFreeAddresses_Type())
bIPPoolGroupPeakFreeAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGroupPeakFreeAddresses.setStatus(_A)
_BIPPoolGroupPeakUsedAddresses_Type=Unsigned32
_BIPPoolGroupPeakUsedAddresses_Object=MibTableColumn
bIPPoolGroupPeakUsedAddresses=_BIPPoolGroupPeakUsedAddresses_Object((1,3,6,1,4,1,39406,2,1,5,1,2,1,8),_BIPPoolGroupPeakUsedAddresses_Type())
bIPPoolGroupPeakUsedAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGroupPeakUsedAddresses.setStatus(_A)
_BIPPoolGlobalTable_Object=MibTable
bIPPoolGlobalTable=_BIPPoolGlobalTable_Object((1,3,6,1,4,1,39406,2,1,5,1,3))
if mibBuilder.loadTexts:bIPPoolGlobalTable.setStatus(_A)
_BIPPoolGlobalEntry_Object=MibTableRow
bIPPoolGlobalEntry=_BIPPoolGlobalEntry_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1))
bIPPoolGlobalEntry.setIndexNames((0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:bIPPoolGlobalEntry.setStatus(_A)
_BIPPoolGlobalStatsInterval_Type=Integer32
_BIPPoolGlobalStatsInterval_Object=MibTableColumn
bIPPoolGlobalStatsInterval=_BIPPoolGlobalStatsInterval_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,1),_BIPPoolGlobalStatsInterval_Type())
bIPPoolGlobalStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bIPPoolGlobalStatsInterval.setStatus(_A)
_BIPPoolClientIndex_Type=Integer32
_BIPPoolClientIndex_Object=MibTableColumn
bIPPoolClientIndex=_BIPPoolClientIndex_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,2),_BIPPoolClientIndex_Type())
bIPPoolClientIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bIPPoolClientIndex.setStatus(_A)
_BIPPoolClientName_Type=DisplayString
_BIPPoolClientName_Object=MibTableColumn
bIPPoolClientName=_BIPPoolClientName_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,3),_BIPPoolClientName_Type())
bIPPoolClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolClientName.setStatus(_A)
_BIPPoolGlobalAllocReq_Type=Unsigned32
_BIPPoolGlobalAllocReq_Object=MibTableColumn
bIPPoolGlobalAllocReq=_BIPPoolGlobalAllocReq_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,4),_BIPPoolGlobalAllocReq_Type())
bIPPoolGlobalAllocReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalAllocReq.setStatus(_A)
_BIPPoolGlobalAllocReqSucc_Type=Unsigned32
_BIPPoolGlobalAllocReqSucc_Object=MibTableColumn
bIPPoolGlobalAllocReqSucc=_BIPPoolGlobalAllocReqSucc_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,5),_BIPPoolGlobalAllocReqSucc_Type())
bIPPoolGlobalAllocReqSucc.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalAllocReqSucc.setStatus(_A)
_BIPPoolGlobalAllocReqUnSucc_Type=Unsigned32
_BIPPoolGlobalAllocReqUnSucc_Object=MibTableColumn
bIPPoolGlobalAllocReqUnSucc=_BIPPoolGlobalAllocReqUnSucc_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,6),_BIPPoolGlobalAllocReqUnSucc_Type())
bIPPoolGlobalAllocReqUnSucc.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalAllocReqUnSucc.setStatus(_A)
_BIPPoolGlobalDupAllocReq_Type=Unsigned32
_BIPPoolGlobalDupAllocReq_Object=MibTableColumn
bIPPoolGlobalDupAllocReq=_BIPPoolGlobalDupAllocReq_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,7),_BIPPoolGlobalDupAllocReq_Type())
bIPPoolGlobalDupAllocReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalDupAllocReq.setStatus(_A)
_BIPPoolGlobalStaticAllocReq_Type=Unsigned32
_BIPPoolGlobalStaticAllocReq_Object=MibTableColumn
bIPPoolGlobalStaticAllocReq=_BIPPoolGlobalStaticAllocReq_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,8),_BIPPoolGlobalStaticAllocReq_Type())
bIPPoolGlobalStaticAllocReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalStaticAllocReq.setStatus(_A)
_BIPPoolGlobalAllocResponses_Type=Unsigned32
_BIPPoolGlobalAllocResponses_Object=MibTableColumn
bIPPoolGlobalAllocResponses=_BIPPoolGlobalAllocResponses_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,9),_BIPPoolGlobalAllocResponses_Type())
bIPPoolGlobalAllocResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalAllocResponses.setStatus(_A)
_BIPPoolGlobalDeAllocReq_Type=Unsigned32
_BIPPoolGlobalDeAllocReq_Object=MibTableColumn
bIPPoolGlobalDeAllocReq=_BIPPoolGlobalDeAllocReq_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,10),_BIPPoolGlobalDeAllocReq_Type())
bIPPoolGlobalDeAllocReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalDeAllocReq.setStatus(_A)
_BIPPoolGlobalDeAllocReqSucc_Type=Unsigned32
_BIPPoolGlobalDeAllocReqSucc_Object=MibTableColumn
bIPPoolGlobalDeAllocReqSucc=_BIPPoolGlobalDeAllocReqSucc_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,11),_BIPPoolGlobalDeAllocReqSucc_Type())
bIPPoolGlobalDeAllocReqSucc.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalDeAllocReqSucc.setStatus(_A)
_BIPPoolGlobalDeAllocReqUnSucc_Type=Unsigned32
_BIPPoolGlobalDeAllocReqUnSucc_Object=MibTableColumn
bIPPoolGlobalDeAllocReqUnSucc=_BIPPoolGlobalDeAllocReqUnSucc_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,12),_BIPPoolGlobalDeAllocReqUnSucc_Type())
bIPPoolGlobalDeAllocReqUnSucc.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalDeAllocReqUnSucc.setStatus(_A)
_BIPPoolGlobalInvalidReq_Type=Unsigned32
_BIPPoolGlobalInvalidReq_Object=MibTableColumn
bIPPoolGlobalInvalidReq=_BIPPoolGlobalInvalidReq_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,13),_BIPPoolGlobalInvalidReq_Type())
bIPPoolGlobalInvalidReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalInvalidReq.setStatus(_A)
_BIPPoolGlobalNotAvailCount_Type=Unsigned32
_BIPPoolGlobalNotAvailCount_Object=MibTableColumn
bIPPoolGlobalNotAvailCount=_BIPPoolGlobalNotAvailCount_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,14),_BIPPoolGlobalNotAvailCount_Type())
bIPPoolGlobalNotAvailCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalNotAvailCount.setStatus(_A)
_BIPPoolGlobalPoolExhaustedCount_Type=Unsigned32
_BIPPoolGlobalPoolExhaustedCount_Object=MibTableColumn
bIPPoolGlobalPoolExhaustedCount=_BIPPoolGlobalPoolExhaustedCount_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,15),_BIPPoolGlobalPoolExhaustedCount_Type())
bIPPoolGlobalPoolExhaustedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalPoolExhaustedCount.setStatus(_A)
_BIPPoolGlobalGroupExhaustedCount_Type=Unsigned32
_BIPPoolGlobalGroupExhaustedCount_Object=MibTableColumn
bIPPoolGlobalGroupExhaustedCount=_BIPPoolGlobalGroupExhaustedCount_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,16),_BIPPoolGlobalGroupExhaustedCount_Type())
bIPPoolGlobalGroupExhaustedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalGroupExhaustedCount.setStatus(_A)
_BIPPoolGlobalInvalidPoolNameCount_Type=Unsigned32
_BIPPoolGlobalInvalidPoolNameCount_Object=MibTableColumn
bIPPoolGlobalInvalidPoolNameCount=_BIPPoolGlobalInvalidPoolNameCount_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,17),_BIPPoolGlobalInvalidPoolNameCount_Type())
bIPPoolGlobalInvalidPoolNameCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalInvalidPoolNameCount.setStatus(_A)
_BIPPoolGlobalInvalidGroupNameCount_Type=Unsigned32
_BIPPoolGlobalInvalidGroupNameCount_Object=MibTableColumn
bIPPoolGlobalInvalidGroupNameCount=_BIPPoolGlobalInvalidGroupNameCount_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,18),_BIPPoolGlobalInvalidGroupNameCount_Type())
bIPPoolGlobalInvalidGroupNameCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalInvalidGroupNameCount.setStatus(_A)
_BIPPoolGlobalInvalidIPAddrCount_Type=Unsigned32
_BIPPoolGlobalInvalidIPAddrCount_Object=MibTableColumn
bIPPoolGlobalInvalidIPAddrCount=_BIPPoolGlobalInvalidIPAddrCount_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,19),_BIPPoolGlobalInvalidIPAddrCount_Type())
bIPPoolGlobalInvalidIPAddrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalInvalidIPAddrCount.setStatus(_A)
_BIPPoolGlobalHashInsertFail_Type=Unsigned32
_BIPPoolGlobalHashInsertFail_Object=MibTableColumn
bIPPoolGlobalHashInsertFail=_BIPPoolGlobalHashInsertFail_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,20),_BIPPoolGlobalHashInsertFail_Type())
bIPPoolGlobalHashInsertFail.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalHashInsertFail.setStatus(_A)
_BIPPoolGlobalHashDeleteFail_Type=Unsigned32
_BIPPoolGlobalHashDeleteFail_Object=MibTableColumn
bIPPoolGlobalHashDeleteFail=_BIPPoolGlobalHashDeleteFail_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,21),_BIPPoolGlobalHashDeleteFail_Type())
bIPPoolGlobalHashDeleteFail.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalHashDeleteFail.setStatus(_A)
_BIPPoolGlobalRequestedAllocatedMismacth_Type=Unsigned32
_BIPPoolGlobalRequestedAllocatedMismacth_Object=MibTableColumn
bIPPoolGlobalRequestedAllocatedMismacth=_BIPPoolGlobalRequestedAllocatedMismacth_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,22),_BIPPoolGlobalRequestedAllocatedMismacth_Type())
bIPPoolGlobalRequestedAllocatedMismacth.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalRequestedAllocatedMismacth.setStatus(_A)
_BIPPoolGlobalRequestedIPNotFree_Type=Unsigned32
_BIPPoolGlobalRequestedIPNotFree_Object=MibTableColumn
bIPPoolGlobalRequestedIPNotFree=_BIPPoolGlobalRequestedIPNotFree_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,23),_BIPPoolGlobalRequestedIPNotFree_Type())
bIPPoolGlobalRequestedIPNotFree.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalRequestedIPNotFree.setStatus(_A)
_BIPPoolGlobalGenErrCount_Type=Unsigned32
_BIPPoolGlobalGenErrCount_Object=MibTableColumn
bIPPoolGlobalGenErrCount=_BIPPoolGlobalGenErrCount_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,24),_BIPPoolGlobalGenErrCount_Type())
bIPPoolGlobalGenErrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalGenErrCount.setStatus(_A)
_BIPPoolGlobalAddrRelDueToIntAdd_Type=Unsigned32
_BIPPoolGlobalAddrRelDueToIntAdd_Object=MibTableColumn
bIPPoolGlobalAddrRelDueToIntAdd=_BIPPoolGlobalAddrRelDueToIntAdd_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,25),_BIPPoolGlobalAddrRelDueToIntAdd_Type())
bIPPoolGlobalAddrRelDueToIntAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalAddrRelDueToIntAdd.setStatus(_A)
_BIPPoolGlobalGroupDeAllocReq_Type=Unsigned32
_BIPPoolGlobalGroupDeAllocReq_Object=MibTableColumn
bIPPoolGlobalGroupDeAllocReq=_BIPPoolGlobalGroupDeAllocReq_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,26),_BIPPoolGlobalGroupDeAllocReq_Type())
bIPPoolGlobalGroupDeAllocReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalGroupDeAllocReq.setStatus(_A)
_BIPPoolGlobalGroupDeAllocReqSucc_Type=Unsigned32
_BIPPoolGlobalGroupDeAllocReqSucc_Object=MibTableColumn
bIPPoolGlobalGroupDeAllocReqSucc=_BIPPoolGlobalGroupDeAllocReqSucc_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,27),_BIPPoolGlobalGroupDeAllocReqSucc_Type())
bIPPoolGlobalGroupDeAllocReqSucc.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalGroupDeAllocReqSucc.setStatus(_A)
_BIPPoolGlobalGroupDeAllocReqUnSucc_Type=Unsigned32
_BIPPoolGlobalGroupDeAllocReqUnSucc_Object=MibTableColumn
bIPPoolGlobalGroupDeAllocReqUnSucc=_BIPPoolGlobalGroupDeAllocReqUnSucc_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,28),_BIPPoolGlobalGroupDeAllocReqUnSucc_Type())
bIPPoolGlobalGroupDeAllocReqUnSucc.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalGroupDeAllocReqUnSucc.setStatus(_A)
_BIPPoolTotalPoolCreatedEvents_Type=Unsigned32
_BIPPoolTotalPoolCreatedEvents_Object=MibTableColumn
bIPPoolTotalPoolCreatedEvents=_BIPPoolTotalPoolCreatedEvents_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,29),_BIPPoolTotalPoolCreatedEvents_Type())
bIPPoolTotalPoolCreatedEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolTotalPoolCreatedEvents.setStatus(_A)
_BIPPoolTotalPoolDeletedEvents_Type=Unsigned32
_BIPPoolTotalPoolDeletedEvents_Object=MibTableColumn
bIPPoolTotalPoolDeletedEvents=_BIPPoolTotalPoolDeletedEvents_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,30),_BIPPoolTotalPoolDeletedEvents_Type())
bIPPoolTotalPoolDeletedEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolTotalPoolDeletedEvents.setStatus(_A)
_BIPPoolGlobalIntervalDuration_Type=Integer32
_BIPPoolGlobalIntervalDuration_Object=MibTableColumn
bIPPoolGlobalIntervalDuration=_BIPPoolGlobalIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,5,1,3,1,31),_BIPPoolGlobalIntervalDuration_Type())
bIPPoolGlobalIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPoolGlobalIntervalDuration.setStatus(_A)
_BIPv4PoolNotifObjects_ObjectIdentity=ObjectIdentity
bIPv4PoolNotifObjects=_BIPv4PoolNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,5,2))
if mibBuilder.loadTexts:bIPv4PoolNotifObjects.setStatus(_A)
_BIPv6PoolMIBObjects_ObjectIdentity=ObjectIdentity
bIPv6PoolMIBObjects=_BIPv6PoolMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,5,3))
if mibBuilder.loadTexts:bIPv6PoolMIBObjects.setStatus(_A)
_BIPv6PoolTable_Object=MibTable
bIPv6PoolTable=_BIPv6PoolTable_Object((1,3,6,1,4,1,39406,2,1,5,3,1))
if mibBuilder.loadTexts:bIPv6PoolTable.setStatus(_A)
_BIPv6PoolEntry_Object=MibTableRow
bIPv6PoolEntry=_BIPv6PoolEntry_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1))
bIPv6PoolEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:bIPv6PoolEntry.setStatus(_A)
_BIPv6PoolStatsInterval_Type=Integer32
_BIPv6PoolStatsInterval_Object=MibTableColumn
bIPv6PoolStatsInterval=_BIPv6PoolStatsInterval_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1,1),_BIPv6PoolStatsInterval_Type())
bIPv6PoolStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bIPv6PoolStatsInterval.setStatus(_A)
_BIPv6PoolIndex_Type=Integer32
_BIPv6PoolIndex_Object=MibTableColumn
bIPv6PoolIndex=_BIPv6PoolIndex_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1,2),_BIPv6PoolIndex_Type())
bIPv6PoolIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bIPv6PoolIndex.setStatus(_A)
_BIPv6PoolIntervalDuration_Type=Integer32
_BIPv6PoolIntervalDuration_Object=MibTableColumn
bIPv6PoolIntervalDuration=_BIPv6PoolIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1,3),_BIPv6PoolIntervalDuration_Type())
bIPv6PoolIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolIntervalDuration.setStatus(_A)
_BIPv6PoolName_Type=DisplayString
_BIPv6PoolName_Object=MibTableColumn
bIPv6PoolName=_BIPv6PoolName_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1,4),_BIPv6PoolName_Type())
bIPv6PoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolName.setStatus(_A)
_BIPv6PoolStartPrefix_Type=InetAddressIPv6
_BIPv6PoolStartPrefix_Object=MibTableColumn
bIPv6PoolStartPrefix=_BIPv6PoolStartPrefix_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1,5),_BIPv6PoolStartPrefix_Type())
bIPv6PoolStartPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolStartPrefix.setStatus(_A)
_BIPv6PoolEndPrefix_Type=InetAddressIPv6
_BIPv6PoolEndPrefix_Object=MibTableColumn
bIPv6PoolEndPrefix=_BIPv6PoolEndPrefix_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1,6),_BIPv6PoolEndPrefix_Type())
bIPv6PoolEndPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolEndPrefix.setStatus(_A)
_BIPv6PoolTotalPrefixes_Type=Unsigned32
_BIPv6PoolTotalPrefixes_Object=MibTableColumn
bIPv6PoolTotalPrefixes=_BIPv6PoolTotalPrefixes_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1,7),_BIPv6PoolTotalPrefixes_Type())
bIPv6PoolTotalPrefixes.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolTotalPrefixes.setStatus(_A)
_BIPv6PoolReservedPrefixes_Type=Unsigned32
_BIPv6PoolReservedPrefixes_Object=MibTableColumn
bIPv6PoolReservedPrefixes=_BIPv6PoolReservedPrefixes_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1,8),_BIPv6PoolReservedPrefixes_Type())
bIPv6PoolReservedPrefixes.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolReservedPrefixes.setStatus(_A)
_BIPv6PoolPeakFreePrefixes_Type=Unsigned32
_BIPv6PoolPeakFreePrefixes_Object=MibTableColumn
bIPv6PoolPeakFreePrefixes=_BIPv6PoolPeakFreePrefixes_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1,9),_BIPv6PoolPeakFreePrefixes_Type())
bIPv6PoolPeakFreePrefixes.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolPeakFreePrefixes.setStatus(_A)
_BIPv6PoolPeakUsedPrefixes_Type=Unsigned32
_BIPv6PoolPeakUsedPrefixes_Object=MibTableColumn
bIPv6PoolPeakUsedPrefixes=_BIPv6PoolPeakUsedPrefixes_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1,10),_BIPv6PoolPeakUsedPrefixes_Type())
bIPv6PoolPeakUsedPrefixes.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolPeakUsedPrefixes.setStatus(_A)
_BIPv6PoolUsedPrefixLowThreshold_Type=Unsigned32
_BIPv6PoolUsedPrefixLowThreshold_Object=MibTableColumn
bIPv6PoolUsedPrefixLowThreshold=_BIPv6PoolUsedPrefixLowThreshold_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1,11),_BIPv6PoolUsedPrefixLowThreshold_Type())
bIPv6PoolUsedPrefixLowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolUsedPrefixLowThreshold.setStatus(_A)
_BIPv6PoolUsedPrefixHighThreshold_Type=Unsigned32
_BIPv6PoolUsedPrefixHighThreshold_Object=MibTableColumn
bIPv6PoolUsedPrefixHighThreshold=_BIPv6PoolUsedPrefixHighThreshold_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1,12),_BIPv6PoolUsedPrefixHighThreshold_Type())
bIPv6PoolUsedPrefixHighThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolUsedPrefixHighThreshold.setStatus(_A)
_BIPv6PoolGrpName_Type=DisplayString
_BIPv6PoolGrpName_Object=MibTableColumn
bIPv6PoolGrpName=_BIPv6PoolGrpName_Object((1,3,6,1,4,1,39406,2,1,5,3,1,1,13),_BIPv6PoolGrpName_Type())
bIPv6PoolGrpName.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGrpName.setStatus(_A)
_BIPv6PoolGroupTable_Object=MibTable
bIPv6PoolGroupTable=_BIPv6PoolGroupTable_Object((1,3,6,1,4,1,39406,2,1,5,3,2))
if mibBuilder.loadTexts:bIPv6PoolGroupTable.setStatus(_A)
_BIPv6PoolGroupEntry_Object=MibTableRow
bIPv6PoolGroupEntry=_BIPv6PoolGroupEntry_Object((1,3,6,1,4,1,39406,2,1,5,3,2,1))
bIPv6PoolGroupEntry.setIndexNames((0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:bIPv6PoolGroupEntry.setStatus(_A)
_BIPv6PoolGroupStatsInterval_Type=Integer32
_BIPv6PoolGroupStatsInterval_Object=MibTableColumn
bIPv6PoolGroupStatsInterval=_BIPv6PoolGroupStatsInterval_Object((1,3,6,1,4,1,39406,2,1,5,3,2,1,1),_BIPv6PoolGroupStatsInterval_Type())
bIPv6PoolGroupStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bIPv6PoolGroupStatsInterval.setStatus(_A)
_BIPv6PoolGroupIndex_Type=Integer32
_BIPv6PoolGroupIndex_Object=MibTableColumn
bIPv6PoolGroupIndex=_BIPv6PoolGroupIndex_Object((1,3,6,1,4,1,39406,2,1,5,3,2,1,2),_BIPv6PoolGroupIndex_Type())
bIPv6PoolGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bIPv6PoolGroupIndex.setStatus(_A)
_BIPv6PoolGroupIntervalDuration_Type=Integer32
_BIPv6PoolGroupIntervalDuration_Object=MibTableColumn
bIPv6PoolGroupIntervalDuration=_BIPv6PoolGroupIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,5,3,2,1,3),_BIPv6PoolGroupIntervalDuration_Type())
bIPv6PoolGroupIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGroupIntervalDuration.setStatus(_A)
_BIPv6PoolGroupName_Type=DisplayString
_BIPv6PoolGroupName_Object=MibTableColumn
bIPv6PoolGroupName=_BIPv6PoolGroupName_Object((1,3,6,1,4,1,39406,2,1,5,3,2,1,4),_BIPv6PoolGroupName_Type())
bIPv6PoolGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGroupName.setStatus(_A)
_BIPv6PoolGroupTotalPrefixes_Type=Unsigned32
_BIPv6PoolGroupTotalPrefixes_Object=MibTableColumn
bIPv6PoolGroupTotalPrefixes=_BIPv6PoolGroupTotalPrefixes_Object((1,3,6,1,4,1,39406,2,1,5,3,2,1,5),_BIPv6PoolGroupTotalPrefixes_Type())
bIPv6PoolGroupTotalPrefixes.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGroupTotalPrefixes.setStatus(_A)
_BIPv6PoolGroupReservedPrefixes_Type=Unsigned32
_BIPv6PoolGroupReservedPrefixes_Object=MibTableColumn
bIPv6PoolGroupReservedPrefixes=_BIPv6PoolGroupReservedPrefixes_Object((1,3,6,1,4,1,39406,2,1,5,3,2,1,6),_BIPv6PoolGroupReservedPrefixes_Type())
bIPv6PoolGroupReservedPrefixes.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGroupReservedPrefixes.setStatus(_A)
_BIPv6PoolGroupPeakFreePrefixes_Type=Unsigned32
_BIPv6PoolGroupPeakFreePrefixes_Object=MibTableColumn
bIPv6PoolGroupPeakFreePrefixes=_BIPv6PoolGroupPeakFreePrefixes_Object((1,3,6,1,4,1,39406,2,1,5,3,2,1,7),_BIPv6PoolGroupPeakFreePrefixes_Type())
bIPv6PoolGroupPeakFreePrefixes.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGroupPeakFreePrefixes.setStatus(_A)
_BIPv6PoolGroupPeakUsedPrefixes_Type=Unsigned32
_BIPv6PoolGroupPeakUsedPrefixes_Object=MibTableColumn
bIPv6PoolGroupPeakUsedPrefixes=_BIPv6PoolGroupPeakUsedPrefixes_Object((1,3,6,1,4,1,39406,2,1,5,3,2,1,8),_BIPv6PoolGroupPeakUsedPrefixes_Type())
bIPv6PoolGroupPeakUsedPrefixes.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGroupPeakUsedPrefixes.setStatus(_A)
_BIPv6PoolGlobalTable_Object=MibTable
bIPv6PoolGlobalTable=_BIPv6PoolGlobalTable_Object((1,3,6,1,4,1,39406,2,1,5,3,3))
if mibBuilder.loadTexts:bIPv6PoolGlobalTable.setStatus(_A)
_BIPv6PoolGlobalEntry_Object=MibTableRow
bIPv6PoolGlobalEntry=_BIPv6PoolGlobalEntry_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1))
bIPv6PoolGlobalEntry.setIndexNames((0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:bIPv6PoolGlobalEntry.setStatus(_A)
_BIPv6PoolGlobalStatsInterval_Type=Integer32
_BIPv6PoolGlobalStatsInterval_Object=MibTableColumn
bIPv6PoolGlobalStatsInterval=_BIPv6PoolGlobalStatsInterval_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,1),_BIPv6PoolGlobalStatsInterval_Type())
bIPv6PoolGlobalStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bIPv6PoolGlobalStatsInterval.setStatus(_A)
_BIPv6PoolClientIndex_Type=Integer32
_BIPv6PoolClientIndex_Object=MibTableColumn
bIPv6PoolClientIndex=_BIPv6PoolClientIndex_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,2),_BIPv6PoolClientIndex_Type())
bIPv6PoolClientIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bIPv6PoolClientIndex.setStatus(_A)
_BIPv6PoolClientName_Type=DisplayString
_BIPv6PoolClientName_Object=MibTableColumn
bIPv6PoolClientName=_BIPv6PoolClientName_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,3),_BIPv6PoolClientName_Type())
bIPv6PoolClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolClientName.setStatus(_A)
_BIPv6PoolGlobalAllocReq_Type=Unsigned32
_BIPv6PoolGlobalAllocReq_Object=MibTableColumn
bIPv6PoolGlobalAllocReq=_BIPv6PoolGlobalAllocReq_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,4),_BIPv6PoolGlobalAllocReq_Type())
bIPv6PoolGlobalAllocReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalAllocReq.setStatus(_A)
_BIPv6PoolGlobalAllocReqSucc_Type=Unsigned32
_BIPv6PoolGlobalAllocReqSucc_Object=MibTableColumn
bIPv6PoolGlobalAllocReqSucc=_BIPv6PoolGlobalAllocReqSucc_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,5),_BIPv6PoolGlobalAllocReqSucc_Type())
bIPv6PoolGlobalAllocReqSucc.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalAllocReqSucc.setStatus(_A)
_BIPv6PoolGlobalAllocReqUnSucc_Type=Unsigned32
_BIPv6PoolGlobalAllocReqUnSucc_Object=MibTableColumn
bIPv6PoolGlobalAllocReqUnSucc=_BIPv6PoolGlobalAllocReqUnSucc_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,6),_BIPv6PoolGlobalAllocReqUnSucc_Type())
bIPv6PoolGlobalAllocReqUnSucc.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalAllocReqUnSucc.setStatus(_A)
_BIPv6PoolGlobalDupAllocReq_Type=Unsigned32
_BIPv6PoolGlobalDupAllocReq_Object=MibTableColumn
bIPv6PoolGlobalDupAllocReq=_BIPv6PoolGlobalDupAllocReq_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,7),_BIPv6PoolGlobalDupAllocReq_Type())
bIPv6PoolGlobalDupAllocReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalDupAllocReq.setStatus(_A)
_BIPv6PoolGlobalStaticAllocReq_Type=Unsigned32
_BIPv6PoolGlobalStaticAllocReq_Object=MibTableColumn
bIPv6PoolGlobalStaticAllocReq=_BIPv6PoolGlobalStaticAllocReq_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,8),_BIPv6PoolGlobalStaticAllocReq_Type())
bIPv6PoolGlobalStaticAllocReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalStaticAllocReq.setStatus(_A)
_BIPv6PoolGlobalAllocResponses_Type=Unsigned32
_BIPv6PoolGlobalAllocResponses_Object=MibTableColumn
bIPv6PoolGlobalAllocResponses=_BIPv6PoolGlobalAllocResponses_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,9),_BIPv6PoolGlobalAllocResponses_Type())
bIPv6PoolGlobalAllocResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalAllocResponses.setStatus(_A)
_BIPv6PoolGlobalDeAllocReq_Type=Unsigned32
_BIPv6PoolGlobalDeAllocReq_Object=MibTableColumn
bIPv6PoolGlobalDeAllocReq=_BIPv6PoolGlobalDeAllocReq_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,10),_BIPv6PoolGlobalDeAllocReq_Type())
bIPv6PoolGlobalDeAllocReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalDeAllocReq.setStatus(_A)
_BIPv6PoolGlobalDeAllocReqSucc_Type=Unsigned32
_BIPv6PoolGlobalDeAllocReqSucc_Object=MibTableColumn
bIPv6PoolGlobalDeAllocReqSucc=_BIPv6PoolGlobalDeAllocReqSucc_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,11),_BIPv6PoolGlobalDeAllocReqSucc_Type())
bIPv6PoolGlobalDeAllocReqSucc.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalDeAllocReqSucc.setStatus(_A)
_BIPv6PoolGlobalDeAllocReqUnSucc_Type=Unsigned32
_BIPv6PoolGlobalDeAllocReqUnSucc_Object=MibTableColumn
bIPv6PoolGlobalDeAllocReqUnSucc=_BIPv6PoolGlobalDeAllocReqUnSucc_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,12),_BIPv6PoolGlobalDeAllocReqUnSucc_Type())
bIPv6PoolGlobalDeAllocReqUnSucc.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalDeAllocReqUnSucc.setStatus(_A)
_BIPv6PoolGlobalInvalidReq_Type=Unsigned32
_BIPv6PoolGlobalInvalidReq_Object=MibTableColumn
bIPv6PoolGlobalInvalidReq=_BIPv6PoolGlobalInvalidReq_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,13),_BIPv6PoolGlobalInvalidReq_Type())
bIPv6PoolGlobalInvalidReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalInvalidReq.setStatus(_A)
_BIPv6PoolGlobalNotAvailCount_Type=Unsigned32
_BIPv6PoolGlobalNotAvailCount_Object=MibTableColumn
bIPv6PoolGlobalNotAvailCount=_BIPv6PoolGlobalNotAvailCount_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,14),_BIPv6PoolGlobalNotAvailCount_Type())
bIPv6PoolGlobalNotAvailCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalNotAvailCount.setStatus(_A)
_BIPv6PoolGlobalPoolExhaustedCount_Type=Unsigned32
_BIPv6PoolGlobalPoolExhaustedCount_Object=MibTableColumn
bIPv6PoolGlobalPoolExhaustedCount=_BIPv6PoolGlobalPoolExhaustedCount_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,15),_BIPv6PoolGlobalPoolExhaustedCount_Type())
bIPv6PoolGlobalPoolExhaustedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalPoolExhaustedCount.setStatus(_A)
_BIPv6PoolGlobalGroupExhaustedCount_Type=Unsigned32
_BIPv6PoolGlobalGroupExhaustedCount_Object=MibTableColumn
bIPv6PoolGlobalGroupExhaustedCount=_BIPv6PoolGlobalGroupExhaustedCount_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,16),_BIPv6PoolGlobalGroupExhaustedCount_Type())
bIPv6PoolGlobalGroupExhaustedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalGroupExhaustedCount.setStatus(_A)
_BIPv6PoolGlobalInvalidPoolNameCount_Type=Unsigned32
_BIPv6PoolGlobalInvalidPoolNameCount_Object=MibTableColumn
bIPv6PoolGlobalInvalidPoolNameCount=_BIPv6PoolGlobalInvalidPoolNameCount_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,17),_BIPv6PoolGlobalInvalidPoolNameCount_Type())
bIPv6PoolGlobalInvalidPoolNameCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalInvalidPoolNameCount.setStatus(_A)
_BIPv6PoolGlobalInvalidGroupNameCount_Type=Unsigned32
_BIPv6PoolGlobalInvalidGroupNameCount_Object=MibTableColumn
bIPv6PoolGlobalInvalidGroupNameCount=_BIPv6PoolGlobalInvalidGroupNameCount_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,18),_BIPv6PoolGlobalInvalidGroupNameCount_Type())
bIPv6PoolGlobalInvalidGroupNameCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalInvalidGroupNameCount.setStatus(_A)
_BIPv6PoolGlobalInvalidIPAddrCount_Type=Unsigned32
_BIPv6PoolGlobalInvalidIPAddrCount_Object=MibTableColumn
bIPv6PoolGlobalInvalidIPAddrCount=_BIPv6PoolGlobalInvalidIPAddrCount_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,19),_BIPv6PoolGlobalInvalidIPAddrCount_Type())
bIPv6PoolGlobalInvalidIPAddrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalInvalidIPAddrCount.setStatus(_A)
_BIPv6PoolGlobalHashInsertFail_Type=Unsigned32
_BIPv6PoolGlobalHashInsertFail_Object=MibTableColumn
bIPv6PoolGlobalHashInsertFail=_BIPv6PoolGlobalHashInsertFail_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,20),_BIPv6PoolGlobalHashInsertFail_Type())
bIPv6PoolGlobalHashInsertFail.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalHashInsertFail.setStatus(_A)
_BIPv6PoolGlobalHashDeleteFail_Type=Unsigned32
_BIPv6PoolGlobalHashDeleteFail_Object=MibTableColumn
bIPv6PoolGlobalHashDeleteFail=_BIPv6PoolGlobalHashDeleteFail_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,21),_BIPv6PoolGlobalHashDeleteFail_Type())
bIPv6PoolGlobalHashDeleteFail.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalHashDeleteFail.setStatus(_A)
_BIPv6PoolGlobalRequestedAllocatedMismacth_Type=Unsigned32
_BIPv6PoolGlobalRequestedAllocatedMismacth_Object=MibTableColumn
bIPv6PoolGlobalRequestedAllocatedMismacth=_BIPv6PoolGlobalRequestedAllocatedMismacth_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,22),_BIPv6PoolGlobalRequestedAllocatedMismacth_Type())
bIPv6PoolGlobalRequestedAllocatedMismacth.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalRequestedAllocatedMismacth.setStatus(_A)
_BIPv6PoolGlobalRequestedIPNotFree_Type=Unsigned32
_BIPv6PoolGlobalRequestedIPNotFree_Object=MibTableColumn
bIPv6PoolGlobalRequestedIPNotFree=_BIPv6PoolGlobalRequestedIPNotFree_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,23),_BIPv6PoolGlobalRequestedIPNotFree_Type())
bIPv6PoolGlobalRequestedIPNotFree.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalRequestedIPNotFree.setStatus(_A)
_BIPv6PoolGlobalGenErrCount_Type=Unsigned32
_BIPv6PoolGlobalGenErrCount_Object=MibTableColumn
bIPv6PoolGlobalGenErrCount=_BIPv6PoolGlobalGenErrCount_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,24),_BIPv6PoolGlobalGenErrCount_Type())
bIPv6PoolGlobalGenErrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalGenErrCount.setStatus(_A)
_BIPv6PoolGlobalPrefixRelDueToIntAdd_Type=Unsigned32
_BIPv6PoolGlobalPrefixRelDueToIntAdd_Object=MibTableColumn
bIPv6PoolGlobalPrefixRelDueToIntAdd=_BIPv6PoolGlobalPrefixRelDueToIntAdd_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,25),_BIPv6PoolGlobalPrefixRelDueToIntAdd_Type())
bIPv6PoolGlobalPrefixRelDueToIntAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalPrefixRelDueToIntAdd.setStatus(_A)
_BIPv6PoolTotalPoolCreatedEvents_Type=Unsigned32
_BIPv6PoolTotalPoolCreatedEvents_Object=MibTableColumn
bIPv6PoolTotalPoolCreatedEvents=_BIPv6PoolTotalPoolCreatedEvents_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,26),_BIPv6PoolTotalPoolCreatedEvents_Type())
bIPv6PoolTotalPoolCreatedEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolTotalPoolCreatedEvents.setStatus(_A)
_BIPv6PoolTotalPoolDeletedEvents_Type=Unsigned32
_BIPv6PoolTotalPoolDeletedEvents_Object=MibTableColumn
bIPv6PoolTotalPoolDeletedEvents=_BIPv6PoolTotalPoolDeletedEvents_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,27),_BIPv6PoolTotalPoolDeletedEvents_Type())
bIPv6PoolTotalPoolDeletedEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolTotalPoolDeletedEvents.setStatus(_A)
_BIPv6PoolGlobalIntervalDuration_Type=Integer32
_BIPv6PoolGlobalIntervalDuration_Object=MibTableColumn
bIPv6PoolGlobalIntervalDuration=_BIPv6PoolGlobalIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,5,3,3,1,28),_BIPv6PoolGlobalIntervalDuration_Type())
bIPv6PoolGlobalIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPv6PoolGlobalIntervalDuration.setStatus(_A)
_BIPv6PoolNotifObjects_ObjectIdentity=ObjectIdentity
bIPv6PoolNotifObjects=_BIPv6PoolNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,5,4))
if mibBuilder.loadTexts:bIPv6PoolNotifObjects.setStatus(_A)
bIPPoolUsedAddrLow=NotificationType((1,3,6,1,4,1,39406,2,1,5,0,1))
bIPPoolUsedAddrLow.setObjects(*((_C,_E),(_C,_F),(_C,_U)))
if mibBuilder.loadTexts:bIPPoolUsedAddrLow.setStatus(_A)
bIPPoolUsedAddrHigh=NotificationType((1,3,6,1,4,1,39406,2,1,5,0,2))
bIPPoolUsedAddrHigh.setObjects(*((_C,_E),(_C,_F),(_C,_V)))
if mibBuilder.loadTexts:bIPPoolUsedAddrHigh.setStatus(_A)
bIPv6PoolUsedPrefixLow=NotificationType((1,3,6,1,4,1,39406,2,1,5,0,3))
bIPv6PoolUsedPrefixLow.setObjects(*((_C,_G),(_C,_H),(_C,_W)))
if mibBuilder.loadTexts:bIPv6PoolUsedPrefixLow.setStatus(_A)
bIPv6PoolUsedPrefixHigh=NotificationType((1,3,6,1,4,1,39406,2,1,5,0,4))
bIPv6PoolUsedPrefixHigh.setObjects(*((_C,_G),(_C,_H),(_C,_X)))
if mibBuilder.loadTexts:bIPv6PoolUsedPrefixHigh.setStatus(_A)
bIPPoolAddrExhausted=NotificationType((1,3,6,1,4,1,39406,2,1,5,0,5))
bIPPoolAddrExhausted.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:bIPPoolAddrExhausted.setStatus(_A)
bIPv6PoolPrefixExhausted=NotificationType((1,3,6,1,4,1,39406,2,1,5,0,6))
bIPv6PoolPrefixExhausted.setObjects(*((_C,_G),(_C,_H)))
if mibBuilder.loadTexts:bIPv6PoolPrefixExhausted.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'benuIPPoolMIB':benuIPPoolMIB,'bIPPoolNotifications':bIPPoolNotifications,'bIPPoolUsedAddrLow':bIPPoolUsedAddrLow,'bIPPoolUsedAddrHigh':bIPPoolUsedAddrHigh,'bIPv6PoolUsedPrefixLow':bIPv6PoolUsedPrefixLow,'bIPv6PoolUsedPrefixHigh':bIPv6PoolUsedPrefixHigh,'bIPPoolAddrExhausted':bIPPoolAddrExhausted,'bIPv6PoolPrefixExhausted':bIPv6PoolPrefixExhausted,'bIPv4PoolMIBObjects':bIPv4PoolMIBObjects,'bIPPoolTable':bIPPoolTable,'bIPPoolEntry':bIPPoolEntry,_I:bIPPoolStatsInterval,_J:bIPPoolIndex,'bIPPoolIntervalDuration':bIPPoolIntervalDuration,_E:bIPPoolName,'bIPPoolStartAddress':bIPPoolStartAddress,'bIPPoolEndAddress':bIPPoolEndAddress,_F:bIPPoolTotalAddresses,'bIPPoolReservedAddresses':bIPPoolReservedAddresses,'bIPPoolPeakFreeAddresses':bIPPoolPeakFreeAddresses,'bIPPoolPeakUsedAddresses':bIPPoolPeakUsedAddresses,_U:bIPPoolUsedAddrLowThreshold,_V:bIPPoolUsedAddrHighThreshold,'bIPPoolGrpName':bIPPoolGrpName,'bIPPoolGroupTable':bIPPoolGroupTable,'bIPPoolGroupEntry':bIPPoolGroupEntry,_K:bIPPoolGroupStatsInterval,_L:bIPPoolGroupIndex,'bIPPoolGroupIntervalDuration':bIPPoolGroupIntervalDuration,'bIPPoolGroupName':bIPPoolGroupName,'bIPPoolGroupTotalAddresses':bIPPoolGroupTotalAddresses,'bIPPoolGroupReservedAddresses':bIPPoolGroupReservedAddresses,'bIPPoolGroupPeakFreeAddresses':bIPPoolGroupPeakFreeAddresses,'bIPPoolGroupPeakUsedAddresses':bIPPoolGroupPeakUsedAddresses,'bIPPoolGlobalTable':bIPPoolGlobalTable,'bIPPoolGlobalEntry':bIPPoolGlobalEntry,_M:bIPPoolGlobalStatsInterval,_N:bIPPoolClientIndex,'bIPPoolClientName':bIPPoolClientName,'bIPPoolGlobalAllocReq':bIPPoolGlobalAllocReq,'bIPPoolGlobalAllocReqSucc':bIPPoolGlobalAllocReqSucc,'bIPPoolGlobalAllocReqUnSucc':bIPPoolGlobalAllocReqUnSucc,'bIPPoolGlobalDupAllocReq':bIPPoolGlobalDupAllocReq,'bIPPoolGlobalStaticAllocReq':bIPPoolGlobalStaticAllocReq,'bIPPoolGlobalAllocResponses':bIPPoolGlobalAllocResponses,'bIPPoolGlobalDeAllocReq':bIPPoolGlobalDeAllocReq,'bIPPoolGlobalDeAllocReqSucc':bIPPoolGlobalDeAllocReqSucc,'bIPPoolGlobalDeAllocReqUnSucc':bIPPoolGlobalDeAllocReqUnSucc,'bIPPoolGlobalInvalidReq':bIPPoolGlobalInvalidReq,'bIPPoolGlobalNotAvailCount':bIPPoolGlobalNotAvailCount,'bIPPoolGlobalPoolExhaustedCount':bIPPoolGlobalPoolExhaustedCount,'bIPPoolGlobalGroupExhaustedCount':bIPPoolGlobalGroupExhaustedCount,'bIPPoolGlobalInvalidPoolNameCount':bIPPoolGlobalInvalidPoolNameCount,'bIPPoolGlobalInvalidGroupNameCount':bIPPoolGlobalInvalidGroupNameCount,'bIPPoolGlobalInvalidIPAddrCount':bIPPoolGlobalInvalidIPAddrCount,'bIPPoolGlobalHashInsertFail':bIPPoolGlobalHashInsertFail,'bIPPoolGlobalHashDeleteFail':bIPPoolGlobalHashDeleteFail,'bIPPoolGlobalRequestedAllocatedMismacth':bIPPoolGlobalRequestedAllocatedMismacth,'bIPPoolGlobalRequestedIPNotFree':bIPPoolGlobalRequestedIPNotFree,'bIPPoolGlobalGenErrCount':bIPPoolGlobalGenErrCount,'bIPPoolGlobalAddrRelDueToIntAdd':bIPPoolGlobalAddrRelDueToIntAdd,'bIPPoolGlobalGroupDeAllocReq':bIPPoolGlobalGroupDeAllocReq,'bIPPoolGlobalGroupDeAllocReqSucc':bIPPoolGlobalGroupDeAllocReqSucc,'bIPPoolGlobalGroupDeAllocReqUnSucc':bIPPoolGlobalGroupDeAllocReqUnSucc,'bIPPoolTotalPoolCreatedEvents':bIPPoolTotalPoolCreatedEvents,'bIPPoolTotalPoolDeletedEvents':bIPPoolTotalPoolDeletedEvents,'bIPPoolGlobalIntervalDuration':bIPPoolGlobalIntervalDuration,'bIPv4PoolNotifObjects':bIPv4PoolNotifObjects,'bIPv6PoolMIBObjects':bIPv6PoolMIBObjects,'bIPv6PoolTable':bIPv6PoolTable,'bIPv6PoolEntry':bIPv6PoolEntry,_O:bIPv6PoolStatsInterval,_P:bIPv6PoolIndex,'bIPv6PoolIntervalDuration':bIPv6PoolIntervalDuration,_G:bIPv6PoolName,'bIPv6PoolStartPrefix':bIPv6PoolStartPrefix,'bIPv6PoolEndPrefix':bIPv6PoolEndPrefix,_H:bIPv6PoolTotalPrefixes,'bIPv6PoolReservedPrefixes':bIPv6PoolReservedPrefixes,'bIPv6PoolPeakFreePrefixes':bIPv6PoolPeakFreePrefixes,'bIPv6PoolPeakUsedPrefixes':bIPv6PoolPeakUsedPrefixes,_W:bIPv6PoolUsedPrefixLowThreshold,_X:bIPv6PoolUsedPrefixHighThreshold,'bIPv6PoolGrpName':bIPv6PoolGrpName,'bIPv6PoolGroupTable':bIPv6PoolGroupTable,'bIPv6PoolGroupEntry':bIPv6PoolGroupEntry,_Q:bIPv6PoolGroupStatsInterval,_R:bIPv6PoolGroupIndex,'bIPv6PoolGroupIntervalDuration':bIPv6PoolGroupIntervalDuration,'bIPv6PoolGroupName':bIPv6PoolGroupName,'bIPv6PoolGroupTotalPrefixes':bIPv6PoolGroupTotalPrefixes,'bIPv6PoolGroupReservedPrefixes':bIPv6PoolGroupReservedPrefixes,'bIPv6PoolGroupPeakFreePrefixes':bIPv6PoolGroupPeakFreePrefixes,'bIPv6PoolGroupPeakUsedPrefixes':bIPv6PoolGroupPeakUsedPrefixes,'bIPv6PoolGlobalTable':bIPv6PoolGlobalTable,'bIPv6PoolGlobalEntry':bIPv6PoolGlobalEntry,_S:bIPv6PoolGlobalStatsInterval,_T:bIPv6PoolClientIndex,'bIPv6PoolClientName':bIPv6PoolClientName,'bIPv6PoolGlobalAllocReq':bIPv6PoolGlobalAllocReq,'bIPv6PoolGlobalAllocReqSucc':bIPv6PoolGlobalAllocReqSucc,'bIPv6PoolGlobalAllocReqUnSucc':bIPv6PoolGlobalAllocReqUnSucc,'bIPv6PoolGlobalDupAllocReq':bIPv6PoolGlobalDupAllocReq,'bIPv6PoolGlobalStaticAllocReq':bIPv6PoolGlobalStaticAllocReq,'bIPv6PoolGlobalAllocResponses':bIPv6PoolGlobalAllocResponses,'bIPv6PoolGlobalDeAllocReq':bIPv6PoolGlobalDeAllocReq,'bIPv6PoolGlobalDeAllocReqSucc':bIPv6PoolGlobalDeAllocReqSucc,'bIPv6PoolGlobalDeAllocReqUnSucc':bIPv6PoolGlobalDeAllocReqUnSucc,'bIPv6PoolGlobalInvalidReq':bIPv6PoolGlobalInvalidReq,'bIPv6PoolGlobalNotAvailCount':bIPv6PoolGlobalNotAvailCount,'bIPv6PoolGlobalPoolExhaustedCount':bIPv6PoolGlobalPoolExhaustedCount,'bIPv6PoolGlobalGroupExhaustedCount':bIPv6PoolGlobalGroupExhaustedCount,'bIPv6PoolGlobalInvalidPoolNameCount':bIPv6PoolGlobalInvalidPoolNameCount,'bIPv6PoolGlobalInvalidGroupNameCount':bIPv6PoolGlobalInvalidGroupNameCount,'bIPv6PoolGlobalInvalidIPAddrCount':bIPv6PoolGlobalInvalidIPAddrCount,'bIPv6PoolGlobalHashInsertFail':bIPv6PoolGlobalHashInsertFail,'bIPv6PoolGlobalHashDeleteFail':bIPv6PoolGlobalHashDeleteFail,'bIPv6PoolGlobalRequestedAllocatedMismacth':bIPv6PoolGlobalRequestedAllocatedMismacth,'bIPv6PoolGlobalRequestedIPNotFree':bIPv6PoolGlobalRequestedIPNotFree,'bIPv6PoolGlobalGenErrCount':bIPv6PoolGlobalGenErrCount,'bIPv6PoolGlobalPrefixRelDueToIntAdd':bIPv6PoolGlobalPrefixRelDueToIntAdd,'bIPv6PoolTotalPoolCreatedEvents':bIPv6PoolTotalPoolCreatedEvents,'bIPv6PoolTotalPoolDeletedEvents':bIPv6PoolTotalPoolDeletedEvents,'bIPv6PoolGlobalIntervalDuration':bIPv6PoolGlobalIntervalDuration,'bIPv6PoolNotifObjects':bIPv6PoolNotifObjects})