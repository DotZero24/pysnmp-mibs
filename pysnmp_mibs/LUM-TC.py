#
# PySNMP MIB module LUM-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/LUM-TC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lumModules, = mibBuilder.importSymbols("LUM-REG", "lumModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lumTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 2))
lumTcModule.setRevisions(('2018-12-21 00:00', '2018-06-29 00:00', '2018-04-16 00:00', '2017-06-15 00:00', '2016-11-30 00:00', '2015-11-30 00:00', '2014-09-30 00:00', '2014-05-16 00:00', '2013-11-15 00:00', '2013-05-01 00:00', '2012-12-20 00:00', '2011-12-20 00:00', '2011-05-11 00:00', '2005-07-07 00:00', '2002-04-10 00:00', '2002-03-05 00:00', '2001-12-03 00:00', '2001-10-23 00:00', '2001-10-11 00:00', '2001-09-04 00:00', '2001-08-14 00:00', '2001-08-09 00:00', '2001-03-12 00:00',))
if mibBuilder.loadTexts: lumTcModule.setLastUpdated('201812210000Z')
if mibBuilder.loadTexts: lumTcModule.setOrganization('Infinera Corporation')
class MgmtNameString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class FaultStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("alarm", 2))

class SubrackNumber(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class SlotNumber(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 22)

class PortNumber(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 116)

class SignalType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("uni", 1), ("biDi", 2))

class PortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rx", 1), ("tx", 2), ("biDi", 3))

class LambdaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("fixed", 1), ("range", 2), ("transparent", 3), ("interleavedOdd", 4), ("interleavedEven", 5), ("interleaved50GHzOdd", 6), ("interleaved50GhzEven", 7))

class LambdaFrequency(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 130, 150, 850, 1270, 1290, 1310, 1330, 1350, 1370, 1390, 1410, 1430, 1450, 1470, 1490, 1510, 1530, 1550, 1570, 1590, 1610, 18710, 18730, 18750, 18770, 18790, 18810, 18830, 18850, 18870, 18890, 18910, 18930, 18950, 18970, 18990, 19010, 19030, 19050, 19070, 19090, 19135, 19140, 19145, 19150, 19155, 19160, 19165, 19170, 19175, 19180, 19185, 19190, 19195, 19200, 19205, 19210, 19215, 19220, 19225, 19230, 19235, 19240, 19245, 19250, 19255, 19260, 19265, 19270, 19275, 19280, 19285, 19290, 19295, 19300, 19305, 19310, 19315, 19320, 19325, 19330, 19335, 19340, 19345, 19350, 19355, 19360, 19365, 19370, 19375, 19380, 19385, 19390, 19395, 19400, 19405, 19410, 19415, 19420, 19425, 19430, 19435, 19440, 19445, 19450, 19455, 19460, 19465, 19470, 19475, 19480, 19485, 19490, 19495, 19500, 19505, 19510, 19515, 19520, 19525, 19530, 19535, 19540, 19545, 19550, 19555, 19560, 19565, 19570, 19575, 19580, 19585, 19590, 19595, 19600, 19605, 19610))
    namedValues = NamedValues(("undefined", 0), ("iWdmPonFrequency", 1), ("otclg", 2), ("b1300", 130), ("b1500", 150), ("w850", 850), ("w1270", 1270), ("w1290", 1290), ("w1310", 1310), ("w1330", 1330), ("w1350", 1350), ("w1370", 1370), ("w1390", 1390), ("w1410", 1410), ("w1430", 1430), ("w1450", 1450), ("w1470", 1470), ("w1490", 1490), ("w1510", 1510), ("w1530", 1530), ("w1550", 1550), ("w1570", 1570), ("w1590", 1590), ("w1610", 1610), ("ch871", 18710), ("ch873", 18730), ("ch875", 18750), ("ch877", 18770), ("ch879", 18790), ("ch881", 18810), ("ch883", 18830), ("ch885", 18850), ("ch887", 18870), ("ch889", 18890), ("ch891", 18910), ("ch893", 18930), ("ch895", 18950), ("ch897", 18970), ("ch899", 18990), ("ch901", 19010), ("ch903", 19030), ("ch905", 19050), ("ch907", 19070), ("ch909", 19090), ("ch9135", 19135), ("ch914", 19140), ("ch9145", 19145), ("ch915", 19150), ("ch9155", 19155), ("ch916", 19160), ("ch9165", 19165), ("ch917", 19170), ("ch9175", 19175), ("ch918", 19180), ("ch9185", 19185), ("ch919", 19190), ("ch9195", 19195), ("ch920", 19200), ("ch9205", 19205), ("ch921", 19210), ("ch9215", 19215), ("ch922", 19220), ("ch9225", 19225), ("ch923", 19230), ("ch9235", 19235), ("ch924", 19240), ("ch9245", 19245), ("ch925", 19250), ("ch9255", 19255), ("ch926", 19260), ("ch9265", 19265), ("ch927", 19270), ("ch9275", 19275), ("ch928", 19280), ("ch9285", 19285), ("ch929", 19290), ("ch9295", 19295), ("ch930", 19300), ("ch9305", 19305), ("ch931", 19310), ("ch9315", 19315), ("ch932", 19320), ("ch9325", 19325), ("ch933", 19330), ("ch9335", 19335), ("ch934", 19340), ("ch9345", 19345), ("ch935", 19350), ("ch9355", 19355), ("ch936", 19360), ("ch9365", 19365), ("ch937", 19370), ("ch9375", 19375), ("ch938", 19380), ("ch9385", 19385), ("ch939", 19390), ("ch9395", 19395), ("ch940", 19400), ("ch9405", 19405), ("ch941", 19410), ("ch9415", 19415), ("ch942", 19420), ("ch9425", 19425), ("ch943", 19430), ("ch9435", 19435), ("ch944", 19440), ("ch9445", 19445), ("ch945", 19450), ("ch9455", 19455), ("ch946", 19460), ("ch9465", 19465), ("ch947", 19470), ("ch9475", 19475), ("ch948", 19480), ("ch9485", 19485), ("ch949", 19490), ("ch9495", 19495), ("ch950", 19500), ("ch9505", 19505), ("ch951", 19510), ("ch9515", 19515), ("ch952", 19520), ("ch9525", 19525), ("ch953", 19530), ("ch9535", 19535), ("ch954", 19540), ("ch9545", 19545), ("ch955", 19550), ("ch9555", 19555), ("ch956", 19560), ("ch9565", 19565), ("ch957", 19570), ("ch9575", 19575), ("ch958", 19580), ("ch9585", 19585), ("ch959", 19590), ("ch9595", 19595), ("ch960", 19600), ("ch9605", 19605), ("ch961", 19610))

class BoardOrInterfaceAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("down", 1), ("service", 2), ("up", 3))

class BoardOrInterfaceOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("notPresent", 1), ("down", 2), ("up", 3))

class CommandString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'

class SignalFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 2147483647))
    namedValues = NamedValues(("other", 1), ("stm1", 2), ("stm4", 3), ("stm16", 4), ("gbE", 5), ("stm64", 6), ("fc1Gb", 7), ("fc2Gb", 8), ("wan10GbE", 9), ("unused", 10), ("lan10GbE", 11), ("escon", 12), ("esconLL", 13), ("dvb270", 14), ("oc3", 15), ("oc12", 16), ("oc48", 17), ("oc192", 18), ("hdtv1485", 19), ("ethernet", 20), ("fastEthernet", 21), ("lan10GbEFec", 22), ("wan10GbEStm64Fec", 23), ("fc4Gb", 24), ("etr", 25), ("auto", 26), ("down", 27), ("stm1Oc3", 28), ("stm4Oc12", 29), ("stm16Oc48", 30), ("stm64Oc192", 31), ("gbe9Line", 32), ("ddgbeLine", 34), ("gbEorTrm5500", 35), ("fc8Gb", 36), ("otu2", 37), ("otu2e", 38), ("e1", 39), ("t1", 40), ("mbh2Gb5", 41), ("syncE", 42), ("line4G", 43), ("mbh4Gbps", 44), ("fecLan10GbE1A", 45), ("fecLan10GbE1B", 46), ("sdi3G", 47), ("iWdm4G", 48), ("sdSdi270", 49), ("hdtvNTSC", 50), ("oc768", 51), ("stm256", 52), ("lan40GbE", 53), ("wan40GbE", 54), ("sfStm256Oc768", 55), ("iwdm40Gb", 56), ("otu4", 57), ("lan100GbE", 58), ("transpLan10GbE", 59), ("cpri1", 60), ("cpri2", 61), ("cpri3", 62), ("cpri4", 63), ("cpri5", 64), ("cpri6", 65), ("cpri7", 66), ("fc10Gb", 67), ("fc16Gb", 68), ("cpri8", 69), ("obsai1x", 70), ("obsai2x", 71), ("obsai4x", 72), ("obsai8x", 73), ("otu1", 74), ("iwdm11G", 75), ("rw100G", 76), ("rw200G", 77), ("otu4SdFec", 78), ("otuj1", 79), ("otuj2", 80), ("notApplicable", 2147483647))

class TrxMedia(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("optical", 1), ("tp1000BaseT", 2), ("tp100BaseT", 3), ("tp10BaseT", 4), ("electrical", 5))

class OtnMonitorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("sm", 0), ("pm", 1), ("tcm", 2))

class OtnMonitorConfig(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("terminated", 0), ("transparent", 1))

class OtnTIMDetMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("sapi", 0), ("dapi", 1), ("both", 2))

class ObjectProperty(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class PmReset(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("reset", 2))

class EnableDisable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class SyncSourceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("normal", 1), ("failed", 2), ("waitToRestore", 3))

class SyncSourceMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1), ("lockedOut", 2))

class AdminStatusWithNA(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 2147483647))
    namedValues = NamedValues(("down", 1), ("service", 2), ("up", 3), ("notApplicable", 2147483647))

class OperStatusWithNA(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 2147483647))
    namedValues = NamedValues(("notPresent", 1), ("down", 2), ("up", 3), ("notApplicable", 2147483647))

class SignalStatusWithNA(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 2147483647))
    namedValues = NamedValues(("down", 1), ("degraded", 2), ("up", 3), ("notApplicable", 2147483647))

class Unsigned32WithNA(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 4294967292), ValueRangeConstraint(4294967293, 4294967293), ValueRangeConstraint(4294967294, 4294967294), )
class EnabledDisabledWithNA(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 2147483647))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2), ("notApplicable", 2147483647))

class Layer(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 2147483646), ValueRangeConstraint(2147483647, 2147483647), )
class Time7200min(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 7200), ValueRangeConstraint(2147483647, 2147483647), )
class Time7200minNo0(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 7200), ValueRangeConstraint(2147483647, 2147483647), )
class Integer32WithNA(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 2147483645), ValueRangeConstraint(2147483646, 2147483646), ValueRangeConstraint(2147483647, 2147483647), )
class Activated(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 2147483647))
    namedValues = NamedValues(("activated", 1), ("deactivated", 2), ("notApplicable", 2147483647))

class ResetWithNA(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 2147483647))
    namedValues = NamedValues(("reset", 1), ("normal", 2), ("notApplicable", 2147483647))

class FaultStatusWithNA(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 2147483647))
    namedValues = NamedValues(("ok", 1), ("alarm", 2), ("notApplicable", 2147483647))

class MgmtNameStringWithNA(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class DisplayStringWithNA(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SignalStructure(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 2147483647))
    namedValues = NamedValues(("phyTrxOptOtsOptOchOtnOtuOtnOduOtnmonSmOtnmonPm", 1), ("phyTrxOptOtsOptOchSdhRsSdhMs", 2), ("phyTrxOptOtsOptOchSonetSectionSonetLine", 3), ("phyTrxOptOtsOptOchEthPhys", 4), ("notApplicable", 2147483647))

class Signed32WithNA(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2147483648, 2147483645), ValueRangeConstraint(2147483646, 2147483646), ValueRangeConstraint(2147483647, 2147483647), )
class LaserMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 2147483647))
    namedValues = NamedValues(("forcedOn", 1), ("als", 2), ("notApplicable", 2147483647))

class OnOff(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 2147483646, 2147483647))
    namedValues = NamedValues(("off", 1), ("on", 2), ("notAvailable", 2147483646), ("notApplicable", 2147483647))

class LaneFrequency(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 130, 150, 850, 1270, 1290, 1297, 1301, 1305, 1309, 1310, 1330, 1350, 1370, 1390, 1410, 1430, 1450, 1470, 1490, 1510, 1523, 1530, 1531, 1539, 1547, 1550, 1555, 1563, 1570, 1571, 1579, 1587, 1590, 1595, 1610, 18710, 18730, 18750, 18770, 18790, 18810, 18830, 18850, 18870, 18890, 18910, 18930, 18950, 18970, 18990, 19010, 19030, 19050, 19070, 19090, 19185, 19190, 19195, 19200, 19205, 19210, 19215, 19220, 19225, 19230, 19235, 19240, 19245, 19250, 19255, 19260, 19265, 19270, 19275, 19280, 19285, 19290, 19295, 19300, 19305, 19310, 19315, 19320, 19325, 19330, 19335, 19340, 19345, 19350, 19355, 19360, 19365, 19370, 19375, 19380, 19385, 19390, 19395, 19400, 19405, 19410, 19415, 19420, 19425, 19430, 19435, 19440, 19445, 19450, 19455, 19460, 19465, 19470, 19475, 19480, 19485, 19490, 19495, 19500, 19505, 19510, 19515, 19520, 19525, 19530, 19535, 19540, 19545, 19550, 19555, 19560, 19565, 19570, 19575, 19580, 19585, 19590, 19595, 19600, 19605, 19610, 2147483646, 2147483647))
    namedValues = NamedValues(("undefined", 0), ("b1300", 130), ("b1500", 150), ("w850", 850), ("w1270", 1270), ("w1290", 1290), ("w1297", 1297), ("w1301", 1301), ("w1305", 1305), ("w1309", 1309), ("w1310", 1310), ("w1330", 1330), ("w1350", 1350), ("w1370", 1370), ("w1390", 1390), ("w1410", 1410), ("w1430", 1430), ("w1450", 1450), ("w1470", 1470), ("w1490", 1490), ("w1510", 1510), ("w1523", 1523), ("w1530", 1530), ("w1531", 1531), ("w1539", 1539), ("w1547", 1547), ("w1550", 1550), ("w1555", 1555), ("w1563", 1563), ("w1570", 1570), ("w1571", 1571), ("w1579", 1579), ("w1587", 1587), ("w1590", 1590), ("w1595", 1595), ("w1610", 1610), ("ch871", 18710), ("ch873", 18730), ("ch875", 18750), ("ch877", 18770), ("ch879", 18790), ("ch881", 18810), ("ch883", 18830), ("ch885", 18850), ("ch887", 18870), ("ch889", 18890), ("ch891", 18910), ("ch893", 18930), ("ch895", 18950), ("ch897", 18970), ("ch899", 18990), ("ch901", 19010), ("ch903", 19030), ("ch905", 19050), ("ch907", 19070), ("ch909", 19090), ("ch9185", 19185), ("ch919", 19190), ("ch9195", 19195), ("ch920", 19200), ("ch9205", 19205), ("ch921", 19210), ("ch9215", 19215), ("ch922", 19220), ("ch9225", 19225), ("ch923", 19230), ("ch9235", 19235), ("ch924", 19240), ("ch9245", 19245), ("ch925", 19250), ("ch9255", 19255), ("ch926", 19260), ("ch9265", 19265), ("ch927", 19270), ("ch9275", 19275), ("ch928", 19280), ("ch9285", 19285), ("ch929", 19290), ("ch9295", 19295), ("ch930", 19300), ("ch9305", 19305), ("ch931", 19310), ("ch9315", 19315), ("ch932", 19320), ("ch9325", 19325), ("ch933", 19330), ("ch9335", 19335), ("ch934", 19340), ("ch9345", 19345), ("ch935", 19350), ("ch9355", 19355), ("ch936", 19360), ("ch9365", 19365), ("ch937", 19370), ("ch9375", 19375), ("ch938", 19380), ("ch9385", 19385), ("ch939", 19390), ("ch9395", 19395), ("ch940", 19400), ("ch9405", 19405), ("ch941", 19410), ("ch9415", 19415), ("ch942", 19420), ("ch9425", 19425), ("ch943", 19430), ("ch9435", 19435), ("ch944", 19440), ("ch9445", 19445), ("ch945", 19450), ("ch9455", 19455), ("ch946", 19460), ("ch9465", 19465), ("ch947", 19470), ("ch9475", 19475), ("ch948", 19480), ("ch9485", 19485), ("ch949", 19490), ("ch9495", 19495), ("ch950", 19500), ("ch9505", 19505), ("ch951", 19510), ("ch9515", 19515), ("ch952", 19520), ("ch9525", 19525), ("ch953", 19530), ("ch9535", 19535), ("ch954", 19540), ("ch9545", 19545), ("ch955", 19550), ("ch9555", 19555), ("ch956", 19560), ("ch9565", 19565), ("ch957", 19570), ("ch9575", 19575), ("ch958", 19580), ("ch9585", 19585), ("ch959", 19590), ("ch9595", 19595), ("ch960", 19600), ("ch9605", 19605), ("ch961", 19610), ("notAvailable", 2147483646), ("notApplicable", 2147483647))

class Frequency(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 130, 150, 850, 1270, 1290, 1310, 1330, 1350, 1370, 1390, 1410, 1430, 1450, 1470, 1490, 1510, 1530, 1550, 1570, 1590, 1610, 18710, 18730, 18750, 18770, 18790, 18810, 18830, 18850, 18870, 18890, 18910, 18930, 18950, 18970, 18990, 19010, 19030, 19050, 19070, 19090, 19135, 19140, 19145, 19150, 19155, 19160, 19165, 19170, 19175, 19180, 19185, 19190, 19195, 19200, 19205, 19210, 19215, 19220, 19225, 19230, 19235, 19240, 19245, 19250, 19255, 19260, 19265, 19270, 19275, 19280, 19285, 19290, 19295, 19300, 19305, 19310, 19315, 19320, 19325, 19330, 19335, 19340, 19345, 19350, 19355, 19360, 19365, 19370, 19375, 19380, 19385, 19390, 19395, 19400, 19405, 19410, 19415, 19420, 19425, 19430, 19435, 19440, 19445, 19450, 19455, 19460, 19465, 19470, 19475, 19480, 19485, 19490, 19495, 19500, 19505, 19510, 19515, 19520, 19525, 19530, 19535, 19540, 19545, 19550, 19555, 19560, 19565, 19570, 19575, 19580, 19585, 19590, 19595, 19600, 19605, 19610, 2147483646, 2147483647))
    namedValues = NamedValues(("undefined", 0), ("b1300", 130), ("b1500", 150), ("w850", 850), ("w1270", 1270), ("w1290", 1290), ("w1310", 1310), ("w1330", 1330), ("w1350", 1350), ("w1370", 1370), ("w1390", 1390), ("w1410", 1410), ("w1430", 1430), ("w1450", 1450), ("w1470", 1470), ("w1490", 1490), ("w1510", 1510), ("w1530", 1530), ("w1550", 1550), ("w1570", 1570), ("w1590", 1590), ("w1610", 1610), ("ch871", 18710), ("ch873", 18730), ("ch875", 18750), ("ch877", 18770), ("ch879", 18790), ("ch881", 18810), ("ch883", 18830), ("ch885", 18850), ("ch887", 18870), ("ch889", 18890), ("ch891", 18910), ("ch893", 18930), ("ch895", 18950), ("ch897", 18970), ("ch899", 18990), ("ch901", 19010), ("ch903", 19030), ("ch905", 19050), ("ch907", 19070), ("ch909", 19090), ("ch9135", 19135), ("ch914", 19140), ("ch9145", 19145), ("ch915", 19150), ("ch9155", 19155), ("ch916", 19160), ("ch9165", 19165), ("ch917", 19170), ("ch9175", 19175), ("ch918", 19180), ("ch9185", 19185), ("ch919", 19190), ("ch9195", 19195), ("ch920", 19200), ("ch9205", 19205), ("ch921", 19210), ("ch9215", 19215), ("ch922", 19220), ("ch9225", 19225), ("ch923", 19230), ("ch9235", 19235), ("ch924", 19240), ("ch9245", 19245), ("ch925", 19250), ("ch9255", 19255), ("ch926", 19260), ("ch9265", 19265), ("ch927", 19270), ("ch9275", 19275), ("ch928", 19280), ("ch9285", 19285), ("ch929", 19290), ("ch9295", 19295), ("ch930", 19300), ("ch9305", 19305), ("ch931", 19310), ("ch9315", 19315), ("ch932", 19320), ("ch9325", 19325), ("ch933", 19330), ("ch9335", 19335), ("ch934", 19340), ("ch9345", 19345), ("ch935", 19350), ("ch9355", 19355), ("ch936", 19360), ("ch9365", 19365), ("ch937", 19370), ("ch9375", 19375), ("ch938", 19380), ("ch9385", 19385), ("ch939", 19390), ("ch9395", 19395), ("ch940", 19400), ("ch9405", 19405), ("ch941", 19410), ("ch9415", 19415), ("ch942", 19420), ("ch9425", 19425), ("ch943", 19430), ("ch9435", 19435), ("ch944", 19440), ("ch9445", 19445), ("ch945", 19450), ("ch9455", 19455), ("ch946", 19460), ("ch9465", 19465), ("ch947", 19470), ("ch9475", 19475), ("ch948", 19480), ("ch9485", 19485), ("ch949", 19490), ("ch9495", 19495), ("ch950", 19500), ("ch9505", 19505), ("ch951", 19510), ("ch9515", 19515), ("ch952", 19520), ("ch9525", 19525), ("ch953", 19530), ("ch9535", 19535), ("ch954", 19540), ("ch9545", 19545), ("ch955", 19550), ("ch9555", 19555), ("ch956", 19560), ("ch9565", 19565), ("ch957", 19570), ("ch9575", 19575), ("ch958", 19580), ("ch9585", 19585), ("ch959", 19590), ("ch9595", 19595), ("ch960", 19600), ("ch9605", 19605), ("ch961", 19610), ("notAvailable", 2147483646), ("notApplicable", 2147483647))

class FrequencyOnlyNotApplicable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 130, 150, 850, 1270, 1290, 1310, 1330, 1350, 1370, 1390, 1410, 1430, 1450, 1470, 1490, 1510, 1530, 1550, 1570, 1590, 1610, 18710, 18730, 18750, 18770, 18790, 18810, 18830, 18850, 18870, 18890, 18910, 18930, 18950, 18970, 18990, 19010, 19030, 19050, 19070, 19090, 19135, 19140, 19145, 19150, 19155, 19160, 19165, 19170, 19175, 19180, 19185, 19190, 19195, 19200, 19205, 19210, 19215, 19220, 19225, 19230, 19235, 19240, 19245, 19250, 19255, 19260, 19265, 19270, 19275, 19280, 19285, 19290, 19295, 19300, 19305, 19310, 19315, 19320, 19325, 19330, 19335, 19340, 19345, 19350, 19355, 19360, 19365, 19370, 19375, 19380, 19385, 19390, 19395, 19400, 19405, 19410, 19415, 19420, 19425, 19430, 19435, 19440, 19445, 19450, 19455, 19460, 19465, 19470, 19475, 19480, 19485, 19490, 19495, 19500, 19505, 19510, 19515, 19520, 19525, 19530, 19535, 19540, 19545, 19550, 19555, 19560, 19565, 19570, 19575, 19580, 19585, 19590, 19595, 19600, 19605, 19610, 2147483647))
    namedValues = NamedValues(("undefined", 0), ("b1300", 130), ("b1500", 150), ("w850", 850), ("w1270", 1270), ("w1290", 1290), ("w1310", 1310), ("w1330", 1330), ("w1350", 1350), ("w1370", 1370), ("w1390", 1390), ("w1410", 1410), ("w1430", 1430), ("w1450", 1450), ("w1470", 1470), ("w1490", 1490), ("w1510", 1510), ("w1530", 1530), ("w1550", 1550), ("w1570", 1570), ("w1590", 1590), ("w1610", 1610), ("ch871", 18710), ("ch873", 18730), ("ch875", 18750), ("ch877", 18770), ("ch879", 18790), ("ch881", 18810), ("ch883", 18830), ("ch885", 18850), ("ch887", 18870), ("ch889", 18890), ("ch891", 18910), ("ch893", 18930), ("ch895", 18950), ("ch897", 18970), ("ch899", 18990), ("ch901", 19010), ("ch903", 19030), ("ch905", 19050), ("ch907", 19070), ("ch909", 19090), ("ch9135", 19135), ("ch914", 19140), ("ch9145", 19145), ("ch915", 19150), ("ch9155", 19155), ("ch916", 19160), ("ch9165", 19165), ("ch917", 19170), ("ch9175", 19175), ("ch918", 19180), ("ch9185", 19185), ("ch919", 19190), ("ch9195", 19195), ("ch920", 19200), ("ch9205", 19205), ("ch921", 19210), ("ch9215", 19215), ("ch922", 19220), ("ch9225", 19225), ("ch923", 19230), ("ch9235", 19235), ("ch924", 19240), ("ch9245", 19245), ("ch925", 19250), ("ch9255", 19255), ("ch926", 19260), ("ch9265", 19265), ("ch927", 19270), ("ch9275", 19275), ("ch928", 19280), ("ch9285", 19285), ("ch929", 19290), ("ch9295", 19295), ("ch930", 19300), ("ch9305", 19305), ("ch931", 19310), ("ch9315", 19315), ("ch932", 19320), ("ch9325", 19325), ("ch933", 19330), ("ch9335", 19335), ("ch934", 19340), ("ch9345", 19345), ("ch935", 19350), ("ch9355", 19355), ("ch936", 19360), ("ch9365", 19365), ("ch937", 19370), ("ch9375", 19375), ("ch938", 19380), ("ch9385", 19385), ("ch939", 19390), ("ch9395", 19395), ("ch940", 19400), ("ch9405", 19405), ("ch941", 19410), ("ch9415", 19415), ("ch942", 19420), ("ch9425", 19425), ("ch943", 19430), ("ch9435", 19435), ("ch944", 19440), ("ch9445", 19445), ("ch945", 19450), ("ch9455", 19455), ("ch946", 19460), ("ch9465", 19465), ("ch947", 19470), ("ch9475", 19475), ("ch948", 19480), ("ch9485", 19485), ("ch949", 19490), ("ch9495", 19495), ("ch950", 19500), ("ch9505", 19505), ("ch951", 19510), ("ch9515", 19515), ("ch952", 19520), ("ch9525", 19525), ("ch953", 19530), ("ch9535", 19535), ("ch954", 19540), ("ch9545", 19545), ("ch955", 19550), ("ch9555", 19555), ("ch956", 19560), ("ch9565", 19565), ("ch957", 19570), ("ch9575", 19575), ("ch958", 19580), ("ch9585", 19585), ("ch959", 19590), ("ch9595", 19595), ("ch960", 19600), ("ch9605", 19605), ("ch961", 19610), ("notApplicable", 2147483647))

class Rate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 2147483646, 2147483647))
    namedValues = NamedValues(("sdh156", 1), ("sdh2488", 2), ("notAvailable", 2147483646), ("notApplicable", 2147483647))

class TrxMediaWithNA(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 2147483646, 2147483647))
    namedValues = NamedValues(("undefined", 0), ("optical", 1), ("tp1000BaseT", 2), ("tp100BaseT", 3), ("tp10BaseT", 4), ("electrical", 5), ("notAvailable", 2147483646), ("notApplicable", 2147483647))

class FecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 2147483647))
    namedValues = NamedValues(("disabled", 0), ("g709", 1), ("g9751I4", 2), ("g9751I7", 3), ("sdFec", 4), ("notApplicable", 2147483647))

class TruthValueWithNA(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2147483646, 2147483647))
    namedValues = NamedValues(("true", 0), ("false", 1), ("notAvailable", 2147483646), ("notApplicable", 2147483647))

class TcmMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 2147483647))
    namedValues = NamedValues(("operational", 0), ("transparent", 1), ("monitor", 2), ("notApplicable", 2147483647))

class TcmNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 2147483647))
    namedValues = NamedValues(("tcm1", 0), ("tcm2", 1), ("tcm3", 2), ("tcm4", 3), ("tcm5", 4), ("tcm6", 5), ("notApplicable", 2147483647))

class OtnTIMDetModeWithNA(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 2147483647))
    namedValues = NamedValues(("off", 0), ("sapi", 1), ("dapi", 2), ("both", 3), ("notApplicable", 2147483647))

class OtnDirectionWithNA(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 2147483647))
    namedValues = NamedValues(("none", 0), ("rx", 1), ("tx", 2), ("notApplicable", 2147483647))

class OtnAlarmMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 2147483647))
    namedValues = NamedValues(("ignore", 0), ("alarm", 1), ("display", 2), ("notApplicable", 2147483647))

class CcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 2147483647))
    namedValues = NamedValues(("addDrop", 0), ("broadcast", 1), ("select", 2), ("notApplicable", 2147483647))

class AutoNegotiationStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2147483646, 2147483647))
    namedValues = NamedValues(("incomplete", 1), ("halfDuplex", 2), ("fullDuplex", 3), ("halfDuplexRxPauseOn", 4), ("halfDuplexTxPauseOn", 5), ("halfDuplexRxTxPauseOn", 6), ("fullDuplexRxPauseOn", 7), ("fullDuplexTxPauseOn", 8), ("fullDuplexRxTxPauseOn", 9), ("fullDuplexFec", 10), ("fec", 11), ("notAvailable", 2147483646), ("notApplicable", 2147483647))

class FlowControlMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 2147483647))
    namedValues = NamedValues(("noPause", 1), ("rxPause", 2), ("txPause", 3), ("bothPause", 4), ("notApplicable", 2147483647))

class OtnType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("sm", 0), ("tcm", 1), ("pm", 2))

class OtnTypeWithNA(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 2147483646, 2147483647))
    namedValues = NamedValues(("sm", 0), ("pm", 1), ("tcm1", 2), ("tcm2", 3), ("tcm3", 4), ("tcm4", 5), ("tcm5", 6), ("tcm6", 7), ("notAvailable", 2147483646), ("notApplicable", 2147483647))

class AuType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("au4Type64c", 0), ("au4Type16c", 1), ("au4Type4c", 2), ("au4", 3), ("au3", 4))

class VcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("vc4Type64c", 0), ("vc4Type16c", 1), ("vc4Type4c", 2), ("vc4", 3), ("vc3", 4))

class StsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("stsType192c", 0), ("stsType48c", 1), ("stsType3c", 2), ("sts3", 3), ("sts1", 4))

class StsSpeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("sts192cSpe", 0), ("sts48cSpe", 1), ("sts12cSpe", 2), ("sts3cSpe", 3), ("sts1Spe", 4))

class AdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("down", 1), ("up", 2))

class BerLevelMTOSI(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(5, 10, 12, 13, 15))
    namedValues = NamedValues(("osnrMargin1", 5), ("osnrMargin2", 10), ("rxBerLevel1", 12), ("rxBerLevel2", 13), ("rxBerLevel3", 15))

class BerLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(12, 13, 15))
    namedValues = NamedValues(("rxBerLevel1", 12), ("rxBerLevel2", 13), ("rxBerLevel3", 15))

class AutoAlarmStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 2147483647))
    namedValues = NamedValues(("suppressTrxAndSignal", 1), ("suppressSignal", 2), ("suppressNone", 3), ("notApplicable", 2147483647))

class InterfaceStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 2147483647))
    namedValues = NamedValues(("outOfService", 1), ("autoInService", 2), ("inService", 3), ("maintenance", 4), ("notApplicable", 2147483647))

class OpticalLayerMappingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("fourOpticalLanes", 1), ("tenOpticalLanes", 2), ("singleOpticalChannel", 3))

class PhysicalLayerMappingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("dualFiber", 1), ("singleFiber", 2))

class TribPortIdType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2147483647))
    namedValues = NamedValues(("unused", 0), ("tp1", 1), ("tp2", 2), ("tp3", 3), ("tp4", 4), ("tp5", 5), ("tp6", 6), ("tp7", 7), ("tp8", 8), ("tp9", 9), ("tp10", 10), ("tp11", 11), ("notApplicable", 2147483647))

class ServiceIdWithNotUsed(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), )
class TrxRxState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 2147483647))
    namedValues = NamedValues(("missing", 0), ("initStarted", 1), ("initReady", 2), ("frequencyReady", 3), ("inputSignalReceived", 4), ("adConverterReady", 5), ("dispersionCompensated", 6), ("ready", 7), ("notApplicable", 2147483647))

class TrxTxState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 2147483647))
    namedValues = NamedValues(("missing", 0), ("initStarted", 1), ("initReady", 2), ("dataPathLocked", 3), ("laserReadyOff", 4), ("laserReady", 5), ("laserBiasReady", 6), ("ready", 7), ("notApplicable", 2147483647))

class DispersionSearchLimit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(22500, 30000))
    namedValues = NamedValues(("medium", 22500), ("high", 30000))

class SignalDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 2147483646))
    namedValues = NamedValues(("rx", 1), ("tx", 2), ("biDir", 3), ("txRx", 4), ("notAvailable", 2147483646))

class RsFecMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("forcedOff", 0), ("forcedOn", 1), ("auto", 2))

class RsFecOnOff(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("off", 0), ("on", 1), ("undefined", 2))

class MplsLabel(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1048575)

class InterfaceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 2147483646, 2147483647))
    namedValues = NamedValues(("individual", 1), ("bundled", 2), ("bundledSplit", 3), ("notAvailable", 2147483646), ("notApplicable", 2147483647))

class ConnectorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 2147483647))
    namedValues = NamedValues(("connector4x10Gb", 1), ("connector1x100Gb", 2), ("notApplicable", 2147483647))

class Platform(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("cuosc", 1), ("cusfpv1", 2), ("cusfpv2", 3), ("cusfpv3", 4), ("culessTU1", 5), ("culessTU2", 6), ("culessTU3", 7), ("culessTU4", 8), ("pizzaboxFHA1UDC", 9), ("pizzaboxEMXP1UDC", 10), ("pizzaboxHDEA1600", 11))

mibBuilder.exportSymbols("LUM-TC", Unsigned32WithNA=Unsigned32WithNA, OtnType=OtnType, MgmtNameString=MgmtNameString, InterfaceStatus=InterfaceStatus, DispersionSearchLimit=DispersionSearchLimit, BoardOrInterfaceOperStatus=BoardOrInterfaceOperStatus, ObjectProperty=ObjectProperty, EnabledDisabledWithNA=EnabledDisabledWithNA, OperStatusWithNA=OperStatusWithNA, InterfaceType=InterfaceType, DisplayStringWithNA=DisplayStringWithNA, EnableDisable=EnableDisable, OtnMonitorType=OtnMonitorType, SignalDirection=SignalDirection, AutoAlarmStatus=AutoAlarmStatus, FaultStatus=FaultStatus, OtnDirectionWithNA=OtnDirectionWithNA, CcType=CcType, RsFecMode=RsFecMode, PmReset=PmReset, TcmNumber=TcmNumber, PortNumber=PortNumber, OtnTypeWithNA=OtnTypeWithNA, FaultStatusWithNA=FaultStatusWithNA, AdminStatus=AdminStatus, Integer32WithNA=Integer32WithNA, StsSpeType=StsSpeType, TrxTxState=TrxTxState, BerLevelMTOSI=BerLevelMTOSI, FrequencyOnlyNotApplicable=FrequencyOnlyNotApplicable, LaneFrequency=LaneFrequency, LambdaFrequency=LambdaFrequency, OtnTIMDetModeWithNA=OtnTIMDetModeWithNA, Time7200minNo0=Time7200minNo0, MplsLabel=MplsLabel, FecType=FecType, Activated=Activated, FlowControlMode=FlowControlMode, OtnTIMDetMode=OtnTIMDetMode, TrxRxState=TrxRxState, OnOff=OnOff, TrxMediaWithNA=TrxMediaWithNA, ConnectorType=ConnectorType, TruthValueWithNA=TruthValueWithNA, CommandString=CommandString, AuType=AuType, PYSNMP_MODULE_ID=lumTcModule, SignalStatusWithNA=SignalStatusWithNA, AutoNegotiationStatus=AutoNegotiationStatus, Platform=Platform, SignalType=SignalType, Layer=Layer, SignalFormat=SignalFormat, VcType=VcType, lumTcModule=lumTcModule, SlotNumber=SlotNumber, Frequency=Frequency, TrxMedia=TrxMedia, SignalStructure=SignalStructure, BoardOrInterfaceAdminStatus=BoardOrInterfaceAdminStatus, SyncSourceMode=SyncSourceMode, OpticalLayerMappingType=OpticalLayerMappingType, Signed32WithNA=Signed32WithNA, LambdaType=LambdaType, OtnAlarmMode=OtnAlarmMode, PhysicalLayerMappingType=PhysicalLayerMappingType, ResetWithNA=ResetWithNA, LaserMode=LaserMode, StsType=StsType, TribPortIdType=TribPortIdType, Rate=Rate, PortType=PortType, OtnMonitorConfig=OtnMonitorConfig, ServiceIdWithNotUsed=ServiceIdWithNotUsed, SubrackNumber=SubrackNumber, SyncSourceState=SyncSourceState, BerLevel=BerLevel, MgmtNameStringWithNA=MgmtNameStringWithNA, TcmMode=TcmMode, RsFecOnOff=RsFecOnOff, AdminStatusWithNA=AdminStatusWithNA, Time7200min=Time7200min)
