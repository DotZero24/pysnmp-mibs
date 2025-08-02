_S='hePsOutputGroup'
_R='hePsUnitGroup'
_Q='hePsOutputMandatoryGroup'
_P='hePsOutputPower'
_O='hePsOutputCurrent'
_N='hePsUnitDescription'
_M='hePsUnitPowerIN'
_L='hePsUnitCurrentIN'
_K='hePsUnitVoltageIN'
_J='hePsOutputVoltage'
_I='hePsOutputIndex'
_H='tenths of a volt'
_G='hundredths of a watt'
_F='milliamperes'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='SCTE-HMS-HE-POWER-SUPPLY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
HeHundredthWatts,HeMilliAmp,HeTenthVolt,hePowerSupply=mibBuilder.importSymbols('SCTE-HMS-HEADENDIDENT-MIB','HeHundredthWatts','HeMilliAmp','HeTenthVolt','hePowerSupply')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hePowerSupplyMIB=ModuleIdentity((1,3,6,1,4,1,5591,1,11,2,2,1))
_HePsMIBObjects_ObjectIdentity=ObjectIdentity
hePsMIBObjects=_HePsMIBObjects_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,2,1,1))
_HePsUnitTable_Object=MibTable
hePsUnitTable=_HePsUnitTable_Object((1,3,6,1,4,1,5591,1,11,2,2,1,1,1))
if mibBuilder.loadTexts:hePsUnitTable.setStatus(_A)
_HePsUnitEntry_Object=MibTableRow
hePsUnitEntry=_HePsUnitEntry_Object((1,3,6,1,4,1,5591,1,11,2,2,1,1,1,1))
hePsUnitEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hePsUnitEntry.setStatus(_A)
_HePsUnitCurrentIN_Type=HeMilliAmp
_HePsUnitCurrentIN_Object=MibTableColumn
hePsUnitCurrentIN=_HePsUnitCurrentIN_Object((1,3,6,1,4,1,5591,1,11,2,2,1,1,1,1,1),_HePsUnitCurrentIN_Type())
hePsUnitCurrentIN.setMaxAccess(_C)
if mibBuilder.loadTexts:hePsUnitCurrentIN.setStatus(_A)
if mibBuilder.loadTexts:hePsUnitCurrentIN.setUnits(_F)
_HePsUnitPowerIN_Type=HeHundredthWatts
_HePsUnitPowerIN_Object=MibTableColumn
hePsUnitPowerIN=_HePsUnitPowerIN_Object((1,3,6,1,4,1,5591,1,11,2,2,1,1,1,1,2),_HePsUnitPowerIN_Type())
hePsUnitPowerIN.setMaxAccess(_C)
if mibBuilder.loadTexts:hePsUnitPowerIN.setStatus(_A)
if mibBuilder.loadTexts:hePsUnitPowerIN.setUnits(_G)
_HePsUnitDescription_Type=DisplayString
_HePsUnitDescription_Object=MibTableColumn
hePsUnitDescription=_HePsUnitDescription_Object((1,3,6,1,4,1,5591,1,11,2,2,1,1,1,1,3),_HePsUnitDescription_Type())
hePsUnitDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hePsUnitDescription.setStatus(_A)
_HePsUnitVoltageIN_Type=HeTenthVolt
_HePsUnitVoltageIN_Object=MibTableColumn
hePsUnitVoltageIN=_HePsUnitVoltageIN_Object((1,3,6,1,4,1,5591,1,11,2,2,1,1,1,1,4),_HePsUnitVoltageIN_Type())
hePsUnitVoltageIN.setMaxAccess(_C)
if mibBuilder.loadTexts:hePsUnitVoltageIN.setStatus(_A)
if mibBuilder.loadTexts:hePsUnitVoltageIN.setUnits(_H)
_HePsOutputTable_Object=MibTable
hePsOutputTable=_HePsOutputTable_Object((1,3,6,1,4,1,5591,1,11,2,2,1,1,2))
if mibBuilder.loadTexts:hePsOutputTable.setStatus(_A)
_HePsOutputEntry_Object=MibTableRow
hePsOutputEntry=_HePsOutputEntry_Object((1,3,6,1,4,1,5591,1,11,2,2,1,1,2,1))
hePsOutputEntry.setIndexNames((0,_D,_E),(0,_B,_I))
if mibBuilder.loadTexts:hePsOutputEntry.setStatus(_A)
_HePsOutputIndex_Type=Unsigned32
_HePsOutputIndex_Object=MibTableColumn
hePsOutputIndex=_HePsOutputIndex_Object((1,3,6,1,4,1,5591,1,11,2,2,1,1,2,1,1),_HePsOutputIndex_Type())
hePsOutputIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hePsOutputIndex.setStatus(_A)
_HePsOutputVoltage_Type=HeTenthVolt
_HePsOutputVoltage_Object=MibTableColumn
hePsOutputVoltage=_HePsOutputVoltage_Object((1,3,6,1,4,1,5591,1,11,2,2,1,1,2,1,2),_HePsOutputVoltage_Type())
hePsOutputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:hePsOutputVoltage.setStatus(_A)
if mibBuilder.loadTexts:hePsOutputVoltage.setUnits(_H)
_HePsOutputCurrent_Type=HeMilliAmp
_HePsOutputCurrent_Object=MibTableColumn
hePsOutputCurrent=_HePsOutputCurrent_Object((1,3,6,1,4,1,5591,1,11,2,2,1,1,2,1,3),_HePsOutputCurrent_Type())
hePsOutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:hePsOutputCurrent.setStatus(_A)
if mibBuilder.loadTexts:hePsOutputCurrent.setUnits(_F)
_HePsOutputPower_Type=HeHundredthWatts
_HePsOutputPower_Object=MibTableColumn
hePsOutputPower=_HePsOutputPower_Object((1,3,6,1,4,1,5591,1,11,2,2,1,1,2,1,4),_HePsOutputPower_Type())
hePsOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hePsOutputPower.setStatus(_A)
if mibBuilder.loadTexts:hePsOutputPower.setUnits(_G)
_HePsMIBConformance_ObjectIdentity=ObjectIdentity
hePsMIBConformance=_HePsMIBConformance_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,2,1,2))
_HePsMIBCompliances_ObjectIdentity=ObjectIdentity
hePsMIBCompliances=_HePsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,2,1,2,1))
_HePsMIBGroups_ObjectIdentity=ObjectIdentity
hePsMIBGroups=_HePsMIBGroups_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,2,1,2,2))
hePsOutputMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,2,2,1,2,2,1))
hePsOutputMandatoryGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:hePsOutputMandatoryGroup.setStatus(_A)
hePsUnitGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,2,2,1,2,2,2))
hePsUnitGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hePsUnitGroup.setStatus(_A)
hePsOutputGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,2,2,1,2,2,3))
hePsOutputGroup.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:hePsOutputGroup.setStatus(_A)
hePsCompliance=ModuleCompliance((1,3,6,1,4,1,5591,1,11,2,2,1,2,1,1))
hePsCompliance.setObjects(*((_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:hePsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hePowerSupplyMIB':hePowerSupplyMIB,'hePsMIBObjects':hePsMIBObjects,'hePsUnitTable':hePsUnitTable,'hePsUnitEntry':hePsUnitEntry,_L:hePsUnitCurrentIN,_M:hePsUnitPowerIN,_N:hePsUnitDescription,_K:hePsUnitVoltageIN,'hePsOutputTable':hePsOutputTable,'hePsOutputEntry':hePsOutputEntry,_I:hePsOutputIndex,_J:hePsOutputVoltage,_O:hePsOutputCurrent,_P:hePsOutputPower,'hePsMIBConformance':hePsMIBConformance,'hePsMIBCompliances':hePsMIBCompliances,'hePsCompliance':hePsCompliance,'hePsMIBGroups':hePsMIBGroups,_Q:hePsOutputMandatoryGroup,_R:hePsUnitGroup,_S:hePsOutputGroup})