#
# PySNMP MIB module DLINKPRIME-STP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINKPRIME-STP-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
dlinkPrimeStpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 18))
dlinkPrimeStpExtMIB.setRevisions(('2014-06-05 00:00',))
if mibBuilder.loadTexts: dlinkPrimeStpExtMIB.setLastUpdated('201406050000Z')
if mibBuilder.loadTexts: dlinkPrimeStpExtMIB.setOrganization('D-Link Corp.')
class IEEE8021BridgePortNumber(TextualConvention, Unsigned32):
    reference = '17.3.2.2'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

dpStpExtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 18, 0))
dpStpExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 18, 1))
dpStpExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 18, 2))
dpStpExtGblMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 1))
dpStpExtStpGblStateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpStpExtStpGblStateEnabled.setStatus('current')
dpStpExtStpMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stp", 1), ("rstp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpStpExtStpMode.setStatus('current')
dpStpExtNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 1, 3), Bits().clone(namedValues=NamedValues(("newRoot", 0), ("topologyChange", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpStpExtNotificationEnable.setStatus('current')
dpStpExtPortMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 2))
dpStpExtPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 2, 1), )
if mibBuilder.loadTexts: dpStpExtPortTable.setStatus('current')
dpStpExtPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 2, 1, 1), ).setIndexNames((0, "DLINKPRIME-STP-EXT-MIB", "dpStpExtPortNumber"))
if mibBuilder.loadTexts: dpStpExtPortEntry.setStatus('current')
dpStpExtPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 2, 1, 1, 1), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: dpStpExtPortNumber.setStatus('current')
dpStpExtPortFast = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("network", 1), ("disabled", 2), ("edge", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpStpExtPortFast.setStatus('current')
dpStpExtPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 18, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("errDisabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6), ("nonStpForwarding", 7), ("nonStpOther", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpStpExtPortState.setStatus('current')
dpStpExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 18, 2, 1))
dpStpExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 15, 18, 2, 1, 1)).setObjects(("DLINKPRIME-STP-EXT-MIB", "dpStpExtBasicGroup"), ("DLINKPRIME-STP-EXT-MIB", "dpStpExtMstpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpStpExtCompliance = dpStpExtCompliance.setStatus('current')
dpStpExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 18, 2, 1, 2))
dpStpExtBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 18, 2, 1, 2, 1)).setObjects(("DLINKPRIME-STP-EXT-MIB", "dpStpExtStpGblStateEnabled"), ("DLINKPRIME-STP-EXT-MIB", "dpStpExtPortState"), ("DLINKPRIME-STP-EXT-MIB", "dpStpExtNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpStpExtBasicGroup = dpStpExtBasicGroup.setStatus('current')
dpStpExtMstpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 18, 2, 1, 2, 2)).setObjects(("DLINKPRIME-STP-EXT-MIB", "dpStpExtPortFast"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpStpExtMstpGroup = dpStpExtMstpGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKPRIME-STP-EXT-MIB", dlinkPrimeStpExtMIB=dlinkPrimeStpExtMIB, dpStpExtGblMgmt=dpStpExtGblMgmt, dpStpExtGroups=dpStpExtGroups, dpStpExtMIBNotifications=dpStpExtMIBNotifications, dpStpExtPortTable=dpStpExtPortTable, dpStpExtMIBConformance=dpStpExtMIBConformance, dpStpExtPortEntry=dpStpExtPortEntry, dpStpExtBasicGroup=dpStpExtBasicGroup, dpStpExtMIBCompliances=dpStpExtMIBCompliances, dpStpExtStpMode=dpStpExtStpMode, dpStpExtPortMgmt=dpStpExtPortMgmt, IEEE8021BridgePortNumber=IEEE8021BridgePortNumber, dpStpExtStpGblStateEnabled=dpStpExtStpGblStateEnabled, dpStpExtPortFast=dpStpExtPortFast, dpStpExtCompliance=dpStpExtCompliance, dpStpExtMstpGroup=dpStpExtMstpGroup, dpStpExtNotificationEnable=dpStpExtNotificationEnable, PYSNMP_MODULE_ID=dlinkPrimeStpExtMIB, dpStpExtPortNumber=dpStpExtPortNumber, dpStpExtPortState=dpStpExtPortState, dpStpExtMIBObjects=dpStpExtMIBObjects)
