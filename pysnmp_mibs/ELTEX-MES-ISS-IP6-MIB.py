# SNMP MIB module (ELTEX-MES-ISS-IP6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-IP6-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:13 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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

eltMesIssL2IpSnp6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25)
)
if mibBuilder.loadTexts:
    eltMesIssL2IpSnp6MIB.setRevisions(
        ("2021-02-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssL2Ip6SnpNotifications_ObjectIdentity = ObjectIdentity
eltMesIssL2Ip6SnpNotifications = _EltMesIssL2Ip6SnpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 0)
)
_EltMesIssL2Ip6SnpObjects_ObjectIdentity = ObjectIdentity
eltMesIssL2Ip6SnpObjects = _EltMesIssL2Ip6SnpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1)
)
_EltMesIssL2Ip6NDInsp_ObjectIdentity = ObjectIdentity
eltMesIssL2Ip6NDInsp = _EltMesIssL2Ip6NDInsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1)
)
_EltMesIssL2Ip6NDInspGlobals_ObjectIdentity = ObjectIdentity
eltMesIssL2Ip6NDInspGlobals = _EltMesIssL2Ip6NDInspGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 1)
)


class _EltMesIssL2Ip6NDInspStatus_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_EltMesIssL2Ip6NDInspStatus_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspStatus_Object = MibScalar
eltMesIssL2Ip6NDInspStatus = _EltMesIssL2Ip6NDInspStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 1, 1),
    _EltMesIssL2Ip6NDInspStatus_Type()
)
eltMesIssL2Ip6NDInspStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspStatus.setStatus("current")
_EltMesIssL2Ip6NDInspPortConfig_ObjectIdentity = ObjectIdentity
eltMesIssL2Ip6NDInspPortConfig = _EltMesIssL2Ip6NDInspPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 2)
)
_EltMesIssL2Ip6NDInspPortTable_Object = MibTable
eltMesIssL2Ip6NDInspPortTable = _EltMesIssL2Ip6NDInspPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspPortTable.setStatus("current")
_EltMesIssL2Ip6NDInspPortEntry_Object = MibTableRow
eltMesIssL2Ip6NDInspPortEntry = _EltMesIssL2Ip6NDInspPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 2, 1, 1)
)
eltMesIssL2Ip6NDInspPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspPortEntry.setStatus("current")


class _EltMesIssL2Ip6NDInspPortStatus_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_EltMesIssL2Ip6NDInspPortStatus_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspPortStatus_Object = MibTableColumn
eltMesIssL2Ip6NDInspPortStatus = _EltMesIssL2Ip6NDInspPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 2, 1, 1, 1),
    _EltMesIssL2Ip6NDInspPortStatus_Type()
)
eltMesIssL2Ip6NDInspPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspPortStatus.setStatus("current")


class _EltMesIssL2Ip6NDInspPortPolicyId_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspPortPolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltMesIssL2Ip6NDInspPortPolicyId_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspPortPolicyId_Object = MibTableColumn
eltMesIssL2Ip6NDInspPortPolicyId = _EltMesIssL2Ip6NDInspPortPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 2, 1, 1, 2),
    _EltMesIssL2Ip6NDInspPortPolicyId_Type()
)
eltMesIssL2Ip6NDInspPortPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspPortPolicyId.setStatus("current")


class _EltMesIssL2Ip6NDInspPortTrustState_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspPortTrustState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untrusted", 1),
          ("trusted", 2))
    )


_EltMesIssL2Ip6NDInspPortTrustState_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspPortTrustState_Object = MibTableColumn
eltMesIssL2Ip6NDInspPortTrustState = _EltMesIssL2Ip6NDInspPortTrustState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 2, 1, 1, 3),
    _EltMesIssL2Ip6NDInspPortTrustState_Type()
)
eltMesIssL2Ip6NDInspPortTrustState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspPortTrustState.setStatus("current")
_EltMesIssL2Ip6NDInspPortRowStatus_Type = RowStatus
_EltMesIssL2Ip6NDInspPortRowStatus_Object = MibTableColumn
eltMesIssL2Ip6NDInspPortRowStatus = _EltMesIssL2Ip6NDInspPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 2, 1, 1, 4),
    _EltMesIssL2Ip6NDInspPortRowStatus_Type()
)
eltMesIssL2Ip6NDInspPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspPortRowStatus.setStatus("current")
_EltMesIssL2Ip6NDInspPolicyConfig_ObjectIdentity = ObjectIdentity
eltMesIssL2Ip6NDInspPolicyConfig = _EltMesIssL2Ip6NDInspPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3)
)
_EltMesIssL2Ip6NDInspPolicyTable_Object = MibTable
eltMesIssL2Ip6NDInspPolicyTable = _EltMesIssL2Ip6NDInspPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspPolicyTable.setStatus("current")
_EltMesIssL2Ip6NDInspPolicyEntry_Object = MibTableRow
eltMesIssL2Ip6NDInspPolicyEntry = _EltMesIssL2Ip6NDInspPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 1, 1)
)
eltMesIssL2Ip6NDInspPolicyEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-IP6-MIB", "eltMesIssL2Ip6NDInspPolicyId"),
)
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspPolicyEntry.setStatus("current")


class _EltMesIssL2Ip6NDInspPolicyId_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltMesIssL2Ip6NDInspPolicyId_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspPolicyId_Object = MibTableColumn
eltMesIssL2Ip6NDInspPolicyId = _EltMesIssL2Ip6NDInspPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 1, 1, 1),
    _EltMesIssL2Ip6NDInspPolicyId_Type()
)
eltMesIssL2Ip6NDInspPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspPolicyId.setStatus("current")


class _EltMesIssL2Ip6NDInspSrcAddrAclId_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspSrcAddrAclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltMesIssL2Ip6NDInspSrcAddrAclId_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspSrcAddrAclId_Object = MibTableColumn
eltMesIssL2Ip6NDInspSrcAddrAclId = _EltMesIssL2Ip6NDInspSrcAddrAclId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 1, 1, 2),
    _EltMesIssL2Ip6NDInspSrcAddrAclId_Type()
)
eltMesIssL2Ip6NDInspSrcAddrAclId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspSrcAddrAclId.setStatus("current")


class _EltMesIssL2Ip6NDInspRbit_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspRbit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_EltMesIssL2Ip6NDInspRbit_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspRbit_Object = MibTableColumn
eltMesIssL2Ip6NDInspRbit = _EltMesIssL2Ip6NDInspRbit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 1, 1, 3),
    _EltMesIssL2Ip6NDInspRbit_Type()
)
eltMesIssL2Ip6NDInspRbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspRbit.setStatus("current")


class _EltMesIssL2Ip6NDInspSbit_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspSbit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_EltMesIssL2Ip6NDInspSbit_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspSbit_Object = MibTableColumn
eltMesIssL2Ip6NDInspSbit = _EltMesIssL2Ip6NDInspSbit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 1, 1, 4),
    _EltMesIssL2Ip6NDInspSbit_Type()
)
eltMesIssL2Ip6NDInspSbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspSbit.setStatus("current")


class _EltMesIssL2Ip6NDInspObit_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspObit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_EltMesIssL2Ip6NDInspObit_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspObit_Object = MibTableColumn
eltMesIssL2Ip6NDInspObit = _EltMesIssL2Ip6NDInspObit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 1, 1, 5),
    _EltMesIssL2Ip6NDInspObit_Type()
)
eltMesIssL2Ip6NDInspObit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspObit.setStatus("current")


class _EltMesIssL2Ip6NDInspTgtAddrAclId_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspTgtAddrAclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltMesIssL2Ip6NDInspTgtAddrAclId_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspTgtAddrAclId_Object = MibTableColumn
eltMesIssL2Ip6NDInspTgtAddrAclId = _EltMesIssL2Ip6NDInspTgtAddrAclId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 1, 1, 6),
    _EltMesIssL2Ip6NDInspTgtAddrAclId_Type()
)
eltMesIssL2Ip6NDInspTgtAddrAclId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtAddrAclId.setStatus("current")


class _EltMesIssL2Ip6NDInspTgtMacAclId_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspTgtMacAclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltMesIssL2Ip6NDInspTgtMacAclId_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspTgtMacAclId_Object = MibTableColumn
eltMesIssL2Ip6NDInspTgtMacAclId = _EltMesIssL2Ip6NDInspTgtMacAclId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 1, 1, 7),
    _EltMesIssL2Ip6NDInspTgtMacAclId_Type()
)
eltMesIssL2Ip6NDInspTgtMacAclId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtMacAclId.setStatus("current")
_EltMesIssL2Ip6NDInspPolicyRowStatus_Type = RowStatus
_EltMesIssL2Ip6NDInspPolicyRowStatus_Object = MibTableColumn
eltMesIssL2Ip6NDInspPolicyRowStatus = _EltMesIssL2Ip6NDInspPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 1, 1, 8),
    _EltMesIssL2Ip6NDInspPolicyRowStatus_Type()
)
eltMesIssL2Ip6NDInspPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspPolicyRowStatus.setStatus("current")
_EltMesIssL2Ip6NDInspSrcAddrAclTable_Object = MibTable
eltMesIssL2Ip6NDInspSrcAddrAclTable = _EltMesIssL2Ip6NDInspSrcAddrAclTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspSrcAddrAclTable.setStatus("current")
_EltMesIssL2Ip6NDInspSrcAddrAclEntry_Object = MibTableRow
eltMesIssL2Ip6NDInspSrcAddrAclEntry = _EltMesIssL2Ip6NDInspSrcAddrAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 2, 1)
)
eltMesIssL2Ip6NDInspSrcAddrAclEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-IP6-MIB", "eltMesIssL2Ip6NDInspSrcAddrAclNo"),
    (0, "ELTEX-MES-ISS-IP6-MIB", "eltMesIssL2Ip6NDInspSrcAddrAclEntryNo"),
)
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspSrcAddrAclEntry.setStatus("current")


class _EltMesIssL2Ip6NDInspSrcAddrAclNo_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspSrcAddrAclNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltMesIssL2Ip6NDInspSrcAddrAclNo_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspSrcAddrAclNo_Object = MibTableColumn
eltMesIssL2Ip6NDInspSrcAddrAclNo = _EltMesIssL2Ip6NDInspSrcAddrAclNo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 2, 1, 1),
    _EltMesIssL2Ip6NDInspSrcAddrAclNo_Type()
)
eltMesIssL2Ip6NDInspSrcAddrAclNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspSrcAddrAclNo.setStatus("current")


class _EltMesIssL2Ip6NDInspSrcAddrAclEntryNo_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspSrcAddrAclEntryNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EltMesIssL2Ip6NDInspSrcAddrAclEntryNo_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspSrcAddrAclEntryNo_Object = MibTableColumn
eltMesIssL2Ip6NDInspSrcAddrAclEntryNo = _EltMesIssL2Ip6NDInspSrcAddrAclEntryNo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 2, 1, 2),
    _EltMesIssL2Ip6NDInspSrcAddrAclEntryNo_Type()
)
eltMesIssL2Ip6NDInspSrcAddrAclEntryNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspSrcAddrAclEntryNo.setStatus("current")
_EltMesIssL2Ip6NDInspSrcAddrAclAddr_Type = InetAddressIPv6
_EltMesIssL2Ip6NDInspSrcAddrAclAddr_Object = MibTableColumn
eltMesIssL2Ip6NDInspSrcAddrAclAddr = _EltMesIssL2Ip6NDInspSrcAddrAclAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 2, 1, 3),
    _EltMesIssL2Ip6NDInspSrcAddrAclAddr_Type()
)
eltMesIssL2Ip6NDInspSrcAddrAclAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspSrcAddrAclAddr.setStatus("current")


class _EltMesIssL2Ip6NDInspSrcAddrAclPrefixLen_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspSrcAddrAclPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_EltMesIssL2Ip6NDInspSrcAddrAclPrefixLen_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspSrcAddrAclPrefixLen_Object = MibTableColumn
eltMesIssL2Ip6NDInspSrcAddrAclPrefixLen = _EltMesIssL2Ip6NDInspSrcAddrAclPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 2, 1, 4),
    _EltMesIssL2Ip6NDInspSrcAddrAclPrefixLen_Type()
)
eltMesIssL2Ip6NDInspSrcAddrAclPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspSrcAddrAclPrefixLen.setStatus("current")
_EltMesIssL2Ip6NDInspSrcAddrAclRowStatus_Type = RowStatus
_EltMesIssL2Ip6NDInspSrcAddrAclRowStatus_Object = MibTableColumn
eltMesIssL2Ip6NDInspSrcAddrAclRowStatus = _EltMesIssL2Ip6NDInspSrcAddrAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 2, 1, 5),
    _EltMesIssL2Ip6NDInspSrcAddrAclRowStatus_Type()
)
eltMesIssL2Ip6NDInspSrcAddrAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspSrcAddrAclRowStatus.setStatus("current")
_EltMesIssL2Ip6NDInspTgtAddrAclTable_Object = MibTable
eltMesIssL2Ip6NDInspTgtAddrAclTable = _EltMesIssL2Ip6NDInspTgtAddrAclTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtAddrAclTable.setStatus("current")
_EltMesIssL2Ip6NDInspTgtAddrAclEntry_Object = MibTableRow
eltMesIssL2Ip6NDInspTgtAddrAclEntry = _EltMesIssL2Ip6NDInspTgtAddrAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 3, 1)
)
eltMesIssL2Ip6NDInspTgtAddrAclEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-IP6-MIB", "eltMesIssL2Ip6NDInspTgtAddrAclNo"),
    (0, "ELTEX-MES-ISS-IP6-MIB", "eltMesIssL2Ip6NDInspTgtAddrAclEntryNo"),
)
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtAddrAclEntry.setStatus("current")


class _EltMesIssL2Ip6NDInspTgtAddrAclNo_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspTgtAddrAclNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltMesIssL2Ip6NDInspTgtAddrAclNo_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspTgtAddrAclNo_Object = MibTableColumn
eltMesIssL2Ip6NDInspTgtAddrAclNo = _EltMesIssL2Ip6NDInspTgtAddrAclNo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 3, 1, 1),
    _EltMesIssL2Ip6NDInspTgtAddrAclNo_Type()
)
eltMesIssL2Ip6NDInspTgtAddrAclNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtAddrAclNo.setStatus("current")


class _EltMesIssL2Ip6NDInspTgtAddrAclEntryNo_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspTgtAddrAclEntryNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EltMesIssL2Ip6NDInspTgtAddrAclEntryNo_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspTgtAddrAclEntryNo_Object = MibTableColumn
eltMesIssL2Ip6NDInspTgtAddrAclEntryNo = _EltMesIssL2Ip6NDInspTgtAddrAclEntryNo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 3, 1, 2),
    _EltMesIssL2Ip6NDInspTgtAddrAclEntryNo_Type()
)
eltMesIssL2Ip6NDInspTgtAddrAclEntryNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtAddrAclEntryNo.setStatus("current")
_EltMesIssL2Ip6NDInspTgtAddrAclAddr_Type = InetAddressIPv6
_EltMesIssL2Ip6NDInspTgtAddrAclAddr_Object = MibTableColumn
eltMesIssL2Ip6NDInspTgtAddrAclAddr = _EltMesIssL2Ip6NDInspTgtAddrAclAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 3, 1, 3),
    _EltMesIssL2Ip6NDInspTgtAddrAclAddr_Type()
)
eltMesIssL2Ip6NDInspTgtAddrAclAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtAddrAclAddr.setStatus("current")


class _EltMesIssL2Ip6NDInspTgtAddrAclPrefixLen_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspTgtAddrAclPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_EltMesIssL2Ip6NDInspTgtAddrAclPrefixLen_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspTgtAddrAclPrefixLen_Object = MibTableColumn
eltMesIssL2Ip6NDInspTgtAddrAclPrefixLen = _EltMesIssL2Ip6NDInspTgtAddrAclPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 3, 1, 4),
    _EltMesIssL2Ip6NDInspTgtAddrAclPrefixLen_Type()
)
eltMesIssL2Ip6NDInspTgtAddrAclPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtAddrAclPrefixLen.setStatus("current")
_EltMesIssL2Ip6NDInspTgtAddrAclRowStatus_Type = RowStatus
_EltMesIssL2Ip6NDInspTgtAddrAclRowStatus_Object = MibTableColumn
eltMesIssL2Ip6NDInspTgtAddrAclRowStatus = _EltMesIssL2Ip6NDInspTgtAddrAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 3, 1, 5),
    _EltMesIssL2Ip6NDInspTgtAddrAclRowStatus_Type()
)
eltMesIssL2Ip6NDInspTgtAddrAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtAddrAclRowStatus.setStatus("current")
_EltMesIssL2Ip6NDInspTgtMacAclTable_Object = MibTable
eltMesIssL2Ip6NDInspTgtMacAclTable = _EltMesIssL2Ip6NDInspTgtMacAclTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtMacAclTable.setStatus("current")
_EltMesIssL2Ip6NDInspTgtMacAclEntry_Object = MibTableRow
eltMesIssL2Ip6NDInspTgtMacAclEntry = _EltMesIssL2Ip6NDInspTgtMacAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 4, 1)
)
eltMesIssL2Ip6NDInspTgtMacAclEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-IP6-MIB", "eltMesIssL2Ip6NDInspTgtMacAclNo"),
    (0, "ELTEX-MES-ISS-IP6-MIB", "eltMesIssL2Ip6NDInspTgtMacAclEntryNo"),
)
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtMacAclEntry.setStatus("current")


class _EltMesIssL2Ip6NDInspTgtMacAclNo_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspTgtMacAclNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltMesIssL2Ip6NDInspTgtMacAclNo_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspTgtMacAclNo_Object = MibTableColumn
eltMesIssL2Ip6NDInspTgtMacAclNo = _EltMesIssL2Ip6NDInspTgtMacAclNo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 4, 1, 1),
    _EltMesIssL2Ip6NDInspTgtMacAclNo_Type()
)
eltMesIssL2Ip6NDInspTgtMacAclNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtMacAclNo.setStatus("current")


class _EltMesIssL2Ip6NDInspTgtMacAclEntryNo_Type(Integer32):
    """Custom type eltMesIssL2Ip6NDInspTgtMacAclEntryNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EltMesIssL2Ip6NDInspTgtMacAclEntryNo_Type.__name__ = "Integer32"
_EltMesIssL2Ip6NDInspTgtMacAclEntryNo_Object = MibTableColumn
eltMesIssL2Ip6NDInspTgtMacAclEntryNo = _EltMesIssL2Ip6NDInspTgtMacAclEntryNo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 4, 1, 2),
    _EltMesIssL2Ip6NDInspTgtMacAclEntryNo_Type()
)
eltMesIssL2Ip6NDInspTgtMacAclEntryNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtMacAclEntryNo.setStatus("current")
_EltMesIssL2Ip6NDInspTgtMacAclMacAddr_Type = MacAddress
_EltMesIssL2Ip6NDInspTgtMacAclMacAddr_Object = MibTableColumn
eltMesIssL2Ip6NDInspTgtMacAclMacAddr = _EltMesIssL2Ip6NDInspTgtMacAclMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 4, 1, 3),
    _EltMesIssL2Ip6NDInspTgtMacAclMacAddr_Type()
)
eltMesIssL2Ip6NDInspTgtMacAclMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtMacAclMacAddr.setStatus("current")
_EltMesIssL2Ip6NDInspTgtMacAclRowStatus_Type = RowStatus
_EltMesIssL2Ip6NDInspTgtMacAclRowStatus_Object = MibTableColumn
eltMesIssL2Ip6NDInspTgtMacAclRowStatus = _EltMesIssL2Ip6NDInspTgtMacAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 1, 1, 3, 4, 1, 4),
    _EltMesIssL2Ip6NDInspTgtMacAclRowStatus_Type()
)
eltMesIssL2Ip6NDInspTgtMacAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltMesIssL2Ip6NDInspTgtMacAclRowStatus.setStatus("current")
_EltMesIssL2Ip6SnpConformance_ObjectIdentity = ObjectIdentity
eltMesIssL2Ip6SnpConformance = _EltMesIssL2Ip6SnpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-IP6-MIB",
    **{"eltMesIssL2IpSnp6MIB": eltMesIssL2IpSnp6MIB,
       "eltMesIssL2Ip6SnpNotifications": eltMesIssL2Ip6SnpNotifications,
       "eltMesIssL2Ip6SnpObjects": eltMesIssL2Ip6SnpObjects,
       "eltMesIssL2Ip6NDInsp": eltMesIssL2Ip6NDInsp,
       "eltMesIssL2Ip6NDInspGlobals": eltMesIssL2Ip6NDInspGlobals,
       "eltMesIssL2Ip6NDInspStatus": eltMesIssL2Ip6NDInspStatus,
       "eltMesIssL2Ip6NDInspPortConfig": eltMesIssL2Ip6NDInspPortConfig,
       "eltMesIssL2Ip6NDInspPortTable": eltMesIssL2Ip6NDInspPortTable,
       "eltMesIssL2Ip6NDInspPortEntry": eltMesIssL2Ip6NDInspPortEntry,
       "eltMesIssL2Ip6NDInspPortStatus": eltMesIssL2Ip6NDInspPortStatus,
       "eltMesIssL2Ip6NDInspPortPolicyId": eltMesIssL2Ip6NDInspPortPolicyId,
       "eltMesIssL2Ip6NDInspPortTrustState": eltMesIssL2Ip6NDInspPortTrustState,
       "eltMesIssL2Ip6NDInspPortRowStatus": eltMesIssL2Ip6NDInspPortRowStatus,
       "eltMesIssL2Ip6NDInspPolicyConfig": eltMesIssL2Ip6NDInspPolicyConfig,
       "eltMesIssL2Ip6NDInspPolicyTable": eltMesIssL2Ip6NDInspPolicyTable,
       "eltMesIssL2Ip6NDInspPolicyEntry": eltMesIssL2Ip6NDInspPolicyEntry,
       "eltMesIssL2Ip6NDInspPolicyId": eltMesIssL2Ip6NDInspPolicyId,
       "eltMesIssL2Ip6NDInspSrcAddrAclId": eltMesIssL2Ip6NDInspSrcAddrAclId,
       "eltMesIssL2Ip6NDInspRbit": eltMesIssL2Ip6NDInspRbit,
       "eltMesIssL2Ip6NDInspSbit": eltMesIssL2Ip6NDInspSbit,
       "eltMesIssL2Ip6NDInspObit": eltMesIssL2Ip6NDInspObit,
       "eltMesIssL2Ip6NDInspTgtAddrAclId": eltMesIssL2Ip6NDInspTgtAddrAclId,
       "eltMesIssL2Ip6NDInspTgtMacAclId": eltMesIssL2Ip6NDInspTgtMacAclId,
       "eltMesIssL2Ip6NDInspPolicyRowStatus": eltMesIssL2Ip6NDInspPolicyRowStatus,
       "eltMesIssL2Ip6NDInspSrcAddrAclTable": eltMesIssL2Ip6NDInspSrcAddrAclTable,
       "eltMesIssL2Ip6NDInspSrcAddrAclEntry": eltMesIssL2Ip6NDInspSrcAddrAclEntry,
       "eltMesIssL2Ip6NDInspSrcAddrAclNo": eltMesIssL2Ip6NDInspSrcAddrAclNo,
       "eltMesIssL2Ip6NDInspSrcAddrAclEntryNo": eltMesIssL2Ip6NDInspSrcAddrAclEntryNo,
       "eltMesIssL2Ip6NDInspSrcAddrAclAddr": eltMesIssL2Ip6NDInspSrcAddrAclAddr,
       "eltMesIssL2Ip6NDInspSrcAddrAclPrefixLen": eltMesIssL2Ip6NDInspSrcAddrAclPrefixLen,
       "eltMesIssL2Ip6NDInspSrcAddrAclRowStatus": eltMesIssL2Ip6NDInspSrcAddrAclRowStatus,
       "eltMesIssL2Ip6NDInspTgtAddrAclTable": eltMesIssL2Ip6NDInspTgtAddrAclTable,
       "eltMesIssL2Ip6NDInspTgtAddrAclEntry": eltMesIssL2Ip6NDInspTgtAddrAclEntry,
       "eltMesIssL2Ip6NDInspTgtAddrAclNo": eltMesIssL2Ip6NDInspTgtAddrAclNo,
       "eltMesIssL2Ip6NDInspTgtAddrAclEntryNo": eltMesIssL2Ip6NDInspTgtAddrAclEntryNo,
       "eltMesIssL2Ip6NDInspTgtAddrAclAddr": eltMesIssL2Ip6NDInspTgtAddrAclAddr,
       "eltMesIssL2Ip6NDInspTgtAddrAclPrefixLen": eltMesIssL2Ip6NDInspTgtAddrAclPrefixLen,
       "eltMesIssL2Ip6NDInspTgtAddrAclRowStatus": eltMesIssL2Ip6NDInspTgtAddrAclRowStatus,
       "eltMesIssL2Ip6NDInspTgtMacAclTable": eltMesIssL2Ip6NDInspTgtMacAclTable,
       "eltMesIssL2Ip6NDInspTgtMacAclEntry": eltMesIssL2Ip6NDInspTgtMacAclEntry,
       "eltMesIssL2Ip6NDInspTgtMacAclNo": eltMesIssL2Ip6NDInspTgtMacAclNo,
       "eltMesIssL2Ip6NDInspTgtMacAclEntryNo": eltMesIssL2Ip6NDInspTgtMacAclEntryNo,
       "eltMesIssL2Ip6NDInspTgtMacAclMacAddr": eltMesIssL2Ip6NDInspTgtMacAclMacAddr,
       "eltMesIssL2Ip6NDInspTgtMacAclRowStatus": eltMesIssL2Ip6NDInspTgtMacAclRowStatus,
       "eltMesIssL2Ip6SnpConformance": eltMesIssL2Ip6SnpConformance}
)
