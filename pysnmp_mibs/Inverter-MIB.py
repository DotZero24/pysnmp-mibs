_K='alarmGroupIndex'
_J='miscInfoGroupIndex'
_I='dcGroupIndex'
_H='acGroupIndex'
_G='phaseGroupIndex'
_F='tsiModulesIndex'
_E='DisplayString'
_D='Inverter-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
argus=ModuleIdentity((1,3,6,1,4,1,7309))
_PwrSysInv_ObjectIdentity=ObjectIdentity
pwrSysInv=_PwrSysInv_ObjectIdentity((1,3,6,1,4,1,7309,10))
class _PwrInvCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PwrInvCount_Type.__name__=_B
_PwrInvCount_Object=MibScalar
pwrInvCount=_PwrInvCount_Object((1,3,6,1,4,1,7309,10,1),_PwrInvCount_Type())
pwrInvCount.setMaxAccess(_C)
if mibBuilder.loadTexts:pwrInvCount.setStatus(_A)
_TsiModules_ObjectIdentity=ObjectIdentity
tsiModules=_TsiModules_ObjectIdentity((1,3,6,1,4,1,7309,10,5))
class _TsiModulesCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiModulesCount_Type.__name__=_B
_TsiModulesCount_Object=MibScalar
tsiModulesCount=_TsiModulesCount_Object((1,3,6,1,4,1,7309,10,5,1),_TsiModulesCount_Type())
tsiModulesCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiModulesCount.setStatus(_A)
_TsiModulesTable_Object=MibTable
tsiModulesTable=_TsiModulesTable_Object((1,3,6,1,4,1,7309,10,5,5))
if mibBuilder.loadTexts:tsiModulesTable.setStatus(_A)
_TsiModulesEntry_Object=MibTableRow
tsiModulesEntry=_TsiModulesEntry_Object((1,3,6,1,4,1,7309,10,5,5,1))
tsiModulesEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:tsiModulesEntry.setStatus(_A)
class _TsiModulesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiModulesIndex_Type.__name__=_B
_TsiModulesIndex_Object=MibTableColumn
tsiModulesIndex=_TsiModulesIndex_Object((1,3,6,1,4,1,7309,10,5,5,1,1),_TsiModulesIndex_Type())
tsiModulesIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiModulesIndex.setStatus(_A)
class _TsiStatusACOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiStatusACOut_Type.__name__=_B
_TsiStatusACOut_Object=MibTableColumn
tsiStatusACOut=_TsiStatusACOut_Object((1,3,6,1,4,1,7309,10,5,5,1,2),_TsiStatusACOut_Type())
tsiStatusACOut.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiStatusACOut.setStatus(_A)
class _TsiStatusACIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiStatusACIn_Type.__name__=_B
_TsiStatusACIn_Object=MibTableColumn
tsiStatusACIn=_TsiStatusACIn_Object((1,3,6,1,4,1,7309,10,5,5,1,3),_TsiStatusACIn_Type())
tsiStatusACIn.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiStatusACIn.setStatus(_A)
class _TsiStatusDCIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiStatusDCIn_Type.__name__=_B
_TsiStatusDCIn_Object=MibTableColumn
tsiStatusDCIn=_TsiStatusDCIn_Object((1,3,6,1,4,1,7309,10,5,5,1,4),_TsiStatusDCIn_Type())
tsiStatusDCIn.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiStatusDCIn.setStatus(_A)
class _TsiAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiAddress_Type.__name__=_B
_TsiAddress_Object=MibTableColumn
tsiAddress=_TsiAddress_Object((1,3,6,1,4,1,7309,10,5,5,1,5),_TsiAddress_Type())
tsiAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiAddress.setStatus(_A)
class _TsiLoadPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiLoadPosition_Type.__name__=_B
_TsiLoadPosition_Object=MibTableColumn
tsiLoadPosition=_TsiLoadPosition_Object((1,3,6,1,4,1,7309,10,5,5,1,6),_TsiLoadPosition_Type())
tsiLoadPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiLoadPosition.setStatus(_A)
class _TsiLoadRatioW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiLoadRatioW_Type.__name__=_B
_TsiLoadRatioW_Object=MibTableColumn
tsiLoadRatioW=_TsiLoadRatioW_Object((1,3,6,1,4,1,7309,10,5,5,1,7),_TsiLoadRatioW_Type())
tsiLoadRatioW.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiLoadRatioW.setStatus(_A)
class _TsiLoadRatioVA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiLoadRatioVA_Type.__name__=_B
_TsiLoadRatioVA_Object=MibTableColumn
tsiLoadRatioVA=_TsiLoadRatioVA_Object((1,3,6,1,4,1,7309,10,5,5,1,8),_TsiLoadRatioVA_Type())
tsiLoadRatioVA.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiLoadRatioVA.setStatus(_A)
class _TsiSerialNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_TsiSerialNumber_Type.__name__=_B
_TsiSerialNumber_Object=MibTableColumn
tsiSerialNumber=_TsiSerialNumber_Object((1,3,6,1,4,1,7309,10,5,5,1,9),_TsiSerialNumber_Type())
tsiSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiSerialNumber.setStatus(_A)
class _TsiVout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiVout_Type.__name__=_B
_TsiVout_Object=MibTableColumn
tsiVout=_TsiVout_Object((1,3,6,1,4,1,7309,10,5,5,1,10),_TsiVout_Type())
tsiVout.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiVout.setStatus(_A)
class _TsiIout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiIout_Type.__name__=_B
_TsiIout_Object=MibTableColumn
tsiIout=_TsiIout_Object((1,3,6,1,4,1,7309,10,5,5,1,11),_TsiIout_Type())
tsiIout.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiIout.setStatus(_A)
class _TsiPoutW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiPoutW_Type.__name__=_B
_TsiPoutW_Object=MibTableColumn
tsiPoutW=_TsiPoutW_Object((1,3,6,1,4,1,7309,10,5,5,1,12),_TsiPoutW_Type())
tsiPoutW.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiPoutW.setStatus(_A)
class _TsiPoutVA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiPoutVA_Type.__name__=_B
_TsiPoutVA_Object=MibTableColumn
tsiPoutVA=_TsiPoutVA_Object((1,3,6,1,4,1,7309,10,5,5,1,13),_TsiPoutVA_Type())
tsiPoutVA.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiPoutVA.setStatus(_A)
class _TsiVinAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiVinAC_Type.__name__=_B
_TsiVinAC_Object=MibTableColumn
tsiVinAC=_TsiVinAC_Object((1,3,6,1,4,1,7309,10,5,5,1,14),_TsiVinAC_Type())
tsiVinAC.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiVinAC.setStatus(_A)
class _TsiIinAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiIinAC_Type.__name__=_B
_TsiIinAC_Object=MibTableColumn
tsiIinAC=_TsiIinAC_Object((1,3,6,1,4,1,7309,10,5,5,1,15),_TsiIinAC_Type())
tsiIinAC.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiIinAC.setStatus(_A)
class _TsiPinACW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiPinACW_Type.__name__=_B
_TsiPinACW_Object=MibTableColumn
tsiPinACW=_TsiPinACW_Object((1,3,6,1,4,1,7309,10,5,5,1,16),_TsiPinACW_Type())
tsiPinACW.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiPinACW.setStatus(_A)
class _TsiPinACVA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiPinACVA_Type.__name__=_B
_TsiPinACVA_Object=MibTableColumn
tsiPinACVA=_TsiPinACVA_Object((1,3,6,1,4,1,7309,10,5,5,1,17),_TsiPinACVA_Type())
tsiPinACVA.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiPinACVA.setStatus(_A)
class _TsiACInFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiACInFreq_Type.__name__=_B
_TsiACInFreq_Object=MibTableColumn
tsiACInFreq=_TsiACInFreq_Object((1,3,6,1,4,1,7309,10,5,5,1,18),_TsiACInFreq_Type())
tsiACInFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiACInFreq.setStatus(_A)
class _TsiVinDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiVinDC_Type.__name__=_B
_TsiVinDC_Object=MibTableColumn
tsiVinDC=_TsiVinDC_Object((1,3,6,1,4,1,7309,10,5,5,1,19),_TsiVinDC_Type())
tsiVinDC.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiVinDC.setStatus(_A)
class _TsiIinDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiIinDC_Type.__name__=_B
_TsiIinDC_Object=MibTableColumn
tsiIinDC=_TsiIinDC_Object((1,3,6,1,4,1,7309,10,5,5,1,20),_TsiIinDC_Type())
tsiIinDC.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiIinDC.setStatus(_A)
class _TsiPinDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiPinDC_Type.__name__=_B
_TsiPinDC_Object=MibTableColumn
tsiPinDC=_TsiPinDC_Object((1,3,6,1,4,1,7309,10,5,5,1,21),_TsiPinDC_Type())
tsiPinDC.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiPinDC.setStatus(_A)
class _TsiTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiTemperature_Type.__name__=_B
_TsiTemperature_Object=MibTableColumn
tsiTemperature=_TsiTemperature_Object((1,3,6,1,4,1,7309,10,5,5,1,22),_TsiTemperature_Type())
tsiTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiTemperature.setStatus(_A)
class _TsiSoftVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiSoftVersion_Type.__name__=_B
_TsiSoftVersion_Object=MibTableColumn
tsiSoftVersion=_TsiSoftVersion_Object((1,3,6,1,4,1,7309,10,5,5,1,23),_TsiSoftVersion_Type())
tsiSoftVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiSoftVersion.setStatus(_A)
class _TsiBusErrorCnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_TsiBusErrorCnt_Type.__name__=_B
_TsiBusErrorCnt_Object=MibTableColumn
tsiBusErrorCnt=_TsiBusErrorCnt_Object((1,3,6,1,4,1,7309,10,5,5,1,24),_TsiBusErrorCnt_Type())
tsiBusErrorCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiBusErrorCnt.setStatus(_A)
class _TsiPhaseNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiPhaseNumber_Type.__name__=_B
_TsiPhaseNumber_Object=MibTableColumn
tsiPhaseNumber=_TsiPhaseNumber_Object((1,3,6,1,4,1,7309,10,5,5,1,25),_TsiPhaseNumber_Type())
tsiPhaseNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiPhaseNumber.setStatus(_A)
class _TsiStatusMod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiStatusMod_Type.__name__=_B
_TsiStatusMod_Object=MibTableColumn
tsiStatusMod=_TsiStatusMod_Object((1,3,6,1,4,1,7309,10,5,5,1,26),_TsiStatusMod_Type())
tsiStatusMod.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiStatusMod.setStatus(_A)
class _TsiStatusAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiStatusAC_Type.__name__=_B
_TsiStatusAC_Object=MibTableColumn
tsiStatusAC=_TsiStatusAC_Object((1,3,6,1,4,1,7309,10,5,5,1,27),_TsiStatusAC_Type())
tsiStatusAC.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiStatusAC.setStatus(_A)
class _TsiStatusDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiStatusDC_Type.__name__=_B
_TsiStatusDC_Object=MibTableColumn
tsiStatusDC=_TsiStatusDC_Object((1,3,6,1,4,1,7309,10,5,5,1,28),_TsiStatusDC_Type())
tsiStatusDC.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiStatusDC.setStatus(_A)
class _TsiPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiPresent_Type.__name__=_B
_TsiPresent_Object=MibTableColumn
tsiPresent=_TsiPresent_Object((1,3,6,1,4,1,7309,10,5,5,1,29),_TsiPresent_Type())
tsiPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiPresent.setStatus(_A)
class _TsiGroupAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiGroupAC_Type.__name__=_B
_TsiGroupAC_Object=MibTableColumn
tsiGroupAC=_TsiGroupAC_Object((1,3,6,1,4,1,7309,10,5,5,1,30),_TsiGroupAC_Type())
tsiGroupAC.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiGroupAC.setStatus(_A)
class _TsiGroupDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiGroupDC_Type.__name__=_B
_TsiGroupDC_Object=MibTableColumn
tsiGroupDC=_TsiGroupDC_Object((1,3,6,1,4,1,7309,10,5,5,1,31),_TsiGroupDC_Type())
tsiGroupDC.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiGroupDC.setStatus(_A)
class _TsiRestrained_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiRestrained_Type.__name__=_B
_TsiRestrained_Object=MibTableColumn
tsiRestrained=_TsiRestrained_Object((1,3,6,1,4,1,7309,10,5,5,1,32),_TsiRestrained_Type())
tsiRestrained.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiRestrained.setStatus(_A)
class _TsiNoEPC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TsiNoEPC_Type.__name__=_B
_TsiNoEPC_Object=MibTableColumn
tsiNoEPC=_TsiNoEPC_Object((1,3,6,1,4,1,7309,10,5,5,1,33),_TsiNoEPC_Type())
tsiNoEPC.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiNoEPC.setStatus(_A)
class _TsiPoutNominalW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiPoutNominalW_Type.__name__=_B
_TsiPoutNominalW_Object=MibTableColumn
tsiPoutNominalW=_TsiPoutNominalW_Object((1,3,6,1,4,1,7309,10,5,5,1,34),_TsiPoutNominalW_Type())
tsiPoutNominalW.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiPoutNominalW.setStatus(_A)
class _TsiPoutNominalVA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiPoutNominalVA_Type.__name__=_B
_TsiPoutNominalVA_Object=MibTableColumn
tsiPoutNominalVA=_TsiPoutNominalVA_Object((1,3,6,1,4,1,7309,10,5,5,1,35),_TsiPoutNominalVA_Type())
tsiPoutNominalVA.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiPoutNominalVA.setStatus(_A)
class _TsiVinNominalAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiVinNominalAC_Type.__name__=_B
_TsiVinNominalAC_Object=MibTableColumn
tsiVinNominalAC=_TsiVinNominalAC_Object((1,3,6,1,4,1,7309,10,5,5,1,36),_TsiVinNominalAC_Type())
tsiVinNominalAC.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiVinNominalAC.setStatus(_A)
class _TsiVinNominalDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiVinNominalDC_Type.__name__=_B
_TsiVinNominalDC_Object=MibTableColumn
tsiVinNominalDC=_TsiVinNominalDC_Object((1,3,6,1,4,1,7309,10,5,5,1,37),_TsiVinNominalDC_Type())
tsiVinNominalDC.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiVinNominalDC.setStatus(_A)
class _TsiVinNominalFreqAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TsiVinNominalFreqAC_Type.__name__=_B
_TsiVinNominalFreqAC_Object=MibTableColumn
tsiVinNominalFreqAC=_TsiVinNominalFreqAC_Object((1,3,6,1,4,1,7309,10,5,5,1,38),_TsiVinNominalFreqAC_Type())
tsiVinNominalFreqAC.setMaxAccess(_C)
if mibBuilder.loadTexts:tsiVinNominalFreqAC.setStatus(_A)
_PhaseGroup_ObjectIdentity=ObjectIdentity
phaseGroup=_PhaseGroup_ObjectIdentity((1,3,6,1,4,1,7309,10,6))
class _PhaseCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhaseCount_Type.__name__=_B
_PhaseCount_Object=MibScalar
phaseCount=_PhaseCount_Object((1,3,6,1,4,1,7309,10,6,1),_PhaseCount_Type())
phaseCount.setMaxAccess(_C)
if mibBuilder.loadTexts:phaseCount.setStatus(_A)
_PhaseGroupTable_Object=MibTable
phaseGroupTable=_PhaseGroupTable_Object((1,3,6,1,4,1,7309,10,6,5))
if mibBuilder.loadTexts:phaseGroupTable.setStatus(_A)
_PhaseGroupEntry_Object=MibTableRow
phaseGroupEntry=_PhaseGroupEntry_Object((1,3,6,1,4,1,7309,10,6,5,1))
phaseGroupEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:phaseGroupEntry.setStatus(_A)
class _PhaseGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhaseGroupIndex_Type.__name__=_B
_PhaseGroupIndex_Object=MibTableColumn
phaseGroupIndex=_PhaseGroupIndex_Object((1,3,6,1,4,1,7309,10,6,5,1,1),_PhaseGroupIndex_Type())
phaseGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:phaseGroupIndex.setStatus(_A)
class _BRatioAvailableW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BRatioAvailableW_Type.__name__=_B
_BRatioAvailableW_Object=MibTableColumn
bRatioAvailableW=_BRatioAvailableW_Object((1,3,6,1,4,1,7309,10,6,5,1,2),_BRatioAvailableW_Type())
bRatioAvailableW.setMaxAccess(_C)
if mibBuilder.loadTexts:bRatioAvailableW.setStatus(_A)
class _BRatioAvailableVA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BRatioAvailableVA_Type.__name__=_B
_BRatioAvailableVA_Object=MibTableColumn
bRatioAvailableVA=_BRatioAvailableVA_Object((1,3,6,1,4,1,7309,10,6,5,1,3),_BRatioAvailableVA_Type())
bRatioAvailableVA.setMaxAccess(_C)
if mibBuilder.loadTexts:bRatioAvailableVA.setStatus(_A)
class _BRatioInstalledW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BRatioInstalledW_Type.__name__=_B
_BRatioInstalledW_Object=MibTableColumn
bRatioInstalledW=_BRatioInstalledW_Object((1,3,6,1,4,1,7309,10,6,5,1,4),_BRatioInstalledW_Type())
bRatioInstalledW.setMaxAccess(_C)
if mibBuilder.loadTexts:bRatioInstalledW.setStatus(_A)
class _BRatioInstalledWA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BRatioInstalledWA_Type.__name__=_B
_BRatioInstalledWA_Object=MibTableColumn
bRatioInstalledWA=_BRatioInstalledWA_Object((1,3,6,1,4,1,7309,10,6,5,1,5),_BRatioInstalledWA_Type())
bRatioInstalledWA.setMaxAccess(_C)
if mibBuilder.loadTexts:bRatioInstalledWA.setStatus(_A)
class _WVout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WVout_Type.__name__=_B
_WVout_Object=MibTableColumn
wVout=_WVout_Object((1,3,6,1,4,1,7309,10,6,5,1,6),_WVout_Type())
wVout.setMaxAccess(_C)
if mibBuilder.loadTexts:wVout.setStatus(_A)
class _WIout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WIout_Type.__name__=_B
_WIout_Object=MibTableColumn
wIout=_WIout_Object((1,3,6,1,4,1,7309,10,6,5,1,7),_WIout_Type())
wIout.setMaxAccess(_C)
if mibBuilder.loadTexts:wIout.setStatus(_A)
class _BNbOndCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BNbOndCfg_Type.__name__=_B
_BNbOndCfg_Object=MibTableColumn
bNbOndCfg=_BNbOndCfg_Object((1,3,6,1,4,1,7309,10,6,5,1,8),_BNbOndCfg_Type())
bNbOndCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:bNbOndCfg.setStatus(_A)
class _BRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BRedundancy_Type.__name__=_B
_BRedundancy_Object=MibTableColumn
bRedundancy=_BRedundancy_Object((1,3,6,1,4,1,7309,10,6,5,1,9),_BRedundancy_Type())
bRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:bRedundancy.setStatus(_A)
class _WACOutFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WACOutFreq_Type.__name__=_B
_WACOutFreq_Object=MibTableColumn
wACOutFreq=_WACOutFreq_Object((1,3,6,1,4,1,7309,10,6,5,1,10),_WACOutFreq_Type())
wACOutFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:wACOutFreq.setStatus(_A)
class _LPinDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_LPinDC_Type.__name__=_B
_LPinDC_Object=MibTableColumn
lPinDC=_LPinDC_Object((1,3,6,1,4,1,7309,10,6,5,1,11),_LPinDC_Type())
lPinDC.setMaxAccess(_C)
if mibBuilder.loadTexts:lPinDC.setStatus(_A)
class _LPinACW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_LPinACW_Type.__name__=_B
_LPinACW_Object=MibTableColumn
lPinACW=_LPinACW_Object((1,3,6,1,4,1,7309,10,6,5,1,12),_LPinACW_Type())
lPinACW.setMaxAccess(_C)
if mibBuilder.loadTexts:lPinACW.setStatus(_A)
class _LPinACVA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_LPinACVA_Type.__name__=_B
_LPinACVA_Object=MibTableColumn
lPinACVA=_LPinACVA_Object((1,3,6,1,4,1,7309,10,6,5,1,13),_LPinACVA_Type())
lPinACVA.setMaxAccess(_C)
if mibBuilder.loadTexts:lPinACVA.setStatus(_A)
class _LCurrentPowerInW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_LCurrentPowerInW_Type.__name__=_B
_LCurrentPowerInW_Object=MibTableColumn
lCurrentPowerInW=_LCurrentPowerInW_Object((1,3,6,1,4,1,7309,10,6,5,1,14),_LCurrentPowerInW_Type())
lCurrentPowerInW.setMaxAccess(_C)
if mibBuilder.loadTexts:lCurrentPowerInW.setStatus(_A)
class _LCurrentPowerInVA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_LCurrentPowerInVA_Type.__name__=_B
_LCurrentPowerInVA_Object=MibTableColumn
lCurrentPowerInVA=_LCurrentPowerInVA_Object((1,3,6,1,4,1,7309,10,6,5,1,15),_LCurrentPowerInVA_Type())
lCurrentPowerInVA.setMaxAccess(_C)
if mibBuilder.loadTexts:lCurrentPowerInVA.setStatus(_A)
class _LInstalledPowerInW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_LInstalledPowerInW_Type.__name__=_B
_LInstalledPowerInW_Object=MibTableColumn
lInstalledPowerInW=_LInstalledPowerInW_Object((1,3,6,1,4,1,7309,10,6,5,1,16),_LInstalledPowerInW_Type())
lInstalledPowerInW.setMaxAccess(_C)
if mibBuilder.loadTexts:lInstalledPowerInW.setStatus(_A)
class _LInstalledPowerInVA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_LInstalledPowerInVA_Type.__name__=_B
_LInstalledPowerInVA_Object=MibTableColumn
lInstalledPowerInVA=_LInstalledPowerInVA_Object((1,3,6,1,4,1,7309,10,6,5,1,17),_LInstalledPowerInVA_Type())
lInstalledPowerInVA.setMaxAccess(_C)
if mibBuilder.loadTexts:lInstalledPowerInVA.setStatus(_A)
class _LAvailablePowerInW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_LAvailablePowerInW_Type.__name__=_B
_LAvailablePowerInW_Object=MibTableColumn
lAvailablePowerInW=_LAvailablePowerInW_Object((1,3,6,1,4,1,7309,10,6,5,1,18),_LAvailablePowerInW_Type())
lAvailablePowerInW.setMaxAccess(_C)
if mibBuilder.loadTexts:lAvailablePowerInW.setStatus(_A)
class _LAvailablePowerInVA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_LAvailablePowerInVA_Type.__name__=_B
_LAvailablePowerInVA_Object=MibTableColumn
lAvailablePowerInVA=_LAvailablePowerInVA_Object((1,3,6,1,4,1,7309,10,6,5,1,19),_LAvailablePowerInVA_Type())
lAvailablePowerInVA.setMaxAccess(_C)
if mibBuilder.loadTexts:lAvailablePowerInVA.setStatus(_A)
class _BNbInvSeen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BNbInvSeen_Type.__name__=_B
_BNbInvSeen_Object=MibTableColumn
bNbInvSeen=_BNbInvSeen_Object((1,3,6,1,4,1,7309,10,6,5,1,20),_BNbInvSeen_Type())
bNbInvSeen.setMaxAccess(_C)
if mibBuilder.loadTexts:bNbInvSeen.setStatus(_A)
class _BNbInvOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BNbInvOK_Type.__name__=_B
_BNbInvOK_Object=MibTableColumn
bNbInvOK=_BNbInvOK_Object((1,3,6,1,4,1,7309,10,6,5,1,21),_BNbInvOK_Type())
bNbInvOK.setMaxAccess(_C)
if mibBuilder.loadTexts:bNbInvOK.setStatus(_A)
class _BNbInvMO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BNbInvMO_Type.__name__=_B
_BNbInvMO_Object=MibTableColumn
bNbInvMO=_BNbInvMO_Object((1,3,6,1,4,1,7309,10,6,5,1,22),_BNbInvMO_Type())
bNbInvMO.setMaxAccess(_C)
if mibBuilder.loadTexts:bNbInvMO.setStatus(_A)
class _BNbInvKO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BNbInvKO_Type.__name__=_B
_BNbInvKO_Object=MibTableColumn
bNbInvKO=_BNbInvKO_Object((1,3,6,1,4,1,7309,10,6,5,1,23),_BNbInvKO_Type())
bNbInvKO.setMaxAccess(_C)
if mibBuilder.loadTexts:bNbInvKO.setStatus(_A)
class _BNbInvNT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BNbInvNT_Type.__name__=_B
_BNbInvNT_Object=MibTableColumn
bNbInvNT=_BNbInvNT_Object((1,3,6,1,4,1,7309,10,6,5,1,24),_BNbInvNT_Type())
bNbInvNT.setMaxAccess(_C)
if mibBuilder.loadTexts:bNbInvNT.setStatus(_A)
_AcGroup_ObjectIdentity=ObjectIdentity
acGroup=_AcGroup_ObjectIdentity((1,3,6,1,4,1,7309,10,7))
class _AcGroupCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcGroupCount_Type.__name__=_B
_AcGroupCount_Object=MibScalar
acGroupCount=_AcGroupCount_Object((1,3,6,1,4,1,7309,10,7,1),_AcGroupCount_Type())
acGroupCount.setMaxAccess(_C)
if mibBuilder.loadTexts:acGroupCount.setStatus(_A)
_AcGroupTable_Object=MibTable
acGroupTable=_AcGroupTable_Object((1,3,6,1,4,1,7309,10,7,5))
if mibBuilder.loadTexts:acGroupTable.setStatus(_A)
_AcGroupEntry_Object=MibTableRow
acGroupEntry=_AcGroupEntry_Object((1,3,6,1,4,1,7309,10,7,5,1))
acGroupEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:acGroupEntry.setStatus(_A)
class _AcGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcGroupIndex_Type.__name__=_B
_AcGroupIndex_Object=MibTableColumn
acGroupIndex=_AcGroupIndex_Object((1,3,6,1,4,1,7309,10,7,5,1,1),_AcGroupIndex_Type())
acGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:acGroupIndex.setStatus(_A)
class _AcNbInvOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcNbInvOK_Type.__name__=_B
_AcNbInvOK_Object=MibTableColumn
acNbInvOK=_AcNbInvOK_Object((1,3,6,1,4,1,7309,10,7,5,1,2),_AcNbInvOK_Type())
acNbInvOK.setMaxAccess(_C)
if mibBuilder.loadTexts:acNbInvOK.setStatus(_A)
class _AcNbInvMO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcNbInvMO_Type.__name__=_B
_AcNbInvMO_Object=MibTableColumn
acNbInvMO=_AcNbInvMO_Object((1,3,6,1,4,1,7309,10,7,5,1,3),_AcNbInvMO_Type())
acNbInvMO.setMaxAccess(_C)
if mibBuilder.loadTexts:acNbInvMO.setStatus(_A)
class _AcNbInvKO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcNbInvKO_Type.__name__=_B
_AcNbInvKO_Object=MibTableColumn
acNbInvKO=_AcNbInvKO_Object((1,3,6,1,4,1,7309,10,7,5,1,4),_AcNbInvKO_Type())
acNbInvKO.setMaxAccess(_C)
if mibBuilder.loadTexts:acNbInvKO.setStatus(_A)
class _AcNbInvSeen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcNbInvSeen_Type.__name__=_B
_AcNbInvSeen_Object=MibTableColumn
acNbInvSeen=_AcNbInvSeen_Object((1,3,6,1,4,1,7309,10,7,5,1,5),_AcNbInvSeen_Type())
acNbInvSeen.setMaxAccess(_C)
if mibBuilder.loadTexts:acNbInvSeen.setStatus(_A)
class _AcPinACW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AcPinACW_Type.__name__=_B
_AcPinACW_Object=MibTableColumn
acPinACW=_AcPinACW_Object((1,3,6,1,4,1,7309,10,7,5,1,6),_AcPinACW_Type())
acPinACW.setMaxAccess(_C)
if mibBuilder.loadTexts:acPinACW.setStatus(_A)
class _AcPinACVA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AcPinACVA_Type.__name__=_B
_AcPinACVA_Object=MibTableColumn
acPinACVA=_AcPinACVA_Object((1,3,6,1,4,1,7309,10,7,5,1,7),_AcPinACVA_Type())
acPinACVA.setMaxAccess(_C)
if mibBuilder.loadTexts:acPinACVA.setStatus(_A)
class _AcVinAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcVinAC_Type.__name__=_B
_AcVinAC_Object=MibTableColumn
acVinAC=_AcVinAC_Object((1,3,6,1,4,1,7309,10,7,5,1,8),_AcVinAC_Type())
acVinAC.setMaxAccess(_C)
if mibBuilder.loadTexts:acVinAC.setStatus(_A)
class _AcIinAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcIinAC_Type.__name__=_B
_AcIinAC_Object=MibTableColumn
acIinAC=_AcIinAC_Object((1,3,6,1,4,1,7309,10,7,5,1,9),_AcIinAC_Type())
acIinAC.setMaxAccess(_C)
if mibBuilder.loadTexts:acIinAC.setStatus(_A)
class _AcACinFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcACinFreq_Type.__name__=_B
_AcACinFreq_Object=MibTableColumn
acACinFreq=_AcACinFreq_Object((1,3,6,1,4,1,7309,10,7,5,1,10),_AcACinFreq_Type())
acACinFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:acACinFreq.setStatus(_A)
class _AcACinOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcACinOK_Type.__name__=_B
_AcACinOK_Object=MibTableColumn
acACinOK=_AcACinOK_Object((1,3,6,1,4,1,7309,10,7,5,1,11),_AcACinOK_Type())
acACinOK.setMaxAccess(_C)
if mibBuilder.loadTexts:acACinOK.setStatus(_A)
_DcGroup_ObjectIdentity=ObjectIdentity
dcGroup=_DcGroup_ObjectIdentity((1,3,6,1,4,1,7309,10,8))
class _DcGroupCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DcGroupCount_Type.__name__=_B
_DcGroupCount_Object=MibScalar
dcGroupCount=_DcGroupCount_Object((1,3,6,1,4,1,7309,10,8,1),_DcGroupCount_Type())
dcGroupCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dcGroupCount.setStatus(_A)
_DcGroupTable_Object=MibTable
dcGroupTable=_DcGroupTable_Object((1,3,6,1,4,1,7309,10,8,5))
if mibBuilder.loadTexts:dcGroupTable.setStatus(_A)
_DcGroupEntry_Object=MibTableRow
dcGroupEntry=_DcGroupEntry_Object((1,3,6,1,4,1,7309,10,8,5,1))
dcGroupEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:dcGroupEntry.setStatus(_A)
class _DcGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DcGroupIndex_Type.__name__=_B
_DcGroupIndex_Object=MibTableColumn
dcGroupIndex=_DcGroupIndex_Object((1,3,6,1,4,1,7309,10,8,5,1,1),_DcGroupIndex_Type())
dcGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dcGroupIndex.setStatus(_A)
class _DcNbInvOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DcNbInvOK_Type.__name__=_B
_DcNbInvOK_Object=MibTableColumn
dcNbInvOK=_DcNbInvOK_Object((1,3,6,1,4,1,7309,10,8,5,1,2),_DcNbInvOK_Type())
dcNbInvOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dcNbInvOK.setStatus(_A)
class _DcNbInvMO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DcNbInvMO_Type.__name__=_B
_DcNbInvMO_Object=MibTableColumn
dcNbInvMO=_DcNbInvMO_Object((1,3,6,1,4,1,7309,10,8,5,1,3),_DcNbInvMO_Type())
dcNbInvMO.setMaxAccess(_C)
if mibBuilder.loadTexts:dcNbInvMO.setStatus(_A)
class _DcNbInvKO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DcNbInvKO_Type.__name__=_B
_DcNbInvKO_Object=MibTableColumn
dcNbInvKO=_DcNbInvKO_Object((1,3,6,1,4,1,7309,10,8,5,1,4),_DcNbInvKO_Type())
dcNbInvKO.setMaxAccess(_C)
if mibBuilder.loadTexts:dcNbInvKO.setStatus(_A)
class _DcNbInvSeen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DcNbInvSeen_Type.__name__=_B
_DcNbInvSeen_Object=MibTableColumn
dcNbInvSeen=_DcNbInvSeen_Object((1,3,6,1,4,1,7309,10,8,5,1,5),_DcNbInvSeen_Type())
dcNbInvSeen.setMaxAccess(_C)
if mibBuilder.loadTexts:dcNbInvSeen.setStatus(_A)
class _DcPinDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_DcPinDC_Type.__name__=_B
_DcPinDC_Object=MibTableColumn
dcPinDC=_DcPinDC_Object((1,3,6,1,4,1,7309,10,8,5,1,6),_DcPinDC_Type())
dcPinDC.setMaxAccess(_C)
if mibBuilder.loadTexts:dcPinDC.setStatus(_A)
class _DcVinDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcVinDC_Type.__name__=_B
_DcVinDC_Object=MibTableColumn
dcVinDC=_DcVinDC_Object((1,3,6,1,4,1,7309,10,8,5,1,7),_DcVinDC_Type())
dcVinDC.setMaxAccess(_C)
if mibBuilder.loadTexts:dcVinDC.setStatus(_A)
class _DcIinDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcIinDC_Type.__name__=_B
_DcIinDC_Object=MibTableColumn
dcIinDC=_DcIinDC_Object((1,3,6,1,4,1,7309,10,8,5,1,8),_DcIinDC_Type())
dcIinDC.setMaxAccess(_C)
if mibBuilder.loadTexts:dcIinDC.setStatus(_A)
class _DcDCInOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DcDCInOK_Type.__name__=_B
_DcDCInOK_Object=MibTableColumn
dcDCInOK=_DcDCInOK_Object((1,3,6,1,4,1,7309,10,8,5,1,9),_DcDCInOK_Type())
dcDCInOK.setMaxAccess(_C)
if mibBuilder.loadTexts:dcDCInOK.setStatus(_A)
_MiscInfoGroup_ObjectIdentity=ObjectIdentity
miscInfoGroup=_MiscInfoGroup_ObjectIdentity((1,3,6,1,4,1,7309,10,9))
class _MiscInfoGroupCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MiscInfoGroupCount_Type.__name__=_B
_MiscInfoGroupCount_Object=MibScalar
miscInfoGroupCount=_MiscInfoGroupCount_Object((1,3,6,1,4,1,7309,10,9,1),_MiscInfoGroupCount_Type())
miscInfoGroupCount.setMaxAccess(_C)
if mibBuilder.loadTexts:miscInfoGroupCount.setStatus(_A)
_MiscInfoGroupTable_Object=MibTable
miscInfoGroupTable=_MiscInfoGroupTable_Object((1,3,6,1,4,1,7309,10,9,5))
if mibBuilder.loadTexts:miscInfoGroupTable.setStatus(_A)
_MiscInfoGroupEntry_Object=MibTableRow
miscInfoGroupEntry=_MiscInfoGroupEntry_Object((1,3,6,1,4,1,7309,10,9,5,1))
miscInfoGroupEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:miscInfoGroupEntry.setStatus(_A)
class _MiscInfoGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MiscInfoGroupIndex_Type.__name__=_B
_MiscInfoGroupIndex_Object=MibTableColumn
miscInfoGroupIndex=_MiscInfoGroupIndex_Object((1,3,6,1,4,1,7309,10,9,5,1,1),_MiscInfoGroupIndex_Type())
miscInfoGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:miscInfoGroupIndex.setStatus(_A)
class _BOldVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BOldVersionNumber_Type.__name__=_B
_BOldVersionNumber_Object=MibTableColumn
bOldVersionNumber=_BOldVersionNumber_Object((1,3,6,1,4,1,7309,10,9,5,1,2),_BOldVersionNumber_Type())
bOldVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:bOldVersionNumber.setStatus(_A)
class _EPhaseNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EPhaseNumber_Type.__name__=_B
_EPhaseNumber_Object=MibTableColumn
ePhaseNumber=_EPhaseNumber_Object((1,3,6,1,4,1,7309,10,9,5,1,3),_EPhaseNumber_Type())
ePhaseNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ePhaseNumber.setStatus(_A)
class _BNbMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BNbMajor_Type.__name__=_B
_BNbMajor_Object=MibTableColumn
bNbMajor=_BNbMajor_Object((1,3,6,1,4,1,7309,10,9,5,1,4),_BNbMajor_Type())
bNbMajor.setMaxAccess(_C)
if mibBuilder.loadTexts:bNbMajor.setStatus(_A)
class _WTempoMajorAl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WTempoMajorAl_Type.__name__=_B
_WTempoMajorAl_Object=MibTableColumn
wTempoMajorAl=_WTempoMajorAl_Object((1,3,6,1,4,1,7309,10,9,5,1,5),_WTempoMajorAl_Type())
wTempoMajorAl.setMaxAccess(_C)
if mibBuilder.loadTexts:wTempoMajorAl.setStatus(_A)
class _WtempoMinorAl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtempoMinorAl_Type.__name__=_B
_WtempoMinorAl_Object=MibTableColumn
wtempoMinorAl=_WtempoMinorAl_Object((1,3,6,1,4,1,7309,10,9,5,1,6),_WtempoMinorAl_Type())
wtempoMinorAl.setMaxAccess(_C)
if mibBuilder.loadTexts:wtempoMinorAl.setStatus(_A)
class _LSerialNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_LSerialNumber_Type.__name__=_B
_LSerialNumber_Object=MibTableColumn
lSerialNumber=_LSerialNumber_Object((1,3,6,1,4,1,7309,10,9,5,1,7),_LSerialNumber_Type())
lSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:lSerialNumber.setStatus(_A)
class _BNbMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BNbMinor_Type.__name__=_B
_BNbMinor_Object=MibTableColumn
bNbMinor=_BNbMinor_Object((1,3,6,1,4,1,7309,10,9,5,1,8),_BNbMinor_Type())
bNbMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:bNbMinor.setStatus(_A)
class _BNbTotalAlarmNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BNbTotalAlarmNumber_Type.__name__=_B
_BNbTotalAlarmNumber_Object=MibTableColumn
bNbTotalAlarmNumber=_BNbTotalAlarmNumber_Object((1,3,6,1,4,1,7309,10,9,5,1,9),_BNbTotalAlarmNumber_Type())
bNbTotalAlarmNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:bNbTotalAlarmNumber.setStatus(_A)
class _BACInputPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BACInputPresent_Type.__name__=_B
_BACInputPresent_Object=MibTableColumn
bACInputPresent=_BACInputPresent_Object((1,3,6,1,4,1,7309,10,9,5,1,10),_BACInputPresent_Type())
bACInputPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:bACInputPresent.setStatus(_A)
class _BSaturationThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BSaturationThresh_Type.__name__=_B
_BSaturationThresh_Object=MibTableColumn
bSaturationThresh=_BSaturationThresh_Object((1,3,6,1,4,1,7309,10,9,5,1,11),_BSaturationThresh_Type())
bSaturationThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:bSaturationThresh.setStatus(_A)
class _BNbGroupsDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BNbGroupsDC_Type.__name__=_B
_BNbGroupsDC_Object=MibTableColumn
bNbGroupsDC=_BNbGroupsDC_Object((1,3,6,1,4,1,7309,10,9,5,1,12),_BNbGroupsDC_Type())
bNbGroupsDC.setMaxAccess(_C)
if mibBuilder.loadTexts:bNbGroupsDC.setStatus(_A)
class _BNbGroupsAC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BNbGroupsAC_Type.__name__=_B
_BNbGroupsAC_Object=MibTableColumn
bNbGroupsAC=_BNbGroupsAC_Object((1,3,6,1,4,1,7309,10,9,5,1,13),_BNbGroupsAC_Type())
bNbGroupsAC.setMaxAccess(_C)
if mibBuilder.loadTexts:bNbGroupsAC.setStatus(_A)
class _BProgRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BProgRelay_Type.__name__=_B
_BProgRelay_Object=MibTableColumn
bProgRelay=_BProgRelay_Object((1,3,6,1,4,1,7309,10,9,5,1,14),_BProgRelay_Type())
bProgRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:bProgRelay.setStatus(_A)
class _BSystemLoadPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BSystemLoadPosition_Type.__name__=_B
_BSystemLoadPosition_Object=MibTableColumn
bSystemLoadPosition=_BSystemLoadPosition_Object((1,3,6,1,4,1,7309,10,9,5,1,15),_BSystemLoadPosition_Type())
bSystemLoadPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:bSystemLoadPosition.setStatus(_A)
class _WSoftSubRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WSoftSubRevision_Type.__name__=_B
_WSoftSubRevision_Object=MibTableColumn
wSoftSubRevision=_WSoftSubRevision_Object((1,3,6,1,4,1,7309,10,9,5,1,16),_WSoftSubRevision_Type())
wSoftSubRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:wSoftSubRevision.setStatus(_A)
class _WSoftMainRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WSoftMainRevision_Type.__name__=_B
_WSoftMainRevision_Object=MibTableColumn
wSoftMainRevision=_WSoftMainRevision_Object((1,3,6,1,4,1,7309,10,9,5,1,17),_WSoftMainRevision_Type())
wSoftMainRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:wSoftMainRevision.setStatus(_A)
class _WInvVersionTextError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WInvVersionTextError_Type.__name__=_B
_WInvVersionTextError_Object=MibTableColumn
wInvVersionTextError=_WInvVersionTextError_Object((1,3,6,1,4,1,7309,10,9,5,1,18),_WInvVersionTextError_Type())
wInvVersionTextError.setMaxAccess(_C)
if mibBuilder.loadTexts:wInvVersionTextError.setStatus(_A)
class _BInvMaxKnowParameters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BInvMaxKnowParameters_Type.__name__=_B
_BInvMaxKnowParameters_Object=MibTableColumn
bInvMaxKnowParameters=_BInvMaxKnowParameters_Object((1,3,6,1,4,1,7309,10,9,5,1,19),_BInvMaxKnowParameters_Type())
bInvMaxKnowParameters.setMaxAccess(_C)
if mibBuilder.loadTexts:bInvMaxKnowParameters.setStatus(_A)
_AlarmGroup_ObjectIdentity=ObjectIdentity
alarmGroup=_AlarmGroup_ObjectIdentity((1,3,6,1,4,1,7309,10,10))
class _AlarmGroupCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlarmGroupCount_Type.__name__=_B
_AlarmGroupCount_Object=MibScalar
alarmGroupCount=_AlarmGroupCount_Object((1,3,6,1,4,1,7309,10,10,1),_AlarmGroupCount_Type())
alarmGroupCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmGroupCount.setStatus(_A)
_AlarmGroupTable_Object=MibTable
alarmGroupTable=_AlarmGroupTable_Object((1,3,6,1,4,1,7309,10,10,5))
if mibBuilder.loadTexts:alarmGroupTable.setStatus(_A)
_AlarmGroupEntry_Object=MibTableRow
alarmGroupEntry=_AlarmGroupEntry_Object((1,3,6,1,4,1,7309,10,10,5,1))
alarmGroupEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:alarmGroupEntry.setStatus(_A)
class _AlarmGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlarmGroupIndex_Type.__name__=_B
_AlarmGroupIndex_Object=MibTableColumn
alarmGroupIndex=_AlarmGroupIndex_Object((1,3,6,1,4,1,7309,10,10,5,1,1),_AlarmGroupIndex_Type())
alarmGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmGroupIndex.setStatus(_A)
class _BDeviceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BDeviceNumber_Type.__name__=_B
_BDeviceNumber_Object=MibTableColumn
bDeviceNumber=_BDeviceNumber_Object((1,3,6,1,4,1,7309,10,10,5,1,2),_BDeviceNumber_Type())
bDeviceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:bDeviceNumber.setStatus(_A)
class _BEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BEventType_Type.__name__=_B
_BEventType_Object=MibTableColumn
bEventType=_BEventType_Object((1,3,6,1,4,1,7309,10,10,5,1,3),_BEventType_Type())
bEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:bEventType.setStatus(_A)
class _WEventNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WEventNumber_Type.__name__=_B
_WEventNumber_Object=MibTableColumn
wEventNumber=_WEventNumber_Object((1,3,6,1,4,1,7309,10,10,5,1,4),_WEventNumber_Type())
wEventNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:wEventNumber.setStatus(_A)
class _SEventString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SEventString_Type.__name__=_E
_SEventString_Object=MibTableColumn
sEventString=_SEventString_Object((1,3,6,1,4,1,7309,10,10,5,1,5),_SEventString_Type())
sEventString.setMaxAccess(_C)
if mibBuilder.loadTexts:sEventString.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'argus':argus,'pwrSysInv':pwrSysInv,'pwrInvCount':pwrInvCount,'tsiModules':tsiModules,'tsiModulesCount':tsiModulesCount,'tsiModulesTable':tsiModulesTable,'tsiModulesEntry':tsiModulesEntry,_F:tsiModulesIndex,'tsiStatusACOut':tsiStatusACOut,'tsiStatusACIn':tsiStatusACIn,'tsiStatusDCIn':tsiStatusDCIn,'tsiAddress':tsiAddress,'tsiLoadPosition':tsiLoadPosition,'tsiLoadRatioW':tsiLoadRatioW,'tsiLoadRatioVA':tsiLoadRatioVA,'tsiSerialNumber':tsiSerialNumber,'tsiVout':tsiVout,'tsiIout':tsiIout,'tsiPoutW':tsiPoutW,'tsiPoutVA':tsiPoutVA,'tsiVinAC':tsiVinAC,'tsiIinAC':tsiIinAC,'tsiPinACW':tsiPinACW,'tsiPinACVA':tsiPinACVA,'tsiACInFreq':tsiACInFreq,'tsiVinDC':tsiVinDC,'tsiIinDC':tsiIinDC,'tsiPinDC':tsiPinDC,'tsiTemperature':tsiTemperature,'tsiSoftVersion':tsiSoftVersion,'tsiBusErrorCnt':tsiBusErrorCnt,'tsiPhaseNumber':tsiPhaseNumber,'tsiStatusMod':tsiStatusMod,'tsiStatusAC':tsiStatusAC,'tsiStatusDC':tsiStatusDC,'tsiPresent':tsiPresent,'tsiGroupAC':tsiGroupAC,'tsiGroupDC':tsiGroupDC,'tsiRestrained':tsiRestrained,'tsiNoEPC':tsiNoEPC,'tsiPoutNominalW':tsiPoutNominalW,'tsiPoutNominalVA':tsiPoutNominalVA,'tsiVinNominalAC':tsiVinNominalAC,'tsiVinNominalDC':tsiVinNominalDC,'tsiVinNominalFreqAC':tsiVinNominalFreqAC,'phaseGroup':phaseGroup,'phaseCount':phaseCount,'phaseGroupTable':phaseGroupTable,'phaseGroupEntry':phaseGroupEntry,_G:phaseGroupIndex,'bRatioAvailableW':bRatioAvailableW,'bRatioAvailableVA':bRatioAvailableVA,'bRatioInstalledW':bRatioInstalledW,'bRatioInstalledWA':bRatioInstalledWA,'wVout':wVout,'wIout':wIout,'bNbOndCfg':bNbOndCfg,'bRedundancy':bRedundancy,'wACOutFreq':wACOutFreq,'lPinDC':lPinDC,'lPinACW':lPinACW,'lPinACVA':lPinACVA,'lCurrentPowerInW':lCurrentPowerInW,'lCurrentPowerInVA':lCurrentPowerInVA,'lInstalledPowerInW':lInstalledPowerInW,'lInstalledPowerInVA':lInstalledPowerInVA,'lAvailablePowerInW':lAvailablePowerInW,'lAvailablePowerInVA':lAvailablePowerInVA,'bNbInvSeen':bNbInvSeen,'bNbInvOK':bNbInvOK,'bNbInvMO':bNbInvMO,'bNbInvKO':bNbInvKO,'bNbInvNT':bNbInvNT,'acGroup':acGroup,'acGroupCount':acGroupCount,'acGroupTable':acGroupTable,'acGroupEntry':acGroupEntry,_H:acGroupIndex,'acNbInvOK':acNbInvOK,'acNbInvMO':acNbInvMO,'acNbInvKO':acNbInvKO,'acNbInvSeen':acNbInvSeen,'acPinACW':acPinACW,'acPinACVA':acPinACVA,'acVinAC':acVinAC,'acIinAC':acIinAC,'acACinFreq':acACinFreq,'acACinOK':acACinOK,'dcGroup':dcGroup,'dcGroupCount':dcGroupCount,'dcGroupTable':dcGroupTable,'dcGroupEntry':dcGroupEntry,_I:dcGroupIndex,'dcNbInvOK':dcNbInvOK,'dcNbInvMO':dcNbInvMO,'dcNbInvKO':dcNbInvKO,'dcNbInvSeen':dcNbInvSeen,'dcPinDC':dcPinDC,'dcVinDC':dcVinDC,'dcIinDC':dcIinDC,'dcDCInOK':dcDCInOK,'miscInfoGroup':miscInfoGroup,'miscInfoGroupCount':miscInfoGroupCount,'miscInfoGroupTable':miscInfoGroupTable,'miscInfoGroupEntry':miscInfoGroupEntry,_J:miscInfoGroupIndex,'bOldVersionNumber':bOldVersionNumber,'ePhaseNumber':ePhaseNumber,'bNbMajor':bNbMajor,'wTempoMajorAl':wTempoMajorAl,'wtempoMinorAl':wtempoMinorAl,'lSerialNumber':lSerialNumber,'bNbMinor':bNbMinor,'bNbTotalAlarmNumber':bNbTotalAlarmNumber,'bACInputPresent':bACInputPresent,'bSaturationThresh':bSaturationThresh,'bNbGroupsDC':bNbGroupsDC,'bNbGroupsAC':bNbGroupsAC,'bProgRelay':bProgRelay,'bSystemLoadPosition':bSystemLoadPosition,'wSoftSubRevision':wSoftSubRevision,'wSoftMainRevision':wSoftMainRevision,'wInvVersionTextError':wInvVersionTextError,'bInvMaxKnowParameters':bInvMaxKnowParameters,'alarmGroup':alarmGroup,'alarmGroupCount':alarmGroupCount,'alarmGroupTable':alarmGroupTable,'alarmGroupEntry':alarmGroupEntry,_K:alarmGroupIndex,'bDeviceNumber':bDeviceNumber,'bEventType':bEventType,'wEventNumber':wEventNumber,'sEventString':sEventString})