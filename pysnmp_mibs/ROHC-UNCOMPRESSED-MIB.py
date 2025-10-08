#
# PySNMP MIB module ROHC-UNCOMPRESSED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/ROHC-UNCOMPRESSED-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:26:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rohcChannelID, rohcContextCID = mibBuilder.importSymbols("ROHC-MIB", "rohcChannelID", "rohcContextCID")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ROHC-UNCOMPRESSED-MIB", rohcUncmprContextMode=rohcUncmprContextMode, rohcUncmprGroups=rohcUncmprGroups, rohcUncmprContextTable=rohcUncmprContextTable, rohcUncmprObjects=rohcUncmprObjects, rohcUncmprContextState=rohcUncmprContextState, rohcUncmprMIB=rohcUncmprMIB, rohcUncmprCompliance=rohcUncmprCompliance, rohcUncmprContextACKs=rohcUncmprContextACKs, rohcUncmprConformance=rohcUncmprConformance, rohcUncmprStatisticsGroup=rohcUncmprStatisticsGroup, PYSNMP_MODULE_ID=rohcUncmprMIB, rohcUncmprCompliances=rohcUncmprCompliances, rohcUncmprContextGroup=rohcUncmprContextGroup, rohcUncmprContextEntry=rohcUncmprContextEntry)
