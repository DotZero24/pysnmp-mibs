#
# PySNMP MIB module MAIPU-POLICYROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/maipu/MAIPU-POLICYROUTE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mpMgmt, = mibBuilder.importSymbols("MAIPU-SMI", "mpMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectSyntax, Counter32, ModuleIdentity, TimeTicks, Counter64, ObjectIdentity, Gauge32, ObjectName = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectSyntax", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "ObjectIdentity", "Gauge32", "ObjectName")
RowStatus, DateAndTime, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("MAIPU-POLICYROUTE-MIB", policyRouteRoutemap=policyRouteRoutemap, routeMib=routeMib, policyRouteEntry=policyRouteEntry, policyRouteIfindex=policyRouteIfindex, policyRouteLocal=policyRouteLocal, EnabledStatus=EnabledStatus, policyRouteRowStatus=policyRouteRowStatus, policyRouteTable=policyRouteTable, policyRouteCache=policyRouteCache, PYSNMP_MODULE_ID=policyRoute, policyRoute=policyRoute)
