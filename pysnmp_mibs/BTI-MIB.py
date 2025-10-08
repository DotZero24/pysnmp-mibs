#
# PySNMP MIB module BTI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/bti/BTI-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BTI-MIB", bti7800=bti7800, widecastCache=widecastCache, btiSystems=btiSystems, btiModules=btiModules, bti7000=bti7000, btiPSM=btiPSM, PYSNMP_MODULE_ID=btiMib, btiProducts=btiProducts, bti800=bti800, btiems=btiems, btiMib=btiMib)
