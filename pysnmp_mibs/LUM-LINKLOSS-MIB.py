_N='linkLossStatusGroup'
_M='linkLossGeneralGroup'
_L='linkLossStatusMeasurementFailedFiveSec'
_K='linkLossStatusMeasurementFailedOneDb'
_J='linkLossStatusMeasurementFailed'
_I='linkLossStatusThresholdExceeded'
_H='linkLossGeneralStatusTableSize'
_G='linkLossGeneralStateLastChangeTime'
_F='linkLossGeneralConfigLastChangeTime'
_E='Unsigned32'
_D='linkLossStatusIndex'
_C='read-only'
_B='LUM-LINKLOSS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumLinkLossMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumLinkLossMIB','lumModules')
FaultStatus,=mibBuilder.importSymbols('LUM-TC','FaultStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumLinkLossMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,45))
if mibBuilder.loadTexts:lumLinkLossMIBModule.setRevisions(('2017-06-15 00:00','2012-03-09 00:00'))
_LumLinkLossConfs_ObjectIdentity=ObjectIdentity
lumLinkLossConfs=_LumLinkLossConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,45,1))
_LumLinkLossGroups_ObjectIdentity=ObjectIdentity
lumLinkLossGroups=_LumLinkLossGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,45,1,1))
_LumLinkLossCompl_ObjectIdentity=ObjectIdentity
lumLinkLossCompl=_LumLinkLossCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,45,1,2))
_LumLinkLossMIBObjects_ObjectIdentity=ObjectIdentity
lumLinkLossMIBObjects=_LumLinkLossMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,45,2))
_LinkLossGeneral_ObjectIdentity=ObjectIdentity
linkLossGeneral=_LinkLossGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,45,2,1))
_LinkLossGeneralConfigLastChangeTime_Type=DateAndTime
_LinkLossGeneralConfigLastChangeTime_Object=MibScalar
linkLossGeneralConfigLastChangeTime=_LinkLossGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,45,2,1,1),_LinkLossGeneralConfigLastChangeTime_Type())
linkLossGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:linkLossGeneralConfigLastChangeTime.setStatus(_A)
_LinkLossGeneralStateLastChangeTime_Type=DateAndTime
_LinkLossGeneralStateLastChangeTime_Object=MibScalar
linkLossGeneralStateLastChangeTime=_LinkLossGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,45,2,1,2),_LinkLossGeneralStateLastChangeTime_Type())
linkLossGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:linkLossGeneralStateLastChangeTime.setStatus(_A)
_LinkLossGeneralStatusTableSize_Type=Unsigned32
_LinkLossGeneralStatusTableSize_Object=MibScalar
linkLossGeneralStatusTableSize=_LinkLossGeneralStatusTableSize_Object((1,3,6,1,4,1,8708,2,45,2,1,3),_LinkLossGeneralStatusTableSize_Type())
linkLossGeneralStatusTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:linkLossGeneralStatusTableSize.setStatus(_A)
_LinkLossStatusList_ObjectIdentity=ObjectIdentity
linkLossStatusList=_LinkLossStatusList_ObjectIdentity((1,3,6,1,4,1,8708,2,45,2,2))
_LinkLossStatusTable_Object=MibTable
linkLossStatusTable=_LinkLossStatusTable_Object((1,3,6,1,4,1,8708,2,45,2,2,1))
if mibBuilder.loadTexts:linkLossStatusTable.setStatus(_A)
_LinkLossStatusEntry_Object=MibTableRow
linkLossStatusEntry=_LinkLossStatusEntry_Object((1,3,6,1,4,1,8708,2,45,2,2,1,1))
linkLossStatusEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:linkLossStatusEntry.setStatus(_A)
class _LinkLossStatusIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LinkLossStatusIndex_Type.__name__=_E
_LinkLossStatusIndex_Object=MibTableColumn
linkLossStatusIndex=_LinkLossStatusIndex_Object((1,3,6,1,4,1,8708,2,45,2,2,1,1,1),_LinkLossStatusIndex_Type())
linkLossStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:linkLossStatusIndex.setStatus(_A)
_LinkLossStatusThresholdExceeded_Type=FaultStatus
_LinkLossStatusThresholdExceeded_Object=MibTableColumn
linkLossStatusThresholdExceeded=_LinkLossStatusThresholdExceeded_Object((1,3,6,1,4,1,8708,2,45,2,2,1,1,2),_LinkLossStatusThresholdExceeded_Type())
linkLossStatusThresholdExceeded.setMaxAccess(_C)
if mibBuilder.loadTexts:linkLossStatusThresholdExceeded.setStatus(_A)
_LinkLossStatusMeasurementFailed_Type=FaultStatus
_LinkLossStatusMeasurementFailed_Object=MibTableColumn
linkLossStatusMeasurementFailed=_LinkLossStatusMeasurementFailed_Object((1,3,6,1,4,1,8708,2,45,2,2,1,1,3),_LinkLossStatusMeasurementFailed_Type())
linkLossStatusMeasurementFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:linkLossStatusMeasurementFailed.setStatus(_A)
_LinkLossStatusMeasurementFailedOneDb_Type=FaultStatus
_LinkLossStatusMeasurementFailedOneDb_Object=MibTableColumn
linkLossStatusMeasurementFailedOneDb=_LinkLossStatusMeasurementFailedOneDb_Object((1,3,6,1,4,1,8708,2,45,2,2,1,1,4),_LinkLossStatusMeasurementFailedOneDb_Type())
linkLossStatusMeasurementFailedOneDb.setMaxAccess(_C)
if mibBuilder.loadTexts:linkLossStatusMeasurementFailedOneDb.setStatus(_A)
_LinkLossStatusMeasurementFailedFiveSec_Type=FaultStatus
_LinkLossStatusMeasurementFailedFiveSec_Object=MibTableColumn
linkLossStatusMeasurementFailedFiveSec=_LinkLossStatusMeasurementFailedFiveSec_Object((1,3,6,1,4,1,8708,2,45,2,2,1,1,5),_LinkLossStatusMeasurementFailedFiveSec_Type())
linkLossStatusMeasurementFailedFiveSec.setMaxAccess(_C)
if mibBuilder.loadTexts:linkLossStatusMeasurementFailedFiveSec.setStatus(_A)
linkLossGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,45,1,1,1))
linkLossGeneralGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:linkLossGeneralGroup.setStatus(_A)
linkLossStatusGroup=ObjectGroup((1,3,6,1,4,1,8708,2,45,1,1,2))
linkLossStatusGroup.setObjects(*((_B,_D),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:linkLossStatusGroup.setStatus(_A)
lumLinkLossBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,45,1,2,1))
lumLinkLossBasicComplV1.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:lumLinkLossBasicComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lumLinkLossMIBModule':lumLinkLossMIBModule,'lumLinkLossConfs':lumLinkLossConfs,'lumLinkLossGroups':lumLinkLossGroups,_M:linkLossGeneralGroup,_N:linkLossStatusGroup,'lumLinkLossCompl':lumLinkLossCompl,'lumLinkLossBasicComplV1':lumLinkLossBasicComplV1,'lumLinkLossMIBObjects':lumLinkLossMIBObjects,'linkLossGeneral':linkLossGeneral,_F:linkLossGeneralConfigLastChangeTime,_G:linkLossGeneralStateLastChangeTime,_H:linkLossGeneralStatusTableSize,'linkLossStatusList':linkLossStatusList,'linkLossStatusTable':linkLossStatusTable,'linkLossStatusEntry':linkLossStatusEntry,_D:linkLossStatusIndex,_I:linkLossStatusThresholdExceeded,_J:linkLossStatusMeasurementFailed,_K:linkLossStatusMeasurementFailedOneDb,_L:linkLossStatusMeasurementFailedFiveSec})