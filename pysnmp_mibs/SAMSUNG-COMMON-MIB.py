#
# PySNMP MIB module SAMSUNG-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/samsung/SAMSUNG-COMMON-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
samsung = ModuleIdentity((1, 3, 6, 1, 4, 1, 236))
if mibBuilder.loadTexts: samsung.setLastUpdated('0209170000Z')
if mibBuilder.loadTexts: samsung.setOrganization('Samsung Corporation - Samsung DPD Solution SW Team')
division = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11))
if mibBuilder.loadTexts: division.setStatus('current')
oadivision = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5))
if mibBuilder.loadTexts: oadivision.setStatus('current')
samsungCommonMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11))
if mibBuilder.loadTexts: samsungCommonMIB.setStatus('current')
mibBuilder.exportSymbols("SAMSUNG-COMMON-MIB", oadivision=oadivision, samsung=samsung, PYSNMP_MODULE_ID=samsung, samsungCommonMIB=samsungCommonMIB, division=division)
