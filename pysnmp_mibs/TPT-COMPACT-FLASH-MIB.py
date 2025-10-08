#
# PySNMP MIB module TPT-COMPACT-FLASH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trendmicro/TPT-COMPACT-FLASH-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("TPT-COMPACT-FLASH-MIB", revision=revision, tpt_compact_flash=tpt_compact_flash, capacity=capacity, MountedOrNot=MountedOrNot, compactFlashPresent=compactFlashPresent, OperationMode=OperationMode, tptCompactFlashDeviceID=tptCompactFlashDeviceID, tptCFEjectedNotify=tptCFEjectedNotify, serialNumber=serialNumber, model=model, compactFlashOperationMode=compactFlashOperationMode, vendorInformation=vendorInformation, compactFlashMounted=compactFlashMounted, tptCFInsertedNotify=tptCFInsertedNotify, FormattedOrNot=FormattedOrNot, compactFlashFormatted=compactFlashFormatted, tptCompactFlashDeviceStatus=tptCompactFlashDeviceStatus, PresentOrNot=PresentOrNot, PYSNMP_MODULE_ID=tpt_compact_flash)
