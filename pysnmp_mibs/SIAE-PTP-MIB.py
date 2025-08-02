_b='ptpRadioBrIndex'
_a='PtpClockToDFormatType'
_Z='ClockPPSInstanceType'
_Y='ptpClockPPSInstanceIndex'
_X='ClockMechanismType'
_W='ClockTimeSourceType'
_V='ClockQualityAccuracyType'
_U='ClockQualityClassType'
_T='ClockInstanceType'
_S='passive'
_R='master'
_Q='ptpPortIndex'
_P='up'
_O='down'
_N='DisplayString'
_M='Unsigned32'
_L='TruthValue'
_K='OctetString'
_J='AlarmSeverityCode'
_I='ptpClockInstanceIndex'
_H='ptpClockTypeIndex'
_G='ptpClockDomainIndex'
_F='read-create'
_E='read-write'
_D='Integer32'
_C='SIAE-PTP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
AlarmSeverityCode,AlarmStatus=mibBuilder.importSymbols('SIAE-ALARM-MIB',_J,'AlarmStatus')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','RowStatus','TextualConvention',_L)
ptp=ModuleIdentity((1,3,6,1,4,1,3373,1103,100))
class ClockDomainType(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(24,43))
class ClockProfileType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('default',1),('telecom',2),('vendorspecific',3)))
class ClockQualityAccuracyType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,254,255)));namedValues=NamedValues(*(('reserved00',1),('nanoSecond25',32),('nanoSecond100',33),('nanoSecond250',34),('microSec1',35),('microSec2dot5',36),('microSec10',37),('microSec25',38),('microSec100',39),('microSec250',40),('milliSec1',41),('milliSec2dot5',42),('milliSec10',43),('milliSec25',44),('milliSec100',45),('milliSec250',46),('second1',47),('second10',48),('secondGreater10',49),('unknown',254),('reserved255',255)))
class ClockQualityClassType(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class ClockStateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('freerun',1),('acquiring',2),('locked',3),('holdoverInSpec',4),('holdoverOutOfSpec',5)))
class ClockTimeSourceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,32,48,64,80,96,144,160,255)));namedValues=NamedValues(*(('atomicClock',16),('gps',32),('terrestrialRadio',48),('ptp',64),('ntp',80),('handSet',96),('other',144),('internalOscillator',160),('reserved',255)))
class ClockInstanceType(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class ClockPPSInstanceType(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class ClockPortNumber(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class ClockPortState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('initializing',1),('faulty',2),('disabled',3),('listening',4),('preMaster',5),(_R,6),(_S,7),('uncalibrated',8),('slave',9)))
class ClockMechanismType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('e2e',1))
class ClockTimeInterval(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class ClockType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('boundaryClock',2))
class PtpClockToDFormatType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('telecomTimeEvent',1),('telecomTimeAnnounce',2),('telecomGNSSstatus',3),('nmeazda',4),('iso8601',5),('ntp',6),('ublox',7),('chinaMobile',8),('chinaTelecom',9),('bcm',10),('bcmts',11)))
class _PtpMibVersion_Type(Integer32):defaultValue=1
_PtpMibVersion_Type.__name__=_D
_PtpMibVersion_Object=MibScalar
ptpMibVersion=_PtpMibVersion_Object((1,3,6,1,4,1,3373,1103,100,1),_PtpMibVersion_Type())
ptpMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpMibVersion.setStatus(_A)
_PtpProfileDataSet_ObjectIdentity=ObjectIdentity
ptpProfileDataSet=_PtpProfileDataSet_ObjectIdentity((1,3,6,1,4,1,3373,1103,100,2))
_PtpSystemProfile_Type=ClockProfileType
_PtpSystemProfile_Object=MibScalar
ptpSystemProfile=_PtpSystemProfile_Object((1,3,6,1,4,1,3373,1103,100,2,1),_PtpSystemProfile_Type())
ptpSystemProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpSystemProfile.setStatus(_A)
class _PtpProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_PtpProfileName_Type.__name__=_N
_PtpProfileName_Object=MibScalar
ptpProfileName=_PtpProfileName_Object((1,3,6,1,4,1,3373,1103,100,2,2),_PtpProfileName_Type())
ptpProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpProfileName.setStatus(_A)
class _PtpProfilePrimaryVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PtpProfilePrimaryVersion_Type.__name__=_D
_PtpProfilePrimaryVersion_Object=MibScalar
ptpProfilePrimaryVersion=_PtpProfilePrimaryVersion_Object((1,3,6,1,4,1,3373,1103,100,2,3),_PtpProfilePrimaryVersion_Type())
ptpProfilePrimaryVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpProfilePrimaryVersion.setStatus(_A)
class _PtpProfileRevisionNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PtpProfileRevisionNumber_Type.__name__=_D
_PtpProfileRevisionNumber_Object=MibScalar
ptpProfileRevisionNumber=_PtpProfileRevisionNumber_Object((1,3,6,1,4,1,3373,1103,100,2,4),_PtpProfileRevisionNumber_Type())
ptpProfileRevisionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpProfileRevisionNumber.setStatus(_A)
class _PtpProfileIdentifier_Type(OctetString):defaultHexValue='0019A7010100';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_PtpProfileIdentifier_Type.__name__=_K
_PtpProfileIdentifier_Object=MibScalar
ptpProfileIdentifier=_PtpProfileIdentifier_Object((1,3,6,1,4,1,3373,1103,100,2,5),_PtpProfileIdentifier_Type())
ptpProfileIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpProfileIdentifier.setStatus(_A)
_PtpSpecificDataSet_ObjectIdentity=ObjectIdentity
ptpSpecificDataSet=_PtpSpecificDataSet_ObjectIdentity((1,3,6,1,4,1,3373,1103,100,3))
_PtpSpecificDataSetTable_Object=MibTable
ptpSpecificDataSetTable=_PtpSpecificDataSetTable_Object((1,3,6,1,4,1,3373,1103,100,3,1))
if mibBuilder.loadTexts:ptpSpecificDataSetTable.setStatus(_A)
_PtpSpecificDataSetEntry_Object=MibTableRow
ptpSpecificDataSetEntry=_PtpSpecificDataSetEntry_Object((1,3,6,1,4,1,3373,1103,100,3,1,1))
ptpSpecificDataSetEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:ptpSpecificDataSetEntry.setStatus(_A)
class _PtpAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_PtpAdminStatus_Type.__name__=_D
_PtpAdminStatus_Object=MibTableColumn
ptpAdminStatus=_PtpAdminStatus_Object((1,3,6,1,4,1,3373,1103,100,3,1,1,1),_PtpAdminStatus_Type())
ptpAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpAdminStatus.setStatus(_A)
class _PtpStaticPortRole_Type(TruthValue):defaultValue=2
_PtpStaticPortRole_Type.__name__=_L
_PtpStaticPortRole_Object=MibTableColumn
ptpStaticPortRole=_PtpStaticPortRole_Object((1,3,6,1,4,1,3373,1103,100,3,1,1,2),_PtpStaticPortRole_Type())
ptpStaticPortRole.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpStaticPortRole.setStatus(_A)
_PtpClockState_Type=ClockStateType
_PtpClockState_Object=MibTableColumn
ptpClockState=_PtpClockState_Object((1,3,6,1,4,1,3373,1103,100,3,1,1,3),_PtpClockState_Type())
ptpClockState.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpClockState.setStatus(_A)
class _PtpCompliance_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strictCompatibility',1),('looseCompatibility',2)))
_PtpCompliance_Type.__name__=_D
_PtpCompliance_Object=MibTableColumn
ptpCompliance=_PtpCompliance_Object((1,3,6,1,4,1,3373,1103,100,3,1,1,4),_PtpCompliance_Type())
ptpCompliance.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpCompliance.setStatus(_A)
_PtpSpecificAlarmTable_Object=MibTable
ptpSpecificAlarmTable=_PtpSpecificAlarmTable_Object((1,3,6,1,4,1,3373,1103,100,3,2))
if mibBuilder.loadTexts:ptpSpecificAlarmTable.setStatus(_A)
_PtpSpecificAlarmEntry_Object=MibTableRow
ptpSpecificAlarmEntry=_PtpSpecificAlarmEntry_Object((1,3,6,1,4,1,3373,1103,100,3,2,1))
ptpSpecificAlarmEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:ptpSpecificAlarmEntry.setStatus(_A)
_PtpFreeRunningAlarm_Type=AlarmStatus
_PtpFreeRunningAlarm_Object=MibTableColumn
ptpFreeRunningAlarm=_PtpFreeRunningAlarm_Object((1,3,6,1,4,1,3373,1103,100,3,2,1,1),_PtpFreeRunningAlarm_Type())
ptpFreeRunningAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpFreeRunningAlarm.setStatus(_A)
_PtpHoldoverInSpecAlarm_Type=AlarmStatus
_PtpHoldoverInSpecAlarm_Object=MibTableColumn
ptpHoldoverInSpecAlarm=_PtpHoldoverInSpecAlarm_Object((1,3,6,1,4,1,3373,1103,100,3,2,1,2),_PtpHoldoverInSpecAlarm_Type())
ptpHoldoverInSpecAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpHoldoverInSpecAlarm.setStatus(_A)
_PtpHoldoverOutOfSpecAlarm_Type=AlarmStatus
_PtpHoldoverOutOfSpecAlarm_Object=MibTableColumn
ptpHoldoverOutOfSpecAlarm=_PtpHoldoverOutOfSpecAlarm_Object((1,3,6,1,4,1,3373,1103,100,3,2,1,3),_PtpHoldoverOutOfSpecAlarm_Type())
ptpHoldoverOutOfSpecAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpHoldoverOutOfSpecAlarm.setStatus(_A)
class _PtpFreeRunningAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=3
_PtpFreeRunningAlarmSeverityCode_Type.__name__=_J
_PtpFreeRunningAlarmSeverityCode_Object=MibScalar
ptpFreeRunningAlarmSeverityCode=_PtpFreeRunningAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,100,3,3),_PtpFreeRunningAlarmSeverityCode_Type())
ptpFreeRunningAlarmSeverityCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpFreeRunningAlarmSeverityCode.setStatus(_A)
class _PtpHoldoverInSpecAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=3
_PtpHoldoverInSpecAlarmSeverityCode_Type.__name__=_J
_PtpHoldoverInSpecAlarmSeverityCode_Object=MibScalar
ptpHoldoverInSpecAlarmSeverityCode=_PtpHoldoverInSpecAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,100,3,4),_PtpHoldoverInSpecAlarmSeverityCode_Type())
ptpHoldoverInSpecAlarmSeverityCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpHoldoverInSpecAlarmSeverityCode.setStatus(_A)
class _PtpHoldoverOutOfSpecAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_PtpHoldoverOutOfSpecAlarmSeverityCode_Type.__name__=_J
_PtpHoldoverOutOfSpecAlarmSeverityCode_Object=MibScalar
ptpHoldoverOutOfSpecAlarmSeverityCode=_PtpHoldoverOutOfSpecAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,100,3,5),_PtpHoldoverOutOfSpecAlarmSeverityCode_Type())
ptpHoldoverOutOfSpecAlarmSeverityCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpHoldoverOutOfSpecAlarmSeverityCode.setStatus(_A)
_PtpDefaultDataSet_ObjectIdentity=ObjectIdentity
ptpDefaultDataSet=_PtpDefaultDataSet_ObjectIdentity((1,3,6,1,4,1,3373,1103,100,4))
_PtpClockDataSetTable_Object=MibTable
ptpClockDataSetTable=_PtpClockDataSetTable_Object((1,3,6,1,4,1,3373,1103,100,4,1))
if mibBuilder.loadTexts:ptpClockDataSetTable.setStatus(_A)
_PtpClockDataSetEntry_Object=MibTableRow
ptpClockDataSetEntry=_PtpClockDataSetEntry_Object((1,3,6,1,4,1,3373,1103,100,4,1,1))
ptpClockDataSetEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:ptpClockDataSetEntry.setStatus(_A)
_PtpClockDomainIndex_Type=ClockDomainType
_PtpClockDomainIndex_Object=MibTableColumn
ptpClockDomainIndex=_PtpClockDomainIndex_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,1),_PtpClockDomainIndex_Type())
ptpClockDomainIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpClockDomainIndex.setStatus(_A)
_PtpClockTypeIndex_Type=ClockType
_PtpClockTypeIndex_Object=MibTableColumn
ptpClockTypeIndex=_PtpClockTypeIndex_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,2),_PtpClockTypeIndex_Type())
ptpClockTypeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpClockTypeIndex.setStatus(_A)
class _PtpClockInstanceIndex_Type(ClockInstanceType):subtypeSpec=ClockInstanceType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PtpClockInstanceIndex_Type.__name__=_T
_PtpClockInstanceIndex_Object=MibTableColumn
ptpClockInstanceIndex=_PtpClockInstanceIndex_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,3),_PtpClockInstanceIndex_Type())
ptpClockInstanceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpClockInstanceIndex.setStatus(_A)
class _PtpClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PtpClockIdentity_Type.__name__=_K
_PtpClockIdentity_Object=MibTableColumn
ptpClockIdentity=_PtpClockIdentity_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,4),_PtpClockIdentity_Type())
ptpClockIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpClockIdentity.setStatus(_A)
class _PtpClockTwoStepFlag_Type(TruthValue):defaultValue=2
_PtpClockTwoStepFlag_Type.__name__=_L
_PtpClockTwoStepFlag_Object=MibTableColumn
ptpClockTwoStepFlag=_PtpClockTwoStepFlag_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,5),_PtpClockTwoStepFlag_Type())
ptpClockTwoStepFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpClockTwoStepFlag.setStatus(_A)
class _PtpClockNumberPorts_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_PtpClockNumberPorts_Type.__name__=_D
_PtpClockNumberPorts_Object=MibTableColumn
ptpClockNumberPorts=_PtpClockNumberPorts_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,6),_PtpClockNumberPorts_Type())
ptpClockNumberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpClockNumberPorts.setStatus(_A)
class _PtpClockClass_Type(ClockQualityClassType):defaultValue=248
_PtpClockClass_Type.__name__=_U
_PtpClockClass_Object=MibTableColumn
ptpClockClass=_PtpClockClass_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,7),_PtpClockClass_Type())
ptpClockClass.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpClockClass.setStatus(_A)
class _PtpClockAccuracy_Type(ClockQualityAccuracyType):defaultValue=254
_PtpClockAccuracy_Type.__name__=_V
_PtpClockAccuracy_Object=MibTableColumn
ptpClockAccuracy=_PtpClockAccuracy_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,8),_PtpClockAccuracy_Type())
ptpClockAccuracy.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpClockAccuracy.setStatus(_A)
class _PtpClockOffsetScaledLogVariance_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PtpClockOffsetScaledLogVariance_Type.__name__=_D
_PtpClockOffsetScaledLogVariance_Object=MibTableColumn
ptpClockOffsetScaledLogVariance=_PtpClockOffsetScaledLogVariance_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,9),_PtpClockOffsetScaledLogVariance_Type())
ptpClockOffsetScaledLogVariance.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpClockOffsetScaledLogVariance.setStatus(_A)
class _PtpClockPriority1_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(128,128))
_PtpClockPriority1_Type.__name__=_D
_PtpClockPriority1_Object=MibTableColumn
ptpClockPriority1=_PtpClockPriority1_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,10),_PtpClockPriority1_Type())
ptpClockPriority1.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpClockPriority1.setStatus(_A)
class _PtpClockPriority2_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PtpClockPriority2_Type.__name__=_D
_PtpClockPriority2_Object=MibTableColumn
ptpClockPriority2=_PtpClockPriority2_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,11),_PtpClockPriority2_Type())
ptpClockPriority2.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpClockPriority2.setStatus(_A)
class _PtpClockSlaveOnly_Type(TruthValue):defaultValue=2
_PtpClockSlaveOnly_Type.__name__=_L
_PtpClockSlaveOnly_Object=MibTableColumn
ptpClockSlaveOnly=_PtpClockSlaveOnly_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,12),_PtpClockSlaveOnly_Type())
ptpClockSlaveOnly.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpClockSlaveOnly.setStatus(_A)
class _PtpClockLocalPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PtpClockLocalPriority_Type.__name__=_D
_PtpClockLocalPriority_Object=MibTableColumn
ptpClockLocalPriority=_PtpClockLocalPriority_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,13),_PtpClockLocalPriority_Type())
ptpClockLocalPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpClockLocalPriority.setStatus(_A)
_PtpClockRowStatus_Type=RowStatus
_PtpClockRowStatus_Object=MibTableColumn
ptpClockRowStatus=_PtpClockRowStatus_Object((1,3,6,1,4,1,3373,1103,100,4,1,1,14),_PtpClockRowStatus_Type())
ptpClockRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpClockRowStatus.setStatus(_A)
_PtpCurrentDataSet_ObjectIdentity=ObjectIdentity
ptpCurrentDataSet=_PtpCurrentDataSet_ObjectIdentity((1,3,6,1,4,1,3373,1103,100,5))
_PtpCurrentDataSetTable_Object=MibTable
ptpCurrentDataSetTable=_PtpCurrentDataSetTable_Object((1,3,6,1,4,1,3373,1103,100,5,1))
if mibBuilder.loadTexts:ptpCurrentDataSetTable.setStatus(_A)
_PtpCurrentDataSetEntry_Object=MibTableRow
ptpCurrentDataSetEntry=_PtpCurrentDataSetEntry_Object((1,3,6,1,4,1,3373,1103,100,5,1,1))
ptpCurrentDataSetEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:ptpCurrentDataSetEntry.setStatus(_A)
_PtpCurrentStepsRemoved_Type=Integer32
_PtpCurrentStepsRemoved_Object=MibTableColumn
ptpCurrentStepsRemoved=_PtpCurrentStepsRemoved_Object((1,3,6,1,4,1,3373,1103,100,5,1,1,1),_PtpCurrentStepsRemoved_Type())
ptpCurrentStepsRemoved.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpCurrentStepsRemoved.setStatus(_A)
_PtpCurrentOffsetFromMaster_Type=ClockTimeInterval
_PtpCurrentOffsetFromMaster_Object=MibTableColumn
ptpCurrentOffsetFromMaster=_PtpCurrentOffsetFromMaster_Object((1,3,6,1,4,1,3373,1103,100,5,1,1,2),_PtpCurrentOffsetFromMaster_Type())
ptpCurrentOffsetFromMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpCurrentOffsetFromMaster.setStatus(_A)
_PtpCurrentMeanPathDelay_Type=ClockTimeInterval
_PtpCurrentMeanPathDelay_Object=MibTableColumn
ptpCurrentMeanPathDelay=_PtpCurrentMeanPathDelay_Object((1,3,6,1,4,1,3373,1103,100,5,1,1,3),_PtpCurrentMeanPathDelay_Type())
ptpCurrentMeanPathDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpCurrentMeanPathDelay.setStatus(_A)
_PtpParentDataSet_ObjectIdentity=ObjectIdentity
ptpParentDataSet=_PtpParentDataSet_ObjectIdentity((1,3,6,1,4,1,3373,1103,100,6))
_PtpParentDataSetTable_Object=MibTable
ptpParentDataSetTable=_PtpParentDataSetTable_Object((1,3,6,1,4,1,3373,1103,100,6,1))
if mibBuilder.loadTexts:ptpParentDataSetTable.setStatus(_A)
_PtpParentDataSetEntry_Object=MibTableRow
ptpParentDataSetEntry=_PtpParentDataSetEntry_Object((1,3,6,1,4,1,3373,1103,100,6,1,1))
ptpParentDataSetEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:ptpParentDataSetEntry.setStatus(_A)
class _PtpParentClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PtpParentClockIdentity_Type.__name__=_K
_PtpParentClockIdentity_Object=MibTableColumn
ptpParentClockIdentity=_PtpParentClockIdentity_Object((1,3,6,1,4,1,3373,1103,100,6,1,1,1),_PtpParentClockIdentity_Type())
ptpParentClockIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpParentClockIdentity.setStatus(_A)
_PtpParentPortNumber_Type=ClockPortNumber
_PtpParentPortNumber_Object=MibTableColumn
ptpParentPortNumber=_PtpParentPortNumber_Object((1,3,6,1,4,1,3373,1103,100,6,1,1,2),_PtpParentPortNumber_Type())
ptpParentPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpParentPortNumber.setStatus(_A)
class _PtpParentGMClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PtpParentGMClockIdentity_Type.__name__=_K
_PtpParentGMClockIdentity_Object=MibTableColumn
ptpParentGMClockIdentity=_PtpParentGMClockIdentity_Object((1,3,6,1,4,1,3373,1103,100,6,1,1,3),_PtpParentGMClockIdentity_Type())
ptpParentGMClockIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpParentGMClockIdentity.setStatus(_A)
_PtpParentGMClockClass_Type=ClockQualityClassType
_PtpParentGMClockClass_Object=MibTableColumn
ptpParentGMClockClass=_PtpParentGMClockClass_Object((1,3,6,1,4,1,3373,1103,100,6,1,1,4),_PtpParentGMClockClass_Type())
ptpParentGMClockClass.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpParentGMClockClass.setStatus(_A)
_PtpParentGMClockAccuracy_Type=ClockQualityAccuracyType
_PtpParentGMClockAccuracy_Object=MibTableColumn
ptpParentGMClockAccuracy=_PtpParentGMClockAccuracy_Object((1,3,6,1,4,1,3373,1103,100,6,1,1,5),_PtpParentGMClockAccuracy_Type())
ptpParentGMClockAccuracy.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpParentGMClockAccuracy.setStatus(_A)
class _PtpParentGMClockOffsetScaledLogVariance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PtpParentGMClockOffsetScaledLogVariance_Type.__name__=_D
_PtpParentGMClockOffsetScaledLogVariance_Object=MibTableColumn
ptpParentGMClockOffsetScaledLogVariance=_PtpParentGMClockOffsetScaledLogVariance_Object((1,3,6,1,4,1,3373,1103,100,6,1,1,6),_PtpParentGMClockOffsetScaledLogVariance_Type())
ptpParentGMClockOffsetScaledLogVariance.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpParentGMClockOffsetScaledLogVariance.setStatus(_A)
class _PtpParentGMPriority1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PtpParentGMPriority1_Type.__name__=_D
_PtpParentGMPriority1_Object=MibTableColumn
ptpParentGMPriority1=_PtpParentGMPriority1_Object((1,3,6,1,4,1,3373,1103,100,6,1,1,7),_PtpParentGMPriority1_Type())
ptpParentGMPriority1.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpParentGMPriority1.setStatus(_A)
class _PtpParentGMPriority2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PtpParentGMPriority2_Type.__name__=_D
_PtpParentGMPriority2_Object=MibTableColumn
ptpParentGMPriority2=_PtpParentGMPriority2_Object((1,3,6,1,4,1,3373,1103,100,6,1,1,8),_PtpParentGMPriority2_Type())
ptpParentGMPriority2.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpParentGMPriority2.setStatus(_A)
_PtpTimePropertiesDataSet_ObjectIdentity=ObjectIdentity
ptpTimePropertiesDataSet=_PtpTimePropertiesDataSet_ObjectIdentity((1,3,6,1,4,1,3373,1103,100,7))
_PtpTimeDataSetTable_Object=MibTable
ptpTimeDataSetTable=_PtpTimeDataSetTable_Object((1,3,6,1,4,1,3373,1103,100,7,1))
if mibBuilder.loadTexts:ptpTimeDataSetTable.setStatus(_A)
_PtpTimeDataSetEntry_Object=MibTableRow
ptpTimeDataSetEntry=_PtpTimeDataSetEntry_Object((1,3,6,1,4,1,3373,1103,100,7,1,1))
ptpTimeDataSetEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:ptpTimeDataSetEntry.setStatus(_A)
class _PtpTimeCurrentUTCOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PtpTimeCurrentUTCOffset_Type.__name__=_D
_PtpTimeCurrentUTCOffset_Object=MibTableColumn
ptpTimeCurrentUTCOffset=_PtpTimeCurrentUTCOffset_Object((1,3,6,1,4,1,3373,1103,100,7,1,1,1),_PtpTimeCurrentUTCOffset_Type())
ptpTimeCurrentUTCOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpTimeCurrentUTCOffset.setStatus(_A)
_PtpTimeCurrentUTCOffsetValid_Type=TruthValue
_PtpTimeCurrentUTCOffsetValid_Object=MibTableColumn
ptpTimeCurrentUTCOffsetValid=_PtpTimeCurrentUTCOffsetValid_Object((1,3,6,1,4,1,3373,1103,100,7,1,1,2),_PtpTimeCurrentUTCOffsetValid_Type())
ptpTimeCurrentUTCOffsetValid.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpTimeCurrentUTCOffsetValid.setStatus(_A)
_PtpTimeLeap59_Type=TruthValue
_PtpTimeLeap59_Object=MibTableColumn
ptpTimeLeap59=_PtpTimeLeap59_Object((1,3,6,1,4,1,3373,1103,100,7,1,1,3),_PtpTimeLeap59_Type())
ptpTimeLeap59.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpTimeLeap59.setStatus(_A)
_PtpTimeLeap61_Type=TruthValue
_PtpTimeLeap61_Object=MibTableColumn
ptpTimeLeap61=_PtpTimeLeap61_Object((1,3,6,1,4,1,3373,1103,100,7,1,1,4),_PtpTimeLeap61_Type())
ptpTimeLeap61.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpTimeLeap61.setStatus(_A)
_PtpTimeTimeTraceable_Type=TruthValue
_PtpTimeTimeTraceable_Object=MibTableColumn
ptpTimeTimeTraceable=_PtpTimeTimeTraceable_Object((1,3,6,1,4,1,3373,1103,100,7,1,1,5),_PtpTimeTimeTraceable_Type())
ptpTimeTimeTraceable.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpTimeTimeTraceable.setStatus(_A)
_PtpTimeFrequencyTraceable_Type=TruthValue
_PtpTimeFrequencyTraceable_Object=MibTableColumn
ptpTimeFrequencyTraceable=_PtpTimeFrequencyTraceable_Object((1,3,6,1,4,1,3373,1103,100,7,1,1,6),_PtpTimeFrequencyTraceable_Type())
ptpTimeFrequencyTraceable.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpTimeFrequencyTraceable.setStatus(_A)
_PtpTimescale_Type=TruthValue
_PtpTimescale_Object=MibTableColumn
ptpTimescale=_PtpTimescale_Object((1,3,6,1,4,1,3373,1103,100,7,1,1,7),_PtpTimescale_Type())
ptpTimescale.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpTimescale.setStatus(_A)
class _PtpTimeTimeSource_Type(ClockTimeSourceType):defaultValue=160
_PtpTimeTimeSource_Type.__name__=_W
_PtpTimeTimeSource_Object=MibTableColumn
ptpTimeTimeSource=_PtpTimeTimeSource_Object((1,3,6,1,4,1,3373,1103,100,7,1,1,8),_PtpTimeTimeSource_Type())
ptpTimeTimeSource.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpTimeTimeSource.setStatus(_A)
_PtpPortDataSet_ObjectIdentity=ObjectIdentity
ptpPortDataSet=_PtpPortDataSet_ObjectIdentity((1,3,6,1,4,1,3373,1103,100,8))
_PtpPortDataSetTable_Object=MibTable
ptpPortDataSetTable=_PtpPortDataSetTable_Object((1,3,6,1,4,1,3373,1103,100,8,1))
if mibBuilder.loadTexts:ptpPortDataSetTable.setStatus(_A)
_PtpPortDataSetEntry_Object=MibTableRow
ptpPortDataSetEntry=_PtpPortDataSetEntry_Object((1,3,6,1,4,1,3373,1103,100,8,1,1))
ptpPortDataSetEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I),(0,_C,_Q))
if mibBuilder.loadTexts:ptpPortDataSetEntry.setStatus(_A)
_PtpPortIndex_Type=ClockPortNumber
_PtpPortIndex_Object=MibTableColumn
ptpPortIndex=_PtpPortIndex_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,1),_PtpPortIndex_Type())
ptpPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpPortIndex.setStatus(_A)
class _PtpPortClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PtpPortClockIdentity_Type.__name__=_K
_PtpPortClockIdentity_Object=MibTableColumn
ptpPortClockIdentity=_PtpPortClockIdentity_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,2),_PtpPortClockIdentity_Type())
ptpPortClockIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpPortClockIdentity.setStatus(_A)
_PtpPortIfIndex_Type=InterfaceIndex
_PtpPortIfIndex_Object=MibTableColumn
ptpPortIfIndex=_PtpPortIfIndex_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,3),_PtpPortIfIndex_Type())
ptpPortIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpPortIfIndex.setStatus(_A)
class _PtpPortStaticRole_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,7,9)));namedValues=NamedValues(*((_R,6),(_S,7),('slave',9)))
_PtpPortStaticRole_Type.__name__=_D
_PtpPortStaticRole_Object=MibTableColumn
ptpPortStaticRole=_PtpPortStaticRole_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,4),_PtpPortStaticRole_Type())
ptpPortStaticRole.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpPortStaticRole.setStatus(_A)
class _PtpPortAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_PtpPortAdminStatus_Type.__name__=_D
_PtpPortAdminStatus_Object=MibTableColumn
ptpPortAdminStatus=_PtpPortAdminStatus_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,5),_PtpPortAdminStatus_Type())
ptpPortAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpPortAdminStatus.setStatus(_A)
_PtpPortState_Type=ClockPortState
_PtpPortState_Object=MibTableColumn
ptpPortState=_PtpPortState_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,6),_PtpPortState_Type())
ptpPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpPortState.setStatus(_A)
class _PtpPortMinDelayReqInterval_Type(Integer32):defaultValue=-4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-7,7))
_PtpPortMinDelayReqInterval_Type.__name__=_D
_PtpPortMinDelayReqInterval_Object=MibTableColumn
ptpPortMinDelayReqInterval=_PtpPortMinDelayReqInterval_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,7),_PtpPortMinDelayReqInterval_Type())
ptpPortMinDelayReqInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpPortMinDelayReqInterval.setStatus(_A)
class _PtpPortLogAnnounceInterval_Type(Integer32):defaultValue=-3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-3,6))
_PtpPortLogAnnounceInterval_Type.__name__=_D
_PtpPortLogAnnounceInterval_Object=MibTableColumn
ptpPortLogAnnounceInterval=_PtpPortLogAnnounceInterval_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,8),_PtpPortLogAnnounceInterval_Type())
ptpPortLogAnnounceInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpPortLogAnnounceInterval.setStatus(_A)
class _PtpPortAnnounceReceiptTimeout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,10))
_PtpPortAnnounceReceiptTimeout_Type.__name__=_D
_PtpPortAnnounceReceiptTimeout_Object=MibTableColumn
ptpPortAnnounceReceiptTimeout=_PtpPortAnnounceReceiptTimeout_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,9),_PtpPortAnnounceReceiptTimeout_Type())
ptpPortAnnounceReceiptTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpPortAnnounceReceiptTimeout.setStatus(_A)
class _PtpPortSyncInterval_Type(Integer32):defaultValue=-4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-7,0))
_PtpPortSyncInterval_Type.__name__=_D
_PtpPortSyncInterval_Object=MibTableColumn
ptpPortSyncInterval=_PtpPortSyncInterval_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,10),_PtpPortSyncInterval_Type())
ptpPortSyncInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpPortSyncInterval.setStatus(_A)
class _PtpPortDelayMechanism_Type(ClockMechanismType):defaultValue=1
_PtpPortDelayMechanism_Type.__name__=_X
_PtpPortDelayMechanism_Object=MibTableColumn
ptpPortDelayMechanism=_PtpPortDelayMechanism_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,11),_PtpPortDelayMechanism_Type())
ptpPortDelayMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpPortDelayMechanism.setStatus(_A)
class _PtpPortVersionNumber_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,2))
_PtpPortVersionNumber_Type.__name__=_D
_PtpPortVersionNumber_Object=MibTableColumn
ptpPortVersionNumber=_PtpPortVersionNumber_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,12),_PtpPortVersionNumber_Type())
ptpPortVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpPortVersionNumber.setStatus(_A)
class _PtpPortNotSlave_Type(TruthValue):defaultValue=1
_PtpPortNotSlave_Type.__name__=_L
_PtpPortNotSlave_Object=MibTableColumn
ptpPortNotSlave=_PtpPortNotSlave_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,13),_PtpPortNotSlave_Type())
ptpPortNotSlave.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpPortNotSlave.setStatus(_A)
class _PtpPortLocalPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PtpPortLocalPriority_Type.__name__=_D
_PtpPortLocalPriority_Object=MibTableColumn
ptpPortLocalPriority=_PtpPortLocalPriority_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,14),_PtpPortLocalPriority_Type())
ptpPortLocalPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpPortLocalPriority.setStatus(_A)
class _PtpPortDestMacAddress_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwardable',1),('nonForwardable',2)))
_PtpPortDestMacAddress_Type.__name__=_D
_PtpPortDestMacAddress_Object=MibTableColumn
ptpPortDestMacAddress=_PtpPortDestMacAddress_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,15),_PtpPortDestMacAddress_Type())
ptpPortDestMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpPortDestMacAddress.setStatus(_A)
class _PtpPortTxAsymmetryCompensation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_PtpPortTxAsymmetryCompensation_Type.__name__=_D
_PtpPortTxAsymmetryCompensation_Object=MibTableColumn
ptpPortTxAsymmetryCompensation=_PtpPortTxAsymmetryCompensation_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,16),_PtpPortTxAsymmetryCompensation_Type())
ptpPortTxAsymmetryCompensation.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpPortTxAsymmetryCompensation.setStatus(_A)
class _PtpPortRxAsymmetryCompensation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_PtpPortRxAsymmetryCompensation_Type.__name__=_D
_PtpPortRxAsymmetryCompensation_Object=MibTableColumn
ptpPortRxAsymmetryCompensation=_PtpPortRxAsymmetryCompensation_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,17),_PtpPortRxAsymmetryCompensation_Type())
ptpPortRxAsymmetryCompensation.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpPortRxAsymmetryCompensation.setStatus(_A)
_PtpPortRowStatus_Type=RowStatus
_PtpPortRowStatus_Object=MibTableColumn
ptpPortRowStatus=_PtpPortRowStatus_Object((1,3,6,1,4,1,3373,1103,100,8,1,1,18),_PtpPortRowStatus_Type())
ptpPortRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ptpPortRowStatus.setStatus(_A)
_PtpPortAlarmTable_Object=MibTable
ptpPortAlarmTable=_PtpPortAlarmTable_Object((1,3,6,1,4,1,3373,1103,100,8,2))
if mibBuilder.loadTexts:ptpPortAlarmTable.setStatus(_A)
_PtpPortAlarmEntry_Object=MibTableRow
ptpPortAlarmEntry=_PtpPortAlarmEntry_Object((1,3,6,1,4,1,3373,1103,100,8,2,1))
ptpPortAlarmEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I),(0,_C,_Q))
if mibBuilder.loadTexts:ptpPortAlarmEntry.setStatus(_A)
_PtpPortFaultyAlarm_Type=AlarmStatus
_PtpPortFaultyAlarm_Object=MibTableColumn
ptpPortFaultyAlarm=_PtpPortFaultyAlarm_Object((1,3,6,1,4,1,3373,1103,100,8,2,1,1),_PtpPortFaultyAlarm_Type())
ptpPortFaultyAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpPortFaultyAlarm.setStatus(_A)
_PtpPortInitializingAlarm_Type=AlarmStatus
_PtpPortInitializingAlarm_Object=MibTableColumn
ptpPortInitializingAlarm=_PtpPortInitializingAlarm_Object((1,3,6,1,4,1,3373,1103,100,8,2,1,2),_PtpPortInitializingAlarm_Type())
ptpPortInitializingAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpPortInitializingAlarm.setStatus(_A)
_PtpPortUncalibratedAlarm_Type=AlarmStatus
_PtpPortUncalibratedAlarm_Object=MibTableColumn
ptpPortUncalibratedAlarm=_PtpPortUncalibratedAlarm_Object((1,3,6,1,4,1,3373,1103,100,8,2,1,3),_PtpPortUncalibratedAlarm_Type())
ptpPortUncalibratedAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpPortUncalibratedAlarm.setStatus(_A)
_PtpPortListeningAlarm_Type=AlarmStatus
_PtpPortListeningAlarm_Object=MibTableColumn
ptpPortListeningAlarm=_PtpPortListeningAlarm_Object((1,3,6,1,4,1,3373,1103,100,8,2,1,4),_PtpPortListeningAlarm_Type())
ptpPortListeningAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpPortListeningAlarm.setStatus(_A)
_PtpPortActiveStatus_Type=AlarmStatus
_PtpPortActiveStatus_Object=MibTableColumn
ptpPortActiveStatus=_PtpPortActiveStatus_Object((1,3,6,1,4,1,3373,1103,100,8,2,1,5),_PtpPortActiveStatus_Type())
ptpPortActiveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpPortActiveStatus.setStatus(_A)
_PtpPortRadioAlarmTable_Object=MibTable
ptpPortRadioAlarmTable=_PtpPortRadioAlarmTable_Object((1,3,6,1,4,1,3373,1103,100,8,3))
if mibBuilder.loadTexts:ptpPortRadioAlarmTable.setStatus(_A)
_PtpPortRadioAlarmEntry_Object=MibTableRow
ptpPortRadioAlarmEntry=_PtpPortRadioAlarmEntry_Object((1,3,6,1,4,1,3373,1103,100,8,3,1))
ptpPortRadioAlarmEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I),(0,_C,_Q))
if mibBuilder.loadTexts:ptpPortRadioAlarmEntry.setStatus(_A)
_PtpPortRadioCapacityAlarm_Type=AlarmStatus
_PtpPortRadioCapacityAlarm_Object=MibTableColumn
ptpPortRadioCapacityAlarm=_PtpPortRadioCapacityAlarm_Object((1,3,6,1,4,1,3373,1103,100,8,3,1,1),_PtpPortRadioCapacityAlarm_Type())
ptpPortRadioCapacityAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpPortRadioCapacityAlarm.setStatus(_A)
class _PtpPortFaultyAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_PtpPortFaultyAlarmSeverityCode_Type.__name__=_J
_PtpPortFaultyAlarmSeverityCode_Object=MibScalar
ptpPortFaultyAlarmSeverityCode=_PtpPortFaultyAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,100,8,4),_PtpPortFaultyAlarmSeverityCode_Type())
ptpPortFaultyAlarmSeverityCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpPortFaultyAlarmSeverityCode.setStatus(_A)
class _PtpPortInitializingAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=3
_PtpPortInitializingAlarmSeverityCode_Type.__name__=_J
_PtpPortInitializingAlarmSeverityCode_Object=MibScalar
ptpPortInitializingAlarmSeverityCode=_PtpPortInitializingAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,100,8,5),_PtpPortInitializingAlarmSeverityCode_Type())
ptpPortInitializingAlarmSeverityCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpPortInitializingAlarmSeverityCode.setStatus(_A)
class _PtpPortUncalibratedAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=3
_PtpPortUncalibratedAlarmSeverityCode_Type.__name__=_J
_PtpPortUncalibratedAlarmSeverityCode_Object=MibScalar
ptpPortUncalibratedAlarmSeverityCode=_PtpPortUncalibratedAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,100,8,6),_PtpPortUncalibratedAlarmSeverityCode_Type())
ptpPortUncalibratedAlarmSeverityCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpPortUncalibratedAlarmSeverityCode.setStatus(_A)
class _PtpPortListeningAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=3
_PtpPortListeningAlarmSeverityCode_Type.__name__=_J
_PtpPortListeningAlarmSeverityCode_Object=MibScalar
ptpPortListeningAlarmSeverityCode=_PtpPortListeningAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,100,8,7),_PtpPortListeningAlarmSeverityCode_Type())
ptpPortListeningAlarmSeverityCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpPortListeningAlarmSeverityCode.setStatus(_A)
class _PtpPortActiveStatusSeverityCode_Type(AlarmSeverityCode):defaultValue=2
_PtpPortActiveStatusSeverityCode_Type.__name__=_J
_PtpPortActiveStatusSeverityCode_Object=MibScalar
ptpPortActiveStatusSeverityCode=_PtpPortActiveStatusSeverityCode_Object((1,3,6,1,4,1,3373,1103,100,8,8),_PtpPortActiveStatusSeverityCode_Type())
ptpPortActiveStatusSeverityCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpPortActiveStatusSeverityCode.setStatus(_A)
class _PtpPortRadioCapacityAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_PtpPortRadioCapacityAlarmSeverityCode_Type.__name__=_J
_PtpPortRadioCapacityAlarmSeverityCode_Object=MibScalar
ptpPortRadioCapacityAlarmSeverityCode=_PtpPortRadioCapacityAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,100,8,9),_PtpPortRadioCapacityAlarmSeverityCode_Type())
ptpPortRadioCapacityAlarmSeverityCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpPortRadioCapacityAlarmSeverityCode.setStatus(_A)
_PtpClockPPSDataSet_ObjectIdentity=ObjectIdentity
ptpClockPPSDataSet=_PtpClockPPSDataSet_ObjectIdentity((1,3,6,1,4,1,3373,1103,100,9))
_PtpClockPPSDataSetTable_Object=MibTable
ptpClockPPSDataSetTable=_PtpClockPPSDataSetTable_Object((1,3,6,1,4,1,3373,1103,100,9,1))
if mibBuilder.loadTexts:ptpClockPPSDataSetTable.setStatus(_A)
_PtpClockPPSDataSetEntry_Object=MibTableRow
ptpClockPPSDataSetEntry=_PtpClockPPSDataSetEntry_Object((1,3,6,1,4,1,3373,1103,100,9,1,1))
ptpClockPPSDataSetEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I),(0,_C,_Y))
if mibBuilder.loadTexts:ptpClockPPSDataSetEntry.setStatus(_A)
class _PtpClockPPSInstanceIndex_Type(ClockPPSInstanceType):defaultValue=0
_PtpClockPPSInstanceIndex_Type.__name__=_Z
_PtpClockPPSInstanceIndex_Object=MibTableColumn
ptpClockPPSInstanceIndex=_PtpClockPPSInstanceIndex_Object((1,3,6,1,4,1,3373,1103,100,9,1,1,1),_PtpClockPPSInstanceIndex_Type())
ptpClockPPSInstanceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpClockPPSInstanceIndex.setStatus(_A)
class _PtpClockPPSInstanceCapability_Type(Unsigned32):defaultValue=0
_PtpClockPPSInstanceCapability_Type.__name__=_M
_PtpClockPPSInstanceCapability_Object=MibTableColumn
ptpClockPPSInstanceCapability=_PtpClockPPSInstanceCapability_Object((1,3,6,1,4,1,3373,1103,100,9,1,1,2),_PtpClockPPSInstanceCapability_Type())
ptpClockPPSInstanceCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpClockPPSInstanceCapability.setStatus(_A)
class _PtpClockPPSDirection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('input',1),('output',2)))
_PtpClockPPSDirection_Type.__name__=_D
_PtpClockPPSDirection_Object=MibTableColumn
ptpClockPPSDirection=_PtpClockPPSDirection_Object((1,3,6,1,4,1,3373,1103,100,9,1,1,3),_PtpClockPPSDirection_Type())
ptpClockPPSDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpClockPPSDirection.setStatus(_A)
class _PtpClockPPSLabel_Type(DisplayString):defaultValue=OctetString('PPS');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PtpClockPPSLabel_Type.__name__=_N
_PtpClockPPSLabel_Object=MibTableColumn
ptpClockPPSLabel=_PtpClockPPSLabel_Object((1,3,6,1,4,1,3373,1103,100,9,1,1,4),_PtpClockPPSLabel_Type())
ptpClockPPSLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpClockPPSLabel.setStatus(_A)
class _PtpClockPPSAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_PtpClockPPSAdminStatus_Type.__name__=_D
_PtpClockPPSAdminStatus_Object=MibTableColumn
ptpClockPPSAdminStatus=_PtpClockPPSAdminStatus_Object((1,3,6,1,4,1,3373,1103,100,9,1,1,5),_PtpClockPPSAdminStatus_Type())
ptpClockPPSAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpClockPPSAdminStatus.setStatus(_A)
_PtpClockPPSOffsetEnabled_Type=TruthValue
_PtpClockPPSOffsetEnabled_Object=MibTableColumn
ptpClockPPSOffsetEnabled=_PtpClockPPSOffsetEnabled_Object((1,3,6,1,4,1,3373,1103,100,9,1,1,6),_PtpClockPPSOffsetEnabled_Type())
ptpClockPPSOffsetEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpClockPPSOffsetEnabled.setStatus(_A)
_PtpClockPPSOffsetValue_Type=Integer32
_PtpClockPPSOffsetValue_Object=MibTableColumn
ptpClockPPSOffsetValue=_PtpClockPPSOffsetValue_Object((1,3,6,1,4,1,3373,1103,100,9,1,1,7),_PtpClockPPSOffsetValue_Type())
ptpClockPPSOffsetValue.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpClockPPSOffsetValue.setStatus(_A)
class _PtpClockToDLabel_Type(DisplayString):defaultValue=OctetString('ToD');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PtpClockToDLabel_Type.__name__=_N
_PtpClockToDLabel_Object=MibTableColumn
ptpClockToDLabel=_PtpClockToDLabel_Object((1,3,6,1,4,1,3373,1103,100,9,1,1,8),_PtpClockToDLabel_Type())
ptpClockToDLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpClockToDLabel.setStatus(_A)
class _PtpClockToDAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_PtpClockToDAdminStatus_Type.__name__=_D
_PtpClockToDAdminStatus_Object=MibTableColumn
ptpClockToDAdminStatus=_PtpClockToDAdminStatus_Object((1,3,6,1,4,1,3373,1103,100,9,1,1,9),_PtpClockToDAdminStatus_Type())
ptpClockToDAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpClockToDAdminStatus.setStatus(_A)
class _PtpClockToDDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_PtpClockToDDelay_Type.__name__=_M
_PtpClockToDDelay_Object=MibTableColumn
ptpClockToDDelay=_PtpClockToDDelay_Object((1,3,6,1,4,1,3373,1103,100,9,1,1,10),_PtpClockToDDelay_Type())
ptpClockToDDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpClockToDDelay.setStatus(_A)
class _PtpClockToDBaudrate_Type(Unsigned32):defaultValue=9600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,300),ValueRangeConstraint(600,600),ValueRangeConstraint(1200,1200),ValueRangeConstraint(1800,1800),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200),ValueRangeConstraint(38400,38400),ValueRangeConstraint(57600,57600),ValueRangeConstraint(115200,115200),ValueRangeConstraint(230400,230400))
_PtpClockToDBaudrate_Type.__name__=_M
_PtpClockToDBaudrate_Object=MibTableColumn
ptpClockToDBaudrate=_PtpClockToDBaudrate_Object((1,3,6,1,4,1,3373,1103,100,9,1,1,11),_PtpClockToDBaudrate_Type())
ptpClockToDBaudrate.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpClockToDBaudrate.setStatus(_A)
class _PtpClockToDFormat_Type(PtpClockToDFormatType):defaultValue=1
_PtpClockToDFormat_Type.__name__=_a
_PtpClockToDFormat_Object=MibTableColumn
ptpClockToDFormat=_PtpClockToDFormat_Object((1,3,6,1,4,1,3373,1103,100,9,1,1,12),_PtpClockToDFormat_Type())
ptpClockToDFormat.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpClockToDFormat.setStatus(_A)
_PtpRadioAsymmetryDataSet_ObjectIdentity=ObjectIdentity
ptpRadioAsymmetryDataSet=_PtpRadioAsymmetryDataSet_ObjectIdentity((1,3,6,1,4,1,3373,1103,100,10))
_PtpRadioAsymmetryDataSetTable_Object=MibTable
ptpRadioAsymmetryDataSetTable=_PtpRadioAsymmetryDataSetTable_Object((1,3,6,1,4,1,3373,1103,100,10,1))
if mibBuilder.loadTexts:ptpRadioAsymmetryDataSetTable.setStatus(_A)
_PtpRadioAsymmetryDataSetEntry_Object=MibTableRow
ptpRadioAsymmetryDataSetEntry=_PtpRadioAsymmetryDataSetEntry_Object((1,3,6,1,4,1,3373,1103,100,10,1,1))
ptpRadioAsymmetryDataSetEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:ptpRadioAsymmetryDataSetEntry.setStatus(_A)
_PtpRadioBrIndex_Type=Integer32
_PtpRadioBrIndex_Object=MibTableColumn
ptpRadioBrIndex=_PtpRadioBrIndex_Object((1,3,6,1,4,1,3373,1103,100,10,1,1,1),_PtpRadioBrIndex_Type())
ptpRadioBrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ptpRadioBrIndex.setStatus(_A)
class _PtpRadioOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_PtpRadioOffset_Type.__name__=_D
_PtpRadioOffset_Object=MibTableColumn
ptpRadioOffset=_PtpRadioOffset_Object((1,3,6,1,4,1,3373,1103,100,10,1,1,2),_PtpRadioOffset_Type())
ptpRadioOffset.setMaxAccess(_E)
if mibBuilder.loadTexts:ptpRadioOffset.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ClockDomainType':ClockDomainType,'ClockProfileType':ClockProfileType,_V:ClockQualityAccuracyType,_U:ClockQualityClassType,'ClockStateType':ClockStateType,_W:ClockTimeSourceType,_T:ClockInstanceType,_Z:ClockPPSInstanceType,'ClockPortNumber':ClockPortNumber,'ClockPortState':ClockPortState,_X:ClockMechanismType,'ClockTimeInterval':ClockTimeInterval,'ClockType':ClockType,_a:PtpClockToDFormatType,'ptp':ptp,'ptpMibVersion':ptpMibVersion,'ptpProfileDataSet':ptpProfileDataSet,'ptpSystemProfile':ptpSystemProfile,'ptpProfileName':ptpProfileName,'ptpProfilePrimaryVersion':ptpProfilePrimaryVersion,'ptpProfileRevisionNumber':ptpProfileRevisionNumber,'ptpProfileIdentifier':ptpProfileIdentifier,'ptpSpecificDataSet':ptpSpecificDataSet,'ptpSpecificDataSetTable':ptpSpecificDataSetTable,'ptpSpecificDataSetEntry':ptpSpecificDataSetEntry,'ptpAdminStatus':ptpAdminStatus,'ptpStaticPortRole':ptpStaticPortRole,'ptpClockState':ptpClockState,'ptpCompliance':ptpCompliance,'ptpSpecificAlarmTable':ptpSpecificAlarmTable,'ptpSpecificAlarmEntry':ptpSpecificAlarmEntry,'ptpFreeRunningAlarm':ptpFreeRunningAlarm,'ptpHoldoverInSpecAlarm':ptpHoldoverInSpecAlarm,'ptpHoldoverOutOfSpecAlarm':ptpHoldoverOutOfSpecAlarm,'ptpFreeRunningAlarmSeverityCode':ptpFreeRunningAlarmSeverityCode,'ptpHoldoverInSpecAlarmSeverityCode':ptpHoldoverInSpecAlarmSeverityCode,'ptpHoldoverOutOfSpecAlarmSeverityCode':ptpHoldoverOutOfSpecAlarmSeverityCode,'ptpDefaultDataSet':ptpDefaultDataSet,'ptpClockDataSetTable':ptpClockDataSetTable,'ptpClockDataSetEntry':ptpClockDataSetEntry,_G:ptpClockDomainIndex,_H:ptpClockTypeIndex,_I:ptpClockInstanceIndex,'ptpClockIdentity':ptpClockIdentity,'ptpClockTwoStepFlag':ptpClockTwoStepFlag,'ptpClockNumberPorts':ptpClockNumberPorts,'ptpClockClass':ptpClockClass,'ptpClockAccuracy':ptpClockAccuracy,'ptpClockOffsetScaledLogVariance':ptpClockOffsetScaledLogVariance,'ptpClockPriority1':ptpClockPriority1,'ptpClockPriority2':ptpClockPriority2,'ptpClockSlaveOnly':ptpClockSlaveOnly,'ptpClockLocalPriority':ptpClockLocalPriority,'ptpClockRowStatus':ptpClockRowStatus,'ptpCurrentDataSet':ptpCurrentDataSet,'ptpCurrentDataSetTable':ptpCurrentDataSetTable,'ptpCurrentDataSetEntry':ptpCurrentDataSetEntry,'ptpCurrentStepsRemoved':ptpCurrentStepsRemoved,'ptpCurrentOffsetFromMaster':ptpCurrentOffsetFromMaster,'ptpCurrentMeanPathDelay':ptpCurrentMeanPathDelay,'ptpParentDataSet':ptpParentDataSet,'ptpParentDataSetTable':ptpParentDataSetTable,'ptpParentDataSetEntry':ptpParentDataSetEntry,'ptpParentClockIdentity':ptpParentClockIdentity,'ptpParentPortNumber':ptpParentPortNumber,'ptpParentGMClockIdentity':ptpParentGMClockIdentity,'ptpParentGMClockClass':ptpParentGMClockClass,'ptpParentGMClockAccuracy':ptpParentGMClockAccuracy,'ptpParentGMClockOffsetScaledLogVariance':ptpParentGMClockOffsetScaledLogVariance,'ptpParentGMPriority1':ptpParentGMPriority1,'ptpParentGMPriority2':ptpParentGMPriority2,'ptpTimePropertiesDataSet':ptpTimePropertiesDataSet,'ptpTimeDataSetTable':ptpTimeDataSetTable,'ptpTimeDataSetEntry':ptpTimeDataSetEntry,'ptpTimeCurrentUTCOffset':ptpTimeCurrentUTCOffset,'ptpTimeCurrentUTCOffsetValid':ptpTimeCurrentUTCOffsetValid,'ptpTimeLeap59':ptpTimeLeap59,'ptpTimeLeap61':ptpTimeLeap61,'ptpTimeTimeTraceable':ptpTimeTimeTraceable,'ptpTimeFrequencyTraceable':ptpTimeFrequencyTraceable,'ptpTimescale':ptpTimescale,'ptpTimeTimeSource':ptpTimeTimeSource,'ptpPortDataSet':ptpPortDataSet,'ptpPortDataSetTable':ptpPortDataSetTable,'ptpPortDataSetEntry':ptpPortDataSetEntry,_Q:ptpPortIndex,'ptpPortClockIdentity':ptpPortClockIdentity,'ptpPortIfIndex':ptpPortIfIndex,'ptpPortStaticRole':ptpPortStaticRole,'ptpPortAdminStatus':ptpPortAdminStatus,'ptpPortState':ptpPortState,'ptpPortMinDelayReqInterval':ptpPortMinDelayReqInterval,'ptpPortLogAnnounceInterval':ptpPortLogAnnounceInterval,'ptpPortAnnounceReceiptTimeout':ptpPortAnnounceReceiptTimeout,'ptpPortSyncInterval':ptpPortSyncInterval,'ptpPortDelayMechanism':ptpPortDelayMechanism,'ptpPortVersionNumber':ptpPortVersionNumber,'ptpPortNotSlave':ptpPortNotSlave,'ptpPortLocalPriority':ptpPortLocalPriority,'ptpPortDestMacAddress':ptpPortDestMacAddress,'ptpPortTxAsymmetryCompensation':ptpPortTxAsymmetryCompensation,'ptpPortRxAsymmetryCompensation':ptpPortRxAsymmetryCompensation,'ptpPortRowStatus':ptpPortRowStatus,'ptpPortAlarmTable':ptpPortAlarmTable,'ptpPortAlarmEntry':ptpPortAlarmEntry,'ptpPortFaultyAlarm':ptpPortFaultyAlarm,'ptpPortInitializingAlarm':ptpPortInitializingAlarm,'ptpPortUncalibratedAlarm':ptpPortUncalibratedAlarm,'ptpPortListeningAlarm':ptpPortListeningAlarm,'ptpPortActiveStatus':ptpPortActiveStatus,'ptpPortRadioAlarmTable':ptpPortRadioAlarmTable,'ptpPortRadioAlarmEntry':ptpPortRadioAlarmEntry,'ptpPortRadioCapacityAlarm':ptpPortRadioCapacityAlarm,'ptpPortFaultyAlarmSeverityCode':ptpPortFaultyAlarmSeverityCode,'ptpPortInitializingAlarmSeverityCode':ptpPortInitializingAlarmSeverityCode,'ptpPortUncalibratedAlarmSeverityCode':ptpPortUncalibratedAlarmSeverityCode,'ptpPortListeningAlarmSeverityCode':ptpPortListeningAlarmSeverityCode,'ptpPortActiveStatusSeverityCode':ptpPortActiveStatusSeverityCode,'ptpPortRadioCapacityAlarmSeverityCode':ptpPortRadioCapacityAlarmSeverityCode,'ptpClockPPSDataSet':ptpClockPPSDataSet,'ptpClockPPSDataSetTable':ptpClockPPSDataSetTable,'ptpClockPPSDataSetEntry':ptpClockPPSDataSetEntry,_Y:ptpClockPPSInstanceIndex,'ptpClockPPSInstanceCapability':ptpClockPPSInstanceCapability,'ptpClockPPSDirection':ptpClockPPSDirection,'ptpClockPPSLabel':ptpClockPPSLabel,'ptpClockPPSAdminStatus':ptpClockPPSAdminStatus,'ptpClockPPSOffsetEnabled':ptpClockPPSOffsetEnabled,'ptpClockPPSOffsetValue':ptpClockPPSOffsetValue,'ptpClockToDLabel':ptpClockToDLabel,'ptpClockToDAdminStatus':ptpClockToDAdminStatus,'ptpClockToDDelay':ptpClockToDDelay,'ptpClockToDBaudrate':ptpClockToDBaudrate,'ptpClockToDFormat':ptpClockToDFormat,'ptpRadioAsymmetryDataSet':ptpRadioAsymmetryDataSet,'ptpRadioAsymmetryDataSetTable':ptpRadioAsymmetryDataSetTable,'ptpRadioAsymmetryDataSetEntry':ptpRadioAsymmetryDataSetEntry,_b:ptpRadioBrIndex,'ptpRadioOffset':ptpRadioOffset})