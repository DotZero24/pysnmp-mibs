# SNMP MIB module (BRCM-SSH-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-SSH-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:21 2025
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

sshMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sshMgmt.setRevisions(
        ("2007-02-05 00:00",
         "2006-09-29 00:00",
         "2006-02-02 00:00",
         "2005-10-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SshIpStackInterfaces_Type(Bits):
    """Custom type sshIpStackInterfaces based on Bits"""
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

_SshIpStackInterfaces_Type.__name__ = "Bits"
_SshIpStackInterfaces_Object = MibScalar
sshIpStackInterfaces = _SshIpStackInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 1),
    _SshIpStackInterfaces_Type()
)
sshIpStackInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshIpStackInterfaces.setStatus("current")


class _SshUserName_Type(DisplayString):
    """Custom type sshUserName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SshUserName_Type.__name__ = "DisplayString"
_SshUserName_Object = MibScalar
sshUserName = _SshUserName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 2),
    _SshUserName_Type()
)
sshUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshUserName.setStatus("current")


class _SshPassword_Type(DisplayString):
    """Custom type sshPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SshPassword_Type.__name__ = "DisplayString"
_SshPassword_Object = MibScalar
sshPassword = _SshPassword_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 3),
    _SshPassword_Type()
)
sshPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPassword.setStatus("current")


class _SshServerControl_Type(Integer32):
    """Custom type sshServerControl based on Integer32"""
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


_SshServerControl_Type.__name__ = "Integer32"
_SshServerControl_Object = MibScalar
sshServerControl = _SshServerControl_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 4),
    _SshServerControl_Type()
)
sshServerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerControl.setStatus("current")
_SshSessionIp_Type = IpAddress
_SshSessionIp_Object = MibScalar
sshSessionIp = _SshSessionIp_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 5),
    _SshSessionIp_Type()
)
sshSessionIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSessionIp.setStatus("deprecated")
_SshSessionInProgress_Type = TruthValue
_SshSessionInProgress_Object = MibScalar
sshSessionInProgress = _SshSessionInProgress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 6),
    _SshSessionInProgress_Type()
)
sshSessionInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSessionInProgress.setStatus("current")
_SshForceUserLogout_Type = TruthValue
_SshForceUserLogout_Object = MibScalar
sshForceUserLogout = _SshForceUserLogout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 7),
    _SshForceUserLogout_Type()
)
sshForceUserLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshForceUserLogout.setStatus("current")
_SshSessionAddressType_Type = InetAddressType
_SshSessionAddressType_Object = MibScalar
sshSessionAddressType = _SshSessionAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 8),
    _SshSessionAddressType_Type()
)
sshSessionAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSessionAddressType.setStatus("current")
_SshSessionAddress_Type = InetAddress
_SshSessionAddress_Object = MibScalar
sshSessionAddress = _SshSessionAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 9),
    _SshSessionAddress_Type()
)
sshSessionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSessionAddress.setStatus("current")
_SshHackerTable_Object = MibTable
sshHackerTable = _SshHackerTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 10)
)
if mibBuilder.loadTexts:
    sshHackerTable.setStatus("current")
_SshHackerEntry_Object = MibTableRow
sshHackerEntry = _SshHackerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 10, 1)
)
sshHackerEntry.setIndexNames(
    (0, "BRCM-SSH-MGMT-MIB", "sshHackerAddressType"),
    (0, "BRCM-SSH-MGMT-MIB", "sshHackerAddress"),
)
if mibBuilder.loadTexts:
    sshHackerEntry.setStatus("current")
_SshHackerAddressType_Type = InetAddressType
_SshHackerAddressType_Object = MibTableColumn
sshHackerAddressType = _SshHackerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 10, 1, 1),
    _SshHackerAddressType_Type()
)
sshHackerAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sshHackerAddressType.setStatus("current")
_SshHackerAddress_Type = InetAddress
_SshHackerAddress_Object = MibTableColumn
sshHackerAddress = _SshHackerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 10, 1, 2),
    _SshHackerAddress_Type()
)
sshHackerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sshHackerAddress.setStatus("current")
_SshHackerNumAttempts_Type = Unsigned32
_SshHackerNumAttempts_Object = MibTableColumn
sshHackerNumAttempts = _SshHackerNumAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 10, 1, 3),
    _SshHackerNumAttempts_Type()
)
sshHackerNumAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshHackerNumAttempts.setStatus("current")
_SshHackerLastTime_Type = TimeTicks
_SshHackerLastTime_Object = MibTableColumn
sshHackerLastTime = _SshHackerLastTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 10, 1, 4),
    _SshHackerLastTime_Type()
)
sshHackerLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshHackerLastTime.setStatus("current")


class _SshSessionInactivityTimeout_Type(Integer32):
    """Custom type sshSessionInactivityTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_SshSessionInactivityTimeout_Type.__name__ = "Integer32"
_SshSessionInactivityTimeout_Object = MibScalar
sshSessionInactivityTimeout = _SshSessionInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 11),
    _SshSessionInactivityTimeout_Type()
)
sshSessionInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshSessionInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    sshSessionInactivityTimeout.setUnits("seconds")


class _SshHackerInactivityTimeout_Type(Integer32):
    """Custom type sshHackerInactivityTimeout based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 86400),
    )


_SshHackerInactivityTimeout_Type.__name__ = "Integer32"
_SshHackerInactivityTimeout_Object = MibScalar
sshHackerInactivityTimeout = _SshHackerInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 12),
    _SshHackerInactivityTimeout_Type()
)
sshHackerInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHackerInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    sshHackerInactivityTimeout.setUnits("seconds")
_SshTraps_ObjectIdentity = ObjectIdentity
sshTraps = _SshTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 99)
)

# Managed Objects groups


# Notification objects

sshHackerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 4, 99, 1)
)
sshHackerTrap.setObjects(
      *(("BRCM-SSH-MGMT-MIB", "sshHackerAddressType"),
        ("BRCM-SSH-MGMT-MIB", "sshHackerAddress"),
        ("BRCM-SSH-MGMT-MIB", "sshHackerNumAttempts"),
        ("BRCM-SSH-MGMT-MIB", "sshHackerLastTime"))
)
if mibBuilder.loadTexts:
    sshHackerTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-SSH-MGMT-MIB",
    **{"sshMgmt": sshMgmt,
       "sshIpStackInterfaces": sshIpStackInterfaces,
       "sshUserName": sshUserName,
       "sshPassword": sshPassword,
       "sshServerControl": sshServerControl,
       "sshSessionIp": sshSessionIp,
       "sshSessionInProgress": sshSessionInProgress,
       "sshForceUserLogout": sshForceUserLogout,
       "sshSessionAddressType": sshSessionAddressType,
       "sshSessionAddress": sshSessionAddress,
       "sshHackerTable": sshHackerTable,
       "sshHackerEntry": sshHackerEntry,
       "sshHackerAddressType": sshHackerAddressType,
       "sshHackerAddress": sshHackerAddress,
       "sshHackerNumAttempts": sshHackerNumAttempts,
       "sshHackerLastTime": sshHackerLastTime,
       "sshSessionInactivityTimeout": sshSessionInactivityTimeout,
       "sshHackerInactivityTimeout": sshHackerInactivityTimeout,
       "sshTraps": sshTraps,
       "sshHackerTrap": sshHackerTrap}
)
