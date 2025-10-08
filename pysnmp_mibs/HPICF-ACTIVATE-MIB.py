#
# PySNMP MIB module HPICF-ACTIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPICF-ACTIVATE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HPICF-ACTIVATE-MIB", hpicfActivateOverrideConfigCheck=hpicfActivateOverrideConfigCheck, hpicfActivateMIBCompliance1=hpicfActivateMIBCompliance1, hpicfActivateMIBCompliance=hpicfActivateMIBCompliance, PYSNMP_MODULE_ID=hpicfActivateMIB, hpicfActivateObjects=hpicfActivateObjects, hpicfActivateMIB=hpicfActivateMIB, hpicfActivateMIBCompliances=hpicfActivateMIBCompliances, hpicfActivateProvisionMode=hpicfActivateProvisionMode, hpicfActivateConfigGroup=hpicfActivateConfigGroup, hpicfActivateSoftwareUpdateMode=hpicfActivateSoftwareUpdateMode, hpicfActivateConformance=hpicfActivateConformance, hpicfActivateMIBGroups=hpicfActivateMIBGroups, hpicfActivateConfigGroup1=hpicfActivateConfigGroup1)
