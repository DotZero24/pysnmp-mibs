# SNMP MIB module (DLINKPRIME-STORM-CTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-STORM-CTRL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:46:39 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

dlinkPrimeStormCtrlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 17)
)
if mibBuilder.loadTexts:
    dlinkPrimeStormCtrlMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DpStormCtlTrafficType(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("broadcast", 2),
          ("multicast", 3),
          ("unicast", 4))
    )



class DpStormCtlThrTypeValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("noLimit", 1),
          ("limit_512Kbps", 2),
          ("limit_1Mbps", 3),
          ("limit_2Mbps", 4),
          ("limit_4Mbps", 5),
          ("limit_8Mbps", 6),
          ("limit_16Mbps", 7),
          ("limit_32Mbps", 8),
          ("limit_64Mbps", 9),
          ("limit_128Mbps", 10),
          ("limit_256Mbps", 11),
          ("limit_512Mbps", 12))
    )



# MIB Managed Objects in the order of their OIDs

_DpStormCtrlMIBObjects_ObjectIdentity = ObjectIdentity
dpStormCtrlMIBObjects = _DpStormCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 17, 1)
)
_DpStormCtrlTrafficInfoTable_Object = MibTable
dpStormCtrlTrafficInfoTable = _DpStormCtrlTrafficInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 17, 1, 1)
)
if mibBuilder.loadTexts:
    dpStormCtrlTrafficInfoTable.setStatus("current")
_DpStormCtrlTrafficInfoEntry_Object = MibTableRow
dpStormCtrlTrafficInfoEntry = _DpStormCtrlTrafficInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 17, 1, 1, 1)
)
dpStormCtrlTrafficInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dpStormCtrlTrafficInfoEntry.setStatus("current")
_DpStormCtrlCurTrafficType_Type = DpStormCtlTrafficType
_DpStormCtrlCurTrafficType_Object = MibTableColumn
dpStormCtrlCurTrafficType = _DpStormCtrlCurTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 17, 1, 1, 1, 1),
    _DpStormCtrlCurTrafficType_Type()
)
dpStormCtrlCurTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpStormCtrlCurTrafficType.setStatus("current")
_DpStormCtrlCurTrafficValue_Type = DpStormCtlThrTypeValue
_DpStormCtrlCurTrafficValue_Object = MibTableColumn
dpStormCtrlCurTrafficValue = _DpStormCtrlCurTrafficValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 17, 1, 1, 1, 2),
    _DpStormCtrlCurTrafficValue_Type()
)
dpStormCtrlCurTrafficValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpStormCtrlCurTrafficValue.setStatus("current")
_DpStormCtrlMIBConformance_ObjectIdentity = ObjectIdentity
dpStormCtrlMIBConformance = _DpStormCtrlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 17, 2)
)
_DpStormCtrlCompliances_ObjectIdentity = ObjectIdentity
dpStormCtrlCompliances = _DpStormCtrlCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 17, 2, 1)
)
_DpStormCtrlGroup_ObjectIdentity = ObjectIdentity
dpStormCtrlGroup = _DpStormCtrlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 17, 2, 2)
)

# Managed Objects groups

dpStormCtrlBaiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 17, 2, 2, 1)
)
dpStormCtrlBaiscGroup.setObjects(
      *(("DLINKPRIME-STORM-CTRL-MIB", "dpStormCtrlCurTrafficType"),
        ("DLINKPRIME-STORM-CTRL-MIB", "dpStormCtrlCurTrafficValue"))
)
if mibBuilder.loadTexts:
    dpStormCtrlBaiscGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpStormCtrlCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 17, 2, 1, 1)
)
dpStormCtrlCompliance.setObjects(
    ("DLINKPRIME-STORM-CTRL-MIB", "dpStormCtrlBaiscGroup")
)
if mibBuilder.loadTexts:
    dpStormCtrlCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-STORM-CTRL-MIB",
    **{"DpStormCtlTrafficType": DpStormCtlTrafficType,
       "DpStormCtlThrTypeValue": DpStormCtlThrTypeValue,
       "dlinkPrimeStormCtrlMIB": dlinkPrimeStormCtrlMIB,
       "dpStormCtrlMIBObjects": dpStormCtrlMIBObjects,
       "dpStormCtrlTrafficInfoTable": dpStormCtrlTrafficInfoTable,
       "dpStormCtrlTrafficInfoEntry": dpStormCtrlTrafficInfoEntry,
       "dpStormCtrlCurTrafficType": dpStormCtrlCurTrafficType,
       "dpStormCtrlCurTrafficValue": dpStormCtrlCurTrafficValue,
       "dpStormCtrlMIBConformance": dpStormCtrlMIBConformance,
       "dpStormCtrlCompliances": dpStormCtrlCompliances,
       "dpStormCtrlCompliance": dpStormCtrlCompliance,
       "dpStormCtrlGroup": dpStormCtrlGroup,
       "dpStormCtrlBaiscGroup": dpStormCtrlBaiscGroup}
)
