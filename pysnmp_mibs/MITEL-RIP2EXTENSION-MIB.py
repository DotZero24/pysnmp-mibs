#
# PySNMP MIB module MITEL-RIP2EXTENSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mitel/MITEL-RIP2EXTENSION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:01 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rip2IfConfAddress, = mibBuilder.importSymbols("RIPv2-MIB", "rip2IfConfAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
mitelRouterRipExtensionGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6))
mitelRouterRipExtensionGroup.setRevisions(('2003-03-24 10:36', '1999-03-01 00:00',))
if mibBuilder.loadTexts: mitelRouterRipExtensionGroup.setLastUpdated('200303241036Z')
if mibBuilder.loadTexts: mitelRouterRipExtensionGroup.setOrganization('MITEL Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelRipExtGrpIfConfTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1), )
if mibBuilder.loadTexts: mitelRipExtGrpIfConfTable.setStatus('current')
mitelRipExtGrpIfConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1, 1), ).setIndexNames((0, "RIPv2-MIB", "rip2IfConfAddress"))
if mibBuilder.loadTexts: mitelRipExtGrpIfConfEntry.setStatus('current')
mitelIfConfTblSendDefaultRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIfConfTblSendDefaultRoutes.setStatus('current')
mitelIfConfTblRipType = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rip", 1), ("triggerRip", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIfConfTblRipType.setStatus('current')
mitelIfConfTblRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mitelIfConfTblRowStatus.setStatus('current')
mibBuilder.exportSymbols("MITEL-RIP2EXTENSION-MIB", mitelRipExtGrpIfConfEntry=mitelRipExtGrpIfConfEntry, mitelIfConfTblSendDefaultRoutes=mitelIfConfTblSendDefaultRoutes, mitelRipExtGrpIfConfTable=mitelRipExtGrpIfConfTable, mitelIpNetRouter=mitelIpNetRouter, PYSNMP_MODULE_ID=mitelRouterRipExtensionGroup, mitelProprietary=mitelProprietary, mitelIfConfTblRowStatus=mitelIfConfTblRowStatus, mitel=mitel, mitelIfConfTblRipType=mitelIfConfTblRipType, mitelRouterRipExtensionGroup=mitelRouterRipExtensionGroup, mitelPropIpNetworking=mitelPropIpNetworking)
