#
# PySNMP MIB module IPE-TERM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nec/IPE-TERM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:44 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Opaque, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Opaque", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class OffOnValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("invalid", 0), ("off", 1), ("on", 2))

class SeverityValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 1), ("indetermine", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6))

nec = MibIdentifier((1, 3, 6, 1, 4, 1, 119))
nec_mib = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2)).setLabel("nec-mib")
necProductDepend = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3))
radioEquipment = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 69))
pasoNeoIpe_common = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501)).setLabel("pasoNeoIpe-common")
alarmStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3))
asTermCardGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36))
asTermCardTable = MibTable((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1), )
if mibBuilder.loadTexts: asTermCardTable.setStatus('current')
asTermCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1), ).setIndexNames((0, "IPE-TERM-MIB", "asTermCardIndex"))
if mibBuilder.loadTexts: asTermCardEntry.setStatus('current')
asTermCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: asTermCardIndex.setStatus('current')
asTermCardNEAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 2), IpAddress())
if mibBuilder.loadTexts: asTermCardNEAddress.setStatus('current')
termAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 3), SeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: termAlarm.setStatus('current')
termComFailAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 4), SeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: termComFailAlarm.setStatus('current')
termUnequipped = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 5), SeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: termUnequipped.setStatus('current')
termTypeMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 6), SeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: termTypeMismatch.setStatus('current')
termCardChange = MibTableColumn((1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 36, 1, 1, 7), OffOnValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: termCardChange.setStatus('current')
mibBuilder.exportSymbols("IPE-TERM-MIB", termTypeMismatch=termTypeMismatch, necProductDepend=necProductDepend, alarmStatusGroup=alarmStatusGroup, asTermCardTable=asTermCardTable, asTermCardIndex=asTermCardIndex, termUnequipped=termUnequipped, OffOnValue=OffOnValue, asTermCardGroup=asTermCardGroup, termCardChange=termCardChange, nec_mib=nec_mib, radioEquipment=radioEquipment, pasoNeoIpe_common=pasoNeoIpe_common, termComFailAlarm=termComFailAlarm, termAlarm=termAlarm, nec=nec, asTermCardEntry=asTermCardEntry, SeverityValue=SeverityValue, asTermCardNEAddress=asTermCardNEAddress)
