_O='sonetClockTransmitSource'
_N='sonetClockExternalRecovery'
_M='sonetMediumExtEntry'
_L='sonetClockEntry'
_K='zhoneSonetErrorStatsIndex'
_J='sonetSectionCurrentStatus'
_I='sonetPathCurrentStatus'
_H='sonetLineCurrentStatus'
_G='TruthValue'
_F='Integer32'
_E='read-write'
_D='SONET-MIB'
_C='ZHONE-PHY-SONET-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_G)
sonetLineCurrentStatus,sonetMediumEntry,sonetPathCurrentStatus,sonetSectionCurrentStatus=mibBuilder.importSymbols(_D,_H,'sonetMediumEntry',_I,_J)
zhoneModules,zhoneSonet=mibBuilder.importSymbols('Zhone','zhoneModules','zhoneSonet')
phySonet=ModuleIdentity((1,3,6,1,4,1,5504,6,16))
if mibBuilder.loadTexts:phySonet.setRevisions(('2004-08-18 11:47','2003-07-10 13:30','2002-03-26 14:30','2001-09-12 15:08','2001-07-19 18:00','2001-02-22 11:35','2000-12-19 15:23','2000-12-18 16:20'))
_SonetClockTable_Object=MibTable
sonetClockTable=_SonetClockTable_Object((1,3,6,1,4,1,5504,5,9,1))
if mibBuilder.loadTexts:sonetClockTable.setStatus(_A)
_SonetClockEntry_Object=MibTableRow
sonetClockEntry=_SonetClockEntry_Object((1,3,6,1,4,1,5504,5,9,1,1))
if mibBuilder.loadTexts:sonetClockEntry.setStatus(_A)
class _SonetClockExternalRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SonetClockExternalRecovery_Type.__name__=_F
_SonetClockExternalRecovery_Object=MibTableColumn
sonetClockExternalRecovery=_SonetClockExternalRecovery_Object((1,3,6,1,4,1,5504,5,9,1,1,1),_SonetClockExternalRecovery_Type())
sonetClockExternalRecovery.setMaxAccess(_E)
if mibBuilder.loadTexts:sonetClockExternalRecovery.setStatus(_A)
class _SonetClockTransmitSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('loopTiming',1),('throughTiming',2),('localTiming',3),('external155MHz',4)))
_SonetClockTransmitSource_Type.__name__=_F
_SonetClockTransmitSource_Object=MibTableColumn
sonetClockTransmitSource=_SonetClockTransmitSource_Object((1,3,6,1,4,1,5504,5,9,1,1,2),_SonetClockTransmitSource_Type())
sonetClockTransmitSource.setMaxAccess(_E)
if mibBuilder.loadTexts:sonetClockTransmitSource.setStatus(_A)
_SonetMediumExtTable_Object=MibTable
sonetMediumExtTable=_SonetMediumExtTable_Object((1,3,6,1,4,1,5504,5,9,2))
if mibBuilder.loadTexts:sonetMediumExtTable.setStatus(_A)
_SonetMediumExtEntry_Object=MibTableRow
sonetMediumExtEntry=_SonetMediumExtEntry_Object((1,3,6,1,4,1,5504,5,9,2,1))
if mibBuilder.loadTexts:sonetMediumExtEntry.setStatus(_A)
class _SonetMediumExtScrambleEnabled_Type(TruthValue):defaultValue=1
_SonetMediumExtScrambleEnabled_Type.__name__=_G
_SonetMediumExtScrambleEnabled_Object=MibTableColumn
sonetMediumExtScrambleEnabled=_SonetMediumExtScrambleEnabled_Object((1,3,6,1,4,1,5504,5,9,2,1,1),_SonetMediumExtScrambleEnabled_Type())
sonetMediumExtScrambleEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:sonetMediumExtScrambleEnabled.setStatus(_A)
class _SonetMediumExtLineScrmEnabled_Type(TruthValue):defaultValue=1
_SonetMediumExtLineScrmEnabled_Type.__name__=_G
_SonetMediumExtLineScrmEnabled_Object=MibTableColumn
sonetMediumExtLineScrmEnabled=_SonetMediumExtLineScrmEnabled_Object((1,3,6,1,4,1,5504,5,9,2,1,2),_SonetMediumExtLineScrmEnabled_Type())
sonetMediumExtLineScrmEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:sonetMediumExtLineScrmEnabled.setStatus(_A)
_SonetTraps_ObjectIdentity=ObjectIdentity
sonetTraps=_SonetTraps_ObjectIdentity((1,3,6,1,4,1,5504,5,9,3))
if mibBuilder.loadTexts:sonetTraps.setStatus(_A)
_SonetV2Traps_ObjectIdentity=ObjectIdentity
sonetV2Traps=_SonetV2Traps_ObjectIdentity((1,3,6,1,4,1,5504,5,9,3,0))
if mibBuilder.loadTexts:sonetV2Traps.setStatus(_A)
_ZhoneSonetErrorStatsTable_Object=MibTable
zhoneSonetErrorStatsTable=_ZhoneSonetErrorStatsTable_Object((1,3,6,1,4,1,5504,5,9,6))
if mibBuilder.loadTexts:zhoneSonetErrorStatsTable.setStatus(_A)
_ZhoneSonetErrorStatsEntry_Object=MibTableRow
zhoneSonetErrorStatsEntry=_ZhoneSonetErrorStatsEntry_Object((1,3,6,1,4,1,5504,5,9,6,1))
zhoneSonetErrorStatsEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:zhoneSonetErrorStatsEntry.setStatus(_A)
_ZhoneSonetErrorStatsIndex_Type=InterfaceIndex
_ZhoneSonetErrorStatsIndex_Object=MibTableColumn
zhoneSonetErrorStatsIndex=_ZhoneSonetErrorStatsIndex_Object((1,3,6,1,4,1,5504,5,9,6,1,1),_ZhoneSonetErrorStatsIndex_Type())
zhoneSonetErrorStatsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zhoneSonetErrorStatsIndex.setStatus(_A)
_ZhoneSonetErrorStatsLineFebeCount_Type=Integer32
_ZhoneSonetErrorStatsLineFebeCount_Object=MibTableColumn
zhoneSonetErrorStatsLineFebeCount=_ZhoneSonetErrorStatsLineFebeCount_Object((1,3,6,1,4,1,5504,5,9,6,1,2),_ZhoneSonetErrorStatsLineFebeCount_Type())
zhoneSonetErrorStatsLineFebeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneSonetErrorStatsLineFebeCount.setStatus(_A)
_ZhoneSonetErrorStatsPathFebeCount_Type=Integer32
_ZhoneSonetErrorStatsPathFebeCount_Object=MibTableColumn
zhoneSonetErrorStatsPathFebeCount=_ZhoneSonetErrorStatsPathFebeCount_Object((1,3,6,1,4,1,5504,5,9,6,1,3),_ZhoneSonetErrorStatsPathFebeCount_Type())
zhoneSonetErrorStatsPathFebeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneSonetErrorStatsPathFebeCount.setStatus(_A)
_ZhoneSonetErrorStatsLineBipCount_Type=Integer32
_ZhoneSonetErrorStatsLineBipCount_Object=MibTableColumn
zhoneSonetErrorStatsLineBipCount=_ZhoneSonetErrorStatsLineBipCount_Object((1,3,6,1,4,1,5504,5,9,6,1,4),_ZhoneSonetErrorStatsLineBipCount_Type())
zhoneSonetErrorStatsLineBipCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneSonetErrorStatsLineBipCount.setStatus(_A)
_ZhoneSonetErrorStatsSectionBipCount_Type=Integer32
_ZhoneSonetErrorStatsSectionBipCount_Object=MibTableColumn
zhoneSonetErrorStatsSectionBipCount=_ZhoneSonetErrorStatsSectionBipCount_Object((1,3,6,1,4,1,5504,5,9,6,1,5),_ZhoneSonetErrorStatsSectionBipCount_Type())
zhoneSonetErrorStatsSectionBipCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneSonetErrorStatsSectionBipCount.setStatus(_A)
_ZhoneSonetErrorStatsPathBipCount_Type=Integer32
_ZhoneSonetErrorStatsPathBipCount_Object=MibTableColumn
zhoneSonetErrorStatsPathBipCount=_ZhoneSonetErrorStatsPathBipCount_Object((1,3,6,1,4,1,5504,5,9,6,1,6),_ZhoneSonetErrorStatsPathBipCount_Type())
zhoneSonetErrorStatsPathBipCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneSonetErrorStatsPathBipCount.setStatus(_A)
_ZhoneSonetErrorStatsOofCount_Type=Integer32
_ZhoneSonetErrorStatsOofCount_Object=MibTableColumn
zhoneSonetErrorStatsOofCount=_ZhoneSonetErrorStatsOofCount_Object((1,3,6,1,4,1,5504,5,9,6,1,7),_ZhoneSonetErrorStatsOofCount_Type())
zhoneSonetErrorStatsOofCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneSonetErrorStatsOofCount.setStatus(_A)
_ZhoneSonetErrorStatsRxCellCount_Type=Integer32
_ZhoneSonetErrorStatsRxCellCount_Object=MibTableColumn
zhoneSonetErrorStatsRxCellCount=_ZhoneSonetErrorStatsRxCellCount_Object((1,3,6,1,4,1,5504,5,9,6,1,8),_ZhoneSonetErrorStatsRxCellCount_Type())
zhoneSonetErrorStatsRxCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneSonetErrorStatsRxCellCount.setStatus(_A)
_ZhoneSonetErrorStatsTxCellCount_Type=Integer32
_ZhoneSonetErrorStatsTxCellCount_Object=MibTableColumn
zhoneSonetErrorStatsTxCellCount=_ZhoneSonetErrorStatsTxCellCount_Object((1,3,6,1,4,1,5504,5,9,6,1,9),_ZhoneSonetErrorStatsTxCellCount_Type())
zhoneSonetErrorStatsTxCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneSonetErrorStatsTxCellCount.setStatus(_A)
_ZhoneSonetErrorStatsHecCorrectedCount_Type=Integer32
_ZhoneSonetErrorStatsHecCorrectedCount_Object=MibTableColumn
zhoneSonetErrorStatsHecCorrectedCount=_ZhoneSonetErrorStatsHecCorrectedCount_Object((1,3,6,1,4,1,5504,5,9,6,1,10),_ZhoneSonetErrorStatsHecCorrectedCount_Type())
zhoneSonetErrorStatsHecCorrectedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneSonetErrorStatsHecCorrectedCount.setStatus(_A)
_ZhoneSonetErrorStatsHecUncorrectedCount_Type=Integer32
_ZhoneSonetErrorStatsHecUncorrectedCount_Object=MibTableColumn
zhoneSonetErrorStatsHecUncorrectedCount=_ZhoneSonetErrorStatsHecUncorrectedCount_Object((1,3,6,1,4,1,5504,5,9,6,1,11),_ZhoneSonetErrorStatsHecUncorrectedCount_Type())
zhoneSonetErrorStatsHecUncorrectedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneSonetErrorStatsHecUncorrectedCount.setStatus(_A)
_ZhoneSonetErrorStatsCellFifoOverflowCount_Type=Integer32
_ZhoneSonetErrorStatsCellFifoOverflowCount_Object=MibTableColumn
zhoneSonetErrorStatsCellFifoOverflowCount=_ZhoneSonetErrorStatsCellFifoOverflowCount_Object((1,3,6,1,4,1,5504,5,9,6,1,12),_ZhoneSonetErrorStatsCellFifoOverflowCount_Type())
zhoneSonetErrorStatsCellFifoOverflowCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneSonetErrorStatsCellFifoOverflowCount.setStatus(_A)
_ZhoneSonetErrorStatsLocdCount_Type=Integer32
_ZhoneSonetErrorStatsLocdCount_Object=MibTableColumn
zhoneSonetErrorStatsLocdCount=_ZhoneSonetErrorStatsLocdCount_Object((1,3,6,1,4,1,5504,5,9,6,1,13),_ZhoneSonetErrorStatsLocdCount_Type())
zhoneSonetErrorStatsLocdCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneSonetErrorStatsLocdCount.setStatus(_A)
sonetMediumEntry.registerAugmentions((_C,_L))
sonetClockEntry.setIndexNames(*sonetMediumEntry.getIndexNames())
sonetMediumEntry.registerAugmentions((_C,_M))
sonetMediumExtEntry.setIndexNames(*sonetMediumEntry.getIndexNames())
sonetClockTransmitSourceChange=NotificationType((1,3,6,1,4,1,5504,5,9,3,0,1))
sonetClockTransmitSourceChange.setObjects(*((_C,_N),(_C,_O)))
if mibBuilder.loadTexts:sonetClockTransmitSourceChange.setStatus(_A)
sonetSectionStatusChange=NotificationType((1,3,6,1,4,1,5504,5,9,3,0,2))
sonetSectionStatusChange.setObjects((_D,_J))
if mibBuilder.loadTexts:sonetSectionStatusChange.setStatus(_A)
sonetLineStatusChange=NotificationType((1,3,6,1,4,1,5504,5,9,3,0,3))
sonetLineStatusChange.setObjects((_D,_H))
if mibBuilder.loadTexts:sonetLineStatusChange.setStatus(_A)
sonetPathStatusChange=NotificationType((1,3,6,1,4,1,5504,5,9,3,0,4))
sonetPathStatusChange.setObjects((_D,_I))
if mibBuilder.loadTexts:sonetPathStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'sonetClockTable':sonetClockTable,_L:sonetClockEntry,_N:sonetClockExternalRecovery,_O:sonetClockTransmitSource,'sonetMediumExtTable':sonetMediumExtTable,_M:sonetMediumExtEntry,'sonetMediumExtScrambleEnabled':sonetMediumExtScrambleEnabled,'sonetMediumExtLineScrmEnabled':sonetMediumExtLineScrmEnabled,'sonetTraps':sonetTraps,'sonetV2Traps':sonetV2Traps,'sonetClockTransmitSourceChange':sonetClockTransmitSourceChange,'sonetSectionStatusChange':sonetSectionStatusChange,'sonetLineStatusChange':sonetLineStatusChange,'sonetPathStatusChange':sonetPathStatusChange,'zhoneSonetErrorStatsTable':zhoneSonetErrorStatsTable,'zhoneSonetErrorStatsEntry':zhoneSonetErrorStatsEntry,_K:zhoneSonetErrorStatsIndex,'zhoneSonetErrorStatsLineFebeCount':zhoneSonetErrorStatsLineFebeCount,'zhoneSonetErrorStatsPathFebeCount':zhoneSonetErrorStatsPathFebeCount,'zhoneSonetErrorStatsLineBipCount':zhoneSonetErrorStatsLineBipCount,'zhoneSonetErrorStatsSectionBipCount':zhoneSonetErrorStatsSectionBipCount,'zhoneSonetErrorStatsPathBipCount':zhoneSonetErrorStatsPathBipCount,'zhoneSonetErrorStatsOofCount':zhoneSonetErrorStatsOofCount,'zhoneSonetErrorStatsRxCellCount':zhoneSonetErrorStatsRxCellCount,'zhoneSonetErrorStatsTxCellCount':zhoneSonetErrorStatsTxCellCount,'zhoneSonetErrorStatsHecCorrectedCount':zhoneSonetErrorStatsHecCorrectedCount,'zhoneSonetErrorStatsHecUncorrectedCount':zhoneSonetErrorStatsHecUncorrectedCount,'zhoneSonetErrorStatsCellFifoOverflowCount':zhoneSonetErrorStatsCellFifoOverflowCount,'zhoneSonetErrorStatsLocdCount':zhoneSonetErrorStatsLocdCount,'phySonet':phySonet})