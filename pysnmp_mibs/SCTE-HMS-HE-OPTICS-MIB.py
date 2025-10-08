#
# PySNMP MIB module SCTE-HMS-HE-OPTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/scte/SCTE-HMS-HE-OPTICS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
heOptics, = mibBuilder.importSymbols("SCTE-HMS-HEADENDIDENT-MIB", "heOptics")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SCTE-HMS-HE-OPTICS-MIB", heOpticalSwitchGroup=heOpticalSwitchGroup, heOpticalAmplifierGroup=heOpticalAmplifierGroup, heOpticalReceiverGroup=heOpticalReceiverGroup, PYSNMP_MODULE_ID=heOpticsMib, heOpticalTransmitterGroup=heOpticalTransmitterGroup, heOpticsMib=heOpticsMib)
