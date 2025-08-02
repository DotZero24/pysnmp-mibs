_G='smcDosWsTrapId'
_F='smcDosWsDrvSpcId'
_E='Integer32'
_D='SMC-AGENT-MIB'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Smc_ObjectIdentity=ObjectIdentity
smc=_Smc_ObjectIdentity((1,3,6,1,4,1,202))
_SmcDosWs_ObjectIdentity=ObjectIdentity
smcDosWs=_SmcDosWs_ObjectIdentity((1,3,6,1,4,1,202,2))
_SmcDosWsPcTyp_Type=DisplayString
_SmcDosWsPcTyp_Object=MibScalar
smcDosWsPcTyp=_SmcDosWsPcTyp_Object((1,3,6,1,4,1,202,2,1),_SmcDosWsPcTyp_Type())
smcDosWsPcTyp.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsPcTyp.setStatus(_A)
_SmcDosWsPcProc_Type=DisplayString
_SmcDosWsPcProc_Object=MibScalar
smcDosWsPcProc=_SmcDosWsPcProc_Object((1,3,6,1,4,1,202,2,2),_SmcDosWsPcProc_Type())
smcDosWsPcProc.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsPcProc.setStatus(_A)
_SmcDosWsPcBios_Type=DisplayString
_SmcDosWsPcBios_Object=MibScalar
smcDosWsPcBios=_SmcDosWsPcBios_Object((1,3,6,1,4,1,202,2,3),_SmcDosWsPcBios_Type())
smcDosWsPcBios.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsPcBios.setStatus(_A)
_SmcDosWsPcRam_Type=DisplayString
_SmcDosWsPcRam_Object=MibScalar
smcDosWsPcRam=_SmcDosWsPcRam_Object((1,3,6,1,4,1,202,2,4),_SmcDosWsPcRam_Type())
smcDosWsPcRam.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsPcRam.setStatus(_A)
_SmcDosWsPcDisk_Type=DisplayString
_SmcDosWsPcDisk_Object=MibScalar
smcDosWsPcDisk=_SmcDosWsPcDisk_Object((1,3,6,1,4,1,202,2,5),_SmcDosWsPcDisk_Type())
smcDosWsPcDisk.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsPcDisk.setStatus(_A)
_SmcDosWsPcVideo_Type=DisplayString
_SmcDosWsPcVideo_Object=MibScalar
smcDosWsPcVideo=_SmcDosWsPcVideo_Object((1,3,6,1,4,1,202,2,6),_SmcDosWsPcVideo_Type())
smcDosWsPcVideo.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsPcVideo.setStatus(_A)
_SmcDosWsPcIo_Type=DisplayString
_SmcDosWsPcIo_Object=MibScalar
smcDosWsPcIo=_SmcDosWsPcIo_Object((1,3,6,1,4,1,202,2,7),_SmcDosWsPcIo_Type())
smcDosWsPcIo.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsPcIo.setStatus(_A)
_SmcDosWsDosVer_Type=DisplayString
_SmcDosWsDosVer_Object=MibScalar
smcDosWsDosVer=_SmcDosWsDosVer_Object((1,3,6,1,4,1,202,2,8),_SmcDosWsDosVer_Type())
smcDosWsDosVer.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsDosVer.setStatus(_A)
_SmcDosWsDrvId_Type=DisplayString
_SmcDosWsDrvId_Object=MibScalar
smcDosWsDrvId=_SmcDosWsDrvId_Object((1,3,6,1,4,1,202,2,9),_SmcDosWsDrvId_Type())
smcDosWsDrvId.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsDrvId.setStatus(_A)
_SmcDosWsNicBasIo_Type=DisplayString
_SmcDosWsNicBasIo_Object=MibScalar
smcDosWsNicBasIo=_SmcDosWsNicBasIo_Object((1,3,6,1,4,1,202,2,10),_SmcDosWsNicBasIo_Type())
smcDosWsNicBasIo.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsNicBasIo.setStatus(_A)
_SmcDosWsNicIrq_Type=DisplayString
_SmcDosWsNicIrq_Object=MibScalar
smcDosWsNicIrq=_SmcDosWsNicIrq_Object((1,3,6,1,4,1,202,2,11),_SmcDosWsNicIrq_Type())
smcDosWsNicIrq.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsNicIrq.setStatus(_A)
_SmcDosWsNicRam_Type=DisplayString
_SmcDosWsNicRam_Object=MibScalar
smcDosWsNicRam=_SmcDosWsNicRam_Object((1,3,6,1,4,1,202,2,12),_SmcDosWsNicRam_Type())
smcDosWsNicRam.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsNicRam.setStatus(_A)
_SmcDosWsNodId_Type=MacAddress
_SmcDosWsNodId_Object=MibScalar
smcDosWsNodId=_SmcDosWsNodId_Object((1,3,6,1,4,1,202,2,13),_SmcDosWsNodId_Type())
smcDosWsNodId.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsNodId.setStatus(_A)
_SmcDosWsIpAdr_Type=IpAddress
_SmcDosWsIpAdr_Object=MibScalar
smcDosWsIpAdr=_SmcDosWsIpAdr_Object((1,3,6,1,4,1,202,2,14),_SmcDosWsIpAdr_Type())
smcDosWsIpAdr.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsIpAdr.setStatus(_A)
_SmcDosWsComment_Type=DisplayString
_SmcDosWsComment_Object=MibScalar
smcDosWsComment=_SmcDosWsComment_Object((1,3,6,1,4,1,202,2,15),_SmcDosWsComment_Type())
smcDosWsComment.setMaxAccess(_C)
if mibBuilder.loadTexts:smcDosWsComment.setStatus(_A)
_SmcDosWsPcDate_Type=DisplayString
_SmcDosWsPcDate_Object=MibScalar
smcDosWsPcDate=_SmcDosWsPcDate_Object((1,3,6,1,4,1,202,2,16),_SmcDosWsPcDate_Type())
smcDosWsPcDate.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsPcDate.setStatus(_A)
_SmcDosWsPcTime_Type=DisplayString
_SmcDosWsPcTime_Object=MibScalar
smcDosWsPcTime=_SmcDosWsPcTime_Object((1,3,6,1,4,1,202,2,17),_SmcDosWsPcTime_Type())
smcDosWsPcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsPcTime.setStatus(_A)
_SmcDosWsRst_Type=Integer32
_SmcDosWsRst_Object=MibScalar
smcDosWsRst=_SmcDosWsRst_Object((1,3,6,1,4,1,202,2,18),_SmcDosWsRst_Type())
smcDosWsRst.setMaxAccess(_C)
if mibBuilder.loadTexts:smcDosWsRst.setStatus(_A)
_SmcDosWsProtoMix_Type=DisplayString
_SmcDosWsProtoMix_Object=MibScalar
smcDosWsProtoMix=_SmcDosWsProtoMix_Object((1,3,6,1,4,1,202,2,19),_SmcDosWsProtoMix_Type())
smcDosWsProtoMix.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsProtoMix.setStatus(_A)
_SmcDosWsRcvPkts_Type=Counter32
_SmcDosWsRcvPkts_Object=MibScalar
smcDosWsRcvPkts=_SmcDosWsRcvPkts_Object((1,3,6,1,4,1,202,2,20),_SmcDosWsRcvPkts_Type())
smcDosWsRcvPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsRcvPkts.setStatus(_A)
_SmcDosWsXmtPkts_Type=Counter32
_SmcDosWsXmtPkts_Object=MibScalar
smcDosWsXmtPkts=_SmcDosWsXmtPkts_Object((1,3,6,1,4,1,202,2,21),_SmcDosWsXmtPkts_Type())
smcDosWsXmtPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsXmtPkts.setStatus(_A)
_SmcDosWsDrvSpcTable_Object=MibTable
smcDosWsDrvSpcTable=_SmcDosWsDrvSpcTable_Object((1,3,6,1,4,1,202,2,22))
if mibBuilder.loadTexts:smcDosWsDrvSpcTable.setStatus(_A)
_SmcDosWsDrvSpcEntry_Object=MibTableRow
smcDosWsDrvSpcEntry=_SmcDosWsDrvSpcEntry_Object((1,3,6,1,4,1,202,2,22,1))
smcDosWsDrvSpcEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:smcDosWsDrvSpcEntry.setStatus(_A)
_SmcDosWsDrvSpcId_Type=Integer32
_SmcDosWsDrvSpcId_Object=MibTableColumn
smcDosWsDrvSpcId=_SmcDosWsDrvSpcId_Object((1,3,6,1,4,1,202,2,22,1,1),_SmcDosWsDrvSpcId_Type())
smcDosWsDrvSpcId.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsDrvSpcId.setStatus(_A)
_SmcDosWsDrvSpcTxt_Type=DisplayString
_SmcDosWsDrvSpcTxt_Object=MibTableColumn
smcDosWsDrvSpcTxt=_SmcDosWsDrvSpcTxt_Object((1,3,6,1,4,1,202,2,22,1,2),_SmcDosWsDrvSpcTxt_Type())
smcDosWsDrvSpcTxt.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsDrvSpcTxt.setStatus(_A)
_SmcDosWsDrvSpcCnt_Type=Counter32
_SmcDosWsDrvSpcCnt_Object=MibTableColumn
smcDosWsDrvSpcCnt=_SmcDosWsDrvSpcCnt_Object((1,3,6,1,4,1,202,2,22,1,3),_SmcDosWsDrvSpcCnt_Type())
smcDosWsDrvSpcCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsDrvSpcCnt.setStatus(_A)
_SmcDosWsTrapDestTable_Object=MibTable
smcDosWsTrapDestTable=_SmcDosWsTrapDestTable_Object((1,3,6,1,4,1,202,2,23))
if mibBuilder.loadTexts:smcDosWsTrapDestTable.setStatus(_A)
_SmcDosWsTrapDestEntry_Object=MibTableRow
smcDosWsTrapDestEntry=_SmcDosWsTrapDestEntry_Object((1,3,6,1,4,1,202,2,23,1))
smcDosWsTrapDestEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:smcDosWsTrapDestEntry.setStatus(_A)
class _SmcDosWsTrapId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_SmcDosWsTrapId_Type.__name__=_E
_SmcDosWsTrapId_Object=MibTableColumn
smcDosWsTrapId=_SmcDosWsTrapId_Object((1,3,6,1,4,1,202,2,23,1,1),_SmcDosWsTrapId_Type())
smcDosWsTrapId.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsTrapId.setStatus(_A)
_SmcDosWsTrapDstAdr_Type=IpAddress
_SmcDosWsTrapDstAdr_Object=MibTableColumn
smcDosWsTrapDstAdr=_SmcDosWsTrapDstAdr_Object((1,3,6,1,4,1,202,2,23,1,2),_SmcDosWsTrapDstAdr_Type())
smcDosWsTrapDstAdr.setMaxAccess(_C)
if mibBuilder.loadTexts:smcDosWsTrapDstAdr.setStatus(_A)
_SmcDosWsTrapDstPro_Type=Integer32
_SmcDosWsTrapDstPro_Object=MibTableColumn
smcDosWsTrapDstPro=_SmcDosWsTrapDstPro_Object((1,3,6,1,4,1,202,2,23,1,3),_SmcDosWsTrapDstPro_Type())
smcDosWsTrapDstPro.setMaxAccess(_C)
if mibBuilder.loadTexts:smcDosWsTrapDstPro.setStatus(_A)
_SmcDosWsApiTrap_Type=DisplayString
_SmcDosWsApiTrap_Object=MibScalar
smcDosWsApiTrap=_SmcDosWsApiTrap_Object((1,3,6,1,4,1,202,2,24),_SmcDosWsApiTrap_Type())
smcDosWsApiTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:smcDosWsApiTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'MacAddress':MacAddress,'smc':smc,'smcDosWs':smcDosWs,'smcDosWsPcTyp':smcDosWsPcTyp,'smcDosWsPcProc':smcDosWsPcProc,'smcDosWsPcBios':smcDosWsPcBios,'smcDosWsPcRam':smcDosWsPcRam,'smcDosWsPcDisk':smcDosWsPcDisk,'smcDosWsPcVideo':smcDosWsPcVideo,'smcDosWsPcIo':smcDosWsPcIo,'smcDosWsDosVer':smcDosWsDosVer,'smcDosWsDrvId':smcDosWsDrvId,'smcDosWsNicBasIo':smcDosWsNicBasIo,'smcDosWsNicIrq':smcDosWsNicIrq,'smcDosWsNicRam':smcDosWsNicRam,'smcDosWsNodId':smcDosWsNodId,'smcDosWsIpAdr':smcDosWsIpAdr,'smcDosWsComment':smcDosWsComment,'smcDosWsPcDate':smcDosWsPcDate,'smcDosWsPcTime':smcDosWsPcTime,'smcDosWsRst':smcDosWsRst,'smcDosWsProtoMix':smcDosWsProtoMix,'smcDosWsRcvPkts':smcDosWsRcvPkts,'smcDosWsXmtPkts':smcDosWsXmtPkts,'smcDosWsDrvSpcTable':smcDosWsDrvSpcTable,'smcDosWsDrvSpcEntry':smcDosWsDrvSpcEntry,_F:smcDosWsDrvSpcId,'smcDosWsDrvSpcTxt':smcDosWsDrvSpcTxt,'smcDosWsDrvSpcCnt':smcDosWsDrvSpcCnt,'smcDosWsTrapDestTable':smcDosWsTrapDestTable,'smcDosWsTrapDestEntry':smcDosWsTrapDestEntry,_G:smcDosWsTrapId,'smcDosWsTrapDstAdr':smcDosWsTrapDstAdr,'smcDosWsTrapDstPro':smcDosWsTrapDstPro,'smcDosWsApiTrap':smcDosWsApiTrap})