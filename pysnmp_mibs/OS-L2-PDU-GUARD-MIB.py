#
# PySNMP MIB module OS-L2-PDU-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/OS-L2-PDU-GUARD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
oaOptiSwitch, = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "oaOptiSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
osL2PduGuard = ModuleIdentity((1, 3, 6, 1, 4, 1, 6926, 2, 17))
osL2PduGuard.setRevisions(('2010-01-09 00:00',))
if mibBuilder.loadTexts: osL2PduGuard.setLastUpdated('201001090000Z')
if mibBuilder.loadTexts: osL2PduGuard.setOrganization('MRV Communications, Inc.')
osL2PduGuardCpGen = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 17, 1))
osL2PduGuardCpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 17, 100))
osL2PduGuardCpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 17, 100, 1))
osL2PduGuardCpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 17, 100, 2))
class L2ProtocolId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("unknown", 1), ("stp", 2), ("ethoam", 3), ("efm", 4), ("dot1x", 5), ("esmc", 6), ("cdp", 7), ("dtp", 8), ("udld", 9), ("pagp", 10), ("pvst", 11), ("vtp", 12), ("lacp", 13), ("erp", 14), ("lamp", 15), ("elmi", 16), ("lldp", 17), ("garp", 18))

class L2PortState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("normal", 2), ("isolated", 3), ("inform", 4))

class SupportValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("notSupported", 1), ("supported", 2))

osL2PduGuardSupprt = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 17, 1, 1), SupportValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osL2PduGuardSupprt.setStatus('current')
osL2PduGuardTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 17, 2), )
if mibBuilder.loadTexts: osL2PduGuardTable.setStatus('current')
osL2PduGuardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 17, 2, 1), ).setIndexNames((0, "OS-L2-PDU-GUARD-MIB", "osL2PduGuardProtocol"), (0, "OS-L2-PDU-GUARD-MIB", "osL2PduGuardPort"))
if mibBuilder.loadTexts: osL2PduGuardEntry.setStatus('current')
osL2PduGuardProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 17, 2, 1, 1), L2ProtocolId())
if mibBuilder.loadTexts: osL2PduGuardProtocol.setStatus('current')
osL2PduGuardPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 17, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: osL2PduGuardPort.setStatus('current')
osL2PduGuardIsolateRate = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 17, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 300), ))).setUnits('packets per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: osL2PduGuardIsolateRate.setStatus('current')
osL2PduGuardInformRate = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 17, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 300), ))).setUnits('packets per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: osL2PduGuardInformRate.setStatus('current')
osL2PduGuardState = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 17, 2, 1, 5), L2PortState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osL2PduGuardState.setStatus('current')
osL2PduGuardCpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6926, 2, 17, 100, 1, 1)).setObjects(("OS-L2-PDU-GUARD-MIB", "osL2PduGuardMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osL2PduGuardCpMIBCompliance = osL2PduGuardCpMIBCompliance.setStatus('current')
osL2PduGuardMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6926, 2, 17, 100, 2, 1)).setObjects(("OS-L2-PDU-GUARD-MIB", "osL2PduGuardSupprt"), ("OS-L2-PDU-GUARD-MIB", "osL2PduGuardIsolateRate"), ("OS-L2-PDU-GUARD-MIB", "osL2PduGuardInformRate"), ("OS-L2-PDU-GUARD-MIB", "osL2PduGuardState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osL2PduGuardMandatoryGroup = osL2PduGuardMandatoryGroup.setStatus('current')
mibBuilder.exportSymbols("OS-L2-PDU-GUARD-MIB", osL2PduGuardState=osL2PduGuardState, L2PortState=L2PortState, osL2PduGuardPort=osL2PduGuardPort, PYSNMP_MODULE_ID=osL2PduGuard, L2ProtocolId=L2ProtocolId, osL2PduGuardTable=osL2PduGuardTable, osL2PduGuardCpMIBGroups=osL2PduGuardCpMIBGroups, osL2PduGuard=osL2PduGuard, osL2PduGuardMandatoryGroup=osL2PduGuardMandatoryGroup, osL2PduGuardCpGen=osL2PduGuardCpGen, osL2PduGuardCpMIBCompliance=osL2PduGuardCpMIBCompliance, osL2PduGuardSupprt=osL2PduGuardSupprt, osL2PduGuardCpConformance=osL2PduGuardCpConformance, osL2PduGuardInformRate=osL2PduGuardInformRate, osL2PduGuardEntry=osL2PduGuardEntry, osL2PduGuardProtocol=osL2PduGuardProtocol, osL2PduGuardCpMIBCompliances=osL2PduGuardCpMIBCompliances, SupportValue=SupportValue, osL2PduGuardIsolateRate=osL2PduGuardIsolateRate)
