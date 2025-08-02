_C='read-write'
_B='Integer32'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctDevice,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctDevice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtTimedResetMIB_ObjectIdentity=ObjectIdentity
ctTimedResetMIB=_CtTimedResetMIB_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,5,2))
class _CtTimedResetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('softEnabled',1),('hardEnabled',2)))
_CtTimedResetStatus_Type.__name__=_B
_CtTimedResetStatus_Object=MibScalar
ctTimedResetStatus=_CtTimedResetStatus_Object((1,3,6,1,4,1,52,4,1,1,5,2,1),_CtTimedResetStatus_Type())
ctTimedResetStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctTimedResetStatus.setStatus(_A)
_CtTimedResetTimeEntered_Type=Integer32
_CtTimedResetTimeEntered_Object=MibScalar
ctTimedResetTimeEntered=_CtTimedResetTimeEntered_Object((1,3,6,1,4,1,52,4,1,1,5,2,2),_CtTimedResetTimeEntered_Type())
ctTimedResetTimeEntered.setMaxAccess(_C)
if mibBuilder.loadTexts:ctTimedResetTimeEntered.setStatus(_A)
_CtTimedResetTimeRemaining_Type=Integer32
_CtTimedResetTimeRemaining_Object=MibScalar
ctTimedResetTimeRemaining=_CtTimedResetTimeRemaining_Object((1,3,6,1,4,1,52,4,1,1,5,2,3),_CtTimedResetTimeRemaining_Type())
ctTimedResetTimeRemaining.setMaxAccess('read-only')
if mibBuilder.loadTexts:ctTimedResetTimeRemaining.setStatus(_A)
class _CtTimedResetOperationalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('currentMode',0),('ieee8021Q',1),('secureFast',2)))
_CtTimedResetOperationalMode_Type.__name__=_B
_CtTimedResetOperationalMode_Object=MibScalar
ctTimedResetOperationalMode=_CtTimedResetOperationalMode_Object((1,3,6,1,4,1,52,4,1,1,5,2,4),_CtTimedResetOperationalMode_Type())
ctTimedResetOperationalMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ctTimedResetOperationalMode.setStatus(_A)
class _CtTimedResetNVRamReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dontResetNVRam',0),('resetNVRam',1)))
_CtTimedResetNVRamReset_Type.__name__=_B
_CtTimedResetNVRamReset_Object=MibScalar
ctTimedResetNVRamReset=_CtTimedResetNVRamReset_Object((1,3,6,1,4,1,52,4,1,1,5,2,5),_CtTimedResetNVRamReset_Type())
ctTimedResetNVRamReset.setMaxAccess(_C)
if mibBuilder.loadTexts:ctTimedResetNVRamReset.setStatus(_A)
mibBuilder.exportSymbols('CTRON-TIMED-RESET-MIB',**{'ctTimedResetMIB':ctTimedResetMIB,'ctTimedResetStatus':ctTimedResetStatus,'ctTimedResetTimeEntered':ctTimedResetTimeEntered,'ctTimedResetTimeRemaining':ctTimedResetTimeRemaining,'ctTimedResetOperationalMode':ctTimedResetOperationalMode,'ctTimedResetNVRamReset':ctTimedResetNVRamReset})