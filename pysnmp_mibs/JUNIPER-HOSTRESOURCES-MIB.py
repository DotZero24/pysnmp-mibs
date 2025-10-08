#
# PySNMP MIB module JUNIPER-HOSTRESOURCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/juniper/JUNIPER-HOSTRESOURCES-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:31:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hrStorageEntry, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrStorageEntry")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxHostResourcesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 31))
jnxHostResourcesMIB.setRevisions(('2004-08-18 00:00', '2004-05-05 00:00',))
if mibBuilder.loadTexts: jnxHostResourcesMIB.setLastUpdated('200408180000Z')
if mibBuilder.loadTexts: jnxHostResourcesMIB.setOrganization('Juniper Networks, Inc.')
jnxHrStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1))
jnxHrSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 31, 2))
jnxHrStorageTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1), )
if mibBuilder.loadTexts: jnxHrStorageTable.setStatus('current')
jnxHrStorageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1, 1), )
hrStorageEntry.registerAugmentions(("JUNIPER-HOSTRESOURCES-MIB", "jnxHrStorageEntry"))
jnxHrStorageEntry.setIndexNames(*hrStorageEntry.getIndexNames())
if mibBuilder.loadTexts: jnxHrStorageEntry.setStatus('current')
jnxHrStoragePercentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxHrStoragePercentUsed.setStatus('current')
jnxHrSystemOpenFiles = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 31, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxHrSystemOpenFiles.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-HOSTRESOURCES-MIB", jnxHrSystemOpenFiles=jnxHrSystemOpenFiles, jnxHostResourcesMIB=jnxHostResourcesMIB, jnxHrStoragePercentUsed=jnxHrStoragePercentUsed, PYSNMP_MODULE_ID=jnxHostResourcesMIB, jnxHrStorageEntry=jnxHrStorageEntry, jnxHrSystem=jnxHrSystem, jnxHrStorage=jnxHrStorage, jnxHrStorageTable=jnxHrStorageTable)
