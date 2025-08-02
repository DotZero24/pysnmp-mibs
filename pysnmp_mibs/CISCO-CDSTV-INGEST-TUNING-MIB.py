_L='ciscoCdstvIngestTuningMIBMainObjectGroup'
_K='cdstvServerRateStandardize'
_J='cdstvServerSequenceEndRemove'
_I='cdstvServerPIDStandardization'
_H='cdstvTrickModeSpeed'
_G='cdstvTrickModeSpeedIndex'
_F='disabled'
_E='enabled'
_D='read-write'
_C='Integer32'
_B='CISCO-CDSTV-INGEST-TUNING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoCdstvIngestTuningMIB=ModuleIdentity((1,3,6,1,4,1,9,9,750))
if mibBuilder.loadTexts:ciscoCdstvIngestTuningMIB.setRevisions(('2010-06-24 00:00',))
_CiscoCdstvIngestTuningMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCdstvIngestTuningMIBNotifs=_CiscoCdstvIngestTuningMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,750,0))
_CiscoCdstvIngestTuningMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCdstvIngestTuningMIBObjects=_CiscoCdstvIngestTuningMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,750,1))
_CdstvTrickModeSpeedTable_Object=MibTable
cdstvTrickModeSpeedTable=_CdstvTrickModeSpeedTable_Object((1,3,6,1,4,1,9,9,750,1,1))
if mibBuilder.loadTexts:cdstvTrickModeSpeedTable.setStatus(_A)
_CdstvTrickModeSpeedEntry_Object=MibTableRow
cdstvTrickModeSpeedEntry=_CdstvTrickModeSpeedEntry_Object((1,3,6,1,4,1,9,9,750,1,1,1))
cdstvTrickModeSpeedEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:cdstvTrickModeSpeedEntry.setStatus(_A)
_CdstvTrickModeSpeedIndex_Type=Unsigned32
_CdstvTrickModeSpeedIndex_Object=MibTableColumn
cdstvTrickModeSpeedIndex=_CdstvTrickModeSpeedIndex_Object((1,3,6,1,4,1,9,9,750,1,1,1,1),_CdstvTrickModeSpeedIndex_Type())
cdstvTrickModeSpeedIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cdstvTrickModeSpeedIndex.setStatus(_A)
class _CdstvTrickModeSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,127))
_CdstvTrickModeSpeed_Type.__name__=_C
_CdstvTrickModeSpeed_Object=MibTableColumn
cdstvTrickModeSpeed=_CdstvTrickModeSpeed_Object((1,3,6,1,4,1,9,9,750,1,1,1,2),_CdstvTrickModeSpeed_Type())
cdstvTrickModeSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvTrickModeSpeed.setStatus(_A)
_CdstvServerIngestMPEGSettings_ObjectIdentity=ObjectIdentity
cdstvServerIngestMPEGSettings=_CdstvServerIngestMPEGSettings_ObjectIdentity((1,3,6,1,4,1,9,9,750,1,2))
class _CdstvServerPIDStandardization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_CdstvServerPIDStandardization_Type.__name__=_C
_CdstvServerPIDStandardization_Object=MibScalar
cdstvServerPIDStandardization=_CdstvServerPIDStandardization_Object((1,3,6,1,4,1,9,9,750,1,2,1),_CdstvServerPIDStandardization_Type())
cdstvServerPIDStandardization.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvServerPIDStandardization.setStatus(_A)
class _CdstvServerSequenceEndRemove_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_CdstvServerSequenceEndRemove_Type.__name__=_C
_CdstvServerSequenceEndRemove_Object=MibScalar
cdstvServerSequenceEndRemove=_CdstvServerSequenceEndRemove_Object((1,3,6,1,4,1,9,9,750,1,2,2),_CdstvServerSequenceEndRemove_Type())
cdstvServerSequenceEndRemove.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvServerSequenceEndRemove.setStatus(_A)
class _CdstvServerRateStandardize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_CdstvServerRateStandardize_Type.__name__=_C
_CdstvServerRateStandardize_Object=MibScalar
cdstvServerRateStandardize=_CdstvServerRateStandardize_Object((1,3,6,1,4,1,9,9,750,1,2,3),_CdstvServerRateStandardize_Type())
cdstvServerRateStandardize.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvServerRateStandardize.setStatus(_A)
_CiscoCdstvIngestTuningMIBConform_ObjectIdentity=ObjectIdentity
ciscoCdstvIngestTuningMIBConform=_CiscoCdstvIngestTuningMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,750,2))
_CiscoCdstvIngestTuningMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCdstvIngestTuningMIBCompliances=_CiscoCdstvIngestTuningMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,750,2,1))
_CiscoCdstvIngestTuningMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCdstvIngestTuningMIBGroups=_CiscoCdstvIngestTuningMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,750,2,2))
ciscoCdstvIngestTuningMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,750,2,2,1))
ciscoCdstvIngestTuningMIBMainObjectGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ciscoCdstvIngestTuningMIBMainObjectGroup.setStatus(_A)
ciscoCdstvIngestTuningMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,750,2,1,1))
ciscoCdstvIngestTuningMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:ciscoCdstvIngestTuningMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCdstvIngestTuningMIB':ciscoCdstvIngestTuningMIB,'ciscoCdstvIngestTuningMIBNotifs':ciscoCdstvIngestTuningMIBNotifs,'ciscoCdstvIngestTuningMIBObjects':ciscoCdstvIngestTuningMIBObjects,'cdstvTrickModeSpeedTable':cdstvTrickModeSpeedTable,'cdstvTrickModeSpeedEntry':cdstvTrickModeSpeedEntry,_G:cdstvTrickModeSpeedIndex,_H:cdstvTrickModeSpeed,'cdstvServerIngestMPEGSettings':cdstvServerIngestMPEGSettings,_I:cdstvServerPIDStandardization,_J:cdstvServerSequenceEndRemove,_K:cdstvServerRateStandardize,'ciscoCdstvIngestTuningMIBConform':ciscoCdstvIngestTuningMIBConform,'ciscoCdstvIngestTuningMIBCompliances':ciscoCdstvIngestTuningMIBCompliances,'ciscoCdstvIngestTuningMIBCompliance':ciscoCdstvIngestTuningMIBCompliance,'ciscoCdstvIngestTuningMIBGroups':ciscoCdstvIngestTuningMIBGroups,_L:ciscoCdstvIngestTuningMIBMainObjectGroup})