_Y='qtechTMMIBGroup'
_X='qtechQoSIfChipTime'
_W='qtechQoSIfChipRate'
_V='qtechQoSIfChipPeak'
_U='qtechQoSIfChipCur'
_T='qtechQoSIfChipMax'
_S='qtechQoSLastClearTime'
_R='qtechQoSDeQueDrop'
_Q='qtechQoSEnQueDropByOther'
_P='qtechQoSEnQueDropByBufDesc'
_O='qtechQoSEnQueDropByBuf'
_N='qtechQoSEnQueDrop'
_M='qtechQoSTotalDeQue'
_L='qtechQoSTotalEnQue'
_K='qtechQosDramCurUsed'
_J='qtechQosDramTotal'
_I='qtechQoSIfChipQueIndex'
_H='qtechQoSIfChipIndex'
_G='qtechQoSIfIndex'
_F='qtechQoSDropIndex'
_E='qtechQoSDramIndex'
_D='Integer32'
_C='read-only'
_B='QTECH-TM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechTMMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,91))
if mibBuilder.loadTexts:qtechTMMIB.setRevisions(('2010-12-13 00:00',))
_QtechTMMIBObjects_ObjectIdentity=ObjectIdentity
qtechTMMIBObjects=_QtechTMMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,91,1))
_QtechTMQosDramMIBObjects_ObjectIdentity=ObjectIdentity
qtechTMQosDramMIBObjects=_QtechTMQosDramMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,91,1,1))
_QtechQosDramTable_Object=MibTable
qtechQosDramTable=_QtechQosDramTable_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,1,1))
if mibBuilder.loadTexts:qtechQosDramTable.setStatus(_A)
_QtechQosDramEntry_Object=MibTableRow
qtechQosDramEntry=_QtechQosDramEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,1,1,1))
qtechQosDramEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:qtechQosDramEntry.setStatus(_A)
_QtechQoSDramIndex_Type=Integer32
_QtechQoSDramIndex_Object=MibTableColumn
qtechQoSDramIndex=_QtechQoSDramIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,1,1,1,1),_QtechQoSDramIndex_Type())
qtechQoSDramIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSDramIndex.setStatus(_A)
_QtechQosDramTotal_Type=Integer32
_QtechQosDramTotal_Object=MibTableColumn
qtechQosDramTotal=_QtechQosDramTotal_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,1,1,1,2),_QtechQosDramTotal_Type())
qtechQosDramTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQosDramTotal.setStatus(_A)
_QtechQosDramCurUsed_Type=Integer32
_QtechQosDramCurUsed_Object=MibTableColumn
qtechQosDramCurUsed=_QtechQosDramCurUsed_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,1,1,1,3),_QtechQosDramCurUsed_Type())
qtechQosDramCurUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQosDramCurUsed.setStatus(_A)
_QtechTMQosDropMIBObjects_ObjectIdentity=ObjectIdentity
qtechTMQosDropMIBObjects=_QtechTMQosDropMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,91,1,2))
_QtechQosDropTable_Object=MibTable
qtechQosDropTable=_QtechQosDropTable_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,2,1))
if mibBuilder.loadTexts:qtechQosDropTable.setStatus(_A)
_QtechQosDropEntry_Object=MibTableRow
qtechQosDropEntry=_QtechQosDropEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,2,1,1))
qtechQosDropEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:qtechQosDropEntry.setStatus(_A)
_QtechQoSDropIndex_Type=Integer32
_QtechQoSDropIndex_Object=MibTableColumn
qtechQoSDropIndex=_QtechQoSDropIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,2,1,1,1),_QtechQoSDropIndex_Type())
qtechQoSDropIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSDropIndex.setStatus(_A)
_QtechQoSTotalEnQue_Type=Integer32
_QtechQoSTotalEnQue_Object=MibTableColumn
qtechQoSTotalEnQue=_QtechQoSTotalEnQue_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,2,1,1,2),_QtechQoSTotalEnQue_Type())
qtechQoSTotalEnQue.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSTotalEnQue.setStatus(_A)
_QtechQoSTotalDeQue_Type=Integer32
_QtechQoSTotalDeQue_Object=MibTableColumn
qtechQoSTotalDeQue=_QtechQoSTotalDeQue_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,2,1,1,3),_QtechQoSTotalDeQue_Type())
qtechQoSTotalDeQue.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSTotalDeQue.setStatus(_A)
_QtechQoSEnQueDrop_Type=Integer32
_QtechQoSEnQueDrop_Object=MibTableColumn
qtechQoSEnQueDrop=_QtechQoSEnQueDrop_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,2,1,1,4),_QtechQoSEnQueDrop_Type())
qtechQoSEnQueDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSEnQueDrop.setStatus(_A)
_QtechQoSEnQueDropByBuf_Type=Integer32
_QtechQoSEnQueDropByBuf_Object=MibTableColumn
qtechQoSEnQueDropByBuf=_QtechQoSEnQueDropByBuf_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,2,1,1,5),_QtechQoSEnQueDropByBuf_Type())
qtechQoSEnQueDropByBuf.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSEnQueDropByBuf.setStatus(_A)
_QtechQoSEnQueDropByBufDesc_Type=Integer32
_QtechQoSEnQueDropByBufDesc_Object=MibTableColumn
qtechQoSEnQueDropByBufDesc=_QtechQoSEnQueDropByBufDesc_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,2,1,1,6),_QtechQoSEnQueDropByBufDesc_Type())
qtechQoSEnQueDropByBufDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSEnQueDropByBufDesc.setStatus(_A)
_QtechQoSEnQueDropByOther_Type=Integer32
_QtechQoSEnQueDropByOther_Object=MibTableColumn
qtechQoSEnQueDropByOther=_QtechQoSEnQueDropByOther_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,2,1,1,7),_QtechQoSEnQueDropByOther_Type())
qtechQoSEnQueDropByOther.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSEnQueDropByOther.setStatus(_A)
_QtechQoSDeQueDrop_Type=Integer32
_QtechQoSDeQueDrop_Object=MibTableColumn
qtechQoSDeQueDrop=_QtechQoSDeQueDrop_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,2,1,1,8),_QtechQoSDeQueDrop_Type())
qtechQoSDeQueDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSDeQueDrop.setStatus(_A)
_QtechQoSLastClearTime_Type=TimeTicks
_QtechQoSLastClearTime_Object=MibTableColumn
qtechQoSLastClearTime=_QtechQoSLastClearTime_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,2,1,1,9),_QtechQoSLastClearTime_Type())
qtechQoSLastClearTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSLastClearTime.setStatus(_A)
_QtechTMQosQueMIBObjects_ObjectIdentity=ObjectIdentity
qtechTMQosQueMIBObjects=_QtechTMQosQueMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,91,1,3))
_QtechQosQueTable_Object=MibTable
qtechQosQueTable=_QtechQosQueTable_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,3,1))
if mibBuilder.loadTexts:qtechQosQueTable.setStatus(_A)
_QtechQosQueEntry_Object=MibTableRow
qtechQosQueEntry=_QtechQosQueEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,3,1,1))
qtechQosQueEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:qtechQosQueEntry.setStatus(_A)
_QtechQoSIfIndex_Type=IfIndex
_QtechQoSIfIndex_Object=MibTableColumn
qtechQoSIfIndex=_QtechQoSIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,3,1,1,1),_QtechQoSIfIndex_Type())
qtechQoSIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSIfIndex.setStatus(_A)
class _QtechQoSIfChipIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('chip-0',0),('chip-1',1)))
_QtechQoSIfChipIndex_Type.__name__=_D
_QtechQoSIfChipIndex_Object=MibTableColumn
qtechQoSIfChipIndex=_QtechQoSIfChipIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,3,1,1,2),_QtechQoSIfChipIndex_Type())
qtechQoSIfChipIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSIfChipIndex.setStatus(_A)
class _QtechQoSIfChipQueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('queue-1',1),('queue-2',2),('queue-3',3),('queue-4',4),('queue-5',5),('queue-6',6),('queue-7',7),('queue-8',8)))
_QtechQoSIfChipQueIndex_Type.__name__=_D
_QtechQoSIfChipQueIndex_Object=MibTableColumn
qtechQoSIfChipQueIndex=_QtechQoSIfChipQueIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,3,1,1,3),_QtechQoSIfChipQueIndex_Type())
qtechQoSIfChipQueIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSIfChipQueIndex.setStatus(_A)
_QtechQoSIfChipMax_Type=Integer32
_QtechQoSIfChipMax_Object=MibTableColumn
qtechQoSIfChipMax=_QtechQoSIfChipMax_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,3,1,1,4),_QtechQoSIfChipMax_Type())
qtechQoSIfChipMax.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSIfChipMax.setStatus(_A)
_QtechQoSIfChipCur_Type=Integer32
_QtechQoSIfChipCur_Object=MibTableColumn
qtechQoSIfChipCur=_QtechQoSIfChipCur_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,3,1,1,5),_QtechQoSIfChipCur_Type())
qtechQoSIfChipCur.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSIfChipCur.setStatus(_A)
_QtechQoSIfChipPeak_Type=Integer32
_QtechQoSIfChipPeak_Object=MibTableColumn
qtechQoSIfChipPeak=_QtechQoSIfChipPeak_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,3,1,1,6),_QtechQoSIfChipPeak_Type())
qtechQoSIfChipPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSIfChipPeak.setStatus(_A)
_QtechQoSIfChipRate_Type=Integer32
_QtechQoSIfChipRate_Object=MibTableColumn
qtechQoSIfChipRate=_QtechQoSIfChipRate_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,3,1,1,7),_QtechQoSIfChipRate_Type())
qtechQoSIfChipRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSIfChipRate.setStatus(_A)
_QtechQoSIfChipTime_Type=TimeTicks
_QtechQoSIfChipTime_Object=MibTableColumn
qtechQoSIfChipTime=_QtechQoSIfChipTime_Object((1,3,6,1,4,1,27514,1,1,10,2,91,1,3,1,1,8),_QtechQoSIfChipTime_Type())
qtechQoSIfChipTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechQoSIfChipTime.setStatus(_A)
_QtechTMMIBConformance_ObjectIdentity=ObjectIdentity
qtechTMMIBConformance=_QtechTMMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,91,2))
_QtechTMMIBCompliances_ObjectIdentity=ObjectIdentity
qtechTMMIBCompliances=_QtechTMMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,91,2,1))
_QtechTMMIBGroups_ObjectIdentity=ObjectIdentity
qtechTMMIBGroups=_QtechTMMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,91,2,2))
qtechTMMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,91,2,2,1))
qtechTMMIBGroup.setObjects(*((_B,_E),(_B,_J),(_B,_K),(_B,_F),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_G),(_B,_H),(_B,_I),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:qtechTMMIBGroup.setStatus(_A)
qtechTMMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,91,2,1,1))
qtechTMMIBCompliance.setObjects((_B,_Y))
if mibBuilder.loadTexts:qtechTMMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechTMMIB':qtechTMMIB,'qtechTMMIBObjects':qtechTMMIBObjects,'qtechTMQosDramMIBObjects':qtechTMQosDramMIBObjects,'qtechQosDramTable':qtechQosDramTable,'qtechQosDramEntry':qtechQosDramEntry,_E:qtechQoSDramIndex,_J:qtechQosDramTotal,_K:qtechQosDramCurUsed,'qtechTMQosDropMIBObjects':qtechTMQosDropMIBObjects,'qtechQosDropTable':qtechQosDropTable,'qtechQosDropEntry':qtechQosDropEntry,_F:qtechQoSDropIndex,_L:qtechQoSTotalEnQue,_M:qtechQoSTotalDeQue,_N:qtechQoSEnQueDrop,_O:qtechQoSEnQueDropByBuf,_P:qtechQoSEnQueDropByBufDesc,_Q:qtechQoSEnQueDropByOther,_R:qtechQoSDeQueDrop,_S:qtechQoSLastClearTime,'qtechTMQosQueMIBObjects':qtechTMQosQueMIBObjects,'qtechQosQueTable':qtechQosQueTable,'qtechQosQueEntry':qtechQosQueEntry,_G:qtechQoSIfIndex,_H:qtechQoSIfChipIndex,_I:qtechQoSIfChipQueIndex,_T:qtechQoSIfChipMax,_U:qtechQoSIfChipCur,_V:qtechQoSIfChipPeak,_W:qtechQoSIfChipRate,_X:qtechQoSIfChipTime,'qtechTMMIBConformance':qtechTMMIBConformance,'qtechTMMIBCompliances':qtechTMMIBCompliances,'qtechTMMIBCompliance':qtechTMMIBCompliance,'qtechTMMIBGroups':qtechTMMIBGroups,_Y:qtechTMMIBGroup})