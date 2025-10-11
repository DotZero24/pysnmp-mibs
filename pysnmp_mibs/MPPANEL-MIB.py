# SNMP MIB module (MPPANEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MPPANEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:09 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 ObjectName,
 ObjectSyntax,
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
    "ObjectName",
    "ObjectSyntax",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mpPanelMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PanelTable_Object = MibTable
panelTable = _PanelTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 1)
)
if mibBuilder.loadTexts:
    panelTable.setStatus("current")
_PanelEntry_Object = MibTableRow
panelEntry = _PanelEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 1, 1)
)
panelEntry.setIndexNames(
    (0, "MPPANEL-MIB", "panelIndex"),
)
if mibBuilder.loadTexts:
    panelEntry.setStatus("current")
_PanelIndex_Type = DisplayString
_PanelIndex_Object = MibTableColumn
panelIndex = _PanelIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 1, 1, 1),
    _PanelIndex_Type()
)
panelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelIndex.setStatus("current")
_PanelType_Type = Integer32
_PanelType_Object = MibTableColumn
panelType = _PanelType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 1, 1, 2),
    _PanelType_Type()
)
panelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelType.setStatus("current")
_PanelIfIndex_Type = Integer32
_PanelIfIndex_Object = MibTableColumn
panelIfIndex = _PanelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 1, 1, 3),
    _PanelIfIndex_Type()
)
panelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelIfIndex.setStatus("current")
_CE1TimeslotsTable_Object = MibTable
cE1TimeslotsTable = _CE1TimeslotsTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cE1TimeslotsTable.setStatus("current")
_CE1TimeslotsEntry_Object = MibTableRow
cE1TimeslotsEntry = _CE1TimeslotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 3, 1)
)
cE1TimeslotsEntry.setIndexNames(
    (0, "MPPANEL-MIB", "cE1IfIndex"),
)
if mibBuilder.loadTexts:
    cE1TimeslotsEntry.setStatus("current")
_CE1IfIndex_Type = Integer32
_CE1IfIndex_Object = MibTableColumn
cE1IfIndex = _CE1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 3, 1, 1),
    _CE1IfIndex_Type()
)
cE1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cE1IfIndex.setStatus("current")
_CE1Timeslots_Type = Integer32
_CE1Timeslots_Object = MibTableColumn
cE1Timeslots = _CE1Timeslots_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 3, 1, 2),
    _CE1Timeslots_Type()
)
cE1Timeslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cE1Timeslots.setStatus("current")
_MprSwPortTable_Object = MibTable
mprSwPortTable = _MprSwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 10)
)
if mibBuilder.loadTexts:
    mprSwPortTable.setStatus("current")
_MprSwPortEntry_Object = MibTableRow
mprSwPortEntry = _MprSwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 10, 1)
)
mprSwPortEntry.setIndexNames(
    (0, "MPPANEL-MIB", "mprSwSlotNo"),
    (0, "MPPANEL-MIB", "mprSwPortNo"),
)
if mibBuilder.loadTexts:
    mprSwPortEntry.setStatus("current")
_MprSwSlotNo_Type = Integer32
_MprSwSlotNo_Object = MibTableColumn
mprSwSlotNo = _MprSwSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 10, 1, 1),
    _MprSwSlotNo_Type()
)
mprSwSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mprSwSlotNo.setStatus("current")
_MprSwPortNo_Type = Integer32
_MprSwPortNo_Object = MibTableColumn
mprSwPortNo = _MprSwPortNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 10, 1, 2),
    _MprSwPortNo_Type()
)
mprSwPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mprSwPortNo.setStatus("current")


class _MprSwPortLinkStatus_Type(Integer32):
    """Custom type mprSwPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_MprSwPortLinkStatus_Type.__name__ = "Integer32"
_MprSwPortLinkStatus_Object = MibTableColumn
mprSwPortLinkStatus = _MprSwPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 10, 1, 3),
    _MprSwPortLinkStatus_Type()
)
mprSwPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mprSwPortLinkStatus.setStatus("current")


class _MprSwPortSpeed_Type(Integer32):
    """Custom type mprSwPortSpeed based on Integer32"""
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
        *(("unkown", 1),
          ("speed10", 2),
          ("speed100", 3),
          ("speed1000", 4))
    )


_MprSwPortSpeed_Type.__name__ = "Integer32"
_MprSwPortSpeed_Object = MibTableColumn
mprSwPortSpeed = _MprSwPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 10, 1, 4),
    _MprSwPortSpeed_Type()
)
mprSwPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mprSwPortSpeed.setStatus("current")


class _MprSwPortDeplux_Type(Integer32):
    """Custom type mprSwPortDeplux based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unkown", 1),
          ("half", 2),
          ("full", 3))
    )


_MprSwPortDeplux_Type.__name__ = "Integer32"
_MprSwPortDeplux_Object = MibTableColumn
mprSwPortDeplux = _MprSwPortDeplux_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 1, 10, 1, 5),
    _MprSwPortDeplux_Type()
)
mprSwPortDeplux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mprSwPortDeplux.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPPANEL-MIB",
    **{"mpPanelMib": mpPanelMib,
       "panelTable": panelTable,
       "panelEntry": panelEntry,
       "panelIndex": panelIndex,
       "panelType": panelType,
       "panelIfIndex": panelIfIndex,
       "cE1TimeslotsTable": cE1TimeslotsTable,
       "cE1TimeslotsEntry": cE1TimeslotsEntry,
       "cE1IfIndex": cE1IfIndex,
       "cE1Timeslots": cE1Timeslots,
       "mprSwPortTable": mprSwPortTable,
       "mprSwPortEntry": mprSwPortEntry,
       "mprSwSlotNo": mprSwSlotNo,
       "mprSwPortNo": mprSwPortNo,
       "mprSwPortLinkStatus": mprSwPortLinkStatus,
       "mprSwPortSpeed": mprSwPortSpeed,
       "mprSwPortDeplux": mprSwPortDeplux}
)
