#
# PySNMP MIB module SYNOLOGY-ISCSITarget-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/synology/SYNOLOGY-ISCSITarget-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SYNOLOGY-ISCSITarget-MIB", synologyiSCSITargetCompliance=synologyiSCSITargetCompliance, iSCSITargetEntry=iSCSITargetEntry, iSCSITargetInfoIndex=iSCSITargetInfoIndex, iSCSITargetName=iSCSITargetName, synologyiSCSITargetGroups=synologyiSCSITargetGroups, synology=synology, PYSNMP_MODULE_ID=synologyiSCSITarget, synologyiSCSITargetConformance=synologyiSCSITargetConformance, synologyiSCSITargetGroup=synologyiSCSITargetGroup, iSCSITargetTable=iSCSITargetTable, iSCSITargetConnectionStatus=iSCSITargetConnectionStatus, synologyiSCSITargetCompliances=synologyiSCSITargetCompliances, synologyiSCSITarget=synologyiSCSITarget, iSCSITargetIQN=iSCSITargetIQN)
