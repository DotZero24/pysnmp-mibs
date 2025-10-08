#
# PySNMP MIB module H3C-MACSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-MACSEC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:49 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cMACsec = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 163))
h3cMACsec.setRevisions(('2015-09-01 16:15',))
if mibBuilder.loadTexts: h3cMACsec.setLastUpdated('201509011615Z')
if mibBuilder.loadTexts: h3cMACsec.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cMACsecCFGObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 163, 1))
h3cMACsecCFGPortTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 163, 1, 1), )
if mibBuilder.loadTexts: h3cMACsecCFGPortTable.setStatus('current')
h3cMACsecCFGPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 163, 1, 1, 1), ).setIndexNames((0, "H3C-MACSEC-MIB", "h3cMACsecCFGPortIndex"))
if mibBuilder.loadTexts: h3cMACsecCFGPortEntry.setStatus('current')
h3cMACsecCFGPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 163, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: h3cMACsecCFGPortIndex.setStatus('current')
h3cMACsecCFGPortPSKCKNName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 163, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cMACsecCFGPortPSKCKNName.setStatus('current')
h3cMACsecCFGPortPSKCAKValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 163, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cMACsecCFGPortPSKCAKValue.setStatus('current')
mibBuilder.exportSymbols("H3C-MACSEC-MIB", PYSNMP_MODULE_ID=h3cMACsec, h3cMACsecCFGPortPSKCAKValue=h3cMACsecCFGPortPSKCAKValue, h3cMACsecCFGPortEntry=h3cMACsecCFGPortEntry, h3cMACsecCFGPortTable=h3cMACsecCFGPortTable, h3cMACsec=h3cMACsec, h3cMACsecCFGPortIndex=h3cMACsecCFGPortIndex, h3cMACsecCFGPortPSKCKNName=h3cMACsecCFGPortPSKCKNName, h3cMACsecCFGObjects=h3cMACsecCFGObjects)
