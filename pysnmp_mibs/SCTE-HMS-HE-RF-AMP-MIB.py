_P='heRFAmpOutputMandatoryGroup'
_O='heRFAmpOutputAttenuatorControl'
_N='heRFAmpOutputLevel'
_M='heRFAmpSlopeControl'
_L='heRFAmpAttenuatorControl'
_K='heRFAmpGainControlMode'
_J='heRFAmpOutputDescription'
_I='read-only'
_H='heRFAmpOutputIndex'
_G='DisplayString'
_F='Integer32'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-write'
_B='SCTE-HMS-HE-RF-AMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
heRFAmplifierGroup,=mibBuilder.importSymbols('SCTE-HMS-HE-RF-MIB','heRFAmplifierGroup')
HeFaultStatus,HeTenthdB,HeTenthdBmV=mibBuilder.importSymbols('SCTE-HMS-HEADENDIDENT-MIB','HeFaultStatus','HeTenthdB','HeTenthdBmV')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
heRFAmpMIB=ModuleIdentity((1,3,6,1,4,1,5591,1,11,4,1,1))
if mibBuilder.loadTexts:heRFAmpMIB.setRevisions(('2003-09-11 00:00','2003-08-29 00:00'))
_HeRFAmpMIBObjects_ObjectIdentity=ObjectIdentity
heRFAmpMIBObjects=_HeRFAmpMIBObjects_ObjectIdentity((1,3,6,1,4,1,5591,1,11,4,1,1,1))
_HeRFAmpUnitTable_Object=MibTable
heRFAmpUnitTable=_HeRFAmpUnitTable_Object((1,3,6,1,4,1,5591,1,11,4,1,1,1,1))
if mibBuilder.loadTexts:heRFAmpUnitTable.setStatus(_A)
_HeRFAmpUnitEntry_Object=MibTableRow
heRFAmpUnitEntry=_HeRFAmpUnitEntry_Object((1,3,6,1,4,1,5591,1,11,4,1,1,1,1,1))
heRFAmpUnitEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:heRFAmpUnitEntry.setStatus(_A)
class _HeRFAmpGainControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('alc',2),('asc',3),('agc',4),('alsc',5)))
_HeRFAmpGainControlMode_Type.__name__=_F
_HeRFAmpGainControlMode_Object=MibTableColumn
heRFAmpGainControlMode=_HeRFAmpGainControlMode_Object((1,3,6,1,4,1,5591,1,11,4,1,1,1,1,1,1),_HeRFAmpGainControlMode_Type())
heRFAmpGainControlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:heRFAmpGainControlMode.setStatus(_A)
_HeRFAmpAttenuatorControl_Type=HeTenthdB
_HeRFAmpAttenuatorControl_Object=MibTableColumn
heRFAmpAttenuatorControl=_HeRFAmpAttenuatorControl_Object((1,3,6,1,4,1,5591,1,11,4,1,1,1,1,1,2),_HeRFAmpAttenuatorControl_Type())
heRFAmpAttenuatorControl.setMaxAccess(_C)
if mibBuilder.loadTexts:heRFAmpAttenuatorControl.setStatus(_A)
_HeRFAmpSlopeControl_Type=HeTenthdB
_HeRFAmpSlopeControl_Object=MibTableColumn
heRFAmpSlopeControl=_HeRFAmpSlopeControl_Object((1,3,6,1,4,1,5591,1,11,4,1,1,1,1,1,3),_HeRFAmpSlopeControl_Type())
heRFAmpSlopeControl.setMaxAccess(_C)
if mibBuilder.loadTexts:heRFAmpSlopeControl.setStatus(_A)
_HeRFAmpOutputTable_Object=MibTable
heRFAmpOutputTable=_HeRFAmpOutputTable_Object((1,3,6,1,4,1,5591,1,11,4,1,1,1,2))
if mibBuilder.loadTexts:heRFAmpOutputTable.setStatus(_A)
_HeRFAmpOutputEntry_Object=MibTableRow
heRFAmpOutputEntry=_HeRFAmpOutputEntry_Object((1,3,6,1,4,1,5591,1,11,4,1,1,1,2,1))
heRFAmpOutputEntry.setIndexNames((0,_D,_E),(0,_B,_H))
if mibBuilder.loadTexts:heRFAmpOutputEntry.setStatus(_A)
_HeRFAmpOutputIndex_Type=Unsigned32
_HeRFAmpOutputIndex_Object=MibTableColumn
heRFAmpOutputIndex=_HeRFAmpOutputIndex_Object((1,3,6,1,4,1,5591,1,11,4,1,1,1,2,1,1),_HeRFAmpOutputIndex_Type())
heRFAmpOutputIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:heRFAmpOutputIndex.setStatus(_A)
class _HeRFAmpOutputDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HeRFAmpOutputDescription_Type.__name__=_G
_HeRFAmpOutputDescription_Object=MibTableColumn
heRFAmpOutputDescription=_HeRFAmpOutputDescription_Object((1,3,6,1,4,1,5591,1,11,4,1,1,1,2,1,2),_HeRFAmpOutputDescription_Type())
heRFAmpOutputDescription.setMaxAccess(_I)
if mibBuilder.loadTexts:heRFAmpOutputDescription.setStatus(_A)
_HeRFAmpOutputLevel_Type=HeTenthdBmV
_HeRFAmpOutputLevel_Object=MibTableColumn
heRFAmpOutputLevel=_HeRFAmpOutputLevel_Object((1,3,6,1,4,1,5591,1,11,4,1,1,1,2,1,3),_HeRFAmpOutputLevel_Type())
heRFAmpOutputLevel.setMaxAccess(_I)
if mibBuilder.loadTexts:heRFAmpOutputLevel.setStatus(_A)
_HeRFAmpOutputAttenuatorControl_Type=HeTenthdB
_HeRFAmpOutputAttenuatorControl_Object=MibTableColumn
heRFAmpOutputAttenuatorControl=_HeRFAmpOutputAttenuatorControl_Object((1,3,6,1,4,1,5591,1,11,4,1,1,1,2,1,4),_HeRFAmpOutputAttenuatorControl_Type())
heRFAmpOutputAttenuatorControl.setMaxAccess(_C)
if mibBuilder.loadTexts:heRFAmpOutputAttenuatorControl.setStatus(_A)
_HeRFAmpMIBConformance_ObjectIdentity=ObjectIdentity
heRFAmpMIBConformance=_HeRFAmpMIBConformance_ObjectIdentity((1,3,6,1,4,1,5591,1,11,4,1,1,2))
_HeRFAmpMIBCompliances_ObjectIdentity=ObjectIdentity
heRFAmpMIBCompliances=_HeRFAmpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5591,1,11,4,1,1,2,1))
_HeRFAmpMIBGroups_ObjectIdentity=ObjectIdentity
heRFAmpMIBGroups=_HeRFAmpMIBGroups_ObjectIdentity((1,3,6,1,4,1,5591,1,11,4,1,1,2,2))
heRFAmpOutputMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,4,1,1,2,2,1))
heRFAmpOutputMandatoryGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:heRFAmpOutputMandatoryGroup.setStatus(_A)
heRFAmpUnitGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,4,1,1,2,2,2))
heRFAmpUnitGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:heRFAmpUnitGroup.setStatus(_A)
heRFAmpOutputGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,4,1,1,2,2,3))
heRFAmpOutputGroup.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:heRFAmpOutputGroup.setStatus(_A)
heRFAmpBasicCompliance=ModuleCompliance((1,3,6,1,4,1,5591,1,11,4,1,1,2,1,1))
heRFAmpBasicCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:heRFAmpBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'heRFAmpMIB':heRFAmpMIB,'heRFAmpMIBObjects':heRFAmpMIBObjects,'heRFAmpUnitTable':heRFAmpUnitTable,'heRFAmpUnitEntry':heRFAmpUnitEntry,_K:heRFAmpGainControlMode,_L:heRFAmpAttenuatorControl,_M:heRFAmpSlopeControl,'heRFAmpOutputTable':heRFAmpOutputTable,'heRFAmpOutputEntry':heRFAmpOutputEntry,_H:heRFAmpOutputIndex,_J:heRFAmpOutputDescription,_N:heRFAmpOutputLevel,_O:heRFAmpOutputAttenuatorControl,'heRFAmpMIBConformance':heRFAmpMIBConformance,'heRFAmpMIBCompliances':heRFAmpMIBCompliances,'heRFAmpBasicCompliance':heRFAmpBasicCompliance,'heRFAmpMIBGroups':heRFAmpMIBGroups,_P:heRFAmpOutputMandatoryGroup,'heRFAmpUnitGroup':heRFAmpUnitGroup,'heRFAmpOutputGroup':heRFAmpOutputGroup})