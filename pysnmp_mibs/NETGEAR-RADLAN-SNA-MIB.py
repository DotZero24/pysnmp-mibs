#
# PySNMP MIB module NETGEAR-RADLAN-SNA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netgear/NETGEAR-RADLAN-SNA-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:28:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("NETGEAR-RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
TestAndIncr, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "DisplayString", "TextualConvention")
rlSna = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 17, 229))
rlSna.setRevisions(('2015-05-12 00:00',))
if mibBuilder.loadTexts: rlSna.setLastUpdated('201101050000Z')
if mibBuilder.loadTexts: rlSna.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlSnaNextFreeSessionId = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 229, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSnaNextFreeSessionId.setStatus('current')
mibBuilder.exportSymbols("NETGEAR-RADLAN-SNA-MIB", PYSNMP_MODULE_ID=rlSna, rlSna=rlSna, rlSnaNextFreeSessionId=rlSnaNextFreeSessionId)
