#
# PySNMP MIB module HPICF-ACTIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPICF-ACTIVATE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:39 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
hpicfActivateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129))
hpicfActivateMIB.setRevisions(('2020-06-20 00:00', '2016-05-03 00:00',))
if mibBuilder.loadTexts: hpicfActivateMIB.setLastUpdated('202006200000Z')
if mibBuilder.loadTexts: hpicfActivateMIB.setOrganization('HPE Networking')
hpicfActivateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1))
hpicfActivateConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2))
hpicfActivateSoftwareUpdateMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfActivateSoftwareUpdateMode.setStatus('current')
hpicfActivateProvisionMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfActivateProvisionMode.setStatus('current')
hpicfActivateOverrideConfigCheck = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfActivateOverrideConfigCheck.setStatus('current')
hpicfActivateMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 1))
hpicfActivateMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 2))
hpicfActivateMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 1, 1)).setObjects(("HPICF-ACTIVATE-MIB", "hpicfActivateConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfActivateMIBCompliance = hpicfActivateMIBCompliance.setStatus('deprecated')
hpicfActivateConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 2, 1)).setObjects(("HPICF-ACTIVATE-MIB", "hpicfActivateSoftwareUpdateMode"), ("HPICF-ACTIVATE-MIB", "hpicfActivateProvisionMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfActivateConfigGroup = hpicfActivateConfigGroup.setStatus('deprecated')
hpicfActivateMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 1, 2)).setObjects(("HPICF-ACTIVATE-MIB", "hpicfActivateConfigGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfActivateMIBCompliance1 = hpicfActivateMIBCompliance1.setStatus('current')
hpicfActivateConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 2, 2)).setObjects(("HPICF-ACTIVATE-MIB", "hpicfActivateSoftwareUpdateMode"), ("HPICF-ACTIVATE-MIB", "hpicfActivateProvisionMode"), ("HPICF-ACTIVATE-MIB", "hpicfActivateOverrideConfigCheck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfActivateConfigGroup1 = hpicfActivateConfigGroup1.setStatus('current')
mibBuilder.exportSymbols("HPICF-ACTIVATE-MIB", hpicfActivateMIBGroups=hpicfActivateMIBGroups, hpicfActivateSoftwareUpdateMode=hpicfActivateSoftwareUpdateMode, hpicfActivateMIB=hpicfActivateMIB, hpicfActivateObjects=hpicfActivateObjects, hpicfActivateProvisionMode=hpicfActivateProvisionMode, hpicfActivateConfigGroup=hpicfActivateConfigGroup, hpicfActivateConfigGroup1=hpicfActivateConfigGroup1, hpicfActivateMIBCompliance=hpicfActivateMIBCompliance, hpicfActivateMIBCompliance1=hpicfActivateMIBCompliance1, hpicfActivateMIBCompliances=hpicfActivateMIBCompliances, PYSNMP_MODULE_ID=hpicfActivateMIB, hpicfActivateConformance=hpicfActivateConformance, hpicfActivateOverrideConfigCheck=hpicfActivateOverrideConfigCheck)
