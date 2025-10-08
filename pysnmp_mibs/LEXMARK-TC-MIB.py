#
# PySNMP MIB module LEXMARK-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/lexmark/LEXMARK-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lexmarkModules, = mibBuilder.importSymbols("LEXMARK-ROOT-MIB", "lexmarkModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lexmarkTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 641, 4, 2))
lexmarkTCMIB.setRevisions(('2017-12-07 16:30', '2017-09-15 15:30', '2017-07-20 18:10', '2011-05-02 15:47', '2009-04-03 00:00',))
if mibBuilder.loadTexts: lexmarkTCMIB.setLastUpdated('201105021547Z')
if mibBuilder.loadTexts: lexmarkTCMIB.setOrganization('Lexmark International, Inc.')
class UnitsTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 21, 22, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("items", 3), ("sides", 4), ("sheets", 5), ("millimeters", 16), ("centimeters", 17), ("meters", 18), ("inches", 19), ("feet", 20), ("grams", 21), ("ounces", 22), ("nanoseconds", 32), ("microseconds", 33), ("milliseconds", 34), ("seconds", 35), ("minutes", 36), ("hours", 37), ("days", 38), ("weeks", 39), ("months", 40), ("years", 41), ("tenthsOfOtherUnits", 42))

class PaperSizeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 32, 33, 34, 35, 36, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 117, 118, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("universal", 3), ("custom", 4), ("letter", 8), ("legal", 9), ("executive", 10), ("folio", 11), ("statement", 12), ("oficio", 13), ("tabloid", 14), ("businessCard", 15), ("idCard", 16), ("card3x5", 17), ("card4x6", 18), ("bookOriginal", 19), ("hagaki", 20), ("card3onehalfx5", 21), ("card4x8", 22), ("card5x7", 23), ("card10x15", 24), ("card10x20", 25), ("card13x18", 26), ("paper12x18", 27), ("sra3", 28), ("envelope7threequarters", 32), ("envelope9", 33), ("envelope10", 34), ("envelopeDL", 35), ("envelopeOther", 36), ("isoA0", 64), ("isoA1", 65), ("isoA2", 66), ("isoA3", 67), ("isoA4", 68), ("isoA5", 69), ("isoA6", 70), ("isoB0", 72), ("isoB1", 73), ("isoB2", 74), ("isoB3", 75), ("isoB4", 76), ("isoB5", 77), ("isoB6", 78), ("isoC0", 80), ("isoC1", 81), ("isoC2", 82), ("isoC3", 83), ("isoC4", 84), ("isoC5", 85), ("isoC6", 86), ("isoEnvelopeA0", 96), ("isoEnvelopeA1", 97), ("isoEnvelopeA2", 98), ("isoEnvelopeA3", 99), ("isoEnvelopeA4", 100), ("isoEnvelopeA5", 101), ("isoEnvelopeA6", 102), ("isoEnvelopeB0", 104), ("isoEnvelopeB1", 105), ("isoEnvelopeB2", 106), ("isoEnvelopeB3", 107), ("isoEnvelopeB4", 108), ("isoEnvelopeB5", 109), ("isoEnvelopeB6", 110), ("isoEnvelopeC0", 112), ("isoEnvelopeC1", 113), ("isoEnvelopeC2", 114), ("isoEnvelopeC3", 115), ("isoEnvelopeC4", 116), ("isoEnvelopeC5", 117), ("isoEnvelopeC6", 118), ("jisB0", 136), ("jisB1", 137), ("jisB2", 138), ("jisB3", 139), ("jisB4", 140), ("jisB5", 141), ("jisB6", 142), ("paper11x17", 143), ("a3Plus", 144), ("bannerLetter", 145), ("bannerA4", 146))

class PaperTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("plain", 3), ("cardstock", 4), ("transparancy", 5), ("recycled", 6), ("labels", 7), ("vinylLabels", 8), ("bond", 9), ("letterhead", 10), ("preprinted", 11), ("colored", 12), ("light", 13), ("heavy", 14), ("roughOrCotton", 15), ("envelope", 16), ("premimuPlain", 17), ("colorLokCertifiedPlain", 18), ("lexmarkPerfectFinishPhoto", 19), ("lexmarkPhoto", 20), ("glossyPhoto", 21), ("mattePhoto", 22), ("inkjetMatteBrochure", 23), ("inkjetGlossyBrochure", 24), ("ironOnTransfer", 25), ("customtype1", 32), ("customtype2", 33), ("customtype3", 34), ("customtype4", 35), ("customtype5", 36), ("customtype6", 37), ("coatedPaper", 38), ("glossy", 39), ("photPaper", 40), ("greetingCard", 41), ("heavyCard", 42), ("roughEnvelop", 43), ("heavyCottonPaper", 44), ("veryHeavyPaper", 45), ("heavyGloss", 46), ("rfidLabels", 47), ("businessCard", 48))

class AdminStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("other", 3), ("up", 4), ("disabled", 5))

class StatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 21, 22, 33, 34, 35, 36, 37, 38, 97, 98, 99, 100, 101, 102))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("ok", 3), ("offline", 4), ("warning", 5), ("broken", 6), ("disabledUnknown", 17), ("disabledOther", 18), ("disabledOk", 19), ("disabledOffline", 20), ("disabledWarning", 21), ("disabledBroken", 22), ("unlicensedUnknown", 33), ("unlicensedOther", 34), ("unlicensedOk", 35), ("unlicensedOffline", 36), ("unlicensedWarning", 37), ("unlicensedBroken", 38), ("licensedUnknown", 97), ("licensedOther", 98), ("licensedOk", 99), ("licensedOffline", 100), ("licensedWarning", 101), ("licensedBroken", 102))

class KeyValueTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("LEXMARK-TC-MIB", lexmarkTCMIB=lexmarkTCMIB, KeyValueTC=KeyValueTC, PYSNMP_MODULE_ID=lexmarkTCMIB, UnitsTC=UnitsTC, PaperSizeTC=PaperSizeTC, PaperTypeTC=PaperTypeTC, StatusTC=StatusTC, AdminStatusTC=AdminStatusTC)
