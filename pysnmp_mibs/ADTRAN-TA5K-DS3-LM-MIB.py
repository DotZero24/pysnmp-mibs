_J='dsx3TotalIndex'
_I='dsx3IntervalNumber'
_H='dsx3IntervalIndex'
_G='dsx3CurrentIndex'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='DS3-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adTrapInformSeqNum,=mibBuilder.importSymbols('ADTRAN-GENTRAPINFORM-MIB','adTrapInformSeqNum')
adIdentity,adMgmt,adProducts=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity','adMgmt','adProducts')
dsx3CurrentIndex,dsx3IntervalIndex,dsx3IntervalNumber,dsx3TotalIndex=mibBuilder.importSymbols(_C,_G,_H,_I,_J)
ifIndex,=mibBuilder.importSymbols(_E,_F)
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adTa5kDs3ModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,979))
_AdTa5kDs3Traps_ObjectIdentity=ObjectIdentity
adTa5kDs3Traps=_AdTa5kDs3Traps_ObjectIdentity((1,3,6,1,4,1,664,1,979))
_AdTa5kDs3_ObjectIdentity=ObjectIdentity
adTa5kDs3=_AdTa5kDs3_ObjectIdentity((1,3,6,1,4,1,664,2,979))
_AdTa5kDS3Provisioning_ObjectIdentity=ObjectIdentity
adTa5kDS3Provisioning=_AdTa5kDS3Provisioning_ObjectIdentity((1,3,6,1,4,1,664,2,979,1))
_AdTa5kDS3Test_ObjectIdentity=ObjectIdentity
adTa5kDS3Test=_AdTa5kDS3Test_ObjectIdentity((1,3,6,1,4,1,664,2,979,2))
_AdTa5kDS3TestPattenTable_Object=MibTable
adTa5kDS3TestPattenTable=_AdTa5kDS3TestPattenTable_Object((1,3,6,1,4,1,664,2,979,2,1))
if mibBuilder.loadTexts:adTa5kDS3TestPattenTable.setStatus(_A)
_AdTa5kDS3TestPattenEntry_Object=MibTableRow
adTa5kDS3TestPattenEntry=_AdTa5kDS3TestPattenEntry_Object((1,3,6,1,4,1,664,2,979,2,1,1))
adTa5kDS3TestPattenEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTa5kDS3TestPattenEntry.setStatus(_A)
_AdTa5kDS3TxTestPattern_Type=Integer32
_AdTa5kDS3TxTestPattern_Object=MibTableColumn
adTa5kDS3TxTestPattern=_AdTa5kDS3TxTestPattern_Object((1,3,6,1,4,1,664,2,979,2,1,1,1),_AdTa5kDS3TxTestPattern_Type())
adTa5kDS3TxTestPattern.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kDS3TxTestPattern.setStatus(_A)
_AdTa5kDS3RxTestPattern_Type=Integer32
_AdTa5kDS3RxTestPattern_Object=MibTableColumn
adTa5kDS3RxTestPattern=_AdTa5kDS3RxTestPattern_Object((1,3,6,1,4,1,664,2,979,2,1,1,2),_AdTa5kDS3RxTestPattern_Type())
adTa5kDS3RxTestPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:adTa5kDS3RxTestPattern.setStatus(_A)
_AdTa5kDS3TestPatternErrors_Type=Integer32
_AdTa5kDS3TestPatternErrors_Object=MibTableColumn
adTa5kDS3TestPatternErrors=_AdTa5kDS3TestPatternErrors_Object((1,3,6,1,4,1,664,2,979,2,1,1,3),_AdTa5kDS3TestPatternErrors_Type())
adTa5kDS3TestPatternErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:adTa5kDS3TestPatternErrors.setStatus(_A)
_AdTa5kDS3TestPatternResetStatus_Type=Integer32
_AdTa5kDS3TestPatternResetStatus_Object=MibTableColumn
adTa5kDS3TestPatternResetStatus=_AdTa5kDS3TestPatternResetStatus_Object((1,3,6,1,4,1,664,2,979,2,1,1,4),_AdTa5kDS3TestPatternResetStatus_Type())
adTa5kDS3TestPatternResetStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kDS3TestPatternResetStatus.setStatus(_A)
_AdTa5kDS3LoopbackTable_Object=MibTable
adTa5kDS3LoopbackTable=_AdTa5kDS3LoopbackTable_Object((1,3,6,1,4,1,664,2,979,2,2))
if mibBuilder.loadTexts:adTa5kDS3LoopbackTable.setStatus(_A)
_AdTa5kDS3LoopbackEntry_Object=MibTableRow
adTa5kDS3LoopbackEntry=_AdTa5kDS3LoopbackEntry_Object((1,3,6,1,4,1,664,2,979,2,2,1))
adTa5kDS3LoopbackEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTa5kDS3LoopbackEntry.setStatus(_A)
_AdTa5kDS3LoopbackFarEnd_Type=Integer32
_AdTa5kDS3LoopbackFarEnd_Object=MibTableColumn
adTa5kDS3LoopbackFarEnd=_AdTa5kDS3LoopbackFarEnd_Object((1,3,6,1,4,1,664,2,979,2,2,1,1),_AdTa5kDS3LoopbackFarEnd_Type())
adTa5kDS3LoopbackFarEnd.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kDS3LoopbackFarEnd.setStatus(_A)
_AdTa5kDS3LoopbackCancelFarEnd_Type=Integer32
_AdTa5kDS3LoopbackCancelFarEnd_Object=MibTableColumn
adTa5kDS3LoopbackCancelFarEnd=_AdTa5kDS3LoopbackCancelFarEnd_Object((1,3,6,1,4,1,664,2,979,2,2,1,2),_AdTa5kDS3LoopbackCancelFarEnd_Type())
adTa5kDS3LoopbackCancelFarEnd.setMaxAccess(_D)
if mibBuilder.loadTexts:adTa5kDS3LoopbackCancelFarEnd.setStatus(_A)
_AdTa5kDS3Performance_ObjectIdentity=ObjectIdentity
adTa5kDS3Performance=_AdTa5kDS3Performance_ObjectIdentity((1,3,6,1,4,1,664,2,979,3))
_AdTa5kDS3CurrentTable_Object=MibTable
adTa5kDS3CurrentTable=_AdTa5kDS3CurrentTable_Object((1,3,6,1,4,1,664,2,979,3,1))
if mibBuilder.loadTexts:adTa5kDS3CurrentTable.setStatus(_A)
_AdTa5kDS3CurrentEntry_Object=MibTableRow
adTa5kDS3CurrentEntry=_AdTa5kDS3CurrentEntry_Object((1,3,6,1,4,1,664,2,979,3,1,1))
adTa5kDS3CurrentEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:adTa5kDS3CurrentEntry.setStatus(_A)
_AdTa5kDS3CurrentBIP8_Type=PerfCurrentCount
_AdTa5kDS3CurrentBIP8_Object=MibTableColumn
adTa5kDS3CurrentBIP8=_AdTa5kDS3CurrentBIP8_Object((1,3,6,1,4,1,664,2,979,3,1,1,1),_AdTa5kDS3CurrentBIP8_Type())
adTa5kDS3CurrentBIP8.setMaxAccess(_B)
if mibBuilder.loadTexts:adTa5kDS3CurrentBIP8.setStatus(_A)
_AdTa5kDS3CurrentPLCPES_Type=PerfCurrentCount
_AdTa5kDS3CurrentPLCPES_Object=MibTableColumn
adTa5kDS3CurrentPLCPES=_AdTa5kDS3CurrentPLCPES_Object((1,3,6,1,4,1,664,2,979,3,1,1,2),_AdTa5kDS3CurrentPLCPES_Type())
adTa5kDS3CurrentPLCPES.setMaxAccess(_B)
if mibBuilder.loadTexts:adTa5kDS3CurrentPLCPES.setStatus(_A)
_AdTa5kDS3IntervalTable_Object=MibTable
adTa5kDS3IntervalTable=_AdTa5kDS3IntervalTable_Object((1,3,6,1,4,1,664,2,979,3,2))
if mibBuilder.loadTexts:adTa5kDS3IntervalTable.setStatus(_A)
_AdTa5kDS3IntervalEntry_Object=MibTableRow
adTa5kDS3IntervalEntry=_AdTa5kDS3IntervalEntry_Object((1,3,6,1,4,1,664,2,979,3,2,1))
adTa5kDS3IntervalEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:adTa5kDS3IntervalEntry.setStatus(_A)
_AdTa5kDS3IntervalBIP8_Type=PerfIntervalCount
_AdTa5kDS3IntervalBIP8_Object=MibTableColumn
adTa5kDS3IntervalBIP8=_AdTa5kDS3IntervalBIP8_Object((1,3,6,1,4,1,664,2,979,3,2,1,1),_AdTa5kDS3IntervalBIP8_Type())
adTa5kDS3IntervalBIP8.setMaxAccess(_B)
if mibBuilder.loadTexts:adTa5kDS3IntervalBIP8.setStatus(_A)
_AdTa5kDS3IntervalPLCPES_Type=PerfIntervalCount
_AdTa5kDS3IntervalPLCPES_Object=MibTableColumn
adTa5kDS3IntervalPLCPES=_AdTa5kDS3IntervalPLCPES_Object((1,3,6,1,4,1,664,2,979,3,2,1,2),_AdTa5kDS3IntervalPLCPES_Type())
adTa5kDS3IntervalPLCPES.setMaxAccess(_B)
if mibBuilder.loadTexts:adTa5kDS3IntervalPLCPES.setStatus(_A)
_AdTa5kDS3TotalTable_Object=MibTable
adTa5kDS3TotalTable=_AdTa5kDS3TotalTable_Object((1,3,6,1,4,1,664,2,979,3,3))
if mibBuilder.loadTexts:adTa5kDS3TotalTable.setStatus(_A)
_AdTa5kDS3TotalEntry_Object=MibTableRow
adTa5kDS3TotalEntry=_AdTa5kDS3TotalEntry_Object((1,3,6,1,4,1,664,2,979,3,3,1))
adTa5kDS3TotalEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:adTa5kDS3TotalEntry.setStatus(_A)
_AdTa5kDS3TotalBIP8_Type=PerfTotalCount
_AdTa5kDS3TotalBIP8_Object=MibTableColumn
adTa5kDS3TotalBIP8=_AdTa5kDS3TotalBIP8_Object((1,3,6,1,4,1,664,2,979,3,3,1,1),_AdTa5kDS3TotalBIP8_Type())
adTa5kDS3TotalBIP8.setMaxAccess(_B)
if mibBuilder.loadTexts:adTa5kDS3TotalBIP8.setStatus(_A)
_AdTa5kDS3TotalPLCPES_Type=PerfTotalCount
_AdTa5kDS3TotalPLCPES_Object=MibTableColumn
adTa5kDS3TotalPLCPES=_AdTa5kDS3TotalPLCPES_Object((1,3,6,1,4,1,664,2,979,3,3,1,2),_AdTa5kDS3TotalPLCPES_Type())
adTa5kDS3TotalPLCPES.setMaxAccess(_B)
if mibBuilder.loadTexts:adTa5kDS3TotalPLCPES.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-TA5K-DS3-LM-MIB',**{'adTa5kDs3Traps':adTa5kDs3Traps,'adTa5kDs3':adTa5kDs3,'adTa5kDS3Provisioning':adTa5kDS3Provisioning,'adTa5kDS3Test':adTa5kDS3Test,'adTa5kDS3TestPattenTable':adTa5kDS3TestPattenTable,'adTa5kDS3TestPattenEntry':adTa5kDS3TestPattenEntry,'adTa5kDS3TxTestPattern':adTa5kDS3TxTestPattern,'adTa5kDS3RxTestPattern':adTa5kDS3RxTestPattern,'adTa5kDS3TestPatternErrors':adTa5kDS3TestPatternErrors,'adTa5kDS3TestPatternResetStatus':adTa5kDS3TestPatternResetStatus,'adTa5kDS3LoopbackTable':adTa5kDS3LoopbackTable,'adTa5kDS3LoopbackEntry':adTa5kDS3LoopbackEntry,'adTa5kDS3LoopbackFarEnd':adTa5kDS3LoopbackFarEnd,'adTa5kDS3LoopbackCancelFarEnd':adTa5kDS3LoopbackCancelFarEnd,'adTa5kDS3Performance':adTa5kDS3Performance,'adTa5kDS3CurrentTable':adTa5kDS3CurrentTable,'adTa5kDS3CurrentEntry':adTa5kDS3CurrentEntry,'adTa5kDS3CurrentBIP8':adTa5kDS3CurrentBIP8,'adTa5kDS3CurrentPLCPES':adTa5kDS3CurrentPLCPES,'adTa5kDS3IntervalTable':adTa5kDS3IntervalTable,'adTa5kDS3IntervalEntry':adTa5kDS3IntervalEntry,'adTa5kDS3IntervalBIP8':adTa5kDS3IntervalBIP8,'adTa5kDS3IntervalPLCPES':adTa5kDS3IntervalPLCPES,'adTa5kDS3TotalTable':adTa5kDS3TotalTable,'adTa5kDS3TotalEntry':adTa5kDS3TotalEntry,'adTa5kDS3TotalBIP8':adTa5kDS3TotalBIP8,'adTa5kDS3TotalPLCPES':adTa5kDS3TotalPLCPES,'adTa5kDs3ModuleIdentity':adTa5kDs3ModuleIdentity})