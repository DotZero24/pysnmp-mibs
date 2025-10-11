# SNMP MIB module (HMIT-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HMIT-IP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:53:11 2025
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

(hmITMgmt,) = mibBuilder.importSymbols(
    "HMIT-SMI",
    "hmITMgmt")

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

hmITIpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 700)
)
if mibBuilder.loadTexts:
    hmITIpMib.setRevisions(
        ("2010-01-08 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmITIpTable_Object = MibTable
hmITIpTable = _HmITIpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 700, 1)
)
if mibBuilder.loadTexts:
    hmITIpTable.setStatus("current")
_HmITIpEntry_Object = MibTableRow
hmITIpEntry = _HmITIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 700, 1, 1)
)
hmITIpEntry.setIndexNames(
    (0, "HMIT-IP-MIB", "hmITIpTIfName"),
    (0, "HMIT-IP-MIB", "hmITIpTAddress"),
    (0, "HMIT-IP-MIB", "hmITIpTMask"),
)
if mibBuilder.loadTexts:
    hmITIpEntry.setStatus("current")


class _HmITIpTIfName_Type(DisplayString):
    """Custom type hmITIpTIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HmITIpTIfName_Type.__name__ = "DisplayString"
_HmITIpTIfName_Object = MibTableColumn
hmITIpTIfName = _HmITIpTIfName_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 700, 1, 1, 1),
    _HmITIpTIfName_Type()
)
hmITIpTIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmITIpTIfName.setStatus("current")
_HmITIpTAddress_Type = IpAddress
_HmITIpTAddress_Object = MibTableColumn
hmITIpTAddress = _HmITIpTAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 700, 1, 1, 2),
    _HmITIpTAddress_Type()
)
hmITIpTAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmITIpTAddress.setStatus("current")
_HmITIpTMask_Type = IpAddress
_HmITIpTMask_Object = MibTableColumn
hmITIpTMask = _HmITIpTMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 700, 1, 1, 3),
    _HmITIpTMask_Type()
)
hmITIpTMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmITIpTMask.setStatus("current")
_HmITIpTBPAddress_Type = IpAddress
_HmITIpTBPAddress_Object = MibTableColumn
hmITIpTBPAddress = _HmITIpTBPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 700, 1, 1, 4),
    _HmITIpTBPAddress_Type()
)
hmITIpTBPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITIpTBPAddress.setStatus("current")


class _HmITIpTType_Type(Integer32):
    """Custom type hmITIpTType based on Integer32"""
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


_HmITIpTType_Type.__name__ = "Integer32"
_HmITIpTType_Object = MibTableColumn
hmITIpTType = _HmITIpTType_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 700, 1, 1, 5),
    _HmITIpTType_Type()
)
hmITIpTType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITIpTType.setStatus("current")


class _HmITIpTWay_Type(Integer32):
    """Custom type hmITIpTWay based on Integer32"""
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


_HmITIpTWay_Type.__name__ = "Integer32"
_HmITIpTWay_Object = MibTableColumn
hmITIpTWay = _HmITIpTWay_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 700, 1, 1, 6),
    _HmITIpTWay_Type()
)
hmITIpTWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITIpTWay.setStatus("current")
_HmITIpTRowStatus_Type = RowStatus
_HmITIpTRowStatus_Object = MibTableColumn
hmITIpTRowStatus = _HmITIpTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 700, 1, 1, 7),
    _HmITIpTRowStatus_Type()
)
hmITIpTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmITIpTRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMIT-IP-MIB",
    **{"hmITIpMib": hmITIpMib,
       "hmITIpTable": hmITIpTable,
       "hmITIpEntry": hmITIpEntry,
       "hmITIpTIfName": hmITIpTIfName,
       "hmITIpTAddress": hmITIpTAddress,
       "hmITIpTMask": hmITIpTMask,
       "hmITIpTBPAddress": hmITIpTBPAddress,
       "hmITIpTType": hmITIpTType,
       "hmITIpTWay": hmITIpTWay,
       "hmITIpTRowStatus": hmITIpTRowStatus}
)
