#
# PySNMP MIB module IPE-TERM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nec/IPE-TERM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32, Opaque = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32", "Opaque")
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
mibBuilder.exportSymbols("IPE-TERM-MIB", asTermCardTable=asTermCardTable, termCardChange=termCardChange, asTermCardIndex=asTermCardIndex, nec_mib=nec_mib, SeverityValue=SeverityValue, asTermCardNEAddress=asTermCardNEAddress, necProductDepend=necProductDepend, termAlarm=termAlarm, pasoNeoIpe_common=pasoNeoIpe_common, termUnequipped=termUnequipped, asTermCardGroup=asTermCardGroup, asTermCardEntry=asTermCardEntry, termTypeMismatch=termTypeMismatch, alarmStatusGroup=alarmStatusGroup, OffOnValue=OffOnValue, nec=nec, termComFailAlarm=termComFailAlarm, radioEquipment=radioEquipment)
