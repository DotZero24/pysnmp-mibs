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
ddmTempThreshold=ModuleIdentity((1,3,6,1,4,1,11863,6,96,1,2))
if mibBuilder.loadTexts:ddmTempThreshold.setRevisions(('2009-08-27 00:00',))
_DdmTempThresholdTable_Object=MibTable
ddmTempThresholdTable=_DdmTempThresholdTable_Object((1,3,6,1,4,1,11863,6,96,1,2,1))
if mibBuilder.loadTexts:ddmTempThresholdTable.setStatus(_A)
_DdmTempThresholdEntry_Object=MibTableRow
ddmTempThresholdEntry=_DdmTempThresholdEntry_Object((1,3,6,1,4,1,11863,6,96,1,2,1,1))
ddmTempThresholdEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ddmTempThresholdEntry.setStatus(_A)
class _DdmTempThresholdPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DdmTempThresholdPort_Type.__name__=_F
_DdmTempThresholdPort_Object=MibTableColumn
ddmTempThresholdPort=_DdmTempThresholdPort_Object((1,3,6,1,4,1,11863,6,96,1,2,1,1,1),_DdmTempThresholdPort_Type())
ddmTempThresholdPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ddmTempThresholdPort.setStatus(_A)
class _DdmTempThresholdHighAlarm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmTempThresholdHighAlarm_Type.__name__=_B
_DdmTempThresholdHighAlarm_Object=MibTableColumn
ddmTempThresholdHighAlarm=_DdmTempThresholdHighAlarm_Object((1,3,6,1,4,1,11863,6,96,1,2,1,1,2),_DdmTempThresholdHighAlarm_Type())
ddmTempThresholdHighAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmTempThresholdHighAlarm.setStatus(_A)
class _DdmTempThresholdLowAlarm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmTempThresholdLowAlarm_Type.__name__=_B
_DdmTempThresholdLowAlarm_Object=MibTableColumn
ddmTempThresholdLowAlarm=_DdmTempThresholdLowAlarm_Object((1,3,6,1,4,1,11863,6,96,1,2,1,1,3),_DdmTempThresholdLowAlarm_Type())
ddmTempThresholdLowAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmTempThresholdLowAlarm.setStatus(_A)
class _DdmTempThresholdHighWarn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmTempThresholdHighWarn_Type.__name__=_B
_DdmTempThresholdHighWarn_Object=MibTableColumn
ddmTempThresholdHighWarn=_DdmTempThresholdHighWarn_Object((1,3,6,1,4,1,11863,6,96,1,2,1,1,4),_DdmTempThresholdHighWarn_Type())
ddmTempThresholdHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmTempThresholdHighWarn.setStatus(_A)
class _DdmTempThresholdLowWarn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmTempThresholdLowWarn_Type.__name__=_B
_DdmTempThresholdLowWarn_Object=MibTableColumn
ddmTempThresholdLowWarn=_DdmTempThresholdLowWarn_Object((1,3,6,1,4,1,11863,6,96,1,2,1,1,5),_DdmTempThresholdLowWarn_Type())
ddmTempThresholdLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmTempThresholdLowWarn.setStatus(_A)
class _DdmTempThresholdPortLAG_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmTempThresholdPortLAG_Type.__name__=_B
_DdmTempThresholdPortLAG_Object=MibTableColumn
ddmTempThresholdPortLAG=_DdmTempThresholdPortLAG_Object((1,3,6,1,4,1,11863,6,96,1,2,1,1,6),_DdmTempThresholdPortLAG_Type())
ddmTempThresholdPortLAG.setMaxAccess(_G)
if mibBuilder.loadTexts:ddmTempThresholdPortLAG.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-DDMTEMPTHRESHOLD-MIB',**{'ddmTempThreshold':ddmTempThreshold,'ddmTempThresholdTable':ddmTempThresholdTable,'ddmTempThresholdEntry':ddmTempThresholdEntry,'ddmTempThresholdPort':ddmTempThresholdPort,'ddmTempThresholdHighAlarm':ddmTempThresholdHighAlarm,'ddmTempThresholdLowAlarm':ddmTempThresholdLowAlarm,'ddmTempThresholdHighWarn':ddmTempThresholdHighWarn,'ddmTempThresholdLowWarn':ddmTempThresholdLowWarn,'ddmTempThresholdPortLAG':ddmTempThresholdPortLAG})