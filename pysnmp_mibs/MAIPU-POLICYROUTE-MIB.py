#
# PySNMP MIB module MAIPU-POLICYROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/maipu/MAIPU-POLICYROUTE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mpMgmt, = mibBuilder.importSymbols("MAIPU-SMI", "mpMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, ObjectSyntax, iso, MibIdentifier, ObjectName, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "ObjectSyntax", "iso", "MibIdentifier", "ObjectName", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
routeMib = MibIdentifier((1, 3, 6, 1, 4, 1, 5651, 3, 81))
policyRoute = ModuleIdentity((1, 3, 6, 1, 4, 1, 5651, 3, 81, 6))
if mibBuilder.loadTexts: policyRoute.setLastUpdated('0703071024Z')
if mibBuilder.loadTexts: policyRoute.setOrganization('ĴͨŹɷ\u07b9˾, Maipu (Sichuan) Communication Technology Co. LTD.')
class EnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

policyRouteLocal = MibScalar((1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyRouteLocal.setStatus('current')
policyRouteTable = MibTable((1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 2), )
if mibBuilder.loadTexts: policyRouteTable.setStatus('current')
policyRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 2, 1), ).setIndexNames((0, "MAIPU-POLICYROUTE-MIB", "policyRouteIfindex"))
if mibBuilder.loadTexts: policyRouteEntry.setStatus('current')
policyRouteIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: policyRouteIfindex.setStatus('current')
policyRouteRoutemap = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyRouteRoutemap.setStatus('current')
policyRouteCache = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 2, 1, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: policyRouteCache.setStatus('current')
policyRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 81, 6, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyRouteRowStatus.setStatus('current')
mibBuilder.exportSymbols("MAIPU-POLICYROUTE-MIB", policyRouteIfindex=policyRouteIfindex, policyRouteTable=policyRouteTable, EnabledStatus=EnabledStatus, policyRouteRoutemap=policyRouteRoutemap, routeMib=routeMib, policyRouteEntry=policyRouteEntry, policyRoute=policyRoute, policyRouteRowStatus=policyRouteRowStatus, PYSNMP_MODULE_ID=policyRoute, policyRouteCache=policyRouteCache, policyRouteLocal=policyRouteLocal)
