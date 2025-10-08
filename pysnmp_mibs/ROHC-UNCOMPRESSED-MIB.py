#
# PySNMP MIB module ROHC-UNCOMPRESSED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/ROHC-UNCOMPRESSED-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:48:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rohcContextCID, rohcChannelID = mibBuilder.importSymbols("ROHC-MIB", "rohcContextCID", "rohcChannelID")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rohcUncmprMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 113))
rohcUncmprMIB.setRevisions(('2004-06-03 00:00',))
if mibBuilder.loadTexts: rohcUncmprMIB.setLastUpdated('200406030000Z')
if mibBuilder.loadTexts: rohcUncmprMIB.setOrganization('IETF Robust Header Compression Working Group')
rohcUncmprObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 113, 1))
rohcUncmprConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 113, 2))
rohcUncmprContextTable = MibTable((1, 3, 6, 1, 2, 1, 113, 1, 1), )
if mibBuilder.loadTexts: rohcUncmprContextTable.setStatus('current')
rohcUncmprContextEntry = MibTableRow((1, 3, 6, 1, 2, 1, 113, 1, 1, 1), ).setIndexNames((0, "ROHC-MIB", "rohcChannelID"), (0, "ROHC-MIB", "rohcContextCID"))
if mibBuilder.loadTexts: rohcUncmprContextEntry.setStatus('current')
rohcUncmprContextState = MibTableColumn((1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("initAndRefresh", 1), ("normal", 2), ("noContext", 3), ("fullContext", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rohcUncmprContextState.setStatus('current')
rohcUncmprContextMode = MibTableColumn((1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unidirectional", 1), ("bidirectional", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rohcUncmprContextMode.setStatus('current')
rohcUncmprContextACKs = MibTableColumn((1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rohcUncmprContextACKs.setStatus('current')
rohcUncmprCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 113, 2, 1))
rohcUncmprGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 113, 2, 2))
rohcUncmprCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 113, 2, 1, 1)).setObjects(("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextGroup"), ("ROHC-UNCOMPRESSED-MIB", "rohcUncmprStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rohcUncmprCompliance = rohcUncmprCompliance.setStatus('current')
rohcUncmprContextGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 113, 2, 2, 1)).setObjects(("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextState"), ("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rohcUncmprContextGroup = rohcUncmprContextGroup.setStatus('current')
rohcUncmprStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 113, 2, 2, 2)).setObjects(("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextACKs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rohcUncmprStatisticsGroup = rohcUncmprStatisticsGroup.setStatus('current')
mibBuilder.exportSymbols("ROHC-UNCOMPRESSED-MIB", rohcUncmprContextMode=rohcUncmprContextMode, rohcUncmprContextACKs=rohcUncmprContextACKs, rohcUncmprContextTable=rohcUncmprContextTable, rohcUncmprObjects=rohcUncmprObjects, rohcUncmprCompliances=rohcUncmprCompliances, rohcUncmprContextEntry=rohcUncmprContextEntry, rohcUncmprMIB=rohcUncmprMIB, rohcUncmprContextGroup=rohcUncmprContextGroup, PYSNMP_MODULE_ID=rohcUncmprMIB, rohcUncmprConformance=rohcUncmprConformance, rohcUncmprStatisticsGroup=rohcUncmprStatisticsGroup, rohcUncmprGroups=rohcUncmprGroups, rohcUncmprCompliance=rohcUncmprCompliance, rohcUncmprContextState=rohcUncmprContextState)
