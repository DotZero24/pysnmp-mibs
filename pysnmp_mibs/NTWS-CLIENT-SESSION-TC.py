#
# PySNMP MIB module NTWS-CLIENT-SESSION-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NTWS-CLIENT-SESSION-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsClientSessionTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 10))
ntwsClientSessionTc.setRevisions(('2007-10-08 00:10', '2007-08-16 00:02', '2006-09-26 00:01',))
if mibBuilder.loadTexts: ntwsClientSessionTc.setLastUpdated('200710080010Z')
if mibBuilder.loadTexts: ntwsClientSessionTc.setOrganization('Nortel Networks')
class NtwsUserAccessType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("mac", 1), ("web", 2), ("dot1x", 3), ("last-resort", 4))

class NtwsClientSessionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("associated", 1), ("authorizing", 2), ("authorized", 3), ("active", 4), ("de-associated", 5), ("roaming-away", 6), ("updated-to-roam", 7), ("wired", 8), ("clearing", 9), ("invalid", 10), ("web-authing", 11))

class NtwsClientDot1xState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("initialize", 1), ("disconnected", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("wired", 6), ("aborting", 7), ("held", 8))

class NtwsClientAuthenProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("eap-tls", 2), ("eap-ttls", 3), ("md5", 4), ("peap", 5), ("leap", 6), ("pass-through", 7))

class NtwsClientAccessMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("ap", 2), ("wired", 3))

mibBuilder.exportSymbols("NTWS-CLIENT-SESSION-TC", NtwsUserAccessType=NtwsUserAccessType, NtwsClientAccessMode=NtwsClientAccessMode, NtwsClientAuthenProtocolType=NtwsClientAuthenProtocolType, PYSNMP_MODULE_ID=ntwsClientSessionTc, NtwsClientSessionState=NtwsClientSessionState, ntwsClientSessionTc=ntwsClientSessionTc, NtwsClientDot1xState=NtwsClientDot1xState)
