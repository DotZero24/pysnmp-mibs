#
# PySNMP MIB module DLINKPRIME-DDP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINKPRIME-DDP-CLIENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("DLINKPRIME-DDP-CLIENT-MIB", dpDdpClientCtrl=dpDdpClientCtrl, dpDdpClientGroups=dpDdpClientGroups, dpDdpClientReportTimer=dpDdpClientReportTimer, PYSNMP_MODULE_ID=dlinkPrimeDdpClientMIB, dpDdpClientCompliance=dpDdpClientCompliance, dpDdpClientControlGroup=dpDdpClientControlGroup, dlinkPrimeDdpClientMIB=dlinkPrimeDdpClientMIB, dpDdpClientConformance=dpDdpClientConformance, dpDdpClientCompliances=dpDdpClientCompliances, dpDdpClientGlobalState=dpDdpClientGlobalState, dpDdpClientNotifications=dpDdpClientNotifications, dpDdpClientObjects=dpDdpClientObjects)
