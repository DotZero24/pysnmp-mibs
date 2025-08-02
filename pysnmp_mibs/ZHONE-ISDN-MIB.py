_L='isdnAlarmProfileEntry'
_K='isdnPerfDataTotalEntry'
_J='isdnPerfDataPreviousEntry'
_I='isdnPerfDataCurrentEntry'
_H='ZHONE-ISDN-MIB'
_G='ifIndex'
_F='IF-MIB'
_E='seconds'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zhonePhysical,zhoneTrapModules=mibBuilder.importSymbols('Zhone','zhonePhysical','zhoneTrapModules')
zhoneIsdn=ModuleIdentity((1,3,6,1,4,1,5504,5,7))
if mibBuilder.loadTexts:zhoneIsdn.setRevisions(('2003-03-03 11:58','2003-02-04 18:04','2000-09-27 10:57','2000-09-27 19:42'))
_ZhoneIsdnTrap_ObjectIdentity=ObjectIdentity
zhoneIsdnTrap=_ZhoneIsdnTrap_ObjectIdentity((1,3,6,1,4,1,5504,3,8,3))
if mibBuilder.loadTexts:zhoneIsdnTrap.setStatus(_A)
_IsdnMibV2Traps_ObjectIdentity=ObjectIdentity
isdnMibV2Traps=_IsdnMibV2Traps_ObjectIdentity((1,3,6,1,4,1,5504,3,8,3,1))
if mibBuilder.loadTexts:isdnMibV2Traps.setStatus(_A)
_ZhoneIsdnMib_ObjectIdentity=ObjectIdentity
zhoneIsdnMib=_ZhoneIsdnMib_ObjectIdentity((1,3,6,1,4,1,5504,5,7,1))
_IsdnConfigTable_Object=MibTable
isdnConfigTable=_IsdnConfigTable_Object((1,3,6,1,4,1,5504,5,7,1,1))
if mibBuilder.loadTexts:isdnConfigTable.setStatus(_A)
_IsdnConfigEntry_Object=MibTableRow
isdnConfigEntry=_IsdnConfigEntry_Object((1,3,6,1,4,1,5504,5,7,1,1,1))
isdnConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:isdnConfigEntry.setStatus(_A)
class _IsdnLineTermClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('class1',1),('class2',2)))
_IsdnLineTermClass_Type.__name__=_C
_IsdnLineTermClass_Object=MibTableColumn
isdnLineTermClass=_IsdnLineTermClass_Object((1,3,6,1,4,1,5504,5,7,1,1,1,1),_IsdnLineTermClass_Type())
isdnLineTermClass.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnLineTermClass.setStatus(_A)
class _IsdnActivationTimer2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('t2-50ms',1),('t2-100ms',2)))
_IsdnActivationTimer2_Type.__name__=_C
_IsdnActivationTimer2_Object=MibTableColumn
isdnActivationTimer2=_IsdnActivationTimer2_Object((1,3,6,1,4,1,5504,5,7,1,1,1,2),_IsdnActivationTimer2_Type())
isdnActivationTimer2.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnActivationTimer2.setStatus(_A)
class _IsdnLineLoopBack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('loop-back-none',1),('loop-back-b1-st-tr',2),('loop-back-b1-st-nt',3),('loop-back-b2-st-tr',4),('loop-back-b2-st-nt',5),('loop-back-b1-idl2-tr',6),('loop-back-b1-idl2-nt',7),('loop-back-b2-idl2-tr',8),('loop-back-b2-idl2-nt',9),('loop-back-2bd-idl2-tr',10),('loop-back-2bd-idl2-nt',11),('loop-back-2bd-u-interface-tr',12),('loop-back-2bd-u-interface-nt',13),('loop-back-2bd-external-analog',14)))
_IsdnLineLoopBack_Type.__name__=_C
_IsdnLineLoopBack_Object=MibTableColumn
isdnLineLoopBack=_IsdnLineLoopBack_Object((1,3,6,1,4,1,5504,5,7,1,1,1,3),_IsdnLineLoopBack_Type())
isdnLineLoopBack.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnLineLoopBack.setStatus(_A)
class _IsdnLinePower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('sealing',2),('powering',3)))
_IsdnLinePower_Type.__name__=_C
_IsdnLinePower_Object=MibTableColumn
isdnLinePower=_IsdnLinePower_Object((1,3,6,1,4,1,5504,5,7,1,1,1,4),_IsdnLinePower_Type())
isdnLinePower.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnLinePower.setStatus(_A)
_IsdnPerfDataCurrentTable_Object=MibTable
isdnPerfDataCurrentTable=_IsdnPerfDataCurrentTable_Object((1,3,6,1,4,1,5504,5,7,1,2))
if mibBuilder.loadTexts:isdnPerfDataCurrentTable.setStatus(_A)
_IsdnPerfDataCurrentEntry_Object=MibTableRow
isdnPerfDataCurrentEntry=_IsdnPerfDataCurrentEntry_Object((1,3,6,1,4,1,5504,5,7,1,2,1))
if mibBuilder.loadTexts:isdnPerfDataCurrentEntry.setStatus(_A)
_IsdnPerfCurBadAmiViolation_Type=PerfCurrentCount
_IsdnPerfCurBadAmiViolation_Object=MibTableColumn
isdnPerfCurBadAmiViolation=_IsdnPerfCurBadAmiViolation_Object((1,3,6,1,4,1,5504,5,7,1,2,1,1),_IsdnPerfCurBadAmiViolation_Type())
isdnPerfCurBadAmiViolation.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerfCurBadAmiViolation.setStatus(_A)
_IsdnPerfCurUnbalancedFrame_Type=PerfCurrentCount
_IsdnPerfCurUnbalancedFrame_Object=MibTableColumn
isdnPerfCurUnbalancedFrame=_IsdnPerfCurUnbalancedFrame_Object((1,3,6,1,4,1,5504,5,7,1,2,1,2),_IsdnPerfCurUnbalancedFrame_Type())
isdnPerfCurUnbalancedFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerfCurUnbalancedFrame.setStatus(_A)
_IsdnPerCurErrorSeconds_Type=PerfCurrentCount
_IsdnPerCurErrorSeconds_Object=MibTableColumn
isdnPerCurErrorSeconds=_IsdnPerCurErrorSeconds_Object((1,3,6,1,4,1,5504,5,7,1,2,1,3),_IsdnPerCurErrorSeconds_Type())
isdnPerCurErrorSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerCurErrorSeconds.setStatus(_A)
if mibBuilder.loadTexts:isdnPerCurErrorSeconds.setUnits(_E)
_IsdnPerCurFsyncSeconds_Type=PerfCurrentCount
_IsdnPerCurFsyncSeconds_Object=MibTableColumn
isdnPerCurFsyncSeconds=_IsdnPerCurFsyncSeconds_Object((1,3,6,1,4,1,5504,5,7,1,2,1,4),_IsdnPerCurFsyncSeconds_Type())
isdnPerCurFsyncSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerCurFsyncSeconds.setStatus(_A)
if mibBuilder.loadTexts:isdnPerCurFsyncSeconds.setUnits(_E)
_IsdnPerfCurTimeElapsed_Type=TimeTicks
_IsdnPerfCurTimeElapsed_Object=MibTableColumn
isdnPerfCurTimeElapsed=_IsdnPerfCurTimeElapsed_Object((1,3,6,1,4,1,5504,5,7,1,2,1,5),_IsdnPerfCurTimeElapsed_Type())
isdnPerfCurTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerfCurTimeElapsed.setStatus(_A)
_IsdnPerfDataPreviousTable_Object=MibTable
isdnPerfDataPreviousTable=_IsdnPerfDataPreviousTable_Object((1,3,6,1,4,1,5504,5,7,1,3))
if mibBuilder.loadTexts:isdnPerfDataPreviousTable.setStatus(_A)
_IsdnPerfDataPreviousEntry_Object=MibTableRow
isdnPerfDataPreviousEntry=_IsdnPerfDataPreviousEntry_Object((1,3,6,1,4,1,5504,5,7,1,3,1))
if mibBuilder.loadTexts:isdnPerfDataPreviousEntry.setStatus(_A)
_IsdnPerfPrevBadAmiViolation_Type=PerfIntervalCount
_IsdnPerfPrevBadAmiViolation_Object=MibTableColumn
isdnPerfPrevBadAmiViolation=_IsdnPerfPrevBadAmiViolation_Object((1,3,6,1,4,1,5504,5,7,1,3,1,1),_IsdnPerfPrevBadAmiViolation_Type())
isdnPerfPrevBadAmiViolation.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerfPrevBadAmiViolation.setStatus(_A)
_IsdnPerfPrevUnbalancedFrame_Type=PerfIntervalCount
_IsdnPerfPrevUnbalancedFrame_Object=MibTableColumn
isdnPerfPrevUnbalancedFrame=_IsdnPerfPrevUnbalancedFrame_Object((1,3,6,1,4,1,5504,5,7,1,3,1,2),_IsdnPerfPrevUnbalancedFrame_Type())
isdnPerfPrevUnbalancedFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerfPrevUnbalancedFrame.setStatus(_A)
_IsdnPerPrevFsyncSeconds_Type=PerfIntervalCount
_IsdnPerPrevFsyncSeconds_Object=MibTableColumn
isdnPerPrevFsyncSeconds=_IsdnPerPrevFsyncSeconds_Object((1,3,6,1,4,1,5504,5,7,1,3,1,3),_IsdnPerPrevFsyncSeconds_Type())
isdnPerPrevFsyncSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerPrevFsyncSeconds.setStatus(_A)
if mibBuilder.loadTexts:isdnPerPrevFsyncSeconds.setUnits(_E)
_IsdnPerfPrevErrorSeconds_Type=PerfIntervalCount
_IsdnPerfPrevErrorSeconds_Object=MibTableColumn
isdnPerfPrevErrorSeconds=_IsdnPerfPrevErrorSeconds_Object((1,3,6,1,4,1,5504,5,7,1,3,1,4),_IsdnPerfPrevErrorSeconds_Type())
isdnPerfPrevErrorSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerfPrevErrorSeconds.setStatus(_A)
if mibBuilder.loadTexts:isdnPerfPrevErrorSeconds.setUnits(_E)
_IsdnPerfDataTotalTable_Object=MibTable
isdnPerfDataTotalTable=_IsdnPerfDataTotalTable_Object((1,3,6,1,4,1,5504,5,7,1,4))
if mibBuilder.loadTexts:isdnPerfDataTotalTable.setStatus(_A)
_IsdnPerfDataTotalEntry_Object=MibTableRow
isdnPerfDataTotalEntry=_IsdnPerfDataTotalEntry_Object((1,3,6,1,4,1,5504,5,7,1,4,1))
if mibBuilder.loadTexts:isdnPerfDataTotalEntry.setStatus(_A)
_IsdnPerfTotalBadAmiViolation_Type=PerfTotalCount
_IsdnPerfTotalBadAmiViolation_Object=MibTableColumn
isdnPerfTotalBadAmiViolation=_IsdnPerfTotalBadAmiViolation_Object((1,3,6,1,4,1,5504,5,7,1,4,1,1),_IsdnPerfTotalBadAmiViolation_Type())
isdnPerfTotalBadAmiViolation.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerfTotalBadAmiViolation.setStatus(_A)
_IsdnPerfTotalUnbalancedFrame_Type=PerfTotalCount
_IsdnPerfTotalUnbalancedFrame_Object=MibTableColumn
isdnPerfTotalUnbalancedFrame=_IsdnPerfTotalUnbalancedFrame_Object((1,3,6,1,4,1,5504,5,7,1,4,1,2),_IsdnPerfTotalUnbalancedFrame_Type())
isdnPerfTotalUnbalancedFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerfTotalUnbalancedFrame.setStatus(_A)
_IsdnPerTotalFsyncSeconds_Type=PerfTotalCount
_IsdnPerTotalFsyncSeconds_Object=MibTableColumn
isdnPerTotalFsyncSeconds=_IsdnPerTotalFsyncSeconds_Object((1,3,6,1,4,1,5504,5,7,1,4,1,3),_IsdnPerTotalFsyncSeconds_Type())
isdnPerTotalFsyncSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerTotalFsyncSeconds.setStatus(_A)
if mibBuilder.loadTexts:isdnPerTotalFsyncSeconds.setUnits(_E)
_IsdnPerfTotalErrorSeconds_Type=PerfTotalCount
_IsdnPerfTotalErrorSeconds_Object=MibTableColumn
isdnPerfTotalErrorSeconds=_IsdnPerfTotalErrorSeconds_Object((1,3,6,1,4,1,5504,5,7,1,4,1,4),_IsdnPerfTotalErrorSeconds_Type())
isdnPerfTotalErrorSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerfTotalErrorSeconds.setStatus(_A)
if mibBuilder.loadTexts:isdnPerfTotalErrorSeconds.setUnits(_E)
class _IsdnPerfTotalTimePeriodsElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_IsdnPerfTotalTimePeriodsElapsed_Type.__name__=_C
_IsdnPerfTotalTimePeriodsElapsed_Object=MibTableColumn
isdnPerfTotalTimePeriodsElapsed=_IsdnPerfTotalTimePeriodsElapsed_Object((1,3,6,1,4,1,5504,5,7,1,4,1,5),_IsdnPerfTotalTimePeriodsElapsed_Type())
isdnPerfTotalTimePeriodsElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:isdnPerfTotalTimePeriodsElapsed.setStatus(_A)
_IsdnAlarmProfileTable_Object=MibTable
isdnAlarmProfileTable=_IsdnAlarmProfileTable_Object((1,3,6,1,4,1,5504,5,7,1,5))
if mibBuilder.loadTexts:isdnAlarmProfileTable.setStatus(_A)
_IsdnAlarmProfileEntry_Object=MibTableRow
isdnAlarmProfileEntry=_IsdnAlarmProfileEntry_Object((1,3,6,1,4,1,5504,5,7,1,5,1))
if mibBuilder.loadTexts:isdnAlarmProfileEntry.setStatus(_A)
_IsdnThresholdAmiViolations_Type=Unsigned32
_IsdnThresholdAmiViolations_Object=MibTableColumn
isdnThresholdAmiViolations=_IsdnThresholdAmiViolations_Object((1,3,6,1,4,1,5504,5,7,1,5,1,1),_IsdnThresholdAmiViolations_Type())
isdnThresholdAmiViolations.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnThresholdAmiViolations.setStatus(_A)
_IsdnThresholdUnbalancedFrame_Type=Unsigned32
_IsdnThresholdUnbalancedFrame_Object=MibTableColumn
isdnThresholdUnbalancedFrame=_IsdnThresholdUnbalancedFrame_Object((1,3,6,1,4,1,5504,5,7,1,5,1,2),_IsdnThresholdUnbalancedFrame_Type())
isdnThresholdUnbalancedFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:isdnThresholdUnbalancedFrame.setStatus(_A)
isdnConfigEntry.registerAugmentions((_H,_I))
isdnPerfDataCurrentEntry.setIndexNames(*isdnConfigEntry.getIndexNames())
isdnConfigEntry.registerAugmentions((_H,_J))
isdnPerfDataPreviousEntry.setIndexNames(*isdnConfigEntry.getIndexNames())
isdnConfigEntry.registerAugmentions((_H,_K))
isdnPerfDataTotalEntry.setIndexNames(*isdnConfigEntry.getIndexNames())
isdnConfigEntry.registerAugmentions((_H,_L))
isdnAlarmProfileEntry.setIndexNames(*isdnConfigEntry.getIndexNames())
isdnTrapFrameSynchLoss=NotificationType((1,3,6,1,4,1,5504,3,8,3,1,1))
isdnTrapFrameSynchLoss.setObjects((_F,_G))
if mibBuilder.loadTexts:isdnTrapFrameSynchLoss.setStatus(_A)
isdnTrapFECV=NotificationType((1,3,6,1,4,1,5504,3,8,3,1,2))
isdnTrapFECV.setObjects((_F,_G))
if mibBuilder.loadTexts:isdnTrapFECV.setStatus(_A)
isdnTrapAmiViolations=NotificationType((1,3,6,1,4,1,5504,3,8,3,1,3))
isdnTrapAmiViolations.setObjects((_F,_G))
if mibBuilder.loadTexts:isdnTrapAmiViolations.setStatus(_A)
isdnTrapUnbalancedFrame=NotificationType((1,3,6,1,4,1,5504,3,8,3,1,4))
if mibBuilder.loadTexts:isdnTrapUnbalancedFrame.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'zhoneIsdnTrap':zhoneIsdnTrap,'isdnMibV2Traps':isdnMibV2Traps,'isdnTrapFrameSynchLoss':isdnTrapFrameSynchLoss,'isdnTrapFECV':isdnTrapFECV,'isdnTrapAmiViolations':isdnTrapAmiViolations,'isdnTrapUnbalancedFrame':isdnTrapUnbalancedFrame,'zhoneIsdn':zhoneIsdn,'zhoneIsdnMib':zhoneIsdnMib,'isdnConfigTable':isdnConfigTable,'isdnConfigEntry':isdnConfigEntry,'isdnLineTermClass':isdnLineTermClass,'isdnActivationTimer2':isdnActivationTimer2,'isdnLineLoopBack':isdnLineLoopBack,'isdnLinePower':isdnLinePower,'isdnPerfDataCurrentTable':isdnPerfDataCurrentTable,_I:isdnPerfDataCurrentEntry,'isdnPerfCurBadAmiViolation':isdnPerfCurBadAmiViolation,'isdnPerfCurUnbalancedFrame':isdnPerfCurUnbalancedFrame,'isdnPerCurErrorSeconds':isdnPerCurErrorSeconds,'isdnPerCurFsyncSeconds':isdnPerCurFsyncSeconds,'isdnPerfCurTimeElapsed':isdnPerfCurTimeElapsed,'isdnPerfDataPreviousTable':isdnPerfDataPreviousTable,_J:isdnPerfDataPreviousEntry,'isdnPerfPrevBadAmiViolation':isdnPerfPrevBadAmiViolation,'isdnPerfPrevUnbalancedFrame':isdnPerfPrevUnbalancedFrame,'isdnPerPrevFsyncSeconds':isdnPerPrevFsyncSeconds,'isdnPerfPrevErrorSeconds':isdnPerfPrevErrorSeconds,'isdnPerfDataTotalTable':isdnPerfDataTotalTable,_K:isdnPerfDataTotalEntry,'isdnPerfTotalBadAmiViolation':isdnPerfTotalBadAmiViolation,'isdnPerfTotalUnbalancedFrame':isdnPerfTotalUnbalancedFrame,'isdnPerTotalFsyncSeconds':isdnPerTotalFsyncSeconds,'isdnPerfTotalErrorSeconds':isdnPerfTotalErrorSeconds,'isdnPerfTotalTimePeriodsElapsed':isdnPerfTotalTimePeriodsElapsed,'isdnAlarmProfileTable':isdnAlarmProfileTable,_L:isdnAlarmProfileEntry,'isdnThresholdAmiViolations':isdnThresholdAmiViolations,'isdnThresholdUnbalancedFrame':isdnThresholdUnbalancedFrame})