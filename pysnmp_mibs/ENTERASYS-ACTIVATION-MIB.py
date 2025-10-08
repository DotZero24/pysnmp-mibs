#
# PySNMP MIB module ENTERASYS-ACTIVATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-ACTIVATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("ENTERASYS-ACTIVATION-MIB", etsysMaxActivationKeyRow=etsysMaxActivationKeyRow, etsysActivationMIB=etsysActivationMIB, etsysActivationCompliance=etsysActivationCompliance, etsysActivationKeyFeature=etsysActivationKeyFeature, etsysActivationBaseBranch=etsysActivationBaseBranch, etsysActivationGroups=etsysActivationGroups, etsysActivationKeyRow=etsysActivationKeyRow, EnterasysFeature=EnterasysFeature, etsysActivationKeyValue=etsysActivationKeyValue, PYSNMP_MODULE_ID=etsysActivationMIB, etsysActivationKeyRestrictions=etsysActivationKeyRestrictions, etsysActivationKeyType=etsysActivationKeyType, etsysActivationCompliances=etsysActivationCompliances, etsysActivationConformance=etsysActivationConformance, etsysActivationKeyTable=etsysActivationKeyTable, etsysActivationObjects=etsysActivationObjects, etsysActivationKeyFeatureTable=etsysActivationKeyFeatureTable, etsysActivationKeyStatus=etsysActivationKeyStatus, etsysActivationKeyFeatureEntry=etsysActivationKeyFeatureEntry, etsysActivationBaseGroup=etsysActivationBaseGroup, EnterasysKeyType=EnterasysKeyType, etsysActivationKeyEntry=etsysActivationKeyEntry, etsysActivationLicenseString=etsysActivationLicenseString)
