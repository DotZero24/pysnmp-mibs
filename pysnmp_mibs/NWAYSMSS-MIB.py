#
# PySNMP MIB module NWAYSMSS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ibm/NWAYSMSS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:41 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
Integer32, = mibBuilder.importSymbols("SNMPv2-SMI-v1", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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

mibBuilder.exportSymbols("NWAYSMSS-MIB", ibmProd=ibmProd, AtmVccTrafficType=AtmVccTrafficType, AtmPrivateAddrEsi=AtmPrivateAddrEsi, mssCommon=mssCommon, AtmSelector=AtmSelector, nwaysMSS=nwaysMSS, mssCommonHWVPD=mssCommonHWVPD, mssCmnClnts=mssCmnClnts, mssCmnSrvrs=mssCmnSrvrs, ibm=ibm, Bandwidth=Bandwidth, mssServerLanE=mssServerLanE)
