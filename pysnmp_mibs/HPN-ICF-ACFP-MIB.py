# SNMP MIB module (HPN-ICF-ACFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-ACFP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:33:27 2025
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(InetAddressPrefixLength,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressPrefixLength")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

hpnicfAcfp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74)
)
if mibBuilder.loadTexts:
    hpnicfAcfp.setRevisions(
        ("2006-07-04 19:36",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfAcfpObjects_ObjectIdentity = ObjectIdentity
hpnicfAcfpObjects = _HpnicfAcfpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1)
)
_HpnicfAcfpOAP_ObjectIdentity = ObjectIdentity
hpnicfAcfpOAP = _HpnicfAcfpOAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1)
)
_HpnicfAcfpServer_ObjectIdentity = ObjectIdentity
hpnicfAcfpServer = _HpnicfAcfpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 1)
)


class _HpnicfAcfpServerInfo_Type(Bits):
    """Custom type hpnicfAcfpServerInfo based on Bits"""
    namedValues = NamedValues(
        *(("ipserver", 0),
          ("redirect", 1),
          ("mirror", 2),
          ("passThrough", 3))
    )

_HpnicfAcfpServerInfo_Type.__name__ = "Bits"
_HpnicfAcfpServerInfo_Object = MibScalar
hpnicfAcfpServerInfo = _HpnicfAcfpServerInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 1, 1),
    _HpnicfAcfpServerInfo_Type()
)
hpnicfAcfpServerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAcfpServerInfo.setStatus("current")


class _HpnicfAcfpServerMaxLifetime_Type(Integer32):
    """Custom type hpnicfAcfpServerMaxLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfAcfpServerMaxLifetime_Type.__name__ = "Integer32"
_HpnicfAcfpServerMaxLifetime_Object = MibScalar
hpnicfAcfpServerMaxLifetime = _HpnicfAcfpServerMaxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 1, 2),
    _HpnicfAcfpServerMaxLifetime_Type()
)
hpnicfAcfpServerMaxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAcfpServerMaxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfAcfpServerMaxLifetime.setUnits("seconds")
_HpnicfAcfpServerPersistentRules_Type = TruthValue
_HpnicfAcfpServerPersistentRules_Object = MibScalar
hpnicfAcfpServerPersistentRules = _HpnicfAcfpServerPersistentRules_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 1, 3),
    _HpnicfAcfpServerPersistentRules_Type()
)
hpnicfAcfpServerPersistentRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAcfpServerPersistentRules.setStatus("current")


class _HpnicfAcfpServerCurContextType_Type(Integer32):
    """Custom type hpnicfAcfpServerCurContextType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("no-context", 1),
          ("context-VLANID", 2),
          ("context-HG", 3),
          ("context-FlowID", 4),
          ("context-HGPlus", 5))
    )


_HpnicfAcfpServerCurContextType_Type.__name__ = "Integer32"
_HpnicfAcfpServerCurContextType_Object = MibScalar
hpnicfAcfpServerCurContextType = _HpnicfAcfpServerCurContextType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 1, 4),
    _HpnicfAcfpServerCurContextType_Type()
)
hpnicfAcfpServerCurContextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAcfpServerCurContextType.setStatus("current")
_HpnicfAcfpClientInfo_ObjectIdentity = ObjectIdentity
hpnicfAcfpClientInfo = _HpnicfAcfpClientInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 2)
)
_HpnicfAcfpClientInfoTable_Object = MibTable
hpnicfAcfpClientInfoTable = _HpnicfAcfpClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfAcfpClientInfoTable.setStatus("current")
_HpnicfAcfpClientInfoEntry_Object = MibTableRow
hpnicfAcfpClientInfoEntry = _HpnicfAcfpClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 2, 1, 1)
)
hpnicfAcfpClientInfoEntry.setIndexNames(
    (0, "HPN-ICF-ACFP-MIB", "hpnicfAcfpClientID"),
)
if mibBuilder.loadTexts:
    hpnicfAcfpClientInfoEntry.setStatus("current")


class _HpnicfAcfpClientID_Type(Integer32):
    """Custom type hpnicfAcfpClientID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfAcfpClientID_Type.__name__ = "Integer32"
_HpnicfAcfpClientID_Object = MibTableColumn
hpnicfAcfpClientID = _HpnicfAcfpClientID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 2, 1, 1, 1),
    _HpnicfAcfpClientID_Type()
)
hpnicfAcfpClientID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAcfpClientID.setStatus("current")


class _HpnicfAcfpClientDescription_Type(DisplayString):
    """Custom type hpnicfAcfpClientDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfAcfpClientDescription_Type.__name__ = "DisplayString"
_HpnicfAcfpClientDescription_Object = MibTableColumn
hpnicfAcfpClientDescription = _HpnicfAcfpClientDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 2, 1, 1, 2),
    _HpnicfAcfpClientDescription_Type()
)
hpnicfAcfpClientDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpClientDescription.setStatus("current")


class _HpnicfAcfpClientHwVersion_Type(DisplayString):
    """Custom type hpnicfAcfpClientHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfAcfpClientHwVersion_Type.__name__ = "DisplayString"
_HpnicfAcfpClientHwVersion_Object = MibTableColumn
hpnicfAcfpClientHwVersion = _HpnicfAcfpClientHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 2, 1, 1, 3),
    _HpnicfAcfpClientHwVersion_Type()
)
hpnicfAcfpClientHwVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpClientHwVersion.setStatus("current")


class _HpnicfAcfpClientOSVersion_Type(DisplayString):
    """Custom type hpnicfAcfpClientOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfAcfpClientOSVersion_Type.__name__ = "DisplayString"
_HpnicfAcfpClientOSVersion_Object = MibTableColumn
hpnicfAcfpClientOSVersion = _HpnicfAcfpClientOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 2, 1, 1, 4),
    _HpnicfAcfpClientOSVersion_Type()
)
hpnicfAcfpClientOSVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpClientOSVersion.setStatus("current")


class _HpnicfAcfpClientAppVersion_Type(DisplayString):
    """Custom type hpnicfAcfpClientAppVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfAcfpClientAppVersion_Type.__name__ = "DisplayString"
_HpnicfAcfpClientAppVersion_Object = MibTableColumn
hpnicfAcfpClientAppVersion = _HpnicfAcfpClientAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 2, 1, 1, 5),
    _HpnicfAcfpClientAppVersion_Type()
)
hpnicfAcfpClientAppVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpClientAppVersion.setStatus("current")
_HpnicfAcfpClientIP_Type = IpAddress
_HpnicfAcfpClientIP_Object = MibTableColumn
hpnicfAcfpClientIP = _HpnicfAcfpClientIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 2, 1, 1, 6),
    _HpnicfAcfpClientIP_Type()
)
hpnicfAcfpClientIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpClientIP.setStatus("current")


class _HpnicfAcfpClientMode_Type(Bits):
    """Custom type hpnicfAcfpClientMode based on Bits"""
    defaultHexValue = ""

    namedValues = NamedValues(
        *(("ipserver", 0),
          ("redirect", 1),
          ("mirror", 2),
          ("passThrough", 3))
    )

_HpnicfAcfpClientMode_Type.__name__ = "Bits"
_HpnicfAcfpClientMode_Object = MibTableColumn
hpnicfAcfpClientMode = _HpnicfAcfpClientMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 2, 1, 1, 7),
    _HpnicfAcfpClientMode_Type()
)
hpnicfAcfpClientMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpClientMode.setStatus("current")
_HpnicfAcfpClientRowStatus_Type = RowStatus
_HpnicfAcfpClientRowStatus_Object = MibTableColumn
hpnicfAcfpClientRowStatus = _HpnicfAcfpClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 2, 1, 1, 8),
    _HpnicfAcfpClientRowStatus_Type()
)
hpnicfAcfpClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpClientRowStatus.setStatus("current")
_HpnicfAcfpPolicy_ObjectIdentity = ObjectIdentity
hpnicfAcfpPolicy = _HpnicfAcfpPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3)
)
_HpnicfAcfpPolicyTable_Object = MibTable
hpnicfAcfpPolicyTable = _HpnicfAcfpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyTable.setStatus("current")
_HpnicfAcfpPolicyEntry_Object = MibTableRow
hpnicfAcfpPolicyEntry = _HpnicfAcfpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1, 1)
)
hpnicfAcfpPolicyEntry.setIndexNames(
    (0, "HPN-ICF-ACFP-MIB", "hpnicfAcfpClientID"),
    (0, "HPN-ICF-ACFP-MIB", "hpnicfAcfpPolicyIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyEntry.setStatus("current")


class _HpnicfAcfpPolicyIndex_Type(Integer32):
    """Custom type hpnicfAcfpPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfAcfpPolicyIndex_Type.__name__ = "Integer32"
_HpnicfAcfpPolicyIndex_Object = MibTableColumn
hpnicfAcfpPolicyIndex = _HpnicfAcfpPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1, 1, 1),
    _HpnicfAcfpPolicyIndex_Type()
)
hpnicfAcfpPolicyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyIndex.setStatus("current")


class _HpnicfAcfpPolicyInIfIndex_Type(Integer32):
    """Custom type hpnicfAcfpPolicyInIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfAcfpPolicyInIfIndex_Type.__name__ = "Integer32"
_HpnicfAcfpPolicyInIfIndex_Object = MibTableColumn
hpnicfAcfpPolicyInIfIndex = _HpnicfAcfpPolicyInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1, 1, 2),
    _HpnicfAcfpPolicyInIfIndex_Type()
)
hpnicfAcfpPolicyInIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyInIfIndex.setStatus("current")


class _HpnicfAcfpPolicyOutIfIndex_Type(Integer32):
    """Custom type hpnicfAcfpPolicyOutIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfAcfpPolicyOutIfIndex_Type.__name__ = "Integer32"
_HpnicfAcfpPolicyOutIfIndex_Object = MibTableColumn
hpnicfAcfpPolicyOutIfIndex = _HpnicfAcfpPolicyOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1, 1, 3),
    _HpnicfAcfpPolicyOutIfIndex_Type()
)
hpnicfAcfpPolicyOutIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyOutIfIndex.setStatus("current")


class _HpnicfAcfpPolicyDestIfIndex_Type(Integer32):
    """Custom type hpnicfAcfpPolicyDestIfIndex based on Integer32"""
    defaultValue = 0


_HpnicfAcfpPolicyDestIfIndex_Type.__name__ = "Integer32"
_HpnicfAcfpPolicyDestIfIndex_Object = MibTableColumn
hpnicfAcfpPolicyDestIfIndex = _HpnicfAcfpPolicyDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1, 1, 4),
    _HpnicfAcfpPolicyDestIfIndex_Type()
)
hpnicfAcfpPolicyDestIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyDestIfIndex.setStatus("current")


class _HpnicfAcfpPolicyContextID_Type(Integer32):
    """Custom type hpnicfAcfpPolicyContextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfAcfpPolicyContextID_Type.__name__ = "Integer32"
_HpnicfAcfpPolicyContextID_Object = MibTableColumn
hpnicfAcfpPolicyContextID = _HpnicfAcfpPolicyContextID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1, 1, 5),
    _HpnicfAcfpPolicyContextID_Type()
)
hpnicfAcfpPolicyContextID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyContextID.setStatus("current")


class _HpnicfAcfpPolicyAdminStatus_Type(Integer32):
    """Custom type hpnicfAcfpPolicyAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpnicfAcfpPolicyAdminStatus_Type.__name__ = "Integer32"
_HpnicfAcfpPolicyAdminStatus_Object = MibTableColumn
hpnicfAcfpPolicyAdminStatus = _HpnicfAcfpPolicyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1, 1, 6),
    _HpnicfAcfpPolicyAdminStatus_Type()
)
hpnicfAcfpPolicyAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyAdminStatus.setStatus("current")


class _HpnicfAcfpPolicyLifetime_Type(Integer32):
    """Custom type hpnicfAcfpPolicyLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfAcfpPolicyLifetime_Type.__name__ = "Integer32"
_HpnicfAcfpPolicyLifetime_Object = MibTableColumn
hpnicfAcfpPolicyLifetime = _HpnicfAcfpPolicyLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1, 1, 7),
    _HpnicfAcfpPolicyLifetime_Type()
)
hpnicfAcfpPolicyLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyLifetime.setUnits("seconds")


class _HpnicfAcfpPolicyTimeStart_Type(OctetString):
    """Custom type hpnicfAcfpPolicyTimeStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_HpnicfAcfpPolicyTimeStart_Type.__name__ = "OctetString"
_HpnicfAcfpPolicyTimeStart_Object = MibTableColumn
hpnicfAcfpPolicyTimeStart = _HpnicfAcfpPolicyTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1, 1, 8),
    _HpnicfAcfpPolicyTimeStart_Type()
)
hpnicfAcfpPolicyTimeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyTimeStart.setStatus("current")


class _HpnicfAcfpPolicyTimeEnd_Type(OctetString):
    """Custom type hpnicfAcfpPolicyTimeEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_HpnicfAcfpPolicyTimeEnd_Type.__name__ = "OctetString"
_HpnicfAcfpPolicyTimeEnd_Object = MibTableColumn
hpnicfAcfpPolicyTimeEnd = _HpnicfAcfpPolicyTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1, 1, 9),
    _HpnicfAcfpPolicyTimeEnd_Type()
)
hpnicfAcfpPolicyTimeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyTimeEnd.setStatus("current")
_HpnicfAcfpPolicyRowStatus_Type = RowStatus
_HpnicfAcfpPolicyRowStatus_Object = MibTableColumn
hpnicfAcfpPolicyRowStatus = _HpnicfAcfpPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1, 1, 10),
    _HpnicfAcfpPolicyRowStatus_Type()
)
hpnicfAcfpPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyRowStatus.setStatus("current")


class _HpnicfAcfpPolicyDestIfFailAction_Type(Integer32):
    """Custom type hpnicfAcfpPolicyDestIfFailAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("reserve", 2))
    )


_HpnicfAcfpPolicyDestIfFailAction_Type.__name__ = "Integer32"
_HpnicfAcfpPolicyDestIfFailAction_Object = MibTableColumn
hpnicfAcfpPolicyDestIfFailAction = _HpnicfAcfpPolicyDestIfFailAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1, 1, 11),
    _HpnicfAcfpPolicyDestIfFailAction_Type()
)
hpnicfAcfpPolicyDestIfFailAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyDestIfFailAction.setStatus("current")


class _HpnicfAcfpPolicyPriority_Type(Integer32):
    """Custom type hpnicfAcfpPolicyPriority based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7),
          ("priority8", 8))
    )


_HpnicfAcfpPolicyPriority_Type.__name__ = "Integer32"
_HpnicfAcfpPolicyPriority_Object = MibTableColumn
hpnicfAcfpPolicyPriority = _HpnicfAcfpPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 3, 1, 1, 12),
    _HpnicfAcfpPolicyPriority_Type()
)
hpnicfAcfpPolicyPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpPolicyPriority.setStatus("current")
_HpnicfAcfpRule_ObjectIdentity = ObjectIdentity
hpnicfAcfpRule = _HpnicfAcfpRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4)
)
_HpnicfAcfpRuleTable_Object = MibTable
hpnicfAcfpRuleTable = _HpnicfAcfpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfAcfpRuleTable.setStatus("current")
_HpnicfAcfpRuleEntry_Object = MibTableRow
hpnicfAcfpRuleEntry = _HpnicfAcfpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1)
)
hpnicfAcfpRuleEntry.setIndexNames(
    (0, "HPN-ICF-ACFP-MIB", "hpnicfAcfpClientID"),
    (0, "HPN-ICF-ACFP-MIB", "hpnicfAcfpPolicyIndex"),
    (0, "HPN-ICF-ACFP-MIB", "hpnicfAcfpRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAcfpRuleEntry.setStatus("current")


class _HpnicfAcfpRuleIndex_Type(Integer32):
    """Custom type hpnicfAcfpRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfAcfpRuleIndex_Type.__name__ = "Integer32"
_HpnicfAcfpRuleIndex_Object = MibTableColumn
hpnicfAcfpRuleIndex = _HpnicfAcfpRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 1),
    _HpnicfAcfpRuleIndex_Type()
)
hpnicfAcfpRuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleIndex.setStatus("current")


class _HpnicfAcfpRuleOperStatus_Type(Integer32):
    """Custom type hpnicfAcfpRuleOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("fail", 2))
    )


_HpnicfAcfpRuleOperStatus_Type.__name__ = "Integer32"
_HpnicfAcfpRuleOperStatus_Object = MibTableColumn
hpnicfAcfpRuleOperStatus = _HpnicfAcfpRuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 2),
    _HpnicfAcfpRuleOperStatus_Type()
)
hpnicfAcfpRuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleOperStatus.setStatus("current")


class _HpnicfAcfpRuleAction_Type(Integer32):
    """Custom type hpnicfAcfpRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2),
          ("redirect", 3),
          ("mirror", 4),
          ("rate", 5))
    )


_HpnicfAcfpRuleAction_Type.__name__ = "Integer32"
_HpnicfAcfpRuleAction_Object = MibTableColumn
hpnicfAcfpRuleAction = _HpnicfAcfpRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 3),
    _HpnicfAcfpRuleAction_Type()
)
hpnicfAcfpRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleAction.setStatus("current")


class _HpnicfAcfpRuleAll_Type(TruthValue):
    """Custom type hpnicfAcfpRuleAll based on TruthValue"""
    defaultValue = 2


_HpnicfAcfpRuleAll_Type.__name__ = "TruthValue"
_HpnicfAcfpRuleAll_Object = MibTableColumn
hpnicfAcfpRuleAll = _HpnicfAcfpRuleAll_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 4),
    _HpnicfAcfpRuleAll_Type()
)
hpnicfAcfpRuleAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleAll.setStatus("current")
_HpnicfAcfpRuleSrcMAC_Type = MacAddress
_HpnicfAcfpRuleSrcMAC_Object = MibTableColumn
hpnicfAcfpRuleSrcMAC = _HpnicfAcfpRuleSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 5),
    _HpnicfAcfpRuleSrcMAC_Type()
)
hpnicfAcfpRuleSrcMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleSrcMAC.setStatus("current")
_HpnicfAcfpRuleDstMAC_Type = MacAddress
_HpnicfAcfpRuleDstMAC_Object = MibTableColumn
hpnicfAcfpRuleDstMAC = _HpnicfAcfpRuleDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 6),
    _HpnicfAcfpRuleDstMAC_Type()
)
hpnicfAcfpRuleDstMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleDstMAC.setStatus("current")


class _HpnicfAcfpRuleVlanStart_Type(Integer32):
    """Custom type hpnicfAcfpRuleVlanStart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfAcfpRuleVlanStart_Type.__name__ = "Integer32"
_HpnicfAcfpRuleVlanStart_Object = MibTableColumn
hpnicfAcfpRuleVlanStart = _HpnicfAcfpRuleVlanStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 7),
    _HpnicfAcfpRuleVlanStart_Type()
)
hpnicfAcfpRuleVlanStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleVlanStart.setStatus("current")


class _HpnicfAcfpRuleVlanEnd_Type(Integer32):
    """Custom type hpnicfAcfpRuleVlanEnd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfAcfpRuleVlanEnd_Type.__name__ = "Integer32"
_HpnicfAcfpRuleVlanEnd_Object = MibTableColumn
hpnicfAcfpRuleVlanEnd = _HpnicfAcfpRuleVlanEnd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 8),
    _HpnicfAcfpRuleVlanEnd_Type()
)
hpnicfAcfpRuleVlanEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleVlanEnd.setStatus("current")


class _HpnicfAcfpRuleProtocol_Type(Integer32):
    """Custom type hpnicfAcfpRuleProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfAcfpRuleProtocol_Type.__name__ = "Integer32"
_HpnicfAcfpRuleProtocol_Object = MibTableColumn
hpnicfAcfpRuleProtocol = _HpnicfAcfpRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 9),
    _HpnicfAcfpRuleProtocol_Type()
)
hpnicfAcfpRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleProtocol.setStatus("current")
_HpnicfAcfpRuleSrcIP_Type = IpAddress
_HpnicfAcfpRuleSrcIP_Object = MibTableColumn
hpnicfAcfpRuleSrcIP = _HpnicfAcfpRuleSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 10),
    _HpnicfAcfpRuleSrcIP_Type()
)
hpnicfAcfpRuleSrcIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleSrcIP.setStatus("current")
_HpnicfAcfpRuleSrcIPMask_Type = IpAddress
_HpnicfAcfpRuleSrcIPMask_Object = MibTableColumn
hpnicfAcfpRuleSrcIPMask = _HpnicfAcfpRuleSrcIPMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 11),
    _HpnicfAcfpRuleSrcIPMask_Type()
)
hpnicfAcfpRuleSrcIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleSrcIPMask.setStatus("current")


class _HpnicfAcfpRuleSrcOp_Type(Integer32):
    """Custom type hpnicfAcfpRuleSrcOp based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("notEqual", 2),
          ("lessThan", 3),
          ("greaterThan", 4),
          ("range", 5),
          ("invalid", 6))
    )


_HpnicfAcfpRuleSrcOp_Type.__name__ = "Integer32"
_HpnicfAcfpRuleSrcOp_Object = MibTableColumn
hpnicfAcfpRuleSrcOp = _HpnicfAcfpRuleSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 12),
    _HpnicfAcfpRuleSrcOp_Type()
)
hpnicfAcfpRuleSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleSrcOp.setStatus("current")


class _HpnicfAcfpRuleSrcStartPort_Type(Integer32):
    """Custom type hpnicfAcfpRuleSrcStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAcfpRuleSrcStartPort_Type.__name__ = "Integer32"
_HpnicfAcfpRuleSrcStartPort_Object = MibTableColumn
hpnicfAcfpRuleSrcStartPort = _HpnicfAcfpRuleSrcStartPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 13),
    _HpnicfAcfpRuleSrcStartPort_Type()
)
hpnicfAcfpRuleSrcStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleSrcStartPort.setStatus("current")


class _HpnicfAcfpRuleSrcEndPort_Type(Integer32):
    """Custom type hpnicfAcfpRuleSrcEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAcfpRuleSrcEndPort_Type.__name__ = "Integer32"
_HpnicfAcfpRuleSrcEndPort_Object = MibTableColumn
hpnicfAcfpRuleSrcEndPort = _HpnicfAcfpRuleSrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 14),
    _HpnicfAcfpRuleSrcEndPort_Type()
)
hpnicfAcfpRuleSrcEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleSrcEndPort.setStatus("current")
_HpnicfAcfpRuleDstIP_Type = IpAddress
_HpnicfAcfpRuleDstIP_Object = MibTableColumn
hpnicfAcfpRuleDstIP = _HpnicfAcfpRuleDstIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 15),
    _HpnicfAcfpRuleDstIP_Type()
)
hpnicfAcfpRuleDstIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleDstIP.setStatus("current")
_HpnicfAcfpRuleDstIPMask_Type = IpAddress
_HpnicfAcfpRuleDstIPMask_Object = MibTableColumn
hpnicfAcfpRuleDstIPMask = _HpnicfAcfpRuleDstIPMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 16),
    _HpnicfAcfpRuleDstIPMask_Type()
)
hpnicfAcfpRuleDstIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleDstIPMask.setStatus("current")


class _HpnicfAcfpRuleDstOp_Type(Integer32):
    """Custom type hpnicfAcfpRuleDstOp based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("nonEqual", 2),
          ("lessThan", 3),
          ("greaterThan", 4),
          ("range", 5),
          ("invalid", 6))
    )


_HpnicfAcfpRuleDstOp_Type.__name__ = "Integer32"
_HpnicfAcfpRuleDstOp_Object = MibTableColumn
hpnicfAcfpRuleDstOp = _HpnicfAcfpRuleDstOp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 17),
    _HpnicfAcfpRuleDstOp_Type()
)
hpnicfAcfpRuleDstOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleDstOp.setStatus("current")


class _HpnicfAcfpRuleDstStartPort_Type(Integer32):
    """Custom type hpnicfAcfpRuleDstStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAcfpRuleDstStartPort_Type.__name__ = "Integer32"
_HpnicfAcfpRuleDstStartPort_Object = MibTableColumn
hpnicfAcfpRuleDstStartPort = _HpnicfAcfpRuleDstStartPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 18),
    _HpnicfAcfpRuleDstStartPort_Type()
)
hpnicfAcfpRuleDstStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleDstStartPort.setStatus("current")


class _HpnicfAcfpRuleDstEndPort_Type(Integer32):
    """Custom type hpnicfAcfpRuleDstEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAcfpRuleDstEndPort_Type.__name__ = "Integer32"
_HpnicfAcfpRuleDstEndPort_Object = MibTableColumn
hpnicfAcfpRuleDstEndPort = _HpnicfAcfpRuleDstEndPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 19),
    _HpnicfAcfpRuleDstEndPort_Type()
)
hpnicfAcfpRuleDstEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleDstEndPort.setStatus("current")


class _HpnicfAcfpRulePrecedence_Type(Integer32):
    """Custom type hpnicfAcfpRulePrecedence based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAcfpRulePrecedence_Type.__name__ = "Integer32"
_HpnicfAcfpRulePrecedence_Object = MibTableColumn
hpnicfAcfpRulePrecedence = _HpnicfAcfpRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 20),
    _HpnicfAcfpRulePrecedence_Type()
)
hpnicfAcfpRulePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRulePrecedence.setStatus("current")


class _HpnicfAcfpRuleTos_Type(Integer32):
    """Custom type hpnicfAcfpRuleTos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAcfpRuleTos_Type.__name__ = "Integer32"
_HpnicfAcfpRuleTos_Object = MibTableColumn
hpnicfAcfpRuleTos = _HpnicfAcfpRuleTos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 21),
    _HpnicfAcfpRuleTos_Type()
)
hpnicfAcfpRuleTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleTos.setStatus("current")


class _HpnicfAcfpRuleDscp_Type(Integer32):
    """Custom type hpnicfAcfpRuleDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfAcfpRuleDscp_Type.__name__ = "Integer32"
_HpnicfAcfpRuleDscp_Object = MibTableColumn
hpnicfAcfpRuleDscp = _HpnicfAcfpRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 22),
    _HpnicfAcfpRuleDscp_Type()
)
hpnicfAcfpRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleDscp.setStatus("current")


class _HpnicfAcfpRuleEstablish_Type(TruthValue):
    """Custom type hpnicfAcfpRuleEstablish based on TruthValue"""
    defaultValue = 2


_HpnicfAcfpRuleEstablish_Type.__name__ = "TruthValue"
_HpnicfAcfpRuleEstablish_Object = MibTableColumn
hpnicfAcfpRuleEstablish = _HpnicfAcfpRuleEstablish_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 23),
    _HpnicfAcfpRuleEstablish_Type()
)
hpnicfAcfpRuleEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleEstablish.setStatus("deprecated")


class _HpnicfAcfpRuleFragment_Type(TruthValue):
    """Custom type hpnicfAcfpRuleFragment based on TruthValue"""
    defaultValue = 2


_HpnicfAcfpRuleFragment_Type.__name__ = "TruthValue"
_HpnicfAcfpRuleFragment_Object = MibTableColumn
hpnicfAcfpRuleFragment = _HpnicfAcfpRuleFragment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 24),
    _HpnicfAcfpRuleFragment_Type()
)
hpnicfAcfpRuleFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleFragment.setStatus("current")
_HpnicfAcfpRulePacketRate_Type = Integer32
_HpnicfAcfpRulePacketRate_Object = MibTableColumn
hpnicfAcfpRulePacketRate = _HpnicfAcfpRulePacketRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 25),
    _HpnicfAcfpRulePacketRate_Type()
)
hpnicfAcfpRulePacketRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRulePacketRate.setStatus("current")
_HpnicfAcfpRuleRowStatus_Type = RowStatus
_HpnicfAcfpRuleRowStatus_Object = MibTableColumn
hpnicfAcfpRuleRowStatus = _HpnicfAcfpRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 26),
    _HpnicfAcfpRuleRowStatus_Type()
)
hpnicfAcfpRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleRowStatus.setStatus("current")


class _HpnicfAcfpRuleTCPFlag_Type(Integer32):
    """Custom type hpnicfAcfpRuleTCPFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAcfpRuleTCPFlag_Type.__name__ = "Integer32"
_HpnicfAcfpRuleTCPFlag_Object = MibTableColumn
hpnicfAcfpRuleTCPFlag = _HpnicfAcfpRuleTCPFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 27),
    _HpnicfAcfpRuleTCPFlag_Type()
)
hpnicfAcfpRuleTCPFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleTCPFlag.setStatus("current")
_HpnicfAcfpRuleSrcIPV6Address_Type = Ipv6Address
_HpnicfAcfpRuleSrcIPV6Address_Object = MibTableColumn
hpnicfAcfpRuleSrcIPV6Address = _HpnicfAcfpRuleSrcIPV6Address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 28),
    _HpnicfAcfpRuleSrcIPV6Address_Type()
)
hpnicfAcfpRuleSrcIPV6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleSrcIPV6Address.setStatus("current")
_HpnicfAcfpRuleSrcPrefixLen_Type = InetAddressPrefixLength
_HpnicfAcfpRuleSrcPrefixLen_Object = MibTableColumn
hpnicfAcfpRuleSrcPrefixLen = _HpnicfAcfpRuleSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 29),
    _HpnicfAcfpRuleSrcPrefixLen_Type()
)
hpnicfAcfpRuleSrcPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleSrcPrefixLen.setStatus("current")
_HpnicfAcfpRuleDstIPV6Address_Type = Ipv6Address
_HpnicfAcfpRuleDstIPV6Address_Object = MibTableColumn
hpnicfAcfpRuleDstIPV6Address = _HpnicfAcfpRuleDstIPV6Address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 30),
    _HpnicfAcfpRuleDstIPV6Address_Type()
)
hpnicfAcfpRuleDstIPV6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleDstIPV6Address.setStatus("current")
_HpnicfAcfpRuleDstPrefixLen_Type = InetAddressPrefixLength
_HpnicfAcfpRuleDstPrefixLen_Object = MibTableColumn
hpnicfAcfpRuleDstPrefixLen = _HpnicfAcfpRuleDstPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 31),
    _HpnicfAcfpRuleDstPrefixLen_Type()
)
hpnicfAcfpRuleDstPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleDstPrefixLen.setStatus("current")


class _HpnicfAcfpRuleTrafficType_Type(Bits):
    """Custom type hpnicfAcfpRuleTrafficType based on Bits"""
    namedValues = NamedValues(
        *(("unicast", 0),
          ("multicast", 1),
          ("broadcast", 2))
    )

_HpnicfAcfpRuleTrafficType_Type.__name__ = "Bits"
_HpnicfAcfpRuleTrafficType_Object = MibTableColumn
hpnicfAcfpRuleTrafficType = _HpnicfAcfpRuleTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 32),
    _HpnicfAcfpRuleTrafficType_Type()
)
hpnicfAcfpRuleTrafficType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleTrafficType.setStatus("current")


class _HpnicfAcfpRuleTypeOrLen_Type(Integer32):
    """Custom type hpnicfAcfpRuleTypeOrLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAcfpRuleTypeOrLen_Type.__name__ = "Integer32"
_HpnicfAcfpRuleTypeOrLen_Object = MibTableColumn
hpnicfAcfpRuleTypeOrLen = _HpnicfAcfpRuleTypeOrLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 4, 1, 1, 33),
    _HpnicfAcfpRuleTypeOrLen_Type()
)
hpnicfAcfpRuleTypeOrLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAcfpRuleTypeOrLen.setStatus("current")
_HpnicfAcfpNotifications_ObjectIdentity = ObjectIdentity
hpnicfAcfpNotifications = _HpnicfAcfpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 5)
)

# Managed Objects groups


# Notification objects

hpnicfAcfpCurContextChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 5, 1)
)
hpnicfAcfpCurContextChanged.setObjects(
    ("HPN-ICF-ACFP-MIB", "hpnicfAcfpServerCurContextType")
)
if mibBuilder.loadTexts:
    hpnicfAcfpCurContextChanged.setStatus(
        "current"
    )

hpnicfAcfpClientRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 5, 2)
)
hpnicfAcfpClientRegister.setObjects(
    ("HPN-ICF-ACFP-MIB", "hpnicfAcfpClientID")
)
if mibBuilder.loadTexts:
    hpnicfAcfpClientRegister.setStatus(
        "current"
    )

hpnicfAcfpClientUnRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 5, 3)
)
hpnicfAcfpClientUnRegister.setObjects(
    ("HPN-ICF-ACFP-MIB", "hpnicfAcfpClientID")
)
if mibBuilder.loadTexts:
    hpnicfAcfpClientUnRegister.setStatus(
        "current"
    )

hpnicfAcfpClientDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 5, 4)
)
hpnicfAcfpClientDead.setObjects(
    ("HPN-ICF-ACFP-MIB", "hpnicfAcfpClientID")
)
if mibBuilder.loadTexts:
    hpnicfAcfpClientDead.setStatus(
        "current"
    )

hpnicfAcfpNotSupportedOAPMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 5, 5)
)
hpnicfAcfpNotSupportedOAPMode.setObjects(
      *(("HPN-ICF-ACFP-MIB", "hpnicfAcfpClientID"),
        ("HPN-ICF-ACFP-MIB", "hpnicfAcfpClientMode"),
        ("HPN-ICF-ACFP-MIB", "hpnicfAcfpServerInfo"))
)
if mibBuilder.loadTexts:
    hpnicfAcfpNotSupportedOAPMode.setStatus(
        "current"
    )

hpnicfAcfpLifetimeChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 5, 6)
)
hpnicfAcfpLifetimeChangeEvent.setObjects(
    ("HPN-ICF-ACFP-MIB", "hpnicfAcfpPolicyLifetime")
)
if mibBuilder.loadTexts:
    hpnicfAcfpLifetimeChangeEvent.setStatus(
        "current"
    )

hpnicfAcfpRuleCreatedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 5, 7)
)
hpnicfAcfpRuleCreatedEvent.setObjects(
    ("HPN-ICF-ACFP-MIB", "hpnicfAcfpRuleIndex")
)
if mibBuilder.loadTexts:
    hpnicfAcfpRuleCreatedEvent.setStatus(
        "current"
    )

hpnicfAcfpRuleDeletedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 5, 8)
)
hpnicfAcfpRuleDeletedEvent.setObjects(
    ("HPN-ICF-ACFP-MIB", "hpnicfAcfpRuleIndex")
)
if mibBuilder.loadTexts:
    hpnicfAcfpRuleDeletedEvent.setStatus(
        "current"
    )

hpnicfAcfpRuleErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 5, 9)
)
hpnicfAcfpRuleErrorEvent.setObjects(
    ("HPN-ICF-ACFP-MIB", "hpnicfAcfpRuleIndex")
)
if mibBuilder.loadTexts:
    hpnicfAcfpRuleErrorEvent.setStatus(
        "current"
    )

hpnicfAcfpLifetimeExpireEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74, 1, 1, 5, 10)
)
hpnicfAcfpLifetimeExpireEvent.setObjects(
    ("HPN-ICF-ACFP-MIB", "hpnicfAcfpPolicyLifetime")
)
if mibBuilder.loadTexts:
    hpnicfAcfpLifetimeExpireEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-ACFP-MIB",
    **{"hpnicfAcfp": hpnicfAcfp,
       "hpnicfAcfpObjects": hpnicfAcfpObjects,
       "hpnicfAcfpOAP": hpnicfAcfpOAP,
       "hpnicfAcfpServer": hpnicfAcfpServer,
       "hpnicfAcfpServerInfo": hpnicfAcfpServerInfo,
       "hpnicfAcfpServerMaxLifetime": hpnicfAcfpServerMaxLifetime,
       "hpnicfAcfpServerPersistentRules": hpnicfAcfpServerPersistentRules,
       "hpnicfAcfpServerCurContextType": hpnicfAcfpServerCurContextType,
       "hpnicfAcfpClientInfo": hpnicfAcfpClientInfo,
       "hpnicfAcfpClientInfoTable": hpnicfAcfpClientInfoTable,
       "hpnicfAcfpClientInfoEntry": hpnicfAcfpClientInfoEntry,
       "hpnicfAcfpClientID": hpnicfAcfpClientID,
       "hpnicfAcfpClientDescription": hpnicfAcfpClientDescription,
       "hpnicfAcfpClientHwVersion": hpnicfAcfpClientHwVersion,
       "hpnicfAcfpClientOSVersion": hpnicfAcfpClientOSVersion,
       "hpnicfAcfpClientAppVersion": hpnicfAcfpClientAppVersion,
       "hpnicfAcfpClientIP": hpnicfAcfpClientIP,
       "hpnicfAcfpClientMode": hpnicfAcfpClientMode,
       "hpnicfAcfpClientRowStatus": hpnicfAcfpClientRowStatus,
       "hpnicfAcfpPolicy": hpnicfAcfpPolicy,
       "hpnicfAcfpPolicyTable": hpnicfAcfpPolicyTable,
       "hpnicfAcfpPolicyEntry": hpnicfAcfpPolicyEntry,
       "hpnicfAcfpPolicyIndex": hpnicfAcfpPolicyIndex,
       "hpnicfAcfpPolicyInIfIndex": hpnicfAcfpPolicyInIfIndex,
       "hpnicfAcfpPolicyOutIfIndex": hpnicfAcfpPolicyOutIfIndex,
       "hpnicfAcfpPolicyDestIfIndex": hpnicfAcfpPolicyDestIfIndex,
       "hpnicfAcfpPolicyContextID": hpnicfAcfpPolicyContextID,
       "hpnicfAcfpPolicyAdminStatus": hpnicfAcfpPolicyAdminStatus,
       "hpnicfAcfpPolicyLifetime": hpnicfAcfpPolicyLifetime,
       "hpnicfAcfpPolicyTimeStart": hpnicfAcfpPolicyTimeStart,
       "hpnicfAcfpPolicyTimeEnd": hpnicfAcfpPolicyTimeEnd,
       "hpnicfAcfpPolicyRowStatus": hpnicfAcfpPolicyRowStatus,
       "hpnicfAcfpPolicyDestIfFailAction": hpnicfAcfpPolicyDestIfFailAction,
       "hpnicfAcfpPolicyPriority": hpnicfAcfpPolicyPriority,
       "hpnicfAcfpRule": hpnicfAcfpRule,
       "hpnicfAcfpRuleTable": hpnicfAcfpRuleTable,
       "hpnicfAcfpRuleEntry": hpnicfAcfpRuleEntry,
       "hpnicfAcfpRuleIndex": hpnicfAcfpRuleIndex,
       "hpnicfAcfpRuleOperStatus": hpnicfAcfpRuleOperStatus,
       "hpnicfAcfpRuleAction": hpnicfAcfpRuleAction,
       "hpnicfAcfpRuleAll": hpnicfAcfpRuleAll,
       "hpnicfAcfpRuleSrcMAC": hpnicfAcfpRuleSrcMAC,
       "hpnicfAcfpRuleDstMAC": hpnicfAcfpRuleDstMAC,
       "hpnicfAcfpRuleVlanStart": hpnicfAcfpRuleVlanStart,
       "hpnicfAcfpRuleVlanEnd": hpnicfAcfpRuleVlanEnd,
       "hpnicfAcfpRuleProtocol": hpnicfAcfpRuleProtocol,
       "hpnicfAcfpRuleSrcIP": hpnicfAcfpRuleSrcIP,
       "hpnicfAcfpRuleSrcIPMask": hpnicfAcfpRuleSrcIPMask,
       "hpnicfAcfpRuleSrcOp": hpnicfAcfpRuleSrcOp,
       "hpnicfAcfpRuleSrcStartPort": hpnicfAcfpRuleSrcStartPort,
       "hpnicfAcfpRuleSrcEndPort": hpnicfAcfpRuleSrcEndPort,
       "hpnicfAcfpRuleDstIP": hpnicfAcfpRuleDstIP,
       "hpnicfAcfpRuleDstIPMask": hpnicfAcfpRuleDstIPMask,
       "hpnicfAcfpRuleDstOp": hpnicfAcfpRuleDstOp,
       "hpnicfAcfpRuleDstStartPort": hpnicfAcfpRuleDstStartPort,
       "hpnicfAcfpRuleDstEndPort": hpnicfAcfpRuleDstEndPort,
       "hpnicfAcfpRulePrecedence": hpnicfAcfpRulePrecedence,
       "hpnicfAcfpRuleTos": hpnicfAcfpRuleTos,
       "hpnicfAcfpRuleDscp": hpnicfAcfpRuleDscp,
       "hpnicfAcfpRuleEstablish": hpnicfAcfpRuleEstablish,
       "hpnicfAcfpRuleFragment": hpnicfAcfpRuleFragment,
       "hpnicfAcfpRulePacketRate": hpnicfAcfpRulePacketRate,
       "hpnicfAcfpRuleRowStatus": hpnicfAcfpRuleRowStatus,
       "hpnicfAcfpRuleTCPFlag": hpnicfAcfpRuleTCPFlag,
       "hpnicfAcfpRuleSrcIPV6Address": hpnicfAcfpRuleSrcIPV6Address,
       "hpnicfAcfpRuleSrcPrefixLen": hpnicfAcfpRuleSrcPrefixLen,
       "hpnicfAcfpRuleDstIPV6Address": hpnicfAcfpRuleDstIPV6Address,
       "hpnicfAcfpRuleDstPrefixLen": hpnicfAcfpRuleDstPrefixLen,
       "hpnicfAcfpRuleTrafficType": hpnicfAcfpRuleTrafficType,
       "hpnicfAcfpRuleTypeOrLen": hpnicfAcfpRuleTypeOrLen,
       "hpnicfAcfpNotifications": hpnicfAcfpNotifications,
       "hpnicfAcfpCurContextChanged": hpnicfAcfpCurContextChanged,
       "hpnicfAcfpClientRegister": hpnicfAcfpClientRegister,
       "hpnicfAcfpClientUnRegister": hpnicfAcfpClientUnRegister,
       "hpnicfAcfpClientDead": hpnicfAcfpClientDead,
       "hpnicfAcfpNotSupportedOAPMode": hpnicfAcfpNotSupportedOAPMode,
       "hpnicfAcfpLifetimeChangeEvent": hpnicfAcfpLifetimeChangeEvent,
       "hpnicfAcfpRuleCreatedEvent": hpnicfAcfpRuleCreatedEvent,
       "hpnicfAcfpRuleDeletedEvent": hpnicfAcfpRuleDeletedEvent,
       "hpnicfAcfpRuleErrorEvent": hpnicfAcfpRuleErrorEvent,
       "hpnicfAcfpLifetimeExpireEvent": hpnicfAcfpLifetimeExpireEvent}
)
