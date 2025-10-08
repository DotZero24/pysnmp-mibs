#
# PySNMP MIB module HPN-ICF-LPBKDT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-LPBKDT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:07:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfLpbkdt = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95))
hpnicfLpbkdt.setRevisions(('2009-03-30 17:41', '2008-09-27 15:04',))
if mibBuilder.loadTexts: hpnicfLpbkdt.setLastUpdated('200903301741Z')
if mibBuilder.loadTexts: hpnicfLpbkdt.setOrganization('')
hpnicfLpbkdtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 1))
hpnicfLpbkdtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 2))
hpnicfLpbkdtTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 1, 0))
hpnicfLpbkdtTrapLoopbacked = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 1, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hpnicfLpbkdtTrapLoopbacked.setStatus('current')
hpnicfLpbkdtTrapRecovered = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 1, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hpnicfLpbkdtTrapRecovered.setStatus('current')
hpnicfLpbkdtTrapPerVlanLoopbacked = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 1, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("HPN-ICF-LPBKDT-MIB", "hpnicfLpbkdtVlanID"))
if mibBuilder.loadTexts: hpnicfLpbkdtTrapPerVlanLoopbacked.setStatus('current')
hpnicfLpbkdtTrapPerVlanRecovered = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 1, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("HPN-ICF-LPBKDT-MIB", "hpnicfLpbkdtVlanID"))
if mibBuilder.loadTexts: hpnicfLpbkdtTrapPerVlanRecovered.setStatus('current')
hpnicfLpbkdtVlanID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 2, 1), VlanId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfLpbkdtVlanID.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-LPBKDT-MIB", hpnicfLpbkdtTrapPrefix=hpnicfLpbkdtTrapPrefix, hpnicfLpbkdt=hpnicfLpbkdt, hpnicfLpbkdtNotifications=hpnicfLpbkdtNotifications, hpnicfLpbkdtTrapLoopbacked=hpnicfLpbkdtTrapLoopbacked, hpnicfLpbkdtTrapRecovered=hpnicfLpbkdtTrapRecovered, hpnicfLpbkdtTrapPerVlanLoopbacked=hpnicfLpbkdtTrapPerVlanLoopbacked, hpnicfLpbkdtTrapPerVlanRecovered=hpnicfLpbkdtTrapPerVlanRecovered, hpnicfLpbkdtVlanID=hpnicfLpbkdtVlanID, PYSNMP_MODULE_ID=hpnicfLpbkdt, hpnicfLpbkdtObjects=hpnicfLpbkdtObjects)
