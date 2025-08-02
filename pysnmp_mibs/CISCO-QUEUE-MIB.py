_Q='cQRotationGroup'
_P='cQStatsGroup'
_O='cQIfGroup'
_N='cQRotationOctets'
_M='cQStatsDiscards'
_L='cQStatsMaxDepth'
_K='cQStatsDepth'
_J='cQIfSubqueues'
_I='cQIfTxLimit'
_H='cQIfQType'
_G='Integer32'
_F='cQStatsQNumber'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='CISCO-QUEUE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoQueueMIB=ModuleIdentity((1,3,6,1,4,1,9,9,37))
if mibBuilder.loadTexts:ciscoQueueMIB.setRevisions(('1995-08-21 00:00',))
class CQAlgorithm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fifo',1),('priority',2),('custom',3),('weightedFair',4)))
_CiscoQueueObjects_ObjectIdentity=ObjectIdentity
ciscoQueueObjects=_CiscoQueueObjects_ObjectIdentity((1,3,6,1,4,1,9,9,37,1))
_CQIfTable_Object=MibTable
cQIfTable=_CQIfTable_Object((1,3,6,1,4,1,9,9,37,1,1))
if mibBuilder.loadTexts:cQIfTable.setStatus(_A)
_CQIfEntry_Object=MibTableRow
cQIfEntry=_CQIfEntry_Object((1,3,6,1,4,1,9,9,37,1,1,1))
cQIfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cQIfEntry.setStatus(_A)
_CQIfQType_Type=CQAlgorithm
_CQIfQType_Object=MibTableColumn
cQIfQType=_CQIfQType_Object((1,3,6,1,4,1,9,9,37,1,1,1,1),_CQIfQType_Type())
cQIfQType.setMaxAccess(_C)
if mibBuilder.loadTexts:cQIfQType.setStatus(_A)
_CQIfTxLimit_Type=Integer32
_CQIfTxLimit_Object=MibTableColumn
cQIfTxLimit=_CQIfTxLimit_Object((1,3,6,1,4,1,9,9,37,1,1,1,2),_CQIfTxLimit_Type())
cQIfTxLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cQIfTxLimit.setStatus(_A)
_CQIfSubqueues_Type=Integer32
_CQIfSubqueues_Object=MibTableColumn
cQIfSubqueues=_CQIfSubqueues_Object((1,3,6,1,4,1,9,9,37,1,1,1,3),_CQIfSubqueues_Type())
cQIfSubqueues.setMaxAccess(_C)
if mibBuilder.loadTexts:cQIfSubqueues.setStatus(_A)
_CQStatsTable_Object=MibTable
cQStatsTable=_CQStatsTable_Object((1,3,6,1,4,1,9,9,37,1,2))
if mibBuilder.loadTexts:cQStatsTable.setStatus(_A)
_CQStatsEntry_Object=MibTableRow
cQStatsEntry=_CQStatsEntry_Object((1,3,6,1,4,1,9,9,37,1,2,1))
cQStatsEntry.setIndexNames((0,_D,_E),(0,_B,_F))
if mibBuilder.loadTexts:cQStatsEntry.setStatus(_A)
class _CQStatsQNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CQStatsQNumber_Type.__name__=_G
_CQStatsQNumber_Object=MibTableColumn
cQStatsQNumber=_CQStatsQNumber_Object((1,3,6,1,4,1,9,9,37,1,2,1,1),_CQStatsQNumber_Type())
cQStatsQNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cQStatsQNumber.setStatus(_A)
_CQStatsDepth_Type=Gauge32
_CQStatsDepth_Object=MibTableColumn
cQStatsDepth=_CQStatsDepth_Object((1,3,6,1,4,1,9,9,37,1,2,1,2),_CQStatsDepth_Type())
cQStatsDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:cQStatsDepth.setStatus(_A)
_CQStatsMaxDepth_Type=Integer32
_CQStatsMaxDepth_Object=MibTableColumn
cQStatsMaxDepth=_CQStatsMaxDepth_Object((1,3,6,1,4,1,9,9,37,1,2,1,3),_CQStatsMaxDepth_Type())
cQStatsMaxDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:cQStatsMaxDepth.setStatus(_A)
_CQStatsDiscards_Type=Counter32
_CQStatsDiscards_Object=MibTableColumn
cQStatsDiscards=_CQStatsDiscards_Object((1,3,6,1,4,1,9,9,37,1,2,1,4),_CQStatsDiscards_Type())
cQStatsDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:cQStatsDiscards.setStatus(_A)
_CQRotationTable_Object=MibTable
cQRotationTable=_CQRotationTable_Object((1,3,6,1,4,1,9,9,37,1,3))
if mibBuilder.loadTexts:cQRotationTable.setStatus(_A)
_CQRotationEntry_Object=MibTableRow
cQRotationEntry=_CQRotationEntry_Object((1,3,6,1,4,1,9,9,37,1,3,1))
cQRotationEntry.setIndexNames((0,_D,_E),(0,_B,_F))
if mibBuilder.loadTexts:cQRotationEntry.setStatus(_A)
_CQRotationOctets_Type=Integer32
_CQRotationOctets_Object=MibTableColumn
cQRotationOctets=_CQRotationOctets_Object((1,3,6,1,4,1,9,9,37,1,3,1,1),_CQRotationOctets_Type())
cQRotationOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cQRotationOctets.setStatus(_A)
_CiscoQueueTraps_ObjectIdentity=ObjectIdentity
ciscoQueueTraps=_CiscoQueueTraps_ObjectIdentity((1,3,6,1,4,1,9,9,37,2))
_CiscoQueueConformance_ObjectIdentity=ObjectIdentity
ciscoQueueConformance=_CiscoQueueConformance_ObjectIdentity((1,3,6,1,4,1,9,9,37,3))
_CQCompliances_ObjectIdentity=ObjectIdentity
cQCompliances=_CQCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,37,3,1))
_CQGroups_ObjectIdentity=ObjectIdentity
cQGroups=_CQGroups_ObjectIdentity((1,3,6,1,4,1,9,9,37,3,2))
cQIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,37,3,2,1))
cQIfGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cQIfGroup.setStatus(_A)
cQStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,37,3,2,2))
cQStatsGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:cQStatsGroup.setStatus(_A)
cQRotationGroup=ObjectGroup((1,3,6,1,4,1,9,9,37,3,2,3))
cQRotationGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:cQRotationGroup.setStatus(_A)
cQCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,37,3,1,1))
cQCompliance.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cQCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CQAlgorithm':CQAlgorithm,'ciscoQueueMIB':ciscoQueueMIB,'ciscoQueueObjects':ciscoQueueObjects,'cQIfTable':cQIfTable,'cQIfEntry':cQIfEntry,_H:cQIfQType,_I:cQIfTxLimit,_J:cQIfSubqueues,'cQStatsTable':cQStatsTable,'cQStatsEntry':cQStatsEntry,_F:cQStatsQNumber,_K:cQStatsDepth,_L:cQStatsMaxDepth,_M:cQStatsDiscards,'cQRotationTable':cQRotationTable,'cQRotationEntry':cQRotationEntry,_N:cQRotationOctets,'ciscoQueueTraps':ciscoQueueTraps,'ciscoQueueConformance':ciscoQueueConformance,'cQCompliances':cQCompliances,'cQCompliance':cQCompliance,'cQGroups':cQGroups,_O:cQIfGroup,_P:cQStatsGroup,_Q:cQRotationGroup})