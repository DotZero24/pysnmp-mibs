_G='fsClkIwfGlobalErrTrapType'
_F='ARICENT-CLKIWF-MIB'
_E='read-only'
_D='TruthValue'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
fsClkIwfMIB=ModuleIdentity((1,3,6,1,4,1,29601,2,46))
if mibBuilder.loadTexts:fsClkIwfMIB.setRevisions(('2012-09-05 00:00',))
class FsClkIwfTimeInterval(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsClkIwfObjects_ObjectIdentity=ObjectIdentity
fsClkIwfObjects=_FsClkIwfObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,46,1))
_FsClkIwfGeneralGroup_ObjectIdentity=ObjectIdentity
fsClkIwfGeneralGroup=_FsClkIwfGeneralGroup_ObjectIdentity((1,3,6,1,4,1,29601,2,46,1,1))
class _FsClkIwfClockVariance_Type(Integer32):defaultValue=0
_FsClkIwfClockVariance_Type.__name__=_C
_FsClkIwfClockVariance_Object=MibScalar
fsClkIwfClockVariance=_FsClkIwfClockVariance_Object((1,3,6,1,4,1,29601,2,46,1,1,1),_FsClkIwfClockVariance_Type())
fsClkIwfClockVariance.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClkIwfClockVariance.setStatus(_A)
class _FsClkIwfClockClass_Type(Integer32):defaultValue=248
_FsClkIwfClockClass_Type.__name__=_C
_FsClkIwfClockClass_Object=MibScalar
fsClkIwfClockClass=_FsClkIwfClockClass_Object((1,3,6,1,4,1,29601,2,46,1,1,2),_FsClkIwfClockClass_Type())
fsClkIwfClockClass.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClkIwfClockClass.setStatus(_A)
class _FsClkIwfClockAccuracy_Type(Integer32):defaultValue=254
_FsClkIwfClockAccuracy_Type.__name__=_C
_FsClkIwfClockAccuracy_Object=MibScalar
fsClkIwfClockAccuracy=_FsClkIwfClockAccuracy_Object((1,3,6,1,4,1,29601,2,46,1,1,3),_FsClkIwfClockAccuracy_Type())
fsClkIwfClockAccuracy.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClkIwfClockAccuracy.setStatus(_A)
class _FsClkIwfClockTimeSource_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,32,64,80,160)));namedValues=NamedValues(*(('atomicClock',16),('gps',32),('ptp',64),('ntp',80),('internalOscillator',160)))
_FsClkIwfClockTimeSource_Type.__name__=_C
_FsClkIwfClockTimeSource_Object=MibScalar
fsClkIwfClockTimeSource=_FsClkIwfClockTimeSource_Object((1,3,6,1,4,1,29601,2,46,1,1,4),_FsClkIwfClockTimeSource_Type())
fsClkIwfClockTimeSource.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClkIwfClockTimeSource.setStatus(_A)
_FsClkIwfCurrentUtcOffset_Type=FsClkIwfTimeInterval
_FsClkIwfCurrentUtcOffset_Object=MibScalar
fsClkIwfCurrentUtcOffset=_FsClkIwfCurrentUtcOffset_Object((1,3,6,1,4,1,29601,2,46,1,1,5),_FsClkIwfCurrentUtcOffset_Type())
fsClkIwfCurrentUtcOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClkIwfCurrentUtcOffset.setStatus('deprecated')
_FsClkIwfARBTime_Type=DisplayString
_FsClkIwfARBTime_Object=MibScalar
fsClkIwfARBTime=_FsClkIwfARBTime_Object((1,3,6,1,4,1,29601,2,46,1,1,6),_FsClkIwfARBTime_Type())
fsClkIwfARBTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClkIwfARBTime.setStatus(_A)
class _FsClkIwfHoldoverSpecification_Type(TruthValue):defaultValue=1
_FsClkIwfHoldoverSpecification_Type.__name__=_D
_FsClkIwfHoldoverSpecification_Object=MibScalar
fsClkIwfHoldoverSpecification=_FsClkIwfHoldoverSpecification_Object((1,3,6,1,4,1,29601,2,46,1,1,7),_FsClkIwfHoldoverSpecification_Type())
fsClkIwfHoldoverSpecification.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClkIwfHoldoverSpecification.setStatus(_A)
class _FsClkIwfLostSync_Type(TruthValue):defaultValue=2
_FsClkIwfLostSync_Type.__name__=_D
_FsClkIwfLostSync_Object=MibScalar
fsClkIwfLostSync=_FsClkIwfLostSync_Object((1,3,6,1,4,1,29601,2,46,1,1,8),_FsClkIwfLostSync_Type())
fsClkIwfLostSync.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClkIwfLostSync.setStatus(_A)
_FsClkIwfUtcOffset_Type=DisplayString
_FsClkIwfUtcOffset_Object=MibScalar
fsClkIwfUtcOffset=_FsClkIwfUtcOffset_Object((1,3,6,1,4,1,29601,2,46,1,1,9),_FsClkIwfUtcOffset_Type())
fsClkIwfUtcOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClkIwfUtcOffset.setStatus(_A)
_FsClkIwfNotifications_ObjectIdentity=ObjectIdentity
fsClkIwfNotifications=_FsClkIwfNotifications_ObjectIdentity((1,3,6,1,4,1,29601,2,46,2))
_FsClkIwfTrap_ObjectIdentity=ObjectIdentity
fsClkIwfTrap=_FsClkIwfTrap_ObjectIdentity((1,3,6,1,4,1,29601,2,46,2,0))
class _FsClkIwfGlobalErrTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',0),('memfail',1),('bufffail',2),('timesourcechange',3),('clockclasschange',4),('clockaccuracychange',5),('clockvariancechange',6),('holdovermodechange',7)))
_FsClkIwfGlobalErrTrapType_Type.__name__=_C
_FsClkIwfGlobalErrTrapType_Object=MibScalar
fsClkIwfGlobalErrTrapType=_FsClkIwfGlobalErrTrapType_Object((1,3,6,1,4,1,29601,2,46,2,1),_FsClkIwfGlobalErrTrapType_Type())
fsClkIwfGlobalErrTrapType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsClkIwfGlobalErrTrapType.setStatus(_A)
_FsClkIwfNotification_Type=OctetString
_FsClkIwfNotification_Object=MibScalar
fsClkIwfNotification=_FsClkIwfNotification_Object((1,3,6,1,4,1,29601,2,46,2,2),_FsClkIwfNotification_Type())
fsClkIwfNotification.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClkIwfNotification.setStatus(_A)
fsClkIwfGlobalErrorTrap=NotificationType((1,3,6,1,4,1,29601,2,46,2,0,1))
fsClkIwfGlobalErrorTrap.setObjects((_F,_G))
if mibBuilder.loadTexts:fsClkIwfGlobalErrorTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'FsClkIwfTimeInterval':FsClkIwfTimeInterval,'fsClkIwfMIB':fsClkIwfMIB,'fsClkIwfObjects':fsClkIwfObjects,'fsClkIwfGeneralGroup':fsClkIwfGeneralGroup,'fsClkIwfClockVariance':fsClkIwfClockVariance,'fsClkIwfClockClass':fsClkIwfClockClass,'fsClkIwfClockAccuracy':fsClkIwfClockAccuracy,'fsClkIwfClockTimeSource':fsClkIwfClockTimeSource,'fsClkIwfCurrentUtcOffset':fsClkIwfCurrentUtcOffset,'fsClkIwfARBTime':fsClkIwfARBTime,'fsClkIwfHoldoverSpecification':fsClkIwfHoldoverSpecification,'fsClkIwfLostSync':fsClkIwfLostSync,'fsClkIwfUtcOffset':fsClkIwfUtcOffset,'fsClkIwfNotifications':fsClkIwfNotifications,'fsClkIwfTrap':fsClkIwfTrap,'fsClkIwfGlobalErrorTrap':fsClkIwfGlobalErrorTrap,_G:fsClkIwfGlobalErrTrapType,'fsClkIwfNotification':fsClkIwfNotification})