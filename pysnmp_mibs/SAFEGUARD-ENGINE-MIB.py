_H='read-only'
_G='enabled'
_F='disabled'
_E='swSafeGuardCurrentStatus'
_D='SAFEGUARD-ENGINE-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
swSafeGuardMIB=ModuleIdentity((1,3,6,1,4,1,171,12,19))
_SwSafeGuardGblMgmt_ObjectIdentity=ObjectIdentity
swSafeGuardGblMgmt=_SwSafeGuardGblMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,19,1))
class _SwSafeGuardAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_F,2),(_G,3)))
_SwSafeGuardAdminState_Type.__name__=_B
_SwSafeGuardAdminState_Object=MibScalar
swSafeGuardAdminState=_SwSafeGuardAdminState_Object((1,3,6,1,4,1,171,12,19,1,1),_SwSafeGuardAdminState_Type())
swSafeGuardAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swSafeGuardAdminState.setStatus(_A)
_SwSafeGuardctrl_ObjectIdentity=ObjectIdentity
swSafeGuardctrl=_SwSafeGuardctrl_ObjectIdentity((1,3,6,1,4,1,171,12,19,2))
class _SwSafeGuardRisingThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,100))
_SwSafeGuardRisingThreshold_Type.__name__=_B
_SwSafeGuardRisingThreshold_Object=MibScalar
swSafeGuardRisingThreshold=_SwSafeGuardRisingThreshold_Object((1,3,6,1,4,1,171,12,19,2,1),_SwSafeGuardRisingThreshold_Type())
swSafeGuardRisingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swSafeGuardRisingThreshold.setStatus(_A)
class _SwSafeGuardFallingThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,100))
_SwSafeGuardFallingThreshold_Type.__name__=_B
_SwSafeGuardFallingThreshold_Object=MibScalar
swSafeGuardFallingThreshold=_SwSafeGuardFallingThreshold_Object((1,3,6,1,4,1,171,12,19,2,2),_SwSafeGuardFallingThreshold_Type())
swSafeGuardFallingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swSafeGuardFallingThreshold.setStatus(_A)
class _SwSafeGuardmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict',1),('fuzzy',2)))
_SwSafeGuardmode_Type.__name__=_B
_SwSafeGuardmode_Object=MibScalar
swSafeGuardmode=_SwSafeGuardmode_Object((1,3,6,1,4,1,171,12,19,2,3),_SwSafeGuardmode_Type())
swSafeGuardmode.setMaxAccess(_C)
if mibBuilder.loadTexts:swSafeGuardmode.setStatus(_A)
class _SwSafeGuardAlarmAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_F,2),(_G,3)))
_SwSafeGuardAlarmAdminState_Type.__name__=_B
_SwSafeGuardAlarmAdminState_Object=MibScalar
swSafeGuardAlarmAdminState=_SwSafeGuardAlarmAdminState_Object((1,3,6,1,4,1,171,12,19,2,4),_SwSafeGuardAlarmAdminState_Type())
swSafeGuardAlarmAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swSafeGuardAlarmAdminState.setStatus(_A)
class _SwSafeGuardCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('exhausted',2)))
_SwSafeGuardCurrentStatus_Type.__name__=_B
_SwSafeGuardCurrentStatus_Object=MibScalar
swSafeGuardCurrentStatus=_SwSafeGuardCurrentStatus_Object((1,3,6,1,4,1,171,12,19,2,5),_SwSafeGuardCurrentStatus_Type())
swSafeGuardCurrentStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swSafeGuardCurrentStatus.setStatus(_A)
class _SwSafeGuardInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwSafeGuardInterval_Type.__name__=_B
_SwSafeGuardInterval_Object=MibScalar
swSafeGuardInterval=_SwSafeGuardInterval_Object((1,3,6,1,4,1,171,12,19,2,6),_SwSafeGuardInterval_Type())
swSafeGuardInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:swSafeGuardInterval.setStatus(_A)
_SwSafeGuardNotify_ObjectIdentity=ObjectIdentity
swSafeGuardNotify=_SwSafeGuardNotify_ObjectIdentity((1,3,6,1,4,1,171,12,19,4))
_SwSafeGuardNotification_ObjectIdentity=ObjectIdentity
swSafeGuardNotification=_SwSafeGuardNotification_ObjectIdentity((1,3,6,1,4,1,171,12,19,4,1))
_SwSafeGuardNotifyPrefix_ObjectIdentity=ObjectIdentity
swSafeGuardNotifyPrefix=_SwSafeGuardNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,19,4,1,0))
swSafeGuardChgToExhausted=NotificationType((1,3,6,1,4,1,171,12,19,4,1,0,1))
swSafeGuardChgToExhausted.setObjects((_D,_E))
if mibBuilder.loadTexts:swSafeGuardChgToExhausted.setStatus(_A)
swSafeGuardChgToNormal=NotificationType((1,3,6,1,4,1,171,12,19,4,1,0,2))
swSafeGuardChgToNormal.setObjects((_D,_E))
if mibBuilder.loadTexts:swSafeGuardChgToNormal.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'swSafeGuardMIB':swSafeGuardMIB,'swSafeGuardGblMgmt':swSafeGuardGblMgmt,'swSafeGuardAdminState':swSafeGuardAdminState,'swSafeGuardctrl':swSafeGuardctrl,'swSafeGuardRisingThreshold':swSafeGuardRisingThreshold,'swSafeGuardFallingThreshold':swSafeGuardFallingThreshold,'swSafeGuardmode':swSafeGuardmode,'swSafeGuardAlarmAdminState':swSafeGuardAlarmAdminState,_E:swSafeGuardCurrentStatus,'swSafeGuardInterval':swSafeGuardInterval,'swSafeGuardNotify':swSafeGuardNotify,'swSafeGuardNotification':swSafeGuardNotification,'swSafeGuardNotifyPrefix':swSafeGuardNotifyPrefix,'swSafeGuardChgToExhausted':swSafeGuardChgToExhausted,'swSafeGuardChgToNormal':swSafeGuardChgToNormal})