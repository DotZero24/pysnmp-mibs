# SNMP MIB module (H3C-DOT11-WM2U-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-DOT11-WM2U-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:14 2025
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

(h3cDot11,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cDot11")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

h3cDot11WM2U = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16)
)
if mibBuilder.loadTexts:
    h3cDot11WM2U.setRevisions(
        ("2016-01-25 10:20",
         "2015-03-31 15:51")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cDot11WM2UEnableStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



class H3cDot11WM2UAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("unicast", 2),
          ("multicast", 3))
    )



class H3cDot11WM2UGroupVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("igmpv1orv2", 1),
          ("igmpv3", 2),
          ("mldv1", 3),
          ("mldv2", 4))
    )



class H3cDot11WM2UGroupMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )



# MIB Managed Objects in the order of their OIDs

_H3cDot11WM2UConfigGroup_ObjectIdentity = ObjectIdentity
h3cDot11WM2UConfigGroup = _H3cDot11WM2UConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1)
)
_H3cDot11WM2USrvTempStatesTable_Object = MibTable
h3cDot11WM2USrvTempStatesTable = _H3cDot11WM2USrvTempStatesTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDot11WM2USrvTempStatesTable.setStatus("current")
_H3cDot11WM2USrvTempStatesEntry_Object = MibTableRow
h3cDot11WM2USrvTempStatesEntry = _H3cDot11WM2USrvTempStatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 1, 1)
)
h3cDot11WM2USrvTempStatesEntry.setIndexNames(
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2USrvTempName"),
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2USrvTempAddressType"),
)
if mibBuilder.loadTexts:
    h3cDot11WM2USrvTempStatesEntry.setStatus("current")


class _H3cDot11WM2USrvTempName_Type(OctetString):
    """Custom type h3cDot11WM2USrvTempName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_H3cDot11WM2USrvTempName_Type.__name__ = "OctetString"
_H3cDot11WM2USrvTempName_Object = MibTableColumn
h3cDot11WM2USrvTempName = _H3cDot11WM2USrvTempName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 1, 1, 1),
    _H3cDot11WM2USrvTempName_Type()
)
h3cDot11WM2USrvTempName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2USrvTempName.setStatus("current")
_H3cDot11WM2USrvTempAddressType_Type = InetAddressType
_H3cDot11WM2USrvTempAddressType_Object = MibTableColumn
h3cDot11WM2USrvTempAddressType = _H3cDot11WM2USrvTempAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 1, 1, 2),
    _H3cDot11WM2USrvTempAddressType_Type()
)
h3cDot11WM2USrvTempAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2USrvTempAddressType.setStatus("current")
_H3cDot11WM2USrvTempState_Type = H3cDot11WM2UEnableStatus
_H3cDot11WM2USrvTempState_Object = MibTableColumn
h3cDot11WM2USrvTempState = _H3cDot11WM2USrvTempState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 1, 1, 3),
    _H3cDot11WM2USrvTempState_Type()
)
h3cDot11WM2USrvTempState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WM2USrvTempState.setStatus("current")
_H3cDot11WM2UAgingTimeTable_Object = MibTable
h3cDot11WM2UAgingTimeTable = _H3cDot11WM2UAgingTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDot11WM2UAgingTimeTable.setStatus("current")
_H3cDot11WM2UAgingTimeEntry_Object = MibTableRow
h3cDot11WM2UAgingTimeEntry = _H3cDot11WM2UAgingTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 2, 1)
)
h3cDot11WM2UAgingTimeEntry.setIndexNames(
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2UAgingAddressType"),
)
if mibBuilder.loadTexts:
    h3cDot11WM2UAgingTimeEntry.setStatus("current")
_H3cDot11WM2UAgingAddressType_Type = InetAddressType
_H3cDot11WM2UAgingAddressType_Object = MibTableColumn
h3cDot11WM2UAgingAddressType = _H3cDot11WM2UAgingAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 2, 1, 1),
    _H3cDot11WM2UAgingAddressType_Type()
)
h3cDot11WM2UAgingAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2UAgingAddressType.setStatus("current")


class _H3cDot11WM2UAgingTime_Type(Unsigned32):
    """Custom type h3cDot11WM2UAgingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_H3cDot11WM2UAgingTime_Type.__name__ = "Unsigned32"
_H3cDot11WM2UAgingTime_Object = MibTableColumn
h3cDot11WM2UAgingTime = _H3cDot11WM2UAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 2, 1, 2),
    _H3cDot11WM2UAgingTime_Type()
)
h3cDot11WM2UAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WM2UAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11WM2UAgingTime.setUnits("seconds")
_H3cDot11WM2UAgingTimeState_Type = H3cDot11WM2UEnableStatus
_H3cDot11WM2UAgingTimeState_Object = MibTableColumn
h3cDot11WM2UAgingTimeState = _H3cDot11WM2UAgingTimeState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 2, 1, 3),
    _H3cDot11WM2UAgingTimeState_Type()
)
h3cDot11WM2UAgingTimeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WM2UAgingTimeState.setStatus("current")
_H3cDot11WM2UClientEtyLmtTable_Object = MibTable
h3cDot11WM2UClientEtyLmtTable = _H3cDot11WM2UClientEtyLmtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 3)
)
if mibBuilder.loadTexts:
    h3cDot11WM2UClientEtyLmtTable.setStatus("current")
_H3cDot11WM2UClientEtyLmtEntry_Object = MibTableRow
h3cDot11WM2UClientEtyLmtEntry = _H3cDot11WM2UClientEtyLmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 3, 1)
)
h3cDot11WM2UClientEtyLmtEntry.setIndexNames(
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2UClientEtyAddrType"),
)
if mibBuilder.loadTexts:
    h3cDot11WM2UClientEtyLmtEntry.setStatus("current")
_H3cDot11WM2UClientEtyAddrType_Type = InetAddressType
_H3cDot11WM2UClientEtyAddrType_Object = MibTableColumn
h3cDot11WM2UClientEtyAddrType = _H3cDot11WM2UClientEtyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 3, 1, 1),
    _H3cDot11WM2UClientEtyAddrType_Type()
)
h3cDot11WM2UClientEtyAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2UClientEtyAddrType.setStatus("current")


class _H3cDot11WM2UClientValue_Type(Unsigned32):
    """Custom type h3cDot11WM2UClientValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1024),
    )


_H3cDot11WM2UClientValue_Type.__name__ = "Unsigned32"
_H3cDot11WM2UClientValue_Object = MibTableColumn
h3cDot11WM2UClientValue = _H3cDot11WM2UClientValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 3, 1, 2),
    _H3cDot11WM2UClientValue_Type()
)
h3cDot11WM2UClientValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WM2UClientValue.setStatus("current")
_H3cDot11WM2UClientState_Type = H3cDot11WM2UEnableStatus
_H3cDot11WM2UClientState_Object = MibTableColumn
h3cDot11WM2UClientState = _H3cDot11WM2UClientState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 3, 1, 3),
    _H3cDot11WM2UClientState_Type()
)
h3cDot11WM2UClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WM2UClientState.setStatus("current")
_H3cDot11WM2UGlobalEtyLmtTable_Object = MibTable
h3cDot11WM2UGlobalEtyLmtTable = _H3cDot11WM2UGlobalEtyLmtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 4)
)
if mibBuilder.loadTexts:
    h3cDot11WM2UGlobalEtyLmtTable.setStatus("current")
_H3cDot11WM2UGlobalEtyLmtEntry_Object = MibTableRow
h3cDot11WM2UGlobalEtyLmtEntry = _H3cDot11WM2UGlobalEtyLmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 4, 1)
)
h3cDot11WM2UGlobalEtyLmtEntry.setIndexNames(
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2UGlobalEtyAddrType"),
)
if mibBuilder.loadTexts:
    h3cDot11WM2UGlobalEtyLmtEntry.setStatus("current")
_H3cDot11WM2UGlobalEtyAddrType_Type = InetAddressType
_H3cDot11WM2UGlobalEtyAddrType_Object = MibTableColumn
h3cDot11WM2UGlobalEtyAddrType = _H3cDot11WM2UGlobalEtyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 4, 1, 1),
    _H3cDot11WM2UGlobalEtyAddrType_Type()
)
h3cDot11WM2UGlobalEtyAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2UGlobalEtyAddrType.setStatus("current")


class _H3cDot11WM2UGlobalValue_Type(Unsigned32):
    """Custom type h3cDot11WM2UGlobalValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8192),
    )


_H3cDot11WM2UGlobalValue_Type.__name__ = "Unsigned32"
_H3cDot11WM2UGlobalValue_Object = MibTableColumn
h3cDot11WM2UGlobalValue = _H3cDot11WM2UGlobalValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 4, 1, 2),
    _H3cDot11WM2UGlobalValue_Type()
)
h3cDot11WM2UGlobalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WM2UGlobalValue.setStatus("current")
_H3cDot11WM2UGlobalState_Type = H3cDot11WM2UEnableStatus
_H3cDot11WM2UGlobalState_Object = MibTableColumn
h3cDot11WM2UGlobalState = _H3cDot11WM2UGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 4, 1, 3),
    _H3cDot11WM2UGlobalState_Type()
)
h3cDot11WM2UGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WM2UGlobalState.setStatus("current")
_H3cDot11WM2UFwdClientLmtsTable_Object = MibTable
h3cDot11WM2UFwdClientLmtsTable = _H3cDot11WM2UFwdClientLmtsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 5)
)
if mibBuilder.loadTexts:
    h3cDot11WM2UFwdClientLmtsTable.setStatus("current")
_H3cDot11WM2UFwdClientLmtsEntry_Object = MibTableRow
h3cDot11WM2UFwdClientLmtsEntry = _H3cDot11WM2UFwdClientLmtsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 5, 1)
)
h3cDot11WM2UFwdClientLmtsEntry.setIndexNames(
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2UFwdClientAddrType"),
)
if mibBuilder.loadTexts:
    h3cDot11WM2UFwdClientLmtsEntry.setStatus("current")
_H3cDot11WM2UFwdClientAddrType_Type = InetAddressType
_H3cDot11WM2UFwdClientAddrType_Object = MibTableColumn
h3cDot11WM2UFwdClientAddrType = _H3cDot11WM2UFwdClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 5, 1, 1),
    _H3cDot11WM2UFwdClientAddrType_Type()
)
h3cDot11WM2UFwdClientAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2UFwdClientAddrType.setStatus("current")


class _H3cDot11WM2UFwdClientValue_Type(Unsigned32):
    """Custom type h3cDot11WM2UFwdClientValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_H3cDot11WM2UFwdClientValue_Type.__name__ = "Unsigned32"
_H3cDot11WM2UFwdClientValue_Object = MibTableColumn
h3cDot11WM2UFwdClientValue = _H3cDot11WM2UFwdClientValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 5, 1, 2),
    _H3cDot11WM2UFwdClientValue_Type()
)
h3cDot11WM2UFwdClientValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WM2UFwdClientValue.setStatus("current")
_H3cDot11WM2UFwdClientAction_Type = H3cDot11WM2UAction
_H3cDot11WM2UFwdClientAction_Object = MibTableColumn
h3cDot11WM2UFwdClientAction = _H3cDot11WM2UFwdClientAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 5, 1, 3),
    _H3cDot11WM2UFwdClientAction_Type()
)
h3cDot11WM2UFwdClientAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WM2UFwdClientAction.setStatus("current")
_H3cDot11WM2UFwdClientState_Type = H3cDot11WM2UEnableStatus
_H3cDot11WM2UFwdClientState_Object = MibTableColumn
h3cDot11WM2UFwdClientState = _H3cDot11WM2UFwdClientState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 5, 1, 4),
    _H3cDot11WM2UFwdClientState_Type()
)
h3cDot11WM2UFwdClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WM2UFwdClientState.setStatus("current")
_H3cDot11WM2URateLimitsTable_Object = MibTable
h3cDot11WM2URateLimitsTable = _H3cDot11WM2URateLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 6)
)
if mibBuilder.loadTexts:
    h3cDot11WM2URateLimitsTable.setStatus("current")
_H3cDot11WM2URateLimitsEntry_Object = MibTableRow
h3cDot11WM2URateLimitsEntry = _H3cDot11WM2URateLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 6, 1)
)
h3cDot11WM2URateLimitsEntry.setIndexNames(
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2URateLmtsAddrType"),
)
if mibBuilder.loadTexts:
    h3cDot11WM2URateLimitsEntry.setStatus("current")
_H3cDot11WM2URateLmtsAddrType_Type = InetAddressType
_H3cDot11WM2URateLmtsAddrType_Object = MibTableColumn
h3cDot11WM2URateLmtsAddrType = _H3cDot11WM2URateLmtsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 6, 1, 1),
    _H3cDot11WM2URateLmtsAddrType_Type()
)
h3cDot11WM2URateLmtsAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2URateLmtsAddrType.setStatus("current")


class _H3cDot11WM2UInterval_Type(Unsigned32):
    """Custom type h3cDot11WM2UInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_H3cDot11WM2UInterval_Type.__name__ = "Unsigned32"
_H3cDot11WM2UInterval_Object = MibTableColumn
h3cDot11WM2UInterval = _H3cDot11WM2UInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 6, 1, 2),
    _H3cDot11WM2UInterval_Type()
)
h3cDot11WM2UInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WM2UInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11WM2UInterval.setUnits("seconds")


class _H3cDot11WM2UThreshold_Type(Unsigned32):
    """Custom type h3cDot11WM2UThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_H3cDot11WM2UThreshold_Type.__name__ = "Unsigned32"
_H3cDot11WM2UThreshold_Object = MibTableColumn
h3cDot11WM2UThreshold = _H3cDot11WM2UThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 6, 1, 3),
    _H3cDot11WM2UThreshold_Type()
)
h3cDot11WM2UThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WM2UThreshold.setStatus("current")
_H3cDot11WM2URateLmtsState_Type = H3cDot11WM2UEnableStatus
_H3cDot11WM2URateLmtsState_Object = MibTableColumn
h3cDot11WM2URateLmtsState = _H3cDot11WM2URateLmtsState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 1, 6, 1, 4),
    _H3cDot11WM2URateLmtsState_Type()
)
h3cDot11WM2URateLmtsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WM2URateLmtsState.setStatus("current")
_H3cDot11WM2UDataGroup_ObjectIdentity = ObjectIdentity
h3cDot11WM2UDataGroup = _H3cDot11WM2UDataGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2)
)
_H3cDot11WM2UClientsTable_Object = MibTable
h3cDot11WM2UClientsTable = _H3cDot11WM2UClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDot11WM2UClientsTable.setStatus("current")
_H3cDot11WM2UClientsEntry_Object = MibTableRow
h3cDot11WM2UClientsEntry = _H3cDot11WM2UClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 1, 1)
)
h3cDot11WM2UClientsEntry.setIndexNames(
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2UClientMacAddress"),
)
if mibBuilder.loadTexts:
    h3cDot11WM2UClientsEntry.setStatus("current")
_H3cDot11WM2UClientMacAddress_Type = MacAddress
_H3cDot11WM2UClientMacAddress_Object = MibTableColumn
h3cDot11WM2UClientMacAddress = _H3cDot11WM2UClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 1, 1, 1),
    _H3cDot11WM2UClientMacAddress_Type()
)
h3cDot11WM2UClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2UClientMacAddress.setStatus("current")
_H3cDot11WM2UDuration_Type = TimeTicks
_H3cDot11WM2UDuration_Object = MibTableColumn
h3cDot11WM2UDuration = _H3cDot11WM2UDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 1, 1, 2),
    _H3cDot11WM2UDuration_Type()
)
h3cDot11WM2UDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11WM2UDuration.setStatus("current")
_H3cDot11WM2UGroupNum4_Type = Unsigned32
_H3cDot11WM2UGroupNum4_Object = MibTableColumn
h3cDot11WM2UGroupNum4 = _H3cDot11WM2UGroupNum4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 1, 1, 3),
    _H3cDot11WM2UGroupNum4_Type()
)
h3cDot11WM2UGroupNum4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11WM2UGroupNum4.setStatus("current")
_H3cDot11WM2UGroupNum6_Type = Unsigned32
_H3cDot11WM2UGroupNum6_Object = MibTableColumn
h3cDot11WM2UGroupNum6 = _H3cDot11WM2UGroupNum6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 1, 1, 4),
    _H3cDot11WM2UGroupNum6_Type()
)
h3cDot11WM2UGroupNum6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11WM2UGroupNum6.setStatus("current")
_H3cDot11WM2UGroupsTable_Object = MibTable
h3cDot11WM2UGroupsTable = _H3cDot11WM2UGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 2)
)
if mibBuilder.loadTexts:
    h3cDot11WM2UGroupsTable.setStatus("current")
_H3cDot11WM2UGroupsEntry_Object = MibTableRow
h3cDot11WM2UGroupsEntry = _H3cDot11WM2UGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 2, 1)
)
h3cDot11WM2UGroupsEntry.setIndexNames(
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2UGrpMacAddress"),
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2UGrpAddressType"),
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2UAddress"),
)
if mibBuilder.loadTexts:
    h3cDot11WM2UGroupsEntry.setStatus("current")
_H3cDot11WM2UGrpMacAddress_Type = MacAddress
_H3cDot11WM2UGrpMacAddress_Object = MibTableColumn
h3cDot11WM2UGrpMacAddress = _H3cDot11WM2UGrpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 2, 1, 1),
    _H3cDot11WM2UGrpMacAddress_Type()
)
h3cDot11WM2UGrpMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2UGrpMacAddress.setStatus("current")
_H3cDot11WM2UGrpAddressType_Type = InetAddressType
_H3cDot11WM2UGrpAddressType_Object = MibTableColumn
h3cDot11WM2UGrpAddressType = _H3cDot11WM2UGrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 2, 1, 2),
    _H3cDot11WM2UGrpAddressType_Type()
)
h3cDot11WM2UGrpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2UGrpAddressType.setStatus("current")
_H3cDot11WM2UAddress_Type = InetAddress
_H3cDot11WM2UAddress_Object = MibTableColumn
h3cDot11WM2UAddress = _H3cDot11WM2UAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 2, 1, 3),
    _H3cDot11WM2UAddress_Type()
)
h3cDot11WM2UAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2UAddress.setStatus("current")
_H3cDot11WM2UVersion_Type = H3cDot11WM2UGroupVersion
_H3cDot11WM2UVersion_Object = MibTableColumn
h3cDot11WM2UVersion = _H3cDot11WM2UVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 2, 1, 4),
    _H3cDot11WM2UVersion_Type()
)
h3cDot11WM2UVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11WM2UVersion.setStatus("current")
_H3cDot11WM2UMode_Type = H3cDot11WM2UGroupMode
_H3cDot11WM2UMode_Object = MibTableColumn
h3cDot11WM2UMode = _H3cDot11WM2UMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 2, 1, 5),
    _H3cDot11WM2UMode_Type()
)
h3cDot11WM2UMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11WM2UMode.setStatus("current")
_H3cDot11WM2USourceNum_Type = Unsigned32
_H3cDot11WM2USourceNum_Object = MibTableColumn
h3cDot11WM2USourceNum = _H3cDot11WM2USourceNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 2, 1, 6),
    _H3cDot11WM2USourceNum_Type()
)
h3cDot11WM2USourceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11WM2USourceNum.setStatus("current")
_H3cDot11WM2UGrpDurLastRefTime_Type = TimeTicks
_H3cDot11WM2UGrpDurLastRefTime_Object = MibTableColumn
h3cDot11WM2UGrpDurLastRefTime = _H3cDot11WM2UGrpDurLastRefTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 2, 1, 7),
    _H3cDot11WM2UGrpDurLastRefTime_Type()
)
h3cDot11WM2UGrpDurLastRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11WM2UGrpDurLastRefTime.setStatus("current")
_H3cDot11WM2USourcesTable_Object = MibTable
h3cDot11WM2USourcesTable = _H3cDot11WM2USourcesTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 3)
)
if mibBuilder.loadTexts:
    h3cDot11WM2USourcesTable.setStatus("current")
_H3cDot11WM2USourcesEntry_Object = MibTableRow
h3cDot11WM2USourcesEntry = _H3cDot11WM2USourcesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 3, 1)
)
h3cDot11WM2USourcesEntry.setIndexNames(
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2USrcMacAddress"),
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2USrcAddressType"),
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2UGroupAddress"),
    (0, "H3C-DOT11-WM2U-MIB", "h3cDot11WM2USourceAddress"),
)
if mibBuilder.loadTexts:
    h3cDot11WM2USourcesEntry.setStatus("current")
_H3cDot11WM2USrcMacAddress_Type = MacAddress
_H3cDot11WM2USrcMacAddress_Object = MibTableColumn
h3cDot11WM2USrcMacAddress = _H3cDot11WM2USrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 3, 1, 1),
    _H3cDot11WM2USrcMacAddress_Type()
)
h3cDot11WM2USrcMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2USrcMacAddress.setStatus("current")
_H3cDot11WM2USrcAddressType_Type = InetAddressType
_H3cDot11WM2USrcAddressType_Object = MibTableColumn
h3cDot11WM2USrcAddressType = _H3cDot11WM2USrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 3, 1, 2),
    _H3cDot11WM2USrcAddressType_Type()
)
h3cDot11WM2USrcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2USrcAddressType.setStatus("current")
_H3cDot11WM2UGroupAddress_Type = InetAddress
_H3cDot11WM2UGroupAddress_Object = MibTableColumn
h3cDot11WM2UGroupAddress = _H3cDot11WM2UGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 3, 1, 3),
    _H3cDot11WM2UGroupAddress_Type()
)
h3cDot11WM2UGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2UGroupAddress.setStatus("current")
_H3cDot11WM2USourceAddress_Type = InetAddress
_H3cDot11WM2USourceAddress_Object = MibTableColumn
h3cDot11WM2USourceAddress = _H3cDot11WM2USourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 3, 1, 4),
    _H3cDot11WM2USourceAddress_Type()
)
h3cDot11WM2USourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WM2USourceAddress.setStatus("current")
_H3cDot11WM2USrcDurLastRefTime_Type = TimeTicks
_H3cDot11WM2USrcDurLastRefTime_Object = MibTableColumn
h3cDot11WM2USrcDurLastRefTime = _H3cDot11WM2USrcDurLastRefTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 16, 2, 3, 1, 5),
    _H3cDot11WM2USrcDurLastRefTime_Type()
)
h3cDot11WM2USrcDurLastRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11WM2USrcDurLastRefTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-DOT11-WM2U-MIB",
    **{"H3cDot11WM2UEnableStatus": H3cDot11WM2UEnableStatus,
       "H3cDot11WM2UAction": H3cDot11WM2UAction,
       "H3cDot11WM2UGroupVersion": H3cDot11WM2UGroupVersion,
       "H3cDot11WM2UGroupMode": H3cDot11WM2UGroupMode,
       "h3cDot11WM2U": h3cDot11WM2U,
       "h3cDot11WM2UConfigGroup": h3cDot11WM2UConfigGroup,
       "h3cDot11WM2USrvTempStatesTable": h3cDot11WM2USrvTempStatesTable,
       "h3cDot11WM2USrvTempStatesEntry": h3cDot11WM2USrvTempStatesEntry,
       "h3cDot11WM2USrvTempName": h3cDot11WM2USrvTempName,
       "h3cDot11WM2USrvTempAddressType": h3cDot11WM2USrvTempAddressType,
       "h3cDot11WM2USrvTempState": h3cDot11WM2USrvTempState,
       "h3cDot11WM2UAgingTimeTable": h3cDot11WM2UAgingTimeTable,
       "h3cDot11WM2UAgingTimeEntry": h3cDot11WM2UAgingTimeEntry,
       "h3cDot11WM2UAgingAddressType": h3cDot11WM2UAgingAddressType,
       "h3cDot11WM2UAgingTime": h3cDot11WM2UAgingTime,
       "h3cDot11WM2UAgingTimeState": h3cDot11WM2UAgingTimeState,
       "h3cDot11WM2UClientEtyLmtTable": h3cDot11WM2UClientEtyLmtTable,
       "h3cDot11WM2UClientEtyLmtEntry": h3cDot11WM2UClientEtyLmtEntry,
       "h3cDot11WM2UClientEtyAddrType": h3cDot11WM2UClientEtyAddrType,
       "h3cDot11WM2UClientValue": h3cDot11WM2UClientValue,
       "h3cDot11WM2UClientState": h3cDot11WM2UClientState,
       "h3cDot11WM2UGlobalEtyLmtTable": h3cDot11WM2UGlobalEtyLmtTable,
       "h3cDot11WM2UGlobalEtyLmtEntry": h3cDot11WM2UGlobalEtyLmtEntry,
       "h3cDot11WM2UGlobalEtyAddrType": h3cDot11WM2UGlobalEtyAddrType,
       "h3cDot11WM2UGlobalValue": h3cDot11WM2UGlobalValue,
       "h3cDot11WM2UGlobalState": h3cDot11WM2UGlobalState,
       "h3cDot11WM2UFwdClientLmtsTable": h3cDot11WM2UFwdClientLmtsTable,
       "h3cDot11WM2UFwdClientLmtsEntry": h3cDot11WM2UFwdClientLmtsEntry,
       "h3cDot11WM2UFwdClientAddrType": h3cDot11WM2UFwdClientAddrType,
       "h3cDot11WM2UFwdClientValue": h3cDot11WM2UFwdClientValue,
       "h3cDot11WM2UFwdClientAction": h3cDot11WM2UFwdClientAction,
       "h3cDot11WM2UFwdClientState": h3cDot11WM2UFwdClientState,
       "h3cDot11WM2URateLimitsTable": h3cDot11WM2URateLimitsTable,
       "h3cDot11WM2URateLimitsEntry": h3cDot11WM2URateLimitsEntry,
       "h3cDot11WM2URateLmtsAddrType": h3cDot11WM2URateLmtsAddrType,
       "h3cDot11WM2UInterval": h3cDot11WM2UInterval,
       "h3cDot11WM2UThreshold": h3cDot11WM2UThreshold,
       "h3cDot11WM2URateLmtsState": h3cDot11WM2URateLmtsState,
       "h3cDot11WM2UDataGroup": h3cDot11WM2UDataGroup,
       "h3cDot11WM2UClientsTable": h3cDot11WM2UClientsTable,
       "h3cDot11WM2UClientsEntry": h3cDot11WM2UClientsEntry,
       "h3cDot11WM2UClientMacAddress": h3cDot11WM2UClientMacAddress,
       "h3cDot11WM2UDuration": h3cDot11WM2UDuration,
       "h3cDot11WM2UGroupNum4": h3cDot11WM2UGroupNum4,
       "h3cDot11WM2UGroupNum6": h3cDot11WM2UGroupNum6,
       "h3cDot11WM2UGroupsTable": h3cDot11WM2UGroupsTable,
       "h3cDot11WM2UGroupsEntry": h3cDot11WM2UGroupsEntry,
       "h3cDot11WM2UGrpMacAddress": h3cDot11WM2UGrpMacAddress,
       "h3cDot11WM2UGrpAddressType": h3cDot11WM2UGrpAddressType,
       "h3cDot11WM2UAddress": h3cDot11WM2UAddress,
       "h3cDot11WM2UVersion": h3cDot11WM2UVersion,
       "h3cDot11WM2UMode": h3cDot11WM2UMode,
       "h3cDot11WM2USourceNum": h3cDot11WM2USourceNum,
       "h3cDot11WM2UGrpDurLastRefTime": h3cDot11WM2UGrpDurLastRefTime,
       "h3cDot11WM2USourcesTable": h3cDot11WM2USourcesTable,
       "h3cDot11WM2USourcesEntry": h3cDot11WM2USourcesEntry,
       "h3cDot11WM2USrcMacAddress": h3cDot11WM2USrcMacAddress,
       "h3cDot11WM2USrcAddressType": h3cDot11WM2USrcAddressType,
       "h3cDot11WM2UGroupAddress": h3cDot11WM2UGroupAddress,
       "h3cDot11WM2USourceAddress": h3cDot11WM2USourceAddress,
       "h3cDot11WM2USrcDurLastRefTime": h3cDot11WM2USrcDurLastRefTime}
)
