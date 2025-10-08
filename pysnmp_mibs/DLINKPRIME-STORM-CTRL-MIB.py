#
# PySNMP MIB module DLINKPRIME-STORM-CTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINKPRIME-STORM-CTRL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:58:03 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DLINKPRIME-STORM-CTRL-MIB", dpStormCtrlCurTrafficValue=dpStormCtrlCurTrafficValue, dpStormCtrlCompliance=dpStormCtrlCompliance, dpStormCtrlCompliances=dpStormCtrlCompliances, DpStormCtlThrTypeValue=DpStormCtlThrTypeValue, dpStormCtrlMIBConformance=dpStormCtrlMIBConformance, dlinkPrimeStormCtrlMIB=dlinkPrimeStormCtrlMIB, DpStormCtlTrafficType=DpStormCtlTrafficType, dpStormCtrlTrafficInfoEntry=dpStormCtrlTrafficInfoEntry, dpStormCtrlCurTrafficType=dpStormCtrlCurTrafficType, dpStormCtrlBaiscGroup=dpStormCtrlBaiscGroup, dpStormCtrlMIBObjects=dpStormCtrlMIBObjects, dpStormCtrlGroup=dpStormCtrlGroup, PYSNMP_MODULE_ID=dlinkPrimeStormCtrlMIB, dpStormCtrlTrafficInfoTable=dpStormCtrlTrafficInfoTable)
