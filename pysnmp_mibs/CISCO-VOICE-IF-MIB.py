_X='cvIfConnectionGroup'
_W='cvIfGroup'
_V='cvIfCfgConnectionNumber'
_U='cvIfCfgConnectionMode'
_T='cvIfCfgEchoCanceller'
_S='cvIfCfgEchoCancelWorstERL'
_R='cvIfCfgRegionalTone'
_Q='cvIfCfgInterDigitTimeOut'
_P='cvIfCfgInitialDigitTimeOut'
_O='cvIfCfgEchoCancelCoverage'
_N='cvIfCfgEchoCancelEnable'
_M='cvIfCfgOutAttn'
_L='cvIfCfgInGain'
_K='cvIfCfgMusicOnHoldThreshold'
_J='cvIfCfgNonLinearProcEnable'
_I='cvIfCfgNoiseRegEnable'
_H='seconds'
_G='DisplayString'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-write'
_B='CISCO-VOICE-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CountryCode,=mibBuilder.importSymbols('CISCO-TC','CountryCode')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention','TruthValue')
ciscoVoiceInterfaceMIB=ModuleIdentity((1,3,6,1,4,1,9,9,64))
if mibBuilder.loadTexts:ciscoVoiceInterfaceMIB.setRevisions(('2003-07-18 00:00','2001-03-08 00:00'))
_CvIfObjects_ObjectIdentity=ObjectIdentity
cvIfObjects=_CvIfObjects_ObjectIdentity((1,3,6,1,4,1,9,9,64,1))
_CvIfCfgObjects_ObjectIdentity=ObjectIdentity
cvIfCfgObjects=_CvIfCfgObjects_ObjectIdentity((1,3,6,1,4,1,9,9,64,1,1))
_CvIfCfgTable_Object=MibTable
cvIfCfgTable=_CvIfCfgTable_Object((1,3,6,1,4,1,9,9,64,1,1,1))
if mibBuilder.loadTexts:cvIfCfgTable.setStatus(_A)
_CvIfCfgEntry_Object=MibTableRow
cvIfCfgEntry=_CvIfCfgEntry_Object((1,3,6,1,4,1,9,9,64,1,1,1,1))
cvIfCfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cvIfCfgEntry.setStatus(_A)
_CvIfCfgNoiseRegEnable_Type=TruthValue
_CvIfCfgNoiseRegEnable_Object=MibTableColumn
cvIfCfgNoiseRegEnable=_CvIfCfgNoiseRegEnable_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,1),_CvIfCfgNoiseRegEnable_Type())
cvIfCfgNoiseRegEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cvIfCfgNoiseRegEnable.setStatus(_A)
_CvIfCfgNonLinearProcEnable_Type=TruthValue
_CvIfCfgNonLinearProcEnable_Object=MibTableColumn
cvIfCfgNonLinearProcEnable=_CvIfCfgNonLinearProcEnable_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,2),_CvIfCfgNonLinearProcEnable_Type())
cvIfCfgNonLinearProcEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cvIfCfgNonLinearProcEnable.setStatus(_A)
class _CvIfCfgMusicOnHoldThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-70,-30))
_CvIfCfgMusicOnHoldThreshold_Type.__name__=_D
_CvIfCfgMusicOnHoldThreshold_Object=MibTableColumn
cvIfCfgMusicOnHoldThreshold=_CvIfCfgMusicOnHoldThreshold_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,3),_CvIfCfgMusicOnHoldThreshold_Type())
cvIfCfgMusicOnHoldThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cvIfCfgMusicOnHoldThreshold.setStatus(_A)
if mibBuilder.loadTexts:cvIfCfgMusicOnHoldThreshold.setUnits('dBm')
class _CvIfCfgInGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-6,14))
_CvIfCfgInGain_Type.__name__=_D
_CvIfCfgInGain_Object=MibTableColumn
cvIfCfgInGain=_CvIfCfgInGain_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,4),_CvIfCfgInGain_Type())
cvIfCfgInGain.setMaxAccess(_C)
if mibBuilder.loadTexts:cvIfCfgInGain.setStatus(_A)
if mibBuilder.loadTexts:cvIfCfgInGain.setUnits('dB')
class _CvIfCfgOutAttn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_CvIfCfgOutAttn_Type.__name__=_D
_CvIfCfgOutAttn_Object=MibTableColumn
cvIfCfgOutAttn=_CvIfCfgOutAttn_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,5),_CvIfCfgOutAttn_Type())
cvIfCfgOutAttn.setMaxAccess(_C)
if mibBuilder.loadTexts:cvIfCfgOutAttn.setStatus(_A)
if mibBuilder.loadTexts:cvIfCfgOutAttn.setUnits('dB')
_CvIfCfgEchoCancelEnable_Type=TruthValue
_CvIfCfgEchoCancelEnable_Object=MibTableColumn
cvIfCfgEchoCancelEnable=_CvIfCfgEchoCancelEnable_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,6),_CvIfCfgEchoCancelEnable_Type())
cvIfCfgEchoCancelEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cvIfCfgEchoCancelEnable.setStatus(_A)
class _CvIfCfgEchoCancelCoverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('echoCanceller16ms',1),('echoCanceller24ms',2),('echoCanceller32ms',3),('echoCanceller8ms',4),('echoCanceller48ms',5),('echoCanceller64ms',6),('echoCanceller80ms',7),('echoCanceller96ms',8),('echoCanceller112ms',9),('echoCanceller128ms',10)))
_CvIfCfgEchoCancelCoverage_Type.__name__=_D
_CvIfCfgEchoCancelCoverage_Object=MibTableColumn
cvIfCfgEchoCancelCoverage=_CvIfCfgEchoCancelCoverage_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,7),_CvIfCfgEchoCancelCoverage_Type())
cvIfCfgEchoCancelCoverage.setMaxAccess(_C)
if mibBuilder.loadTexts:cvIfCfgEchoCancelCoverage.setStatus(_A)
class _CvIfCfgConnectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('trunk',2),('plar',3),('tieline',4)))
_CvIfCfgConnectionMode_Type.__name__=_D
_CvIfCfgConnectionMode_Object=MibTableColumn
cvIfCfgConnectionMode=_CvIfCfgConnectionMode_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,8),_CvIfCfgConnectionMode_Type())
cvIfCfgConnectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cvIfCfgConnectionMode.setStatus(_A)
class _CvIfCfgConnectionNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CvIfCfgConnectionNumber_Type.__name__=_G
_CvIfCfgConnectionNumber_Object=MibTableColumn
cvIfCfgConnectionNumber=_CvIfCfgConnectionNumber_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,9),_CvIfCfgConnectionNumber_Type())
cvIfCfgConnectionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cvIfCfgConnectionNumber.setStatus(_A)
class _CvIfCfgInitialDigitTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_CvIfCfgInitialDigitTimeOut_Type.__name__=_D
_CvIfCfgInitialDigitTimeOut_Object=MibTableColumn
cvIfCfgInitialDigitTimeOut=_CvIfCfgInitialDigitTimeOut_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,10),_CvIfCfgInitialDigitTimeOut_Type())
cvIfCfgInitialDigitTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cvIfCfgInitialDigitTimeOut.setStatus(_A)
if mibBuilder.loadTexts:cvIfCfgInitialDigitTimeOut.setUnits(_H)
class _CvIfCfgInterDigitTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_CvIfCfgInterDigitTimeOut_Type.__name__=_D
_CvIfCfgInterDigitTimeOut_Object=MibTableColumn
cvIfCfgInterDigitTimeOut=_CvIfCfgInterDigitTimeOut_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,11),_CvIfCfgInterDigitTimeOut_Type())
cvIfCfgInterDigitTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cvIfCfgInterDigitTimeOut.setStatus(_A)
if mibBuilder.loadTexts:cvIfCfgInterDigitTimeOut.setUnits(_H)
_CvIfCfgRegionalTone_Type=CountryCode
_CvIfCfgRegionalTone_Object=MibTableColumn
cvIfCfgRegionalTone=_CvIfCfgRegionalTone_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,12),_CvIfCfgRegionalTone_Type())
cvIfCfgRegionalTone.setMaxAccess(_C)
if mibBuilder.loadTexts:cvIfCfgRegionalTone.setStatus(_A)
class _CvIfCfgEchoCancelWorstERL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('echoCancellerWorstERLUnknown',1),('echoCancellerWorstERL6dB',2),('echoCancellerWorstERL3dB',3),('echoCancellerWorstERL0dB',4)))
_CvIfCfgEchoCancelWorstERL_Type.__name__=_D
_CvIfCfgEchoCancelWorstERL_Object=MibTableColumn
cvIfCfgEchoCancelWorstERL=_CvIfCfgEchoCancelWorstERL_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,13),_CvIfCfgEchoCancelWorstERL_Type())
cvIfCfgEchoCancelWorstERL.setMaxAccess(_C)
if mibBuilder.loadTexts:cvIfCfgEchoCancelWorstERL.setStatus(_A)
class _CvIfCfgEchoCanceller_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('echoCancellerStandard',1),('echoCancellerExtended',2)))
_CvIfCfgEchoCanceller_Type.__name__=_D
_CvIfCfgEchoCanceller_Object=MibTableColumn
cvIfCfgEchoCanceller=_CvIfCfgEchoCanceller_Object((1,3,6,1,4,1,9,9,64,1,1,1,1,14),_CvIfCfgEchoCanceller_Type())
cvIfCfgEchoCanceller.setMaxAccess('read-only')
if mibBuilder.loadTexts:cvIfCfgEchoCanceller.setStatus(_A)
_CvIfConformance_ObjectIdentity=ObjectIdentity
cvIfConformance=_CvIfConformance_ObjectIdentity((1,3,6,1,4,1,9,9,64,2))
_CvIfCompliances_ObjectIdentity=ObjectIdentity
cvIfCompliances=_CvIfCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,64,2,1))
_CvIfGroups_ObjectIdentity=ObjectIdentity
cvIfGroups=_CvIfGroups_ObjectIdentity((1,3,6,1,4,1,9,9,64,2,2))
cvIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,64,2,2,1))
cvIfGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cvIfGroup.setStatus(_A)
cvIfConnectionGroup=ObjectGroup((1,3,6,1,4,1,9,9,64,2,2,2))
cvIfConnectionGroup.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:cvIfConnectionGroup.setStatus(_A)
cvIfCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,64,2,1,1))
cvIfCompliance.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:cvIfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVoiceInterfaceMIB':ciscoVoiceInterfaceMIB,'cvIfObjects':cvIfObjects,'cvIfCfgObjects':cvIfCfgObjects,'cvIfCfgTable':cvIfCfgTable,'cvIfCfgEntry':cvIfCfgEntry,_I:cvIfCfgNoiseRegEnable,_J:cvIfCfgNonLinearProcEnable,_K:cvIfCfgMusicOnHoldThreshold,_L:cvIfCfgInGain,_M:cvIfCfgOutAttn,_N:cvIfCfgEchoCancelEnable,_O:cvIfCfgEchoCancelCoverage,_U:cvIfCfgConnectionMode,_V:cvIfCfgConnectionNumber,_P:cvIfCfgInitialDigitTimeOut,_Q:cvIfCfgInterDigitTimeOut,_R:cvIfCfgRegionalTone,_S:cvIfCfgEchoCancelWorstERL,_T:cvIfCfgEchoCanceller,'cvIfConformance':cvIfConformance,'cvIfCompliances':cvIfCompliances,'cvIfCompliance':cvIfCompliance,'cvIfGroups':cvIfGroups,_W:cvIfGroup,_X:cvIfConnectionGroup})