#
# PySNMP MIB module HM2-OEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HM2-OEM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hm2ConfigurationMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2ConfigurationMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hm2OemMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 15))
hm2OemMib.setRevisions(('2011-03-31 00:00',))
if mibBuilder.loadTexts: hm2OemMib.setLastUpdated('201103310000Z')
if mibBuilder.loadTexts: hm2OemMib.setOrganization('Hirschmann Automation and Control GmbH')
hm2OemMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 15, 1))
hm2OemID = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2OemID.setStatus('current')
mibBuilder.exportSymbols("HM2-OEM-MIB", hm2OemID=hm2OemID, hm2OemMibObjects=hm2OemMibObjects, PYSNMP_MODULE_ID=hm2OemMib, hm2OemMib=hm2OemMib)
