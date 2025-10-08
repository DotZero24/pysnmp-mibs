#
# PySNMP MIB module DLINKPRIME-SWITCHPORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINKPRIME-SWITCHPORT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:58 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("DLINKPRIME-SWITCHPORT-MIB", dpSwPortIfTable=dpSwPortIfTable, dpSwPortCompliance=dpSwPortCompliance, dlinkPrimeSwitchPortMIB=dlinkPrimeSwitchPortMIB, PYSNMP_MODULE_ID=dlinkPrimeSwitchPortMIB, dpSwPortNotifications=dpSwPortNotifications, dpSwPortIfJumboFrameSize=dpSwPortIfJumboFrameSize, dpSwPortIfSpeedAutoDowngrade=dpSwPortIfSpeedAutoDowngrade, dpSwPortCompliances=dpSwPortCompliances, dpSwPortObjects=dpSwPortObjects, dpSwPortConformance=dpSwPortConformance, dpSwPortIfMdix=dpSwPortIfMdix, dpSwPortGroups=dpSwPortGroups, dpSwPortIfEntry=dpSwPortIfEntry, dpSwPortBasicGroup=dpSwPortBasicGroup)
