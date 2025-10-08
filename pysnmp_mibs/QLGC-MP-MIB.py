#
# PySNMP MIB module QLGC-MP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/marvell/QLGC-MP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
qlogicMgmt, = mibBuilder.importSymbols("QLOGIC-SMI", "qlogicMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qlgcMaintenancePanelModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3873, 3, 2))
qlgcMaintenancePanelModule.setRevisions(('2009-09-29 00:00', '2007-03-31 00:00',))
if mibBuilder.loadTexts: qlgcMaintenancePanelModule.setLastUpdated('200909290000Z')
if mibBuilder.loadTexts: qlgcMaintenancePanelModule.setOrganization('QLogic Corp.')
qlgcMPNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 3, 2, 0))
qlgcMPObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 3, 2, 1))
qlgcMPConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 3, 2, 2))
class MPEpromStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("alarm", 2))

qlgcMPStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 3, 2, 1, 1))
qlgcMPEpromStatus = MibScalar((1, 3, 6, 1, 4, 1, 3873, 3, 2, 1, 1, 1), MPEpromStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qlgcMPEpromStatus.setStatus('current')
qlgcMPStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 3873, 3, 2, 0, 1)).setObjects(("QLGC-MP-MIB", "qlgcMPEpromStatus"))
if mibBuilder.loadTexts: qlgcMPStatusChange.setStatus('current')
qlgcMPGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 3, 2, 2, 1))
qlgcMPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3873, 3, 2, 2, 1, 1)).setObjects(("QLGC-MP-MIB", "qlgcMPEpromStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qlgcMPGroup = qlgcMPGroup.setStatus('current')
qlgcMPCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 3, 2, 2, 2))
qlgcMPComplianceV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 3873, 3, 2, 2, 2, 1)).setObjects(("QLGC-MP-MIB", "qlgcMPGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qlgcMPComplianceV1 = qlgcMPComplianceV1.setStatus('current')
mibBuilder.exportSymbols("QLGC-MP-MIB", qlgcMPGroups=qlgcMPGroups, qlgcMaintenancePanelModule=qlgcMaintenancePanelModule, MPEpromStatus=MPEpromStatus, qlgcMPGroup=qlgcMPGroup, PYSNMP_MODULE_ID=qlgcMaintenancePanelModule, qlgcMPNotifications=qlgcMPNotifications, qlgcMPEpromStatus=qlgcMPEpromStatus, qlgcMPCompliances=qlgcMPCompliances, qlgcMPStatusChange=qlgcMPStatusChange, qlgcMPComplianceV1=qlgcMPComplianceV1, qlgcMPConformance=qlgcMPConformance, qlgcMPStatus=qlgcMPStatus, qlgcMPObjects=qlgcMPObjects)
