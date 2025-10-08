#
# PySNMP MIB module CISCO-IETF-PW-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-IETF-PW-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cpwTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 20000, 1))
cpwTCMIB.setRevisions(('2006-07-21 12:00', '2003-02-26 12:00', '2002-05-28 12:00', '2002-01-30 12:00', '2001-12-20 12:00', '2001-07-12 12:00',))
if mibBuilder.loadTexts: cpwTCMIB.setLastUpdated('200607211200Z')
if mibBuilder.loadTexts: cpwTCMIB.setOrganization('Cisco Systems, Inc.')
cpwMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 20000))
class CpwGroupID(TextualConvention, Unsigned32):
    status = 'current'

class CpwVcIDType(TextualConvention, Unsigned32):
    status = 'current'

class CpwVcIndexType(TextualConvention, Unsigned32):
    status = 'current'

class CpwVcVlanCfg(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4097)

class CpwOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7))

class CpwVcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("other", 0), ("frameRelay", 1), ("atmAal5Vcc", 2), ("atmTransparent", 3), ("ethernetVLAN", 4), ("ethernet", 5), ("hdlc", 6), ("ppp", 7), ("cep", 8), ("atmVccCell", 9), ("atmVpcCell", 10), ("ethernetVPLS", 11), ("e1Satop", 12), ("t1Satop", 13), ("e3Satop", 14), ("t3Satop", 15), ("basicCesPsn", 16), ("basicTdmIp", 17), ("tdmCasCesPsn", 18), ("tdmCasTdmIp", 19))

mibBuilder.exportSymbols("CISCO-IETF-PW-TC-MIB", cpwMIB=cpwMIB, PYSNMP_MODULE_ID=cpwTCMIB, CpwOperStatus=CpwOperStatus, cpwTCMIB=cpwTCMIB, CpwGroupID=CpwGroupID, CpwVcType=CpwVcType, CpwVcIndexType=CpwVcIndexType, CpwVcIDType=CpwVcIDType, CpwVcVlanCfg=CpwVcVlanCfg)
