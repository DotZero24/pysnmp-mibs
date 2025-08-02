_L='read-only'
_K='read-create'
_J='dhcpFilteringVlanId'
_I='TPLINK-DHCPFILTERING-MIB'
_H='read-write'
_G='ifIndex'
_F='IF-MIB'
_E='enable'
_D='disable'
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
tplinkDhcpFilteringMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,48))
if mibBuilder.loadTexts:tplinkDhcpFilteringMIB.setRevisions(('2012-12-17 10:14',))
_TplinkDhcpFilteringMIBObjects_ObjectIdentity=ObjectIdentity
tplinkDhcpFilteringMIBObjects=_TplinkDhcpFilteringMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,48,1))
_DhcpFilteringGlobalConfig_ObjectIdentity=ObjectIdentity
dhcpFilteringGlobalConfig=_DhcpFilteringGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,48,1,1))
class _DhcpFilteringEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DhcpFilteringEnable_Type.__name__=_B
_DhcpFilteringEnable_Object=MibScalar
dhcpFilteringEnable=_DhcpFilteringEnable_Object((1,3,6,1,4,1,11863,6,48,1,1,1),_DhcpFilteringEnable_Type())
dhcpFilteringEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:dhcpFilteringEnable.setStatus(_A)
_DhcpFilteringVlanConfigTable_Object=MibTable
dhcpFilteringVlanConfigTable=_DhcpFilteringVlanConfigTable_Object((1,3,6,1,4,1,11863,6,48,1,1,2))
if mibBuilder.loadTexts:dhcpFilteringVlanConfigTable.setStatus(_A)
_DhcpFilteringVlanConfigEntry_Object=MibTableRow
dhcpFilteringVlanConfigEntry=_DhcpFilteringVlanConfigEntry_Object((1,3,6,1,4,1,11863,6,48,1,1,2,1))
dhcpFilteringVlanConfigEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:dhcpFilteringVlanConfigEntry.setStatus(_A)
class _DhcpFilteringVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_DhcpFilteringVlanId_Type.__name__=_B
_DhcpFilteringVlanId_Object=MibTableColumn
dhcpFilteringVlanId=_DhcpFilteringVlanId_Object((1,3,6,1,4,1,11863,6,48,1,1,2,1,1),_DhcpFilteringVlanId_Type())
dhcpFilteringVlanId.setMaxAccess(_K)
if mibBuilder.loadTexts:dhcpFilteringVlanId.setStatus(_A)
class _DhcpFilteringVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DhcpFilteringVlanStatus_Type.__name__=_B
_DhcpFilteringVlanStatus_Object=MibTableColumn
dhcpFilteringVlanStatus=_DhcpFilteringVlanStatus_Object((1,3,6,1,4,1,11863,6,48,1,1,2,1,2),_DhcpFilteringVlanStatus_Type())
dhcpFilteringVlanStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:dhcpFilteringVlanStatus.setStatus(_A)
_DhcpFilteringPortConfig_ObjectIdentity=ObjectIdentity
dhcpFilteringPortConfig=_DhcpFilteringPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,48,1,3))
_DhcpFilteringPortConfigTable_Object=MibTable
dhcpFilteringPortConfigTable=_DhcpFilteringPortConfigTable_Object((1,3,6,1,4,1,11863,6,48,1,3,1))
if mibBuilder.loadTexts:dhcpFilteringPortConfigTable.setStatus(_A)
_DhcpFilteringPortConfigEntry_Object=MibTableRow
dhcpFilteringPortConfigEntry=_DhcpFilteringPortConfigEntry_Object((1,3,6,1,4,1,11863,6,48,1,3,1,1))
dhcpFilteringPortConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dhcpFilteringPortConfigEntry.setStatus(_A)
class _DhcpFilteringPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DhcpFilteringPort_Type.__name__=_C
_DhcpFilteringPort_Object=MibTableColumn
dhcpFilteringPort=_DhcpFilteringPort_Object((1,3,6,1,4,1,11863,6,48,1,3,1,1,1),_DhcpFilteringPort_Type())
dhcpFilteringPort.setMaxAccess(_L)
if mibBuilder.loadTexts:dhcpFilteringPort.setStatus(_A)
class _DhcpFilteringPortConfigTrustedPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DhcpFilteringPortConfigTrustedPort_Type.__name__=_B
_DhcpFilteringPortConfigTrustedPort_Object=MibTableColumn
dhcpFilteringPortConfigTrustedPort=_DhcpFilteringPortConfigTrustedPort_Object((1,3,6,1,4,1,11863,6,48,1,3,1,1,2),_DhcpFilteringPortConfigTrustedPort_Type())
dhcpFilteringPortConfigTrustedPort.setMaxAccess(_H)
if mibBuilder.loadTexts:dhcpFilteringPortConfigTrustedPort.setStatus(_A)
class _DhcpFilteringPortConfigPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DhcpFilteringPortConfigPortLag_Type.__name__=_C
_DhcpFilteringPortConfigPortLag_Object=MibTableColumn
dhcpFilteringPortConfigPortLag=_DhcpFilteringPortConfigPortLag_Object((1,3,6,1,4,1,11863,6,48,1,3,1,1,3),_DhcpFilteringPortConfigPortLag_Type())
dhcpFilteringPortConfigPortLag.setMaxAccess(_L)
if mibBuilder.loadTexts:dhcpFilteringPortConfigPortLag.setStatus(_A)
_TplinkDhcpFilteringNotifications_ObjectIdentity=ObjectIdentity
tplinkDhcpFilteringNotifications=_TplinkDhcpFilteringNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,48,2))
mibBuilder.exportSymbols(_I,**{'tplinkDhcpFilteringMIB':tplinkDhcpFilteringMIB,'tplinkDhcpFilteringMIBObjects':tplinkDhcpFilteringMIBObjects,'dhcpFilteringGlobalConfig':dhcpFilteringGlobalConfig,'dhcpFilteringEnable':dhcpFilteringEnable,'dhcpFilteringVlanConfigTable':dhcpFilteringVlanConfigTable,'dhcpFilteringVlanConfigEntry':dhcpFilteringVlanConfigEntry,_J:dhcpFilteringVlanId,'dhcpFilteringVlanStatus':dhcpFilteringVlanStatus,'dhcpFilteringPortConfig':dhcpFilteringPortConfig,'dhcpFilteringPortConfigTable':dhcpFilteringPortConfigTable,'dhcpFilteringPortConfigEntry':dhcpFilteringPortConfigEntry,'dhcpFilteringPort':dhcpFilteringPort,'dhcpFilteringPortConfigTrustedPort':dhcpFilteringPortConfigTrustedPort,'dhcpFilteringPortConfigPortLag':dhcpFilteringPortConfigPortLag,'tplinkDhcpFilteringNotifications':tplinkDhcpFilteringNotifications})