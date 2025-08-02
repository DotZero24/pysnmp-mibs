_j='ntcBissScrConfGrpV1Standard'
_i='ntcSwRefusedError'
_h='ntcScramblingError'
_g='ntcCaDescriptorFoundOnInput'
_f='ntcAlreadyScrambled'
_e='ntcCatError'
_d='ntcPmtError'
_c='ntcPatError'
_b='ntcGeneralBissError'
_a='ntcBissSessionWordChanged'
_Z='ntcBissScramblingState'
_Y='ntcBissSetupId'
_X='ntcBissBuriedId'
_W='ntcBissInjectedId'
_V='ntcBissInKeyEncryptionMode'
_U='ntcBissEncryptedOddSessionWord'
_T='ntcBissEncryptedEvenSessionWord'
_S='ntcBissOddSessionWord'
_R='ntcBissEvenSessionWord'
_Q='ntcBissClearKeys'
_P='ntcBissMaxRawUnscrambledPid'
_O='ntcBissMinRawUnscrambledPid'
_N='ntcBissScramblingSuppression'
_M='ntcBissKeyParity'
_L='ntcBissScramblingMode'
_K='ntcBissScrambling'
_J='****************'
_I='************'
_H='NtcEnable'
_G='Unsigned32'
_F='Integer32'
_E='DisplayString'
_D='read-only'
_C='read-write'
_B='NEWTEC-BISSSCRAMBLER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
ntcBissScrambler=ModuleIdentity((1,3,6,1,4,1,5835,5,2,3100))
if mibBuilder.loadTexts:ntcBissScrambler.setRevisions(('2017-07-10 12:00','2014-09-09 09:00','2013-07-02 10:00','2013-03-27 10:00'))
_NtcBissScrObjects_ObjectIdentity=ObjectIdentity
ntcBissScrObjects=_NtcBissScrObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3100,1))
if mibBuilder.loadTexts:ntcBissScrObjects.setStatus(_A)
class _NtcBissScrambling_Type(NtcEnable):defaultValue=0
_NtcBissScrambling_Type.__name__=_H
_NtcBissScrambling_Object=MibScalar
ntcBissScrambling=_NtcBissScrambling_Object((1,3,6,1,4,1,5835,5,2,3100,1,1),_NtcBissScrambling_Type())
ntcBissScrambling.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissScrambling.setStatus(_A)
class _NtcBissScramblingMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('standard',0),('raw',1)))
_NtcBissScramblingMode_Type.__name__=_F
_NtcBissScramblingMode_Object=MibScalar
ntcBissScramblingMode=_NtcBissScramblingMode_Object((1,3,6,1,4,1,5835,5,2,3100,1,2),_NtcBissScramblingMode_Type())
ntcBissScramblingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissScramblingMode.setStatus(_A)
class _NtcBissKeyParity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('odd',0),('even',1)))
_NtcBissKeyParity_Type.__name__=_F
_NtcBissKeyParity_Object=MibScalar
ntcBissKeyParity=_NtcBissKeyParity_Object((1,3,6,1,4,1,5835,5,2,3100,1,3),_NtcBissKeyParity_Type())
ntcBissKeyParity.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissKeyParity.setStatus(_A)
class _NtcBissScramblingSuppression_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_NtcBissScramblingSuppression_Type.__name__=_F
_NtcBissScramblingSuppression_Object=MibScalar
ntcBissScramblingSuppression=_NtcBissScramblingSuppression_Object((1,3,6,1,4,1,5835,5,2,3100,1,4),_NtcBissScramblingSuppression_Type())
ntcBissScramblingSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissScramblingSuppression.setStatus(_A)
class _NtcBissMinRawUnscrambledPid_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8190))
_NtcBissMinRawUnscrambledPid_Type.__name__=_G
_NtcBissMinRawUnscrambledPid_Object=MibScalar
ntcBissMinRawUnscrambledPid=_NtcBissMinRawUnscrambledPid_Object((1,3,6,1,4,1,5835,5,2,3100,1,5),_NtcBissMinRawUnscrambledPid_Type())
ntcBissMinRawUnscrambledPid.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissMinRawUnscrambledPid.setStatus(_A)
class _NtcBissMaxRawUnscrambledPid_Type(Unsigned32):defaultValue=31;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8190))
_NtcBissMaxRawUnscrambledPid_Type.__name__=_G
_NtcBissMaxRawUnscrambledPid_Object=MibScalar
ntcBissMaxRawUnscrambledPid=_NtcBissMaxRawUnscrambledPid_Object((1,3,6,1,4,1,5835,5,2,3100,1,6),_NtcBissMaxRawUnscrambledPid_Type())
ntcBissMaxRawUnscrambledPid.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissMaxRawUnscrambledPid.setStatus(_A)
_NtcBissScrKeys_ObjectIdentity=ObjectIdentity
ntcBissScrKeys=_NtcBissScrKeys_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3100,1,7))
if mibBuilder.loadTexts:ntcBissScrKeys.setStatus(_A)
class _NtcBissClearKeys_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('donothing',0),('clearkeys',1)))
_NtcBissClearKeys_Type.__name__=_F
_NtcBissClearKeys_Object=MibScalar
ntcBissClearKeys=_NtcBissClearKeys_Object((1,3,6,1,4,1,5835,5,2,3100,1,7,1),_NtcBissClearKeys_Type())
ntcBissClearKeys.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissClearKeys.setStatus(_A)
class _NtcBissEvenSessionWord_Type(DisplayString):defaultValue=OctetString(_I);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_NtcBissEvenSessionWord_Type.__name__=_E
_NtcBissEvenSessionWord_Object=MibScalar
ntcBissEvenSessionWord=_NtcBissEvenSessionWord_Object((1,3,6,1,4,1,5835,5,2,3100,1,7,2),_NtcBissEvenSessionWord_Type())
ntcBissEvenSessionWord.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissEvenSessionWord.setStatus(_A)
class _NtcBissOddSessionWord_Type(DisplayString):defaultValue=OctetString(_I);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_NtcBissOddSessionWord_Type.__name__=_E
_NtcBissOddSessionWord_Object=MibScalar
ntcBissOddSessionWord=_NtcBissOddSessionWord_Object((1,3,6,1,4,1,5835,5,2,3100,1,7,3),_NtcBissOddSessionWord_Type())
ntcBissOddSessionWord.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissOddSessionWord.setStatus(_A)
class _NtcBissEncryptedEvenSessionWord_Type(DisplayString):defaultValue=OctetString(_J);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_NtcBissEncryptedEvenSessionWord_Type.__name__=_E
_NtcBissEncryptedEvenSessionWord_Object=MibScalar
ntcBissEncryptedEvenSessionWord=_NtcBissEncryptedEvenSessionWord_Object((1,3,6,1,4,1,5835,5,2,3100,1,7,4),_NtcBissEncryptedEvenSessionWord_Type())
ntcBissEncryptedEvenSessionWord.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissEncryptedEvenSessionWord.setStatus(_A)
class _NtcBissEncryptedOddSessionWord_Type(DisplayString):defaultValue=OctetString(_J);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_NtcBissEncryptedOddSessionWord_Type.__name__=_E
_NtcBissEncryptedOddSessionWord_Object=MibScalar
ntcBissEncryptedOddSessionWord=_NtcBissEncryptedOddSessionWord_Object((1,3,6,1,4,1,5835,5,2,3100,1,7,5),_NtcBissEncryptedOddSessionWord_Type())
ntcBissEncryptedOddSessionWord.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissEncryptedOddSessionWord.setStatus(_A)
class _NtcBissInKeyEncryptionMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('buried',0),('injected',1)))
_NtcBissInKeyEncryptionMode_Type.__name__=_F
_NtcBissInKeyEncryptionMode_Object=MibScalar
ntcBissInKeyEncryptionMode=_NtcBissInKeyEncryptionMode_Object((1,3,6,1,4,1,5835,5,2,3100,1,7,6),_NtcBissInKeyEncryptionMode_Type())
ntcBissInKeyEncryptionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissInKeyEncryptionMode.setStatus(_A)
class _NtcBissInjectedId_Type(DisplayString):defaultValue=OctetString('00000000000000');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
_NtcBissInjectedId_Type.__name__=_E
_NtcBissInjectedId_Object=MibScalar
ntcBissInjectedId=_NtcBissInjectedId_Object((1,3,6,1,4,1,5835,5,2,3100,1,7,7),_NtcBissInjectedId_Type())
ntcBissInjectedId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissInjectedId.setStatus(_A)
class _NtcBissBuriedId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
_NtcBissBuriedId_Type.__name__=_E
_NtcBissBuriedId_Object=MibScalar
ntcBissBuriedId=_NtcBissBuriedId_Object((1,3,6,1,4,1,5835,5,2,3100,1,7,8),_NtcBissBuriedId_Type())
ntcBissBuriedId.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBissBuriedId.setStatus(_A)
class _NtcBissSetupId_Type(DisplayString):defaultValue=OctetString('BD28121969BD');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_NtcBissSetupId_Type.__name__=_E
_NtcBissSetupId_Object=MibScalar
ntcBissSetupId=_NtcBissSetupId_Object((1,3,6,1,4,1,5835,5,2,3100,1,7,9),_NtcBissSetupId_Type())
ntcBissSetupId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBissSetupId.setStatus(_A)
_NtcBissMonitor_ObjectIdentity=ObjectIdentity
ntcBissMonitor=_NtcBissMonitor_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3100,1,8))
if mibBuilder.loadTexts:ntcBissMonitor.setStatus(_A)
class _NtcBissScramblingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('scrambling',0),('suppressed',1),('unscrambled',2)))
_NtcBissScramblingState_Type.__name__=_F
_NtcBissScramblingState_Object=MibScalar
ntcBissScramblingState=_NtcBissScramblingState_Object((1,3,6,1,4,1,5835,5,2,3100,1,8,1),_NtcBissScramblingState_Type())
ntcBissScramblingState.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBissScramblingState.setStatus(_A)
class _NtcBissSessionWordChanged_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcBissSessionWordChanged_Type.__name__=_E
_NtcBissSessionWordChanged_Object=MibScalar
ntcBissSessionWordChanged=_NtcBissSessionWordChanged_Object((1,3,6,1,4,1,5835,5,2,3100,1,8,2),_NtcBissSessionWordChanged_Type())
ntcBissSessionWordChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBissSessionWordChanged.setStatus(_A)
_NtcBissAlarms_ObjectIdentity=ObjectIdentity
ntcBissAlarms=_NtcBissAlarms_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3100,1,9))
if mibBuilder.loadTexts:ntcBissAlarms.setStatus(_A)
_NtcGeneralBissError_Type=NtcAlarmState
_NtcGeneralBissError_Object=MibScalar
ntcGeneralBissError=_NtcGeneralBissError_Object((1,3,6,1,4,1,5835,5,2,3100,1,9,1),_NtcGeneralBissError_Type())
ntcGeneralBissError.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcGeneralBissError.setStatus(_A)
_NtcPatError_Type=NtcAlarmState
_NtcPatError_Object=MibScalar
ntcPatError=_NtcPatError_Object((1,3,6,1,4,1,5835,5,2,3100,1,9,2),_NtcPatError_Type())
ntcPatError.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcPatError.setStatus(_A)
_NtcPmtError_Type=NtcAlarmState
_NtcPmtError_Object=MibScalar
ntcPmtError=_NtcPmtError_Object((1,3,6,1,4,1,5835,5,2,3100,1,9,3),_NtcPmtError_Type())
ntcPmtError.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcPmtError.setStatus(_A)
_NtcCatError_Type=NtcAlarmState
_NtcCatError_Object=MibScalar
ntcCatError=_NtcCatError_Object((1,3,6,1,4,1,5835,5,2,3100,1,9,4),_NtcCatError_Type())
ntcCatError.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcCatError.setStatus(_A)
_NtcAlreadyScrambled_Type=NtcAlarmState
_NtcAlreadyScrambled_Object=MibScalar
ntcAlreadyScrambled=_NtcAlreadyScrambled_Object((1,3,6,1,4,1,5835,5,2,3100,1,9,5),_NtcAlreadyScrambled_Type())
ntcAlreadyScrambled.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAlreadyScrambled.setStatus(_A)
_NtcCaDescriptorFoundOnInput_Type=NtcAlarmState
_NtcCaDescriptorFoundOnInput_Object=MibScalar
ntcCaDescriptorFoundOnInput=_NtcCaDescriptorFoundOnInput_Object((1,3,6,1,4,1,5835,5,2,3100,1,9,6),_NtcCaDescriptorFoundOnInput_Type())
ntcCaDescriptorFoundOnInput.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcCaDescriptorFoundOnInput.setStatus(_A)
_NtcScramblingError_Type=NtcAlarmState
_NtcScramblingError_Object=MibScalar
ntcScramblingError=_NtcScramblingError_Object((1,3,6,1,4,1,5835,5,2,3100,1,9,7),_NtcScramblingError_Type())
ntcScramblingError.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcScramblingError.setStatus(_A)
_NtcSwRefusedError_Type=NtcAlarmState
_NtcSwRefusedError_Object=MibScalar
ntcSwRefusedError=_NtcSwRefusedError_Object((1,3,6,1,4,1,5835,5,2,3100,1,9,8),_NtcSwRefusedError_Type())
ntcSwRefusedError.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcSwRefusedError.setStatus(_A)
_NtcBissScrConformance_ObjectIdentity=ObjectIdentity
ntcBissScrConformance=_NtcBissScrConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3100,2))
if mibBuilder.loadTexts:ntcBissScrConformance.setStatus(_A)
_NtcBissScrConfCompliance_ObjectIdentity=ObjectIdentity
ntcBissScrConfCompliance=_NtcBissScrConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3100,2,1))
if mibBuilder.loadTexts:ntcBissScrConfCompliance.setStatus(_A)
_NtcBissScrConfGroup_ObjectIdentity=ObjectIdentity
ntcBissScrConfGroup=_NtcBissScrConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3100,2,2))
if mibBuilder.loadTexts:ntcBissScrConfGroup.setStatus(_A)
ntcBissScrConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,3100,2,2,1))
ntcBissScrConfGrpV1Standard.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:ntcBissScrConfGrpV1Standard.setStatus(_A)
ntcBissScrConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,3100,2,1,1))
ntcBissScrConfCompV1Standard.setObjects((_B,_j))
if mibBuilder.loadTexts:ntcBissScrConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcBissScrambler':ntcBissScrambler,'ntcBissScrObjects':ntcBissScrObjects,_K:ntcBissScrambling,_L:ntcBissScramblingMode,_M:ntcBissKeyParity,_N:ntcBissScramblingSuppression,_O:ntcBissMinRawUnscrambledPid,_P:ntcBissMaxRawUnscrambledPid,'ntcBissScrKeys':ntcBissScrKeys,_Q:ntcBissClearKeys,_R:ntcBissEvenSessionWord,_S:ntcBissOddSessionWord,_T:ntcBissEncryptedEvenSessionWord,_U:ntcBissEncryptedOddSessionWord,_V:ntcBissInKeyEncryptionMode,_W:ntcBissInjectedId,_X:ntcBissBuriedId,_Y:ntcBissSetupId,'ntcBissMonitor':ntcBissMonitor,_Z:ntcBissScramblingState,_a:ntcBissSessionWordChanged,'ntcBissAlarms':ntcBissAlarms,_b:ntcGeneralBissError,_c:ntcPatError,_d:ntcPmtError,_e:ntcCatError,_f:ntcAlreadyScrambled,_g:ntcCaDescriptorFoundOnInput,_h:ntcScramblingError,_i:ntcSwRefusedError,'ntcBissScrConformance':ntcBissScrConformance,'ntcBissScrConfCompliance':ntcBissScrConfCompliance,'ntcBissScrConfCompV1Standard':ntcBissScrConfCompV1Standard,'ntcBissScrConfGroup':ntcBissScrConfGroup,_j:ntcBissScrConfGrpV1Standard})