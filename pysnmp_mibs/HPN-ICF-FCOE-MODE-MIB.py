#
# PySNMP MIB module HPN-ICF-FCOE-MODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-FCOE-MODE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:37 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfFcoeMode = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135))
hpnicfFcoeMode.setRevisions(('2013-03-08 11:00',))
if mibBuilder.loadTexts: hpnicfFcoeMode.setLastUpdated('201303081100Z')
if mibBuilder.loadTexts: hpnicfFcoeMode.setOrganization('')
hpnicfFcoeModeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135, 1))
hpnicfFcoeModeCfgMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFcoeModeCfgMode.setStatus('current')
hpnicfFcoeModeCfgLastResult = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("success", 1), ("noLicence", 2), ("needReset", 3), ("unknownFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcoeModeCfgLastResult.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-FCOE-MODE-MIB", PYSNMP_MODULE_ID=hpnicfFcoeMode, hpnicfFcoeModeCfgLastResult=hpnicfFcoeModeCfgLastResult, hpnicfFcoeModeCfgMode=hpnicfFcoeModeCfgMode, hpnicfFcoeModeMibObjects=hpnicfFcoeModeMibObjects, hpnicfFcoeMode=hpnicfFcoeMode)
