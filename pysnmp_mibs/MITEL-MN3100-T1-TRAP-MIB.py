#
# PySNMP MIB module MITEL-MN3100-T1-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mitel/MITEL-MN3100-T1-TRAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:39 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dsx1LineStatus, = mibBuilder.importSymbols("RFC1406-MIB", "dsx1LineStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MITEL-MN3100-T1-TRAP-MIB", mitelDS1Extension=mitelDS1Extension, mitelIdentification=mitelIdentification, mitelProprietary=mitelProprietary, mitelIdCallServers=mitelIdCallServers, PYSNMP_MODULE_ID=mitelDS1Extension, mitelIpera1000Notifications=mitelIpera1000Notifications, mitelMn3100dsx1LineSatusChangeNotif=mitelMn3100dsx1LineSatusChangeNotif, mitel=mitel, mitelIdCsIpera1000=mitelIdCsIpera1000)
