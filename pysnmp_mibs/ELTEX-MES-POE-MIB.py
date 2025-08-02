_D='Integer32'
_C='current'
_B='read-write'
_A='TruthValue'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_A)
eltMesPoe=ModuleIdentity((1,3,6,1,4,1,35265,1,23,16))
if mibBuilder.loadTexts:eltMesPoe.setRevisions(('2019-04-02 00:00','2017-11-07 00:00'))
_EltMesPoeNotifications_ObjectIdentity=ObjectIdentity
eltMesPoeNotifications=_EltMesPoeNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,23,16,0))
_EltMesPoeObjects_ObjectIdentity=ObjectIdentity
eltMesPoeObjects=_EltMesPoeObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,16,1))
class _EltPoeRestartAction_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,8),ValueRangeConstraint(255,255))
_EltPoeRestartAction_Type.__name__=_D
_EltPoeRestartAction_Object=MibScalar
eltPoeRestartAction=_EltPoeRestartAction_Object((1,3,6,1,4,1,35265,1,23,16,1,1),_EltPoeRestartAction_Type())
eltPoeRestartAction.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPoeRestartAction.setStatus(_C)
class _EltPoeDisabled_Type(TruthValue):defaultValue=1
_EltPoeDisabled_Type.__name__=_A
_EltPoeDisabled_Object=MibScalar
eltPoeDisabled=_EltPoeDisabled_Object((1,3,6,1,4,1,35265,1,23,16,1,2),_EltPoeDisabled_Type())
eltPoeDisabled.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPoeDisabled.setStatus(_C)
class _EltPoeAutoRestart_Type(TruthValue):defaultValue=1
_EltPoeAutoRestart_Type.__name__=_A
_EltPoeAutoRestart_Object=MibScalar
eltPoeAutoRestart=_EltPoeAutoRestart_Object((1,3,6,1,4,1,35265,1,23,16,1,3),_EltPoeAutoRestart_Type())
eltPoeAutoRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPoeAutoRestart.setStatus(_C)
mibBuilder.exportSymbols('ELTEX-MES-POE-MIB',**{'eltMesPoe':eltMesPoe,'eltMesPoeNotifications':eltMesPoeNotifications,'eltMesPoeObjects':eltMesPoeObjects,'eltPoeRestartAction':eltPoeRestartAction,'eltPoeDisabled':eltPoeDisabled,'eltPoeAutoRestart':eltPoeAutoRestart})