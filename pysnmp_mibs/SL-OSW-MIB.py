_E='read-only'
_D='slOSWPortConfigLineIndex'
_C='SL-OSW-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
slService,=mibBuilder.importSymbols('SL-NE-MIB','slService')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
slOSW=ModuleIdentity((1,3,6,1,4,1,4515,1,1,17))
_SlOSWConfig_ObjectIdentity=ObjectIdentity
slOSWConfig=_SlOSWConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,1,17,1))
_SlOSWPortConfigTable_Object=MibTable
slOSWPortConfigTable=_SlOSWPortConfigTable_Object((1,3,6,1,4,1,4515,1,1,17,1,1))
if mibBuilder.loadTexts:slOSWPortConfigTable.setStatus(_A)
_SlOSWPortConfigEntry_Object=MibTableRow
slOSWPortConfigEntry=_SlOSWPortConfigEntry_Object((1,3,6,1,4,1,4515,1,1,17,1,1,1))
slOSWPortConfigEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:slOSWPortConfigEntry.setStatus(_A)
_SlOSWPortConfigLineIndex_Type=InterfaceIndex
_SlOSWPortConfigLineIndex_Object=MibTableColumn
slOSWPortConfigLineIndex=_SlOSWPortConfigLineIndex_Object((1,3,6,1,4,1,4515,1,1,17,1,1,1,1),_SlOSWPortConfigLineIndex_Type())
slOSWPortConfigLineIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:slOSWPortConfigLineIndex.setStatus(_A)
_SlOSWPortConfigInPowerLevel_Type=Integer32
_SlOSWPortConfigInPowerLevel_Object=MibTableColumn
slOSWPortConfigInPowerLevel=_SlOSWPortConfigInPowerLevel_Object((1,3,6,1,4,1,4515,1,1,17,1,1,1,2),_SlOSWPortConfigInPowerLevel_Type())
slOSWPortConfigInPowerLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:slOSWPortConfigInPowerLevel.setStatus(_A)
class _SlOSWPortConfigLosThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SlOSWPortConfigLosThreshold_Type.__name__=_B
_SlOSWPortConfigLosThreshold_Object=MibTableColumn
slOSWPortConfigLosThreshold=_SlOSWPortConfigLosThreshold_Object((1,3,6,1,4,1,4515,1,1,17,1,1,1,3),_SlOSWPortConfigLosThreshold_Type())
slOSWPortConfigLosThreshold.setMaxAccess('read-write')
if mibBuilder.loadTexts:slOSWPortConfigLosThreshold.setStatus(_A)
_SlOSWPm_ObjectIdentity=ObjectIdentity
slOSWPm=_SlOSWPm_ObjectIdentity((1,3,6,1,4,1,4515,1,1,17,2))
_SlOSWTraps_ObjectIdentity=ObjectIdentity
slOSWTraps=_SlOSWTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,1,17,3))
mibBuilder.exportSymbols(_C,**{'slOSW':slOSW,'slOSWConfig':slOSWConfig,'slOSWPortConfigTable':slOSWPortConfigTable,'slOSWPortConfigEntry':slOSWPortConfigEntry,_D:slOSWPortConfigLineIndex,'slOSWPortConfigInPowerLevel':slOSWPortConfigInPowerLevel,'slOSWPortConfigLosThreshold':slOSWPortConfigLosThreshold,'slOSWPm':slOSWPm,'slOSWTraps':slOSWTraps})