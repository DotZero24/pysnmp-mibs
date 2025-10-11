# SNMP MIB module (MBG-SNMP-NTP-DISPLAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/meinberg/MBG-SNMP-NTP-DISPLAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:09 2025
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

(mbgSnmpRoot,) = mibBuilder.importSymbols(
    "MBG-SNMP-ROOT-MIB",
    "mbgSnmpRoot")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MbgNtpDisp_ObjectIdentity = ObjectIdentity
mbgNtpDisp = _MbgNtpDisp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 20)
)
_MbgNtpDispInfo_ObjectIdentity = ObjectIdentity
mbgNtpDispInfo = _MbgNtpDispInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 20, 2)
)
_MbgNtpDispClockType_Type = DisplayString
_MbgNtpDispClockType_Object = MibScalar
mbgNtpDispClockType = _MbgNtpDispClockType_Object(
    (1, 3, 6, 1, 4, 1, 5597, 20, 2, 1),
    _MbgNtpDispClockType_Type()
)
mbgNtpDispClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgNtpDispClockType.setStatus("mandatory")
_MbgNtpDispClockTypeVal_Type = Integer32
_MbgNtpDispClockTypeVal_Object = MibScalar
mbgNtpDispClockTypeVal = _MbgNtpDispClockTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 20, 2, 2),
    _MbgNtpDispClockTypeVal_Type()
)
mbgNtpDispClockTypeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgNtpDispClockTypeVal.setStatus("mandatory")
_MbgNtpDispMode_Type = DisplayString
_MbgNtpDispMode_Object = MibScalar
mbgNtpDispMode = _MbgNtpDispMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 20, 2, 3),
    _MbgNtpDispMode_Type()
)
mbgNtpDispMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgNtpDispMode.setStatus("mandatory")
_MbgNtpDispModeVal_Type = Integer32
_MbgNtpDispModeVal_Object = MibScalar
mbgNtpDispModeVal = _MbgNtpDispModeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 20, 2, 4),
    _MbgNtpDispModeVal_Type()
)
mbgNtpDispModeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgNtpDispModeVal.setStatus("mandatory")
_MbgNtpDispState_Type = DisplayString
_MbgNtpDispState_Object = MibScalar
mbgNtpDispState = _MbgNtpDispState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 20, 2, 5),
    _MbgNtpDispState_Type()
)
mbgNtpDispState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgNtpDispState.setStatus("mandatory")
_MbgNtpDispTraps_ObjectIdentity = ObjectIdentity
mbgNtpDispTraps = _MbgNtpDispTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 20, 3)
)

# Managed Objects groups


# Notification objects

mbgNtpDispTrapBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 20, 3, 0, 1)
)
if mibBuilder.loadTexts:
    mbgNtpDispTrapBoot.setStatus(
        ""
    )

mbgNtpDispTrapSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 20, 3, 0, 2)
)
if mibBuilder.loadTexts:
    mbgNtpDispTrapSync.setStatus(
        ""
    )

mbgNtpDispTrapNotSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 20, 3, 0, 3)
)
if mibBuilder.loadTexts:
    mbgNtpDispTrapNotSync.setStatus(
        ""
    )

mbgNtpDispTrapTestNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 20, 3, 0, 4)
)
if mibBuilder.loadTexts:
    mbgNtpDispTrapTestNotification.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MBG-SNMP-NTP-DISPLAY-MIB",
    **{"mbgNtpDisp": mbgNtpDisp,
       "mbgNtpDispInfo": mbgNtpDispInfo,
       "mbgNtpDispClockType": mbgNtpDispClockType,
       "mbgNtpDispClockTypeVal": mbgNtpDispClockTypeVal,
       "mbgNtpDispMode": mbgNtpDispMode,
       "mbgNtpDispModeVal": mbgNtpDispModeVal,
       "mbgNtpDispState": mbgNtpDispState,
       "mbgNtpDispTraps": mbgNtpDispTraps,
       "mbgNtpDispTrapBoot": mbgNtpDispTrapBoot,
       "mbgNtpDispTrapSync": mbgNtpDispTrapSync,
       "mbgNtpDispTrapNotSync": mbgNtpDispTrapNotSync,
       "mbgNtpDispTrapTestNotification": mbgNtpDispTrapTestNotification}
)
