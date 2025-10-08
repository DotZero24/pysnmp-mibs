#
# PySNMP MIB module ARRIS-MOCA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/arris/ARRIS-MOCA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
arrisProducts, = mibBuilder.importSymbols("ARRIS-MIB", "arrisProducts")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
arrisMoCAMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 21))
arrisMoCAMib.setRevisions(('2014-08-13 00:00', '2013-08-21 00:00', '2013-08-01 00:00', '2013-06-26 00:00', '2013-06-04 00:00', '2012-11-18 00:00', '2012-11-04 00:00', '2012-10-10 00:00',))
if mibBuilder.loadTexts: arrisMoCAMib.setLastUpdated('201408130000Z')
if mibBuilder.loadTexts: arrisMoCAMib.setOrganization('Arris Interactive')
class ArrisMocaTabooChannelMsk(TextualConvention, Unsigned32):
    status = 'current'

class ArrisMocaChannelMsk(TextualConvention, Unsigned32):
    status = 'current'

arrisMoCAConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 21, 1))
arrisMoCAChannelSelMethod = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 21, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("scan", 1), ("manual", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisMoCAChannelSelMethod.setStatus('current')
arrisMoCAChannelMsk = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 21, 1, 2), ArrisMocaChannelMsk().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisMoCAChannelMsk.setStatus('current')
arrisMoCATabooChannel = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 21, 1, 4), ArrisMocaTabooChannelMsk()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisMoCATabooChannel.setStatus('current')
arrisMoCALOF = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 21, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600))).clone(namedValues=NamedValues(("d1", 1150), ("d2", 1200), ("d3", 1250), ("d4", 1300), ("d5", 1350), ("d6", 1400), ("d7", 1450), ("d8", 1500), ("d9", 1550), ("d10", 1600))).clone(1150)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisMoCALOF.setStatus('current')
arrisMoCAPrimchnOff = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 21, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("same", 0), ("above", 1), ("below", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisMoCAPrimchnOff.setStatus('current')
arrisMoCAApplySettings = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 21, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("applySettings-Save", 1), ("applySettings-NoSave", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisMoCAApplySettings.setStatus('current')
mibBuilder.exportSymbols("ARRIS-MOCA-MIB", arrisMoCATabooChannel=arrisMoCATabooChannel, ArrisMocaTabooChannelMsk=ArrisMocaTabooChannelMsk, arrisMoCAMib=arrisMoCAMib, ArrisMocaChannelMsk=ArrisMocaChannelMsk, arrisMoCALOF=arrisMoCALOF, arrisMoCAConfiguration=arrisMoCAConfiguration, arrisMoCAPrimchnOff=arrisMoCAPrimchnOff, PYSNMP_MODULE_ID=arrisMoCAMib, arrisMoCAChannelMsk=arrisMoCAChannelMsk, arrisMoCAApplySettings=arrisMoCAApplySettings, arrisMoCAChannelSelMethod=arrisMoCAChannelSelMethod)
