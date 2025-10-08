#
# PySNMP MIB module ADTRAN-SHARED-CND-SYSTEM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-CND-SYSTEM-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:08 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adGenSystemTCID, = mibBuilder.importSymbols("ADTRAN-SHARED-CND-SYSTEM-MIB", "adGenSystemTCID")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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

mibBuilder.exportSymbols("ADTRAN-SHARED-CND-SYSTEM-TC-MIB", adGenCndSystemTCIdentity=adGenCndSystemTCIdentity, GenSystemInterfaceType=GenSystemInterfaceType, PYSNMP_MODULE_ID=adGenCndSystemTCIdentity, AdGenTrapVersion=AdGenTrapVersion)
