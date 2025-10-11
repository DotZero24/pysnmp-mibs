# SNMP MIB module (BRCM-TELNET-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-TELNET-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:51 2025
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

(cableDataMgmtBase,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-MGMT-MIB",
    "cableDataMgmtBase")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

telnetMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    telnetMgmt.setRevisions(
        ("2007-02-05 00:00",
         "2006-09-29 00:00",
         "2006-02-02 00:00",
         "2005-06-08 00:00",
         "2003-03-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _TelnetIpStackInterfaces_Type(Bits):
    """Custom type telnetIpStackInterfaces based on Bits"""
    defaultHexValue = "00"

    namedValues = NamedValues(
        *(("interface1", 0),
          ("interface2", 1),
          ("interface3", 2),
          ("interface4", 3),
          ("interface5", 4),
          ("interface6", 5),
          ("interface7", 6),
          ("interface8", 7))
    )

_TelnetIpStackInterfaces_Type.__name__ = "Bits"
_TelnetIpStackInterfaces_Object = MibScalar
telnetIpStackInterfaces = _TelnetIpStackInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 1),
    _TelnetIpStackInterfaces_Type()
)
telnetIpStackInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetIpStackInterfaces.setStatus("current")


class _TelnetUserName_Type(DisplayString):
    """Custom type telnetUserName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TelnetUserName_Type.__name__ = "DisplayString"
_TelnetUserName_Object = MibScalar
telnetUserName = _TelnetUserName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 2),
    _TelnetUserName_Type()
)
telnetUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetUserName.setStatus("current")


class _TelnetPassword_Type(DisplayString):
    """Custom type telnetPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TelnetPassword_Type.__name__ = "DisplayString"
_TelnetPassword_Object = MibScalar
telnetPassword = _TelnetPassword_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 3),
    _TelnetPassword_Type()
)
telnetPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPassword.setStatus("current")


class _TelnetServerControl_Type(Integer32):
    """Custom type telnetServerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stop", 0),
          ("start", 1))
    )


_TelnetServerControl_Type.__name__ = "Integer32"
_TelnetServerControl_Object = MibScalar
telnetServerControl = _TelnetServerControl_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 4),
    _TelnetServerControl_Type()
)
telnetServerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetServerControl.setStatus("current")
_TelnetSessionIp_Type = IpAddress
_TelnetSessionIp_Object = MibScalar
telnetSessionIp = _TelnetSessionIp_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 5),
    _TelnetSessionIp_Type()
)
telnetSessionIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetSessionIp.setStatus("deprecated")
_TelnetSessionInProgress_Type = TruthValue
_TelnetSessionInProgress_Object = MibScalar
telnetSessionInProgress = _TelnetSessionInProgress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 6),
    _TelnetSessionInProgress_Type()
)
telnetSessionInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetSessionInProgress.setStatus("current")
_TelnetForceUserLogout_Type = TruthValue
_TelnetForceUserLogout_Object = MibScalar
telnetForceUserLogout = _TelnetForceUserLogout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 7),
    _TelnetForceUserLogout_Type()
)
telnetForceUserLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetForceUserLogout.setStatus("current")
_TelnetSessionAddressType_Type = InetAddressType
_TelnetSessionAddressType_Object = MibScalar
telnetSessionAddressType = _TelnetSessionAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 8),
    _TelnetSessionAddressType_Type()
)
telnetSessionAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetSessionAddressType.setStatus("current")
_TelnetSessionAddress_Type = InetAddress
_TelnetSessionAddress_Object = MibScalar
telnetSessionAddress = _TelnetSessionAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 9),
    _TelnetSessionAddress_Type()
)
telnetSessionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetSessionAddress.setStatus("current")
_TelnetHackerTable_Object = MibTable
telnetHackerTable = _TelnetHackerTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    telnetHackerTable.setStatus("current")
_TelnetHackerEntry_Object = MibTableRow
telnetHackerEntry = _TelnetHackerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 10, 1)
)
telnetHackerEntry.setIndexNames(
    (0, "BRCM-TELNET-MGMT-MIB", "telnetHackerAddressType"),
    (0, "BRCM-TELNET-MGMT-MIB", "telnetHackerAddress"),
)
if mibBuilder.loadTexts:
    telnetHackerEntry.setStatus("current")
_TelnetHackerAddressType_Type = InetAddressType
_TelnetHackerAddressType_Object = MibTableColumn
telnetHackerAddressType = _TelnetHackerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 10, 1, 1),
    _TelnetHackerAddressType_Type()
)
telnetHackerAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    telnetHackerAddressType.setStatus("current")
_TelnetHackerAddress_Type = InetAddress
_TelnetHackerAddress_Object = MibTableColumn
telnetHackerAddress = _TelnetHackerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 10, 1, 2),
    _TelnetHackerAddress_Type()
)
telnetHackerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    telnetHackerAddress.setStatus("current")
_TelnetHackerNumAttempts_Type = Unsigned32
_TelnetHackerNumAttempts_Object = MibTableColumn
telnetHackerNumAttempts = _TelnetHackerNumAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 10, 1, 3),
    _TelnetHackerNumAttempts_Type()
)
telnetHackerNumAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetHackerNumAttempts.setStatus("current")
_TelnetHackerLastTime_Type = TimeTicks
_TelnetHackerLastTime_Object = MibTableColumn
telnetHackerLastTime = _TelnetHackerLastTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 10, 1, 4),
    _TelnetHackerLastTime_Type()
)
telnetHackerLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetHackerLastTime.setStatus("current")


class _TelnetSessionInactivityTimeout_Type(Integer32):
    """Custom type telnetSessionInactivityTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TelnetSessionInactivityTimeout_Type.__name__ = "Integer32"
_TelnetSessionInactivityTimeout_Object = MibScalar
telnetSessionInactivityTimeout = _TelnetSessionInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 11),
    _TelnetSessionInactivityTimeout_Type()
)
telnetSessionInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSessionInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    telnetSessionInactivityTimeout.setUnits("seconds")


class _TelnetHackerInactivityTimeout_Type(Integer32):
    """Custom type telnetHackerInactivityTimeout based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 86400),
    )


_TelnetHackerInactivityTimeout_Type.__name__ = "Integer32"
_TelnetHackerInactivityTimeout_Object = MibScalar
telnetHackerInactivityTimeout = _TelnetHackerInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 12),
    _TelnetHackerInactivityTimeout_Type()
)
telnetHackerInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetHackerInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    telnetHackerInactivityTimeout.setUnits("seconds")
_TelnetTraps_ObjectIdentity = ObjectIdentity
telnetTraps = _TelnetTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 99)
)

# Managed Objects groups


# Notification objects

telnetHackerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 1, 99, 1)
)
telnetHackerTrap.setObjects(
      *(("BRCM-TELNET-MGMT-MIB", "telnetHackerAddressType"),
        ("BRCM-TELNET-MGMT-MIB", "telnetHackerAddress"),
        ("BRCM-TELNET-MGMT-MIB", "telnetHackerNumAttempts"),
        ("BRCM-TELNET-MGMT-MIB", "telnetHackerLastTime"))
)
if mibBuilder.loadTexts:
    telnetHackerTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-TELNET-MGMT-MIB",
    **{"telnetMgmt": telnetMgmt,
       "telnetIpStackInterfaces": telnetIpStackInterfaces,
       "telnetUserName": telnetUserName,
       "telnetPassword": telnetPassword,
       "telnetServerControl": telnetServerControl,
       "telnetSessionIp": telnetSessionIp,
       "telnetSessionInProgress": telnetSessionInProgress,
       "telnetForceUserLogout": telnetForceUserLogout,
       "telnetSessionAddressType": telnetSessionAddressType,
       "telnetSessionAddress": telnetSessionAddress,
       "telnetHackerTable": telnetHackerTable,
       "telnetHackerEntry": telnetHackerEntry,
       "telnetHackerAddressType": telnetHackerAddressType,
       "telnetHackerAddress": telnetHackerAddress,
       "telnetHackerNumAttempts": telnetHackerNumAttempts,
       "telnetHackerLastTime": telnetHackerLastTime,
       "telnetSessionInactivityTimeout": telnetSessionInactivityTimeout,
       "telnetHackerInactivityTimeout": telnetHackerInactivityTimeout,
       "telnetTraps": telnetTraps,
       "telnetHackerTrap": telnetHackerTrap}
)
