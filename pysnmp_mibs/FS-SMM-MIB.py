# SNMP MIB module (FS-SMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-SMM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:29 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

fsSmmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120)
)
if mibBuilder.loadTexts:
    fsSmmMIB.setRevisions(
        ("2012-12-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsSmmObjects_ObjectIdentity = ObjectIdentity
fsSmmObjects = _FsSmmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 1)
)
_FsReportSimBillSwitch_Type = Unsigned32
_FsReportSimBillSwitch_Object = MibScalar
fsReportSimBillSwitch = _FsReportSimBillSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 1, 1),
    _FsReportSimBillSwitch_Type()
)
fsReportSimBillSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsReportSimBillSwitch.setStatus("current")


class _FsQuerySimBillCmd_Type(OctetString):
    """Custom type fsQuerySimBillCmd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FsQuerySimBillCmd_Type.__name__ = "OctetString"
_FsQuerySimBillCmd_Object = MibScalar
fsQuerySimBillCmd = _FsQuerySimBillCmd_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 1, 2),
    _FsQuerySimBillCmd_Type()
)
fsQuerySimBillCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQuerySimBillCmd.setStatus("current")
_FsSmsUseTable_Object = MibTable
fsSmsUseTable = _FsSmsUseTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 1, 3)
)
if mibBuilder.loadTexts:
    fsSmsUseTable.setStatus("current")
_FsSmsUseEntry_Object = MibTableRow
fsSmsUseEntry = _FsSmsUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 1, 3, 1)
)
fsSmsUseEntry.setIndexNames(
    (0, "FS-SMM-MIB", "fsSimImsi"),
)
if mibBuilder.loadTexts:
    fsSmsUseEntry.setStatus("current")


class _FsSimImsi_Type(DisplayString):
    """Custom type fsSimImsi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FsSimImsi_Type.__name__ = "DisplayString"
_FsSimImsi_Object = MibTableColumn
fsSimImsi = _FsSimImsi_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 1, 3, 1, 1),
    _FsSimImsi_Type()
)
fsSimImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSimImsi.setStatus("current")
_FsSmsUseCnt_Type = Unsigned32
_FsSmsUseCnt_Object = MibTableColumn
fsSmsUseCnt = _FsSmsUseCnt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 1, 3, 1, 2),
    _FsSmsUseCnt_Type()
)
fsSmsUseCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSmsUseCnt.setStatus("current")
_FsSmmTrapObjects_ObjectIdentity = ObjectIdentity
fsSmmTrapObjects = _FsSmmTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 2)
)
_FsSimBillTrapObjects_ObjectIdentity = ObjectIdentity
fsSimBillTrapObjects = _FsSimBillTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 2, 1)
)


class _FsQuerySimBillContent_Type(OctetString):
    """Custom type fsQuerySimBillContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_FsQuerySimBillContent_Type.__name__ = "OctetString"
_FsQuerySimBillContent_Object = MibScalar
fsQuerySimBillContent = _FsQuerySimBillContent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 2, 1, 1),
    _FsQuerySimBillContent_Type()
)
fsQuerySimBillContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsQuerySimBillContent.setStatus("current")


class _FsReportSimBillContent_Type(OctetString):
    """Custom type fsReportSimBillContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_FsReportSimBillContent_Type.__name__ = "OctetString"
_FsReportSimBillContent_Object = MibScalar
fsReportSimBillContent = _FsReportSimBillContent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 2, 1, 2),
    _FsReportSimBillContent_Type()
)
fsReportSimBillContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsReportSimBillContent.setStatus("current")
_FsSmmTraps_ObjectIdentity = ObjectIdentity
fsSmmTraps = _FsSmmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 3)
)
_FsSimBillNotifications_ObjectIdentity = ObjectIdentity
fsSimBillNotifications = _FsSimBillNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 3, 1)
)

# Managed Objects groups


# Notification objects

fsQuerySimBill = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 3, 1, 1)
)
fsQuerySimBill.setObjects(
    ("FS-SMM-MIB", "fsQuerySimBillContent")
)
if mibBuilder.loadTexts:
    fsQuerySimBill.setStatus(
        "current"
    )

fsReportSimBill = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 120, 3, 1, 2)
)
fsReportSimBill.setObjects(
    ("FS-SMM-MIB", "fsReportSimBillContent")
)
if mibBuilder.loadTexts:
    fsReportSimBill.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-SMM-MIB",
    **{"fsSmmMIB": fsSmmMIB,
       "fsSmmObjects": fsSmmObjects,
       "fsReportSimBillSwitch": fsReportSimBillSwitch,
       "fsQuerySimBillCmd": fsQuerySimBillCmd,
       "fsSmsUseTable": fsSmsUseTable,
       "fsSmsUseEntry": fsSmsUseEntry,
       "fsSimImsi": fsSimImsi,
       "fsSmsUseCnt": fsSmsUseCnt,
       "fsSmmTrapObjects": fsSmmTrapObjects,
       "fsSimBillTrapObjects": fsSimBillTrapObjects,
       "fsQuerySimBillContent": fsQuerySimBillContent,
       "fsReportSimBillContent": fsReportSimBillContent,
       "fsSmmTraps": fsSmmTraps,
       "fsSimBillNotifications": fsSimBillNotifications,
       "fsQuerySimBill": fsQuerySimBill,
       "fsReportSimBill": fsReportSimBill}
)
