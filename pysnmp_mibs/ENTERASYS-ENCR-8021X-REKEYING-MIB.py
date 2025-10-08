#
# PySNMP MIB module ENTERASYS-ENCR-8021X-REKEYING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-ENCR-8021X-REKEYING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
dot1xPaePortNumber, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xPaePortNumber")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysEncr8021xRekeyingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20))
etsysEncr8021xRekeyingMIB.setRevisions(('2002-03-14 20:49',))
if mibBuilder.loadTexts: etsysEncr8021xRekeyingMIB.setLastUpdated('200203142049Z')
if mibBuilder.loadTexts: etsysEncr8021xRekeyingMIB.setOrganization('Enterasys Networks, Inc')
etsysEncrDot1xRekeyingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1))
etsysEncrDot1xRekeyBaseBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1))
etsysEncrDot1xRekeyConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1, 1), )
if mibBuilder.loadTexts: etsysEncrDot1xRekeyConfigTable.setStatus('current')
etsysEncrDot1xRekeyConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: etsysEncrDot1xRekeyConfigEntry.setStatus('current')
etsysEncrDot1xRekeyEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysEncrDot1xRekeyEnabled.setStatus('current')
etsysEncrDot1xRekeyPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysEncrDot1xRekeyPeriod.setStatus('current')
etsysEncrDot1xRekeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysEncrDot1xRekeyLength.setStatus('current')
etsysEncrDot1xRekeyAsymmetric = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysEncrDot1xRekeyAsymmetric.setStatus('current')
etsysEncrDot1xRekeyingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 2))
etsysEncrDot1xRekeyingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 2, 1))
etsysEncrDot1xRekeyingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 2, 2))
etsysEncrDot1xRekeyingBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 2, 1, 1)).setObjects(("ENTERASYS-ENCR-8021X-REKEYING-MIB", "etsysEncrDot1xRekeyPeriod"), ("ENTERASYS-ENCR-8021X-REKEYING-MIB", "etsysEncrDot1xRekeyEnabled"), ("ENTERASYS-ENCR-8021X-REKEYING-MIB", "etsysEncrDot1xRekeyLength"), ("ENTERASYS-ENCR-8021X-REKEYING-MIB", "etsysEncrDot1xRekeyAsymmetric"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysEncrDot1xRekeyingBaseGroup = etsysEncrDot1xRekeyingBaseGroup.setStatus('current')
etsysEncrDot1xRekeyingCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 2, 2, 1)).setObjects(("ENTERASYS-ENCR-8021X-REKEYING-MIB", "etsysEncrDot1xRekeyingBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysEncrDot1xRekeyingCompliance = etsysEncrDot1xRekeyingCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-ENCR-8021X-REKEYING-MIB", etsysEncrDot1xRekeyingGroups=etsysEncrDot1xRekeyingGroups, etsysEncrDot1xRekeyingObjects=etsysEncrDot1xRekeyingObjects, etsysEncrDot1xRekeyingCompliance=etsysEncrDot1xRekeyingCompliance, etsysEncrDot1xRekeyingCompliances=etsysEncrDot1xRekeyingCompliances, etsysEncrDot1xRekeyConfigTable=etsysEncrDot1xRekeyConfigTable, etsysEncrDot1xRekeyPeriod=etsysEncrDot1xRekeyPeriod, etsysEncr8021xRekeyingMIB=etsysEncr8021xRekeyingMIB, etsysEncrDot1xRekeyingBaseGroup=etsysEncrDot1xRekeyingBaseGroup, etsysEncrDot1xRekeyingConformance=etsysEncrDot1xRekeyingConformance, etsysEncrDot1xRekeyBaseBranch=etsysEncrDot1xRekeyBaseBranch, etsysEncrDot1xRekeyEnabled=etsysEncrDot1xRekeyEnabled, etsysEncrDot1xRekeyLength=etsysEncrDot1xRekeyLength, etsysEncrDot1xRekeyConfigEntry=etsysEncrDot1xRekeyConfigEntry, etsysEncrDot1xRekeyAsymmetric=etsysEncrDot1xRekeyAsymmetric, PYSNMP_MODULE_ID=etsysEncr8021xRekeyingMIB)
