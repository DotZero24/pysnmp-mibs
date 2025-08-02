_W='cpqMeAlarmIndex'
_V='cpqMeOsCommonModuleIndex'
_U='NotificationType'
_T='OctetString'
_S='cpqMeAlarmExtendedDescription'
_R='cpqMeAlarmSeverity'
_Q='cpqMeAlarmFallingThreshold'
_P='cpqMeAlarmRisingThreshold'
_O='DisplayString'
_N='deprecated'
_M='sysName'
_L='SNMPv2-MIB'
_K='cpqHoTrapFlags'
_J='CPQHOST-MIB'
_I='cpqMeAlarmOwner'
_H='cpqMeAlarmValue'
_G='cpqMeAlarmSampleType'
_F='cpqMeAlarmVariable'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='mandatory'
_A='CPQTHRSH-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_T,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_J,'compaq',_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_L,_M)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_U,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_U,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','TextualConvention')
_CpqThresholdMgmt_ObjectIdentity=ObjectIdentity
cpqThresholdMgmt=_CpqThresholdMgmt_ObjectIdentity((1,3,6,1,4,1,232,10))
_CpqMeMibRev_ObjectIdentity=ObjectIdentity
cpqMeMibRev=_CpqMeMibRev_ObjectIdentity((1,3,6,1,4,1,232,10,1))
class _CpqMeMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqMeMibRevMajor_Type.__name__=_C
_CpqMeMibRevMajor_Object=MibScalar
cpqMeMibRevMajor=_CpqMeMibRevMajor_Object((1,3,6,1,4,1,232,10,1,1),_CpqMeMibRevMajor_Type())
cpqMeMibRevMajor.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqMeMibRevMajor.setStatus(_B)
class _CpqMeMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqMeMibRevMinor_Type.__name__=_C
_CpqMeMibRevMinor_Object=MibScalar
cpqMeMibRevMinor=_CpqMeMibRevMinor_Object((1,3,6,1,4,1,232,10,1,2),_CpqMeMibRevMinor_Type())
cpqMeMibRevMinor.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqMeMibRevMinor.setStatus(_B)
class _CpqMeMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ok',2),('degraded',3),('failed',4)))
_CpqMeMibCondition_Type.__name__=_C
_CpqMeMibCondition_Object=MibScalar
cpqMeMibCondition=_CpqMeMibCondition_Object((1,3,6,1,4,1,232,10,1,3),_CpqMeMibCondition_Type())
cpqMeMibCondition.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqMeMibCondition.setStatus(_B)
_CpqMeComponent_ObjectIdentity=ObjectIdentity
cpqMeComponent=_CpqMeComponent_ObjectIdentity((1,3,6,1,4,1,232,10,2))
_CpqMeInterface_ObjectIdentity=ObjectIdentity
cpqMeInterface=_CpqMeInterface_ObjectIdentity((1,3,6,1,4,1,232,10,2,1))
_CpqMeOsCommon_ObjectIdentity=ObjectIdentity
cpqMeOsCommon=_CpqMeOsCommon_ObjectIdentity((1,3,6,1,4,1,232,10,2,1,4))
class _CpqMeOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CpqMeOsCommonPollFreq_Type.__name__=_C
_CpqMeOsCommonPollFreq_Object=MibScalar
cpqMeOsCommonPollFreq=_CpqMeOsCommonPollFreq_Object((1,3,6,1,4,1,232,10,2,1,4,1),_CpqMeOsCommonPollFreq_Type())
cpqMeOsCommonPollFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqMeOsCommonPollFreq.setStatus(_B)
_CpqMeOsCommonModuleTable_Object=MibTable
cpqMeOsCommonModuleTable=_CpqMeOsCommonModuleTable_Object((1,3,6,1,4,1,232,10,2,1,4,2))
if mibBuilder.loadTexts:cpqMeOsCommonModuleTable.setStatus(_N)
_CpqMeOsCommonModuleEntry_Object=MibTableRow
cpqMeOsCommonModuleEntry=_CpqMeOsCommonModuleEntry_Object((1,3,6,1,4,1,232,10,2,1,4,2,1))
cpqMeOsCommonModuleEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:cpqMeOsCommonModuleEntry.setStatus(_N)
class _CpqMeOsCommonModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqMeOsCommonModuleIndex_Type.__name__=_C
_CpqMeOsCommonModuleIndex_Object=MibTableColumn
cpqMeOsCommonModuleIndex=_CpqMeOsCommonModuleIndex_Object((1,3,6,1,4,1,232,10,2,1,4,2,1,1),_CpqMeOsCommonModuleIndex_Type())
cpqMeOsCommonModuleIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqMeOsCommonModuleIndex.setStatus(_N)
class _CpqMeOsCommonModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqMeOsCommonModuleName_Type.__name__=_O
_CpqMeOsCommonModuleName_Object=MibTableColumn
cpqMeOsCommonModuleName=_CpqMeOsCommonModuleName_Object((1,3,6,1,4,1,232,10,2,1,4,2,1,2),_CpqMeOsCommonModuleName_Type())
cpqMeOsCommonModuleName.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqMeOsCommonModuleName.setStatus(_N)
class _CpqMeOsCommonModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqMeOsCommonModuleVersion_Type.__name__=_O
_CpqMeOsCommonModuleVersion_Object=MibTableColumn
cpqMeOsCommonModuleVersion=_CpqMeOsCommonModuleVersion_Object((1,3,6,1,4,1,232,10,2,1,4,2,1,3),_CpqMeOsCommonModuleVersion_Type())
cpqMeOsCommonModuleVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqMeOsCommonModuleVersion.setStatus(_N)
class _CpqMeOsCommonModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqMeOsCommonModuleDate_Type.__name__=_T
_CpqMeOsCommonModuleDate_Object=MibTableColumn
cpqMeOsCommonModuleDate=_CpqMeOsCommonModuleDate_Object((1,3,6,1,4,1,232,10,2,1,4,2,1,4),_CpqMeOsCommonModuleDate_Type())
cpqMeOsCommonModuleDate.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqMeOsCommonModuleDate.setStatus(_N)
class _CpqMeOsCommonModulePurpose_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqMeOsCommonModulePurpose_Type.__name__=_O
_CpqMeOsCommonModulePurpose_Object=MibTableColumn
cpqMeOsCommonModulePurpose=_CpqMeOsCommonModulePurpose_Object((1,3,6,1,4,1,232,10,2,1,4,2,1,5),_CpqMeOsCommonModulePurpose_Type())
cpqMeOsCommonModulePurpose.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqMeOsCommonModulePurpose.setStatus(_N)
_CpqMeAlarm_ObjectIdentity=ObjectIdentity
cpqMeAlarm=_CpqMeAlarm_ObjectIdentity((1,3,6,1,4,1,232,10,2,2))
_CpqMeAlarmNextIndex_Type=Integer32
_CpqMeAlarmNextIndex_Object=MibScalar
cpqMeAlarmNextIndex=_CpqMeAlarmNextIndex_Object((1,3,6,1,4,1,232,10,2,2,1),_CpqMeAlarmNextIndex_Type())
cpqMeAlarmNextIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqMeAlarmNextIndex.setStatus(_B)
_CpqMeAlarmTable_Object=MibTable
cpqMeAlarmTable=_CpqMeAlarmTable_Object((1,3,6,1,4,1,232,10,2,2,2))
if mibBuilder.loadTexts:cpqMeAlarmTable.setStatus(_B)
_CpqMeAlarmEntry_Object=MibTableRow
cpqMeAlarmEntry=_CpqMeAlarmEntry_Object((1,3,6,1,4,1,232,10,2,2,2,1))
cpqMeAlarmEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:cpqMeAlarmEntry.setStatus(_B)
class _CpqMeAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqMeAlarmIndex_Type.__name__=_C
_CpqMeAlarmIndex_Object=MibTableColumn
cpqMeAlarmIndex=_CpqMeAlarmIndex_Object((1,3,6,1,4,1,232,10,2,2,2,1,1),_CpqMeAlarmIndex_Type())
cpqMeAlarmIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqMeAlarmIndex.setStatus(_B)
class _CpqMeAlarmInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CpqMeAlarmInterval_Type.__name__=_C
_CpqMeAlarmInterval_Object=MibTableColumn
cpqMeAlarmInterval=_CpqMeAlarmInterval_Object((1,3,6,1,4,1,232,10,2,2,2,1,2),_CpqMeAlarmInterval_Type())
cpqMeAlarmInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqMeAlarmInterval.setStatus(_B)
_CpqMeAlarmVariable_Type=ObjectIdentifier
_CpqMeAlarmVariable_Object=MibTableColumn
cpqMeAlarmVariable=_CpqMeAlarmVariable_Object((1,3,6,1,4,1,232,10,2,2,2,1,3),_CpqMeAlarmVariable_Type())
cpqMeAlarmVariable.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqMeAlarmVariable.setStatus(_B)
class _CpqMeAlarmSampleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2),('absSuppressRisingTrap',3),('absSuppressFallingTrap',4)))
_CpqMeAlarmSampleType_Type.__name__=_C
_CpqMeAlarmSampleType_Object=MibTableColumn
cpqMeAlarmSampleType=_CpqMeAlarmSampleType_Object((1,3,6,1,4,1,232,10,2,2,2,1,4),_CpqMeAlarmSampleType_Type())
cpqMeAlarmSampleType.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqMeAlarmSampleType.setStatus(_B)
_CpqMeAlarmValue_Type=Integer32
_CpqMeAlarmValue_Object=MibTableColumn
cpqMeAlarmValue=_CpqMeAlarmValue_Object((1,3,6,1,4,1,232,10,2,2,2,1,5),_CpqMeAlarmValue_Type())
cpqMeAlarmValue.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqMeAlarmValue.setStatus(_B)
class _CpqMeAlarmStartupAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('risingAlarm',1),('fallingAlarm',2),('risingOrFallingAlarm',3)))
_CpqMeAlarmStartupAlarm_Type.__name__=_C
_CpqMeAlarmStartupAlarm_Object=MibTableColumn
cpqMeAlarmStartupAlarm=_CpqMeAlarmStartupAlarm_Object((1,3,6,1,4,1,232,10,2,2,2,1,6),_CpqMeAlarmStartupAlarm_Type())
cpqMeAlarmStartupAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqMeAlarmStartupAlarm.setStatus(_B)
_CpqMeAlarmRisingThreshold_Type=Integer32
_CpqMeAlarmRisingThreshold_Object=MibTableColumn
cpqMeAlarmRisingThreshold=_CpqMeAlarmRisingThreshold_Object((1,3,6,1,4,1,232,10,2,2,2,1,7),_CpqMeAlarmRisingThreshold_Type())
cpqMeAlarmRisingThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqMeAlarmRisingThreshold.setStatus(_B)
_CpqMeAlarmFallingThreshold_Type=Integer32
_CpqMeAlarmFallingThreshold_Object=MibTableColumn
cpqMeAlarmFallingThreshold=_CpqMeAlarmFallingThreshold_Object((1,3,6,1,4,1,232,10,2,2,2,1,8),_CpqMeAlarmFallingThreshold_Type())
cpqMeAlarmFallingThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqMeAlarmFallingThreshold.setStatus(_B)
class _CpqMeAlarmPermanence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('temporary',1),('permanent',2)))
_CpqMeAlarmPermanence_Type.__name__=_C
_CpqMeAlarmPermanence_Object=MibTableColumn
cpqMeAlarmPermanence=_CpqMeAlarmPermanence_Object((1,3,6,1,4,1,232,10,2,2,2,1,9),_CpqMeAlarmPermanence_Type())
cpqMeAlarmPermanence.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqMeAlarmPermanence.setStatus(_B)
class _CpqMeAlarmOwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CpqMeAlarmOwner_Type.__name__=_O
_CpqMeAlarmOwner_Object=MibTableColumn
cpqMeAlarmOwner=_CpqMeAlarmOwner_Object((1,3,6,1,4,1,232,10,2,2,2,1,10),_CpqMeAlarmOwner_Type())
cpqMeAlarmOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqMeAlarmOwner.setStatus(_B)
class _CpqMeAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('valid',1),('createRequest',2),('underCreation',3),('invalid',4),('tempUnavailable',5)))
_CpqMeAlarmStatus_Type.__name__=_C
_CpqMeAlarmStatus_Object=MibTableColumn
cpqMeAlarmStatus=_CpqMeAlarmStatus_Object((1,3,6,1,4,1,232,10,2,2,2,1,11),_CpqMeAlarmStatus_Type())
cpqMeAlarmStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqMeAlarmStatus.setStatus(_B)
class _CpqMeAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('normal',2),('minor',3),('warning',4),('major',5),('critical',6)))
_CpqMeAlarmSeverity_Type.__name__=_C
_CpqMeAlarmSeverity_Object=MibTableColumn
cpqMeAlarmSeverity=_CpqMeAlarmSeverity_Object((1,3,6,1,4,1,232,10,2,2,2,1,12),_CpqMeAlarmSeverity_Type())
cpqMeAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqMeAlarmSeverity.setStatus(_B)
class _CpqMeAlarmExtendedDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CpqMeAlarmExtendedDescription_Type.__name__=_O
_CpqMeAlarmExtendedDescription_Object=MibTableColumn
cpqMeAlarmExtendedDescription=_CpqMeAlarmExtendedDescription_Object((1,3,6,1,4,1,232,10,2,2,2,1,13),_CpqMeAlarmExtendedDescription_Type())
cpqMeAlarmExtendedDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqMeAlarmExtendedDescription.setStatus(_B)
cpqMeRisingAlarm=NotificationType((1,3,6,1,4,1,232,0,10001))
cpqMeRisingAlarm.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_P),(_A,_I)))
if mibBuilder.loadTexts:cpqMeRisingAlarm.setStatus('')
cpqMeFallingAlarm=NotificationType((1,3,6,1,4,1,232,0,10002))
cpqMeFallingAlarm.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_Q),(_A,_I)))
if mibBuilder.loadTexts:cpqMeFallingAlarm.setStatus('')
cpqMe2RisingAlarm=NotificationType((1,3,6,1,4,1,232,0,10003))
cpqMe2RisingAlarm.setObjects(*((_L,_M),(_J,_K),(_A,_F),(_A,_G),(_A,_H),(_A,_P),(_A,_I)))
if mibBuilder.loadTexts:cpqMe2RisingAlarm.setStatus('')
cpqMe2FallingAlarm=NotificationType((1,3,6,1,4,1,232,0,10004))
cpqMe2FallingAlarm.setObjects(*((_L,_M),(_J,_K),(_A,_F),(_A,_G),(_A,_H),(_A,_Q),(_A,_I)))
if mibBuilder.loadTexts:cpqMe2FallingAlarm.setStatus('')
cpqMeRisingAlarmExtended=NotificationType((1,3,6,1,4,1,232,0,10005))
cpqMeRisingAlarmExtended.setObjects(*((_L,_M),(_J,_K),(_A,_F),(_A,_G),(_A,_H),(_A,_P),(_A,_I),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:cpqMeRisingAlarmExtended.setStatus('')
cpqMeFallingAlarmExtended=NotificationType((1,3,6,1,4,1,232,0,10006))
cpqMeFallingAlarmExtended.setObjects(*((_L,_M),(_J,_K),(_A,_F),(_A,_G),(_A,_H),(_A,_Q),(_A,_I),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:cpqMeFallingAlarmExtended.setStatus('')
cpqMeCriticalRisingAlarmExtended=NotificationType((1,3,6,1,4,1,232,0,10007))
cpqMeCriticalRisingAlarmExtended.setObjects(*((_L,_M),(_J,_K),(_A,_F),(_A,_G),(_A,_H),(_A,_P),(_A,_I),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:cpqMeCriticalRisingAlarmExtended.setStatus('')
cpqMeCriticalFallingAlarmExtended=NotificationType((1,3,6,1,4,1,232,0,10008))
cpqMeCriticalFallingAlarmExtended.setObjects(*((_L,_M),(_J,_K),(_A,_F),(_A,_G),(_A,_H),(_A,_Q),(_A,_I),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:cpqMeCriticalFallingAlarmExtended.setStatus('')
mibBuilder.exportSymbols(_A,**{'cpqMeRisingAlarm':cpqMeRisingAlarm,'cpqMeFallingAlarm':cpqMeFallingAlarm,'cpqMe2RisingAlarm':cpqMe2RisingAlarm,'cpqMe2FallingAlarm':cpqMe2FallingAlarm,'cpqMeRisingAlarmExtended':cpqMeRisingAlarmExtended,'cpqMeFallingAlarmExtended':cpqMeFallingAlarmExtended,'cpqMeCriticalRisingAlarmExtended':cpqMeCriticalRisingAlarmExtended,'cpqMeCriticalFallingAlarmExtended':cpqMeCriticalFallingAlarmExtended,'cpqThresholdMgmt':cpqThresholdMgmt,'cpqMeMibRev':cpqMeMibRev,'cpqMeMibRevMajor':cpqMeMibRevMajor,'cpqMeMibRevMinor':cpqMeMibRevMinor,'cpqMeMibCondition':cpqMeMibCondition,'cpqMeComponent':cpqMeComponent,'cpqMeInterface':cpqMeInterface,'cpqMeOsCommon':cpqMeOsCommon,'cpqMeOsCommonPollFreq':cpqMeOsCommonPollFreq,'cpqMeOsCommonModuleTable':cpqMeOsCommonModuleTable,'cpqMeOsCommonModuleEntry':cpqMeOsCommonModuleEntry,_V:cpqMeOsCommonModuleIndex,'cpqMeOsCommonModuleName':cpqMeOsCommonModuleName,'cpqMeOsCommonModuleVersion':cpqMeOsCommonModuleVersion,'cpqMeOsCommonModuleDate':cpqMeOsCommonModuleDate,'cpqMeOsCommonModulePurpose':cpqMeOsCommonModulePurpose,'cpqMeAlarm':cpqMeAlarm,'cpqMeAlarmNextIndex':cpqMeAlarmNextIndex,'cpqMeAlarmTable':cpqMeAlarmTable,'cpqMeAlarmEntry':cpqMeAlarmEntry,_W:cpqMeAlarmIndex,'cpqMeAlarmInterval':cpqMeAlarmInterval,_F:cpqMeAlarmVariable,_G:cpqMeAlarmSampleType,_H:cpqMeAlarmValue,'cpqMeAlarmStartupAlarm':cpqMeAlarmStartupAlarm,_P:cpqMeAlarmRisingThreshold,_Q:cpqMeAlarmFallingThreshold,'cpqMeAlarmPermanence':cpqMeAlarmPermanence,_I:cpqMeAlarmOwner,'cpqMeAlarmStatus':cpqMeAlarmStatus,_R:cpqMeAlarmSeverity,_S:cpqMeAlarmExtendedDescription})