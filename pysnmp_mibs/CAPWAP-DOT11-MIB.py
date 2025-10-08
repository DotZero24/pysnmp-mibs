#
# PySNMP MIB module CAPWAP-DOT11-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/CAPWAP-DOT11-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
CapwapBaseTunnelModeTC, CapwapBaseMacTypeTC = mibBuilder.importSymbols("CAPWAP-BASE-MIB", "CapwapBaseTunnelModeTC", "CapwapBaseMacTypeTC")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
capwapDot11MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 195))
capwapDot11MIB.setRevisions(('2010-04-30 00:00',))
if mibBuilder.loadTexts: capwapDot11MIB.setLastUpdated('201004300000Z')
if mibBuilder.loadTexts: capwapDot11MIB.setOrganization('IETF Control And Provisioning of Wireless Access Points (CAPWAP) Working Group http://www.ietf.org/html.charters/capwap-charter.html')
class CapwapDot11WlanIdTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16)

class CapwapDot11WlanIdProfileTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 512)

capwapDot11Objects = MibIdentifier((1, 3, 6, 1, 2, 1, 195, 1))
capwapDot11Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 195, 2))
capwapDot11WlanTable = MibTable((1, 3, 6, 1, 2, 1, 195, 1, 1), )
if mibBuilder.loadTexts: capwapDot11WlanTable.setStatus('current')
capwapDot11WlanEntry = MibTableRow((1, 3, 6, 1, 2, 1, 195, 1, 1, 1), ).setIndexNames((0, "CAPWAP-DOT11-MIB", "capwapDot11WlanProfileId"))
if mibBuilder.loadTexts: capwapDot11WlanEntry.setStatus('current')
capwapDot11WlanProfileId = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 1), CapwapDot11WlanIdProfileTC())
if mibBuilder.loadTexts: capwapDot11WlanProfileId.setStatus('current')
capwapDot11WlanProfileIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapDot11WlanProfileIfIndex.setStatus('current')
capwapDot11WlanMacType = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 3), CapwapBaseMacTypeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: capwapDot11WlanMacType.setStatus('current')
capwapDot11WlanTunnelMode = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 4), CapwapBaseTunnelModeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: capwapDot11WlanTunnelMode.setStatus('current')
capwapDot11WlanRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: capwapDot11WlanRowStatus.setStatus('current')
capwapDot11WlanBindTable = MibTable((1, 3, 6, 1, 2, 1, 195, 1, 2), )
if mibBuilder.loadTexts: capwapDot11WlanBindTable.setStatus('current')
capwapDot11WlanBindEntry = MibTableRow((1, 3, 6, 1, 2, 1, 195, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CAPWAP-DOT11-MIB", "capwapDot11WlanProfileId"))
if mibBuilder.loadTexts: capwapDot11WlanBindEntry.setStatus('current')
capwapDot11WlanBindWlanId = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 2, 1, 1), CapwapDot11WlanIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapDot11WlanBindWlanId.setStatus('current')
capwapDot11WlanBindBssIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapDot11WlanBindBssIfIndex.setStatus('current')
capwapDot11WlanBindRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: capwapDot11WlanBindRowStatus.setStatus('current')
capwapDot11Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 195, 2, 1))
capwapDot11Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 195, 2, 2))
capwapDot11Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 195, 2, 2, 1)).setObjects(("CAPWAP-DOT11-MIB", "capwapDot11WlanGroup"), ("CAPWAP-DOT11-MIB", "capwapDot11WlanBindGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capwapDot11Compliance = capwapDot11Compliance.setStatus('current')
capwapDot11WlanGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 195, 2, 1, 1)).setObjects(("CAPWAP-DOT11-MIB", "capwapDot11WlanProfileIfIndex"), ("CAPWAP-DOT11-MIB", "capwapDot11WlanMacType"), ("CAPWAP-DOT11-MIB", "capwapDot11WlanTunnelMode"), ("CAPWAP-DOT11-MIB", "capwapDot11WlanRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capwapDot11WlanGroup = capwapDot11WlanGroup.setStatus('current')
capwapDot11WlanBindGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 195, 2, 1, 2)).setObjects(("CAPWAP-DOT11-MIB", "capwapDot11WlanBindWlanId"), ("CAPWAP-DOT11-MIB", "capwapDot11WlanBindBssIfIndex"), ("CAPWAP-DOT11-MIB", "capwapDot11WlanBindRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capwapDot11WlanBindGroup = capwapDot11WlanBindGroup.setStatus('current')
mibBuilder.exportSymbols("CAPWAP-DOT11-MIB", capwapDot11WlanTable=capwapDot11WlanTable, capwapDot11WlanBindBssIfIndex=capwapDot11WlanBindBssIfIndex, capwapDot11WlanBindRowStatus=capwapDot11WlanBindRowStatus, capwapDot11WlanTunnelMode=capwapDot11WlanTunnelMode, capwapDot11Conformance=capwapDot11Conformance, capwapDot11Groups=capwapDot11Groups, capwapDot11WlanGroup=capwapDot11WlanGroup, capwapDot11Compliances=capwapDot11Compliances, capwapDot11WlanRowStatus=capwapDot11WlanRowStatus, capwapDot11WlanEntry=capwapDot11WlanEntry, capwapDot11WlanBindWlanId=capwapDot11WlanBindWlanId, capwapDot11WlanBindGroup=capwapDot11WlanBindGroup, capwapDot11Objects=capwapDot11Objects, capwapDot11Compliance=capwapDot11Compliance, capwapDot11WlanBindEntry=capwapDot11WlanBindEntry, capwapDot11WlanProfileId=capwapDot11WlanProfileId, capwapDot11WlanProfileIfIndex=capwapDot11WlanProfileIfIndex, capwapDot11WlanMacType=capwapDot11WlanMacType, PYSNMP_MODULE_ID=capwapDot11MIB, capwapDot11MIB=capwapDot11MIB, capwapDot11WlanBindTable=capwapDot11WlanBindTable, CapwapDot11WlanIdProfileTC=CapwapDot11WlanIdProfileTC, CapwapDot11WlanIdTC=CapwapDot11WlanIdTC)
