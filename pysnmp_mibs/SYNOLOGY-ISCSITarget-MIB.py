#
# PySNMP MIB module SYNOLOGY-ISCSITarget-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/synology/SYNOLOGY-ISCSITarget-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
synologyiSCSITarget = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 110))
if mibBuilder.loadTexts: synologyiSCSITarget.setLastUpdated('202004150000Z')
if mibBuilder.loadTexts: synologyiSCSITarget.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
iSCSITargetTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 110, 1), )
if mibBuilder.loadTexts: iSCSITargetTable.setStatus('current')
iSCSITargetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 110, 1, 1), ).setIndexNames((0, "SYNOLOGY-ISCSITarget-MIB", "iSCSITargetInfoIndex"))
if mibBuilder.loadTexts: iSCSITargetEntry.setStatus('current')
iSCSITargetInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 110, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: iSCSITargetInfoIndex.setStatus('current')
iSCSITargetName = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 110, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSITargetName.setStatus('current')
iSCSITargetIQN = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 110, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSITargetIQN.setStatus('current')
iSCSITargetConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 110, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iSCSITargetConnectionStatus.setStatus('current')
synologyiSCSITargetConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 110, 2))
synologyiSCSITargetCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 110, 2, 1))
synologyiSCSITargetGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 110, 2, 2))
synologyiSCSITargetCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 110, 2, 1, 1)).setObjects(("SYNOLOGY-ISCSITarget-MIB", "synologyiSCSITargetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyiSCSITargetCompliance = synologyiSCSITargetCompliance.setStatus('current')
synologyiSCSITargetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 110, 2, 2, 1)).setObjects(("SYNOLOGY-ISCSITarget-MIB", "iSCSITargetName"), ("SYNOLOGY-ISCSITarget-MIB", "iSCSITargetIQN"), ("SYNOLOGY-ISCSITarget-MIB", "iSCSITargetConnectionStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyiSCSITargetGroup = synologyiSCSITargetGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-ISCSITarget-MIB", iSCSITargetIQN=iSCSITargetIQN, synologyiSCSITargetGroup=synologyiSCSITargetGroup, iSCSITargetName=iSCSITargetName, synologyiSCSITargetConformance=synologyiSCSITargetConformance, iSCSITargetEntry=iSCSITargetEntry, iSCSITargetInfoIndex=iSCSITargetInfoIndex, synologyiSCSITargetCompliances=synologyiSCSITargetCompliances, PYSNMP_MODULE_ID=synologyiSCSITarget, synologyiSCSITargetCompliance=synologyiSCSITargetCompliance, iSCSITargetConnectionStatus=iSCSITargetConnectionStatus, synologyiSCSITargetGroups=synologyiSCSITargetGroups, synologyiSCSITarget=synologyiSCSITarget, synology=synology, iSCSITargetTable=iSCSITargetTable)
