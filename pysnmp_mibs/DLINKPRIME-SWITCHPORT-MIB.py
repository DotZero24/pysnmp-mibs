#
# PySNMP MIB module DLINKPRIME-SWITCHPORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINKPRIME-SWITCHPORT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:58:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
dlinkPrimeSwitchPortMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 20))
dlinkPrimeSwitchPortMIB.setRevisions(('2014-05-07 00:00',))
if mibBuilder.loadTexts: dlinkPrimeSwitchPortMIB.setLastUpdated('201405070000Z')
if mibBuilder.loadTexts: dlinkPrimeSwitchPortMIB.setOrganization('D-Link Corp.')
dpSwPortNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 20, 0))
dpSwPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 20, 1))
dpSwPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 20, 2))
dpSwPortIfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 15, 20, 1, 1), )
if mibBuilder.loadTexts: dpSwPortIfTable.setStatus('current')
dpSwPortIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 15, 20, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dpSwPortIfEntry.setStatus('current')
dpSwPortIfMdix = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 20, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("normal", 2), ("cross", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpSwPortIfMdix.setStatus('current')
dpSwPortIfJumboFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 20, 1, 1, 1, 2), Unsigned32().clone(1518)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpSwPortIfJumboFrameSize.setStatus('current')
dpSwPortIfSpeedAutoDowngrade = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 20, 1, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpSwPortIfSpeedAutoDowngrade.setStatus('current')
dpSwPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 20, 2, 1))
dpSwPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 15, 20, 2, 1, 1)).setObjects(("DLINKPRIME-SWITCHPORT-MIB", "dpSwPortBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpSwPortCompliance = dpSwPortCompliance.setStatus('current')
dpSwPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 20, 2, 2))
dpSwPortBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 20, 2, 2, 1)).setObjects(("DLINKPRIME-SWITCHPORT-MIB", "dpSwPortIfMdix"), ("DLINKPRIME-SWITCHPORT-MIB", "dpSwPortIfJumboFrameSize"), ("DLINKPRIME-SWITCHPORT-MIB", "dpSwPortIfSpeedAutoDowngrade"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpSwPortBasicGroup = dpSwPortBasicGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKPRIME-SWITCHPORT-MIB", dlinkPrimeSwitchPortMIB=dlinkPrimeSwitchPortMIB, dpSwPortCompliance=dpSwPortCompliance, dpSwPortIfMdix=dpSwPortIfMdix, dpSwPortGroups=dpSwPortGroups, dpSwPortCompliances=dpSwPortCompliances, dpSwPortIfSpeedAutoDowngrade=dpSwPortIfSpeedAutoDowngrade, dpSwPortObjects=dpSwPortObjects, dpSwPortIfTable=dpSwPortIfTable, dpSwPortIfEntry=dpSwPortIfEntry, PYSNMP_MODULE_ID=dlinkPrimeSwitchPortMIB, dpSwPortBasicGroup=dpSwPortBasicGroup, dpSwPortConformance=dpSwPortConformance, dpSwPortNotifications=dpSwPortNotifications, dpSwPortIfJumboFrameSize=dpSwPortIfJumboFrameSize)
