# SNMP MIB module (SL-XPDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smartoptics/SL-XPDR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:11:34 2025
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

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(sitelight,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "sitelight")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slXpdr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XpdrServiceType(TextualConvention, Integer32):
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              170,
              171,
              1701)
        )
    )
    namedValues = NamedValues(
        *(("ds3Sts1", 1),
          ("fe", 2),
          ("escon", 3),
          ("dvbVideo", 4),
          ("fc1gFicon", 5),
          ("gbE", 6),
          ("fc2g", 7),
          ("oc3Stm1", 8),
          ("oc12Stm4", 9),
          ("oc48Stm16", 10),
          ("other", 11),
          ("fc4g", 12),
          ("infiniband25G", 13),
          ("otn27g", 14),
          ("oc24gpon", 15),
          ("smpteSdi", 16),
          ("copperFe", 17),
          ("copperGbe", 18),
          ("mux2GbE", 19),
          ("mux4GbE", 20),
          ("xpdr5G", 21),
          ("ficon1g", 22),
          ("ficon2g", 23),
          ("stm1", 24),
          ("stm4", 25),
          ("stm16", 26),
          ("gpon248", 27),
          ("ficon4g", 28),
          ("eth10m", 29),
          ("xfp10oc192", 30),
          ("xfp10stm64", 31),
          ("xfp10GbEWan", 32),
          ("xfp10GbELan", 33),
          ("xfp10otu2", 34),
          ("xfp10GFC", 35),
          ("xfp10GbEWanStm64", 36),
          ("mux1GbE", 37),
          ("mux1GbERegen", 38),
          ("mux2GbERegen", 39),
          ("mux4GbERegen", 40),
          ("fc8g", 41),
          ("ficon8g", 42),
          ("mux10GbE", 43),
          ("syncEgbE", 44),
          ("otu1e", 50),
          ("otu2e", 51),
          ("otu1f", 52),
          ("otu2f", 53),
          ("oc192ToOtu2", 54),
          ("stm64ToOtu2", 55),
          ("gbe10WanToOtu2", 56),
          ("gbe10LanToOtu2A", 57),
          ("gbe10LanToOtu1e", 58),
          ("gbe10LanToOtu2e", 59),
          ("gbe10LanToOtu2B", 60),
          ("fc10LanToOtu1f", 61),
          ("fc10LanToOtu2f", 62),
          ("fc8LanToOtu2", 63),
          ("otu3", 64),
          ("oc768", 65),
          ("stm256", 66),
          ("otu4", 67),
          ("gbe40lan", 68),
          ("gbe100lan", 69),
          ("fc16g", 70),
          ("smpteHdSdi", 71),
          ("smpteSdSdi", 72),
          ("smpte3gSdi", 73),
          ("smpte3dSdi", 74),
          ("smpteHdSdiNtsc", 75),
          ("smpte3gSdiNtsc", 76),
          ("fc16gNoIsl", 77),
          ("cpri1", 81),
          ("cpri2", 82),
          ("cpri3", 83),
          ("cpri4", 84),
          ("cpri5", 85),
          ("cpri6", 86),
          ("cpri7", 87),
          ("enc10GbELan", 91),
          ("enc1GbELan", 92),
          ("encfc1g", 93),
          ("encfc2g", 94),
          ("encfc4g", 95),
          ("encfc8g", 96),
          ("encfc16g", 97),
          ("encfc10g", 98),
          ("copper10m", 170),
          ("copper10mAn", 171),
          ("copperFeAn", 1701))
    )



# MIB Managed Objects in the order of their OIDs

_SlXpdrConn_ObjectIdentity = ObjectIdentity
slXpdrConn = _SlXpdrConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1)
)
_XpdrConnConfigTable_Object = MibTable
xpdrConnConfigTable = _XpdrConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    xpdrConnConfigTable.setStatus("current")
_XpdrConnConfigEntry_Object = MibTableRow
xpdrConnConfigEntry = _XpdrConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1)
)
xpdrConnConfigEntry.setIndexNames(
    (0, "SL-XPDR-MIB", "xpdrConnConfigIf1"),
    (0, "SL-XPDR-MIB", "xpdrConnConfigIf2"),
)
if mibBuilder.loadTexts:
    xpdrConnConfigEntry.setStatus("current")
_XpdrConnConfigIf1_Type = InterfaceIndex
_XpdrConnConfigIf1_Object = MibTableColumn
xpdrConnConfigIf1 = _XpdrConnConfigIf1_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 1),
    _XpdrConnConfigIf1_Type()
)
xpdrConnConfigIf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpdrConnConfigIf1.setStatus("current")
_XpdrConnConfigIf2_Type = InterfaceIndex
_XpdrConnConfigIf2_Object = MibTableColumn
xpdrConnConfigIf2 = _XpdrConnConfigIf2_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 2),
    _XpdrConnConfigIf2_Type()
)
xpdrConnConfigIf2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpdrConnConfigIf2.setStatus("current")
_XpdrConnConfigRateControlAdmin_Type = Integer32
_XpdrConnConfigRateControlAdmin_Object = MibTableColumn
xpdrConnConfigRateControlAdmin = _XpdrConnConfigRateControlAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 3),
    _XpdrConnConfigRateControlAdmin_Type()
)
xpdrConnConfigRateControlAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrConnConfigRateControlAdmin.setStatus("current")
_XpdrConnConfigRateControlOper_Type = Integer32
_XpdrConnConfigRateControlOper_Object = MibTableColumn
xpdrConnConfigRateControlOper = _XpdrConnConfigRateControlOper_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 4),
    _XpdrConnConfigRateControlOper_Type()
)
xpdrConnConfigRateControlOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpdrConnConfigRateControlOper.setStatus("current")
_XpdrConnConfigLosPropagation_Type = TruthValue
_XpdrConnConfigLosPropagation_Object = MibTableColumn
xpdrConnConfigLosPropagation = _XpdrConnConfigLosPropagation_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 5),
    _XpdrConnConfigLosPropagation_Type()
)
xpdrConnConfigLosPropagation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrConnConfigLosPropagation.setStatus("current")
_XpdrServiceType_Type = XpdrServiceType
_XpdrServiceType_Object = MibTableColumn
xpdrServiceType = _XpdrServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 6),
    _XpdrServiceType_Type()
)
xpdrServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrServiceType.setStatus("current")
_XpdrConnAddMask_Type = Integer32
_XpdrConnAddMask_Object = MibTableColumn
xpdrConnAddMask = _XpdrConnAddMask_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 7),
    _XpdrConnAddMask_Type()
)
xpdrConnAddMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrConnAddMask.setStatus("current")


class _XpdrMuxInbandAdmin_Type(Integer32):
    """Custom type xpdrMuxInbandAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("standby", 3))
    )


_XpdrMuxInbandAdmin_Type.__name__ = "Integer32"
_XpdrMuxInbandAdmin_Object = MibTableColumn
xpdrMuxInbandAdmin = _XpdrMuxInbandAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 8),
    _XpdrMuxInbandAdmin_Type()
)
xpdrMuxInbandAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrMuxInbandAdmin.setStatus("current")


class _XpdrMuxInbandOper_Type(Integer32):
    """Custom type xpdrMuxInbandOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("standby", 3))
    )


_XpdrMuxInbandOper_Type.__name__ = "Integer32"
_XpdrMuxInbandOper_Object = MibTableColumn
xpdrMuxInbandOper = _XpdrMuxInbandOper_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 9),
    _XpdrMuxInbandOper_Type()
)
xpdrMuxInbandOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpdrMuxInbandOper.setStatus("current")


class _XpdrDirection_Type(Integer32):
    """Custom type xpdrDirection based on Integer32"""
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
        *(("bidirectional", 1),
          ("unidirectionalTx", 2),
          ("unidirectionalRx", 3),
          ("loopback", 4))
    )


_XpdrDirection_Type.__name__ = "Integer32"
_XpdrDirection_Object = MibTableColumn
xpdrDirection = _XpdrDirection_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 10),
    _XpdrDirection_Type()
)
xpdrDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrDirection.setStatus("current")
_XpdrConnConfigCpriRateControl_Type = TruthValue
_XpdrConnConfigCpriRateControl_Object = MibTableColumn
xpdrConnConfigCpriRateControl = _XpdrConnConfigCpriRateControl_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 11),
    _XpdrConnConfigCpriRateControl_Type()
)
xpdrConnConfigCpriRateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrConnConfigCpriRateControl.setStatus("current")
_XpdrFaultPropagationDelay_Type = Integer32
_XpdrFaultPropagationDelay_Object = MibTableColumn
xpdrFaultPropagationDelay = _XpdrFaultPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 12),
    _XpdrFaultPropagationDelay_Type()
)
xpdrFaultPropagationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrFaultPropagationDelay.setStatus("current")
_XpdrFecMode_Type = Integer32
_XpdrFecMode_Object = MibTableColumn
xpdrFecMode = _XpdrFecMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 13),
    _XpdrFecMode_Type()
)
xpdrFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrFecMode.setStatus("current")
_OduXcConnConfigTable_Object = MibTable
oduXcConnConfigTable = _OduXcConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    oduXcConnConfigTable.setStatus("current")
_OduXcConnConfigEntry_Object = MibTableRow
oduXcConnConfigEntry = _OduXcConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1)
)
oduXcConnConfigEntry.setIndexNames(
    (0, "SL-XPDR-MIB", "oduXcConnConfigP1"),
    (0, "SL-XPDR-MIB", "oduXcConnConfigP2"),
)
if mibBuilder.loadTexts:
    oduXcConnConfigEntry.setStatus("current")
_OduXcConnConfigP1_Type = Integer32
_OduXcConnConfigP1_Object = MibTableColumn
oduXcConnConfigP1 = _OduXcConnConfigP1_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 1),
    _OduXcConnConfigP1_Type()
)
oduXcConnConfigP1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oduXcConnConfigP1.setStatus("current")
_OduXcConnConfigP2_Type = Integer32
_OduXcConnConfigP2_Object = MibTableColumn
oduXcConnConfigP2 = _OduXcConnConfigP2_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 2),
    _OduXcConnConfigP2_Type()
)
oduXcConnConfigP2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oduXcConnConfigP2.setStatus("current")
_OduXcConnConfigProtected_Type = TruthValue
_OduXcConnConfigProtected_Object = MibTableColumn
oduXcConnConfigProtected = _OduXcConnConfigProtected_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 3),
    _OduXcConnConfigProtected_Type()
)
oduXcConnConfigProtected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oduXcConnConfigProtected.setStatus("current")
_OduXcConnConfigRowStatus_Type = RowStatus
_OduXcConnConfigRowStatus_Object = MibTableColumn
oduXcConnConfigRowStatus = _OduXcConnConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 4),
    _OduXcConnConfigRowStatus_Type()
)
oduXcConnConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oduXcConnConfigRowStatus.setStatus("current")
_XpdrOduMappingStatus_Type = Integer32
_XpdrOduMappingStatus_Object = MibScalar
xpdrOduMappingStatus = _XpdrOduMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3),
    _XpdrOduMappingStatus_Type()
)
xpdrOduMappingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpdrOduMappingStatus.setStatus("current")
_XpdrOduMappingMaskedAdmin_Type = Integer32
_XpdrOduMappingMaskedAdmin_Object = MibScalar
xpdrOduMappingMaskedAdmin = _XpdrOduMappingMaskedAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 4),
    _XpdrOduMappingMaskedAdmin_Type()
)
xpdrOduMappingMaskedAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xpdrOduMappingMaskedAdmin.setStatus("current")
_SlXpdrLastChange_ObjectIdentity = ObjectIdentity
slXpdrLastChange = _SlXpdrLastChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 6)
)
_SlXpdrTraps_ObjectIdentity = ObjectIdentity
slXpdrTraps = _SlXpdrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 7)
)
_SlXpdrTraps0_ObjectIdentity = ObjectIdentity
slXpdrTraps0 = _SlXpdrTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 7, 0)
)

# Managed Objects groups


# Notification objects

xpdrConnConfigTableChange0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 7, 0, 1)
)
if mibBuilder.loadTexts:
    xpdrConnConfigTableChange0.setStatus(
        "current"
    )

xpdrConnConfigTableChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 8, 7, 1)
)
if mibBuilder.loadTexts:
    xpdrConnConfigTableChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-XPDR-MIB",
    **{"XpdrServiceType": XpdrServiceType,
       "slXpdr": slXpdr,
       "slXpdrConn": slXpdrConn,
       "xpdrConnConfigTable": xpdrConnConfigTable,
       "xpdrConnConfigEntry": xpdrConnConfigEntry,
       "xpdrConnConfigIf1": xpdrConnConfigIf1,
       "xpdrConnConfigIf2": xpdrConnConfigIf2,
       "xpdrConnConfigRateControlAdmin": xpdrConnConfigRateControlAdmin,
       "xpdrConnConfigRateControlOper": xpdrConnConfigRateControlOper,
       "xpdrConnConfigLosPropagation": xpdrConnConfigLosPropagation,
       "xpdrServiceType": xpdrServiceType,
       "xpdrConnAddMask": xpdrConnAddMask,
       "xpdrMuxInbandAdmin": xpdrMuxInbandAdmin,
       "xpdrMuxInbandOper": xpdrMuxInbandOper,
       "xpdrDirection": xpdrDirection,
       "xpdrConnConfigCpriRateControl": xpdrConnConfigCpriRateControl,
       "xpdrFaultPropagationDelay": xpdrFaultPropagationDelay,
       "xpdrFecMode": xpdrFecMode,
       "oduXcConnConfigTable": oduXcConnConfigTable,
       "oduXcConnConfigEntry": oduXcConnConfigEntry,
       "oduXcConnConfigP1": oduXcConnConfigP1,
       "oduXcConnConfigP2": oduXcConnConfigP2,
       "oduXcConnConfigProtected": oduXcConnConfigProtected,
       "oduXcConnConfigRowStatus": oduXcConnConfigRowStatus,
       "xpdrOduMappingStatus": xpdrOduMappingStatus,
       "xpdrOduMappingMaskedAdmin": xpdrOduMappingMaskedAdmin,
       "slXpdrLastChange": slXpdrLastChange,
       "slXpdrTraps": slXpdrTraps,
       "slXpdrTraps0": slXpdrTraps0,
       "xpdrConnConfigTableChange0": xpdrConnConfigTableChange0,
       "xpdrConnConfigTableChange": xpdrConnConfigTableChange}
)
