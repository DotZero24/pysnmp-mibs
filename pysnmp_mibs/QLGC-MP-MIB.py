#
# PySNMP MIB module QLGC-MP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/marvell/QLGC-MP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
qlogicMgmt, = mibBuilder.importSymbols("QLOGIC-SMI", "qlogicMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("QLGC-MP-MIB", PYSNMP_MODULE_ID=qlgcMaintenancePanelModule, qlgcMPStatus=qlgcMPStatus, qlgcMaintenancePanelModule=qlgcMaintenancePanelModule, qlgcMPEpromStatus=qlgcMPEpromStatus, qlgcMPGroup=qlgcMPGroup, MPEpromStatus=MPEpromStatus, qlgcMPGroups=qlgcMPGroups, qlgcMPComplianceV1=qlgcMPComplianceV1, qlgcMPStatusChange=qlgcMPStatusChange, qlgcMPNotifications=qlgcMPNotifications, qlgcMPObjects=qlgcMPObjects, qlgcMPConformance=qlgcMPConformance, qlgcMPCompliances=qlgcMPCompliances)
