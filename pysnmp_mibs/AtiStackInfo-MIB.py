#
# PySNMP MIB module AtiStackInfo-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/allied-old/AtiStackInfo-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
alliedTelesyn = ModuleIdentity((1, 3, 6, 1, 4, 1, 207))
if mibBuilder.loadTexts: alliedTelesyn.setLastUpdated('200407270000Z')
if mibBuilder.loadTexts: alliedTelesyn.setOrganization('Allied Telesyn International')
mibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8))
atiStackInfoMib = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 16))
class MACAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

atiswitchEnhancedStacking = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 16, 1))
atiswitchEnhStackMode = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("master", 1), ("slave", 2), ("unavailable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiswitchEnhStackMode.setStatus('current')
atiswitchEnhStackDiscover = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("discover", 1), ("do-not-discover", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiswitchEnhStackDiscover.setStatus('current')
atiswitchEnhStackRemoteNumber = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiswitchEnhStackRemoteNumber.setStatus('current')
atiswitchEnhStackTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4), )
if mibBuilder.loadTexts: atiswitchEnhStackTable.setStatus('current')
atiswitchEnhStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1), ).setIndexNames((0, "AtiStackInfo-MIB", "atiswitchEnhStackSwId"))
if mibBuilder.loadTexts: atiswitchEnhStackEntry.setStatus('current')
atiswitchEnhStackSwId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiswitchEnhStackSwId.setStatus('current')
atiswitchEnhStackSwMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 2), MACAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiswitchEnhStackSwMacAddr.setStatus('current')
atiswitchEnhStackSwName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiswitchEnhStackSwName.setStatus('current')
atiswitchEnhStackSwMode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiswitchEnhStackSwMode.setStatus('current')
atiswitchEnhStackSwSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiswitchEnhStackSwSoftwareVersion.setStatus('current')
atiswitchEnhStackSwModel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiswitchEnhStackSwModel.setStatus('current')
atiswitchEnhStackConnect = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 16, 1, 4, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiswitchEnhStackConnect.setStatus('current')
mibBuilder.exportSymbols("AtiStackInfo-MIB", atiswitchEnhStackConnect=atiswitchEnhStackConnect, atiswitchEnhStackRemoteNumber=atiswitchEnhStackRemoteNumber, PYSNMP_MODULE_ID=alliedTelesyn, atiswitchEnhStackSwName=atiswitchEnhStackSwName, atiswitchEnhStackSwSoftwareVersion=atiswitchEnhStackSwSoftwareVersion, atiStackInfoMib=atiStackInfoMib, mibObject=mibObject, atiswitchEnhStackSwMode=atiswitchEnhStackSwMode, atiswitchEnhStackSwMacAddr=atiswitchEnhStackSwMacAddr, MACAddress=MACAddress, atiswitchEnhStackDiscover=atiswitchEnhStackDiscover, atiswitchEnhStackEntry=atiswitchEnhStackEntry, atiswitchEnhStackSwId=atiswitchEnhStackSwId, atiswitchEnhancedStacking=atiswitchEnhancedStacking, atiswitchEnhStackSwModel=atiswitchEnhStackSwModel, atiswitchEnhStackMode=atiswitchEnhStackMode, atiswitchEnhStackTable=atiswitchEnhStackTable, alliedTelesyn=alliedTelesyn)
