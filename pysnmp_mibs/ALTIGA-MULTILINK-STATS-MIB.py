_Y='altigaMultiLinkStatsGroup'
_X='alMultiLinkStatsIdleTmrCleanup'
_W='alMultiLinkStatsRxOOSFragments'
_V='alMultiLinkStatsRxDroppedFragments'
_U='alMultiLinkStatsRxStaleFragments'
_T='alMultiLinkStatsRxStalePackets'
_S='alMultiLinkStatsRxLostEnd'
_R='alMultiLinkStatsRxThroughput'
_Q='alMultiLinkStatsRxNonMlpPackets'
_P='alMultiLinkStatsRxMlpPackets'
_O='alMultiLinkStatsRxMlpFragments'
_N='alMultiLinkStatsRxPackets'
_M='alMultiLinkStatsRxOctets'
_L='alMultiLinkStatsTxThroughput'
_K='alMultiLinkStatsTxNonMlpPackets'
_J='alMultiLinkStatsTxMlpPackets'
_I='alMultiLinkStatsTxMlpFragments'
_H='alMultiLinkStatsTxPackets'
_G='alMultiLinkStatsTxOctets'
_F='alMultiLinkStatsRowStatus'
_E='Integer32'
_D='alMultiLinkStatsIndex'
_C='read-only'
_B='ALTIGA-MULTILINK-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alMultiLinkMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alMultiLinkMibModule')
alMultiLinkGroup,alStatsMultiLink=mibBuilder.importSymbols('ALTIGA-MIB','alMultiLinkGroup','alStatsMultiLink')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
altigaMultiLinkStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,39,2))
if mibBuilder.loadTexts:altigaMultiLinkStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaMultiLinkStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaMultiLinkStatsMibConformance=_AltigaMultiLinkStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,39,2,1))
_AltigaMultiLinkStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaMultiLinkStatsMibCompliances=_AltigaMultiLinkStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,39,2,1,1))
_AlStatsMultiLinkGlobal_ObjectIdentity=ObjectIdentity
alStatsMultiLinkGlobal=_AlStatsMultiLinkGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,34,1))
_AlMultiLinkStatsTable_Object=MibTable
alMultiLinkStatsTable=_AlMultiLinkStatsTable_Object((1,3,6,1,4,1,3076,2,1,2,34,2))
if mibBuilder.loadTexts:alMultiLinkStatsTable.setStatus(_A)
_AlMultiLinkStatsEntry_Object=MibTableRow
alMultiLinkStatsEntry=_AlMultiLinkStatsEntry_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1))
alMultiLinkStatsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:alMultiLinkStatsEntry.setStatus(_A)
_AlMultiLinkStatsRowStatus_Type=RowStatus
_AlMultiLinkStatsRowStatus_Object=MibTableColumn
alMultiLinkStatsRowStatus=_AlMultiLinkStatsRowStatus_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,1),_AlMultiLinkStatsRowStatus_Type())
alMultiLinkStatsRowStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:alMultiLinkStatsRowStatus.setStatus(_A)
class _AlMultiLinkStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlMultiLinkStatsIndex_Type.__name__=_E
_AlMultiLinkStatsIndex_Object=MibTableColumn
alMultiLinkStatsIndex=_AlMultiLinkStatsIndex_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,2),_AlMultiLinkStatsIndex_Type())
alMultiLinkStatsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsIndex.setStatus(_A)
_AlMultiLinkStatsTxOctets_Type=Unsigned32
_AlMultiLinkStatsTxOctets_Object=MibTableColumn
alMultiLinkStatsTxOctets=_AlMultiLinkStatsTxOctets_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,3),_AlMultiLinkStatsTxOctets_Type())
alMultiLinkStatsTxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsTxOctets.setStatus(_A)
_AlMultiLinkStatsTxPackets_Type=Unsigned32
_AlMultiLinkStatsTxPackets_Object=MibTableColumn
alMultiLinkStatsTxPackets=_AlMultiLinkStatsTxPackets_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,4),_AlMultiLinkStatsTxPackets_Type())
alMultiLinkStatsTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsTxPackets.setStatus(_A)
_AlMultiLinkStatsTxMlpFragments_Type=Unsigned32
_AlMultiLinkStatsTxMlpFragments_Object=MibTableColumn
alMultiLinkStatsTxMlpFragments=_AlMultiLinkStatsTxMlpFragments_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,5),_AlMultiLinkStatsTxMlpFragments_Type())
alMultiLinkStatsTxMlpFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsTxMlpFragments.setStatus(_A)
_AlMultiLinkStatsTxMlpPackets_Type=Unsigned32
_AlMultiLinkStatsTxMlpPackets_Object=MibTableColumn
alMultiLinkStatsTxMlpPackets=_AlMultiLinkStatsTxMlpPackets_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,6),_AlMultiLinkStatsTxMlpPackets_Type())
alMultiLinkStatsTxMlpPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsTxMlpPackets.setStatus(_A)
_AlMultiLinkStatsTxNonMlpPackets_Type=Unsigned32
_AlMultiLinkStatsTxNonMlpPackets_Object=MibTableColumn
alMultiLinkStatsTxNonMlpPackets=_AlMultiLinkStatsTxNonMlpPackets_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,7),_AlMultiLinkStatsTxNonMlpPackets_Type())
alMultiLinkStatsTxNonMlpPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsTxNonMlpPackets.setStatus(_A)
_AlMultiLinkStatsTxThroughput_Type=Gauge32
_AlMultiLinkStatsTxThroughput_Object=MibTableColumn
alMultiLinkStatsTxThroughput=_AlMultiLinkStatsTxThroughput_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,8),_AlMultiLinkStatsTxThroughput_Type())
alMultiLinkStatsTxThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsTxThroughput.setStatus(_A)
_AlMultiLinkStatsRxOctets_Type=Unsigned32
_AlMultiLinkStatsRxOctets_Object=MibTableColumn
alMultiLinkStatsRxOctets=_AlMultiLinkStatsRxOctets_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,9),_AlMultiLinkStatsRxOctets_Type())
alMultiLinkStatsRxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsRxOctets.setStatus(_A)
_AlMultiLinkStatsRxPackets_Type=Unsigned32
_AlMultiLinkStatsRxPackets_Object=MibTableColumn
alMultiLinkStatsRxPackets=_AlMultiLinkStatsRxPackets_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,10),_AlMultiLinkStatsRxPackets_Type())
alMultiLinkStatsRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsRxPackets.setStatus(_A)
_AlMultiLinkStatsRxMlpFragments_Type=Unsigned32
_AlMultiLinkStatsRxMlpFragments_Object=MibTableColumn
alMultiLinkStatsRxMlpFragments=_AlMultiLinkStatsRxMlpFragments_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,11),_AlMultiLinkStatsRxMlpFragments_Type())
alMultiLinkStatsRxMlpFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsRxMlpFragments.setStatus(_A)
_AlMultiLinkStatsRxMlpPackets_Type=Unsigned32
_AlMultiLinkStatsRxMlpPackets_Object=MibTableColumn
alMultiLinkStatsRxMlpPackets=_AlMultiLinkStatsRxMlpPackets_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,12),_AlMultiLinkStatsRxMlpPackets_Type())
alMultiLinkStatsRxMlpPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsRxMlpPackets.setStatus(_A)
_AlMultiLinkStatsRxNonMlpPackets_Type=Unsigned32
_AlMultiLinkStatsRxNonMlpPackets_Object=MibTableColumn
alMultiLinkStatsRxNonMlpPackets=_AlMultiLinkStatsRxNonMlpPackets_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,13),_AlMultiLinkStatsRxNonMlpPackets_Type())
alMultiLinkStatsRxNonMlpPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsRxNonMlpPackets.setStatus(_A)
_AlMultiLinkStatsRxThroughput_Type=Gauge32
_AlMultiLinkStatsRxThroughput_Object=MibTableColumn
alMultiLinkStatsRxThroughput=_AlMultiLinkStatsRxThroughput_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,14),_AlMultiLinkStatsRxThroughput_Type())
alMultiLinkStatsRxThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsRxThroughput.setStatus(_A)
_AlMultiLinkStatsRxLostEnd_Type=Unsigned32
_AlMultiLinkStatsRxLostEnd_Object=MibTableColumn
alMultiLinkStatsRxLostEnd=_AlMultiLinkStatsRxLostEnd_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,15),_AlMultiLinkStatsRxLostEnd_Type())
alMultiLinkStatsRxLostEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsRxLostEnd.setStatus(_A)
_AlMultiLinkStatsRxStalePackets_Type=Unsigned32
_AlMultiLinkStatsRxStalePackets_Object=MibTableColumn
alMultiLinkStatsRxStalePackets=_AlMultiLinkStatsRxStalePackets_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,16),_AlMultiLinkStatsRxStalePackets_Type())
alMultiLinkStatsRxStalePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsRxStalePackets.setStatus(_A)
_AlMultiLinkStatsRxStaleFragments_Type=Unsigned32
_AlMultiLinkStatsRxStaleFragments_Object=MibTableColumn
alMultiLinkStatsRxStaleFragments=_AlMultiLinkStatsRxStaleFragments_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,17),_AlMultiLinkStatsRxStaleFragments_Type())
alMultiLinkStatsRxStaleFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsRxStaleFragments.setStatus(_A)
_AlMultiLinkStatsRxDroppedFragments_Type=Unsigned32
_AlMultiLinkStatsRxDroppedFragments_Object=MibTableColumn
alMultiLinkStatsRxDroppedFragments=_AlMultiLinkStatsRxDroppedFragments_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,18),_AlMultiLinkStatsRxDroppedFragments_Type())
alMultiLinkStatsRxDroppedFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsRxDroppedFragments.setStatus(_A)
_AlMultiLinkStatsRxOOSFragments_Type=Unsigned32
_AlMultiLinkStatsRxOOSFragments_Object=MibTableColumn
alMultiLinkStatsRxOOSFragments=_AlMultiLinkStatsRxOOSFragments_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,19),_AlMultiLinkStatsRxOOSFragments_Type())
alMultiLinkStatsRxOOSFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsRxOOSFragments.setStatus(_A)
_AlMultiLinkStatsIdleTmrCleanup_Type=Unsigned32
_AlMultiLinkStatsIdleTmrCleanup_Object=MibTableColumn
alMultiLinkStatsIdleTmrCleanup=_AlMultiLinkStatsIdleTmrCleanup_Object((1,3,6,1,4,1,3076,2,1,2,34,2,1,20),_AlMultiLinkStatsIdleTmrCleanup_Type())
alMultiLinkStatsIdleTmrCleanup.setMaxAccess(_C)
if mibBuilder.loadTexts:alMultiLinkStatsIdleTmrCleanup.setStatus(_A)
altigaMultiLinkStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,34,2))
altigaMultiLinkStatsGroup.setObjects(*((_B,_F),(_B,_D),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:altigaMultiLinkStatsGroup.setStatus(_A)
altigaMultiLinkStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,39,2,1,1,1))
altigaMultiLinkStatsMibCompliance.setObjects((_B,_Y))
if mibBuilder.loadTexts:altigaMultiLinkStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaMultiLinkStatsMibModule':altigaMultiLinkStatsMibModule,'altigaMultiLinkStatsMibConformance':altigaMultiLinkStatsMibConformance,'altigaMultiLinkStatsMibCompliances':altigaMultiLinkStatsMibCompliances,'altigaMultiLinkStatsMibCompliance':altigaMultiLinkStatsMibCompliance,_Y:altigaMultiLinkStatsGroup,'alStatsMultiLinkGlobal':alStatsMultiLinkGlobal,'alMultiLinkStatsTable':alMultiLinkStatsTable,'alMultiLinkStatsEntry':alMultiLinkStatsEntry,_F:alMultiLinkStatsRowStatus,_D:alMultiLinkStatsIndex,_G:alMultiLinkStatsTxOctets,_H:alMultiLinkStatsTxPackets,_I:alMultiLinkStatsTxMlpFragments,_J:alMultiLinkStatsTxMlpPackets,_K:alMultiLinkStatsTxNonMlpPackets,_L:alMultiLinkStatsTxThroughput,_M:alMultiLinkStatsRxOctets,_N:alMultiLinkStatsRxPackets,_O:alMultiLinkStatsRxMlpFragments,_P:alMultiLinkStatsRxMlpPackets,_Q:alMultiLinkStatsRxNonMlpPackets,_R:alMultiLinkStatsRxThroughput,_S:alMultiLinkStatsRxLostEnd,_T:alMultiLinkStatsRxStalePackets,_U:alMultiLinkStatsRxStaleFragments,_V:alMultiLinkStatsRxDroppedFragments,_W:alMultiLinkStatsRxOOSFragments,_X:alMultiLinkStatsIdleTmrCleanup})