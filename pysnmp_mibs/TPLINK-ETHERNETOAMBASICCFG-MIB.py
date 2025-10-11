# SNMP MIB module (TPLINK-ETHERNETOAMBASICCFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-ETHERNETOAMBASICCFG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:56:43 2025
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

(ethernetOamBasicConfig,) = mibBuilder.importSymbols(
    "TPLINK-ETHERNETOAM-MIB",
    "ethernetOamBasicConfig")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EthernetOamBasicCfgTable_Object = MibTable
ethernetOamBasicCfgTable = _EthernetOamBasicCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ethernetOamBasicCfgTable.setStatus("current")
_EthernetOamBasicCfgEntry_Object = MibTableRow
ethernetOamBasicCfgEntry = _EthernetOamBasicCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1)
)
ethernetOamBasicCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ethernetOamBasicCfgEntry.setStatus("current")
_EthernetOamBasicCfgPort_Type = DisplayString
_EthernetOamBasicCfgPort_Object = MibTableColumn
ethernetOamBasicCfgPort = _EthernetOamBasicCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1, 1),
    _EthernetOamBasicCfgPort_Type()
)
ethernetOamBasicCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamBasicCfgPort.setStatus("current")


class _EthernetOamBasicCfgMode_Type(Integer32):
    """Custom type ethernetOamBasicCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("passive", 0),
          ("active", 1))
    )


_EthernetOamBasicCfgMode_Type.__name__ = "Integer32"
_EthernetOamBasicCfgMode_Object = MibTableColumn
ethernetOamBasicCfgMode = _EthernetOamBasicCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1, 2),
    _EthernetOamBasicCfgMode_Type()
)
ethernetOamBasicCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOamBasicCfgMode.setStatus("current")


class _EthernetOamBasicCfgState_Type(Integer32):
    """Custom type ethernetOamBasicCfgState based on Integer32"""
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


_EthernetOamBasicCfgState_Type.__name__ = "Integer32"
_EthernetOamBasicCfgState_Object = MibTableColumn
ethernetOamBasicCfgState = _EthernetOamBasicCfgState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1, 3),
    _EthernetOamBasicCfgState_Type()
)
ethernetOamBasicCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOamBasicCfgState.setStatus("current")


class _EthernetOamBasicCfgLAG_Type(OctetString):
    """Custom type ethernetOamBasicCfgLAG based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EthernetOamBasicCfgLAG_Type.__name__ = "OctetString"
_EthernetOamBasicCfgLAG_Object = MibTableColumn
ethernetOamBasicCfgLAG = _EthernetOamBasicCfgLAG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1, 4),
    _EthernetOamBasicCfgLAG_Type()
)
ethernetOamBasicCfgLAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamBasicCfgLAG.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-ETHERNETOAMBASICCFG-MIB",
    **{"ethernetOamBasicCfgTable": ethernetOamBasicCfgTable,
       "ethernetOamBasicCfgEntry": ethernetOamBasicCfgEntry,
       "ethernetOamBasicCfgPort": ethernetOamBasicCfgPort,
       "ethernetOamBasicCfgMode": ethernetOamBasicCfgMode,
       "ethernetOamBasicCfgState": ethernetOamBasicCfgState,
       "ethernetOamBasicCfgLAG": ethernetOamBasicCfgLAG}
)
