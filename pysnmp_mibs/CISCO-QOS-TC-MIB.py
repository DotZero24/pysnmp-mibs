#
# PySNMP MIB module CISCO-QOS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-QOS-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:26:35 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoQosTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 573))
ciscoQosTcMIB.setRevisions(('2007-03-05 00:00', '2006-09-18 12:00',))
if mibBuilder.loadTexts: ciscoQosTcMIB.setLastUpdated('200703050000Z')
if mibBuilder.loadTexts: ciscoQosTcMIB.setOrganization('Cisco Systems, Inc.')
class QosIpPrecedence(TextualConvention, Unsigned32):
    reference = 'RFC791 INTERNET PROTOCOL, Chapter 3.1'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class QosQueueNumber(TextualConvention, Unsigned32):
    status = 'current'

class QosThresholdNumber(TextualConvention, Unsigned32):
    status = 'current'

class QosMplsExpValue(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class QosMutationMapName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '99a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 99)

class QosMutationMapNameOrEmpty(TextualConvention, OctetString):
    status = 'current'
    displayHint = '99a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 99)

class QosPolicerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("microflow", 1), ("aggregate", 2))

mibBuilder.exportSymbols("CISCO-QOS-TC-MIB", QosMutationMapNameOrEmpty=QosMutationMapNameOrEmpty, QosIpPrecedence=QosIpPrecedence, QosMutationMapName=QosMutationMapName, QosThresholdNumber=QosThresholdNumber, QosPolicerType=QosPolicerType, ciscoQosTcMIB=ciscoQosTcMIB, QosQueueNumber=QosQueueNumber, QosMplsExpValue=QosMplsExpValue, PYSNMP_MODULE_ID=ciscoQosTcMIB)
