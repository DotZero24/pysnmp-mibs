#
# PySNMP MIB module RBTWS-CLIENT-SESSION-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cabletron/RBTWS-CLIENT-SESSION-TC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rbtwsMibs, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbtwsClientSessionTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 10))
rbtwsClientSessionTc.setRevisions(('2007-10-08 00:10', '2006-09-26 00:01',))
if mibBuilder.loadTexts: rbtwsClientSessionTc.setLastUpdated('200710091719Z')
if mibBuilder.loadTexts: rbtwsClientSessionTc.setOrganization('Enterasys Networks')
class RbtwsUserAccessType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("mac", 1), ("web", 2), ("dot1x", 3), ("last-resort", 4))

class RbtwsClientSessionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("associated", 1), ("authorizing", 2), ("authorized", 3), ("active", 4), ("de-associated", 5), ("roaming-away", 6), ("updated-to-roam", 7), ("wired", 8), ("clearing", 9), ("invalid", 10), ("web-authing", 11))

class RbtwsClientDot1xState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("initialize", 1), ("disconnected", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("wired", 6), ("aborting", 7), ("held", 8))

class RbtwsClientAuthenProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("eap-tls", 2), ("eap-ttls", 3), ("md5", 4), ("peap", 5), ("leap", 6), ("pass-through", 7))

class RbtwsClientAccessMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("ap", 2), ("wired", 3))

mibBuilder.exportSymbols("RBTWS-CLIENT-SESSION-TC", RbtwsClientAuthenProtocolType=RbtwsClientAuthenProtocolType, rbtwsClientSessionTc=rbtwsClientSessionTc, RbtwsClientDot1xState=RbtwsClientDot1xState, RbtwsClientSessionState=RbtwsClientSessionState, PYSNMP_MODULE_ID=rbtwsClientSessionTc, RbtwsClientAccessMode=RbtwsClientAccessMode, RbtwsUserAccessType=RbtwsUserAccessType)
