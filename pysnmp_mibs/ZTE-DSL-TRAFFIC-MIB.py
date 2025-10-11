# SNMP MIB module (ZTE-DSL-TRAFFIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-DSL-TRAFFIC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:42 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

zxDslTrafficMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxDsl_ObjectIdentity = ObjectIdentity
zxDsl = _ZxDsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004)
)
_ZxDslTrafficConfProfileTable_Object = MibTable
zxDslTrafficConfProfileTable = _ZxDslTrafficConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 1)
)
if mibBuilder.loadTexts:
    zxDslTrafficConfProfileTable.setStatus("current")
_ZxDslTrafficConfProfileEntry_Object = MibTableRow
zxDslTrafficConfProfileEntry = _ZxDslTrafficConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 1, 1)
)
zxDslTrafficConfProfileEntry.setIndexNames(
    (0, "ZTE-DSL-TRAFFIC-MIB", "zxDslTrafficConfPrfName"),
)
if mibBuilder.loadTexts:
    zxDslTrafficConfProfileEntry.setStatus("current")


class _ZxDslTrafficConfPrfName_Type(DisplayString):
    """Custom type zxDslTrafficConfPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxDslTrafficConfPrfName_Type.__name__ = "DisplayString"
_ZxDslTrafficConfPrfName_Object = MibTableColumn
zxDslTrafficConfPrfName = _ZxDslTrafficConfPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 1, 1, 1),
    _ZxDslTrafficConfPrfName_Type()
)
zxDslTrafficConfPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslTrafficConfPrfName.setStatus("current")
_ZxDslTrafficConfPrfCir_Type = Integer32
_ZxDslTrafficConfPrfCir_Object = MibTableColumn
zxDslTrafficConfPrfCir = _ZxDslTrafficConfPrfCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 1, 1, 2),
    _ZxDslTrafficConfPrfCir_Type()
)
zxDslTrafficConfPrfCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficConfPrfCir.setStatus("current")
if mibBuilder.loadTexts:
    zxDslTrafficConfPrfCir.setUnits("kbps")
_ZxDslTrafficConfPrfCbs_Type = Integer32
_ZxDslTrafficConfPrfCbs_Object = MibTableColumn
zxDslTrafficConfPrfCbs = _ZxDslTrafficConfPrfCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 1, 1, 3),
    _ZxDslTrafficConfPrfCbs_Type()
)
zxDslTrafficConfPrfCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficConfPrfCbs.setStatus("current")
if mibBuilder.loadTexts:
    zxDslTrafficConfPrfCbs.setUnits("kbytes")
_ZxDslTrafficConfPrfPir_Type = Integer32
_ZxDslTrafficConfPrfPir_Object = MibTableColumn
zxDslTrafficConfPrfPir = _ZxDslTrafficConfPrfPir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 1, 1, 4),
    _ZxDslTrafficConfPrfPir_Type()
)
zxDslTrafficConfPrfPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficConfPrfPir.setStatus("current")
if mibBuilder.loadTexts:
    zxDslTrafficConfPrfPir.setUnits("kbps")
_ZxDslTrafficConfPrfPbs_Type = Integer32
_ZxDslTrafficConfPrfPbs_Object = MibTableColumn
zxDslTrafficConfPrfPbs = _ZxDslTrafficConfPrfPbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 1, 1, 5),
    _ZxDslTrafficConfPrfPbs_Type()
)
zxDslTrafficConfPrfPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficConfPrfPbs.setStatus("current")
if mibBuilder.loadTexts:
    zxDslTrafficConfPrfPbs.setUnits("kbytes")


class _ZxDslTrafficConfPrfCosPriTrust_Type(Integer32):
    """Custom type zxDslTrafficConfPrfCosPriTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("override", 1),
          ("trust", 2))
    )


_ZxDslTrafficConfPrfCosPriTrust_Type.__name__ = "Integer32"
_ZxDslTrafficConfPrfCosPriTrust_Object = MibTableColumn
zxDslTrafficConfPrfCosPriTrust = _ZxDslTrafficConfPrfCosPriTrust_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 1, 1, 6),
    _ZxDslTrafficConfPrfCosPriTrust_Type()
)
zxDslTrafficConfPrfCosPriTrust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficConfPrfCosPriTrust.setStatus("current")
_ZxDslTrafficConfPrfCosPriority_Type = Integer32
_ZxDslTrafficConfPrfCosPriority_Object = MibTableColumn
zxDslTrafficConfPrfCosPriority = _ZxDslTrafficConfPrfCosPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 1, 1, 7),
    _ZxDslTrafficConfPrfCosPriority_Type()
)
zxDslTrafficConfPrfCosPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficConfPrfCosPriority.setStatus("current")


class _ZxDslTrafficConfPrfDiscardMode_Type(Integer32):
    """Custom type zxDslTrafficConfPrfDiscardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noDistinction", 1),
          ("lowPriorityFirst", 2))
    )


_ZxDslTrafficConfPrfDiscardMode_Type.__name__ = "Integer32"
_ZxDslTrafficConfPrfDiscardMode_Object = MibTableColumn
zxDslTrafficConfPrfDiscardMode = _ZxDslTrafficConfPrfDiscardMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 1, 1, 8),
    _ZxDslTrafficConfPrfDiscardMode_Type()
)
zxDslTrafficConfPrfDiscardMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficConfPrfDiscardMode.setStatus("current")
_ZxDslTrafficConfPrfRowStatus_Type = RowStatus
_ZxDslTrafficConfPrfRowStatus_Object = MibTableColumn
zxDslTrafficConfPrfRowStatus = _ZxDslTrafficConfPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 1, 1, 30),
    _ZxDslTrafficConfPrfRowStatus_Type()
)
zxDslTrafficConfPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficConfPrfRowStatus.setStatus("current")
_ZxDslTrafficInterfaceTable_Object = MibTable
zxDslTrafficInterfaceTable = _ZxDslTrafficInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 2)
)
if mibBuilder.loadTexts:
    zxDslTrafficInterfaceTable.setStatus("current")
_ZxDslTrafficInterfaceEntry_Object = MibTableRow
zxDslTrafficInterfaceEntry = _ZxDslTrafficInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 2, 1)
)
zxDslTrafficInterfaceEntry.setIndexNames(
    (0, "ZTE-DSL-TRAFFIC-MIB", "zxDslTrafficPort"),
    (0, "ZTE-DSL-TRAFFIC-MIB", "zxDslTrafficSvcIface"),
)
if mibBuilder.loadTexts:
    zxDslTrafficInterfaceEntry.setStatus("current")
_ZxDslTrafficPort_Type = Integer32
_ZxDslTrafficPort_Object = MibTableColumn
zxDslTrafficPort = _ZxDslTrafficPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 2, 1, 1),
    _ZxDslTrafficPort_Type()
)
zxDslTrafficPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslTrafficPort.setStatus("current")
_ZxDslTrafficSvcIface_Type = Integer32
_ZxDslTrafficSvcIface_Object = MibTableColumn
zxDslTrafficSvcIface = _ZxDslTrafficSvcIface_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 2, 1, 2),
    _ZxDslTrafficSvcIface_Type()
)
zxDslTrafficSvcIface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslTrafficSvcIface.setStatus("current")


class _ZxDslTrafficSvcIfaceType_Type(Integer32):
    """Custom type zxDslTrafficSvcIfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("vlan", 2))
    )


_ZxDslTrafficSvcIfaceType_Type.__name__ = "Integer32"
_ZxDslTrafficSvcIfaceType_Object = MibTableColumn
zxDslTrafficSvcIfaceType = _ZxDslTrafficSvcIfaceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 2, 1, 3),
    _ZxDslTrafficSvcIfaceType_Type()
)
zxDslTrafficSvcIfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficSvcIfaceType.setStatus("current")


class _ZxDslTrafficSvcEncapType_Type(Integer32):
    """Custom type zxDslTrafficSvcEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pppoe", 1),
          ("ipoe", 2),
          ("all", 3))
    )


_ZxDslTrafficSvcEncapType_Type.__name__ = "Integer32"
_ZxDslTrafficSvcEncapType_Object = MibTableColumn
zxDslTrafficSvcEncapType = _ZxDslTrafficSvcEncapType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 2, 1, 4),
    _ZxDslTrafficSvcEncapType_Type()
)
zxDslTrafficSvcEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficSvcEncapType.setStatus("current")
_ZxDslTrafficIfaceEgressPrf_Type = DisplayString
_ZxDslTrafficIfaceEgressPrf_Object = MibTableColumn
zxDslTrafficIfaceEgressPrf = _ZxDslTrafficIfaceEgressPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 2, 1, 5),
    _ZxDslTrafficIfaceEgressPrf_Type()
)
zxDslTrafficIfaceEgressPrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficIfaceEgressPrf.setStatus("current")
_ZxDslTrafficIfaceIngressPrf_Type = DisplayString
_ZxDslTrafficIfaceIngressPrf_Object = MibTableColumn
zxDslTrafficIfaceIngressPrf = _ZxDslTrafficIfaceIngressPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 2, 1, 6),
    _ZxDslTrafficIfaceIngressPrf_Type()
)
zxDslTrafficIfaceIngressPrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficIfaceIngressPrf.setStatus("current")
_ZxDslTrafficIfaceRowStatus_Type = RowStatus
_ZxDslTrafficIfaceRowStatus_Object = MibTableColumn
zxDslTrafficIfaceRowStatus = _ZxDslTrafficIfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 2, 1, 20),
    _ZxDslTrafficIfaceRowStatus_Type()
)
zxDslTrafficIfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficIfaceRowStatus.setStatus("current")
_ZxDslTrafficIfTable_Object = MibTable
zxDslTrafficIfTable = _ZxDslTrafficIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 3)
)
if mibBuilder.loadTexts:
    zxDslTrafficIfTable.setStatus("current")
_ZxDslTrafficIfEntry_Object = MibTableRow
zxDslTrafficIfEntry = _ZxDslTrafficIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 3, 1)
)
zxDslTrafficIfEntry.setIndexNames(
    (0, "ZTE-DSL-TRAFFIC-MIB", "zxDslTrafficIfIndex"),
    (0, "ZTE-DSL-TRAFFIC-MIB", "zxDslTrafficIfCircuitType"),
    (0, "ZTE-DSL-TRAFFIC-MIB", "zxDslTrafficIfLogicalId"),
)
if mibBuilder.loadTexts:
    zxDslTrafficIfEntry.setStatus("current")
_ZxDslTrafficIfIndex_Type = Integer32
_ZxDslTrafficIfIndex_Object = MibTableColumn
zxDslTrafficIfIndex = _ZxDslTrafficIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 3, 1, 1),
    _ZxDslTrafficIfIndex_Type()
)
zxDslTrafficIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslTrafficIfIndex.setStatus("current")


class _ZxDslTrafficIfCircuitType_Type(Integer32):
    """Custom type zxDslTrafficIfCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridgePort", 1),
          ("vlan", 2))
    )


_ZxDslTrafficIfCircuitType_Type.__name__ = "Integer32"
_ZxDslTrafficIfCircuitType_Object = MibTableColumn
zxDslTrafficIfCircuitType = _ZxDslTrafficIfCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 3, 1, 2),
    _ZxDslTrafficIfCircuitType_Type()
)
zxDslTrafficIfCircuitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslTrafficIfCircuitType.setStatus("current")
_ZxDslTrafficIfLogicalId_Type = Integer32
_ZxDslTrafficIfLogicalId_Object = MibTableColumn
zxDslTrafficIfLogicalId = _ZxDslTrafficIfLogicalId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 3, 1, 3),
    _ZxDslTrafficIfLogicalId_Type()
)
zxDslTrafficIfLogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslTrafficIfLogicalId.setStatus("current")


class _ZxDslTrafficIfEthType_Type(Integer32):
    """Custom type zxDslTrafficIfEthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("pppoe", 2),
          ("ipoe", 3))
    )


_ZxDslTrafficIfEthType_Type.__name__ = "Integer32"
_ZxDslTrafficIfEthType_Object = MibTableColumn
zxDslTrafficIfEthType = _ZxDslTrafficIfEthType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 3, 1, 4),
    _ZxDslTrafficIfEthType_Type()
)
zxDslTrafficIfEthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficIfEthType.setStatus("current")


class _ZxDslTrafficIfEgressPrf_Type(DisplayString):
    """Custom type zxDslTrafficIfEgressPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxDslTrafficIfEgressPrf_Type.__name__ = "DisplayString"
_ZxDslTrafficIfEgressPrf_Object = MibTableColumn
zxDslTrafficIfEgressPrf = _ZxDslTrafficIfEgressPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 3, 1, 5),
    _ZxDslTrafficIfEgressPrf_Type()
)
zxDslTrafficIfEgressPrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficIfEgressPrf.setStatus("current")


class _ZxDslTrafficIfIngressPrf_Type(DisplayString):
    """Custom type zxDslTrafficIfIngressPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxDslTrafficIfIngressPrf_Type.__name__ = "DisplayString"
_ZxDslTrafficIfIngressPrf_Object = MibTableColumn
zxDslTrafficIfIngressPrf = _ZxDslTrafficIfIngressPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 3, 1, 6),
    _ZxDslTrafficIfIngressPrf_Type()
)
zxDslTrafficIfIngressPrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficIfIngressPrf.setStatus("current")
_ZxDslTrafficIfRowStatus_Type = RowStatus
_ZxDslTrafficIfRowStatus_Object = MibTableColumn
zxDslTrafficIfRowStatus = _ZxDslTrafficIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 3, 1, 50),
    _ZxDslTrafficIfRowStatus_Type()
)
zxDslTrafficIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslTrafficIfRowStatus.setStatus("current")
_ZxDslTrafficMgmtGlobalObjects_ObjectIdentity = ObjectIdentity
zxDslTrafficMgmtGlobalObjects = _ZxDslTrafficMgmtGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 50)
)


class _ZxDslTrafficMgmtCapabilities_Type(Bits):
    """Custom type zxDslTrafficMgmtCapabilities based on Bits"""
    namedValues = NamedValues(
        ("supportZxDslTrafficIfTable", 0)
    )

_ZxDslTrafficMgmtCapabilities_Type.__name__ = "Bits"
_ZxDslTrafficMgmtCapabilities_Object = MibScalar
zxDslTrafficMgmtCapabilities = _ZxDslTrafficMgmtCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 42, 50, 1),
    _ZxDslTrafficMgmtCapabilities_Type()
)
zxDslTrafficMgmtCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslTrafficMgmtCapabilities.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-DSL-TRAFFIC-MIB",
    **{"zte": zte,
       "zxDsl": zxDsl,
       "zxDslTrafficMgmt": zxDslTrafficMgmt,
       "zxDslTrafficConfProfileTable": zxDslTrafficConfProfileTable,
       "zxDslTrafficConfProfileEntry": zxDslTrafficConfProfileEntry,
       "zxDslTrafficConfPrfName": zxDslTrafficConfPrfName,
       "zxDslTrafficConfPrfCir": zxDslTrafficConfPrfCir,
       "zxDslTrafficConfPrfCbs": zxDslTrafficConfPrfCbs,
       "zxDslTrafficConfPrfPir": zxDslTrafficConfPrfPir,
       "zxDslTrafficConfPrfPbs": zxDslTrafficConfPrfPbs,
       "zxDslTrafficConfPrfCosPriTrust": zxDslTrafficConfPrfCosPriTrust,
       "zxDslTrafficConfPrfCosPriority": zxDslTrafficConfPrfCosPriority,
       "zxDslTrafficConfPrfDiscardMode": zxDslTrafficConfPrfDiscardMode,
       "zxDslTrafficConfPrfRowStatus": zxDslTrafficConfPrfRowStatus,
       "zxDslTrafficInterfaceTable": zxDslTrafficInterfaceTable,
       "zxDslTrafficInterfaceEntry": zxDslTrafficInterfaceEntry,
       "zxDslTrafficPort": zxDslTrafficPort,
       "zxDslTrafficSvcIface": zxDslTrafficSvcIface,
       "zxDslTrafficSvcIfaceType": zxDslTrafficSvcIfaceType,
       "zxDslTrafficSvcEncapType": zxDslTrafficSvcEncapType,
       "zxDslTrafficIfaceEgressPrf": zxDslTrafficIfaceEgressPrf,
       "zxDslTrafficIfaceIngressPrf": zxDslTrafficIfaceIngressPrf,
       "zxDslTrafficIfaceRowStatus": zxDslTrafficIfaceRowStatus,
       "zxDslTrafficIfTable": zxDslTrafficIfTable,
       "zxDslTrafficIfEntry": zxDslTrafficIfEntry,
       "zxDslTrafficIfIndex": zxDslTrafficIfIndex,
       "zxDslTrafficIfCircuitType": zxDslTrafficIfCircuitType,
       "zxDslTrafficIfLogicalId": zxDslTrafficIfLogicalId,
       "zxDslTrafficIfEthType": zxDslTrafficIfEthType,
       "zxDslTrafficIfEgressPrf": zxDslTrafficIfEgressPrf,
       "zxDslTrafficIfIngressPrf": zxDslTrafficIfIngressPrf,
       "zxDslTrafficIfRowStatus": zxDslTrafficIfRowStatus,
       "zxDslTrafficMgmtGlobalObjects": zxDslTrafficMgmtGlobalObjects,
       "zxDslTrafficMgmtCapabilities": zxDslTrafficMgmtCapabilities}
)
