_Q='satelliteSatelliteGroup'
_P='satelliteGeneralGroup'
_O='satelliteSatelliteExpectedBoardType'
_N='satelliteSatelliteDescr'
_M='satelliteSatelliteName'
_L='satelliteGeneralSatelliteTableSize'
_K='satelliteGeneralStateLastChangeTime'
_J='satelliteGeneralLastChangeTime'
_I='read-write'
_H='DisplayString'
_G='Unsigned32'
_F='Integer32'
_E='MgmtNameString'
_D='satelliteSatelliteIndex'
_C='read-only'
_B='LUM-SATELLITE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumSatelliteMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumSatelliteMIB')
MgmtNameString,=mibBuilder.importSymbols('LUM-TC',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_H,'PhysAddress','TextualConvention')
lumSatelliteMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,36))
if mibBuilder.loadTexts:lumSatelliteMIBModule.setRevisions(('2017-06-15 00:00','2009-06-15 00:00'))
_LumSatelliteConfs_ObjectIdentity=ObjectIdentity
lumSatelliteConfs=_LumSatelliteConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,36,1))
_LumSatelliteGroups_ObjectIdentity=ObjectIdentity
lumSatelliteGroups=_LumSatelliteGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,36,1,1))
_LumSatelliteCompl_ObjectIdentity=ObjectIdentity
lumSatelliteCompl=_LumSatelliteCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,36,1,2))
_LumSatelliteMIBObjects_ObjectIdentity=ObjectIdentity
lumSatelliteMIBObjects=_LumSatelliteMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,36,2))
_SatelliteGeneral_ObjectIdentity=ObjectIdentity
satelliteGeneral=_SatelliteGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,36,2,1))
_SatelliteGeneralLastChangeTime_Type=DateAndTime
_SatelliteGeneralLastChangeTime_Object=MibScalar
satelliteGeneralLastChangeTime=_SatelliteGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,36,2,1,1),_SatelliteGeneralLastChangeTime_Type())
satelliteGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteGeneralLastChangeTime.setStatus(_A)
_SatelliteGeneralStateLastChangeTime_Type=DateAndTime
_SatelliteGeneralStateLastChangeTime_Object=MibScalar
satelliteGeneralStateLastChangeTime=_SatelliteGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,36,2,1,2),_SatelliteGeneralStateLastChangeTime_Type())
satelliteGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteGeneralStateLastChangeTime.setStatus(_A)
_SatelliteGeneralSatelliteTableSize_Type=Unsigned32
_SatelliteGeneralSatelliteTableSize_Object=MibScalar
satelliteGeneralSatelliteTableSize=_SatelliteGeneralSatelliteTableSize_Object((1,3,6,1,4,1,8708,2,36,2,1,3),_SatelliteGeneralSatelliteTableSize_Type())
satelliteGeneralSatelliteTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteGeneralSatelliteTableSize.setStatus(_A)
_SatelliteSatelliteList_ObjectIdentity=ObjectIdentity
satelliteSatelliteList=_SatelliteSatelliteList_ObjectIdentity((1,3,6,1,4,1,8708,2,36,2,2))
_SatelliteSatelliteTable_Object=MibTable
satelliteSatelliteTable=_SatelliteSatelliteTable_Object((1,3,6,1,4,1,8708,2,36,2,2,1))
if mibBuilder.loadTexts:satelliteSatelliteTable.setStatus(_A)
_SatelliteSatelliteEntry_Object=MibTableRow
satelliteSatelliteEntry=_SatelliteSatelliteEntry_Object((1,3,6,1,4,1,8708,2,36,2,2,1,1))
satelliteSatelliteEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:satelliteSatelliteEntry.setStatus(_A)
class _SatelliteSatelliteIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SatelliteSatelliteIndex_Type.__name__=_G
_SatelliteSatelliteIndex_Object=MibTableColumn
satelliteSatelliteIndex=_SatelliteSatelliteIndex_Object((1,3,6,1,4,1,8708,2,36,2,2,1,1,1),_SatelliteSatelliteIndex_Type())
satelliteSatelliteIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteSatelliteIndex.setStatus(_A)
class _SatelliteSatelliteName_Type(MgmtNameString):defaultValue=OctetString('')
_SatelliteSatelliteName_Type.__name__=_E
_SatelliteSatelliteName_Object=MibTableColumn
satelliteSatelliteName=_SatelliteSatelliteName_Object((1,3,6,1,4,1,8708,2,36,2,2,1,1,2),_SatelliteSatelliteName_Type())
satelliteSatelliteName.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteSatelliteName.setStatus(_A)
class _SatelliteSatelliteDescr_Type(DisplayString):defaultValue=OctetString('')
_SatelliteSatelliteDescr_Type.__name__=_H
_SatelliteSatelliteDescr_Object=MibTableColumn
satelliteSatelliteDescr=_SatelliteSatelliteDescr_Object((1,3,6,1,4,1,8708,2,36,2,2,1,1,3),_SatelliteSatelliteDescr_Type())
satelliteSatelliteDescr.setMaxAccess(_I)
if mibBuilder.loadTexts:satelliteSatelliteDescr.setStatus(_A)
class _SatelliteSatelliteExpectedBoardType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mba1',1),('mba2',2)))
_SatelliteSatelliteExpectedBoardType_Type.__name__=_F
_SatelliteSatelliteExpectedBoardType_Object=MibTableColumn
satelliteSatelliteExpectedBoardType=_SatelliteSatelliteExpectedBoardType_Object((1,3,6,1,4,1,8708,2,36,2,2,1,1,4),_SatelliteSatelliteExpectedBoardType_Type())
satelliteSatelliteExpectedBoardType.setMaxAccess(_I)
if mibBuilder.loadTexts:satelliteSatelliteExpectedBoardType.setStatus(_A)
satelliteGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,36,1,1,1))
satelliteGeneralGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:satelliteGeneralGroup.setStatus(_A)
satelliteSatelliteGroup=ObjectGroup((1,3,6,1,4,1,8708,2,36,1,1,2))
satelliteSatelliteGroup.setObjects(*((_B,_D),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:satelliteSatelliteGroup.setStatus(_A)
lumSatelliteBasicCompl1=ModuleCompliance((1,3,6,1,4,1,8708,2,36,1,2,1))
lumSatelliteBasicCompl1.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:lumSatelliteBasicCompl1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lumSatelliteMIBModule':lumSatelliteMIBModule,'lumSatelliteConfs':lumSatelliteConfs,'lumSatelliteGroups':lumSatelliteGroups,_P:satelliteGeneralGroup,_Q:satelliteSatelliteGroup,'lumSatelliteCompl':lumSatelliteCompl,'lumSatelliteBasicCompl1':lumSatelliteBasicCompl1,'lumSatelliteMIBObjects':lumSatelliteMIBObjects,'satelliteGeneral':satelliteGeneral,_J:satelliteGeneralLastChangeTime,_K:satelliteGeneralStateLastChangeTime,_L:satelliteGeneralSatelliteTableSize,'satelliteSatelliteList':satelliteSatelliteList,'satelliteSatelliteTable':satelliteSatelliteTable,'satelliteSatelliteEntry':satelliteSatelliteEntry,_D:satelliteSatelliteIndex,_M:satelliteSatelliteName,_N:satelliteSatelliteDescr,_O:satelliteSatelliteExpectedBoardType})