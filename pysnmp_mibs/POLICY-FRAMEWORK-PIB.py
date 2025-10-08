#
# PySNMP MIB module POLICY-FRAMEWORK-PIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/POLICY-FRAMEWORK-PIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
policy, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "policy")
policyFrameworkPib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 4, 1))
policyFrameworkPib.setRevisions(('2004-07-20 00:00',))
if mibBuilder.loadTexts: policyFrameworkPib.setLastUpdated('200407200000Z')
if mibBuilder.loadTexts: policyFrameworkPib.setOrganization('IETF RAP WG')
policyBasePibClass = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 1, 1))
class Role(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class RoleCombination(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class PolicyInstanceId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

policyPrcSupportTable = MibTable((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1), )
if mibBuilder.loadTexts: policyPrcSupportTable.setStatus('current')
policyPrcSupportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1), ).setIndexNames((0, "POLICY-FRAMEWORK-PIB", "policyPrcSupportPrid"))
if mibBuilder.loadTexts: policyPrcSupportEntry.setStatus('current')
policyPrcSupportPrid = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1, 1), PolicyInstanceId())
if mibBuilder.loadTexts: policyPrcSupportPrid.setStatus('current')
policyPrcSupportSupportedPrc = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyPrcSupportSupportedPrc.setStatus('current')
policyPrcSupportSupportedAttrs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyPrcSupportSupportedAttrs.setStatus('current')
policyPrcSupportMaxPris = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyPrcSupportMaxPris.setStatus('current')
policyPibIncarnationTable = MibTable((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2), )
if mibBuilder.loadTexts: policyPibIncarnationTable.setStatus('current')
policyPibIncarnationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1), ).setIndexNames((0, "POLICY-FRAMEWORK-PIB", "policyPibIncarnationPrid"))
if mibBuilder.loadTexts: policyPibIncarnationEntry.setStatus('current')
policyPibIncarnationPrid = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 1), PolicyInstanceId())
if mibBuilder.loadTexts: policyPibIncarnationPrid.setStatus('current')
policyPibIncarnationName = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyPibIncarnationName.setStatus('current')
policyPibIncarnationId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyPibIncarnationId.setStatus('current')
policyPibIncarnationLongevity = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("expireNever", 1), ("expireImmediate", 2), ("expireOnTimeout", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyPibIncarnationLongevity.setStatus('current')
policyPibIncarnationTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyPibIncarnationTtl.setStatus('current')
policyPibIncarnationActive = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyPibIncarnationActive.setStatus('current')
policyDeviceIdentificationTable = MibTable((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3), )
if mibBuilder.loadTexts: policyDeviceIdentificationTable.setStatus('current')
policyDeviceIdentificationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3, 1), ).setIndexNames((0, "POLICY-FRAMEWORK-PIB", "policyDeviceIdentificationPrid"))
if mibBuilder.loadTexts: policyDeviceIdentificationEntry.setStatus('current')
policyDeviceIdentificationPrid = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3, 1, 1), PolicyInstanceId())
if mibBuilder.loadTexts: policyDeviceIdentificationPrid.setStatus('current')
policyDeviceIdentificationDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyDeviceIdentificationDescr.setStatus('current')
policyDeviceIdentificationMaxMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyDeviceIdentificationMaxMsg.setStatus('current')
policyCompLimitsTable = MibTable((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4), )
if mibBuilder.loadTexts: policyCompLimitsTable.setStatus('current')
policyCompLimitsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1), ).setIndexNames((0, "POLICY-FRAMEWORK-PIB", "policyCompLimitsPrid"))
if mibBuilder.loadTexts: policyCompLimitsEntry.setStatus('current')
policyCompLimitsPrid = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1, 1), PolicyInstanceId())
if mibBuilder.loadTexts: policyCompLimitsPrid.setStatus('current')
policyCompLimitsComponent = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyCompLimitsComponent.setStatus('current')
policyCompLimitsType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyCompLimitsType.setStatus('current')
policyCompLimitsGuidance = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: policyCompLimitsGuidance.setStatus('current')
policyBasePibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 1, 2))
policyBasePibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 1))
policyBasePibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2))
policyBasePibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 1, 1)).setObjects(("POLICY-FRAMEWORK-PIB", "policyPrcSupportGroup"), ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationGroup"), ("POLICY-FRAMEWORK-PIB", "policyDeviceIdentificationGroup"), ("POLICY-FRAMEWORK-PIB", "policyCompLimitsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyBasePibCompliance = policyBasePibCompliance.setStatus('current')
policyPrcSupportGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2, 1)).setObjects(("POLICY-FRAMEWORK-PIB", "policyPrcSupportSupportedPrc"), ("POLICY-FRAMEWORK-PIB", "policyPrcSupportSupportedAttrs"), ("POLICY-FRAMEWORK-PIB", "policyPrcSupportMaxPris"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyPrcSupportGroup = policyPrcSupportGroup.setStatus('current')
policyPibIncarnationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2, 2)).setObjects(("POLICY-FRAMEWORK-PIB", "policyPibIncarnationName"), ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationId"), ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationLongevity"), ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationTtl"), ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationActive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyPibIncarnationGroup = policyPibIncarnationGroup.setStatus('current')
policyDeviceIdentificationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2, 3)).setObjects(("POLICY-FRAMEWORK-PIB", "policyDeviceIdentificationDescr"), ("POLICY-FRAMEWORK-PIB", "policyDeviceIdentificationMaxMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyDeviceIdentificationGroup = policyDeviceIdentificationGroup.setStatus('current')
policyCompLimitsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2, 4)).setObjects(("POLICY-FRAMEWORK-PIB", "policyCompLimitsComponent"), ("POLICY-FRAMEWORK-PIB", "policyCompLimitsType"), ("POLICY-FRAMEWORK-PIB", "policyCompLimitsGuidance"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyCompLimitsGroup = policyCompLimitsGroup.setStatus('current')
mibBuilder.exportSymbols("POLICY-FRAMEWORK-PIB", policyPibIncarnationTable=policyPibIncarnationTable, policyDeviceIdentificationTable=policyDeviceIdentificationTable, policyCompLimitsEntry=policyCompLimitsEntry, policyPrcSupportGroup=policyPrcSupportGroup, policyPrcSupportSupportedAttrs=policyPrcSupportSupportedAttrs, policyDeviceIdentificationGroup=policyDeviceIdentificationGroup, Role=Role, policyDeviceIdentificationMaxMsg=policyDeviceIdentificationMaxMsg, policyBasePibClass=policyBasePibClass, policyPibIncarnationId=policyPibIncarnationId, policyPrcSupportMaxPris=policyPrcSupportMaxPris, policyPibIncarnationActive=policyPibIncarnationActive, policyCompLimitsPrid=policyCompLimitsPrid, policyCompLimitsComponent=policyCompLimitsComponent, policyCompLimitsGuidance=policyCompLimitsGuidance, policyPibIncarnationGroup=policyPibIncarnationGroup, policyPibIncarnationName=policyPibIncarnationName, policyFrameworkPib=policyFrameworkPib, PYSNMP_MODULE_ID=policyFrameworkPib, policyPibIncarnationLongevity=policyPibIncarnationLongevity, policyDeviceIdentificationPrid=policyDeviceIdentificationPrid, policyPrcSupportEntry=policyPrcSupportEntry, policyDeviceIdentificationEntry=policyDeviceIdentificationEntry, policyCompLimitsTable=policyCompLimitsTable, policyPibIncarnationPrid=policyPibIncarnationPrid, policyPibIncarnationEntry=policyPibIncarnationEntry, policyBasePibGroups=policyBasePibGroups, policyCompLimitsType=policyCompLimitsType, policyBasePibCompliances=policyBasePibCompliances, policyPibIncarnationTtl=policyPibIncarnationTtl, policyBasePibCompliance=policyBasePibCompliance, RoleCombination=RoleCombination, PolicyInstanceId=PolicyInstanceId, policyPrcSupportSupportedPrc=policyPrcSupportSupportedPrc, policyPrcSupportPrid=policyPrcSupportPrid, policyCompLimitsGroup=policyCompLimitsGroup, policyPrcSupportTable=policyPrcSupportTable, policyBasePibConformance=policyBasePibConformance, policyDeviceIdentificationDescr=policyDeviceIdentificationDescr)
