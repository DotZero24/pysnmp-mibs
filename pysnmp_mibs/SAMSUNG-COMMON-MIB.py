#
# PySNMP MIB module SAMSUNG-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/samsung/SAMSUNG-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
samsung = ModuleIdentity((1, 3, 6, 1, 4, 1, 236))
if mibBuilder.loadTexts: samsung.setLastUpdated('0209170000Z')
if mibBuilder.loadTexts: samsung.setOrganization('Samsung Corporation - Samsung DPD Solution SW Team')
division = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11))
if mibBuilder.loadTexts: division.setStatus('current')
oadivision = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5))
if mibBuilder.loadTexts: oadivision.setStatus('current')
samsungCommonMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11))
if mibBuilder.loadTexts: samsungCommonMIB.setStatus('current')
mibBuilder.exportSymbols("SAMSUNG-COMMON-MIB", samsungCommonMIB=samsungCommonMIB, samsung=samsung, PYSNMP_MODULE_ID=samsung, division=division, oadivision=oadivision)
