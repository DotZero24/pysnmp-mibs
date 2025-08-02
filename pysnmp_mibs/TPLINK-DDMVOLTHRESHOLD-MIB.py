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
ddmVolThreshold=ModuleIdentity((1,3,6,1,4,1,11863,6,96,1,3))
if mibBuilder.loadTexts:ddmVolThreshold.setRevisions(('2009-08-27 00:00',))
_DdmVolThresholdTable_Object=MibTable
ddmVolThresholdTable=_DdmVolThresholdTable_Object((1,3,6,1,4,1,11863,6,96,1,3,1))
if mibBuilder.loadTexts:ddmVolThresholdTable.setStatus(_A)
_DdmVolThresholdEntry_Object=MibTableRow
ddmVolThresholdEntry=_DdmVolThresholdEntry_Object((1,3,6,1,4,1,11863,6,96,1,3,1,1))
ddmVolThresholdEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ddmVolThresholdEntry.setStatus(_A)
class _DdmVolThresholdPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DdmVolThresholdPort_Type.__name__=_F
_DdmVolThresholdPort_Object=MibTableColumn
ddmVolThresholdPort=_DdmVolThresholdPort_Object((1,3,6,1,4,1,11863,6,96,1,3,1,1,1),_DdmVolThresholdPort_Type())
ddmVolThresholdPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ddmVolThresholdPort.setStatus(_A)
class _DdmVolThresholdHighAlarm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmVolThresholdHighAlarm_Type.__name__=_B
_DdmVolThresholdHighAlarm_Object=MibTableColumn
ddmVolThresholdHighAlarm=_DdmVolThresholdHighAlarm_Object((1,3,6,1,4,1,11863,6,96,1,3,1,1,2),_DdmVolThresholdHighAlarm_Type())
ddmVolThresholdHighAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmVolThresholdHighAlarm.setStatus(_A)
class _DdmVolThresholdLowAlarm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmVolThresholdLowAlarm_Type.__name__=_B
_DdmVolThresholdLowAlarm_Object=MibTableColumn
ddmVolThresholdLowAlarm=_DdmVolThresholdLowAlarm_Object((1,3,6,1,4,1,11863,6,96,1,3,1,1,3),_DdmVolThresholdLowAlarm_Type())
ddmVolThresholdLowAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmVolThresholdLowAlarm.setStatus(_A)
class _DdmVolThresholdHighWarn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmVolThresholdHighWarn_Type.__name__=_B
_DdmVolThresholdHighWarn_Object=MibTableColumn
ddmVolThresholdHighWarn=_DdmVolThresholdHighWarn_Object((1,3,6,1,4,1,11863,6,96,1,3,1,1,4),_DdmVolThresholdHighWarn_Type())
ddmVolThresholdHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmVolThresholdHighWarn.setStatus(_A)
class _DdmVolThresholdLowWarn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmVolThresholdLowWarn_Type.__name__=_B
_DdmVolThresholdLowWarn_Object=MibTableColumn
ddmVolThresholdLowWarn=_DdmVolThresholdLowWarn_Object((1,3,6,1,4,1,11863,6,96,1,3,1,1,5),_DdmVolThresholdLowWarn_Type())
ddmVolThresholdLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmVolThresholdLowWarn.setStatus(_A)
class _DdmVolThresholdPortLAG_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmVolThresholdPortLAG_Type.__name__=_B
_DdmVolThresholdPortLAG_Object=MibTableColumn
ddmVolThresholdPortLAG=_DdmVolThresholdPortLAG_Object((1,3,6,1,4,1,11863,6,96,1,3,1,1,6),_DdmVolThresholdPortLAG_Type())
ddmVolThresholdPortLAG.setMaxAccess(_G)
if mibBuilder.loadTexts:ddmVolThresholdPortLAG.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-DDMVOLTHRESHOLD-MIB',**{'ddmVolThreshold':ddmVolThreshold,'ddmVolThresholdTable':ddmVolThresholdTable,'ddmVolThresholdEntry':ddmVolThresholdEntry,'ddmVolThresholdPort':ddmVolThresholdPort,'ddmVolThresholdHighAlarm':ddmVolThresholdHighAlarm,'ddmVolThresholdLowAlarm':ddmVolThresholdLowAlarm,'ddmVolThresholdHighWarn':ddmVolThresholdHighWarn,'ddmVolThresholdLowWarn':ddmVolThresholdLowWarn,'ddmVolThresholdPortLAG':ddmVolThresholdPortLAG})