#
# PySNMP MIB module GREENTECH-MASTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/gcom/GREENTECH-MASTER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
greentech = ModuleIdentity((1, 3, 6, 1, 4, 1, 13464))
greentech.setRevisions(('1900-08-29 00:00',))
if mibBuilder.loadTexts: greentech.setLastUpdated('0008290000Z')
if mibBuilder.loadTexts: greentech.setOrganization('Greentech')
dataCom = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1))
gbn = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 3))
gbnPlatform = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1))
gbnDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 2))
gbnService = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 3))
gbnL2 = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4))
gbnL3 = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 5))
gbnLS = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 6))
gbnServiceAAA = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 1))
rmonMib = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 3, 2))
mibBuilder.exportSymbols("GREENTECH-MASTER-MIB", gbn=gbn, gbnServiceAAA=gbnServiceAAA, greentech=greentech, gbnDevice=gbnDevice, gbnL3=gbnL3, gbnPlatform=gbnPlatform, rmonMib=rmonMib, PYSNMP_MODULE_ID=greentech, dataCom=dataCom, switch=switch, gbnL2=gbnL2, gbnService=gbnService, gbnLS=gbnLS)
