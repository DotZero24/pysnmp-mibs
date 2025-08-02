_D='other'
_C='Integer32'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
jnxAlarms=ModuleIdentity((1,3,6,1,4,1,2636,3,4))
_JnxCraftAlarms_ObjectIdentity=ObjectIdentity
jnxCraftAlarms=_JnxCraftAlarms_ObjectIdentity((1,3,6,1,4,1,2636,3,4,2))
class _JnxAlarmRelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('passOn',2),('cutOff',3)))
_JnxAlarmRelayMode_Type.__name__=_C
_JnxAlarmRelayMode_Object=MibScalar
jnxAlarmRelayMode=_JnxAlarmRelayMode_Object((1,3,6,1,4,1,2636,3,4,2,1),_JnxAlarmRelayMode_Type())
jnxAlarmRelayMode.setMaxAccess(_A)
if mibBuilder.loadTexts:jnxAlarmRelayMode.setStatus(_B)
_JnxYellowAlarms_ObjectIdentity=ObjectIdentity
jnxYellowAlarms=_JnxYellowAlarms_ObjectIdentity((1,3,6,1,4,1,2636,3,4,2,2))
class _JnxYellowAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('off',2),('on',3)))
_JnxYellowAlarmState_Type.__name__=_C
_JnxYellowAlarmState_Object=MibScalar
jnxYellowAlarmState=_JnxYellowAlarmState_Object((1,3,6,1,4,1,2636,3,4,2,2,1),_JnxYellowAlarmState_Type())
jnxYellowAlarmState.setMaxAccess(_A)
if mibBuilder.loadTexts:jnxYellowAlarmState.setStatus(_B)
_JnxYellowAlarmCount_Type=Gauge32
_JnxYellowAlarmCount_Object=MibScalar
jnxYellowAlarmCount=_JnxYellowAlarmCount_Object((1,3,6,1,4,1,2636,3,4,2,2,2),_JnxYellowAlarmCount_Type())
jnxYellowAlarmCount.setMaxAccess(_A)
if mibBuilder.loadTexts:jnxYellowAlarmCount.setStatus(_B)
_JnxYellowAlarmLastChange_Type=TimeStamp
_JnxYellowAlarmLastChange_Object=MibScalar
jnxYellowAlarmLastChange=_JnxYellowAlarmLastChange_Object((1,3,6,1,4,1,2636,3,4,2,2,3),_JnxYellowAlarmLastChange_Type())
jnxYellowAlarmLastChange.setMaxAccess(_A)
if mibBuilder.loadTexts:jnxYellowAlarmLastChange.setStatus(_B)
_JnxRedAlarms_ObjectIdentity=ObjectIdentity
jnxRedAlarms=_JnxRedAlarms_ObjectIdentity((1,3,6,1,4,1,2636,3,4,2,3))
class _JnxRedAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('off',2),('on',3)))
_JnxRedAlarmState_Type.__name__=_C
_JnxRedAlarmState_Object=MibScalar
jnxRedAlarmState=_JnxRedAlarmState_Object((1,3,6,1,4,1,2636,3,4,2,3,1),_JnxRedAlarmState_Type())
jnxRedAlarmState.setMaxAccess(_A)
if mibBuilder.loadTexts:jnxRedAlarmState.setStatus(_B)
_JnxRedAlarmCount_Type=Gauge32
_JnxRedAlarmCount_Object=MibScalar
jnxRedAlarmCount=_JnxRedAlarmCount_Object((1,3,6,1,4,1,2636,3,4,2,3,2),_JnxRedAlarmCount_Type())
jnxRedAlarmCount.setMaxAccess(_A)
if mibBuilder.loadTexts:jnxRedAlarmCount.setStatus(_B)
_JnxRedAlarmLastChange_Type=TimeStamp
_JnxRedAlarmLastChange_Object=MibScalar
jnxRedAlarmLastChange=_JnxRedAlarmLastChange_Object((1,3,6,1,4,1,2636,3,4,2,3,3),_JnxRedAlarmLastChange_Type())
jnxRedAlarmLastChange.setMaxAccess(_A)
if mibBuilder.loadTexts:jnxRedAlarmLastChange.setStatus(_B)
mibBuilder.exportSymbols('JUNIPER-ALARM-MIB',**{'jnxAlarms':jnxAlarms,'jnxCraftAlarms':jnxCraftAlarms,'jnxAlarmRelayMode':jnxAlarmRelayMode,'jnxYellowAlarms':jnxYellowAlarms,'jnxYellowAlarmState':jnxYellowAlarmState,'jnxYellowAlarmCount':jnxYellowAlarmCount,'jnxYellowAlarmLastChange':jnxYellowAlarmLastChange,'jnxRedAlarms':jnxRedAlarms,'jnxRedAlarmState':jnxRedAlarmState,'jnxRedAlarmCount':jnxRedAlarmCount,'jnxRedAlarmLastChange':jnxRedAlarmLastChange})