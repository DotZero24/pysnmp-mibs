#
# PySNMP MIB module BTI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/bti/BTI-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:46:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
btiMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 18070, 1, 1))
btiMib.setRevisions(('2012-11-30 12:00', '2012-03-09 12:00', '2012-02-10 12:00', '2011-09-26 12:00', '2008-05-30 12:00', '2007-08-27 12:00', '2005-07-25 12:00', '2004-09-23 12:00', '2003-12-01 12:00',))
if mibBuilder.loadTexts: btiMib.setLastUpdated('201211301200Z')
if mibBuilder.loadTexts: btiMib.setOrganization('BTI Systems Inc.')
btiSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 18070))
btiModules = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 1))
btiProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2))
bti7000 = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 2))
btiems = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 4))
btiPSM = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 6))
widecastCache = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 7))
bti800 = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 8))
bti7800 = MibIdentifier((1, 3, 6, 1, 4, 1, 18070, 2, 9))
mibBuilder.exportSymbols("BTI-MIB", PYSNMP_MODULE_ID=btiMib, btiMib=btiMib, widecastCache=widecastCache, bti800=bti800, btiModules=btiModules, btiems=btiems, btiProducts=btiProducts, bti7000=bti7000, btiPSM=btiPSM, btiSystems=btiSystems, bti7800=bti7800)
