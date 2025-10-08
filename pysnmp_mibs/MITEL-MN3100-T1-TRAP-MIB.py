#
# PySNMP MIB module MITEL-MN3100-T1-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mitel/MITEL-MN3100-T1-TRAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dsx1LineStatus, = mibBuilder.importSymbols("RFC1406-MIB", "dsx1LineStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mitelDS1Extension = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 12))
mitelDS1Extension.setRevisions(('2003-03-24 01:41', '2002-04-02 00:00',))
if mibBuilder.loadTexts: mitelDS1Extension.setLastUpdated('200204020000Z')
if mibBuilder.loadTexts: mitelDS1Extension.setOrganization('MITEL Networks Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelIdentification = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1))
mitelIdCallServers = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2))
mitelIdCsIpera1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4))
mitelIpera1000Notifications = NotificationGroup((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0)).setObjects(("MITEL-MN3100-T1-TRAP-MIB", "mitelMn3100dsx1LineSatusChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mitelIpera1000Notifications = mitelIpera1000Notifications.setStatus('current')
mitelMn3100dsx1LineSatusChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 410)).setObjects(("RFC1406-MIB", "dsx1LineStatus"))
if mibBuilder.loadTexts: mitelMn3100dsx1LineSatusChangeNotif.setStatus('current')
mibBuilder.exportSymbols("MITEL-MN3100-T1-TRAP-MIB", mitelIdCallServers=mitelIdCallServers, mitelIpera1000Notifications=mitelIpera1000Notifications, mitelMn3100dsx1LineSatusChangeNotif=mitelMn3100dsx1LineSatusChangeNotif, mitelProprietary=mitelProprietary, mitelIdCsIpera1000=mitelIdCsIpera1000, mitel=mitel, PYSNMP_MODULE_ID=mitelDS1Extension, mitelIdentification=mitelIdentification, mitelDS1Extension=mitelDS1Extension)
