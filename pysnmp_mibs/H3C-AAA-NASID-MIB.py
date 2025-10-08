#
# PySNMP MIB module H3C-AAA-NASID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-AAA-NASID-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cAAANasId = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114))
h3cAAANasId.setRevisions(('2011-03-09 09:45',))
if mibBuilder.loadTexts: h3cAAANasId.setLastUpdated('201103090945Z')
if mibBuilder.loadTexts: h3cAAANasId.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cAAANasIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114, 1))
h3cAAANasIdTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114, 1, 1), )
if mibBuilder.loadTexts: h3cAAANasIdTable.setStatus('current')
h3cAAANasIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114, 1, 1, 1), ).setIndexNames((0, "H3C-AAA-NASID-MIB", "h3cAAANasIdName"))
if mibBuilder.loadTexts: h3cAAANasIdEntry.setStatus('current')
h3cAAANasIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 114, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAAANasIdName.setStatus('current')
mibBuilder.exportSymbols("H3C-AAA-NASID-MIB", h3cAAANasIdTable=h3cAAANasIdTable, h3cAAANasId=h3cAAANasId, h3cAAANasIdEntry=h3cAAANasIdEntry, h3cAAANasIdObjects=h3cAAANasIdObjects, PYSNMP_MODULE_ID=h3cAAANasId, h3cAAANasIdName=h3cAAANasIdName)
