# SNMP MIB module (INFINERA-TP-DWCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-DWCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:54 2025
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

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatArbitraryPrecision,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision")

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

dwCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64)
)
if mibBuilder.loadTexts:
    dwCtpMIB.setRevisions(
        ("2017-01-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DwCtpTable_Object = MibTable
dwCtpTable = _DwCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 1)
)
if mibBuilder.loadTexts:
    dwCtpTable.setStatus("current")
_DwCtpEntry_Object = MibTableRow
dwCtpEntry = _DwCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 1, 1)
)
dwCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dwCtpEntry.setStatus("current")
_DwCtpMoID_Type = DisplayString
_DwCtpMoID_Object = MibTableColumn
dwCtpMoID = _DwCtpMoID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 1, 1, 1),
    _DwCtpMoID_Type()
)
dwCtpMoID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dwCtpMoID.setStatus("current")
_DwCtpCarrierCtpList_Type = DisplayString
_DwCtpCarrierCtpList_Object = MibTableColumn
dwCtpCarrierCtpList = _DwCtpCarrierCtpList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 1, 1, 2),
    _DwCtpCarrierCtpList_Type()
)
dwCtpCarrierCtpList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwCtpCarrierCtpList.setStatus("current")
_DwCtpTxTTI_Type = DisplayString
_DwCtpTxTTI_Object = MibTableColumn
dwCtpTxTTI = _DwCtpTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 1, 1, 3),
    _DwCtpTxTTI_Type()
)
dwCtpTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwCtpTxTTI.setStatus("current")
_DwCtpExpTTI_Type = DisplayString
_DwCtpExpTTI_Object = MibTableColumn
dwCtpExpTTI = _DwCtpExpTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 1, 1, 4),
    _DwCtpExpTTI_Type()
)
dwCtpExpTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwCtpExpTTI.setStatus("current")
_DwCtpRxTTI_Type = DisplayString
_DwCtpRxTTI_Object = MibTableColumn
dwCtpRxTTI = _DwCtpRxTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 1, 1, 5),
    _DwCtpRxTTI_Type()
)
dwCtpRxTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpRxTTI.setStatus("current")
_DwCtpTotalBW_Type = Unsigned32
_DwCtpTotalBW_Object = MibTableColumn
dwCtpTotalBW = _DwCtpTotalBW_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 1, 1, 6),
    _DwCtpTotalBW_Type()
)
dwCtpTotalBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpTotalBW.setStatus("current")
_DwCtpPropagationDelay_Type = FloatArbitraryPrecision
_DwCtpPropagationDelay_Object = MibTableColumn
dwCtpPropagationDelay = _DwCtpPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 1, 1, 7),
    _DwCtpPropagationDelay_Type()
)
dwCtpPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPropagationDelay.setStatus("current")
_DwCtpOprCarrierCtpList_Type = DisplayString
_DwCtpOprCarrierCtpList_Object = MibTableColumn
dwCtpOprCarrierCtpList = _DwCtpOprCarrierCtpList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 1, 1, 8),
    _DwCtpOprCarrierCtpList_Type()
)
dwCtpOprCarrierCtpList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwCtpOprCarrierCtpList.setStatus("current")
_DwCtpConformance_ObjectIdentity = ObjectIdentity
dwCtpConformance = _DwCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 3)
)
_DwCtpCompliances_ObjectIdentity = ObjectIdentity
dwCtpCompliances = _DwCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 3, 1)
)
_DwCtpGroups_ObjectIdentity = ObjectIdentity
dwCtpGroups = _DwCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 3, 2)
)

# Managed Objects groups

dwCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 3, 2, 1)
)
dwCtpGroup.setObjects(
      *(("INFINERA-TP-DWCTP-MIB", "dwCtpMoID"),
        ("INFINERA-TP-DWCTP-MIB", "dwCtpCarrierCtpList"),
        ("INFINERA-TP-DWCTP-MIB", "dwCtpTxTTI"),
        ("INFINERA-TP-DWCTP-MIB", "dwCtpExpTTI"),
        ("INFINERA-TP-DWCTP-MIB", "dwCtpRxTTI"),
        ("INFINERA-TP-DWCTP-MIB", "dwCtpTotalBW"),
        ("INFINERA-TP-DWCTP-MIB", "dwCtpPropagationDelay"),
        ("INFINERA-TP-DWCTP-MIB", "dwCtpOprCarrierCtpList"))
)
if mibBuilder.loadTexts:
    dwCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dwCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 64, 3, 1, 1)
)
dwCtpCompliance.setObjects(
    ("INFINERA-TP-DWCTP-MIB", "dwCtpGroup")
)
if mibBuilder.loadTexts:
    dwCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-DWCTP-MIB",
    **{"dwCtpMIB": dwCtpMIB,
       "dwCtpTable": dwCtpTable,
       "dwCtpEntry": dwCtpEntry,
       "dwCtpMoID": dwCtpMoID,
       "dwCtpCarrierCtpList": dwCtpCarrierCtpList,
       "dwCtpTxTTI": dwCtpTxTTI,
       "dwCtpExpTTI": dwCtpExpTTI,
       "dwCtpRxTTI": dwCtpRxTTI,
       "dwCtpTotalBW": dwCtpTotalBW,
       "dwCtpPropagationDelay": dwCtpPropagationDelay,
       "dwCtpOprCarrierCtpList": dwCtpOprCarrierCtpList,
       "dwCtpConformance": dwCtpConformance,
       "dwCtpCompliances": dwCtpCompliances,
       "dwCtpCompliance": dwCtpCompliance,
       "dwCtpGroups": dwCtpGroups,
       "dwCtpGroup": dwCtpGroup}
)
