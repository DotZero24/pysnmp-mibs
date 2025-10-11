# SNMP MIB module (RUCKUS-PPPOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruckus/RUCKUS-PPPOE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:13:38 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ruckusCommonPPPOEModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonPPPOEModule")

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

ruckusPPPOEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusPPPOEObjects_ObjectIdentity = ObjectIdentity
ruckusPPPOEObjects = _RuckusPPPOEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1)
)
_RuckusPPPOEInfo_ObjectIdentity = ObjectIdentity
ruckusPPPOEInfo = _RuckusPPPOEInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1)
)


class _RuckusPPPOEUserName_Type(DisplayString):
    """Custom type ruckusPPPOEUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusPPPOEUserName_Type.__name__ = "DisplayString"
_RuckusPPPOEUserName_Object = MibScalar
ruckusPPPOEUserName = _RuckusPPPOEUserName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 1),
    _RuckusPPPOEUserName_Type()
)
ruckusPPPOEUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusPPPOEUserName.setStatus("current")


class _RuckusPPPOEPassword_Type(OctetString):
    """Custom type ruckusPPPOEPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusPPPOEPassword_Type.__name__ = "OctetString"
_RuckusPPPOEPassword_Object = MibScalar
ruckusPPPOEPassword = _RuckusPPPOEPassword_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 2),
    _RuckusPPPOEPassword_Type()
)
ruckusPPPOEPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusPPPOEPassword.setStatus("current")


class _RuckusPPPOEConnectionStatus_Type(Integer32):
    """Custom type ruckusPPPOEConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notConnected", 2))
    )


_RuckusPPPOEConnectionStatus_Type.__name__ = "Integer32"
_RuckusPPPOEConnectionStatus_Object = MibScalar
ruckusPPPOEConnectionStatus = _RuckusPPPOEConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 3),
    _RuckusPPPOEConnectionStatus_Type()
)
ruckusPPPOEConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusPPPOEConnectionStatus.setStatus("current")


class _RuckusPPPOEConnection_Type(Integer32):
    """Custom type ruckusPPPOEConnection based on Integer32"""
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
        *(("connect", 1),
          ("disConnect", 2),
          ("ok", 3),
          ("disabled", 4))
    )


_RuckusPPPOEConnection_Type.__name__ = "Integer32"
_RuckusPPPOEConnection_Object = MibScalar
ruckusPPPOEConnection = _RuckusPPPOEConnection_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 4),
    _RuckusPPPOEConnection_Type()
)
ruckusPPPOEConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusPPPOEConnection.setStatus("current")
_RuckusPPPOEIfindex_Type = InterfaceIndex
_RuckusPPPOEIfindex_Object = MibScalar
ruckusPPPOEIfindex = _RuckusPPPOEIfindex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 5),
    _RuckusPPPOEIfindex_Type()
)
ruckusPPPOEIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusPPPOEIfindex.setStatus("current")


class _RuckusPPPOEApply_Type(Integer32):
    """Custom type ruckusPPPOEApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("apply", 1)
    )


_RuckusPPPOEApply_Type.__name__ = "Integer32"
_RuckusPPPOEApply_Object = MibScalar
ruckusPPPOEApply = _RuckusPPPOEApply_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 6),
    _RuckusPPPOEApply_Type()
)
ruckusPPPOEApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusPPPOEApply.setStatus("current")
_RuckusPPPOEEvents_ObjectIdentity = ObjectIdentity
ruckusPPPOEEvents = _RuckusPPPOEEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-PPPOE-MIB",
    **{"ruckusPPPOEMIB": ruckusPPPOEMIB,
       "ruckusPPPOEObjects": ruckusPPPOEObjects,
       "ruckusPPPOEInfo": ruckusPPPOEInfo,
       "ruckusPPPOEUserName": ruckusPPPOEUserName,
       "ruckusPPPOEPassword": ruckusPPPOEPassword,
       "ruckusPPPOEConnectionStatus": ruckusPPPOEConnectionStatus,
       "ruckusPPPOEConnection": ruckusPPPOEConnection,
       "ruckusPPPOEIfindex": ruckusPPPOEIfindex,
       "ruckusPPPOEApply": ruckusPPPOEApply,
       "ruckusPPPOEEvents": ruckusPPPOEEvents}
)
