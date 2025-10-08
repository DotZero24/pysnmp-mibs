#
# PySNMP MIB module H3C-MACSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/H3C-MACSEC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("H3C-MACSEC-MIB", h3cMACsecCFGPortEntry=h3cMACsecCFGPortEntry, PYSNMP_MODULE_ID=h3cMACsec, h3cMACsecCFGPortIndex=h3cMACsecCFGPortIndex, h3cMACsec=h3cMACsec, h3cMACsecCFGPortPSKCAKValue=h3cMACsecCFGPortPSKCAKValue, h3cMACsecCFGObjects=h3cMACsecCFGObjects, h3cMACsecCFGPortTable=h3cMACsecCFGPortTable, h3cMACsecCFGPortPSKCKNName=h3cMACsecCFGPortPSKCKNName)
