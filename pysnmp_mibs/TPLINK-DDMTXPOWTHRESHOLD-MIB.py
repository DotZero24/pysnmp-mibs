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
ddmTxPowThreshold=ModuleIdentity((1,3,6,1,4,1,11863,6,96,1,5))
if mibBuilder.loadTexts:ddmTxPowThreshold.setRevisions(('2009-08-27 00:00',))
_DdmTxPowThresholdTable_Object=MibTable
ddmTxPowThresholdTable=_DdmTxPowThresholdTable_Object((1,3,6,1,4,1,11863,6,96,1,5,1))
if mibBuilder.loadTexts:ddmTxPowThresholdTable.setStatus(_A)
_DdmTxPowThresholdEntry_Object=MibTableRow
ddmTxPowThresholdEntry=_DdmTxPowThresholdEntry_Object((1,3,6,1,4,1,11863,6,96,1,5,1,1))
ddmTxPowThresholdEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ddmTxPowThresholdEntry.setStatus(_A)
class _DdmTxPowThresholdPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DdmTxPowThresholdPort_Type.__name__=_F
_DdmTxPowThresholdPort_Object=MibTableColumn
ddmTxPowThresholdPort=_DdmTxPowThresholdPort_Object((1,3,6,1,4,1,11863,6,96,1,5,1,1,1),_DdmTxPowThresholdPort_Type())
ddmTxPowThresholdPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ddmTxPowThresholdPort.setStatus(_A)
class _DdmTxPowThresholdHighAlarm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmTxPowThresholdHighAlarm_Type.__name__=_B
_DdmTxPowThresholdHighAlarm_Object=MibTableColumn
ddmTxPowThresholdHighAlarm=_DdmTxPowThresholdHighAlarm_Object((1,3,6,1,4,1,11863,6,96,1,5,1,1,2),_DdmTxPowThresholdHighAlarm_Type())
ddmTxPowThresholdHighAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmTxPowThresholdHighAlarm.setStatus(_A)
class _DdmTxPowThresholdLowAlarm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmTxPowThresholdLowAlarm_Type.__name__=_B
_DdmTxPowThresholdLowAlarm_Object=MibTableColumn
ddmTxPowThresholdLowAlarm=_DdmTxPowThresholdLowAlarm_Object((1,3,6,1,4,1,11863,6,96,1,5,1,1,3),_DdmTxPowThresholdLowAlarm_Type())
ddmTxPowThresholdLowAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmTxPowThresholdLowAlarm.setStatus(_A)
class _DdmTxPowThresholdHighWarn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmTxPowThresholdHighWarn_Type.__name__=_B
_DdmTxPowThresholdHighWarn_Object=MibTableColumn
ddmTxPowThresholdHighWarn=_DdmTxPowThresholdHighWarn_Object((1,3,6,1,4,1,11863,6,96,1,5,1,1,4),_DdmTxPowThresholdHighWarn_Type())
ddmTxPowThresholdHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmTxPowThresholdHighWarn.setStatus(_A)
class _DdmTxPowThresholdLowWarn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmTxPowThresholdLowWarn_Type.__name__=_B
_DdmTxPowThresholdLowWarn_Object=MibTableColumn
ddmTxPowThresholdLowWarn=_DdmTxPowThresholdLowWarn_Object((1,3,6,1,4,1,11863,6,96,1,5,1,1,5),_DdmTxPowThresholdLowWarn_Type())
ddmTxPowThresholdLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmTxPowThresholdLowWarn.setStatus(_A)
class _DdmTxPowThresholdPortLAG_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmTxPowThresholdPortLAG_Type.__name__=_B
_DdmTxPowThresholdPortLAG_Object=MibTableColumn
ddmTxPowThresholdPortLAG=_DdmTxPowThresholdPortLAG_Object((1,3,6,1,4,1,11863,6,96,1,5,1,1,6),_DdmTxPowThresholdPortLAG_Type())
ddmTxPowThresholdPortLAG.setMaxAccess(_G)
if mibBuilder.loadTexts:ddmTxPowThresholdPortLAG.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-DDMTXPOWTHRESHOLD-MIB',**{'ddmTxPowThreshold':ddmTxPowThreshold,'ddmTxPowThresholdTable':ddmTxPowThresholdTable,'ddmTxPowThresholdEntry':ddmTxPowThresholdEntry,'ddmTxPowThresholdPort':ddmTxPowThresholdPort,'ddmTxPowThresholdHighAlarm':ddmTxPowThresholdHighAlarm,'ddmTxPowThresholdLowAlarm':ddmTxPowThresholdLowAlarm,'ddmTxPowThresholdHighWarn':ddmTxPowThresholdHighWarn,'ddmTxPowThresholdLowWarn':ddmTxPowThresholdLowWarn,'ddmTxPowThresholdPortLAG':ddmTxPowThresholdPortLAG})