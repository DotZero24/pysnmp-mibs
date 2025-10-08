#
# PySNMP MIB module JUNIPER-HOSTRESOURCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/juniper/JUNIPER-HOSTRESOURCES-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:55:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hrStorageEntry, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrStorageEntry")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("JUNIPER-HOSTRESOURCES-MIB", jnxHrStorage=jnxHrStorage, jnxHrSystemOpenFiles=jnxHrSystemOpenFiles, jnxHrStorageTable=jnxHrStorageTable, jnxHrSystem=jnxHrSystem, jnxHostResourcesMIB=jnxHostResourcesMIB, jnxHrStoragePercentUsed=jnxHrStoragePercentUsed, jnxHrStorageEntry=jnxHrStorageEntry, PYSNMP_MODULE_ID=jnxHostResourcesMIB)
