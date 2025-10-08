#
# PySNMP MIB module CAMBIUM-NETWORKS-MACSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cambium/CAMBIUM-NETWORKS-MACSEC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
cnMacSecMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 17713, 24, 10))
cnMacSecMib.setRevisions(('2021-11-28 00:00', '2021-06-04 00:00',))
if mibBuilder.loadTexts: cnMacSecMib.setLastUpdated('202111280000Z')
if mibBuilder.loadTexts: cnMacSecMib.setOrganization('Cambium Networks, Inc.')
class MacSecViolationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("protect", 1), ("restrict", 2), ("shutdown", 3))

cnMacSecPort = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1))
cnMacSecPortTable = MibTable((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1), )
if mibBuilder.loadTexts: cnMacSecPortTable.setStatus('current')
cnMacSecPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1), ).setIndexNames((0, "CAMBIUM-NETWORKS-MACSEC-MIB", "cnMacSecPortIndex"))
if mibBuilder.loadTexts: cnMacSecPortEntry.setStatus('current')
cnMacSecPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 52)))
if mibBuilder.loadTexts: cnMacSecPortIndex.setStatus('current')
cnMacSecPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMacSecPortStatus.setStatus('current')
cnMacSecPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 3), MacSecViolationMode().clone('protect')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMacSecPortMode.setStatus('current')
cnMacSecPortMaxAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 4), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMacSecPortMaxAddr.setStatus('current')
cnMacSecPortNumAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnMacSecPortNumAddr.setStatus('current')
cnMacSecPortNumViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnMacSecPortNumViolations.setStatus('current')
cnMacSecPortLastViolationAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnMacSecPortLastViolationAddr.setStatus('current')
cnMacSecPortLastViolationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnMacSecPortLastViolationTime.setStatus('current')
cnMacSecGlobalDebug = MibScalar((1, 3, 6, 1, 4, 1, 17713, 24, 10, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMacSecGlobalDebug.setStatus('current')
cnMacSecDebugOption = MibScalar((1, 3, 6, 1, 4, 1, 17713, 24, 10, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMacSecDebugOption.setStatus('current')
mibBuilder.exportSymbols("CAMBIUM-NETWORKS-MACSEC-MIB", cnMacSecPortMode=cnMacSecPortMode, cnMacSecPortStatus=cnMacSecPortStatus, MacSecViolationMode=MacSecViolationMode, PYSNMP_MODULE_ID=cnMacSecMib, cnMacSecPortEntry=cnMacSecPortEntry, cnMacSecPortMaxAddr=cnMacSecPortMaxAddr, cnMacSecPortNumAddr=cnMacSecPortNumAddr, cnMacSecPort=cnMacSecPort, cnMacSecPortLastViolationAddr=cnMacSecPortLastViolationAddr, cnMacSecGlobalDebug=cnMacSecGlobalDebug, cnMacSecMib=cnMacSecMib, cnMacSecPortIndex=cnMacSecPortIndex, cnMacSecDebugOption=cnMacSecDebugOption, cnMacSecPortLastViolationTime=cnMacSecPortLastViolationTime, cnMacSecPortTable=cnMacSecPortTable, cnMacSecPortNumViolations=cnMacSecPortNumViolations)
