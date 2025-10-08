#
# PySNMP MIB module A3COM-HUAWEI-AAA-NASID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-AAA-NASID-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cAAANasId = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114))
h3cAAANasId.setRevisions(('2011-03-09 09:45',))
if mibBuilder.loadTexts: h3cAAANasId.setLastUpdated('201103090945Z')
if mibBuilder.loadTexts: h3cAAANasId.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cAAANasIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1))
h3cAAANasIdTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1, 1), )
if mibBuilder.loadTexts: h3cAAANasIdTable.setStatus('current')
h3cAAANasIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-AAA-NASID-MIB", "h3cAAANasIdName"))
if mibBuilder.loadTexts: h3cAAANasIdEntry.setStatus('current')
h3cAAANasIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAAANasIdName.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-AAA-NASID-MIB", PYSNMP_MODULE_ID=h3cAAANasId, h3cAAANasIdObjects=h3cAAANasIdObjects, h3cAAANasIdEntry=h3cAAANasIdEntry, h3cAAANasIdTable=h3cAAANasIdTable, h3cAAANasId=h3cAAANasId, h3cAAANasIdName=h3cAAANasIdName)
