#
# PySNMP MIB module MRV-PRIV-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/MRV-PRIV-TRAPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbPrivTraps = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 1, 50, 21))
nbPrivTraps.setRevisions(('2006-02-22 00:00',))
if mibBuilder.loadTexts: nbPrivTraps.setLastUpdated('200602220000Z')
if mibBuilder.loadTexts: nbPrivTraps.setOrganization('MRV Communications, Inc.')
nbase = MibIdentifier((1, 3, 6, 1, 4, 1, 629))
nbSwitchG1 = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1))
nbSwitchG1Il = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50))
mrvPrivateTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3))
mrvTrapParameters = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1))
mrvPrivateGenTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6))
mrvPrivateSpecTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7))
mrvPrivateTrapsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 100))
mrvPrivateTrapsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 100, 1))
mrvPrivateTrapsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 100, 2))
class TCEventClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("serviceAffecting", 1), ("nonServiceAffecting", 2))

class TCEventLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("info", 4), ("clear", 5))

class NbEthOamMepId(TextualConvention, Unsigned32):
    reference = '802.1ag clauses 3.19 and 19.2.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4095)

class NbEthOamMDLevel(TextualConvention, Integer32):
    reference = '802.1ag clauses 18.3, 21.4.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class NbEthOamCcmHighestDefectPri(TextualConvention, Integer32):
    reference = '802.1ag clause 20.1.2, 12.14.7.7.2:c and 20.33.9'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("defRDICCM", 1), ("defMACstatus", 2), ("defRemoteCCM", 3), ("defErrorCCM", 4), ("defXconCCM", 5))

mrvElementID = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvElementID.setStatus('current')
mrvPortIndex = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvPortIndex.setStatus('current')
mrvEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvEventDescription.setStatus('current')
mrvEventClass = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 8), TCEventClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvEventClass.setStatus('current')
mrvEventLevel = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 9), TCEventLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvEventLevel.setStatus('current')
mrvDevPSIndex = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvDevPSIndex.setStatus('current')
mrvDevFANIndex = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvDevFANIndex.setStatus('current')
mrvEthOamMdLevel = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 12), NbEthOamMDLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvEthOamMdLevel.setStatus('current')
mrvEthOamMaIndex = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvEthOamMaIndex.setStatus('current')
mrvEthOamMepIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 14), NbEthOamMepId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvEthOamMepIdentifier.setStatus('current')
mrvEthOamTrapCcmHighestPrDefect = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 15), NbEthOamCcmHighestDefectPri()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvEthOamTrapCcmHighestPrDefect.setStatus('current')
mrvDevLosGrActivePortNumber = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrvDevLosGrActivePortNumber.setStatus('current')
mrvDevLosGrPrimaryPort = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrvDevLosGrPrimaryPort.setStatus('current')
mrvDevLosGrSecondaryPort = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvDevLosGrSecondaryPort.setStatus('current')
mrvDevLosGrActionCause = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("noAction", 1), ("portLinkUp", 2), ("portLinkDown", 3), ("agRMepDiscardEvent", 4), ("agRMepNoConnEvent", 5), ("agRMepAliveEvent", 6), ("activePortAdminSet", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvDevLosGrActionCause.setStatus('current')
mrvPortLinSlavePorts = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mrvPortLinSlavePorts.setStatus('current')
mrvPortLinActionCause = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noAction", 1), ("portLinkUp", 2), ("portLinkDown", 3), ("agRMepDiscardEvent", 4), ("agRMepNoConnEvent", 5), ("agRMepAliveEvent", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mrvPortLinActionCause.setStatus('current')
mrvPrivateGenTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6, 0))
mrvColdStart = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6, 0, 1)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"))
if mibBuilder.loadTexts: mrvColdStart.setStatus('current')
mrvWarmStart = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6, 0, 2)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"))
if mibBuilder.loadTexts: mrvWarmStart.setStatus('current')
mrvPortLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6, 0, 3)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"), ("MRV-PRIV-TRAPS-MIB", "mrvPortIndex"))
if mibBuilder.loadTexts: mrvPortLinkDown.setStatus('current')
mrvPortLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6, 0, 4)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"), ("MRV-PRIV-TRAPS-MIB", "mrvPortIndex"))
if mibBuilder.loadTexts: mrvPortLinkUp.setStatus('current')
mrvAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6, 0, 5)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"))
if mibBuilder.loadTexts: mrvAuthenticationFailure.setStatus('current')
mrvPrivateSpecTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0))
mrvPowerSupplyUp = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 1)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"), ("MRV-PRIV-TRAPS-MIB", "mrvDevPSIndex"))
if mibBuilder.loadTexts: mrvPowerSupplyUp.setStatus('current')
mrvPowerSupplyDown = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 2)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"), ("MRV-PRIV-TRAPS-MIB", "mrvDevPSIndex"))
if mibBuilder.loadTexts: mrvPowerSupplyDown.setStatus('current')
mrvFANUnitUp = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 3)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"), ("MRV-PRIV-TRAPS-MIB", "mrvDevFANIndex"))
if mibBuilder.loadTexts: mrvFANUnitUp.setStatus('current')
mrvFANUnitDown = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 4)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"), ("MRV-PRIV-TRAPS-MIB", "mrvDevFANIndex"))
if mibBuilder.loadTexts: mrvFANUnitDown.setStatus('current')
mrvDeviceTemperatureNormal = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 5)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"))
if mibBuilder.loadTexts: mrvDeviceTemperatureNormal.setStatus('current')
mrvDeviceTemperatureHigh = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 6)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"))
if mibBuilder.loadTexts: mrvDeviceTemperatureHigh.setStatus('current')
mrvDot1agCfmFault = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 7)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"), ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMdLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMaIndex"), ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMepIdentifier"), ("MRV-PRIV-TRAPS-MIB", "mrvEthOamTrapCcmHighestPrDefect"))
if mibBuilder.loadTexts: mrvDot1agCfmFault.setStatus('current')
mrvDot1agCfmRecovery = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 8)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"), ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMdLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMaIndex"), ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMepIdentifier"), ("MRV-PRIV-TRAPS-MIB", "mrvEthOamTrapCcmHighestPrDefect"))
if mibBuilder.loadTexts: mrvDot1agCfmRecovery.setStatus('current')
mrvPortProtectionBackup = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 9)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"), ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrActivePortNumber"), ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrPrimaryPort"), ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrSecondaryPort"), ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrActionCause"))
if mibBuilder.loadTexts: mrvPortProtectionBackup.setStatus('current')
mrvPortProtectionPrimary = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 10)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"), ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrActivePortNumber"), ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrPrimaryPort"), ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrSecondaryPort"), ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrActionCause"))
if mibBuilder.loadTexts: mrvPortProtectionPrimary.setStatus('current')
mrvPortReflectionLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 11)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"), ("MRV-PRIV-TRAPS-MIB", "mrvPortIndex"), ("MRV-PRIV-TRAPS-MIB", "mrvPortLinSlavePorts"), ("MRV-PRIV-TRAPS-MIB", "mrvPortLinActionCause"))
if mibBuilder.loadTexts: mrvPortReflectionLinkDown.setStatus('current')
mrvPortReflectionLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 12)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"), ("MRV-PRIV-TRAPS-MIB", "mrvPortIndex"), ("MRV-PRIV-TRAPS-MIB", "mrvPortLinSlavePorts"), ("MRV-PRIV-TRAPS-MIB", "mrvPortLinActionCause"))
if mibBuilder.loadTexts: mrvPortReflectionLinkUp.setStatus('current')
mrvPrivateTrapsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 100, 1, 1)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvPrivateTrapsMandatoryGroup"), ("MRV-PRIV-TRAPS-MIB", "mrvPrivateTrapsNotifGrp"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mrvPrivateTrapsMIBCompliance = mrvPrivateTrapsMIBCompliance.setStatus('current')
mrvPrivateTrapsMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 100, 2, 1)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvPortIndex"), ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"), ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"), ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvElementID"), ("MRV-PRIV-TRAPS-MIB", "mrvDevPSIndex"), ("MRV-PRIV-TRAPS-MIB", "mrvDevFANIndex"), ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMdLevel"), ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMaIndex"), ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMepIdentifier"), ("MRV-PRIV-TRAPS-MIB", "mrvEthOamTrapCcmHighestPrDefect"), ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrActivePortNumber"), ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrPrimaryPort"), ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrSecondaryPort"), ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrActionCause"), ("MRV-PRIV-TRAPS-MIB", "mrvPortLinSlavePorts"), ("MRV-PRIV-TRAPS-MIB", "mrvPortLinActionCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mrvPrivateTrapsMandatoryGroup = mrvPrivateTrapsMandatoryGroup.setStatus('current')
mrvPrivateTrapsNotifGrp = NotificationGroup((1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 100, 2, 2)).setObjects(("MRV-PRIV-TRAPS-MIB", "mrvColdStart"), ("MRV-PRIV-TRAPS-MIB", "mrvWarmStart"), ("MRV-PRIV-TRAPS-MIB", "mrvPortLinkUp"), ("MRV-PRIV-TRAPS-MIB", "mrvPortLinkDown"), ("MRV-PRIV-TRAPS-MIB", "mrvAuthenticationFailure"), ("MRV-PRIV-TRAPS-MIB", "mrvPowerSupplyUp"), ("MRV-PRIV-TRAPS-MIB", "mrvPowerSupplyDown"), ("MRV-PRIV-TRAPS-MIB", "mrvFANUnitUp"), ("MRV-PRIV-TRAPS-MIB", "mrvFANUnitDown"), ("MRV-PRIV-TRAPS-MIB", "mrvDeviceTemperatureNormal"), ("MRV-PRIV-TRAPS-MIB", "mrvDeviceTemperatureHigh"), ("MRV-PRIV-TRAPS-MIB", "mrvDot1agCfmFault"), ("MRV-PRIV-TRAPS-MIB", "mrvDot1agCfmRecovery"), ("MRV-PRIV-TRAPS-MIB", "mrvPortProtectionBackup"), ("MRV-PRIV-TRAPS-MIB", "mrvPortProtectionPrimary"), ("MRV-PRIV-TRAPS-MIB", "mrvPortReflectionLinkDown"), ("MRV-PRIV-TRAPS-MIB", "mrvPortReflectionLinkUp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mrvPrivateTrapsNotifGrp = mrvPrivateTrapsNotifGrp.setStatus('current')
mibBuilder.exportSymbols("MRV-PRIV-TRAPS-MIB", mrvPrivateTrapsMIBCompliances=mrvPrivateTrapsMIBCompliances, mrvEventDescription=mrvEventDescription, mrvEthOamTrapCcmHighestPrDefect=mrvEthOamTrapCcmHighestPrDefect, mrvDot1agCfmRecovery=mrvDot1agCfmRecovery, mrvDevLosGrActionCause=mrvDevLosGrActionCause, mrvEventClass=mrvEventClass, mrvPortProtectionBackup=mrvPortProtectionBackup, mrvPortProtectionPrimary=mrvPortProtectionPrimary, mrvWarmStart=mrvWarmStart, mrvPrivateTrapsConformance=mrvPrivateTrapsConformance, nbPrivTraps=nbPrivTraps, NbEthOamCcmHighestDefectPri=NbEthOamCcmHighestDefectPri, mrvEthOamMepIdentifier=mrvEthOamMepIdentifier, mrvPortIndex=mrvPortIndex, mrvElementID=mrvElementID, mrvPrivateTrapsMIBGroups=mrvPrivateTrapsMIBGroups, mrvPrivateGenTrapPrefix=mrvPrivateGenTrapPrefix, mrvColdStart=mrvColdStart, mrvEthOamMdLevel=mrvEthOamMdLevel, mrvPrivateTrapsMandatoryGroup=mrvPrivateTrapsMandatoryGroup, mrvPrivateTrapsMIBCompliance=mrvPrivateTrapsMIBCompliance, mrvPowerSupplyUp=mrvPowerSupplyUp, mrvPortLinkUp=mrvPortLinkUp, mrvPrivateSpecTrapPrefix=mrvPrivateSpecTrapPrefix, mrvPrivateTraps=mrvPrivateTraps, mrvEventLevel=mrvEventLevel, mrvDevPSIndex=mrvDevPSIndex, mrvPortReflectionLinkDown=mrvPortReflectionLinkDown, mrvDevLosGrActivePortNumber=mrvDevLosGrActivePortNumber, mrvPortLinSlavePorts=mrvPortLinSlavePorts, mrvDevFANIndex=mrvDevFANIndex, mrvFANUnitUp=mrvFANUnitUp, mrvEthOamMaIndex=mrvEthOamMaIndex, mrvDevLosGrSecondaryPort=mrvDevLosGrSecondaryPort, nbase=nbase, mrvFANUnitDown=mrvFANUnitDown, mrvPortReflectionLinkUp=mrvPortReflectionLinkUp, mrvPrivateTrapsNotifGrp=mrvPrivateTrapsNotifGrp, nbSwitchG1=nbSwitchG1, mrvPrivateSpecTraps=mrvPrivateSpecTraps, NbEthOamMepId=NbEthOamMepId, NbEthOamMDLevel=NbEthOamMDLevel, mrvPrivateGenTraps=mrvPrivateGenTraps, nbSwitchG1Il=nbSwitchG1Il, mrvTrapParameters=mrvTrapParameters, mrvPortLinActionCause=mrvPortLinActionCause, mrvPowerSupplyDown=mrvPowerSupplyDown, mrvDevLosGrPrimaryPort=mrvDevLosGrPrimaryPort, PYSNMP_MODULE_ID=nbPrivTraps, mrvDot1agCfmFault=mrvDot1agCfmFault, TCEventLevel=TCEventLevel, TCEventClass=TCEventClass, mrvDeviceTemperatureHigh=mrvDeviceTemperatureHigh, mrvDeviceTemperatureNormal=mrvDeviceTemperatureNormal, mrvPortLinkDown=mrvPortLinkDown, mrvAuthenticationFailure=mrvAuthenticationFailure)
