# SNMP MIB module (TPLINK-ETHERNETOAMLINKMONCFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-ETHERNETOAMLINKMONCFG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:15 2025
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

(ethernetOamLinkMonConfig,) = mibBuilder.importSymbols(
    "TPLINK-ETHERNETOAM-MIB",
    "ethernetOamLinkMonConfig")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EthernetOamLinkMonCfgTable_Object = MibTable
ethernetOamLinkMonCfgTable = _EthernetOamLinkMonCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ethernetOamLinkMonCfgTable.setStatus("current")
_EthernetOamLinkMonCfgEntry_Object = MibTableRow
ethernetOamLinkMonCfgEntry = _EthernetOamLinkMonCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1)
)
ethernetOamLinkMonCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TPLINK-ETHERNETOAMLINKMONCFG-MIB", "ethernetOamLinkMonCfgEvent"),
)
if mibBuilder.loadTexts:
    ethernetOamLinkMonCfgEntry.setStatus("current")
_EthernetOamLinkMonCfgPort_Type = DisplayString
_EthernetOamLinkMonCfgPort_Object = MibTableColumn
ethernetOamLinkMonCfgPort = _EthernetOamLinkMonCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1, 1),
    _EthernetOamLinkMonCfgPort_Type()
)
ethernetOamLinkMonCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamLinkMonCfgPort.setStatus("current")


class _EthernetOamLinkMonCfgEvent_Type(Integer32):
    """Custom type ethernetOamLinkMonCfgEvent based on Integer32"""
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
        *(("symbol-period", 1),
          ("frame", 2),
          ("frame-period", 3),
          ("frame-seconds", 4))
    )


_EthernetOamLinkMonCfgEvent_Type.__name__ = "Integer32"
_EthernetOamLinkMonCfgEvent_Object = MibTableColumn
ethernetOamLinkMonCfgEvent = _EthernetOamLinkMonCfgEvent_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1, 2),
    _EthernetOamLinkMonCfgEvent_Type()
)
ethernetOamLinkMonCfgEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamLinkMonCfgEvent.setStatus("current")
_EthernetOamLinkMonCfgThreshold_Type = Unsigned32
_EthernetOamLinkMonCfgThreshold_Object = MibTableColumn
ethernetOamLinkMonCfgThreshold = _EthernetOamLinkMonCfgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1, 3),
    _EthernetOamLinkMonCfgThreshold_Type()
)
ethernetOamLinkMonCfgThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOamLinkMonCfgThreshold.setStatus("current")
_EthernetOamLinkMonCfgWindow_Type = Unsigned32
_EthernetOamLinkMonCfgWindow_Object = MibTableColumn
ethernetOamLinkMonCfgWindow = _EthernetOamLinkMonCfgWindow_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1, 4),
    _EthernetOamLinkMonCfgWindow_Type()
)
ethernetOamLinkMonCfgWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOamLinkMonCfgWindow.setStatus("current")


class _EthernetOamLinkMonCfgNotify_Type(Integer32):
    """Custom type ethernetOamLinkMonCfgNotify based on Integer32"""
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


_EthernetOamLinkMonCfgNotify_Type.__name__ = "Integer32"
_EthernetOamLinkMonCfgNotify_Object = MibTableColumn
ethernetOamLinkMonCfgNotify = _EthernetOamLinkMonCfgNotify_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1, 5),
    _EthernetOamLinkMonCfgNotify_Type()
)
ethernetOamLinkMonCfgNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOamLinkMonCfgNotify.setStatus("current")


class _EthernetOamLinkMonCfgLAG_Type(OctetString):
    """Custom type ethernetOamLinkMonCfgLAG based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EthernetOamLinkMonCfgLAG_Type.__name__ = "OctetString"
_EthernetOamLinkMonCfgLAG_Object = MibTableColumn
ethernetOamLinkMonCfgLAG = _EthernetOamLinkMonCfgLAG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2, 1, 1, 6),
    _EthernetOamLinkMonCfgLAG_Type()
)
ethernetOamLinkMonCfgLAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamLinkMonCfgLAG.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-ETHERNETOAMLINKMONCFG-MIB",
    **{"ethernetOamLinkMonCfgTable": ethernetOamLinkMonCfgTable,
       "ethernetOamLinkMonCfgEntry": ethernetOamLinkMonCfgEntry,
       "ethernetOamLinkMonCfgPort": ethernetOamLinkMonCfgPort,
       "ethernetOamLinkMonCfgEvent": ethernetOamLinkMonCfgEvent,
       "ethernetOamLinkMonCfgThreshold": ethernetOamLinkMonCfgThreshold,
       "ethernetOamLinkMonCfgWindow": ethernetOamLinkMonCfgWindow,
       "ethernetOamLinkMonCfgNotify": ethernetOamLinkMonCfgNotify,
       "ethernetOamLinkMonCfgLAG": ethernetOamLinkMonCfgLAG}
)
