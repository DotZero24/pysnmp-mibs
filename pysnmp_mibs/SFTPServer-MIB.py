# SNMP MIB module (SFTPServer-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/SFTPServer-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:46:11 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swSFTPServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 104)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSFTPServerMgmt_ObjectIdentity = ObjectIdentity
swSFTPServerMgmt = _SwSFTPServerMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 104, 1)
)
_SwSFTPServerVersion_Type = Integer32
_SwSFTPServerVersion_Object = MibScalar
swSFTPServerVersion = _SwSFTPServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 104, 1, 1),
    _SwSFTPServerVersion_Type()
)
swSFTPServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSFTPServerVersion.setStatus("current")


class _SwSFTPServerState_Type(Integer32):
    """Custom type swSFTPServerState based on Integer32"""
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


_SwSFTPServerState_Type.__name__ = "Integer32"
_SwSFTPServerState_Object = MibScalar
swSFTPServerState = _SwSFTPServerState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 104, 1, 2),
    _SwSFTPServerState_Type()
)
swSFTPServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSFTPServerState.setStatus("current")


class _SwSFTPServerConnectionTimeout_Type(Integer32):
    """Custom type swSFTPServerConnectionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_SwSFTPServerConnectionTimeout_Type.__name__ = "Integer32"
_SwSFTPServerConnectionTimeout_Object = MibScalar
swSFTPServerConnectionTimeout = _SwSFTPServerConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 104, 1, 3),
    _SwSFTPServerConnectionTimeout_Type()
)
swSFTPServerConnectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSFTPServerConnectionTimeout.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SFTPServer-MIB",
    **{"swSFTPServerMIB": swSFTPServerMIB,
       "swSFTPServerMgmt": swSFTPServerMgmt,
       "swSFTPServerVersion": swSFTPServerVersion,
       "swSFTPServerState": swSFTPServerState,
       "swSFTPServerConnectionTimeout": swSFTPServerConnectionTimeout}
)
