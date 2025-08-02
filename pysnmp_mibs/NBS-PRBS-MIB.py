_R='nbsPrbsCheckProgress'
_Q='nbsPrbsCheckErrors'
_P='nbsPrbsCheckIfIndex'
_O='nbsPrbsGenIfIndex'
_N='nbsPrbsPatternIndex'
_M='not-accessible'
_L='notSupported'
_K='nbsPrbsCheckStatus'
_J='read-write'
_I='Integer32'
_H='nbsCmmcSlotIndex'
_G='nbsCmmcPortName'
_F='nbsCmmcPortIndex'
_E='nbsCmmcChassisIndex'
_D='NBS-PRBS-MIB'
_C='read-only'
_B='NBS-CMMC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nbsCmmcChassisIndex,nbsCmmcPortIndex,nbsCmmcPortName,nbsCmmcSlotIndex=mibBuilder.importSymbols(_B,_E,_F,_G,_H)
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsPrbsMib=ModuleIdentity((1,3,6,1,4,1,629,212))
_NbsPrbsPatternGrp_ObjectIdentity=ObjectIdentity
nbsPrbsPatternGrp=_NbsPrbsPatternGrp_ObjectIdentity((1,3,6,1,4,1,629,212,1))
if mibBuilder.loadTexts:nbsPrbsPatternGrp.setStatus(_A)
_NbsPrbsPatternTableSize_Type=Unsigned32
_NbsPrbsPatternTableSize_Object=MibScalar
nbsPrbsPatternTableSize=_NbsPrbsPatternTableSize_Object((1,3,6,1,4,1,629,212,1,1),_NbsPrbsPatternTableSize_Type())
nbsPrbsPatternTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsPatternTableSize.setStatus(_A)
_NbsPrbsPatternTable_Object=MibTable
nbsPrbsPatternTable=_NbsPrbsPatternTable_Object((1,3,6,1,4,1,629,212,1,2))
if mibBuilder.loadTexts:nbsPrbsPatternTable.setStatus(_A)
_NbsPrbsPatternEntry_Object=MibTableRow
nbsPrbsPatternEntry=_NbsPrbsPatternEntry_Object((1,3,6,1,4,1,629,212,1,2,1))
nbsPrbsPatternEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:nbsPrbsPatternEntry.setStatus(_A)
_NbsPrbsPatternIndex_Type=Integer32
_NbsPrbsPatternIndex_Object=MibTableColumn
nbsPrbsPatternIndex=_NbsPrbsPatternIndex_Object((1,3,6,1,4,1,629,212,1,2,1,1),_NbsPrbsPatternIndex_Type())
nbsPrbsPatternIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:nbsPrbsPatternIndex.setStatus(_A)
_NbsPrbsPatternName_Type=DisplayString
_NbsPrbsPatternName_Object=MibTableColumn
nbsPrbsPatternName=_NbsPrbsPatternName_Object((1,3,6,1,4,1,629,212,1,2,1,2),_NbsPrbsPatternName_Type())
nbsPrbsPatternName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsPatternName.setStatus(_A)
_NbsPrbsPatternDesc_Type=DisplayString
_NbsPrbsPatternDesc_Object=MibTableColumn
nbsPrbsPatternDesc=_NbsPrbsPatternDesc_Object((1,3,6,1,4,1,629,212,1,2,1,3),_NbsPrbsPatternDesc_Type())
nbsPrbsPatternDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsPatternDesc.setStatus(_A)
_NbsPrbsGenGrp_ObjectIdentity=ObjectIdentity
nbsPrbsGenGrp=_NbsPrbsGenGrp_ObjectIdentity((1,3,6,1,4,1,629,212,2))
if mibBuilder.loadTexts:nbsPrbsGenGrp.setStatus(_A)
_NbsPrbsGenTableSize_Type=Unsigned32
_NbsPrbsGenTableSize_Object=MibScalar
nbsPrbsGenTableSize=_NbsPrbsGenTableSize_Object((1,3,6,1,4,1,629,212,2,1),_NbsPrbsGenTableSize_Type())
nbsPrbsGenTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsGenTableSize.setStatus(_A)
_NbsPrbsGenTable_Object=MibTable
nbsPrbsGenTable=_NbsPrbsGenTable_Object((1,3,6,1,4,1,629,212,2,2))
if mibBuilder.loadTexts:nbsPrbsGenTable.setStatus(_A)
_NbsPrbsGenEntry_Object=MibTableRow
nbsPrbsGenEntry=_NbsPrbsGenEntry_Object((1,3,6,1,4,1,629,212,2,2,1))
nbsPrbsGenEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:nbsPrbsGenEntry.setStatus(_A)
_NbsPrbsGenIfIndex_Type=InterfaceIndex
_NbsPrbsGenIfIndex_Object=MibTableColumn
nbsPrbsGenIfIndex=_NbsPrbsGenIfIndex_Object((1,3,6,1,4,1,629,212,2,2,1,1),_NbsPrbsGenIfIndex_Type())
nbsPrbsGenIfIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:nbsPrbsGenIfIndex.setStatus(_A)
_NbsPrbsGenPatternCaps_Type=OctetString
_NbsPrbsGenPatternCaps_Object=MibTableColumn
nbsPrbsGenPatternCaps=_NbsPrbsGenPatternCaps_Object((1,3,6,1,4,1,629,212,2,2,1,2),_NbsPrbsGenPatternCaps_Type())
nbsPrbsGenPatternCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsGenPatternCaps.setStatus(_A)
_NbsPrbsGenPatternIndex_Type=Integer32
_NbsPrbsGenPatternIndex_Object=MibTableColumn
nbsPrbsGenPatternIndex=_NbsPrbsGenPatternIndex_Object((1,3,6,1,4,1,629,212,2,2,1,3),_NbsPrbsGenPatternIndex_Type())
nbsPrbsGenPatternIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsPrbsGenPatternIndex.setStatus(_A)
class _NbsPrbsGenDurationMax_Type(Integer32):defaultValue=0
_NbsPrbsGenDurationMax_Type.__name__=_I
_NbsPrbsGenDurationMax_Object=MibTableColumn
nbsPrbsGenDurationMax=_NbsPrbsGenDurationMax_Object((1,3,6,1,4,1,629,212,2,2,1,4),_NbsPrbsGenDurationMax_Type())
nbsPrbsGenDurationMax.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsGenDurationMax.setStatus(_A)
class _NbsPrbsGenDuration_Type(Integer32):defaultValue=60
_NbsPrbsGenDuration_Type.__name__=_I
_NbsPrbsGenDuration_Object=MibTableColumn
nbsPrbsGenDuration=_NbsPrbsGenDuration_Object((1,3,6,1,4,1,629,212,2,2,1,5),_NbsPrbsGenDuration_Type())
nbsPrbsGenDuration.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsPrbsGenDuration.setStatus(_A)
class _NbsPrbsGenAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('stop',2),('start',3)))
_NbsPrbsGenAction_Type.__name__=_I
_NbsPrbsGenAction_Object=MibTableColumn
nbsPrbsGenAction=_NbsPrbsGenAction_Object((1,3,6,1,4,1,629,212,2,2,1,6),_NbsPrbsGenAction_Type())
nbsPrbsGenAction.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsPrbsGenAction.setStatus(_A)
class _NbsPrbsGenStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('unknown',2),('idle',3),('generating',4)))
_NbsPrbsGenStatus_Type.__name__=_I
_NbsPrbsGenStatus_Object=MibTableColumn
nbsPrbsGenStatus=_NbsPrbsGenStatus_Object((1,3,6,1,4,1,629,212,2,2,1,7),_NbsPrbsGenStatus_Type())
nbsPrbsGenStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsGenStatus.setStatus(_A)
_NbsPrbsGenProgress_Type=Counter32
_NbsPrbsGenProgress_Object=MibTableColumn
nbsPrbsGenProgress=_NbsPrbsGenProgress_Object((1,3,6,1,4,1,629,212,2,2,1,8),_NbsPrbsGenProgress_Type())
nbsPrbsGenProgress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsGenProgress.setStatus(_A)
_NbsPrbsCheckGrp_ObjectIdentity=ObjectIdentity
nbsPrbsCheckGrp=_NbsPrbsCheckGrp_ObjectIdentity((1,3,6,1,4,1,629,212,3))
if mibBuilder.loadTexts:nbsPrbsCheckGrp.setStatus(_A)
_NbsPrbsCheckTableSize_Type=Unsigned32
_NbsPrbsCheckTableSize_Object=MibScalar
nbsPrbsCheckTableSize=_NbsPrbsCheckTableSize_Object((1,3,6,1,4,1,629,212,3,1),_NbsPrbsCheckTableSize_Type())
nbsPrbsCheckTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsCheckTableSize.setStatus(_A)
_NbsPrbsCheckTable_Object=MibTable
nbsPrbsCheckTable=_NbsPrbsCheckTable_Object((1,3,6,1,4,1,629,212,3,2))
if mibBuilder.loadTexts:nbsPrbsCheckTable.setStatus(_A)
_NbsPrbsCheckEntry_Object=MibTableRow
nbsPrbsCheckEntry=_NbsPrbsCheckEntry_Object((1,3,6,1,4,1,629,212,3,2,1))
nbsPrbsCheckEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:nbsPrbsCheckEntry.setStatus(_A)
_NbsPrbsCheckIfIndex_Type=InterfaceIndex
_NbsPrbsCheckIfIndex_Object=MibTableColumn
nbsPrbsCheckIfIndex=_NbsPrbsCheckIfIndex_Object((1,3,6,1,4,1,629,212,3,2,1,1),_NbsPrbsCheckIfIndex_Type())
nbsPrbsCheckIfIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:nbsPrbsCheckIfIndex.setStatus(_A)
_NbsPrbsCheckPatternCaps_Type=OctetString
_NbsPrbsCheckPatternCaps_Object=MibTableColumn
nbsPrbsCheckPatternCaps=_NbsPrbsCheckPatternCaps_Object((1,3,6,1,4,1,629,212,3,2,1,2),_NbsPrbsCheckPatternCaps_Type())
nbsPrbsCheckPatternCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsCheckPatternCaps.setStatus(_A)
_NbsPrbsCheckPatternIndex_Type=Integer32
_NbsPrbsCheckPatternIndex_Object=MibTableColumn
nbsPrbsCheckPatternIndex=_NbsPrbsCheckPatternIndex_Object((1,3,6,1,4,1,629,212,3,2,1,3),_NbsPrbsCheckPatternIndex_Type())
nbsPrbsCheckPatternIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsPrbsCheckPatternIndex.setStatus(_A)
class _NbsPrbsCheckDurationMax_Type(Integer32):defaultValue=0
_NbsPrbsCheckDurationMax_Type.__name__=_I
_NbsPrbsCheckDurationMax_Object=MibTableColumn
nbsPrbsCheckDurationMax=_NbsPrbsCheckDurationMax_Object((1,3,6,1,4,1,629,212,3,2,1,4),_NbsPrbsCheckDurationMax_Type())
nbsPrbsCheckDurationMax.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsCheckDurationMax.setStatus(_A)
class _NbsPrbsCheckDuration_Type(Integer32):defaultValue=60
_NbsPrbsCheckDuration_Type.__name__=_I
_NbsPrbsCheckDuration_Object=MibTableColumn
nbsPrbsCheckDuration=_NbsPrbsCheckDuration_Object((1,3,6,1,4,1,629,212,3,2,1,5),_NbsPrbsCheckDuration_Type())
nbsPrbsCheckDuration.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsPrbsCheckDuration.setStatus(_A)
class _NbsPrbsCheckAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('stop',2),('start',3)))
_NbsPrbsCheckAction_Type.__name__=_I
_NbsPrbsCheckAction_Object=MibTableColumn
nbsPrbsCheckAction=_NbsPrbsCheckAction_Object((1,3,6,1,4,1,629,212,3,2,1,6),_NbsPrbsCheckAction_Type())
nbsPrbsCheckAction.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsPrbsCheckAction.setStatus(_A)
class _NbsPrbsCheckStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_L,1),('idle',2),('syncIn',3),('syncOut',4),('error',5),('errOverflow',6),('gaveUp',7)))
_NbsPrbsCheckStatus_Type.__name__=_I
_NbsPrbsCheckStatus_Object=MibTableColumn
nbsPrbsCheckStatus=_NbsPrbsCheckStatus_Object((1,3,6,1,4,1,629,212,3,2,1,7),_NbsPrbsCheckStatus_Type())
nbsPrbsCheckStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsCheckStatus.setStatus(_A)
_NbsPrbsCheckProgress_Type=Counter32
_NbsPrbsCheckProgress_Object=MibTableColumn
nbsPrbsCheckProgress=_NbsPrbsCheckProgress_Object((1,3,6,1,4,1,629,212,3,2,1,8),_NbsPrbsCheckProgress_Type())
nbsPrbsCheckProgress.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsCheckProgress.setStatus(_A)
_NbsPrbsCheckErrors_Type=Counter32
_NbsPrbsCheckErrors_Object=MibTableColumn
nbsPrbsCheckErrors=_NbsPrbsCheckErrors_Object((1,3,6,1,4,1,629,212,3,2,1,9),_NbsPrbsCheckErrors_Type())
nbsPrbsCheckErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsPrbsCheckErrors.setStatus(_A)
class _NbsPrbsCheckUpdateFreq_Type(Integer32):defaultValue=0
_NbsPrbsCheckUpdateFreq_Type.__name__=_I
_NbsPrbsCheckUpdateFreq_Object=MibTableColumn
nbsPrbsCheckUpdateFreq=_NbsPrbsCheckUpdateFreq_Object((1,3,6,1,4,1,629,212,3,2,1,10),_NbsPrbsCheckUpdateFreq_Type())
nbsPrbsCheckUpdateFreq.setMaxAccess(_J)
if mibBuilder.loadTexts:nbsPrbsCheckUpdateFreq.setStatus(_A)
_NbsPrbsTrapGrp_ObjectIdentity=ObjectIdentity
nbsPrbsTrapGrp=_NbsPrbsTrapGrp_ObjectIdentity((1,3,6,1,4,1,629,212,200))
if mibBuilder.loadTexts:nbsPrbsTrapGrp.setStatus(_A)
_NbsPrbsTraps0_ObjectIdentity=ObjectIdentity
nbsPrbsTraps0=_NbsPrbsTraps0_ObjectIdentity((1,3,6,1,4,1,629,212,200,0))
if mibBuilder.loadTexts:nbsPrbsTraps0.setStatus(_A)
nbsPrbsTrapGeneratorStarted=NotificationType((1,3,6,1,4,1,629,212,200,0,10))
nbsPrbsTrapGeneratorStarted.setObjects(*((_B,_E),(_B,_H),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:nbsPrbsTrapGeneratorStarted.setStatus(_A)
nbsPrbsTrapGeneratorStopped=NotificationType((1,3,6,1,4,1,629,212,200,0,11))
nbsPrbsTrapGeneratorStopped.setObjects(*((_B,_E),(_B,_H),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:nbsPrbsTrapGeneratorStopped.setStatus(_A)
nbsPrbsTrapCheckerStarted=NotificationType((1,3,6,1,4,1,629,212,200,0,20))
nbsPrbsTrapCheckerStarted.setObjects(*((_B,_E),(_B,_H),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:nbsPrbsTrapCheckerStarted.setStatus(_A)
nbsPrbsTrapCheckerStopped=NotificationType((1,3,6,1,4,1,629,212,200,0,21))
nbsPrbsTrapCheckerStopped.setObjects(*((_B,_E),(_B,_H),(_B,_F),(_B,_G),(_D,_K)))
if mibBuilder.loadTexts:nbsPrbsTrapCheckerStopped.setStatus(_A)
nbsPrbsTrapCheckerOverflowed=NotificationType((1,3,6,1,4,1,629,212,200,0,22))
nbsPrbsTrapCheckerOverflowed.setObjects(*((_B,_E),(_B,_H),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:nbsPrbsTrapCheckerOverflowed.setStatus(_A)
nbsPrbsTrapCheckerErrorDetected=NotificationType((1,3,6,1,4,1,629,212,200,0,23))
nbsPrbsTrapCheckerErrorDetected.setObjects(*((_B,_E),(_B,_H),(_B,_F),(_B,_G),(_D,_K)))
if mibBuilder.loadTexts:nbsPrbsTrapCheckerErrorDetected.setStatus(_A)
nbsPrbsTrapCheckerStatusUpdate=NotificationType((1,3,6,1,4,1,629,212,200,0,24))
nbsPrbsTrapCheckerStatusUpdate.setObjects(*((_B,_E),(_B,_H),(_B,_F),(_B,_G),(_D,_K),(_D,_Q),(_D,_R)))
if mibBuilder.loadTexts:nbsPrbsTrapCheckerStatusUpdate.setStatus(_A)
nbsPrbsTrapCheckerSyncIn=NotificationType((1,3,6,1,4,1,629,212,200,0,25))
nbsPrbsTrapCheckerSyncIn.setObjects(*((_B,_E),(_B,_H),(_B,_F),(_B,_G),(_D,_K)))
if mibBuilder.loadTexts:nbsPrbsTrapCheckerSyncIn.setStatus(_A)
nbsPrbsTrapCheckerSyncOut=NotificationType((1,3,6,1,4,1,629,212,200,0,26))
nbsPrbsTrapCheckerSyncOut.setObjects(*((_B,_E),(_B,_H),(_B,_F),(_B,_G),(_D,_K)))
if mibBuilder.loadTexts:nbsPrbsTrapCheckerSyncOut.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nbsPrbsMib':nbsPrbsMib,'nbsPrbsPatternGrp':nbsPrbsPatternGrp,'nbsPrbsPatternTableSize':nbsPrbsPatternTableSize,'nbsPrbsPatternTable':nbsPrbsPatternTable,'nbsPrbsPatternEntry':nbsPrbsPatternEntry,_N:nbsPrbsPatternIndex,'nbsPrbsPatternName':nbsPrbsPatternName,'nbsPrbsPatternDesc':nbsPrbsPatternDesc,'nbsPrbsGenGrp':nbsPrbsGenGrp,'nbsPrbsGenTableSize':nbsPrbsGenTableSize,'nbsPrbsGenTable':nbsPrbsGenTable,'nbsPrbsGenEntry':nbsPrbsGenEntry,_O:nbsPrbsGenIfIndex,'nbsPrbsGenPatternCaps':nbsPrbsGenPatternCaps,'nbsPrbsGenPatternIndex':nbsPrbsGenPatternIndex,'nbsPrbsGenDurationMax':nbsPrbsGenDurationMax,'nbsPrbsGenDuration':nbsPrbsGenDuration,'nbsPrbsGenAction':nbsPrbsGenAction,'nbsPrbsGenStatus':nbsPrbsGenStatus,'nbsPrbsGenProgress':nbsPrbsGenProgress,'nbsPrbsCheckGrp':nbsPrbsCheckGrp,'nbsPrbsCheckTableSize':nbsPrbsCheckTableSize,'nbsPrbsCheckTable':nbsPrbsCheckTable,'nbsPrbsCheckEntry':nbsPrbsCheckEntry,_P:nbsPrbsCheckIfIndex,'nbsPrbsCheckPatternCaps':nbsPrbsCheckPatternCaps,'nbsPrbsCheckPatternIndex':nbsPrbsCheckPatternIndex,'nbsPrbsCheckDurationMax':nbsPrbsCheckDurationMax,'nbsPrbsCheckDuration':nbsPrbsCheckDuration,'nbsPrbsCheckAction':nbsPrbsCheckAction,_K:nbsPrbsCheckStatus,_R:nbsPrbsCheckProgress,_Q:nbsPrbsCheckErrors,'nbsPrbsCheckUpdateFreq':nbsPrbsCheckUpdateFreq,'nbsPrbsTrapGrp':nbsPrbsTrapGrp,'nbsPrbsTraps0':nbsPrbsTraps0,'nbsPrbsTrapGeneratorStarted':nbsPrbsTrapGeneratorStarted,'nbsPrbsTrapGeneratorStopped':nbsPrbsTrapGeneratorStopped,'nbsPrbsTrapCheckerStarted':nbsPrbsTrapCheckerStarted,'nbsPrbsTrapCheckerStopped':nbsPrbsTrapCheckerStopped,'nbsPrbsTrapCheckerOverflowed':nbsPrbsTrapCheckerOverflowed,'nbsPrbsTrapCheckerErrorDetected':nbsPrbsTrapCheckerErrorDetected,'nbsPrbsTrapCheckerStatusUpdate':nbsPrbsTrapCheckerStatusUpdate,'nbsPrbsTrapCheckerSyncIn':nbsPrbsTrapCheckerSyncIn,'nbsPrbsTrapCheckerSyncOut':nbsPrbsTrapCheckerSyncOut})