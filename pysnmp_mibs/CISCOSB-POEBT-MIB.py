_J='rlPethPseBtPortEntry'
_I='CISCOSB-POEBT-MIB'
_H='deliveringPower'
_G='searching'
_F='disabled'
_E='2020-04-10 00:00'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
rlPethPsePortEntry,=mibBuilder.importSymbols('CISCOSB-POE-MIB','rlPethPsePortEntry')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
rlPoeBt=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,151))
if mibBuilder.loadTexts:rlPoeBt.setRevisions((_E,_E))
class RlPoeBtClass(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noClass',1),('class1',2),('class2',3),('class3',4),('class4',5),('class5',6),('class6',7),('class7',8),('class8',9)))
_RlPethPseBtPortTable_Object=MibTable
rlPethPseBtPortTable=_RlPethPseBtPortTable_Object((1,3,6,1,4,1,9,6,1,101,151,1))
if mibBuilder.loadTexts:rlPethPseBtPortTable.setStatus(_A)
_RlPethPseBtPortEntry_Object=MibTableRow
rlPethPseBtPortEntry=_RlPethPseBtPortEntry_Object((1,3,6,1,4,1,9,6,1,101,151,1,1))
if mibBuilder.loadTexts:rlPethPseBtPortEntry.setStatus(_A)
class _RlPethPseBtPortAltAStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPseBtPortAltAStatus_Type.__name__=_C
_RlPethPseBtPortAltAStatus_Object=MibTableColumn
rlPethPseBtPortAltAStatus=_RlPethPseBtPortAltAStatus_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,1),_RlPethPseBtPortAltAStatus_Type())
rlPethPseBtPortAltAStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltAStatus.setStatus(_A)
class _RlPethPseBtPortAltADetectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),('fault',4)))
_RlPethPseBtPortAltADetectionStatus_Type.__name__=_C
_RlPethPseBtPortAltADetectionStatus_Object=MibTableColumn
rlPethPseBtPortAltADetectionStatus=_RlPethPseBtPortAltADetectionStatus_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,2),_RlPethPseBtPortAltADetectionStatus_Type())
rlPethPseBtPortAltADetectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltADetectionStatus.setStatus(_A)
_RlPethPseBtPortAltAMeasuredClass_Type=RlPoeBtClass
_RlPethPseBtPortAltAMeasuredClass_Object=MibTableColumn
rlPethPseBtPortAltAMeasuredClass=_RlPethPseBtPortAltAMeasuredClass_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,3),_RlPethPseBtPortAltAMeasuredClass_Type())
rlPethPseBtPortAltAMeasuredClass.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltAMeasuredClass.setStatus(_A)
_RlPethPseBtPortAltAAssignedClass_Type=RlPoeBtClass
_RlPethPseBtPortAltAAssignedClass_Object=MibTableColumn
rlPethPseBtPortAltAAssignedClass=_RlPethPseBtPortAltAAssignedClass_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,4),_RlPethPseBtPortAltAAssignedClass_Type())
rlPethPseBtPortAltAAssignedClass.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltAAssignedClass.setStatus(_A)
class _RlPethPseBtPortAltAAllocPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPseBtPortAltAAllocPower_Type.__name__=_C
_RlPethPseBtPortAltAAllocPower_Object=MibTableColumn
rlPethPseBtPortAltAAllocPower=_RlPethPseBtPortAltAAllocPower_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,5),_RlPethPseBtPortAltAAllocPower_Type())
rlPethPseBtPortAltAAllocPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltAAllocPower.setStatus(_A)
_RlPethPseBtPortAltAInvalidSigCounter_Type=Counter32
_RlPethPseBtPortAltAInvalidSigCounter_Object=MibTableColumn
rlPethPseBtPortAltAInvalidSigCounter=_RlPethPseBtPortAltAInvalidSigCounter_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,6),_RlPethPseBtPortAltAInvalidSigCounter_Type())
rlPethPseBtPortAltAInvalidSigCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltAInvalidSigCounter.setStatus(_A)
_RlPethPseBtPortAltAPowerDeniedCounter_Type=Counter32
_RlPethPseBtPortAltAPowerDeniedCounter_Object=MibTableColumn
rlPethPseBtPortAltAPowerDeniedCounter=_RlPethPseBtPortAltAPowerDeniedCounter_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,7),_RlPethPseBtPortAltAPowerDeniedCounter_Type())
rlPethPseBtPortAltAPowerDeniedCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltAPowerDeniedCounter.setStatus(_A)
_RlPethPseBtPortAltAOverloadCounter_Type=Counter32
_RlPethPseBtPortAltAOverloadCounter_Object=MibTableColumn
rlPethPseBtPortAltAOverloadCounter=_RlPethPseBtPortAltAOverloadCounter_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,8),_RlPethPseBtPortAltAOverloadCounter_Type())
rlPethPseBtPortAltAOverloadCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltAOverloadCounter.setStatus(_A)
_RlPethPseBtPortAltAMPSAbsentCounter_Type=Counter32
_RlPethPseBtPortAltAMPSAbsentCounter_Object=MibTableColumn
rlPethPseBtPortAltAMPSAbsentCounter=_RlPethPseBtPortAltAMPSAbsentCounter_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,9),_RlPethPseBtPortAltAMPSAbsentCounter_Type())
rlPethPseBtPortAltAMPSAbsentCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltAMPSAbsentCounter.setStatus(_A)
class _RlPethPseBtPortAltBStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPseBtPortAltBStatus_Type.__name__=_C
_RlPethPseBtPortAltBStatus_Object=MibTableColumn
rlPethPseBtPortAltBStatus=_RlPethPseBtPortAltBStatus_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,10),_RlPethPseBtPortAltBStatus_Type())
rlPethPseBtPortAltBStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltBStatus.setStatus(_A)
class _RlPethPseBtPortAltBDetectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),('fault',4)))
_RlPethPseBtPortAltBDetectionStatus_Type.__name__=_C
_RlPethPseBtPortAltBDetectionStatus_Object=MibTableColumn
rlPethPseBtPortAltBDetectionStatus=_RlPethPseBtPortAltBDetectionStatus_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,11),_RlPethPseBtPortAltBDetectionStatus_Type())
rlPethPseBtPortAltBDetectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltBDetectionStatus.setStatus(_A)
_RlPethPseBtPortAltBMeasuredClass_Type=RlPoeBtClass
_RlPethPseBtPortAltBMeasuredClass_Object=MibTableColumn
rlPethPseBtPortAltBMeasuredClass=_RlPethPseBtPortAltBMeasuredClass_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,12),_RlPethPseBtPortAltBMeasuredClass_Type())
rlPethPseBtPortAltBMeasuredClass.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltBMeasuredClass.setStatus(_A)
_RlPethPseBtPortAltBAssignedClass_Type=RlPoeBtClass
_RlPethPseBtPortAltBAssignedClass_Object=MibTableColumn
rlPethPseBtPortAltBAssignedClass=_RlPethPseBtPortAltBAssignedClass_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,13),_RlPethPseBtPortAltBAssignedClass_Type())
rlPethPseBtPortAltBAssignedClass.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltBAssignedClass.setStatus(_A)
class _RlPethPseBtPortAltBAllocPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPethPseBtPortAltBAllocPower_Type.__name__=_C
_RlPethPseBtPortAltBAllocPower_Object=MibTableColumn
rlPethPseBtPortAltBAllocPower=_RlPethPseBtPortAltBAllocPower_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,14),_RlPethPseBtPortAltBAllocPower_Type())
rlPethPseBtPortAltBAllocPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltBAllocPower.setStatus(_A)
_RlPethPseBtPortAltBInvalidSigCounter_Type=Counter32
_RlPethPseBtPortAltBInvalidSigCounter_Object=MibTableColumn
rlPethPseBtPortAltBInvalidSigCounter=_RlPethPseBtPortAltBInvalidSigCounter_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,15),_RlPethPseBtPortAltBInvalidSigCounter_Type())
rlPethPseBtPortAltBInvalidSigCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltBInvalidSigCounter.setStatus(_A)
_RlPethPseBtPortAltBPowerDeniedCounter_Type=Counter32
_RlPethPseBtPortAltBPowerDeniedCounter_Object=MibTableColumn
rlPethPseBtPortAltBPowerDeniedCounter=_RlPethPseBtPortAltBPowerDeniedCounter_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,16),_RlPethPseBtPortAltBPowerDeniedCounter_Type())
rlPethPseBtPortAltBPowerDeniedCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltBPowerDeniedCounter.setStatus(_A)
_RlPethPseBtPortAltBOverloadCounter_Type=Counter32
_RlPethPseBtPortAltBOverloadCounter_Object=MibTableColumn
rlPethPseBtPortAltBOverloadCounter=_RlPethPseBtPortAltBOverloadCounter_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,17),_RlPethPseBtPortAltBOverloadCounter_Type())
rlPethPseBtPortAltBOverloadCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltBOverloadCounter.setStatus(_A)
_RlPethPseBtPortAltBMPSAbsentCounter_Type=Counter32
_RlPethPseBtPortAltBMPSAbsentCounter_Object=MibTableColumn
rlPethPseBtPortAltBMPSAbsentCounter=_RlPethPseBtPortAltBMPSAbsentCounter_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,18),_RlPethPseBtPortAltBMPSAbsentCounter_Type())
rlPethPseBtPortAltBMPSAbsentCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltBMPSAbsentCounter.setStatus(_A)
class _RlPethPseBtPortPowerClassMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('powerClassMethodRegular',1),('powerClassMethodAutoClass',2)))
_RlPethPseBtPortPowerClassMethod_Type.__name__=_C
_RlPethPseBtPortPowerClassMethod_Object=MibTableColumn
rlPethPseBtPortPowerClassMethod=_RlPethPseBtPortPowerClassMethod_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,19),_RlPethPseBtPortPowerClassMethod_Type())
rlPethPseBtPortPowerClassMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortPowerClassMethod.setStatus(_A)
class _RlPethPseBtPortAltAStatusDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,120))
_RlPethPseBtPortAltAStatusDescription_Type.__name__=_D
_RlPethPseBtPortAltAStatusDescription_Object=MibTableColumn
rlPethPseBtPortAltAStatusDescription=_RlPethPseBtPortAltAStatusDescription_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,20),_RlPethPseBtPortAltAStatusDescription_Type())
rlPethPseBtPortAltAStatusDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltAStatusDescription.setStatus(_A)
class _RlPethPseBtPortAltBStatusDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,120))
_RlPethPseBtPortAltBStatusDescription_Type.__name__=_D
_RlPethPseBtPortAltBStatusDescription_Object=MibTableColumn
rlPethPseBtPortAltBStatusDescription=_RlPethPseBtPortAltBStatusDescription_Object((1,3,6,1,4,1,9,6,1,101,151,1,1,21),_RlPethPseBtPortAltBStatusDescription_Type())
rlPethPseBtPortAltBStatusDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPethPseBtPortAltBStatusDescription.setStatus(_A)
rlPethPsePortEntry.registerAugmentions((_I,_J))
rlPethPseBtPortEntry.setIndexNames(*rlPethPsePortEntry.getIndexNames())
mibBuilder.exportSymbols(_I,**{'RlPoeBtClass':RlPoeBtClass,'rlPoeBt':rlPoeBt,'rlPethPseBtPortTable':rlPethPseBtPortTable,_J:rlPethPseBtPortEntry,'rlPethPseBtPortAltAStatus':rlPethPseBtPortAltAStatus,'rlPethPseBtPortAltADetectionStatus':rlPethPseBtPortAltADetectionStatus,'rlPethPseBtPortAltAMeasuredClass':rlPethPseBtPortAltAMeasuredClass,'rlPethPseBtPortAltAAssignedClass':rlPethPseBtPortAltAAssignedClass,'rlPethPseBtPortAltAAllocPower':rlPethPseBtPortAltAAllocPower,'rlPethPseBtPortAltAInvalidSigCounter':rlPethPseBtPortAltAInvalidSigCounter,'rlPethPseBtPortAltAPowerDeniedCounter':rlPethPseBtPortAltAPowerDeniedCounter,'rlPethPseBtPortAltAOverloadCounter':rlPethPseBtPortAltAOverloadCounter,'rlPethPseBtPortAltAMPSAbsentCounter':rlPethPseBtPortAltAMPSAbsentCounter,'rlPethPseBtPortAltBStatus':rlPethPseBtPortAltBStatus,'rlPethPseBtPortAltBDetectionStatus':rlPethPseBtPortAltBDetectionStatus,'rlPethPseBtPortAltBMeasuredClass':rlPethPseBtPortAltBMeasuredClass,'rlPethPseBtPortAltBAssignedClass':rlPethPseBtPortAltBAssignedClass,'rlPethPseBtPortAltBAllocPower':rlPethPseBtPortAltBAllocPower,'rlPethPseBtPortAltBInvalidSigCounter':rlPethPseBtPortAltBInvalidSigCounter,'rlPethPseBtPortAltBPowerDeniedCounter':rlPethPseBtPortAltBPowerDeniedCounter,'rlPethPseBtPortAltBOverloadCounter':rlPethPseBtPortAltBOverloadCounter,'rlPethPseBtPortAltBMPSAbsentCounter':rlPethPseBtPortAltBMPSAbsentCounter,'rlPethPseBtPortPowerClassMethod':rlPethPseBtPortPowerClassMethod,'rlPethPseBtPortAltAStatusDescription':rlPethPseBtPortAltAStatusDescription,'rlPethPseBtPortAltBStatusDescription':rlPethPseBtPortAltBStatusDescription})