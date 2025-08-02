_Y='fsTMMIBGroup'
_X='fsQoSIfChipTime'
_W='fsQoSIfChipRate'
_V='fsQoSIfChipPeak'
_U='fsQoSIfChipCur'
_T='fsQoSIfChipMax'
_S='fsQoSLastClearTime'
_R='fsQoSDeQueDrop'
_Q='fsQoSEnQueDropByOther'
_P='fsQoSEnQueDropByBufDesc'
_O='fsQoSEnQueDropByBuf'
_N='fsQoSEnQueDrop'
_M='fsQoSTotalDeQue'
_L='fsQoSTotalEnQue'
_K='fsQosDramCurUsed'
_J='fsQosDramTotal'
_I='fsQoSIfChipQueIndex'
_H='fsQoSIfChipIndex'
_G='fsQoSIfIndex'
_F='fsQoSDropIndex'
_E='fsQoSDramIndex'
_D='Integer32'
_C='read-only'
_B='FS-TM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsTMMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,91))
if mibBuilder.loadTexts:fsTMMIB.setRevisions(('2010-12-13 00:00',))
_FsTMMIBObjects_ObjectIdentity=ObjectIdentity
fsTMMIBObjects=_FsTMMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,91,1))
_FsTMQosDramMIBObjects_ObjectIdentity=ObjectIdentity
fsTMQosDramMIBObjects=_FsTMQosDramMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,91,1,1))
_FsQosDramTable_Object=MibTable
fsQosDramTable=_FsQosDramTable_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,1,1))
if mibBuilder.loadTexts:fsQosDramTable.setStatus(_A)
_FsQosDramEntry_Object=MibTableRow
fsQosDramEntry=_FsQosDramEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,1,1,1))
fsQosDramEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsQosDramEntry.setStatus(_A)
_FsQoSDramIndex_Type=Integer32
_FsQoSDramIndex_Object=MibTableColumn
fsQoSDramIndex=_FsQoSDramIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,1,1,1,1),_FsQoSDramIndex_Type())
fsQoSDramIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSDramIndex.setStatus(_A)
_FsQosDramTotal_Type=Integer32
_FsQosDramTotal_Object=MibTableColumn
fsQosDramTotal=_FsQosDramTotal_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,1,1,1,2),_FsQosDramTotal_Type())
fsQosDramTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQosDramTotal.setStatus(_A)
_FsQosDramCurUsed_Type=Integer32
_FsQosDramCurUsed_Object=MibTableColumn
fsQosDramCurUsed=_FsQosDramCurUsed_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,1,1,1,3),_FsQosDramCurUsed_Type())
fsQosDramCurUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQosDramCurUsed.setStatus(_A)
_FsTMQosDropMIBObjects_ObjectIdentity=ObjectIdentity
fsTMQosDropMIBObjects=_FsTMQosDropMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,91,1,2))
_FsQosDropTable_Object=MibTable
fsQosDropTable=_FsQosDropTable_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,2,1))
if mibBuilder.loadTexts:fsQosDropTable.setStatus(_A)
_FsQosDropEntry_Object=MibTableRow
fsQosDropEntry=_FsQosDropEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,2,1,1))
fsQosDropEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fsQosDropEntry.setStatus(_A)
_FsQoSDropIndex_Type=Integer32
_FsQoSDropIndex_Object=MibTableColumn
fsQoSDropIndex=_FsQoSDropIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,2,1,1,1),_FsQoSDropIndex_Type())
fsQoSDropIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSDropIndex.setStatus(_A)
_FsQoSTotalEnQue_Type=Integer32
_FsQoSTotalEnQue_Object=MibTableColumn
fsQoSTotalEnQue=_FsQoSTotalEnQue_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,2,1,1,2),_FsQoSTotalEnQue_Type())
fsQoSTotalEnQue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSTotalEnQue.setStatus(_A)
_FsQoSTotalDeQue_Type=Integer32
_FsQoSTotalDeQue_Object=MibTableColumn
fsQoSTotalDeQue=_FsQoSTotalDeQue_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,2,1,1,3),_FsQoSTotalDeQue_Type())
fsQoSTotalDeQue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSTotalDeQue.setStatus(_A)
_FsQoSEnQueDrop_Type=Integer32
_FsQoSEnQueDrop_Object=MibTableColumn
fsQoSEnQueDrop=_FsQoSEnQueDrop_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,2,1,1,4),_FsQoSEnQueDrop_Type())
fsQoSEnQueDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSEnQueDrop.setStatus(_A)
_FsQoSEnQueDropByBuf_Type=Integer32
_FsQoSEnQueDropByBuf_Object=MibTableColumn
fsQoSEnQueDropByBuf=_FsQoSEnQueDropByBuf_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,2,1,1,5),_FsQoSEnQueDropByBuf_Type())
fsQoSEnQueDropByBuf.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSEnQueDropByBuf.setStatus(_A)
_FsQoSEnQueDropByBufDesc_Type=Integer32
_FsQoSEnQueDropByBufDesc_Object=MibTableColumn
fsQoSEnQueDropByBufDesc=_FsQoSEnQueDropByBufDesc_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,2,1,1,6),_FsQoSEnQueDropByBufDesc_Type())
fsQoSEnQueDropByBufDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSEnQueDropByBufDesc.setStatus(_A)
_FsQoSEnQueDropByOther_Type=Integer32
_FsQoSEnQueDropByOther_Object=MibTableColumn
fsQoSEnQueDropByOther=_FsQoSEnQueDropByOther_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,2,1,1,7),_FsQoSEnQueDropByOther_Type())
fsQoSEnQueDropByOther.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSEnQueDropByOther.setStatus(_A)
_FsQoSDeQueDrop_Type=Integer32
_FsQoSDeQueDrop_Object=MibTableColumn
fsQoSDeQueDrop=_FsQoSDeQueDrop_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,2,1,1,8),_FsQoSDeQueDrop_Type())
fsQoSDeQueDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSDeQueDrop.setStatus(_A)
_FsQoSLastClearTime_Type=TimeTicks
_FsQoSLastClearTime_Object=MibTableColumn
fsQoSLastClearTime=_FsQoSLastClearTime_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,2,1,1,9),_FsQoSLastClearTime_Type())
fsQoSLastClearTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSLastClearTime.setStatus(_A)
_FsTMQosQueMIBObjects_ObjectIdentity=ObjectIdentity
fsTMQosQueMIBObjects=_FsTMQosQueMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,91,1,3))
_FsQosQueTable_Object=MibTable
fsQosQueTable=_FsQosQueTable_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,3,1))
if mibBuilder.loadTexts:fsQosQueTable.setStatus(_A)
_FsQosQueEntry_Object=MibTableRow
fsQosQueEntry=_FsQosQueEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,3,1,1))
fsQosQueEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:fsQosQueEntry.setStatus(_A)
_FsQoSIfIndex_Type=IfIndex
_FsQoSIfIndex_Object=MibTableColumn
fsQoSIfIndex=_FsQoSIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,3,1,1,1),_FsQoSIfIndex_Type())
fsQoSIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSIfIndex.setStatus(_A)
class _FsQoSIfChipIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('chip-0',0),('chip-1',1)))
_FsQoSIfChipIndex_Type.__name__=_D
_FsQoSIfChipIndex_Object=MibTableColumn
fsQoSIfChipIndex=_FsQoSIfChipIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,3,1,1,2),_FsQoSIfChipIndex_Type())
fsQoSIfChipIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSIfChipIndex.setStatus(_A)
class _FsQoSIfChipQueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('queue-1',1),('queue-2',2),('queue-3',3),('queue-4',4),('queue-5',5),('queue-6',6),('queue-7',7),('queue-8',8)))
_FsQoSIfChipQueIndex_Type.__name__=_D
_FsQoSIfChipQueIndex_Object=MibTableColumn
fsQoSIfChipQueIndex=_FsQoSIfChipQueIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,3,1,1,3),_FsQoSIfChipQueIndex_Type())
fsQoSIfChipQueIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSIfChipQueIndex.setStatus(_A)
_FsQoSIfChipMax_Type=Integer32
_FsQoSIfChipMax_Object=MibTableColumn
fsQoSIfChipMax=_FsQoSIfChipMax_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,3,1,1,4),_FsQoSIfChipMax_Type())
fsQoSIfChipMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSIfChipMax.setStatus(_A)
_FsQoSIfChipCur_Type=Integer32
_FsQoSIfChipCur_Object=MibTableColumn
fsQoSIfChipCur=_FsQoSIfChipCur_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,3,1,1,5),_FsQoSIfChipCur_Type())
fsQoSIfChipCur.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSIfChipCur.setStatus(_A)
_FsQoSIfChipPeak_Type=Integer32
_FsQoSIfChipPeak_Object=MibTableColumn
fsQoSIfChipPeak=_FsQoSIfChipPeak_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,3,1,1,6),_FsQoSIfChipPeak_Type())
fsQoSIfChipPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSIfChipPeak.setStatus(_A)
_FsQoSIfChipRate_Type=Integer32
_FsQoSIfChipRate_Object=MibTableColumn
fsQoSIfChipRate=_FsQoSIfChipRate_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,3,1,1,7),_FsQoSIfChipRate_Type())
fsQoSIfChipRate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSIfChipRate.setStatus(_A)
_FsQoSIfChipTime_Type=TimeTicks
_FsQoSIfChipTime_Object=MibTableColumn
fsQoSIfChipTime=_FsQoSIfChipTime_Object((1,3,6,1,4,1,52642,1,1,10,2,91,1,3,1,1,8),_FsQoSIfChipTime_Type())
fsQoSIfChipTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsQoSIfChipTime.setStatus(_A)
_FsTMMIBConformance_ObjectIdentity=ObjectIdentity
fsTMMIBConformance=_FsTMMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,91,2))
_FsTMMIBCompliances_ObjectIdentity=ObjectIdentity
fsTMMIBCompliances=_FsTMMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,91,2,1))
_FsTMMIBGroups_ObjectIdentity=ObjectIdentity
fsTMMIBGroups=_FsTMMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,91,2,2))
fsTMMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,91,2,2,1))
fsTMMIBGroup.setObjects(*((_B,_E),(_B,_J),(_B,_K),(_B,_F),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_G),(_B,_H),(_B,_I),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:fsTMMIBGroup.setStatus(_A)
fsTMMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,91,2,1,1))
fsTMMIBCompliance.setObjects((_B,_Y))
if mibBuilder.loadTexts:fsTMMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsTMMIB':fsTMMIB,'fsTMMIBObjects':fsTMMIBObjects,'fsTMQosDramMIBObjects':fsTMQosDramMIBObjects,'fsQosDramTable':fsQosDramTable,'fsQosDramEntry':fsQosDramEntry,_E:fsQoSDramIndex,_J:fsQosDramTotal,_K:fsQosDramCurUsed,'fsTMQosDropMIBObjects':fsTMQosDropMIBObjects,'fsQosDropTable':fsQosDropTable,'fsQosDropEntry':fsQosDropEntry,_F:fsQoSDropIndex,_L:fsQoSTotalEnQue,_M:fsQoSTotalDeQue,_N:fsQoSEnQueDrop,_O:fsQoSEnQueDropByBuf,_P:fsQoSEnQueDropByBufDesc,_Q:fsQoSEnQueDropByOther,_R:fsQoSDeQueDrop,_S:fsQoSLastClearTime,'fsTMQosQueMIBObjects':fsTMQosQueMIBObjects,'fsQosQueTable':fsQosQueTable,'fsQosQueEntry':fsQosQueEntry,_G:fsQoSIfIndex,_H:fsQoSIfChipIndex,_I:fsQoSIfChipQueIndex,_T:fsQoSIfChipMax,_U:fsQoSIfChipCur,_V:fsQoSIfChipPeak,_W:fsQoSIfChipRate,_X:fsQoSIfChipTime,'fsTMMIBConformance':fsTMMIBConformance,'fsTMMIBCompliances':fsTMMIBCompliances,'fsTMMIBCompliance':fsTMMIBCompliance,'fsTMMIBGroups':fsTMMIBGroups,_Y:fsTMMIBGroup})