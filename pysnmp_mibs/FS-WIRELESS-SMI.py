_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
products,=mibBuilder.importSymbols('FS-SMI','products')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
wirelessMib=ModuleIdentity((1,3,6,1,4,1,52642,1,3,1))
if mibBuilder.loadTexts:wirelessMib.setRevisions(('2007-07-04 00:00',))
_Wireless_ObjectIdentity=ObjectIdentity
wireless=_Wireless_ObjectIdentity((1,3,6,1,4,1,52642,1,3))
_FsWirelessProducts_ObjectIdentity=ObjectIdentity
fsWirelessProducts=_FsWirelessProducts_ObjectIdentity((1,3,6,1,4,1,52642,1,3,1,1))
if mibBuilder.loadTexts:fsWirelessProducts.setStatus(_A)
_FsWirelessMgmt_ObjectIdentity=ObjectIdentity
fsWirelessMgmt=_FsWirelessMgmt_ObjectIdentity((1,3,6,1,4,1,52642,1,3,1,2))
if mibBuilder.loadTexts:fsWirelessMgmt.setStatus(_A)
mibBuilder.exportSymbols('FS-WIRELESS-SMI',**{'wireless':wireless,'wirelessMib':wirelessMib,'fsWirelessProducts':fsWirelessProducts,'fsWirelessMgmt':fsWirelessMgmt})