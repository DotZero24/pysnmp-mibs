# SNMP MIB module (BN-IF-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/BN-IF-EXTENSIONS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:18:14 2025
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

(s5IfExt,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5IfExt")

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


# MODULE-IDENTITY

bnIfExtensionsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 2)
)
if mibBuilder.loadTexts:
    bnIfExtensionsMib.setRevisions(
        ("2016-11-28 00:00",
         "2013-07-26 00:00",
         "2011-10-05 00:00",
         "2011-09-16 00:00",
         "2004-07-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BnIfExtensions_ObjectIdentity = ObjectIdentity
bnIfExtensions = _BnIfExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1)
)
_BnIfExtnTable_Object = MibTable
bnIfExtnTable = _BnIfExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1)
)
if mibBuilder.loadTexts:
    bnIfExtnTable.setStatus("current")
_BnIfExtnEntry_Object = MibTableRow
bnIfExtnEntry = _BnIfExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1)
)
bnIfExtnEntry.setIndexNames(
    (0, "BN-IF-EXTENSIONS-MIB", "bnIfExtnIndex"),
)
if mibBuilder.loadTexts:
    bnIfExtnEntry.setStatus("current")
_BnIfExtnIndex_Type = Integer32
_BnIfExtnIndex_Object = MibTableColumn
bnIfExtnIndex = _BnIfExtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 1),
    _BnIfExtnIndex_Type()
)
bnIfExtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnIfExtnIndex.setStatus("current")
_BnIfExtnSlot_Type = Integer32
_BnIfExtnSlot_Object = MibTableColumn
bnIfExtnSlot = _BnIfExtnSlot_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 2),
    _BnIfExtnSlot_Type()
)
bnIfExtnSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnIfExtnSlot.setStatus("current")
_BnIfExtnPort_Type = Integer32
_BnIfExtnPort_Object = MibTableColumn
bnIfExtnPort = _BnIfExtnPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 3),
    _BnIfExtnPort_Type()
)
bnIfExtnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnIfExtnPort.setStatus("current")


class _BnIfExtnIsPortShared_Type(Integer32):
    """Custom type bnIfExtnIsPortShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portShared", 1),
          ("portNotShared", 2))
    )


_BnIfExtnIsPortShared_Type.__name__ = "Integer32"
_BnIfExtnIsPortShared_Object = MibTableColumn
bnIfExtnIsPortShared = _BnIfExtnIsPortShared_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 4),
    _BnIfExtnIsPortShared_Type()
)
bnIfExtnIsPortShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnIfExtnIsPortShared.setStatus("current")


class _BnIfExtnPortActiveComponent_Type(Integer32):
    """Custom type bnIfExtnPortActiveComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixedPort", 1),
          ("gbicPort", 2),
          ("mdaPort", 3))
    )


_BnIfExtnPortActiveComponent_Type.__name__ = "Integer32"
_BnIfExtnPortActiveComponent_Object = MibTableColumn
bnIfExtnPortActiveComponent = _BnIfExtnPortActiveComponent_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 5),
    _BnIfExtnPortActiveComponent_Type()
)
bnIfExtnPortActiveComponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnIfExtnPortActiveComponent.setStatus("current")


class _BnIfExtnPoweredDeviceDetectType_Type(Integer32):
    """Custom type bnIfExtnPoweredDeviceDetectType based on Integer32"""
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
        *(("compliantWith802dot3af", 1),
          ("compliantWith802dot3afAndLegacySupport", 2),
          ("compliantWith802dot3at", 3),
          ("compliantWith802dot3atAndLegacySupport", 4))
    )


_BnIfExtnPoweredDeviceDetectType_Type.__name__ = "Integer32"
_BnIfExtnPoweredDeviceDetectType_Object = MibTableColumn
bnIfExtnPoweredDeviceDetectType = _BnIfExtnPoweredDeviceDetectType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 6),
    _BnIfExtnPoweredDeviceDetectType_Type()
)
bnIfExtnPoweredDeviceDetectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnIfExtnPoweredDeviceDetectType.setStatus("current")


class _BnIfExtnAutoNegotiationExtAdv_Type(Bits):
    """Custom type bnIfExtnAutoNegotiationExtAdv based on Bits"""
    namedValues = NamedValues(
        *(("advertise10Half", 0),
          ("advertise10Full", 1),
          ("advertise100Half", 2),
          ("advertise100Full", 3),
          ("advertise1000Half", 4),
          ("advertise1000Full", 5),
          ("advertisePauseFrame", 6),
          ("advertiseAsymmPauseFrame", 7),
          ("advertise10000Full", 8),
          ("advertise40000Full", 9),
          ("advertise2500Full", 10))
    )

_BnIfExtnAutoNegotiationExtAdv_Type.__name__ = "Bits"
_BnIfExtnAutoNegotiationExtAdv_Object = MibTableColumn
bnIfExtnAutoNegotiationExtAdv = _BnIfExtnAutoNegotiationExtAdv_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 7),
    _BnIfExtnAutoNegotiationExtAdv_Type()
)
bnIfExtnAutoNegotiationExtAdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnIfExtnAutoNegotiationExtAdv.setStatus("current")


class _BnIfExtnExtHwAdvCapability_Type(Bits):
    """Custom type bnIfExtnExtHwAdvCapability based on Bits"""
    namedValues = NamedValues(
        *(("advertise10Half", 0),
          ("advertise10Full", 1),
          ("advertise100Half", 2),
          ("advertise100Full", 3),
          ("advertise1000Half", 4),
          ("advertise1000Full", 5),
          ("advertisePauseFrame", 6),
          ("advertiseAsymmPauseFrame", 7),
          ("advertise10000Full", 8),
          ("advertise40000Full", 9),
          ("advertise2500Full", 10))
    )

_BnIfExtnExtHwAdvCapability_Type.__name__ = "Bits"
_BnIfExtnExtHwAdvCapability_Object = MibTableColumn
bnIfExtnExtHwAdvCapability = _BnIfExtnExtHwAdvCapability_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 15, 1, 1, 1, 8),
    _BnIfExtnExtHwAdvCapability_Type()
)
bnIfExtnExtHwAdvCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnIfExtnExtHwAdvCapability.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BN-IF-EXTENSIONS-MIB",
    **{"bnIfExtensions": bnIfExtensions,
       "bnIfExtnTable": bnIfExtnTable,
       "bnIfExtnEntry": bnIfExtnEntry,
       "bnIfExtnIndex": bnIfExtnIndex,
       "bnIfExtnSlot": bnIfExtnSlot,
       "bnIfExtnPort": bnIfExtnPort,
       "bnIfExtnIsPortShared": bnIfExtnIsPortShared,
       "bnIfExtnPortActiveComponent": bnIfExtnPortActiveComponent,
       "bnIfExtnPoweredDeviceDetectType": bnIfExtnPoweredDeviceDetectType,
       "bnIfExtnAutoNegotiationExtAdv": bnIfExtnAutoNegotiationExtAdv,
       "bnIfExtnExtHwAdvCapability": bnIfExtnExtHwAdvCapability,
       "bnIfExtensionsMib": bnIfExtensionsMib}
)
