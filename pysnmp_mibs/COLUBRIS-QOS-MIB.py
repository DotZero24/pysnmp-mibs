_O='coQOSCountersGroup'
_N='coQOSMulticastReceivedFrameCount'
_M='coQOSReceivedFrameCount'
_L='coQOSFrameDuplicateCount'
_K='coQOSMultipleRetryCount'
_J='coQOSRetryCount'
_I='coQOSFailedCount'
_H='coQOSMulticastTransmittedFrameCount'
_G='coQOSTransmittedFrameCount'
_F='coQOSQueueId'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='COLUBRIS-QOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ColubrisPriorityQueue,=mibBuilder.importSymbols('COLUBRIS-TC','ColubrisPriorityQueue')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
colubrisQOS=ModuleIdentity((1,3,6,1,4,1,8744,5,13))
_ColubrisQOSMIBObjects_ObjectIdentity=ObjectIdentity
colubrisQOSMIBObjects=_ColubrisQOSMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,13,1))
_CoQOSStatistics_ObjectIdentity=ObjectIdentity
coQOSStatistics=_CoQOSStatistics_ObjectIdentity((1,3,6,1,4,1,8744,5,13,1,1))
_CoQOSCountersTable_Object=MibTable
coQOSCountersTable=_CoQOSCountersTable_Object((1,3,6,1,4,1,8744,5,13,1,1,1))
if mibBuilder.loadTexts:coQOSCountersTable.setStatus(_A)
_CoQOSCountersEntry_Object=MibTableRow
coQOSCountersEntry=_CoQOSCountersEntry_Object((1,3,6,1,4,1,8744,5,13,1,1,1,1))
coQOSCountersEntry.setIndexNames((0,_D,_E),(0,_B,_F))
if mibBuilder.loadTexts:coQOSCountersEntry.setStatus(_A)
_CoQOSQueueId_Type=ColubrisPriorityQueue
_CoQOSQueueId_Object=MibTableColumn
coQOSQueueId=_CoQOSQueueId_Object((1,3,6,1,4,1,8744,5,13,1,1,1,1,1),_CoQOSQueueId_Type())
coQOSQueueId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:coQOSQueueId.setStatus(_A)
_CoQOSTransmittedFrameCount_Type=Counter32
_CoQOSTransmittedFrameCount_Object=MibTableColumn
coQOSTransmittedFrameCount=_CoQOSTransmittedFrameCount_Object((1,3,6,1,4,1,8744,5,13,1,1,1,1,2),_CoQOSTransmittedFrameCount_Type())
coQOSTransmittedFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:coQOSTransmittedFrameCount.setStatus(_A)
_CoQOSMulticastTransmittedFrameCount_Type=Counter32
_CoQOSMulticastTransmittedFrameCount_Object=MibTableColumn
coQOSMulticastTransmittedFrameCount=_CoQOSMulticastTransmittedFrameCount_Object((1,3,6,1,4,1,8744,5,13,1,1,1,1,3),_CoQOSMulticastTransmittedFrameCount_Type())
coQOSMulticastTransmittedFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:coQOSMulticastTransmittedFrameCount.setStatus(_A)
_CoQOSFailedCount_Type=Counter32
_CoQOSFailedCount_Object=MibTableColumn
coQOSFailedCount=_CoQOSFailedCount_Object((1,3,6,1,4,1,8744,5,13,1,1,1,1,4),_CoQOSFailedCount_Type())
coQOSFailedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:coQOSFailedCount.setStatus(_A)
_CoQOSRetryCount_Type=Counter32
_CoQOSRetryCount_Object=MibTableColumn
coQOSRetryCount=_CoQOSRetryCount_Object((1,3,6,1,4,1,8744,5,13,1,1,1,1,5),_CoQOSRetryCount_Type())
coQOSRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:coQOSRetryCount.setStatus(_A)
_CoQOSMultipleRetryCount_Type=Counter32
_CoQOSMultipleRetryCount_Object=MibTableColumn
coQOSMultipleRetryCount=_CoQOSMultipleRetryCount_Object((1,3,6,1,4,1,8744,5,13,1,1,1,1,6),_CoQOSMultipleRetryCount_Type())
coQOSMultipleRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:coQOSMultipleRetryCount.setStatus(_A)
_CoQOSFrameDuplicateCount_Type=Counter32
_CoQOSFrameDuplicateCount_Object=MibTableColumn
coQOSFrameDuplicateCount=_CoQOSFrameDuplicateCount_Object((1,3,6,1,4,1,8744,5,13,1,1,1,1,7),_CoQOSFrameDuplicateCount_Type())
coQOSFrameDuplicateCount.setMaxAccess(_C)
if mibBuilder.loadTexts:coQOSFrameDuplicateCount.setStatus(_A)
_CoQOSReceivedFrameCount_Type=Counter32
_CoQOSReceivedFrameCount_Object=MibTableColumn
coQOSReceivedFrameCount=_CoQOSReceivedFrameCount_Object((1,3,6,1,4,1,8744,5,13,1,1,1,1,8),_CoQOSReceivedFrameCount_Type())
coQOSReceivedFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:coQOSReceivedFrameCount.setStatus(_A)
_CoQOSMulticastReceivedFrameCount_Type=Counter32
_CoQOSMulticastReceivedFrameCount_Object=MibTableColumn
coQOSMulticastReceivedFrameCount=_CoQOSMulticastReceivedFrameCount_Object((1,3,6,1,4,1,8744,5,13,1,1,1,1,9),_CoQOSMulticastReceivedFrameCount_Type())
coQOSMulticastReceivedFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:coQOSMulticastReceivedFrameCount.setStatus(_A)
_CoQOSConformance_ObjectIdentity=ObjectIdentity
coQOSConformance=_CoQOSConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,13,1,2))
_CoQOSGroups_ObjectIdentity=ObjectIdentity
coQOSGroups=_CoQOSGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,13,1,2,1))
_CoQOSCompliances_ObjectIdentity=ObjectIdentity
coQOSCompliances=_CoQOSCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,13,1,2,2))
coQOSCountersGroup=ObjectGroup((1,3,6,1,4,1,8744,5,13,1,2,1,1))
coQOSCountersGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:coQOSCountersGroup.setStatus(_A)
coQOSCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,13,1,2,2,1))
coQOSCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:coQOSCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'colubrisQOS':colubrisQOS,'colubrisQOSMIBObjects':colubrisQOSMIBObjects,'coQOSStatistics':coQOSStatistics,'coQOSCountersTable':coQOSCountersTable,'coQOSCountersEntry':coQOSCountersEntry,_F:coQOSQueueId,_G:coQOSTransmittedFrameCount,_H:coQOSMulticastTransmittedFrameCount,_I:coQOSFailedCount,_J:coQOSRetryCount,_K:coQOSMultipleRetryCount,_L:coQOSFrameDuplicateCount,_M:coQOSReceivedFrameCount,_N:coQOSMulticastReceivedFrameCount,'coQOSConformance':coQOSConformance,'coQOSGroups':coQOSGroups,_O:coQOSCountersGroup,'coQOSCompliances':coQOSCompliances,'coQOSCompliance':coQOSCompliance})