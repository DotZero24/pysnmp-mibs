_N='h3cSecHighHgMonitorAlarmReason'
_M='h3cSecHighHgMonitorAlarmDstPort'
_L='h3cSecHighHgMonitorAlarmDstChip'
_K='h3cSecHighHgMonitorAlarmDstSlot'
_J='h3cSecHighHgMonitorAlarmDstChassis'
_I='h3cSecHighHgMonitorAlarmSrcPort'
_H='h3cSecHighHgMonitorAlarmSrcChip'
_G='h3cSecHighHgMonitorAlarmSrcSlot'
_F='h3cSecHighHgMonitorAlarmSrcChassis'
_E='h3cSecHighHgMonitorAlarmType'
_D='OctetString'
_C='accessible-for-notify'
_B='H3C-SECHIGH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cSecHigh=ModuleIdentity((1,3,6,1,4,1,2011,10,2,171))
if mibBuilder.loadTexts:h3cSecHigh.setRevisions(('2017-09-16 20:20',))
_H3cSecHighMonitor_ObjectIdentity=ObjectIdentity
h3cSecHighMonitor=_H3cSecHighMonitor_ObjectIdentity((1,3,6,1,4,1,2011,10,2,171,1))
_H3cSecHighHgMonitorAlarmVar_ObjectIdentity=ObjectIdentity
h3cSecHighHgMonitorAlarmVar=_H3cSecHighHgMonitorAlarmVar_ObjectIdentity((1,3,6,1,4,1,2011,10,2,171,1,1))
_H3cSecHighHgMonitorAlarmType_Type=Integer32
_H3cSecHighHgMonitorAlarmType_Object=MibScalar
h3cSecHighHgMonitorAlarmType=_H3cSecHighHgMonitorAlarmType_Object((1,3,6,1,4,1,2011,10,2,171,1,1,1),_H3cSecHighHgMonitorAlarmType_Type())
h3cSecHighHgMonitorAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecHighHgMonitorAlarmType.setStatus(_A)
_H3cSecHighHgMonitorAlarmSrcChassis_Type=Integer32
_H3cSecHighHgMonitorAlarmSrcChassis_Object=MibScalar
h3cSecHighHgMonitorAlarmSrcChassis=_H3cSecHighHgMonitorAlarmSrcChassis_Object((1,3,6,1,4,1,2011,10,2,171,1,1,2),_H3cSecHighHgMonitorAlarmSrcChassis_Type())
h3cSecHighHgMonitorAlarmSrcChassis.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecHighHgMonitorAlarmSrcChassis.setStatus(_A)
_H3cSecHighHgMonitorAlarmSrcSlot_Type=Integer32
_H3cSecHighHgMonitorAlarmSrcSlot_Object=MibScalar
h3cSecHighHgMonitorAlarmSrcSlot=_H3cSecHighHgMonitorAlarmSrcSlot_Object((1,3,6,1,4,1,2011,10,2,171,1,1,3),_H3cSecHighHgMonitorAlarmSrcSlot_Type())
h3cSecHighHgMonitorAlarmSrcSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecHighHgMonitorAlarmSrcSlot.setStatus(_A)
_H3cSecHighHgMonitorAlarmSrcChip_Type=Integer32
_H3cSecHighHgMonitorAlarmSrcChip_Object=MibScalar
h3cSecHighHgMonitorAlarmSrcChip=_H3cSecHighHgMonitorAlarmSrcChip_Object((1,3,6,1,4,1,2011,10,2,171,1,1,4),_H3cSecHighHgMonitorAlarmSrcChip_Type())
h3cSecHighHgMonitorAlarmSrcChip.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecHighHgMonitorAlarmSrcChip.setStatus(_A)
_H3cSecHighHgMonitorAlarmSrcPort_Type=Integer32
_H3cSecHighHgMonitorAlarmSrcPort_Object=MibScalar
h3cSecHighHgMonitorAlarmSrcPort=_H3cSecHighHgMonitorAlarmSrcPort_Object((1,3,6,1,4,1,2011,10,2,171,1,1,5),_H3cSecHighHgMonitorAlarmSrcPort_Type())
h3cSecHighHgMonitorAlarmSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecHighHgMonitorAlarmSrcPort.setStatus(_A)
_H3cSecHighHgMonitorAlarmDstChassis_Type=Integer32
_H3cSecHighHgMonitorAlarmDstChassis_Object=MibScalar
h3cSecHighHgMonitorAlarmDstChassis=_H3cSecHighHgMonitorAlarmDstChassis_Object((1,3,6,1,4,1,2011,10,2,171,1,1,6),_H3cSecHighHgMonitorAlarmDstChassis_Type())
h3cSecHighHgMonitorAlarmDstChassis.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecHighHgMonitorAlarmDstChassis.setStatus(_A)
_H3cSecHighHgMonitorAlarmDstSlot_Type=Integer32
_H3cSecHighHgMonitorAlarmDstSlot_Object=MibScalar
h3cSecHighHgMonitorAlarmDstSlot=_H3cSecHighHgMonitorAlarmDstSlot_Object((1,3,6,1,4,1,2011,10,2,171,1,1,7),_H3cSecHighHgMonitorAlarmDstSlot_Type())
h3cSecHighHgMonitorAlarmDstSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecHighHgMonitorAlarmDstSlot.setStatus(_A)
_H3cSecHighHgMonitorAlarmDstChip_Type=Integer32
_H3cSecHighHgMonitorAlarmDstChip_Object=MibScalar
h3cSecHighHgMonitorAlarmDstChip=_H3cSecHighHgMonitorAlarmDstChip_Object((1,3,6,1,4,1,2011,10,2,171,1,1,8),_H3cSecHighHgMonitorAlarmDstChip_Type())
h3cSecHighHgMonitorAlarmDstChip.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecHighHgMonitorAlarmDstChip.setStatus(_A)
_H3cSecHighHgMonitorAlarmDstPort_Type=Integer32
_H3cSecHighHgMonitorAlarmDstPort_Object=MibScalar
h3cSecHighHgMonitorAlarmDstPort=_H3cSecHighHgMonitorAlarmDstPort_Object((1,3,6,1,4,1,2011,10,2,171,1,1,9),_H3cSecHighHgMonitorAlarmDstPort_Type())
h3cSecHighHgMonitorAlarmDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecHighHgMonitorAlarmDstPort.setStatus(_A)
class _H3cSecHighHgMonitorAlarmReason_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_H3cSecHighHgMonitorAlarmReason_Type.__name__=_D
_H3cSecHighHgMonitorAlarmReason_Object=MibScalar
h3cSecHighHgMonitorAlarmReason=_H3cSecHighHgMonitorAlarmReason_Object((1,3,6,1,4,1,2011,10,2,171,1,1,10),_H3cSecHighHgMonitorAlarmReason_Type())
h3cSecHighHgMonitorAlarmReason.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecHighHgMonitorAlarmReason.setStatus(_A)
_H3cSecHighHgMonitorAlarmTrap_ObjectIdentity=ObjectIdentity
h3cSecHighHgMonitorAlarmTrap=_H3cSecHighHgMonitorAlarmTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,171,1,2))
_H3cSecHighHgMonitorAlarmNotifications_ObjectIdentity=ObjectIdentity
h3cSecHighHgMonitorAlarmNotifications=_H3cSecHighHgMonitorAlarmNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,171,1,2,0))
h3cSecHighHgMonitorAlarmNotification=NotificationType((1,3,6,1,4,1,2011,10,2,171,1,2,0,1))
h3cSecHighHgMonitorAlarmNotification.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:h3cSecHighHgMonitorAlarmNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cSecHigh':h3cSecHigh,'h3cSecHighMonitor':h3cSecHighMonitor,'h3cSecHighHgMonitorAlarmVar':h3cSecHighHgMonitorAlarmVar,_E:h3cSecHighHgMonitorAlarmType,_F:h3cSecHighHgMonitorAlarmSrcChassis,_G:h3cSecHighHgMonitorAlarmSrcSlot,_H:h3cSecHighHgMonitorAlarmSrcChip,_I:h3cSecHighHgMonitorAlarmSrcPort,_J:h3cSecHighHgMonitorAlarmDstChassis,_K:h3cSecHighHgMonitorAlarmDstSlot,_L:h3cSecHighHgMonitorAlarmDstChip,_M:h3cSecHighHgMonitorAlarmDstPort,_N:h3cSecHighHgMonitorAlarmReason,'h3cSecHighHgMonitorAlarmTrap':h3cSecHighHgMonitorAlarmTrap,'h3cSecHighHgMonitorAlarmNotifications':h3cSecHighHgMonitorAlarmNotifications,'h3cSecHighHgMonitorAlarmNotification':h3cSecHighHgMonitorAlarmNotification})