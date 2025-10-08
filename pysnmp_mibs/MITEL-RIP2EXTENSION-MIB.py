#
# PySNMP MIB module MITEL-RIP2EXTENSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mitel/MITEL-RIP2EXTENSION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:41 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rip2IfConfAddress, = mibBuilder.importSymbols("RIPv2-MIB", "rip2IfConfAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("MITEL-RIP2EXTENSION-MIB", mitelProprietary=mitelProprietary, mitelRipExtGrpIfConfTable=mitelRipExtGrpIfConfTable, PYSNMP_MODULE_ID=mitelRouterRipExtensionGroup, mitelPropIpNetworking=mitelPropIpNetworking, mitelRouterRipExtensionGroup=mitelRouterRipExtensionGroup, mitelIfConfTblRipType=mitelIfConfTblRipType, mitel=mitel, mitelRipExtGrpIfConfEntry=mitelRipExtGrpIfConfEntry, mitelIfConfTblRowStatus=mitelIfConfTblRowStatus, mitelIfConfTblSendDefaultRoutes=mitelIfConfTblSendDefaultRoutes, mitelIpNetRouter=mitelIpNetRouter)
