#
# PySNMP MIB module SCTE-HMS-HE-OPTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/scte/SCTE-HMS-HE-OPTICS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
heOptics, = mibBuilder.importSymbols("SCTE-HMS-HEADENDIDENT-MIB", "heOptics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
heOpticsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 0))
if mibBuilder.loadTexts: heOpticsMib.setLastUpdated('200302170000Z')
if mibBuilder.loadTexts: heOpticsMib.setOrganization('SCTE HMS Working Group')
heOpticalTransmitterGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1))
if mibBuilder.loadTexts: heOpticalTransmitterGroup.setStatus('current')
heOpticalReceiverGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2))
if mibBuilder.loadTexts: heOpticalReceiverGroup.setStatus('current')
heOpticalAmplifierGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3))
if mibBuilder.loadTexts: heOpticalAmplifierGroup.setStatus('current')
heOpticalSwitchGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4))
if mibBuilder.loadTexts: heOpticalSwitchGroup.setStatus('current')
mibBuilder.exportSymbols("SCTE-HMS-HE-OPTICS-MIB", heOpticalReceiverGroup=heOpticalReceiverGroup, PYSNMP_MODULE_ID=heOpticsMib, heOpticsMib=heOpticsMib, heOpticalTransmitterGroup=heOpticalTransmitterGroup, heOpticalAmplifierGroup=heOpticalAmplifierGroup, heOpticalSwitchGroup=heOpticalSwitchGroup)
