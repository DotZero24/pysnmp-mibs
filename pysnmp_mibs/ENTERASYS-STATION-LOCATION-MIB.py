_A9='etsysLocationBatchReportGroup2'
_A8='etsysLocationEngineGlobalGroup3'
_A7='etsysLocationBatchReportGroup'
_A6='etsysLocationEngineGlobalGroup2'
_A5='etsysLocationEngineGlobalGroup'
_A4='etsysPublishLocationPassword'
_A3='etsysPublishLocationUserId'
_A2='etsysLocationEngineTrackMode'
_A1='etsysMaxTrackedStationLimit'
_A0='etsysMaxOnDemandStationLimit'
_z='etsysStationLocnGridProbability'
_y='etsysStationLocnGridY'
_x='etsysStationLocnGridX'
_w='etsysTrackedStationAPDistance'
_v='etsysTrackedStationReportingAPSN'
_u='etsysTrackedStationLocationType'
_t='etsysTrackedStationFloorID'
_s='etsysOnDemandStationRowStatus'
_r='etsysLocationFloorConfigured'
_q='etsysLocationMaxFloorLimit'
_p='etsysFloorEnvironment'
_o='etsysFloorHashString'
_n='etsysFloorCellLength'
_m='etsysFloorCellWidth'
_l='etsysFloorNumberOfCells'
_k='etsysFloorLength'
_j='etsysFloorWidth'
_i='etsysFloorNumberOfAPs'
_h='etsysFloorName'
_g='etsysFloorRowStatus'
_f='etsysPublishLocationIndex'
_e='etsysStationLocnGridIndex'
_d='etsysOnDemandStationMAC'
_c='etsysFloorID'
_b='SnmpAdminString'
_a='etsysLocationEngineTrackAreaChange'
_Z='etsysPublishLocationRowStatus'
_Y='etsysPublishLocationURL'
_X='etsysPublishLocationURLNumEntries'
_W='etsysPublishLocationURLMaxEntries'
_V='etsysLocationBatchReportDimensionUnit'
_U='etsysLocationBatchReportFrequency'
_T='etsysLocationBatchReportEnable'
_S='etsysTrackedStationMAC'
_R='OctetString'
_Q='etsysTrackedStationsGroup'
_P='etsysOnDemandStationsGroup'
_O='etsysFloorGroup'
_N='etsysLocationEngineGlobalEnv'
_M='etsysLocationEngineGlblAPHeight'
_L='etsysLocationEngineAutoTrkEnable'
_K='etsysLocationEngineEnable'
_J='deprecated'
_I='not-accessible'
_H='Unsigned32'
_G='centimeters'
_F='Integer32'
_E='read-write'
_D='read-only'
_C='read-create'
_B='current'
_A='ENTERASYS-STATION-LOCATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_b)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
etsysStationLocationMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,98))
if mibBuilder.loadTexts:etsysStationLocationMIB.setRevisions(('2016-05-11 19:36','2015-09-10 16:18','2014-06-13 16:10','2013-04-18 15:20'))
class FloorEnvironmentType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('openSpace',0),('lightDivision',1),('dryWallsDivision',2),('hardDivision',3),('interiorWalls',4)))
_EtsysStationLocationMIBObjects_ObjectIdentity=ObjectIdentity
etsysStationLocationMIBObjects=_EtsysStationLocationMIBObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,98,1))
_EtsysLocationConfiguration_ObjectIdentity=ObjectIdentity
etsysLocationConfiguration=_EtsysLocationConfiguration_ObjectIdentity((1,3,6,1,4,1,5624,1,2,98,1,1))
_EtsysLocationEngineEnable_Type=TruthValue
_EtsysLocationEngineEnable_Object=MibScalar
etsysLocationEngineEnable=_EtsysLocationEngineEnable_Object((1,3,6,1,4,1,5624,1,2,98,1,1,1),_EtsysLocationEngineEnable_Type())
etsysLocationEngineEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysLocationEngineEnable.setStatus(_B)
_EtsysLocationEngineAutoTrkEnable_Type=TruthValue
_EtsysLocationEngineAutoTrkEnable_Object=MibScalar
etsysLocationEngineAutoTrkEnable=_EtsysLocationEngineAutoTrkEnable_Object((1,3,6,1,4,1,5624,1,2,98,1,1,2),_EtsysLocationEngineAutoTrkEnable_Type())
etsysLocationEngineAutoTrkEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysLocationEngineAutoTrkEnable.setStatus(_B)
class _EtsysLocationEngineGlblAPHeight_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_EtsysLocationEngineGlblAPHeight_Type.__name__=_H
_EtsysLocationEngineGlblAPHeight_Object=MibScalar
etsysLocationEngineGlblAPHeight=_EtsysLocationEngineGlblAPHeight_Object((1,3,6,1,4,1,5624,1,2,98,1,1,3),_EtsysLocationEngineGlblAPHeight_Type())
etsysLocationEngineGlblAPHeight.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysLocationEngineGlblAPHeight.setStatus(_B)
if mibBuilder.loadTexts:etsysLocationEngineGlblAPHeight.setUnits(_G)
_EtsysLocationEngineGlobalEnv_Type=FloorEnvironmentType
_EtsysLocationEngineGlobalEnv_Object=MibScalar
etsysLocationEngineGlobalEnv=_EtsysLocationEngineGlobalEnv_Object((1,3,6,1,4,1,5624,1,2,98,1,1,4),_EtsysLocationEngineGlobalEnv_Type())
etsysLocationEngineGlobalEnv.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysLocationEngineGlobalEnv.setStatus(_B)
_EtsysLocationFloors_ObjectIdentity=ObjectIdentity
etsysLocationFloors=_EtsysLocationFloors_ObjectIdentity((1,3,6,1,4,1,5624,1,2,98,1,1,5))
_EtsysLocationMaxFloorLimit_Type=Unsigned32
_EtsysLocationMaxFloorLimit_Object=MibScalar
etsysLocationMaxFloorLimit=_EtsysLocationMaxFloorLimit_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,1),_EtsysLocationMaxFloorLimit_Type())
etsysLocationMaxFloorLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLocationMaxFloorLimit.setStatus(_B)
_EtsysLocationFloorConfigured_Type=Unsigned32
_EtsysLocationFloorConfigured_Object=MibScalar
etsysLocationFloorConfigured=_EtsysLocationFloorConfigured_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,2),_EtsysLocationFloorConfigured_Type())
etsysLocationFloorConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLocationFloorConfigured.setStatus(_B)
_EtsysFloorTable_Object=MibTable
etsysFloorTable=_EtsysFloorTable_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,3))
if mibBuilder.loadTexts:etsysFloorTable.setStatus(_B)
_EtsysFloorEntry_Object=MibTableRow
etsysFloorEntry=_EtsysFloorEntry_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,3,1))
etsysFloorEntry.setIndexNames((0,_A,_c))
if mibBuilder.loadTexts:etsysFloorEntry.setStatus(_B)
_EtsysFloorID_Type=Unsigned32
_EtsysFloorID_Object=MibTableColumn
etsysFloorID=_EtsysFloorID_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,3,1,1),_EtsysFloorID_Type())
etsysFloorID.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysFloorID.setStatus(_B)
_EtsysFloorRowStatus_Type=RowStatus
_EtsysFloorRowStatus_Object=MibTableColumn
etsysFloorRowStatus=_EtsysFloorRowStatus_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,3,1,2),_EtsysFloorRowStatus_Type())
etsysFloorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFloorRowStatus.setStatus(_B)
class _EtsysFloorName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_EtsysFloorName_Type.__name__=_b
_EtsysFloorName_Object=MibTableColumn
etsysFloorName=_EtsysFloorName_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,3,1,3),_EtsysFloorName_Type())
etsysFloorName.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFloorName.setStatus(_B)
_EtsysFloorNumberOfAPs_Type=Unsigned32
_EtsysFloorNumberOfAPs_Object=MibTableColumn
etsysFloorNumberOfAPs=_EtsysFloorNumberOfAPs_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,3,1,4),_EtsysFloorNumberOfAPs_Type())
etsysFloorNumberOfAPs.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFloorNumberOfAPs.setStatus(_B)
_EtsysFloorWidth_Type=Unsigned32
_EtsysFloorWidth_Object=MibTableColumn
etsysFloorWidth=_EtsysFloorWidth_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,3,1,5),_EtsysFloorWidth_Type())
etsysFloorWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFloorWidth.setStatus(_B)
if mibBuilder.loadTexts:etsysFloorWidth.setUnits(_G)
_EtsysFloorLength_Type=Unsigned32
_EtsysFloorLength_Object=MibTableColumn
etsysFloorLength=_EtsysFloorLength_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,3,1,6),_EtsysFloorLength_Type())
etsysFloorLength.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFloorLength.setStatus(_B)
if mibBuilder.loadTexts:etsysFloorLength.setUnits(_G)
_EtsysFloorNumberOfCells_Type=Unsigned32
_EtsysFloorNumberOfCells_Object=MibTableColumn
etsysFloorNumberOfCells=_EtsysFloorNumberOfCells_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,3,1,7),_EtsysFloorNumberOfCells_Type())
etsysFloorNumberOfCells.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFloorNumberOfCells.setStatus(_B)
if mibBuilder.loadTexts:etsysFloorNumberOfCells.setUnits(_G)
_EtsysFloorCellWidth_Type=Unsigned32
_EtsysFloorCellWidth_Object=MibTableColumn
etsysFloorCellWidth=_EtsysFloorCellWidth_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,3,1,8),_EtsysFloorCellWidth_Type())
etsysFloorCellWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFloorCellWidth.setStatus(_B)
if mibBuilder.loadTexts:etsysFloorCellWidth.setUnits(_G)
_EtsysFloorCellLength_Type=Unsigned32
_EtsysFloorCellLength_Object=MibTableColumn
etsysFloorCellLength=_EtsysFloorCellLength_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,3,1,9),_EtsysFloorCellLength_Type())
etsysFloorCellLength.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFloorCellLength.setStatus(_B)
if mibBuilder.loadTexts:etsysFloorCellLength.setUnits(_G)
_EtsysFloorEnvironment_Type=FloorEnvironmentType
_EtsysFloorEnvironment_Object=MibTableColumn
etsysFloorEnvironment=_EtsysFloorEnvironment_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,3,1,10),_EtsysFloorEnvironment_Type())
etsysFloorEnvironment.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFloorEnvironment.setStatus(_B)
class _EtsysFloorHashString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_EtsysFloorHashString_Type.__name__=_R
_EtsysFloorHashString_Object=MibTableColumn
etsysFloorHashString=_EtsysFloorHashString_Object((1,3,6,1,4,1,5624,1,2,98,1,1,5,3,1,11),_EtsysFloorHashString_Type())
etsysFloorHashString.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFloorHashString.setStatus(_B)
_EtsysLocationStations_ObjectIdentity=ObjectIdentity
etsysLocationStations=_EtsysLocationStations_ObjectIdentity((1,3,6,1,4,1,5624,1,2,98,1,1,6))
_EtsysMaxTrackedStationLimit_Type=Unsigned32
_EtsysMaxTrackedStationLimit_Object=MibScalar
etsysMaxTrackedStationLimit=_EtsysMaxTrackedStationLimit_Object((1,3,6,1,4,1,5624,1,2,98,1,1,6,1),_EtsysMaxTrackedStationLimit_Type())
etsysMaxTrackedStationLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMaxTrackedStationLimit.setStatus(_B)
class _EtsysMaxOnDemandStationLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_EtsysMaxOnDemandStationLimit_Type.__name__=_H
_EtsysMaxOnDemandStationLimit_Object=MibScalar
etsysMaxOnDemandStationLimit=_EtsysMaxOnDemandStationLimit_Object((1,3,6,1,4,1,5624,1,2,98,1,1,6,2),_EtsysMaxOnDemandStationLimit_Type())
etsysMaxOnDemandStationLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMaxOnDemandStationLimit.setStatus(_B)
_EtsysOnDemandStationTable_Object=MibTable
etsysOnDemandStationTable=_EtsysOnDemandStationTable_Object((1,3,6,1,4,1,5624,1,2,98,1,1,6,3))
if mibBuilder.loadTexts:etsysOnDemandStationTable.setStatus(_B)
_EtsysOnDemandStationEntry_Object=MibTableRow
etsysOnDemandStationEntry=_EtsysOnDemandStationEntry_Object((1,3,6,1,4,1,5624,1,2,98,1,1,6,3,1))
etsysOnDemandStationEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:etsysOnDemandStationEntry.setStatus(_B)
_EtsysOnDemandStationMAC_Type=MacAddress
_EtsysOnDemandStationMAC_Object=MibTableColumn
etsysOnDemandStationMAC=_EtsysOnDemandStationMAC_Object((1,3,6,1,4,1,5624,1,2,98,1,1,6,3,1,1),_EtsysOnDemandStationMAC_Type())
etsysOnDemandStationMAC.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysOnDemandStationMAC.setStatus(_B)
_EtsysOnDemandStationRowStatus_Type=RowStatus
_EtsysOnDemandStationRowStatus_Object=MibTableColumn
etsysOnDemandStationRowStatus=_EtsysOnDemandStationRowStatus_Object((1,3,6,1,4,1,5624,1,2,98,1,1,6,3,1,2),_EtsysOnDemandStationRowStatus_Type())
etsysOnDemandStationRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysOnDemandStationRowStatus.setStatus(_B)
class _EtsysLocationEngineTrackAreaChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_EtsysLocationEngineTrackAreaChange_Type.__name__=_F
_EtsysLocationEngineTrackAreaChange_Object=MibScalar
etsysLocationEngineTrackAreaChange=_EtsysLocationEngineTrackAreaChange_Object((1,3,6,1,4,1,5624,1,2,98,1,1,7),_EtsysLocationEngineTrackAreaChange_Type())
etsysLocationEngineTrackAreaChange.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysLocationEngineTrackAreaChange.setStatus(_B)
class _EtsysLocationEngineTrackMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('trackClients',1),('trackAll',2),('trackNone',3)))
_EtsysLocationEngineTrackMode_Type.__name__=_F
_EtsysLocationEngineTrackMode_Object=MibScalar
etsysLocationEngineTrackMode=_EtsysLocationEngineTrackMode_Object((1,3,6,1,4,1,5624,1,2,98,1,1,8),_EtsysLocationEngineTrackMode_Type())
etsysLocationEngineTrackMode.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysLocationEngineTrackMode.setStatus(_B)
_EtsysLocationReports_ObjectIdentity=ObjectIdentity
etsysLocationReports=_EtsysLocationReports_ObjectIdentity((1,3,6,1,4,1,5624,1,2,98,1,2))
_EtsysTrackedStationTable_Object=MibTable
etsysTrackedStationTable=_EtsysTrackedStationTable_Object((1,3,6,1,4,1,5624,1,2,98,1,2,1))
if mibBuilder.loadTexts:etsysTrackedStationTable.setStatus(_B)
_EtsysTrackedStationEntry_Object=MibTableRow
etsysTrackedStationEntry=_EtsysTrackedStationEntry_Object((1,3,6,1,4,1,5624,1,2,98,1,2,1,1))
etsysTrackedStationEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:etsysTrackedStationEntry.setStatus(_B)
_EtsysTrackedStationMAC_Type=MacAddress
_EtsysTrackedStationMAC_Object=MibTableColumn
etsysTrackedStationMAC=_EtsysTrackedStationMAC_Object((1,3,6,1,4,1,5624,1,2,98,1,2,1,1,1),_EtsysTrackedStationMAC_Type())
etsysTrackedStationMAC.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysTrackedStationMAC.setStatus(_B)
_EtsysTrackedStationFloorID_Type=Unsigned32
_EtsysTrackedStationFloorID_Object=MibTableColumn
etsysTrackedStationFloorID=_EtsysTrackedStationFloorID_Object((1,3,6,1,4,1,5624,1,2,98,1,2,1,1,2),_EtsysTrackedStationFloorID_Type())
etsysTrackedStationFloorID.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTrackedStationFloorID.setStatus(_B)
class _EtsysTrackedStationLocationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),('rssBasedLocation',1),('cellOfOrigin',2)))
_EtsysTrackedStationLocationType_Type.__name__=_F
_EtsysTrackedStationLocationType_Object=MibTableColumn
etsysTrackedStationLocationType=_EtsysTrackedStationLocationType_Object((1,3,6,1,4,1,5624,1,2,98,1,2,1,1,3),_EtsysTrackedStationLocationType_Type())
etsysTrackedStationLocationType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTrackedStationLocationType.setStatus(_B)
_EtsysTrackedStationReportingAPSN_Type=SnmpAdminString
_EtsysTrackedStationReportingAPSN_Object=MibTableColumn
etsysTrackedStationReportingAPSN=_EtsysTrackedStationReportingAPSN_Object((1,3,6,1,4,1,5624,1,2,98,1,2,1,1,6),_EtsysTrackedStationReportingAPSN_Type())
etsysTrackedStationReportingAPSN.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTrackedStationReportingAPSN.setStatus(_B)
_EtsysTrackedStationAPDistance_Type=Integer32
_EtsysTrackedStationAPDistance_Object=MibTableColumn
etsysTrackedStationAPDistance=_EtsysTrackedStationAPDistance_Object((1,3,6,1,4,1,5624,1,2,98,1,2,1,1,7),_EtsysTrackedStationAPDistance_Type())
etsysTrackedStationAPDistance.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysTrackedStationAPDistance.setStatus(_B)
if mibBuilder.loadTexts:etsysTrackedStationAPDistance.setUnits('meters')
_EtsysStationLocationGridTable_Object=MibTable
etsysStationLocationGridTable=_EtsysStationLocationGridTable_Object((1,3,6,1,4,1,5624,1,2,98,1,2,2))
if mibBuilder.loadTexts:etsysStationLocationGridTable.setStatus(_B)
_EtsysStationLocationGridEntry_Object=MibTableRow
etsysStationLocationGridEntry=_EtsysStationLocationGridEntry_Object((1,3,6,1,4,1,5624,1,2,98,1,2,2,1))
etsysStationLocationGridEntry.setIndexNames((0,_A,_S),(0,_A,_e))
if mibBuilder.loadTexts:etsysStationLocationGridEntry.setStatus(_B)
_EtsysStationLocnGridIndex_Type=Unsigned32
_EtsysStationLocnGridIndex_Object=MibTableColumn
etsysStationLocnGridIndex=_EtsysStationLocnGridIndex_Object((1,3,6,1,4,1,5624,1,2,98,1,2,2,1,1),_EtsysStationLocnGridIndex_Type())
etsysStationLocnGridIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysStationLocnGridIndex.setStatus(_B)
_EtsysStationLocnGridX_Type=Integer32
_EtsysStationLocnGridX_Object=MibTableColumn
etsysStationLocnGridX=_EtsysStationLocnGridX_Object((1,3,6,1,4,1,5624,1,2,98,1,2,2,1,2),_EtsysStationLocnGridX_Type())
etsysStationLocnGridX.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysStationLocnGridX.setStatus(_B)
_EtsysStationLocnGridY_Type=Integer32
_EtsysStationLocnGridY_Object=MibTableColumn
etsysStationLocnGridY=_EtsysStationLocnGridY_Object((1,3,6,1,4,1,5624,1,2,98,1,2,2,1,3),_EtsysStationLocnGridY_Type())
etsysStationLocnGridY.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysStationLocnGridY.setStatus(_B)
class _EtsysStationLocnGridProbability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EtsysStationLocnGridProbability_Type.__name__=_F
_EtsysStationLocnGridProbability_Object=MibTableColumn
etsysStationLocnGridProbability=_EtsysStationLocnGridProbability_Object((1,3,6,1,4,1,5624,1,2,98,1,2,2,1,4),_EtsysStationLocnGridProbability_Type())
etsysStationLocnGridProbability.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysStationLocnGridProbability.setStatus(_B)
_EtsysLocationBatchReport_ObjectIdentity=ObjectIdentity
etsysLocationBatchReport=_EtsysLocationBatchReport_ObjectIdentity((1,3,6,1,4,1,5624,1,2,98,1,3))
_EtsysLocationBatchReportEnable_Type=TruthValue
_EtsysLocationBatchReportEnable_Object=MibScalar
etsysLocationBatchReportEnable=_EtsysLocationBatchReportEnable_Object((1,3,6,1,4,1,5624,1,2,98,1,3,1),_EtsysLocationBatchReportEnable_Type())
etsysLocationBatchReportEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysLocationBatchReportEnable.setStatus(_B)
class _EtsysLocationBatchReportFrequency_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,4294967295))
_EtsysLocationBatchReportFrequency_Type.__name__=_H
_EtsysLocationBatchReportFrequency_Object=MibScalar
etsysLocationBatchReportFrequency=_EtsysLocationBatchReportFrequency_Object((1,3,6,1,4,1,5624,1,2,98,1,3,2),_EtsysLocationBatchReportFrequency_Type())
etsysLocationBatchReportFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysLocationBatchReportFrequency.setStatus(_B)
_EtsysPublishLocationURLMaxEntries_Type=Unsigned32
_EtsysPublishLocationURLMaxEntries_Object=MibScalar
etsysPublishLocationURLMaxEntries=_EtsysPublishLocationURLMaxEntries_Object((1,3,6,1,4,1,5624,1,2,98,1,3,3),_EtsysPublishLocationURLMaxEntries_Type())
etsysPublishLocationURLMaxEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPublishLocationURLMaxEntries.setStatus(_B)
_EtsysPublishLocationURLNumEntries_Type=Unsigned32
_EtsysPublishLocationURLNumEntries_Object=MibScalar
etsysPublishLocationURLNumEntries=_EtsysPublishLocationURLNumEntries_Object((1,3,6,1,4,1,5624,1,2,98,1,3,4),_EtsysPublishLocationURLNumEntries_Type())
etsysPublishLocationURLNumEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPublishLocationURLNumEntries.setStatus(_B)
_EtsysPublishLocationURLTable_Object=MibTable
etsysPublishLocationURLTable=_EtsysPublishLocationURLTable_Object((1,3,6,1,4,1,5624,1,2,98,1,3,5))
if mibBuilder.loadTexts:etsysPublishLocationURLTable.setStatus(_B)
_EtsysPublishLocationURLEntry_Object=MibTableRow
etsysPublishLocationURLEntry=_EtsysPublishLocationURLEntry_Object((1,3,6,1,4,1,5624,1,2,98,1,3,5,1))
etsysPublishLocationURLEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:etsysPublishLocationURLEntry.setStatus(_B)
class _EtsysPublishLocationIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysPublishLocationIndex_Type.__name__=_H
_EtsysPublishLocationIndex_Object=MibTableColumn
etsysPublishLocationIndex=_EtsysPublishLocationIndex_Object((1,3,6,1,4,1,5624,1,2,98,1,3,5,1,1),_EtsysPublishLocationIndex_Type())
etsysPublishLocationIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysPublishLocationIndex.setStatus(_B)
class _EtsysPublishLocationURL_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,512))
_EtsysPublishLocationURL_Type.__name__=_R
_EtsysPublishLocationURL_Object=MibTableColumn
etsysPublishLocationURL=_EtsysPublishLocationURL_Object((1,3,6,1,4,1,5624,1,2,98,1,3,5,1,2),_EtsysPublishLocationURL_Type())
etsysPublishLocationURL.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPublishLocationURL.setStatus(_B)
_EtsysPublishLocationRowStatus_Type=RowStatus
_EtsysPublishLocationRowStatus_Object=MibTableColumn
etsysPublishLocationRowStatus=_EtsysPublishLocationRowStatus_Object((1,3,6,1,4,1,5624,1,2,98,1,3,5,1,3),_EtsysPublishLocationRowStatus_Type())
etsysPublishLocationRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPublishLocationRowStatus.setStatus(_B)
_EtsysPublishLocationUserId_Type=SnmpAdminString
_EtsysPublishLocationUserId_Object=MibTableColumn
etsysPublishLocationUserId=_EtsysPublishLocationUserId_Object((1,3,6,1,4,1,5624,1,2,98,1,3,5,1,4),_EtsysPublishLocationUserId_Type())
etsysPublishLocationUserId.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPublishLocationUserId.setStatus(_B)
_EtsysPublishLocationPassword_Type=SnmpAdminString
_EtsysPublishLocationPassword_Object=MibTableColumn
etsysPublishLocationPassword=_EtsysPublishLocationPassword_Object((1,3,6,1,4,1,5624,1,2,98,1,3,5,1,5),_EtsysPublishLocationPassword_Type())
etsysPublishLocationPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPublishLocationPassword.setStatus(_B)
class _EtsysLocationBatchReportDimensionUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('meter',0),('feet',1)))
_EtsysLocationBatchReportDimensionUnit_Type.__name__=_F
_EtsysLocationBatchReportDimensionUnit_Object=MibScalar
etsysLocationBatchReportDimensionUnit=_EtsysLocationBatchReportDimensionUnit_Object((1,3,6,1,4,1,5624,1,2,98,1,3,6),_EtsysLocationBatchReportDimensionUnit_Type())
etsysLocationBatchReportDimensionUnit.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysLocationBatchReportDimensionUnit.setStatus(_B)
_EtsysStationLocationConformance_ObjectIdentity=ObjectIdentity
etsysStationLocationConformance=_EtsysStationLocationConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,98,2))
_EtsysStationLocationGroups_ObjectIdentity=ObjectIdentity
etsysStationLocationGroups=_EtsysStationLocationGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,98,2,1))
_EtsysStationLocationCompliances_ObjectIdentity=ObjectIdentity
etsysStationLocationCompliances=_EtsysStationLocationCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,98,2,2))
etsysLocationEngineGlobalGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,98,2,1,1))
etsysLocationEngineGlobalGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:etsysLocationEngineGlobalGroup.setStatus(_J)
etsysFloorGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,98,2,1,2))
etsysFloorGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:etsysFloorGroup.setStatus(_B)
etsysOnDemandStationsGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,98,2,1,3))
etsysOnDemandStationsGroup.setObjects((_A,_s))
if mibBuilder.loadTexts:etsysOnDemandStationsGroup.setStatus(_B)
etsysTrackedStationsGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,98,2,1,4))
etsysTrackedStationsGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:etsysTrackedStationsGroup.setStatus(_B)
etsysLocationBatchReportGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,98,2,1,5))
etsysLocationBatchReportGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:etsysLocationBatchReportGroup.setStatus(_J)
etsysLocationEngineGlobalGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,98,2,1,6))
etsysLocationEngineGlobalGroup2.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_a)))
if mibBuilder.loadTexts:etsysLocationEngineGlobalGroup2.setStatus(_J)
etsysLocationEngineGlobalGroup3=ObjectGroup((1,3,6,1,4,1,5624,1,2,98,2,1,7))
etsysLocationEngineGlobalGroup3.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_a),(_A,_A2)))
if mibBuilder.loadTexts:etsysLocationEngineGlobalGroup3.setStatus(_B)
etsysLocationBatchReportGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,98,2,1,8))
etsysLocationBatchReportGroup2.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:etsysLocationBatchReportGroup2.setStatus(_B)
etsysStationLocationCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,98,2,2,1))
etsysStationLocationCompliance.setObjects(*((_A,_A5),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:etsysStationLocationCompliance.setStatus(_J)
etsysStationLocationCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,98,2,2,2))
etsysStationLocationCompliance2.setObjects(*((_A,_A6),(_A,_O),(_A,_P),(_A,_Q),(_A,_A7)))
if mibBuilder.loadTexts:etsysStationLocationCompliance2.setStatus(_J)
etsysStationLocationCompliance3=ModuleCompliance((1,3,6,1,4,1,5624,1,2,98,2,2,3))
etsysStationLocationCompliance3.setObjects(*((_A,_A8),(_A,_O),(_A,_P),(_A,_Q),(_A,_A9)))
if mibBuilder.loadTexts:etsysStationLocationCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'FloorEnvironmentType':FloorEnvironmentType,'etsysStationLocationMIB':etsysStationLocationMIB,'etsysStationLocationMIBObjects':etsysStationLocationMIBObjects,'etsysLocationConfiguration':etsysLocationConfiguration,_K:etsysLocationEngineEnable,_L:etsysLocationEngineAutoTrkEnable,_M:etsysLocationEngineGlblAPHeight,_N:etsysLocationEngineGlobalEnv,'etsysLocationFloors':etsysLocationFloors,_q:etsysLocationMaxFloorLimit,_r:etsysLocationFloorConfigured,'etsysFloorTable':etsysFloorTable,'etsysFloorEntry':etsysFloorEntry,_c:etsysFloorID,_g:etsysFloorRowStatus,_h:etsysFloorName,_i:etsysFloorNumberOfAPs,_j:etsysFloorWidth,_k:etsysFloorLength,_l:etsysFloorNumberOfCells,_m:etsysFloorCellWidth,_n:etsysFloorCellLength,_p:etsysFloorEnvironment,_o:etsysFloorHashString,'etsysLocationStations':etsysLocationStations,_A1:etsysMaxTrackedStationLimit,_A0:etsysMaxOnDemandStationLimit,'etsysOnDemandStationTable':etsysOnDemandStationTable,'etsysOnDemandStationEntry':etsysOnDemandStationEntry,_d:etsysOnDemandStationMAC,_s:etsysOnDemandStationRowStatus,_a:etsysLocationEngineTrackAreaChange,_A2:etsysLocationEngineTrackMode,'etsysLocationReports':etsysLocationReports,'etsysTrackedStationTable':etsysTrackedStationTable,'etsysTrackedStationEntry':etsysTrackedStationEntry,_S:etsysTrackedStationMAC,_t:etsysTrackedStationFloorID,_u:etsysTrackedStationLocationType,_v:etsysTrackedStationReportingAPSN,_w:etsysTrackedStationAPDistance,'etsysStationLocationGridTable':etsysStationLocationGridTable,'etsysStationLocationGridEntry':etsysStationLocationGridEntry,_e:etsysStationLocnGridIndex,_x:etsysStationLocnGridX,_y:etsysStationLocnGridY,_z:etsysStationLocnGridProbability,'etsysLocationBatchReport':etsysLocationBatchReport,_T:etsysLocationBatchReportEnable,_U:etsysLocationBatchReportFrequency,_W:etsysPublishLocationURLMaxEntries,_X:etsysPublishLocationURLNumEntries,'etsysPublishLocationURLTable':etsysPublishLocationURLTable,'etsysPublishLocationURLEntry':etsysPublishLocationURLEntry,_f:etsysPublishLocationIndex,_Y:etsysPublishLocationURL,_Z:etsysPublishLocationRowStatus,_A3:etsysPublishLocationUserId,_A4:etsysPublishLocationPassword,_V:etsysLocationBatchReportDimensionUnit,'etsysStationLocationConformance':etsysStationLocationConformance,'etsysStationLocationGroups':etsysStationLocationGroups,_A5:etsysLocationEngineGlobalGroup,_O:etsysFloorGroup,_P:etsysOnDemandStationsGroup,_Q:etsysTrackedStationsGroup,_A7:etsysLocationBatchReportGroup,_A6:etsysLocationEngineGlobalGroup2,_A8:etsysLocationEngineGlobalGroup3,_A9:etsysLocationBatchReportGroup2,'etsysStationLocationCompliances':etsysStationLocationCompliances,'etsysStationLocationCompliance':etsysStationLocationCompliance,'etsysStationLocationCompliance2':etsysStationLocationCompliance2,'etsysStationLocationCompliance3':etsysStationLocationCompliance3})