#
# PySNMP MIB module HPOV-SNMPSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPOV-SNMPSEC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
openView = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17))
class OVTDAddress(TextualConvention, OctetString):
    reference = 'RFC 1906, Transport Mappings for SNMP Version 2'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

hpOVSNMPSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17, 5))
hpOVSecureTarget = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 5, 1), OVTDAddress())
if mibBuilder.loadTexts: hpOVSecureTarget.setStatus('current')
mibBuilder.exportSymbols("HPOV-SNMPSEC-MIB", OVTDAddress=OVTDAddress, hpOVSNMPSecurity=hpOVSNMPSecurity, hpOVSecureTarget=hpOVSecureTarget, openView=openView, hp=hp, nm=nm)
