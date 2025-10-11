# SNMP MIB module (TPLINK-IP-SOURCE-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-IP-SOURCE-GUARD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:56:14 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkIpSourceGuardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29)
)
if mibBuilder.loadTexts:
    tplinkIpSourceGuardMIB.setRevisions(
        ("2012-12-13 09:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkIpSourceGuardMIBObjects_ObjectIdentity = ObjectIdentity
tplinkIpSourceGuardMIBObjects = _TplinkIpSourceGuardMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1)
)
_TpIpSourceGuardConfig_ObjectIdentity = ObjectIdentity
tpIpSourceGuardConfig = _TpIpSourceGuardConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1)
)


class _TpIpSourceGuardLoggingConfig_Type(Integer32):
    """Custom type tpIpSourceGuardLoggingConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpIpSourceGuardLoggingConfig_Type.__name__ = "Integer32"
_TpIpSourceGuardLoggingConfig_Object = MibScalar
tpIpSourceGuardLoggingConfig = _TpIpSourceGuardLoggingConfig_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 1),
    _TpIpSourceGuardLoggingConfig_Type()
)
tpIpSourceGuardLoggingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIpSourceGuardLoggingConfig.setStatus("current")
_TpIpSourceGuardConfigTable_Object = MibTable
tpIpSourceGuardConfigTable = _TpIpSourceGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tpIpSourceGuardConfigTable.setStatus("current")
_TpIpSourceGuardConfigEntry_Object = MibTableRow
tpIpSourceGuardConfigEntry = _TpIpSourceGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 2, 1)
)
tpIpSourceGuardConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpIpSourceGuardConfigEntry.setStatus("current")


class _TpIpSourceGuardConfigPort_Type(OctetString):
    """Custom type tpIpSourceGuardConfigPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpIpSourceGuardConfigPort_Type.__name__ = "OctetString"
_TpIpSourceGuardConfigPort_Object = MibTableColumn
tpIpSourceGuardConfigPort = _TpIpSourceGuardConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 2, 1, 1),
    _TpIpSourceGuardConfigPort_Type()
)
tpIpSourceGuardConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpSourceGuardConfigPort.setStatus("current")


class _TpIpSourceGuardConfigType_Type(Integer32):
    """Custom type tpIpSourceGuardConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("sip", 1),
          ("sip-mac", 2))
    )


_TpIpSourceGuardConfigType_Type.__name__ = "Integer32"
_TpIpSourceGuardConfigType_Object = MibTableColumn
tpIpSourceGuardConfigType = _TpIpSourceGuardConfigType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 2, 1, 2),
    _TpIpSourceGuardConfigType_Type()
)
tpIpSourceGuardConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIpSourceGuardConfigType.setStatus("current")


class _TpIpSourceGuardConfigPortLag_Type(OctetString):
    """Custom type tpIpSourceGuardConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpIpSourceGuardConfigPortLag_Type.__name__ = "OctetString"
_TpIpSourceGuardConfigPortLag_Object = MibTableColumn
tpIpSourceGuardConfigPortLag = _TpIpSourceGuardConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 2, 1, 3),
    _TpIpSourceGuardConfigPortLag_Type()
)
tpIpSourceGuardConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpSourceGuardConfigPortLag.setStatus("current")
_TplinkIpSourceGuardNotifications_ObjectIdentity = ObjectIdentity
tplinkIpSourceGuardNotifications = _TplinkIpSourceGuardNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 2)
)

# Managed Objects groups


# Notification objects

tpIpSourceGuardRxIllegalIpPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 29, 2, 1)
)
if mibBuilder.loadTexts:
    tpIpSourceGuardRxIllegalIpPacket.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-IP-SOURCE-GUARD-MIB",
    **{"tplinkIpSourceGuardMIB": tplinkIpSourceGuardMIB,
       "tplinkIpSourceGuardMIBObjects": tplinkIpSourceGuardMIBObjects,
       "tpIpSourceGuardConfig": tpIpSourceGuardConfig,
       "tpIpSourceGuardLoggingConfig": tpIpSourceGuardLoggingConfig,
       "tpIpSourceGuardConfigTable": tpIpSourceGuardConfigTable,
       "tpIpSourceGuardConfigEntry": tpIpSourceGuardConfigEntry,
       "tpIpSourceGuardConfigPort": tpIpSourceGuardConfigPort,
       "tpIpSourceGuardConfigType": tpIpSourceGuardConfigType,
       "tpIpSourceGuardConfigPortLag": tpIpSourceGuardConfigPortLag,
       "tplinkIpSourceGuardNotifications": tplinkIpSourceGuardNotifications,
       "tpIpSourceGuardRxIllegalIpPacket": tpIpSourceGuardRxIllegalIpPacket}
)
