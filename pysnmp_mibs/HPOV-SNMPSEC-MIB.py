#
# PySNMP MIB module HPOV-SNMPSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPOV-SNMPSEC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("HPOV-SNMPSEC-MIB", hpOVSecureTarget=hpOVSecureTarget, hp=hp, nm=nm, hpOVSNMPSecurity=hpOVSNMPSecurity, openView=openView, OVTDAddress=OVTDAddress)
