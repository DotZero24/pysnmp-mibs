#
# PySNMP MIB module ZXPW-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zte/ZXPW-TC-STD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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

mibBuilder.exportSymbols("ZXPW-TC-STD-MIB", PwCwStatusTC=PwCwStatusTC, PYSNMP_MODULE_ID=zxPwTcStdMIB, PwVlanCfg=PwVlanCfg, PwIndexType=PwIndexType, zxPwTcStdMIB=zxPwTcStdMIB, PwAttachmentIdentifierType=PwAttachmentIdentifierType, PwCapabilities=PwCapabilities, PwGroupID=PwGroupID, PwOperStatusTC=PwOperStatusTC, PwStatus=PwStatus, PwFragStatus=PwFragStatus, PwIDType=PwIDType, PwFragSize=PwFragSize)
