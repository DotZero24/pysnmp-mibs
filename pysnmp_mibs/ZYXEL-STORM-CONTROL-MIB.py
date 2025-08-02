_I='zyStormControlType'
_H='ZYXEL-STORM-CONTROL-MIB'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='dot1dBasePort'
_C='BRIDGE-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_C,_D)
ifIndex,=mibBuilder.importSymbols(_E,_F)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelStormControl=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,78))
_ZyxelStormControlSetup_ObjectIdentity=ObjectIdentity
zyxelStormControlSetup=_ZyxelStormControlSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,78,1))
_ZyStromControlState_Type=EnabledStatus
_ZyStromControlState_Object=MibScalar
zyStromControlState=_ZyStromControlState_Object((1,3,6,1,4,1,890,1,15,3,78,1,1),_ZyStromControlState_Type())
zyStromControlState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyStromControlState.setStatus(_A)
_ZyxelStromControlPortTable_Object=MibTable
zyxelStromControlPortTable=_ZyxelStromControlPortTable_Object((1,3,6,1,4,1,890,1,15,3,78,1,2))
if mibBuilder.loadTexts:zyxelStromControlPortTable.setStatus(_A)
_ZyxelStromControlPortEntry_Object=MibTableRow
zyxelStromControlPortEntry=_ZyxelStromControlPortEntry_Object((1,3,6,1,4,1,890,1,15,3,78,1,2,1))
zyxelStromControlPortEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelStromControlPortEntry.setStatus(_A)
_ZyStromControlPortBroadcastState_Type=EnabledStatus
_ZyStromControlPortBroadcastState_Object=MibTableColumn
zyStromControlPortBroadcastState=_ZyStromControlPortBroadcastState_Object((1,3,6,1,4,1,890,1,15,3,78,1,2,1,1),_ZyStromControlPortBroadcastState_Type())
zyStromControlPortBroadcastState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyStromControlPortBroadcastState.setStatus(_A)
_ZyStromControlPortBroadcastRate_Type=Integer32
_ZyStromControlPortBroadcastRate_Object=MibTableColumn
zyStromControlPortBroadcastRate=_ZyStromControlPortBroadcastRate_Object((1,3,6,1,4,1,890,1,15,3,78,1,2,1,2),_ZyStromControlPortBroadcastRate_Type())
zyStromControlPortBroadcastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zyStromControlPortBroadcastRate.setStatus(_A)
_ZyStromControlPortMulticastState_Type=EnabledStatus
_ZyStromControlPortMulticastState_Object=MibTableColumn
zyStromControlPortMulticastState=_ZyStromControlPortMulticastState_Object((1,3,6,1,4,1,890,1,15,3,78,1,2,1,3),_ZyStromControlPortMulticastState_Type())
zyStromControlPortMulticastState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyStromControlPortMulticastState.setStatus(_A)
_ZyStromControlPortMulticastRate_Type=Integer32
_ZyStromControlPortMulticastRate_Object=MibTableColumn
zyStromControlPortMulticastRate=_ZyStromControlPortMulticastRate_Object((1,3,6,1,4,1,890,1,15,3,78,1,2,1,4),_ZyStromControlPortMulticastRate_Type())
zyStromControlPortMulticastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zyStromControlPortMulticastRate.setStatus(_A)
_ZyStromControlPortDlfState_Type=EnabledStatus
_ZyStromControlPortDlfState_Object=MibTableColumn
zyStromControlPortDlfState=_ZyStromControlPortDlfState_Object((1,3,6,1,4,1,890,1,15,3,78,1,2,1,5),_ZyStromControlPortDlfState_Type())
zyStromControlPortDlfState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyStromControlPortDlfState.setStatus(_A)
_ZyStromControlPortDlfRate_Type=Integer32
_ZyStromControlPortDlfRate_Object=MibTableColumn
zyStromControlPortDlfRate=_ZyStromControlPortDlfRate_Object((1,3,6,1,4,1,890,1,15,3,78,1,2,1,6),_ZyStromControlPortDlfRate_Type())
zyStromControlPortDlfRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zyStromControlPortDlfRate.setStatus(_A)
_ZyxelStormControlNotifications_ObjectIdentity=ObjectIdentity
zyxelStormControlNotifications=_ZyxelStormControlNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,78,2))
_ZyxelStormControlTrapInfoObject_ObjectIdentity=ObjectIdentity
zyxelStormControlTrapInfoObject=_ZyxelStormControlTrapInfoObject_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,78,3))
class _ZyStormControlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('broadcast-storm',1),('multicast-storm',2)))
_ZyStormControlType_Type.__name__=_G
_ZyStormControlType_Object=MibScalar
zyStormControlType=_ZyStormControlType_Object((1,3,6,1,4,1,890,1,15,3,78,3,1),_ZyStormControlType_Type())
zyStormControlType.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyStormControlType.setStatus(_A)
zyPortStormControlTrap=NotificationType((1,3,6,1,4,1,890,1,15,3,78,2,1))
zyPortStormControlTrap.setObjects(*((_E,_F),(_H,_I)))
if mibBuilder.loadTexts:zyPortStormControlTrap.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'zyxelStormControl':zyxelStormControl,'zyxelStormControlSetup':zyxelStormControlSetup,'zyStromControlState':zyStromControlState,'zyxelStromControlPortTable':zyxelStromControlPortTable,'zyxelStromControlPortEntry':zyxelStromControlPortEntry,'zyStromControlPortBroadcastState':zyStromControlPortBroadcastState,'zyStromControlPortBroadcastRate':zyStromControlPortBroadcastRate,'zyStromControlPortMulticastState':zyStromControlPortMulticastState,'zyStromControlPortMulticastRate':zyStromControlPortMulticastRate,'zyStromControlPortDlfState':zyStromControlPortDlfState,'zyStromControlPortDlfRate':zyStromControlPortDlfRate,'zyxelStormControlNotifications':zyxelStormControlNotifications,'zyPortStormControlTrap':zyPortStormControlTrap,'zyxelStormControlTrapInfoObject':zyxelStormControlTrapInfoObject,_I:zyStormControlType})