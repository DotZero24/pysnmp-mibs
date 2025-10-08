#
# PySNMP MIB module NWAYSMSS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ibm/NWAYSMSS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:45:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
Integer32, = mibBuilder.importSymbols("SNMPv2-SMI-v1", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nwaysMSS = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118))
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
mssCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1))
mssCommonHWVPD = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 1))
mssCmnSrvrs = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2))
mssServerLanE = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1))
mssCmnClnts = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 3))
class AtmPrivateAddrEsi(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class AtmSelector(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class AtmVccTrafficType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bestEffort", 1), ("reservedBandwidth", 2))

class Bandwidth(Integer32):
    pass

mibBuilder.exportSymbols("NWAYSMSS-MIB", nwaysMSS=nwaysMSS, ibm=ibm, Bandwidth=Bandwidth, AtmVccTrafficType=AtmVccTrafficType, AtmSelector=AtmSelector, mssCmnSrvrs=mssCmnSrvrs, mssServerLanE=mssServerLanE, mssCmnClnts=mssCmnClnts, ibmProd=ibmProd, AtmPrivateAddrEsi=AtmPrivateAddrEsi, mssCommonHWVPD=mssCommonHWVPD, mssCommon=mssCommon)
