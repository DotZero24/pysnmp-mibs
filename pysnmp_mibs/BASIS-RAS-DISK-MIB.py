_G='testInProgress'
_F='unknown'
_E='read-write'
_D='DisplayString'
_C='read-only'
_B='mandatory'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
axisDiagnostics,=mibBuilder.importSymbols('BASIS-MIB','axisDiagnostics')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_RasDsk_ObjectIdentity=ObjectIdentity
rasDsk=_RasDsk_ObjectIdentity((1,3,6,1,4,1,351,110,6,2))
class _RasDskStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_RasDskStatus_Type.__name__=_A
_RasDskStatus_Object=MibScalar
rasDskStatus=_RasDskStatus_Object((1,3,6,1,4,1,351,110,6,2,1),_RasDskStatus_Type())
rasDskStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rasDskStatus.setStatus(_B)
class _DskHealth_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pass',1),('fail',2),(_F,3),(_G,4)))
_DskHealth_Type.__name__=_A
_DskHealth_Object=MibScalar
dskHealth=_DskHealth_Object((1,3,6,1,4,1,351,110,6,2,2),_DskHealth_Type())
dskHealth.setMaxAccess(_C)
if mibBuilder.loadTexts:dskHealth.setStatus(_B)
class _StandbyDskHealth_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pass',1),('fail',2),(_F,3),(_G,4)))
_StandbyDskHealth_Type.__name__=_A
_StandbyDskHealth_Object=MibScalar
standbyDskHealth=_StandbyDskHealth_Object((1,3,6,1,4,1,351,110,6,2,3),_StandbyDskHealth_Type())
standbyDskHealth.setMaxAccess(_C)
if mibBuilder.loadTexts:standbyDskHealth.setStatus(_B)
class _WakeupInterval_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(12,168))
_WakeupInterval_Type.__name__=_A
_WakeupInterval_Object=MibScalar
wakeupInterval=_WakeupInterval_Object((1,3,6,1,4,1,351,110,6,2,4),_WakeupInterval_Type())
wakeupInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:wakeupInterval.setStatus(_B)
class _LastTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_LastTime_Type.__name__=_D
_LastTime_Object=MibScalar
lastTime=_LastTime_Object((1,3,6,1,4,1,351,110,6,2,5),_LastTime_Type())
lastTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lastTime.setStatus(_B)
class _NumBadSectors_Type(Integer32):defaultValue=0
_NumBadSectors_Type.__name__=_A
_NumBadSectors_Object=MibScalar
numBadSectors=_NumBadSectors_Object((1,3,6,1,4,1,351,110,6,2,6),_NumBadSectors_Type())
numBadSectors.setMaxAccess(_C)
if mibBuilder.loadTexts:numBadSectors.setStatus(_B)
class _CrptdPRIfiles_Type(Integer32):defaultValue=0
_CrptdPRIfiles_Type.__name__=_A
_CrptdPRIfiles_Object=MibScalar
crptdPRIfiles=_CrptdPRIfiles_Object((1,3,6,1,4,1,351,110,6,2,7),_CrptdPRIfiles_Type())
crptdPRIfiles.setMaxAccess(_C)
if mibBuilder.loadTexts:crptdPRIfiles.setStatus(_B)
class _CrptdFWfiles_Type(Integer32):defaultValue=0
_CrptdFWfiles_Type.__name__=_A
_CrptdFWfiles_Object=MibScalar
crptdFWfiles=_CrptdFWfiles_Object((1,3,6,1,4,1,351,110,6,2,8),_CrptdFWfiles_Type())
crptdFWfiles.setMaxAccess(_C)
if mibBuilder.loadTexts:crptdFWfiles.setStatus(_B)
mibBuilder.exportSymbols('BASIS-RAS-DISK-MIB',**{'rasDsk':rasDsk,'rasDskStatus':rasDskStatus,'dskHealth':dskHealth,'standbyDskHealth':standbyDskHealth,'wakeupInterval':wakeupInterval,'lastTime':lastTime,'numBadSectors':numBadSectors,'crptdPRIfiles':crptdPRIfiles,'crptdFWfiles':crptdFWfiles})