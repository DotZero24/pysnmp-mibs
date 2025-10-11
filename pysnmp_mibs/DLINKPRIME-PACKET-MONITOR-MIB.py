# SNMP MIB module (DLINKPRIME-PACKET-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-PACKET-MONITOR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:03 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

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

dlinkPrimePktMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 10)
)
if mibBuilder.loadTexts:
    dlinkPrimePktMonitorMIB.setRevisions(
        ("2014-06-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpPktMonMIBNotifications_ObjectIdentity = ObjectIdentity
dpPktMonMIBNotifications = _DpPktMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 10, 0)
)
_DpPktMonMIBObjects_ObjectIdentity = ObjectIdentity
dpPktMonMIBObjects = _DpPktMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 10, 1)
)
_DpPktMonDstPort_Type = Integer32
_DpPktMonDstPort_Object = MibScalar
dpPktMonDstPort = _DpPktMonDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 10, 1, 1),
    _DpPktMonDstPort_Type()
)
dpPktMonDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpPktMonDstPort.setStatus("current")


class _DpPktMonMirrorType_Type(Integer32):
    """Custom type dpPktMonMirrorType based on Integer32"""
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
        *(("disable", 0),
          ("rx", 1),
          ("tx", 2),
          ("both", 3))
    )


_DpPktMonMirrorType_Type.__name__ = "Integer32"
_DpPktMonMirrorType_Object = MibScalar
dpPktMonMirrorType = _DpPktMonMirrorType_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 10, 1, 2),
    _DpPktMonMirrorType_Type()
)
dpPktMonMirrorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpPktMonMirrorType.setStatus("current")
_DpPktMonSrcPort_Type = PortList
_DpPktMonSrcPort_Object = MibScalar
dpPktMonSrcPort = _DpPktMonSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 10, 1, 3),
    _DpPktMonSrcPort_Type()
)
dpPktMonSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpPktMonSrcPort.setStatus("current")
_DpPktMonMIBConformance_ObjectIdentity = ObjectIdentity
dpPktMonMIBConformance = _DpPktMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 10, 2)
)
_DpPktMonMIBCompliances_ObjectIdentity = ObjectIdentity
dpPktMonMIBCompliances = _DpPktMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 10, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-PACKET-MONITOR-MIB",
    **{"dlinkPrimePktMonitorMIB": dlinkPrimePktMonitorMIB,
       "dpPktMonMIBNotifications": dpPktMonMIBNotifications,
       "dpPktMonMIBObjects": dpPktMonMIBObjects,
       "dpPktMonDstPort": dpPktMonDstPort,
       "dpPktMonMirrorType": dpPktMonMirrorType,
       "dpPktMonSrcPort": dpPktMonSrcPort,
       "dpPktMonMIBConformance": dpPktMonMIBConformance,
       "dpPktMonMIBCompliances": dpPktMonMIBCompliances}
)
