#
# PySNMP MIB module PW-TC-STD-R-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rad/PW-TC-STD-R-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:42:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, transmission, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "transmission", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pwTcStdMIBR = ModuleIdentity((1, 3, 6, 1, 4, 1, 164, 20, 11))
pwTcStdMIBR.setRevisions(('2007-02-04 12:00',))
if mibBuilder.loadTexts: pwTcStdMIBR.setLastUpdated('200702041200Z')
if mibBuilder.loadTexts: pwTcStdMIBR.setOrganization('Pseudo Wire Edge-to-Edge Emulation (PWE3) Working Group')
radExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 164, 20))
class PwGroupID(TextualConvention, Unsigned32):
    status = 'current'

class PwIDType(TextualConvention, Unsigned32):
    status = 'current'

class PwIndexType(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class PwIndexOrZeroType(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class PwVlanCfg(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4097)

class PwOperStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("dormant", 4), ("notPresent", 5), ("lowerLayerDown", 6))

class PwAttachmentIdentifierType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class PwCwStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("waitingForNextMsg", 1), ("sentWrongBitErrorCode", 2), ("rxWithdrawWithWrongBitErrorCode", 3), ("illegalReceivedBit", 4), ("cwPresent", 5), ("cwNotPresent", 6), ("notYetKnown", 7))

class PwStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("pwNotForwarding", 0), ("servicePwRxFault", 1), ("servicePwTxFault", 2), ("psnPwRxFault", 3), ("psnPwTxFault", 4))

class PwFragSize(TextualConvention, Unsigned32):
    status = 'current'

class PwFragStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("noFrag", 0), ("cfgFragGreaterThanPsnMtu", 1), ("cfgFragButRemoteIncapable", 2), ("remoteFragCapable", 3), ("fragEnabled", 4))

class PwCfgIndexOrzero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

mibBuilder.exportSymbols("PW-TC-STD-R-MIB", PwCfgIndexOrzero=PwCfgIndexOrzero, PwCwStatusTC=PwCwStatusTC, PwVlanCfg=PwVlanCfg, radExperimental=radExperimental, PwIndexType=PwIndexType, PwAttachmentIdentifierType=PwAttachmentIdentifierType, PwGroupID=PwGroupID, pwTcStdMIBR=pwTcStdMIBR, PwIndexOrZeroType=PwIndexOrZeroType, PwOperStatusTC=PwOperStatusTC, PwStatus=PwStatus, PYSNMP_MODULE_ID=pwTcStdMIBR, PwFragStatus=PwFragStatus, PwIDType=PwIDType, PwFragSize=PwFragSize)
