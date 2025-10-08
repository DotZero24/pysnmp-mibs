#
# PySNMP MIB module HPN-ICF-LPBKDT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-LPBKDT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("HPN-ICF-LPBKDT-MIB", hpnicfLpbkdtTrapPerVlanRecovered=hpnicfLpbkdtTrapPerVlanRecovered, hpnicfLpbkdt=hpnicfLpbkdt, hpnicfLpbkdtObjects=hpnicfLpbkdtObjects, PYSNMP_MODULE_ID=hpnicfLpbkdt, hpnicfLpbkdtTrapRecovered=hpnicfLpbkdtTrapRecovered, hpnicfLpbkdtTrapLoopbacked=hpnicfLpbkdtTrapLoopbacked, hpnicfLpbkdtNotifications=hpnicfLpbkdtNotifications, hpnicfLpbkdtVlanID=hpnicfLpbkdtVlanID, hpnicfLpbkdtTrapPerVlanLoopbacked=hpnicfLpbkdtTrapPerVlanLoopbacked, hpnicfLpbkdtTrapPrefix=hpnicfLpbkdtTrapPrefix)
