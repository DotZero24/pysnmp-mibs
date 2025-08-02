_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelFdb=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,48))
_ZyxelMacStatus_ObjectIdentity=ObjectIdentity
zyxelMacStatus=_ZyxelMacStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,48,1))
_ZyMacFlush_Type=EnabledStatus
_ZyMacFlush_Object=MibScalar
zyMacFlush=_ZyMacFlush_Object((1,3,6,1,4,1,890,1,15,3,48,1,1),_ZyMacFlush_Type())
zyMacFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacFlush.setStatus(_A)
_ZyMacFlushPort_Type=Integer32
_ZyMacFlushPort_Object=MibScalar
zyMacFlushPort=_ZyMacFlushPort_Object((1,3,6,1,4,1,890,1,15,3,48,1,2),_ZyMacFlushPort_Type())
zyMacFlushPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacFlushPort.setStatus(_A)
_ZyMacFlushVlan_Type=Integer32
_ZyMacFlushVlan_Object=MibScalar
zyMacFlushVlan=_ZyMacFlushVlan_Object((1,3,6,1,4,1,890,1,15,3,48,1,3),_ZyMacFlushVlan_Type())
zyMacFlushVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMacFlushVlan.setStatus(_A)
_ZyxelMacStatusNotifications_ObjectIdentity=ObjectIdentity
zyxelMacStatusNotifications=_ZyxelMacStatusNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,48,2))
zyMacForwardingTableFull=NotificationType((1,3,6,1,4,1,890,1,15,3,48,2,1))
if mibBuilder.loadTexts:zyMacForwardingTableFull.setStatus(_A)
zyMacForwardingTableFullRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,48,2,2))
if mibBuilder.loadTexts:zyMacForwardingTableFullRecovered.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-FDB-MIB',**{'zyxelFdb':zyxelFdb,'zyxelMacStatus':zyxelMacStatus,'zyMacFlush':zyMacFlush,'zyMacFlushPort':zyMacFlushPort,'zyMacFlushVlan':zyMacFlushVlan,'zyxelMacStatusNotifications':zyxelMacStatusNotifications,'zyMacForwardingTableFull':zyMacForwardingTableFull,'zyMacForwardingTableFullRecovered':zyMacForwardingTableFullRecovered})