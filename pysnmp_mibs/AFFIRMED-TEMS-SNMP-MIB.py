if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
affirmedSnmp,=mibBuilder.importSymbols('AFFIRMED-SNMP-MIB','affirmedSnmp')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
affirmedTemsSnmp=ModuleIdentity((1,3,6,1,4,1,37963,6))
if mibBuilder.loadTexts:affirmedTemsSnmp.setRevisions(('2011-05-16 00:00',))
_AffirmedSnmpTc_ObjectIdentity=ObjectIdentity
affirmedSnmpTc=_AffirmedSnmpTc_ObjectIdentity((1,3,6,1,4,1,37963,6,1))
_AffirmedSnmpObjects_ObjectIdentity=ObjectIdentity
affirmedSnmpObjects=_AffirmedSnmpObjects_ObjectIdentity((1,3,6,1,4,1,37963,6,2))
_AffirmedSnmpNotifications_ObjectIdentity=ObjectIdentity
affirmedSnmpNotifications=_AffirmedSnmpNotifications_ObjectIdentity((1,3,6,1,4,1,37963,6,3))
mibBuilder.exportSymbols('AFFIRMED-TEMS-SNMP-MIB',**{'affirmedTemsSnmp':affirmedTemsSnmp,'affirmedSnmpTc':affirmedSnmpTc,'affirmedSnmpObjects':affirmedSnmpObjects,'affirmedSnmpNotifications':affirmedSnmpNotifications})