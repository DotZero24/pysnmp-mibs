#
# PySNMP MIB module RBN-ATM-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ericsson/RBN-ATM-PROFILE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
atmTrafficDescrParamEntry, = mibBuilder.importSymbols("ATM-MIB", "atmTrafficDescrParamEntry")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("RBN-ATM-PROFILE-MIB", rbnAtmProfileMIBObjects=rbnAtmProfileMIBObjects, rbnAtmProfileMIBCompliances=rbnAtmProfileMIBCompliances, rbnAtmProfileEntry=rbnAtmProfileEntry, PYSNMP_MODULE_ID=rbnAtmProfileMIB, AtmProfileName=AtmProfileName, rbnAtmProfileMIBGroups=rbnAtmProfileMIBGroups, rbnAtmProfileTable=rbnAtmProfileTable, rbnAtmProfileGroup=rbnAtmProfileGroup, rbnAtmProfileName=rbnAtmProfileName, rbnAtmTransmitBuffers=rbnAtmTransmitBuffers, rbnAtmProfileMIBCompliance=rbnAtmProfileMIBCompliance, rbnAtmCellLossPriority=rbnAtmCellLossPriority, rbnAtmProfileMIBConformance=rbnAtmProfileMIBConformance, rbnAtmProfileMIB=rbnAtmProfileMIB, rbnAtmCountersEnabled=rbnAtmCountersEnabled)
