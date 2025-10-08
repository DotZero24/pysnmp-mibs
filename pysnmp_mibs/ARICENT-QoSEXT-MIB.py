#
# PySNMP MIB module ARICENT-QoSEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siaemic/ARICENT-QoSEXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
fsQoSClassMapEntry, = mibBuilder.importSymbols("ARICENT-DIFFSERV-MIB", "fsQoSClassMapEntry")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
smfutqos = ModuleIdentity((1, 3, 6, 1, 4, 1, 29601, 100, 1, 3))
if mibBuilder.loadTexts: smfutqos.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: smfutqos.setOrganization('ARICENT COMMUNICATIONS SOFTWARE')
smQoSClass = MibIdentifier((1, 3, 6, 1, 4, 1, 29601, 100, 1, 3, 1))
smQoSClassMapExtTable = MibTable((1, 3, 6, 1, 4, 1, 29601, 100, 1, 3, 1, 1), )
if mibBuilder.loadTexts: smQoSClassMapExtTable.setStatus('current')
smQoSClassMapExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 29601, 100, 1, 3, 1, 1, 1), )
fsQoSClassMapEntry.registerAugmentions(("ARICENT-QoSEXT-MIB", "smQoSClassMapExtEntry"))
smQoSClassMapExtEntry.setIndexNames(*fsQoSClassMapEntry.getIndexNames())
if mibBuilder.loadTexts: smQoSClassMapExtEntry.setStatus('current')
smQoSExtClassMapYpDeiBit = MibTableColumn((1, 3, 6, 1, 4, 1, 29601, 100, 1, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("reset", 0), ("set", 1), ("None", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smQoSExtClassMapYpDeiBit.setStatus('current')
mibBuilder.exportSymbols("ARICENT-QoSEXT-MIB", smQoSClass=smQoSClass, PYSNMP_MODULE_ID=smfutqos, smQoSClassMapExtTable=smQoSClassMapExtTable, smfutqos=smfutqos, smQoSClassMapExtEntry=smQoSClassMapExtEntry, smQoSExtClassMapYpDeiBit=smQoSExtClassMapYpDeiBit)
