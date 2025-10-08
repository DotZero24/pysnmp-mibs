#
# PySNMP MIB module DC-L2VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/DC-L2VPN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:49 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NumericIndex, OperStatus, MjStatus, NpgOperStatus, AdminStatus, SjStatus = mibBuilder.importSymbols("DC-MASTER-TC", "NumericIndex", "OperStatus", "MjStatus", "NpgOperStatus", "AdminStatus", "SjStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
l2vpnMib = ModuleIdentity((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1))
if mibBuilder.loadTexts: l2vpnMib.setLastUpdated('201309200000Z')
if mibBuilder.loadTexts: l2vpnMib.setOrganization('Data Connection Ltd.')
l2vpnObjects = MibIdentifier((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1))
l2vpnConformance = MibIdentifier((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2))
class L2vmMjIfId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(696844288, 697761792, 1921384448))
    namedValues = NamedValues(("ifAtgI3", 696844288), ("ifAtgBdpi", 697761792), ("ifAtgPvpi", 1921384448))

class L2vmSjIfId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1031864320))
    namedValues = NamedValues(("ifAtgRpi", 1031864320))

class L2vpnADType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("bgp", 2))

class L2vpnSigType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("ldp", 2), ("bgp", 3))

class L2vpnPwBindType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pwMibIndex", 1), ("lclRmtVeId", 2))

class L2vpnType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("vpls", 1), ("vpws", 2))

class L2vpnSiteId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class L2vpnVeIdOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class BgpRouteDistinguisher(TextualConvention, OctetString):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class BgpExtendedCommunity(TextualConvention, OctetString):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class BgpRouteTargetType(TextualConvention, Integer32):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("import", 1), ("export", 2), ("both", 3))

l2vmEntityTable = MibTable((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1), )
if mibBuilder.loadTexts: l2vmEntityTable.setStatus('current')
l2vmEntityEntry = MibTableRow((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1), ).setIndexNames((0, "DC-L2VPN-MIB", "l2vmEntityIndex"))
if mibBuilder.loadTexts: l2vmEntityEntry.setStatus('current')
l2vmEntityIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 1), NumericIndex())
if mibBuilder.loadTexts: l2vmEntityIndex.setStatus('current')
l2vmEntityRowStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntityRowStatus.setStatus('current')
l2vmEntityAdminStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 3), AdminStatus().clone('adminStatusUp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntityAdminStatus.setStatus('current')
l2vmEntityOperStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 4), NpgOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2vmEntityOperStatus.setStatus('current')
l2vmEntityVplsIndexNext = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 5), NumericIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2vmEntityVplsIndexNext.setStatus('current')
l2vmEntityVpwsIndexNext = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 6), NumericIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2vmEntityVpwsIndexNext.setStatus('current')
l2vmEntityNbasePriority = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntityNbasePriority.setStatus('current')
l2vmEntityTimerGranularity = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntityTimerGranularity.setStatus('current')
l2vmEntityRestartDuration = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 9), TimeTicks().clone(18000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntityRestartDuration.setStatus('current')
l2vmEntityRescheduleLimit = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(1000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntityRescheduleLimit.setStatus('current')
l2vmEntityPvpiBufferPoolSize = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntityPvpiBufferPoolSize.setStatus('current')
l2vmEntityRpiBufferPoolSize = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntityRpiBufferPoolSize.setStatus('current')
l2vmEntityRpiFailTimeout = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 13), TimeTicks().clone(3000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntityRpiFailTimeout.setStatus('current')
l2vmEntityRetryInterval = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 14), TimeTicks().clone(1000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntityRetryInterval.setStatus('current')
l2vmEntityVpnNotifEnable = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 15), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntityVpnNotifEnable.setStatus('current')
l2vmEntityVpnNotifBufferPoolSize = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntityVpnNotifBufferPoolSize.setStatus('current')
l2vmEntitySupportVpls = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 17), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntitySupportVpls.setStatus('current')
l2vmEntityBdpiBufferPoolSize = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmEntityBdpiBufferPoolSize.setStatus('current')
l2vmMjTable = MibTable((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2), )
if mibBuilder.loadTexts: l2vmMjTable.setStatus('current')
l2vmMjEntry = MibTableRow((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1), ).setIndexNames((0, "DC-L2VPN-MIB", "l2vmEntityIndex"), (0, "DC-L2VPN-MIB", "l2vmMjInterfaceId"), (0, "DC-L2VPN-MIB", "l2vmMjPartnerType"), (0, "DC-L2VPN-MIB", "l2vmMjPartnerIndex"), (0, "DC-L2VPN-MIB", "l2vmMjSubIndex"))
if mibBuilder.loadTexts: l2vmMjEntry.setStatus('current')
l2vmMjInterfaceId = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 2), L2vmMjIfId())
if mibBuilder.loadTexts: l2vmMjInterfaceId.setStatus('current')
l2vmMjPartnerType = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: l2vmMjPartnerType.setStatus('current')
l2vmMjPartnerIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: l2vmMjPartnerIndex.setStatus('current')
l2vmMjSubIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 5), Unsigned32())
if mibBuilder.loadTexts: l2vmMjSubIndex.setStatus('current')
l2vmMjRowStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmMjRowStatus.setStatus('current')
l2vmMjAdminStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 7), AdminStatus().clone('adminStatusUp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmMjAdminStatus.setStatus('current')
l2vmMjOperStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 8), OperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2vmMjOperStatus.setStatus('current')
l2vmMjJoinStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 9), MjStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2vmMjJoinStatus.setStatus('current')
l2vmSjTable = MibTable((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3), )
if mibBuilder.loadTexts: l2vmSjTable.setStatus('current')
l2vmSjEntry = MibTableRow((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3, 1), ).setIndexNames((0, "DC-L2VPN-MIB", "l2vmEntityIndex"), (0, "DC-L2VPN-MIB", "l2vmSjInterfaceId"), (0, "DC-L2VPN-MIB", "l2vmSjPartnerType"), (0, "DC-L2VPN-MIB", "l2vmSjPartnerIndex"), (0, "DC-L2VPN-MIB", "l2vmSjSubIndex"))
if mibBuilder.loadTexts: l2vmSjEntry.setStatus('current')
l2vmSjInterfaceId = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3, 1, 2), L2vmSjIfId())
if mibBuilder.loadTexts: l2vmSjInterfaceId.setStatus('current')
l2vmSjPartnerType = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3, 1, 3), Unsigned32())
if mibBuilder.loadTexts: l2vmSjPartnerType.setStatus('current')
l2vmSjPartnerIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: l2vmSjPartnerIndex.setStatus('current')
l2vmSjSubIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3, 1, 5), Unsigned32())
if mibBuilder.loadTexts: l2vmSjSubIndex.setStatus('current')
l2vmSjJoinStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3, 1, 6), SjStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2vmSjJoinStatus.setStatus('current')
l2vmBgpRTCfgTable = MibTable((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4), )
if mibBuilder.loadTexts: l2vmBgpRTCfgTable.setStatus('current')
l2vmBgpRTCfgEntry = MibTableRow((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1), ).setIndexNames((0, "DC-L2VPN-MIB", "l2vmEntityIndex"), (0, "DC-L2VPN-MIB", "l2vmBgpRTCfgVpnType"), (0, "DC-L2VPN-MIB", "l2vmBgpRTCfgVpnIndex"), (0, "DC-L2VPN-MIB", "l2vmBgpRTCfgIndex"))
if mibBuilder.loadTexts: l2vmBgpRTCfgEntry.setStatus('current')
l2vmBgpRTCfgVpnType = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 2), L2vpnType())
if mibBuilder.loadTexts: l2vmBgpRTCfgVpnType.setStatus('current')
l2vmBgpRTCfgVpnIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 3), NumericIndex())
if mibBuilder.loadTexts: l2vmBgpRTCfgVpnIndex.setStatus('current')
l2vmBgpRTCfgIndex = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 4), NumericIndex())
if mibBuilder.loadTexts: l2vmBgpRTCfgIndex.setStatus('current')
l2vmBgpRTCfgRowStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmBgpRTCfgRowStatus.setStatus('current')
l2vmBgpRTCfgAdminStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 6), AdminStatus().clone('adminStatusUp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmBgpRTCfgAdminStatus.setStatus('current')
l2vmBgpRTCfgOperStatus = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 7), NpgOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2vmBgpRTCfgOperStatus.setStatus('current')
l2vmBgpRTCfgType = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 8), BgpRouteTargetType().clone('both')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmBgpRTCfgType.setStatus('current')
l2vmBgpRTCfgRT = MibTableColumn((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 9), BgpExtendedCommunity().clone(hexValue="0000000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: l2vmBgpRTCfgRT.setStatus('current')
l2vpnCompliances = MibIdentifier((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2, 1))
l2vpnGroups = MibIdentifier((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2, 2))
l2vpnFrameworkCompliance = ModuleCompliance((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2, 1, 1)).setObjects(("DC-L2VPN-MIB", "l2vpnFrameworkGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2vpnFrameworkCompliance = l2vpnFrameworkCompliance.setStatus('current')
l2vmBgpADCompliance = ModuleCompliance((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2, 1, 2)).setObjects(("DC-L2VPN-MIB", "l2vpnFrameworkGroup"), ("DC-L2VPN-MIB", "l2vmBgpADGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2vmBgpADCompliance = l2vmBgpADCompliance.setStatus('current')
l2vpnFrameworkGroup = ObjectGroup((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2, 2, 1)).setObjects(("DC-L2VPN-MIB", "l2vmEntityRowStatus"), ("DC-L2VPN-MIB", "l2vmEntityAdminStatus"), ("DC-L2VPN-MIB", "l2vmEntityOperStatus"), ("DC-L2VPN-MIB", "l2vmEntityVplsIndexNext"), ("DC-L2VPN-MIB", "l2vmEntityVpwsIndexNext"), ("DC-L2VPN-MIB", "l2vmEntityNbasePriority"), ("DC-L2VPN-MIB", "l2vmEntityTimerGranularity"), ("DC-L2VPN-MIB", "l2vmEntityRestartDuration"), ("DC-L2VPN-MIB", "l2vmEntityRescheduleLimit"), ("DC-L2VPN-MIB", "l2vmEntityPvpiBufferPoolSize"), ("DC-L2VPN-MIB", "l2vmEntityRpiBufferPoolSize"), ("DC-L2VPN-MIB", "l2vmEntityRpiFailTimeout"), ("DC-L2VPN-MIB", "l2vmEntityRetryInterval"), ("DC-L2VPN-MIB", "l2vmEntityVpnNotifEnable"), ("DC-L2VPN-MIB", "l2vmEntityVpnNotifBufferPoolSize"), ("DC-L2VPN-MIB", "l2vmEntitySupportVpls"), ("DC-L2VPN-MIB", "l2vmEntityBdpiBufferPoolSize"), ("DC-L2VPN-MIB", "l2vmMjRowStatus"), ("DC-L2VPN-MIB", "l2vmMjAdminStatus"), ("DC-L2VPN-MIB", "l2vmMjOperStatus"), ("DC-L2VPN-MIB", "l2vmMjJoinStatus"), ("DC-L2VPN-MIB", "l2vmSjJoinStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2vpnFrameworkGroup = l2vpnFrameworkGroup.setStatus('current')
l2vmBgpADGroup = ObjectGroup((1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2, 2, 2)).setObjects(("DC-L2VPN-MIB", "l2vmBgpRTCfgRowStatus"), ("DC-L2VPN-MIB", "l2vmBgpRTCfgAdminStatus"), ("DC-L2VPN-MIB", "l2vmBgpRTCfgOperStatus"), ("DC-L2VPN-MIB", "l2vmBgpRTCfgType"), ("DC-L2VPN-MIB", "l2vmBgpRTCfgRT"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    l2vmBgpADGroup = l2vmBgpADGroup.setStatus('current')
mibBuilder.exportSymbols("DC-L2VPN-MIB", l2vpnFrameworkGroup=l2vpnFrameworkGroup, L2vmSjIfId=L2vmSjIfId, L2vmMjIfId=L2vmMjIfId, L2vpnSigType=L2vpnSigType, l2vpnMib=l2vpnMib, l2vmEntityOperStatus=l2vmEntityOperStatus, l2vmMjRowStatus=l2vmMjRowStatus, l2vmMjPartnerIndex=l2vmMjPartnerIndex, l2vmBgpRTCfgVpnType=l2vmBgpRTCfgVpnType, l2vmEntityIndex=l2vmEntityIndex, l2vmEntityPvpiBufferPoolSize=l2vmEntityPvpiBufferPoolSize, l2vmSjInterfaceId=l2vmSjInterfaceId, PYSNMP_MODULE_ID=l2vpnMib, L2vpnPwBindType=L2vpnPwBindType, l2vmEntityTable=l2vmEntityTable, l2vmEntityAdminStatus=l2vmEntityAdminStatus, l2vmSjJoinStatus=l2vmSjJoinStatus, l2vmBgpRTCfgAdminStatus=l2vmBgpRTCfgAdminStatus, l2vmEntityTimerGranularity=l2vmEntityTimerGranularity, BgpRouteDistinguisher=BgpRouteDistinguisher, l2vmBgpADGroup=l2vmBgpADGroup, L2vpnType=L2vpnType, l2vmEntityRescheduleLimit=l2vmEntityRescheduleLimit, l2vmBgpRTCfgIndex=l2vmBgpRTCfgIndex, BgpExtendedCommunity=BgpExtendedCommunity, l2vmSjTable=l2vmSjTable, l2vmEntityNbasePriority=l2vmEntityNbasePriority, l2vpnCompliances=l2vpnCompliances, l2vmBgpRTCfgType=l2vmBgpRTCfgType, l2vmBgpRTCfgRowStatus=l2vmBgpRTCfgRowStatus, l2vmEntityVpwsIndexNext=l2vmEntityVpwsIndexNext, l2vmEntityRowStatus=l2vmEntityRowStatus, l2vmBgpRTCfgTable=l2vmBgpRTCfgTable, l2vpnObjects=l2vpnObjects, l2vmMjJoinStatus=l2vmMjJoinStatus, L2vpnVeIdOrZero=L2vpnVeIdOrZero, l2vmEntityEntry=l2vmEntityEntry, l2vmSjPartnerType=l2vmSjPartnerType, l2vmEntityRpiBufferPoolSize=l2vmEntityRpiBufferPoolSize, L2vpnADType=L2vpnADType, l2vmMjSubIndex=l2vmMjSubIndex, l2vmBgpRTCfgEntry=l2vmBgpRTCfgEntry, l2vmBgpRTCfgVpnIndex=l2vmBgpRTCfgVpnIndex, l2vmBgpADCompliance=l2vmBgpADCompliance, l2vmBgpRTCfgRT=l2vmBgpRTCfgRT, l2vpnConformance=l2vpnConformance, l2vmEntityVpnNotifEnable=l2vmEntityVpnNotifEnable, l2vmEntityRetryInterval=l2vmEntityRetryInterval, l2vmMjOperStatus=l2vmMjOperStatus, l2vmSjSubIndex=l2vmSjSubIndex, L2vpnSiteId=L2vpnSiteId, l2vmEntityVplsIndexNext=l2vmEntityVplsIndexNext, l2vpnGroups=l2vpnGroups, l2vmEntityRestartDuration=l2vmEntityRestartDuration, l2vmSjEntry=l2vmSjEntry, l2vmEntitySupportVpls=l2vmEntitySupportVpls, l2vmMjEntry=l2vmMjEntry, l2vmEntityRpiFailTimeout=l2vmEntityRpiFailTimeout, l2vmMjTable=l2vmMjTable, l2vmMjPartnerType=l2vmMjPartnerType, l2vpnFrameworkCompliance=l2vpnFrameworkCompliance, l2vmMjInterfaceId=l2vmMjInterfaceId, BgpRouteTargetType=BgpRouteTargetType, l2vmBgpRTCfgOperStatus=l2vmBgpRTCfgOperStatus, l2vmEntityBdpiBufferPoolSize=l2vmEntityBdpiBufferPoolSize, l2vmSjPartnerIndex=l2vmSjPartnerIndex, l2vmMjAdminStatus=l2vmMjAdminStatus, l2vmEntityVpnNotifBufferPoolSize=l2vmEntityVpnNotifBufferPoolSize)
