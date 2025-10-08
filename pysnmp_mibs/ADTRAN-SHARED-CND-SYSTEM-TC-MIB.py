#
# PySNMP MIB module ADTRAN-SHARED-CND-SYSTEM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-CND-SYSTEM-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adGenSystemTCID, = mibBuilder.importSymbols("ADTRAN-SHARED-CND-SYSTEM-MIB", "adGenSystemTCID")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenCndSystemTCIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 14, 1))
adGenCndSystemTCIdentity.setRevisions(('2019-06-20 00:00', '2014-08-26 00:00', '2014-07-02 00:00', '2012-03-23 00:00', '2012-03-21 00:00', '2012-01-05 00:00', '2009-03-26 00:00',))
if mibBuilder.loadTexts: adGenCndSystemTCIdentity.setLastUpdated('201906200000Z')
if mibBuilder.loadTexts: adGenCndSystemTCIdentity.setOrganization('Adtran, Inc.')
class GenSystemInterfaceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43))
    namedValues = NamedValues(("unknown", 1), ("ds1", 2), ("dsx1", 3), ("e1", 4), ("dsxE1", 5), ("gigabitEthernet", 6), ("ds3", 7), ("portChannel", 8), ("tenGigabitEthernet", 9), ("erps", 10), ("shdsl", 11), ("adsl", 12), ("vdsl", 13), ("efmGroup", 14), ("efmLink", 15), ("efmPort", 16), ("lagGroup", 17), ("pppGroup", 18), ("imaGroup", 19), ("imaLink", 20), ("atm", 21), ("fxs", 22), ("hdsl2", 23), ("hdsl4", 24), ("adsl2", 25), ("vdsl2", 26), ("ethernet", 27), ("fast", 28), ("interleave", 29), ("hdsl", 30), ("gpon", 31), ("ipHost", 32), ("frpvc", 33), ("sonet", 34), ("otn", 35), ("wan", 36), ("defaultEthernet", 37), ("genericBridge", 38), ("fibreChannel", 39), ("otnTenGigabitEthernet", 40), ("hundredGigabitEthernet", 41), ("otnHundredGigabitEthernet", 42), ("xgigabitEthernet", 43))

class AdGenTrapVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("snmpV1", 1), ("snmpV2", 2))

mibBuilder.exportSymbols("ADTRAN-SHARED-CND-SYSTEM-TC-MIB", GenSystemInterfaceType=GenSystemInterfaceType, PYSNMP_MODULE_ID=adGenCndSystemTCIdentity, adGenCndSystemTCIdentity=adGenCndSystemTCIdentity, AdGenTrapVersion=AdGenTrapVersion)
