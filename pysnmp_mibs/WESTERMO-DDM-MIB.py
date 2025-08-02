_L='ddmPortGroup'
_K='ddmPortRxPower'
_J='ddmPortTxPower'
_I='ddmPortBiasCurrent'
_H='ddmPortTemperature'
_G='ddmPortVoltage'
_F='ddmPortIfName'
_E='ddmPortIfIndex'
_D='read-only'
_C='Integer32'
_B='WESTERMO-DDM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
common,=mibBuilder.importSymbols('WESTERMO-OID-MIB','common')
ddmMIB=ModuleIdentity((1,3,6,1,4,1,16177,2,2))
if mibBuilder.loadTexts:ddmMIB.setRevisions(('2017-12-05 00:00',))
_DdmObjects_ObjectIdentity=ObjectIdentity
ddmObjects=_DdmObjects_ObjectIdentity((1,3,6,1,4,1,16177,2,2,1))
_DdmPortTable_Object=MibTable
ddmPortTable=_DdmPortTable_Object((1,3,6,1,4,1,16177,2,2,1,1))
if mibBuilder.loadTexts:ddmPortTable.setStatus(_A)
_DdmPortEntry_Object=MibTableRow
ddmPortEntry=_DdmPortEntry_Object((1,3,6,1,4,1,16177,2,2,1,1,1))
ddmPortEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:ddmPortEntry.setStatus(_A)
_DdmPortIfIndex_Type=InterfaceIndex
_DdmPortIfIndex_Object=MibTableColumn
ddmPortIfIndex=_DdmPortIfIndex_Object((1,3,6,1,4,1,16177,2,2,1,1,1,1),_DdmPortIfIndex_Type())
ddmPortIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ddmPortIfIndex.setStatus(_A)
_DdmPortIfName_Type=DisplayString
_DdmPortIfName_Object=MibTableColumn
ddmPortIfName=_DdmPortIfName_Object((1,3,6,1,4,1,16177,2,2,1,1,1,2),_DdmPortIfName_Type())
ddmPortIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:ddmPortIfName.setStatus(_A)
class _DdmPortVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6550))
_DdmPortVoltage_Type.__name__=_C
_DdmPortVoltage_Object=MibTableColumn
ddmPortVoltage=_DdmPortVoltage_Object((1,3,6,1,4,1,16177,2,2,1,1,1,3),_DdmPortVoltage_Type())
ddmPortVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:ddmPortVoltage.setStatus(_A)
class _DdmPortTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,128))
_DdmPortTemperature_Type.__name__=_C
_DdmPortTemperature_Object=MibTableColumn
ddmPortTemperature=_DdmPortTemperature_Object((1,3,6,1,4,1,16177,2,2,1,1,1,4),_DdmPortTemperature_Type())
ddmPortTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:ddmPortTemperature.setStatus(_A)
class _DdmPortBiasCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131))
_DdmPortBiasCurrent_Type.__name__=_C
_DdmPortBiasCurrent_Object=MibTableColumn
ddmPortBiasCurrent=_DdmPortBiasCurrent_Object((1,3,6,1,4,1,16177,2,2,1,1,1,5),_DdmPortBiasCurrent_Type())
ddmPortBiasCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:ddmPortBiasCurrent.setStatus(_A)
class _DdmPortTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-4000,820))
_DdmPortTxPower_Type.__name__=_C
_DdmPortTxPower_Object=MibTableColumn
ddmPortTxPower=_DdmPortTxPower_Object((1,3,6,1,4,1,16177,2,2,1,1,1,6),_DdmPortTxPower_Type())
ddmPortTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:ddmPortTxPower.setStatus(_A)
class _DdmPortRxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-4000,820))
_DdmPortRxPower_Type.__name__=_C
_DdmPortRxPower_Object=MibTableColumn
ddmPortRxPower=_DdmPortRxPower_Object((1,3,6,1,4,1,16177,2,2,1,1,1,7),_DdmPortRxPower_Type())
ddmPortRxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:ddmPortRxPower.setStatus(_A)
_DdmConformance_ObjectIdentity=ObjectIdentity
ddmConformance=_DdmConformance_ObjectIdentity((1,3,6,1,4,1,16177,2,2,2))
_DdmGroups_ObjectIdentity=ObjectIdentity
ddmGroups=_DdmGroups_ObjectIdentity((1,3,6,1,4,1,16177,2,2,2,1))
_DdmCompliances_ObjectIdentity=ObjectIdentity
ddmCompliances=_DdmCompliances_ObjectIdentity((1,3,6,1,4,1,16177,2,2,2,2))
ddmPortGroup=ObjectGroup((1,3,6,1,4,1,16177,2,2,2,1,1))
ddmPortGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ddmPortGroup.setStatus(_A)
ddmCompliance=ModuleCompliance((1,3,6,1,4,1,16177,2,2,2,2,1))
ddmCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:ddmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ddmMIB':ddmMIB,'ddmObjects':ddmObjects,'ddmPortTable':ddmPortTable,'ddmPortEntry':ddmPortEntry,_E:ddmPortIfIndex,_F:ddmPortIfName,_G:ddmPortVoltage,_H:ddmPortTemperature,_I:ddmPortBiasCurrent,_J:ddmPortTxPower,_K:ddmPortRxPower,'ddmConformance':ddmConformance,'ddmGroups':ddmGroups,_L:ddmPortGroup,'ddmCompliances':ddmCompliances,'ddmCompliance':ddmCompliance})