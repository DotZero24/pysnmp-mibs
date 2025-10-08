#
# PySNMP MIB module QTECH-MASTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-MASTER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
qtech = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514))
qtech.setRevisions(('1900-08-29 00:00',))
if mibBuilder.loadTexts: qtech.setLastUpdated('0008290000Z')
if mibBuilder.loadTexts: qtech.setOrganization('QTECH LLC.')
dataCom = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1))
gbn = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 2))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 3))
gbnPlatform = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 2, 1))
gbnDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 2, 2))
gbnService = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 2, 3))
gbnL2 = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 2, 4))
gbnL3 = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 2, 5))
gbnLS = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 2, 6))
gbnServiceAAA = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 2, 3, 1))
rmonMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 2, 3, 2))
QSW_2724 = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 3, 11))
QSW_3924 = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 3, 18))
mibBuilder.exportSymbols("QTECH-MASTER-MIB", gbnPlatform=gbnPlatform, gbnLS=gbnLS, switch=switch, gbnL2=gbnL2, dataCom=dataCom, gbnDevice=gbnDevice, rmonMib=rmonMib, gbnL3=gbnL3, gbnService=gbnService, qtech=qtech, PYSNMP_MODULE_ID=qtech, QSW_3924=QSW_3924, QSW_2724=QSW_2724, gbn=gbn, gbnServiceAAA=gbnServiceAAA)
