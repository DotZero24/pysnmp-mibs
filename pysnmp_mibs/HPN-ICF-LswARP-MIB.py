#
# PySNMP MIB module HPN-ICF-LswARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-LswARP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicflswCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicflswCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfLswArpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4))
hpnicfLswArpMib.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hpnicfLswArpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hpnicfLswArpMib.setOrganization('')
hpnicfLswProxyArpObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1))
if mibBuilder.loadTexts: hpnicfLswProxyArpObject.setStatus('current')
hpnicfLswProxyArpEnableTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1), )
if mibBuilder.loadTexts: hpnicfLswProxyArpEnableTable.setStatus('current')
hpnicfLswProxyArpEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-LswARP-MIB", "hpnicfLswIfIndex"))
if mibBuilder.loadTexts: hpnicfLswProxyArpEnableEntry.setStatus('current')
hpnicfLswIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLswIfIndex.setStatus('current')
hpnicfLswProxyArpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfLswProxyArpStatus.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-LswARP-MIB", hpnicfLswProxyArpEnableEntry=hpnicfLswProxyArpEnableEntry, hpnicfLswProxyArpObject=hpnicfLswProxyArpObject, hpnicfLswIfIndex=hpnicfLswIfIndex, PYSNMP_MODULE_ID=hpnicfLswArpMib, hpnicfLswProxyArpEnableTable=hpnicfLswProxyArpEnableTable, hpnicfLswProxyArpStatus=hpnicfLswProxyArpStatus, hpnicfLswArpMib=hpnicfLswArpMib)
