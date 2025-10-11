# SNMP MIB module (NEWTEC-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-MODEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:14 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcModem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500)
)
if mibBuilder.loadTexts:
    ntcModem.setRevisions(
        ("2014-02-03 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcModemObjects_ObjectIdentity = ObjectIdentity
ntcModemObjects = _NtcModemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 1)
)
if mibBuilder.loadTexts:
    ntcModemObjects.setStatus("current")


class _NtcModemTxCtrlDemodLockAlarm_Type(Integer32):
    """Custom type ntcModemTxCtrlDemodLockAlarm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableTransmit", 0),
          ("noImpact", 1))
    )


_NtcModemTxCtrlDemodLockAlarm_Type.__name__ = "Integer32"
_NtcModemTxCtrlDemodLockAlarm_Object = MibScalar
ntcModemTxCtrlDemodLockAlarm = _NtcModemTxCtrlDemodLockAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 1, 1),
    _NtcModemTxCtrlDemodLockAlarm_Type()
)
ntcModemTxCtrlDemodLockAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcModemTxCtrlDemodLockAlarm.setStatus("current")
_NtcModemConformance_ObjectIdentity = ObjectIdentity
ntcModemConformance = _NtcModemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 2)
)
if mibBuilder.loadTexts:
    ntcModemConformance.setStatus("current")
_NtcModemConfCompliance_ObjectIdentity = ObjectIdentity
ntcModemConfCompliance = _NtcModemConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 2, 1)
)
if mibBuilder.loadTexts:
    ntcModemConfCompliance.setStatus("current")
_NtcModemConfGroup_ObjectIdentity = ObjectIdentity
ntcModemConfGroup = _NtcModemConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 2, 2)
)
if mibBuilder.loadTexts:
    ntcModemConfGroup.setStatus("current")

# Managed Objects groups

ntcModemConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 2, 2, 1)
)
ntcModemConfGrpV1Standard.setObjects(
    ("NEWTEC-MODEM-MIB", "ntcModemTxCtrlDemodLockAlarm")
)
if mibBuilder.loadTexts:
    ntcModemConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcModemConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 6500, 2, 1, 1)
)
ntcModemConfCompV1Standard.setObjects(
    ("NEWTEC-MODEM-MIB", "ntcModemConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcModemConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-MODEM-MIB",
    **{"ntcModem": ntcModem,
       "ntcModemObjects": ntcModemObjects,
       "ntcModemTxCtrlDemodLockAlarm": ntcModemTxCtrlDemodLockAlarm,
       "ntcModemConformance": ntcModemConformance,
       "ntcModemConfCompliance": ntcModemConfCompliance,
       "ntcModemConfCompV1Standard": ntcModemConfCompV1Standard,
       "ntcModemConfGroup": ntcModemConfGroup,
       "ntcModemConfGrpV1Standard": ntcModemConfGrpV1Standard}
)
