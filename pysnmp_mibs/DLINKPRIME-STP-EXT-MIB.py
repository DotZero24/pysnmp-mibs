#
# PySNMP MIB module DLINKPRIME-STP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINKPRIME-STP-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:01 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DLINKPRIME-STP-EXT-MIB", dpStpExtPortMgmt=dpStpExtPortMgmt, dpStpExtPortFast=dpStpExtPortFast, dpStpExtMstpGroup=dpStpExtMstpGroup, dpStpExtNotificationEnable=dpStpExtNotificationEnable, dpStpExtMIBObjects=dpStpExtMIBObjects, PYSNMP_MODULE_ID=dlinkPrimeStpExtMIB, dpStpExtStpGblStateEnabled=dpStpExtStpGblStateEnabled, dpStpExtPortState=dpStpExtPortState, dlinkPrimeStpExtMIB=dlinkPrimeStpExtMIB, dpStpExtGblMgmt=dpStpExtGblMgmt, dpStpExtMIBNotifications=dpStpExtMIBNotifications, dpStpExtGroups=dpStpExtGroups, dpStpExtPortEntry=dpStpExtPortEntry, dpStpExtPortNumber=dpStpExtPortNumber, dpStpExtBasicGroup=dpStpExtBasicGroup, dpStpExtMIBCompliances=dpStpExtMIBCompliances, dpStpExtMIBConformance=dpStpExtMIBConformance, IEEE8021BridgePortNumber=IEEE8021BridgePortNumber, dpStpExtStpMode=dpStpExtStpMode, dpStpExtPortTable=dpStpExtPortTable, dpStpExtCompliance=dpStpExtCompliance)
