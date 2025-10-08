#
# PySNMP MIB module OCNOS-VR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ipinfusion/OCNOS-VR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:17 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
ipi, = mibBuilder.importSymbols("OCNOS-IPI-MODULE-MIB", "ipi")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
ModuleIdentity, Counter64, enterprises, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, DateAndTime, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "DateAndTime", "PhysAddress", "TextualConvention")
vr = ModuleIdentity((1, 3, 6, 1, 4, 1, 36673, 2))
vr.setRevisions(('2018-06-21 00:00',))
if mibBuilder.loadTexts: vr.setLastUpdated('201806210000Z')
if mibBuilder.loadTexts: vr.setOrganization('IP Infusion Inc.')
vrVrTable = MibTable((1, 3, 6, 1, 4, 1, 36673, 2, 1), )
if mibBuilder.loadTexts: vrVrTable.setStatus('current')
vrVrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36673, 2, 1, 1), ).setIndexNames((0, "OCNOS-VR-MIB", "vrVrId"))
if mibBuilder.loadTexts: vrVrEntry.setStatus('current')
vrVrId = MibTableColumn((1, 3, 6, 1, 4, 1, 36673, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrVrId.setStatus('current')
vrName = MibTableColumn((1, 3, 6, 1, 4, 1, 36673, 2, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrName.setStatus('current')
mibBuilder.exportSymbols("OCNOS-VR-MIB", PYSNMP_MODULE_ID=vr, vrName=vrName, vrVrEntry=vrVrEntry, vrVrId=vrVrId, vr=vr, vrVrTable=vrVrTable)
