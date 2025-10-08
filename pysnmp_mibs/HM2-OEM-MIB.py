#
# PySNMP MIB module HM2-OEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HM2-OEM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hm2ConfigurationMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2ConfigurationMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2OemMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 15))
hm2OemMib.setRevisions(('2011-03-31 00:00',))
if mibBuilder.loadTexts: hm2OemMib.setLastUpdated('201103310000Z')
if mibBuilder.loadTexts: hm2OemMib.setOrganization('Hirschmann Automation and Control GmbH')
hm2OemMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 15, 1))
hm2OemID = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2OemID.setStatus('current')
mibBuilder.exportSymbols("HM2-OEM-MIB", hm2OemMibObjects=hm2OemMibObjects, hm2OemMib=hm2OemMib, PYSNMP_MODULE_ID=hm2OemMib, hm2OemID=hm2OemID)
