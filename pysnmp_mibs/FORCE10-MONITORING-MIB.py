_a='f10CpuIngUnicastQueueId'
_Z='f10CpuIngUnicastDestCpu'
_Y='f10CpuIngUnicastSrcPortPipe'
_X='f10CpuIngUnicastSrcCard'
_W='f10EgMulticastQueueId'
_V='f10EgUnicastQueueId'
_U='f10IngMulticastQueueId'
_T='f10IngMulticastSrcPortPipe'
_S='f10IngMulticastSrcCard'
_R='f10IngUnicastQueueId'
_Q='f10IngUnicastDestPortPipe'
_P='f10IngUnicastSrcPortPipe'
_O='f10IngUnicastDestCard'
_N='f10IngUnicastSrcCard'
_M='f10MacAccMacAddr'
_L='f10MacAccVlan'
_K='f10MacAccInIfIndex'
_J='f10WredQueueId'
_I='f10OutQueueId'
_H='f10InQueueId'
_G='Integer32'
_F='not-accessible'
_E='ifIndex'
_D='IF-MIB'
_C='FORCE10-MONITORING-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
f10Mgmt,=mibBuilder.importSymbols('FORCE10-SMI','f10Mgmt')
F10CycloneVersion,F10PortPipeID,F10ProcessorModuleType,F10QueueID,F10SlotID,F10VlanID=mibBuilder.importSymbols('FORCE10-TC','F10CycloneVersion','F10PortPipeID','F10ProcessorModuleType','F10QueueID','F10SlotID','F10VlanID')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
f10MonitoringMib=ModuleIdentity((1,3,6,1,4,1,6027,3,3))
if mibBuilder.loadTexts:f10MonitoringMib.setRevisions(('2008-12-18 12:00','1906-01-20 00:00','2000-11-02 10:30'))
_F10MonGroup_ObjectIdentity=ObjectIdentity
f10MonGroup=_F10MonGroup_ObjectIdentity((1,3,6,1,4,1,6027,3,3,1))
class _F10MonMibVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('version1',1),('version1dot1',2),('version1dot2',3)))
_F10MonMibVersion_Type.__name__=_G
_F10MonMibVersion_Object=MibScalar
f10MonMibVersion=_F10MonMibVersion_Object((1,3,6,1,4,1,6027,3,3,1,1),_F10MonMibVersion_Type())
f10MonMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:f10MonMibVersion.setStatus(_A)
_F10MonQueue_ObjectIdentity=ObjectIdentity
f10MonQueue=_F10MonQueue_ObjectIdentity((1,3,6,1,4,1,6027,3,3,2))
_F10MonQueueGroup_ObjectIdentity=ObjectIdentity
f10MonQueueGroup=_F10MonQueueGroup_ObjectIdentity((1,3,6,1,4,1,6027,3,3,2,1))
_F10MonMaxQueue_Type=Integer32
_F10MonMaxQueue_Object=MibScalar
f10MonMaxQueue=_F10MonMaxQueue_Object((1,3,6,1,4,1,6027,3,3,2,1,1),_F10MonMaxQueue_Type())
f10MonMaxQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:f10MonMaxQueue.setStatus(_A)
_F10InQueueStatisticsTable_Object=MibTable
f10InQueueStatisticsTable=_F10InQueueStatisticsTable_Object((1,3,6,1,4,1,6027,3,3,2,2))
if mibBuilder.loadTexts:f10InQueueStatisticsTable.setStatus(_A)
_F10InQueueStatisticsEntry_Object=MibTableRow
f10InQueueStatisticsEntry=_F10InQueueStatisticsEntry_Object((1,3,6,1,4,1,6027,3,3,2,2,1))
f10InQueueStatisticsEntry.setIndexNames((0,_D,_E),(0,_C,_H))
if mibBuilder.loadTexts:f10InQueueStatisticsEntry.setStatus(_A)
_F10InQueueId_Type=F10QueueID
_F10InQueueId_Object=MibTableColumn
f10InQueueId=_F10InQueueId_Object((1,3,6,1,4,1,6027,3,3,2,2,1,1),_F10InQueueId_Type())
f10InQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:f10InQueueId.setStatus(_A)
_F10InQueueDropPackets_Type=Counter64
_F10InQueueDropPackets_Object=MibTableColumn
f10InQueueDropPackets=_F10InQueueDropPackets_Object((1,3,6,1,4,1,6027,3,3,2,2,1,2),_F10InQueueDropPackets_Type())
f10InQueueDropPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:f10InQueueDropPackets.setStatus(_A)
_F10InQueueBytes_Type=Counter64
_F10InQueueBytes_Object=MibTableColumn
f10InQueueBytes=_F10InQueueBytes_Object((1,3,6,1,4,1,6027,3,3,2,2,1,3),_F10InQueueBytes_Type())
f10InQueueBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:f10InQueueBytes.setStatus(_A)
_F10InQueueMatchPackets_Type=Counter64
_F10InQueueMatchPackets_Object=MibTableColumn
f10InQueueMatchPackets=_F10InQueueMatchPackets_Object((1,3,6,1,4,1,6027,3,3,2,2,1,4),_F10InQueueMatchPackets_Type())
f10InQueueMatchPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:f10InQueueMatchPackets.setStatus(_A)
_F10InQueueMatchBytes_Type=Counter64
_F10InQueueMatchBytes_Object=MibTableColumn
f10InQueueMatchBytes=_F10InQueueMatchBytes_Object((1,3,6,1,4,1,6027,3,3,2,2,1,5),_F10InQueueMatchBytes_Type())
f10InQueueMatchBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:f10InQueueMatchBytes.setStatus(_A)
_F10InQueueMatchBps_Type=Counter64
_F10InQueueMatchBps_Object=MibTableColumn
f10InQueueMatchBps=_F10InQueueMatchBps_Object((1,3,6,1,4,1,6027,3,3,2,2,1,6),_F10InQueueMatchBps_Type())
f10InQueueMatchBps.setMaxAccess(_B)
if mibBuilder.loadTexts:f10InQueueMatchBps.setStatus(_A)
_F10InQueueCycloneVersion_Type=F10CycloneVersion
_F10InQueueCycloneVersion_Object=MibTableColumn
f10InQueueCycloneVersion=_F10InQueueCycloneVersion_Object((1,3,6,1,4,1,6027,3,3,2,2,1,7),_F10InQueueCycloneVersion_Type())
f10InQueueCycloneVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:f10InQueueCycloneVersion.setStatus(_A)
_F10InQueueBytesCount_Type=Counter64
_F10InQueueBytesCount_Object=MibTableColumn
f10InQueueBytesCount=_F10InQueueBytesCount_Object((1,3,6,1,4,1,6027,3,3,2,2,1,8),_F10InQueueBytesCount_Type())
f10InQueueBytesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:f10InQueueBytesCount.setStatus(_A)
_F10InQueuePktsCount_Type=Counter64
_F10InQueuePktsCount_Object=MibTableColumn
f10InQueuePktsCount=_F10InQueuePktsCount_Object((1,3,6,1,4,1,6027,3,3,2,2,1,9),_F10InQueuePktsCount_Type())
f10InQueuePktsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:f10InQueuePktsCount.setStatus(_A)
_F10OutQueueStatisticsTable_Object=MibTable
f10OutQueueStatisticsTable=_F10OutQueueStatisticsTable_Object((1,3,6,1,4,1,6027,3,3,2,3))
if mibBuilder.loadTexts:f10OutQueueStatisticsTable.setStatus(_A)
_F10OutQueueStatisticsEntry_Object=MibTableRow
f10OutQueueStatisticsEntry=_F10OutQueueStatisticsEntry_Object((1,3,6,1,4,1,6027,3,3,2,3,1))
f10OutQueueStatisticsEntry.setIndexNames((0,_D,_E),(0,_C,_I))
if mibBuilder.loadTexts:f10OutQueueStatisticsEntry.setStatus(_A)
_F10OutQueueId_Type=F10QueueID
_F10OutQueueId_Object=MibTableColumn
f10OutQueueId=_F10OutQueueId_Object((1,3,6,1,4,1,6027,3,3,2,3,1,1),_F10OutQueueId_Type())
f10OutQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:f10OutQueueId.setStatus(_A)
_F10OutQueuePackets_Type=Counter64
_F10OutQueuePackets_Object=MibTableColumn
f10OutQueuePackets=_F10OutQueuePackets_Object((1,3,6,1,4,1,6027,3,3,2,3,1,2),_F10OutQueuePackets_Type())
f10OutQueuePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:f10OutQueuePackets.setStatus(_A)
_F10OutQueueBytes_Type=Counter64
_F10OutQueueBytes_Object=MibTableColumn
f10OutQueueBytes=_F10OutQueueBytes_Object((1,3,6,1,4,1,6027,3,3,2,3,1,3),_F10OutQueueBytes_Type())
f10OutQueueBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:f10OutQueueBytes.setStatus(_A)
_F10OutQueueBps_Type=Counter64
_F10OutQueueBps_Object=MibTableColumn
f10OutQueueBps=_F10OutQueueBps_Object((1,3,6,1,4,1,6027,3,3,2,3,1,4),_F10OutQueueBps_Type())
f10OutQueueBps.setMaxAccess(_B)
if mibBuilder.loadTexts:f10OutQueueBps.setStatus(_A)
_F10OutQueueCycloneVersion_Type=F10CycloneVersion
_F10OutQueueCycloneVersion_Object=MibTableColumn
f10OutQueueCycloneVersion=_F10OutQueueCycloneVersion_Object((1,3,6,1,4,1,6027,3,3,2,3,1,5),_F10OutQueueCycloneVersion_Type())
f10OutQueueCycloneVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:f10OutQueueCycloneVersion.setStatus(_A)
_F10OutQueueBytesCount_Type=Counter64
_F10OutQueueBytesCount_Object=MibTableColumn
f10OutQueueBytesCount=_F10OutQueueBytesCount_Object((1,3,6,1,4,1,6027,3,3,2,3,1,6),_F10OutQueueBytesCount_Type())
f10OutQueueBytesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:f10OutQueueBytesCount.setStatus(_A)
_F10WredStatisticsTable_Object=MibTable
f10WredStatisticsTable=_F10WredStatisticsTable_Object((1,3,6,1,4,1,6027,3,3,2,4))
if mibBuilder.loadTexts:f10WredStatisticsTable.setStatus(_A)
_F10WredStatisticsEntry_Object=MibTableRow
f10WredStatisticsEntry=_F10WredStatisticsEntry_Object((1,3,6,1,4,1,6027,3,3,2,4,1))
f10WredStatisticsEntry.setIndexNames((0,_D,_E),(0,_C,_J))
if mibBuilder.loadTexts:f10WredStatisticsEntry.setStatus(_A)
_F10WredQueueId_Type=F10QueueID
_F10WredQueueId_Object=MibTableColumn
f10WredQueueId=_F10WredQueueId_Object((1,3,6,1,4,1,6027,3,3,2,4,1,1),_F10WredQueueId_Type())
f10WredQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredQueueId.setStatus(_A)
_F10WredGreenName_Type=DisplayString
_F10WredGreenName_Object=MibTableColumn
f10WredGreenName=_F10WredGreenName_Object((1,3,6,1,4,1,6027,3,3,2,4,1,2),_F10WredGreenName_Type())
f10WredGreenName.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredGreenName.setStatus(_A)
_F10WredGreenThresholdLow_Type=Unsigned32
_F10WredGreenThresholdLow_Object=MibTableColumn
f10WredGreenThresholdLow=_F10WredGreenThresholdLow_Object((1,3,6,1,4,1,6027,3,3,2,4,1,3),_F10WredGreenThresholdLow_Type())
f10WredGreenThresholdLow.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredGreenThresholdLow.setStatus(_A)
_F10WredGreenThresholdHigh_Type=Unsigned32
_F10WredGreenThresholdHigh_Object=MibTableColumn
f10WredGreenThresholdHigh=_F10WredGreenThresholdHigh_Object((1,3,6,1,4,1,6027,3,3,2,4,1,4),_F10WredGreenThresholdHigh_Type())
f10WredGreenThresholdHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredGreenThresholdHigh.setStatus(_A)
_F10WredGreenDropPackets_Type=Counter64
_F10WredGreenDropPackets_Object=MibTableColumn
f10WredGreenDropPackets=_F10WredGreenDropPackets_Object((1,3,6,1,4,1,6027,3,3,2,4,1,5),_F10WredGreenDropPackets_Type())
f10WredGreenDropPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredGreenDropPackets.setStatus(_A)
_F10WredGreenReserve1_Type=Counter64
_F10WredGreenReserve1_Object=MibTableColumn
f10WredGreenReserve1=_F10WredGreenReserve1_Object((1,3,6,1,4,1,6027,3,3,2,4,1,6),_F10WredGreenReserve1_Type())
f10WredGreenReserve1.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredGreenReserve1.setStatus(_A)
_F10WredGreenReserve2_Type=Counter64
_F10WredGreenReserve2_Object=MibTableColumn
f10WredGreenReserve2=_F10WredGreenReserve2_Object((1,3,6,1,4,1,6027,3,3,2,4,1,7),_F10WredGreenReserve2_Type())
f10WredGreenReserve2.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredGreenReserve2.setStatus(_A)
_F10WredYellowName_Type=DisplayString
_F10WredYellowName_Object=MibTableColumn
f10WredYellowName=_F10WredYellowName_Object((1,3,6,1,4,1,6027,3,3,2,4,1,8),_F10WredYellowName_Type())
f10WredYellowName.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredYellowName.setStatus(_A)
_F10WredYellowThresholdLow_Type=Unsigned32
_F10WredYellowThresholdLow_Object=MibTableColumn
f10WredYellowThresholdLow=_F10WredYellowThresholdLow_Object((1,3,6,1,4,1,6027,3,3,2,4,1,9),_F10WredYellowThresholdLow_Type())
f10WredYellowThresholdLow.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredYellowThresholdLow.setStatus(_A)
_F10WredYellowThresholdHigh_Type=Unsigned32
_F10WredYellowThresholdHigh_Object=MibTableColumn
f10WredYellowThresholdHigh=_F10WredYellowThresholdHigh_Object((1,3,6,1,4,1,6027,3,3,2,4,1,10),_F10WredYellowThresholdHigh_Type())
f10WredYellowThresholdHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredYellowThresholdHigh.setStatus(_A)
_F10WredYellowDropPackets_Type=Counter64
_F10WredYellowDropPackets_Object=MibTableColumn
f10WredYellowDropPackets=_F10WredYellowDropPackets_Object((1,3,6,1,4,1,6027,3,3,2,4,1,11),_F10WredYellowDropPackets_Type())
f10WredYellowDropPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredYellowDropPackets.setStatus(_A)
_F10WredYellowReserve1_Type=Counter64
_F10WredYellowReserve1_Object=MibTableColumn
f10WredYellowReserve1=_F10WredYellowReserve1_Object((1,3,6,1,4,1,6027,3,3,2,4,1,12),_F10WredYellowReserve1_Type())
f10WredYellowReserve1.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredYellowReserve1.setStatus(_A)
_F10WredYellowReserve2_Type=Counter64
_F10WredYellowReserve2_Object=MibTableColumn
f10WredYellowReserve2=_F10WredYellowReserve2_Object((1,3,6,1,4,1,6027,3,3,2,4,1,13),_F10WredYellowReserve2_Type())
f10WredYellowReserve2.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredYellowReserve2.setStatus(_A)
_F10WredRedName_Type=DisplayString
_F10WredRedName_Object=MibTableColumn
f10WredRedName=_F10WredRedName_Object((1,3,6,1,4,1,6027,3,3,2,4,1,14),_F10WredRedName_Type())
f10WredRedName.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredRedName.setStatus(_A)
_F10WredRedThresholdLow_Type=Unsigned32
_F10WredRedThresholdLow_Object=MibTableColumn
f10WredRedThresholdLow=_F10WredRedThresholdLow_Object((1,3,6,1,4,1,6027,3,3,2,4,1,15),_F10WredRedThresholdLow_Type())
f10WredRedThresholdLow.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredRedThresholdLow.setStatus(_A)
_F10WredRedThresholdHigh_Type=Unsigned32
_F10WredRedThresholdHigh_Object=MibTableColumn
f10WredRedThresholdHigh=_F10WredRedThresholdHigh_Object((1,3,6,1,4,1,6027,3,3,2,4,1,16),_F10WredRedThresholdHigh_Type())
f10WredRedThresholdHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredRedThresholdHigh.setStatus(_A)
_F10WredRedDropPackets_Type=Counter64
_F10WredRedDropPackets_Object=MibTableColumn
f10WredRedDropPackets=_F10WredRedDropPackets_Object((1,3,6,1,4,1,6027,3,3,2,4,1,17),_F10WredRedDropPackets_Type())
f10WredRedDropPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredRedDropPackets.setStatus(_A)
_F10WredRedReserve1_Type=Counter64
_F10WredRedReserve1_Object=MibTableColumn
f10WredRedReserve1=_F10WredRedReserve1_Object((1,3,6,1,4,1,6027,3,3,2,4,1,18),_F10WredRedReserve1_Type())
f10WredRedReserve1.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredRedReserve1.setStatus(_A)
_F10WredRedReserve2_Type=Counter64
_F10WredRedReserve2_Object=MibTableColumn
f10WredRedReserve2=_F10WredRedReserve2_Object((1,3,6,1,4,1,6027,3,3,2,4,1,19),_F10WredRedReserve2_Type())
f10WredRedReserve2.setMaxAccess(_B)
if mibBuilder.loadTexts:f10WredRedReserve2.setStatus(_A)
_F10MonMac_ObjectIdentity=ObjectIdentity
f10MonMac=_F10MonMac_ObjectIdentity((1,3,6,1,4,1,6027,3,3,3))
_F10MacGroup_ObjectIdentity=ObjectIdentity
f10MacGroup=_F10MacGroup_ObjectIdentity((1,3,6,1,4,1,6027,3,3,3,1))
_F10MacAccounting_ObjectIdentity=ObjectIdentity
f10MacAccounting=_F10MacAccounting_ObjectIdentity((1,3,6,1,4,1,6027,3,3,3,2))
_F10MacAccountingDestTable_Object=MibTable
f10MacAccountingDestTable=_F10MacAccountingDestTable_Object((1,3,6,1,4,1,6027,3,3,3,2,1))
if mibBuilder.loadTexts:f10MacAccountingDestTable.setStatus(_A)
_F10MacAccountingDestEntry_Object=MibTableRow
f10MacAccountingDestEntry=_F10MacAccountingDestEntry_Object((1,3,6,1,4,1,6027,3,3,3,2,1,1))
f10MacAccountingDestEntry.setIndexNames((0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:f10MacAccountingDestEntry.setStatus(_A)
_F10MacAccInIfIndex_Type=Integer32
_F10MacAccInIfIndex_Object=MibTableColumn
f10MacAccInIfIndex=_F10MacAccInIfIndex_Object((1,3,6,1,4,1,6027,3,3,3,2,1,1,1),_F10MacAccInIfIndex_Type())
f10MacAccInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:f10MacAccInIfIndex.setStatus(_A)
_F10MacAccVlan_Type=F10VlanID
_F10MacAccVlan_Object=MibTableColumn
f10MacAccVlan=_F10MacAccVlan_Object((1,3,6,1,4,1,6027,3,3,3,2,1,1,2),_F10MacAccVlan_Type())
f10MacAccVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:f10MacAccVlan.setStatus(_A)
_F10MacAccMacAddr_Type=MacAddress
_F10MacAccMacAddr_Object=MibTableColumn
f10MacAccMacAddr=_F10MacAccMacAddr_Object((1,3,6,1,4,1,6027,3,3,3,2,1,1,3),_F10MacAccMacAddr_Type())
f10MacAccMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:f10MacAccMacAddr.setStatus(_A)
_F10MacAccOutIfIndex_Type=Integer32
_F10MacAccOutIfIndex_Object=MibTableColumn
f10MacAccOutIfIndex=_F10MacAccOutIfIndex_Object((1,3,6,1,4,1,6027,3,3,3,2,1,1,4),_F10MacAccOutIfIndex_Type())
f10MacAccOutIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:f10MacAccOutIfIndex.setStatus(_A)
_F10MacAccPackets_Type=Counter64
_F10MacAccPackets_Object=MibTableColumn
f10MacAccPackets=_F10MacAccPackets_Object((1,3,6,1,4,1,6027,3,3,3,2,1,1,5),_F10MacAccPackets_Type())
f10MacAccPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:f10MacAccPackets.setStatus(_A)
_F10MacAccBytes_Type=Counter64
_F10MacAccBytes_Object=MibTableColumn
f10MacAccBytes=_F10MacAccBytes_Object((1,3,6,1,4,1,6027,3,3,3,2,1,1,6),_F10MacAccBytes_Type())
f10MacAccBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:f10MacAccBytes.setStatus(_A)
_F10MonIfQueue_ObjectIdentity=ObjectIdentity
f10MonIfQueue=_F10MonIfQueue_ObjectIdentity((1,3,6,1,4,1,6027,3,3,4))
_F10MonIfQueueGroup_ObjectIdentity=ObjectIdentity
f10MonIfQueueGroup=_F10MonIfQueueGroup_ObjectIdentity((1,3,6,1,4,1,6027,3,3,4,1))
_F10IngQueueUnicastStatTable_Object=MibTable
f10IngQueueUnicastStatTable=_F10IngQueueUnicastStatTable_Object((1,3,6,1,4,1,6027,3,3,4,2))
if mibBuilder.loadTexts:f10IngQueueUnicastStatTable.setStatus(_A)
_F10IngQueueUnicastStatEntry_Object=MibTableRow
f10IngQueueUnicastStatEntry=_F10IngQueueUnicastStatEntry_Object((1,3,6,1,4,1,6027,3,3,4,2,1))
f10IngQueueUnicastStatEntry.setIndexNames((0,_C,_N),(0,_C,_O),(0,_C,_P),(0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:f10IngQueueUnicastStatEntry.setStatus(_A)
_F10IngUnicastSrcCard_Type=F10SlotID
_F10IngUnicastSrcCard_Object=MibTableColumn
f10IngUnicastSrcCard=_F10IngUnicastSrcCard_Object((1,3,6,1,4,1,6027,3,3,4,2,1,1),_F10IngUnicastSrcCard_Type())
f10IngUnicastSrcCard.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastSrcCard.setStatus(_A)
_F10IngUnicastDestCard_Type=F10SlotID
_F10IngUnicastDestCard_Object=MibTableColumn
f10IngUnicastDestCard=_F10IngUnicastDestCard_Object((1,3,6,1,4,1,6027,3,3,4,2,1,2),_F10IngUnicastDestCard_Type())
f10IngUnicastDestCard.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastDestCard.setStatus(_A)
_F10IngUnicastSrcPortPipe_Type=F10PortPipeID
_F10IngUnicastSrcPortPipe_Object=MibTableColumn
f10IngUnicastSrcPortPipe=_F10IngUnicastSrcPortPipe_Object((1,3,6,1,4,1,6027,3,3,4,2,1,3),_F10IngUnicastSrcPortPipe_Type())
f10IngUnicastSrcPortPipe.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastSrcPortPipe.setStatus(_A)
_F10IngUnicastDestPortPipe_Type=F10PortPipeID
_F10IngUnicastDestPortPipe_Object=MibTableColumn
f10IngUnicastDestPortPipe=_F10IngUnicastDestPortPipe_Object((1,3,6,1,4,1,6027,3,3,4,2,1,4),_F10IngUnicastDestPortPipe_Type())
f10IngUnicastDestPortPipe.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastDestPortPipe.setStatus(_A)
_F10IngUnicastQueueId_Type=F10QueueID
_F10IngUnicastQueueId_Object=MibTableColumn
f10IngUnicastQueueId=_F10IngUnicastQueueId_Object((1,3,6,1,4,1,6027,3,3,4,2,1,5),_F10IngUnicastQueueId_Type())
f10IngUnicastQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastQueueId.setStatus(_A)
_F10IngUnicastCycloneVersion_Type=F10CycloneVersion
_F10IngUnicastCycloneVersion_Object=MibTableColumn
f10IngUnicastCycloneVersion=_F10IngUnicastCycloneVersion_Object((1,3,6,1,4,1,6027,3,3,4,2,1,6),_F10IngUnicastCycloneVersion_Type())
f10IngUnicastCycloneVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastCycloneVersion.setStatus(_A)
_F10IngUnicastBytes_Type=Counter64
_F10IngUnicastBytes_Object=MibTableColumn
f10IngUnicastBytes=_F10IngUnicastBytes_Object((1,3,6,1,4,1,6027,3,3,4,2,1,7),_F10IngUnicastBytes_Type())
f10IngUnicastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastBytes.setStatus(_A)
_F10IngUnicastBytesCount_Type=Counter64
_F10IngUnicastBytesCount_Object=MibTableColumn
f10IngUnicastBytesCount=_F10IngUnicastBytesCount_Object((1,3,6,1,4,1,6027,3,3,4,2,1,8),_F10IngUnicastBytesCount_Type())
f10IngUnicastBytesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastBytesCount.setStatus(_A)
_F10IngUnicastPacketCount_Type=Counter64
_F10IngUnicastPacketCount_Object=MibTableColumn
f10IngUnicastPacketCount=_F10IngUnicastPacketCount_Object((1,3,6,1,4,1,6027,3,3,4,2,1,9),_F10IngUnicastPacketCount_Type())
f10IngUnicastPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastPacketCount.setStatus(_A)
_F10IngUnicastGreenMin_Type=Unsigned32
_F10IngUnicastGreenMin_Object=MibTableColumn
f10IngUnicastGreenMin=_F10IngUnicastGreenMin_Object((1,3,6,1,4,1,6027,3,3,4,2,1,10),_F10IngUnicastGreenMin_Type())
f10IngUnicastGreenMin.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastGreenMin.setStatus(_A)
_F10IngUnicastGreenMax_Type=Unsigned32
_F10IngUnicastGreenMax_Object=MibTableColumn
f10IngUnicastGreenMax=_F10IngUnicastGreenMax_Object((1,3,6,1,4,1,6027,3,3,4,2,1,11),_F10IngUnicastGreenMax_Type())
f10IngUnicastGreenMax.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastGreenMax.setStatus(_A)
_F10IngUnicastGreenDrop_Type=Counter64
_F10IngUnicastGreenDrop_Object=MibTableColumn
f10IngUnicastGreenDrop=_F10IngUnicastGreenDrop_Object((1,3,6,1,4,1,6027,3,3,4,2,1,12),_F10IngUnicastGreenDrop_Type())
f10IngUnicastGreenDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastGreenDrop.setStatus(_A)
_F10IngUnicastYellowMin_Type=Unsigned32
_F10IngUnicastYellowMin_Object=MibTableColumn
f10IngUnicastYellowMin=_F10IngUnicastYellowMin_Object((1,3,6,1,4,1,6027,3,3,4,2,1,13),_F10IngUnicastYellowMin_Type())
f10IngUnicastYellowMin.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastYellowMin.setStatus(_A)
_F10IngUnicastYellowMax_Type=Unsigned32
_F10IngUnicastYellowMax_Object=MibTableColumn
f10IngUnicastYellowMax=_F10IngUnicastYellowMax_Object((1,3,6,1,4,1,6027,3,3,4,2,1,14),_F10IngUnicastYellowMax_Type())
f10IngUnicastYellowMax.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastYellowMax.setStatus(_A)
_F10IngUnicastYellowDrop_Type=Counter64
_F10IngUnicastYellowDrop_Object=MibTableColumn
f10IngUnicastYellowDrop=_F10IngUnicastYellowDrop_Object((1,3,6,1,4,1,6027,3,3,4,2,1,15),_F10IngUnicastYellowDrop_Type())
f10IngUnicastYellowDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastYellowDrop.setStatus(_A)
_F10IngUnicastRedDrop_Type=Counter64
_F10IngUnicastRedDrop_Object=MibTableColumn
f10IngUnicastRedDrop=_F10IngUnicastRedDrop_Object((1,3,6,1,4,1,6027,3,3,4,2,1,16),_F10IngUnicastRedDrop_Type())
f10IngUnicastRedDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngUnicastRedDrop.setStatus(_A)
_F10IngQueueMulticastStatTable_Object=MibTable
f10IngQueueMulticastStatTable=_F10IngQueueMulticastStatTable_Object((1,3,6,1,4,1,6027,3,3,4,3))
if mibBuilder.loadTexts:f10IngQueueMulticastStatTable.setStatus(_A)
_F10IngQueueMulticastStatEntry_Object=MibTableRow
f10IngQueueMulticastStatEntry=_F10IngQueueMulticastStatEntry_Object((1,3,6,1,4,1,6027,3,3,4,3,1))
f10IngQueueMulticastStatEntry.setIndexNames((0,_C,_S),(0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:f10IngQueueMulticastStatEntry.setStatus(_A)
_F10IngMulticastSrcCard_Type=F10SlotID
_F10IngMulticastSrcCard_Object=MibTableColumn
f10IngMulticastSrcCard=_F10IngMulticastSrcCard_Object((1,3,6,1,4,1,6027,3,3,4,3,1,1),_F10IngMulticastSrcCard_Type())
f10IngMulticastSrcCard.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastSrcCard.setStatus(_A)
_F10IngMulticastSrcPortPipe_Type=F10PortPipeID
_F10IngMulticastSrcPortPipe_Object=MibTableColumn
f10IngMulticastSrcPortPipe=_F10IngMulticastSrcPortPipe_Object((1,3,6,1,4,1,6027,3,3,4,3,1,2),_F10IngMulticastSrcPortPipe_Type())
f10IngMulticastSrcPortPipe.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastSrcPortPipe.setStatus(_A)
_F10IngMulticastQueueId_Type=F10QueueID
_F10IngMulticastQueueId_Object=MibTableColumn
f10IngMulticastQueueId=_F10IngMulticastQueueId_Object((1,3,6,1,4,1,6027,3,3,4,3,1,3),_F10IngMulticastQueueId_Type())
f10IngMulticastQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastQueueId.setStatus(_A)
_F10IngMulticastCycloneVersion_Type=F10CycloneVersion
_F10IngMulticastCycloneVersion_Object=MibTableColumn
f10IngMulticastCycloneVersion=_F10IngMulticastCycloneVersion_Object((1,3,6,1,4,1,6027,3,3,4,3,1,4),_F10IngMulticastCycloneVersion_Type())
f10IngMulticastCycloneVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastCycloneVersion.setStatus(_A)
_F10IngMulticastBytes_Type=Counter64
_F10IngMulticastBytes_Object=MibTableColumn
f10IngMulticastBytes=_F10IngMulticastBytes_Object((1,3,6,1,4,1,6027,3,3,4,3,1,5),_F10IngMulticastBytes_Type())
f10IngMulticastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastBytes.setStatus(_A)
_F10IngMulticastBytesCount_Type=Counter64
_F10IngMulticastBytesCount_Object=MibTableColumn
f10IngMulticastBytesCount=_F10IngMulticastBytesCount_Object((1,3,6,1,4,1,6027,3,3,4,3,1,6),_F10IngMulticastBytesCount_Type())
f10IngMulticastBytesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastBytesCount.setStatus(_A)
_F10IngMulticastPacketCount_Type=Counter64
_F10IngMulticastPacketCount_Object=MibTableColumn
f10IngMulticastPacketCount=_F10IngMulticastPacketCount_Object((1,3,6,1,4,1,6027,3,3,4,3,1,7),_F10IngMulticastPacketCount_Type())
f10IngMulticastPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastPacketCount.setStatus(_A)
_F10IngMulticastGreenMin_Type=Unsigned32
_F10IngMulticastGreenMin_Object=MibTableColumn
f10IngMulticastGreenMin=_F10IngMulticastGreenMin_Object((1,3,6,1,4,1,6027,3,3,4,3,1,8),_F10IngMulticastGreenMin_Type())
f10IngMulticastGreenMin.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastGreenMin.setStatus(_A)
_F10IngMulticastGreenMax_Type=Unsigned32
_F10IngMulticastGreenMax_Object=MibTableColumn
f10IngMulticastGreenMax=_F10IngMulticastGreenMax_Object((1,3,6,1,4,1,6027,3,3,4,3,1,9),_F10IngMulticastGreenMax_Type())
f10IngMulticastGreenMax.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastGreenMax.setStatus(_A)
_F10IngMulticastGreenDrop_Type=Counter64
_F10IngMulticastGreenDrop_Object=MibTableColumn
f10IngMulticastGreenDrop=_F10IngMulticastGreenDrop_Object((1,3,6,1,4,1,6027,3,3,4,3,1,10),_F10IngMulticastGreenDrop_Type())
f10IngMulticastGreenDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastGreenDrop.setStatus(_A)
_F10IngMulticastYellowMin_Type=Unsigned32
_F10IngMulticastYellowMin_Object=MibTableColumn
f10IngMulticastYellowMin=_F10IngMulticastYellowMin_Object((1,3,6,1,4,1,6027,3,3,4,3,1,11),_F10IngMulticastYellowMin_Type())
f10IngMulticastYellowMin.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastYellowMin.setStatus(_A)
_F10IngMulticastYellowMax_Type=Unsigned32
_F10IngMulticastYellowMax_Object=MibTableColumn
f10IngMulticastYellowMax=_F10IngMulticastYellowMax_Object((1,3,6,1,4,1,6027,3,3,4,3,1,12),_F10IngMulticastYellowMax_Type())
f10IngMulticastYellowMax.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastYellowMax.setStatus(_A)
_F10IngMulticastYellowDrop_Type=Counter64
_F10IngMulticastYellowDrop_Object=MibTableColumn
f10IngMulticastYellowDrop=_F10IngMulticastYellowDrop_Object((1,3,6,1,4,1,6027,3,3,4,3,1,13),_F10IngMulticastYellowDrop_Type())
f10IngMulticastYellowDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastYellowDrop.setStatus(_A)
_F10IngMulticastRedDrop_Type=Counter64
_F10IngMulticastRedDrop_Object=MibTableColumn
f10IngMulticastRedDrop=_F10IngMulticastRedDrop_Object((1,3,6,1,4,1,6027,3,3,4,3,1,14),_F10IngMulticastRedDrop_Type())
f10IngMulticastRedDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10IngMulticastRedDrop.setStatus(_A)
_F10EgQueueUnicastStatTable_Object=MibTable
f10EgQueueUnicastStatTable=_F10EgQueueUnicastStatTable_Object((1,3,6,1,4,1,6027,3,3,4,4))
if mibBuilder.loadTexts:f10EgQueueUnicastStatTable.setStatus(_A)
_F10EgQueueUnicastStatEntry_Object=MibTableRow
f10EgQueueUnicastStatEntry=_F10EgQueueUnicastStatEntry_Object((1,3,6,1,4,1,6027,3,3,4,4,1))
f10EgQueueUnicastStatEntry.setIndexNames((0,_D,_E),(0,_C,_V))
if mibBuilder.loadTexts:f10EgQueueUnicastStatEntry.setStatus(_A)
_F10EgUnicastQueueId_Type=F10QueueID
_F10EgUnicastQueueId_Object=MibTableColumn
f10EgUnicastQueueId=_F10EgUnicastQueueId_Object((1,3,6,1,4,1,6027,3,3,4,4,1,1),_F10EgUnicastQueueId_Type())
f10EgUnicastQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgUnicastQueueId.setStatus(_A)
_F10EgUnicastCycloneVersion_Type=F10CycloneVersion
_F10EgUnicastCycloneVersion_Object=MibTableColumn
f10EgUnicastCycloneVersion=_F10EgUnicastCycloneVersion_Object((1,3,6,1,4,1,6027,3,3,4,4,1,2),_F10EgUnicastCycloneVersion_Type())
f10EgUnicastCycloneVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgUnicastCycloneVersion.setStatus(_A)
_F10EgUnicastBytes_Type=Counter64
_F10EgUnicastBytes_Object=MibTableColumn
f10EgUnicastBytes=_F10EgUnicastBytes_Object((1,3,6,1,4,1,6027,3,3,4,4,1,3),_F10EgUnicastBytes_Type())
f10EgUnicastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgUnicastBytes.setStatus(_A)
_F10EgUnicastBytesCount_Type=Counter64
_F10EgUnicastBytesCount_Object=MibTableColumn
f10EgUnicastBytesCount=_F10EgUnicastBytesCount_Object((1,3,6,1,4,1,6027,3,3,4,4,1,4),_F10EgUnicastBytesCount_Type())
f10EgUnicastBytesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgUnicastBytesCount.setStatus(_A)
_F10EgUnicastPacketCount_Type=Counter64
_F10EgUnicastPacketCount_Object=MibTableColumn
f10EgUnicastPacketCount=_F10EgUnicastPacketCount_Object((1,3,6,1,4,1,6027,3,3,4,4,1,5),_F10EgUnicastPacketCount_Type())
f10EgUnicastPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgUnicastPacketCount.setStatus(_A)
_F10EgUnicastGreenMin_Type=Unsigned32
_F10EgUnicastGreenMin_Object=MibTableColumn
f10EgUnicastGreenMin=_F10EgUnicastGreenMin_Object((1,3,6,1,4,1,6027,3,3,4,4,1,6),_F10EgUnicastGreenMin_Type())
f10EgUnicastGreenMin.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgUnicastGreenMin.setStatus(_A)
_F10EgUnicastGreenMax_Type=Unsigned32
_F10EgUnicastGreenMax_Object=MibTableColumn
f10EgUnicastGreenMax=_F10EgUnicastGreenMax_Object((1,3,6,1,4,1,6027,3,3,4,4,1,7),_F10EgUnicastGreenMax_Type())
f10EgUnicastGreenMax.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgUnicastGreenMax.setStatus(_A)
_F10EgUnicastGreenDrop_Type=Counter64
_F10EgUnicastGreenDrop_Object=MibTableColumn
f10EgUnicastGreenDrop=_F10EgUnicastGreenDrop_Object((1,3,6,1,4,1,6027,3,3,4,4,1,8),_F10EgUnicastGreenDrop_Type())
f10EgUnicastGreenDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgUnicastGreenDrop.setStatus(_A)
_F10EgUnicastYellowMin_Type=Unsigned32
_F10EgUnicastYellowMin_Object=MibTableColumn
f10EgUnicastYellowMin=_F10EgUnicastYellowMin_Object((1,3,6,1,4,1,6027,3,3,4,4,1,9),_F10EgUnicastYellowMin_Type())
f10EgUnicastYellowMin.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgUnicastYellowMin.setStatus(_A)
_F10EgUnicastYellowMax_Type=Unsigned32
_F10EgUnicastYellowMax_Object=MibTableColumn
f10EgUnicastYellowMax=_F10EgUnicastYellowMax_Object((1,3,6,1,4,1,6027,3,3,4,4,1,10),_F10EgUnicastYellowMax_Type())
f10EgUnicastYellowMax.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgUnicastYellowMax.setStatus(_A)
_F10EgUnicastYellowDrop_Type=Counter64
_F10EgUnicastYellowDrop_Object=MibTableColumn
f10EgUnicastYellowDrop=_F10EgUnicastYellowDrop_Object((1,3,6,1,4,1,6027,3,3,4,4,1,11),_F10EgUnicastYellowDrop_Type())
f10EgUnicastYellowDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgUnicastYellowDrop.setStatus(_A)
_F10EgUnicastRedDrop_Type=Counter64
_F10EgUnicastRedDrop_Object=MibTableColumn
f10EgUnicastRedDrop=_F10EgUnicastRedDrop_Object((1,3,6,1,4,1,6027,3,3,4,4,1,12),_F10EgUnicastRedDrop_Type())
f10EgUnicastRedDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgUnicastRedDrop.setStatus(_A)
_F10EgQueueMulticastStatTable_Object=MibTable
f10EgQueueMulticastStatTable=_F10EgQueueMulticastStatTable_Object((1,3,6,1,4,1,6027,3,3,4,5))
if mibBuilder.loadTexts:f10EgQueueMulticastStatTable.setStatus(_A)
_F10EgQueueMulticastStatEntry_Object=MibTableRow
f10EgQueueMulticastStatEntry=_F10EgQueueMulticastStatEntry_Object((1,3,6,1,4,1,6027,3,3,4,5,1))
f10EgQueueMulticastStatEntry.setIndexNames((0,_D,_E),(0,_C,_W))
if mibBuilder.loadTexts:f10EgQueueMulticastStatEntry.setStatus(_A)
_F10EgMulticastQueueId_Type=F10QueueID
_F10EgMulticastQueueId_Object=MibTableColumn
f10EgMulticastQueueId=_F10EgMulticastQueueId_Object((1,3,6,1,4,1,6027,3,3,4,5,1,1),_F10EgMulticastQueueId_Type())
f10EgMulticastQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgMulticastQueueId.setStatus(_A)
_F10EgMulticastCycloneVersion_Type=F10CycloneVersion
_F10EgMulticastCycloneVersion_Object=MibTableColumn
f10EgMulticastCycloneVersion=_F10EgMulticastCycloneVersion_Object((1,3,6,1,4,1,6027,3,3,4,5,1,2),_F10EgMulticastCycloneVersion_Type())
f10EgMulticastCycloneVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgMulticastCycloneVersion.setStatus(_A)
_F10EgMulticastBytes_Type=Counter64
_F10EgMulticastBytes_Object=MibTableColumn
f10EgMulticastBytes=_F10EgMulticastBytes_Object((1,3,6,1,4,1,6027,3,3,4,5,1,3),_F10EgMulticastBytes_Type())
f10EgMulticastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgMulticastBytes.setStatus(_A)
_F10EgMulticastBytesCount_Type=Counter64
_F10EgMulticastBytesCount_Object=MibTableColumn
f10EgMulticastBytesCount=_F10EgMulticastBytesCount_Object((1,3,6,1,4,1,6027,3,3,4,5,1,4),_F10EgMulticastBytesCount_Type())
f10EgMulticastBytesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgMulticastBytesCount.setStatus(_A)
_F10EgMulticastPacketCount_Type=Counter64
_F10EgMulticastPacketCount_Object=MibTableColumn
f10EgMulticastPacketCount=_F10EgMulticastPacketCount_Object((1,3,6,1,4,1,6027,3,3,4,5,1,5),_F10EgMulticastPacketCount_Type())
f10EgMulticastPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgMulticastPacketCount.setStatus(_A)
_F10EgMulticastGreenMin_Type=Unsigned32
_F10EgMulticastGreenMin_Object=MibTableColumn
f10EgMulticastGreenMin=_F10EgMulticastGreenMin_Object((1,3,6,1,4,1,6027,3,3,4,5,1,6),_F10EgMulticastGreenMin_Type())
f10EgMulticastGreenMin.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgMulticastGreenMin.setStatus(_A)
_F10EgMulticastGreenMax_Type=Unsigned32
_F10EgMulticastGreenMax_Object=MibTableColumn
f10EgMulticastGreenMax=_F10EgMulticastGreenMax_Object((1,3,6,1,4,1,6027,3,3,4,5,1,7),_F10EgMulticastGreenMax_Type())
f10EgMulticastGreenMax.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgMulticastGreenMax.setStatus(_A)
_F10EgMulticastGreenDrop_Type=Counter64
_F10EgMulticastGreenDrop_Object=MibTableColumn
f10EgMulticastGreenDrop=_F10EgMulticastGreenDrop_Object((1,3,6,1,4,1,6027,3,3,4,5,1,8),_F10EgMulticastGreenDrop_Type())
f10EgMulticastGreenDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgMulticastGreenDrop.setStatus(_A)
_F10EgMulticastYellowMin_Type=Unsigned32
_F10EgMulticastYellowMin_Object=MibTableColumn
f10EgMulticastYellowMin=_F10EgMulticastYellowMin_Object((1,3,6,1,4,1,6027,3,3,4,5,1,9),_F10EgMulticastYellowMin_Type())
f10EgMulticastYellowMin.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgMulticastYellowMin.setStatus(_A)
_F10EgMulticastYellowMax_Type=Unsigned32
_F10EgMulticastYellowMax_Object=MibTableColumn
f10EgMulticastYellowMax=_F10EgMulticastYellowMax_Object((1,3,6,1,4,1,6027,3,3,4,5,1,10),_F10EgMulticastYellowMax_Type())
f10EgMulticastYellowMax.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgMulticastYellowMax.setStatus(_A)
_F10EgMulticastYellowDrop_Type=Counter64
_F10EgMulticastYellowDrop_Object=MibTableColumn
f10EgMulticastYellowDrop=_F10EgMulticastYellowDrop_Object((1,3,6,1,4,1,6027,3,3,4,5,1,11),_F10EgMulticastYellowDrop_Type())
f10EgMulticastYellowDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgMulticastYellowDrop.setStatus(_A)
_F10EgMulticastRedDrop_Type=Counter64
_F10EgMulticastRedDrop_Object=MibTableColumn
f10EgMulticastRedDrop=_F10EgMulticastRedDrop_Object((1,3,6,1,4,1,6027,3,3,4,5,1,12),_F10EgMulticastRedDrop_Type())
f10EgMulticastRedDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10EgMulticastRedDrop.setStatus(_A)
_F10CpuIngQueueUnicastStatTable_Object=MibTable
f10CpuIngQueueUnicastStatTable=_F10CpuIngQueueUnicastStatTable_Object((1,3,6,1,4,1,6027,3,3,4,6))
if mibBuilder.loadTexts:f10CpuIngQueueUnicastStatTable.setStatus(_A)
_F10CpuIngQueueUnicastStatEntry_Object=MibTableRow
f10CpuIngQueueUnicastStatEntry=_F10CpuIngQueueUnicastStatEntry_Object((1,3,6,1,4,1,6027,3,3,4,6,1))
f10CpuIngQueueUnicastStatEntry.setIndexNames((0,_C,_X),(0,_C,_Y),(0,_C,_Z),(0,_C,_a))
if mibBuilder.loadTexts:f10CpuIngQueueUnicastStatEntry.setStatus(_A)
_F10CpuIngUnicastSrcCard_Type=F10SlotID
_F10CpuIngUnicastSrcCard_Object=MibTableColumn
f10CpuIngUnicastSrcCard=_F10CpuIngUnicastSrcCard_Object((1,3,6,1,4,1,6027,3,3,4,6,1,1),_F10CpuIngUnicastSrcCard_Type())
f10CpuIngUnicastSrcCard.setMaxAccess(_F)
if mibBuilder.loadTexts:f10CpuIngUnicastSrcCard.setStatus(_A)
_F10CpuIngUnicastSrcPortPipe_Type=F10PortPipeID
_F10CpuIngUnicastSrcPortPipe_Object=MibTableColumn
f10CpuIngUnicastSrcPortPipe=_F10CpuIngUnicastSrcPortPipe_Object((1,3,6,1,4,1,6027,3,3,4,6,1,2),_F10CpuIngUnicastSrcPortPipe_Type())
f10CpuIngUnicastSrcPortPipe.setMaxAccess(_F)
if mibBuilder.loadTexts:f10CpuIngUnicastSrcPortPipe.setStatus(_A)
_F10CpuIngUnicastDestCpu_Type=F10ProcessorModuleType
_F10CpuIngUnicastDestCpu_Object=MibTableColumn
f10CpuIngUnicastDestCpu=_F10CpuIngUnicastDestCpu_Object((1,3,6,1,4,1,6027,3,3,4,6,1,3),_F10CpuIngUnicastDestCpu_Type())
f10CpuIngUnicastDestCpu.setMaxAccess(_F)
if mibBuilder.loadTexts:f10CpuIngUnicastDestCpu.setStatus(_A)
_F10CpuIngUnicastQueueId_Type=F10QueueID
_F10CpuIngUnicastQueueId_Object=MibTableColumn
f10CpuIngUnicastQueueId=_F10CpuIngUnicastQueueId_Object((1,3,6,1,4,1,6027,3,3,4,6,1,4),_F10CpuIngUnicastQueueId_Type())
f10CpuIngUnicastQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:f10CpuIngUnicastQueueId.setStatus(_A)
_F10CpuIngUnicastCycloneVersion_Type=F10CycloneVersion
_F10CpuIngUnicastCycloneVersion_Object=MibTableColumn
f10CpuIngUnicastCycloneVersion=_F10CpuIngUnicastCycloneVersion_Object((1,3,6,1,4,1,6027,3,3,4,6,1,5),_F10CpuIngUnicastCycloneVersion_Type())
f10CpuIngUnicastCycloneVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:f10CpuIngUnicastCycloneVersion.setStatus(_A)
_F10CpuIngUnicastBytesCount_Type=Counter64
_F10CpuIngUnicastBytesCount_Object=MibTableColumn
f10CpuIngUnicastBytesCount=_F10CpuIngUnicastBytesCount_Object((1,3,6,1,4,1,6027,3,3,4,6,1,6),_F10CpuIngUnicastBytesCount_Type())
f10CpuIngUnicastBytesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:f10CpuIngUnicastBytesCount.setStatus(_A)
_F10CpuIngUnicastPacketCount_Type=Counter64
_F10CpuIngUnicastPacketCount_Object=MibTableColumn
f10CpuIngUnicastPacketCount=_F10CpuIngUnicastPacketCount_Object((1,3,6,1,4,1,6027,3,3,4,6,1,7),_F10CpuIngUnicastPacketCount_Type())
f10CpuIngUnicastPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:f10CpuIngUnicastPacketCount.setStatus(_A)
_F10CpuIngUnicastGreenMin_Type=Unsigned32
_F10CpuIngUnicastGreenMin_Object=MibTableColumn
f10CpuIngUnicastGreenMin=_F10CpuIngUnicastGreenMin_Object((1,3,6,1,4,1,6027,3,3,4,6,1,8),_F10CpuIngUnicastGreenMin_Type())
f10CpuIngUnicastGreenMin.setMaxAccess(_B)
if mibBuilder.loadTexts:f10CpuIngUnicastGreenMin.setStatus(_A)
_F10CpuIngUnicastGreenMax_Type=Unsigned32
_F10CpuIngUnicastGreenMax_Object=MibTableColumn
f10CpuIngUnicastGreenMax=_F10CpuIngUnicastGreenMax_Object((1,3,6,1,4,1,6027,3,3,4,6,1,9),_F10CpuIngUnicastGreenMax_Type())
f10CpuIngUnicastGreenMax.setMaxAccess(_B)
if mibBuilder.loadTexts:f10CpuIngUnicastGreenMax.setStatus(_A)
_F10CpuIngUnicastGreenDrop_Type=Counter64
_F10CpuIngUnicastGreenDrop_Object=MibTableColumn
f10CpuIngUnicastGreenDrop=_F10CpuIngUnicastGreenDrop_Object((1,3,6,1,4,1,6027,3,3,4,6,1,10),_F10CpuIngUnicastGreenDrop_Type())
f10CpuIngUnicastGreenDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10CpuIngUnicastGreenDrop.setStatus(_A)
_F10CpuIngUnicastYellowMin_Type=Unsigned32
_F10CpuIngUnicastYellowMin_Object=MibTableColumn
f10CpuIngUnicastYellowMin=_F10CpuIngUnicastYellowMin_Object((1,3,6,1,4,1,6027,3,3,4,6,1,11),_F10CpuIngUnicastYellowMin_Type())
f10CpuIngUnicastYellowMin.setMaxAccess(_B)
if mibBuilder.loadTexts:f10CpuIngUnicastYellowMin.setStatus(_A)
_F10CpuIngUnicastYellowMax_Type=Unsigned32
_F10CpuIngUnicastYellowMax_Object=MibTableColumn
f10CpuIngUnicastYellowMax=_F10CpuIngUnicastYellowMax_Object((1,3,6,1,4,1,6027,3,3,4,6,1,12),_F10CpuIngUnicastYellowMax_Type())
f10CpuIngUnicastYellowMax.setMaxAccess(_B)
if mibBuilder.loadTexts:f10CpuIngUnicastYellowMax.setStatus(_A)
_F10CpuIngUnicastYellowDrop_Type=Counter64
_F10CpuIngUnicastYellowDrop_Object=MibTableColumn
f10CpuIngUnicastYellowDrop=_F10CpuIngUnicastYellowDrop_Object((1,3,6,1,4,1,6027,3,3,4,6,1,13),_F10CpuIngUnicastYellowDrop_Type())
f10CpuIngUnicastYellowDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10CpuIngUnicastYellowDrop.setStatus(_A)
_F10CpuIngUnicastRedDrop_Type=Counter64
_F10CpuIngUnicastRedDrop_Object=MibTableColumn
f10CpuIngUnicastRedDrop=_F10CpuIngUnicastRedDrop_Object((1,3,6,1,4,1,6027,3,3,4,6,1,14),_F10CpuIngUnicastRedDrop_Type())
f10CpuIngUnicastRedDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:f10CpuIngUnicastRedDrop.setStatus(_A)
_F10NetworkStat_ObjectIdentity=ObjectIdentity
f10NetworkStat=_F10NetworkStat_ObjectIdentity((1,3,6,1,4,1,6027,3,3,5))
_F10IpStatistic_ObjectIdentity=ObjectIdentity
f10IpStatistic=_F10IpStatistic_ObjectIdentity((1,3,6,1,4,1,6027,3,3,5,1))
_F10BcastPktRecv_Type=Counter64
_F10BcastPktRecv_Object=MibScalar
f10BcastPktRecv=_F10BcastPktRecv_Object((1,3,6,1,4,1,6027,3,3,5,1,1),_F10BcastPktRecv_Type())
f10BcastPktRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:f10BcastPktRecv.setStatus(_A)
_F10BcastPktSent_Type=Counter64
_F10BcastPktSent_Object=MibScalar
f10BcastPktSent=_F10BcastPktSent_Object((1,3,6,1,4,1,6027,3,3,5,1,2),_F10BcastPktSent_Type())
f10BcastPktSent.setMaxAccess(_B)
if mibBuilder.loadTexts:f10BcastPktSent.setStatus(_A)
_F10McastPktRecv_Type=Counter64
_F10McastPktRecv_Object=MibScalar
f10McastPktRecv=_F10McastPktRecv_Object((1,3,6,1,4,1,6027,3,3,5,1,3),_F10McastPktRecv_Type())
f10McastPktRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:f10McastPktRecv.setStatus(_A)
_F10McastPktSent_Type=Counter64
_F10McastPktSent_Object=MibScalar
f10McastPktSent=_F10McastPktSent_Object((1,3,6,1,4,1,6027,3,3,5,1,4),_F10McastPktSent_Type())
f10McastPktSent.setMaxAccess(_B)
if mibBuilder.loadTexts:f10McastPktSent.setStatus(_A)
_F10ArpStatistic_ObjectIdentity=ObjectIdentity
f10ArpStatistic=_F10ArpStatistic_ObjectIdentity((1,3,6,1,4,1,6027,3,3,5,2))
_F10ArpReqRecv_Type=Counter64
_F10ArpReqRecv_Object=MibScalar
f10ArpReqRecv=_F10ArpReqRecv_Object((1,3,6,1,4,1,6027,3,3,5,2,1),_F10ArpReqRecv_Type())
f10ArpReqRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:f10ArpReqRecv.setStatus(_A)
_F10ArpReqSent_Type=Counter64
_F10ArpReqSent_Object=MibScalar
f10ArpReqSent=_F10ArpReqSent_Object((1,3,6,1,4,1,6027,3,3,5,2,2),_F10ArpReqSent_Type())
f10ArpReqSent.setMaxAccess(_B)
if mibBuilder.loadTexts:f10ArpReqSent.setStatus(_A)
_F10ArpReplyRecv_Type=Counter64
_F10ArpReplyRecv_Object=MibScalar
f10ArpReplyRecv=_F10ArpReplyRecv_Object((1,3,6,1,4,1,6027,3,3,5,2,3),_F10ArpReplyRecv_Type())
f10ArpReplyRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:f10ArpReplyRecv.setStatus(_A)
_F10ArpReplySent_Type=Counter64
_F10ArpReplySent_Object=MibScalar
f10ArpReplySent=_F10ArpReplySent_Object((1,3,6,1,4,1,6027,3,3,5,2,4),_F10ArpReplySent_Type())
f10ArpReplySent.setMaxAccess(_B)
if mibBuilder.loadTexts:f10ArpReplySent.setStatus(_A)
_F10ArpProxySent_Type=Counter64
_F10ArpProxySent_Object=MibScalar
f10ArpProxySent=_F10ArpProxySent_Object((1,3,6,1,4,1,6027,3,3,5,2,5),_F10ArpProxySent_Type())
f10ArpProxySent.setMaxAccess(_B)
if mibBuilder.loadTexts:f10ArpProxySent.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'f10MonitoringMib':f10MonitoringMib,'f10MonGroup':f10MonGroup,'f10MonMibVersion':f10MonMibVersion,'f10MonQueue':f10MonQueue,'f10MonQueueGroup':f10MonQueueGroup,'f10MonMaxQueue':f10MonMaxQueue,'f10InQueueStatisticsTable':f10InQueueStatisticsTable,'f10InQueueStatisticsEntry':f10InQueueStatisticsEntry,_H:f10InQueueId,'f10InQueueDropPackets':f10InQueueDropPackets,'f10InQueueBytes':f10InQueueBytes,'f10InQueueMatchPackets':f10InQueueMatchPackets,'f10InQueueMatchBytes':f10InQueueMatchBytes,'f10InQueueMatchBps':f10InQueueMatchBps,'f10InQueueCycloneVersion':f10InQueueCycloneVersion,'f10InQueueBytesCount':f10InQueueBytesCount,'f10InQueuePktsCount':f10InQueuePktsCount,'f10OutQueueStatisticsTable':f10OutQueueStatisticsTable,'f10OutQueueStatisticsEntry':f10OutQueueStatisticsEntry,_I:f10OutQueueId,'f10OutQueuePackets':f10OutQueuePackets,'f10OutQueueBytes':f10OutQueueBytes,'f10OutQueueBps':f10OutQueueBps,'f10OutQueueCycloneVersion':f10OutQueueCycloneVersion,'f10OutQueueBytesCount':f10OutQueueBytesCount,'f10WredStatisticsTable':f10WredStatisticsTable,'f10WredStatisticsEntry':f10WredStatisticsEntry,_J:f10WredQueueId,'f10WredGreenName':f10WredGreenName,'f10WredGreenThresholdLow':f10WredGreenThresholdLow,'f10WredGreenThresholdHigh':f10WredGreenThresholdHigh,'f10WredGreenDropPackets':f10WredGreenDropPackets,'f10WredGreenReserve1':f10WredGreenReserve1,'f10WredGreenReserve2':f10WredGreenReserve2,'f10WredYellowName':f10WredYellowName,'f10WredYellowThresholdLow':f10WredYellowThresholdLow,'f10WredYellowThresholdHigh':f10WredYellowThresholdHigh,'f10WredYellowDropPackets':f10WredYellowDropPackets,'f10WredYellowReserve1':f10WredYellowReserve1,'f10WredYellowReserve2':f10WredYellowReserve2,'f10WredRedName':f10WredRedName,'f10WredRedThresholdLow':f10WredRedThresholdLow,'f10WredRedThresholdHigh':f10WredRedThresholdHigh,'f10WredRedDropPackets':f10WredRedDropPackets,'f10WredRedReserve1':f10WredRedReserve1,'f10WredRedReserve2':f10WredRedReserve2,'f10MonMac':f10MonMac,'f10MacGroup':f10MacGroup,'f10MacAccounting':f10MacAccounting,'f10MacAccountingDestTable':f10MacAccountingDestTable,'f10MacAccountingDestEntry':f10MacAccountingDestEntry,_K:f10MacAccInIfIndex,_L:f10MacAccVlan,_M:f10MacAccMacAddr,'f10MacAccOutIfIndex':f10MacAccOutIfIndex,'f10MacAccPackets':f10MacAccPackets,'f10MacAccBytes':f10MacAccBytes,'f10MonIfQueue':f10MonIfQueue,'f10MonIfQueueGroup':f10MonIfQueueGroup,'f10IngQueueUnicastStatTable':f10IngQueueUnicastStatTable,'f10IngQueueUnicastStatEntry':f10IngQueueUnicastStatEntry,_N:f10IngUnicastSrcCard,_O:f10IngUnicastDestCard,_P:f10IngUnicastSrcPortPipe,_Q:f10IngUnicastDestPortPipe,_R:f10IngUnicastQueueId,'f10IngUnicastCycloneVersion':f10IngUnicastCycloneVersion,'f10IngUnicastBytes':f10IngUnicastBytes,'f10IngUnicastBytesCount':f10IngUnicastBytesCount,'f10IngUnicastPacketCount':f10IngUnicastPacketCount,'f10IngUnicastGreenMin':f10IngUnicastGreenMin,'f10IngUnicastGreenMax':f10IngUnicastGreenMax,'f10IngUnicastGreenDrop':f10IngUnicastGreenDrop,'f10IngUnicastYellowMin':f10IngUnicastYellowMin,'f10IngUnicastYellowMax':f10IngUnicastYellowMax,'f10IngUnicastYellowDrop':f10IngUnicastYellowDrop,'f10IngUnicastRedDrop':f10IngUnicastRedDrop,'f10IngQueueMulticastStatTable':f10IngQueueMulticastStatTable,'f10IngQueueMulticastStatEntry':f10IngQueueMulticastStatEntry,_S:f10IngMulticastSrcCard,_T:f10IngMulticastSrcPortPipe,_U:f10IngMulticastQueueId,'f10IngMulticastCycloneVersion':f10IngMulticastCycloneVersion,'f10IngMulticastBytes':f10IngMulticastBytes,'f10IngMulticastBytesCount':f10IngMulticastBytesCount,'f10IngMulticastPacketCount':f10IngMulticastPacketCount,'f10IngMulticastGreenMin':f10IngMulticastGreenMin,'f10IngMulticastGreenMax':f10IngMulticastGreenMax,'f10IngMulticastGreenDrop':f10IngMulticastGreenDrop,'f10IngMulticastYellowMin':f10IngMulticastYellowMin,'f10IngMulticastYellowMax':f10IngMulticastYellowMax,'f10IngMulticastYellowDrop':f10IngMulticastYellowDrop,'f10IngMulticastRedDrop':f10IngMulticastRedDrop,'f10EgQueueUnicastStatTable':f10EgQueueUnicastStatTable,'f10EgQueueUnicastStatEntry':f10EgQueueUnicastStatEntry,_V:f10EgUnicastQueueId,'f10EgUnicastCycloneVersion':f10EgUnicastCycloneVersion,'f10EgUnicastBytes':f10EgUnicastBytes,'f10EgUnicastBytesCount':f10EgUnicastBytesCount,'f10EgUnicastPacketCount':f10EgUnicastPacketCount,'f10EgUnicastGreenMin':f10EgUnicastGreenMin,'f10EgUnicastGreenMax':f10EgUnicastGreenMax,'f10EgUnicastGreenDrop':f10EgUnicastGreenDrop,'f10EgUnicastYellowMin':f10EgUnicastYellowMin,'f10EgUnicastYellowMax':f10EgUnicastYellowMax,'f10EgUnicastYellowDrop':f10EgUnicastYellowDrop,'f10EgUnicastRedDrop':f10EgUnicastRedDrop,'f10EgQueueMulticastStatTable':f10EgQueueMulticastStatTable,'f10EgQueueMulticastStatEntry':f10EgQueueMulticastStatEntry,_W:f10EgMulticastQueueId,'f10EgMulticastCycloneVersion':f10EgMulticastCycloneVersion,'f10EgMulticastBytes':f10EgMulticastBytes,'f10EgMulticastBytesCount':f10EgMulticastBytesCount,'f10EgMulticastPacketCount':f10EgMulticastPacketCount,'f10EgMulticastGreenMin':f10EgMulticastGreenMin,'f10EgMulticastGreenMax':f10EgMulticastGreenMax,'f10EgMulticastGreenDrop':f10EgMulticastGreenDrop,'f10EgMulticastYellowMin':f10EgMulticastYellowMin,'f10EgMulticastYellowMax':f10EgMulticastYellowMax,'f10EgMulticastYellowDrop':f10EgMulticastYellowDrop,'f10EgMulticastRedDrop':f10EgMulticastRedDrop,'f10CpuIngQueueUnicastStatTable':f10CpuIngQueueUnicastStatTable,'f10CpuIngQueueUnicastStatEntry':f10CpuIngQueueUnicastStatEntry,_X:f10CpuIngUnicastSrcCard,_Y:f10CpuIngUnicastSrcPortPipe,_Z:f10CpuIngUnicastDestCpu,_a:f10CpuIngUnicastQueueId,'f10CpuIngUnicastCycloneVersion':f10CpuIngUnicastCycloneVersion,'f10CpuIngUnicastBytesCount':f10CpuIngUnicastBytesCount,'f10CpuIngUnicastPacketCount':f10CpuIngUnicastPacketCount,'f10CpuIngUnicastGreenMin':f10CpuIngUnicastGreenMin,'f10CpuIngUnicastGreenMax':f10CpuIngUnicastGreenMax,'f10CpuIngUnicastGreenDrop':f10CpuIngUnicastGreenDrop,'f10CpuIngUnicastYellowMin':f10CpuIngUnicastYellowMin,'f10CpuIngUnicastYellowMax':f10CpuIngUnicastYellowMax,'f10CpuIngUnicastYellowDrop':f10CpuIngUnicastYellowDrop,'f10CpuIngUnicastRedDrop':f10CpuIngUnicastRedDrop,'f10NetworkStat':f10NetworkStat,'f10IpStatistic':f10IpStatistic,'f10BcastPktRecv':f10BcastPktRecv,'f10BcastPktSent':f10BcastPktSent,'f10McastPktRecv':f10McastPktRecv,'f10McastPktSent':f10McastPktSent,'f10ArpStatistic':f10ArpStatistic,'f10ArpReqRecv':f10ArpReqRecv,'f10ArpReqSent':f10ArpReqSent,'f10ArpReplyRecv':f10ArpReplyRecv,'f10ArpReplySent':f10ArpReplySent,'f10ArpProxySent':f10ArpProxySent})