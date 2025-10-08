#
# PySNMP MIB module HPNSARPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPNSARPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
hpnsa = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23))
hpnsaRPS = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 22))
hpnsaRPSMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 22, 1))
hpnsaRPSMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 22, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaRPSMibRevMajor.setStatus('mandatory')
hpnsaRPSMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 22, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaRPSMibRevMinor.setStatus('mandatory')
mibBuilder.exportSymbols("HPNSARPS-MIB", hpnsaRPSMibRev=hpnsaRPSMibRev, hpnsaRPS=hpnsaRPS, hp=hp, nm=nm, hpnsaRPSMibRevMinor=hpnsaRPSMibRevMinor, hpnsa=hpnsa, hpnsaRPSMibRevMajor=hpnsaRPSMibRevMajor)
