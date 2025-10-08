#
# PySNMP MIB module ZXPW-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/ZXPW-TC-STD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zxAnCesMib, = mibBuilder.importSymbols("ZTE-MASTER-MIB", "zxAnCesMib")
zxPwTcStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 4))
if mibBuilder.loadTexts: zxPwTcStdMIB.setLastUpdated('200605150000Z')
if mibBuilder.loadTexts: zxPwTcStdMIB.setOrganization('Zhongxing Telcom Co. Ltd.')
class PwGroupID(TextualConvention, Unsigned32):
    status = 'current'

class PwIDType(TextualConvention, Unsigned32):
    status = 'current'

class PwIndexType(TextualConvention, Unsigned32):
    status = 'current'

class PwVlanCfg(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4097)

class PwOperStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7))

class PwAttachmentIdentifierType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class PwCwStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("waitingForNextMsg", 1), ("sentWrongBitErrorCode", 2), ("rxWithdrawWithWrongBitErrorCode", 3), ("illegalReceivedBit", 4), ("cwPresent", 5), ("cwNotPresent", 6), ("notYetKnown", 7))

class PwCapabilities(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("pwStatusIndication", 0))

class PwStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("pwNotForwarding", 0), ("customerFacingPwRxFault", 1), ("customerFacingPwTxFault", 2), ("psnFacingPwRxFault", 3), ("psnFacingPwTxFault", 4))

class PwFragSize(TextualConvention, Unsigned32):
    status = 'current'

class PwFragStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("noFrag", 0), ("cfgFragGreaterThanPsnMtu", 1), ("cfgFragButRemoteIncapable", 2), ("remoteFragCapable", 3), ("fragEnabled", 4))

mibBuilder.exportSymbols("ZXPW-TC-STD-MIB", PwCapabilities=PwCapabilities, PwFragStatus=PwFragStatus, PwIDType=PwIDType, PwStatus=PwStatus, PwGroupID=PwGroupID, PwAttachmentIdentifierType=PwAttachmentIdentifierType, PwVlanCfg=PwVlanCfg, PwIndexType=PwIndexType, PwOperStatusTC=PwOperStatusTC, PYSNMP_MODULE_ID=zxPwTcStdMIB, PwFragSize=PwFragSize, PwCwStatusTC=PwCwStatusTC, zxPwTcStdMIB=zxPwTcStdMIB)
