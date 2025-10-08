#
# PySNMP MIB module RBN-ATM-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ericsson/RBN-ATM-PROFILE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
atmTrafficDescrParamEntry, = mibBuilder.importSymbols("ATM-MIB", "atmTrafficDescrParamEntry")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rbnAtmProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 2))
rbnAtmProfileMIB.setRevisions(('2002-04-19 00:00', '2001-12-11 00:00', '1998-07-15 16:45',))
if mibBuilder.loadTexts: rbnAtmProfileMIB.setLastUpdated('200204190000Z')
if mibBuilder.loadTexts: rbnAtmProfileMIB.setOrganization('RedBack Networks, Inc.')
class AtmProfileName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '80a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 80)

rbnAtmProfileMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1))
rbnAtmProfileTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1), )
if mibBuilder.loadTexts: rbnAtmProfileTable.setStatus('current')
rbnAtmProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1), )
atmTrafficDescrParamEntry.registerAugmentions(("RBN-ATM-PROFILE-MIB", "rbnAtmProfileEntry"))
rbnAtmProfileEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
if mibBuilder.loadTexts: rbnAtmProfileEntry.setStatus('current')
rbnAtmProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 1), AtmProfileName().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmProfileName.setStatus('current')
rbnAtmCountersEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmCountersEnabled.setStatus('current')
rbnAtmCellLossPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmCellLossPriority.setStatus('current')
rbnAtmTransmitBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63)).clone(50)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnAtmTransmitBuffers.setStatus('current')
rbnAtmProfileMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2))
rbnAtmProfileMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 1))
rbnAtmProfileMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 2))
rbnAtmProfileMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 2, 1)).setObjects(("RBN-ATM-PROFILE-MIB", "rbnAtmProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmProfileMIBCompliance = rbnAtmProfileMIBCompliance.setStatus('current')
rbnAtmProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 2, 2, 1, 1)).setObjects(("RBN-ATM-PROFILE-MIB", "rbnAtmProfileName"), ("RBN-ATM-PROFILE-MIB", "rbnAtmCountersEnabled"), ("RBN-ATM-PROFILE-MIB", "rbnAtmCellLossPriority"), ("RBN-ATM-PROFILE-MIB", "rbnAtmTransmitBuffers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmProfileGroup = rbnAtmProfileGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-ATM-PROFILE-MIB", rbnAtmProfileMIB=rbnAtmProfileMIB, rbnAtmProfileGroup=rbnAtmProfileGroup, rbnAtmCountersEnabled=rbnAtmCountersEnabled, rbnAtmProfileName=rbnAtmProfileName, rbnAtmCellLossPriority=rbnAtmCellLossPriority, rbnAtmProfileTable=rbnAtmProfileTable, rbnAtmProfileMIBCompliances=rbnAtmProfileMIBCompliances, rbnAtmProfileEntry=rbnAtmProfileEntry, rbnAtmProfileMIBConformance=rbnAtmProfileMIBConformance, rbnAtmProfileMIBCompliance=rbnAtmProfileMIBCompliance, rbnAtmTransmitBuffers=rbnAtmTransmitBuffers, rbnAtmProfileMIBGroups=rbnAtmProfileMIBGroups, rbnAtmProfileMIBObjects=rbnAtmProfileMIBObjects, PYSNMP_MODULE_ID=rbnAtmProfileMIB, AtmProfileName=AtmProfileName)
