#
# PySNMP MIB module IANA-FINISHER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/IANA-FINISHER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianafinisherMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 110))
ianafinisherMIB.setRevisions(('2014-05-22 00:00', '2009-11-03 00:00', '2004-06-02 00:00',))
if mibBuilder.loadTexts: ianafinisherMIB.setLastUpdated('201405220000Z')
if mibBuilder.loadTexts: ianafinisherMIB.setOrganization('IANA')
class FinDeviceTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("stitcher", 3), ("folder", 4), ("binder", 5), ("trimmer", 6), ("dieCutter", 7), ("puncher", 8), ("perforater", 9), ("slitter", 10), ("separationCutter", 11), ("imprinter", 12), ("wrapper", 13), ("bander", 14), ("makeEnvelope", 15), ("stacker", 16), ("sheetRotator", 17), ("inserter", 18))

class FinAttributeTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 31, 40, 50, 80, 81, 82, 83, 100, 130, 160, 161, 162))
    namedValues = NamedValues(("other", 1), ("deviceName", 3), ("deviceVendorName", 4), ("deviceModel", 5), ("deviceVersion", 6), ("deviceSerialNumber", 7), ("maximumSheets", 8), ("finProcessOffsetUnits", 9), ("finReferenceEdge", 10), ("finAxisOffset", 11), ("finJogEdge", 12), ("finHeadLocation", 13), ("finOperationRestrictions", 14), ("finNumberOfPositions", 15), ("namedConfiguration", 16), ("finMediaTypeRestriction", 17), ("finPrinterInputTraySupported", 18), ("finPreviousFinishingOperation", 19), ("finNextFinishingOperation", 20), ("stitchingType", 30), ("stitchingDirection", 31), ("foldingType", 40), ("bindingType", 50), ("punchHoleType", 80), ("punchHoleSizeLongDim", 81), ("punchHoleSizeShortDim", 82), ("punchPattern", 83), ("slittingType", 100), ("wrappingType", 130), ("stackOutputType", 160), ("stackOffset", 161), ("stackRotation", 162))

class FinEdgeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4, 5, 6))
    namedValues = NamedValues(("topEdge", 3), ("bottomEdge", 4), ("leftEdge", 5), ("rightEdge", 6))

class FinStitchingTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("stapleTopLeft", 4), ("stapleBottomLeft", 5), ("stapleTopRight", 6), ("stapleBottomRight", 7), ("saddleStitch", 8), ("edgeStitch", 9), ("stapleDual", 10))

class FinStitchingDirTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4))
    namedValues = NamedValues(("unknown", 2), ("topDown", 3), ("bottomUp", 4))

class FinStitchingAngleTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 2), ("horizontal", 3), ("vertical", 4), ("slanted", 5))

class FinFoldingTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("zFold", 3), ("halfFold", 4), ("letterFold", 5))

class FinBindingTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("tape", 4), ("plastic", 5), ("velo", 6), ("perfect", 7), ("spiral", 8), ("adhesive", 9), ("comb", 10), ("padding", 11), ("plasticMultiRing", 12))

class FinPunchHoleTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("round", 3), ("oblong", 4), ("square", 5), ("rectangular", 6), ("star", 7))

class FinPunchPatternTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("twoHoleUSTop", 4), ("threeHoleUS", 5), ("twoHoleDIN", 6), ("fourHoleDIN", 7), ("twentyTwoHoleUS", 8), ("nineteenHoleUS", 9), ("twoHoleMetric", 10), ("swedish4Hole", 11), ("twoHoleUSSide", 12), ("fiveHoleUS", 13), ("sevenHoleUS", 14), ("mixed7H4S", 15), ("norweg6Hole", 16), ("metric26Hole", 17), ("metric30Hole", 18))

class FinSlittingTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("slitAndSeparate", 4), ("slitAndMerge", 5))

class FinWrappingTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("shrinkWrap", 4), ("paperWrap", 5))

class FinStackOutputTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("straight", 4), ("offset", 5), ("crissCross", 6))

mibBuilder.exportSymbols("IANA-FINISHER-MIB", FinFoldingTypeTC=FinFoldingTypeTC, FinEdgeTC=FinEdgeTC, FinBindingTypeTC=FinBindingTypeTC, FinStitchingAngleTypeTC=FinStitchingAngleTypeTC, FinWrappingTypeTC=FinWrappingTypeTC, ianafinisherMIB=ianafinisherMIB, FinStackOutputTypeTC=FinStackOutputTypeTC, FinDeviceTypeTC=FinDeviceTypeTC, PYSNMP_MODULE_ID=ianafinisherMIB, FinPunchPatternTC=FinPunchPatternTC, FinPunchHoleTypeTC=FinPunchHoleTypeTC, FinSlittingTypeTC=FinSlittingTypeTC, FinAttributeTypeTC=FinAttributeTypeTC, FinStitchingDirTypeTC=FinStitchingDirTypeTC, FinStitchingTypeTC=FinStitchingTypeTC)
