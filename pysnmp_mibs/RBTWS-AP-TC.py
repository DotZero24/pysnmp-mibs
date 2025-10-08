#
# PySNMP MIB module RBTWS-AP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cabletron/RBTWS-AP-TC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rbtwsMibs, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbtwsApTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 3))
rbtwsApTc.setRevisions(('2008-05-07 00:41', '2008-02-14 00:32', '2007-12-03 00:30', '2007-07-06 00:23', '2007-07-05 00:22', '2006-07-10 00:15', '2006-03-30 00:14',))
if mibBuilder.loadTexts: rbtwsApTc.setLastUpdated('200805081148Z')
if mibBuilder.loadTexts: rbtwsApTc.setOrganization('Enterasys Networks')
class RbtwsAccessType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ap", 1), ("dap", 2), ("wired", 3))

class RbtwsApAttachType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("directAttach", 1), ("networkAttach", 2))

class RbtwsApPortOrDapNum(TextualConvention, Unsigned32):
    status = 'obsolete'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1000)

class RbtwsApNum(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9999)

class RbtwsApState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("cleared", 1), ("init", 2), ("bootStarted", 3), ("imageDownloaded", 4), ("connectFailed", 5), ("configuring", 6), ("configured", 7))

class RbtwsApTransition(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("clear", 1), ("timeout", 2), ("reset", 3), ("bootSuccess", 4), ("startConfiguring", 5), ("connectFail", 6))

class RbtwsApFailDetail(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 11, 12, 91, 99))
    namedValues = NamedValues(("secureHandshakeFailure", 2), ("fingerprintRequired", 3), ("fingerprintMismatch", 4), ("portLinkUp", 11), ("portLinkDown", 12), ("normalTransition", 91), ("failUnknown", 99))

class RbtwsApConnectSecurityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("secure", 1), ("insecure", 2), ("auto", 3))

class RbtwsApServiceAvailability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fullService", 1), ("noService", 2), ("degradedService", 3))

class RbtwsApBias(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("high", 1), ("low", 2))

class RbtwsApSerialNum(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class RbtwsApFingerprint(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
class RbtwsRadioNum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("radio-1", 1), ("radio-2", 2), ("not-applicable", 3))

class RbtwsPowerLevel(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 18)

class RbtwsRadioPowerChangeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("dup-pkts-threshold-exceed", 1), ("retransmit-threshold-exceed", 2), ("clients-optimal-performance-reached", 3), ("def-power-threshold-exceed", 4))

class RbtwsChannelChangeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("util-index", 1), ("rexmit-pkt-offset", 2), ("noise-offset", 3), ("noise", 4), ("utilization", 5), ("phy-error-offset", 6), ("crc-errors-offset", 7), ("radar-detected", 8))

class RbtwsChannelNum(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

class RbtwsRadioEnable(TextualConvention, Integer32):
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class RbtwsRadioMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("sentry", 3))

class RbtwsRadioConfigState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("configInit", 1), ("configFail", 2), ("configOk", 3))

class RbtwsRadioRate(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 540), )
class RbtwsRadioType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("typeUnknown", 1), ("typeA", 2), ("typeB", 3), ("typeG", 4), ("typeNA", 5), ("typeNG", 6))

class RbtwsRssi(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-100, 0)

class RbtwsApWasOperational(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oper", 1), ("nonOper", 2))

class RbtwsRadioChannelWidth(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("channelWidth20MHz", 1), ("channelWidth40MHz", 2))

class RbtwsRadioMimoState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("mimoOther", 1), ("mimo1x1", 2), ("mimo2x3", 3), ("mimo3x3", 4))

class RbtwsCryptoType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("clear", 2), ("wep", 3), ("wep40", 4), ("wep104", 5), ("tkip", 6), ("aesCcmp", 7))

mibBuilder.exportSymbols("RBTWS-AP-TC", RbtwsApTransition=RbtwsApTransition, RbtwsAccessType=RbtwsAccessType, RbtwsApPortOrDapNum=RbtwsApPortOrDapNum, RbtwsRadioNum=RbtwsRadioNum, RbtwsApWasOperational=RbtwsApWasOperational, RbtwsApFingerprint=RbtwsApFingerprint, RbtwsApState=RbtwsApState, RbtwsRssi=RbtwsRssi, RbtwsRadioMimoState=RbtwsRadioMimoState, RbtwsApSerialNum=RbtwsApSerialNum, RbtwsApFailDetail=RbtwsApFailDetail, RbtwsChannelChangeType=RbtwsChannelChangeType, RbtwsCryptoType=RbtwsCryptoType, RbtwsRadioMode=RbtwsRadioMode, RbtwsChannelNum=RbtwsChannelNum, RbtwsRadioRate=RbtwsRadioRate, RbtwsRadioType=RbtwsRadioType, RbtwsApServiceAvailability=RbtwsApServiceAvailability, RbtwsApAttachType=RbtwsApAttachType, RbtwsPowerLevel=RbtwsPowerLevel, RbtwsRadioConfigState=RbtwsRadioConfigState, RbtwsApBias=RbtwsApBias, RbtwsApConnectSecurityType=RbtwsApConnectSecurityType, rbtwsApTc=rbtwsApTc, RbtwsRadioPowerChangeType=RbtwsRadioPowerChangeType, PYSNMP_MODULE_ID=rbtwsApTc, RbtwsApNum=RbtwsApNum, RbtwsRadioChannelWidth=RbtwsRadioChannelWidth, RbtwsRadioEnable=RbtwsRadioEnable)
