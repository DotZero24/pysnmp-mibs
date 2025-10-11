# SNMP MIB module (ZTE-AN-DHCP-L3PUB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-DHCP-L3PUB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:49 2025
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

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnDhcpL3PubMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 52)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnDhcpL3PubMIBNotifs_ObjectIdentity = ObjectIdentity
zxAnDhcpL3PubMIBNotifs = _ZxAnDhcpL3PubMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 52, 0)
)
_ZxAnDhcpL3PubMIBObjects_ObjectIdentity = ObjectIdentity
zxAnDhcpL3PubMIBObjects = _ZxAnDhcpL3PubMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1)
)
_ZxAnDlGlobal_ObjectIdentity = ObjectIdentity
zxAnDlGlobal = _ZxAnDlGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 1)
)


class _ZxAnDlGlobalEnable_Type(Integer32):
    """Custom type zxAnDlGlobalEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnDlGlobalEnable_Type.__name__ = "Integer32"
_ZxAnDlGlobalEnable_Object = MibScalar
zxAnDlGlobalEnable = _ZxAnDlGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 1, 1),
    _ZxAnDlGlobalEnable_Type()
)
zxAnDlGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDlGlobalEnable.setStatus("current")


class _ZxAnDlLog_Type(Integer32):
    """Custom type zxAnDlLog based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnDlLog_Type.__name__ = "Integer32"
_ZxAnDlLog_Object = MibScalar
zxAnDlLog = _ZxAnDlLog_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 1, 2),
    _ZxAnDlLog_Type()
)
zxAnDlLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDlLog.setStatus("current")
_ZxAnDlVlanInterface_ObjectIdentity = ObjectIdentity
zxAnDlVlanInterface = _ZxAnDlVlanInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 2)
)
_ZxAnDlVlanIntTable_Object = MibTable
zxAnDlVlanIntTable = _ZxAnDlVlanIntTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnDlVlanIntTable.setStatus("current")
_ZxAnDlVlanIntEntry_Object = MibTableRow
zxAnDlVlanIntEntry = _ZxAnDlVlanIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 2, 1, 1)
)
zxAnDlVlanIntEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-L3PUB-MIB", "zxAnDlIntIndex"),
)
if mibBuilder.loadTexts:
    zxAnDlVlanIntEntry.setStatus("current")
_ZxAnDlIntIndex_Type = ZxAnIfindex
_ZxAnDlIntIndex_Object = MibTableColumn
zxAnDlIntIndex = _ZxAnDlIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 2, 1, 1, 1),
    _ZxAnDlIntIndex_Type()
)
zxAnDlIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDlIntIndex.setStatus("current")


class _ZxAnDlMode_Type(Integer32):
    """Custom type zxAnDlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nowork", 0),
          ("server", 1),
          ("relay", 2),
          ("proxy", 3))
    )


_ZxAnDlMode_Type.__name__ = "Integer32"
_ZxAnDlMode_Object = MibTableColumn
zxAnDlMode = _ZxAnDlMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 2, 1, 1, 2),
    _ZxAnDlMode_Type()
)
zxAnDlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDlMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-DHCP-L3PUB-MIB",
    **{"zxAnDhcpL3PubMIB": zxAnDhcpL3PubMIB,
       "zxAnDhcpL3PubMIBNotifs": zxAnDhcpL3PubMIBNotifs,
       "zxAnDhcpL3PubMIBObjects": zxAnDhcpL3PubMIBObjects,
       "zxAnDlGlobal": zxAnDlGlobal,
       "zxAnDlGlobalEnable": zxAnDlGlobalEnable,
       "zxAnDlLog": zxAnDlLog,
       "zxAnDlVlanInterface": zxAnDlVlanInterface,
       "zxAnDlVlanIntTable": zxAnDlVlanIntTable,
       "zxAnDlVlanIntEntry": zxAnDlVlanIntEntry,
       "zxAnDlIntIndex": zxAnDlIntIndex,
       "zxAnDlMode": zxAnDlMode}
)
