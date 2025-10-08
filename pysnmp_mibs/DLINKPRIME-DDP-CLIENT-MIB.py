#
# PySNMP MIB module DLINKPRIME-DDP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINKPRIME-DDP-CLIENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:58:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
dlinkPrimeDdpClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 2))
dlinkPrimeDdpClientMIB.setRevisions(('2014-04-26 00:00',))
if mibBuilder.loadTexts: dlinkPrimeDdpClientMIB.setLastUpdated('201404260000Z')
if mibBuilder.loadTexts: dlinkPrimeDdpClientMIB.setOrganization('D-Link Corp.')
dpDdpClientNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 2, 0))
dpDdpClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 2, 1))
dpDdpClientConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 2, 2))
dpDdpClientCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 2, 1, 1))
dpDdpClientGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 2, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpDdpClientGlobalState.setStatus('current')
dpDdpClientReportTimer = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 30), ValueRangeConstraint(60, 60), ValueRangeConstraint(90, 90), ValueRangeConstraint(120, 120), ))).setUnits('second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpDdpClientReportTimer.setStatus('current')
dpDdpClientCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 2, 2, 1))
dpDdpClientGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 2, 2, 2))
dpDdpClientCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 15, 2, 2, 1, 1)).setObjects(("DLINKPRIME-DDP-CLIENT-MIB", "dpDdpClientControlGroup"), ("DLINKPRIME-DDP-CLIENT-MIB", "dpDdpClientControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpDdpClientCompliance = dpDdpClientCompliance.setStatus('current')
dpDdpClientControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 2, 2, 2, 1)).setObjects(("DLINKPRIME-DDP-CLIENT-MIB", "dpDdpClientGlobalState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpDdpClientControlGroup = dpDdpClientControlGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKPRIME-DDP-CLIENT-MIB", dlinkPrimeDdpClientMIB=dlinkPrimeDdpClientMIB, dpDdpClientObjects=dpDdpClientObjects, dpDdpClientNotifications=dpDdpClientNotifications, dpDdpClientCompliance=dpDdpClientCompliance, dpDdpClientReportTimer=dpDdpClientReportTimer, PYSNMP_MODULE_ID=dlinkPrimeDdpClientMIB, dpDdpClientConformance=dpDdpClientConformance, dpDdpClientCtrl=dpDdpClientCtrl, dpDdpClientGroups=dpDdpClientGroups, dpDdpClientGlobalState=dpDdpClientGlobalState, dpDdpClientCompliances=dpDdpClientCompliances, dpDdpClientControlGroup=dpDdpClientControlGroup)
