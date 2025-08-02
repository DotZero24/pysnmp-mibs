_J='slTestsTrapsLoopbackActive'
_I='slTestsIfLoopType'
_H='slmTrapLogId'
_G='SL-MAIN-MIB'
_F='read-write'
_E='slTestsIfLoopIfIndex'
_D='read-only'
_C='Integer32'
_B='SL-TESTS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
slMain,slmTrapLogId=mibBuilder.importSymbols(_G,'slMain',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
slTests=ModuleIdentity((1,3,6,1,4,1,4515,1,3,13))
_SlTestsIfLoop_ObjectIdentity=ObjectIdentity
slTestsIfLoop=_SlTestsIfLoop_ObjectIdentity((1,3,6,1,4,1,4515,1,3,13,1))
_SlTestsIfLoopTable_Object=MibTable
slTestsIfLoopTable=_SlTestsIfLoopTable_Object((1,3,6,1,4,1,4515,1,3,13,1,1))
if mibBuilder.loadTexts:slTestsIfLoopTable.setStatus(_A)
_SlTestsIfLoopEntry_Object=MibTableRow
slTestsIfLoopEntry=_SlTestsIfLoopEntry_Object((1,3,6,1,4,1,4515,1,3,13,1,1,1))
slTestsIfLoopEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:slTestsIfLoopEntry.setStatus(_A)
_SlTestsIfLoopIfIndex_Type=InterfaceIndex
_SlTestsIfLoopIfIndex_Object=MibTableColumn
slTestsIfLoopIfIndex=_SlTestsIfLoopIfIndex_Object((1,3,6,1,4,1,4515,1,3,13,1,1,1,1),_SlTestsIfLoopIfIndex_Type())
slTestsIfLoopIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:slTestsIfLoopIfIndex.setStatus(_A)
_SlTestsIfLoopDuration_Type=Integer32
_SlTestsIfLoopDuration_Object=MibTableColumn
slTestsIfLoopDuration=_SlTestsIfLoopDuration_Object((1,3,6,1,4,1,4515,1,3,13,1,1,1,2),_SlTestsIfLoopDuration_Type())
slTestsIfLoopDuration.setMaxAccess(_F)
if mibBuilder.loadTexts:slTestsIfLoopDuration.setStatus(_A)
class _SlTestsIfLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('start',1),('stop',2),('fail',3)))
_SlTestsIfLoopStatus_Type.__name__=_C
_SlTestsIfLoopStatus_Object=MibTableColumn
slTestsIfLoopStatus=_SlTestsIfLoopStatus_Object((1,3,6,1,4,1,4515,1,3,13,1,1,1,3),_SlTestsIfLoopStatus_Type())
slTestsIfLoopStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:slTestsIfLoopStatus.setStatus(_A)
class _SlTestsIfLoopType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('terminal',1),('facility',2),('prbs',3),('otnPrbs',4)))
_SlTestsIfLoopType_Type.__name__=_C
_SlTestsIfLoopType_Object=MibTableColumn
slTestsIfLoopType=_SlTestsIfLoopType_Object((1,3,6,1,4,1,4515,1,3,13,1,1,1,5),_SlTestsIfLoopType_Type())
slTestsIfLoopType.setMaxAccess(_F)
if mibBuilder.loadTexts:slTestsIfLoopType.setStatus(_A)
class _SlTestsIfLoopMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('timeout',1),('toggle',2)))
_SlTestsIfLoopMode_Type.__name__=_C
_SlTestsIfLoopMode_Object=MibTableColumn
slTestsIfLoopMode=_SlTestsIfLoopMode_Object((1,3,6,1,4,1,4515,1,3,13,1,1,1,6),_SlTestsIfLoopMode_Type())
slTestsIfLoopMode.setMaxAccess(_F)
if mibBuilder.loadTexts:slTestsIfLoopMode.setStatus(_A)
_SlTestsIfLoopErrors_Type=Counter32
_SlTestsIfLoopErrors_Object=MibTableColumn
slTestsIfLoopErrors=_SlTestsIfLoopErrors_Object((1,3,6,1,4,1,4515,1,3,13,1,1,1,7),_SlTestsIfLoopErrors_Type())
slTestsIfLoopErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:slTestsIfLoopErrors.setStatus(_A)
class _SlTestsIfLoopResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('fail',2)))
_SlTestsIfLoopResult_Type.__name__=_C
_SlTestsIfLoopResult_Object=MibTableColumn
slTestsIfLoopResult=_SlTestsIfLoopResult_Object((1,3,6,1,4,1,4515,1,3,13,1,1,1,8),_SlTestsIfLoopResult_Type())
slTestsIfLoopResult.setMaxAccess(_D)
if mibBuilder.loadTexts:slTestsIfLoopResult.setStatus(_A)
_SlTestsIfLoopPassedSeconds_Type=Integer32
_SlTestsIfLoopPassedSeconds_Object=MibTableColumn
slTestsIfLoopPassedSeconds=_SlTestsIfLoopPassedSeconds_Object((1,3,6,1,4,1,4515,1,3,13,1,1,1,9),_SlTestsIfLoopPassedSeconds_Type())
slTestsIfLoopPassedSeconds.setMaxAccess(_D)
if mibBuilder.loadTexts:slTestsIfLoopPassedSeconds.setStatus(_A)
_SlTestsTraps_ObjectIdentity=ObjectIdentity
slTestsTraps=_SlTestsTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,3,13,2))
_SlTestsTraps0_ObjectIdentity=ObjectIdentity
slTestsTraps0=_SlTestsTraps0_ObjectIdentity((1,3,6,1,4,1,4515,1,3,13,2,0))
_SlTestsTrapsLoopbackActive_Type=TruthValue
_SlTestsTrapsLoopbackActive_Object=MibScalar
slTestsTrapsLoopbackActive=_SlTestsTrapsLoopbackActive_Object((1,3,6,1,4,1,4515,1,3,13,2,1),_SlTestsTrapsLoopbackActive_Type())
slTestsTrapsLoopbackActive.setMaxAccess(_D)
if mibBuilder.loadTexts:slTestsTrapsLoopbackActive.setStatus(_A)
slTestsTrapsLoopbackTableChanged0=NotificationType((1,3,6,1,4,1,4515,1,3,13,2,0,2))
slTestsTrapsLoopbackTableChanged0.setObjects(*((_B,_E),(_B,_I),(_B,_J),(_G,_H)))
if mibBuilder.loadTexts:slTestsTrapsLoopbackTableChanged0.setStatus(_A)
slTestsTrapsLoopbackTableChanged=NotificationType((1,3,6,1,4,1,4515,1,3,13,2,2))
slTestsTrapsLoopbackTableChanged.setObjects(*((_B,_E),(_B,_I),(_B,_J),(_G,_H)))
if mibBuilder.loadTexts:slTestsTrapsLoopbackTableChanged.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'slTests':slTests,'slTestsIfLoop':slTestsIfLoop,'slTestsIfLoopTable':slTestsIfLoopTable,'slTestsIfLoopEntry':slTestsIfLoopEntry,_E:slTestsIfLoopIfIndex,'slTestsIfLoopDuration':slTestsIfLoopDuration,'slTestsIfLoopStatus':slTestsIfLoopStatus,_I:slTestsIfLoopType,'slTestsIfLoopMode':slTestsIfLoopMode,'slTestsIfLoopErrors':slTestsIfLoopErrors,'slTestsIfLoopResult':slTestsIfLoopResult,'slTestsIfLoopPassedSeconds':slTestsIfLoopPassedSeconds,'slTestsTraps':slTestsTraps,'slTestsTraps0':slTestsTraps0,'slTestsTrapsLoopbackTableChanged0':slTestsTrapsLoopbackTableChanged0,_J:slTestsTrapsLoopbackActive,'slTestsTrapsLoopbackTableChanged':slTestsTrapsLoopbackTableChanged})