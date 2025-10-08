#
# PySNMP MIB module RADLAN-SNA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/radlan/RADLAN-SNA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:07:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TestAndIncr")
rlSna = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 229))
rlSna.setRevisions(('2015-05-12 00:00',))
if mibBuilder.loadTexts: rlSna.setLastUpdated('201101050000Z')
if mibBuilder.loadTexts: rlSna.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlSnaNextFreeSessionId = MibScalar((1, 3, 6, 1, 4, 1, 89, 229, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSnaNextFreeSessionId.setStatus('current')
mibBuilder.exportSymbols("RADLAN-SNA-MIB", rlSnaNextFreeSessionId=rlSnaNextFreeSessionId, PYSNMP_MODULE_ID=rlSna, rlSna=rlSna)
