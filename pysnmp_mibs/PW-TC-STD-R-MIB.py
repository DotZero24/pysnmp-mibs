#
# PySNMP MIB module PW-TC-STD-R-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rad/PW-TC-STD-R-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:10:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
transmission, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "transmission", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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

mibBuilder.exportSymbols("PW-TC-STD-R-MIB", PwIndexOrZeroType=PwIndexOrZeroType, PwFragStatus=PwFragStatus, PYSNMP_MODULE_ID=pwTcStdMIBR, PwIDType=PwIDType, PwStatus=PwStatus, PwGroupID=PwGroupID, PwAttachmentIdentifierType=PwAttachmentIdentifierType, PwVlanCfg=PwVlanCfg, pwTcStdMIBR=pwTcStdMIBR, PwIndexType=PwIndexType, radExperimental=radExperimental, PwOperStatusTC=PwOperStatusTC, PwFragSize=PwFragSize, PwCwStatusTC=PwCwStatusTC, PwCfgIndexOrzero=PwCfgIndexOrzero)
