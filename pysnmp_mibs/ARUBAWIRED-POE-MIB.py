_A9='arubaWiredPoePethPseModuleTableGroup'
_A8='arubaWiredPoePethMainPseTableGroup'
_A7='arubaWiredPoePethPseFourPairPortTableGroup'
_A6='arubaWiredPoePethPsePortTableGroup'
_A5='arubaWiredPoePethPseModuleTable'
_A4='arubaWiredPoePethMainPseTable'
_A3='arubaWiredPoePethPsePortTable'
_A2='arubaWiredPoePethPseModuleAlwaysOnPoe'
_A1='arubaWiredPoePethMainPseRedundantPower'
_A0='arubaWiredPoePethMainPseFailoverPower'
_z='arubaWiredPoePethMainPseReservedPower'
_y='arubaWiredPoePethPsePortMPSAbsentCounterPairB'
_x='arubaWiredPoePethPsePortMPSAbsentCounterPairA'
_w='arubaWiredPoePethPsePortOverLoadCounterPairB'
_v='arubaWiredPoePethPsePortOverLoadCounterPairA'
_u='arubaWiredPoePethPsePortPowerDeniedCounterPairB'
_t='arubaWiredPoePethPsePortPowerDeniedCounterPairA'
_s='arubaWiredPoePethPsePortInvalidSignatureCounterPairB'
_r='arubaWiredPoePethPsePortInvalidSignatureCounterPairA'
_q='arubaWiredPoePethPsePortPseAssignedClassB'
_p='arubaWiredPoePethPsePortPseAssignedClassA'
_o='arubaWiredPoePethPsePortPowerClassificationPairB'
_n='arubaWiredPoePethPsePortPowerClassificationPairA'
_m='arubaWiredPoePethPsePortDetectionStatusPairB'
_l='arubaWiredPoePethPsePortDetectionStatusPairA'
_k='arubaWiredPoePethPsePortPoECycle'
_j='arubaWiredPoePethPsePortPseAssignedClass'
_i='arubaWiredPoePethPsePortPowerClassification'
_h='arubaWiredPoePethPsePortPdSignature'
_g='arubaWiredPoePethPsePortOperStatus'
_f='arubaWiredPoePethPsePortPeakPower'
_e='arubaWiredPoePethPsePortAveragePower'
_d='arubaWiredPoePethPsePortPowerDrawn'
_c='arubaWiredPoePethPsePortReservedPower'
_b='arubaWiredPoePethPsePortVoltage'
_a='arubaWiredPoePethPsePortCurrent'
_Z='arubaWiredPoePethPsePortRpd'
_Y='arubaWiredPoePethPsePortPreStdDetect'
_X='arubaWiredPoePethPsePortPowerAllocateBy'
_W='arubaWiredPoePethMainPseEntry'
_V='arubaWiredPoePethPseFourPairPortEntry'
_U='arubaWiredPoePethPsePortEntry'
_T='not-accessible'
_S='arubaWiredPoePethPseModuleSlotIndex'
_R='arubaWiredPoePethPseModuleGroupIndex'
_Q='class6'
_P='class0'
_O='read-write'
_N='Watts'
_M='class5'
_L='milliwatts'
_K='on'
_J='off'
_I='class4'
_H='class3'
_G='class2'
_F='class1'
_E='Counter32'
_D='Integer32'
_C='read-only'
_B='ARUBAWIRED-POE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
pethMainPseEntry,pethPsePortEntry=mibBuilder.importSymbols('POWER-ETHERNET-MIB','pethMainPseEntry','pethPsePortEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_E,'Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
arubaWiredPoeMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,8))
if mibBuilder.loadTexts:arubaWiredPoeMIB.setRevisions(('2019-06-24 00:00',))
_ArubaWiredPoePethPsePort_ObjectIdentity=ObjectIdentity
arubaWiredPoePethPsePort=_ArubaWiredPoePethPsePort_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,8,1))
_ArubaWiredPoePethPsePortTable_Object=MibTable
arubaWiredPoePethPsePortTable=_ArubaWiredPoePethPsePortTable_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1))
if mibBuilder.loadTexts:arubaWiredPoePethPsePortTable.setStatus(_A)
_ArubaWiredPoePethPsePortEntry_Object=MibTableRow
arubaWiredPoePethPsePortEntry=_ArubaWiredPoePethPsePortEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1))
if mibBuilder.loadTexts:arubaWiredPoePethPsePortEntry.setStatus(_A)
class _ArubaWiredPoePethPsePortPowerAllocateBy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('usage',1),('class',2)))
_ArubaWiredPoePethPsePortPowerAllocateBy_Type.__name__=_D
_ArubaWiredPoePethPsePortPowerAllocateBy_Object=MibTableColumn
arubaWiredPoePethPsePortPowerAllocateBy=_ArubaWiredPoePethPsePortPowerAllocateBy_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,1),_ArubaWiredPoePethPsePortPowerAllocateBy_Type())
arubaWiredPoePethPsePortPowerAllocateBy.setMaxAccess(_O)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPowerAllocateBy.setStatus(_A)
class _ArubaWiredPoePethPsePortPreStdDetect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ArubaWiredPoePethPsePortPreStdDetect_Type.__name__=_D
_ArubaWiredPoePethPsePortPreStdDetect_Object=MibTableColumn
arubaWiredPoePethPsePortPreStdDetect=_ArubaWiredPoePethPsePortPreStdDetect_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,2),_ArubaWiredPoePethPsePortPreStdDetect_Type())
arubaWiredPoePethPsePortPreStdDetect.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPreStdDetect.setStatus(_A)
class _ArubaWiredPoePethPsePortRpd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ArubaWiredPoePethPsePortRpd_Type.__name__=_D
_ArubaWiredPoePethPsePortRpd_Object=MibTableColumn
arubaWiredPoePethPsePortRpd=_ArubaWiredPoePethPsePortRpd_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,3),_ArubaWiredPoePethPsePortRpd_Type())
arubaWiredPoePethPsePortRpd.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortRpd.setStatus(_A)
class _ArubaWiredPoePethPsePortCurrent_Type(Integer32):defaultValue=0
_ArubaWiredPoePethPsePortCurrent_Type.__name__=_D
_ArubaWiredPoePethPsePortCurrent_Object=MibTableColumn
arubaWiredPoePethPsePortCurrent=_ArubaWiredPoePethPsePortCurrent_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,4),_ArubaWiredPoePethPsePortCurrent_Type())
arubaWiredPoePethPsePortCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortCurrent.setStatus(_A)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortCurrent.setUnits('milliamperes')
class _ArubaWiredPoePethPsePortVoltage_Type(Integer32):defaultValue=0
_ArubaWiredPoePethPsePortVoltage_Type.__name__=_D
_ArubaWiredPoePethPsePortVoltage_Object=MibTableColumn
arubaWiredPoePethPsePortVoltage=_ArubaWiredPoePethPsePortVoltage_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,5),_ArubaWiredPoePethPsePortVoltage_Type())
arubaWiredPoePethPsePortVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortVoltage.setStatus(_A)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortVoltage.setUnits('deciVolts')
class _ArubaWiredPoePethPsePortReservedPower_Type(Integer32):defaultValue=0
_ArubaWiredPoePethPsePortReservedPower_Type.__name__=_D
_ArubaWiredPoePethPsePortReservedPower_Object=MibTableColumn
arubaWiredPoePethPsePortReservedPower=_ArubaWiredPoePethPsePortReservedPower_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,6),_ArubaWiredPoePethPsePortReservedPower_Type())
arubaWiredPoePethPsePortReservedPower.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortReservedPower.setStatus(_A)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortReservedPower.setUnits(_L)
class _ArubaWiredPoePethPsePortPowerDrawn_Type(Integer32):defaultValue=0
_ArubaWiredPoePethPsePortPowerDrawn_Type.__name__=_D
_ArubaWiredPoePethPsePortPowerDrawn_Object=MibTableColumn
arubaWiredPoePethPsePortPowerDrawn=_ArubaWiredPoePethPsePortPowerDrawn_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,7),_ArubaWiredPoePethPsePortPowerDrawn_Type())
arubaWiredPoePethPsePortPowerDrawn.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPowerDrawn.setStatus(_A)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPowerDrawn.setUnits(_L)
class _ArubaWiredPoePethPsePortAveragePower_Type(Integer32):defaultValue=0
_ArubaWiredPoePethPsePortAveragePower_Type.__name__=_D
_ArubaWiredPoePethPsePortAveragePower_Object=MibTableColumn
arubaWiredPoePethPsePortAveragePower=_ArubaWiredPoePethPsePortAveragePower_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,8),_ArubaWiredPoePethPsePortAveragePower_Type())
arubaWiredPoePethPsePortAveragePower.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortAveragePower.setStatus(_A)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortAveragePower.setUnits(_L)
class _ArubaWiredPoePethPsePortPeakPower_Type(Integer32):defaultValue=0
_ArubaWiredPoePethPsePortPeakPower_Type.__name__=_D
_ArubaWiredPoePethPsePortPeakPower_Object=MibTableColumn
arubaWiredPoePethPsePortPeakPower=_ArubaWiredPoePethPsePortPeakPower_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,9),_ArubaWiredPoePethPsePortPeakPower_Type())
arubaWiredPoePethPsePortPeakPower.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPeakPower.setStatus(_A)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPeakPower.setUnits(_L)
class _ArubaWiredPoePethPsePortOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('deny',1),(_J,2),(_K,3)))
_ArubaWiredPoePethPsePortOperStatus_Type.__name__=_D
_ArubaWiredPoePethPsePortOperStatus_Object=MibTableColumn
arubaWiredPoePethPsePortOperStatus=_ArubaWiredPoePethPsePortOperStatus_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,10),_ArubaWiredPoePethPsePortOperStatus_Type())
arubaWiredPoePethPsePortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortOperStatus.setStatus(_A)
class _ArubaWiredPoePethPsePortPdSignature_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknownSignature',0),('singleSignature',1),('dualSignature',2)))
_ArubaWiredPoePethPsePortPdSignature_Type.__name__=_D
_ArubaWiredPoePethPsePortPdSignature_Object=MibTableColumn
arubaWiredPoePethPsePortPdSignature=_ArubaWiredPoePethPsePortPdSignature_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,11),_ArubaWiredPoePethPsePortPdSignature_Type())
arubaWiredPoePethPsePortPdSignature.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPdSignature.setStatus(_A)
class _ArubaWiredPoePethPsePortPowerClassification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,1),(_F,2),(_G,3),(_H,4),(_I,5),(_M,6),(_Q,7),('class7',8),('class8',9)))
_ArubaWiredPoePethPsePortPowerClassification_Type.__name__=_D
_ArubaWiredPoePethPsePortPowerClassification_Object=MibTableColumn
arubaWiredPoePethPsePortPowerClassification=_ArubaWiredPoePethPsePortPowerClassification_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,12),_ArubaWiredPoePethPsePortPowerClassification_Type())
arubaWiredPoePethPsePortPowerClassification.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPowerClassification.setStatus(_A)
class _ArubaWiredPoePethPsePortPseAssignedClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,1),(_F,2),(_G,3),(_H,4),(_I,5),(_M,6),(_Q,7)))
_ArubaWiredPoePethPsePortPseAssignedClass_Type.__name__=_D
_ArubaWiredPoePethPsePortPseAssignedClass_Object=MibTableColumn
arubaWiredPoePethPsePortPseAssignedClass=_ArubaWiredPoePethPsePortPseAssignedClass_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,13),_ArubaWiredPoePethPsePortPseAssignedClass_Type())
arubaWiredPoePethPsePortPseAssignedClass.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPseAssignedClass.setStatus(_A)
class _ArubaWiredPoePethPsePortPoECycle_Type(Integer32):defaultValue=1
_ArubaWiredPoePethPsePortPoECycle_Type.__name__=_D
_ArubaWiredPoePethPsePortPoECycle_Object=MibTableColumn
arubaWiredPoePethPsePortPoECycle=_ArubaWiredPoePethPsePortPoECycle_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,1,1,14),_ArubaWiredPoePethPsePortPoECycle_Type())
arubaWiredPoePethPsePortPoECycle.setMaxAccess(_O)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPoECycle.setStatus(_A)
_ArubaWiredPoePethPseFourPairPortTable_Object=MibTable
arubaWiredPoePethPseFourPairPortTable=_ArubaWiredPoePethPseFourPairPortTable_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2))
if mibBuilder.loadTexts:arubaWiredPoePethPseFourPairPortTable.setStatus(_A)
_ArubaWiredPoePethPseFourPairPortEntry_Object=MibTableRow
arubaWiredPoePethPseFourPairPortEntry=_ArubaWiredPoePethPseFourPairPortEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1))
if mibBuilder.loadTexts:arubaWiredPoePethPseFourPairPortEntry.setStatus(_A)
class _ArubaWiredPoePethPsePortDetectionStatusPairA_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('searchingAltA',1),('deliveringPowerAltA',2),('faultAltA',3)))
_ArubaWiredPoePethPsePortDetectionStatusPairA_Type.__name__=_D
_ArubaWiredPoePethPsePortDetectionStatusPairA_Object=MibTableColumn
arubaWiredPoePethPsePortDetectionStatusPairA=_ArubaWiredPoePethPsePortDetectionStatusPairA_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,1),_ArubaWiredPoePethPsePortDetectionStatusPairA_Type())
arubaWiredPoePethPsePortDetectionStatusPairA.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortDetectionStatusPairA.setStatus(_A)
class _ArubaWiredPoePethPsePortDetectionStatusPairB_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('searchingAltB',1),('deliveringPowerAltB',2),('faultAltB',3)))
_ArubaWiredPoePethPsePortDetectionStatusPairB_Type.__name__=_D
_ArubaWiredPoePethPsePortDetectionStatusPairB_Object=MibTableColumn
arubaWiredPoePethPsePortDetectionStatusPairB=_ArubaWiredPoePethPsePortDetectionStatusPairB_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,2),_ArubaWiredPoePethPsePortDetectionStatusPairB_Type())
arubaWiredPoePethPsePortDetectionStatusPairB.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortDetectionStatusPairB.setStatus(_A)
class _ArubaWiredPoePethPsePortPowerClassificationPairA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_M,5)))
_ArubaWiredPoePethPsePortPowerClassificationPairA_Type.__name__=_D
_ArubaWiredPoePethPsePortPowerClassificationPairA_Object=MibTableColumn
arubaWiredPoePethPsePortPowerClassificationPairA=_ArubaWiredPoePethPsePortPowerClassificationPairA_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,3),_ArubaWiredPoePethPsePortPowerClassificationPairA_Type())
arubaWiredPoePethPsePortPowerClassificationPairA.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPowerClassificationPairA.setStatus(_A)
class _ArubaWiredPoePethPsePortPowerClassificationPairB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4),(_M,5)))
_ArubaWiredPoePethPsePortPowerClassificationPairB_Type.__name__=_D
_ArubaWiredPoePethPsePortPowerClassificationPairB_Object=MibTableColumn
arubaWiredPoePethPsePortPowerClassificationPairB=_ArubaWiredPoePethPsePortPowerClassificationPairB_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,4),_ArubaWiredPoePethPsePortPowerClassificationPairB_Type())
arubaWiredPoePethPsePortPowerClassificationPairB.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPowerClassificationPairB.setStatus(_A)
class _ArubaWiredPoePethPsePortPseAssignedClassA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4)))
_ArubaWiredPoePethPsePortPseAssignedClassA_Type.__name__=_D
_ArubaWiredPoePethPsePortPseAssignedClassA_Object=MibTableColumn
arubaWiredPoePethPsePortPseAssignedClassA=_ArubaWiredPoePethPsePortPseAssignedClassA_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,5),_ArubaWiredPoePethPsePortPseAssignedClassA_Type())
arubaWiredPoePethPsePortPseAssignedClassA.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPseAssignedClassA.setStatus(_A)
class _ArubaWiredPoePethPsePortPseAssignedClassB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_I,4)))
_ArubaWiredPoePethPsePortPseAssignedClassB_Type.__name__=_D
_ArubaWiredPoePethPsePortPseAssignedClassB_Object=MibTableColumn
arubaWiredPoePethPsePortPseAssignedClassB=_ArubaWiredPoePethPsePortPseAssignedClassB_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,6),_ArubaWiredPoePethPsePortPseAssignedClassB_Type())
arubaWiredPoePethPsePortPseAssignedClassB.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPseAssignedClassB.setStatus(_A)
class _ArubaWiredPoePethPsePortInvalidSignatureCounterPairA_Type(Counter32):defaultValue=0
_ArubaWiredPoePethPsePortInvalidSignatureCounterPairA_Type.__name__=_E
_ArubaWiredPoePethPsePortInvalidSignatureCounterPairA_Object=MibTableColumn
arubaWiredPoePethPsePortInvalidSignatureCounterPairA=_ArubaWiredPoePethPsePortInvalidSignatureCounterPairA_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,7),_ArubaWiredPoePethPsePortInvalidSignatureCounterPairA_Type())
arubaWiredPoePethPsePortInvalidSignatureCounterPairA.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortInvalidSignatureCounterPairA.setStatus(_A)
class _ArubaWiredPoePethPsePortInvalidSignatureCounterPairB_Type(Counter32):defaultValue=0
_ArubaWiredPoePethPsePortInvalidSignatureCounterPairB_Type.__name__=_E
_ArubaWiredPoePethPsePortInvalidSignatureCounterPairB_Object=MibTableColumn
arubaWiredPoePethPsePortInvalidSignatureCounterPairB=_ArubaWiredPoePethPsePortInvalidSignatureCounterPairB_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,8),_ArubaWiredPoePethPsePortInvalidSignatureCounterPairB_Type())
arubaWiredPoePethPsePortInvalidSignatureCounterPairB.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortInvalidSignatureCounterPairB.setStatus(_A)
class _ArubaWiredPoePethPsePortPowerDeniedCounterPairA_Type(Counter32):defaultValue=0
_ArubaWiredPoePethPsePortPowerDeniedCounterPairA_Type.__name__=_E
_ArubaWiredPoePethPsePortPowerDeniedCounterPairA_Object=MibTableColumn
arubaWiredPoePethPsePortPowerDeniedCounterPairA=_ArubaWiredPoePethPsePortPowerDeniedCounterPairA_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,9),_ArubaWiredPoePethPsePortPowerDeniedCounterPairA_Type())
arubaWiredPoePethPsePortPowerDeniedCounterPairA.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPowerDeniedCounterPairA.setStatus(_A)
class _ArubaWiredPoePethPsePortPowerDeniedCounterPairB_Type(Counter32):defaultValue=0
_ArubaWiredPoePethPsePortPowerDeniedCounterPairB_Type.__name__=_E
_ArubaWiredPoePethPsePortPowerDeniedCounterPairB_Object=MibTableColumn
arubaWiredPoePethPsePortPowerDeniedCounterPairB=_ArubaWiredPoePethPsePortPowerDeniedCounterPairB_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,10),_ArubaWiredPoePethPsePortPowerDeniedCounterPairB_Type())
arubaWiredPoePethPsePortPowerDeniedCounterPairB.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortPowerDeniedCounterPairB.setStatus(_A)
class _ArubaWiredPoePethPsePortOverLoadCounterPairA_Type(Counter32):defaultValue=0
_ArubaWiredPoePethPsePortOverLoadCounterPairA_Type.__name__=_E
_ArubaWiredPoePethPsePortOverLoadCounterPairA_Object=MibTableColumn
arubaWiredPoePethPsePortOverLoadCounterPairA=_ArubaWiredPoePethPsePortOverLoadCounterPairA_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,11),_ArubaWiredPoePethPsePortOverLoadCounterPairA_Type())
arubaWiredPoePethPsePortOverLoadCounterPairA.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortOverLoadCounterPairA.setStatus(_A)
class _ArubaWiredPoePethPsePortOverLoadCounterPairB_Type(Counter32):defaultValue=0
_ArubaWiredPoePethPsePortOverLoadCounterPairB_Type.__name__=_E
_ArubaWiredPoePethPsePortOverLoadCounterPairB_Object=MibTableColumn
arubaWiredPoePethPsePortOverLoadCounterPairB=_ArubaWiredPoePethPsePortOverLoadCounterPairB_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,12),_ArubaWiredPoePethPsePortOverLoadCounterPairB_Type())
arubaWiredPoePethPsePortOverLoadCounterPairB.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortOverLoadCounterPairB.setStatus(_A)
class _ArubaWiredPoePethPsePortMPSAbsentCounterPairA_Type(Counter32):defaultValue=0
_ArubaWiredPoePethPsePortMPSAbsentCounterPairA_Type.__name__=_E
_ArubaWiredPoePethPsePortMPSAbsentCounterPairA_Object=MibTableColumn
arubaWiredPoePethPsePortMPSAbsentCounterPairA=_ArubaWiredPoePethPsePortMPSAbsentCounterPairA_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,13),_ArubaWiredPoePethPsePortMPSAbsentCounterPairA_Type())
arubaWiredPoePethPsePortMPSAbsentCounterPairA.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortMPSAbsentCounterPairA.setStatus(_A)
class _ArubaWiredPoePethPsePortMPSAbsentCounterPairB_Type(Counter32):defaultValue=0
_ArubaWiredPoePethPsePortMPSAbsentCounterPairB_Type.__name__=_E
_ArubaWiredPoePethPsePortMPSAbsentCounterPairB_Object=MibTableColumn
arubaWiredPoePethPsePortMPSAbsentCounterPairB=_ArubaWiredPoePethPsePortMPSAbsentCounterPairB_Object((1,3,6,1,4,1,47196,4,1,1,3,8,1,2,1,14),_ArubaWiredPoePethPsePortMPSAbsentCounterPairB_Type())
arubaWiredPoePethPsePortMPSAbsentCounterPairB.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPsePortMPSAbsentCounterPairB.setStatus(_A)
_ArubaWiredPoeConformance_ObjectIdentity=ObjectIdentity
arubaWiredPoeConformance=_ArubaWiredPoeConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,8,2))
_ArubaWiredPoeCompliances_ObjectIdentity=ObjectIdentity
arubaWiredPoeCompliances=_ArubaWiredPoeCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,8,2,1))
_ArubaWiredPoeGroups_ObjectIdentity=ObjectIdentity
arubaWiredPoeGroups=_ArubaWiredPoeGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,8,2,2))
_ArubaWiredPoePethMainPse_ObjectIdentity=ObjectIdentity
arubaWiredPoePethMainPse=_ArubaWiredPoePethMainPse_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,8,3))
_ArubaWiredPoePethMainPseTable_Object=MibTable
arubaWiredPoePethMainPseTable=_ArubaWiredPoePethMainPseTable_Object((1,3,6,1,4,1,47196,4,1,1,3,8,3,1))
if mibBuilder.loadTexts:arubaWiredPoePethMainPseTable.setStatus(_A)
_ArubaWiredPoePethMainPseEntry_Object=MibTableRow
arubaWiredPoePethMainPseEntry=_ArubaWiredPoePethMainPseEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,8,3,1,1))
if mibBuilder.loadTexts:arubaWiredPoePethMainPseEntry.setStatus(_A)
class _ArubaWiredPoePethMainPseReservedPower_Type(Integer32):defaultValue=0
_ArubaWiredPoePethMainPseReservedPower_Type.__name__=_D
_ArubaWiredPoePethMainPseReservedPower_Object=MibTableColumn
arubaWiredPoePethMainPseReservedPower=_ArubaWiredPoePethMainPseReservedPower_Object((1,3,6,1,4,1,47196,4,1,1,3,8,3,1,1,1),_ArubaWiredPoePethMainPseReservedPower_Type())
arubaWiredPoePethMainPseReservedPower.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethMainPseReservedPower.setStatus(_A)
if mibBuilder.loadTexts:arubaWiredPoePethMainPseReservedPower.setUnits(_N)
class _ArubaWiredPoePethMainPseFailoverPower_Type(Integer32):defaultValue=0
_ArubaWiredPoePethMainPseFailoverPower_Type.__name__=_D
_ArubaWiredPoePethMainPseFailoverPower_Object=MibTableColumn
arubaWiredPoePethMainPseFailoverPower=_ArubaWiredPoePethMainPseFailoverPower_Object((1,3,6,1,4,1,47196,4,1,1,3,8,3,1,1,2),_ArubaWiredPoePethMainPseFailoverPower_Type())
arubaWiredPoePethMainPseFailoverPower.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethMainPseFailoverPower.setStatus(_A)
if mibBuilder.loadTexts:arubaWiredPoePethMainPseFailoverPower.setUnits(_N)
class _ArubaWiredPoePethMainPseRedundantPower_Type(Integer32):defaultValue=0
_ArubaWiredPoePethMainPseRedundantPower_Type.__name__=_D
_ArubaWiredPoePethMainPseRedundantPower_Object=MibTableColumn
arubaWiredPoePethMainPseRedundantPower=_ArubaWiredPoePethMainPseRedundantPower_Object((1,3,6,1,4,1,47196,4,1,1,3,8,3,1,1,3),_ArubaWiredPoePethMainPseRedundantPower_Type())
arubaWiredPoePethMainPseRedundantPower.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethMainPseRedundantPower.setStatus(_A)
if mibBuilder.loadTexts:arubaWiredPoePethMainPseRedundantPower.setUnits(_N)
_ArubaWiredPoePethPseModule_ObjectIdentity=ObjectIdentity
arubaWiredPoePethPseModule=_ArubaWiredPoePethPseModule_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,8,4))
_ArubaWiredPoePethPseModuleTable_Object=MibTable
arubaWiredPoePethPseModuleTable=_ArubaWiredPoePethPseModuleTable_Object((1,3,6,1,4,1,47196,4,1,1,3,8,4,1))
if mibBuilder.loadTexts:arubaWiredPoePethPseModuleTable.setStatus(_A)
_ArubaWiredPoePethPseModuleEntry_Object=MibTableRow
arubaWiredPoePethPseModuleEntry=_ArubaWiredPoePethPseModuleEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,8,4,1,1))
arubaWiredPoePethPseModuleEntry.setIndexNames((0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:arubaWiredPoePethPseModuleEntry.setStatus(_A)
class _ArubaWiredPoePethPseModuleGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredPoePethPseModuleGroupIndex_Type.__name__=_D
_ArubaWiredPoePethPseModuleGroupIndex_Object=MibTableColumn
arubaWiredPoePethPseModuleGroupIndex=_ArubaWiredPoePethPseModuleGroupIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,8,4,1,1,1),_ArubaWiredPoePethPseModuleGroupIndex_Type())
arubaWiredPoePethPseModuleGroupIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:arubaWiredPoePethPseModuleGroupIndex.setStatus(_A)
class _ArubaWiredPoePethPseModuleSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredPoePethPseModuleSlotIndex_Type.__name__=_D
_ArubaWiredPoePethPseModuleSlotIndex_Object=MibTableColumn
arubaWiredPoePethPseModuleSlotIndex=_ArubaWiredPoePethPseModuleSlotIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,8,4,1,1,2),_ArubaWiredPoePethPseModuleSlotIndex_Type())
arubaWiredPoePethPseModuleSlotIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:arubaWiredPoePethPseModuleSlotIndex.setStatus(_A)
class _ArubaWiredPoePethPseModuleAlwaysOnPoe_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ArubaWiredPoePethPseModuleAlwaysOnPoe_Type.__name__=_D
_ArubaWiredPoePethPseModuleAlwaysOnPoe_Object=MibTableColumn
arubaWiredPoePethPseModuleAlwaysOnPoe=_ArubaWiredPoePethPseModuleAlwaysOnPoe_Object((1,3,6,1,4,1,47196,4,1,1,3,8,4,1,1,3),_ArubaWiredPoePethPseModuleAlwaysOnPoe_Type())
arubaWiredPoePethPseModuleAlwaysOnPoe.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPoePethPseModuleAlwaysOnPoe.setStatus(_A)
pethPsePortEntry.registerAugmentions((_B,_U))
arubaWiredPoePethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethPsePortEntry.registerAugmentions((_B,_V))
arubaWiredPoePethPseFourPairPortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethMainPseEntry.registerAugmentions((_B,_W))
arubaWiredPoePethMainPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
arubaWiredPoePethPsePortTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,8,2,2,1))
arubaWiredPoePethPsePortTableGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:arubaWiredPoePethPsePortTableGroup.setStatus(_A)
arubaWiredPoePethPseFourPairPortTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,8,2,2,2))
arubaWiredPoePethPseFourPairPortTableGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:arubaWiredPoePethPseFourPairPortTableGroup.setStatus(_A)
arubaWiredPoePethMainPseTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,8,2,2,3))
arubaWiredPoePethMainPseTableGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:arubaWiredPoePethMainPseTableGroup.setStatus(_A)
arubaWiredPoePethPseModuleTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,8,2,2,4))
arubaWiredPoePethPseModuleTableGroup.setObjects((_B,_A2))
if mibBuilder.loadTexts:arubaWiredPoePethPseModuleTableGroup.setStatus(_A)
arubaWiredPoeCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,8,2,1,1))
arubaWiredPoeCompliance.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:arubaWiredPoeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'arubaWiredPoeMIB':arubaWiredPoeMIB,'arubaWiredPoePethPsePort':arubaWiredPoePethPsePort,_A3:arubaWiredPoePethPsePortTable,_U:arubaWiredPoePethPsePortEntry,_X:arubaWiredPoePethPsePortPowerAllocateBy,_Y:arubaWiredPoePethPsePortPreStdDetect,_Z:arubaWiredPoePethPsePortRpd,_a:arubaWiredPoePethPsePortCurrent,_b:arubaWiredPoePethPsePortVoltage,_c:arubaWiredPoePethPsePortReservedPower,_d:arubaWiredPoePethPsePortPowerDrawn,_e:arubaWiredPoePethPsePortAveragePower,_f:arubaWiredPoePethPsePortPeakPower,_g:arubaWiredPoePethPsePortOperStatus,_h:arubaWiredPoePethPsePortPdSignature,_i:arubaWiredPoePethPsePortPowerClassification,_j:arubaWiredPoePethPsePortPseAssignedClass,_k:arubaWiredPoePethPsePortPoECycle,'arubaWiredPoePethPseFourPairPortTable':arubaWiredPoePethPseFourPairPortTable,_V:arubaWiredPoePethPseFourPairPortEntry,_l:arubaWiredPoePethPsePortDetectionStatusPairA,_m:arubaWiredPoePethPsePortDetectionStatusPairB,_n:arubaWiredPoePethPsePortPowerClassificationPairA,_o:arubaWiredPoePethPsePortPowerClassificationPairB,_p:arubaWiredPoePethPsePortPseAssignedClassA,_q:arubaWiredPoePethPsePortPseAssignedClassB,_r:arubaWiredPoePethPsePortInvalidSignatureCounterPairA,_s:arubaWiredPoePethPsePortInvalidSignatureCounterPairB,_t:arubaWiredPoePethPsePortPowerDeniedCounterPairA,_u:arubaWiredPoePethPsePortPowerDeniedCounterPairB,_v:arubaWiredPoePethPsePortOverLoadCounterPairA,_w:arubaWiredPoePethPsePortOverLoadCounterPairB,_x:arubaWiredPoePethPsePortMPSAbsentCounterPairA,_y:arubaWiredPoePethPsePortMPSAbsentCounterPairB,'arubaWiredPoeConformance':arubaWiredPoeConformance,'arubaWiredPoeCompliances':arubaWiredPoeCompliances,'arubaWiredPoeCompliance':arubaWiredPoeCompliance,'arubaWiredPoeGroups':arubaWiredPoeGroups,_A6:arubaWiredPoePethPsePortTableGroup,_A7:arubaWiredPoePethPseFourPairPortTableGroup,_A8:arubaWiredPoePethMainPseTableGroup,_A9:arubaWiredPoePethPseModuleTableGroup,'arubaWiredPoePethMainPse':arubaWiredPoePethMainPse,_A4:arubaWiredPoePethMainPseTable,_W:arubaWiredPoePethMainPseEntry,_z:arubaWiredPoePethMainPseReservedPower,_A0:arubaWiredPoePethMainPseFailoverPower,_A1:arubaWiredPoePethMainPseRedundantPower,'arubaWiredPoePethPseModule':arubaWiredPoePethPseModule,_A5:arubaWiredPoePethPseModuleTable,'arubaWiredPoePethPseModuleEntry':arubaWiredPoePethPseModuleEntry,_R:arubaWiredPoePethPseModuleGroupIndex,_S:arubaWiredPoePethPseModuleSlotIndex,_A2:arubaWiredPoePethPseModuleAlwaysOnPoe})