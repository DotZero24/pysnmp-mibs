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
ddmBiasCurThreshold=ModuleIdentity((1,3,6,1,4,1,11863,6,96,1,4))
if mibBuilder.loadTexts:ddmBiasCurThreshold.setRevisions(('2009-08-27 00:00',))
_DdmBiasCurThresholdTable_Object=MibTable
ddmBiasCurThresholdTable=_DdmBiasCurThresholdTable_Object((1,3,6,1,4,1,11863,6,96,1,4,1))
if mibBuilder.loadTexts:ddmBiasCurThresholdTable.setStatus(_A)
_DdmBiasCurThresholdEntry_Object=MibTableRow
ddmBiasCurThresholdEntry=_DdmBiasCurThresholdEntry_Object((1,3,6,1,4,1,11863,6,96,1,4,1,1))
ddmBiasCurThresholdEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ddmBiasCurThresholdEntry.setStatus(_A)
class _DdmBiasCurThresholdPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DdmBiasCurThresholdPort_Type.__name__=_F
_DdmBiasCurThresholdPort_Object=MibTableColumn
ddmBiasCurThresholdPort=_DdmBiasCurThresholdPort_Object((1,3,6,1,4,1,11863,6,96,1,4,1,1,1),_DdmBiasCurThresholdPort_Type())
ddmBiasCurThresholdPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ddmBiasCurThresholdPort.setStatus(_A)
class _DdmBiasCurThresholdHighAlarm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmBiasCurThresholdHighAlarm_Type.__name__=_B
_DdmBiasCurThresholdHighAlarm_Object=MibTableColumn
ddmBiasCurThresholdHighAlarm=_DdmBiasCurThresholdHighAlarm_Object((1,3,6,1,4,1,11863,6,96,1,4,1,1,2),_DdmBiasCurThresholdHighAlarm_Type())
ddmBiasCurThresholdHighAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmBiasCurThresholdHighAlarm.setStatus(_A)
class _DdmBiasCurThresholdLowAlarm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmBiasCurThresholdLowAlarm_Type.__name__=_B
_DdmBiasCurThresholdLowAlarm_Object=MibTableColumn
ddmBiasCurThresholdLowAlarm=_DdmBiasCurThresholdLowAlarm_Object((1,3,6,1,4,1,11863,6,96,1,4,1,1,3),_DdmBiasCurThresholdLowAlarm_Type())
ddmBiasCurThresholdLowAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmBiasCurThresholdLowAlarm.setStatus(_A)
class _DdmBiasCurThresholdHighWarn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmBiasCurThresholdHighWarn_Type.__name__=_B
_DdmBiasCurThresholdHighWarn_Object=MibTableColumn
ddmBiasCurThresholdHighWarn=_DdmBiasCurThresholdHighWarn_Object((1,3,6,1,4,1,11863,6,96,1,4,1,1,4),_DdmBiasCurThresholdHighWarn_Type())
ddmBiasCurThresholdHighWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmBiasCurThresholdHighWarn.setStatus(_A)
class _DdmBiasCurThresholdLowWarn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmBiasCurThresholdLowWarn_Type.__name__=_B
_DdmBiasCurThresholdLowWarn_Object=MibTableColumn
ddmBiasCurThresholdLowWarn=_DdmBiasCurThresholdLowWarn_Object((1,3,6,1,4,1,11863,6,96,1,4,1,1,5),_DdmBiasCurThresholdLowWarn_Type())
ddmBiasCurThresholdLowWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:ddmBiasCurThresholdLowWarn.setStatus(_A)
class _DdmBiasCurThresholdPortLAG_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmBiasCurThresholdPortLAG_Type.__name__=_B
_DdmBiasCurThresholdPortLAG_Object=MibTableColumn
ddmBiasCurThresholdPortLAG=_DdmBiasCurThresholdPortLAG_Object((1,3,6,1,4,1,11863,6,96,1,4,1,1,6),_DdmBiasCurThresholdPortLAG_Type())
ddmBiasCurThresholdPortLAG.setMaxAccess(_G)
if mibBuilder.loadTexts:ddmBiasCurThresholdPortLAG.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-DDMBIASCURTHRESHOLD-MIB',**{'ddmBiasCurThreshold':ddmBiasCurThreshold,'ddmBiasCurThresholdTable':ddmBiasCurThresholdTable,'ddmBiasCurThresholdEntry':ddmBiasCurThresholdEntry,'ddmBiasCurThresholdPort':ddmBiasCurThresholdPort,'ddmBiasCurThresholdHighAlarm':ddmBiasCurThresholdHighAlarm,'ddmBiasCurThresholdLowAlarm':ddmBiasCurThresholdLowAlarm,'ddmBiasCurThresholdHighWarn':ddmBiasCurThresholdHighWarn,'ddmBiasCurThresholdLowWarn':ddmBiasCurThresholdLowWarn,'ddmBiasCurThresholdPortLAG':ddmBiasCurThresholdPortLAG})