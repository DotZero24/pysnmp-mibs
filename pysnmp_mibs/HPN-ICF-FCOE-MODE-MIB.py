#
# PySNMP MIB module HPN-ICF-FCOE-MODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-FCOE-MODE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfFcoeMode = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135))
hpnicfFcoeMode.setRevisions(('2013-03-08 11:00',))
if mibBuilder.loadTexts: hpnicfFcoeMode.setLastUpdated('201303081100Z')
if mibBuilder.loadTexts: hpnicfFcoeMode.setOrganization('')
hpnicfFcoeModeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135, 1))
hpnicfFcoeModeCfgMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFcoeModeCfgMode.setStatus('current')
hpnicfFcoeModeCfgLastResult = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("success", 1), ("noLicence", 2), ("needReset", 3), ("unknownFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcoeModeCfgLastResult.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-FCOE-MODE-MIB", hpnicfFcoeModeCfgMode=hpnicfFcoeModeCfgMode, hpnicfFcoeModeCfgLastResult=hpnicfFcoeModeCfgLastResult, hpnicfFcoeMode=hpnicfFcoeMode, PYSNMP_MODULE_ID=hpnicfFcoeMode, hpnicfFcoeModeMibObjects=hpnicfFcoeModeMibObjects)
