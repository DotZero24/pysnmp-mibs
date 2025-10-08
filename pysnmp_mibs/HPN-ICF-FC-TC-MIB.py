#
# PySNMP MIB module HPN-ICF-FC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-FC-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class HpnicfFcAddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("wwn", 1), ("fcid", 2))

class HpnicfFcAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(3, 3), ValueSizeConstraint(8, 8), )
class HpnicfFcAddressId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class HpnicfFcAddressIdOrZero(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(3, 3), )
class HpnicfFcNameId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class HpnicfFcNameIdOrZero(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), )
class HpnicfFcClassOfServices(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("classF", 0), ("class1", 1), ("class2", 2), ("class3", 3), ("class4", 4), ("class5", 5), ("class6", 6))

class HpnicfFcBbCredit(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 32767)

class HpnicfFcRxMTU(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(128, 2112)

class HpnicfFcVsanIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4095)

class HpnicfFcStartOper(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class HpnicfFcDomainId(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 239)

class HpnicfFcDomainIdOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 239)

class HpnicfFcDomainPriority(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 254)

class HpnicfFcDmState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("disabledWithNoDomain", 1), ("disabledWithDomainCfg", 2), ("stableWithNoEports", 3), ("stableWithDomainCfg", 4), ("stableWithNoDomain", 5), ("principalSwitchInSelect", 6), ("domainIdRequesting", 7), ("buildFabricPhase", 8), ("reconfigureFabricPhase", 9), ("unknown", 10))

class HpnicfFcDomainIdList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

mibBuilder.exportSymbols("HPN-ICF-FC-TC-MIB", HpnicfFcDomainId=HpnicfFcDomainId, HpnicfFcDomainIdOrZero=HpnicfFcDomainIdOrZero, HpnicfFcDomainIdList=HpnicfFcDomainIdList, HpnicfFcVsanIndex=HpnicfFcVsanIndex, HpnicfFcStartOper=HpnicfFcStartOper, HpnicfFcNameId=HpnicfFcNameId, HpnicfFcNameIdOrZero=HpnicfFcNameIdOrZero, HpnicfFcDmState=HpnicfFcDmState, HpnicfFcAddress=HpnicfFcAddress, HpnicfFcAddressId=HpnicfFcAddressId, HpnicfFcBbCredit=HpnicfFcBbCredit, HpnicfFcDomainPriority=HpnicfFcDomainPriority, HpnicfFcClassOfServices=HpnicfFcClassOfServices, HpnicfFcAddressType=HpnicfFcAddressType, HpnicfFcRxMTU=HpnicfFcRxMTU, HpnicfFcAddressIdOrZero=HpnicfFcAddressIdOrZero)
