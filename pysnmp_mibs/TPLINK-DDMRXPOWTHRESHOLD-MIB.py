_G='read-only'
_F='DisplayString'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
tplinkDdmManageMIBObjects,=mibBuilder.importSymbols('TPLINK-DDMMANAGE-MIB','tplinkDdmManageMIBObjects')
ddmRxPowThreshold=ModuleIdentity((1,3,6,1,4,1,11863,6,96,1,6))
if mibBuilder.loadTexts:ddmRxPowThreshold.setRevisions(('2009-08-27 00:00',))
_DdmRxPowThresholdTable_Object=MibTable
ddmRxPowThresholdTable=_DdmRxPowThresholdTable_Object((1,3,6,1,4,1,11863,6,96,1,6,1))
if mibBuilder.loadTexts:ddmRxPowThresholdTable.setStatus(_A)
_DdmRxPowThresholdEntry_Object=MibTableRow
ddmRxPowThresholdEntry=_DdmRxPowThresholdEntry_Object((1,3,6,1,4,1,11863,6,96,1,6,1,1))
ddmRxPowThresholdEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ddmRxPowThresholdEntry.setStatus(_A)
class _DdmRxPowThresholdPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DdmRxPowThresholdPort_Type.__name__=_F
_DdmRxPowThresholdPort_Object=MibTableColumn
ddmRxPowThresholdPort=_DdmRxPowThresholdPort_Object((1,3,6,1,4,1,11863,6,96,1,6,1,1,1),_DdmRxPowThresholdPort_Type())
ddmRxPowThresholdPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ddmRxPowThresholdPort.setStatus(_A)
class _DdmRxPowThresholdHighAlarm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmRxPowThresholdHighAlarm_Type.__name__=_B
_DdmRxPowThresholdHighAlarm_Object=MibTableColumn
ddmRxPowThresholdHighAlarm=_DdmRxPowThresholdHighAlarm_Object((1,3,6,1,4,1,11863,6,96,1,6,1,1,2),_DdmRxPowThresholdHighAlarm_Type())
ddmRxPowThresholdHighAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmRxPowThresholdHighAlarm.setStatus(_A)
class _DdmRxPowThresholdLowAlarm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmRxPowThresholdLowAlarm_Type.__name__=_B
_DdmRxPowThresholdLowAlarm_Object=MibTableColumn
ddmRxPowThresholdLowAlarm=_DdmRxPowThresholdLowAlarm_Object((1,3,6,1,4,1,11863,6,96,1,6,1,1,3),_DdmRxPowThresholdLowAlarm_Type())
ddmRxPowThresholdLowAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmRxPowThresholdLowAlarm.setStatus(_A)
class _DdmRxPowThresholdHighWarn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmRxPowThresholdHighWarn_Type.__name__=_B
_DdmRxPowThresholdHighWarn_Object=MibTableColumn
ddmRxPowThresholdHighWarn=_DdmRxPowThresholdHighWarn_Object((1,3,6,1,4,1,11863,6,96,1,6,1,1,4),_DdmRxPowThresholdHighWarn_Type())
ddmRxPowThresholdHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmRxPowThresholdHighWarn.setStatus(_A)
class _DdmRxPowThresholdLowWarn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmRxPowThresholdLowWarn_Type.__name__=_B
_DdmRxPowThresholdLowWarn_Object=MibTableColumn
ddmRxPowThresholdLowWarn=_DdmRxPowThresholdLowWarn_Object((1,3,6,1,4,1,11863,6,96,1,6,1,1,5),_DdmRxPowThresholdLowWarn_Type())
ddmRxPowThresholdLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmRxPowThresholdLowWarn.setStatus(_A)
class _DdmRxPowThresholdPortLAG_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmRxPowThresholdPortLAG_Type.__name__=_B
_DdmRxPowThresholdPortLAG_Object=MibTableColumn
ddmRxPowThresholdPortLAG=_DdmRxPowThresholdPortLAG_Object((1,3,6,1,4,1,11863,6,96,1,6,1,1,6),_DdmRxPowThresholdPortLAG_Type())
ddmRxPowThresholdPortLAG.setMaxAccess(_G)
if mibBuilder.loadTexts:ddmRxPowThresholdPortLAG.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-DDMRXPOWTHRESHOLD-MIB',**{'ddmRxPowThreshold':ddmRxPowThreshold,'ddmRxPowThresholdTable':ddmRxPowThresholdTable,'ddmRxPowThresholdEntry':ddmRxPowThresholdEntry,'ddmRxPowThresholdPort':ddmRxPowThresholdPort,'ddmRxPowThresholdHighAlarm':ddmRxPowThresholdHighAlarm,'ddmRxPowThresholdLowAlarm':ddmRxPowThresholdLowAlarm,'ddmRxPowThresholdHighWarn':ddmRxPowThresholdHighWarn,'ddmRxPowThresholdLowWarn':ddmRxPowThresholdLowWarn,'ddmRxPowThresholdPortLAG':ddmRxPowThresholdPortLAG})