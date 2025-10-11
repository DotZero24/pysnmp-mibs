# SNMP MIB module (ARRIS-MOCA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/ARRIS-MOCA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:09:34 2025
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

(arrisProducts,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisProducts")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arrisMoCAMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 21)
)
if mibBuilder.loadTexts:
    arrisMoCAMib.setRevisions(
        ("2014-08-13 00:00",
         "2013-08-21 00:00",
         "2013-08-01 00:00",
         "2013-06-26 00:00",
         "2013-06-04 00:00",
         "2012-11-18 00:00",
         "2012-11-04 00:00",
         "2012-10-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ArrisMocaTabooChannelMsk(TextualConvention, Unsigned32):
    status = "current"


class ArrisMocaChannelMsk(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_ArrisMoCAConfiguration_ObjectIdentity = ObjectIdentity
arrisMoCAConfiguration = _ArrisMoCAConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 21, 1)
)


class _ArrisMoCAChannelSelMethod_Type(Integer32):
    """Custom type arrisMoCAChannelSelMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scan", 1),
          ("manual", 2))
    )


_ArrisMoCAChannelSelMethod_Type.__name__ = "Integer32"
_ArrisMoCAChannelSelMethod_Object = MibScalar
arrisMoCAChannelSelMethod = _ArrisMoCAChannelSelMethod_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 21, 1, 1),
    _ArrisMoCAChannelSelMethod_Type()
)
arrisMoCAChannelSelMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMoCAChannelSelMethod.setStatus("current")


class _ArrisMoCAChannelMsk_Type(ArrisMocaChannelMsk):
    """Custom type arrisMoCAChannelMsk based on ArrisMocaChannelMsk"""
    defaultValue = 1


_ArrisMoCAChannelMsk_Type.__name__ = "ArrisMocaChannelMsk"
_ArrisMoCAChannelMsk_Object = MibScalar
arrisMoCAChannelMsk = _ArrisMoCAChannelMsk_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 21, 1, 2),
    _ArrisMoCAChannelMsk_Type()
)
arrisMoCAChannelMsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMoCAChannelMsk.setStatus("current")


class _ArrisMoCATabooChannel_Type(ArrisMocaTabooChannelMsk):
    """Custom type arrisMoCATabooChannel based on ArrisMocaTabooChannelMsk"""
    defaultValue = 0


_ArrisMoCATabooChannel_Type.__name__ = "ArrisMocaTabooChannelMsk"
_ArrisMoCATabooChannel_Object = MibScalar
arrisMoCATabooChannel = _ArrisMoCATabooChannel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 21, 1, 4),
    _ArrisMoCATabooChannel_Type()
)
arrisMoCATabooChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMoCATabooChannel.setStatus("current")


class _ArrisMoCALOF_Type(Integer32):
    """Custom type arrisMoCALOF based on Integer32"""
    defaultValue = 1150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1150,
              1200,
              1250,
              1300,
              1350,
              1400,
              1450,
              1500,
              1550,
              1600)
        )
    )
    namedValues = NamedValues(
        *(("d1", 1150),
          ("d2", 1200),
          ("d3", 1250),
          ("d4", 1300),
          ("d5", 1350),
          ("d6", 1400),
          ("d7", 1450),
          ("d8", 1500),
          ("d9", 1550),
          ("d10", 1600))
    )


_ArrisMoCALOF_Type.__name__ = "Integer32"
_ArrisMoCALOF_Object = MibScalar
arrisMoCALOF = _ArrisMoCALOF_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 21, 1, 5),
    _ArrisMoCALOF_Type()
)
arrisMoCALOF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMoCALOF.setStatus("current")


class _ArrisMoCAPrimchnOff_Type(Integer32):
    """Custom type arrisMoCAPrimchnOff based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("same", 0),
          ("above", 1),
          ("below", 2))
    )


_ArrisMoCAPrimchnOff_Type.__name__ = "Integer32"
_ArrisMoCAPrimchnOff_Object = MibScalar
arrisMoCAPrimchnOff = _ArrisMoCAPrimchnOff_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 21, 1, 6),
    _ArrisMoCAPrimchnOff_Type()
)
arrisMoCAPrimchnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMoCAPrimchnOff.setStatus("current")


class _ArrisMoCAApplySettings_Type(Integer32):
    """Custom type arrisMoCAApplySettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("applySettings-Save", 1),
          ("applySettings-NoSave", 2))
    )


_ArrisMoCAApplySettings_Type.__name__ = "Integer32"
_ArrisMoCAApplySettings_Object = MibScalar
arrisMoCAApplySettings = _ArrisMoCAApplySettings_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 21, 2),
    _ArrisMoCAApplySettings_Type()
)
arrisMoCAApplySettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisMoCAApplySettings.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-MOCA-MIB",
    **{"ArrisMocaTabooChannelMsk": ArrisMocaTabooChannelMsk,
       "ArrisMocaChannelMsk": ArrisMocaChannelMsk,
       "arrisMoCAMib": arrisMoCAMib,
       "arrisMoCAConfiguration": arrisMoCAConfiguration,
       "arrisMoCAChannelSelMethod": arrisMoCAChannelSelMethod,
       "arrisMoCAChannelMsk": arrisMoCAChannelMsk,
       "arrisMoCATabooChannel": arrisMoCATabooChannel,
       "arrisMoCALOF": arrisMoCALOF,
       "arrisMoCAPrimchnOff": arrisMoCAPrimchnOff,
       "arrisMoCAApplySettings": arrisMoCAApplySettings}
)
