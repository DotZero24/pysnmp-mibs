#
# PySNMP MIB module ENTERASYS-ACTIVATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-ACTIVATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
etsysActivationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999))
etsysActivationMIB.setRevisions(('2002-04-18 14:54',))
if mibBuilder.loadTexts: etsysActivationMIB.setLastUpdated('200204181454Z')
if mibBuilder.loadTexts: etsysActivationMIB.setOrganization('Enterasys Networks, Inc')
etsysActivationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1))
class EnterasysKeyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noKey", 1), ("unknownKeyType", 2), ("productKey", 3), ("demoKey", 4))

class EnterasysFeature(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("dot1xAuthentication", 1), ("pointToMultipoint", 2))

etsysActivationBaseBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1))
etsysMaxActivationKeyRow = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMaxActivationKeyRow.setStatus('current')
etsysActivationKeyTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2), )
if mibBuilder.loadTexts: etsysActivationKeyTable.setStatus('current')
etsysActivationKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1), ).setIndexNames((0, "ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyRow"))
if mibBuilder.loadTexts: etsysActivationKeyEntry.setStatus('current')
etsysActivationKeyRow = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: etsysActivationKeyRow.setStatus('current')
etsysActivationLicenseString = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysActivationLicenseString.setStatus('current')
etsysActivationKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysActivationKeyValue.setStatus('current')
etsysActivationKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 4), EnterasysKeyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysActivationKeyType.setStatus('current')
etsysActivationKeyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysActivationKeyStatus.setStatus('current')
etsysActivationKeyFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3), )
if mibBuilder.loadTexts: etsysActivationKeyFeatureTable.setStatus('current')
etsysActivationKeyFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3, 1), ).setIndexNames((0, "ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyRow"), (0, "ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyFeature"))
if mibBuilder.loadTexts: etsysActivationKeyFeatureEntry.setStatus('current')
etsysActivationKeyFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3, 1, 1), EnterasysFeature())
if mibBuilder.loadTexts: etsysActivationKeyFeature.setStatus('current')
etsysActivationKeyRestrictions = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 1, 1, 3, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysActivationKeyRestrictions.setStatus('current')
etsysActivationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2))
etsysActivationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 1))
etsysActivationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 2))
etsysActivationBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 1, 1)).setObjects(("ENTERASYS-ACTIVATION-MIB", "etsysMaxActivationKeyRow"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationLicenseString"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyValue"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyType"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyStatus"), ("ENTERASYS-ACTIVATION-MIB", "etsysActivationKeyRestrictions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysActivationBaseGroup = etsysActivationBaseGroup.setStatus('current')
etsysActivationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 99999, 2, 2, 1)).setObjects(("ENTERASYS-ACTIVATION-MIB", "etsysActivationBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysActivationCompliance = etsysActivationCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-ACTIVATION-MIB", etsysActivationCompliance=etsysActivationCompliance, PYSNMP_MODULE_ID=etsysActivationMIB, etsysActivationKeyStatus=etsysActivationKeyStatus, EnterasysKeyType=EnterasysKeyType, etsysActivationBaseGroup=etsysActivationBaseGroup, etsysActivationCompliances=etsysActivationCompliances, etsysActivationKeyFeature=etsysActivationKeyFeature, etsysActivationKeyType=etsysActivationKeyType, etsysActivationKeyFeatureEntry=etsysActivationKeyFeatureEntry, etsysActivationGroups=etsysActivationGroups, etsysActivationKeyRow=etsysActivationKeyRow, etsysActivationKeyEntry=etsysActivationKeyEntry, etsysActivationKeyTable=etsysActivationKeyTable, etsysActivationLicenseString=etsysActivationLicenseString, etsysActivationBaseBranch=etsysActivationBaseBranch, etsysActivationMIB=etsysActivationMIB, etsysMaxActivationKeyRow=etsysMaxActivationKeyRow, etsysActivationKeyFeatureTable=etsysActivationKeyFeatureTable, etsysActivationConformance=etsysActivationConformance, EnterasysFeature=EnterasysFeature, etsysActivationObjects=etsysActivationObjects, etsysActivationKeyRestrictions=etsysActivationKeyRestrictions, etsysActivationKeyValue=etsysActivationKeyValue)
