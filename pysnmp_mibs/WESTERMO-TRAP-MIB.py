_M='rtTrapGroup'
_L='rtTrapMsgGroup'
_K='notifyInfo'
_J='notifyNotice'
_I='notifyWarning'
_H='notifyError'
_G='notifyCritical'
_F='notifyAlert'
_E='notifyEmergency'
_D='DisplayString'
_C='trapMsgString'
_B='current'
_A='WESTERMO-TRAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
notification=ModuleIdentity((1,3,6,1,4,1,16177,1,400,200))
if mibBuilder.loadTexts:notification.setRevisions(('2019-09-06 00:00',))
_RtTraps_ObjectIdentity=ObjectIdentity
rtTraps=_RtTraps_ObjectIdentity((1,3,6,1,4,1,16177,1,400,200,0))
_RtTrapMsg_ObjectIdentity=ObjectIdentity
rtTrapMsg=_RtTrapMsg_ObjectIdentity((1,3,6,1,4,1,16177,1,400,200,1))
class _TrapMsgString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_TrapMsgString_Type.__name__=_D
_TrapMsgString_Object=MibScalar
trapMsgString=_TrapMsgString_Object((1,3,6,1,4,1,16177,1,400,200,1,1),_TrapMsgString_Type())
trapMsgString.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:trapMsgString.setStatus(_B)
_RtTrapConformance_ObjectIdentity=ObjectIdentity
rtTrapConformance=_RtTrapConformance_ObjectIdentity((1,3,6,1,4,1,16177,1,400,200,3))
_RtTrapGroups_ObjectIdentity=ObjectIdentity
rtTrapGroups=_RtTrapGroups_ObjectIdentity((1,3,6,1,4,1,16177,1,400,200,3,1))
_RtTrapCompliances_ObjectIdentity=ObjectIdentity
rtTrapCompliances=_RtTrapCompliances_ObjectIdentity((1,3,6,1,4,1,16177,1,400,200,3,2))
rtTrapMsgGroup=ObjectGroup((1,3,6,1,4,1,16177,1,400,200,3,1,1))
rtTrapMsgGroup.setObjects((_A,_C))
if mibBuilder.loadTexts:rtTrapMsgGroup.setStatus(_B)
notifyEmergency=NotificationType((1,3,6,1,4,1,16177,1,400,200,0,1))
notifyEmergency.setObjects((_A,_C))
if mibBuilder.loadTexts:notifyEmergency.setStatus(_B)
notifyAlert=NotificationType((1,3,6,1,4,1,16177,1,400,200,0,2))
notifyAlert.setObjects((_A,_C))
if mibBuilder.loadTexts:notifyAlert.setStatus(_B)
notifyCritical=NotificationType((1,3,6,1,4,1,16177,1,400,200,0,3))
notifyCritical.setObjects((_A,_C))
if mibBuilder.loadTexts:notifyCritical.setStatus(_B)
notifyError=NotificationType((1,3,6,1,4,1,16177,1,400,200,0,4))
notifyError.setObjects((_A,_C))
if mibBuilder.loadTexts:notifyError.setStatus(_B)
notifyWarning=NotificationType((1,3,6,1,4,1,16177,1,400,200,0,5))
notifyWarning.setObjects((_A,_C))
if mibBuilder.loadTexts:notifyWarning.setStatus(_B)
notifyNotice=NotificationType((1,3,6,1,4,1,16177,1,400,200,0,6))
notifyNotice.setObjects((_A,_C))
if mibBuilder.loadTexts:notifyNotice.setStatus(_B)
notifyInfo=NotificationType((1,3,6,1,4,1,16177,1,400,200,0,7))
notifyInfo.setObjects((_A,_C))
if mibBuilder.loadTexts:notifyInfo.setStatus(_B)
rtTrapGroup=NotificationGroup((1,3,6,1,4,1,16177,1,400,200,3,1,2))
rtTrapGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:rtTrapGroup.setStatus(_B)
rttrapCompliance=ModuleCompliance((1,3,6,1,4,1,16177,1,400,200,3,2,1))
rttrapCompliance.setObjects(*((_A,_L),(_A,_M)))
if mibBuilder.loadTexts:rttrapCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'notification':notification,'rtTraps':rtTraps,_E:notifyEmergency,_F:notifyAlert,_G:notifyCritical,_H:notifyError,_I:notifyWarning,_J:notifyNotice,_K:notifyInfo,'rtTrapMsg':rtTrapMsg,_C:trapMsgString,'rtTrapConformance':rtTrapConformance,'rtTrapGroups':rtTrapGroups,_L:rtTrapMsgGroup,_M:rtTrapGroup,'rtTrapCompliances':rtTrapCompliances,'rttrapCompliance':rttrapCompliance})