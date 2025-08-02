_R='adGenChassisOptionalGroup'
_Q='adGenChassisBaseGroup'
_P='adGenChassisViewAll'
_O='adGenChassisFaceplates'
_N='adGenChassisActiveMux'
_M='adGenChassisProvVersion'
_L='adGenChassisAlarmStatus'
_K='adGenChassisTftpAddr'
_J='adGenChassisTime'
_I='adGenChassisDate'
_H='adGenChassisProduct'
_G='adGenChassisViewIndex'
_F='read-write'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='ADTRAN-GENCHASSIS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adShared,=mibBuilder.importSymbols('ADTRAN-MIB','adShared')
AdProductIdentifier,=mibBuilder.importSymbols('ADTRAN-TC','AdProductIdentifier')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
adGenericShelves=ModuleIdentity((1,3,6,1,4,1,664,5,13))
_AdGenChassis_ObjectIdentity=ObjectIdentity
adGenChassis=_AdGenChassis_ObjectIdentity((1,3,6,1,4,1,664,5,13,1))
_AdGenChassisScalars_ObjectIdentity=ObjectIdentity
adGenChassisScalars=_AdGenChassisScalars_ObjectIdentity((1,3,6,1,4,1,664,5,13,1,1))
_AdGenChassisProduct_Type=AdProductIdentifier
_AdGenChassisProduct_Object=MibScalar
adGenChassisProduct=_AdGenChassisProduct_Object((1,3,6,1,4,1,664,5,13,1,1,1),_AdGenChassisProduct_Type())
adGenChassisProduct.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenChassisProduct.setStatus(_A)
class _AdGenChassisDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_AdGenChassisDate_Type.__name__=_E
_AdGenChassisDate_Object=MibScalar
adGenChassisDate=_AdGenChassisDate_Object((1,3,6,1,4,1,664,5,13,1,1,5),_AdGenChassisDate_Type())
adGenChassisDate.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenChassisDate.setStatus(_A)
class _AdGenChassisTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_AdGenChassisTime_Type.__name__=_E
_AdGenChassisTime_Object=MibScalar
adGenChassisTime=_AdGenChassisTime_Object((1,3,6,1,4,1,664,5,13,1,1,6),_AdGenChassisTime_Type())
adGenChassisTime.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenChassisTime.setStatus(_A)
_AdGenChassisTftpAddr_Type=IpAddress
_AdGenChassisTftpAddr_Object=MibScalar
adGenChassisTftpAddr=_AdGenChassisTftpAddr_Object((1,3,6,1,4,1,664,5,13,1,1,7),_AdGenChassisTftpAddr_Type())
adGenChassisTftpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenChassisTftpAddr.setStatus(_A)
_AdGenChassisAlarmStatus_Type=OctetString
_AdGenChassisAlarmStatus_Object=MibScalar
adGenChassisAlarmStatus=_AdGenChassisAlarmStatus_Object((1,3,6,1,4,1,664,5,13,1,1,9),_AdGenChassisAlarmStatus_Type())
adGenChassisAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenChassisAlarmStatus.setStatus(_A)
_AdGenChassisProvVersion_Type=Integer32
_AdGenChassisProvVersion_Object=MibScalar
adGenChassisProvVersion=_AdGenChassisProvVersion_Object((1,3,6,1,4,1,664,5,13,1,1,10),_AdGenChassisProvVersion_Type())
adGenChassisProvVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenChassisProvVersion.setStatus(_A)
class _AdGenChassisActiveMux_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenChassisActiveMux_Type.__name__=_D
_AdGenChassisActiveMux_Object=MibScalar
adGenChassisActiveMux=_AdGenChassisActiveMux_Object((1,3,6,1,4,1,664,5,13,1,1,11),_AdGenChassisActiveMux_Type())
adGenChassisActiveMux.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenChassisActiveMux.setStatus(_A)
_AdGenChassisViewAll_Type=OctetString
_AdGenChassisViewAll_Object=MibScalar
adGenChassisViewAll=_AdGenChassisViewAll_Object((1,3,6,1,4,1,664,5,13,1,1,12),_AdGenChassisViewAll_Type())
adGenChassisViewAll.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenChassisViewAll.setStatus(_A)
_AdGenChassisTables_ObjectIdentity=ObjectIdentity
adGenChassisTables=_AdGenChassisTables_ObjectIdentity((1,3,6,1,4,1,664,5,13,1,2))
_AdGenChassisViewTable_Object=MibTable
adGenChassisViewTable=_AdGenChassisViewTable_Object((1,3,6,1,4,1,664,5,13,1,2,1))
if mibBuilder.loadTexts:adGenChassisViewTable.setStatus(_A)
_AdGenChassisViewEntry_Object=MibTableRow
adGenChassisViewEntry=_AdGenChassisViewEntry_Object((1,3,6,1,4,1,664,5,13,1,2,1,1))
adGenChassisViewEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:adGenChassisViewEntry.setStatus(_A)
class _AdGenChassisViewIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenChassisViewIndex_Type.__name__=_D
_AdGenChassisViewIndex_Object=MibTableColumn
adGenChassisViewIndex=_AdGenChassisViewIndex_Object((1,3,6,1,4,1,664,5,13,1,2,1,1,1),_AdGenChassisViewIndex_Type())
adGenChassisViewIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenChassisViewIndex.setStatus(_A)
_AdGenChassisFaceplates_Type=OctetString
_AdGenChassisFaceplates_Object=MibTableColumn
adGenChassisFaceplates=_AdGenChassisFaceplates_Object((1,3,6,1,4,1,664,5,13,1,2,1,1,2),_AdGenChassisFaceplates_Type())
adGenChassisFaceplates.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenChassisFaceplates.setStatus(_A)
_AdGenChassisConformance_ObjectIdentity=ObjectIdentity
adGenChassisConformance=_AdGenChassisConformance_ObjectIdentity((1,3,6,1,4,1,664,5,13,99))
_AdGenChassisCompliances_ObjectIdentity=ObjectIdentity
adGenChassisCompliances=_AdGenChassisCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,13,99,1))
_AdGenChassisMIBGroups_ObjectIdentity=ObjectIdentity
adGenChassisMIBGroups=_AdGenChassisMIBGroups_ObjectIdentity((1,3,6,1,4,1,664,5,13,99,2))
adGenChassisBaseGroup=ObjectGroup((1,3,6,1,4,1,664,5,13,99,2,1))
adGenChassisBaseGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_G),(_B,_O)))
if mibBuilder.loadTexts:adGenChassisBaseGroup.setStatus(_A)
adGenChassisOptionalGroup=ObjectGroup((1,3,6,1,4,1,664,5,13,99,2,2))
adGenChassisOptionalGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:adGenChassisOptionalGroup.setStatus(_A)
adGenChassisCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,13,99,1,1))
adGenChassisCompliance.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:adGenChassisCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenericShelves':adGenericShelves,'adGenChassis':adGenChassis,'adGenChassisScalars':adGenChassisScalars,_H:adGenChassisProduct,_I:adGenChassisDate,_J:adGenChassisTime,_K:adGenChassisTftpAddr,_L:adGenChassisAlarmStatus,_M:adGenChassisProvVersion,_N:adGenChassisActiveMux,_P:adGenChassisViewAll,'adGenChassisTables':adGenChassisTables,'adGenChassisViewTable':adGenChassisViewTable,'adGenChassisViewEntry':adGenChassisViewEntry,_G:adGenChassisViewIndex,_O:adGenChassisFaceplates,'adGenChassisConformance':adGenChassisConformance,'adGenChassisCompliances':adGenChassisCompliances,'adGenChassisCompliance':adGenChassisCompliance,'adGenChassisMIBGroups':adGenChassisMIBGroups,_Q:adGenChassisBaseGroup,_R:adGenChassisOptionalGroup})