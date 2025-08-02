_X='mGpsSourcesGroup'
_W='mGpsStatusGroup'
_V='mGpsSourceDevice'
_U='mGpsSatellitesSnr'
_T='mGpsSatellitesAzimuth'
_S='mGpsSatellitesElevation'
_R='mGpsSatellitesUsed'
_Q='mGpsStatusSatellitesUsed'
_P='mGpsStatusSatellitesVisible'
_O='mGpsStatusHeading'
_N='mGpsStatusSpeed'
_M='mGpsStatusAltitude'
_L='mGpsStatusLongitude'
_K='mGpsStatusLatitude'
_J='mGpsStatusTime'
_I='mGpsStatusFixMode'
_H='mGpsSourceName'
_G='not-accessible'
_F='mGpsSatellitesPrn'
_E='Integer32'
_D='Unsigned32'
_C='read-only'
_B='MDS-SERVICE-GPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mdsServices,=mibBuilder.importSymbols('MDS-ORBIT-SMI-MIB','mdsServices')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
mdsGpsMIB=ModuleIdentity((1,3,6,1,4,1,4130,10,3,12))
if mibBuilder.loadTexts:mdsGpsMIB.setRevisions(('2018-05-16 00:00','2016-06-06 00:00','2015-01-29 00:00'))
_MGpsMIBObjects_ObjectIdentity=ObjectIdentity
mGpsMIBObjects=_MGpsMIBObjects_ObjectIdentity((1,3,6,1,4,1,4130,10,3,12,1))
_MGpsConfig_ObjectIdentity=ObjectIdentity
mGpsConfig=_MGpsConfig_ObjectIdentity((1,3,6,1,4,1,4130,10,3,12,1,1))
_MGpsStatus_ObjectIdentity=ObjectIdentity
mGpsStatus=_MGpsStatus_ObjectIdentity((1,3,6,1,4,1,4130,10,3,12,1,2))
class _MGpsStatusFixMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('nofix',0),('a2dfix',1),('a3dfix',2)))
_MGpsStatusFixMode_Type.__name__=_E
_MGpsStatusFixMode_Object=MibScalar
mGpsStatusFixMode=_MGpsStatusFixMode_Object((1,3,6,1,4,1,4130,10,3,12,1,2,1),_MGpsStatusFixMode_Type())
mGpsStatusFixMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsStatusFixMode.setStatus(_A)
_MGpsStatusTime_Type=OctetString
_MGpsStatusTime_Object=MibScalar
mGpsStatusTime=_MGpsStatusTime_Object((1,3,6,1,4,1,4130,10,3,12,1,2,2),_MGpsStatusTime_Type())
mGpsStatusTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsStatusTime.setStatus(_A)
_MGpsStatusLatitude_Type=OctetString
_MGpsStatusLatitude_Object=MibScalar
mGpsStatusLatitude=_MGpsStatusLatitude_Object((1,3,6,1,4,1,4130,10,3,12,1,2,3),_MGpsStatusLatitude_Type())
mGpsStatusLatitude.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsStatusLatitude.setStatus(_A)
_MGpsStatusLongitude_Type=OctetString
_MGpsStatusLongitude_Object=MibScalar
mGpsStatusLongitude=_MGpsStatusLongitude_Object((1,3,6,1,4,1,4130,10,3,12,1,2,4),_MGpsStatusLongitude_Type())
mGpsStatusLongitude.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsStatusLongitude.setStatus(_A)
_MGpsStatusAltitude_Type=OctetString
_MGpsStatusAltitude_Object=MibScalar
mGpsStatusAltitude=_MGpsStatusAltitude_Object((1,3,6,1,4,1,4130,10,3,12,1,2,5),_MGpsStatusAltitude_Type())
mGpsStatusAltitude.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsStatusAltitude.setStatus(_A)
_MGpsStatusSpeed_Type=OctetString
_MGpsStatusSpeed_Object=MibScalar
mGpsStatusSpeed=_MGpsStatusSpeed_Object((1,3,6,1,4,1,4130,10,3,12,1,2,6),_MGpsStatusSpeed_Type())
mGpsStatusSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsStatusSpeed.setStatus(_A)
_MGpsStatusHeading_Type=OctetString
_MGpsStatusHeading_Object=MibScalar
mGpsStatusHeading=_MGpsStatusHeading_Object((1,3,6,1,4,1,4130,10,3,12,1,2,7),_MGpsStatusHeading_Type())
mGpsStatusHeading.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsStatusHeading.setStatus(_A)
class _MGpsStatusSatellitesVisible_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MGpsStatusSatellitesVisible_Type.__name__=_D
_MGpsStatusSatellitesVisible_Object=MibScalar
mGpsStatusSatellitesVisible=_MGpsStatusSatellitesVisible_Object((1,3,6,1,4,1,4130,10,3,12,1,2,8),_MGpsStatusSatellitesVisible_Type())
mGpsStatusSatellitesVisible.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsStatusSatellitesVisible.setStatus(_A)
class _MGpsStatusSatellitesUsed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MGpsStatusSatellitesUsed_Type.__name__=_D
_MGpsStatusSatellitesUsed_Object=MibScalar
mGpsStatusSatellitesUsed=_MGpsStatusSatellitesUsed_Object((1,3,6,1,4,1,4130,10,3,12,1,2,9),_MGpsStatusSatellitesUsed_Type())
mGpsStatusSatellitesUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsStatusSatellitesUsed.setStatus(_A)
_MGpsSatellitesTable_Object=MibTable
mGpsSatellitesTable=_MGpsSatellitesTable_Object((1,3,6,1,4,1,4130,10,3,12,1,2,10))
if mibBuilder.loadTexts:mGpsSatellitesTable.setStatus(_A)
_MGpsSatellitesEntry_Object=MibTableRow
mGpsSatellitesEntry=_MGpsSatellitesEntry_Object((1,3,6,1,4,1,4130,10,3,12,1,2,10,1))
mGpsSatellitesEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:mGpsSatellitesEntry.setStatus(_A)
class _MGpsSatellitesPrn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MGpsSatellitesPrn_Type.__name__=_D
_MGpsSatellitesPrn_Object=MibTableColumn
mGpsSatellitesPrn=_MGpsSatellitesPrn_Object((1,3,6,1,4,1,4130,10,3,12,1,2,10,1,1),_MGpsSatellitesPrn_Type())
mGpsSatellitesPrn.setMaxAccess(_G)
if mibBuilder.loadTexts:mGpsSatellitesPrn.setStatus(_A)
_MGpsSatellitesUsed_Type=TruthValue
_MGpsSatellitesUsed_Object=MibTableColumn
mGpsSatellitesUsed=_MGpsSatellitesUsed_Object((1,3,6,1,4,1,4130,10,3,12,1,2,10,1,2),_MGpsSatellitesUsed_Type())
mGpsSatellitesUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsSatellitesUsed.setStatus(_A)
class _MGpsSatellitesElevation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MGpsSatellitesElevation_Type.__name__=_D
_MGpsSatellitesElevation_Object=MibTableColumn
mGpsSatellitesElevation=_MGpsSatellitesElevation_Object((1,3,6,1,4,1,4130,10,3,12,1,2,10,1,3),_MGpsSatellitesElevation_Type())
mGpsSatellitesElevation.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsSatellitesElevation.setStatus(_A)
class _MGpsSatellitesAzimuth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MGpsSatellitesAzimuth_Type.__name__=_D
_MGpsSatellitesAzimuth_Object=MibTableColumn
mGpsSatellitesAzimuth=_MGpsSatellitesAzimuth_Object((1,3,6,1,4,1,4130,10,3,12,1,2,10,1,4),_MGpsSatellitesAzimuth_Type())
mGpsSatellitesAzimuth.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsSatellitesAzimuth.setStatus(_A)
class _MGpsSatellitesSnr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MGpsSatellitesSnr_Type.__name__=_D
_MGpsSatellitesSnr_Object=MibTableColumn
mGpsSatellitesSnr=_MGpsSatellitesSnr_Object((1,3,6,1,4,1,4130,10,3,12,1,2,10,1,5),_MGpsSatellitesSnr_Type())
mGpsSatellitesSnr.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsSatellitesSnr.setStatus(_A)
_MGpsSourcesTable_Object=MibTable
mGpsSourcesTable=_MGpsSourcesTable_Object((1,3,6,1,4,1,4130,10,3,12,1,3))
if mibBuilder.loadTexts:mGpsSourcesTable.setStatus(_A)
_MGpsSourcesEntry_Object=MibTableRow
mGpsSourcesEntry=_MGpsSourcesEntry_Object((1,3,6,1,4,1,4130,10,3,12,1,3,1))
mGpsSourcesEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:mGpsSourcesEntry.setStatus(_A)
_MGpsSourceName_Type=DisplayString
_MGpsSourceName_Object=MibTableColumn
mGpsSourceName=_MGpsSourceName_Object((1,3,6,1,4,1,4130,10,3,12,1,3,1,1),_MGpsSourceName_Type())
mGpsSourceName.setMaxAccess(_G)
if mibBuilder.loadTexts:mGpsSourceName.setStatus(_A)
_MGpsSourceDevice_Type=OctetString
_MGpsSourceDevice_Object=MibTableColumn
mGpsSourceDevice=_MGpsSourceDevice_Object((1,3,6,1,4,1,4130,10,3,12,1,3,1,2),_MGpsSourceDevice_Type())
mGpsSourceDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:mGpsSourceDevice.setStatus(_A)
_MdsGpsMIBConformance_ObjectIdentity=ObjectIdentity
mdsGpsMIBConformance=_MdsGpsMIBConformance_ObjectIdentity((1,3,6,1,4,1,4130,10,3,12,3))
_MdsGpsMIBCompliances_ObjectIdentity=ObjectIdentity
mdsGpsMIBCompliances=_MdsGpsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4130,10,3,12,3,1))
_MdsGpsMIBGroups_ObjectIdentity=ObjectIdentity
mdsGpsMIBGroups=_MdsGpsMIBGroups_ObjectIdentity((1,3,6,1,4,1,4130,10,3,12,3,2))
mGpsStatusGroup=ObjectGroup((1,3,6,1,4,1,4130,10,3,12,3,2,1))
mGpsStatusGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:mGpsStatusGroup.setStatus(_A)
mGpsSourcesGroup=ObjectGroup((1,3,6,1,4,1,4130,10,3,12,3,2,2))
mGpsSourcesGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:mGpsSourcesGroup.setStatus(_A)
mGpsCompliance=ModuleCompliance((1,3,6,1,4,1,4130,10,3,12,3,1,1))
mGpsCompliance.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:mGpsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mdsGpsMIB':mdsGpsMIB,'mGpsMIBObjects':mGpsMIBObjects,'mGpsConfig':mGpsConfig,'mGpsStatus':mGpsStatus,_I:mGpsStatusFixMode,_J:mGpsStatusTime,_K:mGpsStatusLatitude,_L:mGpsStatusLongitude,_M:mGpsStatusAltitude,_N:mGpsStatusSpeed,_O:mGpsStatusHeading,_P:mGpsStatusSatellitesVisible,_Q:mGpsStatusSatellitesUsed,'mGpsSatellitesTable':mGpsSatellitesTable,'mGpsSatellitesEntry':mGpsSatellitesEntry,_F:mGpsSatellitesPrn,_R:mGpsSatellitesUsed,_S:mGpsSatellitesElevation,_T:mGpsSatellitesAzimuth,_U:mGpsSatellitesSnr,'mGpsSourcesTable':mGpsSourcesTable,'mGpsSourcesEntry':mGpsSourcesEntry,_H:mGpsSourceName,_V:mGpsSourceDevice,'mdsGpsMIBConformance':mdsGpsMIBConformance,'mdsGpsMIBCompliances':mdsGpsMIBCompliances,'mGpsCompliance':mGpsCompliance,'mdsGpsMIBGroups':mdsGpsMIBGroups,_W:mGpsStatusGroup,_X:mGpsSourcesGroup})