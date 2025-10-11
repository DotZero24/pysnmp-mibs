# SNMP MIB module (SUPERMICRO-BEEP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-BEEP-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:51 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsBeepServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 18)
)
if mibBuilder.loadTexts:
    fsBeepServer.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsBeepServerScalars_ObjectIdentity = ObjectIdentity
fsBeepServerScalars = _FsBeepServerScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 18, 1)
)


class _FsBeepServerAdminStatus_Type(Integer32):
    """Custom type fsBeepServerAdminStatus based on Integer32"""
    defaultValue = 2

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


_FsBeepServerAdminStatus_Type.__name__ = "Integer32"
_FsBeepServerAdminStatus_Object = MibScalar
fsBeepServerAdminStatus = _FsBeepServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 18, 1, 1),
    _FsBeepServerAdminStatus_Type()
)
fsBeepServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBeepServerAdminStatus.setStatus("current")


class _FsBeepServerRawProfile_Type(Integer32):
    """Custom type fsBeepServerRawProfile based on Integer32"""
    defaultValue = 1

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


_FsBeepServerRawProfile_Type.__name__ = "Integer32"
_FsBeepServerRawProfile_Object = MibScalar
fsBeepServerRawProfile = _FsBeepServerRawProfile_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 18, 1, 2),
    _FsBeepServerRawProfile_Type()
)
fsBeepServerRawProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBeepServerRawProfile.setStatus("current")


class _FsBeepServerIpv4PortNum_Type(Integer32):
    """Custom type fsBeepServerIpv4PortNum based on Integer32"""
    defaultValue = 601

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsBeepServerIpv4PortNum_Type.__name__ = "Integer32"
_FsBeepServerIpv4PortNum_Object = MibScalar
fsBeepServerIpv4PortNum = _FsBeepServerIpv4PortNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 18, 1, 3),
    _FsBeepServerIpv4PortNum_Type()
)
fsBeepServerIpv4PortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBeepServerIpv4PortNum.setStatus("current")


class _FsBeepServerIpv6PortNum_Type(Integer32):
    """Custom type fsBeepServerIpv6PortNum based on Integer32"""
    defaultValue = 601

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsBeepServerIpv6PortNum_Type.__name__ = "Integer32"
_FsBeepServerIpv6PortNum_Object = MibScalar
fsBeepServerIpv6PortNum = _FsBeepServerIpv6PortNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 18, 1, 4),
    _FsBeepServerIpv6PortNum_Type()
)
fsBeepServerIpv6PortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBeepServerIpv6PortNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-BEEP-SERVER-MIB",
    **{"fsBeepServer": fsBeepServer,
       "fsBeepServerScalars": fsBeepServerScalars,
       "fsBeepServerAdminStatus": fsBeepServerAdminStatus,
       "fsBeepServerRawProfile": fsBeepServerRawProfile,
       "fsBeepServerIpv4PortNum": fsBeepServerIpv4PortNum,
       "fsBeepServerIpv6PortNum": fsBeepServerIpv6PortNum}
)
