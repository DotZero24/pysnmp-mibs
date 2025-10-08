#
# PySNMP MIB module ARICENT-QoSEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siaemic/ARICENT-QoSEXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:45:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
fsQoSClassMapEntry, = mibBuilder.importSymbols("ARICENT-DIFFSERV-MIB", "fsQoSClassMapEntry")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
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
mibBuilder.exportSymbols("ARICENT-QoSEXT-MIB", smQoSExtClassMapYpDeiBit=smQoSExtClassMapYpDeiBit, smQoSClass=smQoSClass, smfutqos=smfutqos, smQoSClassMapExtEntry=smQoSClassMapExtEntry, PYSNMP_MODULE_ID=smfutqos, smQoSClassMapExtTable=smQoSClassMapExtTable)
