_L='read-write'
_K='adGenPolicerPM24HrIntervalNumber'
_J='adGenPolicerPM15MinIntervalNumber'
_I='ADTRAN-GENPOLICERPM-MIB'
_H='adGenPolicerFixedLengthName'
_G='adGenPolicerName'
_F='Integer32'
_E='ADTRAN-GENPOLICER-MIB'
_D='adGenSlotInfoIndex'
_C='ADTRAN-GENSLOT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPolicerFixedLengthName,adGenPolicerName=mibBuilder.importSymbols(_E,_H,_G)
adGenSlotInfoIndex,=mibBuilder.importSymbols(_C,_D)
adGenPolicer,adGenPolicerID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenPolicer','adGenPolicerID')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
adGenPolicerPMMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,35,2))
if mibBuilder.loadTexts:adGenPolicerPMMIB.setRevisions(('2010-11-03 00:00',))
_AdGenPolicerPerformance_ObjectIdentity=ObjectIdentity
adGenPolicerPerformance=_AdGenPolicerPerformance_ObjectIdentity((1,3,6,1,4,1,664,5,70,35,2))
_AdGenPolicerPM15MinCurrentTable_Object=MibTable
adGenPolicerPM15MinCurrentTable=_AdGenPolicerPM15MinCurrentTable_Object((1,3,6,1,4,1,664,5,70,35,2,1))
if mibBuilder.loadTexts:adGenPolicerPM15MinCurrentTable.setStatus(_A)
_AdGenPolicerPM15MinCurrentEntry_Object=MibTableRow
adGenPolicerPM15MinCurrentEntry=_AdGenPolicerPM15MinCurrentEntry_Object((1,3,6,1,4,1,664,5,70,35,2,1,1))
adGenPolicerPM15MinCurrentEntry.setIndexNames((0,_C,_D),(0,_E,_G))
if mibBuilder.loadTexts:adGenPolicerPM15MinCurrentEntry.setStatus(_A)
_AdGenPolicerPM15MinCurrentIngressGreenFrames_Type=Counter64
_AdGenPolicerPM15MinCurrentIngressGreenFrames_Object=MibTableColumn
adGenPolicerPM15MinCurrentIngressGreenFrames=_AdGenPolicerPM15MinCurrentIngressGreenFrames_Object((1,3,6,1,4,1,664,5,70,35,2,1,1,1),_AdGenPolicerPM15MinCurrentIngressGreenFrames_Type())
adGenPolicerPM15MinCurrentIngressGreenFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM15MinCurrentIngressGreenFrames.setStatus(_A)
_AdGenPolicerPM15MinCurrentIngressYellowFrames_Type=Counter64
_AdGenPolicerPM15MinCurrentIngressYellowFrames_Object=MibTableColumn
adGenPolicerPM15MinCurrentIngressYellowFrames=_AdGenPolicerPM15MinCurrentIngressYellowFrames_Object((1,3,6,1,4,1,664,5,70,35,2,1,1,2),_AdGenPolicerPM15MinCurrentIngressYellowFrames_Type())
adGenPolicerPM15MinCurrentIngressYellowFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM15MinCurrentIngressYellowFrames.setStatus(_A)
_AdGenPolicerPM15MinCurrentIngressRedFrames_Type=Counter64
_AdGenPolicerPM15MinCurrentIngressRedFrames_Object=MibTableColumn
adGenPolicerPM15MinCurrentIngressRedFrames=_AdGenPolicerPM15MinCurrentIngressRedFrames_Object((1,3,6,1,4,1,664,5,70,35,2,1,1,3),_AdGenPolicerPM15MinCurrentIngressRedFrames_Type())
adGenPolicerPM15MinCurrentIngressRedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM15MinCurrentIngressRedFrames.setStatus(_A)
_AdGenPolicerPM15MinIntervalTable_Object=MibTable
adGenPolicerPM15MinIntervalTable=_AdGenPolicerPM15MinIntervalTable_Object((1,3,6,1,4,1,664,5,70,35,2,2))
if mibBuilder.loadTexts:adGenPolicerPM15MinIntervalTable.setStatus(_A)
_AdGenPolicerPM15MinIntervalEntry_Object=MibTableRow
adGenPolicerPM15MinIntervalEntry=_AdGenPolicerPM15MinIntervalEntry_Object((1,3,6,1,4,1,664,5,70,35,2,2,1))
adGenPolicerPM15MinIntervalEntry.setIndexNames((0,_C,_D),(0,_E,_H),(0,_I,_J))
if mibBuilder.loadTexts:adGenPolicerPM15MinIntervalEntry.setStatus(_A)
_AdGenPolicerPM15MinIntervalNumber_Type=Integer32
_AdGenPolicerPM15MinIntervalNumber_Object=MibTableColumn
adGenPolicerPM15MinIntervalNumber=_AdGenPolicerPM15MinIntervalNumber_Object((1,3,6,1,4,1,664,5,70,35,2,2,1,1),_AdGenPolicerPM15MinIntervalNumber_Type())
adGenPolicerPM15MinIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM15MinIntervalNumber.setStatus(_A)
_AdGenPolicerPM15MinIntervalIngressGreenFrames_Type=Counter64
_AdGenPolicerPM15MinIntervalIngressGreenFrames_Object=MibTableColumn
adGenPolicerPM15MinIntervalIngressGreenFrames=_AdGenPolicerPM15MinIntervalIngressGreenFrames_Object((1,3,6,1,4,1,664,5,70,35,2,2,1,2),_AdGenPolicerPM15MinIntervalIngressGreenFrames_Type())
adGenPolicerPM15MinIntervalIngressGreenFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM15MinIntervalIngressGreenFrames.setStatus(_A)
_AdGenPolicerPM15MinIntervalIngressYellowFrames_Type=Counter64
_AdGenPolicerPM15MinIntervalIngressYellowFrames_Object=MibTableColumn
adGenPolicerPM15MinIntervalIngressYellowFrames=_AdGenPolicerPM15MinIntervalIngressYellowFrames_Object((1,3,6,1,4,1,664,5,70,35,2,2,1,3),_AdGenPolicerPM15MinIntervalIngressYellowFrames_Type())
adGenPolicerPM15MinIntervalIngressYellowFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM15MinIntervalIngressYellowFrames.setStatus(_A)
_AdGenPolicerPM15MinIntervalIngressRedFrames_Type=Counter64
_AdGenPolicerPM15MinIntervalIngressRedFrames_Object=MibTableColumn
adGenPolicerPM15MinIntervalIngressRedFrames=_AdGenPolicerPM15MinIntervalIngressRedFrames_Object((1,3,6,1,4,1,664,5,70,35,2,2,1,4),_AdGenPolicerPM15MinIntervalIngressRedFrames_Type())
adGenPolicerPM15MinIntervalIngressRedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM15MinIntervalIngressRedFrames.setStatus(_A)
_AdGenPolicerPM15MinIntervalValidData_Type=TruthValue
_AdGenPolicerPM15MinIntervalValidData_Object=MibTableColumn
adGenPolicerPM15MinIntervalValidData=_AdGenPolicerPM15MinIntervalValidData_Object((1,3,6,1,4,1,664,5,70,35,2,2,1,5),_AdGenPolicerPM15MinIntervalValidData_Type())
adGenPolicerPM15MinIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM15MinIntervalValidData.setStatus(_A)
_AdGenPolicerPM24HrCurrentTable_Object=MibTable
adGenPolicerPM24HrCurrentTable=_AdGenPolicerPM24HrCurrentTable_Object((1,3,6,1,4,1,664,5,70,35,2,3))
if mibBuilder.loadTexts:adGenPolicerPM24HrCurrentTable.setStatus(_A)
_AdGenPolicerPM24HrCurrentEntry_Object=MibTableRow
adGenPolicerPM24HrCurrentEntry=_AdGenPolicerPM24HrCurrentEntry_Object((1,3,6,1,4,1,664,5,70,35,2,3,1))
adGenPolicerPM24HrCurrentEntry.setIndexNames((0,_C,_D),(0,_E,_G))
if mibBuilder.loadTexts:adGenPolicerPM24HrCurrentEntry.setStatus(_A)
_AdGenPolicerPM24HrCurrentIngressGreenFrames_Type=Counter64
_AdGenPolicerPM24HrCurrentIngressGreenFrames_Object=MibTableColumn
adGenPolicerPM24HrCurrentIngressGreenFrames=_AdGenPolicerPM24HrCurrentIngressGreenFrames_Object((1,3,6,1,4,1,664,5,70,35,2,3,1,1),_AdGenPolicerPM24HrCurrentIngressGreenFrames_Type())
adGenPolicerPM24HrCurrentIngressGreenFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM24HrCurrentIngressGreenFrames.setStatus(_A)
_AdGenPolicerPM24hrCurrentIngressYellowFrames_Type=Counter64
_AdGenPolicerPM24hrCurrentIngressYellowFrames_Object=MibTableColumn
adGenPolicerPM24hrCurrentIngressYellowFrames=_AdGenPolicerPM24hrCurrentIngressYellowFrames_Object((1,3,6,1,4,1,664,5,70,35,2,3,1,2),_AdGenPolicerPM24hrCurrentIngressYellowFrames_Type())
adGenPolicerPM24hrCurrentIngressYellowFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM24hrCurrentIngressYellowFrames.setStatus(_A)
_AdGenPolicerPM24HrCurrentIngressRedFrames_Type=Counter64
_AdGenPolicerPM24HrCurrentIngressRedFrames_Object=MibTableColumn
adGenPolicerPM24HrCurrentIngressRedFrames=_AdGenPolicerPM24HrCurrentIngressRedFrames_Object((1,3,6,1,4,1,664,5,70,35,2,3,1,3),_AdGenPolicerPM24HrCurrentIngressRedFrames_Type())
adGenPolicerPM24HrCurrentIngressRedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM24HrCurrentIngressRedFrames.setStatus(_A)
_AdGenPolicerPM24HrIntervalTable_Object=MibTable
adGenPolicerPM24HrIntervalTable=_AdGenPolicerPM24HrIntervalTable_Object((1,3,6,1,4,1,664,5,70,35,2,4))
if mibBuilder.loadTexts:adGenPolicerPM24HrIntervalTable.setStatus(_A)
_AdGenPolicerPM24HrIntervalEntry_Object=MibTableRow
adGenPolicerPM24HrIntervalEntry=_AdGenPolicerPM24HrIntervalEntry_Object((1,3,6,1,4,1,664,5,70,35,2,4,1))
adGenPolicerPM24HrIntervalEntry.setIndexNames((0,_C,_D),(0,_E,_H),(0,_I,_K))
if mibBuilder.loadTexts:adGenPolicerPM24HrIntervalEntry.setStatus(_A)
_AdGenPolicerPM24HrIntervalNumber_Type=Integer32
_AdGenPolicerPM24HrIntervalNumber_Object=MibTableColumn
adGenPolicerPM24HrIntervalNumber=_AdGenPolicerPM24HrIntervalNumber_Object((1,3,6,1,4,1,664,5,70,35,2,4,1,1),_AdGenPolicerPM24HrIntervalNumber_Type())
adGenPolicerPM24HrIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM24HrIntervalNumber.setStatus(_A)
_AdGenPolicerPM24HrIntervalIngressGreenFrames_Type=Counter64
_AdGenPolicerPM24HrIntervalIngressGreenFrames_Object=MibTableColumn
adGenPolicerPM24HrIntervalIngressGreenFrames=_AdGenPolicerPM24HrIntervalIngressGreenFrames_Object((1,3,6,1,4,1,664,5,70,35,2,4,1,2),_AdGenPolicerPM24HrIntervalIngressGreenFrames_Type())
adGenPolicerPM24HrIntervalIngressGreenFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM24HrIntervalIngressGreenFrames.setStatus(_A)
_AdGenPolicerPM24HrIntervalIngressYellowFrames_Type=Counter64
_AdGenPolicerPM24HrIntervalIngressYellowFrames_Object=MibTableColumn
adGenPolicerPM24HrIntervalIngressYellowFrames=_AdGenPolicerPM24HrIntervalIngressYellowFrames_Object((1,3,6,1,4,1,664,5,70,35,2,4,1,3),_AdGenPolicerPM24HrIntervalIngressYellowFrames_Type())
adGenPolicerPM24HrIntervalIngressYellowFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM24HrIntervalIngressYellowFrames.setStatus(_A)
_AdGenPolicerPM24HrIntervalIngressRedFrames_Type=Counter64
_AdGenPolicerPM24HrIntervalIngressRedFrames_Object=MibTableColumn
adGenPolicerPM24HrIntervalIngressRedFrames=_AdGenPolicerPM24HrIntervalIngressRedFrames_Object((1,3,6,1,4,1,664,5,70,35,2,4,1,4),_AdGenPolicerPM24HrIntervalIngressRedFrames_Type())
adGenPolicerPM24HrIntervalIngressRedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM24HrIntervalIngressRedFrames.setStatus(_A)
_AdGenPolicerPM24HrIntervalValidData_Type=TruthValue
_AdGenPolicerPM24HrIntervalValidData_Object=MibTableColumn
adGenPolicerPM24HrIntervalValidData=_AdGenPolicerPM24HrIntervalValidData_Object((1,3,6,1,4,1,664,5,70,35,2,4,1,5),_AdGenPolicerPM24HrIntervalValidData_Type())
adGenPolicerPM24HrIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPM24HrIntervalValidData.setStatus(_A)
_AdGenPolicerPMSlotTable_Object=MibTable
adGenPolicerPMSlotTable=_AdGenPolicerPMSlotTable_Object((1,3,6,1,4,1,664,5,70,35,2,5))
if mibBuilder.loadTexts:adGenPolicerPMSlotTable.setStatus(_A)
_AdGenPolicerPMSlotEntry_Object=MibTableRow
adGenPolicerPMSlotEntry=_AdGenPolicerPMSlotEntry_Object((1,3,6,1,4,1,664,5,70,35,2,5,1))
adGenPolicerPMSlotEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenPolicerPMSlotEntry.setStatus(_A)
class _AdGenPolicerPMResetSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdGenPolicerPMResetSlot_Type.__name__=_F
_AdGenPolicerPMResetSlot_Object=MibTableColumn
adGenPolicerPMResetSlot=_AdGenPolicerPMResetSlot_Object((1,3,6,1,4,1,664,5,70,35,2,5,1,1),_AdGenPolicerPMResetSlot_Type())
adGenPolicerPMResetSlot.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenPolicerPMResetSlot.setStatus(_A)
_AdGenPolicerPMPerPolicerTable_Object=MibTable
adGenPolicerPMPerPolicerTable=_AdGenPolicerPMPerPolicerTable_Object((1,3,6,1,4,1,664,5,70,35,2,6))
if mibBuilder.loadTexts:adGenPolicerPMPerPolicerTable.setStatus(_A)
_AdGenPolicerPMPerPolicerEntry_Object=MibTableRow
adGenPolicerPMPerPolicerEntry=_AdGenPolicerPMPerPolicerEntry_Object((1,3,6,1,4,1,664,5,70,35,2,6,1))
adGenPolicerPMPerPolicerEntry.setIndexNames((0,_C,_D),(0,_E,_G))
if mibBuilder.loadTexts:adGenPolicerPMPerPolicerEntry.setStatus(_A)
class _AdGenPolicerPMResetPolicer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdGenPolicerPMResetPolicer_Type.__name__=_F
_AdGenPolicerPMResetPolicer_Object=MibTableColumn
adGenPolicerPMResetPolicer=_AdGenPolicerPMResetPolicer_Object((1,3,6,1,4,1,664,5,70,35,2,6,1,1),_AdGenPolicerPMResetPolicer_Type())
adGenPolicerPMResetPolicer.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenPolicerPMResetPolicer.setStatus(_A)
class _AdGenPolicerPMPerPolicer15MinValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_AdGenPolicerPMPerPolicer15MinValidIntervals_Type.__name__=_F
_AdGenPolicerPMPerPolicer15MinValidIntervals_Object=MibTableColumn
adGenPolicerPMPerPolicer15MinValidIntervals=_AdGenPolicerPMPerPolicer15MinValidIntervals_Object((1,3,6,1,4,1,664,5,70,35,2,6,1,2),_AdGenPolicerPMPerPolicer15MinValidIntervals_Type())
adGenPolicerPMPerPolicer15MinValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPMPerPolicer15MinValidIntervals.setStatus(_A)
class _AdGenPolicerPMPerPolicer24HrValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenPolicerPMPerPolicer24HrValidIntervals_Type.__name__=_F
_AdGenPolicerPMPerPolicer24HrValidIntervals_Object=MibTableColumn
adGenPolicerPMPerPolicer24HrValidIntervals=_AdGenPolicerPMPerPolicer24HrValidIntervals_Object((1,3,6,1,4,1,664,5,70,35,2,6,1,3),_AdGenPolicerPMPerPolicer24HrValidIntervals_Type())
adGenPolicerPMPerPolicer24HrValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPolicerPMPerPolicer24HrValidIntervals.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'adGenPolicerPerformance':adGenPolicerPerformance,'adGenPolicerPM15MinCurrentTable':adGenPolicerPM15MinCurrentTable,'adGenPolicerPM15MinCurrentEntry':adGenPolicerPM15MinCurrentEntry,'adGenPolicerPM15MinCurrentIngressGreenFrames':adGenPolicerPM15MinCurrentIngressGreenFrames,'adGenPolicerPM15MinCurrentIngressYellowFrames':adGenPolicerPM15MinCurrentIngressYellowFrames,'adGenPolicerPM15MinCurrentIngressRedFrames':adGenPolicerPM15MinCurrentIngressRedFrames,'adGenPolicerPM15MinIntervalTable':adGenPolicerPM15MinIntervalTable,'adGenPolicerPM15MinIntervalEntry':adGenPolicerPM15MinIntervalEntry,_J:adGenPolicerPM15MinIntervalNumber,'adGenPolicerPM15MinIntervalIngressGreenFrames':adGenPolicerPM15MinIntervalIngressGreenFrames,'adGenPolicerPM15MinIntervalIngressYellowFrames':adGenPolicerPM15MinIntervalIngressYellowFrames,'adGenPolicerPM15MinIntervalIngressRedFrames':adGenPolicerPM15MinIntervalIngressRedFrames,'adGenPolicerPM15MinIntervalValidData':adGenPolicerPM15MinIntervalValidData,'adGenPolicerPM24HrCurrentTable':adGenPolicerPM24HrCurrentTable,'adGenPolicerPM24HrCurrentEntry':adGenPolicerPM24HrCurrentEntry,'adGenPolicerPM24HrCurrentIngressGreenFrames':adGenPolicerPM24HrCurrentIngressGreenFrames,'adGenPolicerPM24hrCurrentIngressYellowFrames':adGenPolicerPM24hrCurrentIngressYellowFrames,'adGenPolicerPM24HrCurrentIngressRedFrames':adGenPolicerPM24HrCurrentIngressRedFrames,'adGenPolicerPM24HrIntervalTable':adGenPolicerPM24HrIntervalTable,'adGenPolicerPM24HrIntervalEntry':adGenPolicerPM24HrIntervalEntry,_K:adGenPolicerPM24HrIntervalNumber,'adGenPolicerPM24HrIntervalIngressGreenFrames':adGenPolicerPM24HrIntervalIngressGreenFrames,'adGenPolicerPM24HrIntervalIngressYellowFrames':adGenPolicerPM24HrIntervalIngressYellowFrames,'adGenPolicerPM24HrIntervalIngressRedFrames':adGenPolicerPM24HrIntervalIngressRedFrames,'adGenPolicerPM24HrIntervalValidData':adGenPolicerPM24HrIntervalValidData,'adGenPolicerPMSlotTable':adGenPolicerPMSlotTable,'adGenPolicerPMSlotEntry':adGenPolicerPMSlotEntry,'adGenPolicerPMResetSlot':adGenPolicerPMResetSlot,'adGenPolicerPMPerPolicerTable':adGenPolicerPMPerPolicerTable,'adGenPolicerPMPerPolicerEntry':adGenPolicerPMPerPolicerEntry,'adGenPolicerPMResetPolicer':adGenPolicerPMResetPolicer,'adGenPolicerPMPerPolicer15MinValidIntervals':adGenPolicerPMPerPolicer15MinValidIntervals,'adGenPolicerPMPerPolicer24HrValidIntervals':adGenPolicerPMPerPolicer24HrValidIntervals,'adGenPolicerPMMIB':adGenPolicerPMMIB})