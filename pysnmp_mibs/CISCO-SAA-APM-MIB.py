_c='ciscoSaaApmOperGroup'
_b='ciscoSaaApmCtrlGroup'
_a='ciscoSaaApmApplGroup'
_Z='saaApmOperLastStatus'
_Y='saaApmOperLastEndTime'
_X='saaApmOperLastStartTime'
_W='saaApmCtrlNvgen'
_V='saaApmCtrlStatus'
_U='saaApmCtrlDataTransStatus'
_T='saaApmCtrlDataTransTime'
_S='saaApmCtrlInitDataTrans'
_R='saaApmCtrlOwner'
_Q='saaApmCtrlScriptCfgURL'
_P='saaApmApplOperCapacity'
_O='saaApmApplFreeMemLowWaterMark'
_N='saaApmApplMaxOper'
_M='saaApmApplMinorVersion'
_L='saaApmApplMajorVersion'
_K='saaApmOperEntry'
_J='saaApmCtrlIndex'
_I='noError'
_H='Gauge32'
_G='OwnerString'
_F='TruthValue'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='CISCO-SAA-APM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
OwnerString,=mibBuilder.importSymbols('IF-MIB',_G)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_H,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_F)
ciscoSaaApmMIB=ModuleIdentity((1,3,6,1,4,1,9,9,177))
if mibBuilder.loadTexts:ciscoSaaApmMIB.setRevisions(('2000-10-10 00:00',))
class SaaApmOperErrorCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_I,1),('ftpDnldErr',2),('targetDown',3),('scriptErr',4),('socketErr',5),('internalErr',6),('digestErr',7),('fileHeaderErr',8),('fileFormatErr',9),('cacheFull',10),('lowMem',11)))
class SaaApmDataTransErrorCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('ftpErr',2),('timeoutErr',3)))
_CiscoSaaApmMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSaaApmMIBObjects=_CiscoSaaApmMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,177,1))
_SaaApmAppl_ObjectIdentity=ObjectIdentity
saaApmAppl=_SaaApmAppl_ObjectIdentity((1,3,6,1,4,1,9,9,177,1,1))
class _SaaApmApplMajorVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_SaaApmApplMajorVersion_Type.__name__=_D
_SaaApmApplMajorVersion_Object=MibScalar
saaApmApplMajorVersion=_SaaApmApplMajorVersion_Object((1,3,6,1,4,1,9,9,177,1,1,1),_SaaApmApplMajorVersion_Type())
saaApmApplMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:saaApmApplMajorVersion.setStatus(_A)
class _SaaApmApplMinorVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_SaaApmApplMinorVersion_Type.__name__=_D
_SaaApmApplMinorVersion_Object=MibScalar
saaApmApplMinorVersion=_SaaApmApplMinorVersion_Object((1,3,6,1,4,1,9,9,177,1,1,2),_SaaApmApplMinorVersion_Type())
saaApmApplMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:saaApmApplMinorVersion.setStatus(_A)
class _SaaApmApplMaxOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_SaaApmApplMaxOper_Type.__name__=_D
_SaaApmApplMaxOper_Object=MibScalar
saaApmApplMaxOper=_SaaApmApplMaxOper_Object((1,3,6,1,4,1,9,9,177,1,1,3),_SaaApmApplMaxOper_Type())
saaApmApplMaxOper.setMaxAccess(_C)
if mibBuilder.loadTexts:saaApmApplMaxOper.setStatus(_A)
class _SaaApmApplFreeMemLowWaterMark_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SaaApmApplFreeMemLowWaterMark_Type.__name__=_D
_SaaApmApplFreeMemLowWaterMark_Object=MibScalar
saaApmApplFreeMemLowWaterMark=_SaaApmApplFreeMemLowWaterMark_Object((1,3,6,1,4,1,9,9,177,1,1,4),_SaaApmApplFreeMemLowWaterMark_Type())
saaApmApplFreeMemLowWaterMark.setMaxAccess('read-write')
if mibBuilder.loadTexts:saaApmApplFreeMemLowWaterMark.setStatus(_A)
if mibBuilder.loadTexts:saaApmApplFreeMemLowWaterMark.setUnits('bytes')
class _SaaApmApplOperCapacity_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_SaaApmApplOperCapacity_Type.__name__=_H
_SaaApmApplOperCapacity_Object=MibScalar
saaApmApplOperCapacity=_SaaApmApplOperCapacity_Object((1,3,6,1,4,1,9,9,177,1,1,5),_SaaApmApplOperCapacity_Type())
saaApmApplOperCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:saaApmApplOperCapacity.setStatus(_A)
_SaaApmCtrl_ObjectIdentity=ObjectIdentity
saaApmCtrl=_SaaApmCtrl_ObjectIdentity((1,3,6,1,4,1,9,9,177,1,2))
_SaaApmCtrlTable_Object=MibTable
saaApmCtrlTable=_SaaApmCtrlTable_Object((1,3,6,1,4,1,9,9,177,1,2,1))
if mibBuilder.loadTexts:saaApmCtrlTable.setStatus(_A)
_SaaApmCtrlEntry_Object=MibTableRow
saaApmCtrlEntry=_SaaApmCtrlEntry_Object((1,3,6,1,4,1,9,9,177,1,2,1,1))
saaApmCtrlEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:saaApmCtrlEntry.setStatus(_A)
class _SaaApmCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SaaApmCtrlIndex_Type.__name__=_D
_SaaApmCtrlIndex_Object=MibTableColumn
saaApmCtrlIndex=_SaaApmCtrlIndex_Object((1,3,6,1,4,1,9,9,177,1,2,1,1,1),_SaaApmCtrlIndex_Type())
saaApmCtrlIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:saaApmCtrlIndex.setStatus(_A)
_SaaApmCtrlScriptCfgURL_Type=SnmpAdminString
_SaaApmCtrlScriptCfgURL_Object=MibTableColumn
saaApmCtrlScriptCfgURL=_SaaApmCtrlScriptCfgURL_Object((1,3,6,1,4,1,9,9,177,1,2,1,1,2),_SaaApmCtrlScriptCfgURL_Type())
saaApmCtrlScriptCfgURL.setMaxAccess(_E)
if mibBuilder.loadTexts:saaApmCtrlScriptCfgURL.setStatus(_A)
class _SaaApmCtrlOwner_Type(OwnerString):subtypeSpec=OwnerString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_SaaApmCtrlOwner_Type.__name__=_G
_SaaApmCtrlOwner_Object=MibTableColumn
saaApmCtrlOwner=_SaaApmCtrlOwner_Object((1,3,6,1,4,1,9,9,177,1,2,1,1,3),_SaaApmCtrlOwner_Type())
saaApmCtrlOwner.setMaxAccess(_E)
if mibBuilder.loadTexts:saaApmCtrlOwner.setStatus(_A)
class _SaaApmCtrlInitDataTrans_Type(TruthValue):defaultValue=2
_SaaApmCtrlInitDataTrans_Type.__name__=_F
_SaaApmCtrlInitDataTrans_Object=MibTableColumn
saaApmCtrlInitDataTrans=_SaaApmCtrlInitDataTrans_Object((1,3,6,1,4,1,9,9,177,1,2,1,1,4),_SaaApmCtrlInitDataTrans_Type())
saaApmCtrlInitDataTrans.setMaxAccess(_E)
if mibBuilder.loadTexts:saaApmCtrlInitDataTrans.setStatus(_A)
_SaaApmCtrlDataTransTime_Type=TimeStamp
_SaaApmCtrlDataTransTime_Object=MibTableColumn
saaApmCtrlDataTransTime=_SaaApmCtrlDataTransTime_Object((1,3,6,1,4,1,9,9,177,1,2,1,1,5),_SaaApmCtrlDataTransTime_Type())
saaApmCtrlDataTransTime.setMaxAccess(_C)
if mibBuilder.loadTexts:saaApmCtrlDataTransTime.setStatus(_A)
_SaaApmCtrlDataTransStatus_Type=SaaApmDataTransErrorCode
_SaaApmCtrlDataTransStatus_Object=MibTableColumn
saaApmCtrlDataTransStatus=_SaaApmCtrlDataTransStatus_Object((1,3,6,1,4,1,9,9,177,1,2,1,1,6),_SaaApmCtrlDataTransStatus_Type())
saaApmCtrlDataTransStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:saaApmCtrlDataTransStatus.setStatus(_A)
_SaaApmCtrlStatus_Type=RowStatus
_SaaApmCtrlStatus_Object=MibTableColumn
saaApmCtrlStatus=_SaaApmCtrlStatus_Object((1,3,6,1,4,1,9,9,177,1,2,1,1,7),_SaaApmCtrlStatus_Type())
saaApmCtrlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:saaApmCtrlStatus.setStatus(_A)
class _SaaApmCtrlNvgen_Type(TruthValue):defaultValue=2
_SaaApmCtrlNvgen_Type.__name__=_F
_SaaApmCtrlNvgen_Object=MibTableColumn
saaApmCtrlNvgen=_SaaApmCtrlNvgen_Object((1,3,6,1,4,1,9,9,177,1,2,1,1,8),_SaaApmCtrlNvgen_Type())
saaApmCtrlNvgen.setMaxAccess(_E)
if mibBuilder.loadTexts:saaApmCtrlNvgen.setStatus(_A)
_SaaApmOper_ObjectIdentity=ObjectIdentity
saaApmOper=_SaaApmOper_ObjectIdentity((1,3,6,1,4,1,9,9,177,1,3))
_SaaApmOperTable_Object=MibTable
saaApmOperTable=_SaaApmOperTable_Object((1,3,6,1,4,1,9,9,177,1,3,1))
if mibBuilder.loadTexts:saaApmOperTable.setStatus(_A)
_SaaApmOperEntry_Object=MibTableRow
saaApmOperEntry=_SaaApmOperEntry_Object((1,3,6,1,4,1,9,9,177,1,3,1,1))
if mibBuilder.loadTexts:saaApmOperEntry.setStatus(_A)
_SaaApmOperLastStartTime_Type=TimeStamp
_SaaApmOperLastStartTime_Object=MibTableColumn
saaApmOperLastStartTime=_SaaApmOperLastStartTime_Object((1,3,6,1,4,1,9,9,177,1,3,1,1,1),_SaaApmOperLastStartTime_Type())
saaApmOperLastStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:saaApmOperLastStartTime.setStatus(_A)
_SaaApmOperLastEndTime_Type=TimeStamp
_SaaApmOperLastEndTime_Object=MibTableColumn
saaApmOperLastEndTime=_SaaApmOperLastEndTime_Object((1,3,6,1,4,1,9,9,177,1,3,1,1,2),_SaaApmOperLastEndTime_Type())
saaApmOperLastEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:saaApmOperLastEndTime.setStatus(_A)
_SaaApmOperLastStatus_Type=SaaApmOperErrorCode
_SaaApmOperLastStatus_Object=MibTableColumn
saaApmOperLastStatus=_SaaApmOperLastStatus_Object((1,3,6,1,4,1,9,9,177,1,3,1,1,3),_SaaApmOperLastStatus_Type())
saaApmOperLastStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:saaApmOperLastStatus.setStatus(_A)
_CiscoSaaApmMIBNotifPrefix_ObjectIdentity=ObjectIdentity
ciscoSaaApmMIBNotifPrefix=_CiscoSaaApmMIBNotifPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,177,2))
_CiscoSaaApmMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSaaApmMIBNotifs=_CiscoSaaApmMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,177,2,0))
_CiscoSaaApmMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSaaApmMIBConformance=_CiscoSaaApmMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,177,3))
_CiscoSaaApmMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSaaApmMIBCompliances=_CiscoSaaApmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,177,3,1))
_CiscoSaaApmMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSaaApmMIBGroups=_CiscoSaaApmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,177,3,2))
saaApmCtrlEntry.registerAugmentions((_B,_K))
saaApmOperEntry.setIndexNames(*saaApmCtrlEntry.getIndexNames())
ciscoSaaApmApplGroup=ObjectGroup((1,3,6,1,4,1,9,9,177,3,2,1))
ciscoSaaApmApplGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ciscoSaaApmApplGroup.setStatus(_A)
ciscoSaaApmCtrlGroup=ObjectGroup((1,3,6,1,4,1,9,9,177,3,2,2))
ciscoSaaApmCtrlGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ciscoSaaApmCtrlGroup.setStatus(_A)
ciscoSaaApmOperGroup=ObjectGroup((1,3,6,1,4,1,9,9,177,3,2,3))
ciscoSaaApmOperGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:ciscoSaaApmOperGroup.setStatus(_A)
ciscoSaaApmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,177,3,1,1))
ciscoSaaApmMIBCompliance.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ciscoSaaApmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SaaApmOperErrorCode':SaaApmOperErrorCode,'SaaApmDataTransErrorCode':SaaApmDataTransErrorCode,'ciscoSaaApmMIB':ciscoSaaApmMIB,'ciscoSaaApmMIBObjects':ciscoSaaApmMIBObjects,'saaApmAppl':saaApmAppl,_L:saaApmApplMajorVersion,_M:saaApmApplMinorVersion,_N:saaApmApplMaxOper,_O:saaApmApplFreeMemLowWaterMark,_P:saaApmApplOperCapacity,'saaApmCtrl':saaApmCtrl,'saaApmCtrlTable':saaApmCtrlTable,'saaApmCtrlEntry':saaApmCtrlEntry,_J:saaApmCtrlIndex,_Q:saaApmCtrlScriptCfgURL,_R:saaApmCtrlOwner,_S:saaApmCtrlInitDataTrans,_T:saaApmCtrlDataTransTime,_U:saaApmCtrlDataTransStatus,_V:saaApmCtrlStatus,_W:saaApmCtrlNvgen,'saaApmOper':saaApmOper,'saaApmOperTable':saaApmOperTable,_K:saaApmOperEntry,_X:saaApmOperLastStartTime,_Y:saaApmOperLastEndTime,_Z:saaApmOperLastStatus,'ciscoSaaApmMIBNotifPrefix':ciscoSaaApmMIBNotifPrefix,'ciscoSaaApmMIBNotifs':ciscoSaaApmMIBNotifs,'ciscoSaaApmMIBConformance':ciscoSaaApmMIBConformance,'ciscoSaaApmMIBCompliances':ciscoSaaApmMIBCompliances,'ciscoSaaApmMIBCompliance':ciscoSaaApmMIBCompliance,'ciscoSaaApmMIBGroups':ciscoSaaApmMIBGroups,_a:ciscoSaaApmApplGroup,_b:ciscoSaaApmCtrlGroup,_c:ciscoSaaApmOperGroup})