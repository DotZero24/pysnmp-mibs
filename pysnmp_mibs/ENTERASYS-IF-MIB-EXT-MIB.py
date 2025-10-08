#
# PySNMP MIB module ENTERASYS-IF-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-IF-MIB-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifEntry, = mibBuilder.importSymbols("IF-MIB", "ifEntry")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysIfMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57))
etsysIfMibExtMIB.setRevisions(('2015-04-14 12:39', '2014-07-24 13:22', '2013-04-12 13:14', '2013-02-11 18:14', '2012-02-02 20:08', '2011-12-07 15:58', '2011-10-25 19:48', '2011-06-08 12:12', '2011-05-12 14:15', '2005-01-13 21:35',))
if mibBuilder.loadTexts: etsysIfMibExtMIB.setLastUpdated('201504141239Z')
if mibBuilder.loadTexts: etsysIfMibExtMIB.setOrganization('Extreme Networks, Inc.')
class EtsysIfOperStatusCauses(TextualConvention, Bits):
    reference = "RFC 2863, 'The Interfaces Group MIB' ENTERASYS-LINK-FLAP-MIB ENTERASYS-FLOW-LIMITING-MIB ENTERASYS-POLICY-PROFILE-MIB ENTERASYS-CLASS-OF-SERVICE-MIB ENTERASYS-ETH-OAM-EXT-MIB ENTERASYS-MAC-LOCKING-MIB IEEE Std. 802.1X-2001 IEEE Std. 802.3-2002 ENTERASYS-VIRTUAL-SWITCH-BONDING-MIB ENTERASYS-LINKSTATE-MIB ENTERASYS-ETH-OAM-EXT-MIB ENTERASYS-TRANSMIT-QUEUE-MONITOR-MIB IEEE Std. 802.1Qbb-2011 IEEE Std. 802.1X-2010"
    status = 'current'
    namedValues = NamedValues(("adminStatus", 0), ("linkLoss", 1), ("linkFlap", 2), ("self", 3), ("initialization", 4), ("flowLimiting", 5), ("policy", 6), ("classOfService", 7), ("ieee8021x", 8), ("ieee8023lag", 9), ("enetOam", 10), ("enetOamLb", 11), ("macLock", 12), ("chassisBonding", 13), ("linkState", 14), ("enetOamUld", 15), ("txqMonitor", 16), ("priorityFlowControl", 17), ("macSec", 18))

etsysIfMibExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1))
etsysIfMibExtSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 1))
etsysIfMibExtInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2))
etsysIfOperStateLinkChange = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysIfOperStateLinkChange.setStatus('current')
etsysInterfaceExtTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1), )
if mibBuilder.loadTexts: etsysInterfaceExtTable.setStatus('current')
etsysInterfaceExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1, 1), )
ifEntry.registerAugmentions(("ENTERASYS-IF-MIB-EXT-MIB", "etsysInterfaceExtEntry"))
etsysInterfaceExtEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: etsysInterfaceExtEntry.setStatus('current')
etsysIfOperStatusCause = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1, 1, 1), EtsysIfOperStatusCauses()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysIfOperStatusCause.setStatus('current')
etsysIfMibExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2))
etsysIfMibExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1))
etsysIfMibExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 2))
etsysIfMibExtOperLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1, 1)).setObjects(("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfOperStateLinkChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIfMibExtOperLinkGroup = etsysIfMibExtOperLinkGroup.setStatus('current')
etsysIfMibExtOperStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1, 2)).setObjects(("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfOperStatusCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIfMibExtOperStatusGroup = etsysIfMibExtOperStatusGroup.setStatus('current')
etsysIfMibExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 2, 1)).setObjects(("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfMibExtOperLinkGroup"), ("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfMibExtOperStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIfMibExtCompliance = etsysIfMibExtCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-IF-MIB-EXT-MIB", etsysIfMibExtObjects=etsysIfMibExtObjects, etsysIfMibExtOperStatusGroup=etsysIfMibExtOperStatusGroup, etsysIfMibExtMIB=etsysIfMibExtMIB, etsysIfMibExtSystem=etsysIfMibExtSystem, etsysIfMibExtGroups=etsysIfMibExtGroups, etsysIfMibExtCompliances=etsysIfMibExtCompliances, etsysInterfaceExtEntry=etsysInterfaceExtEntry, EtsysIfOperStatusCauses=EtsysIfOperStatusCauses, etsysIfMibExtCompliance=etsysIfMibExtCompliance, etsysIfMibExtConformance=etsysIfMibExtConformance, etsysIfOperStatusCause=etsysIfOperStatusCause, etsysIfMibExtInterface=etsysIfMibExtInterface, PYSNMP_MODULE_ID=etsysIfMibExtMIB, etsysInterfaceExtTable=etsysInterfaceExtTable, etsysIfOperStateLinkChange=etsysIfOperStateLinkChange, etsysIfMibExtOperLinkGroup=etsysIfMibExtOperLinkGroup)
