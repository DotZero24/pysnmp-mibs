#
# PySNMP MIB module DLINKPRIME-STORM-CTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINKPRIME-STORM-CTRL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlinkPrimeStormCtrlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 17))
dlinkPrimeStormCtrlMIB.setRevisions(('2014-04-26 00:00',))
if mibBuilder.loadTexts: dlinkPrimeStormCtrlMIB.setLastUpdated('201404260000Z')
if mibBuilder.loadTexts: dlinkPrimeStormCtrlMIB.setOrganization('D-Link Corp.')
class DpStormCtlTrafficType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("broadcast", 2), ("multicast", 3), ("unicast", 4))

class DpStormCtlThrTypeValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("noLimit", 1), ("limit_512Kbps", 2), ("limit_1Mbps", 3), ("limit_2Mbps", 4), ("limit_4Mbps", 5), ("limit_8Mbps", 6), ("limit_16Mbps", 7), ("limit_32Mbps", 8), ("limit_64Mbps", 9), ("limit_128Mbps", 10), ("limit_256Mbps", 11), ("limit_512Mbps", 12))

dpStormCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 17, 1))
dpStormCtrlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 17, 2))
dpStormCtrlTrafficInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 15, 17, 1, 1), )
if mibBuilder.loadTexts: dpStormCtrlTrafficInfoTable.setStatus('current')
dpStormCtrlTrafficInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 15, 17, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dpStormCtrlTrafficInfoEntry.setStatus('current')
dpStormCtrlCurTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 17, 1, 1, 1, 1), DpStormCtlTrafficType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpStormCtrlCurTrafficType.setStatus('current')
dpStormCtrlCurTrafficValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 17, 1, 1, 1, 2), DpStormCtlThrTypeValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpStormCtrlCurTrafficValue.setStatus('current')
dpStormCtrlCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 17, 2, 1))
dpStormCtrlCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 15, 17, 2, 1, 1)).setObjects(("DLINKPRIME-STORM-CTRL-MIB", "dpStormCtrlBaiscGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpStormCtrlCompliance = dpStormCtrlCompliance.setStatus('current')
dpStormCtrlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 17, 2, 2))
dpStormCtrlBaiscGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 17, 2, 2, 1)).setObjects(("DLINKPRIME-STORM-CTRL-MIB", "dpStormCtrlCurTrafficType"), ("DLINKPRIME-STORM-CTRL-MIB", "dpStormCtrlCurTrafficValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpStormCtrlBaiscGroup = dpStormCtrlBaiscGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKPRIME-STORM-CTRL-MIB", dpStormCtrlTrafficInfoEntry=dpStormCtrlTrafficInfoEntry, dpStormCtrlBaiscGroup=dpStormCtrlBaiscGroup, dpStormCtrlMIBObjects=dpStormCtrlMIBObjects, dpStormCtrlCompliance=dpStormCtrlCompliance, dpStormCtrlCompliances=dpStormCtrlCompliances, dlinkPrimeStormCtrlMIB=dlinkPrimeStormCtrlMIB, dpStormCtrlCurTrafficValue=dpStormCtrlCurTrafficValue, dpStormCtrlTrafficInfoTable=dpStormCtrlTrafficInfoTable, dpStormCtrlGroup=dpStormCtrlGroup, dpStormCtrlCurTrafficType=dpStormCtrlCurTrafficType, PYSNMP_MODULE_ID=dlinkPrimeStormCtrlMIB, DpStormCtlTrafficType=DpStormCtlTrafficType, dpStormCtrlMIBConformance=dpStormCtrlMIBConformance, DpStormCtlThrTypeValue=DpStormCtlThrTypeValue)
