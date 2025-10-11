# SNMP MIB module (RAD-RadVdsl2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-RadVdsl2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:19:15 2025
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

(ifAlias,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias",
    "ifIndex")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason")

(diverseIfWanGen,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "diverseIfWanGen")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

vdsl2If = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vdsl2Events_ObjectIdentity = ObjectIdentity
vdsl2Events = _Vdsl2Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 0)
)
_Vdsl2Objects_ObjectIdentity = ObjectIdentity
vdsl2Objects = _Vdsl2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 1)
)
_Vdsl2IfNotifVarbindTable_Object = MibTable
vdsl2IfNotifVarbindTable = _Vdsl2IfNotifVarbindTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 1, 2)
)
if mibBuilder.loadTexts:
    vdsl2IfNotifVarbindTable.setStatus("current")
_Vdsl2IfNotifVarbindEntry_Object = MibTableRow
vdsl2IfNotifVarbindEntry = _Vdsl2IfNotifVarbindEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 1, 2, 1)
)
vdsl2IfNotifVarbindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAD-RadVdsl2-MIB", "vdsl2SideIdx"),
)
if mibBuilder.loadTexts:
    vdsl2IfNotifVarbindEntry.setStatus("current")


class _Vdsl2SideIdx_Type(Integer32):
    """Custom type vdsl2SideIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nearEnd", 2),
          ("farEnd", 3))
    )


_Vdsl2SideIdx_Type.__name__ = "Integer32"
_Vdsl2SideIdx_Object = MibTableColumn
vdsl2SideIdx = _Vdsl2SideIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 1, 2, 1, 1),
    _Vdsl2SideIdx_Type()
)
vdsl2SideIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdsl2SideIdx.setStatus("current")


class _Vdsl2LinkDownReason_Type(Integer32):
    """Custom type vdsl2LinkDownReason based on Integer32"""
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
        *(("lossOfFraming", 1),
          ("lossOfSignal", 2),
          ("lossOfPower", 3),
          ("initFailure", 4))
    )


_Vdsl2LinkDownReason_Type.__name__ = "Integer32"
_Vdsl2LinkDownReason_Object = MibTableColumn
vdsl2LinkDownReason = _Vdsl2LinkDownReason_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 1, 2, 1, 2),
    _Vdsl2LinkDownReason_Type()
)
vdsl2LinkDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vdsl2LinkDownReason.setStatus("current")

# Managed Objects groups


# Notification objects

vdsl2LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 0, 1)
)
vdsl2LinkDown.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("RAD-RadVdsl2-MIB", "vdsl2LinkDownReason"))
)
if mibBuilder.loadTexts:
    vdsl2LinkDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-RadVdsl2-MIB",
    **{"vdsl2If": vdsl2If,
       "vdsl2Events": vdsl2Events,
       "vdsl2LinkDown": vdsl2LinkDown,
       "vdsl2Objects": vdsl2Objects,
       "vdsl2IfNotifVarbindTable": vdsl2IfNotifVarbindTable,
       "vdsl2IfNotifVarbindEntry": vdsl2IfNotifVarbindEntry,
       "vdsl2SideIdx": vdsl2SideIdx,
       "vdsl2LinkDownReason": vdsl2LinkDownReason}
)
