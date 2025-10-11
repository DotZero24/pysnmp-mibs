# SNMP MIB module (RUCKUS-SCG-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruckus/RUCKUS-SCG-WLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:13:47 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ruckusSCGWLANModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusSCGWLANModule")

(RuckusAdminStatus,
 RuckusRadioMode,
 RuckusRateLimiting,
 RuckusSSID,
 RuckusdB) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusAdminStatus",
    "RuckusRadioMode",
    "RuckusRateLimiting",
    "RuckusSSID",
    "RuckusdB")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusWLANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusWLANObjects_ObjectIdentity = ObjectIdentity
ruckusWLANObjects = _RuckusWLANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1)
)
_RuckusWLANInfo_ObjectIdentity = ObjectIdentity
ruckusWLANInfo = _RuckusWLANInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1)
)
_RuckusWLANTable_Object = MibTable
ruckusWLANTable = _RuckusWLANTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusWLANTable.setStatus("obsolete")
_RuckusWLANEntry_Object = MibTableRow
ruckusWLANEntry = _RuckusWLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 1, 1)
)
ruckusWLANEntry.setIndexNames(
    (0, "RUCKUS-SCG-WLAN-MIB", "ruckusWLANIndex"),
)
if mibBuilder.loadTexts:
    ruckusWLANEntry.setStatus("current")
_RuckusWLANSSID_Type = RuckusSSID
_RuckusWLANSSID_Object = MibTableColumn
ruckusWLANSSID = _RuckusWLANSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 1, 1, 1),
    _RuckusWLANSSID_Type()
)
ruckusWLANSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANSSID.setStatus("current")
_RuckusWLANNumSta_Type = Unsigned32
_RuckusWLANNumSta_Object = MibTableColumn
ruckusWLANNumSta = _RuckusWLANNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 1, 1, 12),
    _RuckusWLANNumSta_Type()
)
ruckusWLANNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANNumSta.setStatus("current")
_RuckusWLANRxBytes_Type = Counter64
_RuckusWLANRxBytes_Object = MibTableColumn
ruckusWLANRxBytes = _RuckusWLANRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 1, 1, 14),
    _RuckusWLANRxBytes_Type()
)
ruckusWLANRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANRxBytes.setStatus("current")
_RuckusWLANTxBytes_Type = Counter64
_RuckusWLANTxBytes_Object = MibTableColumn
ruckusWLANTxBytes = _RuckusWLANTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 1, 1, 16),
    _RuckusWLANTxBytes_Type()
)
ruckusWLANTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANTxBytes.setStatus("current")


class _RuckusWLANIndex_Type(Integer32):
    """Custom type ruckusWLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuckusWLANIndex_Type.__name__ = "Integer32"
_RuckusWLANIndex_Object = MibTableColumn
ruckusWLANIndex = _RuckusWLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 1, 1, 99),
    _RuckusWLANIndex_Type()
)
ruckusWLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANIndex.setStatus("current")
_RuckusSCGWLANTable_Object = MibTable
ruckusSCGWLANTable = _RuckusSCGWLANTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruckusSCGWLANTable.setStatus("current")
_RuckusSCGWLANEntry_Object = MibTableRow
ruckusSCGWLANEntry = _RuckusSCGWLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 2, 1)
)
ruckusSCGWLANEntry.setIndexNames(
    (0, "RUCKUS-SCG-WLAN-MIB", "ruckusSCGWLANIndex"),
)
if mibBuilder.loadTexts:
    ruckusSCGWLANEntry.setStatus("current")
_RuckusSCGWLANSSID_Type = RuckusSSID
_RuckusSCGWLANSSID_Object = MibTableColumn
ruckusSCGWLANSSID = _RuckusSCGWLANSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 2, 1, 1),
    _RuckusSCGWLANSSID_Type()
)
ruckusSCGWLANSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANSSID.setStatus("current")
_RuckusSCGWLANZone_Type = DisplayString
_RuckusSCGWLANZone_Object = MibTableColumn
ruckusSCGWLANZone = _RuckusSCGWLANZone_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 2, 1, 2),
    _RuckusSCGWLANZone_Type()
)
ruckusSCGWLANZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANZone.setStatus("current")
_RuckusSCGWLANDomain_Type = DisplayString
_RuckusSCGWLANDomain_Object = MibTableColumn
ruckusSCGWLANDomain = _RuckusSCGWLANDomain_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 2, 1, 3),
    _RuckusSCGWLANDomain_Type()
)
ruckusSCGWLANDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANDomain.setStatus("current")
_RuckusSCGWLANNumSta_Type = Unsigned32
_RuckusSCGWLANNumSta_Object = MibTableColumn
ruckusSCGWLANNumSta = _RuckusSCGWLANNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 2, 1, 12),
    _RuckusSCGWLANNumSta_Type()
)
ruckusSCGWLANNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANNumSta.setStatus("current")
_RuckusSCGWLANRxBytes_Type = Counter64
_RuckusSCGWLANRxBytes_Object = MibTableColumn
ruckusSCGWLANRxBytes = _RuckusSCGWLANRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 2, 1, 14),
    _RuckusSCGWLANRxBytes_Type()
)
ruckusSCGWLANRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANRxBytes.setStatus("current")
_RuckusSCGWLANTxBytes_Type = Counter64
_RuckusSCGWLANTxBytes_Object = MibTableColumn
ruckusSCGWLANTxBytes = _RuckusSCGWLANTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 2, 1, 16),
    _RuckusSCGWLANTxBytes_Type()
)
ruckusSCGWLANTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANTxBytes.setStatus("current")
_RuckusSCGWLANAuthType_Type = DisplayString
_RuckusSCGWLANAuthType_Object = MibTableColumn
ruckusSCGWLANAuthType = _RuckusSCGWLANAuthType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 2, 1, 17),
    _RuckusSCGWLANAuthType_Type()
)
ruckusSCGWLANAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAuthType.setStatus("current")


class _RuckusSCGWLANIndex_Type(Integer32):
    """Custom type ruckusSCGWLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuckusSCGWLANIndex_Type.__name__ = "Integer32"
_RuckusSCGWLANIndex_Object = MibTableColumn
ruckusSCGWLANIndex = _RuckusSCGWLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 1, 2, 1, 99),
    _RuckusSCGWLANIndex_Type()
)
ruckusSCGWLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANIndex.setStatus("current")
_RuckusWLANAPInfo_ObjectIdentity = ObjectIdentity
ruckusWLANAPInfo = _RuckusWLANAPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2)
)
_RuckusWLANAPTable_Object = MibTable
ruckusWLANAPTable = _RuckusWLANAPTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruckusWLANAPTable.setStatus("obsolete")
_RuckusWLANAPEntry_Object = MibTableRow
ruckusWLANAPEntry = _RuckusWLANAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 1, 1)
)
ruckusWLANAPEntry.setIndexNames(
    (0, "RUCKUS-SCG-WLAN-MIB", "ruckusWLANAPMacAddr"),
)
if mibBuilder.loadTexts:
    ruckusWLANAPEntry.setStatus("current")
_RuckusWLANAPMacAddr_Type = MacAddress
_RuckusWLANAPMacAddr_Object = MibTableColumn
ruckusWLANAPMacAddr = _RuckusWLANAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 1, 1, 1),
    _RuckusWLANAPMacAddr_Type()
)
ruckusWLANAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANAPMacAddr.setStatus("current")
_RuckusWLANAPUptime_Type = TimeTicks
_RuckusWLANAPUptime_Object = MibTableColumn
ruckusWLANAPUptime = _RuckusWLANAPUptime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 1, 1, 6),
    _RuckusWLANAPUptime_Type()
)
ruckusWLANAPUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANAPUptime.setStatus("current")
_RuckusWLANAPSWversion_Type = DisplayString
_RuckusWLANAPSWversion_Object = MibTableColumn
ruckusWLANAPSWversion = _RuckusWLANAPSWversion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 1, 1, 7),
    _RuckusWLANAPSWversion_Type()
)
ruckusWLANAPSWversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANAPSWversion.setStatus("current")
_RuckusWLANAPIPAddr_Type = IpAddress
_RuckusWLANAPIPAddr_Object = MibTableColumn
ruckusWLANAPIPAddr = _RuckusWLANAPIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 1, 1, 10),
    _RuckusWLANAPIPAddr_Type()
)
ruckusWLANAPIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANAPIPAddr.setStatus("current")
_RuckusWLANAPNumSta_Type = Unsigned32
_RuckusWLANAPNumSta_Object = MibTableColumn
ruckusWLANAPNumSta = _RuckusWLANAPNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 1, 1, 15),
    _RuckusWLANAPNumSta_Type()
)
ruckusWLANAPNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANAPNumSta.setStatus("current")
_RuckusSCGAPTable_Object = MibTable
ruckusSCGAPTable = _RuckusSCGAPTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruckusSCGAPTable.setStatus("current")
_RuckusSCGAPEntry_Object = MibTableRow
ruckusSCGAPEntry = _RuckusSCGAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1)
)
ruckusSCGAPEntry.setIndexNames(
    (0, "RUCKUS-SCG-WLAN-MIB", "ruckusSCGAPMac"),
)
if mibBuilder.loadTexts:
    ruckusSCGAPEntry.setStatus("current")
_RuckusSCGAPMac_Type = MacAddress
_RuckusSCGAPMac_Object = MibTableColumn
ruckusSCGAPMac = _RuckusSCGAPMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 1),
    _RuckusSCGAPMac_Type()
)
ruckusSCGAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPMac.setStatus("current")
_RuckusSCGAPGroup_Type = DisplayString
_RuckusSCGAPGroup_Object = MibTableColumn
ruckusSCGAPGroup = _RuckusSCGAPGroup_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 2),
    _RuckusSCGAPGroup_Type()
)
ruckusSCGAPGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPGroup.setStatus("current")
_RuckusSCGAPZone_Type = DisplayString
_RuckusSCGAPZone_Object = MibTableColumn
ruckusSCGAPZone = _RuckusSCGAPZone_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 3),
    _RuckusSCGAPZone_Type()
)
ruckusSCGAPZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPZone.setStatus("current")
_RuckusSCGAPDomain_Type = DisplayString
_RuckusSCGAPDomain_Object = MibTableColumn
ruckusSCGAPDomain = _RuckusSCGAPDomain_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 4),
    _RuckusSCGAPDomain_Type()
)
ruckusSCGAPDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPDomain.setStatus("current")
_RuckusSCGAPName_Type = DisplayString
_RuckusSCGAPName_Object = MibTableColumn
ruckusSCGAPName = _RuckusSCGAPName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 5),
    _RuckusSCGAPName_Type()
)
ruckusSCGAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPName.setStatus("current")
_RuckusSCGAPUptime_Type = TimeTicks
_RuckusSCGAPUptime_Object = MibTableColumn
ruckusSCGAPUptime = _RuckusSCGAPUptime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 6),
    _RuckusSCGAPUptime_Type()
)
ruckusSCGAPUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPUptime.setStatus("current")
_RuckusSCGAPFWversion_Type = DisplayString
_RuckusSCGAPFWversion_Object = MibTableColumn
ruckusSCGAPFWversion = _RuckusSCGAPFWversion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 7),
    _RuckusSCGAPFWversion_Type()
)
ruckusSCGAPFWversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPFWversion.setStatus("current")
_RuckusSCGAPModel_Type = DisplayString
_RuckusSCGAPModel_Object = MibTableColumn
ruckusSCGAPModel = _RuckusSCGAPModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 8),
    _RuckusSCGAPModel_Type()
)
ruckusSCGAPModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPModel.setStatus("current")
_RuckusSCGAPSerial_Type = DisplayString
_RuckusSCGAPSerial_Object = MibTableColumn
ruckusSCGAPSerial = _RuckusSCGAPSerial_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 9),
    _RuckusSCGAPSerial_Type()
)
ruckusSCGAPSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPSerial.setStatus("current")
_RuckusSCGAPIp_Type = IpAddress
_RuckusSCGAPIp_Object = MibTableColumn
ruckusSCGAPIp = _RuckusSCGAPIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 10),
    _RuckusSCGAPIp_Type()
)
ruckusSCGAPIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPIp.setStatus("current")
_RuckusSCGAPIPType_Type = DisplayString
_RuckusSCGAPIPType_Object = MibTableColumn
ruckusSCGAPIPType = _RuckusSCGAPIPType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 11),
    _RuckusSCGAPIPType_Type()
)
ruckusSCGAPIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPIPType.setStatus("current")
_RuckusSCGAPExtIp_Type = IpAddress
_RuckusSCGAPExtIp_Object = MibTableColumn
ruckusSCGAPExtIp = _RuckusSCGAPExtIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 12),
    _RuckusSCGAPExtIp_Type()
)
ruckusSCGAPExtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPExtIp.setStatus("current")
_RuckusSCGAPExtPort_Type = Unsigned32
_RuckusSCGAPExtPort_Object = MibTableColumn
ruckusSCGAPExtPort = _RuckusSCGAPExtPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 13),
    _RuckusSCGAPExtPort_Type()
)
ruckusSCGAPExtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPExtPort.setStatus("current")
_RuckusSCGAPNumSta_Type = Unsigned32
_RuckusSCGAPNumSta_Object = MibTableColumn
ruckusSCGAPNumSta = _RuckusSCGAPNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 15),
    _RuckusSCGAPNumSta_Type()
)
ruckusSCGAPNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPNumSta.setStatus("current")
_RuckusSCGAPConnStatus_Type = DisplayString
_RuckusSCGAPConnStatus_Object = MibTableColumn
ruckusSCGAPConnStatus = _RuckusSCGAPConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 16),
    _RuckusSCGAPConnStatus_Type()
)
ruckusSCGAPConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPConnStatus.setStatus("current")
_RuckusSCGAPRegStatus_Type = DisplayString
_RuckusSCGAPRegStatus_Object = MibTableColumn
ruckusSCGAPRegStatus = _RuckusSCGAPRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 17),
    _RuckusSCGAPRegStatus_Type()
)
ruckusSCGAPRegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPRegStatus.setStatus("current")
_RuckusSCGAPConfigStatus_Type = DisplayString
_RuckusSCGAPConfigStatus_Object = MibTableColumn
ruckusSCGAPConfigStatus = _RuckusSCGAPConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 18),
    _RuckusSCGAPConfigStatus_Type()
)
ruckusSCGAPConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPConfigStatus.setStatus("current")
_RuckusSCGAPLocation_Type = DisplayString
_RuckusSCGAPLocation_Object = MibTableColumn
ruckusSCGAPLocation = _RuckusSCGAPLocation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 19),
    _RuckusSCGAPLocation_Type()
)
ruckusSCGAPLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPLocation.setStatus("current")
_RuckusSCGAPGPSInfo_Type = DisplayString
_RuckusSCGAPGPSInfo_Object = MibTableColumn
ruckusSCGAPGPSInfo = _RuckusSCGAPGPSInfo_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 20),
    _RuckusSCGAPGPSInfo_Type()
)
ruckusSCGAPGPSInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPGPSInfo.setStatus("current")
_RuckusSCGAPMeshRole_Type = DisplayString
_RuckusSCGAPMeshRole_Object = MibTableColumn
ruckusSCGAPMeshRole = _RuckusSCGAPMeshRole_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 21),
    _RuckusSCGAPMeshRole_Type()
)
ruckusSCGAPMeshRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPMeshRole.setStatus("current")
_RuckusSCGAPDescription_Type = DisplayString
_RuckusSCGAPDescription_Object = MibTableColumn
ruckusSCGAPDescription = _RuckusSCGAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 22),
    _RuckusSCGAPDescription_Type()
)
ruckusSCGAPDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPDescription.setStatus("current")
_RuckusSCGAPRXBytes_Type = Counter64
_RuckusSCGAPRXBytes_Object = MibTableColumn
ruckusSCGAPRXBytes = _RuckusSCGAPRXBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 30),
    _RuckusSCGAPRXBytes_Type()
)
ruckusSCGAPRXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPRXBytes.setStatus("current")
_RuckusSCGAPTXBytes_Type = Counter64
_RuckusSCGAPTXBytes_Object = MibTableColumn
ruckusSCGAPTXBytes = _RuckusSCGAPTXBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 31),
    _RuckusSCGAPTXBytes_Type()
)
ruckusSCGAPTXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPTXBytes.setStatus("current")
_RuckusSCGAPIpsecSessionTime_Type = Unsigned32
_RuckusSCGAPIpsecSessionTime_Object = MibTableColumn
ruckusSCGAPIpsecSessionTime = _RuckusSCGAPIpsecSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 50),
    _RuckusSCGAPIpsecSessionTime_Type()
)
ruckusSCGAPIpsecSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPIpsecSessionTime.setStatus("current")
_RuckusSCGAPIpsecTXPkts_Type = Counter64
_RuckusSCGAPIpsecTXPkts_Object = MibTableColumn
ruckusSCGAPIpsecTXPkts = _RuckusSCGAPIpsecTXPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 55),
    _RuckusSCGAPIpsecTXPkts_Type()
)
ruckusSCGAPIpsecTXPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPIpsecTXPkts.setStatus("current")
_RuckusSCGAPIpsecRXPkts_Type = Counter64
_RuckusSCGAPIpsecRXPkts_Object = MibTableColumn
ruckusSCGAPIpsecRXPkts = _RuckusSCGAPIpsecRXPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 56),
    _RuckusSCGAPIpsecRXPkts_Type()
)
ruckusSCGAPIpsecRXPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPIpsecRXPkts.setStatus("current")
_RuckusSCGAPIpsecTXBytes_Type = Counter64
_RuckusSCGAPIpsecTXBytes_Object = MibTableColumn
ruckusSCGAPIpsecTXBytes = _RuckusSCGAPIpsecTXBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 57),
    _RuckusSCGAPIpsecTXBytes_Type()
)
ruckusSCGAPIpsecTXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPIpsecTXBytes.setStatus("current")
_RuckusSCGAPIpsecRXBytes_Type = Counter64
_RuckusSCGAPIpsecRXBytes_Object = MibTableColumn
ruckusSCGAPIpsecRXBytes = _RuckusSCGAPIpsecRXBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 58),
    _RuckusSCGAPIpsecRXBytes_Type()
)
ruckusSCGAPIpsecRXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPIpsecRXBytes.setStatus("current")
_RuckusSCGAPIpsecTXPktsDropped_Type = Counter64
_RuckusSCGAPIpsecTXPktsDropped_Object = MibTableColumn
ruckusSCGAPIpsecTXPktsDropped = _RuckusSCGAPIpsecTXPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 59),
    _RuckusSCGAPIpsecTXPktsDropped_Type()
)
ruckusSCGAPIpsecTXPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPIpsecTXPktsDropped.setStatus("current")
_RuckusSCGAPIpsecRXPktsDropped_Type = Counter64
_RuckusSCGAPIpsecRXPktsDropped_Object = MibTableColumn
ruckusSCGAPIpsecRXPktsDropped = _RuckusSCGAPIpsecRXPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 60),
    _RuckusSCGAPIpsecRXPktsDropped_Type()
)
ruckusSCGAPIpsecRXPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPIpsecRXPktsDropped.setStatus("current")
_RuckusSCGAPIpsecTXIdleTime_Type = Unsigned32
_RuckusSCGAPIpsecTXIdleTime_Object = MibTableColumn
ruckusSCGAPIpsecTXIdleTime = _RuckusSCGAPIpsecTXIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 65),
    _RuckusSCGAPIpsecTXIdleTime_Type()
)
ruckusSCGAPIpsecTXIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPIpsecTXIdleTime.setStatus("current")
_RuckusSCGAPIpsecRXIdleTime_Type = Unsigned32
_RuckusSCGAPIpsecRXIdleTime_Object = MibTableColumn
ruckusSCGAPIpsecRXIdleTime = _RuckusSCGAPIpsecRXIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 66),
    _RuckusSCGAPIpsecRXIdleTime_Type()
)
ruckusSCGAPIpsecRXIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPIpsecRXIdleTime.setStatus("current")
_RuckusSCGAPIPV6Addr_Type = Ipv6Address
_RuckusSCGAPIPV6Addr_Object = MibTableColumn
ruckusSCGAPIPV6Addr = _RuckusSCGAPIPV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 2, 1, 150),
    _RuckusSCGAPIPV6Addr_Type()
)
ruckusSCGAPIPV6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGAPIPV6Addr.setStatus("current")
_RuckusSCGWLANAPSoftGREStatsTable_Object = MibTable
ruckusSCGWLANAPSoftGREStatsTable = _RuckusSCGWLANAPSoftGREStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGREStatsTable.setStatus("current")
_RuckusSCGWLANAPSoftGREStatsEntry_Object = MibTableRow
ruckusSCGWLANAPSoftGREStatsEntry = _RuckusSCGWLANAPSoftGREStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1)
)
ruckusSCGWLANAPSoftGREStatsEntry.setIndexNames(
    (0, "RUCKUS-SCG-WLAN-MIB", "ruckusSCGWLANAPSoftGREMacAddr"),
    (0, "RUCKUS-SCG-WLAN-MIB", "ruckusSCGWLANAPSoftGREIndex"),
)
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGREStatsEntry.setStatus("current")
_RuckusSCGWLANAPSoftGREMacAddr_Type = MacAddress
_RuckusSCGWLANAPSoftGREMacAddr_Object = MibTableColumn
ruckusSCGWLANAPSoftGREMacAddr = _RuckusSCGWLANAPSoftGREMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 1),
    _RuckusSCGWLANAPSoftGREMacAddr_Type()
)
ruckusSCGWLANAPSoftGREMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGREMacAddr.setStatus("current")
_RuckusSCGWLANAPSoftGREIndex_Type = Unsigned32
_RuckusSCGWLANAPSoftGREIndex_Object = MibTableColumn
ruckusSCGWLANAPSoftGREIndex = _RuckusSCGWLANAPSoftGREIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 2),
    _RuckusSCGWLANAPSoftGREIndex_Type()
)
ruckusSCGWLANAPSoftGREIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGREIndex.setStatus("current")
_RuckusSCGWLANAPSoftGREGWAddr_Type = DisplayString
_RuckusSCGWLANAPSoftGREGWAddr_Object = MibTableColumn
ruckusSCGWLANAPSoftGREGWAddr = _RuckusSCGWLANAPSoftGREGWAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 3),
    _RuckusSCGWLANAPSoftGREGWAddr_Type()
)
ruckusSCGWLANAPSoftGREGWAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGREGWAddr.setStatus("current")
_RuckusSCGWLANAPSoftGREActive_Type = Unsigned32
_RuckusSCGWLANAPSoftGREActive_Object = MibTableColumn
ruckusSCGWLANAPSoftGREActive = _RuckusSCGWLANAPSoftGREActive_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 4),
    _RuckusSCGWLANAPSoftGREActive_Type()
)
ruckusSCGWLANAPSoftGREActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGREActive.setStatus("current")
_RuckusSCGWLANAPSoftGRETxPkts_Type = Counter64
_RuckusSCGWLANAPSoftGRETxPkts_Object = MibTableColumn
ruckusSCGWLANAPSoftGRETxPkts = _RuckusSCGWLANAPSoftGRETxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 5),
    _RuckusSCGWLANAPSoftGRETxPkts_Type()
)
ruckusSCGWLANAPSoftGRETxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGRETxPkts.setStatus("current")
_RuckusSCGWLANAPSoftGRETxBytes_Type = Counter64
_RuckusSCGWLANAPSoftGRETxBytes_Object = MibTableColumn
ruckusSCGWLANAPSoftGRETxBytes = _RuckusSCGWLANAPSoftGRETxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 6),
    _RuckusSCGWLANAPSoftGRETxBytes_Type()
)
ruckusSCGWLANAPSoftGRETxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGRETxBytes.setStatus("current")
_RuckusSCGWLANAPSoftGRERxPkts_Type = Counter64
_RuckusSCGWLANAPSoftGRERxPkts_Object = MibTableColumn
ruckusSCGWLANAPSoftGRERxPkts = _RuckusSCGWLANAPSoftGRERxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 7),
    _RuckusSCGWLANAPSoftGRERxPkts_Type()
)
ruckusSCGWLANAPSoftGRERxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGRERxPkts.setStatus("current")
_RuckusSCGWLANAPSoftGRERxBytes_Type = Counter64
_RuckusSCGWLANAPSoftGRERxBytes_Object = MibTableColumn
ruckusSCGWLANAPSoftGRERxBytes = _RuckusSCGWLANAPSoftGRERxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 8),
    _RuckusSCGWLANAPSoftGRERxBytes_Type()
)
ruckusSCGWLANAPSoftGRERxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGRERxBytes.setStatus("current")
_RuckusSCGWLANAPSoftGRETxPktsErr_Type = Counter64
_RuckusSCGWLANAPSoftGRETxPktsErr_Object = MibTableColumn
ruckusSCGWLANAPSoftGRETxPktsErr = _RuckusSCGWLANAPSoftGRETxPktsErr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 9),
    _RuckusSCGWLANAPSoftGRETxPktsErr_Type()
)
ruckusSCGWLANAPSoftGRETxPktsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGRETxPktsErr.setStatus("current")
_RuckusSCGWLANAPSoftGRERxPktsErr_Type = Counter64
_RuckusSCGWLANAPSoftGRERxPktsErr_Object = MibTableColumn
ruckusSCGWLANAPSoftGRERxPktsErr = _RuckusSCGWLANAPSoftGRERxPktsErr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 10),
    _RuckusSCGWLANAPSoftGRERxPktsErr_Type()
)
ruckusSCGWLANAPSoftGRERxPktsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGRERxPktsErr.setStatus("current")
_RuckusSCGWLANAPSoftGRETxPktsDropped_Type = Counter64
_RuckusSCGWLANAPSoftGRETxPktsDropped_Object = MibTableColumn
ruckusSCGWLANAPSoftGRETxPktsDropped = _RuckusSCGWLANAPSoftGRETxPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 11),
    _RuckusSCGWLANAPSoftGRETxPktsDropped_Type()
)
ruckusSCGWLANAPSoftGRETxPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGRETxPktsDropped.setStatus("current")
_RuckusSCGWLANAPSoftGRERxPktsDropped_Type = Counter64
_RuckusSCGWLANAPSoftGRERxPktsDropped_Object = MibTableColumn
ruckusSCGWLANAPSoftGRERxPktsDropped = _RuckusSCGWLANAPSoftGRERxPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 12),
    _RuckusSCGWLANAPSoftGRERxPktsDropped_Type()
)
ruckusSCGWLANAPSoftGRERxPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGRERxPktsDropped.setStatus("current")
_RuckusSCGWLANAPSoftGRETxPktsFrag_Type = Counter64
_RuckusSCGWLANAPSoftGRETxPktsFrag_Object = MibTableColumn
ruckusSCGWLANAPSoftGRETxPktsFrag = _RuckusSCGWLANAPSoftGRETxPktsFrag_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 13),
    _RuckusSCGWLANAPSoftGRETxPktsFrag_Type()
)
ruckusSCGWLANAPSoftGRETxPktsFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGRETxPktsFrag.setStatus("current")
_RuckusSCGWLANAPSoftGREICMPTotal_Type = Counter64
_RuckusSCGWLANAPSoftGREICMPTotal_Object = MibTableColumn
ruckusSCGWLANAPSoftGREICMPTotal = _RuckusSCGWLANAPSoftGREICMPTotal_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 14),
    _RuckusSCGWLANAPSoftGREICMPTotal_Type()
)
ruckusSCGWLANAPSoftGREICMPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGREICMPTotal.setStatus("current")
_RuckusSCGWLANAPSoftGREICMPNoReply_Type = Counter64
_RuckusSCGWLANAPSoftGREICMPNoReply_Object = MibTableColumn
ruckusSCGWLANAPSoftGREICMPNoReply = _RuckusSCGWLANAPSoftGREICMPNoReply_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 15),
    _RuckusSCGWLANAPSoftGREICMPNoReply_Type()
)
ruckusSCGWLANAPSoftGREICMPNoReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGREICMPNoReply.setStatus("current")
_RuckusSCGWLANAPSoftGREDisconnect_Type = Counter64
_RuckusSCGWLANAPSoftGREDisconnect_Object = MibTableColumn
ruckusSCGWLANAPSoftGREDisconnect = _RuckusSCGWLANAPSoftGREDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 2, 1, 1, 2, 3, 1, 16),
    _RuckusSCGWLANAPSoftGREDisconnect_Type()
)
ruckusSCGWLANAPSoftGREDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSCGWLANAPSoftGREDisconnect.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-SCG-WLAN-MIB",
    **{"ruckusWLANMIB": ruckusWLANMIB,
       "ruckusWLANObjects": ruckusWLANObjects,
       "ruckusWLANInfo": ruckusWLANInfo,
       "ruckusWLANTable": ruckusWLANTable,
       "ruckusWLANEntry": ruckusWLANEntry,
       "ruckusWLANSSID": ruckusWLANSSID,
       "ruckusWLANNumSta": ruckusWLANNumSta,
       "ruckusWLANRxBytes": ruckusWLANRxBytes,
       "ruckusWLANTxBytes": ruckusWLANTxBytes,
       "ruckusWLANIndex": ruckusWLANIndex,
       "ruckusSCGWLANTable": ruckusSCGWLANTable,
       "ruckusSCGWLANEntry": ruckusSCGWLANEntry,
       "ruckusSCGWLANSSID": ruckusSCGWLANSSID,
       "ruckusSCGWLANZone": ruckusSCGWLANZone,
       "ruckusSCGWLANDomain": ruckusSCGWLANDomain,
       "ruckusSCGWLANNumSta": ruckusSCGWLANNumSta,
       "ruckusSCGWLANRxBytes": ruckusSCGWLANRxBytes,
       "ruckusSCGWLANTxBytes": ruckusSCGWLANTxBytes,
       "ruckusSCGWLANAuthType": ruckusSCGWLANAuthType,
       "ruckusSCGWLANIndex": ruckusSCGWLANIndex,
       "ruckusWLANAPInfo": ruckusWLANAPInfo,
       "ruckusWLANAPTable": ruckusWLANAPTable,
       "ruckusWLANAPEntry": ruckusWLANAPEntry,
       "ruckusWLANAPMacAddr": ruckusWLANAPMacAddr,
       "ruckusWLANAPUptime": ruckusWLANAPUptime,
       "ruckusWLANAPSWversion": ruckusWLANAPSWversion,
       "ruckusWLANAPIPAddr": ruckusWLANAPIPAddr,
       "ruckusWLANAPNumSta": ruckusWLANAPNumSta,
       "ruckusSCGAPTable": ruckusSCGAPTable,
       "ruckusSCGAPEntry": ruckusSCGAPEntry,
       "ruckusSCGAPMac": ruckusSCGAPMac,
       "ruckusSCGAPGroup": ruckusSCGAPGroup,
       "ruckusSCGAPZone": ruckusSCGAPZone,
       "ruckusSCGAPDomain": ruckusSCGAPDomain,
       "ruckusSCGAPName": ruckusSCGAPName,
       "ruckusSCGAPUptime": ruckusSCGAPUptime,
       "ruckusSCGAPFWversion": ruckusSCGAPFWversion,
       "ruckusSCGAPModel": ruckusSCGAPModel,
       "ruckusSCGAPSerial": ruckusSCGAPSerial,
       "ruckusSCGAPIp": ruckusSCGAPIp,
       "ruckusSCGAPIPType": ruckusSCGAPIPType,
       "ruckusSCGAPExtIp": ruckusSCGAPExtIp,
       "ruckusSCGAPExtPort": ruckusSCGAPExtPort,
       "ruckusSCGAPNumSta": ruckusSCGAPNumSta,
       "ruckusSCGAPConnStatus": ruckusSCGAPConnStatus,
       "ruckusSCGAPRegStatus": ruckusSCGAPRegStatus,
       "ruckusSCGAPConfigStatus": ruckusSCGAPConfigStatus,
       "ruckusSCGAPLocation": ruckusSCGAPLocation,
       "ruckusSCGAPGPSInfo": ruckusSCGAPGPSInfo,
       "ruckusSCGAPMeshRole": ruckusSCGAPMeshRole,
       "ruckusSCGAPDescription": ruckusSCGAPDescription,
       "ruckusSCGAPRXBytes": ruckusSCGAPRXBytes,
       "ruckusSCGAPTXBytes": ruckusSCGAPTXBytes,
       "ruckusSCGAPIpsecSessionTime": ruckusSCGAPIpsecSessionTime,
       "ruckusSCGAPIpsecTXPkts": ruckusSCGAPIpsecTXPkts,
       "ruckusSCGAPIpsecRXPkts": ruckusSCGAPIpsecRXPkts,
       "ruckusSCGAPIpsecTXBytes": ruckusSCGAPIpsecTXBytes,
       "ruckusSCGAPIpsecRXBytes": ruckusSCGAPIpsecRXBytes,
       "ruckusSCGAPIpsecTXPktsDropped": ruckusSCGAPIpsecTXPktsDropped,
       "ruckusSCGAPIpsecRXPktsDropped": ruckusSCGAPIpsecRXPktsDropped,
       "ruckusSCGAPIpsecTXIdleTime": ruckusSCGAPIpsecTXIdleTime,
       "ruckusSCGAPIpsecRXIdleTime": ruckusSCGAPIpsecRXIdleTime,
       "ruckusSCGAPIPV6Addr": ruckusSCGAPIPV6Addr,
       "ruckusSCGWLANAPSoftGREStatsTable": ruckusSCGWLANAPSoftGREStatsTable,
       "ruckusSCGWLANAPSoftGREStatsEntry": ruckusSCGWLANAPSoftGREStatsEntry,
       "ruckusSCGWLANAPSoftGREMacAddr": ruckusSCGWLANAPSoftGREMacAddr,
       "ruckusSCGWLANAPSoftGREIndex": ruckusSCGWLANAPSoftGREIndex,
       "ruckusSCGWLANAPSoftGREGWAddr": ruckusSCGWLANAPSoftGREGWAddr,
       "ruckusSCGWLANAPSoftGREActive": ruckusSCGWLANAPSoftGREActive,
       "ruckusSCGWLANAPSoftGRETxPkts": ruckusSCGWLANAPSoftGRETxPkts,
       "ruckusSCGWLANAPSoftGRETxBytes": ruckusSCGWLANAPSoftGRETxBytes,
       "ruckusSCGWLANAPSoftGRERxPkts": ruckusSCGWLANAPSoftGRERxPkts,
       "ruckusSCGWLANAPSoftGRERxBytes": ruckusSCGWLANAPSoftGRERxBytes,
       "ruckusSCGWLANAPSoftGRETxPktsErr": ruckusSCGWLANAPSoftGRETxPktsErr,
       "ruckusSCGWLANAPSoftGRERxPktsErr": ruckusSCGWLANAPSoftGRERxPktsErr,
       "ruckusSCGWLANAPSoftGRETxPktsDropped": ruckusSCGWLANAPSoftGRETxPktsDropped,
       "ruckusSCGWLANAPSoftGRERxPktsDropped": ruckusSCGWLANAPSoftGRERxPktsDropped,
       "ruckusSCGWLANAPSoftGRETxPktsFrag": ruckusSCGWLANAPSoftGRETxPktsFrag,
       "ruckusSCGWLANAPSoftGREICMPTotal": ruckusSCGWLANAPSoftGREICMPTotal,
       "ruckusSCGWLANAPSoftGREICMPNoReply": ruckusSCGWLANAPSoftGREICMPNoReply,
       "ruckusSCGWLANAPSoftGREDisconnect": ruckusSCGWLANAPSoftGREDisconnect}
)
