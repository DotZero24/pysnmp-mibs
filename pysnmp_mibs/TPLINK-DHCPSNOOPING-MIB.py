_K='dhcpSnoopingVlanId'
_J='TPLINK-DHCPSNOOPING-MIB'
_I='enable'
_H='disable'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='read-write'
_C='OctetString'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkDhcpSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,27))
if mibBuilder.loadTexts:tplinkDhcpSnoopingMIB.setRevisions(('2012-12-17 10:14',))
_TplinkDhcpSnoopingMIBObjects_ObjectIdentity=ObjectIdentity
tplinkDhcpSnoopingMIBObjects=_TplinkDhcpSnoopingMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,27,1))
_DhcpSnoopingGlobalConfig_ObjectIdentity=ObjectIdentity
dhcpSnoopingGlobalConfig=_DhcpSnoopingGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,27,1,1))
class _DhcpSnoopingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_DhcpSnoopingEnable_Type.__name__=_B
_DhcpSnoopingEnable_Object=MibScalar
dhcpSnoopingEnable=_DhcpSnoopingEnable_Object((1,3,6,1,4,1,11863,6,27,1,1,1),_DhcpSnoopingEnable_Type())
dhcpSnoopingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpSnoopingEnable.setStatus(_A)
_DhcpSnoopingVlanConfigTable_Object=MibTable
dhcpSnoopingVlanConfigTable=_DhcpSnoopingVlanConfigTable_Object((1,3,6,1,4,1,11863,6,27,1,1,2))
if mibBuilder.loadTexts:dhcpSnoopingVlanConfigTable.setStatus(_A)
_DhcpSnoopingVlanConfigEntry_Object=MibTableRow
dhcpSnoopingVlanConfigEntry=_DhcpSnoopingVlanConfigEntry_Object((1,3,6,1,4,1,11863,6,27,1,1,2,1))
dhcpSnoopingVlanConfigEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:dhcpSnoopingVlanConfigEntry.setStatus(_A)
class _DhcpSnoopingVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_DhcpSnoopingVlanId_Type.__name__=_B
_DhcpSnoopingVlanId_Object=MibTableColumn
dhcpSnoopingVlanId=_DhcpSnoopingVlanId_Object((1,3,6,1,4,1,11863,6,27,1,1,2,1,1),_DhcpSnoopingVlanId_Type())
dhcpSnoopingVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpSnoopingVlanId.setStatus(_A)
class _DhcpSnoopingVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_DhcpSnoopingVlanStatus_Type.__name__=_B
_DhcpSnoopingVlanStatus_Object=MibTableColumn
dhcpSnoopingVlanStatus=_DhcpSnoopingVlanStatus_Object((1,3,6,1,4,1,11863,6,27,1,1,2,1,2),_DhcpSnoopingVlanStatus_Type())
dhcpSnoopingVlanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpSnoopingVlanStatus.setStatus(_A)
_DhcpSnoopingPortConfig_ObjectIdentity=ObjectIdentity
dhcpSnoopingPortConfig=_DhcpSnoopingPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,27,1,3))
_DhcpSnoopingPortConfigTable_Object=MibTable
dhcpSnoopingPortConfigTable=_DhcpSnoopingPortConfigTable_Object((1,3,6,1,4,1,11863,6,27,1,3,1))
if mibBuilder.loadTexts:dhcpSnoopingPortConfigTable.setStatus(_A)
_DhcpSnoopingPortConfigEntry_Object=MibTableRow
dhcpSnoopingPortConfigEntry=_DhcpSnoopingPortConfigEntry_Object((1,3,6,1,4,1,11863,6,27,1,3,1,1))
dhcpSnoopingPortConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dhcpSnoopingPortConfigEntry.setStatus(_A)
class _DhcpSnoopingPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DhcpSnoopingPort_Type.__name__=_C
_DhcpSnoopingPort_Object=MibTableColumn
dhcpSnoopingPort=_DhcpSnoopingPort_Object((1,3,6,1,4,1,11863,6,27,1,3,1,1,1),_DhcpSnoopingPort_Type())
dhcpSnoopingPort.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpSnoopingPort.setStatus(_A)
_DhcpSnoopingPortConfigMaxEntry_Type=Integer32
_DhcpSnoopingPortConfigMaxEntry_Object=MibTableColumn
dhcpSnoopingPortConfigMaxEntry=_DhcpSnoopingPortConfigMaxEntry_Object((1,3,6,1,4,1,11863,6,27,1,3,1,1,2),_DhcpSnoopingPortConfigMaxEntry_Type())
dhcpSnoopingPortConfigMaxEntry.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpSnoopingPortConfigMaxEntry.setStatus(_A)
class _DhcpSnoopingPortConfigPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DhcpSnoopingPortConfigPortLag_Type.__name__=_C
_DhcpSnoopingPortConfigPortLag_Object=MibTableColumn
dhcpSnoopingPortConfigPortLag=_DhcpSnoopingPortConfigPortLag_Object((1,3,6,1,4,1,11863,6,27,1,3,1,1,3),_DhcpSnoopingPortConfigPortLag_Type())
dhcpSnoopingPortConfigPortLag.setMaxAccess(_E)
if mibBuilder.loadTexts:dhcpSnoopingPortConfigPortLag.setStatus(_A)
_TplinkDhcpSnoopingNotifications_ObjectIdentity=ObjectIdentity
tplinkDhcpSnoopingNotifications=_TplinkDhcpSnoopingNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,27,2))
mibBuilder.exportSymbols(_J,**{'tplinkDhcpSnoopingMIB':tplinkDhcpSnoopingMIB,'tplinkDhcpSnoopingMIBObjects':tplinkDhcpSnoopingMIBObjects,'dhcpSnoopingGlobalConfig':dhcpSnoopingGlobalConfig,'dhcpSnoopingEnable':dhcpSnoopingEnable,'dhcpSnoopingVlanConfigTable':dhcpSnoopingVlanConfigTable,'dhcpSnoopingVlanConfigEntry':dhcpSnoopingVlanConfigEntry,_K:dhcpSnoopingVlanId,'dhcpSnoopingVlanStatus':dhcpSnoopingVlanStatus,'dhcpSnoopingPortConfig':dhcpSnoopingPortConfig,'dhcpSnoopingPortConfigTable':dhcpSnoopingPortConfigTable,'dhcpSnoopingPortConfigEntry':dhcpSnoopingPortConfigEntry,'dhcpSnoopingPort':dhcpSnoopingPort,'dhcpSnoopingPortConfigMaxEntry':dhcpSnoopingPortConfigMaxEntry,'dhcpSnoopingPortConfigPortLag':dhcpSnoopingPortConfigPortLag,'tplinkDhcpSnoopingNotifications':tplinkDhcpSnoopingNotifications})