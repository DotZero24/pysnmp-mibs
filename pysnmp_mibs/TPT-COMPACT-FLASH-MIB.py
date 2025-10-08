#
# PySNMP MIB module TPT-COMPACT-FLASH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trendmicro/TPT-COMPACT-FLASH-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_tpa_objs, tpt_tpa_unkparams, tpt_tpa_eventsV2 = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs", "tpt-tpa-unkparams", "tpt-tpa-eventsV2")
tpt_compact_flash = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14)).setLabel("tpt-compact-flash")
tpt_compact_flash.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_compact_flash.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_compact_flash.setOrganization('Trend Micro, Inc.')
class MountedOrNot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("mounted", 0), ("unmounted", 1))

class OperationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("secure", 0), ("auto-mount", 1))

class FormattedOrNot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("formatted", 0), ("unformatted", 1))

class PresentOrNot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("present", 0), ("absent", 1))

compactFlashPresent = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 1), PresentOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: compactFlashPresent.setStatus('current')
compactFlashMounted = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 2), MountedOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: compactFlashMounted.setStatus('current')
compactFlashFormatted = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 3), FormattedOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: compactFlashFormatted.setStatus('current')
compactFlashOperationMode = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 4), OperationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: compactFlashOperationMode.setStatus('current')
vendorInformation = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5))
if mibBuilder.loadTexts: vendorInformation.setStatus('current')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
model = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: model.setStatus('current')
capacity = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capacity.setStatus('current')
revision = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: revision.setStatus('current')
tptCompactFlashDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 261), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptCompactFlashDeviceID.setStatus('current')
tptCompactFlashDeviceStatus = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 262), PresentOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptCompactFlashDeviceStatus.setStatus('current')
tptCFInsertedNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 51)).setObjects(("TPT-COMPACT-FLASH-MIB", "tptCompactFlashDeviceID"), ("TPT-COMPACT-FLASH-MIB", "tptCompactFlashDeviceStatus"))
if mibBuilder.loadTexts: tptCFInsertedNotify.setStatus('current')
tptCFEjectedNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 52)).setObjects(("TPT-COMPACT-FLASH-MIB", "tptCompactFlashDeviceID"), ("TPT-COMPACT-FLASH-MIB", "tptCompactFlashDeviceStatus"))
if mibBuilder.loadTexts: tptCFEjectedNotify.setStatus('current')
mibBuilder.exportSymbols("TPT-COMPACT-FLASH-MIB", FormattedOrNot=FormattedOrNot, tptCompactFlashDeviceID=tptCompactFlashDeviceID, compactFlashFormatted=compactFlashFormatted, tpt_compact_flash=tpt_compact_flash, tptCFEjectedNotify=tptCFEjectedNotify, compactFlashMounted=compactFlashMounted, serialNumber=serialNumber, OperationMode=OperationMode, revision=revision, PresentOrNot=PresentOrNot, vendorInformation=vendorInformation, tptCompactFlashDeviceStatus=tptCompactFlashDeviceStatus, compactFlashPresent=compactFlashPresent, model=model, tptCFInsertedNotify=tptCFInsertedNotify, PYSNMP_MODULE_ID=tpt_compact_flash, capacity=capacity, compactFlashOperationMode=compactFlashOperationMode, MountedOrNot=MountedOrNot)
