#
# PySNMP MIB module ALVARION-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/alvarion/ALVARION-LICENSE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alvarionLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29))
if mibBuilder.loadTexts: alvarionLicenseMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionLicenseMIB.setOrganization('Alvarion Ltd.')
alvarionLicenseMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1))
coLicenseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1))
coLicenseFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1), )
if mibBuilder.loadTexts: coLicenseFeatureTable.setStatus('current')
coLicenseFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1, 1), ).setIndexNames((0, "ALVARION-LICENSE-MIB", "coLicenseFeatureIndex"))
if mibBuilder.loadTexts: coLicenseFeatureEntry.setStatus('current')
coLicenseFeatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coLicenseFeatureIndex.setStatus('current')
coLicenseFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureName.setStatus('current')
coLicenseFeatureState = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureState.setStatus('current')
coLicenseFeatureEndingDate = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureEndingDate.setStatus('current')
coLicenseFeatureRemainingDays = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coLicenseFeatureRemainingDays.setStatus('current')
alvarionLicenseMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 2))
alvarionLicenseMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 2, 1))
alvarionLicenseMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 2, 2))
alvarionLicenseMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 2, 1, 1)).setObjects(("ALVARION-LICENSE-MIB", "alvarionLicenseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionLicenseMIBCompliance = alvarionLicenseMIBCompliance.setStatus('current')
alvarionLicenseMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 29, 2, 2, 1)).setObjects(("ALVARION-LICENSE-MIB", "coLicenseFeatureName"), ("ALVARION-LICENSE-MIB", "coLicenseFeatureState"), ("ALVARION-LICENSE-MIB", "coLicenseFeatureEndingDate"), ("ALVARION-LICENSE-MIB", "coLicenseFeatureRemainingDays"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionLicenseMIBGroup = alvarionLicenseMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALVARION-LICENSE-MIB", alvarionLicenseMIB=alvarionLicenseMIB, coLicenseFeatureTable=coLicenseFeatureTable, PYSNMP_MODULE_ID=alvarionLicenseMIB, alvarionLicenseMIBConformance=alvarionLicenseMIBConformance, coLicenseGroup=coLicenseGroup, coLicenseFeatureEndingDate=coLicenseFeatureEndingDate, coLicenseFeatureRemainingDays=coLicenseFeatureRemainingDays, coLicenseFeatureEntry=coLicenseFeatureEntry, coLicenseFeatureState=coLicenseFeatureState, alvarionLicenseMIBCompliance=alvarionLicenseMIBCompliance, coLicenseFeatureName=coLicenseFeatureName, alvarionLicenseMIBGroup=alvarionLicenseMIBGroup, alvarionLicenseMIBObjects=alvarionLicenseMIBObjects, coLicenseFeatureIndex=coLicenseFeatureIndex, alvarionLicenseMIBGroups=alvarionLicenseMIBGroups, alvarionLicenseMIBCompliances=alvarionLicenseMIBCompliances)
