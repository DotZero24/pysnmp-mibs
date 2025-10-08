#
# PySNMP MIB module MARVELL-GREEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/radlan/MARVELL-GREEN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlGreenEth = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 134))
rlGreenEth.setRevisions(('2008-08-15 00:00',))
if mibBuilder.loadTexts: rlGreenEth.setLastUpdated('200808150000Z')
if mibBuilder.loadTexts: rlGreenEth.setOrganization('MARVELL Semiconductor, Inc.')
rlGreenEthEnergyDetectEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 134, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthEnergyDetectEnable.setStatus('current')
rlGreenEthShortReachEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 134, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthShortReachEnable.setStatus('current')
rlGreenEthCurrentEnergyConsumption = MibScalar((1, 3, 6, 1, 4, 1, 89, 134, 3), Unsigned32()).setUnits('mWatt').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCurrentEnergyConsumption.setStatus('current')
rlGreenEthCurrentMaxEnergyConsumption = MibScalar((1, 3, 6, 1, 4, 1, 89, 134, 4), Unsigned32()).setUnits('mWatt').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCurrentMaxEnergyConsumption.setStatus('current')
rlGreenEthCumulativePowerSaveMeter = MibScalar((1, 3, 6, 1, 4, 1, 89, 134, 5), Unsigned32()).setUnits('Watt*Hour').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeter.setStatus('current')
rlGreenEthShortReachThreshold = MibScalar((1, 3, 6, 1, 4, 1, 89, 134, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 70))).setUnits('meter').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthShortReachThreshold.setStatus('current')
rlGreenEthCumulativePowerSaveMeterReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 134, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeterReset.setStatus('current')
class RlGreenSavingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("energyDetect", 1), ("shortReach", 2))

class NonOperReasonType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("np", 1), ("lt", 2), ("lu", 3), ("ls", 4), ("ll", 5), ("er", 6), ("ld", 7), ("unknown", 8))

rlGreenEthPortTable = MibTable((1, 3, 6, 1, 4, 1, 89, 134, 8), )
if mibBuilder.loadTexts: rlGreenEthPortTable.setStatus('current')
rlGreenEthPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 134, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MARVELL-GREEN-MIB", "rlGreenEthPortSavingTypeValue"))
if mibBuilder.loadTexts: rlGreenEthPortEntry.setStatus('current')
rlGreenEthPortSavingTypeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 134, 8, 1, 1), RlGreenSavingType())
if mibBuilder.loadTexts: rlGreenEthPortSavingTypeValue.setStatus('current')
rlGreenEthPortAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 134, 8, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthPortAdminState.setStatus('current')
rlGreenEthPortOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 134, 8, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthPortOperState.setStatus('current')
rlGreenEthPortNonOperReason = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 134, 8, 1, 4), NonOperReasonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthPortNonOperReason.setStatus('current')
rlGreenEthForceShortReachIfIndexList = MibScalar((1, 3, 6, 1, 4, 1, 89, 134, 9), PortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthForceShortReachIfIndexList.setStatus('current')
rlGreenEthMaskLedStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 134, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthMaskLedStatus.setStatus('current')
mibBuilder.exportSymbols("MARVELL-GREEN-MIB", rlGreenEth=rlGreenEth, RlGreenSavingType=RlGreenSavingType, rlGreenEthPortEntry=rlGreenEthPortEntry, rlGreenEthPortSavingTypeValue=rlGreenEthPortSavingTypeValue, rlGreenEthPortAdminState=rlGreenEthPortAdminState, rlGreenEthCumulativePowerSaveMeter=rlGreenEthCumulativePowerSaveMeter, NonOperReasonType=NonOperReasonType, rlGreenEthCurrentEnergyConsumption=rlGreenEthCurrentEnergyConsumption, rlGreenEthForceShortReachIfIndexList=rlGreenEthForceShortReachIfIndexList, rlGreenEthPortOperState=rlGreenEthPortOperState, rlGreenEthPortTable=rlGreenEthPortTable, rlGreenEthCurrentMaxEnergyConsumption=rlGreenEthCurrentMaxEnergyConsumption, rlGreenEthEnergyDetectEnable=rlGreenEthEnergyDetectEnable, rlGreenEthCumulativePowerSaveMeterReset=rlGreenEthCumulativePowerSaveMeterReset, rlGreenEthShortReachThreshold=rlGreenEthShortReachThreshold, PYSNMP_MODULE_ID=rlGreenEth, rlGreenEthShortReachEnable=rlGreenEthShortReachEnable, rlGreenEthMaskLedStatus=rlGreenEthMaskLedStatus, rlGreenEthPortNonOperReason=rlGreenEthPortNonOperReason)
