_J='Integer32'
_I='jnxPMonLastOverloadDate'
_H='jnxPMonCurrentOverload'
_G='jnxPMonLastOverload'
_F='ifDescr'
_E='ifIndex'
_D='IF-MIB'
_C='JUNIPER-PMon-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifDescr,ifIndex=mibBuilder.importSymbols(_D,_F,_E)
jnxMibs,jnxPMonNotifications=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs','jnxPMonNotifications')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
jnxPMon=ModuleIdentity((1,3,6,1,4,1,2636,3,19))
if mibBuilder.loadTexts:jnxPMon.setRevisions(('2002-06-05 00:00','2002-08-27 00:00','2002-09-09 00:00'))
class JnxPMonOverloadId(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('pmonMemOverload',0),('pmonPpsOverload',1),('pmonBpsOverload',2),('pmonMemWarning',3)))
_JnxPMonFlowTable_Object=MibTable
jnxPMonFlowTable=_JnxPMonFlowTable_Object((1,3,6,1,4,1,2636,3,19,1))
if mibBuilder.loadTexts:jnxPMonFlowTable.setStatus(_A)
_JnxPMonFlowEntry_Object=MibTableRow
jnxPMonFlowEntry=_JnxPMonFlowEntry_Object((1,3,6,1,4,1,2636,3,19,1,1))
jnxPMonFlowEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:jnxPMonFlowEntry.setStatus(_A)
_JnxPMonCurrentActiveFlows_Type=Gauge32
_JnxPMonCurrentActiveFlows_Object=MibTableColumn
jnxPMonCurrentActiveFlows=_JnxPMonCurrentActiveFlows_Object((1,3,6,1,4,1,2636,3,19,1,1,1),_JnxPMonCurrentActiveFlows_Type())
jnxPMonCurrentActiveFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonCurrentActiveFlows.setStatus(_A)
_JnxPMonTotalFlows_Type=Counter32
_JnxPMonTotalFlows_Object=MibTableColumn
jnxPMonTotalFlows=_JnxPMonTotalFlows_Object((1,3,6,1,4,1,2636,3,19,1,1,2),_JnxPMonTotalFlows_Type())
jnxPMonTotalFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonTotalFlows.setStatus(_A)
_JnxPMonTotalFlowsPackets_Type=Counter64
_JnxPMonTotalFlowsPackets_Object=MibTableColumn
jnxPMonTotalFlowsPackets=_JnxPMonTotalFlowsPackets_Object((1,3,6,1,4,1,2636,3,19,1,1,3),_JnxPMonTotalFlowsPackets_Type())
jnxPMonTotalFlowsPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonTotalFlowsPackets.setStatus(_A)
_JnxPMonTenSecondAverageFlowPackets_Type=Gauge32
_JnxPMonTenSecondAverageFlowPackets_Object=MibTableColumn
jnxPMonTenSecondAverageFlowPackets=_JnxPMonTenSecondAverageFlowPackets_Object((1,3,6,1,4,1,2636,3,19,1,1,4),_JnxPMonTenSecondAverageFlowPackets_Type())
jnxPMonTenSecondAverageFlowPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonTenSecondAverageFlowPackets.setStatus(_A)
_JnxPMonTotalFlowsBytes_Type=Counter64
_JnxPMonTotalFlowsBytes_Object=MibTableColumn
jnxPMonTotalFlowsBytes=_JnxPMonTotalFlowsBytes_Object((1,3,6,1,4,1,2636,3,19,1,1,5),_JnxPMonTotalFlowsBytes_Type())
jnxPMonTotalFlowsBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonTotalFlowsBytes.setStatus(_A)
_JnxPMonTenSecondAverageFlowBytes_Type=Gauge32
_JnxPMonTenSecondAverageFlowBytes_Object=MibTableColumn
jnxPMonTenSecondAverageFlowBytes=_JnxPMonTenSecondAverageFlowBytes_Object((1,3,6,1,4,1,2636,3,19,1,1,6),_JnxPMonTenSecondAverageFlowBytes_Type())
jnxPMonTenSecondAverageFlowBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonTenSecondAverageFlowBytes.setStatus(_A)
_JnxPMonTotalFlowsExpired_Type=Counter32
_JnxPMonTotalFlowsExpired_Object=MibTableColumn
jnxPMonTotalFlowsExpired=_JnxPMonTotalFlowsExpired_Object((1,3,6,1,4,1,2636,3,19,1,1,7),_JnxPMonTotalFlowsExpired_Type())
jnxPMonTotalFlowsExpired.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonTotalFlowsExpired.setStatus(_A)
_JnxPMonTotalFlowsAged_Type=Counter32
_JnxPMonTotalFlowsAged_Object=MibTableColumn
jnxPMonTotalFlowsAged=_JnxPMonTotalFlowsAged_Object((1,3,6,1,4,1,2636,3,19,1,1,8),_JnxPMonTotalFlowsAged_Type())
jnxPMonTotalFlowsAged.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonTotalFlowsAged.setStatus(_A)
_JnxPMonTotalFlowsExported_Type=Counter32
_JnxPMonTotalFlowsExported_Object=MibTableColumn
jnxPMonTotalFlowsExported=_JnxPMonTotalFlowsExported_Object((1,3,6,1,4,1,2636,3,19,1,1,9),_JnxPMonTotalFlowsExported_Type())
jnxPMonTotalFlowsExported.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonTotalFlowsExported.setStatus(_A)
_JnxPMonTotalFlowsPacketsExported_Type=Counter32
_JnxPMonTotalFlowsPacketsExported_Object=MibTableColumn
jnxPMonTotalFlowsPacketsExported=_JnxPMonTotalFlowsPacketsExported_Object((1,3,6,1,4,1,2636,3,19,1,1,10),_JnxPMonTotalFlowsPacketsExported_Type())
jnxPMonTotalFlowsPacketsExported.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonTotalFlowsPacketsExported.setStatus(_A)
_JnxPMonErrorTable_Object=MibTable
jnxPMonErrorTable=_JnxPMonErrorTable_Object((1,3,6,1,4,1,2636,3,19,2))
if mibBuilder.loadTexts:jnxPMonErrorTable.setStatus(_A)
_JnxPMonErrorEntry_Object=MibTableRow
jnxPMonErrorEntry=_JnxPMonErrorEntry_Object((1,3,6,1,4,1,2636,3,19,2,1))
jnxPMonErrorEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:jnxPMonErrorEntry.setStatus(_A)
_JnxPMonFlowAllocFailures_Type=Counter32
_JnxPMonFlowAllocFailures_Object=MibTableColumn
jnxPMonFlowAllocFailures=_JnxPMonFlowAllocFailures_Object((1,3,6,1,4,1,2636,3,19,2,1,1),_JnxPMonFlowAllocFailures_Type())
jnxPMonFlowAllocFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonFlowAllocFailures.setStatus(_A)
_JnxPMonFlowFreeFailures_Type=Counter32
_JnxPMonFlowFreeFailures_Object=MibTableColumn
jnxPMonFlowFreeFailures=_JnxPMonFlowFreeFailures_Object((1,3,6,1,4,1,2636,3,19,2,1,2),_JnxPMonFlowFreeFailures_Type())
jnxPMonFlowFreeFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonFlowFreeFailures.setStatus(_A)
_JnxPMonFreeListFailures_Type=Counter32
_JnxPMonFreeListFailures_Object=MibTableColumn
jnxPMonFreeListFailures=_JnxPMonFreeListFailures_Object((1,3,6,1,4,1,2636,3,19,2,1,3),_JnxPMonFreeListFailures_Type())
jnxPMonFreeListFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonFreeListFailures.setStatus(_A)
_JnxPMonNoMemDrops_Type=Counter64
_JnxPMonNoMemDrops_Object=MibTableColumn
jnxPMonNoMemDrops=_JnxPMonNoMemDrops_Object((1,3,6,1,4,1,2636,3,19,2,1,4),_JnxPMonNoMemDrops_Type())
jnxPMonNoMemDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonNoMemDrops.setStatus(_A)
_JnxPMonNotIPDrops_Type=Counter64
_JnxPMonNotIPDrops_Object=MibTableColumn
jnxPMonNotIPDrops=_JnxPMonNotIPDrops_Object((1,3,6,1,4,1,2636,3,19,2,1,5),_JnxPMonNotIPDrops_Type())
jnxPMonNotIPDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonNotIPDrops.setStatus(_A)
_JnxPMonNotIPv4Drops_Type=Counter64
_JnxPMonNotIPv4Drops_Object=MibTableColumn
jnxPMonNotIPv4Drops=_JnxPMonNotIPv4Drops_Object((1,3,6,1,4,1,2636,3,19,2,1,6),_JnxPMonNotIPv4Drops_Type())
jnxPMonNotIPv4Drops.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonNotIPv4Drops.setStatus(_A)
_JnxPMonTooSmallDrops_Type=Counter64
_JnxPMonTooSmallDrops_Object=MibTableColumn
jnxPMonTooSmallDrops=_JnxPMonTooSmallDrops_Object((1,3,6,1,4,1,2636,3,19,2,1,7),_JnxPMonTooSmallDrops_Type())
jnxPMonTooSmallDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonTooSmallDrops.setStatus(_A)
_JnxPMonCurrentOverload_Type=JnxPMonOverloadId
_JnxPMonCurrentOverload_Object=MibTableColumn
jnxPMonCurrentOverload=_JnxPMonCurrentOverload_Object((1,3,6,1,4,1,2636,3,19,2,1,8),_JnxPMonCurrentOverload_Type())
jnxPMonCurrentOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonCurrentOverload.setStatus(_A)
_JnxPMonLastOverload_Type=JnxPMonOverloadId
_JnxPMonLastOverload_Object=MibTableColumn
jnxPMonLastOverload=_JnxPMonLastOverload_Object((1,3,6,1,4,1,2636,3,19,2,1,9),_JnxPMonLastOverload_Type())
jnxPMonLastOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonLastOverload.setStatus(_A)
_JnxPMonLastOverloadTime_Type=TimeTicks
_JnxPMonLastOverloadTime_Object=MibTableColumn
jnxPMonLastOverloadTime=_JnxPMonLastOverloadTime_Object((1,3,6,1,4,1,2636,3,19,2,1,10),_JnxPMonLastOverloadTime_Type())
jnxPMonLastOverloadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonLastOverloadTime.setStatus(_A)
_JnxPMonLastOverloadDate_Type=DateAndTime
_JnxPMonLastOverloadDate_Object=MibTableColumn
jnxPMonLastOverloadDate=_JnxPMonLastOverloadDate_Object((1,3,6,1,4,1,2636,3,19,2,1,11),_JnxPMonLastOverloadDate_Type())
jnxPMonLastOverloadDate.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonLastOverloadDate.setStatus(_A)
class _JnxPMonLastOverloadEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('set',2),('cleared',3)))
_JnxPMonLastOverloadEvent_Type.__name__=_J
_JnxPMonLastOverloadEvent_Object=MibTableColumn
jnxPMonLastOverloadEvent=_JnxPMonLastOverloadEvent_Object((1,3,6,1,4,1,2636,3,19,2,1,12),_JnxPMonLastOverloadEvent_Type())
jnxPMonLastOverloadEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonLastOverloadEvent.setStatus(_A)
_JnxPMonMemoryTable_Object=MibTable
jnxPMonMemoryTable=_JnxPMonMemoryTable_Object((1,3,6,1,4,1,2636,3,19,3))
if mibBuilder.loadTexts:jnxPMonMemoryTable.setStatus(_A)
_JnxPMonMemoryEntry_Object=MibTableRow
jnxPMonMemoryEntry=_JnxPMonMemoryEntry_Object((1,3,6,1,4,1,2636,3,19,3,1))
jnxPMonMemoryEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:jnxPMonMemoryEntry.setStatus(_A)
_JnxPMonFlowTotalAlloc_Type=Counter64
_JnxPMonFlowTotalAlloc_Object=MibTableColumn
jnxPMonFlowTotalAlloc=_JnxPMonFlowTotalAlloc_Object((1,3,6,1,4,1,2636,3,19,3,1,1),_JnxPMonFlowTotalAlloc_Type())
jnxPMonFlowTotalAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonFlowTotalAlloc.setStatus(_A)
_JnxPMonFlowTotalFree_Type=Counter64
_JnxPMonFlowTotalFree_Object=MibTableColumn
jnxPMonFlowTotalFree=_JnxPMonFlowTotalFree_Object((1,3,6,1,4,1,2636,3,19,3,1,2),_JnxPMonFlowTotalFree_Type())
jnxPMonFlowTotalFree.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonFlowTotalFree.setStatus(_A)
_JnxPMonFlowMaxAlloc_Type=Counter64
_JnxPMonFlowMaxAlloc_Object=MibTableColumn
jnxPMonFlowMaxAlloc=_JnxPMonFlowMaxAlloc_Object((1,3,6,1,4,1,2636,3,19,3,1,3),_JnxPMonFlowMaxAlloc_Type())
jnxPMonFlowMaxAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonFlowMaxAlloc.setStatus(_A)
_JnxPMonAllocPerSecond_Type=Gauge32
_JnxPMonAllocPerSecond_Object=MibTableColumn
jnxPMonAllocPerSecond=_JnxPMonAllocPerSecond_Object((1,3,6,1,4,1,2636,3,19,3,1,4),_JnxPMonAllocPerSecond_Type())
jnxPMonAllocPerSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonAllocPerSecond.setStatus(_A)
_JnxPMonFreePerSecond_Type=Gauge32
_JnxPMonFreePerSecond_Object=MibTableColumn
jnxPMonFreePerSecond=_JnxPMonFreePerSecond_Object((1,3,6,1,4,1,2636,3,19,3,1,5),_JnxPMonFreePerSecond_Type())
jnxPMonFreePerSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonFreePerSecond.setStatus(_A)
_JnxPMonTotalMemoryUsed_Type=Gauge32
_JnxPMonTotalMemoryUsed_Object=MibTableColumn
jnxPMonTotalMemoryUsed=_JnxPMonTotalMemoryUsed_Object((1,3,6,1,4,1,2636,3,19,3,1,6),_JnxPMonTotalMemoryUsed_Type())
jnxPMonTotalMemoryUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonTotalMemoryUsed.setStatus(_A)
_JnxPMonTotalMemoryFree_Type=Gauge32
_JnxPMonTotalMemoryFree_Object=MibTableColumn
jnxPMonTotalMemoryFree=_JnxPMonTotalMemoryFree_Object((1,3,6,1,4,1,2636,3,19,3,1,7),_JnxPMonTotalMemoryFree_Type())
jnxPMonTotalMemoryFree.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxPMonTotalMemoryFree.setStatus(_A)
_JnxPMonNotificationPrefix_ObjectIdentity=ObjectIdentity
jnxPMonNotificationPrefix=_JnxPMonNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,2636,4,7,0))
jnxPMonOverloadSet=NotificationType((1,3,6,1,4,1,2636,4,7,0,1))
jnxPMonOverloadSet.setObjects(*((_D,_F),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:jnxPMonOverloadSet.setStatus(_A)
jnxPMonOverloadCleared=NotificationType((1,3,6,1,4,1,2636,4,7,0,2))
jnxPMonOverloadCleared.setObjects(*((_D,_F),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:jnxPMonOverloadCleared.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'JnxPMonOverloadId':JnxPMonOverloadId,'jnxPMon':jnxPMon,'jnxPMonFlowTable':jnxPMonFlowTable,'jnxPMonFlowEntry':jnxPMonFlowEntry,'jnxPMonCurrentActiveFlows':jnxPMonCurrentActiveFlows,'jnxPMonTotalFlows':jnxPMonTotalFlows,'jnxPMonTotalFlowsPackets':jnxPMonTotalFlowsPackets,'jnxPMonTenSecondAverageFlowPackets':jnxPMonTenSecondAverageFlowPackets,'jnxPMonTotalFlowsBytes':jnxPMonTotalFlowsBytes,'jnxPMonTenSecondAverageFlowBytes':jnxPMonTenSecondAverageFlowBytes,'jnxPMonTotalFlowsExpired':jnxPMonTotalFlowsExpired,'jnxPMonTotalFlowsAged':jnxPMonTotalFlowsAged,'jnxPMonTotalFlowsExported':jnxPMonTotalFlowsExported,'jnxPMonTotalFlowsPacketsExported':jnxPMonTotalFlowsPacketsExported,'jnxPMonErrorTable':jnxPMonErrorTable,'jnxPMonErrorEntry':jnxPMonErrorEntry,'jnxPMonFlowAllocFailures':jnxPMonFlowAllocFailures,'jnxPMonFlowFreeFailures':jnxPMonFlowFreeFailures,'jnxPMonFreeListFailures':jnxPMonFreeListFailures,'jnxPMonNoMemDrops':jnxPMonNoMemDrops,'jnxPMonNotIPDrops':jnxPMonNotIPDrops,'jnxPMonNotIPv4Drops':jnxPMonNotIPv4Drops,'jnxPMonTooSmallDrops':jnxPMonTooSmallDrops,_H:jnxPMonCurrentOverload,_G:jnxPMonLastOverload,'jnxPMonLastOverloadTime':jnxPMonLastOverloadTime,_I:jnxPMonLastOverloadDate,'jnxPMonLastOverloadEvent':jnxPMonLastOverloadEvent,'jnxPMonMemoryTable':jnxPMonMemoryTable,'jnxPMonMemoryEntry':jnxPMonMemoryEntry,'jnxPMonFlowTotalAlloc':jnxPMonFlowTotalAlloc,'jnxPMonFlowTotalFree':jnxPMonFlowTotalFree,'jnxPMonFlowMaxAlloc':jnxPMonFlowMaxAlloc,'jnxPMonAllocPerSecond':jnxPMonAllocPerSecond,'jnxPMonFreePerSecond':jnxPMonFreePerSecond,'jnxPMonTotalMemoryUsed':jnxPMonTotalMemoryUsed,'jnxPMonTotalMemoryFree':jnxPMonTotalMemoryFree,'jnxPMonNotificationPrefix':jnxPMonNotificationPrefix,'jnxPMonOverloadSet':jnxPMonOverloadSet,'jnxPMonOverloadCleared':jnxPMonOverloadCleared})