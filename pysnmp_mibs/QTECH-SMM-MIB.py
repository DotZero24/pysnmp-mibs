# SNMP MIB module (QTECH-SMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-SMM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:43 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechSmmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120)
)
if mibBuilder.loadTexts:
    qtechSmmMIB.setRevisions(
        ("2012-12-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechSmmObjects_ObjectIdentity = ObjectIdentity
qtechSmmObjects = _QtechSmmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 1)
)
_QtechReportSimBillSwitch_Type = Unsigned32
_QtechReportSimBillSwitch_Object = MibScalar
qtechReportSimBillSwitch = _QtechReportSimBillSwitch_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 1, 1),
    _QtechReportSimBillSwitch_Type()
)
qtechReportSimBillSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechReportSimBillSwitch.setStatus("current")


class _QtechQuerySimBillCmd_Type(OctetString):
    """Custom type qtechQuerySimBillCmd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_QtechQuerySimBillCmd_Type.__name__ = "OctetString"
_QtechQuerySimBillCmd_Object = MibScalar
qtechQuerySimBillCmd = _QtechQuerySimBillCmd_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 1, 2),
    _QtechQuerySimBillCmd_Type()
)
qtechQuerySimBillCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechQuerySimBillCmd.setStatus("current")
_QtechSmsUseTable_Object = MibTable
qtechSmsUseTable = _QtechSmsUseTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 1, 3)
)
if mibBuilder.loadTexts:
    qtechSmsUseTable.setStatus("current")
_QtechSmsUseEntry_Object = MibTableRow
qtechSmsUseEntry = _QtechSmsUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 1, 3, 1)
)
qtechSmsUseEntry.setIndexNames(
    (0, "QTECH-SMM-MIB", "qtechSimImsi"),
)
if mibBuilder.loadTexts:
    qtechSmsUseEntry.setStatus("current")


class _QtechSimImsi_Type(DisplayString):
    """Custom type qtechSimImsi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QtechSimImsi_Type.__name__ = "DisplayString"
_QtechSimImsi_Object = MibTableColumn
qtechSimImsi = _QtechSimImsi_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 1, 3, 1, 1),
    _QtechSimImsi_Type()
)
qtechSimImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSimImsi.setStatus("current")
_QtechSmsUseCnt_Type = Unsigned32
_QtechSmsUseCnt_Object = MibTableColumn
qtechSmsUseCnt = _QtechSmsUseCnt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 1, 3, 1, 2),
    _QtechSmsUseCnt_Type()
)
qtechSmsUseCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSmsUseCnt.setStatus("current")
_QtechSmmTrapObjects_ObjectIdentity = ObjectIdentity
qtechSmmTrapObjects = _QtechSmmTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 2)
)
_QtechSimBillTrapObjects_ObjectIdentity = ObjectIdentity
qtechSimBillTrapObjects = _QtechSimBillTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 2, 1)
)


class _QtechQuerySimBillContent_Type(OctetString):
    """Custom type qtechQuerySimBillContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_QtechQuerySimBillContent_Type.__name__ = "OctetString"
_QtechQuerySimBillContent_Object = MibScalar
qtechQuerySimBillContent = _QtechQuerySimBillContent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 2, 1, 1),
    _QtechQuerySimBillContent_Type()
)
qtechQuerySimBillContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechQuerySimBillContent.setStatus("current")


class _QtechReportSimBillContent_Type(OctetString):
    """Custom type qtechReportSimBillContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_QtechReportSimBillContent_Type.__name__ = "OctetString"
_QtechReportSimBillContent_Object = MibScalar
qtechReportSimBillContent = _QtechReportSimBillContent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 2, 1, 2),
    _QtechReportSimBillContent_Type()
)
qtechReportSimBillContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechReportSimBillContent.setStatus("current")
_QtechSmmTraps_ObjectIdentity = ObjectIdentity
qtechSmmTraps = _QtechSmmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 3)
)
_QtechSimBillNotifications_ObjectIdentity = ObjectIdentity
qtechSimBillNotifications = _QtechSimBillNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 3, 1)
)

# Managed Objects groups


# Notification objects

qtechQuerySimBill = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 3, 1, 1)
)
qtechQuerySimBill.setObjects(
    ("QTECH-SMM-MIB", "qtechQuerySimBillContent")
)
if mibBuilder.loadTexts:
    qtechQuerySimBill.setStatus(
        "current"
    )

qtechReportSimBill = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 120, 3, 1, 2)
)
qtechReportSimBill.setObjects(
    ("QTECH-SMM-MIB", "qtechReportSimBillContent")
)
if mibBuilder.loadTexts:
    qtechReportSimBill.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-SMM-MIB",
    **{"qtechSmmMIB": qtechSmmMIB,
       "qtechSmmObjects": qtechSmmObjects,
       "qtechReportSimBillSwitch": qtechReportSimBillSwitch,
       "qtechQuerySimBillCmd": qtechQuerySimBillCmd,
       "qtechSmsUseTable": qtechSmsUseTable,
       "qtechSmsUseEntry": qtechSmsUseEntry,
       "qtechSimImsi": qtechSimImsi,
       "qtechSmsUseCnt": qtechSmsUseCnt,
       "qtechSmmTrapObjects": qtechSmmTrapObjects,
       "qtechSimBillTrapObjects": qtechSimBillTrapObjects,
       "qtechQuerySimBillContent": qtechQuerySimBillContent,
       "qtechReportSimBillContent": qtechReportSimBillContent,
       "qtechSmmTraps": qtechSmmTraps,
       "qtechSimBillNotifications": qtechSimBillNotifications,
       "qtechQuerySimBill": qtechQuerySimBill,
       "qtechReportSimBill": qtechReportSimBill}
)
