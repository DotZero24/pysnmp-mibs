#
# PySNMP MIB module ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/alcatel-ent1/ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
alcatelIND1VirtualChassisMIBVCSP, = mibBuilder.importSymbols("ALCATEL-ENT1-VIRTUAL-CHASSIS-MIB", "alcatelIND1VirtualChassisMIBVCSP")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
alaVCSPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1))
alaVCSPMIB.setRevisions(('2013-10-14 00:00',))
if mibBuilder.loadTexts: alaVCSPMIB.setLastUpdated('201310140000Z')
if mibBuilder.loadTexts: alaVCSPMIB.setOrganization('Alcatel-Lucent, Enterprise Solutions Division')
alaVCSPMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 0))
alaVCSPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1))
alaVCSPMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2))
class AlaVCSPChassisID(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8)

class AlaVCSPOpState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("protection", 2), ("inactive", 3))

class AlaVCSPState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

alaVCSPConfigInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 2))
alaVCSPAdminState = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 2, 1), AlaVCSPState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVCSPAdminState.setStatus('current')
alaVCSPLinkaggId = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 128)).clone(-1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVCSPLinkaggId.setStatus('current')
alaVCSPGuardTimer = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 100)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVCSPGuardTimer.setStatus('current')
alaVCSPUpTime = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 2, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVCSPUpTime.setStatus('current')
alaVCSPProtectionStateUpTime = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 2, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVCSPProtectionStateUpTime.setStatus('current')
alaVCSPHelperGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 1))
alaVCSPHelperAdminState = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 1, 1), AlaVCSPState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVCSPHelperAdminState.setStatus('current')
alaVCSPHelperLinkaggTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 3), )
if mibBuilder.loadTexts: alaVCSPHelperLinkaggTable.setStatus('current')
alaVCSPHelperLinkaggEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 3, 1), ).setIndexNames((0, "ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPHelperLinkaggId"))
if mibBuilder.loadTexts: alaVCSPHelperLinkaggEntry.setStatus('current')
alaVCSPHelperLinkaggId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVCSPHelperLinkaggId.setStatus('current')
alaVCSPHelperLinkaggRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVCSPHelperLinkaggRowStatus.setStatus('current')
alaVCSPStateTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 4), )
if mibBuilder.loadTexts: alaVCSPStateTable.setStatus('current')
alaVCSPStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 4, 1), ).setIndexNames((0, "ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPTableChassisID"))
if mibBuilder.loadTexts: alaVCSPStateEntry.setStatus('current')
alaVCSPTableChassisID = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 4, 1, 1), AlaVCSPChassisID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVCSPTableChassisID.setStatus('current')
alaVCSPTableOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 4, 1, 2), AlaVCSPOpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVCSPTableOperState.setStatus('current')
alaVCSPProtectionTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 0, 1)).setObjects(("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPTableChassisID"))
if mibBuilder.loadTexts: alaVCSPProtectionTrap.setStatus('current')
alaVCSPRecoveryTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 0, 2)).setObjects(("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPTableChassisID"))
if mibBuilder.loadTexts: alaVCSPRecoveryTrap.setStatus('current')
alaVCSPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2, 1))
alaVCSPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2, 2))
alaVCSPMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2, 2, 1)).setObjects(("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPNotificationGroup"), ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPConfigInfoGroup"), ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPHelperGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVCSPMIBCompliance = alaVCSPMIBCompliance.setStatus('current')
alaVCSPNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2, 1, 1)).setObjects(("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPProtectionTrap"), ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPRecoveryTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVCSPNotificationGroup = alaVCSPNotificationGroup.setStatus('current')
alaVCSPHelperGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2, 1, 3)).setObjects(("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPHelperAdminState"), ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPHelperLinkaggId"), ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPHelperLinkaggRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVCSPHelperGroup = alaVCSPHelperGroup.setStatus('current')
alaVCSPConfigInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2, 1, 2)).setObjects(("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPLinkaggId"), ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPProtectionStateUpTime"), ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPTableChassisID"), ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPTableOperState"), ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPUpTime"), ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPGuardTimer"), ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPAdminState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVCSPConfigInfoGroup = alaVCSPConfigInfoGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", alaVCSPMIBCompliance=alaVCSPMIBCompliance, alaVCSPAdminState=alaVCSPAdminState, alaVCSPHelperAdminState=alaVCSPHelperAdminState, AlaVCSPChassisID=AlaVCSPChassisID, AlaVCSPOpState=AlaVCSPOpState, alaVCSPNotificationGroup=alaVCSPNotificationGroup, AlaVCSPState=AlaVCSPState, alaVCSPProtectionTrap=alaVCSPProtectionTrap, alaVCSPHelperGroup=alaVCSPHelperGroup, alaVCSPMIB=alaVCSPMIB, alaVCSPHelperLinkaggEntry=alaVCSPHelperLinkaggEntry, alaVCSPConfigInfo=alaVCSPConfigInfo, alaVCSPStateTable=alaVCSPStateTable, PYSNMP_MODULE_ID=alaVCSPMIB, alaVCSPGuardTimer=alaVCSPGuardTimer, alaVCSPMIBGroups=alaVCSPMIBGroups, alaVCSPHelperLinkaggId=alaVCSPHelperLinkaggId, alaVCSPProtectionStateUpTime=alaVCSPProtectionStateUpTime, alaVCSPMIBNotifications=alaVCSPMIBNotifications, alaVCSPHelperGlobalConfig=alaVCSPHelperGlobalConfig, alaVCSPConfigInfoGroup=alaVCSPConfigInfoGroup, alaVCSPHelperLinkaggTable=alaVCSPHelperLinkaggTable, alaVCSPTableChassisID=alaVCSPTableChassisID, alaVCSPTableOperState=alaVCSPTableOperState, alaVCSPHelperLinkaggRowStatus=alaVCSPHelperLinkaggRowStatus, alaVCSPLinkaggId=alaVCSPLinkaggId, alaVCSPRecoveryTrap=alaVCSPRecoveryTrap, alaVCSPMIBConformance=alaVCSPMIBConformance, alaVCSPMIBObjects=alaVCSPMIBObjects, alaVCSPMIBCompliances=alaVCSPMIBCompliances, alaVCSPStateEntry=alaVCSPStateEntry, alaVCSPUpTime=alaVCSPUpTime)
