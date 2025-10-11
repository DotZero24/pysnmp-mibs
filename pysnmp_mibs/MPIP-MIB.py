# SNMP MIB module (MPIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MPIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:11 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 ObjectName,
 ObjectSyntax,
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
    "ObjectName",
    "ObjectSyntax",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mpIpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 700)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpIpTable_Object = MibTable
mpIpTable = _MpIpTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 700, 1)
)
if mibBuilder.loadTexts:
    mpIpTable.setStatus("current")
_MpIpEntry_Object = MibTableRow
mpIpEntry = _MpIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 700, 1, 1)
)
mpIpEntry.setIndexNames(
    (0, "MPIP-MIB", "mpIpTIfName"),
    (0, "MPIP-MIB", "mpIpTAddress"),
    (0, "MPIP-MIB", "mpIpTMask"),
)
if mibBuilder.loadTexts:
    mpIpEntry.setStatus("current")


class _MpIpTIfName_Type(DisplayString):
    """Custom type mpIpTIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MpIpTIfName_Type.__name__ = "DisplayString"
_MpIpTIfName_Object = MibTableColumn
mpIpTIfName = _MpIpTIfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 700, 1, 1, 1),
    _MpIpTIfName_Type()
)
mpIpTIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpIpTIfName.setStatus("current")
_MpIpTAddress_Type = IpAddress
_MpIpTAddress_Object = MibTableColumn
mpIpTAddress = _MpIpTAddress_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 700, 1, 1, 2),
    _MpIpTAddress_Type()
)
mpIpTAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpIpTAddress.setStatus("current")
_MpIpTMask_Type = IpAddress
_MpIpTMask_Object = MibTableColumn
mpIpTMask = _MpIpTMask_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 700, 1, 1, 3),
    _MpIpTMask_Type()
)
mpIpTMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpIpTMask.setStatus("current")
_MpIpTBPAddress_Type = IpAddress
_MpIpTBPAddress_Object = MibTableColumn
mpIpTBPAddress = _MpIpTBPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 700, 1, 1, 4),
    _MpIpTBPAddress_Type()
)
mpIpTBPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpIpTBPAddress.setStatus("current")


class _MpIpTType_Type(Integer32):
    """Custom type mpIpTType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_MpIpTType_Type.__name__ = "Integer32"
_MpIpTType_Object = MibTableColumn
mpIpTType = _MpIpTType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 700, 1, 1, 5),
    _MpIpTType_Type()
)
mpIpTType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpIpTType.setStatus("current")


class _MpIpTWay_Type(Integer32):
    """Custom type mpIpTWay based on Integer32"""
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
        *(("manual", 1),
          ("dhcp", 2),
          ("negotiated", 3),
          ("unnumbered", 4),
          ("virtual", 5))
    )


_MpIpTWay_Type.__name__ = "Integer32"
_MpIpTWay_Object = MibTableColumn
mpIpTWay = _MpIpTWay_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 700, 1, 1, 6),
    _MpIpTWay_Type()
)
mpIpTWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpIpTWay.setStatus("current")
_MpIpTRowStatus_Type = RowStatus
_MpIpTRowStatus_Object = MibTableColumn
mpIpTRowStatus = _MpIpTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 700, 1, 1, 7),
    _MpIpTRowStatus_Type()
)
mpIpTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpIpTRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPIP-MIB",
    **{"mpIpMib": mpIpMib,
       "mpIpTable": mpIpTable,
       "mpIpEntry": mpIpEntry,
       "mpIpTIfName": mpIpTIfName,
       "mpIpTAddress": mpIpTAddress,
       "mpIpTMask": mpIpTMask,
       "mpIpTBPAddress": mpIpTBPAddress,
       "mpIpTType": mpIpTType,
       "mpIpTWay": mpIpTWay,
       "mpIpTRowStatus": mpIpTRowStatus}
)
