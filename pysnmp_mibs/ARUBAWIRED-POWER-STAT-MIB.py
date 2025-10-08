#
# PySNMP MIB module ARUBAWIRED-POWER-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aruba/ARUBAWIRED-POWER-STAT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
arubaWiredChassisMIB, = mibBuilder.importSymbols("ARUBAWIRED-CHASSIS-MIB", "arubaWiredChassisMIB")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaWiredPowerStat = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8))
arubaWiredPowerStat.setRevisions(('2023-07-25 00:00', '2023-06-20 00:00',))
if mibBuilder.loadTexts: arubaWiredPowerStat.setLastUpdated('202307250000Z')
if mibBuilder.loadTexts: arubaWiredPowerStat.setOrganization('HPE/Aruba Networking Division')
arubaWiredPowerStatNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 0))
arubaWiredPowerStatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1))
arubaWiredPowerStatConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 2))
class RealDecTwo(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'

arubaWiredPowerStatSys = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0))
arubaWiredPowerStatTable = MibTable((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1), )
if mibBuilder.loadTexts: arubaWiredPowerStatTable.setStatus('current')
arubaWiredPowerStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1), ).setIndexNames((0, "ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatGroupIndex"), (0, "ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatTypeIndex"), (0, "ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatSlotIndex"))
if mibBuilder.loadTexts: arubaWiredPowerStatEntry.setStatus('current')
arubaWiredPowerStatGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: arubaWiredPowerStatGroupIndex.setStatus('current')
arubaWiredPowerStatTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: arubaWiredPowerStatTypeIndex.setStatus('current')
arubaWiredPowerStatSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: arubaWiredPowerStatSlotIndex.setStatus('current')
arubaWiredPowerStatName = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredPowerStatName.setStatus('current')
arubaWiredPowerStatType = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredPowerStatType.setStatus('current')
arubaWiredPowerStatPowerConsumed = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredPowerStatPowerConsumed.setStatus('current')
arubaWiredPowerStatPowerConsumedAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 7), RealDecTwo()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredPowerStatPowerConsumedAverage.setStatus('current')
arubaWiredPowerStatPowerConsumedAveragePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 1, 0, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 3600)).clone(600)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredPowerStatPowerConsumedAveragePeriod.setStatus('current')
arubaWiredPowerStatCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 2, 1))
arubaWiredPowerStatGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 2, 2))
arubaWiredPowerStatTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 2, 2, 1)).setObjects(("ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatName"), ("ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatType"), ("ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatPowerConsumed"), ("ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatPowerConsumedAverage"), ("ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatPowerConsumedAveragePeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredPowerStatTableGroup = arubaWiredPowerStatTableGroup.setStatus('current')
arubaWiredPowerStatCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8, 2, 1, 1)).setObjects(("ARUBAWIRED-POWER-STAT-MIB", "arubaWiredPowerStatTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredPowerStatCompliance = arubaWiredPowerStatCompliance.setStatus('current')
mibBuilder.exportSymbols("ARUBAWIRED-POWER-STAT-MIB", arubaWiredPowerStatConformance=arubaWiredPowerStatConformance, arubaWiredPowerStatCompliance=arubaWiredPowerStatCompliance, arubaWiredPowerStatType=arubaWiredPowerStatType, arubaWiredPowerStatObjects=arubaWiredPowerStatObjects, arubaWiredPowerStatTable=arubaWiredPowerStatTable, arubaWiredPowerStatName=arubaWiredPowerStatName, arubaWiredPowerStat=arubaWiredPowerStat, arubaWiredPowerStatSys=arubaWiredPowerStatSys, arubaWiredPowerStatGroupIndex=arubaWiredPowerStatGroupIndex, arubaWiredPowerStatPowerConsumedAverage=arubaWiredPowerStatPowerConsumedAverage, arubaWiredPowerStatNotifications=arubaWiredPowerStatNotifications, arubaWiredPowerStatTypeIndex=arubaWiredPowerStatTypeIndex, arubaWiredPowerStatEntry=arubaWiredPowerStatEntry, arubaWiredPowerStatCompliances=arubaWiredPowerStatCompliances, arubaWiredPowerStatSlotIndex=arubaWiredPowerStatSlotIndex, PYSNMP_MODULE_ID=arubaWiredPowerStat, arubaWiredPowerStatGroups=arubaWiredPowerStatGroups, RealDecTwo=RealDecTwo, arubaWiredPowerStatTableGroup=arubaWiredPowerStatTableGroup, arubaWiredPowerStatPowerConsumedAveragePeriod=arubaWiredPowerStatPowerConsumedAveragePeriod, arubaWiredPowerStatPowerConsumed=arubaWiredPowerStatPowerConsumed)
