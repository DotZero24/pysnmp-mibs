_H='atG8032v2NotificationSystemAlarmState'
_G='atG8032v2NotificationInstanceCurrentState'
_F='atG8032v2NotificationInstanceFromState'
_E='atG8032v2NotificationInstanceName'
_D='DisplayStringUnsized'
_C='read-only'
_B='AT-G8032v2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB',_D,'modules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
atG8032v2=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,604))
if mibBuilder.loadTexts:atG8032v2.setRevisions(('2017-02-06 00:00','2017-01-17 00:00'))
class AtG8032v2InstanceState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',1),('init',2),('idle',3),('protection',4),('manualSwitch',5),('forcedSwitch',6),('pending',7)))
_AtG8032v2Notifications_ObjectIdentity=ObjectIdentity
atG8032v2Notifications=_AtG8032v2Notifications_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,604,0))
_AtG8032v2NotificationVariable_ObjectIdentity=ObjectIdentity
atG8032v2NotificationVariable=_AtG8032v2NotificationVariable_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,604,1))
class _AtG8032v2NotificationInstanceName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AtG8032v2NotificationInstanceName_Type.__name__=_D
_AtG8032v2NotificationInstanceName_Object=MibScalar
atG8032v2NotificationInstanceName=_AtG8032v2NotificationInstanceName_Object((1,3,6,1,4,1,207,8,4,4,4,604,1,1),_AtG8032v2NotificationInstanceName_Type())
atG8032v2NotificationInstanceName.setMaxAccess(_C)
if mibBuilder.loadTexts:atG8032v2NotificationInstanceName.setStatus(_A)
_AtG8032v2NotificationInstanceFromState_Type=AtG8032v2InstanceState
_AtG8032v2NotificationInstanceFromState_Object=MibScalar
atG8032v2NotificationInstanceFromState=_AtG8032v2NotificationInstanceFromState_Object((1,3,6,1,4,1,207,8,4,4,4,604,1,2),_AtG8032v2NotificationInstanceFromState_Type())
atG8032v2NotificationInstanceFromState.setMaxAccess(_C)
if mibBuilder.loadTexts:atG8032v2NotificationInstanceFromState.setStatus(_A)
_AtG8032v2NotificationInstanceCurrentState_Type=AtG8032v2InstanceState
_AtG8032v2NotificationInstanceCurrentState_Object=MibScalar
atG8032v2NotificationInstanceCurrentState=_AtG8032v2NotificationInstanceCurrentState_Object((1,3,6,1,4,1,207,8,4,4,4,604,1,3),_AtG8032v2NotificationInstanceCurrentState_Type())
atG8032v2NotificationInstanceCurrentState.setMaxAccess(_C)
if mibBuilder.loadTexts:atG8032v2NotificationInstanceCurrentState.setStatus(_A)
_AtG8032v2NotificationSystemAlarmState_Type=TruthValue
_AtG8032v2NotificationSystemAlarmState_Object=MibScalar
atG8032v2NotificationSystemAlarmState=_AtG8032v2NotificationSystemAlarmState_Object((1,3,6,1,4,1,207,8,4,4,4,604,1,4),_AtG8032v2NotificationSystemAlarmState_Type())
atG8032v2NotificationSystemAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:atG8032v2NotificationSystemAlarmState.setStatus(_A)
atG8032v2InstanceNotify=NotificationType((1,3,6,1,4,1,207,8,4,4,4,604,0,1))
atG8032v2InstanceNotify.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:atG8032v2InstanceNotify.setStatus(_A)
atG8032v2SystemAlarmNotify=NotificationType((1,3,6,1,4,1,207,8,4,4,4,604,0,2))
atG8032v2SystemAlarmNotify.setObjects((_B,_H))
if mibBuilder.loadTexts:atG8032v2SystemAlarmNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AtG8032v2InstanceState':AtG8032v2InstanceState,'atG8032v2':atG8032v2,'atG8032v2Notifications':atG8032v2Notifications,'atG8032v2InstanceNotify':atG8032v2InstanceNotify,'atG8032v2SystemAlarmNotify':atG8032v2SystemAlarmNotify,'atG8032v2NotificationVariable':atG8032v2NotificationVariable,_E:atG8032v2NotificationInstanceName,_F:atG8032v2NotificationInstanceFromState,_G:atG8032v2NotificationInstanceCurrentState,_H:atG8032v2NotificationSystemAlarmState})