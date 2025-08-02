_O='vancServiceStatusServiceID'
_N='sdiAudioSlotPosition'
_M='sdiAudioSlotGroup'
_L='multiOP47'
_K='sdpOP47'
_J='smpte2031'
_I='eia708'
_H='vancCfgSvcID'
_G='enabled'
_F='disabled'
_E='CISCO-DMN-DSG-SDI-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoDSGSDI=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,32))
if mibBuilder.loadTexts:ciscoDSGSDI.setRevisions(('2012-03-20 11:00','2010-08-24 07:00'))
_SdiInfo_ObjectIdentity=ObjectIdentity
sdiInfo=_SdiInfo_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,32,1))
class _SdiVii_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SdiVii_Type.__name__=_C
_SdiVii_Object=MibScalar
sdiVii=_SdiVii_Object((1,3,6,1,4,1,1429,2,2,5,32,1,1),_SdiVii_Type())
sdiVii.setMaxAccess(_D)
if mibBuilder.loadTexts:sdiVii.setStatus(_A)
class _VancGlobalStatusInterlaced_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_VancGlobalStatusInterlaced_Type.__name__=_C
_VancGlobalStatusInterlaced_Object=MibScalar
vancGlobalStatusInterlaced=_VancGlobalStatusInterlaced_Object((1,3,6,1,4,1,1429,2,2,5,32,1,2),_VancGlobalStatusInterlaced_Type())
vancGlobalStatusInterlaced.setMaxAccess(_B)
if mibBuilder.loadTexts:vancGlobalStatusInterlaced.setStatus(_A)
_VancGlobalStatusFrames_Type=Counter32
_VancGlobalStatusFrames_Object=MibScalar
vancGlobalStatusFrames=_VancGlobalStatusFrames_Object((1,3,6,1,4,1,1429,2,2,5,32,1,3),_VancGlobalStatusFrames_Type())
vancGlobalStatusFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:vancGlobalStatusFrames.setStatus(_A)
_VancGlobalStatusLines_Type=Counter32
_VancGlobalStatusLines_Object=MibScalar
vancGlobalStatusLines=_VancGlobalStatusLines_Object((1,3,6,1,4,1,1429,2,2,5,32,1,4),_VancGlobalStatusLines_Type())
vancGlobalStatusLines.setMaxAccess(_B)
if mibBuilder.loadTexts:vancGlobalStatusLines.setStatus(_A)
_VancGlobalStatusWords_Type=Counter32
_VancGlobalStatusWords_Object=MibScalar
vancGlobalStatusWords=_VancGlobalStatusWords_Object((1,3,6,1,4,1,1429,2,2,5,32,1,5),_VancGlobalStatusWords_Type())
vancGlobalStatusWords.setMaxAccess(_B)
if mibBuilder.loadTexts:vancGlobalStatusWords.setStatus(_A)
_VancGlobalStatusFirst_Type=Counter32
_VancGlobalStatusFirst_Object=MibScalar
vancGlobalStatusFirst=_VancGlobalStatusFirst_Object((1,3,6,1,4,1,1429,2,2,5,32,1,6),_VancGlobalStatusFirst_Type())
vancGlobalStatusFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:vancGlobalStatusFirst.setStatus(_A)
_VancGlobalStatusLast_Type=Counter32
_VancGlobalStatusLast_Object=MibScalar
vancGlobalStatusLast=_VancGlobalStatusLast_Object((1,3,6,1,4,1,1429,2,2,5,32,1,7),_VancGlobalStatusLast_Type())
vancGlobalStatusLast.setMaxAccess(_B)
if mibBuilder.loadTexts:vancGlobalStatusLast.setStatus(_A)
_VancGlobalStatusSwitch_Type=Counter32
_VancGlobalStatusSwitch_Object=MibScalar
vancGlobalStatusSwitch=_VancGlobalStatusSwitch_Object((1,3,6,1,4,1,1429,2,2,5,32,1,8),_VancGlobalStatusSwitch_Type())
vancGlobalStatusSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:vancGlobalStatusSwitch.setStatus(_A)
class _VancGlobalStatusMultiLine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_VancGlobalStatusMultiLine_Type.__name__=_C
_VancGlobalStatusMultiLine_Object=MibScalar
vancGlobalStatusMultiLine=_VancGlobalStatusMultiLine_Object((1,3,6,1,4,1,1429,2,2,5,32,1,9),_VancGlobalStatusMultiLine_Type())
vancGlobalStatusMultiLine.setMaxAccess(_B)
if mibBuilder.loadTexts:vancGlobalStatusMultiLine.setStatus(_A)
_SdiTable_ObjectIdentity=ObjectIdentity
sdiTable=_SdiTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,32,2))
_VancCfgTable_Object=MibTable
vancCfgTable=_VancCfgTable_Object((1,3,6,1,4,1,1429,2,2,5,32,2,1))
if mibBuilder.loadTexts:vancCfgTable.setStatus(_A)
_VancCfgEntry_Object=MibTableRow
vancCfgEntry=_VancCfgEntry_Object((1,3,6,1,4,1,1429,2,2,5,32,2,1,1))
vancCfgEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:vancCfgEntry.setStatus(_A)
class _VancCfgSvcID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),('afd',2),('dpi',3),(_J,4),(_K,5),(_L,6)))
_VancCfgSvcID_Type.__name__=_C
_VancCfgSvcID_Object=MibTableColumn
vancCfgSvcID=_VancCfgSvcID_Object((1,3,6,1,4,1,1429,2,2,5,32,2,1,1,1),_VancCfgSvcID_Type())
vancCfgSvcID.setMaxAccess(_B)
if mibBuilder.loadTexts:vancCfgSvcID.setStatus(_A)
class _VancCfgEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_VancCfgEnable_Type.__name__=_C
_VancCfgEnable_Object=MibTableColumn
vancCfgEnable=_VancCfgEnable_Object((1,3,6,1,4,1,1429,2,2,5,32,2,1,1,2),_VancCfgEnable_Type())
vancCfgEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:vancCfgEnable.setStatus(_A)
class _VancCfgOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18))
_VancCfgOffset_Type.__name__=_C
_VancCfgOffset_Object=MibTableColumn
vancCfgOffset=_VancCfgOffset_Object((1,3,6,1,4,1,1429,2,2,5,32,2,1,1,3),_VancCfgOffset_Type())
vancCfgOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:vancCfgOffset.setStatus(_A)
_SdiAudioSlotTable_Object=MibTable
sdiAudioSlotTable=_SdiAudioSlotTable_Object((1,3,6,1,4,1,1429,2,2,5,32,2,2))
if mibBuilder.loadTexts:sdiAudioSlotTable.setStatus(_A)
_SdiAudioSlotEntry_Object=MibTableRow
sdiAudioSlotEntry=_SdiAudioSlotEntry_Object((1,3,6,1,4,1,1429,2,2,5,32,2,2,1))
sdiAudioSlotEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:sdiAudioSlotEntry.setStatus(_A)
class _SdiAudioSlotGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_SdiAudioSlotGroup_Type.__name__=_C
_SdiAudioSlotGroup_Object=MibTableColumn
sdiAudioSlotGroup=_SdiAudioSlotGroup_Object((1,3,6,1,4,1,1429,2,2,5,32,2,2,1,1),_SdiAudioSlotGroup_Type())
sdiAudioSlotGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:sdiAudioSlotGroup.setStatus(_A)
class _SdiAudioSlotPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_SdiAudioSlotPosition_Type.__name__=_C
_SdiAudioSlotPosition_Object=MibTableColumn
sdiAudioSlotPosition=_SdiAudioSlotPosition_Object((1,3,6,1,4,1,1429,2,2,5,32,2,2,1,2),_SdiAudioSlotPosition_Type())
sdiAudioSlotPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:sdiAudioSlotPosition.setStatus(_A)
class _SdiAudioSlotAud_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SdiAudioSlotAud_Type.__name__=_C
_SdiAudioSlotAud_Object=MibTableColumn
sdiAudioSlotAud=_SdiAudioSlotAud_Object((1,3,6,1,4,1,1429,2,2,5,32,2,2,1,3),_SdiAudioSlotAud_Type())
sdiAudioSlotAud.setMaxAccess(_D)
if mibBuilder.loadTexts:sdiAudioSlotAud.setStatus(_A)
class _SdiAudioSlotChan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SdiAudioSlotChan_Type.__name__=_C
_SdiAudioSlotChan_Object=MibTableColumn
sdiAudioSlotChan=_SdiAudioSlotChan_Object((1,3,6,1,4,1,1429,2,2,5,32,2,2,1,4),_SdiAudioSlotChan_Type())
sdiAudioSlotChan.setMaxAccess(_D)
if mibBuilder.loadTexts:sdiAudioSlotChan.setStatus(_A)
_VancServiceStatusTable_Object=MibTable
vancServiceStatusTable=_VancServiceStatusTable_Object((1,3,6,1,4,1,1429,2,2,5,32,2,3))
if mibBuilder.loadTexts:vancServiceStatusTable.setStatus(_A)
_VancServiceStatusEntry_Object=MibTableRow
vancServiceStatusEntry=_VancServiceStatusEntry_Object((1,3,6,1,4,1,1429,2,2,5,32,2,3,1))
vancServiceStatusEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:vancServiceStatusEntry.setStatus(_A)
class _VancServiceStatusServiceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),('afd',2),('dpi',3),(_J,4),(_K,5),(_L,6)))
_VancServiceStatusServiceID_Type.__name__=_C
_VancServiceStatusServiceID_Object=MibTableColumn
vancServiceStatusServiceID=_VancServiceStatusServiceID_Object((1,3,6,1,4,1,1429,2,2,5,32,2,3,1,1),_VancServiceStatusServiceID_Type())
vancServiceStatusServiceID.setMaxAccess(_B)
if mibBuilder.loadTexts:vancServiceStatusServiceID.setStatus(_A)
class _VancServiceStatusActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_VancServiceStatusActive_Type.__name__=_C
_VancServiceStatusActive_Object=MibTableColumn
vancServiceStatusActive=_VancServiceStatusActive_Object((1,3,6,1,4,1,1429,2,2,5,32,2,3,1,2),_VancServiceStatusActive_Type())
vancServiceStatusActive.setMaxAccess(_B)
if mibBuilder.loadTexts:vancServiceStatusActive.setStatus(_A)
_VancServiceStatusADJLine_Type=Counter32
_VancServiceStatusADJLine_Object=MibTableColumn
vancServiceStatusADJLine=_VancServiceStatusADJLine_Object((1,3,6,1,4,1,1429,2,2,5,32,2,3,1,3),_VancServiceStatusADJLine_Type())
vancServiceStatusADJLine.setMaxAccess(_B)
if mibBuilder.loadTexts:vancServiceStatusADJLine.setStatus(_A)
_VancServiceStatusACTLineF1_Type=Counter32
_VancServiceStatusACTLineF1_Object=MibTableColumn
vancServiceStatusACTLineF1=_VancServiceStatusACTLineF1_Object((1,3,6,1,4,1,1429,2,2,5,32,2,3,1,4),_VancServiceStatusACTLineF1_Type())
vancServiceStatusACTLineF1.setMaxAccess(_B)
if mibBuilder.loadTexts:vancServiceStatusACTLineF1.setStatus(_A)
_VancServiceStatusACTLineF2_Type=Counter32
_VancServiceStatusACTLineF2_Object=MibTableColumn
vancServiceStatusACTLineF2=_VancServiceStatusACTLineF2_Object((1,3,6,1,4,1,1429,2,2,5,32,2,3,1,5),_VancServiceStatusACTLineF2_Type())
vancServiceStatusACTLineF2.setMaxAccess(_B)
if mibBuilder.loadTexts:vancServiceStatusACTLineF2.setStatus(_A)
_VancServiceStatusLinesMAX_Type=Counter32
_VancServiceStatusLinesMAX_Object=MibTableColumn
vancServiceStatusLinesMAX=_VancServiceStatusLinesMAX_Object((1,3,6,1,4,1,1429,2,2,5,32,2,3,1,6),_VancServiceStatusLinesMAX_Type())
vancServiceStatusLinesMAX.setMaxAccess(_B)
if mibBuilder.loadTexts:vancServiceStatusLinesMAX.setStatus(_A)
_VancServiceStatusDataAvg_Type=Counter32
_VancServiceStatusDataAvg_Object=MibTableColumn
vancServiceStatusDataAvg=_VancServiceStatusDataAvg_Object((1,3,6,1,4,1,1429,2,2,5,32,2,3,1,7),_VancServiceStatusDataAvg_Type())
vancServiceStatusDataAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:vancServiceStatusDataAvg.setStatus(_A)
_VancServiceStatusPacketsOKAvg_Type=Counter32
_VancServiceStatusPacketsOKAvg_Object=MibTableColumn
vancServiceStatusPacketsOKAvg=_VancServiceStatusPacketsOKAvg_Object((1,3,6,1,4,1,1429,2,2,5,32,2,3,1,8),_VancServiceStatusPacketsOKAvg_Type())
vancServiceStatusPacketsOKAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:vancServiceStatusPacketsOKAvg.setStatus(_A)
_VancServiceStatusPacketsDroppedAvg_Type=Counter32
_VancServiceStatusPacketsDroppedAvg_Object=MibTableColumn
vancServiceStatusPacketsDroppedAvg=_VancServiceStatusPacketsDroppedAvg_Object((1,3,6,1,4,1,1429,2,2,5,32,2,3,1,9),_VancServiceStatusPacketsDroppedAvg_Type())
vancServiceStatusPacketsDroppedAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:vancServiceStatusPacketsDroppedAvg.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ciscoDSGSDI':ciscoDSGSDI,'sdiInfo':sdiInfo,'sdiVii':sdiVii,'vancGlobalStatusInterlaced':vancGlobalStatusInterlaced,'vancGlobalStatusFrames':vancGlobalStatusFrames,'vancGlobalStatusLines':vancGlobalStatusLines,'vancGlobalStatusWords':vancGlobalStatusWords,'vancGlobalStatusFirst':vancGlobalStatusFirst,'vancGlobalStatusLast':vancGlobalStatusLast,'vancGlobalStatusSwitch':vancGlobalStatusSwitch,'vancGlobalStatusMultiLine':vancGlobalStatusMultiLine,'sdiTable':sdiTable,'vancCfgTable':vancCfgTable,'vancCfgEntry':vancCfgEntry,_H:vancCfgSvcID,'vancCfgEnable':vancCfgEnable,'vancCfgOffset':vancCfgOffset,'sdiAudioSlotTable':sdiAudioSlotTable,'sdiAudioSlotEntry':sdiAudioSlotEntry,_M:sdiAudioSlotGroup,_N:sdiAudioSlotPosition,'sdiAudioSlotAud':sdiAudioSlotAud,'sdiAudioSlotChan':sdiAudioSlotChan,'vancServiceStatusTable':vancServiceStatusTable,'vancServiceStatusEntry':vancServiceStatusEntry,_O:vancServiceStatusServiceID,'vancServiceStatusActive':vancServiceStatusActive,'vancServiceStatusADJLine':vancServiceStatusADJLine,'vancServiceStatusACTLineF1':vancServiceStatusACTLineF1,'vancServiceStatusACTLineF2':vancServiceStatusACTLineF2,'vancServiceStatusLinesMAX':vancServiceStatusLinesMAX,'vancServiceStatusDataAvg':vancServiceStatusDataAvg,'vancServiceStatusPacketsOKAvg':vancServiceStatusPacketsOKAvg,'vancServiceStatusPacketsDroppedAvg':vancServiceStatusPacketsDroppedAvg})